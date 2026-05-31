import { Component, inject, signal, computed } from '@angular/core'
import { CommonModule } from '@angular/common'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'
import { injectQuery } from '@tanstack/angular-query-experimental'

import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatIconModule } from '@angular/material/icon'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'

import { FeedsApiService, MitreSoftware } from '../../api/feeds-api.service'
import { ThemeService } from '../../core/services/theme.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

const INTEL_DARK  = '#e06030'
const INTEL_LIGHT = '#c64227'
const MALWARE_COLOR = '#9C27B0'
const TOOL_COLOR    = '#0288D1'
const PER_PAGE = 50

const PLATFORM_DARK: Record<string, { bg: string; color: string }> = {
  'Windows':    { bg: 'rgba(0,120,212,0.20)',  color: '#60b0ff' },
  'Linux':      { bg: 'rgba(232,160,32,0.18)', color: '#FFA726' },
  'macOS':      { bg: 'rgba(160,160,160,0.14)',color: '#cccccc' },
  'Android':    { bg: 'rgba(61,220,132,0.15)', color: '#3DDC84' },
  'iOS':        { bg: 'rgba(20,126,251,0.18)', color: '#60b0ff' },
  'Network':    { bg: 'rgba(92,122,214,0.18)', color: '#8fa8f8' },
  'Office 365': { bg: 'rgba(216,59,1,0.18)',   color: '#ff8c66' },
  'SaaS':       { bg: 'rgba(108,92,231,0.18)', color: '#b39ddb' },
  'ESXi':       { bg: 'rgba(96,125,139,0.20)',  color: '#90A4AE' },
  'IaaS':       { bg: 'rgba(38,166,154,0.18)',  color: '#4DB6AC' },
}
const PLATFORM_LIGHT: Record<string, { bg: string; color: string }> = {
  'Windows':    { bg: 'rgba(0,120,212,0.13)',  color: '#0055A5' },
  'Linux':      { bg: 'rgba(186,117,23,0.15)', color: '#7A4500' },
  'macOS':      { bg: 'rgba(44,44,42,0.10)',   color: '#5F5E5A' },
  'Android':    { bg: 'rgba(29,158,117,0.13)', color: '#0F6E56' },
  'iOS':        { bg: 'rgba(24,95,165,0.13)',  color: '#185FA5' },
  'Network':    { bg: 'rgba(92,122,214,0.12)', color: '#3D5BB0' },
  'Office 365': { bg: 'rgba(216,59,1,0.12)',   color: '#A02800' },
  'SaaS':       { bg: 'rgba(108,92,231,0.12)', color: '#4527A0' },
  'ESXi':       { bg: 'rgba(96,125,139,0.14)',  color: '#455A64' },
  'IaaS':       { bg: 'rgba(38,166,154,0.13)',  color: '#00695C' },
}

