import { Component, inject, signal, computed } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'
import { injectQuery, injectMutation, injectQueryClient } from '@tanstack/angular-query-experimental'

import { MatCardModule } from '@angular/material/card'
import { MatTableModule } from '@angular/material/table'
import { MatButtonModule } from '@angular/material/button'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatDialogModule } from '@angular/material/dialog'
import { MatIconModule } from '@angular/material/icon'
import { MatChipsModule } from '@angular/material/chips'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatProgressBarModule } from '@angular/material/progress-bar'
import { MatTabsModule } from '@angular/material/tabs'
import { MatSnackBar, MatSnackBarModule } from '@angular/material/snack-bar'

import {
  RisksApiService,
  type RemediationAction,
  type RemediationActionCreate,
  type PoamItem,
} from '../../api/risks-api.service'
import { ProjectService } from '../../core/services/project.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

// ── Helpers ───────────────────────────────────────────────────────────────────

interface StatusMeta { label: string; color: string; icon: string }

const STATUS_META: Record<string, StatusMeta> = {
  planned:     { label: 'Planned',     color: '#9E9E9E', icon: 'schedule' },
  in_progress: { label: 'In Progress', color: '#2196F3', icon: 'hourglass_empty' },
  completed:   { label: 'Completed',   color: '#4CAF50', icon: 'check_circle' },
  cancelled:   { label: 'Cancelled',   color: '#F44336', icon: 'error' },
}

const EFFORT_COLOR: Record<string, string> = {
  low:    '#4CAF50',
  medium: '#FF9800',
  high:   '#F44336',
}

const SOURCE_META: Record<string, { label: string; color: string }> = {
  risk: { label: 'Risk', color: '#F44336' },
  gap:  { label: 'Gap',  color: '#FF9800' },
  tprm: { label: 'TPRM', color: '#9C27B0' },
}

function isOverdue(action: RemediationAction): boolean {
  return !!(action.eta &&
    new Date(action.eta) < new Date() &&
    !['completed', 'cancelled'].includes(action.status))
}

function fmtDate(d: string | null | undefined): string {
  if (!d) return '—'
  return new Date(d).toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: '2-digit' })
}

// ── Component ─────────────────────────────────────────────────────────────────

