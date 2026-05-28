import { Component, inject, signal, computed } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { Router } from '@angular/router'
import { firstValueFrom } from 'rxjs'
import { injectQuery, injectMutation, injectQueryClient } from '@tanstack/angular-query-experimental'

import { MatTabsModule } from '@angular/material/tabs'
import { MatChipsModule } from '@angular/material/chips'
import { MatIconModule } from '@angular/material/icon'
import { MatButtonModule } from '@angular/material/button'
import { MatTableModule } from '@angular/material/table'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatSelectModule } from '@angular/material/select'
import { MatSlideToggleModule } from '@angular/material/slide-toggle'

import { FeedsApiService, FeedStatusItem } from '../../api/feeds-api.service'
import { ThreatIntelApiService } from '../../api/threat-intel-api.service'
import { AuthService } from '../../core/services/auth.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'
import { StatusChipComponent } from '../../shared/components/status-chip.component'

const INTEL_COLOR = '#FFA726'

const TI_FEED_DEFS: Pick<FeedStatusItem, 'feed_name' | 'display_name'>[] = [
  { feed_name: 'circl_misp',       display_name: 'MISP CIRCL' },
  { feed_name: 'botvrij_misp',     display_name: 'MISP Botvrij' },
  { feed_name: 'abuseipdb',        display_name: 'AbuseIPDB' },
  { feed_name: 'urlhaus',          display_name: 'URLhaus' },
  { feed_name: 'threatfox',        display_name: 'ThreatFox' },
  { feed_name: 'sslbl',            display_name: 'SSL Blacklist' },
  { feed_name: 'feodotracker',     display_name: 'Feodo Tracker' },
  { feed_name: 'red_flag_domains', display_name: 'Red Flag Domains' },
  { feed_name: 'stopforumspam',    display_name: 'Stopforumspam' },
  { feed_name: 'malwarebazaar',    display_name: 'MalwareBazaar' },
  { feed_name: 'malpedia',         display_name: 'Malpedia' },
  { feed_name: 'alienvault',       display_name: 'AlienVault OTX' },
]
const TI_NAMES = new Set(TI_FEED_DEFS.map(f => f.feed_name))

const TACTIC_COLORS = [
  '#FFA726','#d35400','#e67e22','#f39c12',
  '#c0392b','#e74c3c','#8e44ad','#2980b9',
  '#27ae60','#16a085','#2c3e50','#7f8c8d',
]

function fmt(iso: string | null): string {
  if (!iso) return '—'
  return new Date(iso).toLocaleString(undefined, {
    year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit',
  })
}

function fmtDate(s: string | null) { return s ? s.slice(0, 10) : '—' }

function feedStatusKey(s: string | null): string {
  if (!s) return 'never_run'
  if (s === 'success') return 'success'
  if (s === 'running') return 'running'
  return 'error'
}

export interface KevAuditEntry {
  cve_id: string; vulnerability_name: string | null; vendor_project: string | null
  product: string | null; date_added: string | null; due_date: string | null
  known_ransomware: boolean; evidence_status: string; evidence_id: string | null; evidence_title: string | null
}

const AUDIT_STATUS: Record<string, { bg: string; color: string; label: string }> = {
  no_evidence:    { bg: 'rgba(192,0,0,0.12)',   color: '#9e0000', label: 'No Evidence' },
  pending_review: { bg: 'rgba(230,160,0,0.12)', color: '#7a4800', label: 'Pending' },
  draft:          { bg: 'rgba(0,0,0,0.07)',     color: '#555',    label: 'Draft' },
  active:         { bg: 'rgba(68,114,196,0.12)',color: '#2E5099', label: 'Active' },
  approved:       { bg: 'rgba(46,125,50,0.12)', color: '#1b5e20', label: 'Approved' },
  rejected:       { bg: 'rgba(192,0,0,0.12)',   color: '#9e0000', label: 'Rejected' },
}

