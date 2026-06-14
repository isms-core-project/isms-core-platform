import { Component, inject, signal, computed } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'
import { injectQuery } from '@tanstack/angular-query-experimental'

import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatIconModule } from '@angular/material/icon'
import { MatSlideToggleModule } from '@angular/material/slide-toggle'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatDividerModule } from '@angular/material/divider'

import { FeedsApiService, EuvdEntry } from '../../api/feeds-api.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'
import { ThemeService } from '../../core/services/theme.service'

const INTEL_DARK  = '#FFA726'
const INTEL_LIGHT = '#BA7517'
const PER_PAGE = 50

const SEVERITY_DARK: Record<string, { bg: string; color: string }> = {
  CRITICAL: { bg: '#3a0a0a', color: '#FFC7CE' },
  HIGH:     { bg: '#2a1a00', color: '#FFEB9C' },
  MEDIUM:   { bg: '#1a2a3a', color: '#9fc8f0' },
  LOW:      { bg: '#1a2a1a', color: '#C6EFCE' },
  NONE:     { bg: '#1e1e2e', color: '#888' },
}
const SEVERITY_LIGHT: Record<string, { bg: string; color: string }> = {
  CRITICAL: { bg: 'rgba(163,45,45,0.15)',   color: '#8A1F1F' },
  HIGH:     { bg: 'rgba(163,45,45,0.10)',   color: '#A32D2D' },
  MEDIUM:   { bg: 'rgba(186,117,23,0.13)',  color: '#7A4500' },
  LOW:      { bg: 'rgba(29,158,117,0.12)',  color: '#0F6E56' },
  NONE:     { bg: 'rgba(44,44,42,0.07)',    color: '#5F5E5A' },
}

function scoreToSeverity(score: number | null): string {
  if (score === null) return 'NONE'
  if (score >= 9) return 'CRITICAL'
  if (score >= 7) return 'HIGH'
  if (score >= 4) return 'MEDIUM'
  return 'LOW'
}

function fmtDate(s: string | null): string {
  return s ? s.slice(0, 10) : '—'
}

