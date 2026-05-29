import { Component, inject, signal, computed } from '@angular/core'
import { DecimalPipe } from '@angular/common'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'
import { injectQuery } from '@tanstack/angular-query-experimental'

import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatIconModule } from '@angular/material/icon'
import { MatButtonToggleModule } from '@angular/material/button-toggle'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'

import { FeedsApiService, MitreTechnique } from '../../api/feeds-api.service'
import { ThemeService } from '../../core/services/theme.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

const INTEL_DARK  = '#FFA726'
const INTEL_LIGHT = '#BA7517'
const PER_PAGE = 50

const PLATFORM_COLORS: Record<string, string> = {
  'Windows': '#0078D4', 'Linux': '#E8A020', 'macOS': '#999',
  'Android': '#3DDC84', 'iOS': '#1A73E8', 'Network': '#5C7AD6',
  'Office 365': '#D83B01', 'Azure AD': '#0078D4', 'SaaS': '#6C5CE7',
  'PRE': '#888', 'Containers': '#2496ED', 'Google Workspace': '#4285F4',
  'ESXi': '#607D8B', 'IaaS': '#26A69A', 'Identity Provider': '#7B1FA2',
}

@Component({
  selector: 'app-mitre-attack',
  standalone: true,
  imports: [
    DecimalPipe, FormsModule, PageHeaderComponent,
    MatFormFieldModule, MatInputModule, MatSelectModule,
    MatIconModule, MatButtonToggleModule, MatTooltipModule,
    MatProgressSpinnerModule,
  ],
  template: `
<div class="ma-page">
  <app-page-header
    title="ATT&CK"
    subtitle="MITRE ATT&CK Enterprise — adversary tactics, techniques & sub-techniques"
  />

  @if (statsQuery.data(); as s) {
    <div class="mitre-stats">
      <div><div class="mitre-stat__val" [style.color]="INTEL_COLOR">{{ s.total_techniques | number }}</div><div class="mitre-stat__lbl">Techniques</div></div>
      <div><div class="mitre-stat__val" [style.color]="INTEL_COLOR">{{ s.total_subtechniques | number }}</div><div class="mitre-stat__lbl">Sub-techniques</div></div>
      <div><div class="mitre-stat__val" [style.color]="INTEL_COLOR">{{ tacticCount() }}</div><div class="mitre-stat__lbl">Tactics</div></div>
      <div><div class="mitre-stat__val" [style.color]="INTEL_COLOR">{{ s.deprecated_count | number }}</div><div class="mitre-stat__lbl">Deprecated</div></div>
    </div>
  }

  <div class="mitre-filters">
    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="mitre-search">
      <mat-label>Search techniques…</mat-label>
      <mat-icon matPrefix>search</mat-icon>
      <input matInput [(ngModel)]="search" (ngModelChange)="onSearch($event)" />
    </mat-form-field>
    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="mitre-select">
      <mat-label>Tactic</mat-label>
      <mat-select [(ngModel)]="tactic" (ngModelChange)="onTactic($event)">
        <mat-option value="">All tactics</mat-option>
        @for (t of tactics(); track t) {
          <mat-option [value]="t">{{ t.replace(/-/g, ' ') }}</mat-option>
        }
      </mat-select>
    </mat-form-field>
    <mat-button-toggle-group [ngModel]="showSubs()" (ngModelChange)="onShowSubs($event)" class="subs-toggle">
      <mat-button-toggle [value]="false">Hide subs</mat-button-toggle>
      <mat-button-toggle [value]="true">Show subs</mat-button-toggle>
    </mat-button-toggle-group>
  </div>

  <div class="mitre-layout">
    <div class="mitre-table-box">
      @if (techQuery.isLoading()) {
        <div class="mitre-empty"><mat-spinner diameter="28" /></div>
      }
      @if (techQuery.isError()) {
        <div class="mitre-error">Failed to load techniques.</div>
      }
      @if (!techQuery.isLoading() && techQuery.data()?.total === 0) {
        <div class="mitre-empty">No ATT&CK v19 data yet — check back after the scheduled weekly pull.</div>
      }
      @if (techQuery.data(); as d) {
        @if (d.items.length > 0) {
          <table class="mitre-table">
            <thead><tr>
              <th class="col-id">ID</th>
              <th>Name</th>
              <th class="col-tactics">Tactics</th>
              <th class="col-plat">Platforms</th>
            </tr></thead>
            <tbody>
              @for (t of d.items; track t.id) {
                <tr class="mitre-row" [class.mitre-row--selected]="selected()?.id === t.id" (click)="toggleSelected(t)">
                  <td class="mono" [style.color]="INTEL_COLOR">{{ t.technique_id }}</td>
                  <td>
                    <div [style.padding-left]="t.is_subtechnique ? '14px' : '0'">
                      <span class="tech-name">{{ t.name }}</span>
                      @if (t.is_subtechnique) { <span class="sub-badge">sub</span> }
                    </div>
                  </td>
                  <td class="col-tactics">
                    <div class="chip-row">
                      @for (tac of t.tactics.slice(0, 2); track tac) {
                        <span class="mitre-chip">{{ tac.replace(/-/g, ' ') }}</span>
                      }
                      @if (t.tactics.length > 2) {
                        <span class="mitre-chip" [matTooltip]="t.tactics.slice(2).join(', ')">+{{ t.tactics.length - 2 }}</span>
                      }
                    </div>
                  </td>
                  <td class="col-plat">
                    <div class="chip-row">
                      @for (p of t.platforms.slice(0, 3); track p) {
                        <span class="mitre-chip mitre-chip--outline" [style.color]="platColor(p)" [style.border-color]="platColor(p) + '55'">{{ p }}</span>
                      }
                      @if (t.platforms.length > 3) {
                        <span class="mitre-chip" [matTooltip]="t.platforms.slice(3).join(', ')">+{{ t.platforms.length - 3 }}</span>
                      }
                    </div>
                  </td>
                </tr>
              }
            </tbody>
          </table>
          <div class="mitre-pagination">
            <span>{{ d.total | number }} techniques</span>
            <div class="mitre-pagination__nav">
              <span class="mitre-pagination__btn" [class.disabled]="page() === 1" (click)="prevPage()">← Prev</span>
              <span>{{ page() }} / {{ totalPages() }}</span>
              <span class="mitre-pagination__btn" [class.disabled]="page() === totalPages()" (click)="nextPage()">Next →</span>
            </div>
          </div>
        }
      }
    </div>

    @if (selected(); as sel) {
      <div class="mitre-detail">
        <div class="mitre-detail__id" [style.color]="INTEL_COLOR">{{ sel.technique_id }}</div>
        <div class="mitre-detail__name">{{ sel.name }}</div>
        <div class="mitre-detail__label">Tactics</div>
        <div class="chip-row chip-row--gap">
          @for (t of sel.tactics; track t) {
            <span class="mitre-chip">{{ t.replace(/-/g, ' ') }}</span>
          }
        </div>
        <div class="mitre-detail__label">Platforms</div>
        <div class="chip-row chip-row--gap">
          @for (p of sel.platforms; track p) {
            <span class="mitre-chip mitre-chip--outline" [style.color]="platColor(p)" [style.border-color]="platColor(p) + '55'">{{ p }}</span>
          }
        </div>
        @if (sel.description) {
          <div class="mitre-detail__desc">{{ sel.description.slice(0, 700) }}{{ sel.description.length > 700 ? '…' : '' }}</div>
        }
        @if (sel.url) {
          <a [href]="sel.url" target="_blank" rel="noopener noreferrer" class="mitre-detail__link" [style.color]="INTEL_COLOR">View on attack.mitre.org →</a>
        }
      </div>
    }
  </div>
</div>
  `,
  styles: [`
    .ma-page { display: flex; flex-direction: column; gap: 16px; }
    .subs-toggle { height: 40px; }
    .col-id      { width: 90px; }
    .col-tactics { width: 200px; }
    .col-plat    { width: 200px; }
    .tech-name   { font-size: 0.78rem; font-weight: 500; }
    .sub-badge {
      display: inline-block; margin-left: 6px; font-size: 0.6rem; padding: 0 4px;
      border-radius: 4px; background: rgba(255,167,38,0.15); color: #FFA726; vertical-align: middle;
    }
    .chip-row { display: flex; flex-wrap: wrap; gap: 2px; }
    .chip-row--gap { gap: 4px; margin-bottom: 2px; }
    .mono { font-family: monospace; font-weight: 600; }
  `],
})
export class MitreAttackComponent {
  private feedsApi = inject(FeedsApiService)
  private readonly theme = inject(ThemeService)

