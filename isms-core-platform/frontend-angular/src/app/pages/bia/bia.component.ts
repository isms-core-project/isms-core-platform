import { Component, inject, signal, computed } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'

import { injectQuery, injectMutation, injectQueryClient } from '@tanstack/angular-query-experimental'

import { MatButtonModule } from '@angular/material/button'
import { MatIconModule } from '@angular/material/icon'
import { MatSelectModule } from '@angular/material/select'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSliderModule } from '@angular/material/slider'
import { MatSlideToggleModule } from '@angular/material/slide-toggle'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatDialogModule, MatDialog } from '@angular/material/dialog'
import { Component as NgComponent } from '@angular/core'

import { BiaApiService, BIARecord, BIACreate } from '../../api/bia-api.service'
import { ProjectService } from '../../core/services/project.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

// ── Constants ─────────────────────────────────────────────────────────────────

const ASSET_TYPES = ['process', 'system', 'service', 'data']

const ASSET_TYPE_COLORS: Record<string, string> = {
  process: '#2196F3',
  system:  '#9C27B0',
  service: '#FF9800',
  data:    '#4CAF50',
}

const IMPACT_DIMS: { key: string; label: string }[] = [
  { key: 'financial_impact',    label: 'Financial impact' },
  { key: 'operational_impact',  label: 'Operational impact' },
  { key: 'reputational_impact', label: 'Reputational impact' },
  { key: 'regulatory_impact',   label: 'Regulatory impact' },
]

function impactColor(score: number): string {
  if (score <= 2) return '#4CAF50'
  if (score === 3) return '#FF9800'
  return '#F44336'
}

function capitalize(s: string): string {
  return s.charAt(0).toUpperCase() + s.slice(1)
}

function fmtDate(d: string | null): string {
  if (!d) return '—'
  return new Date(d).toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: '2-digit' })
}

// ── BIA Dialog ────────────────────────────────────────────────────────────────

