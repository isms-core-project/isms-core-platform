import { Component, inject, signal, computed } from '@angular/core'
import { CommonModule } from '@angular/common'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'

import { injectQuery } from '@tanstack/angular-query-experimental'

import { MatTableModule } from '@angular/material/table'
import { MatChipsModule } from '@angular/material/chips'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatIconModule } from '@angular/material/icon'
import { MatSlideToggleModule } from '@angular/material/slide-toggle'
import { MatButtonModule } from '@angular/material/button'
import { MatDividerModule } from '@angular/material/divider'

import { FeedsApiService, EuvdEntry } from '../../api/feeds-api.service'

const INTEL_COLOR = '#FFA726'
const PER_PAGE = 25

function severityColor(score: number | null): string {
  if (score === null) return '#555'
  if (score >= 9) return '#d32f2f'
  if (score >= 7) return '#ed6c02'
  if (score >= 4) return '#f9a825'
  return '#388e3c'
}

function fmtDate(s: string | null): string {
  return s ? s.slice(0, 10) : '—'
}

@Component({
  selector: 'app-euvd-explorer',
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
    MatSelectModule,
    MatIconModule,
    MatSlideToggleModule,
    MatButtonModule,
    MatDividerModule,
  ],
  template: `
<div class="euvd-root">

  <!-- Header -->
  <div class="euvd-header">
    <h2 class="euvd-title">ENISA EUVD Explorer</h2>
    <p class="euvd-subtitle">
      European Vulnerability Database — actively exploited &amp; critical vulnerabilities under NIS2/CRA
    </p>
  </div>

  <!-- Stats bar -->
  @if (statsQuery.data(); as stats) {
    <div class="stats-bar">
      @for (s of [
        {label:'Total', value: stats.total | number},
        {label:'Exploited', value: stats.exploited | number},
        {label:'Critical', value: stats.critical | number},
        {label:'EU Assigned', value: stats.eu_assigned | number},
        {label:'With CVSS', value: stats.with_cvss | number}
      ]; track s.label) {
        <div>
          <div class="stat-value" [style.color]="INTEL_COLOR">{{s.value}}</div>
          <div class="stat-label">{{s.label}}</div>
        </div>
      }
    </div>
  }

  <!-- Layout: table + detail -->
  <div class="layout-row">

    <!-- Table panel -->
    <div class="table-panel">

      <!-- Filters -->
      <div class="filters-row">
        <mat-form-field appearance="outline" subscriptSizing="dynamic" class="search-field">
          <mat-label>Search</mat-label>
          <mat-icon matPrefix class="search-prefix-icon">search</mat-icon>
          <input matInput [ngModel]="searchInput()" (ngModelChange)="searchInput.set($event)"
            (keydown.enter)="commitSearch()"
            placeholder="Search EUVD ID, CVE, description, vendor…" />
        </mat-form-field>

        <mat-form-field appearance="outline" subscriptSizing="dynamic" class="score-field">
          <mat-label>Score</mat-label>
          <mat-select [ngModel]="minScore()" (ngModelChange)="onMinScore($event)">
            <mat-option value="">Any Score</mat-option>
            <mat-option value="9">Critical (9+)</mat-option>
            <mat-option value="7">High+ (7+)</mat-option>
            <mat-option value="4">Medium+ (4+)</mat-option>
          </mat-select>
        </mat-form-field>

        <div class="toggle-wrap">
          <mat-slide-toggle [checked]="exploitedOnly()" (change)="onExploitedToggle($event.checked)"
            class="toggle-label">Exploited</mat-slide-toggle>
        </div>
        <div class="toggle-wrap">
          <mat-slide-toggle [checked]="criticalOnly()" (change)="onCriticalToggle($event.checked)"
            class="toggle-label">Critical</mat-slide-toggle>
        </div>
        <div class="toggle-wrap">
          <mat-slide-toggle [checked]="euAssignedOnly()" (change)="onEuToggle($event.checked)"
            class="toggle-label">EU Assigned</mat-slide-toggle>
        </div>
      </div>

      <!-- Table -->
      <div class="table-scroll">
        <table mat-table [dataSource]="tableData()" class="euvd-table">

          <ng-container matColumnDef="euvd_id">
            <th mat-header-cell *matHeaderCellDef>EUVD ID</th>
            <td mat-cell *matCellDef="let e">{{e.euvd_id}}</td>
          </ng-container>

          <ng-container matColumnDef="cve_id">
            <th mat-header-cell *matHeaderCellDef>CVE</th>
            <td mat-cell *matCellDef="let e" class="td-cve">{{e.cve_id ?? '—'}}</td>
          </ng-container>

          <ng-container matColumnDef="description">
            <th mat-header-cell *matHeaderCellDef>Description</th>
            <td mat-cell *matCellDef="let e">
              <div class="desc-clamp">{{e.description ?? '—'}}</div>
            </td>
          </ng-container>

          <ng-container matColumnDef="score">
            <th mat-header-cell *matHeaderCellDef>Score</th>
            <td mat-cell *matCellDef="let e" class="td-nowrap">
              @if (e.base_score !== null) {
                <mat-chip class="chip-score"
                  [style.background]="severityColor(e.base_score)">
                  {{e.base_score | number:'1.1-1'}}
                </mat-chip>
              } @else {
                —
              }
            </td>
          </ng-container>

          <ng-container matColumnDef="epss">
            <th mat-header-cell *matHeaderCellDef>EPSS</th>
            <td mat-cell *matCellDef="let e" class="td-epss">
              {{e.epss_score !== null ? (e.epss_score | number:'1.1-1') + '%' : '—'}}</td>
          </ng-container>

          <ng-container matColumnDef="date">
            <th mat-header-cell *matHeaderCellDef>Date</th>
            <td mat-cell *matCellDef="let e" class="td-date">
              {{fmtDate(e.date_published)}}</td>
          </ng-container>

          <ng-container matColumnDef="flags">
            <th mat-header-cell *matHeaderCellDef>Flags</th>
            <td mat-cell *matCellDef="let e">
              <div class="flags-cell">
                @if (e.is_exploited) {
                  <mat-icon class="icon-sm" [style.color]="'#ff6b6b'" [matTooltip]="'Actively Exploited'">warning_amber</mat-icon>
                }
                @if (e.is_critical) {
                  <mat-icon class="icon-sm" [style.color]="'#ed6c02'" [matTooltip]="'Critical Severity'">bug_report</mat-icon>
                }
                @if (e.is_eu_assigned) {
                  <mat-icon class="icon-sm" [style.color]="'#5c7ad6'" [matTooltip]="'EU Assigned'">flag</mat-icon>
                }
              </div>
            </td>
          </ng-container>

          <tr mat-header-row *matHeaderRowDef="displayedColumns" class="table-header-row"></tr>
          <tr mat-row *matRowDef="let e; columns: displayedColumns"
            class="table-data-row"
            [style.background]="selected()?.euvd_id === e.euvd_id ? 'rgba(184,79,0,0.08)' : ''"
            (click)="selected.set(e)"></tr>

          @if (!listQuery.isLoading() && tableData().length === 0) {
            <tr>
              <td [attr.colspan]="displayedColumns.length" class="empty-cell">
                No entries. Trigger the EUVD feed from Threat Feeds to populate data.
              </td>
            </tr>
          }
        </table>

        @if (listQuery.isLoading()) {
          <div class="spinner-wrap">
            <mat-spinner [diameter]="20" />
          </div>
        }
      </div>

      <!-- Pagination -->
      <div class="pagination-row">
        <span class="pagination-total">
          {{listQuery.data() ? (listQuery.data()!.total | number) + ' entries' : ''}}
        </span>
        <div class="pagination-controls">
          <mat-chip class="chip-nav" [class.disabled]="page() <= 1"
            (click)="page() > 1 && setPage(page() - 1)">‹</mat-chip>
          <span class="pagination-page">{{page()}} / {{totalPages()}}</span>
          <mat-chip class="chip-nav" [class.disabled]="page() >= totalPages()"
            (click)="page() < totalPages() && setPage(page() + 1)">›</mat-chip>
        </div>
      </div>
    </div>

    <!-- Detail panel -->
    @if (selected(); as entry) {
      <div class="detail-panel">
        <div class="detail-inner">

          <!-- Header row -->
          <div class="detail-header-row">
            <div>
              <div class="detail-euvd-id">{{entry.euvd_id}}</div>
              @if (entry.cve_id) {
                <div class="detail-cve-id">{{entry.cve_id}}</div>
              }
              <div class="detail-chips-row">
                @if (entry.base_score !== null) {
                  <mat-chip class="chip-score"
                    [style.background]="severityColor(entry.base_score)">
                    {{entry.base_score | number:'1.1-1'}}
                  </mat-chip>
                }
                @if (entry.is_exploited) {
                  <mat-chip class="chip-flag chip-flag--exploited">EXPLOITED</mat-chip>
                }
                @if (entry.is_critical) {
                  <mat-chip class="chip-flag chip-flag--critical">CRITICAL</mat-chip>
                }
                @if (entry.is_eu_assigned) {
                  <mat-chip class="chip-flag chip-flag--eu">EU ASSIGNED</mat-chip>
                }
              </div>
            </div>
            <mat-chip class="chip-close" (click)="selected.set(null)">✕</mat-chip>
          </div>

          <div class="detail-description">{{entry.description ?? 'No description available.'}}</div>

          <!-- Meta grid -->
          <div class="meta-grid">
            @for (row of metaRows(entry); track row[0]) {
              <div>
                <div class="meta-key">{{row[0]}}</div>
                <div class="meta-val">{{row[1]}}</div>
              </div>
            }
          </div>

          @if (entry.vendors.length > 0) {
            <div>
              <div class="detail-section-label">Vendors</div>
              <div class="chip-list">
                @for (v of entry.vendors; track v) {
                  <mat-chip class="chip-tag">{{v}}</mat-chip>
                }
              </div>
            </div>
          }

          @if (entry.products.length > 0) {
            <div>
              <div class="detail-section-label">Products</div>
              <div class="chip-list">
                @for (p of entry.products.slice(0, 20); track p) {
                  <mat-chip class="chip-tag">{{p}}</mat-chip>
                }
                @if (entry.products.length > 20) {
                  <span class="more-label">+{{entry.products.length - 20}} more</span>
                }
              </div>
            </div>
          }

          @if (entry.aliases.length > 0) {
            <div>
              <div class="detail-section-label">Aliases</div>
              <div class="chip-list">
                @for (a of entry.aliases; track a) {
                  <mat-chip class="chip-tag">{{a}}</mat-chip>
                }
              </div>
            </div>
          }
        </div>
      </div>
    }
  </div>
</div>
  `,
  styles: [`
    /* Root */
    .euvd-root { padding: 24px; }

    /* Header */
    .euvd-header { margin-bottom: 16px; }
    .euvd-title { margin: 0; font-size: 1.3rem; font-weight: 700; }
    .euvd-subtitle { margin: 4px 0 0; color: #888; font-size: 0.85rem; }

    /* Stats bar */
    .stats-bar { display: flex; gap: 24px; margin-bottom: 16px; flex-wrap: wrap; }
    .stat-value { font-size: 1.25rem; font-weight: 700; line-height: 1; }
    .stat-label { font-size: 0.72rem; color: #888; }

    /* Layout */
    .layout-row { display: flex; height: calc(100vh - 280px); gap: 12px; overflow: hidden; }
    .table-panel { flex: 1; display: flex; flex-direction: column; min-width: 0; }

    /* Filters */
    .filters-row { display: flex; gap: 8px; margin-bottom: 12px; align-items: center; flex-wrap: wrap; }
    .search-field { flex: 1; min-width: 200px; }
    .search-prefix-icon { font-size: 16px; line-height: 1; }
    .score-field { min-width: 130px; }
    .toggle-wrap { display: flex; align-items: center; gap: 4px; }
    .toggle-label { font-size: 0.8rem; }

    /* Table scroll wrapper */
    .table-scroll { flex: 1; overflow-y: auto; border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; background: var(--mat-sys-surface-container); }
    .euvd-table { width: 100%; }

    /* Column headers */
    .euvd-table th.mat-mdc-header-cell { font-size: 0.72rem; font-weight: 600; }

    /* Column cells */
    .euvd-table .mat-column-euvd_id { font-size: 0.72rem; font-family: monospace; white-space: nowrap; }
    .euvd-table .mat-column-cve_id  { font-size: 0.72rem; white-space: nowrap; }
    .td-cve { font-family: monospace; color: #888; }
    .euvd-table .mat-column-description { max-width: 300px; }
    .euvd-table .mat-column-score { white-space: nowrap; }
    .td-nowrap { white-space: nowrap; }
    .euvd-table .mat-column-epss { font-size: 0.75rem; white-space: nowrap; }
    .td-epss { font-size: 0.75rem; white-space: nowrap; }
    .euvd-table .mat-column-date { font-size: 0.75rem; white-space: nowrap; }
    .td-date { font-size: 0.75rem; white-space: nowrap; }

    /* Description clamp */
    .desc-clamp {
      font-size: 0.72rem; line-height: 1.4;
      display: -webkit-box; -webkit-line-clamp: 2;
      -webkit-box-orient: vertical; overflow: hidden;
    }

    /* Flags cell */
    .flags-cell { display: flex; gap: 2px; }

    /* Table rows */
    .table-header-row { height: 36px; position: sticky; top: 0; z-index: 2; }
    .table-data-row { height: 44px; cursor: pointer; }

    /* Empty state cell */
    .empty-cell { text-align: center; padding: 24px; color: #888; font-size: 0.82rem; }

    /* Spinner */
    .spinner-wrap { display: flex; justify-content: center; padding: 32px; }

    /* Pagination */
    .pagination-row { display: flex; justify-content: space-between; align-items: center; margin-top: 8px; }
    .pagination-total { font-size: 0.75rem; color: #888; }
    .pagination-controls { display: flex; gap: 8px; align-items: center; }
    .pagination-page { font-size: 0.75rem; }
    .chip-nav { cursor: pointer; }

    /* Detail panel */
    .detail-panel {
      width: 380px; flex-shrink: 0; border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 8px; overflow-y: auto;
      background: var(--mat-sys-surface-container);
    }
    .detail-inner { padding: 16px; display: flex; flex-direction: column; gap: 12px; }
    .detail-header-row { display: flex; justify-content: space-between; align-items: flex-start; }
    .detail-euvd-id { font-size: 0.88rem; font-weight: 700; font-family: monospace; }
    .detail-cve-id { font-size: 0.72rem; color: #888; }
    .detail-chips-row { display: flex; gap: 4px; margin-top: 4px; flex-wrap: wrap; }
    .detail-description { font-size: 0.8rem; line-height: 1.6; }

    /* Meta grid */
    .meta-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 4px; }
    .meta-key { font-size: 0.72rem; color: #888; }
    .meta-val { font-size: 0.72rem; font-weight: 500; }

    /* Detail sections */
    .detail-section-label { font-size: 0.72rem; color: #888; margin-bottom: 4px; }
    .chip-list { display: flex; flex-wrap: wrap; gap: 4px; }
    .more-label { font-size: 0.72rem; color: #888; }

    /* Chips */
    .chip-score { font-size: 0.68rem; height: 18px; color: #fff; }
    .chip-flag { font-size: 0.68rem; height: 18px; color: #fff; }
    .chip-flag--exploited { background: #d32f2f; }
    .chip-flag--critical  { background: #b71c1c; }
    .chip-flag--eu        { background: #003399; }
    .chip-close { cursor: pointer; }
    .chip-tag { font-size: 0.65rem; height: 18px; }

    .mat-mdc-row:hover { background: rgba(0,0,0,0.04); }
  `],
})
export class EuvdExplorerComponent {
  private feedsApi = inject(FeedsApiService)

