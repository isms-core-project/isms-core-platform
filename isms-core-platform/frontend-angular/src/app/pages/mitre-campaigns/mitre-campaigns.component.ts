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

import { FeedsApiService, MitreCampaign } from '../../api/feeds-api.service'
import { ThemeService } from '../../core/services/theme.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

const INTEL_DARK  = '#FFA726'
const INTEL_LIGHT = '#BA7517'
const PER_PAGE = 50

@Component({
  selector: 'app-mitre-campaigns',
  standalone: true,
  imports: [
    DecimalPipe, FormsModule, PageHeaderComponent,
    MatFormFieldModule, MatInputModule,
    MatIconModule, MatTooltipModule, MatProgressSpinnerModule,
  ],
  template: `
<div class="cmp-page">
  <app-page-header
    title="Campaigns"
    subtitle="MITRE ATT&CK — time-bound targeted intrusion activity clusters"
  />

  @if (listQuery.data(); as data) {
    <div class="mitre-stats">
      <div><div class="mitre-stat__val" [style.color]="INTEL_COLOR">{{ data.total | number }}</div><div class="mitre-stat__lbl">Campaigns</div></div>
    </div>
  }

  <div class="mitre-filters">
    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="mitre-search">
      <mat-label>Search campaigns…</mat-label>
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
        <div class="mitre-error">Failed to load campaigns.</div>
      }
      @if (!listQuery.isLoading() && listQuery.data()?.total === 0) {
        <div class="mitre-empty">No ATT&CK v19 data yet — check back after the scheduled weekly pull.</div>
      }
      @if (!listQuery.isLoading() && (listQuery.data()?.items?.length ?? 0) > 0) {
        <table class="mitre-table">
          <thead><tr>
            <th class="col-id">ID</th>
            <th class="col-name">Name</th>
            <th class="col-date">First Seen</th>
            <th class="col-date">Last Seen</th>
            <th>Aliases</th>
          </tr></thead>
          <tbody>
            @for (c of listQuery.data()!.items; track c.id) {
              <tr class="mitre-row" [class.mitre-row--selected]="selected()?.id === c.id" (click)="onRowClick(c)">
                <td class="mono" [style.color]="INTEL_COLOR">{{ c.campaign_id }}</td>
                <td class="cell-name">{{ c.name }}</td>
                <td class="cell-date mono">{{ c.first_seen ?? '—' }}</td>
                <td class="cell-date mono">{{ c.last_seen ?? '—' }}</td>
                <td>
                  <div class="alias-row">
                    @for (a of c.aliases.slice(0, 2); track a) {
                      <span class="alias-chip" [matTooltip]="a">{{ a }}</span>
                    }
                    @if (c.aliases.length > 2) {
                      <span class="alias-chip" [matTooltip]="c.aliases.slice(2).join(', ')">+{{ c.aliases.length - 2 }}</span>
                    }
                  </div>
                </td>
              </tr>
            }
          </tbody>
        </table>
        <div class="mitre-pagination">
          <span>{{ listQuery.data()!.total | number }} campaigns</span>
          <div class="mitre-pagination__nav">
            <span class="mitre-pagination__btn" [class.disabled]="page() <= 1" (click)="page() > 1 && setPage(page() - 1)">← Prev</span>
            <span>{{ page() }} / {{ totalPages() }}</span>
            <span class="mitre-pagination__btn" [class.disabled]="page() >= totalPages()" (click)="page() < totalPages() && setPage(page() + 1)">Next →</span>
          </div>
        </div>
      }
    </div>

    @if (selected(); as c) {
      <div class="mitre-detail">
        <div class="mitre-detail__id" [style.color]="INTEL_COLOR">{{ c.campaign_id }}</div>
        <div class="mitre-detail__name">{{ c.name }}</div>
        @if (c.first_seen || c.last_seen) {
          <div class="dates-row">
            @if (c.first_seen) {
              <div><div class="mitre-detail__label">First seen</div><div class="date-val mono">{{ c.first_seen }}</div></div>
            }
            @if (c.last_seen) {
              <div><div class="mitre-detail__label">Last seen</div><div class="date-val mono">{{ c.last_seen }}</div></div>
            }
          </div>
        }
        @if (c.aliases.length > 0) {
          <div class="mitre-detail__label">Also known as</div>
          <div class="alias-row alias-row--wrap">
            @for (a of c.aliases; track a) {
              <span class="alias-chip">{{ a }}</span>
            }
          </div>
        }
        @if (c.description) {
          <div class="mitre-detail__desc">{{ c.description.slice(0, 700) }}{{ c.description.length > 700 ? '…' : '' }}</div>
        }
        @if (c.url) {
          <a [href]="c.url" target="_blank" rel="noopener noreferrer" class="mitre-detail__link" [style.color]="INTEL_COLOR">View on attack.mitre.org →</a>
        }
      </div>
    }
  </div>
</div>
  `,
  styles: [`
    .cmp-page { display: flex; flex-direction: column; gap: 16px; }
    .col-id   { width: 80px; }
    .col-name { width: 180px; }
    .col-date { width: 100px; }
    .cell-name { font-size: 0.78rem; font-weight: 500; max-width: 200px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .cell-date { font-size: 0.72rem; }
    .mono { font-family: monospace; font-weight: 600; }
    .alias-row { display: flex; gap: 3px; align-items: center; flex-wrap: nowrap; overflow: hidden; }
    .alias-row--wrap { flex-wrap: wrap; gap: 4px; margin-top: 4px; }
    .alias-chip {
      display: inline-flex; align-items: center; font-size: 0.62rem; height: 16px;
      padding: 0 6px; border-radius: 8px; white-space: nowrap;
      max-width: 100px; overflow: hidden; text-overflow: ellipsis; flex-shrink: 0;
      background: var(--mat-sys-surface-container-high);
      color: var(--mat-sys-on-surface-variant);
    }
    :host-context(html[data-theme='light']) .alias-chip { background: #C4C2B8; color: #2C2C2A; }
    .dates-row { display: flex; gap: 16px; margin-bottom: 8px; }
    .date-val { font-size: 0.72rem; margin-top: 2px; }
  `],
})
export class MitreCampaignsComponent {
  private feedsApi = inject(FeedsApiService)
  private readonly theme = inject(ThemeService)

  get INTEL_COLOR() { return this.theme.isDark() ? INTEL_DARK : INTEL_LIGHT }

  search   = signal('')
  page     = signal(1)
  selected = signal<MitreCampaign | null>(null)

  readonly listQuery = injectQuery(() => ({
    queryKey: ['feeds', 'campaigns', 'attack_v19', this.search(), this.page()],
    queryFn: () => firstValueFrom(this.feedsApi.getMitreCampaigns({
      source: 'attack_v19', search: this.search() || undefined,
      deprecated: false, page: this.page(), per_page: PER_PAGE,
    })),
  }))

  readonly totalPages = computed(() => Math.ceil((this.listQuery.data()?.total ?? 0) / PER_PAGE) || 1)

  onSearch(v: string) { this.search.set(v); this.page.set(1) }
  setPage(p: number)  { this.page.set(p) }
  onRowClick(c: MitreCampaign) { this.selected.update(s => s?.id === c.id ? null : c) }
}
