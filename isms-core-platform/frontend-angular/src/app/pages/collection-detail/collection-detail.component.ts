import { Component, inject, signal, computed } from '@angular/core'
import { ActivatedRoute, Router } from '@angular/router'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'
import { HttpClient } from '@angular/common/http'

import { injectQuery, injectMutation, injectQueryClient } from '@tanstack/angular-query-experimental'

import { MatCardModule } from '@angular/material/card'
import { MatButtonModule } from '@angular/material/button'
import { MatIconModule } from '@angular/material/icon'
import { MatChipsModule } from '@angular/material/chips'
import { MatProgressBarModule } from '@angular/material/progress-bar'
import { MatTableModule } from '@angular/material/table'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatDialogModule, MatDialog } from '@angular/material/dialog'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatCheckboxModule } from '@angular/material/checkbox'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatDividerModule } from '@angular/material/divider'

import {
  CollectionsApiService,
  CollectionRead,
  CollectionMember,
  CollectionListItem,
} from '../../api/collections-api.service'
import { ThemeService } from '../../core/services/theme.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

// ── Types ─────────────────────────────────────────────────────────────────────

interface AssessmentListItem {
  id: string
  document_id: string
  workbook_name: string
  group_code: string
  group_name: string
  product_type: string
  items_total: number
  items_compliant: number
  items_non_compliant: number
  compliance_pct: number
  overall_score: number | null
}

// ── Helpers ───────────────────────────────────────────────────────────────────

function scoreColor(pct: number): string {
  if (pct >= 80) return '#70AD47'
  if (pct >= 50) return '#FFC000'
  return '#FF5252'
}

function statusConfig(status: string): { label: string; bg: string; color: string } {
  switch (status) {
    case 'complete':    return { label: 'Complete',    bg: 'rgba(198,239,206,0.15)', color: '#C6EFCE' }
    case 'in_progress': return { label: 'In Progress', bg: 'rgba(255,192,0,0.12)',   color: '#856404' }
    default:            return { label: 'Not Started', bg: 'rgba(255,255,255,0.06)', color: '#888' }
  }
}

// ── Component ─────────────────────────────────────────────────────────────────

