import { Component, inject, signal, computed } from '@angular/core'
import { DecimalPipe } from '@angular/common'
import { firstValueFrom } from 'rxjs'

import { injectQuery } from '@tanstack/angular-query-experimental'

import { MatCardModule } from '@angular/material/card'
import { MatButtonModule } from '@angular/material/button'
import { MatIconModule } from '@angular/material/icon'
import { MatChipsModule } from '@angular/material/chips'
import { MatButtonToggleModule } from '@angular/material/button-toggle'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'

import { DashboardApiService } from '../../api/dashboard-api.service'
import { ControlsApiService } from '../../api/controls-api.service'
import { ProductService, PRODUCT_COLORS, PRODUCT_LABELS, Product } from '../../core/services/product.service'
import { ProjectService } from '../../core/services/project.service'
import { ThemeService } from '../../core/services/theme.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

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
  framework: { coverage_pct: number; has_policy: number; has_ug: number; has_tg: number; has_assessment: number }
  operational: { coverage_pct: number }
  sections: SectionRow[]
}

interface RealReadiness {
  policies_pct: number
  ug_pct: number
  tg_pct: number
  assessments_pct: number
  evidence_pct: number
  gaps_closed_pct: number
  composite_score: number
  status: 'green' | 'amber' | 'red'
}

interface GroupRow {
  id: string
  group_code: string
  name: string
  section: string
  section_name: string
  has_framework: boolean
  has_implementation: boolean
  product_family: string
}

// ── Constants ─────────────────────────────────────────────────────────────────

const STATUS_LABEL: Record<string, string> = {
  green: 'Compliant', amber: 'Partially Compliant', red: 'Non-Compliant',
}
const STATUS_BG_DARK: Record<string, string>  = { green: '#1a3a27', amber: '#3a2e00', red: '#3a0000' }
const STATUS_BG_LIGHT: Record<string, string> = { green: 'rgba(46,125,50,.12)', amber: 'rgba(230,160,0,.12)', red: 'rgba(192,0,0,.12)' }
const STATUS_FG_DARK: Record<string, string>  = { green: '#C6EFCE', amber: '#FFEB9C', red: '#FFC7CE' }
const STATUS_FG_LIGHT: Record<string, string> = { green: '#1b5e20', amber: '#7a4800', red: '#9e0000' }

const STANDARD_NAMES: Record<Product, string> = {
  isms:    'ISO/IEC 27001:2022',
  privacy: 'ISO/IEC 27701:2025',
  cloud:   'ISO/IEC 27018:2025',
  ai:      'ISO/IEC 42001:2023',
}
const HEADER_COLORS: Record<Product, string> = {
  isms:    '#4472C4',
  privacy: PRODUCT_COLORS.privacy,
  cloud:   PRODUCT_COLORS.cloud,
  ai:      PRODUCT_COLORS.ai,
}

function pct(v: number): string { return `${v.toFixed(0)}%` }

// ── Component ─────────────────────────────────────────────────────────────────

