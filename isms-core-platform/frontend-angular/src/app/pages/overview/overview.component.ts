import { Component, inject, signal, computed } from '@angular/core'
import { Router, RouterLink } from '@angular/router'
import { NgTemplateOutlet } from '@angular/common'
import { firstValueFrom } from 'rxjs'

import { injectQuery } from '@tanstack/angular-query-experimental'

import { MatCardModule } from '@angular/material/card'
import { MatButtonModule } from '@angular/material/button'
import { MatIconModule } from '@angular/material/icon'
import { MatChipsModule } from '@angular/material/chips'
import { MatTooltipModule } from '@angular/material/tooltip'

import { DashboardApiService, FrameworkOverview } from '../../api/dashboard-api.service'
import { FeedsApiService } from '../../api/feeds-api.service'
import { ProductService, PRODUCT_COLORS, PRODUCT_SUBTITLES } from '../../core/services/product.service'
import { ProjectService } from '../../core/services/project.service'
import { ThemeService } from '../../core/services/theme.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'
import { MetricCardComponent } from '../../shared/components/metric-card.component'
import { StatusChipComponent } from '../../shared/components/status-chip.component'
import { ExpandableCardComponent } from '../../shared/components/expandable-card.component'

// ── Types ─────────────────────────────────────────────────────────────────────

interface SectionRow {
  section: string
  section_name: string
  total_controls: number
  framework_covered: number
  operational_covered: number
  framework_pct: number
  operational_pct: number
}

interface RealOverview {
  total_controls: number
  total_policies: number
  total_implementations: number
  total_assessments: number
  total_gaps_open: number
  framework: { total: number; has_policy: number; has_ug: number; has_tg: number; has_assessment: number; coverage_pct: number }
  operational: { total: number; has_policy: number; has_assessment: number; coverage_pct: number }
  items_by_status: Record<string, number>
  sections: SectionRow[]
}

interface RealReadiness {
  composite_score: number
  status: 'green' | 'amber' | 'red'
  components: {
    policies: number
    user_guides: number
    technical_guides: number
    assessments: number
    evidence: number
    gaps: number
  }
  policies_pct: number
  ug_pct: number
  tg_pct: number
  assessments_pct: number
  evidence_pct: number
  gaps_closed_pct: number
  breakdown: Record<string, number>
}

// ── Helpers ────────────────────────────────────────────────────────────────────

const SECTION_COLORS: Record<string, string> = {
  'A.5': '#327df4',
  'A.6': '#00c752',
  'A.7': '#ff9800',
  'A.8': '#f44336',
}

function sectionColor(section: string): string {
  return SECTION_COLORS[section] ?? '#327df4'
}

function readinessScoreColor(status: string, dark: boolean): string {
  if (status === 'green') return dark ? '#C6EFCE' : '#1b5e20'
  if (status === 'amber') return dark ? '#FFEB9C' : '#9a6500'
  return dark ? '#FFC7CE' : '#9e0000'
}

function progressBarColor(value: number, dark: boolean): string {
  if (value >= 80) return dark ? '#C6EFCE' : '#2e7d32'
  if (value >= 50) return dark ? '#FFEB9C' : '#e65100'
  return dark ? '#FFC7CE' : '#c62828'
}

function clamp(v: number): number {
  return Math.min(100, Math.max(0, v))
}

function fmt(n: number | null | undefined): string {
  if (n == null) return '—'
  return n.toLocaleString()
}

function fmtPct(n: number | null | undefined): string {
  if (n == null) return '—'
  return Math.round(n) + '%'
}

// ── Component ─────────────────────────────────────────────────────────────────

