import { Component, inject, signal, computed } from '@angular/core'
import { Router } from '@angular/router'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'
import { injectQuery } from '@tanstack/angular-query-experimental'

import { MatCardModule } from '@angular/material/card'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatButtonToggleModule } from '@angular/material/button-toggle'
import { MatIconModule } from '@angular/material/icon'
import { MatChipsModule } from '@angular/material/chips'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatButtonModule } from '@angular/material/button'

import { ControlsApiService } from '../../api/controls-api.service'
import { ProductService } from '../../core/services/product.service'
import { ThemeService } from '../../core/services/theme.service'
import { ControlGroupList } from '../../shared/types'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

const ISMS_SECTION_COLORS: Record<string, string> = {
  'A.5': '#4472C4',
  'A.6': '#70AD47',
  'A.7': '#FFC000',
  'A.8': '#C00000',
}

const PRIVACY_SECTION_COLORS: Record<string, string> = {
  'A.1': '#ba68c8',  // Controller — canonical Privacy purple
  'A.2': '#5c6bc0',  // Processor — indigo
  'A.3': '#4db6ac',  // Shared — teal-green
}

const HEATMAP_DARK: Record<string, string> = {
  complete:   '#66BB6A',
  partial:    '#FFA726',
  basic:      '#EF6C00',
  incomplete: '#EF5350',
}

const HEATMAP_LIGHT: Record<string, string> = {
  complete:   '#4caf50',
  partial:    '#ff9800',
  basic:      '#f57c00',
  incomplete: '#f44336',
}

type ViewMode = 'grid' | 'heatmap'

function getSectionKey(cg: ControlGroupList): string {
  return cg.section
}

function deriveSectionName(cg: ControlGroupList): string {
  const names: Record<string, string> = {
    'A.5': 'Organisational Controls',
    'A.6': 'People Controls',
    'A.7': 'Physical Controls',
    'A.8': 'Technological Controls',
    'A.1': 'Privacy Controller',
    'A.2': 'Privacy Processor',
    'A.3': 'Privacy Shared',
  }
  return (cg as unknown as Record<string, string>)['section_name'] ?? names[cg.section] ?? cg.section
}

function getSectionColor(product: string, section: string): string {
  if (product === 'isms') return ISMS_SECTION_COLORS[section] ?? '#4472C4'
  if (product === 'privacy') return PRIVACY_SECTION_COLORS[section] ?? '#ba68c8'
  if (product === 'cloud') return '#29b6f6'
  return '#ffa726'
}

function getHeatmapStatus(cg: ControlGroupList): string {
  const cgExt = cg as unknown as Record<string, unknown>
  const fw = cgExt['framework_status'] as string | undefined
  const op = cgExt['operational_status'] as string | undefined
  if (fw === 'complete' && op === 'complete') return 'complete'
  if (fw === 'complete' || op === 'complete') return 'partial'
  if (fw || op) return 'basic'
  return 'incomplete'
}

