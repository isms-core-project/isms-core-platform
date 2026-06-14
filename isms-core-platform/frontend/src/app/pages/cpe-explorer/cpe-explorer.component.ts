import { Component, inject, signal, computed } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'
import { injectQuery } from '@tanstack/angular-query-experimental'

import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatChipsModule } from '@angular/material/chips'
import { MatIconModule } from '@angular/material/icon'
import { MatButtonModule } from '@angular/material/button'
import { MatSlideToggleModule } from '@angular/material/slide-toggle'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatDividerModule } from '@angular/material/divider'

import { FeedsApiService, NvdCpeEntry } from '../../api/feeds-api.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'
import { ThemeService } from '../../core/services/theme.service'

const PER_PAGE = 50

@Component({
  selector: 'app-cpe-explorer',
  standalone: true,
  imports: [
    FormsModule,
    PageHeaderComponent,
    MatFormFieldModule, MatInputModule, MatSelectModule, MatChipsModule,
    MatIconModule, MatButtonModule, MatSlideToggleModule,
    MatTooltipModule, MatProgressSpinnerModule, MatDividerModule,
  ],
  template: `
<div class="cpe-page">
  <app-page-header
    title="CPE Explorer"
    subtitle="NVD Common Platform Enumeration — vendor, product and platform inventory"
  />

  <!-- Stats bar -->
  @if (indexStatsQuery.data(); as s) {
    <div class="stats-bar">
      <div class="stats-bar__item">
        <mat-icon class="stat-icon stat-icon--cpe">security</mat-icon>
        <span class="stats-bar__val">{{ s.cpe_total.toLocaleString() }}</span>
        <span class="stats-bar__lbl">CPEs</span>
      </div>
      <mat-divider vertical class="stats-divider" />
      <span class="dim">Last sync: {{ lastSync() }}</span>
      @if (s.cpe_full_enabled) {
        <span class="info-chip">CPE Option B active</span>
      }
    </div>
  }

  <!-- Filters row -->
  <div class="filters-row">
    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="search-field">
      <mat-label>Search vendor, product, CPE URI…</mat-label>
      <mat-icon matPrefix>search</mat-icon>
      <input matInput [(ngModel)]="searchInput" (keydown.enter)="commitSearch()" />
    </mat-form-field>

    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="filter-type">
      <mat-label>Type</mat-label>
      <mat-select [(ngModel)]="cpePart" (ngModelChange)="onFilter()">
        <mat-option value="">All</mat-option>
        <mat-option value="a">Application</mat-option>
        <mat-option value="o">Operating System</mat-option>
        <mat-option value="h">Hardware</mat-option>
      </mat-select>
    </mat-form-field>

    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="filter-source">
      <mat-label>Source</mat-label>
      <mat-select [(ngModel)]="cpeSource" (ngModelChange)="onFilter()">
        <mat-option value="">All</mat-option>
        <mat-option value="cve_config">CVE Config (A)</mat-option>
        <mat-option value="kev_vendor">KEV Vendor (B)</mat-option>
      </mat-select>
    </mat-form-field>

    <mat-slide-toggle [(ngModel)]="cpeKevOnly" (ngModelChange)="onFilter()">KEV only</mat-slide-toggle>

    <span class="dim ml-auto">
      {{ totalText() }}
    </span>
    @if (page() > 1) {
      <span class="pag-chip" (click)="prevPage()">← Prev</span>
    }
    @if (page() < totalPages()) {
      <span class="pag-chip" (click)="nextPage()">Next →</span>
    }
  </div>

  <!-- Table -->
  <div class="table-box">
    @if (cpeQuery.isLoading()) {
      <div class="table-loading">Loading…</div>
    }
    <table>
      <thead>
        <tr>
          <th>CPE URI</th>
          <th class="col-vendor">Vendor</th>
          <th class="col-product">Product</th>
          <th class="col-type">Type</th>
          <th class="col-source">Source</th>
          <th class="col-kev">KEV</th>
          <th class="col-expand"></th>
        </tr>
      </thead>
      <tbody>
        @for (cpe of cpeQuery.data()?.items ?? []; track cpe.cpe_uri) {
          <tr class="cpe-row" (click)="toggleExpand(cpe.cpe_uri)">
            <td class="mono trunc val-cell" [title]="cpe.cpe_uri">{{ cpe.cpe_uri }}</td>
            <td>{{ cpe.vendor ?? '—' }}</td>
            <td>{{ cpe.product ?? '—' }}</td>
            <td>
              <span class="tag-chip">{{ partLabel(cpe.part) }}</span>
            </td>
            <td>
              <span class="src-chip"
                [style.background]="cpe.source === 'kev_vendor' ? 'rgba(192,0,0,0.1)' : 'rgba(46,125,50,0.1)'"
                [style.color]="cpe.source === 'kev_vendor' ? '#9e0000' : '#1b5e20'">
                {{ cpe.source === 'kev_vendor' ? 'KEV-vendor' : 'CVE-config' }}
              </span>
            </td>
            <td>
              @if (cpe.in_kev) {
                <mat-icon [style.color]="isDark() ? '#FFEB9C' : '#9a6500'" class="flag-icon">check_circle</mat-icon>
              } @else {
                <span class="dim">—</span>
              }
            </td>
            <td class="expand-cell">
              <mat-icon class="expand-icon">
                {{ expandedId() === cpe.cpe_uri ? 'expand_less' : 'expand_more' }}
              </mat-icon>
            </td>
          </tr>

          <!-- Expanded detail row -->
          @if (expandedId() === cpe.cpe_uri) {
            <tr class="detail-row">
              <td colspan="7">
                <div class="detail-body">
                  <div class="detail-grid">
                    <div class="detail-full-row">
                      <span class="detail-key">Full CPE URI</span>
                      <span class="detail-val mono break-all">{{ cpe.cpe_uri }}</span>
                    </div>
                    <div>
                      <span class="detail-key">Vendor</span>
                      <span class="detail-val">{{ cpe.vendor ?? '—' }}</span>
                    </div>
                    <div>
                      <span class="detail-key">Product</span>
                      <span class="detail-val">{{ cpe.product ?? '—' }}</span>
                    </div>
                    <div>
                      <span class="detail-key">Version</span>
                      <span class="detail-val mono">{{ cpe.version ?? '—' }}</span>
                    </div>
                    <div>
                      <span class="detail-key">Type</span>
                      <span class="detail-val">{{ partLabel(cpe.part) }}</span>
                    </div>
                    <div>
                      <span class="detail-key">Source</span>
                      <span class="detail-val">{{ cpe.source === 'kev_vendor' ? 'KEV-vendor (B)' : 'CVE-config (A)' }}</span>
                    </div>
                    <div>
                      <span class="detail-key">KEV Status</span>
                      @if (cpe.in_kev) {
                        <span class="detail-val kev-yes">In CISA KEV</span>
                      } @else {
                        <span class="detail-val dim">Not in KEV</span>
                      }
                    </div>
                  </div>
                </div>
              </td>
            </tr>
          }
        }
        @if (!cpeQuery.isLoading() && (cpeQuery.data()?.items?.length ?? 0) === 0) {
          <tr><td colspan="7" class="empty-cell">
            No CPEs found. Enable FEEDS_CVE_ENABLED=true to populate the CPE index.
          </td></tr>
        }
      </tbody>
    </table>
  </div>
</div>
  `,
  styles: [`
    .cpe-page {
      display: flex;
      flex-direction: column;
      gap: 14px;
      padding-bottom: 24px;
    }

    .stats-bar {
      display: flex; align-items: center; gap: 16px; flex-wrap: wrap;
      padding: 8px 14px; border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 8px; background: var(--mat-sys-surface-container);
    }
    .stats-bar__item { display: flex; align-items: center; gap: 4px; }
    .stats-bar__val  { font-size: 0.85rem; font-weight: 700; }
    .stats-bar__lbl  { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
    .stats-divider   { height: 24px; margin: 0 4px; }
    .info-chip { font-size: 0.68rem; padding: 2px 7px; border-radius: 8px; background: rgba(21,101,192,0.12); color: #1565c0; }

    .filters-row { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; padding-top: 10px; }
    .search-field  { flex: 1 1 260px; min-width: 200px; }
    .filter-type   { width: 120px; flex-shrink: 0; }
    .filter-source { width: 130px; flex-shrink: 0; }

    .ml-auto { margin-left: auto; }

    .pag-chip {
      font-size: 0.75rem; padding: 3px 8px; border-radius: 12px;
      background: var(--mat-sys-surface-container-high);
      color: var(--mat-sys-on-surface); cursor: pointer;
    }
    .pag-chip:hover { background: var(--mat-sys-primary-container); }

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
    tr.cpe-row { cursor: pointer; }
    tr.cpe-row:hover td { background: rgba(255,255,255,0.03); }

    .col-vendor  { width: 140px; }
    .col-product { width: 160px; }
    .col-type    { width: 110px; }
    .col-source  { width: 110px; }
    .col-kev     { width: 50px; }
    .col-expand  { width: 24px; padding: 0 4px; }

    .val-cell { max-width: 320px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

    .tag-chip {
      display: inline-block; font-size: 0.68rem; height: 18px; padding: 0 6px; line-height: 18px;
      border-radius: 8px; background: var(--mat-sys-surface-container-high); color: var(--mat-sys-on-surface-variant);
    }
    .src-chip {
      display: inline-block; font-size: 0.68rem; height: 18px; padding: 0 6px; line-height: 18px;
      border-radius: 8px; font-weight: 600;
    }
    .flag-icon { font-size: 14px; width: 14px; height: 14px; }

    .expand-cell { text-align: center; }
    .expand-icon { font-size: 16px; width: 16px; height: 16px; color: var(--mat-sys-on-surface-variant); }

    .detail-row td { padding: 0; border: none; }
    .detail-body {
      padding: 12px 20px;
      background: rgba(184,79,0,0.03);
      border-bottom: 1px solid rgba(255,255,255,0.06);
    }
    .detail-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 12px;
    }
    .detail-full-row { grid-column: 1 / -1; }
    .detail-key { display: block; font-size: 0.68rem; color: var(--mat-sys-on-surface-variant); margin-bottom: 2px; }
    .detail-val { display: block; font-size: 0.72rem; }
    .kev-yes { color: #9a6500; font-weight: 600; }
    .break-all { word-break: break-all; }

    .empty-cell { text-align: center; padding: 24px; color: var(--mat-sys-on-surface-variant); font-size: 0.82rem; }

    .stat-icon      { font-size: 14px; width: 14px; height: 14px; }
    .stat-icon--cpe { color: #FFA726; }
    .mono   { font-family: monospace; }
    .dim    { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
  `],
})
export class CpeExplorerComponent {
  private feedsApi = inject(FeedsApiService)
  private theme    = inject(ThemeService)

