import { Component, inject, Input } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { DecimalPipe } from '@angular/common'
import { firstValueFrom } from 'rxjs'

import { injectQuery } from '@tanstack/angular-query-experimental'

import { MatButtonModule } from '@angular/material/button'
import { MatCardModule } from '@angular/material/card'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatIconModule } from '@angular/material/icon'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatChipsModule } from '@angular/material/chips'
import { MatProgressBarModule } from '@angular/material/progress-bar'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'

import { CompassApiService, CompassFramework } from '../../api/compass-api.service'
import { ProjectsApiService } from '../../api/projects-api.service'
import { ProjectService } from '../../core/services/project.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

// ─── Helpers ───────────────────────────────────────────────────────────────────

interface FrameworkMeta { label: string; color: string }

const FRAMEWORK_META: Record<string, FrameworkMeta> = {
  iso27001: { label: 'ISO 27001:2022', color: '#4472C4' },
  iso27701: { label: 'ISO 27701:2019', color: '#ba68c8' },
  iso27018: { label: 'ISO 27018:2019', color: '#29b6f6' },
  iso42001: { label: 'ISO 42001:2023', color: '#ffa726' },
  soc2:     { label: 'SOC 2',          color: '#1565C0' },
  nist_csf: { label: 'NIST CSF 2.0',   color: '#ED7D31' },
  gdpr:     { label: 'GDPR',           color: '#C00000' },
  ndsg:     { label: 'nDSG',           color: '#B71C1C' },
}

function frameworkColor(code: string): string {
  return FRAMEWORK_META[code.toLowerCase()]?.color ?? '#888888'
}

function frameworkLabel(code: string, name: string): string {
  return FRAMEWORK_META[code.toLowerCase()]?.label ?? name
}

function coverageColor(pct: number): string {
  if (pct >= 80) return '#2E7D32'
  if (pct >= 60) return '#F57F17'
  if (pct >= 40) return '#E65100'
  return '#B71C1C'
}

function coverageBg(pct: number): string {
  if (pct >= 80) return 'rgba(46,125,50,0.10)'
  if (pct >= 60) return 'rgba(245,127,23,0.10)'
  if (pct >= 40) return 'rgba(230,81,0,0.10)'
  return 'rgba(183,28,28,0.10)'
}

function statusColor(status: string): string {
  const map: Record<string, string> = {
    complete:    '#2E7D32',
    in_progress: '#F57F17',
    draft:       '#888888',
    not_started: '#B71C1C',
  }
  return map[status] ?? '#888888'
}

function formatDate(iso: string): string {
  return new Date(iso).toLocaleDateString('en-GB', {
    day: '2-digit', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit',
  })
}

// ─── Framework Coverage Card ────────────────────────────────────────────────────