@Component({
  selector: 'app-remediation',
  standalone: true,
  imports: [
    FormsModule,
    MatCardModule, MatTableModule, MatButtonModule, MatFormFieldModule,
    MatInputModule, MatSelectModule, MatDialogModule, MatIconModule,
    MatChipsModule, MatTooltipModule, MatProgressBarModule,
    MatTabsModule, MatSnackBarModule,
    PageHeaderComponent,
  ],
  template: `
<app-page-header
  title="Remediation Tracker"
  subtitle="Plan of Action and Milestones (POA&M) — ISO 27001:2022 §6.1.3">
  <div actions>
    @if (activeTab() === 0) {
      <button mat-flat-button color="primary"
        [disabled]="!project.activeProject()"
        [matTooltip]="!project.activeProject() ? 'Select a project first' : ''"
        (click)="openCreate()">
        <mat-icon>add</mat-icon>
        New Action
      </button>
    }
  </div>
</app-page-header>

<mat-tab-group [selectedIndex]="activeTab()" (selectedIndexChange)="activeTab.set($event)">

  <!-- ── TAB 0: Risk Treatments ─────────────────────────────────────────────── -->
  <mat-tab label="Risk Treatments">
    <div class="tab-content">

      @if (project.activeProject()) {
        <div class="alert alert-info">
          Showing actions for project: <strong>{{ project.activeProject()!.name }}</strong>
        </div>
      }

      <!-- Summary cards -->
      @if (summaryQuery.isSuccess() && summaryQuery.data()) {
        @let s = summaryQuery.data()!;
        <div class="summary-row">
          @for (card of remediationSummaryCards(s); track card.label) {
            <div class="summary-card" [style.border-color]="card.color + '30'" [style.background]="card.color + '08'">
              <div class="sc-value" [style.color]="card.color">{{ card.value }}</div>
              <div class="sc-label">{{ card.label }}</div>
            </div>
          }
        </div>
      }

      <!-- Filters -->
      <div class="filter-row">
        <mat-form-field appearance="outline" subscriptSizing="dynamic" class="filter-field">
          <mat-label>Status</mat-label>
          <mat-select [(ngModel)]="statusFilter">
            <mat-option value="">All statuses</mat-option>
            @for (e of statusEntries; track e.k) {
              <mat-option [value]="e.k">{{ e.v.label }}</mat-option>
            }
          </mat-select>
        </mat-form-field>
        @if (statusFilter) {
          <button mat-button class="filter-clear-btn" (click)="statusFilter = ''">Clear</button>
        }
        @if (actionsQuery.isSuccess()) {
          <span class="count-label">{{ actions().length }} action{{ actions().length !== 1 ? 's' : '' }}</span>
        }
      </div>

      <!-- Table header -->
      <div class="action-table-header">
        <span class="th th-title-risk">Title / Risk</span>
        <span class="th th-progress">Progress</span>
        <span class="th th-status">Status</span>
        <span class="th th-effort">Effort</span>
        <span class="th th-eta">ETA</span>
        <span class="th th-actions-col"></span>
      </div>

      <!-- Rows -->
      <div class="action-table-body">
        @if (actionsQuery.isLoading()) {
          @for (i of [0,1,2,3]; track i) {
            <div class="action-row">
              <div class="skeleton skeleton-row-item"></div>
            </div>
          }
        } @else if (!actions().length) {
          <div class="empty-state">
            <mat-icon>task_alt</mat-icon>
            <div>
              <p>{{ project.activeProject() ? 'No remediation actions yet.' : 'Select a project to create remediation actions.' }}</p>
              @if (project.activeProject()) {
                <button mat-stroked-button class="create-first-btn" (click)="openCreate()">
                  <mat-icon>add</mat-icon> Create first action
                </button>
              }
            </div>
          </div>
        } @else {
          @for (action of actions(); track action.id) {
            <div class="action-row" [class.action-overdue]="isOverdue(action)">
              <!-- Title + risk link -->
              <div class="action-title-col">
                <span class="action-title" [class.text-error]="isOverdue(action)">{{ action.title }}</span>
                @if (action.risk_name) {
                  <span class="dim-sm">Risk: {{ action.risk_name }}</span>
                }
              </div>

              <!-- Progress bar -->
              <div class="action-progress-col">
                <mat-progress-bar mode="determinate" [value]="action.progress"
                  [style.--mat-progress-bar-active-indicator-color]="statusMeta(action.status).color" />
                <span class="progress-pct">{{ action.progress }}%</span>
              </div>

              <!-- Status chip -->
              <div class="col-status">
                <span class="chip"
                  [style.background]="statusMeta(action.status).color + '18'"
                  [style.color]="statusMeta(action.status).color"
                  [style.border]="'1px solid ' + statusMeta(action.status).color + '40'">
                  <mat-icon class="chip-icon">{{ statusMeta(action.status).icon }}</mat-icon>
                  {{ statusMeta(action.status).label }}
                </span>
              </div>

              <!-- Effort -->
              @if (action.effort) {
                <span class="chip col-effort"
                  [style.background]="effortColor(action.effort) + '18'"
                  [style.color]="effortColor(action.effort)"
                  [style.border]="'1px solid ' + effortColor(action.effort) + '40'">
                  {{ action.effort }}
                </span>
              } @else {
                <div class="col-effort-spacer"></div>
              }

              <!-- ETA -->
              <div class="col-eta">
                @if (action.eta) {
                  <span class="dim-sm" [class.text-error]="isOverdue(action)" [class.fw600]="isOverdue(action)">
                    @if (isOverdue(action)) { <mat-icon class="chip-icon">warning_amber</mat-icon> }
                    {{ fmtDate(action.eta) }}
                  </span>
                }
              </div>

              <!-- Actions -->
              <div class="col-row-actions">
                <button mat-icon-button matTooltip="Edit" (click)="openEdit(action)">
                  <mat-icon class="icon-sm">edit</mat-icon>
                </button>
                <button mat-icon-button matTooltip="Delete" color="warn"
                  (click)="deleteAction(action)">
                  <mat-icon class="icon-sm">delete</mat-icon>
                </button>
              </div>
            </div>
          }
        }
      </div>
    </div>
  </mat-tab>

  <!-- ── TAB 1: All Sources (POA&M) ───────────────────────────────────────── -->
  <mat-tab label="All Sources (POA&amp;M)">
    <div class="tab-content">

      <!-- POAM summary cards -->
      @if (poamSummaryQuery.isSuccess() && poamSummaryQuery.data()) {
        @let ps = poamSummaryQuery.data()!;
        <div class="summary-row">
          @for (card of poamSummaryCards(ps); track card.label) {
            <div class="summary-card" [style.border-color]="card.color + '30'" [style.background]="card.color + '08'">
              <div class="sc-value" [style.color]="card.color">{{ card.value }}</div>
              <div class="sc-label">{{ card.label }}</div>
            </div>
          }
        </div>
      }

      <!-- Source filter chips -->
      <div class="source-filter-row">
        @for (s of sourceFilters; track s.value) {
          <span class="filter-chip"
            [class.filter-chip--active]="poamSourceFilter() === s.value"
            (click)="poamSourceFilter.set(s.value)">
            {{ s.label }}
          </span>
        }
        @if (poamQuery.isSuccess()) {
          <span class="count-label count-label-right">
            {{ poamQuery.data()!.length }} item{{ poamQuery.data()!.length !== 1 ? 's' : '' }}
          </span>
        }
      </div>

      <!-- POAM table header -->
      <div class="poam-table-header">
        <span class="th poam-th-source">Source</span>
        <span class="th poam-th-title">Title</span>
        <span class="th poam-th-control">Control</span>
        <span class="th poam-th-status">Status</span>
        <span class="th poam-th-priority">Priority</span>
        <span class="th poam-th-eta">ETA</span>
      </div>

      <div class="poam-table-body">
        @if (poamQuery.isLoading()) {
          @for (i of [0,1,2,3]; track i) {
            <div class="poam-row">
              <div class="skeleton skeleton-poam-item"></div>
            </div>
          }
        } @else if (!poamQuery.data()?.length) {
          <div class="empty-state">
            <mat-icon>check_circle</mat-icon>
            <p>No open items.</p>
          </div>
        } @else {
          @for (item of poamQuery.data()!; track item.source + item.id) {
            <div class="poam-row" [class.action-overdue]="item.is_overdue">
              <span class="chip source-chip"
                [style.background]="sourceColor(item.source) + '18'"
                [style.color]="sourceColor(item.source)"
                [style.border]="'1px solid ' + sourceColor(item.source) + '40'">
                {{ sourceLabel(item.source) }}
              </span>

              <div class="poam-title-col">
                <span class="action-title" [class.text-error]="item.is_overdue">{{ item.title }}</span>
                @if (item.description) {
                  <span class="dim-sm ellipsis">{{ item.description }}</span>
                }
              </div>

              @if (item.control_code) {
                <span class="chip chip-neutral poam-control-chip">
                  {{ item.control_code }}
                </span>
              } @else {
                <div class="poam-col-control-spacer"></div>
              }

              <div class="poam-col-status">
                <span class="body-sm">{{ item.status.replace('_', ' ') }}</span>
              </div>

              <div class="poam-col-priority">
                @if (item.severity) {
                  <span class="dim-sm">{{ item.severity }}</span>
                }
              </div>

              <div class="poam-col-eta">
                @if (item.eta) {
                  <span class="dim-sm" [class.text-error]="item.is_overdue" [class.fw600]="item.is_overdue">
                    @if (item.is_overdue) {
                      <mat-icon class="chip-icon">warning_amber</mat-icon>
                    }
                    {{ fmtDate(item.eta) }}
                  </span>
                }
              </div>
            </div>
          }
        }
      </div>
    </div>
  </mat-tab>

</mat-tab-group>

<!-- ── Create / Edit dialog ───────────────────────────────────────────────── -->
@if (dialogOpen()) {
  <div class="dialog-backdrop" (click)="dialogOpen.set(false)">
    <mat-card class="dialog-card" (click)="$event.stopPropagation()">
      <mat-card-header>
        <mat-card-title>{{ editingAction() ? 'Edit Action' : 'New Remediation Action' }}</mat-card-title>
      </mat-card-header>
      <mat-card-content>
        @if (formError()) { <div class="alert alert-error">{{ formError() }}</div> }

        <div class="form-grid">
          <mat-form-field appearance="outline" class="full">
            <mat-label>Title *</mat-label>
            <input matInput [(ngModel)]="form.title" />
          </mat-form-field>
          <mat-form-field appearance="outline" class="full">
            <mat-label>Description</mat-label>
            <textarea matInput [(ngModel)]="form.description" rows="2"></textarea>
          </mat-form-field>
          <mat-form-field appearance="outline">
            <mat-label>Status</mat-label>
            <mat-select [(ngModel)]="form.status">
              @for (e of statusEntries; track e.k) {
                <mat-option [value]="e.k">{{ e.v.label }}</mat-option>
              }
            </mat-select>
          </mat-form-field>
          <mat-form-field appearance="outline">
            <mat-label>Effort</mat-label>
            <mat-select [(ngModel)]="form.effort">
              <mat-option value="">—</mat-option>
              <mat-option value="low">Low</mat-option>
              <mat-option value="medium">Medium</mat-option>
              <mat-option value="high">High</mat-option>
            </mat-select>
          </mat-form-field>
          <mat-form-field appearance="outline">
            <mat-label>Target date</mat-label>
            <input matInput type="date" [(ngModel)]="form.eta" />
          </mat-form-field>
          <mat-form-field appearance="outline">
            <mat-label>Progress %</mat-label>
            <input matInput type="number" min="0" max="100" [(ngModel)]="form.progress" />
          </mat-form-field>
        </div>
      </mat-card-content>
      <mat-card-actions>
        <button mat-button (click)="dialogOpen.set(false)">Cancel</button>
        <button mat-flat-button color="primary"
          [disabled]="saveMut.isPending()"
          (click)="submitAction()">
          {{ saveMut.isPending() ? 'Saving…' : (editingAction() ? 'Save' : 'Create') }}
        </button>
      </mat-card-actions>
    </mat-card>
  </div>
}
  `,
  styles: [`
    :host { display: block; padding: 24px; }

    .tab-content { padding: 20px 0; }

    .alert { padding: 10px 14px; border-radius: 6px; margin-bottom: 14px; font-size: 0.85rem; }
    .alert-info  { background: rgba(21,101,192,0.12); color: #9fc8f0; }
    .alert-error { background: rgba(192,0,0,0.12);   color: #FFC7CE; }

    .summary-row { display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 20px; }
    .summary-card {
      min-width: 90px; padding: 10px 14px;
      border: 1px solid; border-radius: 10px;
    }
    .sc-value { font-size: 1.4rem; font-weight: 700; line-height: 1; }
    .sc-label  { font-size: 0.65rem; color: var(--mat-sys-on-surface-variant); margin-top: 2px; }

    .filter-row { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; margin-bottom: 14px; }
    .filter-field { min-width: 150px; }
    .filter-clear-btn { font-size: 0.75rem; }
    .count-label { font-size: 0.78rem; color: var(--mat-sys-on-surface-variant); }
    .count-label-right { margin-left: auto; }

    /* Action table */
    .action-table-header {
      display: flex; align-items: center; gap: 8px;
      padding: 6px 16px;
      background: rgba(255,255,255,0.03);
      border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 8px 8px 0 0; border-bottom: none;
    }
    .th {
      font-size: 0.7rem; text-transform: uppercase;
      letter-spacing: 0.06em; color: var(--mat-sys-on-surface-variant); font-weight: 600;
    }
    .th-title-risk { flex: 3; }
    .th-progress { flex: 1.5; }
    .th-status { flex: 1; }
    .th-effort { width: 52px; }
    .th-eta { width: 80px; text-align: right; }
    .th-actions-col { width: 80px; }

    .action-table-body {
      border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 0 0 8px 8px; overflow: hidden;
    }
    .action-row {
      display: flex; align-items: center; gap: 8px;
      padding: 10px 16px;
      border-bottom: 1px solid var(--mat-sys-outline-variant);
    }
    .action-row:last-child { border-bottom: none; }
    .action-row:hover { background: rgba(255,255,255,0.02); }
    .action-overdue { background: rgba(244,67,54,0.04) !important; }

    .action-title-col { flex: 3; min-width: 0; display: flex; flex-direction: column; }
    .action-title { font-size: 0.82rem; font-weight: 500; }
    .action-progress-col { flex: 1.5; display: flex; align-items: center; gap: 8px; }
    .progress-pct { font-size: 0.65rem; color: var(--mat-sys-on-surface-variant); min-width: 28px; }

    .col-status { flex: 1; }
    .col-effort { width: 52px; text-align: center; }
    .col-effort-spacer { width: 52px; }
    .col-eta { width: 80px; text-align: right; }
    .col-row-actions { width: 80px; display: flex; gap: 2px; justify-content: flex-end; }
    .create-first-btn { margin-top: 12px; }

    /* Skeleton */
    .skeleton-row-item { width: 55%; height: 14px; border-radius: 3px; flex: 3; }
    .skeleton-poam-item { width: 60%; height: 14px; border-radius: 3px; }

    /* POAM */
    .source-filter-row { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 14px; align-items: center; }
    .filter-chip {
      padding: 4px 12px; border-radius: 14px; font-size: 0.75rem; cursor: pointer;
      border: 1px solid var(--mat-sys-outline-variant);
      transition: background 0.15s;
    }
    .filter-chip--active {
      background: rgba(68,114,196,0.18); color: #93bbf5;
      border-color: rgba(68,114,196,0.4); font-weight: 700;
    }

    .poam-table-header {
      display: flex; align-items: center; gap: 8px;
      padding: 6px 16px;
      background: rgba(255,255,255,0.03);
      border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 8px 8px 0 0; border-bottom: none;
    }
    .poam-th-source { width: 40px; }
    .poam-th-title { flex: 3; }
    .poam-th-control { width: 60px; }
    .poam-th-status { width: 80px; }
    .poam-th-priority { width: 60px; }
    .poam-th-eta { width: 80px; text-align: right; }

    .poam-table-body {
      border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 0 0 8px 8px; overflow: hidden;
    }
    .poam-row {
      display: flex; align-items: center; gap: 8px;
      padding: 10px 16px;
      border-bottom: 1px solid var(--mat-sys-outline-variant);
    }
    .poam-row:last-child { border-bottom: none; }
    .poam-row:hover { background: rgba(255,255,255,0.02); }
    .poam-title-col { flex: 3; min-width: 0; display: flex; flex-direction: column; }
    .poam-control-chip { width: 60px; text-align: center; font-family: monospace; }
    .poam-col-control-spacer { width: 60px; }
    .poam-col-status { width: 80px; }
    .poam-col-priority { width: 60px; }
    .poam-col-eta { width: 80px; text-align: right; }

    /* Chips */
    .chip {
      display: inline-flex; align-items: center;
      padding: 2px 7px; border-radius: 10px;
      font-size: 0.62rem; font-weight: 600; line-height: 1.6;
    }
    .chip-icon { font-size: 11px; vertical-align: middle; margin-right: 2px; }
    .chip-neutral { background: rgba(255,255,255,0.07); color: #d9d9d9; }
    .source-chip { min-width: 40px; justify-content: center; }

    .text-error { color: var(--mat-sys-error) !important; }
    .fw600 { font-weight: 600; }
    .dim-sm { font-size: 0.65rem; color: var(--mat-sys-on-surface-variant); }
    .body-sm { font-size: 0.78rem; }
    .ellipsis { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; display: block; }
    .skeleton { background: rgba(255,255,255,0.06); }

    .empty-state {
      display: flex; align-items: center; gap: 16px;
      padding: 48px 32px; color: var(--mat-sys-on-surface-variant);
      justify-content: center; text-align: center; flex-direction: column;
    }
    .empty-state mat-icon { font-size: 36px; width: 36px; height: 36px; }
    .empty-state p { margin: 4px 0; }

    /* Dialog */
    .dialog-backdrop {
      position: fixed; inset: 0; background: rgba(0,0,0,0.5);
      display: flex; align-items: center; justify-content: center;
      z-index: 1000; padding: 24px;
    }
    .dialog-card { max-width: 500px; width: 100%; max-height: 90vh; overflow-y: auto; }
    .dialog-card mat-card-content { padding: 12px 16px 0; }
    .dialog-card mat-card-actions { padding: 12px 16px 16px; display: flex; justify-content: flex-end; gap: 8px; }

    .form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px 16px; padding-top: 8px; }
    .form-grid .full { grid-column: 1 / -1; }
    .form-grid mat-form-field { width: 100%; }
  `],
})
export class RemediationComponent {
  project = inject(ProjectService)
  private risksApi = inject(RisksApiService)
  private qc = injectQueryClient()