@Component({
  selector: 'app-collection-detail',
  standalone: true,
  imports: [
    FormsModule,
    MatCardModule, MatButtonModule, MatIconModule, MatChipsModule,
    MatProgressBarModule, MatTableModule, MatTooltipModule,
    MatDialogModule, MatFormFieldModule, MatInputModule,
    MatCheckboxModule, MatProgressSpinnerModule, MatDividerModule,
    PageHeaderComponent,
  ],
  styles: [`
    :host { display: block; padding-bottom: 40px; }

    .stats-card {
      padding: 16px;
      background: rgba(68,114,196,0.04);
      border: 1px solid rgba(68,114,196,0.12);
      border-radius: 8px;
      margin-bottom: 20px;
    }
    .stats-row { display: flex; gap: 32px; flex-wrap: wrap; align-items: center; }

    .bar-wrapper { flex: 1; min-width: 180px; }
    .bar-header { display: flex; justify-content: space-between; margin-bottom: 4px; font-size: 0.78rem; }

    .count-col { text-align: center; }
    .count-val { font-size: 1.1rem; font-weight: 700; line-height: 1; margin-bottom: 2px; }
    .count-label { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }

    .section-header {
      display: flex; align-items: center; gap: 8px; margin-bottom: 12px;
    }

    .empty-box {
      padding: 24px; border-radius: 8px; text-align: center; cursor: pointer;
      border: 1px dashed rgba(68,114,196,0.3); background: rgba(68,114,196,0.03);
      transition: background 0.15s, border-color 0.15s;
    }
    .empty-box:hover { background: rgba(68,114,196,0.07); border-color: rgba(68,114,196,0.5); }

    .nc-expand-btn {
      font-size: 0.7rem; color: #FF5252; cursor: pointer; background: none; border: none;
      padding: 2px 6px; display: inline-flex; align-items: center; gap: 4px;
    }
    .nc-box {
      margin-left: 8px; margin-top: 4px; padding: 8px;
      background: rgba(255,82,82,0.04); border-radius: 4px;
      border: 1px solid rgba(255,82,82,0.1);
      font-size: 0.72rem; color: var(--mat-sys-on-surface-variant);
    }

    /* Manage dialog overlay */
    .overlay-backdrop {
      position: fixed; inset: 0; background: rgba(0,0,0,0.5); z-index: 900;
    }
    .manage-dialog {
      position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%);
      width: 560px; max-width: 100vw; max-height: 80vh;
      background: var(--mat-sys-surface); border-radius: 8px; z-index: 901;
      display: flex; flex-direction: column; box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    }
    .manage-dialog-header {
      padding: 16px 20px; border-bottom: 1px solid var(--mat-sys-outline-variant);
      font-size: 1rem; font-weight: 700;
    }
    .manage-dialog-body { flex: 1; overflow-y: auto; padding: 12px 16px; }
    .manage-dialog-footer {
      padding: 10px 16px; border-top: 1px solid var(--mat-sys-outline-variant);
      display: flex; justify-content: flex-end;
    }

    .assessment-row {
      display: flex; align-items: center; gap: 8px; padding: 8px;
      border-radius: 4px; border: 1px solid var(--mat-sys-outline-variant);
      margin-bottom: 6px; cursor: pointer;
      transition: background 0.1s, border-color 0.1s;
    }
    .assessment-row.in-collection {
      border-color: rgba(68,114,196,0.3);
      background: rgba(68,114,196,0.06);
    }
    .assessment-row:hover { background: rgba(0,0,0,0.04); }
    .assessment-row.in-collection:hover { background: rgba(68,114,196,0.1); }

    table { width: 100%; }
    .doc-id { font-family: monospace; font-size: 0.7rem; color: var(--mat-sys-on-surface-variant); }

    /* Spinner / error states */
    .spinner-center { display: flex; justify-content: center; padding: 40px; }
    .error-wrap { padding: 16px; }
    .error-box {
      padding: 12px; border-radius: 6px;
      background: rgba(244,67,54,0.1); color: #f44336; margin-top: 12px;
    }

    /* Stats bar extras */
    .status-label { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); margin-bottom: 4px; }
    .status-chip { font-size: 0.72rem; font-weight: 700; padding: 3px 10px; border-radius: 12px; }
    .bar-completion-label { color: var(--mat-sys-on-surface-variant); }
    .bar-score-label { font-weight: 700; color: var(--mat-sys-primary); }
    .progress-bar { height: 6px; border-radius: 3px; }
    .counts-row { display: flex; gap: 24px; }
    .count-val-compliant { color: #70AD47; }
    .count-val-noncompliant { color: #FF5252; }
    .count-val-total { color: var(--mat-sys-on-surface-variant); }
    .due-date-row { display: flex; align-items: center; gap: 4px; }
    .due-date-text { font-size: 0.78rem; color: var(--mat-sys-on-surface-variant); }
    .description-text { margin-top: 12px; font-size: 0.85rem; color: var(--mat-sys-on-surface-variant); font-style: italic; }

    /* Members table */
    .section-title { font-weight: 700; color: var(--mat-sys-primary); font-size: 0.9rem; }
    .section-count {
      font-size: 0.65rem; padding: 1px 7px; border-radius: 10px;
      background: var(--mat-sys-surface-variant);
    }
    .empty-icon { color: var(--mat-sys-on-surface-variant); display: block; margin-bottom: 4px; }
    .empty-text { color: var(--mat-sys-on-surface-variant); font-size: 0.88rem; }
    .empty-cta { color: var(--mat-sys-primary); font-size: 0.78rem; margin-top: 4px; }
    .group-code { font-family: monospace; font-weight: 700; color: var(--mat-sys-primary); font-size: 0.8rem; }
    .group-name { font-size: 0.62rem; color: var(--mat-sys-on-surface-variant); }
    .workbook-name { font-weight: 600; font-size: 0.85rem; line-height: 1.3; }
    .product-chip {
      font-size: 0.6rem; padding: 1px 6px; border-radius: 10px;
      border: 1px solid var(--mat-sys-outline-variant);
    }
    .cell-right { text-align: right; font-size: 0.78rem; }
    .score-dash { color: var(--mat-sys-on-surface-variant); font-size: 0.78rem; }
    .score-val { font-weight: 700; font-size: 0.78rem; }
    .remove-btn { color: var(--mat-sys-error); opacity: 0.4; }
    .row-default { cursor: default; }

    /* Manage dialog body */
    .manage-search { width: 100%; margin-bottom: 12px; }
    .manage-spinner-wrap { display: flex; justify-content: center; padding: 24px; }
    .manage-empty { text-align: center; padding: 24px; color: var(--mat-sys-on-surface-variant); font-size: 0.88rem; }
    .assess-row-inner { flex: 1; min-width: 0; }
    .assess-workbook { font-size: 0.88rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
    .assess-group { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
    .checkbox-no-events { pointer-events: none; }
  `],
  template: `
    @if (collectionQuery.isLoading()) {
      <div class="spinner-center">
        <mat-spinner diameter="36"></mat-spinner>
      </div>
    }

    @if (collectionQuery.error()) {
      <div class="error-wrap">
        <button mat-button (click)="router.navigate(['/assessments'])">
          <mat-icon>arrow_back</mat-icon> Back to Assessments
        </button>
        <div class="error-box">
          Collection not found or failed to load.
        </div>
      </div>
    }

    @if (collectionQuery.data(); as coll) {
      <!-- Page header -->
      <app-page-header
        [title]="coll.name"
        [subtitle]="coll.product_family + (coll.product_type ? ' / ' + coll.product_type : '') + ' · Assessment Collection'">
        <div actions class="actions-row">
          <button mat-stroked-button (click)="router.navigate(['/assessments'])">
            <mat-icon>arrow_back</mat-icon>
            Back
          </button>
          <button mat-stroked-button (click)="manageOpen.set(true)">
            <mat-icon>person_add</mat-icon>
            Manage Assessments
          </button>
          <button mat-stroked-button [disabled]="!!downloading()"
            (click)="handleExport(coll, 'csv')">
            <mat-icon>download</mat-icon>
            {{ downloading() === 'csv' ? 'Exporting…' : 'CSV' }}
          </button>
          <button mat-stroked-button [disabled]="!!downloading()"
            (click)="handleExport(coll, 'xlsx')">
            <mat-icon>download</mat-icon>
            {{ downloading() === 'xlsx' ? 'Exporting…' : 'XLSX' }}
          </button>
          <button mat-raised-button color="primary" [disabled]="!!downloading()"
            (click)="handleExport(coll, 'pdf')">
            <mat-icon>download</mat-icon>
            {{ downloading() === 'pdf' ? 'Exporting…' : 'PDF' }}
          </button>
        </div>
      </app-page-header>

      <!-- Stats bar -->
      <div class="stats-card">
        <div class="stats-row">

          <!-- Status chip -->
          <div>
            <div class="status-label">Status</div>
            <span class="status-chip"
              [style.background]="statusCfg(coll.stats.status).bg"
              [style.color]="statusCfg(coll.stats.status).color">
              {{ statusCfg(coll.stats.status).label }}
            </span>
          </div>

          <!-- Completion progress -->
          <div class="bar-wrapper">
            <div class="bar-header">
              <span class="bar-completion-label">Completion</span>
              <span class="bar-score-label">
                {{ coll.stats.started }}/{{ coll.stats.total }} assessments · {{ coll.stats.completion_pct }}%
              </span>
            </div>
            <mat-progress-bar mode="determinate"
              [value]="coll.stats.completion_pct"
              class="progress-bar">
            </mat-progress-bar>
          </div>

          <!-- Compliance score -->
          <div class="bar-wrapper">
            <div class="bar-header">
              <span class="bar-completion-label">Compliance Score</span>
              <span [style.color]="scoreColor(coll.stats.compliance_pct)" class="score-val">
                {{ coll.stats.compliance_pct }}%
              </span>
            </div>
            <mat-progress-bar mode="determinate"
              [value]="coll.stats.compliance_pct"
              [style.--mat-progress-bar-active-indicator-color]="scoreColor(coll.stats.compliance_pct)"
              class="progress-bar">
            </mat-progress-bar>
          </div>

          <!-- Counts -->
          <div class="counts-row">
            <div class="count-col">
              <div class="count-val count-val-compliant">{{ coll.stats.items_compliant }}</div>
              <div class="count-label">Compliant</div>
            </div>
            <div class="count-col">
              <div class="count-val count-val-noncompliant">{{ coll.stats.items_non_compliant }}</div>
              <div class="count-label">Non-Compliant</div>
            </div>
            <div class="count-col">
              <div class="count-val count-val-total">{{ coll.stats.items_total }}</div>
              <div class="count-label">Total Items</div>
            </div>
          </div>

          <!-- Due date -->
          @if (coll.due_date) {
            <div class="due-date-row">
              <mat-icon class="icon-sm">calendar_today</mat-icon>
              <span class="due-date-text">Due {{ coll.due_date }}</span>
            </div>
          }

        </div>

        <!-- Description -->
        @if (coll.description) {
          <div class="description-text">
            {{ coll.description }}
          </div>
        }
      </div>

      <!-- Members table -->
      <div>
        <div class="section-header">
          <span class="section-title">Assessments</span>
          <span class="section-count">{{ coll.members.length }}</span>
        </div>

        @if (coll.members.length === 0) {
          <div class="empty-box" (click)="manageOpen.set(true)">
            <mat-icon class="empty-icon">person_add</mat-icon>
            <div class="empty-text">
              No assessments in this collection yet.
            </div>
            <div class="empty-cta">
              Click to add assessments
            </div>
          </div>
        } @else {
          <mat-card class="members-card">
            <table mat-table [dataSource]="coll.members">

              <ng-container matColumnDef="control_group">
                <th mat-header-cell *matHeaderCellDef class="mat-column-control_group">Control Group</th>
                <td mat-cell *matCellDef="let m">
                  <div class="group-code">
                    {{ m.group_code }}
                  </div>
                  <div class="group-name">{{ m.group_name }}</div>
                </td>
              </ng-container>

              <ng-container matColumnDef="workbook">
                <th mat-header-cell *matHeaderCellDef>Workbook</th>
                <td mat-cell *matCellDef="let m">
                  <div class="doc-id">{{ m.document_id }}</div>
                  <div class="workbook-name">{{ m.workbook_name }}</div>
                  @if (m.items_non_compliant > 0) {
                    <div>
                      <button class="nc-expand-btn"
                        (click)="toggleNcExpand(m.assessment_id)">
                        <mat-icon class="icon-sm">{{ ncExpanded().has(m.assessment_id) ? 'expand_less' : 'expand_more' }}</mat-icon>
                        {{ m.items_non_compliant }} non-compliant
                      </button>
                      @if (ncExpanded().has(m.assessment_id)) {
                        <div class="nc-box">
                          Non-compliant item details visible in the export report.
                        </div>
                      }
                    </div>
                  }
                </td>
              </ng-container>

              <ng-container matColumnDef="product">
                <th mat-header-cell *matHeaderCellDef class="mat-column-product">Product</th>
                <td mat-cell *matCellDef="let m">
                  <span class="product-chip">{{ m.product_type }}</span>
                </td>
              </ng-container>

              <ng-container matColumnDef="items">
                <th mat-header-cell *matHeaderCellDef class="mat-column-items col-right">Items</th>
                <td mat-cell *matCellDef="let m" class="cell-right">
                  {{ m.items_total }}
                </td>
              </ng-container>

              <ng-container matColumnDef="compliant">
                <th mat-header-cell *matHeaderCellDef class="mat-column-compliant col-right">Compliant</th>
                <td mat-cell *matCellDef="let m" class="cell-right"
                  [style.color]="m.items_compliant > 0 ? '#70AD47' : 'var(--mat-sys-on-surface-variant)'">
                  {{ m.items_compliant }}
                </td>
              </ng-container>

              <ng-container matColumnDef="non_compliant">
                <th mat-header-cell *matHeaderCellDef class="mat-column-non_compliant col-right">Non-Compliant</th>
                <td mat-cell *matCellDef="let m" class="cell-right"
                  [style.color]="m.items_non_compliant > 0 ? '#FF5252' : 'var(--mat-sys-on-surface-variant)'">
                  {{ m.items_non_compliant }}
                </td>
              </ng-container>

              <ng-container matColumnDef="score">
                <th mat-header-cell *matHeaderCellDef class="mat-column-score col-right">Score</th>
                <td mat-cell *matCellDef="let m" class="cell-right">
                  @if (m.items_total > 0) {
                    <span class="score-val"
                      [style.color]="scoreColor(m.compliance_pct)">
                      {{ m.compliance_pct }}%
                    </span>
                  } @else {
                    <span class="score-dash">—</span>
                  }
                </td>
              </ng-container>

              <ng-container matColumnDef="remove">
                <th mat-header-cell *matHeaderCellDef class="mat-column-remove"></th>
                <td mat-cell *matCellDef="let m">
                  <button mat-icon-button matTooltip="Remove from collection"
                    class="remove-btn"
                    [disabled]="removeAssessmentMut.isPending()"
                    (click)="removeAssessmentMut.mutate({ collId: coll.id, assessmentId: m.assessment_id })"
                    (mouseenter)="$event.target && ($any($event.target).closest('button').style.opacity='1')"
                    (mouseleave)="$event.target && ($any($event.target).closest('button').style.opacity='0.4')">
                    <mat-icon class="icon-sm">person_remove</mat-icon>
                  </button>
                </td>
              </ng-container>

              <tr mat-header-row *matHeaderRowDef="memberColumns"></tr>
              <tr mat-row *matRowDef="let row; columns: memberColumns" class="row-default"></tr>
            </table>
          </mat-card>
        }
      </div>
    }

    <!-- ── Manage Assessments Dialog ── -->
    @if (manageOpen()) {
      <div class="overlay-backdrop" (click)="closeManageDialog()"></div>
      <div class="manage-dialog">
        <div class="manage-dialog-header">Manage Assessments</div>

        <div class="manage-dialog-body">
          <mat-form-field appearance="outline" class="manage-search" subscriptSizing="dynamic">
            <mat-label>Search</mat-label>
            <input matInput [(ngModel)]="manageSearch" placeholder="Search assessments…">
          </mat-form-field>

          @if (assessmentsForCollectionQuery.isLoading()) {
            <div class="manage-spinner-wrap">
              <mat-spinner diameter="24"></mat-spinner>
            </div>
          } @else if (filteredAssessments().length === 0) {
            <div class="manage-empty">
              No assessments found.
            </div>
          } @else {
            @for (a of filteredAssessments(); track a.id) {
              @let inColl = currentMemberIds().has(a.id);
              <div class="assessment-row" [class.in-collection]="inColl"
                (click)="toggleAssessment(a.id, inColl)">
                <mat-checkbox [checked]="inColl" (click)="$event.stopPropagation()"
                  (change)="toggleAssessment(a.id, inColl)" class="checkbox-no-events">
                </mat-checkbox>
                <div class="assess-row-inner">
                  <div class="doc-id">{{ a.document_id }}</div>
                  <div class="assess-workbook">
                    {{ a.workbook_name }}
                  </div>
                  <div class="assess-group">
                    {{ a.group_code.toUpperCase() }} — {{ a.group_name }}
                  </div>
                </div>
                <span class="product-chip">{{ a.product_type }}</span>
              </div>
            }
          }
        </div>

        <div class="manage-dialog-footer">
          <button mat-raised-button color="primary" (click)="closeManageDialog()">Done</button>
        </div>
      </div>
    }
  `,
})
export class CollectionDetailComponent {
  private readonly route          = inject(ActivatedRoute)
  readonly router                 = inject(Router)
  private readonly http           = inject(HttpClient)
  private readonly collectionsApi = inject(CollectionsApiService)
  private readonly theme          = inject(ThemeService)
  private readonly qc             = injectQueryClient()