  // Search
  searchInput = ''
  private _search  = signal('')
  private _cpePart   = signal('')
  private _cpeSource = signal('')
  private _cpeKevOnly = signal(false)
  private _page = signal(1)

  get cpePart(): string { return this._cpePart() }
  set cpePart(v: string) { this._cpePart.set(v) }
  get cpeSource(): string { return this._cpeSource() }
  set cpeSource(v: string) { this._cpeSource.set(v) }
  get cpeKevOnly(): boolean { return this._cpeKevOnly() }
  set cpeKevOnly(v: boolean) { this._cpeKevOnly.set(v) }

  readonly page       = computed(() => this._page())
  expandedId          = signal<string | null>(null)
  readonly isDark     = computed(() => this.theme.isDark())

  readonly indexStatsQuery = injectQuery(() => ({
    queryKey: ['nvd', 'index-stats'],
    queryFn:  () => firstValueFrom(this.feedsApi.getNvdIndexStats()),
    staleTime: 60_000,
  }))

  readonly lastSync = computed(() => {
    const s = this.indexStatsQuery.data()
    if (!s?.last_cpe_sync) return 'Never'
    return new Date(s.last_cpe_sync).toLocaleString(undefined, { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' })
  })

  readonly cpeQuery = injectQuery(() => ({
    queryKey: ['nvd', 'cpe', this._search(), this._cpePart(), this._cpeSource(), this._cpeKevOnly(), this._page()],
    queryFn:  () => firstValueFrom(this.feedsApi.getCpe({
      search:   this._search() || undefined,
      part:     this._cpePart() || undefined,
      source:   this._cpeSource() || undefined,
      kev_only: this._cpeKevOnly() || undefined,
      page:     this._page(),
      per_page: PER_PAGE,
    })),
    staleTime: 30_000,
  }))

  readonly totalPages = computed(() => Math.max(1, Math.ceil((this.cpeQuery.data()?.total ?? 0) / PER_PAGE)))

  readonly totalText = computed(() => {
    const total = this.cpeQuery.data()?.total ?? 0
    const p = this._page()
    const tp = this.totalPages()
    if (tp > 1) return `${total.toLocaleString()} results · page ${p}/${tp}`
    return `${total.toLocaleString()} results`
  })

  commitSearch() { this._search.set(this.searchInput); this._page.set(1) }
  onFilter()     { this._page.set(1); this.expandedId.set(null) }
  prevPage()     { if (this._page() > 1) this._page.update(p => p - 1) }
  nextPage()     { if (this._page() < this.totalPages()) this._page.update(p => p + 1) }

  toggleExpand(id: string) {
    this.expandedId.update(cur => cur === id ? null : id)
  }

  partLabel(part: string | null): string {
    const map: Record<string, string> = { a: 'Application', o: 'OS', h: 'Hardware' }
    return (part ? map[part] : null) ?? part ?? '—'
  }
}