  activeTab       = signal(0)
  statusFilter    = ''
  poamSourceFilter = signal('')
  dialogOpen      = signal(false)
  editingAction   = signal<RemediationAction | null>(null)
  formError       = signal<string | null>(null)
  form: RemediationActionCreate = this.blankForm()

  statusEntries = Object.entries(STATUS_META).map(([k, v]) => ({ k, v }))
  sourceFilters = [
    { value: '',     label: 'All Sources' },
    { value: 'risk', label: 'Risk Treatments' },
    { value: 'gap',  label: 'Open Gaps' },
    { value: 'tprm', label: 'TPRM Findings' },
  ]

  // ── Queries ────────────────────────────────────────────────────────────────

  summaryQuery = injectQuery(() => ({
    queryKey: ['remediation-summary', this.project.activeProjectId()] as const,
    queryFn: () => firstValueFrom(this.risksApi.remediationSummary({ project_id: this.project.activeProjectId() ?? undefined })),
    enabled: this.activeTab() === 0,
  }))

  actionsQuery = injectQuery(() => ({
    queryKey: ['remediation', this.statusFilter, this.project.activeProjectId()] as const,
    queryFn: () => firstValueFrom(this.risksApi.listRemediation({
      ...(this.statusFilter ? { status: this.statusFilter } : {}),
      project_id: this.project.activeProjectId() ?? undefined,
    })),
    enabled: this.activeTab() === 0,
  }))