@Component({
  selector: 'app-overview',
  standalone: true,
  imports: [
    RouterLink,
    NgTemplateOutlet,
    MatCardModule,
    MatButtonModule,
    MatIconModule,
    MatChipsModule,
    MatTooltipModule,
    PageHeaderComponent,
    MetricCardComponent,
    StatusChipComponent,
    ExpandableCardComponent,
  ],
  template: `
<div class="overview-page">

  <!-- ── No project selected — info card ───────────────────────────────── -->
  @if (!activeProjectId()) {

    <app-page-header [title]="'Compliance Overview'"
      [subtitle]="product.product() === 'isms' ? pageSubtitle() : nonIsmsSubtitle()" />

    <mat-card class="no-project-card">
      <mat-card-content>
        <div class="no-project-inner">
          <mat-icon class="no-project-icon">folder_open</mat-icon>
          <div class="no-project-text">
            <div class="no-project-title">No active project selected</div>
            <div class="no-project-sub">
              Go to Projects to create or select one to view compliance data.
            </div>
          </div>
          <a mat-stroked-button routerLink="/projects">
            <mat-icon>arrow_forward</mat-icon>
            Go to Projects
          </a>
        </div>
      </mat-card-content>
    </mat-card>

    @if (product.product() !== 'isms') {
      <div class="fw-section-mt">
        <ng-container [ngTemplateOutlet]="nonIsmsTemplate" />
      </div>
    }
  }

  <!-- ── Loading ────────────────────────────────────────────────────────── -->
  @if (activeProjectId() && dashQuery.isLoading()) {
    <app-page-header [title]="'Compliance Overview'" subtitle="Loading…" />
    <div class="skeletons">
      @for (n of [1,2,3,4,5,6]; track n) {
        <div class="skeleton-card"></div>
      }
    </div>
  }

  <!-- ── Error ──────────────────────────────────────────────────────────── -->
  @if (activeProjectId() && dashQuery.isError()) {
    <app-page-header [title]="'Compliance Overview'" />
    <mat-card>
      <mat-card-content class="msg-row">
        <mat-icon color="warn">error_outline</mat-icon>
        <span>Failed to load dashboard data.</span>
      </mat-card-content>
    </mat-card>
  }

  <!-- ── Non-ISMS product (privacy / cloud / ai) with active project ────── -->
  @if (activeProjectId() && dashQuery.isSuccess() && product.product() !== 'isms') {
    <app-page-header [title]="'Compliance Overview'" [subtitle]="nonIsmsSubtitle()" />
    <ng-container [ngTemplateOutlet]="nonIsmsTemplate" />
  }

  <!-- ── ISMS main view ─────────────────────────────────────────────────── -->
  @if (activeProjectId() && dashQuery.isSuccess() && product.product() === 'isms') {

    <app-page-header [title]="'Compliance Overview'" [subtitle]="headerSubtitle()">
      <div actions class="header-actions">
        @if (readiness()) {
          <span class="readiness-label">Audit readiness</span>
          <app-status-chip [status]="readiness()!.status" />
          <span class="readiness-score" [style.color]="scoreColor()">
            {{ compositeScore() }}%
          </span>
        }
        <button mat-stroked-button (click)="router.navigate(['/report'])">
          <mat-icon>download</mat-icon>
          Export Report
        </button>
      </div>
    </app-page-header>

    <!-- Metric row -->
    <div class="metrics-grid">
      <app-metric-card title="Controls"        [value]="ov()?.total_controls ?? 0"        icon="account_tree" />
      <app-metric-card title="Policies"        [value]="ov()?.total_policies ?? 0"        icon="policy" />
      <app-metric-card title="Implementations" [value]="ov()?.total_implementations ?? 0" icon="description" />
      <app-metric-card title="Assessments"     [value]="ov()?.total_assessments ?? 0"     icon="assignment" />
      <app-metric-card
        title="Framework"
        [value]="fmtPct(frameworkPct())"
        subtitle="coverage"
        [progress]="frameworkPct()"
        progressColor="primary"
      />
      <app-metric-card
        title="Operational"
        [value]="fmtPct(operationalPct())"
        subtitle="coverage"
        [progress]="operationalPct()"
        progressColor="primary"
      />
    </div>

    <!-- Intelligence cards -->
    <div class="intel-section">
      <div class="intel-section__header">
        <mat-icon class="intel-section__icon">stream</mat-icon>
        <span>Intelligence</span>
      </div>
      <div class="intel-cards">
        <mat-card class="intel-card" (click)="router.navigate(['/cve-explorer'])">
          <mat-card-content>
            <div class="intel-card__row">
              <mat-icon class="intel-icon intel-icon--cve">bug_report</mat-icon>
              <span class="intel-card__label">CVE Index</span>
            </div>
            <div class="intel-card__value intel-val--cve">{{ fmt(nvdStats()?.cve_total) }}</div>
            <div class="intel-card__sub">{{ nvdStats()?.cpe_total ? fmt(nvdStats()!.cpe_total) + ' CPEs' : 'Enable FEEDS_CVE_ENABLED' }}</div>
          </mat-card-content>
        </mat-card>

        <mat-card class="intel-card" (click)="router.navigate(['/threat-feeds'])">
          <mat-card-content>
            <div class="intel-card__row">
              <mat-icon class="intel-icon" [style.color]="theme.isDark() ? '#FFEB9C' : '#9a6500'">warning_amber</mat-icon>
              <span class="intel-card__label">CISA KEV</span>
            </div>
            <div class="intel-card__value" [style.color]="theme.isDark() ? '#FFEB9C' : '#9a6500'">
              {{ fmt(kevStats()?.total_entries) }}
            </div>
            <div class="intel-card__sub">
              @if (kevStats()?.recent_30d != null) { {{ kevStats()!.recent_30d }} added last 30d }
            </div>
          </mat-card-content>
        </mat-card>

        <mat-card class="intel-card" (click)="router.navigate(['/mitre-attack'])">
          <mat-card-content>
            <div class="intel-card__row">
              <mat-icon class="intel-icon intel-icon--mitre">security</mat-icon>
              <span class="intel-card__label">MITRE ATT&amp;CK</span>
            </div>
            <div class="intel-card__value intel-val--mitre">
              {{ attackTotal() > 0 ? fmt(attackTotal()) : '—' }}
            </div>
            <div class="intel-card__sub">
              @if (attackStats()) {
                {{ attackStats()!.total_techniques }} techniques · {{ attackStats()!.total_subtechniques }} sub
              }
            </div>
          </mat-card-content>
        </mat-card>

        <mat-card class="intel-card" (click)="router.navigate(['/threat-feeds'])">
          <mat-card-content>
            <div class="intel-card__row">
              @if (anyFeedError()) {
                <mat-icon class="intel-icon" [style.color]="theme.isDark() ? '#FFC7CE' : '#9e0000'">error_outline</mat-icon>
              } @else {
                <mat-icon class="intel-icon" [style.color]="theme.isDark() ? '#C6EFCE' : '#1b5e20'">check_circle</mat-icon>
              }
              <span class="intel-card__label">Feed Status</span>
            </div>
            <div class="intel-card__value"
                 [style.color]="anyFeedError() ? (theme.isDark() ? '#FFC7CE' : '#9e0000') : (theme.isDark() ? '#C6EFCE' : '#1b5e20')">
              {{ anyFeedError() ? (failedFeedsCount() + ' failure' + (failedFeedsCount() > 1 ? 's' : '')) : 'All OK' }}
            </div>
            <div class="intel-card__sub">
              {{ anyFeedError() ? failedFeedNames() : ((feedStatus()?.feeds?.length ?? 0) + ' feeds active') }}
            </div>
          </mat-card-content>
        </mat-card>
      </div>
    </div>

    <!-- Section breakdown -->
    <app-expandable-card [expandable]="true" [initiallyExpanded]="true">
      <span card-title>
        <mat-icon>account_tree</mat-icon>
        Controls Covered by Section
      </span>
        @for (s of ismsSection(); track s.section) {
          <div class="section-row"
               (click)="router.navigate(['/controls'], { queryParams: { section: s.section } })">
            <div class="section-row__head">
              <div class="section-row__left">
                <div class="section-dot" [style.background]="sectionColor(s.section)"></div>
                <span class="section-row__name">{{ s.section }} — {{ s.section_name }}</span>
                <span class="section-row__count">({{ s.total_controls }} control{{ s.total_controls !== 1 ? 's' : '' }})</span>
              </div>
              <mat-icon class="section-row__arrow">chevron_right</mat-icon>
            </div>
            <div class="section-row__bars">
              <div class="bar-group">
                <div class="bar-label">
                  <span>Framework</span>
                  <span>{{ fmtPct(s.framework_pct) }}</span>
                </div>
                <div class="progress-track">
                  <div class="progress-fill progress-fill--fw" [style.width.%]="clamp(s.framework_pct)"></div>
                </div>
              </div>
              <div class="bar-group">
                <div class="bar-label">
                  <span>Operational</span>
                  <span>{{ fmtPct(s.operational_pct) }}</span>
                </div>
                <div class="progress-track">
                  <div class="progress-fill progress-fill--op" [style.width.%]="clamp(s.operational_pct)"></div>
                </div>
              </div>
            </div>
          </div>
        }
    </app-expandable-card>

    <!-- Audit Readiness breakdown -->
    @if (readiness()) {
      <app-expandable-card [expandable]="true" [initiallyExpanded]="true">
        <span card-title>
          <mat-icon>verified</mat-icon>
          Audit Readiness Breakdown
          <span class="readiness-score" [style.color]="scoreColor()">{{ compositeScore() }}%</span>
        </span>
          @for (item of readinessItems(); track item.name) {
            <div class="readiness-item">
              <div class="bar-label">
                <span>{{ item.name }}</span>
                <span class="readiness-pct">{{ fmtPct(item.value) }}</span>
              </div>
              <div class="progress-track">
                <div class="progress-fill"
                     [style.width.%]="clamp(item.value)"
                     [style.background]="rdBarColor(item.value)">
                </div>
              </div>
            </div>
          }
      </app-expandable-card>
    }

    <!-- Top Mapped Frameworks (cross-framework mapping coverage) -->
    @if (topTargets().length > 0) {
      <app-expandable-card [expandable]="true" [initiallyExpanded]="true">
        <span card-title>
          <mat-icon>hub</mat-icon>
          Top Mapped Frameworks
        </span>
          @for (item of topTargets(); track item.name) {
            <div class="top-fw-row">
              <div class="bar-label">
                <span class="top-fw-name" [matTooltip]="item.name">{{ item.name }}</span>
                <span class="fw-count">{{ item.count }}</span>
              </div>
              <div class="progress-track">
                <div class="progress-fill" [style.width.%]="item.pct" [style.background]="productColor()"></div>
              </div>
            </div>
          }
      </app-expandable-card>
    }
  }

</div>

<!-- ── Non-ISMS template ───────────────────────────────────────────────────── -->
<ng-template #nonIsmsTemplate>

  @if (fwOverviewQuery.isLoading()) {
    <div class="skeletons">
      @for (n of [1,2,3,4]; track n) { <div class="skeleton-card"></div> }
    </div>
  }

  @if (fwOverviewQuery.isSuccess() && fwOverview()) {
    <div class="fw-overview-content">
      @if (product.product() === 'cloud') {
        <div class="cloud-toggle">
          @for (opt of cloudOptions; track opt.value) {
            <div class="cloud-opt"
                 [class.cloud-opt--active]="cloudSub() === opt.value"
                 (click)="cloudSub.set(opt.value)">
              <span class="cloud-opt__label">{{ opt.label }}</span>
              <span class="cloud-opt__sep"> · </span>
              <span class="cloud-opt__desc">{{ opt.desc }}</span>
            </div>
          }
        </div>
      }
      <div class="metrics-grid">
        <app-metric-card title="Controls"         [value]="fwOverview()!.total_controls"              icon="account_tree" />
        <app-metric-card title="Controls Mapped"  [value]="fwOverview()!.controls_with_mappings"      icon="hub" />
        <app-metric-card title="Total Mappings"   [value]="fmt(fwOverview()!.total_mappings)"         icon="compare_arrows" />
        <app-metric-card title="Implementations"  [value]="fwOverview()!.total_implementations"       icon="description" />
        <app-metric-card title="Assessments"      [value]="fwOverview()!.total_assessments"           icon="assignment" />
        <app-metric-card
          title="Coverage"
          [value]="fmtPct(fwOverview()!.coverage_pct)"
          subtitle="controls mapped"
          [progress]="fwOverview()!.coverage_pct"
          progressColor="primary"
          icon="donut_large"
        />
      </div>

      @if (topTargets().length > 0) {
        <app-expandable-card [expandable]="true" [initiallyExpanded]="true">
          <span card-title>
            <mat-icon>hub</mat-icon>
            Top Mapped Frameworks
          </span>
            @for (item of topTargets(); track item.name) {
              <div class="top-fw-row">
                <div class="bar-label">
                  <span class="top-fw-name" [matTooltip]="item.name">{{ item.name }}</span>
                  <span class="fw-count">{{ item.count }}</span>
                </div>
                <div class="progress-track">
                  <div class="progress-fill" [style.width.%]="item.pct" [style.background]="productColor()"></div>
                </div>
              </div>
            }
        </app-expandable-card>
      }

      @if (fwOverview()!.total_mappings === 0) {
        <mat-card>
          <mat-card-content class="msg-row">
            <mat-icon>info</mat-icon>
            <span>No cross-framework mappings loaded yet. Import mapping datasets to populate this view.</span>
          </mat-card-content>
        </mat-card>
      }
    </div>
  }
</ng-template>
  `,
  styles: [`
    .overview-page {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    /* ── No project ── */
    .no-project-card mat-card-content { padding: 24px !important; }
    .no-project-inner {
      display: flex;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
    }
    .no-project-icon {
      font-size: 40px; width: 40px; height: 40px;
      color: var(--mat-sys-on-surface-variant);
      opacity: 0.4;
      flex-shrink: 0;
    }
    .no-project-text { flex: 1; min-width: 180px; }
    .no-project-title { font-size: 1rem; font-weight: 600; color: var(--mat-sys-on-surface); }
    .no-project-sub { font-size: 0.85rem; color: var(--mat-sys-on-surface-variant); margin-top: 4px; }

    /* ── Skeletons ── */
    .skeletons {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
      gap: 12px;
    }
    .skeleton-card {
      height: 110px;
      border-radius: 8px;
      background: var(--mat-sys-surface-container-high);
      animation: pulse 1.5s ease-in-out infinite;
    }
    @keyframes pulse { 0%,100% { opacity:1 } 50% { opacity:0.45 } }

    /* ── Header actions ── */
    .header-actions {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }
    .readiness-label { font-size: 0.78rem; color: var(--mat-sys-on-surface-variant); }
    .readiness-score { font-size: 1.4rem; font-weight: 700; line-height: 1; }

    /* ── Non-ISMS overview wrapper ── */
    .fw-overview-content {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    /* ── Metrics ── */
    .metrics-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(175px, 1fr));
      gap: 12px;
    }

    /* ── Intelligence ── */
    .intel-section { display: flex; flex-direction: column; gap: 8px; }
    .intel-section__header {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 0.62rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.07em;
      color: #9c27b0;
    }
    .intel-section__icon { font-size: 14px; width: 14px; height: 14px; }
    .intel-cards { display: flex; gap: 12px; flex-wrap: wrap; }
    .intel-card {
      flex: 1 1 140px;
      min-width: 130px;
      cursor: pointer;
      transition: box-shadow 0.15s;
    }
    .intel-card:hover { box-shadow: 0 2px 8px rgba(0,0,0,0.2); }
    .intel-card mat-card-content { padding: 12px !important; }
    .intel-card__row {
      display: flex; align-items: center; gap: 6px; margin-bottom: 4px;
    }
    .intel-card__label { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
    .intel-card__value { font-size: 1.1rem; font-weight: 700; line-height: 1.2; }
    .intel-card__sub {
      font-size: 0.68rem;
      color: var(--mat-sys-on-surface-variant);
      margin-top: 2px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    /* ── Shared ── */
    mat-card-content { padding: 16px !important; }
    .card-title {
      font-size: 1rem; font-weight: 600;
      color: var(--mat-sys-on-surface);
      margin-bottom: 12px;
    }
    .msg-row {
      display: flex; align-items: center; gap: 8px;
      font-size: 0.875rem; color: var(--mat-sys-on-surface-variant);
    }

    /* ── Section breakdown ── */
    .section-row {
      margin-bottom: 10px;
      padding: 4px 6px;
      border-radius: 4px;
      cursor: pointer;
      transition: background 0.1s;
    }
    .section-row:hover { background: rgba(68,114,196,0.06); }
    .section-row__head {
      display: flex; align-items: center;
      justify-content: space-between; margin-bottom: 6px;
    }
    .section-row__left { display: flex; align-items: center; gap: 8px; }
    .section-dot { width: 3px; height: 16px; border-radius: 2px; flex-shrink: 0; }
    .section-row__name { font-size: 0.85rem; font-weight: 600; color: var(--mat-sys-on-surface); }
    .section-row__count { font-size: 0.73rem; color: var(--mat-sys-on-surface-variant); }
    .section-row__arrow { font-size: 16px; width: 16px; height: 16px; color: var(--mat-sys-on-surface-variant); opacity: 0.4; }
    .section-row__bars {
      display: grid; grid-template-columns: 1fr 1fr; gap: 8px;
    }

    /* ── Bars ── */
    .bar-group { display: flex; flex-direction: column; gap: 3px; }
    .bar-label {
      display: flex; justify-content: space-between;
      font-size: 0.7rem; color: var(--mat-sys-on-surface-variant);
    }
    .progress-track {
      height: 4px; border-radius: 2px;
      background: var(--mat-sys-surface-container-high);
      overflow: hidden;
    }
    .progress-fill { height: 100%; border-radius: 2px; transition: width 0.3s; }

    /* ── Readiness ── */
    .readiness-head {
      display: flex; align-items: baseline;
      justify-content: space-between; margin-bottom: 12px;
    }
    .readiness-item { margin-bottom: 10px; display: flex; flex-direction: column; gap: 4px; }
    .readiness-pct { font-weight: 600; color: var(--mat-sys-on-surface); }

    /* ── Cloud toggle ── */
    .cloud-toggle { display: flex; gap: 8px; flex-wrap: wrap; }
    .cloud-opt {
      padding: 6px 12px; border-radius: 4px; cursor: pointer;
      border: 1px solid var(--mat-sys-outline-variant);
      background: var(--mat-sys-surface-container);
      transition: border-color 0.15s, background 0.15s;
    }
    .cloud-opt--active { border-color: #29b6f6; background: rgba(41,182,246,0.12); }
    .cloud-opt__label { font-size: 0.75rem; font-weight: 600; color: var(--mat-sys-on-surface); }
    .cloud-opt__sep  { font-size: 0.7rem; color: var(--mat-sys-on-surface-variant); opacity: .5; }
    .cloud-opt__desc { font-size: 0.7rem; color: var(--mat-sys-on-surface-variant); }

    /* ── Top fw ── */
    .top-fw-row { margin-bottom: 8px; display: flex; flex-direction: column; gap: 3px; }
    .top-fw-name {
      font-size: 0.72rem; color: var(--mat-sys-on-surface-variant);
      max-width: 220px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
    }

    .fw-section-mt { margin-top: 8px; }
    .intel-icon { font-size: 18px; width: 18px; height: 18px; }
    .intel-icon--cve   { color: #f44336; }
    .intel-icon--mitre { color: #9c27b0; }
    .intel-val--cve   { color: #f44336; }
    .intel-val--mitre { color: #9c27b0; }
    .progress-fill--fw { background: #327df4; }
    .progress-fill--op { background: #00c752; }
    .card-mt { margin-top: 12px; }
    .fw-count { font-size: 0.75rem; font-weight: 600; }
  `],
})
export class OverviewComponent {
  readonly router  = inject(Router)
  readonly product = inject(ProductService)
  readonly theme   = inject(ThemeService)
  private dashApi  = inject(DashboardApiService)
  private feedsApi = inject(FeedsApiService)
  private projSvc  = inject(ProjectService)