@NgComponent({
  selector: 'app-bia-dialog',
  standalone: true,
  imports: [
    FormsModule,
    MatButtonModule, MatDialogModule, MatFormFieldModule,
    MatInputModule, MatSelectModule, MatSliderModule, MatSlideToggleModule, MatIconModule,
  ],
  template: `
    <h2 mat-dialog-title>{{ data.existing ? 'Edit BIA Record' : 'New BIA Record' }}</h2>
    <mat-dialog-content class="dlg-content">

      @if (error()) {
        <div class="dlg-error">{{ error() }}</div>
      }

      <div class="dlg-row">
        <mat-form-field appearance="outline" class="field-flex-2">
          <mat-label>Asset name *</mat-label>
          <input matInput [(ngModel)]="assetName" />
        </mat-form-field>
        <mat-form-field appearance="outline" class="field-flex-1">
          <mat-label>Type</mat-label>
          <mat-select [(ngModel)]="assetType">
            @for (t of assetTypes; track t) { <mat-option [value]="t">{{ capitalize(t) }}</mat-option> }
          </mat-select>
        </mat-form-field>
      </div>

      <!-- Recovery objectives -->
      <div class="dlg-section-label">
        Recovery objectives (hours)
      </div>
      <div class="dlg-row dlg-row-mb">
        <mat-form-field appearance="outline" class="field-flex-1">
          <mat-label>RTO</mat-label>
          <input matInput type="number" min="0" [(ngModel)]="rtoHours" />
        </mat-form-field>
        <mat-form-field appearance="outline" class="field-flex-1">
          <mat-label>RPO</mat-label>
          <input matInput type="number" min="0" [(ngModel)]="rpoHours" />
        </mat-form-field>
        <mat-form-field appearance="outline" class="field-flex-1">
          <mat-label>MTPD</mat-label>
          <input matInput type="number" min="0" [(ngModel)]="mtpdHours" />
        </mat-form-field>
      </div>

      <!-- Impact sliders -->
      <div class="dlg-section-label dlg-section-label-mb">
        Business impact (1 = low, 5 = critical)
      </div>
      @for (dim of impactDims; track dim.key) {
        <div class="dlg-impact-row">
          <span class="dlg-impact-label">{{ dim.label }}</span>
          <mat-slider min="1" max="5" step="1" discrete class="dlg-slider">
            <input matSliderThumb [ngModel]="impactValues[dim.key]" (ngModelChange)="impactValues[dim.key] = $event" />
          </mat-slider>
          <div [style]="impactBadgeStyle(impactValues[dim.key])">{{ impactValues[dim.key] }}</div>
        </div>
      }

      <!-- Recovery tested -->
      <div class="dlg-tested-row">
        <mat-slide-toggle [(ngModel)]="recoveryTested">
          <span class="dlg-toggle-label">Recovery tested</span>
        </mat-slide-toggle>
        @if (recoveryTested) {
          <mat-form-field appearance="outline" class="field-flex-1" subscriptSizing="dynamic">
            <mat-label>Last tested date</mat-label>
            <input matInput type="date" [(ngModel)]="lastTestedDate" />
          </mat-form-field>
        }
      </div>

      <mat-form-field appearance="outline" class="field-full">
        <mat-label>Continuity plan ref</mat-label>
        <input matInput [(ngModel)]="continuityPlanRef" />
      </mat-form-field>

      <mat-form-field appearance="outline" class="field-full">
        <mat-label>Notes</mat-label>
        <textarea matInput rows="2" [(ngModel)]="notes"></textarea>
      </mat-form-field>
    </mat-dialog-content>
    <mat-dialog-actions align="end">
      <button mat-button mat-dialog-close>Cancel</button>
      <button mat-raised-button color="primary" [disabled]="saving()" (click)="submit()">
        {{ saving() ? 'Saving…' : (data.existing ? 'Save' : 'Create') }}
      </button>
    </mat-dialog-actions>
  `,
  styles: [`
    .dlg-content { padding-top: 16px; min-width: 520px; display: flex; flex-direction: column; gap: 0; }
    .dlg-error { color: #f44336; font-size: 0.8rem; margin-bottom: 12px; padding: 8px 10px; background: rgba(244,67,54,0.08); border-radius: 4px; }
    .dlg-row { display: flex; gap: 12px; }
    .dlg-row-mb { margin-bottom: 8px; }
    .field-flex-1 { flex: 1; }
    .field-flex-2 { flex: 2; }
    .field-full { width: 100%; }
    .dlg-section-label { font-size: 0.65rem; font-weight: 700; text-transform: uppercase; color: var(--mat-sys-on-surface-variant); padding: 4px 0 8px; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 8px; }
    .dlg-section-label-mb { margin-bottom: 12px; }
    .dlg-impact-row { display: flex; align-items: center; gap: 16px; margin-bottom: 8px; }
    .dlg-impact-label { min-width: 160px; font-size: 0.75rem; color: var(--mat-sys-on-surface-variant); }
    .dlg-slider { flex: 1; }
    .dlg-tested-row { display: flex; align-items: center; gap: 16px; margin-bottom: 12px; }
    .dlg-toggle-label { font-size: 0.82rem; }
  `],
})
export class BiaDialogComponent {
  private api     = inject(BiaApiService)
  private qc      = injectQueryClient()
  readonly dialog = inject(MatDialog)

  data: { existing?: BIARecord; projectId?: string } = {}

  assetTypes  = ASSET_TYPES
  impactDims  = IMPACT_DIMS
  capitalize  = capitalize

  // Flat fields — set externally after open() or by ngOnInit
  assetName        = ''
  assetType        = 'process'
  rtoHours         = ''
  rpoHours         = ''
  mtpdHours        = ''
  recoveryTested   = false
  lastTestedDate   = ''
  continuityPlanRef = ''
  notes            = ''

  impactValues: Record<string, number> = {
    financial_impact: 3, operational_impact: 3,
    reputational_impact: 3, regulatory_impact: 3,
  }

  error  = signal('')
  saving = signal(false)

  impactBadgeStyle(val: number): string {
    const color = impactColor(val)
    return `width:24px;height:24px;border-radius:50%;background:${color};display:flex;align-items:center;justify-content:center;font-size:0.65rem;font-weight:700;color:#fff;flex-shrink:0`
  }