  private readonly collectionId   = signal<string>('')

  constructor() {
    this.route.paramMap.subscribe(p => {
      const id = p.get('id')
      if (id) this.collectionId.set(id)
    })
  }

  // ── Queries ──────────────────────────────────────────────────────────────────

  collectionQuery = injectQuery(() => ({
    queryKey: ['collection', this.collectionId()],
    queryFn:  () => firstValueFrom(this.collectionsApi.get(this.collectionId())),
    enabled:  !!this.collectionId(),
  }))

  assessmentsForCollectionQuery = injectQuery(() => ({
    queryKey: ['assessments-for-collection', this.collectionQuery.data()?.product_family],
    queryFn:  () => {
      const family = this.collectionQuery.data()!.product_family
      return firstValueFrom(this.http.get<AssessmentListItem[]>('/api/v1/assessments', {
        params: { product_family: family }
      }))
    },
    enabled: !!this.collectionQuery.data() && this.manageOpen(),
  }))

  // ── Mutations ────────────────────────────────────────────────────────────────

  addAssessmentMut = injectMutation(() => ({
    mutationFn: (assessmentId: string) =>
      firstValueFrom(this.collectionsApi.addAssessment(this.collectionId(), assessmentId)),
    onSuccess: () => this.qc.invalidateQueries({ queryKey: ['collection', this.collectionId()] }),
  }))