  // ── Cloud sub-framework toggle ───────────────────────────────────────────────
  readonly cloudSub = signal<'ISO27017' | 'ISO27018'>('ISO27017')
  readonly cloudOptions = [
    { value: 'ISO27017' as const, label: 'ISO 27017', desc: 'Cloud Security' },
    { value: 'ISO27018' as const, label: 'ISO 27018', desc: 'PII in Cloud' },
  ]

  // ── Active project for current product ──────────────────────────────────────
  readonly activeProjectId = computed(() => {
    const p = this.product.product()
    const fam = p === 'isms' ? 'ISMS' : p === 'privacy' ? 'PRIVACY' : p === 'cloud' ? 'CLOUD' : 'AI'
    return this.projSvc.getActiveProject(fam)?.id ?? null
  })

  readonly pageSubtitle = computed(() => PRODUCT_SUBTITLES[this.product.product()] ?? '')

  readonly headerSubtitle = computed(() =>
    `${this.ov()?.total_controls ?? 0} control groups · ${PRODUCT_SUBTITLES['isms']}`
  )

  readonly nonIsmsSubtitle = computed(() => {
    const p = this.product.product()
    const fw = p === 'cloud'
      ? (this.cloudSub() === 'ISO27017' ? 'Cloud Security' : 'PII in Cloud')
      : p === 'ai' ? 'AI Management System'
      : 'Privacy Extension'
    return `${PRODUCT_SUBTITLES[p]} · ${fw}`
  })

