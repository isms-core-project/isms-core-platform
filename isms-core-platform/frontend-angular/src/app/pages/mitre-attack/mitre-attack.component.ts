import { Component, inject, signal, computed } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'
import { injectQuery } from '@tanstack/angular-query-experimental'

import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatChipsModule } from '@angular/material/chips'
import { MatIconModule } from '@angular/material/icon'
import { MatButtonToggleModule } from '@angular/material/button-toggle'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatButtonModule } from '@angular/material/button'

import { FeedsApiService, MitreTechnique } from '../../api/feeds-api.service'
import { ThemeService } from '../../core/services/theme.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

const INTEL_DARK  = '#FFA726'
const INTEL_LIGHT = '#E65100'
const PER_PAGE = 50

@Component({
  selector: 'app-mitre-attack',
  standalone: true,
  imports: [
    FormsModule,
    PageHeaderComponent,
    MatFormFieldModule, MatInputModule, MatSelectModule, MatChipsModule,
    MatIconModule, MatButtonToggleModule, MatTooltipModule,
    MatProgressSpinnerModule, MatButtonModule,
  ],
  template: `
<div class="ma-page">
  <app-page-header
    title="MITRE ATT&CK"
    subtitle="Enterprise adversary tactics, techniques & sub-techniques"
  />

  <!-- Stats row -->
  @if (statsQuery.data(); as stats) {
    <div class="stats-row">
      <div class="stat-item">
        <span class="stat-val" [style.color]="INTEL_COLOR">{{ stats.total_techniques.toLocaleString() }}</span>
        <span class="stat-lbl">Techniques</span>
      </div>
      <div class="stat-item">
        <span class="stat-val" [style.color]="INTEL_COLOR">{{ stats.total_subtechniques.toLocaleString() }}</span>
        <span class="stat-lbl">Sub-techniques</span>
      </div>
      <div class="stat-item">
        <span class="stat-val" [style.color]="INTEL_COLOR">{{ tacticCount() }}</span>
        <span class="stat-lbl">Tactics</span>
      </div>
      <div class="stat-item">
        <span class="stat-val" [style.color]="INTEL_COLOR">{{ stats.sources.join(', ') }}</span>
        <span class="stat-lbl">Sources</span>
      </div>
    </div>
  }

  <!-- Filters -->
  <div class="filters-row">
    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="filter-search">
      <mat-label>Search</mat-label>
      <mat-icon matPrefix>search</mat-icon>
      <input matInput placeholder="Search by ID or name…"
        [(ngModel)]="search" (ngModelChange)="onSearch($event)" />
    </mat-form-field>

    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="filter-tactic">
      <mat-label>Tactic</mat-label>
      <mat-select [(ngModel)]="tactic" (ngModelChange)="onTactic($event)">
        <mat-option value="">All tactics</mat-option>
        @for (t of tactics(); track t) {
          <mat-option [value]="t">{{ t.replace('-', ' ') }}</mat-option>
        }
      </mat-select>
    </mat-form-field>

    <mat-button-toggle-group [(ngModel)]="showSubs" class="sub-toggle">
      <mat-button-toggle [value]="true">Sub-techniques</mat-button-toggle>
    </mat-button-toggle-group>
  </div>

  <!-- Table + detail panel -->
  <div class="layout-row">
    <div class="table-box">
      @if (techQuery.isLoading()) {
        <div class="loading-center"><mat-spinner diameter="28" /></div>
      }
      @if (techQuery.isError()) {
        <div class="alert alert-error"><mat-icon>error</mat-icon> Failed to load techniques</div>
      }
      @if (!techQuery.isLoading() && techQuery.data()?.total === 0) {
        <div class="alert alert-info">
          <mat-icon>info</mat-icon>
          ATT&amp;CK v19 data not yet available. Check back after the scheduled weekly pull.
        </div>
      }

      @if (techQuery.data(); as d) {
        @if (d.items.length > 0) {
          <table>
            <thead>
              <tr>
                <th class="col-id">ID</th>
                <th>Name</th>
                <th>Tactics</th>
                <th class="col-plat">Platforms</th>
              </tr>
            </thead>
            <tbody>
              @for (t of d.items; track t.id) {
                <tr [class.row-selected]="selected()?.id === t.id"
                  (click)="toggleSelected(t)" class="clickable">
                  <td class="mono" [style.color]="INTEL_COLOR">{{ t.technique_id }}</td>
                  <td>
                    <div [style.padding-left]="t.is_subtechnique ? '16px' : '0'">
                      <span class="tech-name">{{ t.name }}</span>
                      @if (t.is_subtechnique) {
                        <span class="sub-label">sub-technique</span>
                      }
                    </div>
                  </td>
                  <td>
                    <div class="chip-row">
                      @for (tac of t.tactics; track tac) {
                        <span class="tac-chip">{{ tac.replace(/-/g, ' ') }}</span>
                      }
                    </div>
                  </td>
                  <td>
                    <div class="chip-row">
                      @for (p of t.platforms.slice(0, 3); track p) {
                        <span class="plat-chip">{{ p }}</span>
                      }
                      @if (t.platforms.length > 3) {
                        <span class="more-chip" [matTooltip]="t.platforms.slice(3).join(', ')">
                          +{{ t.platforms.length - 3 }}
                        </span>
                      }
                    </div>
                  </td>
                </tr>
              }
            </tbody>
          </table>

          <!-- Pagination -->
          <div class="pagination">
            <span class="dim">{{ d.total.toLocaleString() }} techniques</span>
            <div class="pag-controls">
              <span class="pag-btn" [class.disabled]="page() === 1" (click)="prevPage()">← Prev</span>
              <span class="dim">{{ page() }} / {{ totalPages() }}</span>
              <span class="pag-btn" [class.disabled]="page() === totalPages()" (click)="nextPage()">Next →</span>
            </div>
          </div>
        }
      }
    </div>

    <!-- Detail panel -->
    @if (selected(); as sel) {
      <div class="detail-panel">
        <div class="detail-id" [style.color]="INTEL_COLOR">{{ sel.technique_id }}</div>
        <div class="detail-name">{{ sel.name }}</div>
        <div class="chip-row chip-row--mb">
          @for (t of sel.tactics; track t) {
            <span class="tac-chip">{{ t.replace(/-/g, ' ') }}</span>
          }
        </div>
        <div class="chip-row">
          @for (p of sel.platforms; track p) {
            <span class="plat-chip">{{ p }}</span>
          }
        </div>
        @if (sel.description) {
          <p class="detail-desc">{{ sel.description.slice(0, 600) }}{{ sel.description.length > 600 ? '…' : '' }}</p>
        }
        @if (sel.url) {
          <a [href]="sel.url" target="_blank" rel="noopener noreferrer" class="detail-link" [style.color]="INTEL_COLOR">
            View on attack.mitre.org →
          </a>
        }
      </div>
    }
  </div>
</div>
  `,
  styles: [`
    .ma-page {
      display: flex;
      flex-direction: column;
      gap: 16px;
      height: 100%;
      overflow-y: auto;
      box-sizing: border-box;
    }

    .stats-row { display: flex; gap: 24px; flex-wrap: wrap; }
    .stat-item { display: flex; flex-direction: column; }
    .stat-val  { font-size: 1.2rem; font-weight: 700; line-height: 1; }
    .stat-lbl  { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }

    .filters-row { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }
    .filter-search { flex: 1; min-width: 200px; }
    .filter-tactic { min-width: 180px; }
    .sub-toggle { height: 40px; }

    .layout-row { display: flex; gap: 16px; align-items: flex-start; }

    .table-box {
      flex: 1;
      border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 8px;
      overflow: hidden;
      min-width: 0;
      background: var(--mat-sys-surface-container);
    }

    .loading-center { display: flex; justify-content: center; padding: 48px; }

    .alert {
      display: flex; align-items: center; gap: 8px;
      padding: 10px 14px; font-size: 0.82rem; margin: 8px;
      border-radius: 6px;
    }
    .alert mat-icon { font-size: 18px; }
    .alert-error { background: rgba(192,0,0,0.08); color: var(--mat-sys-error); border: 1px solid rgba(192,0,0,0.2); }
    .alert-info  { background: var(--mat-sys-surface-container); border: 1px solid var(--mat-sys-outline-variant); }

    table { width: 100%; border-collapse: collapse; }
    thead { background: var(--mat-sys-surface-container); position: sticky; top: 0; }
    th { font-size: 0.72rem; font-weight: 600; padding: 6px 10px; text-align: left; }
    td { font-size: 0.75rem; padding: 5px 10px; border-top: 1px solid var(--mat-sys-outline-variant); vertical-align: middle; }
    tr.clickable { cursor: pointer; }
    tr.clickable:hover td { background: var(--mat-sys-surface-container); }
    tr.row-selected td { background: rgba(184,79,0,0.08); }

    .col-id   { width: 90px; }
    .col-plat { width: 160px; }

    .tech-name { font-size: 0.78rem; font-weight: 500; }
    .sub-label { display: block; font-size: 0.65rem; color: var(--mat-sys-on-surface-variant); }

    .chip-row { display: flex; flex-wrap: wrap; gap: 2px; }
    .chip-row--mb { margin-bottom: 8px; }
    .tac-chip {
      display: inline-block; font-size: 0.65rem; padding: 1px 5px; border-radius: 8px;
      background: var(--mat-sys-surface-container-high);
      color: var(--mat-sys-on-surface-variant);
      text-transform: capitalize;
    }
    .plat-chip {
      display: inline-block; font-size: 0.62rem; padding: 1px 5px; border-radius: 8px;
      border: 1px solid var(--mat-sys-outline-variant);
      color: var(--mat-sys-on-surface-variant);
    }
    .more-chip {
      display: inline-block; font-size: 0.62rem; padding: 1px 5px; border-radius: 8px;
      background: var(--mat-sys-surface-container-high);
      color: var(--mat-sys-on-surface-variant); cursor: default;
    }

    .pagination {
      display: flex; justify-content: space-between; align-items: center;
      padding: 6px 10px; border-top: 1px solid var(--mat-sys-outline-variant);
    }
    .pag-controls { display: flex; align-items: center; gap: 8px; }
    .pag-btn { font-size: 0.75rem; cursor: pointer; color: var(--mat-sys-primary); }
    .pag-btn.disabled { color: var(--mat-sys-on-surface-variant); cursor: default; pointer-events: none; }

    .detail-panel {
      width: 320px;
      flex-shrink: 0;
      border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 8px;
      padding: 14px;
      position: sticky;
      top: 16px;
    }
    .detail-id   { font-family: monospace; font-size: 0.85rem; font-weight: 700; margin-bottom: 4px; }
    .detail-name { font-size: 0.85rem; font-weight: 600; margin-bottom: 8px; }
    .detail-desc {
      font-size: 0.75rem; color: var(--mat-sys-on-surface-variant);
      margin-top: 10px; line-height: 1.5; max-height: 280px; overflow-y: auto;
    }
    .detail-link { font-size: 0.75rem; display: block; margin-top: 8px; text-decoration: none; }
    .detail-link:hover { text-decoration: underline; }

    .mono { font-family: monospace; font-weight: 600; }
    .dim  { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
  `],
})
export class MitreAttackComponent {
  private feedsApi = inject(FeedsApiService)
  private readonly theme = inject(ThemeService)