@Component({
  selector: 'app-threat-feeds',
  standalone: true,
  imports: [
    FormsModule,
    PageHeaderComponent, StatusChipComponent,
    MatTabsModule, MatChipsModule, MatIconModule, MatButtonModule,
    MatTableModule, MatTooltipModule, MatProgressSpinnerModule,
    MatFormFieldModule, MatSelectModule, MatSlideToggleModule,
  ],
  template: `
<div class="tf-page">
  <app-page-header
    title="Threat Intelligence"
    subtitle="Live threat & vulnerability feeds — MITRE ATT&CK, ATLAS, CISA KEV, EPSS"
  />

  @if (statusQuery.isLoading()) {
    <mat-spinner diameter="20" />
  }
  @if (triggerError()) {
    <div class="alert alert-error">
      <mat-icon>error</mat-icon>
      {{ triggerError() }}
      <button mat-icon-button (click)="triggerError.set(null)"><mat-icon>close</mat-icon></button>
    </div>
  }

  <!-- Feed tabs -->
  <mat-tab-group [(selectedIndex)]="feedTab" class="feed-tabs">
    <mat-tab [label]="'Vulnerability Feeds (' + regularFeeds().length + ')'">
      <div class="feed-grid">
        @for (feed of regularFeeds(); track feed.feed_name) {
          <div class="feed-card">
            <div class="feed-card__header">
              <mat-icon class="feed-icon">security</mat-icon>
              <div class="feed-card__meta">
                <span class="feed-card__name">{{ feed.display_name }}</span>
                <app-status-chip [status]="feedStatusKey(feed.last_status)" />
              </div>
            </div>
            <div class="feed-card__body">
              <span class="feed-card__last">Last: {{ fmt(feed.last_run) }}</span>
              @if (feed.item_count != null && feed.item_count > 0) {
                <span class="feed-card__count">{{ feed.item_count.toLocaleString() }} items</span>
              }
              @if (feed.error_message) {
                <span class="feed-card__error">{{ feed.error_message }}</span>
              }
            </div>
            @if (isAdmin()) {
              <div class="feed-card__actions">
                @if (feed.last_status === 'running') {
                  <button mat-stroked-button color="warn" class="btn-sm"
                    [disabled]="cancelMutation.isPending()"
                    (click)="cancelFeed(feed.feed_name)">
                    <mat-icon>stop</mat-icon> Stop
                  </button>
                } @else {
                  <button mat-stroked-button class="btn-sm"
                    [disabled]="triggerMutation.isPending()"
                    (click)="triggerFeed(feed.feed_name, isDeltaFeed(feed.feed_name) ? 'delta' : undefined)"
                    [matTooltip]="isDeltaFeed(feed.feed_name) ? 'Run delta update now' : 'Run feed now'">
                    <mat-icon>play_arrow</mat-icon>
                    {{ isDeltaFeed(feed.feed_name) ? 'Delta' : 'Run' }}
                  </button>
                  @if (isDeltaFeed(feed.feed_name)) {
                    <button mat-stroked-button color="warn" class="btn-sm"
                      [disabled]="triggerMutation.isPending()"
                      (click)="triggerFeed(feed.feed_name, 'full')"
                      matTooltip="Run full pull (slow — 30-60 min)">
                      <mat-icon>download</mat-icon> Full
                    </button>
                  }
                }
              </div>
            }
          </div>
        }
        @if (!statusQuery.isLoading() && regularFeeds().length === 0) {
          <div class="alert alert-info alert-full-col">
            <mat-icon>hourglass_empty</mat-icon>
            No feed data yet — feeds container will populate data on its first run.
          </div>
        }
      </div>

      <!-- Feed settings (admin) -->
      @if (isAdmin() && feedSettings()) {
        <div class="settings-bar">
          <mat-icon class="tune-icon">tune</mat-icon>
          <span class="settings-bar__label">Feed Settings</span>
          <mat-slide-toggle
            [checked]="feedSettings()!.feeds_cpe_full"
            [disabled]="settingsMutation.isPending()"
            (change)="onCpeFullChange($event.checked)"
            matTooltip="Query NVD CPE API for KEV vendor/product names. Takes effect Sunday 01:30 UTC.">
            NVD CPE Option B (KEV-vendor)
          </mat-slide-toggle>
          @if (settingsMutation.isSuccess()) {
            <span class="settings-saved">Saved</span>
          }
          @if (settingsMutation.isError()) {
            <span class="settings-error">Failed to save</span>
          }
        </div>
      }

      <!-- KEV stats -->
      @if (kevStatsQuery.data(); as ks) {
        <div class="stats-section">
          <div class="stats-section__title">CISA KEV — New Entries by Month</div>
          <div class="stats-section__kpi">
            <div class="kpi-item">
              <span class="kpi-val kpi-val--red">{{ ks.total_entries.toLocaleString() }}</span>
              <span class="kpi-lbl">Total CVEs</span>
            </div>
            <div class="kpi-item">
              <span class="kpi-val kpi-val--red2">{{ ks.ransomware_count.toLocaleString() }}</span>
              <span class="kpi-lbl">Ransomware</span>
            </div>
            <div class="kpi-item">
              <span class="kpi-val kpi-val--orange">{{ ks.recent_30d }}</span>
              <span class="kpi-lbl">Last 30d</span>
            </div>
          </div>
          <div class="bar-chart">
            @for (m of ks.by_month.slice(-12); track m.month) {
              <div class="bar-chart__col">
                <div class="bar-chart__bar"
                  [style.height.%]="barPct(m.count, ks.by_month)"
                  [matTooltip]="m.month + ': ' + m.count">
                </div>
                <span class="bar-chart__label">{{ m.month.slice(2) }}</span>
              </div>
            }
          </div>
        </div>
      }

      <!-- ATT&CK tactic distribution -->
      @if (attackStatsQuery.data(); as attackStats) {
        <div class="stats-section">
          <div class="stats-section__title">ATT&amp;CK Techniques by Tactic</div>
          <div class="stats-section__kpi">
            <div class="kpi-item">
              <span class="kpi-val kpi-val--intel">{{ attackStats.total_techniques.toLocaleString() }}</span>
              <span class="kpi-lbl">Techniques</span>
            </div>
            <div class="kpi-item">
              <span class="kpi-val kpi-val--intel">{{ attackStats.total_subtechniques.toLocaleString() }}</span>
              <span class="kpi-lbl">Sub-techniques</span>
            </div>
          </div>
          <div class="tactic-bars">
            @for (tac of tacticData(); track tac.name; let i = $index) {
              <div class="tactic-bar tactic-bar--link" [matTooltip]="tac.name + ': ' + tac.count"
                (click)="drillTactic()">
                <span class="tactic-bar__name">{{ tac.name }}</span>
                <div class="tactic-bar__track">
                  <div class="tactic-bar__fill"
                    [style.width.%]="tac.pct"
                    [style.background]="tacticColor(i)">
                  </div>
                </div>
                <span class="tactic-bar__count">{{ tac.count }}</span>
              </div>
            }
          </div>
        </div>
      }

      <!-- Recent KEV -->
      @if (recentKevQuery.data(); as rk) {
        @if (rk.items.length > 0) {
          <div class="table-section">
            <div class="table-section__header">
              <span class="table-section__title">Recent CISA KEV Entries</span>
              <span class="table-section__sub">{{ rk.total.toLocaleString() }} total</span>
            </div>
            <table>
              <thead>
                <tr>
                  <th>CVE</th><th>Vendor / Product</th><th>Added</th><th>Ransomware</th>
                </tr>
              </thead>
              <tbody>
                @for (e of rk.items; track e.id) {
                  <tr>
                    <td class="mono red">{{ e.cve_id }}</td>
                    <td class="trunc">{{ e.vendor_project }} — {{ e.product }}</td>
                    <td class="nowrap">{{ e.date_added ?? '—' }}</td>
                    <td>
                      @if (e.known_ransomware) {
                        <span class="chip chip-error">Yes</span>
                      } @else {
                        <span class="dim">No</span>
                      }
                    </td>
                  </tr>
                }
              </tbody>
            </table>
          </div>
        }
      }

      <!-- A.8.8 KEV Audit Report -->
      <div class="table-section">
        <div class="table-section__header">
          <div>
            <span class="table-section__title">A.8.8 KEV Audit Report</span>
            <span class="table-section__sub">CISA KEV entries with evidence status — exportable</span>
          </div>
          <div class="audit-actions">
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="sm-select-field">
              <mat-select [(ngModel)]="auditMonths">
                <mat-option [value]="3">3 months</mat-option>
                <mat-option [value]="6">6 months</mat-option>
                <mat-option [value]="12">12 months</mat-option>
                <mat-option [value]="24">24 months</mat-option>
              </mat-select>
            </mat-form-field>
            @if (auditReportQuery.data()) {
              <button mat-stroked-button class="btn-sm" (click)="exportCsv()">
                <mat-icon>download</mat-icon> Export CSV
              </button>
            }
          </div>
        </div>

        @if (auditReportQuery.data(); as ar) {
          <div class="audit-kpi">
            <div class="kpi-item">
              <span class="kpi-val">{{ ar.total }}</span><span class="kpi-lbl">Total KEV</span>
            </div>
            <div class="kpi-item">
              <span class="kpi-val kpi-val--green">{{ ar.covered }}</span><span class="kpi-lbl">With Evidence</span>
            </div>
            <div class="kpi-item">
              <span class="kpi-val kpi-val--dark-red">{{ ar.uncovered }}</span><span class="kpi-lbl">No Evidence</span>
            </div>
            <div class="kpi-item">
              <span class="kpi-val kpi-val--dark-red">{{ ar.ransomware_uncovered }}</span><span class="kpi-lbl">Ransomware / No Evid.</span>
            </div>
          </div>

          @if (ar.entries.length > 0) {
            <table>
              <thead>
                <tr>
                  <th>CVE</th><th>Vulnerability / Vendor</th><th>Added</th>
                  <th>Due</th><th>Ransomware</th><th>Evidence Status</th>
                </tr>
              </thead>
              <tbody>
                @for (e of ar.entries; track e.cve_id) {
                  <tr>
                    <td class="mono red nowrap">{{ e.cve_id }}</td>
                    <td class="trunc trunc-wide">
                      <span [matTooltip]="e.vulnerability_name ?? ''">{{ e.vulnerability_name ?? '—' }}</span>
                      <span class="dim block">{{ e.vendor_project }}{{ e.product ? ' — ' + e.product : '' }}</span>
                    </td>
                    <td class="nowrap">{{ e.date_added ?? '—' }}</td>
                    <td class="nowrap">{{ e.due_date ?? '—' }}</td>
                    <td>
                      @if (e.known_ransomware) {
                        <span class="chip chip-error">Yes</span>
                      } @else {
                        <span class="dim">No</span>
                      }
                    </td>
                    <td>
                      <span class="audit-status-chip"
                        [style.background]="auditStatusBg(e.evidence_status)"
                        [style.color]="auditStatusFg(e.evidence_status)"
                        [matTooltip]="e.evidence_title ?? ''">
                        {{ auditStatusLabel(e.evidence_status) }}
                      </span>
                    </td>
                  </tr>
                }
              </tbody>
            </table>
          } @else {
            <div class="empty-state">
              <mat-icon>hourglass_empty</mat-icon>
              <span>No KEV entries in the selected window</span>
            </div>
          }
        }
        @if (auditReportQuery.isLoading()) {
          <div class="audit-spinner"><mat-spinner diameter="18" /></div>
        }
      </div>
    </mat-tab>

    <mat-tab>
      <ng-template mat-tab-label>
        Threat Intelligence ({{ tiFeedItems().length }})
        @if (!tiEnabled()) {
          <span class="inactive-badge">inactive</span>
        }
      </ng-template>

      @if (!tiEnabled()) {
        <div class="alert alert-info alert-mb">
          Threat Intelligence feeds require <code>--profile threat-intel</code>.
          Set <code>THREAT_INTEL_ENABLED=true</code> in your .env once the profile is running.
        </div>
      }

      <div class="feed-grid">
        @for (feed of tiFeedItems(); track feed.feed_name) {
          <div class="feed-card" [class.feed-card--disabled]="!tiEnabled()"
            [matTooltip]="!tiEnabled() ? 'Activate with --profile threat-intel' : ''">
            <div class="feed-card__header">
              <mat-icon class="feed-icon">track_changes</mat-icon>
              <div class="feed-card__meta">
                <span class="feed-card__name">{{ feed.display_name }}</span>
                <app-status-chip [status]="feedStatusKey(feed.last_status)" />
              </div>
            </div>
            <div class="feed-card__body">
              <span class="feed-card__last">Last: {{ fmt(feed.last_run) }}</span>
              @if (feed.item_count != null && feed.item_count > 0) {
                <span class="feed-card__count">{{ feed.item_count.toLocaleString() }} items</span>
              }
            </div>
            @if (isAdmin() && tiEnabled()) {
              <div class="feed-card__actions">
                @if (feed.last_status === 'running') {
                  <button mat-stroked-button color="warn" class="btn-sm"
                    [disabled]="tiCancelMutation.isPending()"
                    (click)="tiCancelFeed(feed.feed_name)">
                    <mat-icon>stop</mat-icon> Stop
                  </button>
                } @else {
                  <button mat-stroked-button class="btn-sm"
                    [disabled]="tiTriggerMutation.isPending()"
                    (click)="tiTriggerFeed(feed.feed_name)">
                    <mat-icon>play_arrow</mat-icon> Run
                  </button>
                }
              </div>
            }
          </div>
        }
      </div>

      <!-- IOC stats charts (TI tab) -->
      @if (iocStatsQuery.data(); as is) {
        <div class="charts-row">
          <div class="chart-box">
            <div class="chart-box__title">IOCs by Source</div>
            <div class="hbar-list">
              @for (s of is.source_totals; track s.source; let i = $index) {
                <div class="hbar-row hbar-row--link" [matTooltip]="s.source + ': ' + s.count"
                  (click)="drillSource(s.source)">
                  <span class="hbar-label">{{ s.source.replace('_misp', ' MISP') }}</span>
                  <div class="hbar-track">
                    <div class="hbar-fill" [style.width.%]="hbarPct(s.count, is.source_totals, 'count')" [style.background]="tacticColor(i)"></div>
                  </div>
                  <span class="hbar-count">{{ s.count.toLocaleString() }}</span>
                </div>
              }
            </div>
          </div>
          <div class="chart-box">
            <div class="chart-box__title">IOC Types</div>
            <div class="hbar-list">
              @for (t of is.type_breakdown; track t.type; let i = $index) {
                <div class="hbar-row hbar-row--link" [matTooltip]="t.type + ': ' + t.count"
                  (click)="drillType(t.type)">
                  <span class="hbar-label mono">{{ t.type }}</span>
                  <div class="hbar-track">
                    <div class="hbar-fill" [style.width.%]="hbarPct(t.count, is.type_breakdown, 'count')" [style.background]="tacticColor(i)"></div>
                  </div>
                  <span class="hbar-count">{{ t.count.toLocaleString() }}</span>
                </div>
              }
            </div>
          </div>
          @if (is.top_families.length > 0) {
            <div class="chart-box">
              <div class="chart-box__title">Top Malware Families</div>
              <div class="hbar-list">
                @for (f of is.top_families; track f.family; let i = $index) {
                  <div class="hbar-row hbar-row--link" [matTooltip]="f.family + ': ' + f.count"
                    (click)="drillFamily(f.family)">
                    <span class="hbar-label">{{ f.family }}</span>
                    <div class="hbar-track">
                      <div class="hbar-fill hbar-fill--malware" [style.width.%]="hbarPct(f.count, is.top_families, 'count')"></div>
                    </div>
                    <span class="hbar-count">{{ f.count.toLocaleString() }}</span>
                  </div>
                }
              </div>
            </div>
          }
        </div>
      }
    </mat-tab>
  </mat-tab-group>
</div>
  `,
  styles: [`
    .tf-page {
      display: flex;
      flex-direction: column;
      gap: 16px;
      height: 100%;
      overflow-y: auto;
      box-sizing: border-box;
    }

    .feed-tabs { margin-top: 8px; }
    ::ng-deep .feed-tabs .mat-mdc-tab-body-content { padding-top: 16px; display: flex; flex-direction: column; gap: 16px; }

    .feed-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
      gap: 12px;
    }

    .feed-card {
      background: var(--mat-sys-surface-container);
      border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 8px;
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      transition: border-color 0.15s;
    }
    .feed-card--disabled { opacity: 0.38; }
    .feed-card__header { display: flex; align-items: flex-start; gap: 8px; }
    .feed-icon { font-size: 22px; color: #FFA726; flex-shrink: 0; margin-top: 2px; }
    .feed-card__meta { display: flex; flex-direction: column; gap: 4px; }
    .feed-card__name { font-size: 0.82rem; font-weight: 600; }
    .feed-card__body { display: flex; flex-direction: column; gap: 2px; }
    .feed-card__last { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
    .feed-card__count { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
    .feed-card__error { font-size: 0.7rem; color: var(--mat-sys-error); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .feed-card__actions { display: flex; gap: 4px; flex-wrap: wrap; margin-top: 4px; }

    .chip {
      display: inline-flex; align-items: center; gap: 2px;
      font-size: 0.68rem; height: 20px; padding: 0 6px; border-radius: 10px;
      font-weight: 500;
    }
    .chip mat-icon { font-size: 12px; width: 12px; height: 12px; }
    .chip-default { background: var(--mat-sys-surface-container-high); color: var(--mat-sys-on-surface-variant); }
    .chip-success { background: rgba(0,199,82,0.12); color: #00c752; }
    .chip-info    { background: rgba(21,101,192,0.15); color: #1565c0; }
    .chip-error   { background: rgba(192,0,0,0.15); color: #9e0000; }

    .btn-sm { height: 26px; font-size: 0.72rem; line-height: 26px; padding: 0 8px; }
    .btn-sm mat-icon { font-size: 14px; width: 14px; height: 14px; margin-right: 2px; }

    .alert {
      display: flex; align-items: center; gap: 8px;
      padding: 10px 14px; border-radius: 6px; font-size: 0.82rem;
    }
    .alert mat-icon { font-size: 18px; flex-shrink: 0; }
    .alert-error { background: rgba(192,0,0,0.08); color: var(--mat-sys-error); border: 1px solid rgba(192,0,0,0.2); }
    .alert-info  { background: var(--mat-sys-surface-container); border: 1px solid var(--mat-sys-outline-variant); color: var(--mat-sys-on-surface); }

    .settings-bar {
      display: flex; align-items: center; gap: 12px; flex-wrap: wrap;
      padding: 10px 14px; border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 8px; font-size: 0.82rem;
    }
    .settings-bar__label { font-weight: 600; }
    .settings-saved { color: #00c752; font-size: 0.75rem; }
    .settings-error { color: var(--mat-sys-error); font-size: 0.75rem; }

    .stats-section {
      border: 1px solid var(--mat-sys-outline-variant); border-radius: 8px; padding: 14px;
      background: var(--mat-sys-surface-container);
    }
    .stats-section__title { font-size: 0.85rem; font-weight: 600; margin-bottom: 10px; display: block; }
    .stats-section__kpi { display: flex; gap: 20px; margin-bottom: 12px; flex-wrap: wrap; }
    .kpi-item { display: flex; flex-direction: column; }
    .kpi-val { font-size: 1.3rem; font-weight: 700; line-height: 1; }
    .kpi-lbl { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }

    .bar-chart { display: flex; align-items: flex-end; gap: 3px; height: 100px; }
    .bar-chart__col { display: flex; flex-direction: column; align-items: center; flex: 1; height: 100%; justify-content: flex-end; }
    .bar-chart__bar { width: 100%; background: #c62828; border-radius: 2px 2px 0 0; min-height: 2px; max-height: 80px; }
    .bar-chart__label { font-size: 0.6rem; color: var(--mat-sys-on-surface-variant); margin-top: 2px; }

    .tactic-bars { display: flex; flex-direction: column; gap: 4px; }
    .tactic-bar { display: flex; align-items: center; gap: 8px; border-radius: 4px; padding: 2px 4px; margin: 0 -4px; }
    .tactic-bar--link { cursor: pointer; }
    .tactic-bar--link:hover { background: var(--mat-sys-surface-container-high); }
    .tactic-bar__name { font-size: 0.72rem; width: 130px; flex-shrink: 0; color: var(--mat-sys-on-surface-variant); text-transform: capitalize; }
    .tactic-bar__track { flex: 1; height: 10px; background: var(--mat-sys-surface-container-highest); border-radius: 3px; overflow: hidden; }
    .tactic-bar__fill { height: 100%; border-radius: 3px; transition: width 0.3s; }
    .tactic-bar__count { font-size: 0.7rem; width: 32px; text-align: right; color: var(--mat-sys-on-surface-variant); }

    .table-section { border: 1px solid var(--mat-sys-outline-variant); border-radius: 8px; overflow: hidden; background: var(--mat-sys-surface-container); }
    .table-section__header {
      display: flex; justify-content: space-between; align-items: center;
      padding: 10px 14px; border-bottom: 1px solid var(--mat-sys-outline-variant);
      flex-wrap: wrap; gap: 8px;
    }
    .table-section__title { font-size: 0.85rem; font-weight: 600; display: block; }
    .table-section__sub { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); display: block; }

    table { width: 100%; border-collapse: collapse; }
    thead { background: var(--mat-sys-surface-container); }
    th { font-size: 0.72rem; font-weight: 600; padding: 6px 10px; text-align: left; }
    td { font-size: 0.75rem; padding: 5px 10px; border-top: 1px solid var(--mat-sys-outline-variant); }
    tr:hover td { background: var(--mat-sys-surface-container); }

    .audit-kpi { display: flex; gap: 16px; padding: 12px 14px; border-bottom: 1px solid var(--mat-sys-outline-variant); flex-wrap: wrap; }
    .audit-status-chip {
      display: inline-block; font-size: 0.68rem; padding: 2px 7px; border-radius: 10px;
      font-weight: 500; border: 1px solid transparent;
    }

    .mono { font-family: monospace; }
    .red  { color: #c62828; font-weight: 600; }
    .dim  { color: var(--mat-sys-on-surface-variant); }
    .block { display: block; }
    .nowrap { white-space: nowrap; }
    .trunc { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; max-width: 260px; }

    .sm-select-field {
      width: 140px;
      font-size: 0.78rem;
    }
    .sm-select-field .mat-mdc-text-field-wrapper { padding: 0 8px; }
    .sm-select-field .mat-mdc-select-value { font-size: 0.78rem; }

    .inactive-badge {
      font-size: 0.6rem; background: var(--mat-sys-surface-container-high);
      color: var(--mat-sys-on-surface-variant); padding: 1px 5px;
      border-radius: 8px; margin-left: 4px; opacity: 0.7;
    }

    .empty-state {
      display: flex; align-items: center; justify-content: center;
      gap: 8px; padding: 32px; color: var(--mat-sys-on-surface-variant);
    }

    .charts-row { display: flex; gap: 16px; flex-wrap: wrap; }
    .chart-box { border: 1px solid var(--mat-sys-outline-variant); border-radius: 8px; padding: 14px; flex: 1 1 280px; background: var(--mat-sys-surface-container); }
    .chart-box__title { font-size: 0.85rem; font-weight: 600; margin-bottom: 10px; }
    .hbar-list { display: flex; flex-direction: column; gap: 5px; }
    .hbar-row { display: flex; align-items: center; gap: 8px; border-radius: 4px; padding: 2px 4px; margin: 0 -4px; }
    .hbar-row--link { cursor: pointer; }
    .hbar-row--link:hover { background: var(--mat-sys-surface-container-high); }
    .hbar-label { font-size: 0.7rem; width: 110px; flex-shrink: 0; color: var(--mat-sys-on-surface-variant); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .hbar-track { flex: 1; height: 10px; background: var(--mat-sys-surface-container-highest); border-radius: 3px; overflow: hidden; }
    .hbar-fill { height: 100%; border-radius: 3px; }
    .hbar-fill--malware { background: #b71c1c; }
    .hbar-count { font-size: 0.68rem; width: 50px; text-align: right; color: var(--mat-sys-on-surface-variant); }

    .kpi-val--dark-red { color: #9e0000; }
    .trunc-wide { max-width: 280px; }
    .audit-spinner { padding: 16px; }
    .alert-mb { margin-bottom: 12px; }
  `],
})
export class ThreatFeedsComponent {
  private feedsApi    = inject(FeedsApiService)
  private tiApi       = inject(ThreatIntelApiService)
  private auth        = inject(AuthService)
  private queryClient = injectQueryClient()
  private router      = inject(Router)