  // ── Dashboard query ──────────────────────────────────────────────────────────
  readonly dashQuery = injectQuery(() => ({
    queryKey: ['dashboard', 'main', this.activeProjectId(), this.product.product()],
    queryFn:  () => firstValueFrom(this.dashApi.get(this.activeProjectId()!, this.product.product())),
    enabled:  !!this.activeProjectId(),
    staleTime: 60_000,
  }))

  readonly ov        = computed(() => this.dashQuery.data()?.overview as unknown as RealOverview | undefined)
  readonly readiness = computed(() => this.dashQuery.data()?.audit_readiness as unknown as RealReadiness | undefined)

  readonly frameworkPct   = computed(() => (this.ov() as any)?.framework?.coverage_pct ?? 0)
  readonly operationalPct = computed(() => (this.ov() as any)?.operational?.coverage_pct ?? 0)
  readonly compositeScore = computed(() => this.readiness()?.composite_score ?? 0)

  readonly scoreColor = computed(() =>
    readinessScoreColor(this.readiness()?.status ?? 'red', this.theme.isDark())
  )

  readonly ismsSection = computed(() =>
    (this.ov()?.sections ?? []).filter(s => !['A.0', '00'].includes(s.section))
  )

  readonly readinessItems = computed(() => {
    const rd = this.readiness()
    if (!rd) return []
    return [
      { name: 'Policies',    value: rd.policies_pct    ?? (rd.components as any)?.policies      ?? 0 },
      { name: 'User Guides', value: rd.ug_pct          ?? (rd.components as any)?.user_guides   ?? 0 },
      { name: 'Tech Guides', value: rd.tg_pct          ?? (rd.components as any)?.technical_guides ?? 0 },
      { name: 'Assessments', value: rd.assessments_pct ?? (rd.components as any)?.assessments   ?? 0 },
      { name: 'Evidence',    value: rd.evidence_pct    ?? (rd.components as any)?.evidence      ?? 0 },
      { name: 'Gaps Closed', value: rd.gaps_closed_pct ?? (rd.components as any)?.gaps          ?? 0 },
    ]
  })

