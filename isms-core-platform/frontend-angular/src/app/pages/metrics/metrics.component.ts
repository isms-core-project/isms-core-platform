import { Component, inject, signal, computed } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'
import { injectQuery, injectMutation, injectQueryClient } from '@tanstack/angular-query-experimental'

import { MatCardModule } from '@angular/material/card'
import { MatButtonModule } from '@angular/material/button'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatSelectModule } from '@angular/material/select'
import { MatIconModule } from '@angular/material/icon'
import { MatProgressBarModule } from '@angular/material/progress-bar'
import { MatTableModule } from '@angular/material/table'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatTabsModule } from '@angular/material/tabs'
import { MatSnackBar, MatSnackBarModule } from '@angular/material/snack-bar'

import { MetricsApiService, type MetricSnapshot } from '../../api/metrics-api.service'
import { ProjectsApiService } from '../../api/projects-api.service'
import { ProjectService } from '../../core/services/project.service'
import { AuthService } from '../../core/services/auth.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'
import { type ProjectRead } from '../../shared/types'

// ── Helpers ───────────────────────────────────────────────────────────────────

function pct(num: number, denom: number): number {
  if (!denom) return 0
  return Math.round(num / denom * 100)
}

function fmtDate(d: string): string {
  return new Date(d).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' })
}

interface KpiCard {
  icon: string
  label: string
  value: number
  unit: 'percent' | 'count'
  color: string
  trend?: number | null   // last snapshot value for comparison
}

function metricColor(unit: 'percent' | 'count', value: number, lowerIsBetter = false): string {
  if (unit === 'count') {
    if (lowerIsBetter) return value === 0 ? '#4CAF50' : value <= 3 ? '#FF9800' : '#F44336'
    return '#607D8B'
  }
  return value >= 75 ? '#4CAF50' : value >= 40 ? '#FF9800' : '#F44336'
}

// ── Component ─────────────────────────────────────────────────────────────────

