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
import { MatSlideToggleModule } from '@angular/material/slide-toggle'

import { FeedsApiService, MitreHeatmapTechnique } from '../../api/feeds-api.service'
import { ThemeService } from '../../core/services/theme.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

const INTEL_DARK  = '#e06030'
const INTEL_LIGHT = '#c64227'

const TACTIC_SHORT: Record<string, string> = {
  'reconnaissance':       'Recon',
  'resource-development': 'Resource Dev',
  'initial-access':       'Initial Access',
  'execution':            'Execution',
  'persistence':          'Persistence',
  'privilege-escalation': 'Priv. Escalation',
  'defense-evasion':      'Defense Evasion',
  'defense-impairment':   'Def. Impairment',
  'credential-access':    'Credential Access',
  'discovery':            'Discovery',
  'lateral-movement':     'Lateral Movement',
  'collection':           'Collection',
  'command-and-control':  'C2',
  'exfiltration':         'Exfiltration',
  'impact':               'Impact',
}

function heatColor(count: number, max: number, isDark: boolean): string {
  if (count === 0) return isDark ? 'rgba(255,255,255,0.04)' : 'rgba(44,44,42,0.06)'
  const ratio = Math.min(count / Math.max(max, 1), 1)
  if (isDark) {
    if (ratio < 0.15) return 'rgba(224,96,48,0.20)'
    if (ratio < 0.35) return 'rgba(224,96,48,0.40)'
    if (ratio < 0.60) return 'rgba(224,96,48,0.65)'
    if (ratio < 0.85) return 'rgba(224,96,48,0.85)'
    return '#e06030'
  } else {
    if (ratio < 0.15) return 'rgba(186,117,23,0.18)'
    if (ratio < 0.35) return 'rgba(186,117,23,0.38)'
    if (ratio < 0.60) return 'rgba(186,117,23,0.60)'
    if (ratio < 0.85) return 'rgba(186,117,23,0.80)'
    return '#c64227'
  }
}

function textColor(count: number, max: number): string {
  const ratio = Math.min(count / Math.max(max, 1), 1)
  return ratio >= 0.5 ? '#fff' : 'inherit'
}

