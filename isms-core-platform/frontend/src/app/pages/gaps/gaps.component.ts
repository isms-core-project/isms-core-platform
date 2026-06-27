import { Component, inject, signal, computed, OnInit, Input, Output, EventEmitter } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { SlicePipe } from '@angular/common'
import { firstValueFrom } from 'rxjs'

import { injectQuery, injectMutation, injectQueryClient } from '@tanstack/angular-query-experimental'

import { MatCardModule } from '@angular/material/card'
import { MatTableModule } from '@angular/material/table'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatButtonModule } from '@angular/material/button'
import { MatIconModule } from '@angular/material/icon'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatChipsModule } from '@angular/material/chips'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatButtonToggleModule } from '@angular/material/button-toggle'
import { MatDialogModule, MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog'

import { GapsApiService } from '../../api/gaps-api.service'
import { ControlsApiService } from '../../api/controls-api.service'
import { GeneratorsApiService, GeneratorItem } from '../../api/generators-api.service'
import { ProductService } from '../../core/services/product.service'
import { ProjectService } from '../../core/services/project.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'
import { MetricCardComponent } from '../../shared/components/metric-card.component'
import { StatusChipComponent } from '../../shared/components/status-chip.component'
import { GapRead, GapCreate, GapPatch, EvidenceRead } from '../../shared/types'

// ─── Constants ────────────────────────────────────────────────────────────────

const SEVERITIES = ['critical', 'high', 'medium', 'low']
const STATUSES   = ['open', 'in_progress', 'accepted', 'closed']
const PRODUCTS   = ['framework', 'operational', 'both']
const RISK_LEVELS = ['LOW', 'MEDIUM', 'HIGH', 'VERY_HIGH']

const RISK_COLOR: Record<string, string> = {
  VERY_HIGH: '#C00000', HIGH: '#FF5722', MEDIUM: '#FF9800', LOW: '#4CAF50',
}

function capitalize(s: string): string { return s.charAt(0).toUpperCase() + s.slice(1) }

function formatDate(d: string): string {
  return new Date(d).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' })
}

// ─── Inline Editor Component ──────────────────────────────────────────────────

@Component({
  selector: 'app-gap-inline-editor',
  standalone: true,
  imports: [
    FormsModule,
    MatButtonModule, MatFormFieldModule, MatInputModule,
    MatSelectModule, MatIconModule, MatProgressSpinnerModule,
    MatTooltipModule,
  ],
  template: `
    <div class="edit-panel">
      @if (errorMsg()) {
        <div class="alert-error">{{ errorMsg() }}</div>
      }

      <mat-form-field appearance="outline" class="gap-editor-field-full" subscriptSizing="dynamic">
        <mat-label>Description</mat-label>
        <textarea matInput [(ngModel)]="form.gap_description" rows="2"></textarea>
      </mat-form-field>

      <div class="gap-editor-row">
        <mat-form-field appearance="outline" class="gap-editor-field-half" subscriptSizing="dynamic">
          <mat-label>Severity</mat-label>
          <mat-select [(ngModel)]="form.severity">
            @for (s of SEVERITIES; track s) { <mat-option [value]="s">{{ cap(s) }}</mat-option> }
          </mat-select>
        </mat-form-field>
        <mat-form-field appearance="outline" class="gap-editor-field-half" subscriptSizing="dynamic">
          <mat-label>Status</mat-label>
          <mat-select [(ngModel)]="form.status">
            @for (s of STATUSES; track s) { <mat-option [value]="s">{{ s.replace('_', ' ') }}</mat-option> }
          </mat-select>
        </mat-form-field>
        <mat-form-field appearance="outline" class="gap-editor-field-half" subscriptSizing="dynamic">
          <mat-label>Owner</mat-label>
          <input matInput [(ngModel)]="form.owner" />
        </mat-form-field>
        <mat-form-field appearance="outline" class="gap-editor-field-half" subscriptSizing="dynamic">
          <mat-label>Due Date</mat-label>
          <input matInput type="date" [(ngModel)]="form.due_date" />
        </mat-form-field>
      </div>

      <mat-form-field appearance="outline" class="gap-editor-field-full" subscriptSizing="dynamic">
        <mat-label>Remediation Plan</mat-label>
        <textarea matInput [(ngModel)]="form.remediation_plan" rows="2"></textarea>
      </mat-form-field>

      <div class="gap-editor-mb10">
        <div class="section-label">Risk Override (optional)</div>
        <mat-form-field appearance="outline" class="gap-editor-field-sm" subscriptSizing="dynamic">
          <mat-label>Risk Level</mat-label>
          <mat-select [(ngModel)]="form.risk_level">
            <mat-option value="">Auto-calculated</mat-option>
            @for (r of RISK_LEVELS; track r) { <mat-option [value]="r">{{ r.replace('_', ' ') }}</mat-option> }
          </mat-select>
        </mat-form-field>
      </div>

      <!-- Linked evidence -->
      <div class="gap-editor-mb12">
        <div class="gap-editor-ev-row">
          <span class="section-label">Evidence Linked</span>
          <span class="count-badge">{{ linkedEvidence().length }}</span>
        </div>
        @if (linkedEvidence().length === 0) {
          <span class="gap-editor-dim">No evidence attached.</span>
        }
        @for (ev of linkedEvidence(); track ev.id) {
          <div class="ev-item">
            <mat-icon class="icon-xs-dim">attach_file</mat-icon>
            <span class="gap-editor-ev-label">{{ ev.title }}</span>
            <span class="gap-editor-ev-type"> {{ ev.evidence_type }}</span>
            <button mat-icon-button matTooltip="Remove link" [disabled]="detachMut.isPending()"
              (click)="detach(ev.id)" class="icon-btn-xs">
              <mat-icon class="icon-xs">link_off</mat-icon>
            </button>
          </div>
        }
      </div>

      <div class="gap-editor-actions">
        <button mat-raised-button color="primary" [disabled]="saveMut.isPending()" (click)="save()">
          @if (saveMut.isPending()) {
            <mat-spinner diameter="14" class="spinner-inline" />Saving…
          } @else { Save }
        </button>
        <button mat-button (click)="closed.emit()">Cancel</button>
      </div>
    </div>
  `,
  styles: [`
    .edit-panel { padding: 16px; background: var(--mat-sys-surface-container); }
    .section-label {
      font-size: 0.68rem; font-weight: 600; text-transform: uppercase;
      letter-spacing: 0.06em; color: var(--mat-sys-on-surface-variant); display: block; margin-bottom: 4px;
    }
    .count-badge {
      height: 16px; min-width: 16px; padding: 0 4px; border-radius: 8px;
      font-size: 0.62rem; font-weight: 600; display: inline-flex; align-items: center;
      background: var(--mat-sys-surface-variant); color: var(--mat-sys-on-surface-variant);
    }
    .ev-item {
      display: flex; align-items: center; gap: 6px; padding: 3px 0;
      border-bottom: 1px solid var(--mat-sys-outline-variant);
    }
    .alert-error {
      padding: 8px 12px; border-radius: 6px; font-size: 0.82rem; margin-bottom: 8px;
      background: rgba(192,0,0,0.1); border: 1px solid rgba(192,0,0,0.3); color: var(--mat-sys-error);
    }
    .gap-editor-field-full { width: 100%; margin-bottom: 10px; }
    .gap-editor-row { display: flex; gap: 12px; margin-bottom: 10px; flex-wrap: wrap; }
    .gap-editor-field-half { flex: 1; min-width: 120px; }
    .gap-editor-field-sm { min-width: 180px; }
    .gap-editor-mb10 { margin-bottom: 10px; }
    .gap-editor-mb12 { margin-bottom: 12px; }
    .gap-editor-ev-row { display: flex; align-items: center; gap: 8px; margin-bottom: 6px; }
    .gap-editor-dim { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
    .icon-xs-dim { font-size: 14px; height: 14px; width: 14px; color: var(--mat-sys-on-surface-variant); }
    .gap-editor-ev-label { flex: 1; min-width: 0; font-size: 0.72rem; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .gap-editor-ev-type { font-size: 0.68rem; color: var(--mat-sys-on-surface-variant); }
    .icon-btn-xs { width: 24px; height: 24px; line-height: 24px; }
    .icon-xs { font-size: 14px; height: 14px; width: 14px; }
    .gap-editor-actions { display: flex; gap: 8px; }
    .spinner-inline { display: inline-block; margin-right: 4px; }
    .gap-panel-title { font-size: 1.1rem; font-weight: 500; }
  `],
})
export class GapInlineEditorComponent implements OnInit {
  @Input() gap!: GapRead
  @Output() closed = new EventEmitter<void>()

  private gapsApi = inject(GapsApiService)
  private qc = injectQueryClient()

  readonly SEVERITIES = SEVERITIES
  readonly STATUSES   = STATUSES
  readonly RISK_LEVELS = RISK_LEVELS

  errorMsg = signal('')
  form: GapPatch = {}

  ngOnInit(): void {
    this.form = {
      gap_description: this.gap.gap_description,
      severity: this.gap.severity,
      status: this.gap.status,
      owner: this.gap.owner ?? '',
      due_date: this.gap.due_date ?? '',
      remediation_plan: this.gap.remediation_plan ?? '',
      risk_level: this.gap.risk_level ?? '',
    }
  }

  linkedQuery = injectQuery(() => ({
    queryKey: ['gap-evidence', this.gap?.id],
    queryFn: () => firstValueFrom(this.gapsApi.listEvidence(this.gap.id)),
    enabled: !!this.gap,
  }))

  linkedEvidence = computed((): EvidenceRead[] => this.linkedQuery.data() ?? [])

  saveMut = injectMutation(() => ({
    mutationFn: (body: GapPatch) => firstValueFrom(this.gapsApi.update(this.gap.id, body)),
    onSuccess: () => { this.qc.invalidateQueries({ queryKey: ['gaps'] }); this.closed.emit() },
    onError: () => this.errorMsg.set('Failed to save changes'),
  }))

  detachMut = injectMutation(() => ({
    mutationFn: (evidenceId: string) => firstValueFrom(this.gapsApi.detachEvidence(this.gap.id, evidenceId)),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['gap-evidence', this.gap.id] })
      this.qc.invalidateQueries({ queryKey: ['gaps'] })
    },
  }))

  save(): void {
    this.errorMsg.set('')
    this.saveMut.mutate({
      ...this.form,
      owner: this.form.owner || null,
      due_date: this.form.due_date || null,
      remediation_plan: this.form.remediation_plan || null,
      risk_assessed_by: this.form.risk_level ? 'manual' : undefined,
    })
  }

  detach(id: string): void { this.detachMut.mutate(id) }
  cap(s: string): string { return capitalize(s) }
}