@Component({
  selector: 'app-report',
  standalone: true,
  imports: [
    DecimalPipe,
    MatCardModule, MatButtonModule, MatIconModule, MatChipsModule,
    MatButtonToggleModule, MatProgressSpinnerModule,
    PageHeaderComponent,
  ],
  template: `
<div class="report-root">

  <!-- Action bar (hidden in print) -->
  <div class="no-print action-bar">
    <mat-button-toggle-group [value]="reportProduct()" (change)="reportProduct.set($event.value)">
      @for (p of products; track p) {
        <mat-button-toggle [value]="p"
          [style.background]="reportProduct() === p ? headerColor(p) + '22' : undefined"
          [style.color]="reportProduct() === p ? headerColor(p) : undefined"
          class="product-toggle">
          {{ productLabel(p) }}
        </mat-button-toggle>
      }
    </mat-button-toggle-group>

    <button mat-flat-button color="primary" (click)="print()">
      <mat-icon>print</mat-icon> Print / Save as PDF
    </button>

    @if (reportProduct() === 'isms') {
      <button mat-stroked-button (click)="exportCsv()" [disabled]="!overviewQuery.data()">
        <mat-icon>file_download</mat-icon> Export CSV
      </button>
    }
  </div>

  <!-- Report body -->
  @if (isLoading()) {
    <div class="skeleton-wrap">
      @for (h of [80, 200, 300]; track h) {
        <div class="skeleton-block" [style.height.px]="h"></div>
      }
    </div>
  }

  @if (!isLoading()) {
    <div class="report-body">

      <!-- ══ Report header ══ -->
      <div class="report-header" [style.borderBottomColor]="headerColor(reportProduct())">
        <h1 class="report-title">ISMS CORE — {{ productLabel(reportProduct()) }} Compliance Report</h1>
        <div class="report-subtitle">{{ standardName(reportProduct()) }} · Generated {{ generatedDate }}</div>
      </div>

      <!-- ══ ISMS ══ -->
      @if (reportProduct() === 'isms') {
        @let ov = overviewQuery.data();
        @let rd = readinessQuery.data();

        <!-- 1 — Executive Summary -->
        <div class="report-section">
          <h2 class="section-heading">1 — Executive Summary</h2>
          @if (rd) {
            <div class="score-row">
              <div class="score-box" [style.background]="statusBg(rd.status)" [style.borderColor]="statusFg(rd.status) + '40'">
                <div class="score-value" [style.color]="statusFg(rd.status)">{{ rd.composite_score }}%</div>
                <div class="score-label" [style.color]="statusFg(rd.status)">Composite Score</div>
              </div>
              <div>
                <div class="status-chip" [style.background]="statusBg(rd.status)" [style.color]="statusFg(rd.status)">{{ statusLabel(rd.status) }}</div>
                <div class="posture-label">ISO/IEC 27001:2022 Annex A compliance posture</div>
              </div>
            </div>
          }
          <table class="summary-table">
            @for (row of ismsSummaryRows(); track row.label) {
              <tr><td class="td-label">{{ row.label }}</td><td class="td-value">{{ row.value }}</td></tr>
            }
          </table>
        </div>
        <hr class="section-divider">

        <!-- 2 — Coverage by Section -->
        @if (ov) {
          <div class="report-section">
            <h2 class="section-heading">2 — Coverage by Section</h2>
            <table class="data-table data-table--full">
              <thead>
                <tr>
                  <th class="th">Section</th>
                  <th class="th">Name</th>
                  <th class="th th--center">Controls</th>
                  <th class="th th--center">Framework %</th>
                  <th class="th th--center">Operational %</th>
                </tr>
              </thead>
              <tbody>
                @for (s of ov.sections; track s.section; let even = $even) {
                  <tr [class.tr-even]="even">
                    <td class="td td--mono td--bold">{{ s.section }}</td>
                    <td class="td">{{ s.section_name }}</td>
                    <td class="td td--center">{{ s.total_controls }}</td>
                    <td class="td td--center">{{ pct(s.framework_pct) }}</td>
                    <td class="td td--center">{{ pct(s.operational_pct) }}</td>
                  </tr>
                }
              </tbody>
            </table>
          </div>
          <hr class="section-divider">
        }

        <!-- 3 — Audit Readiness -->
        @if (rd) {
          <div class="report-section">
            <h2 class="section-heading">3 — Audit Readiness Breakdown</h2>
            <table class="data-table data-table--min400">
              <thead>
                <tr>
                  <th class="th">Component</th>
                  <th class="th th--center">Score</th>
                  <th class="th th--center">Status</th>
                </tr>
              </thead>
              <tbody>
                @for (r of ismsReadinessRows(); track r.name; let even = $even) {
                  <tr [class.tr-even]="even">
                    <td class="td td--bold">{{ r.name }}</td>
                    <td class="td td--center">{{ pct(r.value) }}</td>
                    <td class="td td--center">
                      <span class="status-badge"
                        [style.background]="statusBg(r.value >= 80 ? 'green' : r.value >= 50 ? 'amber' : 'red')"
                        [style.color]="statusFg(r.value >= 80 ? 'green' : r.value >= 50 ? 'amber' : 'red')">
                        {{ r.value >= 80 ? 'Good' : r.value >= 50 ? 'Partial' : 'Attention' }}
                      </span>
                    </td>
                  </tr>
                }
              </tbody>
            </table>
          </div>
          <hr class="section-divider">
        }

        <!-- 4 — Framework vs Operational -->
        @if (ov) {
          <div class="report-section">
            <h2 class="section-heading">4 — Framework vs Operational Coverage</h2>
            <table class="data-table data-table--min400">
              <thead>
                <tr>
                  <th class="th">Product</th>
                  <th class="th th--center">Total Controls</th>
                  <th class="th th--center">Coverage %</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td class="td td--bold">Framework</td>
                  <td class="td td--center">{{ ov.total_controls }}</td>
                  <td class="td td--center">{{ pct(ov.framework.coverage_pct) }}</td>
                </tr>
                <tr class="tr-even">
                  <td class="td td--bold">Operational</td>
                  <td class="td td--center">{{ ov.total_controls }}</td>
                  <td class="td td--center">{{ pct(ov.operational.coverage_pct) }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        }
      }

      <!-- ══ Privacy / Cloud / AI — unified structure ══ -->
      @if (reportProduct() !== 'isms') {
        @let summary = productSummary();
        @let groups  = groupsQuery.data();

        @if (summary) {
          @let score     = Math.round((summary.pol_coverage_pct + summary.impl_coverage_pct) / 2);
          @let rdStatus  = score >= 90 ? 'green' : score >= 60 ? 'amber' : 'red';

          <!-- 1 — Executive Summary -->
          <div class="report-section">
            <h2 class="section-heading">1 — Executive Summary</h2>
            <div class="score-row">
              <div class="score-box" [style.background]="statusBg(rdStatus)" [style.borderColor]="statusFg(rdStatus) + '40'">
                <div class="score-value" [style.color]="statusFg(rdStatus)">{{ score }}%</div>
                <div class="score-label" [style.color]="statusFg(rdStatus)">Composite Score</div>
              </div>
              <div>
                <div class="status-chip" [style.background]="statusBg(rdStatus)" [style.color]="statusFg(rdStatus)">{{ statusLabel(rdStatus) }}</div>
                <div class="posture-label">{{ standardName(reportProduct()) }} compliance posture</div>
              </div>
            </div>
            <table class="summary-table">
              @for (row of extSummaryRowsComputed(); track row.label) {
                <tr><td class="td-label">{{ row.label }}</td><td class="td-value">{{ row.value }}</td></tr>
              }
            </table>
          </div>
          <hr class="section-divider">

          <!-- 2 — Coverage by Control Group -->
          @if (groups && groups.length > 0) {
            <div class="report-section">
              <h2 class="section-heading">2 — Coverage by Control Group</h2>
              @for (sec of bySection($any(groups)); track sec.section) {
                <div class="section-group">
                  <div class="section-group-header">
                    <span class="mono">{{ sec.section }}</span>
                    <span class="section-group-name">— {{ sec.section_name }}</span>
                  </div>
                  <table class="data-table data-table--full">
                    <thead>
                      <tr>
                        <th class="th th--code">Code</th>
                        <th class="th">Control Group</th>
                        <th class="th th--center th--badge">Policy</th>
                        <th class="th th--center th--badge">Implementation</th>
                      </tr>
                    </thead>
                    <tbody>
                      @for (g of sec.rows; track g.id; let even = $even) {
                        <tr [class.tr-even]="even">
                          <td class="td td--mono td--bold td--nowrap">{{ g.group_code }}</td>
                          <td class="td">{{ g.name }}</td>
                          <td class="td td--center">
                            <span class="status-badge"
                              [style.background]="statusBg(g.has_framework ? 'green' : 'red')"
                              [style.color]="statusFg(g.has_framework ? 'green' : 'red')">
                              {{ g.has_framework ? '✓' : '✗' }}
                            </span>
                          </td>
                          <td class="td td--center">
                            <span class="status-badge"
                              [style.background]="statusBg(g.has_implementation ? 'green' : 'red')"
                              [style.color]="statusFg(g.has_implementation ? 'green' : 'red')">
                              {{ g.has_implementation ? '✓' : '✗' }}
                            </span>
                          </td>
                        </tr>
                      }
                    </tbody>
                  </table>
                </div>
              }
            </div>
            <hr class="section-divider">
          }

          <!-- 3 — Audit Readiness Breakdown -->
          <div class="report-section">
            <h2 class="section-heading">3 — Audit Readiness Breakdown</h2>
            <table class="data-table data-table--min400">
              <thead>
                <tr>
                  <th class="th">Component</th>
                  <th class="th th--center">Score</th>
                  <th class="th th--center">Status</th>
                </tr>
              </thead>
              <tbody>
                @for (r of extReadinessRows(); track r.name; let even = $even) {
                  <tr [class.tr-even]="even">
                    <td class="td td--bold">{{ r.name }}</td>
                    <td class="td td--center">{{ pct(r.value) }}</td>
                    <td class="td td--center">
                      <span class="status-badge"
                        [style.background]="statusBg(r.value >= 80 ? 'green' : r.value >= 50 ? 'amber' : 'red')"
                        [style.color]="statusFg(r.value >= 80 ? 'green' : r.value >= 50 ? 'amber' : 'red')">
                        {{ r.value >= 80 ? 'Good' : r.value >= 50 ? 'Partial' : 'Attention' }}
                      </span>
                    </td>
                  </tr>
                }
              </tbody>
            </table>
          </div>
        }
      }

      <!-- Footer -->
      <hr class="footer-divider">
      <div class="report-footer">
        Generated by ISMS CORE · {{ standardName(reportProduct()) }} · {{ generatedDate }}
      </div>
    </div>
  }
</div>
`,
  styles: [`
    :host { display: block; }

    /* Layout */
    .report-root { padding: 0 4px; }
    .action-bar { display: flex; align-items: center; gap: 12px; margin-bottom: 24px; flex-wrap: wrap; }
    .product-toggle { font-size: .72rem; padding: 0 12px; }

    /* Skeleton loader */
    .skeleton-wrap { padding: 32px; }
    .skeleton-block { background: rgba(255,255,255,.06); border-radius: 8px; margin-bottom: 16px; }

    /* Report body */
    .report-body {
      background: white; color: #1a1a2e; padding: 40px; border-radius: 8px;
      max-width: 900px; margin: 0 auto; box-shadow: 0 2px 12px rgba(0,0,0,.18);
    }

    /* Report header */
    .report-header { margin-bottom: 24px; padding-bottom: 16px; border-bottom: 2px solid; }
    .report-title { color: #003366; font-weight: 700; margin: 0 0 4px; font-size: 1.4rem; }
    .report-subtitle { color: #555; font-size: .82rem; }

    /* Sections */
    .report-section { margin-bottom: 32px; }
    .section-heading {
      color: #003366; font-weight: 700; font-size: .85rem;
      text-transform: uppercase; letter-spacing: .06em; margin: 0 0 12px;
    }
    .section-divider { border: none; border-top: 1px solid #c8d0e0; margin-bottom: 32px; }

    /* Score / status */
    .score-row { display: flex; align-items: center; gap: 16px; margin-bottom: 16px; }
    .score-box { padding: 12px 20px; border-radius: 8px; border: 1px solid; }
    .score-value { font-size: 2rem; font-weight: 800; line-height: 1; }
    .score-label { font-size: .7rem; opacity: .8; margin-top: 2px; }
    .status-chip {
      display: inline-block; padding: 2px 10px; border-radius: 8px;
      font-weight: 700; font-size: .8rem; margin-bottom: 4px;
    }
    .posture-label { font-size: .82rem; color: #555; }

    /* Summary key-value table */
    .summary-table { border-collapse: collapse; font-size: .8rem; }
    .td-label {
      padding: 5px 12px 5px 0; font-weight: 600; color: #1a1a2e;
      min-width: 220px; border-bottom: 1px solid #e0e4ec;
    }
    .td-value { padding: 5px 0; color: #1a1a2e; border-bottom: 1px solid #e0e4ec; }

    /* Data tables */
    .data-table { border-collapse: collapse; font-size: .8rem; }
    .data-table--full { width: 100%; }
    .data-table--min400 { min-width: 400px; }

    .th {
      font-weight: 700; font-size: .78rem; color: #1a1a2e;
      background: #e8ecf4; border-bottom: 2px solid #c8d0e0;
      padding: 6px 12px; text-align: left;
    }
    .th--center { text-align: center; }
    .th--code { width: 110px; }
    .th--badge { width: 90px; }

    .td { font-size: .8rem; color: #1a1a2e; border-bottom: 1px solid #e0e4ec; padding: 6px 12px; }
    .td--center { text-align: center; }
    .td--bold { font-weight: 600; }
    .td--mono { font-family: monospace; }
    .td--nowrap { white-space: nowrap; }
    .tr-even { background: #f7f9fc; }

    /* Badges */
    .status-badge { padding: 1px 6px; border-radius: 6px; font-size: .65rem; font-weight: 600; }
    .policy-badge { padding: 1px 5px; border-radius: 6px; font-size: .65rem; font-weight: 600; }

    /* Section group (privacy/cloud/ai) */
    .section-group { margin-bottom: 24px; }
    .section-group-header { font-weight: 700; font-size: .78rem; color: #003366; margin-bottom: 6px; }
    .section-group-name { color: #555; font-weight: 400; margin-left: 8px; }
    .mono { font-family: monospace; }

    /* Footer */
    .footer-divider { border: none; border-top: 1px solid #c8d0e0; margin-bottom: 16px; }
    .report-footer { text-align: center; font-size: .72rem; color: #888; }

    @media print {
      .no-print { display: none !important; }
      .report-body { box-shadow: none !important; border-radius: 0 !important; max-width: 100% !important; }
    }
  `],
})
export class ReportComponent {
  private dashboard    = inject(DashboardApiService)
  private controls     = inject(ControlsApiService)
  readonly product     = inject(ProductService)
  private projectSvc   = inject(ProjectService)
  private theme        = inject(ThemeService)