  private _feedTab = signal(0)
  get feedTab(): number { return this._feedTab() }
  set feedTab(v: number) { this._feedTab.set(v) }

  private _auditMonths = signal(12)
  get auditMonths(): number { return this._auditMonths() }
  set auditMonths(v: number) { this._auditMonths.set(Number(v)) }

  readonly isAdmin   = computed(() => {
    const role = this.auth.user()?.role
    return role === 'admin' || role === 'super_admin'
  })
  readonly triggerError = signal<string | null>(null)

  readonly statusQuery = injectQuery(() => ({
    queryKey: ['feeds', 'status'],
    queryFn:  () => firstValueFrom(this.feedsApi.getStatus()),
    refetchInterval: 30_000,
  }))

  readonly feedSettingsQuery = injectQuery(() => ({
    queryKey: ['feeds', 'settings'],
    queryFn:  () => firstValueFrom(this.feedsApi.getFeedSettings()),
    enabled:  this.isAdmin(),
  }))

  readonly feedSettings = computed(() => this.feedSettingsQuery.data())

  readonly tiSummaryQuery = injectQuery(() => ({
    queryKey: ['threat-intel', 'summary'],
    queryFn:  () => firstValueFrom(this.tiApi.getSummary()),
    refetchInterval: 30_000,
  }))