@Component({
  selector: 'app-metrics',
  standalone: true,
  imports: [
    FormsModule,
    MatCardModule, MatButtonModule, MatFormFieldModule, MatSelectModule,
    MatIconModule, MatProgressBarModule, MatTableModule,
    MatTooltipModule, MatTabsModule, MatSnackBarModule,
    PageHeaderComponent,
  ],
  template: `
<app-page-header
  title="KPI Dashboard"
  subtitle="ISO 27001:2022 §9.1 — performance evaluation and measurement">
  <div actions>
    @if (activeTab() === 0) {
      <div class="header-actions">
        <button mat-icon-button matTooltip="Compute snapshot now"
          [disabled]="snapshotMut.isPending() || !selectedProjectId()"
          (click)="computeSnapshot()">
          @if (snapshotMut.isPending()) {
            <span class="pending-indicator">…</span>
          } @else {
            <mat-icon>refresh</mat-icon>
          }
        </button>
        <mat-form-field appearance="outline" subscriptSizing="dynamic" class="project-select-field">
          <mat-label>Project</mat-label>
          <mat-select [ngModel]="selectedProjectId()" (ngModelChange)="selectedProjectId.set($event)">
            <mat-option value="">Select a project</mat-option>
            @for (p of projectsQuery.data() ?? []; track p.id) {
              <mat-option [value]="p.id">{{ p.name }}</mat-option>
            }
          </mat-select>
        </mat-form-field>
      </div>
    }
  </div>
</app-page-header>

@if (auth.isSuperAdmin()) {
  <mat-tab-group [selectedIndex]="activeTab()" (selectedIndexChange)="activeTab.set($event)"
    class="tabs-no-margin-bottom">
    <mat-tab label="My Metrics" />
    <mat-tab label="Portfolio" />
  </mat-tab-group>
}

<!-- ── My Metrics ────────────────────────────────────────────────────────── -->
@if (activeTab() === 0) {

  @if (!selectedProjectId()) {
    <div class="empty-state empty-state-top-lg">
      <mat-icon>insights</mat-icon>
      <p>Select a project to view KPI metrics.</p>
    </div>
  } @else {

    @if (snapshotsQuery.isLoading()) {
      <div class="loading-grid">
        @for (i of [0,1,2,3,4,5,6,7,8]; track i) {
          <div class="skeleton-card"></div>
        }
      </div>
    } @else if (snapshotsQuery.isError()) {
      <div class="alert alert-error">Failed to load metrics.</div>
    } @else if (!latestSnapshot()) {
      <div class="empty-state empty-state-top-md">
        <mat-icon>bar_chart</mat-icon>
        <div>
          <p>No snapshots yet for this project.</p>
          <button mat-flat-button color="primary" class="compute-btn"
            [disabled]="snapshotMut.isPending()"
            (click)="computeSnapshot()">
            <mat-icon>add_chart</mat-icon>
            Compute First Snapshot
          </button>
        </div>
      </div>
    } @else {
      @let snap = latestSnapshot()!;

      <!-- Audit Readiness Hero -->
      <div class="audit-hero" [style.border-color]="auditColor() + '40'" [style.background]="auditColor() + '08'">
        <mat-icon class="audit-hero-icon" [style.color]="auditColor()">insights</mat-icon>
        <div>
          <p class="audit-hero-label">Audit Readiness Score</p>
          <p class="audit-hero-value" [style.color]="auditColor()">{{ snap.audit_readiness_score }}%</p>
          <p class="dim-sm">Composite of compliance, policy coverage, evidence freshness, open risks &amp; gaps</p>
        </div>
        <div class="audit-hero-date">
          <span class="dim-sm">Snapshot: {{ fmtDate(snap.snapshot_date) }}</span>
        </div>
      </div>

      <!-- KPI grid -->
      <div class="kpi-grid">
        @for (card of kpiCards(snap); track card.label) {
          <div class="kpi-card"
            [style.border-color]="card.color + '25'"
            [style.background]="card.color + '06'"
            [matTooltip]="'Snapshot: ' + fmtDate(snap.snapshot_date)">
            <div class="kpi-header">
              <mat-icon [style.color]="card.color">{{ card.icon }}</mat-icon>
              <div>
                <p class="kpi-label">{{ card.label }}</p>
                <p class="kpi-value" [style.color]="card.color">
                  {{ card.value }}{{ card.unit === 'percent' ? '%' : '' }}
                </p>
              </div>
            </div>
            <mat-progress-bar mode="determinate"
              [value]="card.unit === 'percent' ? card.value : 0"
              [style.display]="card.unit === 'percent' ? 'block' : 'none'"
              [style.--mat-progress-bar-active-indicator-color]="card.color"
              class="kpi-progress-bar" />
          </div>
        }
      </div>

      <!-- Trend table (last 30 days snapshots) -->
      @if (snapshotsQuery.data()!.length > 1) {
        <div class="trend-section">
          <p class="section-title">Snapshot History (last 30 days)</p>
          <div class="table-wrapper">
            <table mat-table [dataSource]="recentSnapshots()" class="trend-table">

              <ng-container matColumnDef="date">
                <th mat-header-cell *matHeaderCellDef>Date</th>
                <td mat-cell *matCellDef="let s">{{ fmtDate(s.snapshot_date) }}</td>
              </ng-container>

              <ng-container matColumnDef="audit">
                <th mat-header-cell *matHeaderCellDef class="col-right">Audit Readiness</th>
                <td mat-cell *matCellDef="let s" class="col-right">
                  <span [style.color]="metricColor('percent', s.audit_readiness_score)" class="fw-600">
                    {{ s.audit_readiness_score }}%
                  </span>
                </td>
              </ng-container>

              <ng-container matColumnDef="policy">
                <th mat-header-cell *matHeaderCellDef class="col-right">Policy Coverage</th>
                <td mat-cell *matCellDef="let s" class="col-right">
                  <span [style.color]="metricColor('percent', pct(s.controls_with_policy, s.total_controls))">
                    {{ pct(s.controls_with_policy, s.total_controls) }}%
                  </span>
                </td>
              </ng-container>

              <ng-container matColumnDef="impl">
                <th mat-header-cell *matHeaderCellDef class="col-right">Impl Coverage</th>
                <td mat-cell *matCellDef="let s" class="col-right">
                  <span [style.color]="metricColor('percent', pct(s.controls_with_impl, s.total_controls))">
                    {{ pct(s.controls_with_impl, s.total_controls) }}%
                  </span>
                </td>
              </ng-container>

              <ng-container matColumnDef="evidence">
                <th mat-header-cell *matHeaderCellDef class="col-right">Evidence</th>
                <td mat-cell *matCellDef="let s" class="col-right">
                  <span [style.color]="metricColor('percent', pct(s.controls_with_evidence, s.total_controls))">
                    {{ pct(s.controls_with_evidence, s.total_controls) }}%
                  </span>
                </td>
              </ng-container>

              <ng-container matColumnDef="gaps">
                <th mat-header-cell *matHeaderCellDef class="col-right">Open Gaps</th>
                <td mat-cell *matCellDef="let s" class="col-right">
                  <span [style.color]="metricColor('count', s.open_gaps, true)">{{ s.open_gaps }}</span>
                </td>
              </ng-container>

              <tr mat-header-row *matHeaderRowDef="trendCols"></tr>
              <tr mat-row *matRowDef="let row; columns: trendCols;"></tr>
            </table>
          </div>
        </div>
      }
    }
  }
}

<!-- ── Portfolio tab ──────────────────────────────────────────────────────── -->
@if (activeTab() === 1 && auth.isSuperAdmin()) {
  <div class="portfolio-section">
    @if (portfolioQuery.isLoading()) {
      <div class="loading-grid portfolio-loading-grid">
        @for (i of [0,1,2,3]; track i) { <div class="skeleton-card skeleton-card-sm"></div> }
      </div>
    } @else if (portfolioQuery.isError()) {
      <div class="alert alert-warn">Portfolio data unavailable.</div>
    } @else if (!portfolioQuery.data()?.length) {
      <div class="empty-state"><mat-icon>folder_open</mat-icon><p>No project snapshots yet.</p></div>
    } @else {
      <div class="table-wrapper">
        <table mat-table [dataSource]="portfolioQuery.data()!" class="trend-table">

          <ng-container matColumnDef="project">
            <th mat-header-cell *matHeaderCellDef>Project</th>
            <td mat-cell *matCellDef="let row" class="fw-500">{{ row.project_name }}</td>
          </ng-container>

          <ng-container matColumnDef="audit">
            <th mat-header-cell *matHeaderCellDef class="col-right">Audit Readiness</th>
            <td mat-cell *matCellDef="let row" class="col-right">
              <span [style.color]="metricColor('percent', row.audit_readiness_score)" class="fw-600">
                {{ row.audit_readiness_score }}%
              </span>
            </td>
          </ng-container>

          <ng-container matColumnDef="policy">
            <th mat-header-cell *matHeaderCellDef class="col-right">Policy</th>
            <td mat-cell *matCellDef="let row" class="col-right">
              <span [style.color]="metricColor('percent', pct(row.controls_with_policy, row.total_controls))">
                {{ pct(row.controls_with_policy, row.total_controls) }}%
              </span>
            </td>
          </ng-container>

          <ng-container matColumnDef="gaps">
            <th mat-header-cell *matHeaderCellDef class="col-right">Open Gaps</th>
            <td mat-cell *matCellDef="let row" class="col-right">
              <span [style.color]="metricColor('count', row.open_gaps, true)">{{ row.open_gaps }}</span>
            </td>
          </ng-container>

          <ng-container matColumnDef="snapshot_date">
            <th mat-header-cell *matHeaderCellDef class="col-right">Last Snapshot</th>
            <td mat-cell *matCellDef="let row" class="col-right">
              <span class="dim-sm">{{ fmtDate(row.snapshot_date) }}</span>
            </td>
          </ng-container>

          <tr mat-header-row *matHeaderRowDef="portfolioCols"></tr>
          <tr mat-row *matRowDef="let row; columns: portfolioCols;"></tr>
        </table>
      </div>
    }
  </div>
}
  `,
  styles: [`
    :host { display: block; padding: 24px; }

    .alert { padding: 10px 14px; border-radius: 6px; margin-bottom: 14px; font-size: 0.85rem; }
    .alert-error { background: rgba(192,0,0,0.12); color: #FFC7CE; }
    .alert-warn  { background: rgba(230,160,0,0.12); color: #FFEB9C; }

    /* Header actions */
    .header-actions { display: flex; align-items: center; gap: 8px; }
    .pending-indicator { font-size: 12px; }
    .project-select-field { min-width: 220px; }
    .tabs-no-margin-bottom { margin-bottom: 0; }

    /* Audit hero */
    .audit-hero {
      display: flex; align-items: center; gap: 24px;
      padding: 20px 24px; border-radius: 10px; border: 1px solid;
      margin-bottom: 24px; flex-wrap: wrap;
    }
    .audit-hero-icon { font-size: 36px; width: 36px; height: 36px; }
    .audit-hero-label {
      font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em;
      color: var(--mat-sys-on-surface-variant); margin: 0;
    }
    .audit-hero-value { font-size: 2.8rem; font-weight: 800; line-height: 1; margin: 0; }
    .audit-hero-date { margin-left: auto; }

    /* KPI grid */
    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
      gap: 16px;
    }
    .kpi-card {
      border: 1px solid; border-radius: 10px; padding: 16px;
    }
    .kpi-header { display: flex; align-items: flex-start; gap: 10px; }
    .kpi-header mat-icon { font-size: 20px; width: 20px; height: 20px; margin-top: 2px; flex-shrink: 0; }
    .kpi-label { font-size: 0.7rem; color: var(--mat-sys-on-surface-variant); line-height: 1.3; margin: 0; }
    .kpi-value { font-size: 1.8rem; font-weight: 700; line-height: 1.1; margin: 2px 0 0; }
    .kpi-progress-bar { height: 4px; border-radius: 2px; margin-top: 8px; }

    /* Skeleton */
    .loading-grid {
      display: grid; grid-template-columns: repeat(auto-fill, minmax(210px, 1fr)); gap: 16px;
    }
    .portfolio-loading-grid { grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); }
    .skeleton-card {
      height: 110px; border-radius: 10px; background: rgba(255,255,255,0.06);
      animation: pulse 1.5s ease-in-out infinite alternate;
    }
    .skeleton-card-sm { height: 80px; }
    @keyframes pulse { from { opacity: 0.4; } to { opacity: 1; } }

    /* Table */
    .table-wrapper { overflow-x: auto; }
    .trend-table { width: 100%; }
    .col-right { text-align: right; }
    .fw-600 { font-weight: 600; }
    .fw-500 { font-weight: 500; }

    .section-title { font-size: 0.85rem; font-weight: 600; margin: 0 0 12px; }
    .trend-section { margin-top: 28px; }
    .portfolio-section { padding-top: 16px; }

    .dim-sm { font-size: 0.68rem; color: var(--mat-sys-on-surface-variant); }

    .empty-state {
      display: flex; align-items: center; gap: 16px;
      padding: 48px 32px; color: var(--mat-sys-on-surface-variant);
      justify-content: center; flex-direction: column; text-align: center;
    }
    .empty-state mat-icon { font-size: 40px; width: 40px; height: 40px; }
    .empty-state p { margin: 4px 0; }
    .empty-state-top-lg { margin-top: 32px; }
    .empty-state-top-md { margin-top: 24px; }
    .compute-btn { margin-top: 12px; }
  `],
})
export class MetricsComponent {
  auth      = inject(AuthService)
  project   = inject(ProjectService)
  private metricsApi  = inject(MetricsApiService)
  private projectsApi = inject(ProjectsApiService)
  private snackBar    = inject(MatSnackBar)
  private qc          = injectQueryClient()

