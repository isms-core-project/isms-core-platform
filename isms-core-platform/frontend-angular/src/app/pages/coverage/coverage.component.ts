import { Component, inject, signal, computed, effect } from '@angular/core'
import { DecimalPipe } from '@angular/common'
import { FormsModule } from '@angular/forms'
import { Router } from '@angular/router'
import { firstValueFrom } from 'rxjs'

import { injectQuery } from '@tanstack/angular-query-experimental'

import { MatCardModule } from '@angular/material/card'
import { MatButtonModule } from '@angular/material/button'
import { MatIconModule } from '@angular/material/icon'
import { MatChipsModule } from '@angular/material/chips'
import { MatProgressBarModule } from '@angular/material/progress-bar'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatSelectModule } from '@angular/material/select'
import { MatSlideToggleModule } from '@angular/material/slide-toggle'
import { MatPaginatorModule, PageEvent } from '@angular/material/paginator'
import { MatTabsModule } from '@angular/material/tabs'

import { DashboardApiService } from '../../api/dashboard-api.service'
import { ProductService, PRODUCT_COLORS } from '../../core/services/product.service'
import { ProjectsApiService } from '../../api/projects-api.service'
import { ThemeService } from '../../core/services/theme.service'
import { TokenStoreService } from '../../core/services/token-store.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

// ── Types ─────────────────────────────────────────────────────────────────────

interface CoverageMapping {
  framework: string
  framework_code: string
  control_id: string
  control_title: string
  mapping_type: string
  confidence: number
}

interface CoverageRow {
  iso_control_id: string
  iso_control_title: string
  control_group_code: string
  mappings: CoverageMapping[]
}

interface RealCoverage {
  frameworks: string[]
  total_iso_controls: number
  total_mappings: number
  by_framework: Record<string, number>
  rows: CoverageRow[]
}

interface InferredResult {
  framework: string
  framework_code: string
  total_controls: number
  covered_controls: number
  uncovered_controls: number
  coverage_pct: number
}

// ── Constants ─────────────────────────────────────────────────────────────────

const PRODUCT_SOURCE_FRAMEWORK: Record<string, string> = {
  isms: 'ISO27001', privacy: 'ISO27701', cloud: 'ISO27018', ai: 'ISO42001',
}
const SOURCE_CONTROL_LABEL: Record<string, string> = {
  isms: 'ISO 27001 Control', privacy: 'ISO 27701 Control',
  cloud: 'ISO 27018 Control', ai: 'ISO 42001 Control',
}
const ISO_EXTENSIONS = new Set(['ISO27017', 'ISO27018', 'ISO27701'])
const ROWS_PER_PAGE = 25

function pctColor(pct: number, dark: boolean): string {
  if (pct === 100) return dark ? '#00c752' : '#0F6E56'
  if (pct >= 50)   return dark ? '#AED581' : '#558b2f'
  if (pct >= 1)    return dark ? '#FFB300' : '#E65100'
  return dark ? '#F44336' : '#c62828'
}

function confColor(c: number, dark: boolean): { bg: string; color: string } {
  if (dark) {
    if (c >= 0.8) return { bg: 'rgba(198,239,206,.15)', color: '#C6EFCE' }
    if (c >= 0.6) return { bg: 'rgba(255,193,7,.20)',   color: '#FFC107' }
    return { bg: 'rgba(255,199,206,.12)', color: '#FFC7CE' }
  }
  if (c >= 0.8) return { bg: 'rgba(29,158,117,.15)',  color: '#0F6E56' }
  if (c >= 0.6) return { bg: 'rgba(230,145,0,.15)',  color: '#9a6500' }
  return { bg: 'rgba(192,0,0,.12)', color: '#9e0000' }
}

// ── Component ─────────────────────────────────────────────────────────────────

