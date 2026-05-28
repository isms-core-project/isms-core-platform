import { Component, inject, signal, computed } from '@angular/core'
import { CommonModule } from '@angular/common'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'

import { injectQuery } from '@tanstack/angular-query-experimental'

import { MatTableModule } from '@angular/material/table'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatIconModule } from '@angular/material/icon'
import { MatButtonToggleModule } from '@angular/material/button-toggle'

import { FeedsApiService, MitreGroup } from '../../api/feeds-api.service'
import { ThemeService } from '../../core/services/theme.service'

const PER_PAGE = 50
const INTEL_COLOR_DARK  = '#FFA726'
const INTEL_COLOR_LIGHT = '#E65100'

@Component({
  selector: 'app-mitre-groups',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    MatTableModule,
    MatTooltipModule,
    MatProgressSpinnerModule,
    MatFormFieldModule,
    MatInputModule,
    MatIconModule,
    MatButtonToggleModule,
  ],
  template: `
<div class="grp-page">

  <!-- Header -->
  <div class="grp-header">
    <h2 class="grp-header__title">MITRE ATT&amp;CK Groups</h2>
    <p class="grp-header__sub">
      Threat actor intrusion sets — adversary groups tracked by MITRE ATT&amp;CK
    </p>
  </div>

  <!-- Stats row -->
  @if (statsQuery.data(); as stats) {
    <div class="grp-stats-row">
      <div>
        <div class="grp-stat__val" [style.color]="intelColor">{{stats.total_groups | number}}</div>
        <div class="grp-stat__lbl">Groups</div>
      </div>
      <div>
        <div class="grp-stat__val" [style.color]="intelColor">{{stats.deprecated_count | number}}</div>
        <div class="grp-stat__lbl">Deprecated</div>
      </div>
      <div>
        <div class="grp-stat__val" [style.color]="intelColor">{{stats.sources.join(', ')}}</div>
        <div class="grp-stat__lbl">Sources</div>
      </div>
    </div>
  }

  <!-- Filters -->
  <div class="grp-filters">
    <mat-button-toggle-group value="attack_v19" class="grp-toggle-group">
      <mat-button-toggle value="attack_v19" class="grp-toggle-btn">v19</mat-button-toggle>
    </mat-button-toggle-group>

    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="grp-search-field">
      <mat-label>Search</mat-label>
      <mat-icon matPrefix class="icon-md">search</mat-icon>
      <input matInput [ngModel]="search()" (ngModelChange)="onSearch($event)" placeholder="Search by ID or name…" />
    </mat-form-field>
  </div>

  <!-- Table + detail panel -->
  <div class="grp-layout">

    <!-- Table panel -->
    <div class="grp-table-panel">

      @if (listQuery.isLoading()) {
        <div class="grp-spinner-wrap">
          <mat-spinner [diameter]="28" />
        </div>
      }

      @if (listQuery.isError()) {
        <div class="grp-error">Failed to load groups.</div>
      }

      @if (!listQuery.isLoading() && listQuery.data()?.total === 0) {
        <div class="grp-empty">
          ATT&amp;CK v19 data not yet available. Check back after the scheduled weekly pull.
        </div>
      }

      @if (!listQuery.isLoading() && (listQuery.data()?.items?.length ?? 0) > 0) {
        <table mat-table [dataSource]="listQuery.data()!.items" class="grp-table">

          <ng-container matColumnDef="group_id">
            <th mat-header-cell *matHeaderCellDef class="grp-th">ID</th>
            <td mat-cell *matCellDef="let g" class="grp-cell-id"
              [style.color]="intelColor">{{g.group_id}}</td>
          </ng-container>

          <ng-container matColumnDef="name">
            <th mat-header-cell *matHeaderCellDef class="grp-th">Name</th>
            <td mat-cell *matCellDef="let g" class="grp-cell-name">
              {{g.name}}</td>
          </ng-container>

          <ng-container matColumnDef="aliases">
            <th mat-header-cell *matHeaderCellDef class="grp-th">Aliases</th>
            <td mat-cell *matCellDef="let g" class="grp-cell-aliases">
              @if (g.aliases.length > 0) {
                @for (a of g.aliases.slice(0, 3); track a) {
                  <span class="alias-pill">{{a}}</span>
                }
                @if (g.aliases.length > 3) {
                  <span class="alias-pill" [matTooltip]="g.aliases.slice(3).join(', ')">+{{g.aliases.length - 3}}</span>
                }
              } @else {
                <span class="grp-empty-dash">—</span>
              }
            </td>
          </ng-container>

          <tr mat-header-row *matHeaderRowDef="displayedColumns" class="grp-header-row"></tr>
          <tr mat-row *matRowDef="let g; columns: displayedColumns"
            class="grp-data-row"
            [style.background]="selected()?.id === g.id ? 'rgba(184,79,0,0.08)' : ''"
            (click)="onRowClick(g)"></tr>
        </table>

        <!-- Pagination -->
        <div class="grp-pagination">
          <span class="grp-pagination__count">{{listQuery.data()!.total | number}} groups</span>
          <div class="grp-pagination__nav">
            <span class="grp-pagination__btn" [class.disabled]="page() <= 1"
              (click)="page() > 1 && setPage(page() - 1)">← Prev</span>
            <span class="grp-pagination__info">{{page()}} / {{totalPages()}}</span>
            <span class="grp-pagination__btn" [class.disabled]="page() >= totalPages()"
              (click)="page() < totalPages() && setPage(page() + 1)">Next →</span>
          </div>
        </div>
      }
    </div>

    <!-- Detail panel -->
    @if (selected(); as g) {
      <div class="grp-detail-panel">
        <div class="grp-detail-panel__id" [style.color]="intelColor">{{g.group_id}}</div>
        <div class="grp-detail-panel__name">{{g.name}}</div>

        @if (g.aliases.length > 0) {
          <div class="grp-detail-section">
            <div class="grp-detail-section__label">Also known as:</div>
            @for (a of g.aliases; track a) {
              <span class="alias-pill">{{a}}</span>
            }
          </div>
        }

        @if (g.description) {
          <div class="grp-detail-panel__desc">
            {{g.description.slice(0, 700)}}{{g.description.length > 700 ? '…' : ''}}
          </div>
        }

        @if (g.url) {
          <div class="grp-detail-panel__link-wrap">
            <a [href]="g.url" target="_blank" rel="noopener noreferrer"
              class="grp-detail-panel__link" [style.color]="intelColor">
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

    .grp-page { padding: 24px; }

    .grp-header { margin-bottom: 16px; }
    .grp-header__title { margin: 0; font-size: 1.3rem; font-weight: 700; }
    .grp-header__sub { margin: 4px 0 0; color: var(--mat-sys-on-surface-variant); font-size: 0.85rem; }

    .grp-stats-row { display: flex; gap: 24px; margin-bottom: 16px; flex-wrap: wrap; }
    .grp-stat__val { font-size: 1.25rem; font-weight: 700; line-height: 1; }
    .grp-stat__lbl { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }

    .grp-filters { display: flex; gap: 12px; margin-bottom: 16px; align-items: center; flex-wrap: wrap; }
    .grp-toggle-group { height: 32px; }
    .grp-toggle-btn { font-size: 0.72rem; padding: 0 12px; }
    .grp-search-field { width: 240px; }

    .grp-layout { display: flex; gap: 16px; }

    .grp-table-panel { flex: 1; min-width: 0; border: 1px solid var(--mat-sys-outline-variant); border-radius: 8px; overflow: hidden; background: var(--mat-sys-surface-container); }
    .grp-spinner-wrap { display: flex; justify-content: center; padding: 48px; }
    .grp-error { padding: 16px; color: #d32f2f; font-size: 0.85rem; }
    .grp-empty { padding: 16px; font-size: 0.85rem; color: var(--mat-sys-on-surface-variant); }
    .grp-table { width: 100%; }

    .grp-th { font-size: 0.72rem; font-weight: 600; }
    .mat-column-group_id { width: 80px; }

    .grp-cell-id { font-family: monospace; font-size: 0.75rem; font-weight: 600; }
    .grp-cell-name { font-size: 0.78rem; max-width: 200px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .grp-cell-aliases { max-width: 240px; }

    .grp-mini-chip { font-size: 0.62rem; height: 16px; margin: 0 2px 2px 0; }
    .grp-empty-dash { color: #bbb; font-size: 0.75rem; }

    .grp-header-row { height: 36px; }
    .grp-data-row { height: 36px; cursor: pointer; }

    .grp-pagination { display: flex; justify-content: space-between; align-items: center; padding: 8px 16px; border-top: 1px solid var(--mat-sys-outline-variant); }
    .grp-pagination__count { font-size: 0.75rem; color: var(--mat-sys-on-surface-variant); }
    .grp-pagination__nav { display: flex; gap: 8px; align-items: center; }
    .grp-pagination__btn { font-size: 0.75rem; cursor: pointer; color: var(--mat-sys-primary); }
    .grp-pagination__btn.disabled { color: var(--mat-sys-on-surface-variant); cursor: default; pointer-events: none; }
    .grp-pagination__info { font-size: 0.75rem; color: var(--mat-sys-on-surface-variant); }

    .grp-detail-panel { width: 320px; flex-shrink: 0; border: 1px solid var(--mat-sys-outline-variant); border-radius: 8px; padding: 16px; height: fit-content; position: sticky; top: 24px; background: var(--mat-sys-surface-container); }
    .grp-detail-panel__id { font-family: monospace; font-size: 0.85rem; font-weight: 700; margin-bottom: 4px; }
    .grp-detail-panel__name { font-size: 0.9rem; font-weight: 600; margin-bottom: 8px; }
    .grp-detail-panel__desc { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); line-height: 1.5; margin-top: 12px; max-height: 320px; overflow-y: auto; }
    .grp-detail-panel__link-wrap { margin-top: 8px; }
    .grp-detail-panel__link { font-size: 0.72rem; text-decoration: none; }

    .grp-detail-section { margin-bottom: 8px; }
    .grp-detail-section__label { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); margin-bottom: 4px; }

    .alias-pill {
      display: inline-block; font-size: 0.62rem; padding: 1px 7px; margin: 0 2px 3px 0;
      border-radius: 4px; line-height: 18px; white-space: nowrap;
      background: var(--mat-sys-surface-container-high);
      color: var(--mat-sys-on-surface-variant);
      border: 1px solid var(--mat-sys-outline-variant);
    }
  `],
})
export class MitreGroupsComponent {
  private feedsApi = inject(FeedsApiService)
  private readonly theme = inject(ThemeService)

  get intelColor() { return this.theme.isDark() ? INTEL_COLOR_DARK : INTEL_COLOR_LIGHT }
  readonly displayedColumns = ['group_id', 'name', 'aliases']

  search = signal('')
  page = signal(1)
  selected = signal<MitreGroup | null>(null)

  statsQuery = injectQuery(() => ({
    queryKey: ['feeds', 'groups', 'stats'],
    queryFn: () => firstValueFrom(this.feedsApi.getMitreGroupStats()),
  }))

  listQuery = injectQuery(() => ({
    queryKey: ['feeds', 'groups', 'attack_v19', this.search(), this.page()],
    queryFn: () => firstValueFrom(this.feedsApi.getMitreGroups({
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

  onRowClick(g: MitreGroup) {
    this.selected.set(this.selected()?.id === g.id ? null : g)
  }
}