  activeTab         = signal(0)
  selectedProjectId = signal(this.project.activeProjectId() ?? '')

  trendCols     = ['date', 'audit', 'policy', 'impl', 'evidence', 'gaps']
  portfolioCols = ['project', 'audit', 'policy', 'gaps', 'snapshot_date']

  // ── Queries ────────────────────────────────────────────────────────────────

  projectsQuery = injectQuery(() => ({
    queryKey: ['projects-list'] as const,
    queryFn: () => firstValueFrom(this.projectsApi.list()),
  }))

  snapshotsQuery = injectQuery(() => ({
    queryKey: ['metrics-snapshots', this.selectedProjectId()] as const,
    queryFn: () => firstValueFrom(this.metricsApi.getSnapshots(this.selectedProjectId(), 30)),
    enabled: !!this.selectedProjectId() && this.activeTab() === 0,
  }))

  portfolioQuery = injectQuery(() => ({
    queryKey: ['metrics-portfolio-all'] as const,
    queryFn: async (): Promise<MetricSnapshot[]> => {
      // Fetch all projects and get the latest snapshot per project
      const projects = await firstValueFrom(this.projectsApi.list())
      const snaps = await Promise.allSettled(
        projects.map(p => firstValueFrom(this.metricsApi.getSnapshots(p.id, 7)))
      )
      const results: (MetricSnapshot & { project_name: string })[] = []
      snaps.forEach((r, i) => {
        if (r.status === 'fulfilled' && r.value.length > 0) {
          const latest = r.value[0]
          results.push({ ...latest, project_name: projects[i].name } as MetricSnapshot & { project_name: string })
        }
      })
      return results.sort((a, b) => b.audit_readiness_score - a.audit_readiness_score)
    },
    enabled: this.activeTab() === 1 && this.auth.isSuperAdmin(),
  }))

