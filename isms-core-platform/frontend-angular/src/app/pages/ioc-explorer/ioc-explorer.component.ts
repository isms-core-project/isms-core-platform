import { Component, inject, signal, computed } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { ActivatedRoute } from '@angular/router'
import { firstValueFrom } from 'rxjs'
import { injectQuery } from '@tanstack/angular-query-experimental'

import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatIconModule } from '@angular/material/icon'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'

import { ThreatIntelApiService } from '../../api/threat-intel-api.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

const PAGE_SIZE = 50

const SOURCE_COLOR: Record<string, string> = {
  circl_misp:       '#ffb74d', botvrij_misp:    '#ffca28',
  abuseipdb:        '#64b5f6', urlhaus:         '#ff8a65',
  threatfox:        '#ef5350', sslbl:           '#ce93d8',
  feodotracker:     '#f48fb1', red_flag_domains:'#ef9a9a',
  stopforumspam:    '#90a4ae', malwarebazaar:   '#ff8a65',
  alienvault:       '#ff7043', malpedia:        '#4db6ac',
}
const SOURCE_LABEL: Record<string, string> = {
  circl_misp:       'CIRCL MISP',    botvrij_misp:    'Botvrij MISP',
  abuseipdb:        'AbuseIPDB',     urlhaus:         'URLhaus',
  threatfox:        'ThreatFox',     sslbl:           'SSLBL',
  feodotracker:     'Feodo Tracker', red_flag_domains:'Red Flag Domains',
  stopforumspam:    'StopForumSpam', malwarebazaar:   'MalwareBazaar',
  alienvault:       'AlienVault OTX',malpedia:        'Malpedia',
}
const TLP_COLOR: Record<string, string> = {
  red: '#d32f2f', amber: '#f57c00', green: '#388e3c', white: '#9e9e9e', clear: '#9e9e9e',
}
const TYPE_COLOR: Record<string, string> = {
  ip: '#1565c0', domain: '#2e7d32', url: '#6a0dad',
  md5: '#607D8B', sha1: '#607D8B', sha256: '#607D8B',
}

function fmt(iso: string | null): string { return iso ? iso.slice(0, 10) : '—' }