// ─── Delete Gap Dialog ────────────────────────────────────────────────────────

export interface DeleteGapDialogData { gap: GapRead }

@Component({
  selector: 'app-delete-gap-dialog',
  standalone: true,
  imports: [MatButtonModule, MatDialogModule, MatProgressSpinnerModule],
  template: `
    <h2 mat-dialog-title>Delete gap?</h2>
    <mat-dialog-content>
      <p class="dialog-body-text">
        <strong>{{ data.gap.control_group_code.toUpperCase() }}</strong> —
        {{ data.gap.gap_description | slice:0:80 }}{{ data.gap.gap_description.length > 80 ? '…' : '' }}
      </p>
    </mat-dialog-content>
    <mat-dialog-actions>
      <button mat-stroked-button [mat-dialog-close]="false">Cancel</button>
      <button mat-raised-button color="warn" [mat-dialog-close]="true">Delete</button>
    </mat-dialog-actions>
  `,
  styles: [`
    .dialog-body-text { font-size: 0.875rem; color: var(--mat-sys-on-surface-variant); margin: 0; }
  `],
})
export class DeleteGapDialogComponent {
  readonly data = inject<DeleteGapDialogData>(MAT_DIALOG_DATA)
}

// ─── Create Gap Dialog ────────────────────────────────────────────────────────