  async submit() {
    if (!this.assetName.trim()) { this.error.set('Asset name is required.'); return }
    this.error.set('')
    this.saving.set(true)
    const body: BIACreate = {
      asset_name:          this.assetName,
      asset_type:          this.assetType,
      project_id:          this.data.projectId,
      rto_hours:           this.rtoHours  ? Number(this.rtoHours)  : undefined,
      rpo_hours:           this.rpoHours  ? Number(this.rpoHours)  : undefined,
      mtpd_hours:          this.mtpdHours ? Number(this.mtpdHours) : undefined,
      financial_impact:    this.impactValues['financial_impact'],
      operational_impact:  this.impactValues['operational_impact'],
      reputational_impact: this.impactValues['reputational_impact'],
      regulatory_impact:   this.impactValues['regulatory_impact'],
      recovery_tested:     this.recoveryTested,
      last_tested_date:    this.lastTestedDate    || undefined,
      continuity_plan_ref: this.continuityPlanRef || undefined,
      notes:               this.notes             || undefined,
    }
    try {
      if (this.data.existing) {
        await firstValueFrom(this.api.update(this.data.existing.id, body))
      } else {
        await firstValueFrom(this.api.create(body))
      }
      this.qc.invalidateQueries({ queryKey: ['bia'] })
      this.qc.invalidateQueries({ queryKey: ['bia-summary'] })
      this.dialog.closeAll()
    } catch {
      this.error.set('Failed to save.')
    } finally {
      this.saving.set(false)
    }
  }
}

// ── Main Component ────────────────────────────────────────────────────────────