@Component({
  selector: 'app-controls',
  standalone: true,
  imports: [
    FormsModule,
    MatCardModule, MatFormFieldModule, MatInputModule, MatSelectModule,
    MatButtonToggleModule, MatIconModule, MatChipsModule,
    MatProgressSpinnerModule, MatTooltipModule, MatButtonModule,
    PageHeaderComponent,
  ],
  template: `
<div class="controls-page">

  <app-page-header
    title="Controls Library"
    [subtitle]="controlsSubtitle()"
  />

  <!-- Toolbar -->
  <div class="controls-toolbar">
    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="search-field">
      <mat-label>Search</mat-label>
      <mat-icon matPrefix>search</mat-icon>
      <input matInput placeholder="Search controls…" [ngModel]="searchTerm()" (ngModelChange)="searchTerm.set($event)" />
    </mat-form-field>

    @if (showSectionFilter()) {
      <mat-form-field appearance="outline" subscriptSizing="dynamic" class="section-field">
        <mat-label>Section</mat-label>
        <mat-select [ngModel]="selectedSection()" (ngModelChange)="selectedSection.set($event)">
          <mat-option value="">All Sections</mat-option>
          @for (s of availableSections(); track s.key) {
            <mat-option [value]="s.key">{{ s.label }}</mat-option>
          }
        </mat-select>
      </mat-form-field>
    }

    @if (product.product() === 'isms') {
      <mat-button-toggle-group [ngModel]="selectedTier()" (ngModelChange)="selectedTier.set($event)" class="tier-toggle">
        <mat-button-toggle value="all">All</mat-button-toggle>
        <mat-button-toggle value="framework">Framework</mat-button-toggle>
        <mat-button-toggle value="operational">Operational</mat-button-toggle>
      </mat-button-toggle-group>
    }

    <mat-button-toggle-group [ngModel]="viewMode()" (ngModelChange)="viewMode.set($event)" class="view-toggle">
      <mat-button-toggle value="grid">
        <mat-icon>grid_view</mat-icon>
      </mat-button-toggle>
      @if (product.product() === 'isms') {
        <mat-button-toggle value="heatmap">
          <mat-icon>grid_on</mat-icon>
        </mat-button-toggle>
      }
    </mat-button-toggle-group>
  </div>

  <!-- Loading -->
  @if (controlsQuery.isLoading()) {
    <div class="controls-loading">
      <mat-spinner diameter="40" />
    </div>
  }

  <!-- Error -->
  @if (controlsQuery.isError()) {
    <div class="controls-error">Failed to load controls.</div>
  }

  <!-- Grid view -->
  @if (controlsQuery.isSuccess() && viewMode() === 'grid') {
    @for (section of groupedSections(); track section.key) {
      <div class="section-group">
        <div class="section-group__header"
             [style.border-left-color]="getSectionColorForProduct(section.key)">
          <span class="section-group__title">{{ section.key }} — {{ section.label }}</span>
          <span class="section-group__count">{{ section.items.length }}</span>
        </div>
        <div class="section-group__grid">
          @for (cg of section.items; track cg.id) {
            <mat-card class="control-card"
                      [style.border-left-color]="getSectionColorForProduct(cg.section)"
                      (click)="openControl(cg)">
              <mat-card-content>
                <div class="control-card__code"
                     [style.color]="getSectionColorForProduct(cg.section)">
                  {{ cg.group_code.toUpperCase() }}
                </div>
                <div class="control-card__name">{{ cg.group_name }}</div>
                <div class="control-card__section">{{ deriveSectionName(cg) }}</div>
                @if (product.product() === 'isms') {
                  <div class="control-card__pills">
                    <span class="pill" [class.pill--fw]="hasFw(cg)">FW</span>
                    <span class="pill" [class.pill--op]="hasOp(cg)">OP</span>
                  </div>
                }
              </mat-card-content>
            </mat-card>
          }
        </div>
      </div>
    }
  }

  <!-- Heatmap view (ISMS only) -->
  @if (controlsQuery.isSuccess() && viewMode() === 'heatmap') {
    <div class="heatmap">
      <div class="heatmap__legend">
        @for (entry of heatmapLegend(); track entry.label) {
          <div class="heatmap__legend-item">
            <span class="heatmap__legend-swatch" [style.background]="entry.color"></span>
            <span>{{ entry.label }}</span>
          </div>
        }
      </div>
      <div class="heatmap__grid">
        @for (cg of filteredControls(); track cg.id) {
          <div class="heatmap__cell"
               [style.background]="heatmapColor(cg)"
               [matTooltip]="cg.group_code.toUpperCase() + ' — ' + cg.group_name"
               (click)="openControl(cg)">
          </div>
        }
      </div>
    </div>
  }

  <!-- Empty state -->
  @if (controlsQuery.isSuccess() && filteredControls().length === 0) {
    <div class="controls-empty">
      <mat-icon>search_off</mat-icon>
      <span>No controls match your filters.</span>
    </div>
  }

</div>
  `,
  styles: [`
    .controls-page {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    /* Toolbar */
    .controls-toolbar {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
      padding-top: 12px;
    }
    .search-field { flex: 1; min-width: 200px; }
    .section-field { width: 200px; }
    .tier-toggle, .view-toggle { flex-shrink: 0; }

    /* Loading / error / empty */
    .controls-loading {
      display: flex;
      justify-content: center;
      padding: 48px;
    }
    .controls-error {
      color: var(--mat-sys-error);
      padding: 16px;
      text-align: center;
    }
    .controls-empty {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      color: var(--mat-sys-on-surface-variant);
      padding: 48px;
    }

    /* Section group */
    .section-group { display: flex; flex-direction: column; gap: 8px; }
    .section-group__header {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 6px 12px;
      background: var(--mat-sys-surface-container);
      border-radius: 4px;
      border-left: 4px solid transparent;
    }
    .section-group__title {
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--mat-sys-on-surface);
      flex: 1;
    }
    .section-group__count {
      font-size: 0.75rem;
      color: var(--mat-sys-on-surface-variant);
    }

    /* Card grid */
    .section-group__grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 8px;
    }

    /* Control card */
    .control-card {
      cursor: pointer;
      border-left: 3px solid transparent;
      transition: box-shadow 0.15s;
    }
    .control-card:hover { box-shadow: 0 2px 8px rgba(0,0,0,0.25); }
    mat-card-content { padding: 12px !important; }

    .control-card__code {
      font-family: monospace;
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.04em;
      margin-bottom: 4px;
    }
    .control-card__name {
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--mat-sys-on-surface);
      margin-bottom: 2px;
      line-height: 1.3;
    }
    .control-card__section {
      font-size: 0.7rem;
      color: var(--mat-sys-on-surface-variant);
      margin-bottom: 8px;
    }

    /* Pills */
    .control-card__pills {
      display: flex;
      gap: 4px;
    }
    .pill {
      font-size: 0.6rem;
      font-weight: 700;
      padding: 1px 6px;
      border-radius: 10px;
      background: var(--mat-sys-surface-container-high);
      color: var(--mat-sys-on-surface-variant);
      border: 1px solid var(--mat-sys-outline-variant);
    }
    .pill--fw {
      background: rgba(50,125,244,0.15);
      color: #327df4;
      border-color: rgba(50,125,244,0.4);
    }
    .pill--op {
      background: rgba(0,199,82,0.15);
      color: #00c752;
      border-color: rgba(0,199,82,0.4);
    }

    /* Heatmap */
    .heatmap { display: flex; flex-direction: column; gap: 12px; }
    .heatmap__legend {
      display: flex;
      gap: 16px;
      flex-wrap: wrap;
    }
    .heatmap__legend-item {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 0.75rem;
      color: var(--mat-sys-on-surface-variant);
    }
    .heatmap__legend-swatch {
      width: 16px;
      height: 16px;
      border-radius: 2px;
      flex-shrink: 0;
    }
    .heatmap__grid {
      display: flex;
      flex-wrap: wrap;
      gap: 4px;
    }
    .heatmap__cell {
      width: 60px;
      height: 60px;
      border-radius: 4px;
      cursor: pointer;
      transition: transform 0.1s;
    }
    .heatmap__cell:hover { transform: scale(1.08); }
  `],
})
export class ControlsComponent {
  readonly router  = inject(Router)
  readonly product = inject(ProductService)
  readonly theme   = inject(ThemeService)
  private  ctrlApi = inject(ControlsApiService)

