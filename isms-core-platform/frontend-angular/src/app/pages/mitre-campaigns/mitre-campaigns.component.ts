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
import { MatIconModule } from '@angular/material/icon'
import { MatButtonToggleModule } from '@angular/material/button-toggle'

import { FeedsApiService, MitreCampaign } from '../../api/feeds-api.service'

const PER_PAGE = 50
const INTEL_COLOR = '#FFA726'

@Component({
  selector: 'app-mitre-campaigns',
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
    MatButtonToggleModule,
  ],
  template: `
<div class="page-wrap">

  <!-- Header -->
  <div class="page-header">
    <h2 class="page-title">MITRE ATT&amp;CK Campaigns</h2>
    <p class="page-subtitle">
      Targeted intrusion activity clusters — time-bound adversary operations
    </p>
  </div>

  <!-- Total pill -->
  @if (listQuery.data(); as data) {
    <div class="stats-bar">
      <div>
        <div class="stat-value" [style.color]="INTEL_COLOR">{{data.total | number}}</div>
        <div class="stat-label">Campaigns</div>
      </div>
    </div>
  }

  <!-- Filters -->
  <div class="controls-row">
    <mat-button-toggle-group value="attack_v19" class="version-toggle">
      <mat-button-toggle value="attack_v19" class="version-btn">v19</mat-button-toggle>
    </mat-button-toggle-group>

    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="search-field">
      <mat-label>Search</mat-label>
      <mat-icon matPrefix class="search-prefix-icon">search</mat-icon>
      <input matInput [ngModel]="search()" (ngModelChange)="onSearch($event)" placeholder="Search by ID or name…" />
    </mat-form-field>
  </div>

  <!-- Table + detail panel -->
  <div class="content-row" [class.content-row--flush]="!!selected()">

    <!-- Table panel -->
    <div class="table-panel">

      @if (listQuery.isLoading()) {
        <div class="spinner-center">
          <mat-spinner [diameter]="28" />
        </div>
      }

      @if (listQuery.isError()) {
        <div class="error-msg">Failed to load campaigns.</div>
      }

      @if (!listQuery.isLoading() && listQuery.data()?.total === 0) {
        <div class="empty-msg">
          ATT&amp;CK v19 data not yet available. Check back after the scheduled weekly pull.
        </div>
      }

      @if (!listQuery.isLoading() && (listQuery.data()?.items?.length ?? 0) > 0) {
        <table mat-table [dataSource]="listQuery.data()!.items" class="full-width">

          <ng-container matColumnDef="campaign_id">
            <th mat-header-cell *matHeaderCellDef class="col-hdr col-campaign-id">ID</th>
            <td mat-cell *matCellDef="let c" class="cell-id"
              [style.color]="INTEL_COLOR">{{c.campaign_id}}</td>
          </ng-container>

          <ng-container matColumnDef="name">
            <th mat-header-cell *matHeaderCellDef class="col-hdr">Name</th>
            <td mat-cell *matCellDef="let c" class="cell-name">
              {{c.name}}</td>
          </ng-container>

          <ng-container matColumnDef="first_seen">
            <th mat-header-cell *matHeaderCellDef class="col-hdr col-date">First Seen</th>
            <td mat-cell *matCellDef="let c" class="cell-date">
              {{c.first_seen ?? '—'}}</td>
          </ng-container>

          <ng-container matColumnDef="last_seen">
            <th mat-header-cell *matHeaderCellDef class="col-hdr col-date">Last Seen</th>
            <td mat-cell *matCellDef="let c" class="cell-date">
              {{c.last_seen ?? '—'}}</td>
          </ng-container>

          <ng-container matColumnDef="aliases">
            <th mat-header-cell *matHeaderCellDef class="col-hdr">Aliases</th>
            <td mat-cell *matCellDef="let c" class="col-aliases">
              @if (c.aliases.length > 0) {
                @for (a of c.aliases.slice(0, 2); track a) {
                  <mat-chip class="chip-alias">{{a}}</mat-chip>
                }
                @if (c.aliases.length > 2) {
                  <mat-chip [matTooltip]="c.aliases.slice(2).join(', ')"
                    class="chip-alias">+{{c.aliases.length - 2}}</mat-chip>
                }
              } @else {
                <span class="no-aliases">—</span>
              }
            </td>
          </ng-container>

          <tr mat-header-row *matHeaderRowDef="displayedColumns" class="hdr-row"></tr>
          <tr mat-row *matRowDef="let c; columns: displayedColumns"
            class="data-row"
            [style.background]="selected()?.id === c.id ? 'rgba(184,79,0,0.08)' : ''"
            (click)="onRowClick(c)"></tr>
        </table>

        <!-- Pagination -->
        <div class="pagination-bar">
          <span class="page-count">{{listQuery.data()!.total | number}} campaigns</span>
          <div class="page-nav">
            <span class="page-btn" [class.disabled]="page() <= 1"
              (click)="page() > 1 && setPage(page() - 1)">← Prev</span>
            <span class="page-info">{{page()}} / {{totalPages()}}</span>
            <span class="page-btn" [class.disabled]="page() >= totalPages()"
              (click)="page() < totalPages() && setPage(page() + 1)">Next →</span>
          </div>
        </div>
      }
    </div>

    <!-- Detail panel -->
    @if (selected(); as c) {
      <div class="detail-panel">
        <div class="detail-id" [style.color]="INTEL_COLOR">{{c.campaign_id}}</div>
        <div class="detail-name">{{c.name}}</div>

        <div class="detail-dates-row">
          @if (c.first_seen) {
            <div>
              <div class="detail-meta-label">First seen</div>
              <div class="detail-meta-val">{{c.first_seen}}</div>
            </div>
          }
          @if (c.last_seen) {
            <div>
              <div class="detail-meta-label">Last seen</div>
              <div class="detail-meta-val">{{c.last_seen}}</div>
            </div>
          }
        </div>

        @if (c.aliases.length > 0) {
          <div class="detail-aliases-wrap">
            <div class="detail-meta-label detail-meta-gap">Also known as:</div>
            @for (a of c.aliases; track a) {
              <mat-chip class="chip-alias">{{a}}</mat-chip>
            }
          </div>
        }

        @if (c.description) {
          <div class="detail-description">
            {{c.description.slice(0, 700)}}{{c.description.length > 700 ? '…' : ''}}
          </div>
        }

        @if (c.url) {
          <div class="detail-url-wrap">
            <a [href]="c.url" target="_blank" rel="noopener noreferrer"
              class="detail-url" [style.color]="INTEL_COLOR">
              View on attack.mitre.org →
            </a>
          </div>
        }
      </div>
    }
  </div>
</div>
  `,
  styles: [`
    .mat-mdc-row:hover { background: rgba(0,0,0,0.04); }

    .page-wrap {}

    .page-header { margin-bottom: 16px; }
    .page-title { margin: 0; font-size: 1.3rem; font-weight: 700; }
    .page-subtitle { margin: 4px 0 0; color: #888; font-size: 0.85rem; }

    .stats-bar { display: flex; gap: 24px; margin-bottom: 16px; }
    .stat-value { font-size: 1.25rem; font-weight: 700; line-height: 1; }
    .stat-label { font-size: 0.72rem; color: #888; }

    .controls-row { display: flex; gap: 12px; margin-bottom: 16px; align-items: center; flex-wrap: wrap; }
    .version-toggle { height: 32px; }
    .version-btn { font-size: 0.72rem; padding: 0 12px; }
    .search-field { width: 240px; }
    .search-prefix-icon { font-size: 16px; line-height: 1; }

    .content-row { display: flex; gap: 16px; }
    .content-row--flush { margin-right: -24px; }
    .content-row--flush .detail-panel { border-radius: 8px 0 0 8px; border-right: none; }

    .table-panel {
      flex: 1; min-width: 0;
      border: 1px solid var(--mat-sys-outline-variant); border-radius: 8px; overflow: hidden;
      background: var(--mat-sys-surface-container);
    }
    .full-width { width: 100%; }

    .spinner-center { display: flex; justify-content: center; padding: 48px; }
    .error-msg { padding: 16px; color: #d32f2f; font-size: 0.85rem; }
    .empty-msg { padding: 16px; font-size: 0.85rem; color: #888; }

    .col-hdr { font-size: 0.72rem; font-weight: 600; }
    .col-campaign-id { width: 80px; }
    .col-date { width: 100px; }
    .col-aliases { max-width: 200px; }

    .cell-id { font-family: monospace; font-size: 0.75rem; font-weight: 600; }
    .cell-name {
      font-size: 0.78rem; max-width: 200px;
      overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
    }
    .cell-date { font-size: 0.75rem; font-family: monospace; }

    .chip-alias { font-size: 0.62rem; height: 16px; margin: 0 2px 2px 0; }
    .no-aliases { color: #bbb; font-size: 0.75rem; }

    .hdr-row { height: 36px; }
    .data-row { height: 36px; cursor: pointer; }

    .pagination-bar {
      display: flex; justify-content: space-between; align-items: center;
      padding: 8px 16px; border-top: 1px solid var(--mat-sys-outline-variant);
    }
    .page-count { font-size: 0.75rem; color: #888; }
    .page-nav { display: flex; gap: 8px; align-items: center; }
    .page-btn { font-size: 0.75rem; cursor: pointer; color: var(--mat-sys-primary); }
    .page-btn.disabled { color: var(--mat-sys-on-surface-variant); cursor: default; pointer-events: none; }
    .page-info { font-size: 0.75rem; color: #888; }

    .detail-panel {
      width: 320px; flex-shrink: 0;
      border: 1px solid var(--mat-sys-outline-variant); border-radius: 8px;
      padding: 16px; height: fit-content; position: sticky; top: 24px;
      background: var(--mat-sys-surface-container);
    }
    .detail-id { font-family: monospace; font-size: 0.85rem; font-weight: 700; margin-bottom: 4px; }
    .detail-name { font-size: 0.9rem; font-weight: 600; margin-bottom: 8px; }
    .detail-dates-row { display: flex; gap: 16px; margin-bottom: 8px; }
    .detail-meta-label { font-size: 0.72rem; color: #888; }
    .detail-meta-val { font-size: 0.72rem; font-family: monospace; }
    .detail-meta-gap { margin-bottom: 4px; }
    .detail-aliases-wrap { margin-bottom: 8px; }
    .detail-description {
      font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); line-height: 1.5;
      margin-top: 12px; max-height: 300px; overflow-y: auto;
    }
    .detail-url-wrap { margin-top: 8px; }
    .detail-url { font-size: 0.72rem; text-decoration: none; }
  `],
})
export class MitreCampaignsComponent {
  private feedsApi = inject(FeedsApiService)

  readonly INTEL_COLOR = INTEL_COLOR
  readonly displayedColumns = ['campaign_id', 'name', 'first_seen', 'last_seen', 'aliases']

  search = signal('')
  page = signal(1)
  selected = signal<MitreCampaign | null>(null)

  listQuery = injectQuery(() => ({
    queryKey: ['feeds', 'campaigns', 'attack_v19', this.search(), this.page()],
    queryFn: () => firstValueFrom(this.feedsApi.getMitreCampaigns({
      source: 'attack_v19',
      search: this.search() || undefined,
      deprecated: false,
      page: this.page(),
      per_page: PER_PAGE,
    })),
  }))

  totalPages = computed(() => {
    const data = this.listQuery.data()
    return data ? Math.ceil(data.total / PER_PAGE) : 0
  })

  onSearch(v: string) {
    this.search.set(v)
    this.page.set(1)
  }

  setPage(p: number) {
    this.page.set(p)
  }

  onRowClick(c: MitreCampaign) {
    this.selected.set(this.selected()?.id === c.id ? null : c)
  }
}
