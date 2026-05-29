import { Component, inject, signal, computed } from '@angular/core'
import { ThemeService } from '../../core/services/theme.service'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'
import { JsonPipe, DatePipe } from '@angular/common'

import { injectQuery } from '@tanstack/angular-query-experimental'

import { MatCardModule } from '@angular/material/card'
import { MatTableModule } from '@angular/material/table'
import { MatPaginatorModule, PageEvent } from '@angular/material/paginator'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatButtonModule } from '@angular/material/button'
import { MatIconModule } from '@angular/material/icon'
import { MatExpansionModule } from '@angular/material/expansion'
import { MatChipsModule } from '@angular/material/chips'
import { MatTabsModule } from '@angular/material/tabs'
import { MatTooltipModule } from '@angular/material/tooltip'

import {
  AdminApiService,
  AuditLogEntry,
  AuditLogParams,
  FeedRunEntry,
  ConnectorRunEntry,
} from '../../api/admin-api.service'
import { AuthService } from '../../core/services/auth.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

// ── Color maps ───────────────────────────────────────────────────────────────

const SEV_DARK: Record<string, { bg: string; fg: string }> = {
  info:     { bg: 'rgba(68,114,196,0.2)',  fg: '#9DC3E6' },
  warning:  { bg: 'rgba(255,192,0,0.15)', fg: '#FFEB9C' },
  error:    { bg: 'rgba(255,100,0,0.18)', fg: '#FFB347' },
  critical: { bg: 'rgba(192,0,0,0.18)',   fg: '#FFC7CE' },
}
const SEV_LIGHT: Record<string, { bg: string; fg: string }> = {
  info:     { bg: 'rgba(24,95,165,0.11)',   fg: '#185FA5' },
  warning:  { bg: 'rgba(186,117,23,0.13)', fg: '#7A4500' },
  error:    { bg: 'rgba(163,45,45,0.11)',  fg: '#8A1F1F' },
  critical: { bg: 'rgba(163,45,45,0.18)',  fg: '#7A0000' },
}

const CAT_DARK: Record<string, { bg: string; fg: string }> = {
  security: { bg: 'rgba(192,0,0,0.12)',    fg: '#FFC7CE' },
  workflow: { bg: 'rgba(68,114,196,0.12)', fg: '#9DC3E6' },
  system:   { bg: 'rgba(255,255,255,0.07)', fg: '#d9d9d9' },
}
const CAT_LIGHT: Record<string, { bg: string; fg: string }> = {
  security: { bg: 'rgba(163,45,45,0.11)',  fg: '#8A1F1F' },
  workflow: { bg: 'rgba(24,95,165,0.11)',  fg: '#185FA5' },
  system:   { bg: 'rgba(44,44,42,0.07)',   fg: '#444441' },
}

const STATUS_DARK: Record<string, { bg: string; fg: string }> = {
  success: { bg: 'rgba(112,173,71,0.15)', fg: '#C6EFCE' },
  error:   { bg: 'rgba(192,0,0,0.18)',    fg: '#FFC7CE' },
  running: { bg: 'rgba(255,192,0,0.15)',  fg: '#FFEB9C' },
}
const STATUS_LIGHT: Record<string, { bg: string; fg: string }> = {
  success: { bg: 'rgba(29,158,117,0.12)', fg: '#0F6E56' },
  error:   { bg: 'rgba(163,45,45,0.11)', fg: '#8A1F1F' },
  running: { bg: 'rgba(186,117,23,0.13)', fg: '#7A4500' },
}

const FEED_NAMES = ['nist_cve', 'cisa_kev', 'epss', 'euvd', 'mitre_attack', 'mitre_atlas',
                    'mitre_atlas_feed', 'exploit_db', 'alienvault_otx', 'virustotal',
                    'circl_misp', 'botvrij_misp', 'abuseipdb', 'urlhaus',
                    'threatfox', 'sslbl', 'feodo_tracker', 'rfd', 'stopforumspam',
                    'malwarebazaar', 'malpedia']

function fmtDuration(s: number | null): string {
  if (s === null) return '—'
  if (s < 60) return `${s}s`
  const m = Math.floor(s / 60)
  const rem = Math.round(s % 60)
  return rem > 0 ? `${m}m ${rem}s` : `${m}m`
}