  removeAssessmentMut = injectMutation(() => ({
    mutationFn: (args: { collId: string; assessmentId: string }) =>
      firstValueFrom(this.collectionsApi.removeAssessment(args.collId, args.assessmentId)),
    onSuccess: () => this.qc.invalidateQueries({ queryKey: ['collection', this.collectionId()] }),
  }))

  // ── Local state ──────────────────────────────────────────────────────────────

  downloading   = signal<string | null>(null)
  manageOpen    = signal(false)
  manageSearch  = ''
  ncExpanded    = signal<Set<string>>(new Set())

  memberColumns = ['control_group', 'workbook', 'product', 'items', 'compliant', 'non_compliant', 'score', 'remove']

  // ── Computed ─────────────────────────────────────────────────────────────────

  currentMemberIds = computed(() => {
    const coll = this.collectionQuery.data()
    if (!coll) return new Set<string>()
    return new Set(coll.members.map(m => m.assessment_id))
  })

  filteredAssessments = computed(() => {
    const items = this.assessmentsForCollectionQuery.data() ?? []
    const q     = this.manageSearch.toLowerCase()
    if (!q) return items
    return items.filter(a =>
      a.document_id.toLowerCase().includes(q) ||
      a.workbook_name.toLowerCase().includes(q) ||
      a.group_code.toLowerCase().includes(q))
  })