  searchTerm      = signal('')
  selectedSection = signal('')
  selectedTier    = signal('all')
  viewMode        = signal<ViewMode>('grid')

  readonly deriveSectionName = deriveSectionName

  private get productFamily(): string {
    const p = this.product.product()
    if (p === 'privacy') return 'PRIVACY'
    if (p === 'cloud')   return 'CLOUD'
    if (p === 'ai')      return 'AI'
    return 'ISMS'
  }

  readonly controlsQuery = injectQuery(() => ({
    queryKey: ['controls', this.product.product()],
    queryFn: () => firstValueFrom(this.ctrlApi.list({ product_family: this.productFamily })),
    staleTime: 60_000,
  }))

  readonly filteredControls = computed((): ControlGroupList[] => {
    const items = this.controlsQuery.data() ?? []
    const search = this.searchTerm().toLowerCase()
    const section = this.selectedSection()
    const tier = this.selectedTier()
    const prod = this.product.product()

    return items.filter(cg => {
      if (search && !cg.group_code.toLowerCase().includes(search) && !cg.group_name.toLowerCase().includes(search)) {
        return false
      }
      if (section && cg.section !== section) return false
      if (prod === 'isms' && tier !== 'all') {
        if (tier === 'framework'   && !cg.has_framework)   return false
        if (tier === 'operational' && !cg.has_operational) return false
      }
      return true
    })
  })

  readonly groupedSections = computed(() => {
    const map = new Map<string, { key: string; label: string; items: ControlGroupList[] }>()
    for (const cg of this.filteredControls()) {
      const key = cg.section
      if (!map.has(key)) {
        map.set(key, { key, label: deriveSectionName(cg), items: [] })
      }
      map.get(key)!.items.push(cg)
    }
    return Array.from(map.values()).sort((a, b) => a.key.localeCompare(b.key))
  })

  readonly availableSections = computed(() => {
    const all = this.controlsQuery.data() ?? []
    const seen = new Map<string, string>()
    for (const cg of all) {
      if (!seen.has(cg.section)) seen.set(cg.section, deriveSectionName(cg))
    }
    return Array.from(seen.entries())
      .sort(([a], [b]) => a.localeCompare(b))
      .map(([key, label]) => ({ key, label }))
  })

  readonly showSectionFilter = computed(() => this.product.product() !== 'ai')

  readonly controlsSubtitle = computed(() => {
    const subtitles: Record<string, string> = {
      isms:    'ISO 27001:2022 Annex A control groups and implementation status',
      privacy: 'ISO 27701:2025 privacy control groups and implementation status',
      cloud:   'ISO 27018:2025 cloud control groups and implementation status',
      ai:      'ISO 42001:2023 AI control groups and implementation status',
    }
    return subtitles[this.product.product()] ?? subtitles['isms']
  })

  readonly heatmapLegend = computed(() => {
    const colors = this.theme.isDark() ? HEATMAP_DARK : HEATMAP_LIGHT
    return [
      { label: 'Complete',   color: colors['complete'] },
      { label: 'Partial',    color: colors['partial'] },
      { label: 'Basic',      color: colors['basic'] },
      { label: 'Incomplete', color: colors['incomplete'] },
    ]
  })

  getSectionColorForProduct(section: string): string {
    return getSectionColor(this.product.product(), section)
  }

  heatmapColor(cg: ControlGroupList): string {
    const status = getHeatmapStatus(cg)
    const colors = this.theme.isDark() ? HEATMAP_DARK : HEATMAP_LIGHT
    return colors[status] ?? colors['incomplete']
  }

  hasFw(cg: ControlGroupList): boolean { return cg.has_framework }
  hasOp(cg: ControlGroupList): boolean { return cg.has_operational }

  openControl(cg: ControlGroupList): void {
    this.router.navigate(['/controls', cg.id])
  }
}