  readonly tiEnabled = computed(() => !!this.tiSummaryQuery.data()?.active)

  readonly kevStatsQuery = injectQuery(() => ({
    queryKey: ['feeds', 'kev', 'stats'],
    queryFn:  () => firstValueFrom(this.feedsApi.getKevStats()),
    enabled:  this._feedTab() === 0,
  }))

  readonly attackStatsQuery = injectQuery(() => ({
    queryKey: ['feeds', 'attack', 'stats'],
    queryFn:  () => firstValueFrom(this.feedsApi.getAttackStats()),
  }))

  readonly recentKevQuery = injectQuery(() => ({
    queryKey: ['feeds', 'kev', 'recent'],
    queryFn:  () => firstValueFrom(this.feedsApi.getKev({ per_page: 10, page: 1 })),
  }))

  readonly auditReportQuery = injectQuery(() => ({
    queryKey: ['feeds', 'kev', 'audit', this._auditMonths()],
    queryFn:  () => firstValueFrom(this.feedsApi.getKevAuditReport(this._auditMonths())),
  }))

  readonly iocStatsQuery = injectQuery(() => ({
    queryKey: ['threat-intel', 'ioc-stats'],
    queryFn:  () => firstValueFrom(this.tiApi.getIocStats()),
    enabled:  this._feedTab() === 1,
  }))