@Component({
  selector: 'app-mitre-heatmap',
  standalone: true,
  imports: [
    DecimalPipe, FormsModule, PageHeaderComponent,
    MatFormFieldModule, MatInputModule, MatSelectModule,
    MatIconModule, MatTooltipModule, MatProgressSpinnerModule,
    MatSlideToggleModule,
  ],
  template: `
<div class="hm-page">
  <app-page-header
    title="ATT&CK Heatmap"
    subtitle="MITRE ATT&CK — technique coverage by threat actor group"
  />

  <!-- Controls -->
  <div class="hm-controls">
    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="hm-group-field">
      <mat-label>Filter by group</mat-label>
      <mat-icon matPrefix>filter_list</mat-icon>
      <mat-select [ngModel]="selectedGroupIds()" (ngModelChange)="onGroupChange($event)" multiple>
        @for (g of allGroups(); track g.group_id) {
          <mat-option [value]="g.group_id">{{ g.group_id }} — {{ g.name }}</mat-option>
        }
      </mat-select>
    </mat-form-field>
    <mat-slide-toggle [checked]="includeSoftware()" (change)="includeSoftware.set($event.checked)">
      Include software
    </mat-slide-toggle>
    <mat-slide-toggle [checked]="showSubs()" (change)="showSubs.set($event.checked)">
      Sub-techniques
    </mat-slide-toggle>
  </div>

  <!-- Stats + legend -->
  @if (heatmapQuery.data(); as hm) {
    <div class="hm-stats-row">
      <div class="mitre-stats" style="margin-bottom:0">
        <div>
          <div class="mitre-stat__val" [style.color]="intelColor">{{ hm.covered | number }} / {{ hm.total_techniques | number }}</div>
          <div class="mitre-stat__lbl">Techniques covered ({{ coveragePct() }}%)</div>
        </div>
        <div>
          <div class="mitre-stat__val" [style.color]="intelColor">{{ hm.selected_actors | number }}</div>
          <div class="mitre-stat__lbl">{{ selectedGroupIds().length > 0 ? 'Selected actors' : 'Actors in scope' }}</div>
        </div>
        <div>
          <div class="mitre-stat__val" [style.color]="intelColor">{{ maxCount() }}</div>
          <div class="mitre-stat__lbl">Max actors / technique</div>
        </div>
      </div>
      <!-- Legend -->
      <div class="hm-legend">
        <span class="hm-legend__label">Coverage:</span>
        @for (s of legendSwatches(); track $index) {
          <div class="hm-legend__swatch" [matTooltip]="s.label" [style.background]="s.bg" [style.border]="'1px solid rgba(0,0,0,0.1)'"></div>
        }
        <span class="hm-legend__label">High</span>
      </div>
    </div>
  }

  @if (heatmapQuery.isLoading()) {
    <div class="hm-spinner"><mat-spinner diameter="32" /></div>
  }
  @if (heatmapQuery.isError()) {
    <div class="mitre-error">Failed to load heatmap data.</div>
  }

  <!-- HEATMAP GRID -->
  @if (!heatmapQuery.isLoading() && heatmapQuery.data(); as hm) {
    <div class="hm-outer">
      <div class="hm-grid-wrap">
        <div class="hm-grid" [style.grid-template-columns]="'repeat(' + hm.tactic_order.length + ', minmax(80px, 1fr))'">

          <!-- Tactic headers -->
          @for (tac of hm.tactic_order; track tac) {
            <div class="hm-tactic-hdr" [matTooltip]="tac.replace(/-/g, ' ')">
              {{ tacticShort(tac) }}
            </div>
          }

          <!-- Technique cells per tactic column -->
          @for (tac of hm.tactic_order; track tac) {
            <div class="hm-col">
              @for (tech of techsByTactic()[tac] ?? []; track tech.stix_id) {
                <div class="hm-cell"
                  [class.hm-cell--sub]="tech.is_subtechnique"
                  [class.hm-cell--selected]="selectedTech()?.stix_id === tech.stix_id"
                  [style.background]="heatColor(tech.usage_count, maxCount())"
                  [style.color]="textColor(tech.usage_count, maxCount())"
                  [matTooltip]="tech.technique_id + ' — ' + tech.name + (tech.usage_count > 0 ? ' (' + tech.usage_count + ' actors)' : '')"
                  (click)="onCellClick(tech)">
                  <span class="hm-cell__id">{{ tech.technique_id }}</span>
                </div>
              }
            </div>
          }
        </div>
      </div>

      <!-- Detail panel -->
      @if (selectedTech(); as tech) {
        <div class="mitre-detail hm-detail">
          <div class="mitre-detail__id" [style.color]="intelColor">{{ tech.technique_id }}</div>
          <div class="mitre-detail__name">{{ tech.name }}</div>
          @if (tech.is_subtechnique) {
            <span class="mitre-chip" style="margin-bottom:8px;display:inline-block">Sub-technique</span>
          }
          <div class="mitre-detail__label">Tactics</div>
          <div class="chip-row" style="gap:4px;margin-bottom:10px">
            @for (t of tech.tactics; track t) {
              <span class="mitre-chip">{{ tacticShort(t) }}</span>
            }
          </div>

          <!-- Coverage box -->
          <div class="hm-coverage-box" [style.background]="intelColor + '18'">
            <div class="hm-coverage__count" [style.color]="intelColor">{{ tech.usage_count }}</div>
            <div class="hm-coverage__lbl">{{ tech.usage_count === 1 ? 'actor' : 'actors' }} in scope</div>
          </div>

          @if (tech.used_by.length > 0) {
            <div class="mitre-detail__label">Used by</div>
            <div class="mitre-detail__actors">
              @for (name of tech.used_by; track name) {
                <div class="mitre-detail__actor">{{ name }}</div>
              }
            </div>
          }
          @if (tech.usage_count === 0) {
            <div class="hm-no-actors">Not attributed to any actor in the current scope.</div>
          }
        </div>
      }
    </div>
  }
</div>
  `,
  styles: [`
    .hm-page { display: flex; flex-direction: column; gap: 16px; }

    .hm-controls {
      display: flex; gap: 12px; align-items: center; flex-wrap: wrap;
    }
    .hm-group-field { flex: 1; min-width: 260px; max-width: 400px; }

    .hm-stats-row {
      display: flex; justify-content: space-between; align-items: center;
      flex-wrap: wrap; gap: 12px;
    }
    .hm-legend {
      display: flex; align-items: center; gap: 4px;
    }
    .hm-legend__label { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
    .hm-legend__swatch { width: 22px; height: 14px; border-radius: 2px; }

    .hm-spinner { display: flex; justify-content: center; padding: 64px; }

    .hm-outer { display: flex; gap: 16px; align-items: flex-start; }

    .hm-grid-wrap {
      flex: 1; min-width: 0; overflow-x: auto;
      border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 8px; background: var(--mat-sys-surface-container);
    }

    .hm-grid {
      display: grid;
      gap: 0;
    }

    .hm-tactic-hdr {
      padding: 6px 4px; font-size: 0.65rem; font-weight: 700;
      text-transform: uppercase; letter-spacing: 0.04em;
      color: var(--mat-sys-on-surface-variant);
      background: var(--mat-sys-surface-container);
      border-bottom: 1px solid var(--mat-sys-outline-variant);
      border-right: 1px solid var(--mat-sys-outline-variant);
      text-align: center; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
      position: sticky; top: 0; z-index: 2;
    }
    .hm-tactic-hdr:last-child { border-right: none; }

    .hm-col {
      display: flex; flex-direction: column;
      border-right: 1px solid var(--mat-sys-outline-variant);
    }
    .hm-col:last-child { border-right: none; }

    .hm-cell {
      padding: 3px 4px; font-size: 0.6rem; cursor: pointer;
      border-bottom: 1px solid rgba(255,255,255,0.04);
      transition: filter 0.1s; min-height: 22px;
      display: flex; align-items: center;
    }
    .hm-cell:hover { filter: brightness(1.3); }
    .hm-cell--sub { padding-left: 10px; opacity: 0.85; }
    .hm-cell--selected { outline: 2px solid var(--mat-sys-primary); outline-offset: -2px; z-index: 1; position: relative; }
    .hm-cell__id { font-family: monospace; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; font-size: 0.58rem; }

    html[data-theme='light'] .hm-cell { border-bottom-color: rgba(44,44,42,0.06); }

    .hm-detail { width: 280px; flex-shrink: 0; }

    .hm-coverage-box {
      padding: 10px; border-radius: 6px; margin-bottom: 12px; text-align: center;
    }
    .hm-coverage__count { font-size: 2rem; font-weight: 800; line-height: 1; }
    .hm-coverage__lbl   { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); margin-top: 2px; }

    .hm-no-actors { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); font-style: italic; }

    .chip-row { display: flex; flex-wrap: wrap; }
  `],
})
export class MitreHeatmapComponent {
  private feedsApi = inject(FeedsApiService)
  private readonly theme = inject(ThemeService)