@Component({
  selector: 'app-framework-coverage-card',
  standalone: true,
  imports: [DecimalPipe, MatProgressBarModule],
  template: `
    <div class="fw-card" [style.border-left-color]="fwColor">
      <div class="fw-top">
        <div class="fw-info">
          <div class="fw-name">{{ fwLabel }}</div>
          <div class="fw-code">{{ framework.framework_code.toUpperCase() }}</div>
          @if (framework.avg_score !== null) {
            <div class="fw-score">Avg score: <strong>{{ framework.avg_score | number:'1.1-1' }}</strong></div>
          }
        </div>
        <div class="gauge" [style.border-color]="covColor" [style.background]="covBg">
          <div class="gauge-pct" [style.color]="covColor">{{ framework.coverage_pct | number:'1.0-0' }}</div>
          <div class="gauge-label">%</div>
        </div>
      </div>

      <div class="fw-bar-row">
        <mat-progress-bar mode="determinate" [value]="framework.coverage_pct"
          class="fw-bar"
          [color]="framework.coverage_pct >= 60 ? 'primary' : 'warn'">
        </mat-progress-bar>
        <span class="fw-counts">{{ framework.mapped_controls }} / {{ framework.total_controls }}</span>
      </div>

      <div class="fw-meta">
        <span class="status-badge" [style.color]="statCol" [style.background]="statCol + '18'" [style.border-color]="statCol + '40'">
          {{ statLabel }}
        </span>
        <span class="meta-text">{{ framework.mapped_controls }} controls mapped</span>
      </div>
    </div>
  `,
  styles: [`
    .fw-card { border:1px solid var(--mat-sys-outline-variant);border-left:4px solid;border-radius:8px;padding:14px 16px }
    .fw-top { display:flex;align-items:flex-start;gap:12px;margin-bottom:10px }
    .fw-info { flex:1;min-width:0 }
    .fw-name { font-weight:700;font-size:0.9rem;line-height:1.3 }
    .fw-code { font-family:monospace;font-size:0.7rem;color:var(--mat-sys-on-surface-variant);margin-top:2px }
    .fw-score { font-size:0.75rem;color:var(--mat-sys-on-surface-variant);margin-top:4px }
    .gauge { display:flex;flex-direction:column;align-items:center;justify-content:center;width:72px;height:72px;border-radius:50%;border:3px solid;flex-shrink:0 }
    .gauge-pct { font-size:1.3rem;font-weight:700;line-height:1 }
    .gauge-label { font-size:0.65rem;color:var(--mat-sys-on-surface-variant) }
    .fw-bar-row { display:flex;align-items:center;gap:10px;margin-bottom:8px }
    .fw-bar { flex:1;border-radius:4px }
    .fw-counts { font-size:0.72rem;color:var(--mat-sys-on-surface-variant);white-space:nowrap }
    .fw-meta { display:flex;align-items:center;gap:10px }
    .status-badge { font-size:0.65rem;padding:2px 7px;border-radius:4px;border:1px solid }
    .meta-text { font-size:0.72rem;color:var(--mat-sys-on-surface-variant) }
  `],
})
export class FrameworkCoverageCardComponent {
  @Input() framework!: CompassFramework

  get fwColor(): string { return frameworkColor(this.framework.framework_code) }
  get fwLabel(): string { return frameworkLabel(this.framework.framework_code, this.framework.framework_name) }
  get covColor(): string { return coverageColor(this.framework.coverage_pct) }
  get covBg(): string { return coverageBg(this.framework.coverage_pct) }
  get statCol(): string { return statusColor(this.framework.status) }
  get statLabel(): string { return this.framework.status.replace(/_/g, ' ') }
}

// ─── Main Compass Component ─────────────────────────────────────────────────────