  readonly regularFeeds = computed(() => {
    const feeds = this.statusQuery.data()?.feeds ?? []
    return feeds.filter(f => !TI_NAMES.has(f.feed_name))
  })

  readonly tiFeedItems = computed((): FeedStatusItem[] => {
    const summary = this.tiSummaryQuery.data()
    if (summary?.active) {
      return summary.sources.map(s => ({
        feed_name: s.source,
        display_name: s.display_name,
        enabled: s.enabled,
        last_run: s.last_run_at,
        last_status: s.last_run_status,
        item_count: s.ioc_count || null,
        error_message: null,
      }))
    }
    return TI_FEED_DEFS.map(f => ({
      feed_name: f.feed_name, display_name: f.display_name,
      enabled: false, last_run: null, last_status: null, item_count: null, error_message: null,
    }))
  })

  readonly tacticData = computed(() => {
    const stats = this.attackStatsQuery.data()
    if (!stats) return []
    const entries = Object.entries(stats.tactic_counts).sort((a, b) => b[1] - a[1]).slice(0, 12)
    const max = entries[0]?.[1] ?? 1
    return entries.map(([name, count]) => ({ name: name.replace(/-/g, ' '), count, pct: Math.round((count / max) * 100) }))
  })

  readonly triggerMutation = injectMutation(() => ({
    mutationFn: ({ feedName, mode }: { feedName: string; mode?: 'full' | 'delta' }) =>
      firstValueFrom(this.feedsApi.triggerFeed(feedName, mode)),
    onSuccess: () => {
      this.triggerError.set(null)
      setTimeout(() => this.queryClient.invalidateQueries({ queryKey: ['feeds', 'status'] }), 2000)
    },
    onError: (err: any) => this.triggerError.set(err?.error?.detail ?? 'Trigger failed'),
  }))