export interface CreateGapDialogData { productFamily: string; projectId?: string }

@Component({
  selector: 'app-create-gap-dialog',
  standalone: true,
  imports: [
    FormsModule,
    MatButtonModule, MatFormFieldModule, MatInputModule,
    MatSelectModule, MatIconModule, MatProgressSpinnerModule,
    MatDialogModule,
  ],
  template: `
    <h2 mat-dialog-title>Create Gap</h2>
    <mat-dialog-content>
      @if (errorMsg()) {
        <div class="alert-error">{{ errorMsg() }}</div>
      }

      <mat-form-field appearance="outline" class="form-full" subscriptSizing="dynamic">
        <mat-label>Control Group *</mat-label>
        <mat-select [(ngModel)]="form.control_group_id">
          @for (c of controls(); track c.id) {
            <mat-option [value]="c.id">
              <span class="opt-code">{{ c.group_code.toUpperCase() }}</span>
              {{ c.group_name }}
            </mat-option>
          }
        </mat-select>
      </mat-form-field>

      <mat-form-field appearance="outline" class="form-full" subscriptSizing="dynamic">
        <mat-label>Description *</mat-label>
        <textarea matInput [(ngModel)]="form.gap_description" rows="3"></textarea>
      </mat-form-field>

      <div class="form-row">
        <mat-form-field appearance="outline" class="form-half" subscriptSizing="dynamic">
          <mat-label>Severity</mat-label>
          <mat-select [(ngModel)]="form.severity">
            @for (s of SEVERITIES; track s) { <mat-option [value]="s">{{ cap(s) }}</mat-option> }
          </mat-select>
        </mat-form-field>
        <mat-form-field appearance="outline" class="form-half" subscriptSizing="dynamic">
          <mat-label>Product</mat-label>
          <mat-select [(ngModel)]="form.product_type">
            @for (p of PRODUCTS; track p) { <mat-option [value]="p">{{ cap(p) }}</mat-option> }
          </mat-select>
        </mat-form-field>
      </div>

      @if (showWorkbookPicker() && generators().length > 1) {
        <mat-form-field appearance="outline" class="form-full" subscriptSizing="dynamic">
          <mat-label>Workbook / IMP (optional)</mat-label>
          <mat-select [(ngModel)]="workbookId">
            <mat-option value="">Any</mat-option>
            @for (g of generators(); track g.document_id) {
              <mat-option [value]="g.document_id">
                <span class="opt-code">{{ g.document_id }}</span>
                {{ g.workbook_name }}
              </mat-option>
            }
          </mat-select>
        </mat-form-field>
      }

      <div class="form-row">
        <mat-form-field appearance="outline" class="form-half" subscriptSizing="dynamic">
          <mat-label>Owner</mat-label>
          <input matInput [(ngModel)]="form.owner" />
        </mat-form-field>
        <mat-form-field appearance="outline" class="form-half" subscriptSizing="dynamic">
          <mat-label>Due Date</mat-label>
          <input matInput type="date" [(ngModel)]="form.due_date" />
        </mat-form-field>
      </div>

      <mat-form-field appearance="outline" class="form-full" subscriptSizing="dynamic">
        <mat-label>Remediation Plan</mat-label>
        <textarea matInput [(ngModel)]="form.remediation_plan" rows="2"></textarea>
      </mat-form-field>
    </mat-dialog-content>
    <mat-dialog-actions>
      <button mat-button [mat-dialog-close]="false">Cancel</button>
      <button mat-raised-button color="primary" [disabled]="createMut.isPending()" (click)="submit()">
        @if (createMut.isPending()) {
          <mat-spinner diameter="14" class="spinner-inline" />Creating…
        } @else { Create Gap }
      </button>
    </mat-dialog-actions>
  `,
  styles: [`
    :host { display: block; min-width: 480px; max-width: 560px; }
    mat-dialog-content { display: flex; flex-direction: column; gap: 12px; max-height: 60vh; }
    .alert-error {
      padding: 8px 12px; border-radius: 6px; font-size: 0.82rem;
      background: rgba(192,0,0,0.1); border: 1px solid rgba(192,0,0,0.3); color: var(--mat-sys-error);
    }
    .spinner-inline { display: inline-block; margin-right: 4px; }
    .form-full { width: 100%; }
    .form-row  { display: flex; gap: 12px; }
    .form-half { flex: 1; }
    .opt-code  { font-family: monospace; font-size: 0.75rem; color: var(--mat-sys-primary); margin-right: 8px; }
  `],
})
export class CreateGapDialogComponent {
  readonly data = inject<CreateGapDialogData>(MAT_DIALOG_DATA)
  private dialogRef = inject(MatDialogRef<CreateGapDialogComponent>)

