import { Component, inject, signal, computed } from '@angular/core'
import { DecimalPipe } from '@angular/common'
import { Router } from '@angular/router'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'

import { injectQuery, injectMutation, injectQueryClient } from '@tanstack/angular-query-experimental'

import { MatCardModule } from '@angular/material/card'
import { MatTableModule } from '@angular/material/table'
import { MatExpansionModule } from '@angular/material/expansion'
import { MatButtonModule } from '@angular/material/button'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatProgressBarModule } from '@angular/material/progress-bar'
import { MatIconModule } from '@angular/material/icon'
import { MatDialogModule, MatDialog } from '@angular/material/dialog'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatChipsModule } from '@angular/material/chips'
import { MatTabsModule } from '@angular/material/tabs'

import { AssessmentsApiService, AssessmentListItem } from '../../api/assessments-api.service'
import { ProductService, PRODUCT_COLORS, PRODUCT_SUBTITLES } from '../../core/services/product.service'
import { ProjectService } from '../../core/services/project.service'
import { ThemeService } from '../../core/services/theme.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'
import { StatusChipComponent } from '../../shared/components/status-chip.component'

// ── Helpers ─────────────────────────────────────────────────────────────────

type AssessmentStatus = 'not_started' | 'in_progress' | 'complete'

function getStatus(a: AssessmentListItem): AssessmentStatus {
  if (a.items_total === 0) return 'not_started'
  if (a.overall_score != null && a.overall_score >= 80) return 'complete'
  return 'in_progress'
}

function isPlatform(a: AssessmentListItem): boolean {
  return a.file_path === 'platform:webui' || a.document_id.startsWith('ISMS-ASS-')
}

function scoreColor(score: number | null): string {
  if (score == null) return 'var(--mat-sys-on-surface-variant)'
  if (score >= 80) return '#70AD47'
  if (score >= 60) return '#FFC000'
  return '#C00000'
}

function productChipStyle(productType: string): { background: string; color: string } {
  switch (productType) {
    case 'framework':   return { background: 'rgba(50,125,244,0.15)',  color: '#327df4' }
    case 'privacy':     return { background: `${PRODUCT_COLORS.privacy}22`, color: PRODUCT_COLORS.privacy }
    case 'cloud':       return { background: `${PRODUCT_COLORS.cloud}22`,   color: PRODUCT_COLORS.cloud }
    case 'ai':          return { background: `${PRODUCT_COLORS.ai}22`,      color: PRODUCT_COLORS.ai }
    default:            return { background: 'rgba(112,173,71,0.15)',  color: '#70AD47' }
  }
}

const STATUS_CONFIG: Record<AssessmentStatus, { label: string; bg: string; color: string }> = {
  not_started: { label: 'Not Started', bg: 'rgba(255,255,255,0.06)', color: '#888' },
  in_progress:  { label: 'In Progress', bg: 'rgba(255,192,0,0.12)',  color: '#FFC000' },
  complete:     { label: 'Complete',    bg: 'rgba(198,239,206,0.15)', color: '#C6EFCE' },
}

// ── New Assessment Dialog ────────────────────────────────────────────────────

@Component({
  selector: 'app-new-assessment-dialog',
  standalone: true,
  imports: [
    FormsModule,
    MatButtonModule, MatDialogModule, MatFormFieldModule,
    MatInputModule, MatSelectModule, MatIconModule,
  ],
  template: `
    <h2 mat-dialog-title>New Assessment</h2>
    <mat-dialog-content class="dialog-content">
      <mat-form-field appearance="outline" class="field-full">
        <mat-label>Control Group Code</mat-label>
        <input matInput [(ngModel)]="groupCode" placeholder="e.g. a.8.1" />
      </mat-form-field>
      <mat-form-field appearance="outline" class="field-full">
        <mat-label>Workbook Name</mat-label>
        <input matInput [(ngModel)]="workbookName" placeholder="e.g. Asset Management Assessment" />
      </mat-form-field>
      <mat-form-field appearance="outline" class="field-full">
        <mat-label>Product Type</mat-label>
        <mat-select [(ngModel)]="productType">
          <mat-option value="framework">Framework</mat-option>
          <mat-option value="operational">Operational</mat-option>
          <mat-option value="privacy">Privacy</mat-option>
          <mat-option value="cloud">Cloud</mat-option>
          <mat-option value="ai">AI</mat-option>
        </mat-select>
      </mat-form-field>
    </mat-dialog-content>
    <mat-dialog-actions align="end">
      <button mat-button mat-dialog-close>Cancel</button>
      <button mat-raised-button color="primary"
        [disabled]="!groupCode.trim()"
        [mat-dialog-close]="{ groupCode, workbookName, productType }">
        Create
      </button>
    </mat-dialog-actions>
  `,
  styles: [`
    .dialog-content { display: flex; flex-direction: column; gap: 16px; padding-top: 8px; min-width: 360px; }
    .field-full { width: 100%; }
  `],
})
export class NewAssessmentDialogComponent {
  groupCode    = ''
  workbookName = ''
  productType  = 'framework'
}