  readonly cancelMutation = injectMutation(() => ({
    mutationFn: (feedName: string) => firstValueFrom(this.feedsApi.cancelFeed(feedName)),
    onSuccess: () => setTimeout(() => this.queryClient.invalidateQueries({ queryKey: ['feeds', 'status'] }), 3000),
  }))

  readonly tiTriggerMutation = injectMutation(() => ({
    mutationFn: (source: string) => firstValueFrom(this.tiApi.triggerFeed(source)),
    onSuccess: () => {
      this.triggerError.set(null)
      setTimeout(() => this.queryClient.invalidateQueries({ queryKey: ['threat-intel', 'summary'] }), 2000)
    },
    onError: (err: any) => this.triggerError.set(err?.error?.detail ?? 'TI trigger failed'),
  }))

  readonly tiCancelMutation = injectMutation(() => ({
    mutationFn: (source: string) => firstValueFrom(this.tiApi.cancelFeed(source)),
    onSuccess: () => setTimeout(() => this.queryClient.invalidateQueries({ queryKey: ['threat-intel', 'summary'] }), 3000),
  }))

  readonly settingsMutation = injectMutation(() => ({
    mutationFn: (payload: { feeds_cpe_full: boolean }) => firstValueFrom(this.feedsApi.patchFeedSettings(payload)),
    onSuccess: () => this.queryClient.invalidateQueries({ queryKey: ['feeds', 'settings'] }),
  }))