  // ── State ──────────────────────────────────────────────────────────────────
  reportProduct  = signal<Product>(this.product.product())
  activeProjectId = computed(() => this.projectSvc.activeProjectId())
  readonly products: Product[] = ['isms', 'privacy', 'cloud', 'ai']
  readonly generatedDate = new Date().toLocaleDateString('en-GB', { year: 'numeric', month: 'long', day: 'numeric' })
  readonly Math = Math

  // Table cell styles (used in template as string interpolation)
  readonly TH = 'font-weight:700;font-size:.78rem;color:#1a1a2e;background:#e8ecf4;border-bottom:2px solid #c8d0e0;padding:6px 12px;text-align:left'
  readonly TD = 'font-size:.8rem;color:#1a1a2e;border-bottom:1px solid #e0e4ec;padding:6px 12px'

  // ── Queries ────────────────────────────────────────────────────────────────
  overviewQuery = injectQuery(() => ({
    queryKey: ['report', 'overview', this.activeProjectId()] as const,
    queryFn: () => firstValueFrom(this.dashboard.getOverview(this.activeProjectId())) as Promise<RealOverview>,
    enabled: this.reportProduct() === 'isms',
  }))

  readinessQuery = injectQuery(() => ({
    queryKey: ['report', 'readiness', this.activeProjectId()] as const,
    queryFn: () => firstValueFrom(this.dashboard.getAuditReadiness(this.activeProjectId())) as Promise<RealReadiness>,
    enabled: this.reportProduct() === 'isms',
  }))