@Component({
  selector: 'app-euvd-explorer',
  standalone: true,
  imports: [
    FormsModule,
    PageHeaderComponent,
    MatFormFieldModule, MatInputModule, MatSelectModule,
    MatIconModule, MatSlideToggleModule,
    MatTooltipModule, MatProgressSpinnerModule, MatDividerModule,
  ],
  template: `
<div class="euvd-page">
  <app-page-header
    title="EUVD Explorer"
    subtitle="ENISA European Vulnerability Database — exploited & critical vulnerabilities under NIS2/CRA"
  />

  <!-- Stats bar -->
  @if (statsQuery.data(); as s) {
    <div class="stats-bar">
      <div class="stats-bar__item">
        <mat-icon class="stat-icon stat-icon--euvd">security</mat-icon>
        <span class="stats-bar__val">{{ s.total.toLocaleString() }}</span>
        <span class="stats-bar__lbl">EUVD Entries</span>
      </div>
      <div class="stats-bar__item">
        <mat-icon class="stat-icon stat-icon--exploited" [matTooltip]="'Actively exploited'">warning_amber</mat-icon>
        <span class="stats-bar__val">{{ s.exploited.toLocaleString() }}</span>
        <span class="stats-bar__lbl">Exploited</span>
      </div>
      <div class="stats-bar__item">
        <mat-icon class="stat-icon stat-icon--critical">bug_report</mat-icon>
        <span class="stats-bar__val">{{ s.critical.toLocaleString() }}</span>
        <span class="stats-bar__lbl">Critical</span>
      </div>
      <div class="stats-bar__item">
        <mat-icon class="stat-icon stat-icon--eu">flag</mat-icon>
        <span class="stats-bar__val">{{ s.eu_assigned.toLocaleString() }}</span>
        <span class="stats-bar__lbl">EU Assigned</span>
      </div>
      @if (s.with_cvss > 0) {
        <div class="stats-bar__item">
          <mat-icon class="stat-icon stat-icon--cvss">shield</mat-icon>
          <span class="stats-bar__val">{{ s.with_cvss.toLocaleString() }}</span>
          <span class="stats-bar__lbl">With CVSS</span>
        </div>
      }
      <mat-divider vertical class="stats-divider" />
      <span class="dim">Last sync: {{ lastSync() }}</span>
    </div>
  }

  <!-- Filters row -->
  <div class="filters-row">
    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="search-field">
      <mat-label>Search EUVD ID, CVE, description, vendor…</mat-label>
      <mat-icon matPrefix>search</mat-icon>
      <input matInput [ngModel]="searchInput()" (ngModelChange)="searchInput.set($event)"
        (keydown.enter)="commitSearch()" />
    </mat-form-field>

    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="filter-score">
      <mat-label>Score ≥</mat-label>
      <mat-select [ngModel]="minScore()" (ngModelChange)="onMinScore($event)">
        <mat-option value="">Any</mat-option>
        <mat-option value="9">Critical (9+)</mat-option>
        <mat-option value="7">High+ (7+)</mat-option>
        <mat-option value="4">Medium+ (4+)</mat-option>
      </mat-select>
    </mat-form-field>

    <mat-slide-toggle [checked]="exploitedOnly()" (change)="onExploitedToggle($event.checked)">Exploited</mat-slide-toggle>
    <mat-slide-toggle [checked]="criticalOnly()" (change)="onCriticalToggle($event.checked)">Critical</mat-slide-toggle>
    <mat-slide-toggle [checked]="euAssignedOnly()" (change)="onEuToggle($event.checked)">EU Assigned</mat-slide-toggle>

    <span class="dim ml-auto">{{ totalText() }}</span>
    @if (page() > 1) {
      <span class="pag-chip" (click)="setPage(page() - 1)">← Prev</span>
    }
    @if (page() < totalPages()) {
      <span class="pag-chip" (click)="setPage(page() + 1)">Next →</span>
    }
  </div>

  <!-- Table -->
  <div class="table-box">
    @if (listQuery.isLoading()) {
      <div class="table-loading">Loading…</div>
    }
    <table>
      <thead>
        <tr>
          <th class="col-id">EUVD ID</th>
          <th class="col-cve">CVE</th>
          <th>Description</th>
          <th class="col-sev">Severity</th>
          <th class="col-score">Score</th>
          <th class="col-epss">EPSS</th>
          <th class="col-pub">Published</th>
          <th class="col-flags">Flags</th>
          <th class="col-expand"></th>
        </tr>
      </thead>
      <tbody>
        @for (e of tableData(); track e.euvd_id) {
          <tr class="euvd-row" (click)="toggleExpand(e.euvd_id)">
            <td class="mono euvd-id-cell">{{ e.euvd_id }}</td>
            <td class="mono cve-cell">{{ e.cve_id ?? '—' }}</td>
            <td class="trunc trunc-desc">
              <span [title]="e.description ?? ''">{{ e.description ?? '—' }}</span>
            </td>
            <td>
              @if (e.base_score !== null) {
                <span class="sev-chip"
                  [style.background]="sevBg(e.base_score)"
                  [style.color]="sevFg(e.base_score)"
                  [style.border]="'1px solid ' + sevFg(e.base_score) + '40'">
                  {{ scoreLabel(e.base_score) }}
                </span>
              } @else {
                <span class="dim">—</span>
              }
            </td>
            <td class="bold dim-val">{{ e.base_score !== null ? (e.base_score.toFixed(1)) : '—' }}</td>
            <td class="dim">{{ e.epss_score !== null ? (e.epss_score.toFixed(1) + '%') : '—' }}</td>
            <td class="dim nowrap">{{ fmtDate(e.date_published) }}</td>
            <td>
              <div class="flags-row">
                @if (e.is_exploited) {
                  <mat-icon class="flag-icon flag-icon--exploited"
                    matTooltip="Actively Exploited">warning_amber</mat-icon>
                }
                @if (e.is_critical) {
                  <mat-icon class="flag-icon flag-icon--critical"
                    matTooltip="Critical Severity">bug_report</mat-icon>
                }
                @if (e.is_eu_assigned) {
                  <span class="eu-badge" matTooltip="EU Assigned">EU</span>
                }
              </div>
            </td>
            <td class="expand-cell">
              <mat-icon class="expand-icon">
                {{ expandedId() === e.euvd_id ? 'expand_less' : 'expand_more' }}
              </mat-icon>
            </td>
          </tr>

          <!-- Inline expanded detail -->
          @if (expandedId() === e.euvd_id) {
            <tr class="detail-row">
              <td colspan="9">
                <div class="detail-body">
                  <div class="detail-chips">
                    @if (e.base_score !== null) {
                      <span class="sev-chip"
                        [style.background]="sevBg(e.base_score)"
                        [style.color]="sevFg(e.base_score)">
                        {{ scoreLabel(e.base_score) }} {{ e.base_score.toFixed(1) }}
                        @if (e.base_score_version) { <span class="cvss-ver">{{ e.base_score_version }}</span> }
                      </span>
                    }
                    @if (e.is_exploited) { <span class="chip chip-error">EXPLOITED</span> }
                    @if (e.is_critical) { <span class="chip chip-error">CRITICAL</span> }
                    @if (e.is_eu_assigned) { <span class="chip chip-eu">EU ASSIGNED</span> }
                    @if (e.epss_score !== null) {
                      <span class="chip chip-info">EPSS {{ e.epss_score.toFixed(1) }}%</span>
                    }
                  </div>

                  <p class="detail-desc">{{ e.description ?? 'No description available.' }}</p>

                  <div class="detail-grid">
                    <div>
                      <span class="detail-key">Published</span>
                      <span class="detail-val">{{ fmtDate(e.date_published) }}</span>
                    </div>
                    <div>
                      <span class="detail-key">Updated</span>
                      <span class="detail-val">{{ fmtDate(e.date_updated) }}</span>
                    </div>
                    <div>
                      <span class="detail-key">Assigner</span>
                      <span class="detail-val">{{ e.assigner ?? '—' }}</span>
                    </div>
                    <div>
                      <span class="detail-key">CVSS Version</span>
                      <span class="detail-val">{{ e.base_score_version ?? '—' }}</span>
                    </div>

                    @if (e.vendors.length > 0) {
                      <div class="detail-full-row">
                        <span class="detail-key">Vendors</span>
                        <div class="chip-row">
                          @for (v of e.vendors; track v) { <span class="tag-chip">{{ v }}</span> }
                        </div>
                      </div>
                    }
                    @if (e.products.length > 0) {
                      <div class="detail-full-row">
                        <span class="detail-key">Products ({{ e.products.length }})</span>
                        <div class="chip-row">
                          @for (p of e.products.slice(0, 15); track p) { <span class="tag-chip">{{ p }}</span> }
                          @if (e.products.length > 15) {
                            <span class="dim">+{{ e.products.length - 15 }} more</span>
                          }
                        </div>
                      </div>
                    }
                    @if (e.aliases.length > 0) {
                      <div class="detail-full-row">
                        <span class="detail-key">Aliases</span>
                        <div class="chip-row">
                          @for (a of e.aliases; track a) { <span class="tag-chip">{{ a }}</span> }
                        </div>
                      </div>
                    }
                  </div>
                </div>
              </td>
            </tr>
          }
        }
        @if (!listQuery.isLoading() && tableData().length === 0) {
          <tr><td colspan="9" class="empty-cell">
            No EUVD entries. Trigger the EUVD feed from Threat Feeds to populate data.
          </td></tr>
        }
      </tbody>
    </table>
  </div>
</div>
  `,
  styles: [`
    .euvd-page {
      display: flex;
      flex-direction: column;
      gap: 14px;
      padding-bottom: 24px;
    }

    /* Stats bar — matches CVE Explorer */
    .stats-bar {
      display: flex; align-items: center; gap: 16px; flex-wrap: wrap;
      padding: 8px 14px; border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 8px; background: var(--mat-sys-surface-container);
    }
    .stats-bar__item { display: flex; align-items: center; gap: 4px; }
    .stats-bar__val  { font-size: 0.85rem; font-weight: 700; }
    .stats-bar__lbl  { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
    .stats-divider   { height: 24px; margin: 0 4px; }

    .stat-icon          { font-size: 14px; width: 14px; height: 14px; }
    .stat-icon--euvd    { color: #003399; }
    .stat-icon--exploited { color: #c62828; }
    .stat-icon--critical  { color: #b71c1c; }
    .stat-icon--eu        { color: #003399; }
    .stat-icon--cvss      { color: var(--mat-sys-primary); }
    :host-context(html[data-theme='light']) .stat-icon--euvd    { color: #185FA5; }
    :host-context(html[data-theme='light']) .stat-icon--exploited { color: #8A1F1F; }
    :host-context(html[data-theme='light']) .stat-icon--critical  { color: #A32D2D; }
    :host-context(html[data-theme='light']) .stat-icon--eu        { color: #185FA5; }

    /* Filters */
    .filters-row { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; padding-top: 10px; }
    .search-field { flex: 1 1 260px; min-width: 200px; }
    .filter-score { width: 130px; flex-shrink: 0; }
    .ml-auto { margin-left: auto; }
    .pag-chip {
      font-size: 0.75rem; padding: 3px 8px; border-radius: 12px;
      background: var(--mat-sys-surface-container-high);
      color: var(--mat-sys-on-surface); cursor: pointer;
    }
    .pag-chip:hover { background: var(--mat-sys-primary-container); }

    /* Table box */
    .table-box {
      border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 8px; overflow: hidden;
      background: var(--mat-sys-surface-container);
    }
    .table-loading { padding: 10px 14px; font-size: 0.82rem; color: var(--mat-sys-on-surface-variant); }

    table { width: 100%; border-collapse: collapse; }
    thead { background: rgba(255,255,255,0.04); position: sticky; top: 0; }
    th { font-size: 0.72rem; font-weight: 600; padding: 6px 10px; text-align: left; }
    td { font-size: 0.75rem; padding: 5px 10px; border-top: 1px solid rgba(0,0,0,0.05); vertical-align: middle; }
    tr.euvd-row { cursor: pointer; }
    tr.euvd-row:hover td { background: rgba(255,255,255,0.03); }
    :host-context(html[data-theme='light']) tr.euvd-row:hover td { background: rgba(44,44,42,0.04); }

    .col-id    { width: 120px; }
    .col-cve   { width: 110px; }
    .col-sev   { width: 85px; }
    .col-score { width: 55px; }
    .col-epss  { width: 55px; }
    .col-pub   { width: 90px; }
    .col-flags { width: 70px; }
    .col-expand { width: 24px; padding: 0 4px; }

    .euvd-id-cell { color: var(--mat-sys-primary); font-size: 0.72rem; }
    .cve-cell { color: var(--mat-sys-on-surface-variant); font-size: 0.72rem; }

    .sev-chip {
      display: inline-block; font-size: 0.68rem; height: 18px; padding: 0 6px;
      border-radius: 8px; font-weight: 600; line-height: 18px; white-space: nowrap;
    }
    .cvss-ver { font-size: 0.6rem; opacity: 0.7; margin-left: 3px; }
    .dim-val  { font-size: 0.75rem; font-weight: 600; }

    .flags-row { display: flex; align-items: center; gap: 2px; }
    .flag-icon           { font-size: 14px; width: 14px; height: 14px; }
    .flag-icon--exploited { color: #FFEB9C; }
    .flag-icon--critical  { color: #ff6b6b; }
    :host-context(html[data-theme='light']) .flag-icon--exploited { color: #9a6500; }
    :host-context(html[data-theme='light']) .flag-icon--critical  { color: #8A1F1F; }
    .eu-badge {
      font-size: 0.58rem; font-weight: 700; color: #fff; background: #003399;
      border-radius: 3px; padding: 0 4px; line-height: 14px; display: inline-block;
    }
    :host-context(html[data-theme='light']) .eu-badge { background: #185FA5; }

    .expand-cell { text-align: center; }
    .expand-icon { font-size: 16px; width: 16px; height: 16px; color: var(--mat-sys-on-surface-variant); }

    /* Inline detail */
    .detail-row td { padding: 0; border: none; }
    .detail-body {
      padding: 14px 20px;
      background: rgba(0,51,153,0.03);
      border-bottom: 1px solid rgba(255,255,255,0.06);
    }
    :host-context(html[data-theme='light']) .detail-body {
      background: rgba(44,44,42,0.04);
      border-bottom-color: rgba(44,44,42,0.10);
    }
    .detail-chips { display: flex; flex-wrap: wrap; gap: 4px; margin-bottom: 10px; }
    .detail-desc { font-size: 0.8rem; line-height: 1.6; margin: 0 0 12px 0; }
    .detail-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 10px 16px;
    }
    .detail-full-row { grid-column: 1 / -1; }
    .detail-key { display: block; font-size: 0.68rem; color: var(--mat-sys-on-surface-variant); margin-bottom: 2px; }
    .detail-val { display: block; font-size: 0.72rem; font-weight: 500; }

    .chip-row { display: flex; flex-wrap: wrap; gap: 2px; margin-top: 3px; }
    .tag-chip {
      display: inline-block; font-size: 0.68rem; height: 18px; padding: 0 6px; line-height: 18px;
      border-radius: 8px; background: var(--mat-sys-surface-container-high);
      color: var(--mat-sys-on-surface-variant);
    }

    .chip { display: inline-block; font-size: 0.68rem; height: 18px; padding: 0 6px; border-radius: 8px; line-height: 18px; }
    .chip-error { background: rgba(192,0,0,0.15); color: #FFC7CE; }
    .chip-eu    { background: rgba(0,51,153,0.20); color: #90b4ff; }
    .chip-info  { background: rgba(21,101,192,0.12); color: #90caf9; }
    :host-context(html[data-theme='light']) .chip-error { background: rgba(163,45,45,0.12); color: #8A1F1F; }
    :host-context(html[data-theme='light']) .chip-eu    { background: rgba(24,95,165,0.12); color: #185FA5; }
    :host-context(html[data-theme='light']) .chip-info  { background: rgba(24,95,165,0.11); color: #185FA5; }

    .empty-cell { text-align: center; padding: 24px; color: var(--mat-sys-on-surface-variant); font-size: 0.82rem; }

    .mono   { font-family: monospace; }
    .bold   { font-weight: 600; }
    .dim    { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
    .nowrap { white-space: nowrap; }
    .trunc  { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .trunc-desc { max-width: 320px; }
  `],
})
export class EuvdExplorerComponent {
  private feedsApi = inject(FeedsApiService)
  private readonly theme = inject(ThemeService)