// ── Main Component ───────────────────────────────────────────────────────────

@Component({
  selector: 'app-assessments',
  standalone: true,
  imports: [
    FormsModule,
    MatCardModule, MatTableModule, MatExpansionModule,
    MatButtonModule, MatFormFieldModule, MatInputModule,
    MatSelectModule, MatProgressBarModule, MatIconModule,
    MatDialogModule, MatTooltipModule, MatChipsModule,
    MatTabsModule,
    DecimalPipe,
    PageHeaderComponent, StatusChipComponent,
  ],
  template: `
    <app-page-header
      title="Assessments"
      [subtitle]="headerSubtitle()">
      <div actions>
        <button mat-raised-button color="primary"
          [disabled]="!projectService.activeProject()"
          [matTooltip]="!projectService.activeProject() ? 'Select a project first' : ''"
          (click)="openNewDialog()">
          <mat-icon>add</mat-icon>
          New Assessment
        </button>
      </div>
    </app-page-header>

    @if (projectService.activeProject()) {
      <div class="isms-alert isms-alert--info" style="margin-top: 16px">
        Showing assessments for project: <strong>{{ projectService.activeProject()!.name }}</strong>
        @if (projectService.activeProject()!.organisation_name) {
          — {{ projectService.activeProject()!.organisation_name }}
        }
      </div>
    }

    <!-- Stat cards -->
    <div class="stats-row">
      <div class="stat-card">
        <div class="stat-value">{{ tierPlatform().length }}</div>
        <div class="stat-label">Total Assessments</div>
      </div>
      <div class="stat-card">
        <div class="stat-value" [style.color]="avgScoreColor()">
          {{ avgScore() != null ? (avgScore()! | number:'1.0-0') + '%' : '—' }}
        </div>
        <div class="stat-label">Avg Score</div>
      </div>
      <div class="stat-card">
        <div class="stat-value color-compliant">{{ totalCompliant() }}</div>
        <div class="stat-label">Compliant Items</div>
      </div>
      <div class="stat-card">
        <div class="stat-value color-danger">{{ totalNonCompliant() }}</div>
        <div class="stat-label">Non-Compliant Items</div>
      </div>
    </div>

    <!-- Tabs -->
    <mat-tab-group [(selectedIndex)]="activeTab" animationDuration="0">

      <!-- Platform Assessments tab -->
      <mat-tab label="Platform Assessments">
        <div class="tab-content">
          <!-- Status filter chips -->
          <div class="section-header">
            <mat-icon class="icon-md color-primary">assignment</mat-icon>
            <span class="section-title">Platform Assessments</span>
            <span class="count-chip">{{ tierPlatform().length }}</span>

            @for (sf of statusFilters; track sf.key) {
              <div class="status-filter-chip"
                [class.active]="statusFilter() === sf.key"
                [style.--chip-color]="filterStyle(sf.key).color"
                [style.--chip-bg]="filterStyle(sf.key).bg"
                (click)="statusFilter.set(sf.key)">
                {{ sf.label }} {{ sf.count() }}
              </div>
            }
          </div>

          @if (assessmentsQuery.isLoading()) {
            <div class="skeleton-rect"></div>
          }

          @if (!assessmentsQuery.isLoading() && tierPlatform().length === 0) {
            <div class="empty-state" [class.clickable]="!!projectService.activeProject()"
              (click)="projectService.activeProject() && openNewDialog()">
              <mat-icon class="icon-muted">add_circle_outline</mat-icon>
              <p class="empty-text">
                No platform assessments yet — fill in your data directly, no Excel required.
              </p>
              <span class="empty-hint" [class.hint-active]="!!projectService.activeProject()">
                {{ projectService.activeProject() ? 'Click to start a new assessment' : 'Select a project first' }}
              </span>
            </div>
          }

          @if (!assessmentsQuery.isLoading() && tierPlatform().length > 0 && filteredPlatform().length === 0) {
            <div class="filter-empty-msg">
              No assessments match the selected status filter.
            </div>
          }

          @for (a of filteredPlatform(); track a.id) {
            <div class="assessment-card">
              <div class="assessment-card__body">
                <!-- Left: info -->
                <div class="card-info">
                  <div class="card-chips">
                    <span class="doc-id">{{ a.document_id }}</span>
                    <app-status-chip [status]="statusStr(a)" />
                    <span class="product-chip"
                      [style.background]="productStyle(a.product_type).background"
                      [style.color]="productStyle(a.product_type).color">
                      {{ a.product_type }}
                    </span>
                  </div>

                  <div class="workbook-name">{{ a.workbook_name }}</div>
                  <div class="card-group-meta">
                    {{ a.group_code.toUpperCase() }} — {{ a.group_name }}
                  </div>

                  <!-- Metadata row -->
                  @if (a.summary) {
                    <div class="meta-row">
                      @if (a.summary['assessor']) {
                        <span class="meta-item">
                          <mat-icon class="icon-xs">person</mat-icon>
                          {{ a.summary['assessor'] }}
                        </span>
                      }
                      @if (a.summary['purpose']) {
                        <span class="meta-item">
                          <mat-icon class="icon-xs">flag</mat-icon>
                          {{ a.summary['purpose'] }}
                        </span>
                      }
                      @if (a.summary['target_date']) {
                        <span class="meta-item">
                          <mat-icon class="icon-xs">calendar_today</mat-icon>
                          Due {{ a.summary['target_date'] }}
                        </span>
                      }
                    </div>
                  }

                  <!-- Compliance bar -->
                  @if (a.items_total > 0) {
                    <div>
                      <div class="compliance-bar">
                        @if (a.items_compliant > 0) {
                          <div class="bar-seg seg-compliant"
                            [style.flex]="a.items_compliant"></div>
                        }
                        @if (a.items_partial > 0) {
                          <div class="bar-seg seg-partial"
                            [style.flex]="a.items_partial"></div>
                        }
                        @if (a.items_non_compliant > 0) {
                          <div class="bar-seg seg-non-compliant"
                            [style.flex]="a.items_non_compliant"></div>
                        }
                        @if (a.items_na > 0) {
                          <div class="bar-seg seg-na"
                            [style.flex]="a.items_na"></div>
                        }
                      </div>
                      <div class="bar-labels">
                        <span class="bar-total">{{ a.items_total }} items</span>
                        @if (a.overall_score != null) {
                          <span class="bar-score" [style.color]="scoreColor(a.overall_score)">
                            {{ a.overall_score }}%
                          </span>
                        }
                      </div>
                    </div>
                  } @else {
                    <span class="bar-total">No items yet</span>
                  }
                </div>

                <!-- Right: actions -->
                <div class="card-actions">
                  <button mat-icon-button matTooltip="Open assessment" class="action-btn action-btn--primary"
                    (click)="router.navigate(['/controls', a.control_group_id])">
                    <mat-icon class="icon-action">open_in_new</mat-icon>
                  </button>
                  <button mat-icon-button matTooltip="Delete" class="action-btn action-btn--danger"
                    [disabled]="deleteMutation.isPending()"
                    (click)="confirmDelete(a)">
                    <mat-icon class="icon-action">delete</mat-icon>
                  </button>
                </div>
              </div>
            </div>
          }
        </div>
      </mat-tab>

      <!-- Workbook Library tab -->
      <mat-tab label="Workbook Library">
        <div class="tab-content">
          <div class="lib-toolbar">
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="lib-search">
              <mat-label>Search workbooks</mat-label>
              <mat-icon matPrefix>search</mat-icon>
              <input matInput [(ngModel)]="libSearch" placeholder="ID, name, group code…" />
            </mat-form-field>
          </div>

          <mat-card>
            <table mat-table [dataSource]="filteredLibrary()" class="full-width">
              <ng-container matColumnDef="group">
                <th mat-header-cell *matHeaderCellDef>Control Group</th>
                <td mat-cell *matCellDef="let a">
                  <span class="doc-id" [style.color]="groupCodeColor(a.group_code, a.product_type)">{{ a.group_code.toUpperCase() }}</span>
                  <br>
                  <span class="cell-sub">{{ a.group_name }}</span>
                </td>
              </ng-container>
              <ng-container matColumnDef="workbook">
                <th mat-header-cell *matHeaderCellDef>Workbook</th>
                <td mat-cell *matCellDef="let a">
                  <span class="cell-mono">{{ a.document_id }}</span>
                  <br>
                  <span class="cell-name">{{ a.workbook_name }}</span>
                </td>
              </ng-container>
              <ng-container matColumnDef="product">
                <th mat-header-cell *matHeaderCellDef class="col-product">Product</th>
                <td mat-cell *matCellDef="let a">
                  <span class="product-chip"
                    [style.background]="productStyle(a.product_type).background"
                    [style.color]="productStyle(a.product_type).color">
                    {{ a.product_type }}
                  </span>
                </td>
              </ng-container>
              <ng-container matColumnDef="sheets">
                <th mat-header-cell *matHeaderCellDef class="col-sheets">Sheets</th>
                <td mat-cell *matCellDef="let a" class="cell-sheets">{{ a.sheets_count }}</td>
              </ng-container>
              <ng-container matColumnDef="compliance">
                <th mat-header-cell *matHeaderCellDef class="col-compliance">Compliance</th>
                <td mat-cell *matCellDef="let a">
                  @if ((a.items_total ?? 0) > 0) {
                    <div class="compliance-bar">
                      @if ((a.items_compliant ?? 0) > 0) {
                        <div class="bar-seg seg-compliant" [style.flex]="a.items_compliant"></div>
                      }
                      @if ((a.items_partial ?? 0) > 0) {
                        <div class="bar-seg seg-partial" [style.flex]="a.items_partial"></div>
                      }
                      @if ((a.items_non_compliant ?? 0) > 0) {
                        <div class="bar-seg seg-non-compliant" [style.flex]="a.items_non_compliant"></div>
                      }
                      @if ((a.items_na ?? 0) > 0) {
                        <div class="bar-seg seg-na" [style.flex]="a.items_na"></div>
                      }
                    </div>
                  } @else {
                    <span class="cell-empty">No items</span>
                  }
                </td>
              </ng-container>

              <tr mat-header-row *matHeaderRowDef="libColumns"></tr>
              <tr mat-row *matRowDef="let row; columns: libColumns;"
                class="row-clickable"
                (click)="router.navigate(['/controls', row.control_group_id])"></tr>
            </table>

            @if (filteredLibrary().length === 0) {
              <div class="table-empty">
                No workbooks match the current filters.
              </div>
            }
          </mat-card>
        </div>
      </mat-tab>

    </mat-tab-group>

    <!-- Delete confirm dialog -->
    @if (deleteTarget()) {
      <div class="dialog-backdrop" (click)="deleteTarget.set(null)">
        <mat-card class="confirm-dialog" (click)="$event.stopPropagation()">
          <mat-card-content>
            <h3 class="confirm-title">Delete Assessment?</h3>
            <p class="confirm-body">
              <strong>{{ deleteTarget()!.name }}</strong> and all its data will be permanently removed.
              This cannot be undone.
            </p>
            @if (deleteMutation.isError()) {
              <div class="alert-error">Delete failed. Try again.</div>
            }
            <div class="confirm-footer">
              <button mat-button (click)="deleteTarget.set(null)" [disabled]="deleteMutation.isPending()">Cancel</button>
              <button mat-raised-button color="warn"
                [disabled]="deleteMutation.isPending()"
                (click)="executeDelete()">
                {{ deleteMutation.isPending() ? 'Deleting…' : 'Delete' }}
              </button>
            </div>
          </mat-card-content>
        </mat-card>
      </div>
    }
  `,
  styles: [`
    :host { display: block; }

    /* ── Stat cards ─────────────────────────────── */
    .stats-row {
      display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 20px;
    }
    .stat-card {
      flex: 1; min-width: 120px; padding: 12px 16px;
      background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
      border-radius: 8px;
    }
    .stat-value { font-size: 1.5rem; font-weight: 700; }
    .stat-label { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); margin-top: 2px; }
    .color-compliant { color: #70AD47; }
    .color-danger    { color: #C00000; }

    /* ── Tab content wrapper ────────────────────── */
    .tab-content { padding-top: 16px; }

    /* ── Section header (platform tab title row) ─ */
    .section-header {
      display: flex; align-items: center; gap: 8px;
      margin-bottom: 16px; flex-wrap: wrap;
    }
    .color-primary { color: var(--mat-sys-primary); }
    .section-title { font-size: 0.85rem; font-weight: 700; color: var(--mat-sys-primary); }
    .count-chip    { height: 18px; line-height: 18px; font-size: 0.65rem; padding: 0 6px; border-radius: 9px; display: inline-flex; align-items: center; background: rgba(255,255,255,0.08); color: var(--mat-sys-on-surface-variant); }
    .icon-md       { font-size: 18px; }
    .icon-xs       { font-size: 12px; height: 12px; width: 12px; }
    .icon-action   { font-size: 16px; }
    .icon-muted    { color: var(--mat-sys-on-surface-variant); }

    /* ── Assessment card ────────────────────────── */
    .assessment-card {
      margin-bottom: 12px;
      background: var(--mat-sys-surface-container);
      border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 8px;
      transition: border-color 0.15s;
    }
    .assessment-card:hover { border-color: var(--mat-sys-primary); }
    .assessment-card__body {
      display: flex; align-items: flex-start; gap: 12px; padding: 12px 14px;
    }
    .card-info    { flex: 1; min-width: 0; }
    .card-chips   { display: flex; align-items: center; gap: 6px; flex-wrap: wrap; margin-bottom: 4px; }
    .card-group-meta { font-size: 0.78rem; color: var(--mat-sys-on-surface-variant); margin-bottom: 6px; }
    .card-actions { display: flex; flex-direction: column; gap: 4px; flex-shrink: 0; }

    /* ── Doc / status / product chips ──────────── */
    .doc-id {
      font-family: monospace; font-size: 0.7rem;
      color: var(--mat-sys-primary); font-weight: 600;
    }
    .status-chip {
      display: inline-block; padding: 1px 7px; border-radius: 9px;
      font-size: 0.65rem; font-weight: 600; height: 18px; line-height: 16px;
    }
    .product-chip {
      display: inline-block; padding: 1px 7px; border-radius: 9px;
      font-size: 0.6rem; font-weight: 500; height: 16px; line-height: 14px;
    }
    .workbook-name {
      font-weight: 700; font-size: 0.9rem; cursor: pointer;
      transition: color 0.1s;
    }
    .workbook-name:hover { color: var(--mat-sys-primary); }

    /* ── Meta row (assessor / purpose / date) ───── */
    .meta-row  { display: flex; gap: 14px; flex-wrap: wrap; margin-bottom: 6px; }
    .meta-item {
      display: inline-flex; align-items: center; gap: 3px;
      font-size: 0.75rem; color: var(--mat-sys-on-surface-variant);
    }

    /* ── Compliance bar ─────────────────────────── */
    .compliance-bar {
      display: flex; height: 5px; border-radius: 3px;
      overflow: hidden; background: rgba(255,255,255,0.06);
    }
    .bar-seg { flex-shrink: 0; }
    .seg-compliant     { background: #C6EFCE; }
    .seg-partial       { background: #FFEB9C; }
    .seg-non-compliant { background: #FFC7CE; }
    .seg-na            { background: #444; }
    .bar-labels { display: flex; gap: 10px; margin-top: 3px; }
    .bar-total  { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
    .bar-score  { font-size: 0.72rem; font-weight: 600; }

    /* ── Action buttons ─────────────────────────── */
    .action-btn {
      width: 30px; height: 30px; display: flex; align-items: center; justify-content: center;
      border-radius: 6px; border: none; cursor: pointer;
    }
    .action-btn--primary {
      color: var(--mat-sys-primary);
      background: color-mix(in srgb, var(--mat-sys-primary) 10%, transparent);
    }
    .action-btn--primary:hover { background: color-mix(in srgb, var(--mat-sys-primary) 20%, transparent); }
    .action-btn--danger {
      color: var(--mat-sys-error); opacity: 0.5;
      background: transparent;
    }
    .action-btn--danger:hover { opacity: 1; }

    /* ── Empty / filter-empty states ────────────── */
    .empty-state {
      padding: 24px; border-radius: 8px; text-align: center;
      border: 1px dashed var(--mat-sys-outline-variant); background: transparent;
    }
    .empty-state.clickable { cursor: pointer; }
    .empty-state.clickable:hover {
      background: var(--mat-sys-surface-container); border-color: var(--mat-sys-primary);
    }
    .empty-text  { color: var(--mat-sys-on-surface-variant); margin: 4px 0; }
    .empty-hint  { font-size: 0.8rem; color: var(--mat-sys-on-surface-variant); }
    .empty-hint.hint-active { color: var(--mat-sys-primary); }
    .filter-empty-msg {
      padding: 12px; background: var(--mat-sys-surface-container);
      border-radius: 6px; font-size: 0.85rem; color: var(--mat-sys-on-surface-variant);
    }

    /* ── Skeleton ────────────────────────────────── */
    .skeleton-rect {
      height: 80px; border-radius: 8px;
      background: rgba(255,255,255,0.05);
      animation: pulse 1.5s ease-in-out infinite;
    }
    @keyframes pulse {
      0%, 100% { opacity: 1; }
      50%       { opacity: 0.4; }
    }

    /* ── Status filter chips ─────────────────────── */
    .status-filter-chip {
      display: inline-flex; align-items: center; padding: 2px 10px;
      border-radius: 12px; font-size: 0.65rem; cursor: pointer;
      border: 1px solid rgba(255,255,255,0.08);
      color: var(--mat-sys-on-surface-variant);
      transition: all 0.1s;
    }
    .status-filter-chip:hover {
      background: var(--chip-bg); color: var(--chip-color);
    }
    .status-filter-chip.active {
      background: var(--chip-bg); color: var(--chip-color);
      border-color: rgba(255,255,255,0.15); font-weight: 700;
    }

    /* ── Workbook Library tab ────────────────────── */
    .lib-toolbar { display: flex; gap: 16px; margin-bottom: 12px; align-items: center; }
    .lib-search  { flex: 1; max-width: 320px; }
    .full-width  { width: 100%; }

    /* Column widths */
    .col-product    { width: 90px; }
    .col-sheets     { width: 60px; text-align: center; }
    .col-compliance { width: 180px; }

    /* Cell styles */
    .cell-sub   { font-size: 0.75rem; color: var(--mat-sys-on-surface-variant); }
    .cell-mono  { font-family: monospace; font-size: 0.68rem; color: var(--mat-sys-on-surface-variant); }
    .cell-name  { font-weight: 600; font-size: 0.85rem; }
    .cell-sheets { text-align: center; font-size: 0.8rem; }
    .cell-empty  { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
    .row-clickable { cursor: pointer; }
    .table-empty {
      padding: 24px; text-align: center;
      color: var(--mat-sys-on-surface-variant); font-size: 0.85rem;
    }

    /* ── Misc ────────────────────────────────────── */
    .compact-field { font-size: 0.85rem; }
    ::ng-deep .compact-field .mat-mdc-form-field-subscript-wrapper { display: none; }

    /* ── Delete confirm dialog ───────────────────── */
    .dialog-backdrop {
      position: fixed; inset: 0; z-index: 1000;
      background: rgba(0,0,0,0.5); display: flex;
      align-items: center; justify-content: center;
    }
    .confirm-dialog { max-width: 400px; width: 100%; }
    .confirm-title  { margin: 0 0 8px; }
    .confirm-body   { font-size: 0.9rem; color: var(--mat-sys-on-surface-variant); }
    .confirm-footer { display: flex; justify-content: flex-end; gap: 8px; margin-top: 16px; }

    .alert-error {
      padding: 8px 12px; border-radius: 6px; font-size: 0.8rem;
      background: rgba(192,0,0,0.12); color: #FFC7CE;
      border: 1px solid rgba(192,0,0,0.25); margin-top: 8px;
    }
  `],
})
export class AssessmentsComponent {
  readonly router         = inject(Router)
  readonly assessmentsApi = inject(AssessmentsApiService)
  readonly productService = inject(ProductService)
  readonly projectService = inject(ProjectService)
  private readonly theme  = inject(ThemeService)
  readonly dialog         = inject(MatDialog)
  readonly queryClient    = injectQueryClient()