  poamSummaryQuery = injectQuery(() => ({
    queryKey: ['poam-summary'] as const,
    queryFn: () => firstValueFrom(this.risksApi.poamSummary()),
    enabled: this.activeTab() === 1,
  }))

  poamQuery = injectQuery(() => ({
    queryKey: ['poam', this.poamSourceFilter()] as const,
    queryFn: () => firstValueFrom(
      this.risksApi.listPoam(this.poamSourceFilter() ? { source: this.poamSourceFilter() } : undefined)
    ),
    enabled: this.activeTab() === 1,
  }))

  // ── Mutations ──────────────────────────────────────────────────────────────

  saveMut = injectMutation(() => ({
    mutationFn: (payload: { body: RemediationActionCreate; id?: string }) =>
      payload.id
        ? firstValueFrom(this.risksApi.updateRemediation(payload.id, payload.body))
        : firstValueFrom(this.risksApi.createRemediation(payload.body)),
    onSuccess: () => {
      this.invalidateRemediation()
      this.dialogOpen.set(false)
    },
    onError: () => this.formError.set('Failed to save.'),
  }))

  deleteMut = injectMutation(() => ({
    mutationFn: (id: string) => firstValueFrom(this.risksApi.deleteRemediation(id)),
    onSuccess: () => this.invalidateRemediation(),
  }))

