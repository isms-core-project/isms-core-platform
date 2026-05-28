import { Component, inject, signal } from '@angular/core'
import { CommonModule } from '@angular/common'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'

import { injectMutation } from '@tanstack/angular-query-experimental'

import { MatTableModule } from '@angular/material/table'
import { MatChipsModule } from '@angular/material/chips'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatIconModule } from '@angular/material/icon'
import { MatButtonModule } from '@angular/material/button'
import { MatDividerModule } from '@angular/material/divider'
import { MatCardModule } from '@angular/material/card'

import { ThreatIntelApiService, EnrichIpResponse, IocRead } from '../../api/threat-intel-api.service'

const INTEL_COLOR = '#FFA726'

const PRIVACY_COLORS: Record<string, string> = {
  Tor: '#b71c1c',
  VPN: '#e65100',
  Proxy: '#f57f17',
  Relay: '#1565c0',
  Hosting: '#6a1b9a',
  Clean: '#2e7d32',
}

@Component({
  selector: 'app-ip-enrichment',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    MatTableModule,
    MatChipsModule,
    MatTooltipModule,
    MatProgressSpinnerModule,
    MatFormFieldModule,
    MatInputModule,
    MatIconModule,
    MatButtonModule,
    MatDividerModule,
    MatCardModule,
  ],
  template: `
<div class="page-root">

  <!-- Header -->
  <div>
    <h2 class="page-title">IP Enrichment</h2>
    <p class="page-subtitle">
      On-demand AbuseIPDB + Shodan + MaxMind + IPInfo lookup — results cached 24h / 30d
    </p>
  </div>

  <!-- Input -->
  <mat-card variant="outlined" class="input-card">
    <form (ngSubmit)="handleSubmit()">
      <div class="input-row">
        <mat-form-field appearance="outline" subscriptSizing="dynamic" class="ip-field">
          <mat-label>IP Address</mat-label>
          <mat-icon matPrefix class="icon-sm">router</mat-icon>
          <input matInput [ngModel]="ip()" (ngModelChange)="ip.set($event)"
            name="ip"
            placeholder="Enter IPv4 or IPv6 address…"
            class="mono-input" />
        </mat-form-field>

        <button mat-flat-button type="submit" color="primary"
          [disabled]="mutation.isPending()"
          class="lookup-btn">
          @if (mutation.isPending()) {
            Looking up…
          } @else {
            <mat-icon class="icon-sm btn-icon">search</mat-icon>
            Lookup
          }
        </button>
      </div>
    </form>
  </mat-card>

  <!-- Error -->
  @if (mutation.isError()) {
    <div class="error-banner">
      Enrichment failed — check API keys or try again.
    </div>
  }

  <!-- Results -->
  @if (mutation.data(); as result) {
    <div class="results-col">

      <!-- IP + cache badge -->
      <div class="ip-header-row">
        <span class="ip-label">{{result.ip}}</span>
        @if (result.cached) {
          <mat-chip [matTooltip]="'Cached ' + (result.cache_age_minutes ?? 0) + ' min ago'"
            class="cached-chip">Cached</mat-chip>
        }
      </div>

      <!-- Row 1: AbuseIPDB + Shodan + DNS -->
      <div class="card-row">

        <!-- AbuseIPDB -->
        @if (result.abuseipdb; as abuse) {
          <mat-card variant="outlined" class="info-card">
            <div class="card-header">
              <mat-icon class="icon-md card-icon-blue">router</mat-icon>
              <span class="card-title">AbuseIPDB</span>
            </div>
            <div class="section-block">
              <div class="label-sm">Abuse confidence score</div>
              <ng-container *ngTemplateOutlet="confBar; context: { score: abuseScore(abuse) }" />
            </div>
            <mat-divider class="divider-sm" />
            @for (row of abuseRows(abuse); track row[0]) {
              <div class="kv-row">
                <span class="kv-key">{{row[0]}}</span>
                <span class="kv-val">{{row[1]}}</span>
              </div>
            }
          </mat-card>
        } @else {
          <mat-card variant="outlined" class="empty-card">
            <mat-icon class="icon-md card-icon-muted">router</mat-icon>
            <span class="empty-text">AbuseIPDB — no result</span>
          </mat-card>
        }

        <!-- Shodan -->
        @if (shodanData(result); as shodan) {
          <mat-card variant="outlined" class="info-card">
            <div class="card-header">
              <mat-icon class="icon-md" [style.color]="INTEL_COLOR">stream</mat-icon>
              <span class="card-title">
                Shodan {{shodan['source'] === 'shodan_internetdb' ? '(InternetDB)' : '(API)'}}
              </span>
            </div>
            @if (shodanHostnames(shodan).length > 0) {
              <div class="mini-section">
                <div class="label-sm">Hostnames</div>
                <div class="mono-sm">{{shodanHostnames(shodan).slice(0,3).join(', ')}}</div>
              </div>
            }
            @if (shodan['org'] || shodan['asn']) {
              <div class="mini-section">
                <div class="label-sm">Org / ASN</div>
                <div class="text-sm">{{[shodan['org'], shodan['asn']].filter(x => !!x).join(' · ')}}</div>
              </div>
            }
            @if (shodanPorts(shodan).length > 0) {
              <div class="mini-section">
                <div class="label-sm chip-label">Open ports ({{shodanPorts(shodan).length}})</div>
                @for (p of shodanPorts(shodan).slice(0, 20); track p) {
                  <mat-chip class="chip-port">{{p}}</mat-chip>
                }
                @if (shodanPorts(shodan).length > 20) {
                  <mat-chip class="chip-port">+{{shodanPorts(shodan).length - 20}}</mat-chip>
                }
              </div>
            }
            @if (shodanCves(shodan).length > 0) {
              <div>
                <div class="label-sm chip-label">CVEs detected ({{shodanCves(shodan).length}})</div>
                @for (c of shodanCves(shodan).slice(0, 10); track c) {
                  <mat-chip class="chip-cve">{{c}}</mat-chip>
                }
                @if (shodanCves(shodan).length > 10) {
                  <mat-chip class="chip-cve">+{{shodanCves(shodan).length - 10}}</mat-chip>
                }
              </div>
            }
          </mat-card>
        } @else {
          <mat-card variant="outlined" class="empty-card">
            <mat-icon class="icon-md card-icon-muted">stream</mat-icon>
            <span class="empty-text">
              {{result.shodan ? 'Shodan — IP not indexed' : 'Shodan — lookup failed'}}
            </span>
          </mat-card>
        }

        <!-- Google DNS -->
        @if (result.google_dns; as dns) {
          <mat-card variant="outlined" class="info-card">
            <div class="card-header">
              <mat-icon class="icon-md card-icon-dns">dns</mat-icon>
              <span class="card-title">Google DNS (PTR)</span>
            </div>
            @if (dnsPtr(dns).length === 0) {
              <span class="label-sm">No PTR record — IP has no reverse DNS entry</span>
            } @else {
              <div class="label-sm chip-label">Reverse hostname(s)</div>
              @for (h of dnsPtr(dns); track h) {
                <div class="dns-hostname">{{h}}</div>
              }
            }
          </mat-card>
        } @else {
          <mat-card variant="outlined" class="empty-card">
            <mat-icon class="icon-md card-icon-muted">dns</mat-icon>
            <span class="empty-text">Google DNS — lookup failed</span>
          </mat-card>
        }
      </div>

      <!-- Row 2: MaxMind + IPInfo -->
      <div class="card-row">

        <!-- MaxMind -->
        @if (result.maxmind && objectKeys(result.maxmind).length > 0; as mm) {
          <mat-card variant="outlined" class="info-card">
            <div class="card-header">
              <mat-icon class="icon-md card-icon-geo">location_on</mat-icon>
              <span class="card-title">MaxMind GeoLite2</span>
            </div>
            <mat-divider class="divider-sm" />
            @for (row of maxmindRows(result.maxmind!); track row[0]) {
              <div class="kv-row">
                <span class="kv-key">{{row[0]}}</span>
                <span class="kv-val">{{row[1]}}</span>
              </div>
            }
          </mat-card>
        } @else {
          <mat-card variant="outlined" class="empty-card">
            <mat-icon class="icon-md card-icon-muted">location_on</mat-icon>
            <span class="empty-text">
              {{result.maxmind === null ? 'MaxMind — API key not configured' : 'MaxMind — IP not found'}}
            </span>
          </mat-card>
        }

        <!-- IPInfo -->
        @if (result.ipinfo; as ipinfo) {
          <mat-card variant="outlined" class="info-card">
            <div class="card-header">
              <mat-icon class="icon-md" [style.color]="privacyColor(ipinfo)">gpp_maybe</mat-icon>
              <span class="card-title">IPInfo Privacy</span>
            </div>
            <div class="mini-section">
              <mat-chip class="privacy-label-chip"
                [style.background]="privacyColor(ipinfo)">
                {{privacyLabel(ipinfo)}}
              </mat-chip>
            </div>
            <div class="privacy-flags">
              @for (flag of privacyFlags(ipinfo); track flag[0]) {
                <mat-chip class="chip-flag"
                  [style.background]="flag[1] ? privacyFlagColor(flag[0]) : ''"
                  [style.color]="flag[1] ? '#fff' : ''"
                  [style.opacity]="flag[1] ? '1' : '0.5'">
                  {{flag[0]}}
                </mat-chip>
              }
            </div>
            @if (ipinfo['service']) {
              <div class="label-sm">Service</div>
              <div class="text-sm font-500">{{ipinfo['service']}}</div>
            }
          </mat-card>
        } @else {
          <mat-card variant="outlined" class="empty-card">
            <mat-icon class="icon-md card-icon-muted">gpp_maybe</mat-icon>
            <span class="empty-text">IPInfo — API key not configured</span>
          </mat-card>
        }
      </div>

      <!-- IOC hits -->
      <mat-card variant="outlined">
        <div class="ioc-header">
          <mat-icon class="icon-sm" [style.color]="INTEL_COLOR">search</mat-icon>
          <span class="ioc-title" [style.color]="INTEL_COLOR">
            IOC Feed Hits ({{result.ioc_hits.length}})
          </span>
        </div>
        <mat-divider />
        @if (result.ioc_hits.length === 0) {
          <div class="ioc-clean-row">
            <mat-icon class="icon-sm ioc-clean-icon">check_circle</mat-icon>
            <span class="label-sm">No IOC hits — IP not seen in MISP or AbuseIPDB feeds.</span>
          </div>
        } @else {
          <table mat-table [dataSource]="result.ioc_hits" class="ioc-table">

            <ng-container matColumnDef="source">
              <th mat-header-cell *matHeaderCellDef class="th-cell">Source</th>
              <td mat-cell *matCellDef="let h">
                <mat-chip class="chip-source">{{h.source.replace('_misp', ' MISP')}}</mat-chip>
              </td>
            </ng-container>

            <ng-container matColumnDef="families">
              <th mat-header-cell *matHeaderCellDef class="th-cell">Families</th>
              <td mat-cell *matCellDef="let h">
                @for (s of h.family_slugs.slice(0, 2); track s) {
                  <mat-chip class="chip-family">{{s}}</mat-chip>
                }
              </td>
            </ng-container>

            <ng-container matColumnDef="actors">
              <th mat-header-cell *matHeaderCellDef class="th-cell">Actors</th>
              <td mat-cell *matCellDef="let h">
                @for (s of h.actor_slugs.slice(0, 2); track s) {
                  <mat-chip class="chip-actor">{{s}}</mat-chip>
                }
              </td>
            </ng-container>

            <ng-container matColumnDef="tids">
              <th mat-header-cell *matHeaderCellDef class="th-cell">TIDs</th>
              <td mat-cell *matCellDef="let h">
                @for (t of h.mitre_tids.slice(0, 3); track t) {
                  <mat-chip class="chip-tid">{{t}}</mat-chip>
                }
              </td>
            </ng-container>

            <ng-container matColumnDef="last_seen">
              <th mat-header-cell *matHeaderCellDef class="th-cell">Last seen</th>
              <td mat-cell *matCellDef="let h" class="cell-mono-muted">
                {{h.last_seen?.slice(0, 10) ?? '—'}}</td>
            </ng-container>

            <tr mat-header-row *matHeaderRowDef="iocCols" class="table-row-sm"></tr>
            <tr mat-row *matRowDef="let h; columns: iocCols" class="table-row-sm"></tr>
          </table>
        }
      </mat-card>
    </div>
  }

  <!-- Empty state -->
  @if (!mutation.data() && !mutation.isPending()) {
    <div class="empty-state">
      <mat-icon class="empty-state-icon">router</mat-icon>
      <span class="empty-state-text">Enter an IP address above to check AbuseIPDB confidence score, Shodan open ports, MaxMind geolocation, IPInfo privacy flags, and cross-reference our IOC feeds.</span>
    </div>
  }
</div>

<!-- Confidence bar template -->
<ng-template #confBar let-score="score">
  <div class="conf-bar-row">
    <div class="conf-bar-track">
      <div class="conf-bar-fill"
        [style.width]="score + '%'"
        [style.background]="confColor(score)"></div>
    </div>
    <span class="conf-bar-label"
      [style.color]="confColor(score)">{{score}}%</span>
  </div>
</ng-template>
  `,
  styles: [`
    .mat-mdc-row:hover { background: rgba(0,0,0,0.04); }

    /* Page layout */
    .page-root { padding: 24px; display: flex; flex-direction: column; gap: 20px; }
    .page-title { margin: 0; font-size: 1.3rem; font-weight: 700; }
    .page-subtitle { margin: 4px 0 0; color: #888; font-size: 0.85rem; }

    /* Input card */
    .input-card { padding: 16px; }
    .input-row { display: flex; gap: 12px; align-items: center; }
    .ip-field { flex: 1; max-width: 400px; }
    .mono-input { font-family: monospace; font-size: 0.85rem; }
    .lookup-btn { font-size: 0.8rem; }
    .btn-icon { font-size: 16px; width: 16px; height: 16px; margin-right: 4px; vertical-align: middle; line-height: 1; }

    /* Error */
    .error-banner {
      padding: 12px;
      background: rgba(211,47,47,0.08);
      border: 1px solid #d32f2f;
      border-radius: 4px;
      color: #d32f2f;
      font-size: 0.85rem;
    }

    /* Results */
    .results-col { display: flex; flex-direction: column; gap: 16px; }
    .ip-header-row { display: flex; align-items: center; gap: 12px; }
    .ip-label { font-family: monospace; font-size: 1rem; font-weight: 700; }
    .cached-chip { font-size: 0.65rem; height: 18px; }

    /* Card rows */
    .card-row { display: flex; gap: 16px; flex-wrap: wrap; }
    .info-card { flex: 1; padding: 16px; min-width: 200px; }
    .empty-card { flex: 1; padding: 16px; min-width: 200px; display: flex; align-items: center; gap: 8px; }
    .empty-text { font-size: 0.75rem; color: #888; }

    /* Card internals */
    .card-header { display: flex; align-items: center; gap: 8px; margin-bottom: 12px; }
    .card-title { font-size: 0.85rem; font-weight: 700; }
    .card-icon-blue { color: #1565c0; }
    .card-icon-muted { color: #bbb; }
    .card-icon-dns { color: #1976d2; }
    .card-icon-geo { color: #2e7d32; }
    .divider-sm { margin: 8px 0; }

    /* KV rows */
    .kv-row { display: flex; justify-content: space-between; padding: 2px 0; }
    .kv-key { font-size: 0.72rem; color: #888; }
    .kv-val { font-size: 0.72rem; font-weight: 500; }

    /* Mini sections */
    .section-block { margin-bottom: 12px; }
    .mini-section { margin-bottom: 8px; }
    .label-sm { font-size: 0.72rem; color: #888; }
    .chip-label { margin-bottom: 4px; }
    .text-sm { font-size: 0.72rem; }
    .mono-sm { font-size: 0.72rem; font-family: monospace; }
    .font-500 { font-weight: 500; }

    /* DNS */
    .dns-hostname { font-size: 0.72rem; font-family: monospace; color: #1565c0; }

    /* Chips */
    .chip-port { font-size: 0.65rem; height: 18px; margin: 0 2px 2px 0; font-family: monospace; }
    .chip-cve { font-size: 0.62rem; height: 18px; margin: 0 2px 2px 0; background: #d32f2f22; color: #d32f2f; }
    .chip-source { font-size: 0.65rem; height: 18px; }
    .chip-family { font-size: 0.62rem; height: 16px; margin: 0 2px; background: rgba(106,27,154,0.12); color: #6a1b9a; }
    .chip-actor { font-size: 0.62rem; height: 16px; margin: 0 2px; background: rgba(21,101,192,0.12); color: #1565c0; }
    .chip-tid { font-size: 0.62rem; height: 16px; margin: 0 2px; background: rgba(230,145,0,0.12); color: #9a6500; }

    /* IPInfo */
    .privacy-label-chip { font-size: 0.72rem; font-weight: 700; color: #fff; }
    .privacy-flags { display: flex; flex-wrap: wrap; gap: 4px; margin-bottom: 8px; }
    .chip-flag { font-size: 0.65rem; height: 18px; }

    /* IOC section */
    .ioc-header { padding: 12px 16px 4px; display: flex; align-items: center; gap: 8px; }
    .ioc-title { font-size: 0.82rem; font-weight: 700; }
    .ioc-clean-row { padding: 8px 16px; display: flex; align-items: center; gap: 8px; }
    .ioc-clean-icon { color: #388e3c; }
    .ioc-table { width: 100%; }
    .th-cell { font-size: 0.72rem; font-weight: 700; }
    .cell-mono-muted { font-size: 0.75rem; font-family: monospace; color: #888; }
    .table-row-sm { height: 36px; }

    /* Empty state */
    .empty-state { text-align: center; padding: 48px; color: #888; }
    .empty-state-icon { font-size: 48px; opacity: 0.2; display: block; margin-bottom: 8px; }
    .empty-state-text { font-size: 0.85rem; }

    /* Confidence bar */
    .conf-bar-row { display: flex; align-items: center; gap: 8px; }
    .conf-bar-track { flex: 1; height: 6px; background: rgba(0,0,0,0.08); border-radius: 3px; overflow: hidden; }
    .conf-bar-fill { height: 100%; border-radius: 3px; transition: width 0.4s; }
    .conf-bar-label { font-size: 0.72rem; font-weight: 700; min-width: 32px; }
  `],
})
export class IpEnrichmentComponent {
  private tiApi = inject(ThreatIntelApiService)