  readonly fmt = fmt
  readonly feedStatusKey = feedStatusKey

  isDeltaFeed(name: string): boolean { return name === 'nist_cve' || name === 'euvd' }
  tacticColor(i: number): string { return TACTIC_COLORS[i % TACTIC_COLORS.length] }

  triggerFeed(name: string, mode?: 'full' | 'delta') {
    this.triggerMutation.mutate({ feedName: name, mode })
  }
  cancelFeed(name: string) { this.cancelMutation.mutate(name) }
  tiTriggerFeed(source: string) { this.tiTriggerMutation.mutate(source) }
  tiCancelFeed(source: string) { this.tiCancelMutation.mutate(source) }

  onCpeFullChange(val: boolean) { this.settingsMutation.mutate({ feeds_cpe_full: val }) }

  barPct(count: number, all: { count: number }[]): number {
    const max = Math.max(...all.map(m => m.count))
    return max > 0 ? Math.round((count / max) * 80) : 0
  }

  hbarPct(count: number, all: any[], key: string): number {
    const max = Math.max(...all.map(i => i[key]))
    return max > 0 ? Math.round((count / max) * 100) : 0
  }

  auditStatusBg(status: string): string { return (AUDIT_STATUS[status] ?? AUDIT_STATUS['draft']).bg }
  auditStatusFg(status: string): string { return (AUDIT_STATUS[status] ?? AUDIT_STATUS['draft']).color }
  auditStatusLabel(status: string): string { return (AUDIT_STATUS[status] ?? { label: status }).label }