@Component({
  selector: 'app-compass',
  standalone: true,
  imports: [
    FormsModule,
    DecimalPipe,
    MatButtonModule, MatCardModule, MatFormFieldModule, MatInputModule,
    MatSelectModule, MatIconModule, MatTooltipModule, MatChipsModule,
    MatProgressBarModule, MatProgressSpinnerModule,
    PageHeaderComponent,
    FrameworkCoverageCardComponent,
  ],
  template: `
    <div class="compass-page">
    <app-page-header
      title="Compass"
      subtitle="Framework coverage — cross-framework assessment status for a project">
    </app-page-header>

    <!-- Project selector -->
    <div class="selector-bar">
      <mat-form-field appearance="outline" subscriptSizing="dynamic" class="proj-select-field">
        <mat-label>Select Project</mat-label>
        <mat-select [(ngModel)]="selectedProjectId">
          @if (projects.isPending()) {
            <mat-option disabled>Loading projects…</mat-option>
          }
          @for (p of projects.data() ?? []; track p.id) {
            <mat-option [value]="p.id">{{ p.name }}</mat-option>
          }
        </mat-select>
      </mat-form-field>

      @if (selectedProjectId) {
        <button mat-flat-button color="primary" (click)="coverage.refetch()">
          <mat-icon>refresh</mat-icon>
          Refresh
        </button>
      }
    </div>

    <!-- No project selected -->
    @if (!selectedProjectId) {
      <div class="empty-state">
        <mat-icon class="empty-icon">explore</mat-icon>
        <div class="empty-title">Select a project</div>
        <div class="empty-sub">Choose a project above to view its framework coverage status.</div>
      </div>
    }

    <!-- Loading -->
    @if (selectedProjectId && coverage.isPending()) {
      <div class="loading-wrap">
        <mat-spinner diameter="40"></mat-spinner>
        <span>Loading coverage data…</span>
      </div>
    }

    <!-- Error -->
    @if (coverage.isError()) {
      <div class="error-alert">
        <mat-icon>error_outline</mat-icon>
        Failed to load coverage data. The project may not have any assessments yet.
      </div>
    }

    <!-- Coverage data -->
    @if (coverage.data(); as data) {
      <!-- Summary strip -->
      <div class="summary-strip">
        @for (m of summaryMetrics(data.frameworks); track m.label) {
          <div class="metric-card" [style.border-top-color]="m.color">
            <div class="metric-value" [style.color]="m.color">{{ m.value }}</div>
            <div class="metric-label">{{ m.label }}</div>
          </div>
        }
        <div class="metric-card updated-card">
          <div class="metric-value-sm">{{ fmtDate(data.generated_at) }}</div>
          <div class="metric-label">Last updated</div>
        </div>
      </div>

      <!-- Overview bar chart -->
      <div class="overview-card">
        <div class="overview-title">
          <mat-icon class="icon-md overview-icon">bar_chart</mat-icon>
          Coverage Overview
        </div>
        <div class="overview-rows">
          @for (fw of data.frameworks; track fw.framework_code) {
            <div class="ov-row">
              <div class="ov-label" [matTooltip]="fw.framework_name" matTooltipPosition="right">
                <span class="ov-dot" [style.background]="fwColor(fw.framework_code)"></span>
                {{ fwLabel(fw.framework_code, fw.framework_name) }}
              </div>
              <div class="ov-bar-wrap">
                <div class="ov-bar-bg">
                  <div class="ov-bar-fill"
                    [style.width.%]="fw.coverage_pct"
                    [style.background]="fwColor(fw.framework_code)">
                  </div>
                </div>
                <span class="ov-pct" [style.color]="covColor(fw.coverage_pct)">{{ fw.coverage_pct | number:'1.0-0' }}%</span>
                <span class="ov-counts">{{ fw.mapped_controls }}/{{ fw.total_controls }}</span>
              </div>
            </div>
          }
        </div>
      </div>

      <!-- Framework cards grid -->
      <div class="fw-grid">
        @for (fw of data.frameworks; track fw.framework_code) {
          <app-framework-coverage-card [framework]="fw"></app-framework-coverage-card>
        }
      </div>

      @if (data.frameworks.length === 0) {
        <div class="info-state">
          <mat-icon>info_outline</mat-icon>
          No framework assessments found for this project. Create assessments in the Compliance Modules to see coverage here.
        </div>
      }
    }
    </div>
  `,
  styles: [`
    .compass-page { display:flex;flex-direction:column;gap:16px }
    .selector-bar { display:flex;gap:12px;align-items:center;flex-wrap:wrap }
    .proj-select-field { min-width: 320px; }
    .overview-icon { vertical-align: middle; margin-right: 6px; }
    .empty-state { display:flex;flex-direction:column;align-items:center;justify-content:center;padding:64px 24px;border:1px dashed var(--mat-sys-outline-variant);border-radius:12px;text-align:center }
    .empty-icon { font-size:48px;width:48px;height:48px;color:var(--mat-sys-on-surface-variant);margin-bottom:12px }
    .empty-title { font-size:1.1rem;font-weight:600;margin-bottom:6px }
    .empty-sub { font-size:0.85rem;color:var(--mat-sys-on-surface-variant) }
    .loading-wrap { display:flex;align-items:center;gap:12px;padding:32px;color:var(--mat-sys-on-surface-variant) }
    .error-alert { display:flex;align-items:center;gap:8px;background:rgba(211,47,47,0.1);color:#d32f2f;border:1px solid rgba(211,47,47,0.25);border-radius:8px;padding:12px 16px;font-size:0.85rem }
    .summary-strip { display:flex;gap:12px;margin-bottom:20px;flex-wrap:wrap }
    .metric-card { background:var(--mat-sys-surface);border:1px solid var(--mat-sys-outline-variant);border-top:3px solid var(--mat-sys-primary);border-radius:8px;padding:10px 16px;min-width:110px }
    .metric-value { font-size:1.6rem;font-weight:700;line-height:1.1 }
    .metric-value-sm { font-size:0.8rem;font-weight:600;line-height:1.5 }
    .metric-label { font-size:0.72rem;color:var(--mat-sys-on-surface-variant);margin-top:2px }
    .updated-card { border-top-color:var(--mat-sys-outline-variant) }
    .overview-card { background:var(--mat-sys-surface);border:1px solid var(--mat-sys-outline-variant);border-radius:10px;padding:16px;margin-bottom:20px }
    .overview-title { font-weight:700;font-size:0.9rem;margin-bottom:12px;display:flex;align-items:center }
    .overview-rows { display:flex;flex-direction:column;gap:10px }
    .ov-row { display:flex;align-items:center;gap:12px }
    .ov-label { font-size:0.78rem;font-weight:600;width:160px;flex-shrink:0;display:flex;align-items:center;gap:6px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis }
    .ov-dot { width:8px;height:8px;border-radius:50%;flex-shrink:0 }
    .ov-bar-wrap { flex:1;display:flex;align-items:center;gap:8px;min-width:0 }
    .ov-bar-bg { flex:1;height:10px;background:var(--mat-sys-surface-variant);border-radius:5px;overflow:hidden }
    .ov-bar-fill { height:100%;border-radius:5px;transition:width 0.6s ease }
    .ov-pct { font-size:0.75rem;font-weight:700;width:36px;text-align:right;flex-shrink:0 }
    .ov-counts { font-size:0.68rem;color:var(--mat-sys-on-surface-variant);width:50px;flex-shrink:0 }
    .fw-grid { display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:16px }
    .info-state { display:flex;align-items:center;gap:8px;background:rgba(21,101,192,0.06);border:1px solid rgba(21,101,192,0.2);border-radius:8px;padding:14px 16px;font-size:0.85rem;color:var(--mat-sys-on-surface-variant) }
  `],
})
export class CompassComponent {
  private api = inject(CompassApiService)
  private projectsApi = inject(ProjectsApiService)
  private projectSvc = inject(ProjectService)