  get INTEL_COLOR() { return this.theme.isDark() ? INTEL_DARK : INTEL_LIGHT }

  search   = ''
  tactic   = ''
  showSubs = signal(true)
  private _page = signal(1)
  readonly page = computed(() => this._page())
  selected = signal<MitreTechnique | null>(null)

  readonly statsQuery = injectQuery(() => ({
    queryKey: ['feeds', 'attack', 'stats'],
    queryFn:  () => firstValueFrom(this.feedsApi.getAttackStats()),
  }))

  readonly tactics = computed(() => Object.keys(this.statsQuery.data()?.tactic_counts ?? {}).sort())
  readonly tacticCount = computed(() => Object.keys(this.statsQuery.data()?.tactic_counts ?? {}).length)

  readonly techQuery = injectQuery(() => ({
    queryKey: ['feeds', 'attack', 'attack_v19', this.tactic, this.search, this.showSubs(), this._page()],
    queryFn:  () => firstValueFrom(this.feedsApi.getAttackTechniques({
      source: 'attack_v19', tactic: this.tactic || undefined,
      search: this.search || undefined, subtechniques: this.showSubs(),
      deprecated: false, page: this._page(), per_page: PER_PAGE,
    })),
  }))

  readonly totalPages = computed(() => Math.max(1, Math.ceil((this.techQuery.data()?.total ?? 0) / PER_PAGE)))

  onSearch(v: string)   { this.search = v; this._page.set(1) }
  onTactic(v: string)   { this.tactic = v; this._page.set(1) }
  onShowSubs(v: boolean) { this.showSubs.set(v); this._page.set(1) }
  prevPage() { if (this._page() > 1) this._page.update(p => p - 1) }
  nextPage() { if (this._page() < this.totalPages()) this._page.update(p => p + 1) }
  toggleSelected(t: MitreTechnique) { this.selected.update(s => s?.id === t.id ? null : t) }
  platColor(p: string): string { return PLATFORM_COLORS[p] ?? (this.theme.isDark() ? '#888' : '#5F5E5A') }
}