  readonly INTEL_COLOR = INTEL_COLOR
  readonly iocCols = ['source', 'families', 'actors', 'tids', 'last_seen']

  ip = signal('')

  mutation = injectMutation(() => ({
    mutationFn: (ipAddr: string) => firstValueFrom(this.tiApi.enrichIp(ipAddr)),
  }))

  handleSubmit() {
    const trimmed = this.ip().trim()
    if (!trimmed) return
    this.mutation.mutate(trimmed)
  }

  confColor(score: number): string {
    if (score >= 80) return '#d32f2f'
    if (score >= 50) return '#ed6c02'
    if (score >= 25) return '#f9a825'
    return '#388e3c'
  }

  abuseScore(data: Record<string, unknown>): number {
    return Number(data['abuseConfidenceScore'] ?? 0)
  }

  abuseRows(data: Record<string, unknown>): [string, string][] {
    return [
      ['ISP / ASN', String(data['isp'] ?? data['asn'] ?? '—')],
      ['Usage type', String(data['usageType'] ?? '—')],
      ['Country', String(data['countryCode'] ?? '—')],
      ['Domain', String(data['domain'] ?? '—')],
      ['Total reports', String(data['totalReports'] ?? '—')],
      ['Last reported', String(data['lastReportedAt'] ?? '—').slice(0, 10)],
    ]
  }