  // ── Helpers ──────────────────────────────────────────────────────────────────

  scoreColor = scoreColor

  statusCfg = (status: string) => {
    const dark = this.theme.isDark()
    if (status === 'complete') return dark
      ? { label: 'Complete',    bg: 'rgba(198,239,206,0.15)', color: '#C6EFCE' }
      : { label: 'Complete',    bg: 'rgba(46,125,50,0.12)',   color: '#1b5e20' }
    if (status === 'in_progress') return dark
      ? { label: 'In Progress', bg: 'rgba(255,192,0,0.12)',   color: '#856404' }
      : { label: 'In Progress', bg: 'rgba(230,145,0,0.15)',   color: '#7a4800' }
    return dark
      ? { label: 'Not Started', bg: 'rgba(255,255,255,0.06)', color: '#888' }
      : { label: 'Not Started', bg: 'rgba(0,0,0,0.06)',       color: '#555' }
  }

  toggleNcExpand(assessmentId: string) {
    this.ncExpanded.update(s => {
      const n = new Set(s)
      n.has(assessmentId) ? n.delete(assessmentId) : n.add(assessmentId)
      return n
    })
  }

  toggleAssessment(assessmentId: string, isInCollection: boolean) {
    if (isInCollection) this.removeAssessmentMut.mutate({ collId: this.collectionId(), assessmentId })
    else this.addAssessmentMut.mutate(assessmentId)
  }

  closeManageDialog() {
    this.manageOpen.set(false)
    this.qc.invalidateQueries({ queryKey: ['collection', this.collectionId()] })
  }

  async handleExport(coll: CollectionRead, format: 'csv' | 'xlsx' | 'pdf') {
    this.downloading.set(format)
    const mimeTypes: Record<string, string> = {
      csv:  'text/csv',
      xlsx: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
      pdf:  'application/pdf',
    }
    try {
      const blob = await firstValueFrom(
        this.http.get(this.collectionsApi.exportUrl(coll.id, format), { responseType: 'blob' }))
      const filename = `collection_${coll.name.replace(/\s+/g, '_')}.${format}`
      const url = URL.createObjectURL(blob)
      const a   = document.createElement('a')
      a.href     = url
      a.download = filename
      document.body.appendChild(a)
      a.click()
      document.body.removeChild(a)
      URL.revokeObjectURL(url)
    } catch {
      // silently fail — user can retry
    } finally {
      this.downloading.set(null)
    }
  }
}