  private gapsApi = inject(GapsApiService)
  private controlsApi = inject(ControlsApiService)
  private generatorsApi = inject(GeneratorsApiService)
  private qc = injectQueryClient()

  readonly SEVERITIES = SEVERITIES
  readonly PRODUCTS   = PRODUCTS

  errorMsg  = signal('')
  workbookId = ''

  form: GapCreate = {
    control_group_id: '',
    gap_description: '',
    severity: 'medium',
    product_type: 'both',
    owner: '',
    due_date: '',
    remediation_plan: '',
  }

  private controlsQuery = injectQuery(() => ({
    queryKey: ['controls', this.data.productFamily],
    queryFn: () => firstValueFrom(this.controlsApi.list({ product_family: this.data.productFamily })),
    enabled: !!this.data.productFamily,
  }))

  controls = computed(() => this.controlsQuery.data() ?? [])

  selectedGroupCode = computed(() => {
    const ctrl = this.controls().find(c => c.id === this.form.control_group_id)
    return ctrl?.group_code ?? ''
  })

  showWorkbookPicker = computed(() =>
    !!this.selectedGroupCode() && this.form.product_type !== 'operational'
  )

  private generatorsQuery = injectQuery(() => ({
    queryKey: ['generators-for-group', this.selectedGroupCode()],
    queryFn: () => firstValueFrom(this.generatorsApi.list({ group_code: this.selectedGroupCode() })),
    enabled: this.showWorkbookPicker() && !!this.selectedGroupCode(),
  }))