@Component({
  selector: 'app-coverage',
  standalone: true,
  imports: [
    FormsModule, DecimalPipe,
    MatCardModule, MatButtonModule, MatIconModule, MatChipsModule,
    MatProgressBarModule, MatTooltipModule,
    MatFormFieldModule, MatSelectModule,
    MatSlideToggleModule, MatPaginatorModule, MatTabsModule,
    PageHeaderComponent,
  ],
  template: `
<div class="page-root">
  <app-page-header
    title="Framework Coverage"
    [subtitle]="activeTab() === 1
      ? 'Inferred compliance coverage across target frameworks based on project assessments'
      : covData() ? (covData()!.frameworks.length + ' frameworks · ' + covData()!.total_mappings.toLocaleString() + ' total mappings') : 'Loading…'">
    @if (activeTab() === 0 && covData()) {
      <mat-form-field appearance="outline" class="header-fw-select" subscriptSizing="dynamic">
        <mat-label>Framework</mat-label>
        <mat-select [ngModel]="activeFramework()" (ngModelChange)="activeFramework.set($event); page.set(0)">
          @for (f of sortedFrameworks(); track f) {
            <mat-option [value]="f">
              {{ f }}
              <span class="option-count">{{ covData()!.by_framework[f] ?? 0 }}</span>
            </mat-option>
          }
        </mat-select>
      </mat-form-field>
    }
  </app-page-header>

  <!-- Tabs -->
  <mat-tab-group [selectedIndex]="activeTab()" (selectedIndexChange)="activeTab.set($event)" class="tab-group" animationDuration="0" style="margin-top: 16px">

    <!-- ── Mapping Matrix ── -->
    <mat-tab label="Mapping Matrix">
      <div class="tab-body">

    <!-- Summary cards -->
    @if (covData()) {
      <div class="summary-grid">
        @for (c of summaryCards(); track c.label) {
          <mat-card>
            <mat-card-content class="summary-card-content">
              <div class="summary-card-label">{{ c.label }}</div>
              <div class="summary-card-value">{{ c.value }}</div>
            </mat-card-content>
          </mat-card>
        }
      </div>
    }

    <!-- Unmapped toggle -->
    @if (covData()) {
      <div class="toggle-row">
        <mat-slide-toggle [checked]="showUnmapped()" (change)="onUnmappedToggle($event.checked)" class="unmapped-toggle">
          Show unmapped only
        </mat-slide-toggle>
      </div>
    }

    <!-- Framework pills -->
    @if (covData()) {
      <mat-card class="fw-pills-card">
        <mat-card-content class="summary-card-content">
          <div class="fw-pills-heading">All Frameworks</div>
          <div class="fw-pills-row">
            @for (f of sortedFrameworks(); track f) {
              <div (click)="activeFramework.set(f); page.set(0)"
                class="fw-pill"
                [class.fw-pill-active]="f === activeFramework()"
                [class.fw-pill-iso-ext]="isIsoExt(f) && f !== activeFramework()"
                [style.background]="(covData()!.by_framework[f] ?? 0) > 0 && f !== activeFramework() ? packColor() + '18' : null"
                [style.borderColor]="(covData()!.by_framework[f] ?? 0) > 0 && f !== activeFramework() ? packColor() + '40' : null">
                {{ f }} <span class="fw-pill-count" [style.opacity]="(covData()!.by_framework[f] ?? 0) > 0 ? '0.8' : '0.35'">· {{ covData()!.by_framework[f] ?? 0 }}</span>
              </div>
            }
          </div>
        </mat-card-content>
      </mat-card>
    }

    @if (coverageQuery.isError()) {
      <div class="error-banner">
        Failed to load coverage data.
      </div>
    }

    <!-- Table -->
    <mat-card>
      <div class="table-scroll">
        <table class="cov-table">
          <thead>
            <tr class="thead-row">
              <th class="th-cell th-col-control">{{ sourceLabel() }}</th>
              <th class="th-cell th-col-group">Control Group</th>
              <th class="th-cell">{{ activeFramework() || 'Framework' }} Mappings</th>
              <th class="th-cell th-col-hit th-center">Hit</th>
            </tr>
          </thead>
          <tbody>
            @if (coverageQuery.isLoading()) {
              @for (i of [1,2,3,4,5,6,7,8]; track i) {
                <tr>
                  @for (j of [1,2,3,4]; track j) {
                    <td class="td-cell td-loading">
                      <div class="skeleton-cell"></div>
                    </td>
                  }
                </tr>
              }
            }
            @for (row of pagedRows(); track row.iso_control_id) {
              @let fwMaps = frameworkMappings(row);
              <tr class="tbody-row">
                <td class="td-cell">
                  <div class="control-id" [style.color]="isoControlColor(row.iso_control_id)">{{ row.iso_control_id }}</div>
                  <div class="control-title">{{ row.iso_control_title }}</div>
                </td>
                <td class="td-cell">
                  <span class="group-code">{{ row.control_group_code }}</span>
                </td>
                <td class="td-cell">
                  <div class="mapping-chips">
                    @for (m of fwMaps.slice(0, 6); track m.control_id; let idx = $index) {
                      @let cc = getConfColor(m.confidence);
                      <span [title]="m.control_title + ' · ' + (m.confidence * 100 | number:'1.0-0') + '% · ' + m.mapping_type"
                        class="conf-chip"
                        [style.background]="cc.bg"
                        [style.color]="cc.color">
                        {{ m.control_id }}
                      </span>
                    }
                    @if (fwMaps.length > 6) {
                      <span class="mapping-overflow">+{{ fwMaps.length - 6 }} more</span>
                    }
                    @if (fwMaps.length === 0) {
                      <span class="mapping-empty">—</span>
                    }
                  </div>
                </td>
                <td class="td-cell td-center">
                  <div class="hit-dot"
                    [style.background]="fwMaps.length > 0 ? (isDark() ? '#C6EFCE' : '#2e7d32') : (isDark() ? '#FFC7CE' : '#c62828')">
                  </div>
                </td>
              </tr>
            }
            @if (!coverageQuery.isLoading() && filteredRows().length === 0) {
              <tr>
                <td colspan="4" class="td-empty">
                  No mappings found{{ activeFramework() ? ' for ' + activeFramework() : '' }}.
                </td>
              </tr>
            }
          </tbody>
        </table>
      </div>
      @if (filteredRows().length > rowsPerPage) {
        <mat-paginator [length]="filteredRows().length" [pageSize]="rowsPerPage"
          [pageIndex]="page()" (page)="onPage($event)" hidePageSize>
        </mat-paginator>
      }
    </mat-card>

    <!-- Content Coverage Gaps — ISMS only (ISO 27001 control groups) -->
    @if (product.product() === 'isms') {
    <div class="gaps-section">
      <div class="gaps-header">
        <h6 class="gaps-title">Content Coverage Gaps</h6>
        @if (product.product() === 'isms') {
          <div class="gap-btns-row">
            @for (btn of gapBtns; track btn.value) {
              <div (click)="gapProduct.set(btn.value)"
                class="gap-btn"
                [class.gap-btn-active]="gapProduct() === btn.value"
                [style.background]="gapProduct() === btn.value ? btn.color + '30' : 'rgba(255,255,255,.05)'"
                [style.color]="gapProduct() === btn.value ? btn.color : 'inherit'"
                [style.borderColor]="gapProduct() === btn.value ? btn.color + '50' : 'transparent'">
                {{ btn.label }}
              </div>
            }
          </div>
        }
      </div>


      @if ((gapsQuery.data()?.length ?? 0) > 0) {
        <mat-card>
          <div class="table-scroll">
            <table class="cov-table">
              <thead>
                <tr class="thead-row">
                  <th class="th-cell th-col-code">Code</th>
                  <th class="th-cell">Control Group</th>
                  <th class="th-cell">Section</th>
                  <th class="th-cell">Missing Artefacts</th>
                </tr>
              </thead>
              <tbody>
                @for (gap of gapsQuery.data() ?? []; track gap.id) {
                  <tr class="tbody-row tbody-row-click"
                    (click)="router.navigate(['/controls', gap.id])">
                    <td class="td-cell">
                      <span class="gap-code">{{ gap.group_code }}</span>
                    </td>
                    <td class="td-cell td-bold td-sm">{{ gap.name }}</td>
                    <td class="td-cell td-muted td-xs">{{ gap.section_name }}</td>
                    <td class="td-cell">
                      <div class="missing-chips">
                        @for (m of gap.missing; track m) {
                          <span class="missing-chip">{{ m }}</span>
                        }
                      </div>
                    </td>
                  </tr>
                }
              </tbody>
            </table>
          </div>
        </mat-card>
      }
    </div>
    }
      </div>
    </mat-tab>

    <!-- ── Inferred Coverage ── -->
    <mat-tab label="Inferred Coverage">
      <div class="tab-body">
        <div class="infer-filter-row">
          <mat-form-field appearance="outline" class="infer-project-field" subscriptSizing="dynamic">
            <mat-label>Project scope</mat-label>
            <mat-select [ngModel]="inferProjectId()" (ngModelChange)="inferProjectId.set($event)">
              <mat-option value="">Org-wide (all assessments)</mat-option>
              @for (p of projectsQuery.data() ?? []; track p.id) {
                <mat-option [value]="p.id">{{ p.name }}</mat-option>
              }
            </mat-select>
          </mat-form-field>
          @if (inferredQuery.data()) {
            <span class="infer-count-label">Based on {{ inferredQuery.data()!.assessed_controls }} assessed controls</span>
          }
        </div>

        @if (inferredQuery.isLoading()) {
          @for (i of [1,2,3,4,5]; track i) {
            <div class="skeleton-row"></div>
          }
        }

        @for (r of inferredQuery.data()?.frameworks ?? []; track r.framework_code) {
          @if (r.total_controls > 0) {
            <div class="infer-card">
              <div class="infer-card-header" (click)="toggleInferred(r.framework_code)">
                <div class="infer-card-info">
                  <div class="infer-fw-name">{{ r.framework }}</div>
                  <div class="infer-fw-sub">{{ r.covered_controls }} / {{ r.total_controls }} controls covered</div>
                </div>
                <div class="infer-progress-wrap">
                  <mat-progress-bar mode="determinate" [value]="r.coverage_pct" class="infer-progress-bar"></mat-progress-bar>
                </div>
                <span class="infer-pct" [style.color]="getPctColor(r.coverage_pct)">{{ r.coverage_pct }}%</span>
                <mat-icon class="icon-sm infer-expand-icon">{{ openInferred()[r.framework_code] ? 'expand_less' : 'expand_more' }}</mat-icon>
              </div>
              @if (openInferred()[r.framework_code]) {
                <div class="infer-card-detail">
                  <span class="infer-detail-text">{{ r.uncovered_controls }} uncovered controls · {{ r.coverage_pct }}% covered</span>
                </div>
              }
            </div>
          }
        }

        @if (inferredQuery.data()?.frameworks?.length === 0) {
          <div class="no-crosswalk-banner">
            No crosswalk data loaded — run the dataset bootstrap to load framework mappings.
          </div>
        }
      </div>
    </mat-tab>

  </mat-tab-group>

</div>
`,
  styles: [`:host { display: block; }

    /* Page root */
    .page-root { padding: 0 4px; }

    /* Header form field */
    .header-fw-select { min-width: 240px; }
    .option-count { margin-left: 8px; font-size: .75rem; opacity: .5; }

    /* Tab group */
    .tab-group { margin-bottom: 20px; }

    /* Inferred Coverage tab */
    .infer-filter-row { display: flex; gap: 16px; align-items: center; margin-bottom: 20px; flex-wrap: wrap; }
    .infer-project-field { min-width: 260px; }
    .infer-count-label { font-size: .72rem; opacity: .5; }
    .skeleton-row { height: 52px; background: rgba(255,255,255,.05); border-radius: 6px; margin-bottom: 8px; }
    .infer-card { border: 1px solid rgba(128,128,128,.2); border-radius: 6px; overflow: hidden; margin-bottom: 8px; }
    .infer-card-header { display: flex; align-items: center; gap: 16px; padding: 10px 16px; cursor: pointer; }
    .infer-card-info { flex: 1; }
    .infer-fw-name { font-weight: 600; font-size: .82rem; }
    .infer-fw-sub { font-size: .65rem; color: var(--mat-sys-on-surface-variant); }
    .infer-progress-wrap { width: 160px; }
    .infer-progress-bar { height: 6px; border-radius: 3px; }
    .infer-pct { font-weight: 700; min-width: 44px; text-align: right; font-size: .9rem; }
    .infer-expand-icon { opacity: .4; }
    .infer-card-detail { padding: 12px 16px; border-top: 1px solid rgba(255,255,255,.08); }
    .infer-detail-text { font-size: .72rem; color: var(--mat-sys-on-surface-variant); }
    .no-crosswalk-banner { padding: 16px; background: rgba(21,101,192,.1); border-radius: 6px; font-size: .85rem; }

    /* Summary cards */
    .tab-body { padding-top: 16px; }
    .summary-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 16px; margin-bottom: 16px; }
    .summary-card-content { padding-bottom: 12px !important; }
    .summary-card-label { font-size: .72rem; opacity: .5; margin-bottom: 4px; }
    .summary-card-value { font-size: 1.5rem; font-weight: 700; }

    /* Unmapped toggle */
    .toggle-row { display: flex; justify-content: flex-end; margin-bottom: 8px; }
    .unmapped-toggle { font-size: .72rem; }

    /* Framework pills */
    .fw-pills-card { margin-bottom: 16px; }
    .fw-pills-heading { font-size: .78rem; font-weight: 600; margin-bottom: 8px; }
    .fw-pills-row { display: flex; gap: 6px; flex-wrap: wrap; }
    .fw-pill {
      cursor: pointer;
      padding: 3px 10px;
      border-radius: 4px;
      font-size: .72rem;
      font-weight: 400;
      background: var(--mat-sys-surface-container);
      border: 1px solid transparent;
    }
    .fw-pill-active {
      font-weight: 700;
      background: color-mix(in srgb, var(--mat-sys-primary) 20%, transparent);
      border-color: color-mix(in srgb, var(--mat-sys-primary) 45%, transparent);
    }
    .fw-pill-iso-ext { background: rgba(255,192,0,.07); }
    .fw-pill-count { margin-left: 6px; opacity: .4; }

    /* Error banner */
    .error-banner { color: #f44336; padding: 12px; margin-bottom: 12px; border-radius: 6px; background: rgba(244,67,54,.1); }

    /* Coverage table */
    .table-scroll { overflow-x: auto; }
    .cov-table { width: 100%; border-collapse: collapse; font-size: .8rem; }
    .thead-row { border-bottom: 1px solid rgba(255,255,255,.1); }
    .tbody-row { border-bottom: 1px solid rgba(255,255,255,.04); }
    .tbody-row-click { cursor: pointer; }
    .th-cell { padding: 10px 12px; text-align: left; font-size: .72rem; font-weight: 600; opacity: .6; }
    .th-center { text-align: center; }
    .th-col-control { width: 140px; }
    .th-col-group { width: 140px; }
    .th-col-hit { width: 60px; }
    .th-col-code { width: 90px; }
    .td-cell { padding: 7px 12px; }
    .td-loading { padding: 8px 12px; border-bottom: 1px solid rgba(255,255,255,.04); }
    .td-center { text-align: center; }
    .td-bold { font-weight: 600; }
    .td-sm { font-size: .82rem; }
    .td-muted { font-size: .72rem; opacity: .5; }
    .td-xs { font-size: .72rem; }
    .td-empty { padding: 32px; text-align: center; opacity: .4; }
    .skeleton-cell { height: 12px; background: rgba(255,255,255,.07); border-radius: 4px; }

    /* Control ID cell */
    .control-id { font-family: monospace; font-size: .75rem; font-weight: 600; }
    .control-title { font-size: .68rem; opacity: .65; line-height: 1.3; }
    .group-code { font-family: monospace; font-size: .72rem; opacity: .65; }
    html[data-theme='light'] .gap-code { color: #185FA5; }


    /* Mapping chips */
    .mapping-chips { display: flex; flex-wrap: wrap; gap: 4px; }
    .conf-chip {
      font-size: .68rem;
      padding: 0 5px;
      height: 18px;
      border-radius: 9px;
      display: inline-flex;
      align-items: center;
    }
    .mapping-overflow { font-size: .68rem; opacity: .5; align-self: center; }
    .mapping-empty { opacity: .3; }

    /* Hit dot */
    .hit-dot { width: 10px; height: 10px; border-radius: 50%; margin: 0 auto; }

    /* Gaps section */
    .gaps-section { margin-top: 32px; }
    .gaps-header { display: flex; align-items: center; gap: 16px; margin-bottom: 12px; flex-wrap: wrap; }
    .gaps-title { margin: 0; font-size: 1rem; font-weight: 700; }
    .gap-btns-row { display: flex; gap: 6px; margin-left: auto; }
    .gap-btn {
      cursor: pointer;
      padding: 2px 10px;
      border-radius: 12px;
      font-size: .72rem;
      border: 1px solid transparent;
    }
    .gaps-empty-state { display: flex; align-items: center; gap: 12px; padding: 24px 8px; opacity: .4; }
    .gaps-empty-text { font-size: .85rem; }

    /* Gaps table */
    .gap-code { font-family: monospace; font-size: .72rem; color: #9DC3E6; }
    .missing-chips { display: flex; gap: 4px; flex-wrap: wrap; }
    .missing-chip {
      font-size: .65rem;
      padding: 0 5px;
      height: 18px;
      border-radius: 9px;
      display: inline-flex;
      align-items: center;
      background: rgba(255,199,206,.15);
      color: #FFC7CE;
    }
  `],
})
export class CoverageComponent {
  readonly product  = inject(ProductService)
  readonly router   = inject(Router)
  private theme     = inject(ThemeService)
  private dashboard   = inject(DashboardApiService)
  private projects    = inject(ProjectsApiService)
  private tokenStore  = inject(TokenStoreService)