  readonly isDark = computed(() => this.theme.isDark())
  get INTEL_COLOR() { return this.isDark() ? INTEL_DARK : INTEL_LIGHT }
  readonly fmtDate = fmtDate

  expandedId = signal<string | null>(null)
  searchInput = signal('')
  search      = signal('')
  exploitedOnly  = signal(false)
  criticalOnly   = signal(false)
  euAssignedOnly = signal(false)
  minScore = signal('')
  page     = signal(1)

  statsQuery = injectQuery(() => ({
    queryKey: ['euvd', 'stats'],
    queryFn:  () => firstValueFrom(this.feedsApi.getEuvdStats()),
    staleTime: 5 * 60_000,
  }))

  listQuery = injectQuery(() => ({
    queryKey: ['euvd', 'list', this.search(), this.exploitedOnly(), this.criticalOnly(), this.euAssignedOnly(), this.minScore(), this.page()],
    queryFn:  () => firstValueFrom(this.feedsApi.getEuvd({
      search:           this.search() || undefined,
      exploited_only:   this.exploitedOnly() || undefined,
      critical_only:    this.criticalOnly() || undefined,
      eu_assigned_only: this.euAssignedOnly() || undefined,
      min_score:        this.minScore() ? Number(this.minScore()) : undefined,
      page:             this.page(),
      per_page:         PER_PAGE,
    })),
    staleTime: 2 * 60_000,
  }))