  generators = computed((): GeneratorItem[] => this.generatorsQuery.data() ?? [])

  createMut = injectMutation(() => ({
    mutationFn: (body: GapCreate) => firstValueFrom(this.gapsApi.create(body)),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['gaps'] })
      this.dialogRef.close(true)
    },
    onError: (e: unknown) => {
      const msg = (e as { error?: { detail?: string } })?.error?.detail
      this.errorMsg.set(msg ?? 'Failed to create gap')
    },
  }))

  submit(): void {
    if (!this.form.control_group_id) { this.errorMsg.set('Select a control group'); return }
    if (!this.form.gap_description.trim()) { this.errorMsg.set('Description is required'); return }
    this.errorMsg.set('')
    this.createMut.mutate({
      ...this.form,
      owner: this.form.owner || undefined,
      due_date: this.form.due_date || undefined,
      remediation_plan: this.form.remediation_plan || undefined,
      workbook_document_id: this.workbookId || undefined,
      project_id: this.data.projectId || undefined,
    })
  }

  cap(s: string): string { return capitalize(s) }
}

// ─── Main Gaps Component ──────────────────────────────────────────────────────

@Component({
  selector: 'app-gaps',
  standalone: true,
  imports: [
    FormsModule, SlicePipe,
    MatCardModule, MatTableModule, MatFormFieldModule, MatInputModule,
    MatSelectModule, MatButtonModule, MatIconModule,
    MatTooltipModule, MatChipsModule, MatProgressSpinnerModule,
    MatButtonToggleModule, MatDialogModule,
    PageHeaderComponent, MetricCardComponent, StatusChipComponent,
    GapInlineEditorComponent,
  ],
  template: `
    <app-page-header title="Gap Analysis" [subtitle]="headerSubtitle()">
      <div actions>
        <span [matTooltip]="!activeProject() ? 'Select a project first to log gaps' : ''">
          <button mat-raised-button color="primary"
            [disabled]="!activeProject()"
            (click)="openCreateDialog()">
            <mat-icon>add</mat-icon>
            Create Gap
          </button>
        </span>
      </div>
    </app-page-header>

    <!-- Project context banner -->
    @if (activeProject()) {
      <div class="info-banner">
        Showing gaps for project: <strong>{{ activeProject()!.name }}</strong>
      </div>
    }

    <!-- Metrics -->
    @if (!gapsQuery.isLoading()) {
      <div class="metrics-row">
        <app-metric-card title="Total"       [value]="totalCount()"      icon="find_in_page" />
        <app-metric-card title="Open"        [value]="openCount()" />
        <app-metric-card title="In Progress" [value]="inProgressCount()" />
        <app-metric-card title="Critical"    [value]="criticalCount()" />
      </div>
    }

    <!-- Filters -->
    <mat-card class="filter-card">
      <mat-card-content>
        <div class="filter-row">
          <mat-button-toggle-group
            [value]="statusSig()"
            (change)="statusSig.set($event.value)">
            <mat-button-toggle value="">All</mat-button-toggle>
            <mat-button-toggle value="open">Open</mat-button-toggle>
            <mat-button-toggle value="in_progress">In Progress</mat-button-toggle>
            <mat-button-toggle value="accepted">Accepted</mat-button-toggle>
            <mat-button-toggle value="closed">Closed</mat-button-toggle>
          </mat-button-toggle-group>

          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="filter-sev-field">
            <mat-label>Severity</mat-label>
            <mat-select [value]="severitySig()" (selectionChange)="severitySig.set($event.value)">
              <mat-option value="">All</mat-option>
              @for (s of SEVERITIES; track s) {
                <mat-option [value]="s">{{ cap(s) }}</mat-option>
              }
            </mat-select>
          </mat-form-field>
        </div>
      </mat-card-content>
    </mat-card>

    <!-- Risk distribution -->
    @if (!gapsQuery.isLoading() && gaps().length > 0) {
      <mat-card class="card-mb">
        <mat-card-content class="card-content-pb">
          <div class="risk-dist-row">
            <span class="dist-label">Risk Distribution</span>
            @for (lvl of RISK_LEVEL_ORDER; track lvl) {
              <div class="risk-bucket">
                <span class="risk-count" [style.color]="riskColor(lvl)">{{ riskCounts()[lvl] }}</span>
                <span class="risk-label">{{ lvl.replace('_', ' ') }}</span>
              </div>
            }
          </div>
        </mat-card-content>
      </mat-card>
    }

    <!-- Error -->
    @if (gapsQuery.isError()) {
      <div class="alert-error alert-mb">Failed to load gaps.</div>
    }

    <!-- Empty state -->
    @if (!gapsQuery.isLoading() && gaps().length === 0 && !gapsQuery.isError()) {
      <div class="success-banner">No gaps match the current filters.</div>
    }

    <!-- Loading skeletons -->
    @if (gapsQuery.isLoading()) {
      <mat-card class="card-overflow">
        @for (i of [1,2,3,4,5]; track i) {
          <div class="skel-row">
            <div class="skel skel-sm"></div>
            <div class="skel skel-lg"></div>
            <div class="skel skel-sm"></div>
            <div class="skel skel-sm"></div>
            <div class="skel skel-sm"></div>
          </div>
        }
      </mat-card>
    }

    <!-- Gaps table -->
    @if (!gapsQuery.isLoading() && gaps().length > 0) {
      <mat-card class="card-overflow">
        <table mat-table [dataSource]="gaps()" class="gaps-table">

          <ng-container matColumnDef="control_group">
            <th mat-header-cell *matHeaderCellDef>Control Group</th>
            <td mat-cell *matCellDef="let gap">
              <span class="group-code">{{ gap.control_group_code.toUpperCase() }}</span>
              <span class="group-name">{{ gap.control_group_name }}</span>
            </td>
          </ng-container>

          <ng-container matColumnDef="description">
            <th mat-header-cell *matHeaderCellDef>Description</th>
            <td mat-cell *matCellDef="let gap">
              <span class="desc-clamp">{{ gap.gap_description }}</span>
            </td>
          </ng-container>

          <ng-container matColumnDef="severity">
            <th mat-header-cell *matHeaderCellDef>Severity</th>
            <td mat-cell *matCellDef="let gap">
              <app-status-chip [status]="gap.severity" />
            </td>
          </ng-container>

          <ng-container matColumnDef="risk">
            <th mat-header-cell *matHeaderCellDef>Risk</th>
            <td mat-cell *matCellDef="let gap">
              @if (gap.risk_level) {
                <app-status-chip [status]="gap.risk_level.toLowerCase()" [matTooltip]="gap.risk_treatment ?? ''" />
              } @else {
                <span class="cell-dim">—</span>
              }
            </td>
          </ng-container>

          <ng-container matColumnDef="status">
            <th mat-header-cell *matHeaderCellDef>Status</th>
            <td mat-cell *matCellDef="let gap">
              <app-status-chip [status]="gap.status" />
            </td>
          </ng-container>

          <ng-container matColumnDef="owner">
            <th mat-header-cell *matHeaderCellDef>Owner</th>
            <td mat-cell *matCellDef="let gap">
              <span class="cell-dim" [class.cell-primary]="!!gap.owner">
                {{ gap.owner ?? '—' }}
              </span>
            </td>
          </ng-container>

          <ng-container matColumnDef="due_date">
            <th mat-header-cell *matHeaderCellDef>Due Date</th>
            <td mat-cell *matCellDef="let gap">
              @if (gap.due_date) {
                <span class="due-date-text" [style.color]="isOverdue(gap) ? '#C00000' : 'inherit'">
                  {{ fmtDate(gap.due_date) }}{{ isOverdue(gap) ? ' ⚠' : '' }}
                </span>
              } @else {
                <span class="cell-dim">—</span>
              }
            </td>
          </ng-container>

          <ng-container matColumnDef="actions">
            <th mat-header-cell *matHeaderCellDef></th>
            <td mat-cell *matCellDef="let gap">
              @if (gap.evidence_count > 0) {
                <span class="ev-badge">{{ gap.evidence_count }} ev</span>
              }
              <button mat-icon-button [matTooltip]="editingId() === gap.id ? 'Collapse' : 'Edit'"
                (click)="toggleEdit(gap.id)">
                <mat-icon class="icon-sm">
                  {{ editingId() === gap.id ? 'expand_less' : 'edit' }}
                </mat-icon>
              </button>
              <button mat-icon-button matTooltip="Delete" class="btn-error"
                (click)="openDeleteDialog(gap)">
                <mat-icon class="icon-sm">delete</mat-icon>
              </button>
            </td>
          </ng-container>

          <tr mat-header-row *matHeaderRowDef="COLUMNS"></tr>
          <tr mat-row *matRowDef="let gap; columns: COLUMNS"
            [style.opacity]="gap.status === 'closed' ? '0.55' : '1'"></tr>
        </table>

        <!-- Inline editor below table -->
        @if (editingGap()) {
          <div class="editor-divider">
            <div class="editor-header">
              <span class="group-code group-code-sm">
                {{ editingGap()!.control_group_code.toUpperCase() }} — editing
              </span>
            </div>
            <app-gap-inline-editor
              [gap]="editingGap()!"
              (closed)="editingId.set(null)" />
          </div>
        }
      </mat-card>
    }
  `,
  styles: [`
    :host { display: block; }

    .metrics-row { display: flex; gap: 16px; margin-bottom: 16px; flex-wrap: wrap; }
    .metrics-row > * { flex: 1; min-width: 140px; }

    .filter-card { margin-bottom: 16px; }
    .filter-card mat-card-content { padding-bottom: 12px !important; }
    .filter-row { display: flex; gap: 12px; align-items: center; flex-wrap: wrap; }
    .filter-sev-field { min-width: 140px; }

    .risk-dist-row { display: flex; align-items: center; gap: 24px; flex-wrap: wrap; }
    .dist-label {
      font-size: 0.68rem; font-weight: 600; text-transform: uppercase;
      letter-spacing: 0.06em; color: var(--mat-sys-on-surface-variant);
    }
    .risk-bucket { text-align: center; }
    .risk-count { display: block; font-size: 1.25rem; font-weight: 800; line-height: 1; }
    .risk-label { font-size: 0.62rem; color: var(--mat-sys-on-surface-variant); }

    .gaps-table { width: 100%; }

    .group-code {
      display: block; font-family: monospace; font-weight: 700;
      font-size: 0.78rem; color: var(--mat-sys-primary);
    }
    .group-name { display: block; font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); line-height: 1.3; }

    .desc-clamp {
      font-size: 0.8rem;
      display: -webkit-box; -webkit-line-clamp: 2;
      -webkit-box-orient: vertical; overflow: hidden;
    }

    .sev-chip, .risk-chip {
      font-size: 0.65rem; height: 18px; line-height: 18px; padding: 0 6px;
      border-radius: 9px; display: inline-block; font-weight: 700;
    }

    .cell-dim { font-size: 0.78rem; color: var(--mat-sys-on-surface-variant); }
    .cell-primary { font-size: 0.78rem; color: var(--mat-sys-on-surface); }

    .ev-badge {
      font-size: 0.62rem; height: 16px; line-height: 16px; padding: 0 5px;
      border-radius: 8px; display: inline-block; margin-right: 4px;
      background: color-mix(in srgb, var(--mat-sys-primary) 14%, transparent); color: var(--mat-sys-primary);
    }

    .skel-row {
      display: flex; gap: 16px; padding: 12px 16px;
      border-bottom: 1px solid var(--mat-sys-outline-variant);
    }
    .skel {
      height: 12px; border-radius: 6px; animation: pulse 1.4s infinite;
      background: var(--mat-sys-surface-variant);
    }
    .skel-sm { width: 80px; flex-shrink: 0; }
    .skel-lg { flex: 1; }
    @keyframes pulse {
      0%, 100% { opacity: 0.5; }
      50% { opacity: 1; }
    }

    .info-banner {
      padding: 8px 14px; margin-top: 16px; margin-bottom: 16px; border-radius: 6px; font-size: 0.85rem;
      background: var(--mat-sys-surface-container); border: 1px solid var(--mat-sys-outline-variant);
    }
    .success-banner {
      padding: 10px 14px; border-radius: 6px; font-size: 0.875rem;
      background: rgba(29,158,117,0.1); border: 1px solid rgba(29,158,117,0.3);
    }
    .alert-error {
      padding: 10px 14px; border-radius: 6px; font-size: 0.85rem;
      background: rgba(192,0,0,0.1); border: 1px solid rgba(192,0,0,0.3); color: var(--mat-sys-error);
    }

    /* ── table column widths ── */
    .gaps-table .mat-column-control_group { width: 160px; min-width: 160px; }
    .gaps-table .mat-column-description   { max-width: 300px; }
    .gaps-table .mat-column-severity      { width: 90px; }
    .gaps-table .mat-column-risk          { width: 100px; }
    .gaps-table .mat-column-status        { width: 100px; }
    .gaps-table .mat-column-owner         { width: 120px; }
    .gaps-table .mat-column-due_date      { width: 110px; }
    .gaps-table .mat-column-actions       { width: 80px; text-align: right; white-space: nowrap; }

    /* ── action icons ── */
    .icon-sm  { font-size: 18px; height: 18px; width: 18px; }
    .btn-error { color: var(--mat-sys-error); }

    /* ── due date text ── */
    .due-date-text { font-size: 0.78rem; }

    /* ── card utilities ── */
    .card-mb          { margin-bottom: 16px; }
    .card-overflow    { overflow: hidden; }
    .card-content-pb  { padding-bottom: 12px !important; }

    /* ── alert margin utilities ── */
    .alert-mb    { margin-bottom: 16px; }
    .alert-mb-sm { margin-bottom: 12px; }

    /* ── inline editor wrapper ── */
    .editor-divider { border-top: 2px solid var(--mat-sys-outline-variant); }
    .editor-header  { padding: 4px 16px 0; background: var(--mat-sys-surface-container-low); }
    .group-code-sm  { font-size: 0.72rem; }
  `],
})
export class GapsComponent {
  private gapsApi      = inject(GapsApiService)
  private productSvc   = inject(ProductService)
  private projectSvc   = inject(ProjectService)
  private qc           = injectQueryClient()
  private dialog       = inject(MatDialog)