  homeSummaryQuery = injectQuery(() => ({
    queryKey: ['home-summary'],
    queryFn: () => firstValueFrom(this.dashboard.getHomeSummary()),
  }))

  groupsQuery = injectQuery(() => ({
    queryKey: ['controls', 'list', this.reportProduct()],
    queryFn: () => firstValueFrom(this.controls.list({ product_family: this.reportProduct().toUpperCase() })),
    enabled: this.reportProduct() !== 'isms',
  }))

  // ── Computed ───────────────────────────────────────────────────────────────
  isDark = computed(() => this.theme.isDark())

  isLoading = computed((): boolean => {
    if (this.reportProduct() === 'isms') return this.overviewQuery.isLoading() || this.readinessQuery.isLoading()
    return this.homeSummaryQuery.isLoading() || this.groupsQuery.isLoading()
  })

  productSummary = computed(() => {
    const hs = this.homeSummaryQuery.data()
    const p = this.reportProduct()
    if (!hs) return null
    return (hs as any)[p] ?? null
  })

  ismsSummaryRows = computed(() => {
    const ov = this.overviewQuery.data()
    if (!ov) return []
    return [
      { label: 'Control Groups',       value: ov.total_controls ?? '—' },
      { label: 'Policies',             value: ov.total_policies ?? '—' },
      { label: 'Implementations',      value: ov.total_implementations ?? '—' },
      { label: 'Open Gaps',            value: ov.total_gaps_open ?? '—' },
      { label: 'Framework Coverage',   value: pct(ov.framework.coverage_pct) },
      { label: 'Operational Coverage', value: pct(ov.operational.coverage_pct) },
    ]
  })