  activeTab       = 0
  statusFilter    = signal<'' | AssessmentStatus>('')
  deleteTarget    = signal<{ id: string; name: string } | null>(null)
  libSearch       = ''
  libColumns      = ['group', 'workbook', 'product', 'sheets', 'compliance']

  // Query: all assessments for current product + project
  assessmentsQuery = injectQuery(() => ({
    queryKey: ['assessments', this.productService.product(), this.projectService.activeProjectId()],
    queryFn:  () => firstValueFrom(this.assessmentsApi.list({
      product_family: this.productService.product().toUpperCase(),
      project_id: this.projectService.activeProjectId() ?? undefined,
    })),
  }))

  // Library: all assessments regardless of project (for workbook library tab)
  libraryQuery = injectQuery(() => ({
    queryKey: ['assessments-library', this.productService.product()],
    queryFn:  () => firstValueFrom(this.assessmentsApi.list({
      product_family: this.productService.product().toUpperCase(),
    })),
  }))

  deleteMutation = injectMutation(() => ({
    mutationFn: (id: string) => firstValueFrom(this.assessmentsApi.delete(id)),
    onSuccess:  () => {
      this.deleteTarget.set(null)
      this.queryClient.invalidateQueries({ queryKey: ['assessments'] })
    },
  }))