  readonly COLUMNS          = ['control_group', 'description', 'severity', 'risk', 'status', 'owner', 'due_date', 'actions']
  readonly SEVERITIES       = SEVERITIES
  readonly RISK_LEVEL_ORDER = ['VERY_HIGH', 'HIGH', 'MEDIUM', 'LOW'] as const

  statusSig   = signal('open')
  severitySig = signal('')
  editingId   = signal<string | null>(null)

  activeProject   = this.projectSvc.activeProject
  activeProjectId = this.projectSvc.activeProjectId
  product         = this.productSvc.product

  productFamilyParam = computed(() => this.product().toUpperCase())

  gapsQuery = injectQuery(() => ({
    queryKey: ['gaps', this.severitySig(), this.statusSig(), this.activeProjectId()],
    queryFn: () => firstValueFrom(this.gapsApi.list({
      severity:   this.severitySig() || undefined,
      status:     this.statusSig()   || undefined,
      project_id: this.activeProjectId() ?? undefined,
    })),
  }))

  gaps            = computed(() => this.gapsQuery.data() ?? [])
  totalCount      = computed(() => this.gaps().length)
  openCount       = computed(() => this.gaps().filter(g => g.status === 'open').length)
  inProgressCount = computed(() => this.gaps().filter(g => g.status === 'in_progress').length)
  criticalCount   = computed(() => this.gaps().filter(g => g.severity === 'critical').length)