  selectedProjectId = this.projectSvc.activeProjectId() ?? ''

  projects = injectQuery(() => ({
    queryKey: ['projects-list'],
    queryFn: () => firstValueFrom(this.projectsApi.list()),
  }))

  coverage = injectQuery(() => ({
    queryKey: ['compass', this.selectedProjectId],
    queryFn: () => firstValueFrom(this.api.get(this.selectedProjectId)),
    enabled: !!this.selectedProjectId,
  }))

  fwColor(code: string): string { return frameworkColor(code) }
  fwLabel(code: string, name: string): string { return frameworkLabel(code, name) }
  covColor(pct: number): string { return coverageColor(pct) }
  fmtDate(iso: string): string { return formatDate(iso) }

  summaryMetrics(frameworks: CompassFramework[]) {
    const total = frameworks.length
    const complete = frameworks.filter(f => f.status === 'complete').length
    const inProgress = frameworks.filter(f => f.status === 'in_progress').length
    const avgCoverage = total > 0
      ? Math.round(frameworks.reduce((s, f) => s + f.coverage_pct, 0) / total)
      : 0
    return [
      { label: 'Frameworks',   value: total,             color: 'var(--mat-sys-primary)' },
      { label: 'Complete',     value: complete,           color: '#2E7D32' },
      { label: 'In Progress',  value: inProgress,         color: '#F57F17' },
      { label: 'Avg Coverage', value: `${avgCoverage}%`,  color: coverageColor(avgCoverage) },
    ]
  }
}