  readonly INTEL_COLOR = INTEL_COLOR
  readonly displayedColumns = ['euvd_id', 'cve_id', 'description', 'score', 'epss', 'date', 'flags']

  searchInput = signal('')
  search = signal('')
  exploitedOnly = signal(false)
  criticalOnly = signal(false)
  euAssignedOnly = signal(false)
  minScore = signal('')
  page = signal(1)
  selected = signal<EuvdEntry | null>(null)

  statsQuery = injectQuery(() => ({
    queryKey: ['euvd', 'stats'],
    queryFn: () => firstValueFrom(this.feedsApi.getEuvdStats()),
    staleTime: 5 * 60_000,
  }))

  listQuery = injectQuery(() => ({
    queryKey: ['euvd', 'list', this.search(), this.exploitedOnly(), this.criticalOnly(), this.euAssignedOnly(), this.minScore(), this.page()],
    queryFn: () => firstValueFrom(this.feedsApi.getEuvd({
      search: this.search() || undefined,
      exploited_only: this.exploitedOnly() || undefined,
      critical_only: this.criticalOnly() || undefined,
      eu_assigned_only: this.euAssignedOnly() || undefined,
      min_score: this.minScore() ? Number(this.minScore()) : undefined,
      page: this.page(),
      per_page: PER_PAGE,
    })),
    staleTime: 2 * 60_000,
  }))