  exportCsv() {
    const ar = this.auditReportQuery.data()
    if (!ar) return
    const header = 'CVE ID,Vulnerability Name,Vendor,Product,Date Added,Due Date,Ransomware,Evidence Status,Evidence Title'
    const rows = ar.entries.map((e: KevAuditEntry) => [
      e.cve_id, e.vulnerability_name ?? '', e.vendor_project ?? '',
      e.product ?? '', e.date_added ?? '', e.due_date ?? '',
      e.known_ransomware ? 'Yes' : 'No', e.evidence_status, e.evidence_title ?? '',
    ].map(v => `"${String(v).replace(/"/g, '""')}"`).join(','))
    const csv = [header, ...rows].join('\n')
    const blob = new Blob([csv], { type: 'text/csv' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url; a.download = `KEV-Audit-Report-${this.auditMonths}m.csv`; a.click()
    URL.revokeObjectURL(url)
  }

  drillSource(source: string)  { this.router.navigate(['/ioc-explorer'], { queryParams: { source } }) }
  drillType(ioc_type: string)  { this.router.navigate(['/ioc-explorer'], { queryParams: { ioc_type } }) }
  drillFamily(q: string)       { this.router.navigate(['/ioc-explorer'], { queryParams: { q } }) }
  drillTactic()                { this.router.navigate(['/mitre-attack']) }
}