@Component({
  selector: 'app-bia',
  standalone: true,
  imports: [
    FormsModule,
    MatButtonModule, MatIconModule, MatSelectModule,
    MatFormFieldModule, MatInputModule, MatTooltipModule,
    PageHeaderComponent,
  ],
  template: `
    <app-page-header
      title="Business Impact Analysis"
      [subtitle]="headerSubtitle()">
      <div actions>
        <button mat-raised-button color="primary"
          [disabled]="!projectService.activeProject()"
          [matTooltip]="!projectService.activeProject() ? 'Select a project first to create BIA records' : ''"
          (click)="openCreate()">
          <mat-icon>add</mat-icon>
          New Record
        </button>
      </div>
    </app-page-header>

    @if (projectService.activeProject()) {
      <div class="project-banner">
        Showing BIA records for project: <strong>{{ projectService.activeProject()!.name }}</strong>
      </div>
    }

    <!-- Summary cards -->
    <div class="summary-cards">
      @for (c of summaryCards(); track c.label) {
        <div [style.border-color]="c.color + '30'" [style.background]="c.color + '08'" class="summary-card">
          @if (summaryQ.isLoading()) {
            <div class="skel-value"></div>
          } @else {
            <div [style.color]="c.color" class="summary-value">{{ c.value }}</div>
          }
          <div class="summary-label">{{ c.label }}</div>
        </div>
      }
    </div>

    <!-- Filter -->
    <div class="filter-row">
      <mat-form-field appearance="outline" class="filter-select" subscriptSizing="dynamic">
        <mat-label>Asset type</mat-label>
        <mat-select [(ngModel)]="typeFilter" (ngModelChange)="typeFilter = $event">
          <mat-option value="">All types</mat-option>
          @for (t of assetTypes; track t) { <mat-option [value]="t">{{ capitalize(t) }}</mat-option> }
        </mat-select>
      </mat-form-field>
      @if (typeFilter) {
        <button mat-button (click)="typeFilter = ''" class="clear-btn">Clear</button>
      }
      <span class="record-count">
        {{ (biaQ.data() ?? []).length }} record{{ (biaQ.data() ?? []).length !== 1 ? 's' : '' }}
      </span>
    </div>

    <!-- Table header -->
    <div class="tbl-header">
      <span class="col-asset-hdr">Asset / Plan</span>
      <span class="col-type-hdr">Type</span>
      <span class="col-rto-hdr">RTO</span>
      <span class="col-rpo-hdr">RPO</span>
      <span class="col-impact-hdr">Impact</span>
      <span class="col-tested-hdr">Tested</span>
      <span class="col-actions-hdr"></span>
    </div>

    <div class="tbl-body">
      @if (biaQ.isLoading()) {
        @for (i of [0,1,2,3]; track i) {
          <div class="skel-row">
            <div class="skel-row-inner"></div>
          </div>
        }
      } @else if (!biaQ.data() || biaQ.data()!.length === 0) {
        <div class="empty-state">
          <div class="empty-msg">
            {{ projectService.activeProject() ? 'No BIA records yet.' : 'Select a project to create BIA records.' }}
          </div>
          @if (projectService.activeProject()) {
            <button mat-stroked-button class="empty-create-btn" (click)="openCreate()">
              <mat-icon>add</mat-icon> Create first record
            </button>
          }
        </div>
      } @else {
        @for (r of biaQ.data()!; track r.id) {
          <div class="tbl-row">

            <!-- Asset name -->
            <div class="col-asset">
              <div class="asset-name">{{ r.asset_name }}</div>
              @if (r.continuity_plan_ref) {
                <div class="asset-plan">Plan: {{ r.continuity_plan_ref }}</div>
              }
            </div>

            <!-- Type chip -->
            <div class="col-type">
              <span [style]="typeChipStyle(r.asset_type)">{{ capitalize(r.asset_type) }}</span>
            </div>

            <!-- RTO -->
            <div class="col-rto"
                 [style.color]="r.rto_hours == null ? 'var(--mat-sys-on-surface-variant)' : '#FF9800'">
              {{ r.rto_hours != null ? r.rto_hours + 'h' : '—' }}
            </div>

            <!-- RPO -->
            <div class="col-rpo">
              {{ r.rpo_hours != null ? r.rpo_hours + 'h' : '—' }}
            </div>

            <!-- Impact -->
            <div class="col-impact">
              @if (r.avg_impact != null) {
                <span [matTooltip]="'Avg impact: ' + r.avg_impact.toFixed(1) + ' / 5'"
                      class="impact-cell">
                  <span [style]="impactDotStyle(r.avg_impact)"></span>
                  <span [style.color]="impactColor(r.avg_impact)" class="impact-val">{{ r.avg_impact.toFixed(1) }}</span>
                </span>
              } @else {
                <span class="dash-muted">—</span>
              }
            </div>

            <!-- Recovery tested -->
            <div class="col-tested">
              @if (r.recovery_tested) {
                <span [matTooltip]="r.last_tested_date ? 'Tested ' + fmtDate(r.last_tested_date) : 'Tested'"
                      class="tested-yes">
                  <mat-icon class="icon-md">check_circle</mat-icon>
                </span>
              } @else {
                <span class="tested-no"></span>
              }
            </div>

            <!-- Actions -->
            <div class="col-actions">
              <button mat-icon-button class="btn-sm" (click)="openEdit(r)">
                <mat-icon class="icon-sm">edit</mat-icon>
              </button>
              <button mat-icon-button class="btn-sm btn-danger" (click)="deleteRecord(r)">
                <mat-icon class="icon-sm">delete</mat-icon>
              </button>
            </div>
          </div>
        }
      }
    </div>
  `,
  styles: [`
    :host { display: block; padding: 24px; }

    /* Project banner */
    .project-banner { margin-top: 16px; margin-bottom: 16px; padding: 8px 12px; border-radius: 6px; font-size: 0.8rem; background: rgba(68,114,196,0.1); border: 1px solid rgba(68,114,196,0.25); }

    /* Summary cards */
    .summary-cards { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 20px; }
    .summary-card { min-width: 100px; padding: 12px; border-radius: 6px; border: 1px solid; }
    .skel-value { width: 32px; height: 28px; background: rgba(255,255,255,0.06); border-radius: 4px; }
    .summary-value { font-size: 1.4rem; font-weight: 700; line-height: 1; }
    .summary-label { font-size: 0.65rem; color: var(--mat-sys-on-surface-variant); }

    /* Filter row */
    .filter-row { display: flex; gap: 12px; margin-bottom: 16px; align-items: center; }
    .filter-select { min-width: 160px; }
    .clear-btn { font-size: 0.75rem; }
    .record-count { margin-left: auto; font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }

    /* Table header */
    .tbl-header { display: flex; align-items: center; gap: 8px; padding: 6px 16px; background: var(--mat-sys-surface-variant); border-radius: 8px 8px 0 0; border: 1px solid var(--mat-sys-outline-variant); border-bottom: none; }
    .col-asset-hdr  { flex: 3; font-size: 0.68rem; font-weight: 600; color: var(--mat-sys-on-surface-variant); text-transform: uppercase; }
    .col-type-hdr   { width: 80px; font-size: 0.68rem; font-weight: 600; color: var(--mat-sys-on-surface-variant); text-transform: uppercase; }
    .col-rto-hdr    { width: 60px; text-align: center; font-size: 0.68rem; font-weight: 600; color: var(--mat-sys-on-surface-variant); text-transform: uppercase; }
    .col-rpo-hdr    { width: 60px; text-align: center; font-size: 0.68rem; font-weight: 600; color: var(--mat-sys-on-surface-variant); text-transform: uppercase; }
    .col-impact-hdr { width: 70px; text-align: center; font-size: 0.68rem; font-weight: 600; color: var(--mat-sys-on-surface-variant); text-transform: uppercase; }
    .col-tested-hdr { width: 80px; text-align: center; font-size: 0.68rem; font-weight: 600; color: var(--mat-sys-on-surface-variant); text-transform: uppercase; }
    .col-actions-hdr { width: 56px; }

    /* Table body */
    .tbl-body { border: 1px solid rgba(255,255,255,0.08); border-radius: 0 0 8px 8px; overflow: hidden; }
    .skel-row { padding: 12px 16px; border-bottom: 1px solid rgba(255,255,255,0.06); }
    .skel-row-inner { height: 20px; background: rgba(255,255,255,0.06); border-radius: 4px; }
    .empty-state { padding: 48px; text-align: center; }
    .empty-msg { font-size: 0.9rem; color: var(--mat-sys-on-surface-variant); }
    .empty-create-btn { margin-top: 12px; }

    /* Table rows */
    .tbl-row { display: flex; align-items: center; gap: 8px; padding: 10px 16px; border-bottom: 1px solid rgba(255,255,255,0.06); }
    .col-asset { flex: 3; min-width: 0; }
    .asset-name { font-weight: 500; font-size: 0.82rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
    .asset-plan { font-size: 0.65rem; color: var(--mat-sys-on-surface-variant); }
    .col-type { width: 80px; }
    .col-rto { width: 60px; text-align: center; font-size: 0.72rem; }
    .col-rpo { width: 60px; text-align: center; font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
    .col-impact { width: 70px; text-align: center; }
    .impact-cell { display: inline-flex; align-items: center; gap: 4px; }
    .impact-val { font-size: 0.7rem; font-weight: 600; }
    .dash-muted { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
    .col-tested { width: 80px; text-align: center; }
    .tested-yes { color: #4CAF50; display: inline-flex; }
    .tested-no { display: inline-block; width: 16px; height: 16px; border-radius: 50%; background: rgba(255,255,255,0.08); }
    .col-actions { display: flex; gap: 2px; width: 56px; justify-content: flex-end; }
    .btn-sm { width: 28px; height: 28px; }
    .btn-danger { color: var(--mat-sys-error); }
  `],
})
export class BiaComponent {
  readonly projectService = inject(ProjectService)
  private api    = inject(BiaApiService)
  private dialog = inject(MatDialog)
  private qc     = injectQueryClient()