  riskCounts = computed(() => {
    const counts: Record<string, number> = {}
    for (const gap of this.gaps()) {
      const lvl = gap.risk_level ?? 'unknown'
      counts[lvl] = (counts[lvl] ?? 0) + 1
    }
    return counts
  })

  editingGap = computed(() => {
    const id = this.editingId()
    return id ? (this.gaps().find(g => g.id === id) ?? null) : null
  })

  headerSubtitle = computed(() => {
    const proj  = this.activeProject()
    const total = this.totalCount()
    const open  = this.openCount()
    return proj
      ? `${proj.name} · ${total} gaps · ${open} open`
      : `${total} total gaps · ${open} open`
  })

  deleteMut = injectMutation(() => ({
    mutationFn: (id: string) => firstValueFrom(this.gapsApi.delete(id)),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['gaps'] })
    },
  }))

  toggleEdit(id: string): void {
    this.editingId.update(cur => (cur === id ? null : id))
  }

  openDeleteDialog(gap: GapRead): void {
    const ref = this.dialog.open(DeleteGapDialogComponent, {
      data: { gap } satisfies DeleteGapDialogData,
      width: '420px',
    })
    ref.afterClosed().subscribe((confirmed: boolean) => {
      if (confirmed) this.deleteMut.mutate(gap.id)
    })
  }

  openCreateDialog(): void {
    this.dialog.open(CreateGapDialogComponent, {
      data: {
        productFamily: this.productFamilyParam(),
        projectId: this.activeProjectId() ?? undefined,
      } satisfies CreateGapDialogData,
      width: '560px',
    })
  }

  isOverdue(gap: GapRead): boolean {
    if (!gap.due_date || gap.status === 'closed') return false
    return new Date(gap.due_date) < new Date()
  }

  riskColor(lvl: string): string { return RISK_COLOR[lvl] ?? '#888' }
  fmtDate(d: string): string    { return formatDate(d) }
  cap(s: string): string        { return capitalize(s) }
}