@Component({
  selector: 'app-mitre-software',
  standalone: true,
  imports: [
    CommonModule, FormsModule, PageHeaderComponent,
    MatFormFieldModule, MatInputModule, MatSelectModule,
    MatIconModule, MatTooltipModule, MatProgressSpinnerModule,
  ],
  template: `
<div class="sw-page">
  <app-page-header
    title="Software"
    subtitle="MITRE ATT&CK — malware and tools used by adversaries"
  />

  @if (statsQuery.data(); as s) {
    <div class="mitre-stats">
      <div><div class="mitre-stat__val" [style.color]="INTEL_COLOR">{{ s.total_software | number }}</div><div class="mitre-stat__lbl">Total</div></div>
      <div><div class="mitre-stat__val" [style.color]="MALWARE_COLOR">{{ s.malware_count | number }}</div><div class="mitre-stat__lbl">Malware</div></div>
      <div><div class="mitre-stat__val" [style.color]="TOOL_COLOR">{{ s.tool_count | number }}</div><div class="mitre-stat__lbl">Tools</div></div>
      <div><div class="mitre-stat__val" [style.color]="INTEL_COLOR">{{ s.deprecated_count | number }}</div><div class="mitre-stat__lbl">Deprecated</div></div>
    </div>
  }

  <div class="mitre-filters">
    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="mitre-search">
      <mat-label>Search software…</mat-label>
      <mat-icon matPrefix>search</mat-icon>
      <input matInput [ngModel]="search()" (ngModelChange)="onSearch($event)" />
    </mat-form-field>
    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="mitre-select">
      <mat-label>Type</mat-label>
      <mat-select [ngModel]="softwareType()" (ngModelChange)="onTypeChange($event)">
        <mat-option value="">All types</mat-option>
        <mat-option value="malware">Malware</mat-option>
        <mat-option value="tool">Tool</mat-option>
      </mat-select>
    </mat-form-field>
  </div>

  <div class="mitre-layout">
    <div class="mitre-table-box">
      @if (listQuery.isLoading()) {
        <div class="mitre-empty"><mat-spinner diameter="28" /></div>
      }
      @if (listQuery.isError()) {
        <div class="mitre-error">Failed to load software.</div>
      }
      @if (!listQuery.isLoading() && listQuery.data()?.total === 0) {
        <div class="mitre-empty">No ATT&CK v19 data yet — check back after the scheduled weekly pull.</div>
      }
      @if (!listQuery.isLoading() && (listQuery.data()?.items?.length ?? 0) > 0) {
        <table class="mitre-table">
          <thead><tr>
            <th class="col-id">ID</th>
            <th class="col-type">Type</th>
            <th>Name</th>
            <th class="col-plat">Platforms</th>
          </tr></thead>
          <tbody>
            @for (s of listQuery.data()!.items; track s.id) {
              <tr class="mitre-row" [class.mitre-row--selected]="selected()?.id === s.id" (click)="onRowClick(s)">
                <td class="mono" [style.color]="INTEL_COLOR">{{ s.software_id }}</td>
                <td>
                  <span class="type-chip"
                    [style.background]="s.software_type === 'malware' ? '#9C27B022' : '#0288D122'"
                    [style.color]="s.software_type === 'malware' ? MALWARE_COLOR : TOOL_COLOR">
                    {{ s.software_type }}
                  </span>
                </td>
                <td class="cell-name">{{ s.name }}</td>
                <td class="col-plat">
                  <div class="plat-row">
                    @for (p of s.platforms.slice(0, 2); track p) {
                      <span class="plat-chip"
                        [style.background]="platStyle(p).bg"
                        [style.color]="platStyle(p).color">{{ p }}</span>
                    }
                    @if (s.platforms.length > 2) {
                      <span class="plat-chip" [matTooltip]="s.platforms.slice(2).join(', ')">+{{ s.platforms.length - 2 }}</span>
                    }
                  </div>
                </td>
              </tr>
            }
          </tbody>
        </table>
        <div class="mitre-pagination">
          <span>{{ listQuery.data()!.total | number }} items</span>
          <div class="mitre-pagination__nav">
            <span class="mitre-pagination__btn" [class.disabled]="page() <= 1" (click)="page() > 1 && setPage(page() - 1)">← Prev</span>
            <span>{{ page() }} / {{ totalPages() }}</span>
            <span class="mitre-pagination__btn" [class.disabled]="page() >= totalPages()" (click)="page() < totalPages() && setPage(page() + 1)">Next →</span>
          </div>
        </div>
      }
    </div>

    @if (selected(); as s) {
      <div class="mitre-detail">
        <div class="detail-top">
          <div class="mitre-detail__id" [style.color]="INTEL_COLOR">{{ s.software_id }}</div>
          <span class="type-chip"
            [style.background]="s.software_type === 'malware' ? '#9C27B022' : '#0288D122'"
            [style.color]="s.software_type === 'malware' ? MALWARE_COLOR : TOOL_COLOR">
            {{ s.software_type }}
          </span>
        </div>
        <div class="mitre-detail__name">{{ s.name }}</div>
        @if (s.aliases.length > 0) {
          <div class="mitre-detail__label">Also known as</div>
          <div class="plat-row plat-row--wrap">
            @for (a of s.aliases; track a) {
              <span class="plat-chip">{{ a }}</span>
            }
          </div>
        }
        @if (s.platforms.length > 0) {
          <div class="mitre-detail__label">Platforms</div>
          <div class="plat-row plat-row--wrap">
            @for (p of s.platforms; track p) {
              <span class="plat-chip" [style.background]="platStyle(p).bg" [style.color]="platStyle(p).color">{{ p }}</span>
            }
          </div>
        }
        @if (s.description) {
          <div class="mitre-detail__desc">{{ s.description.slice(0, 700) }}{{ s.description.length > 700 ? '…' : '' }}</div>
        }
        @if (s.url) {
          <a [href]="s.url" target="_blank" rel="noopener noreferrer" class="mitre-detail__link" [style.color]="INTEL_COLOR">View on attack.mitre.org →</a>
        }
      </div>
    }
  </div>
</div>
  `,
  styles: [`
    .sw-page { display: flex; flex-direction: column; gap: 16px; }
    .col-id   { width: 80px; }
    .col-type { width: 80px; }
    .col-plat { width: 180px; }
    .cell-name { font-size: 0.78rem; font-weight: 500; max-width: 220px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .mono { font-family: monospace; font-weight: 600; }
    .type-chip { display: inline-flex; align-items: center; font-size: 0.65rem; height: 18px; padding: 0 7px; border-radius: 9px; font-weight: 600; }
    .plat-row { display: flex; flex-wrap: nowrap; gap: 3px; align-items: center; overflow: hidden; }
    .plat-row--wrap { flex-wrap: wrap; gap: 4px; margin-top: 4px; }
    .plat-chip {
      display: inline-flex; align-items: center; font-size: 0.62rem; height: 16px;
      padding: 0 6px; border-radius: 8px; white-space: nowrap;
      overflow: hidden; text-overflow: ellipsis; max-width: 110px; flex-shrink: 0;
      background: var(--mat-sys-surface-container-high);
      color: var(--mat-sys-on-surface-variant);
    }
    .detail-top { display: flex; align-items: center; gap: 8px; margin-bottom: 4px; }
  `],
})
export class MitreSoftwareComponent {
  private feedsApi = inject(FeedsApiService)
  private readonly theme = inject(ThemeService)