  assetTypes  = ASSET_TYPES
  capitalize  = capitalize
  fmtDate     = fmtDate
  impactColor = impactColor

  typeFilter = ''

  headerSubtitle = computed(() => {
    const p = this.projectService.activeProject()
    return p
      ? `${p.name} · RTO/RPO modelling — ISO 27001:2022 §A.5.29`
      : 'RTO/RPO modelling and continuity planning — ISO 27001:2022 §A.5.29'
  })

  // ── Queries ───────────────────────────────────────────────────────────────

  summaryQ = injectQuery(() => ({
    queryKey: ['bia-summary', this.projectService.activeProjectId()],
    queryFn:  () => firstValueFrom(this.api.summary({ project_id: this.projectService.activeProjectId() ?? undefined })),
  }))

  biaQ = injectQuery(() => ({
    queryKey: ['bia', this.typeFilter, this.projectService.activeProjectId()],
    queryFn:  () => firstValueFrom(this.api.list({
      project_id: this.projectService.activeProjectId() ?? undefined,
      ...(this.typeFilter ? { asset_type: this.typeFilter } : {}),
    })),
  }))

  // ── Mutation ──────────────────────────────────────────────────────────────

  deleteMut = injectMutation(() => ({
    mutationFn: (id: string) => firstValueFrom(this.api.delete(id)),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['bia'] })
      this.qc.invalidateQueries({ queryKey: ['bia-summary'] })
    },
  }))

  // ── Summary cards ─────────────────────────────────────────────────────────

  summaryCards = computed(() => {
    const d = this.summaryQ.data()
    return [
      { label: 'Total Assets',    value: d?.total ?? 0,                                              color: '#607D8B' },
      { label: 'Recovery Tested', value: d?.tested_pct != null ? `${Math.round(d.tested_pct)}%` : 0, color: '#4CAF50' },
      { label: 'High Impact',     value: d?.high_impact ?? 0,                                         color: '#F44336' },
      { label: 'RTO Missing',     value: d?.rto_missing ?? 0,                                         color: '#FF9800' },
    ]
  })

  // ── Actions ───────────────────────────────────────────────────────────────

  openCreate() {
    const ref = this.dialog.open(BiaDialogComponent, { maxWidth: '580px', width: '100%' })
    ref.componentInstance.data = { projectId: this.projectService.activeProjectId() ?? undefined }
    ref.componentInstance.assetName = ''
    ref.componentInstance.assetType = 'process'
    ref.componentInstance.rtoHours = ''
    ref.componentInstance.rpoHours = ''
    ref.componentInstance.mtpdHours = ''
    ref.componentInstance.recoveryTested = false
    ref.componentInstance.lastTestedDate = ''
    ref.componentInstance.continuityPlanRef = ''
    ref.componentInstance.notes = ''
    ref.componentInstance.impactValues = { financial_impact: 3, operational_impact: 3, reputational_impact: 3, regulatory_impact: 3 }
    ref.componentInstance.error.set('')
  }

  openEdit(r: BIARecord) {
    const ref = this.dialog.open(BiaDialogComponent, { maxWidth: '580px', width: '100%' })
    ref.componentInstance.data = { existing: r, projectId: r.project_id ?? undefined }
    ref.componentInstance.assetName = r.asset_name
    ref.componentInstance.assetType = r.asset_type
    ref.componentInstance.rtoHours  = r.rto_hours  != null ? String(r.rto_hours)  : ''
    ref.componentInstance.rpoHours  = r.rpo_hours  != null ? String(r.rpo_hours)  : ''
    ref.componentInstance.mtpdHours = r.mtpd_hours != null ? String(r.mtpd_hours) : ''
    ref.componentInstance.recoveryTested   = r.recovery_tested
    ref.componentInstance.lastTestedDate   = r.last_tested_date ?? ''
    ref.componentInstance.continuityPlanRef = r.continuity_plan_ref ?? ''
    ref.componentInstance.notes            = r.notes ?? ''
    ref.componentInstance.impactValues = {
      financial_impact:    r.financial_impact    ?? 3,
      operational_impact:  r.operational_impact  ?? 3,
      reputational_impact: r.reputational_impact ?? 3,
      regulatory_impact:   r.regulatory_impact   ?? 3,
    }
    ref.componentInstance.error.set('')
  }

  deleteRecord(r: BIARecord) {
    if (!confirm(`Delete "${r.asset_name}"?`)) return
    this.deleteMut.mutate(r.id)
  }

  // ── Style helpers ──────────────────────────────────────────────────────────

  typeChipStyle(type: string): string {
    const color = ASSET_TYPE_COLORS[type] ?? '#607D8B'
    return `font-size:0.62rem;font-weight:700;padding:2px 6px;border-radius:10px;background:${color}18;color:${color};border:1px solid ${color}40`
  }

  impactDotStyle(score: number): string {
    const color = impactColor(score)
    return `width:8px;height:8px;border-radius:50%;background:${color};display:inline-block`
  }
}