@Component({
  selector: 'app-ioc-explorer',
  standalone: true,
  imports: [
    FormsModule, PageHeaderComponent,
    MatFormFieldModule, MatInputModule, MatSelectModule,
    MatIconModule, MatTooltipModule, MatProgressSpinnerModule,
  ],
  template: `
<div class="ioc-page">
  <app-page-header title="IOC Explorer" [subtitle]="subtitle()" />

  <div class="mitre-filters">
    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="mitre-search">
      <mat-label>Search value…</mat-label>
      <mat-icon matPrefix>search</mat-icon>
      <input matInput [(ngModel)]="q" (ngModelChange)="onFilter()" />
    </mat-form-field>
    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="mitre-select" style="min-width:120px">
      <mat-label>Type</mat-label>
      <mat-select [(ngModel)]="iocType" (ngModelChange)="onFilter()">
        <mat-option value="">All types</mat-option>
        @for (t of IOC_TYPES; track t) { <mat-option [value]="t">{{ t }}</mat-option> }
      </mat-select>
    </mat-form-field>
    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="mitre-select" style="min-width:150px">
      <mat-label>Source</mat-label>
      <mat-select [(ngModel)]="source" (ngModelChange)="onFilter()">
        <mat-option value="">All sources</mat-option>
        @for (s of SOURCE_LIST; track s.value) { <mat-option [value]="s.value">{{ s.label }}</mat-option> }
      </mat-select>
    </mat-form-field>
    <div class="ioc-pagination">
      <span class="dim">{{ total().toLocaleString() }} results</span>
      <span class="mitre-pagination__btn" [class.disabled]="page() === 0" (click)="page() > 0 && prevPage()">← Prev</span>
      <span class="dim">{{ page() + 1 }} / {{ totalPages() || 1 }}</span>
      <span class="mitre-pagination__btn" [class.disabled]="page() >= totalPages() - 1" (click)="page() < totalPages() - 1 && nextPage()">Next →</span>
    </div>
  </div>

  <div class="mitre-table-box">
    @if (iocQuery.isLoading()) {
      <div class="mitre-empty"><mat-spinner diameter="28" /></div>
    }
    @if (!iocQuery.isLoading()) {
      <table class="mitre-table">
        <thead><tr>
          <th class="col-type">Type</th>
          <th>Value</th>
          <th class="col-src">Source</th>
          <th class="col-conf">Conf.</th>
          <th class="col-tlp">TLP</th>
          <th class="col-date">Last Seen</th>
          <th>Attribution</th>
          <th class="col-expand"></th>
        </tr></thead>
        <tbody>
          @if ((iocQuery.data()?.items ?? []).length === 0) {
            <tr><td colspan="8" class="mitre-empty">No IOCs found — feeds may still be loading on first boot.</td></tr>
          }
          @for (ioc of iocQuery.data()?.items ?? []; track ioc.id) {
            <tr class="mitre-row" (click)="toggleExpand(ioc.id)">
              <td>
                <span class="ioc-chip" [style.background]="typeColor(ioc.ioc_type) + '22'" [style.color]="typeColor(ioc.ioc_type)">{{ ioc.ioc_type }}</span>
              </td>
              <td class="mono val-cell">{{ ioc.value }}</td>
              <td>
                <span class="ioc-chip" [style.background]="srcColor(ioc.source) + '22'" [style.color]="srcColor(ioc.source)">{{ srcLabel(ioc.source) }}</span>
              </td>
              <td>
                @if (ioc.confidence !== null) {
                  <span class="ioc-chip" [style.background]="ioc.confidence >= 80 ? 'rgba(192,0,0,0.15)' : 'rgba(230,160,0,0.15)'" [style.color]="ioc.confidence >= 80 ? '#9e0000' : '#7a4800'">{{ ioc.confidence }}%</span>
                } @else { <span class="dim">—</span> }
              </td>
              <td>
                @if (ioc.tlp) {
                  <span class="ioc-chip" [style.background]="tlpColor(ioc.tlp) + '22'" [style.color]="tlpColor(ioc.tlp)">TLP:{{ ioc.tlp.toUpperCase() }}</span>
                } @else { <span class="dim">—</span> }
              </td>
              <td class="mono dim">{{ fmt(ioc.last_seen) }}</td>
              <td>
                <div class="attr-row">
                  @for (f of ioc.family_slugs.slice(0, 2); track f) {
                    <span class="family-chip"><mat-icon class="attr-icon">coronavirus</mat-icon>{{ f }}</span>
                  }
                  @for (a of ioc.actor_slugs.slice(0, 2); track a) {
                    <span class="actor-chip"><mat-icon class="attr-icon">stream</mat-icon>{{ a }}</span>
                  }
                  @for (t of ioc.mitre_tids.slice(0, 3); track t) {
                    <span class="tid-chip">{{ t }}</span>
                  }
                </div>
              </td>
              <td class="expand-cell">
                <mat-icon class="expand-icon">{{ expandedId() === ioc.id ? 'expand_less' : 'expand_more' }}</mat-icon>
              </td>
            </tr>
            @if (expandedId() === ioc.id) {
              <tr class="detail-row">
                <td colspan="8">
                  <div class="detail-body">
                    <div class="detail-grid">
                      <div>
                        <span class="detail-key">Full value</span>
                        <span class="detail-val mono break-all">{{ ioc.value }}</span>
                      </div>
                      @if (ioc.first_seen) {
                        <div><span class="detail-key">First seen</span><span class="detail-val">{{ fmt(ioc.first_seen) }}</span></div>
                      }
                      @if (ioc.family_slugs.length > 0) {
                        <div>
                          <span class="detail-key">Malware families</span>
                          <div class="chip-row">@for (f of ioc.family_slugs; track f) { <span class="tag-chip">{{ f }}</span> }</div>
                        </div>
                      }
                      @if (ioc.actor_slugs.length > 0) {
                        <div>
                          <span class="detail-key">Threat actors</span>
                          <div class="chip-row">@for (a of ioc.actor_slugs; track a) { <span class="tag-chip">{{ a }}</span> }</div>
                        </div>
                      }
                      @if (ioc.mitre_tids.length > 0) {
                        <div>
                          <span class="detail-key">ATT&amp;CK TIDs</span>
                          <div class="chip-row">@for (t of ioc.mitre_tids; track t) { <span class="tid-chip-lg">{{ t }}</span> }</div>
                        </div>
                      }
                      @if (ioc.tags.length > 0) {
                        <div class="detail-full-row">
                          <span class="detail-key">Tags ({{ ioc.tags.length }})</span>
                          <div class="chip-row chip-row--clipped">
                            @for (t of ioc.tags.slice(0, 12); track $index) { <span class="tag-chip sm">{{ cleanTag(t) }}</span> }
                          </div>
                        </div>
                      }
                    </div>
                  </div>
                </td>
              </tr>
            }
          }
        </tbody>
      </table>
    }
  </div>
</div>
  `,
  styles: [`
    .ioc-page { display: flex; flex-direction: column; gap: 16px; }

    .ioc-pagination { display: flex; align-items: center; gap: 8px; margin-left: auto; font-size: 0.75rem; }

    .val-cell { max-width: 300px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .col-type   { width: 70px; }
    .col-src    { width: 130px; }
    .col-conf   { width: 70px; }
    .col-tlp    { width: 90px; }
    .col-date   { width: 90px; }
    .col-expand { width: 24px; padding: 0 4px; }

    .ioc-chip { display: inline-block; font-size: 0.65rem; height: 18px; padding: 0 6px; border-radius: 8px; line-height: 18px; font-weight: 600; white-space: nowrap; }

    .attr-row { display: flex; flex-wrap: wrap; gap: 2px; }
    .attr-icon { font-size: 11px; width: 11px; height: 11px; }
    .family-chip {
      display: inline-flex; align-items: center; gap: 2px; font-size: 0.62rem;
      height: 16px; padding: 0 4px; border-radius: 6px;
      background: rgba(106,13,173,0.12); color: #4a0080;
    }
    .actor-chip {
      display: inline-flex; align-items: center; gap: 2px; font-size: 0.62rem;
      height: 16px; padding: 0 4px; border-radius: 6px;
      background: rgba(68,114,196,0.12); color: #2E5099;
    }
    .tid-chip {
      display: inline-block; font-size: 0.62rem; height: 16px; padding: 0 4px;
      line-height: 16px; border-radius: 6px; background: rgba(180,100,0,0.12); color: #7a4800;
    }
    :host-context(html[data-theme='light']) .family-chip { color: #4a148c; background: rgba(106,13,173,0.10); }
    :host-context(html[data-theme='light']) .actor-chip  { color: #1565c0; background: rgba(21,101,192,0.10); }
    :host-context(html[data-theme='light']) .tid-chip    { color: #7a4800; background: rgba(180,100,0,0.10); }

    .expand-cell { text-align: center; }
    .expand-icon { font-size: 16px; width: 16px; height: 16px; color: var(--mat-sys-on-surface-variant); }

    .detail-row td { padding: 0; border: none; }
    .detail-body {
      padding: 14px 20px;
      background: var(--mat-sys-surface-container-high);
      border-top: 2px solid var(--mat-sys-outline-variant);
      border-bottom: 1px solid var(--mat-sys-outline-variant);
    }
    .detail-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 12px; }
    .detail-key  { display: block; font-size: 0.68rem; color: var(--mat-sys-on-surface-variant); text-transform: uppercase; letter-spacing: 0.04em; margin-bottom: 3px; }
    .detail-val  { display: block; font-size: 0.72rem; }
    .break-all   { word-break: break-all; }
    .detail-full-row { grid-column: 1 / -1; }

    .chip-row { display: flex; flex-wrap: wrap; gap: 3px; margin-top: 3px; }
    .chip-row--clipped { max-height: 56px; overflow: hidden; }
    .tag-chip {
      display: inline-block; font-size: 0.62rem; height: 16px; padding: 0 5px;
      line-height: 16px; border-radius: 6px;
      background: var(--mat-sys-surface-container-high); color: var(--mat-sys-on-surface-variant);
    }
    .tag-chip.sm { height: 14px; font-size: 0.6rem; line-height: 14px; }
    .tid-chip-lg {
      display: inline-block; font-size: 0.62rem; height: 16px; padding: 0 5px;
      line-height: 16px; border-radius: 6px; background: rgba(180,100,0,0.18); color: #ffcc80;
    }
    :host-context(html[data-theme='light']) .tid-chip-lg { background: rgba(180,100,0,0.12); color: #7a4800; }

    .mono { font-family: monospace; }
    .dim  { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
  `],
})
export class IocExplorerComponent {
  private tiApi = inject(ThreatIntelApiService)
  private route = inject(ActivatedRoute)

