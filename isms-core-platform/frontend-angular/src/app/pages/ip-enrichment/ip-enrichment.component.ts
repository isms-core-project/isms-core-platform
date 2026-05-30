import { Component, inject, signal } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'
import { injectMutation } from '@tanstack/angular-query-experimental'

import { MatTooltipModule } from '@angular/material/tooltip'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatIconModule } from '@angular/material/icon'
import { MatButtonModule } from '@angular/material/button'
import { MatCardModule } from '@angular/material/card'

import { ThreatIntelApiService, EnrichIpResponse } from '../../api/threat-intel-api.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

const PRIVACY_COLORS: Record<string, string> = {
  Tor: '#b71c1c', VPN: '#e65100', Proxy: '#f57f17',
  Relay: '#1565c0', Hosting: '#6a1b9a', Clean: '#2e7d32',
}

@Component({
  selector: 'app-ip-enrichment',
  standalone: true,
  imports: [
    FormsModule, PageHeaderComponent,
    MatTooltipModule, MatProgressSpinnerModule,
    MatFormFieldModule, MatInputModule,
    MatIconModule, MatButtonModule, MatCardModule,
  ],
  template: `
<div class="ipe-page">
  <app-page-header
    title="IP Enrichment"
    subtitle="On-demand AbuseIPDB + Shodan + MaxMind + IPInfo lookup — results cached 24h / 30d"
  />

  <!-- Input -->
  <div class="input-row">
    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="ip-field">
      <mat-label>IP Address</mat-label>
      <mat-icon matPrefix class="icon-sm">router</mat-icon>
      <input matInput [ngModel]="ip()" (ngModelChange)="ip.set($event)"
        placeholder="Enter IPv4 or IPv6 address…" class="mono-input"
        (keydown.enter)="handleSubmit()" />
    </mat-form-field>
    <button mat-flat-button color="primary" [disabled]="mutation.isPending()" (click)="handleSubmit()" class="lookup-btn">
      @if (mutation.isPending()) { Looking up… } @else { Lookup }
    </button>
  </div>

  @if (mutation.isError()) {
    <div class="isms-alert isms-alert--error">Enrichment failed — check API keys or try again.</div>
  }

  @if (mutation.data(); as result) {
    <div class="results-col">

      <div class="ip-header-row">
        <span class="ip-label">{{ result.ip }}</span>
        @if (result.cached) {
          <span class="cached-badge" [matTooltip]="'Cached ' + (result.cache_age_minutes ?? 0) + ' min ago'">Cached</span>
        }
      </div>

      <!-- Row 1: AbuseIPDB + Shodan + DNS -->
      <div class="card-row">

        @if (result.abuseipdb; as abuse) {
          <mat-card variant="outlined" class="info-card">
            <div class="card-hdr"><mat-icon class="icon-md" style="color:#1565c0">router</mat-icon><span class="card-title">AbuseIPDB</span></div>
            <div class="conf-bar-row">
              <div class="conf-bar-track">
                <div class="conf-bar-fill" [style.width]="abuseScore(abuse) + '%'" [style.background]="confColor(abuseScore(abuse))"></div>
              </div>
              <span class="conf-bar-label" [style.color]="confColor(abuseScore(abuse))">{{ abuseScore(abuse) }}%</span>
            </div>
            <hr class="card-divider" />
            @for (row of abuseRows(abuse); track row[0]) {
              <div class="kv-row"><span class="kv-key">{{ row[0] }}</span><span class="kv-val">{{ row[1] }}</span></div>
            }
          </mat-card>
        } @else {
          <mat-card variant="outlined" class="empty-card"><mat-icon class="icon-md muted-icon">router</mat-icon><span class="empty-text">AbuseIPDB — no result</span></mat-card>
        }

        @if (shodanData(result); as shodan) {
          <mat-card variant="outlined" class="info-card">
            <div class="card-hdr"><mat-icon class="icon-md" style="color:#FFA726">stream</mat-icon><span class="card-title">Shodan {{ shodan['source'] === 'shodan_internetdb' ? '(InternetDB)' : '(API)' }}</span></div>
            @if (shodanHostnames(shodan).length > 0) {
              <div class="mini-sec"><div class="kv-key">Hostnames</div><div class="mono-sm">{{ shodanHostnames(shodan).slice(0,3).join(', ') }}</div></div>
            }
            @if (shodan['org'] || shodan['asn']) {
              <div class="mini-sec"><div class="kv-key">Org / ASN</div><div class="text-sm">{{ shodanOrgAsn(shodan) }}</div></div>
            }
            @if (shodanPorts(shodan).length > 0) {
              <div class="mini-sec">
                <div class="kv-key">Open ports ({{ shodanPorts(shodan).length }})</div>
                <div class="chip-row">
                  @for (p of shodanPorts(shodan).slice(0, 20); track p) { <span class="port-chip">{{ p }}</span> }
                  @if (shodanPorts(shodan).length > 20) { <span class="port-chip">+{{ shodanPorts(shodan).length - 20 }}</span> }
                </div>
              </div>
            }
            @if (shodanCves(shodan).length > 0) {
              <div>
                <div class="kv-key">CVEs ({{ shodanCves(shodan).length }})</div>
                <div class="chip-row">
                  @for (c of shodanCves(shodan).slice(0, 10); track c) { <span class="cve-chip">{{ c }}</span> }
                  @if (shodanCves(shodan).length > 10) { <span class="cve-chip">+{{ shodanCves(shodan).length - 10 }}</span> }
                </div>
              </div>
            }
          </mat-card>
        } @else {
          <mat-card variant="outlined" class="empty-card"><mat-icon class="icon-md muted-icon">stream</mat-icon><span class="empty-text">{{ result.shodan ? 'Shodan — IP not indexed' : 'Shodan — lookup failed' }}</span></mat-card>
        }

        @if (result.google_dns; as dns) {
          <mat-card variant="outlined" class="info-card">
            <div class="card-hdr"><mat-icon class="icon-md" style="color:#1976d2">dns</mat-icon><span class="card-title">Google DNS (PTR)</span></div>
            @if (dnsPtr(dns).length === 0) {
              <span class="kv-key">No PTR record — IP has no reverse DNS entry</span>
            } @else {
              <div class="kv-key">Reverse hostname(s)</div>
              @for (h of dnsPtr(dns); track h) { <div class="dns-hostname">{{ h }}</div> }
            }
          </mat-card>
        } @else {
          <mat-card variant="outlined" class="empty-card"><mat-icon class="icon-md muted-icon">dns</mat-icon><span class="empty-text">Google DNS — lookup failed</span></mat-card>
        }
      </div>

      <!-- Row 2: MaxMind + IPInfo -->
      <div class="card-row">
        @if (result.maxmind && objectKeys(result.maxmind).length > 0) {
          <mat-card variant="outlined" class="info-card">
            <div class="card-hdr"><mat-icon class="icon-md" style="color:#2e7d32">location_on</mat-icon><span class="card-title">MaxMind GeoLite2</span></div>
            <hr class="card-divider" />
            @for (row of maxmindRows(result.maxmind!); track row[0]) {
              <div class="kv-row"><span class="kv-key">{{ row[0] }}</span><span class="kv-val">{{ row[1] }}</span></div>
            }
          </mat-card>
        } @else {
          <mat-card variant="outlined" class="empty-card"><mat-icon class="icon-md muted-icon">location_on</mat-icon><span class="empty-text">{{ result.maxmind === null ? 'MaxMind — API key not configured' : 'MaxMind — IP not found' }}</span></mat-card>
        }

        @if (result.ipinfo; as ipinfo) {
          <mat-card variant="outlined" class="info-card">
            <div class="card-hdr"><mat-icon class="icon-md" [style.color]="privacyColor(ipinfo)">gpp_maybe</mat-icon><span class="card-title">IPInfo Privacy</span></div>
            <span class="privacy-badge" [style.background]="privacyColor(ipinfo)">{{ privacyLabel(ipinfo) }}</span>
            <div class="privacy-flags">
              @for (flag of privacyFlags(ipinfo); track flag[0]) {
                <span class="flag-chip"
                  [style.background]="flag[1] ? privacyFlagColor(flag[0]) : 'var(--mat-sys-surface-container-high)'"
                  [style.color]="flag[1] ? '#fff' : 'var(--mat-sys-on-surface-variant)'"
                  [style.opacity]="flag[1] ? '1' : '0.5'">
                  {{ flag[0] }}
                </span>
              }
            </div>
            @if (ipinfo['service']) {
              <div class="kv-key">Service</div>
              <div class="text-sm font-500">{{ ipinfo['service'] }}</div>
            }
          </mat-card>
        } @else {
          <mat-card variant="outlined" class="empty-card"><mat-icon class="icon-md muted-icon">gpp_maybe</mat-icon><span class="empty-text">IPInfo — API key not configured</span></mat-card>
        }
      </div>

      <!-- IOC hits -->
      <div class="mitre-table-box">
        <div class="ioc-hits-hdr">
          <mat-icon class="icon-sm" style="color:#FFA726">search</mat-icon>
          <span class="ioc-hits-title" style="color:#FFA726">IOC Feed Hits ({{ result.ioc_hits.length }})</span>
        </div>
        @if (result.ioc_hits.length === 0) {
          <div class="ioc-clean">
            <mat-icon class="icon-sm" style="color:#4caf50">check_circle</mat-icon>
            <span class="dim">No IOC hits — IP not seen in MISP or AbuseIPDB feeds.</span>
          </div>
        } @else {
          <table class="mitre-table">
            <thead><tr>
              <th>Source</th>
              <th>Families</th>
              <th>Actors</th>
              <th>TIDs</th>
              <th class="col-date">Last Seen</th>
            </tr></thead>
            <tbody>
              @for (h of result.ioc_hits; track $index) {
                <tr>
                  <td><span class="ioc-src-chip">{{ h.source.replace('_misp', ' MISP') }}</span></td>
                  <td>
                    <div class="chip-row">
                      @for (s of h.family_slugs.slice(0, 2); track s) { <span class="pill pill--family">{{ s }}</span> }
                    </div>
                  </td>
                  <td>
                    <div class="chip-row">
                      @for (s of h.actor_slugs.slice(0, 2); track s) { <span class="pill pill--actor">{{ s }}</span> }
                    </div>
                  </td>
                  <td>
                    <div class="chip-row">
                      @for (t of h.mitre_tids.slice(0, 3); track t) { <span class="pill pill--tid">{{ t }}</span> }
                    </div>
                  </td>
                  <td class="mono dim">{{ h.last_seen?.slice(0, 10) ?? '—' }}</td>
                </tr>
              }
            </tbody>
          </table>
        }
      </div>
    </div>
  }

  @if (!mutation.data() && !mutation.isPending()) {
    <div class="empty-state">
      <mat-icon class="empty-state-icon">router</mat-icon>
      <span class="dim">Enter an IP address above to check AbuseIPDB, Shodan open ports, MaxMind geolocation, IPInfo privacy flags, and IOC feed hits.</span>
    </div>
  }
</div>
  `,
  styles: [`
    .ipe-page { display: flex; flex-direction: column; gap: 16px; }

    .input-row { display: flex; gap: 12px; align-items: center; }
    .ip-field  { flex: 1; max-width: 400px; }
    .mono-input { font-family: monospace; font-size: 0.85rem; }
    .lookup-btn { height: 40px; }

    .results-col { display: flex; flex-direction: column; gap: 16px; }
    .ip-header-row { display: flex; align-items: center; gap: 12px; }
    .ip-label { font-family: monospace; font-size: 1rem; font-weight: 700; }
    .cached-badge {
      font-size: 0.65rem; padding: 2px 8px; border-radius: 8px;
      background: rgba(68,114,196,0.2); color: var(--mat-sys-primary);
    }

    .card-row  { display: flex; gap: 16px; flex-wrap: wrap; }
    .info-card { flex: 1; padding: 14px; min-width: 200px; display: flex; flex-direction: column; gap: 6px; }
    .empty-card { flex: 1; padding: 14px; min-width: 200px; display: flex; align-items: center; gap: 8px; }
    .empty-text { font-size: 0.75rem; color: var(--mat-sys-on-surface-variant); }
    .muted-icon { color: var(--mat-sys-on-surface-variant); opacity: 0.4; }

    .card-hdr   { display: flex; align-items: center; gap: 8px; }
    .card-title { font-size: 0.85rem; font-weight: 700; }
    .card-divider { border: none; border-top: 1px solid var(--mat-sys-outline-variant); margin: 2px 0; }

    .kv-row { display: flex; justify-content: space-between; padding: 2px 0; }
    .kv-key { font-size: 0.68rem; color: var(--mat-sys-on-surface-variant); text-transform: uppercase; letter-spacing: 0.04em; }
    .kv-val { font-size: 0.72rem; font-weight: 500; }
    .mini-sec { display: flex; flex-direction: column; gap: 3px; }
    .text-sm  { font-size: 0.72rem; }
    .mono-sm  { font-size: 0.72rem; font-family: monospace; }
    .font-500 { font-weight: 500; }

    .dns-hostname { font-size: 0.72rem; font-family: monospace; color: #1565c0; }

    .conf-bar-row   { display: flex; align-items: center; gap: 8px; }
    .conf-bar-track { flex: 1; height: 6px; background: var(--mat-sys-surface-container-high); border-radius: 3px; overflow: hidden; }
    .conf-bar-fill  { height: 100%; border-radius: 3px; transition: width 0.4s; }
    .conf-bar-label { font-size: 0.72rem; font-weight: 700; min-width: 32px; }

    .chip-row  { display: flex; flex-wrap: wrap; gap: 3px; }
    .port-chip { display: inline-block; font-size: 0.62rem; height: 16px; padding: 0 5px; line-height: 16px; border-radius: 6px; font-family: monospace; background: var(--mat-sys-surface-container-high); color: var(--mat-sys-on-surface-variant); }
    .cve-chip  { display: inline-block; font-size: 0.62rem; height: 16px; padding: 0 5px; line-height: 16px; border-radius: 6px; background: rgba(211,47,47,0.15); color: #d32f2f; }

    .privacy-badge  { display: inline-block; font-size: 0.72rem; font-weight: 700; padding: 2px 8px; border-radius: 8px; color: #fff; margin-bottom: 4px; }
    .privacy-flags  { display: flex; flex-wrap: wrap; gap: 4px; margin-bottom: 6px; }
    .flag-chip      { display: inline-block; font-size: 0.65rem; height: 18px; padding: 0 7px; line-height: 18px; border-radius: 9px; }

    .ioc-hits-hdr   { display: flex; align-items: center; gap: 8px; padding: 10px 12px 6px; border-bottom: 1px solid var(--mat-sys-outline-variant); }
    .ioc-hits-title { font-size: 0.82rem; font-weight: 700; }
    .ioc-clean      { display: flex; align-items: center; gap: 8px; padding: 12px; }
    .col-date       { width: 90px; }

    .ioc-src-chip { display: inline-block; font-size: 0.65rem; height: 18px; padding: 0 6px; line-height: 18px; border-radius: 8px; background: var(--mat-sys-surface-container-high); color: var(--mat-sys-on-surface-variant); }

    .pill { display: inline-flex; align-items: center; font-size: 0.62rem; height: 16px; padding: 0 5px; border-radius: 8px; white-space: nowrap; background: var(--mat-sys-surface-container-high); color: var(--mat-sys-on-surface-variant); }
    .pill--family { background: rgba(106,27,154,0.12); color: #6a1b9a; }
    .pill--actor  { background: rgba(21,101,192,0.12); color: #1565c0; }
    .pill--tid    { background: rgba(230,145,0,0.12);  color: #9a6500; }
    :host-context(html[data-theme='light']) .pill--family { background: rgba(106,27,154,0.10); color: #4a148c; }
    :host-context(html[data-theme='light']) .pill--actor  { background: rgba(21,101,192,0.10); color: #1565c0; }
    :host-context(html[data-theme='light']) .pill--tid    { background: rgba(186,117,23,0.12); color: #7A4500; }

    .empty-state      { text-align: center; padding: 48px; color: var(--mat-sys-on-surface-variant); }
    .empty-state-icon { font-size: 48px; opacity: 0.2; display: block; margin-bottom: 8px; }

    .mono { font-family: monospace; }
    .dim  { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
  `],
})
export class IpEnrichmentComponent {
  private tiApi = inject(ThreatIntelApiService)
  ip = signal('')