  // ── Mutations ──────────────────────────────────────────────────────────────

  snapshotMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.metricsApi.createSnapshot(this.selectedProjectId())),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['metrics-snapshots', this.selectedProjectId()] })
      this.snackBar.open('Snapshot computed.', '', { duration: 3000 })
    },
    onError: () => this.snackBar.open('Failed to compute snapshot.', 'Dismiss', { duration: 4000 }),
  }))

  // ── Computed ───────────────────────────────────────────────────────────────

  latestSnapshot = computed(() => {
    const snaps = this.snapshotsQuery.data()
    return snaps && snaps.length > 0 ? snaps[0] : null
  })

  recentSnapshots = computed(() => (this.snapshotsQuery.data() ?? []).slice(0, 30))

  auditColor = computed(() => {
    const s = this.latestSnapshot()
    if (!s) return '#607D8B'
    return metricColor('percent', s.audit_readiness_score)
  })

  // ── Methods ────────────────────────────────────────────────────────────────

  computeSnapshot() {
    if (!this.selectedProjectId()) return
    this.snapshotMut.mutate(undefined)
  }

  kpiCards(snap: MetricSnapshot): KpiCard[] {
    const total = snap.total_controls || 1
    const policyCov  = pct(snap.controls_with_policy,     total)
    const implCov    = pct(snap.controls_with_impl,       total)
    const assessCov  = pct(snap.controls_with_assessment, total)
    const evidenceCov = pct(snap.controls_with_evidence,  total)
    const gapClosed  = snap.closed_gaps + snap.open_gaps > 0
      ? pct(snap.closed_gaps, snap.closed_gaps + snap.open_gaps)
      : 0

    return [
      { icon: 'inventory',        label: 'Policy Coverage',    value: policyCov,  unit: 'percent', color: metricColor('percent', policyCov) },
      { icon: 'developer_guide',  label: 'Impl Coverage',      value: implCov,    unit: 'percent', color: metricColor('percent', implCov) },
      { icon: 'assignment_turned_in', label: 'Assessment Coverage', value: assessCov, unit: 'percent', color: metricColor('percent', assessCov) },
      { icon: 'verified',         label: 'Evidence Coverage',  value: evidenceCov, unit: 'percent', color: metricColor('percent', evidenceCov) },
      { icon: 'task_alt',         label: 'Gap Closure Rate',   value: gapClosed,  unit: 'percent', color: metricColor('percent', gapClosed) },
      { icon: 'security',         label: 'Open Gaps',          value: snap.open_gaps,  unit: 'count', color: metricColor('count', snap.open_gaps, true) },
      { icon: 'dns',              label: 'Total Controls',     value: snap.total_controls, unit: 'count', color: '#607D8B' },
    ]
  }

  metricColor = metricColor
  pct         = pct
  fmtDate     = fmtDate
}