  readonly IOC_TYPES  = ['ip', 'domain', 'url', 'md5', 'sha1', 'sha256']
  readonly SOURCE_LIST = Object.entries(SOURCE_LABEL).map(([value, label]) => ({ value, label }))
  readonly fmt = fmt

  private _q       = signal('')
  private _iocType = signal('')
  private _source  = signal('')

  get q(): string      { return this._q() }       set q(v: string)       { this._q.set(v) }
  get iocType(): string{ return this._iocType() }  set iocType(v: string) { this._iocType.set(v) }
  get source(): string { return this._source() }   set source(v: string)  { this._source.set(v) }

  constructor() {
    const p = this.route.snapshot.queryParams
    if (p['source'])   this._source.set(p['source'])
    if (p['ioc_type']) this._iocType.set(p['ioc_type'])
    if (p['q'])        this._q.set(p['q'])
  }

  private _page = signal(0)
  expandedId    = signal<string | null>(null)
  readonly page = computed(() => this._page())

  readonly iocQuery = injectQuery(() => ({
    queryKey: ['threat-intel', 'iocs', this._q(), this._iocType(), this._source(), this._page()],
    queryFn:  () => firstValueFrom(this.tiApi.getIocs({
      q: this._q() || undefined, ioc_type: this._iocType() || undefined,
      source: this._source() || undefined,
      skip: this._page() * PAGE_SIZE, limit: PAGE_SIZE,
    })),
    staleTime: 30_000,
  }))