  // ── State ──────────────────────────────────────────────────────────────────
  activeTab       = signal(0)
  activeFramework = signal('')
  showUnmapped    = signal(false)
  page            = signal(0)
  gapProduct      = signal<'framework' | 'operational'>('framework')
  inferProjectId  = signal('')
  openInferred    = signal<Record<string, boolean>>({})
  readonly rowsPerPage = ROWS_PER_PAGE

  constructor() {
    // Reset framework selection when the active product changes (different source framework)
    effect(() => {
      this.product.product()
      this.activeFramework.set('')
      this.page.set(0)
    })
  }

  gapBtns = [
    { value: 'framework'   as const, label: 'FW', color: PRODUCT_COLORS.isms },
    { value: 'operational' as const, label: 'OP', color: '#70AD47' },
  ]

  // ── Queries ────────────────────────────────────────────────────────────────
  coverageQuery = injectQuery(() => ({
    queryKey: ['dashboard-coverage', PRODUCT_SOURCE_FRAMEWORK[this.product.product()] ?? 'ISO27001'],
    queryFn: () => fetch(
      `/api/v1/dashboard/coverage?source_framework=${PRODUCT_SOURCE_FRAMEWORK[this.product.product()] ?? 'ISO27001'}`,
      { headers: { Authorization: 'Bearer ' + (this.tokenStore.get() ?? '') } }
    ).then(r => r.json()) as Promise<RealCoverage>,
  }))

