import { Component, inject, signal, computed } from '@angular/core'
import { DecimalPipe } from '@angular/common'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'
import { injectQuery } from '@tanstack/angular-query-experimental'

import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatIconModule } from '@angular/material/icon'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'

import { FeedsApiService, MitreTechnique } from '../../api/feeds-api.service'
import { ThemeService } from '../../core/services/theme.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

const INTEL_DARK  = '#e06030'
const INTEL_LIGHT = '#c64227'
const PER_PAGE = 50

@Component({
  selector: 'app-mitre-atlas',
  standalone: true,
  imports: [
    DecimalPipe, FormsModule, PageHeaderComponent,
    MatFormFieldModule, MatInputModule, MatSelectModule,
    MatIconModule, MatTooltipModule, MatProgressSpinnerModule,
  ],
  template: `
<div class="atlas-page">
  <app-page-header
    title="ATLAS"
    subtitle="MITRE ATLAS — adversarial ML attacks targeting AI/ML systems"
  />

  @if (statsQuery.data(); as s) {
    <div class="mitre-stats">
      <div><div class="mitre-stat__val" [style.color]="INTEL_COLOR">{{ s.total_techniques | number }}</div><div class="mitre-stat__lbl">Techniques</div></div>
      <div><div class="mitre-stat__val" [style.color]="INTEL_COLOR">{{ tacticCount() }}</div><div class="mitre-stat__lbl">Tactics</div></div>
    </div>
  }

  <div class="context-banner">
    <mat-icon>info</mat-icon>
    Covers model evasion, data poisoning, inversion and theft attacks.
    Relevant for AI Act (A.8.28), DORA AI risk, and ISO 42001.
  </div>

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
          <mat-option [value]="t">{{ t }}</mat-option>
        }
      </mat-select>
    </mat-form-field>
  </div>

  <div class="mitre-layout">
    <div class="mitre-table-box">
      @if (techQuery.isLoading()) {
        <div class="mitre-empty"><mat-spinner diameter="28" /></div>
      }
      @if (techQuery.isError()) {
        <div class="mitre-error">Failed to load ATLAS techniques.</div>
      }
      @if (!techQuery.isLoading() && techQuery.data()?.total === 0) {
        <div class="mitre-empty">No ATLAS data yet — check back after the scheduled weekly pull.</div>
      }
      @if (techQuery.data(); as d) {
        @if (d.items.length > 0) {
          <table class="mitre-table">
            <thead><tr>
              <th class="col-id">ID</th>
              <th>Name</th>
              <th class="col-tactics">Tactics</th>
              <th class="col-type">Type</th>
            </tr></thead>
            <tbody>
              @for (t of d.items; track t.id) {
                <tr class="mitre-row" [class.mitre-row--selected]="selected()?.id === t.id" (click)="toggleSelected(t)">
                  <td class="mono" [style.color]="INTEL_COLOR">{{ t.technique_id }}</td>
                  <td>
                    <div [style.padding-left]="t.is_subtechnique ? '14px' : '0'">
                      <span class="tech-name">{{ t.name }}</span>
                    </div>
                  </td>
                  <td class="col-tactics">
                    <div class="chip-row">
                      @for (tac of t.tactics.slice(0, 2); track tac) {
                        <span class="mitre-chip">{{ tac }}</span>
                      }
                    </div>
                  </td>
                  <td>
                    @if (t.is_subtechnique) {
                      <span class="mitre-chip">Sub</span>
                    } @else {
                      <span class="mitre-chip mitre-chip--outline">Tech</span>
                    }
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
        @if (sel.is_subtechnique) {
          <span class="mitre-chip" style="margin-bottom:8px">Sub-technique</span>
        }
        <div class="mitre-detail__label">Tactics</div>
        <div class="chip-row chip-row--gap">
          @for (t of sel.tactics; track t) {
            <span class="mitre-chip">{{ t }}</span>
          }
        </div>
        @if (sel.description) {
          <div class="mitre-detail__desc">{{ sel.description.slice(0, 700) }}{{ sel.description.length > 700 ? '…' : '' }}</div>
        }
        @if (sel.url) {
          <a [href]="sel.url" target="_blank" rel="noopener noreferrer" class="mitre-detail__link" [style.color]="INTEL_COLOR">View on atlas.mitre.org →</a>
        }
      </div>
    }
  </div>
</div>
  `,
  styles: [`
    .atlas-page { display: flex; flex-direction: column; gap: 16px; }
    .context-banner {
      display: flex; align-items: flex-start; gap: 8px;
      padding: 10px 14px; border-radius: 6px; font-size: 0.8rem;
      border: 1px solid var(--mat-sys-outline-variant);
      background: var(--mat-sys-surface-container);
      color: var(--mat-sys-on-surface);
    }
    .context-banner mat-icon { font-size: 18px; flex-shrink: 0; margin-top: 1px; color: var(--mat-sys-primary); }
    .col-id      { width: 110px; }
    .col-tactics { width: 200px; }
    .col-type    { width: 70px; }
    .tech-name   { font-size: 0.78rem; font-weight: 500; }
    .chip-row { display: flex; flex-wrap: wrap; gap: 2px; }
    .chip-row--gap { gap: 4px; margin-bottom: 2px; }
    .mono { font-family: monospace; font-weight: 600; }
  `],
})
export class MitreAtlasComponent {
  private feedsApi = inject(FeedsApiService)
  private readonly theme = inject(ThemeService)

  get INTEL_COLOR() { return this.theme.isDark() ? INTEL_DARK : INTEL_LIGHT }

  search = ''
  tactic = ''
  private _page = signal(1)
  readonly page = computed(() => this._page())
  selected = signal<MitreTechnique | null>(null)

  readonly statsQuery = injectQuery(() => ({
    queryKey: ['feeds', 'atlas', 'stats'],
    queryFn:  () => firstValueFrom(this.feedsApi.getAtlasStats()),
  }))

  readonly tactics = computed(() => Object.keys(this.statsQuery.data()?.tactic_counts ?? {}).sort())
  readonly tacticCount = computed(() => Object.keys(this.statsQuery.data()?.tactic_counts ?? {}).length)

  readonly techQuery = injectQuery(() => ({
    queryKey: ['feeds', 'atlas', this.tactic, this.search, this._page()],
    queryFn:  () => firstValueFrom(this.feedsApi.getAtlasTechniques({
      tactic: this.tactic || undefined,
      search: this.search || undefined,
      page: this._page(), per_page: PER_PAGE,
    })),
  }))

  readonly totalPages = computed(() => Math.max(1, Math.ceil((this.techQuery.data()?.total ?? 0) / PER_PAGE)))

  onSearch(v: string) { this.search = v; this._page.set(1) }
  onTactic(v: string) { this.tactic = v; this._page.set(1) }
  prevPage() { if (this._page() > 1) this._page.update(p => p - 1) }
  nextPage() { if (this._page() < this.totalPages()) this._page.update(p => p + 1) }
  toggleSelected(t: MitreTechnique) { this.selected.update(s => s?.id === t.id ? null : t) }
}