  readonly total      = computed(() => this.iocQuery.data()?.total ?? 0)
  readonly totalPages = computed(() => Math.ceil(this.total() / PAGE_SIZE))
  readonly subtitle   = computed(() => {
    const t = this.total()
    return `Indicators of compromise from MISP, Abuse.ch, AbuseIPDB, AlienVault OTX and reputation feeds${t ? ` — ${t.toLocaleString()} total` : ''}`
  })

  onFilter()  { this._page.set(0); this.expandedId.set(null) }
  prevPage()  { if (this._page() > 0) this._page.update(p => p - 1) }
  nextPage()  { if (this._page() < this.totalPages() - 1) this._page.update(p => p + 1) }
  toggleExpand(id: string) { this.expandedId.update(cur => cur === id ? null : id) }

  srcColor(s: string)  { return SOURCE_COLOR[s] ?? '#888' }
  srcLabel(s: string)  { return SOURCE_LABEL[s] ?? s }
  typeColor(t: string) { return TYPE_COLOR[t] ?? '#888' }
  tlpColor(t: string)  { return TLP_COLOR[t.toLowerCase()] ?? '#9e9e9e' }
  cleanTag(t: unknown): string {
    if (typeof t !== 'string') return String(t)
    const m = t.match(/"([^"]+)"/)
    return m ? m[1] : t
  }
}
