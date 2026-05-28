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
import { MatButtonToggleModule } from '@angular/material/button-toggle'

import { FeedsApiService, MitreSoftware } from '../../api/feeds-api.service'

const PER_PAGE = 50
const INTEL_COLOR = '#FFA726'
const MALWARE_COLOR = '#9C27B0'
const TOOL_COLOR = '#0288D1'

@Component({
  selector: 'app-mitre-software',
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
    MatButtonToggleModule,
  ],
  template: `
<div class="sw-page">

  <!-- Header -->
  <div class="sw-header">
    <h2 class="sw-header__title">MITRE ATT&amp;CK Software</h2>
    <p class="sw-header__sub">
      Malware and tools used by adversaries — tracked by MITRE ATT&amp;CK
    </p>
  </div>

  <!-- Stats row -->
  @if (statsQuery.data(); as stats) {
    <div class="sw-stats-row">
      @for (s of [
        {label:'Total', value: stats.total_software},
        {label:'Malware', value: stats.malware_count},
        {label:'Tools', value: stats.tool_count},
        {label:'Deprecated', value: stats.deprecated_count}
      ]; track s.label) {
        <div>
          <div class="sw-stat__val" [style.color]="INTEL_COLOR">{{s.value | number}}</div>
          <div class="sw-stat__lbl">{{s.label}}</div>
        </div>
      }
    </div>
  }

  <!-- Filters -->
  <div class="sw-filters">
    <mat-button-toggle-group value="attack_v19" class="sw-toggle-group">
      <mat-button-toggle value="attack_v19" class="sw-toggle-btn">v19</mat-button-toggle>
    </mat-button-toggle-group>

    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="sw-search-field">
      <mat-label>Search</mat-label>
      <mat-icon matPrefix class="icon-md">search</mat-icon>
      <input matInput [ngModel]="search()" (ngModelChange)="onSearch($event)" placeholder="Search by ID or name…" />
    </mat-form-field>

    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="sw-type-field">
      <mat-label>Type</mat-label>
      <mat-select [ngModel]="softwareType()" (ngModelChange)="onTypeChange($event)">
        <mat-option value="">All types</mat-option>
        <mat-option value="malware">Malware</mat-option>
        <mat-option value="tool">Tool</mat-option>
      </mat-select>
    </mat-form-field>
  </div>

  <!-- Table + detail panel -->
  <div class="sw-layout">

    <!-- Table panel -->
    <div class="sw-table-panel">

      @if (listQuery.isLoading()) {
        <div class="sw-spinner-wrap">
          <mat-spinner [diameter]="28" />
        </div>
      }

      @if (listQuery.isError()) {
        <div class="sw-error">Failed to load software.</div>
      }

      @if (!listQuery.isLoading() && listQuery.data()?.total === 0) {
        <div class="sw-empty">
          ATT&amp;CK v19 data not yet available. Check back after the scheduled weekly pull.
        </div>
      }

      @if (!listQuery.isLoading() && (listQuery.data()?.items?.length ?? 0) > 0) {
        <table mat-table [dataSource]="listQuery.data()!.items" class="sw-table">

          <ng-container matColumnDef="software_id">
            <th mat-header-cell *matHeaderCellDef class="sw-th">ID</th>
            <td mat-cell *matCellDef="let s" class="sw-cell-id"
              [style.color]="INTEL_COLOR">{{s.software_id}}</td>
          </ng-container>

          <ng-container matColumnDef="type">
            <th mat-header-cell *matHeaderCellDef class="sw-th">Type</th>
            <td mat-cell *matCellDef="let s">
              <mat-chip class="sw-type-chip"
                [style.background]="s.software_type === 'malware' ? '#9C27B022' : '#0288D122'"
                [style.color]="s.software_type === 'malware' ? MALWARE_COLOR : TOOL_COLOR">
                {{s.software_type}}
              </mat-chip>
            </td>
          </ng-container>

          <ng-container matColumnDef="name">
            <th mat-header-cell *matHeaderCellDef class="sw-th">Name</th>
            <td mat-cell *matCellDef="let s" class="sw-cell-name">
              {{s.name}}</td>
          </ng-container>

          <ng-container matColumnDef="platforms">
            <th mat-header-cell *matHeaderCellDef class="sw-th">Platforms</th>
            <td mat-cell *matCellDef="let s" class="sw-cell-platforms">
              @if (s.platforms.length > 0) {
                @for (p of s.platforms.slice(0, 2); track p) {
                  <mat-chip class="sw-mini-chip">{{p}}</mat-chip>
                }
                @if (s.platforms.length > 2) {
                  <mat-chip [matTooltip]="s.platforms.slice(2).join(', ')"
                    class="sw-mini-chip">+{{s.platforms.length - 2}}</mat-chip>
                }
              } @else {
                <span class="sw-empty-dash">—</span>
              }
            </td>
          </ng-container>

          <tr mat-header-row *matHeaderRowDef="displayedColumns" class="sw-header-row"></tr>
          <tr mat-row *matRowDef="let s; columns: displayedColumns"
            class="sw-data-row"
            [style.background]="selected()?.id === s.id ? 'rgba(184,79,0,0.08)' : ''"
            (click)="onRowClick(s)"></tr>
        </table>

        <!-- Pagination -->
        <div class="sw-pagination">
          <span class="sw-pagination__count">{{listQuery.data()!.total | number}} items</span>
          <div class="sw-pagination__nav">
            <span class="sw-pagination__btn" [class.disabled]="page() <= 1"
              (click)="page() > 1 && setPage(page() - 1)">← Prev</span>
            <span class="sw-pagination__info">{{page()}} / {{totalPages()}}</span>
            <span class="sw-pagination__btn" [class.disabled]="page() >= totalPages()"
              (click)="page() < totalPages() && setPage(page() + 1)">Next →</span>
          </div>
        </div>
      }
    </div>

    <!-- Detail panel -->
    @if (selected(); as s) {
      <div class="sw-detail-panel">
        <div class="sw-detail-panel__top">
          <div class="sw-detail-panel__id" [style.color]="INTEL_COLOR">{{s.software_id}}</div>
          <mat-chip class="sw-type-chip"
            [style.background]="s.software_type === 'malware' ? '#9C27B022' : '#0288D122'"
            [style.color]="s.software_type === 'malware' ? MALWARE_COLOR : TOOL_COLOR">
            {{s.software_type}}
          </mat-chip>
        </div>
        <div class="sw-detail-panel__name">{{s.name}}</div>

        @if (s.aliases.length > 0) {
          <div class="sw-detail-section">
            <div class="sw-detail-section__label">Also known as:</div>
            @for (a of s.aliases; track a) {
              <mat-chip class="sw-mini-chip">{{a}}</mat-chip>
            }
          </div>
        }

        @if (s.platforms.length > 0) {
          <div class="sw-detail-section">
            <div class="sw-detail-section__label">Platforms:</div>
            @for (p of s.platforms; track p) {
              <mat-chip class="sw-mini-chip">{{p}}</mat-chip>
            }
          </div>
        }

        @if (s.description) {
          <div class="sw-detail-panel__desc">
            {{s.description.slice(0, 600)}}{{s.description.length > 600 ? '…' : ''}}
          </div>
        }

        @if (s.url) {
          <div class="sw-detail-panel__link-wrap">
            <a [href]="s.url" target="_blank" rel="noopener noreferrer"
              class="sw-detail-panel__link" [style.color]="INTEL_COLOR">
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

    .sw-page { padding: 24px; }

    .sw-header { margin-bottom: 16px; }
    .sw-header__title { margin: 0; font-size: 1.3rem; font-weight: 700; }
    .sw-header__sub { margin: 4px 0 0; color: #888; font-size: 0.85rem; }

    .sw-stats-row { display: flex; gap: 24px; margin-bottom: 16px; flex-wrap: wrap; }
    .sw-stat__val { font-size: 1.25rem; font-weight: 700; line-height: 1; }
    .sw-stat__lbl { font-size: 0.72rem; color: #888; }

    .sw-filters { display: flex; gap: 12px; margin-bottom: 16px; align-items: center; flex-wrap: wrap; }
    .sw-toggle-group { height: 32px; }
    .sw-toggle-btn { font-size: 0.72rem; padding: 0 12px; }
    .sw-search-field { width: 240px; }
    .sw-type-field { min-width: 140px; }

    .sw-layout { display: flex; gap: 16px; }

    .sw-table-panel { flex: 1; min-width: 0; border: 1px solid var(--mat-sys-outline-variant); border-radius: 8px; overflow: hidden; background: var(--mat-sys-surface-container); }
    .sw-spinner-wrap { display: flex; justify-content: center; padding: 48px; }
    .sw-error { padding: 16px; color: #d32f2f; font-size: 0.85rem; }
    .sw-empty { padding: 16px; font-size: 0.85rem; color: #888; }
    .sw-table { width: 100%; }

    .sw-th { font-size: 0.72rem; font-weight: 600; }
    .mat-column-software_id { width: 80px; }
    .mat-column-type { width: 90px; }

    .sw-cell-id { font-family: monospace; font-size: 0.75rem; font-weight: 600; }
    .sw-cell-name { font-size: 0.78rem; max-width: 200px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .sw-cell-platforms { max-width: 180px; }

    .sw-type-chip { font-size: 0.65rem; height: 18px; font-weight: 600; }
    .sw-mini-chip { font-size: 0.62rem; height: 16px; margin: 0 2px 2px 0; }
    .sw-empty-dash { color: #bbb; font-size: 0.75rem; }

    .sw-header-row { height: 36px; }
    .sw-data-row { height: 36px; cursor: pointer; }

    .sw-pagination { display: flex; justify-content: space-between; align-items: center; padding: 8px 16px; border-top: 1px solid var(--mat-sys-outline-variant); }
    .sw-pagination__count { font-size: 0.75rem; color: #888; }
    .sw-pagination__nav { display: flex; gap: 8px; align-items: center; }
    .sw-pagination__btn { font-size: 0.75rem; cursor: pointer; color: var(--mat-sys-primary); }
    .sw-pagination__btn.disabled { color: var(--mat-sys-on-surface-variant); cursor: default; pointer-events: none; }
    .sw-pagination__info { font-size: 0.75rem; color: #888; }

    .sw-detail-panel { width: 320px; flex-shrink: 0; border: 1px solid var(--mat-sys-outline-variant); border-radius: 8px; padding: 16px; height: fit-content; position: sticky; top: 24px; background: var(--mat-sys-surface-container); }
    .sw-detail-panel__top { display: flex; align-items: center; gap: 8px; margin-bottom: 4px; }
    .sw-detail-panel__id { font-family: monospace; font-size: 0.85rem; font-weight: 700; }
    .sw-detail-panel__name { font-size: 0.9rem; font-weight: 600; margin-bottom: 8px; }
    .sw-detail-panel__desc { font-size: 0.72rem; color: #888; line-height: 1.5; margin-top: 12px; max-height: 280px; overflow-y: auto; }
    .sw-detail-panel__link-wrap { margin-top: 8px; }
    .sw-detail-panel__link { font-size: 0.72rem; text-decoration: none; }

    .sw-detail-section { margin-bottom: 8px; }
    .sw-detail-section__label { font-size: 0.72rem; color: #888; margin-bottom: 4px; }
  `],
})
export class MitreSoftwareComponent {
  private feedsApi = inject(FeedsApiService)

  readonly INTEL_COLOR = INTEL_COLOR
  readonly MALWARE_COLOR = MALWARE_COLOR
  readonly TOOL_COLOR = TOOL_COLOR
  readonly displayedColumns = ['software_id', 'type', 'name', 'platforms']

  search = signal('')
  page = signal(1)
  softwareType = signal<'malware' | 'tool' | ''>('')
  selected = signal<MitreSoftware | null>(null)

  statsQuery = injectQuery(() => ({
    queryKey: ['feeds', 'software', 'stats'],
    queryFn: () => firstValueFrom(this.feedsApi.getMitreSoftwareStats()),
  }))

  listQuery = injectQuery(() => ({
    queryKey: ['feeds', 'software', 'attack_v19', this.softwareType(), this.search(), this.page()],
    queryFn: () => firstValueFrom(this.feedsApi.getMitreSoftware({
      source: 'attack_v19',
      software_type: this.softwareType() || undefined,
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

  onTypeChange(v: 'malware' | 'tool' | '') {
    this.softwareType.set(v)
    this.page.set(1)
  }

  setPage(p: number) {
    this.page.set(p)
  }

  onRowClick(s: MitreSoftware) {
    this.selected.set(this.selected()?.id === s.id ? null : s)
  }
}