  get intelColor() { return this.theme.isDark() ? INTEL_DARK : INTEL_LIGHT }

  selectedGroupIds = signal<string[]>([])
  includeSoftware  = signal(true)
  showSubs         = signal(false)
  selectedTech     = signal<MitreHeatmapTechnique | null>(null)

  readonly groupsQuery = injectQuery(() => ({
    queryKey: ['feeds', 'groups', 'all', 'attack_v19'],
    queryFn: () => firstValueFrom(this.feedsApi.getMitreGroups({ source: 'attack_v19', deprecated: false, per_page: 200 })),
  }))

  readonly allGroups = computed(() => this.groupsQuery.data()?.items ?? [])

  readonly heatmapQuery = injectQuery(() => ({
    queryKey: ['feeds', 'heatmap', 'attack_v19', this.selectedGroupIds().join(','), this.includeSoftware()],
    queryFn: () => firstValueFrom(this.feedsApi.getMitreHeatmap({
      source: 'attack_v19',
      group_ids: this.selectedGroupIds().length > 0 ? this.selectedGroupIds().join(',') : undefined,
      include_software: this.includeSoftware(),
    })),
    staleTime: 60_000,
  }))

  readonly maxCount = computed(() => {
    const techs = this.heatmapQuery.data()?.techniques ?? []
    return Math.max(...techs.map(t => t.usage_count), 1)
  })

  readonly coveragePct = computed(() => {
    const hm = this.heatmapQuery.data()
    return hm ? Math.round((hm.covered / Math.max(hm.total_techniques, 1)) * 100) : 0
  })

  readonly legendSwatches = computed(() => {
    const max = this.maxCount()
    const isDark = this.theme.isDark()
    return [0, 0.15, 0.4, 0.7, 1].map((r, i) => ({
      bg: heatColor(Math.round(r * max), max, isDark),
      label: i === 0 ? 'Not covered' : `~${Math.round(r * max)}+ actors`,
    }))
  })

  // Group techniques by tactic, respecting showSubs toggle
  readonly techsByTactic = computed(() => {
    const hm = this.heatmapQuery.data()
    if (!hm) return {} as Record<string, MitreHeatmapTechnique[]>
    const showSubs = this.showSubs()
    const result: Record<string, MitreHeatmapTechnique[]> = {}
    for (const tac of hm.tactic_order) {
      const inTactic = hm.techniques.filter(t => t.tactics.includes(tac))
      const parents = inTactic.filter(t => !t.is_subtechnique)
        .sort((a, b) => a.technique_id.localeCompare(b.technique_id))
      if (showSubs) {
        const subs = inTactic.filter(t => t.is_subtechnique)
        const rows: MitreHeatmapTechnique[] = []
        for (const p of parents) {
          rows.push(p)
          const mySubs = subs.filter(s => s.technique_id.startsWith(p.technique_id + '.'))
            .sort((a, b) => a.technique_id.localeCompare(b.technique_id))
          rows.push(...mySubs)
        }
        result[tac] = rows
      } else {
        result[tac] = parents
      }
    }
    return result
  })

  tacticShort(tac: string): string { return TACTIC_SHORT[tac] ?? tac }
  heatColor(count: number, max: number): string { return heatColor(count, max, this.theme.isDark()) }
  textColor(count: number, max: number): string { return textColor(count, max) }

  onGroupChange(ids: string[]) { this.selectedGroupIds.set(ids); this.selectedTech.set(null) }
  onCellClick(tech: MitreHeatmapTechnique) {
    this.selectedTech.update(s => s?.stix_id === tech.stix_id ? null : tech)
  }
}