  // ── Intelligence feed queries ────────────────────────────────────────────────
  readonly kevQuery = injectQuery(() => ({
    queryKey: ['feeds', 'kev', 'stats'],
    queryFn:  () => firstValueFrom(this.feedsApi.getKevStats()),
    staleTime: 5 * 60_000,
  }))
  readonly attackQuery = injectQuery(() => ({
    queryKey: ['feeds', 'attack', 'stats'],
    queryFn:  () => firstValueFrom(this.feedsApi.getAttackStats()),
    staleTime: 5 * 60_000,
  }))
  readonly nvdStatsQuery = injectQuery(() => ({
    queryKey: ['nvd', 'index-stats'],
    queryFn:  () => firstValueFrom(this.feedsApi.getNvdIndexStats()),
    staleTime: 5 * 60_000,
  }))
  readonly feedStatusQuery = injectQuery(() => ({
    queryKey: ['feeds', 'status'],
    queryFn:  () => firstValueFrom(this.feedsApi.getStatus()),
    staleTime: 5 * 60_000,
  }))

  readonly kevStats    = computed(() => this.kevQuery.data())
  readonly attackStats = computed(() => this.attackQuery.data())
  readonly nvdStats    = computed(() => this.nvdStatsQuery.data())
  readonly feedStatus  = computed(() => this.feedStatusQuery.data())