  get INTEL_COLOR() { return this.theme.isDark() ? INTEL_DARK : INTEL_LIGHT }
  readonly MALWARE_COLOR = MALWARE_COLOR
  readonly TOOL_COLOR    = TOOL_COLOR

  search       = signal('')
  page         = signal(1)
  softwareType = signal<'malware' | 'tool' | ''>('')
  selected     = signal<MitreSoftware | null>(null)

  readonly statsQuery = injectQuery(() => ({
    queryKey: ['feeds', 'software', 'stats'],
    queryFn: () => firstValueFrom(this.feedsApi.getMitreSoftwareStats()),
  }))

  readonly listQuery = injectQuery(() => ({
    queryKey: ['feeds', 'software', 'attack_v19', this.softwareType(), this.search(), this.page()],
    queryFn: () => firstValueFrom(this.feedsApi.getMitreSoftware({
      source: 'attack_v19', software_type: this.softwareType() || undefined,
      search: this.search() || undefined, deprecated: false,
      page: this.page(), per_page: PER_PAGE,
    })),
  }))

  readonly totalPages = computed(() => Math.ceil((this.listQuery.data()?.total ?? 0) / PER_PAGE) || 1)

  onSearch(v: string)              { this.search.set(v); this.page.set(1) }
  onTypeChange(v: 'malware' | 'tool' | '') { this.softwareType.set(v); this.page.set(1) }
  setPage(p: number)               { this.page.set(p) }
  onRowClick(s: MitreSoftware)     { this.selected.update(cur => cur?.id === s.id ? null : s) }

  platStyle(p: string): { bg: string; color: string } {
    const m = this.theme.isDark() ? PLATFORM_DARK : PLATFORM_LIGHT
    return m[p] ?? (this.theme.isDark()
      ? { bg: 'rgba(255,255,255,0.08)', color: '#aaa' }
      : { bg: 'rgba(44,44,42,0.08)',    color: '#5F5E5A' })
  }
}