  gapsQuery = injectQuery(() => ({
    queryKey: ['coverage-gaps', this.gapProduct()],
    queryFn: () => firstValueFrom(this.dashboard.getCoverageGaps(this.gapProduct())),
    enabled: this.product.product() === 'isms',
  }))

  projectsQuery = injectQuery(() => ({
    queryKey: ['projects-list'],
    queryFn: () => firstValueFrom(this.projects.list()),
  }))

  inferredQuery = injectQuery(() => ({
    queryKey: ['coverage-inferred', this.inferProjectId()],
    queryFn: () => fetch(
      `/api/v1/coverage/multi-framework${this.inferProjectId() ? '?project_id=' + this.inferProjectId() : ''}`,
      { headers: { Authorization: 'Bearer ' + (this.tokenStore.get() ?? '') } }
    ).then(r => r.json()) as Promise<{ assessed_controls: number; frameworks: InferredResult[] }>,
    enabled: this.activeTab() === 1,
  }))

  // ── Computed ───────────────────────────────────────────────────────────────
  covData = computed((): RealCoverage | null => this.coverageQuery.data() ?? null)
  isDark  = computed(() => this.theme.isDark())

  sortedFrameworks = computed((): string[] => {
    const c = this.covData()
    if (!c) return []
    return [...new Set(c.frameworks)].sort((a, b) => (c.by_framework[b] ?? 0) - (c.by_framework[a] ?? 0))
  })