  get INTEL_COLOR() { return this.theme.isDark() ? INTEL_DARK : INTEL_LIGHT }

  search   = ''
  tactic   = ''
  showSubs = true
  private _page = signal(1)

  readonly page = computed(() => this._page())

  readonly statsQuery = injectQuery(() => ({
    queryKey: ['feeds', 'attack', 'stats'],
    queryFn:  () => firstValueFrom(this.feedsApi.getAttackStats()),
  }))

  readonly tactics = computed(() =>
    Object.keys(this.statsQuery.data()?.tactic_counts ?? {}).sort()
  )

  readonly tacticCount = computed(() =>
    Object.keys(this.statsQuery.data()?.tactic_counts ?? {}).length
  )

  readonly techQuery = injectQuery(() => ({
    queryKey: ['feeds', 'attack', 'attack_v19', this.tactic, this.search, this.showSubs, this._page()],
    queryFn:  () => firstValueFrom(this.feedsApi.getAttackTechniques({
      source: 'attack_v19',
      tactic: this.tactic || undefined,
      search: this.search || undefined,
      subtechniques: this.showSubs,
      deprecated: false,
      page: this._page(),
      per_page: PER_PAGE,
    })),
  }))

  readonly totalPages = computed(() => {
    const total = this.techQuery.data()?.total ?? 0
    return Math.max(1, Math.ceil(total / PER_PAGE))
  })

  selected = signal<MitreTechnique | null>(null)

  onSearch(v: string) { this.search = v; this._page.set(1) }
  onTactic(v: string) { this.tactic = v; this._page.set(1) }
  prevPage() { if (this._page() > 1) this._page.update(p => p - 1) }
  nextPage() { if (this._page() < this.totalPages()) this._page.update(p => p + 1) }

  toggleSelected(t: MitreTechnique) {
    this.selected.update(s => s?.id === t.id ? null : t)
  }
}