  // Derived: platform assessments only (created via webui)
  tierPlatform = computed(() => {
    const all  = this.assessmentsQuery.data() ?? []
    const prod = this.productService.product()
    const tier = this.productService.ismsTier()
    return all
      .filter(isPlatform)
      .filter(a => prod !== 'isms' || tier === 'all' || a.product_type === tier)
  })

  filteredPlatform = computed(() => {
    const sf = this.statusFilter()
    return this.tierPlatform().filter(a => !sf || getStatus(a) === sf)
  })

  filteredLibrary = computed(() => {
    const all    = this.libraryQuery.data() ?? []
    const prod   = this.productService.product()
    const tier   = this.productService.ismsTier()
    const search = this.libSearch.toLowerCase()
    return all
      .filter(a => !isPlatform(a))
      .filter(a => prod === 'isms' || a.product_type === prod)
      .filter(a => prod !== 'isms' || tier === 'all' || a.product_type === tier)
      .filter(a => !search ||
        a.document_id.toLowerCase().includes(search) ||
        a.workbook_name.toLowerCase().includes(search) ||
        a.group_code.toLowerCase().includes(search)
      )
  })

  // Aggregate stats
  avgScore = computed(() => {
    const items = this.tierPlatform().filter(a => a.overall_score != null)
    if (!items.length) return null
    return items.reduce((sum, a) => sum + (a.overall_score ?? 0), 0) / items.length
  })
  avgScoreColor   = computed(() => scoreColor(this.avgScore()))
  totalCompliant  = computed(() => this.tierPlatform().reduce((s, a) => s + (a.items_compliant ?? 0), 0))
  totalNonCompliant = computed(() => this.tierPlatform().reduce((s, a) => s + (a.items_non_compliant ?? 0), 0))