  filteredRows = computed((): CoverageRow[] => {
    const c = this.covData()
    if (!c) return []
    if (this.showUnmapped()) return c.rows.filter(row => !row.mappings.some(m => m.framework === this.activeFramework()))
    if (!this.activeFramework()) return c.rows
    return c.rows.filter(row => row.mappings.some(m => m.framework === this.activeFramework()))
  })

  pagedRows = computed((): CoverageRow[] => {
    const p = this.page()
    return this.filteredRows().slice(p * ROWS_PER_PAGE, (p + 1) * ROWS_PER_PAGE)
  })

  summaryCards = computed(() => {
    const c = this.covData()
    if (!c) return []
    return [
      { label: 'Frameworks',    value: c.frameworks.length },
      { label: 'Total Mappings', value: c.total_mappings.toLocaleString() },
      { label: this.activeFramework() || 'Selected', value: this.activeFramework() ? (c.by_framework[this.activeFramework()] ?? 0) : '—' },
      { label: this.showUnmapped() ? 'Unmapped Controls' : 'Controls Shown', value: this.filteredRows().length },
    ]
  })

  sourceLabel = computed((): string => SOURCE_CONTROL_LABEL[this.product.product()] ?? 'ISO Control')
  packColor   = computed((): string => PRODUCT_COLORS[this.product.product()] ?? '#327df4')