  extSummaryRowsComputed = computed(() => {
    const s = this.productSummary()
    if (!s) return []
    return [
      { label: 'Control Groups',       value: s.groups },
      { label: 'Policies',             value: s.policies },
      { label: 'Implementations',      value: s.imps },
      { label: 'Open Gaps',            value: s.coverage_gaps },
      { label: 'Policy Coverage',      value: pct(s.pol_coverage_pct) },
      { label: 'Implementation Coverage', value: pct(s.impl_coverage_pct) },
    ]
  })

  ismsReadinessRows = computed(() => {
    const rd = this.readinessQuery.data()
    if (!rd) return []
    return [
      { name: 'Policies',       value: rd.policies_pct },
      { name: 'User Guides',    value: rd.ug_pct },
      { name: 'Tech Guides',    value: rd.tg_pct },
      { name: 'Assessments',    value: rd.assessments_pct },
      { name: 'Evidence',       value: rd.evidence_pct },
      { name: 'Gaps Closed',    value: rd.gaps_closed_pct },
    ]
  })

  extReadinessRows = computed(() => {
    const s = this.productSummary()
    if (!s) return []
    const gapsPct = s.groups > 0 ? Math.round(((s.groups - s.coverage_gaps) / s.groups) * 100) : 100
    return [
      { name: 'Policies',            value: s.pol_coverage_pct },
      { name: 'Implementations',     value: s.impl_coverage_pct },
      { name: 'Evidence',            value: s.evidence_coverage_pct },
      { name: 'Coverage Gaps Closed', value: gapsPct },
    ]
  })