function fmtDateShort(iso: string | null): string {
  if (!iso) return '—'
  const d = new Date(iso)
  return d.toLocaleDateString('en-GB', { day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit' })
}

function fmtDateFull(iso: string | null): string {
  if (!iso) return ''
  const d = new Date(iso)
  return d.toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit', second: '2-digit' })
}

@Component({
  selector: 'app-logs',
  standalone: true,
  imports: [
    FormsModule, JsonPipe, DatePipe,
    MatCardModule, MatTableModule, MatPaginatorModule,
    MatFormFieldModule, MatInputModule, MatSelectModule,
    MatButtonModule, MatIconModule, MatExpansionModule,
    MatChipsModule, MatTabsModule, MatTooltipModule,
    PageHeaderComponent,
  ],
  template: `
    @if (!canAccess()) {
      <div class="access-denied-wrap">
        <div class="alert-error">Admin role required to access this page.</div>
      </div>
    } @else {
      <app-page-header title="Logs" subtitle="Audit trail, feed run history, and connector run history" />

      <mat-tab-group [(selectedIndex)]="activeTab" animationDuration="0">

        <!-- ── Audit Trail ─────────────────────────────────────────────────── -->
        <mat-tab>
          <ng-template mat-tab-label>
            <mat-icon class="tab-icon">history</mat-icon>
            Audit Trail
          </ng-template>

          <div class="tab-body">
            <mat-card>
              <mat-card-content>
                <!-- Header row -->
                <div class="card-title-group card-title-group--wrap card-title-group--mb">
                  <mat-icon class="icon-primary">history</mat-icon>
                  <h2 class="card-title">Audit Trail</h2>
                  @if (auditQuery.data()) {
                    <span class="count-chip">{{ auditQuery.data()!.total }} entries</span>
                  }
                  @if (draftFilters.category === 'security') {
                    <span class="count-chip chip-security">
                      Security filter active
                    </span>
                  }
                  <div class="ml-auto">
                    <button mat-stroked-button (click)="exportCsv()">
                      <mat-icon>file_download</mat-icon>
                      Export CSV
                    </button>
                  </div>
                </div>

                <!-- Quick security filter -->
                <div class="quick-filter-row">
                  <button mat-stroked-button color="warn"
                    [class.mat-raised-button]="appliedFilters.category === 'security'"
                    (click)="toggleSecurityFilter()">
                    <mat-icon>security</mat-icon>
                    Security Events
                  </button>
                </div>

                <!-- Filter bar -->
                <div class="filter-bar">
                  <mat-form-field appearance="outline" subscriptSizing="dynamic" class="compact-field field-category">
                    <mat-label>Category</mat-label>
                    <mat-select [(ngModel)]="draftFilters.category">
                      <mat-option value="">All</mat-option>
                      <mat-option value="security">Security</mat-option>
                      <mat-option value="workflow">Workflow</mat-option>
                      <mat-option value="system">System</mat-option>
                    </mat-select>
                  </mat-form-field>

                  <mat-form-field appearance="outline" subscriptSizing="dynamic" class="compact-field field-severity">
                    <mat-label>Severity</mat-label>
                    <mat-select [(ngModel)]="draftFilters.severity">
                      <mat-option value="">All</mat-option>
                      <mat-option value="info">Info</mat-option>
                      <mat-option value="warning">Warning</mat-option>
                      <mat-option value="error">Error</mat-option>
                      <mat-option value="critical">Critical</mat-option>
                    </mat-select>
                  </mat-form-field>

                  <mat-form-field appearance="outline" subscriptSizing="dynamic" class="compact-field field-event-type">
                    <mat-label>Event type</mat-label>
                    <input matInput [(ngModel)]="draftFilters.event_type" placeholder="e.g. login" />
                  </mat-form-field>

                  <mat-form-field appearance="outline" subscriptSizing="dynamic" class="compact-field field-actor-email">
                    <mat-label>Actor email</mat-label>
                    <input matInput [(ngModel)]="draftFilters.actor_email" />
                  </mat-form-field>

                  <mat-form-field appearance="outline" subscriptSizing="dynamic" class="compact-field field-date">
                    <mat-label>From</mat-label>
                    <input matInput type="date" [(ngModel)]="draftFilters.date_from" />
                  </mat-form-field>

                  <mat-form-field appearance="outline" subscriptSizing="dynamic" class="compact-field field-date">
                    <mat-label>To</mat-label>
                    <input matInput type="date" [(ngModel)]="draftFilters.date_to" />
                  </mat-form-field>

                  <button mat-stroked-button (click)="applyFilters()">
                    <mat-icon>filter_list</mat-icon> Apply
                  </button>
                  <button mat-button (click)="clearFilters()">Clear</button>
                </div>

                <!-- Table -->
                <div class="table-scroll">
                  <table mat-table [dataSource]="auditRows()" class="full-width">

                    <ng-container matColumnDef="event_type">
                      <th mat-header-cell *matHeaderCellDef>Event</th>
                      <td mat-cell *matCellDef="let e">
                        <span class="text-mono-xs">{{ e.event_type }}</span>
                      </td>
                    </ng-container>

                    <ng-container matColumnDef="category">
                      <th mat-header-cell *matHeaderCellDef>Category</th>
                      <td mat-cell *matCellDef="let e">
                        <span class="chip-pill"
                          [style.background]="catColor(e.category).bg"
                          [style.color]="catColor(e.category).fg">
                          {{ e.category }}
                        </span>
                      </td>
                    </ng-container>

                    <ng-container matColumnDef="severity">
                      <th mat-header-cell *matHeaderCellDef>Severity</th>
                      <td mat-cell *matCellDef="let e">
                        <span class="chip-pill"
                          [style.background]="sevColor(e.severity).bg"
                          [style.color]="sevColor(e.severity).fg">
                          {{ e.severity }}
                        </span>
                      </td>
                    </ng-container>

                    <ng-container matColumnDef="actor">
                      <th mat-header-cell *matHeaderCellDef>Actor</th>
                      <td mat-cell *matCellDef="let e">
                        <span class="text-muted-xs">
                          {{ e.actor_email ?? (e.user_id ? e.user_id.slice(0,8) + '…' : '—') }}
                        </span>
                      </td>
                    </ng-container>

                    <ng-container matColumnDef="target">
                      <th mat-header-cell *matHeaderCellDef>Target</th>
                      <td mat-cell *matCellDef="let e">
                        @if (e.target_type) {
                          <span class="text-muted-xs">
                            {{ e.target_type }}{{ e.target_id ? ' · ' + e.target_id.slice(0,8) + '…' : '' }}
                          </span>
                        } @else { <span>—</span> }
                      </td>
                    </ng-container>

                    <ng-container matColumnDef="description">
                      <th mat-header-cell *matHeaderCellDef>Description</th>
                      <td mat-cell *matCellDef="let e" class="col-description">
                        <span class="description-cell">
                          {{ e.description ?? '—' }}
                        </span>
                      </td>
                    </ng-container>

                    <ng-container matColumnDef="time">
                      <th mat-header-cell *matHeaderCellDef>Time</th>
                      <td mat-cell *matCellDef="let e">
                        <span [matTooltip]="fmtFull(e.created_at)" class="text-muted-xs text-nowrap">
                          {{ fmtShort(e.created_at) }}
                        </span>
                      </td>
                    </ng-container>

                    <tr mat-header-row *matHeaderRowDef="auditColumns"></tr>
                    <tr mat-row *matRowDef="let row; columns: auditColumns;" class="hover-row"></tr>
                  </table>
                </div>

                @if (auditQuery.isLoading()) {
                  <div class="loading-rows">
                    @for (_ of [1,2,3,4,5]; track $index) {
                      <div class="skeleton-row"></div>
                    }
                  </div>
                }

                @if (!auditQuery.isLoading() && auditRows().length === 0) {
                  <div class="empty-state">
                    No audit log entries found.
                  </div>
                }

                @if (auditQuery.data() && auditQuery.data()!.pages > 1) {
                  <mat-paginator
                    [length]="auditQuery.data()!.total"
                    [pageSize]="pageSize"
                    [pageIndex]="auditPage - 1"
                    [pageSizeOptions]="[25, 50, 100]"
                    (page)="onAuditPage($event)">
                  </mat-paginator>
                }
              </mat-card-content>
            </mat-card>
          </div>
        </mat-tab>

        <!-- ── Feed Runs ───────────────────────────────────────────────────── -->
        <mat-tab>
          <ng-template mat-tab-label>
            <mat-icon class="tab-icon">sync</mat-icon>
            Feed Runs
          </ng-template>

          <div class="tab-body">
            <mat-card>
              <mat-card-content>
                <div class="card-title-group card-title-group--wrap card-title-group--mb">
                  <mat-icon class="icon-primary">sync</mat-icon>
                  <h2 class="card-title">Feed Runs</h2>
                  @if (feedRunsQuery.data()) {
                    <span class="count-chip">{{ feedRunsQuery.data()!.length }} runs</span>
                  }
                  <div class="ml-auto">
                    <button mat-stroked-button
                      [disabled]="feedRunsQuery.isFetching()"
                      (click)="feedRunsQuery.refetch()">
                      <mat-icon>refresh</mat-icon> Refresh
                    </button>
                  </div>
                </div>

                <div class="filter-bar filter-bar--mb">
                  <mat-form-field appearance="outline" subscriptSizing="dynamic" class="compact-field field-feed-name">
                    <mat-label>Feed</mat-label>
                    <mat-select [(ngModel)]="feedFilter" (ngModelChange)="feedFilter = $event">
                      <mat-option value="">All feeds</mat-option>
                      @for (f of feedNames; track f) {
                        <mat-option [value]="f">{{ f }}</mat-option>
                      }
                    </mat-select>
                  </mat-form-field>

                  <mat-form-field appearance="outline" subscriptSizing="dynamic" class="compact-field field-severity">
                    <mat-label>Status</mat-label>
                    <mat-select [(ngModel)]="feedStatusFilter" (ngModelChange)="feedStatusFilter = $event">
                      <mat-option value="">All</mat-option>
                      <mat-option value="success">Success</mat-option>
                      <mat-option value="error">Error</mat-option>
                      <mat-option value="running">Running</mat-option>
                    </mat-select>
                  </mat-form-field>
                </div>

                <div class="table-scroll">
                  <table mat-table [dataSource]="feedRunsQuery.data() ?? []" class="full-width">
                    <ng-container matColumnDef="feed_name">
                      <th mat-header-cell *matHeaderCellDef>Feed</th>
                      <td mat-cell *matCellDef="let r">
                        <span class="text-mono-xs">{{ r.feed_name }}</span>
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="status">
                      <th mat-header-cell *matHeaderCellDef>Status</th>
                      <td mat-cell *matCellDef="let r">
                        <span class="chip-pill"
                          [style.background]="statusColor(r.status).bg"
                          [style.color]="statusColor(r.status).fg">
                          {{ r.status }}
                        </span>
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="started_at">
                      <th mat-header-cell *matHeaderCellDef>Started</th>
                      <td mat-cell *matCellDef="let r">
                        <span [matTooltip]="fmtFull(r.started_at)" class="text-muted-xs text-nowrap">
                          {{ fmtShort(r.started_at) }}
                        </span>
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="duration">
                      <th mat-header-cell *matHeaderCellDef>Duration</th>
                      <td mat-cell *matCellDef="let r">
                        <span class="text-muted-xs">
                          {{ fmtDuration(r.duration_seconds) }}
                        </span>
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="item_count">
                      <th mat-header-cell *matHeaderCellDef>Items</th>
                      <td mat-cell *matCellDef="let r">
                        <span class="text-muted-xs">
                          {{ r.item_count ?? '—' }}
                        </span>
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="error_message">
                      <th mat-header-cell *matHeaderCellDef>Error</th>
                      <td mat-cell *matCellDef="let r" class="col-error">
                        @if (r.error_message) {
                          <span class="error-cell">
                            {{ r.error_message }}
                          </span>
                        } @else {
                          <span class="text-muted-xs">—</span>
                        }
                      </td>
                    </ng-container>

                    <tr mat-header-row *matHeaderRowDef="feedRunColumns"></tr>
                    <tr mat-row *matRowDef="let row; columns: feedRunColumns;" class="hover-row"></tr>
                  </table>
                </div>

                @if (feedRunsQuery.isLoading()) {
                  <div class="loading-rows">
                    @for (_ of [1,2,3,4]; track $index) {
                      <div class="skeleton-row"></div>
                    }
                  </div>
                }
                @if (!feedRunsQuery.isLoading() && (feedRunsQuery.data()?.length ?? 0) === 0) {
                  <div class="empty-state">
                    No feed runs found.
                  </div>
                }
              </mat-card-content>
            </mat-card>
          </div>
        </mat-tab>

        <!-- ── Connector Runs ──────────────────────────────────────────────── -->
        <mat-tab>
          <ng-template mat-tab-label>
            <mat-icon class="tab-icon">electrical_services</mat-icon>
            Connector Runs
          </ng-template>

          <div class="tab-body">
            <mat-card>
              <mat-card-content>
                <div class="card-title-group card-title-group--wrap card-title-group--mb">
                  <mat-icon class="icon-primary">electrical_services</mat-icon>
                  <h2 class="card-title">Connector Runs</h2>
                  @if (connectorRunsQuery.data()) {
                    <span class="count-chip">{{ connectorRunsQuery.data()!.length }} runs</span>
                  }
                  <div class="ml-auto">
                    <button mat-stroked-button
                      [disabled]="connectorRunsQuery.isFetching()"
                      (click)="connectorRunsQuery.refetch()">
                      <mat-icon>refresh</mat-icon> Refresh
                    </button>
                  </div>
                </div>

                <div class="filter-bar filter-bar--mb">
                  <mat-form-field appearance="outline" subscriptSizing="dynamic" class="compact-field field-severity">
                    <mat-label>Status</mat-label>
                    <mat-select [(ngModel)]="connectorStatusFilter" (ngModelChange)="connectorStatusFilter = $event">
                      <mat-option value="">All</mat-option>
                      <mat-option value="success">Success</mat-option>
                      <mat-option value="error">Error</mat-option>
                    </mat-select>
                  </mat-form-field>
                </div>

                <div class="table-scroll">
                  <table mat-table [dataSource]="connectorRunsQuery.data() ?? []" class="full-width">
                    <ng-container matColumnDef="connector_name">
                      <th mat-header-cell *matHeaderCellDef>Connector</th>
                      <td mat-cell *matCellDef="let r">
                        <span class="text-mono-xs">
                          {{ r.connector_name ?? r.connector_id.slice(0,8) + '…' }}
                        </span>
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="status">
                      <th mat-header-cell *matHeaderCellDef>Status</th>
                      <td mat-cell *matCellDef="let r">
                        <span class="chip-pill"
                          [style.background]="statusColor(r.status).bg"
                          [style.color]="statusColor(r.status).fg">
                          {{ r.status }}
                        </span>
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="started_at">
                      <th mat-header-cell *matHeaderCellDef>Started</th>
                      <td mat-cell *matCellDef="let r">
                        <span class="text-muted-xs text-nowrap">
                          {{ fmtShort(r.started_at) }}
                        </span>
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="finished_at">
                      <th mat-header-cell *matHeaderCellDef>Finished</th>
                      <td mat-cell *matCellDef="let r">
                        <span class="text-muted-xs text-nowrap">
                          {{ fmtShort(r.finished_at) }}
                        </span>
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="items">
                      <th mat-header-cell *matHeaderCellDef>Items</th>
                      <td mat-cell *matCellDef="let r">
                        <span class="text-muted-xs">
                          {{ (r.evidence_count ?? r.item_count) ?? '—' }}
                        </span>
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="error_message">
                      <th mat-header-cell *matHeaderCellDef>Error</th>
                      <td mat-cell *matCellDef="let r" class="col-error">
                        @if (r.error_message) {
                          <span class="error-cell">
                            {{ r.error_message }}
                          </span>
                        } @else {
                          <span class="text-muted-xs">—</span>
                        }
                      </td>
                    </ng-container>

                    <tr mat-header-row *matHeaderRowDef="connectorRunColumns"></tr>
                    <tr mat-row *matRowDef="let row; columns: connectorRunColumns;" class="hover-row"></tr>
                  </table>
                </div>

                @if (connectorRunsQuery.isLoading()) {
                  <div class="loading-rows">
                    @for (_ of [1,2,3,4]; track $index) {
                      <div class="skeleton-row"></div>
                    }
                  </div>
                }
                @if (!connectorRunsQuery.isLoading() && (connectorRunsQuery.data()?.length ?? 0) === 0) {
                  <div class="empty-state">
                    No connector runs found.
                  </div>
                }
              </mat-card-content>
            </mat-card>
          </div>
        </mat-tab>

      </mat-tab-group>
    }
  `,
  styles: [`
    :host { display: block; }

    /* ── Layout ─────────────────────────────────────────────────────── */
    .access-denied-wrap { padding: 24px; }
    .tab-body { padding-top: 16px; }
    .table-scroll { overflow-x: auto; }
    .full-width { width: 100%; }
    .empty-state { padding: 32px; text-align: center; color: var(--mat-sys-on-surface-variant); font-size: 0.85rem; }
    .ml-auto { margin-left: auto; }

    /* ── Tab labels ─────────────────────────────────────────────────── */
    .tab-icon { font-size: 18px; margin-right: 6px; }

    /* ── Card headers ───────────────────────────────────────────────── */
    .card-title-group { display: flex; align-items: center; gap: 8px; }
    .card-title-group--wrap { flex-wrap: wrap; }
    .card-title-group--mb { margin-bottom: 16px; }
    .card-title { margin: 0; font-size: 1.1rem; }
    .icon-primary { color: var(--mat-sys-primary); }

    /* ── Chips ──────────────────────────────────────────────────────── */
    .count-chip {
      display: inline-block; padding: 1px 8px; border-radius: 10px;
      background: rgba(0,0,0,0.08); color: var(--mat-sys-on-surface-variant);
      font-size: 0.65rem; height: 18px; line-height: 16px;
    }
    .chip-security { background: rgba(192,0,0,0.18); color: #FFC7CE; }
    .chip-pill {
      display: inline-block; padding: 1px 8px; border-radius: 9px;
      font-size: 0.65rem; height: 18px; line-height: 16px; font-weight: 500;
    }

    /* ── Filter bars ────────────────────────────────────────────────── */
    .filter-bar {
      display: flex; gap: 10px; flex-wrap: wrap; align-items: flex-end; margin-bottom: 16px;
    }
    .filter-bar--mb { margin-bottom: 16px; }
    .quick-filter-row { margin-bottom: 10px; }

    /* ── Filter field widths ────────────────────────────────────────── */
    .field-category    { min-width: 120px; }
    .field-severity    { min-width: 110px; }
    .field-event-type  { width: 160px; }
    .field-actor-email { width: 200px; }
    .field-date        { width: 150px; }
    .field-feed-name   { min-width: 150px; }

    /* ── Text helpers ───────────────────────────────────────────────── */
    .text-muted-xs { font-size: 0.78rem; color: var(--mat-sys-on-surface-variant); }
    .text-mono-xs  { font-family: monospace; font-size: 0.75rem; }
    .text-nowrap   { white-space: nowrap; }

    /* ── Table col helpers ──────────────────────────────────────────── */
    .col-description { max-width: 300px; }
    .col-error       { max-width: 260px; }

    /* ── Cell content ───────────────────────────────────────────────── */
    .description-cell { font-size: 0.78rem; color: var(--mat-sys-on-surface-variant); white-space: normal; word-break: break-word; }
    .error-cell { font-size: 0.78rem; color: var(--mat-sys-error); white-space: normal; word-break: break-word; }

    /* ── Rows ───────────────────────────────────────────────────────── */
    .hover-row:hover { background: rgba(255,255,255,0.03); }
    .loading-rows { padding: 8px 0; }
    .skeleton-row {
      height: 36px; border-radius: 4px; margin-bottom: 4px;
      background: rgba(0,0,0,0.04);
      animation: pulse 1.5s ease-in-out infinite;
    }
    @keyframes pulse {
      0%, 100% { opacity: 1; }
      50%       { opacity: 0.4; }
    }

    /* ── Compact field ──────────────────────────────────────────────── */
    .compact-field { font-size: 0.85rem; }
    ::ng-deep .compact-field .mat-mdc-form-field-subscript-wrapper { display: none; }

    /* ── Alerts ─────────────────────────────────────────────────────── */
    .alert-error {
      padding: 10px 14px; border-radius: 6px; font-size: 0.85rem;
      background: rgba(192,0,0,0.12); color: #FFC7CE;
      border: 1px solid rgba(192,0,0,0.25);
    }
    .alert-info {
      padding: 10px 14px; border-radius: 6px; font-size: 0.8rem;
      background: rgba(68,114,196,0.1); color: var(--mat-sys-on-surface-variant);
      border: 1px solid rgba(68,114,196,0.25);
    }
  `],
})
export class LogsComponent {
  private adminApi = inject(AdminApiService)
  private authService = inject(AuthService)
  private readonly theme = inject(ThemeService)

  canAccess = () => {
    const role = this.authService.user()?.role
    return role === 'super_admin' || role === 'admin'
  }

  activeTab = 0

  // Audit trail state
  auditPage  = 1
  pageSize   = 50
  appliedFilters: AuditLogParams = { page_size: 50 }
  draftFilters: AuditLogParams   = {}

  // Feed runs state
  feedFilter       = ''
  feedStatusFilter = ''
  feedNames        = FEED_NAMES

  // Connector runs state
  connectorStatusFilter = ''

  // Queries
  auditQuery = injectQuery(() => ({
    queryKey: ['logs', 'audit', this.auditPage, JSON.stringify(this.appliedFilters)],
    queryFn:  () => firstValueFrom(this.adminApi.getAuditLog({
      ...this.appliedFilters,
      page: this.auditPage,
      page_size: this.pageSize,
    })),
  }))

  feedRunsQuery = injectQuery(() => ({
    queryKey: ['logs', 'feed-runs', this.feedFilter, this.feedStatusFilter],
    queryFn:  () => firstValueFrom(this.adminApi.getFeedRuns({
      feed_name: this.feedFilter || undefined,
      status:    this.feedStatusFilter || undefined,
      limit: 300,
    })),
  }))

  connectorRunsQuery = injectQuery(() => ({
    queryKey: ['logs', 'connector-runs', this.connectorStatusFilter],
    queryFn:  () => firstValueFrom(this.adminApi.getConnectorRuns({
      status: this.connectorStatusFilter || undefined,
      limit: 300,
    })),
  }))

  auditRows = () => this.auditQuery.data()?.items ?? []

  auditColumns        = ['event_type', 'category', 'severity', 'actor', 'target', 'description', 'time']
  feedRunColumns      = ['feed_name', 'status', 'started_at', 'duration', 'item_count', 'error_message']
  connectorRunColumns = ['connector_name', 'status', 'started_at', 'finished_at', 'items', 'error_message']

  applyFilters(): void {
    this.auditPage      = 1
    this.appliedFilters = { page_size: this.pageSize, ...this.draftFilters }
  }

  clearFilters(): void {
    this.draftFilters   = {}
    this.auditPage      = 1
    this.appliedFilters = { page_size: this.pageSize }
  }

  toggleSecurityFilter(): void {
    this.auditPage = 1
    if (this.appliedFilters.category === 'security') {
      this.appliedFilters   = { page_size: this.pageSize }
      this.draftFilters     = {}
    } else {
      this.appliedFilters   = { page_size: this.pageSize, category: 'security' }
      this.draftFilters     = { category: 'security' }
    }
  }

  onAuditPage(event: PageEvent): void {
    this.auditPage = event.pageIndex + 1
    this.pageSize  = event.pageSize
  }

  async exportCsv(): Promise<void> {
    const all = await firstValueFrom(this.adminApi.getAuditLog({
      ...this.appliedFilters, page: 1, page_size: 10000,
    }))
    const header = 'timestamp,event_type,category,severity,actor_email,description,target_type,ip_address'
    const rows = all.items.map(e =>
      [e.created_at, e.event_type, e.category, e.severity,
       e.actor_email ?? '', (e.description ?? '').replace(/"/g, '""'),
       e.target_type ?? '', e.ip_address ?? '']
        .map(v => `"${v}"`).join(',')
    )
    const csv = [header, ...rows].join('\n')
    const a = document.createElement('a')
    a.href = URL.createObjectURL(new Blob([csv], { type: 'text/csv' }))
    a.download = `isms-audit-log-${new Date().toISOString().slice(0, 10)}.csv`
    a.click()
  }

  // Template helpers
  sevColor    = (s: string) => { const m = this.theme.isDark() ? SEV_DARK    : SEV_LIGHT;    return m[s]    ?? m['info']    }
  catColor    = (c: string) => { const m = this.theme.isDark() ? CAT_DARK    : CAT_LIGHT;    return m[c]    ?? m['system']  }
  statusColor = (s: string) => { const m = this.theme.isDark() ? STATUS_DARK : STATUS_LIGHT; return m[s]    ?? m['success'] }
  fmtShort    = fmtDateShort
  fmtFull     = fmtDateFull
  fmtDuration = fmtDuration
}