  tableData = computed(() => this.listQuery.data()?.items ?? [])

  totalPages = computed(() => {
    const data = this.listQuery.data()
    return data ? Math.ceil(data.total / PER_PAGE) : 1
  })

  commitSearch() {
    this.search.set(this.searchInput())
    this.page.set(1)
  }

  onMinScore(v: string) {
    this.minScore.set(v)
    this.page.set(1)
  }

  onExploitedToggle(v: boolean) {
    this.exploitedOnly.set(v)
    if (v) { this.criticalOnly.set(false); this.euAssignedOnly.set(false) }
    this.page.set(1)
  }

  onCriticalToggle(v: boolean) {
    this.criticalOnly.set(v)
    if (v) { this.exploitedOnly.set(false); this.euAssignedOnly.set(false) }
    this.page.set(1)
  }

  onEuToggle(v: boolean) {
    this.euAssignedOnly.set(v)
    if (v) { this.exploitedOnly.set(false); this.criticalOnly.set(false) }
    this.page.set(1)
  }

  setPage(p: number) {
    this.page.set(p)
  }

  severityColor(score: number | null): string {
    return severityColor(score)
  }

  fmtDate(s: string | null): string {
    return fmtDate(s)
  }

  metaRows(entry: EuvdEntry): [string, string][] {
    return [
      ['Published', fmtDate(entry.date_published)],
      ['Updated', fmtDate(entry.date_updated)],
      ['Assigner', entry.assigner ?? '—'],
      ['CVSS Version', entry.base_score_version ?? '—'],
      ['EPSS Score', entry.epss_score !== null ? entry.epss_score.toFixed(2) + '%' : '—'],
    ]
  }
}