  mutation = injectMutation(() => ({
    mutationFn: (ipAddr: string) => firstValueFrom(this.tiApi.enrichIp(ipAddr)),
  }))

  handleSubmit() {
    const trimmed = this.ip().trim()
    if (trimmed) this.mutation.mutate(trimmed)
  }

  confColor(score: number): string {
    if (score >= 80) return '#d32f2f'
    if (score >= 50) return '#ed6c02'
    if (score >= 25) return '#f9a825'
    return '#388e3c'
  }
  abuseScore(data: Record<string, unknown>): number { return Number(data['abuseConfidenceScore'] ?? 0) }
  abuseRows(data: Record<string, unknown>): [string, string][] {
    return [
      ['ISP / ASN',    String(data['isp'] ?? data['asn'] ?? '—')],
      ['Usage type',   String(data['usageType'] ?? '—')],
      ['Country',      String(data['countryCode'] ?? '—')],
      ['Domain',       String(data['domain'] ?? '—')],
      ['Reports',      String(data['totalReports'] ?? '—')],
      ['Last reported',String(data['lastReportedAt'] ?? '—').slice(0, 10)],
    ]
  }
  shodanData(result: EnrichIpResponse): Record<string, unknown> | null {
    if (!result.shodan) return null
    const d = result.shodan as Record<string, unknown>
    return d['not_found'] ? null : d
  }
  shodanHostnames(d: Record<string, unknown>): string[] { return Array.isArray(d['hostnames']) ? d['hostnames'] as string[] : [] }
  shodanOrgAsn(d: Record<string, unknown>): string {
    return [d['org'], d['asn']].filter(v => v != null && v !== '').join(' · ')
  }
  shodanPorts(d: Record<string, unknown>): number[]     { return Array.isArray(d['ports'])     ? d['ports']     as number[] : [] }
  shodanCves(d: Record<string, unknown>): string[]      { return Array.isArray(d['cves'])      ? d['cves']      as string[] : [] }
  dnsPtr(d: Record<string, unknown>): string[] {
    const ptr = Array.isArray(d['ptr']) ? d['ptr'] as string[] : []
    return Number(d['status'] ?? -1) === 3 || ptr.length === 0 ? [] : ptr
  }
  maxmindRows(data: Record<string, unknown>): [string, string][] {
    return [
      ['Country', [String(data['country_code'] ?? ''), String(data['country_name'] ?? '')].filter(Boolean).join(' — ') || '—'],
      ['City',    String(data['city'] ?? '—')],
      ['ASN',     String(data['asn'] ?? '—')],
      ['Org',     String(data['asn_org'] ?? '—')],
    ]
  }
  privacyLabel(d: Record<string, unknown>): string { return String(d['privacy_label'] ?? 'Clean') }
  privacyColor(d: Record<string, unknown>): string { return PRIVACY_COLORS[this.privacyLabel(d)] ?? '#757575' }
  privacyFlagColor(name: string): string { return PRIVACY_COLORS[name] ?? '#757575' }
  privacyFlags(d: Record<string, unknown>): [string, boolean][] {
    return [['VPN', !!d['is_vpn']], ['Proxy', !!d['is_proxy']], ['Tor', !!d['is_tor']], ['Relay', !!d['is_relay']], ['Hosting', !!d['is_hosting']]]
  }
  objectKeys(obj: Record<string, unknown> | null): string[] { return obj ? Object.keys(obj) : [] }
}