  readonly tableData    = computed(() => this.listQuery.data()?.items ?? [])
  readonly totalPages   = computed(() => Math.max(1, Math.ceil((this.listQuery.data()?.total ?? 0) / PER_PAGE)))
  readonly totalText    = computed(() => {
    const total = this.listQuery.data()?.total ?? 0
    const p = this.page(), tp = this.totalPages()
    return tp > 1 ? `${total.toLocaleString()} entries · page ${p}/${tp}` : `${total.toLocaleString()} entries`
  })
  readonly lastSync = computed(() => {
    const s = this.statsQuery.data() as any
    if (!s?.last_sync) return 'Unknown'
    return new Date(s.last_sync).toLocaleString(undefined, { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' })
  })

  toggleExpand(id: string) { this.expandedId.update(cur => cur === id ? null : id) }
  commitSearch() { this.search.set(this.searchInput()); this.page.set(1); this.expandedId.set(null) }
  setPage(p: number) { this.page.set(p); this.expandedId.set(null) }
  onMinScore(v: string) { this.minScore.set(v); this.page.set(1); this.expandedId.set(null) }

  onExploitedToggle(v: boolean)  { this.exploitedOnly.set(v);  if (v) { this.criticalOnly.set(false); this.euAssignedOnly.set(false) } this.page.set(1) }
  onCriticalToggle(v: boolean)   { this.criticalOnly.set(v);   if (v) { this.exploitedOnly.set(false); this.euAssignedOnly.set(false) } this.page.set(1) }
  onEuToggle(v: boolean)         { this.euAssignedOnly.set(v); if (v) { this.exploitedOnly.set(false); this.criticalOnly.set(false) } this.page.set(1) }

  scoreLabel(score: number | null): string {
    if (score === null) return '—'
    const sev = scoreToSeverity(score)
    return sev === 'NONE' ? 'N/A' : sev.charAt(0) + sev.slice(1).toLowerCase()
  }

  private sevMap(score: number | null): { bg: string; color: string } {
    const sev = scoreToSeverity(score)
    const map = this.isDark() ? SEVERITY_DARK : SEVERITY_LIGHT
    return map[sev] ?? map['NONE']
  }

  sevBg(score: number | null): string { return this.sevMap(score).bg }
  sevFg(score: number | null): string { return this.sevMap(score).color }
}