  isoControlColor(controlId: string): string {
    if (this.product.product() !== 'isms') return this.packColor()
    if (controlId.startsWith('A.5')) return '#9E9E9E'
    if (controlId.startsWith('A.6')) return '#70AD47'
    if (controlId.startsWith('A.7')) return '#FFC000'
    if (controlId.startsWith('A.8')) return '#C00000'
    return this.packColor()
  }

  // ── Helpers ────────────────────────────────────────────────────────────────
  isIsoExt(f: string): boolean { return ISO_EXTENSIONS.has(f) }

  getPctColor(pct: number): string { return pctColor(pct, this.isDark()) }

  getConfColor(c: number): { bg: string; color: string } { return confColor(c, this.isDark()) }

  frameworkMappings(row: CoverageRow): CoverageMapping[] {
    if (!this.activeFramework()) return row.mappings
    return row.mappings.filter(m => m.framework === this.activeFramework())
  }

  // ── Actions ────────────────────────────────────────────────────────────────
  onUnmappedToggle(v: boolean): void { this.showUnmapped.set(v); this.page.set(0) }
  onPage(e: PageEvent): void { this.page.set(e.pageIndex) }
  toggleInferred(code: string): void { this.openInferred.update(m => ({ ...m, [code]: !m[code] })) }
}