  // ── Helpers ────────────────────────────────────────────────────────────────
  statusBg(s: string): string {
    return this.isDark() ? (STATUS_BG_DARK[s] ?? '#222') : (STATUS_BG_LIGHT[s] ?? 'rgba(0,0,0,.07)')
  }
  statusFg(s: string): string {
    return this.isDark() ? (STATUS_FG_DARK[s] ?? '#fff') : (STATUS_FG_LIGHT[s] ?? '#333')
  }
  statusLabel(s: string): string { return STATUS_LABEL[s] ?? s }
  headerColor(p: Product): string { return HEADER_COLORS[p] ?? '#4472C4' }
  productLabel(p: Product): string { return PRODUCT_LABELS[p] ?? p.toUpperCase() }
  standardName(p: Product): string { return STANDARD_NAMES[p] ?? '' }
  pct = pct

  bySection(groups: GroupRow[]): { section: string; section_name: string; rows: GroupRow[] }[] {
    const map: Record<string, { section: string; section_name: string; rows: GroupRow[] }> = {}
    for (const g of groups) {
      if (!map[g.section]) map[g.section] = { section: g.section, section_name: g.section_name, rows: [] }
      map[g.section].rows.push(g)
    }
    return Object.values(map)
  }

  // ── Actions ────────────────────────────────────────────────────────────────
  print(): void { window.print() }

  exportCsv(): void {
    const ov = this.overviewQuery.data()
    if (!ov) return
    const headers = ['section', 'section_name', 'total_controls', 'framework_covered', 'framework_pct', 'operational_covered', 'operational_pct']
    const rows = ov.sections.map(s => [
      s.section, s.section_name, s.total_controls, s.framework_covered,
      s.framework_pct.toFixed(1), s.operational_covered, s.operational_pct.toFixed(1),
    ])
    const csv = [headers.join(','), ...rows.map(r => r.join(','))].join('\n')
    const today = new Date().toISOString().slice(0, 10).replace(/-/g, '')
    const url = URL.createObjectURL(new Blob([csv], { type: 'text/csv' }))
    const a = document.createElement('a'); a.href = url; a.download = `isms-report-${today}.csv`; a.click()
    URL.revokeObjectURL(url)
  }
}