  // ── Computed ───────────────────────────────────────────────────────────────

  actions = computed(() => this.actionsQuery.data() ?? [])

  // ── Methods ────────────────────────────────────────────────────────────────

  private invalidateRemediation() {
    this.qc.invalidateQueries({ queryKey: ['remediation'] })
    this.qc.invalidateQueries({ queryKey: ['remediation-summary'] })
  }

  private blankForm(): RemediationActionCreate {
    return { title: '', status: 'planned', effort: '', eta: '', progress: 0 }
  }

  openCreate() {
    this.editingAction.set(null)
    this.form = this.blankForm()
    this.formError.set(null)
    this.dialogOpen.set(true)
  }

  openEdit(action: RemediationAction) {
    this.editingAction.set(action)
    this.form = {
      title: action.title,
      description: action.description ?? undefined,
      status: action.status,
      effort: action.effort ?? '',
      eta: action.eta ?? '',
      progress: action.progress,
    }
    this.formError.set(null)
    this.dialogOpen.set(true)
  }

  submitAction() {
    if (!this.form.title.trim()) { this.formError.set('Title is required.'); return }
    const body = {
      ...this.form,
      description: this.form.description || undefined,
      effort:      (this.form.effort as string) || undefined,
      eta:         (this.form.eta as string) || undefined,
    }
    this.saveMut.mutate({ body, id: this.editingAction()?.id })
  }

