import { Component, inject, signal, computed } from '@angular/core'
import { DecimalPipe } from '@angular/common'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'
import { injectQuery } from '@tanstack/angular-query-experimental'

import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatIconModule } from '@angular/material/icon'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'

import { FeedsApiService, MitreGroup } from '../../api/feeds-api.service'
import { ThemeService } from '../../core/services/theme.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

const INTEL_DARK  = '#FFA726'
const INTEL_LIGHT = '#BA7517'
const PER_PAGE = 50

@Component({
  selector: 'app-mitre-groups',
  standalone: true,
  imports: [
    DecimalPipe, FormsModule, PageHeaderComponent,
    MatFormFieldModule, MatInputModule,
    MatIconModule, MatTooltipModule, MatProgressSpinnerModule,
  ],
  template: `
<div class="grp-page">
  <app-page-header
    title="Groups"
    subtitle="MITRE ATT&CK — threat actor intrusion sets tracked by MITRE"
  />

  @if (statsQuery.data(); as s) {
    <div class="mitre-stats">
      <div><div class="mitre-stat__val" [style.color]="intelColor">{{ s.total_groups | number }}</div><div class="mitre-stat__lbl">Groups</div></div>
      <div><div class="mitre-stat__val" [style.color]="intelColor">{{ s.deprecated_count | number }}</div><div class="mitre-stat__lbl">Deprecated</div></div>
      <div><div class="mitre-stat__val" [style.color]="intelColor">{{ s.sources.join(', ') }}</div><div class="mitre-stat__lbl">Source</div></div>
    </div>
  }

  <div class="mitre-filters">
    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="mitre-search">
      <mat-label>Search groups…</mat-label>
      <mat-icon matPrefix>search</mat-icon>
      <input matInput [ngModel]="search()" (ngModelChange)="onSearch($event)" />
    </mat-form-field>
  </div>

  <div class="mitre-layout">
    <div class="mitre-table-box">
      @if (listQuery.isLoading()) {
        <div class="mitre-empty"><mat-spinner diameter="28" /></div>
      }
      @if (listQuery.isError()) {
        <div class="mitre-error">Failed to load groups.</div>
      }
      @if (!listQuery.isLoading() && listQuery.data()?.total === 0) {
        <div class="mitre-empty">No ATT&CK v19 data yet — check back after the scheduled weekly pull.</div>
      }
      @if (!listQuery.isLoading() && (listQuery.data()?.items?.length ?? 0) > 0) {
        <table class="mitre-table">
          <thead><tr>
            <th class="col-id">ID</th>
            <th class="col-name">Name</th>
            <th>Aliases</th>
          </tr></thead>
          <tbody>
            @for (g of listQuery.data()!.items; track g.id) {
              <tr class="mitre-row" [class.mitre-row--selected]="selected()?.id === g.id" (click)="onRowClick(g)">
                <td class="mono" [style.color]="intelColor">{{ g.group_id }}</td>
                <td class="cell-name">{{ g.name }}</td>
                <td>
                  <div class="alias-row">
                    @for (a of g.aliases.slice(0, 3); track a) {
                      <span class="alias-pill" [matTooltip]="a">{{ a }}</span>
                    }
                    @if (g.aliases.length > 3) {
                      <span class="alias-pill" [matTooltip]="g.aliases.slice(3).join(', ')">+{{ g.aliases.length - 3 }}</span>
                    }
                  </div>
                </td>
              </tr>
            }
          </tbody>
        </table>
        <div class="mitre-pagination">
          <span>{{ listQuery.data()!.total | number }} groups</span>
          <div class="mitre-pagination__nav">
            <span class="mitre-pagination__btn" [class.disabled]="page() <= 1" (click)="page() > 1 && setPage(page() - 1)">← Prev</span>
            <span>{{ page() }} / {{ totalPages() }}</span>
            <span class="mitre-pagination__btn" [class.disabled]="page() >= totalPages()" (click)="page() < totalPages() && setPage(page() + 1)">Next →</span>
          </div>
        </div>
      }
    </div>

    @if (selected(); as g) {
      <div class="mitre-detail">
        <div class="mitre-detail__id" [style.color]="intelColor">{{ g.group_id }}</div>
        <div class="mitre-detail__name">{{ g.name }}</div>
        @if (g.aliases.length > 0) {
          <div class="mitre-detail__label">Also known as</div>
          <div class="alias-row alias-row--wrap">
            @for (a of g.aliases; track a) {
              <span class="alias-pill">{{ a }}</span>
            }
          </div>
        }
        @if (g.description) {
          <div class="mitre-detail__desc">{{ g.description.slice(0, 700) }}{{ g.description.length > 700 ? '…' : '' }}</div>
        }
        @if (g.url) {
          <a [href]="g.url" target="_blank" rel="noopener noreferrer" class="mitre-detail__link" [style.color]="intelColor">View on attack.mitre.org →</a>
        }
      </div>
    }
  </div>
</div>
  `,
  styles: [`
    .grp-page { display: flex; flex-direction: column; gap: 16px; }
    .col-id   { width: 80px; }
    .col-name { width: 180px; }
    .cell-name { font-size: 0.78rem; font-weight: 500; }
    .mono { font-family: monospace; font-weight: 600; }
    .alias-row { display: flex; gap: 3px; align-items: center; flex-wrap: nowrap; overflow: hidden; }
    .alias-row--wrap { flex-wrap: wrap; gap: 4px; margin-top: 4px; }
    .alias-pill {
      display: inline-block; font-size: 0.62rem; padding: 1px 6px;
      border-radius: 4px; white-space: nowrap; max-width: 110px;
      overflow: hidden; text-overflow: ellipsis; flex-shrink: 0;
      background: var(--mat-sys-surface-container-high);
      color: var(--mat-sys-on-surface-variant);
      border: 1px solid var(--mat-sys-outline-variant);
    }
    :host-context(html[data-theme='light']) .alias-pill { background: #C4C2B8; color: #2C2C2A; border-color: rgba(44,44,42,0.2); }
  `],
})
export class MitreGroupsComponent {
  private feedsApi = inject(FeedsApiService)
  private readonly theme = inject(ThemeService)

  get intelColor() { return this.theme.isDark() ? INTEL_DARK : INTEL_LIGHT }

  search = signal('')
  page   = signal(1)
  selected = signal<MitreGroup | null>(null)

  readonly statsQuery = injectQuery(() => ({
    queryKey: ['feeds', 'groups', 'stats'],
    queryFn: () => firstValueFrom(this.feedsApi.getMitreGroupStats()),
  }))

  readonly listQuery = injectQuery(() => ({
    queryKey: ['feeds', 'groups', 'attack_v19', this.search(), this.page()],
    queryFn: () => firstValueFrom(this.feedsApi.getMitreGroups({
      source: 'attack_v19', search: this.search() || undefined,
      deprecated: false, page: this.page(), per_page: PER_PAGE,
    })),
  }))

  readonly totalPages = computed(() => Math.ceil((this.listQuery.data()?.total ?? 0) / PER_PAGE) || 1)

  onSearch(v: string) { this.search.set(v); this.page.set(1) }
  setPage(p: number)  { this.page.set(p) }
  onRowClick(g: MitreGroup) { this.selected.update(s => s?.id === g.id ? null : g) }
}