  headerSubtitle = computed(() => {
    const proj = this.projectService.activeProject()
    const prod = this.productService.product()
    const sub  = prod !== 'isms' ? PRODUCT_SUBTITLES[prod] + ' · ' : ''
    return proj
      ? `${proj.name} · ${sub}Platform assessments and workbook library`
      : `${sub}Platform assessments and workbook library`
  })

  // Status filter chips definition
  statusFilters = [
    { key: '' as const,            label: 'All',         bg: 'rgba(255,255,255,0.07)', color: '#aaa', count: computed(() => this.tierPlatform().length) },
    { key: 'not_started' as const, label: 'Not Started', bg: 'rgba(255,255,255,0.06)', color: '#888', count: computed(() => this.tierPlatform().filter(a => getStatus(a) === 'not_started').length) },
    { key: 'in_progress' as const, label: 'In Progress', bg: 'rgba(255,192,0,0.12)',   color: '#FFC000', count: computed(() => this.tierPlatform().filter(a => getStatus(a) === 'in_progress').length) },
    { key: 'complete' as const,    label: 'Complete',    bg: 'rgba(198,239,206,0.15)', color: '#C6EFCE', count: computed(() => this.tierPlatform().filter(a => getStatus(a) === 'complete').length) },
  ]

  // Template helpers
  scoreColor     = scoreColor
  productStyle   = productChipStyle