  readonly attackTotal      = computed(() => { const s = this.attackStats(); return s ? s.total_techniques + s.total_subtechniques : 0 })
  readonly failedFeeds      = computed(() => (this.feedStatus()?.feeds ?? []).filter(f => f.last_status === 'error'))
  readonly anyFeedError     = computed(() => this.failedFeeds().length > 0)
  readonly failedFeedsCount = computed(() => this.failedFeeds().length)
  readonly failedFeedNames  = computed(() => this.failedFeeds().map(f => f.display_name).join(', '))

  // ── Framework overview (all products) ────────────────────────────────────────
  readonly sourceFramework = computed(() => {
    const p = this.product.product()
    if (p === 'cloud') return this.cloudSub()
    if (p === 'ai')    return 'ISO42001'
    if (p === 'isms')  return 'ISO27001'
    return 'ISO27701'
  })

  readonly fwOverviewQuery = injectQuery(() => ({
    queryKey: ['dashboard', 'framework-overview', this.sourceFramework()],
    queryFn:  () => firstValueFrom(this.dashApi.getFrameworkOverview(this.sourceFramework())),
    enabled:  true,
    staleTime: 60_000,
  }))

  readonly fwOverview   = computed(() => this.fwOverviewQuery.data() as FrameworkOverview | undefined)
  readonly productColor = computed(() => PRODUCT_COLORS[this.product.product()])

  readonly topTargets = computed(() => {
    const fw = this.fwOverview()
    if (!fw) return []
    const entries = Object.entries(fw.by_target_framework).sort((a, b) => b[1] - a[1]).slice(0, 8)
    const max = entries[0]?.[1] ?? 1
    return entries.map(([name, count]) => ({ name, count, pct: Math.min(100, (count / max) * 100) }))
  })

  // ── Template helpers ─────────────────────────────────────────────────────────
  sectionColor(s: string): string { return sectionColor(s) }
  clamp(v: number): number        { return clamp(v) }
  fmt(n: number | null | undefined): string  { return fmt(n) }
  fmtPct(n: number | null | undefined): string { return fmtPct(n) }
  rdBarColor(v: number): string   { return progressBarColor(v, this.theme.isDark()) }
}