  deleteAction(action: RemediationAction) {
    if (confirm(`Delete "${action.title}"?`)) this.deleteMut.mutate(action.id)
  }

  remediationSummaryCards(s: { total: number; planned: number; in_progress: number; completed: number; overdue: number }) {
    return [
      { label: 'Total',       value: s.total,       color: '#607D8B' },
      { label: 'Planned',     value: s.planned,     color: '#9E9E9E' },
      { label: 'In Progress', value: s.in_progress, color: '#2196F3' },
      { label: 'Completed',   value: s.completed,   color: '#4CAF50' },
      { label: 'Overdue',     value: s.overdue,     color: '#F44336' },
    ]
  }

  poamSummaryCards(s: { total: number; overdue: number; risk_count: number; gap_count: number; tprm_count: number }) {
    return [
      { label: 'Total Open',      value: s.total,      color: '#607D8B' },
      { label: 'Overdue',         value: s.overdue,    color: '#F44336' },
      { label: 'Risk Treatments', value: s.risk_count, color: '#F44336' },
      { label: 'Open Gaps',       value: s.gap_count,  color: '#FF9800' },
      { label: 'TPRM Findings',   value: s.tprm_count, color: '#9C27B0' },
    ]
  }

  statusMeta(s: string): StatusMeta { return STATUS_META[s] ?? STATUS_META['planned'] }
  effortColor(e: string): string { return EFFORT_COLOR[e] ?? '#9E9E9E' }
  sourceColor(s: string): string { return SOURCE_META[s]?.color ?? '#607D8B' }
  sourceLabel(s: string): string { return SOURCE_META[s]?.label ?? s }
  isOverdue = isOverdue
  fmtDate   = fmtDate
}