  shodanData(result: EnrichIpResponse): Record<string, unknown> | null {
    if (!result.shodan) return null
    const d = result.shodan as Record<string, unknown>
    if (d['not_found']) return null
    return d
  }

  shodanHostnames(data: Record<string, unknown>): string[] {
    return Array.isArray(data['hostnames']) ? data['hostnames'] as string[] : []
  }

  shodanPorts(data: Record<string, unknown>): number[] {
    return Array.isArray(data['ports']) ? data['ports'] as number[] : []
  }

  shodanCves(data: Record<string, unknown>): string[] {
    return Array.isArray(data['cves']) ? data['cves'] as string[] : []
  }

  dnsPtr(data: Record<string, unknown>): string[] {
    const ptr = Array.isArray(data['ptr']) ? data['ptr'] as string[] : []
    const status = Number(data['status'] ?? -1)
    return status === 3 || ptr.length === 0 ? [] : ptr
  }

  maxmindRows(data: Record<string, unknown>): [string, string][] {
    return [
      ['Country', [String(data['country_code'] ?? ''), String(data['country_name'] ?? '')].filter(Boolean).join(' — ') || '—'],
      ['City', String(data['city'] ?? '—')],
      ['ASN', String(data['asn'] ?? '—')],
      ['Org', String(data['asn_org'] ?? '—')],
    ]
  }

  privacyLabel(data: Record<string, unknown>): string {
    return String(data['privacy_label'] ?? 'Clean')
  }

  privacyColor(data: Record<string, unknown>): string {
    const label = this.privacyLabel(data)
    return PRIVACY_COLORS[label] ?? '#757575'
  }

  privacyFlagColor(name: string): string {
    return PRIVACY_COLORS[name] ?? '#757575'
  }

  privacyFlags(data: Record<string, unknown>): [string, boolean][] {
    return [
      ['VPN', !!data['is_vpn']],
      ['Proxy', !!data['is_proxy']],
      ['Tor', !!data['is_tor']],
      ['Relay', !!data['is_relay']],
      ['Hosting', !!data['is_hosting']],
    ]
  }

  objectKeys(obj: Record<string, unknown> | null): string[] {
    return obj ? Object.keys(obj) : []
  }
}