  groupCodeColor(groupCode: string, productType: string): string {
    const c = (groupCode ?? '').toUpperCase()
    if (c === '00') return '#FFC000'
    if (productType === 'framework') {
      if (c.startsWith('A.5')) return '#9E9E9E'
      if (c.startsWith('A.6')) return '#70AD47'
      if (c.startsWith('A.7')) return '#FFC000'
      if (c.startsWith('A.8')) return '#C00000'
    }
    if (productType === 'privacy') {
      if (c.startsWith('A.1')) return '#ba68c8'
      if (c.startsWith('A.2')) return '#5c6bc0'
      if (c.startsWith('A.3')) return '#4db6ac'
    }
    return productChipStyle(productType).color
  }
  statusConfig   = (a: AssessmentListItem) => STATUS_CONFIG[getStatus(a)]
  statusStr      = (a: AssessmentListItem): string => getStatus(a)

  filterStyle = (key: string): { bg: string; color: string } => {
    const dark = this.theme.isDark()
    if (key === 'in_progress') return dark
      ? { bg: 'rgba(255,192,0,0.12)',   color: '#FFC000' }
      : { bg: 'rgba(230,145,0,0.15)',   color: '#7a4800' }
    if (key === 'complete') return dark
      ? { bg: 'rgba(198,239,206,0.15)', color: '#C6EFCE' }
      : { bg: 'rgba(29,158,117,0.12)',  color: '#0F6E56' }
    if (key === 'not_started') return dark
      ? { bg: 'rgba(255,255,255,0.06)', color: '#888' }
      : { bg: 'rgba(0,0,0,0.06)',       color: '#555' }
    return dark
      ? { bg: 'rgba(255,255,255,0.07)', color: '#aaa' }
      : { bg: 'rgba(0,0,0,0.07)',       color: '#444' }
  }

  openNewDialog(): void {
    const ref = this.dialog.open(NewAssessmentDialogComponent, { width: '420px' })
    ref.afterClosed().subscribe(result => {
      if (!result) return
      const proj = this.projectService.activeProject()
      firstValueFrom(this.assessmentsApi.create(
        result.groupCode,
        result.productType,
        result.workbookName,
        { project_id: proj?.id }
      )).then(() => {
        this.queryClient.invalidateQueries({ queryKey: ['assessments'] })
      })
    })
  }

  confirmDelete(a: AssessmentListItem): void {
    this.deleteTarget.set({ id: a.id, name: a.workbook_name })
  }

  executeDelete(): void {
    const target = this.deleteTarget()
    if (!target) return
    this.deleteMutation.mutate(target.id)
  }
}
