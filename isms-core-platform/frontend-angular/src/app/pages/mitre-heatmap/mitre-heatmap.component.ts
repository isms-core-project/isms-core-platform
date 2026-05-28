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
import { MatSlideToggleModule } from '@angular/material/slide-toggle'

import { FeedsApiService, MitreGroup, MitreHeatmapTechnique } from '../../api/feeds-api.service'
import { ThemeService } from '../../core/services/theme.service'

const INTEL_DARK  = '#FFA726'
const INTEL_LIGHT = '#E65100'

const TACTIC_LABELS: Record<string, string> = {
  'reconnaissance':       'Reconnaissance',
  'resource-development': 'Resource Dev.',
  'initial-access':       'Initial Access',
  'execution':            'Execution',
  'persistence':          'Persistence',
  'privilege-escalation': 'Priv. Escalation',
  'defense-evasion':      'Stealth',
  'defense-impairment':   'Defense Impairment',
  'credential-access':    'Credential Access',
  'discovery':            'Discovery',
  'lateral-movement':     'Lateral Movement',
  'collection':           'Collection',
  'command-and-control':  'C2',
  'exfiltration':         'Exfiltration',
  'impact':               'Impact',
}

function cellBg(count: number, max: number, isDark: boolean): string {
  if (count === 0) return 'transparent'
  const ratio = Math.min(count / Math.max(max, 1), 1)
  if (isDark) {
    if (ratio < 0.1)  return '#FFE0C8'
    if (ratio < 0.25) return '#FFBC8A'
    if (ratio < 0.5)  return '#F09050'
    if (ratio < 0.75) return '#D06020'
    return INTEL_DARK
  } else {
    if (ratio < 0.1)  return '#FFD1A0'
    if (ratio < 0.25) return '#FFAB5A'
    if (ratio < 0.5)  return '#E07030'
    if (ratio < 0.75) return '#B05010'
    return INTEL_LIGHT
  }
}

function cellFg(count: number, max: number): string {
  const ratio = Math.min(count / Math.max(max, 1), 1)
  return ratio >= 0.25 ? '#fff' : '#7A3800'
}

const TIER_LABELS: Record<number, string> = { 1: 'Partial', 2: 'Risk Informed', 3: 'Repeatable', 4: 'Adaptive' }

@Component({
  selector: 'app-mitre-heatmap',
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
    MatSlideToggleModule,
  ],
  template: `
<div class="page-wrap">

  <!-- Header -->
  <div class="page-header">
    <h2 class="page-title">MITRE ATT&amp;CK Heatmap</h2>
    <p class="page-subtitle">
      Technique coverage by threat actor — click any row to inspect
    </p>
  </div>

  <!-- Controls -->
  <div class="controls-row">
    <mat-button-toggle-group value="attack_v19" class="version-toggle">
      <mat-button-toggle value="attack_v19" class="version-btn">v19</mat-button-toggle>
    </mat-button-toggle-group>

    <!-- Group filter -->
    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="group-filter">
      <mat-label>Filter by group</mat-label>
      <mat-select [ngModel]="selectedGroupIds()" (ngModelChange)="onGroupChange($event)" multiple>
        @for (g of allGroups(); track g.group_id) {
          <mat-option [value]="g.group_id" class="group-option">{{g.group_id}} — {{g.name}}</mat-option>
        }
      </mat-select>
    </mat-form-field>

    <mat-slide-toggle [checked]="includeSoftware()" (change)="includeSoftware.set($event.checked)" class="slide-label">
      Include software
    </mat-slide-toggle>

    <mat-slide-toggle [checked]="showSubs()" (change)="showSubs.set($event.checked)" class="slide-label">
      Sub-techniques
    </mat-slide-toggle>
  </div>

  <!-- Stats bar -->
  @if (heatmapQuery.data(); as hm) {
    <div class="stats-bar">
      <div>
        <div class="stat-value" [style.color]="intelColor">
          {{hm.covered | number}} / {{hm.total_techniques | number}}
        </div>
        <div class="stat-label">Techniques covered ({{coveragePct()}}%)</div>
      </div>
      <div>
        <div class="stat-value" [style.color]="intelColor">{{hm.selected_actors | number}}</div>
        <div class="stat-label">{{selectedGroupIds().length > 0 ? 'Selected actors' : 'Actors in scope'}}</div>
      </div>
      <div>
        <div class="stat-value" [style.color]="intelColor">{{maxCount()}}</div>
        <div class="stat-label">Max actors / technique</div>
      </div>

      <!-- Color legend -->
      <div class="legend-row">
        <span class="legend-label legend-label-left">Coverage:</span>
        @for (swatch of legendSwatches(); track $index) {
          <div [matTooltip]="swatch.label" class="legend-swatch"
            [style.background]="swatch.bg"></div>
        }
        <span class="legend-label legend-label-right">High</span>
      </div>
    </div>
  }

  @if (heatmapQuery.isLoading()) {
    <div class="spinner-center">
      <mat-spinner [diameter]="32" />
    </div>
  }

  @if (heatmapQuery.isError()) {
    <div class="error-msg">Failed to load heatmap data.</div>
  }

  <!-- Heatmap table view + detail panel -->
  @if (!heatmapQuery.isLoading() && heatmapQuery.data(); as hm) {
    <div class="content-row">

      <!-- Tactic/technique table -->
      <div class="table-panel">
        <table mat-table [dataSource]="tableRows()" class="full-width">

          <ng-container matColumnDef="tactic">
            <th mat-header-cell *matHeaderCellDef class="col-hdr col-tactic">Tactic</th>
            <td mat-cell *matCellDef="let row" class="cell-tactic">
              {{tacticLabel(row.tactic)}}</td>
          </ng-container>

          <ng-container matColumnDef="technique_id">
            <th mat-header-cell *matHeaderCellDef class="col-hdr col-technique-id">Technique</th>
            <td mat-cell *matCellDef="let row" class="cell-technique-id"
              [style.color]="intelColor"
              [style.paddingLeft]="row.tech.is_subtechnique ? '24px' : ''">
              {{row.tech.technique_id}}</td>
          </ng-container>

          <ng-container matColumnDef="name">
            <th mat-header-cell *matHeaderCellDef class="col-hdr">Name</th>
            <td mat-cell *matCellDef="let row" class="cell-name">
              {{row.tech.name}}</td>
          </ng-container>

          <ng-container matColumnDef="usage">
            <th mat-header-cell *matHeaderCellDef class="col-hdr col-actors">Actors</th>
            <td mat-cell *matCellDef="let row" class="col-actors">
              <div class="usage-cell">
                <div class="bar-track">
                  <div class="bar-fill"
                    [style.width]="barWidth(row.tech.usage_count) + '%'"
                    [style.background]="cellBg(row.tech.usage_count, maxCount())"></div>
                </div>
                <span class="bar-count"
                  [style.color]="row.tech.usage_count > 0 ? intelColor : '#bbb'">
                  {{row.tech.usage_count}}
                </span>
              </div>
            </td>
          </ng-container>

          <tr mat-header-row *matHeaderRowDef="displayedColumns" class="hdr-row"></tr>
          <tr mat-row *matRowDef="let row; columns: displayedColumns"
            class="data-row"
            [style.background]="selectedTech()?.stix_id === row.tech.stix_id ? 'rgba(184,79,0,0.08)' : ''"
            (click)="onTechClick(row.tech)"></tr>
        </table>
      </div>

      <!-- Detail panel -->
      @if (selectedTech(); as tech) {
        <div class="detail-panel">
          <div class="detail-id-row">
            <div class="detail-tech-id" [style.color]="intelColor">{{tech.technique_id}}</div>
            @if (tech.is_subtechnique) {
              <mat-chip class="chip-sub">sub</mat-chip>
            }
          </div>
          <div class="detail-name">{{tech.name}}</div>

          <!-- Tactics -->
          <div class="detail-tactics">
            @for (t of tech.tactics; track t) {
              <mat-chip class="chip-tactic">{{tacticLabel(t)}}</mat-chip>
            }
          </div>

          <!-- Coverage box -->
          <div class="coverage-box" [style.background]="intelColor + '18'">
            <div class="coverage-label">Used by</div>
            <div class="coverage-count" [style.color]="intelColor">{{tech.usage_count}}</div>
            <div class="coverage-label">{{tech.usage_count === 1 ? 'actor' : 'actors'}} in scope</div>
          </div>

          <!-- Actor list -->
          @if (tech.used_by.length > 0) {
            <div>
              <div class="actor-list-hdr">
                Actors ({{tech.used_by.length}}):
              </div>
              @for (name of tech.used_by; track name) {
                <div class="actor-item">· {{name}}</div>
              }
            </div>
          }

          @if (tech.usage_count === 0) {
            <div class="no-actor-msg">Not attributed to any actor in the current scope.</div>
          }
        </div>
      }
    </div>
  }
</div>
  `,
  styles: [`
    .mat-mdc-row:hover { background: rgba(0,0,0,0.04); }

    .page-wrap { padding: 24px; }

    .page-header { margin-bottom: 16px; }
    .page-title { margin: 0; font-size: 1.3rem; font-weight: 700; }
    .page-subtitle { margin: 4px 0 0; color: var(--mat-sys-on-surface-variant); font-size: 0.85rem; }

    .controls-row {
      display: flex; gap: 12px; margin-bottom: 16px;
      align-items: center; flex-wrap: wrap;
    }
    .version-toggle { height: 32px; }
    .version-btn { font-size: 0.72rem; padding: 0 12px; }
    ::ng-deep .version-btn .mat-button-toggle-label-content { display: flex; align-items: center; justify-content: center; gap: 4px; padding: 0; }
    .group-filter { min-width: 280px; }
    .group-option { font-size: 0.8rem; }
    .slide-label { font-size: 0.8rem; }

    .stats-bar {
      display: flex; gap: 24px; margin-bottom: 16px;
      flex-wrap: wrap; align-items: center;
    }
    .stat-value { font-size: 1.25rem; font-weight: 700; line-height: 1; }
    .stat-label { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }

    .legend-row { display: flex; align-items: center; gap: 4px; margin-left: auto; }
    .legend-label { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
    .legend-label-left { margin-right: 4px; }
    .legend-label-right { margin-left: 4px; }
    .legend-swatch { width: 20px; height: 14px; border-radius: 2px; border: 1px solid rgba(0,0,0,0.1); }

    .spinner-center { display: flex; justify-content: center; padding: 64px; }
    .error-msg { padding: 16px; color: #d32f2f; font-size: 0.85rem; }

    .content-row { display: flex; gap: 16px; }

    .table-panel {
      flex: 1; min-width: 0;
      border: 1px solid var(--mat-sys-outline-variant); border-radius: 8px; overflow: hidden;
      background: var(--mat-sys-surface-container);
    }
    .full-width { width: 100%; }

    .col-hdr { font-size: 0.72rem; font-weight: 600; }
    .col-tactic { width: 140px; }
    .col-technique-id { width: 110px; }
    .col-actors { width: 100px; }

    .cell-tactic { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
    .cell-technique-id { font-family: monospace; font-size: 0.72rem; font-weight: 600; }
    .cell-name {
      font-size: 0.78rem; max-width: 260px;
      overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
    }

    .usage-cell { display: flex; align-items: center; gap: 6px; }
    .bar-track { width: 56px; height: 10px; border-radius: 2px; overflow: hidden; background: var(--mat-sys-surface-container-high); }
    .bar-fill { height: 100%; border-radius: 2px; transition: width 0.2s; min-width: 3px; }
    .bar-count { font-size: 0.72rem; min-width: 20px; text-align: right; }

    .hdr-row { height: 36px; }
    .data-row { height: 32px; cursor: pointer; }

    .detail-panel {
      width: 300px; flex-shrink: 0;
      border: 1px solid var(--mat-sys-outline-variant); border-radius: 8px;
      padding: 16px; position: sticky; top: 24px;
      max-height: 80vh; overflow-y: auto;
      background: var(--mat-sys-surface-container);
    }
    .detail-id-row { display: flex; align-items: baseline; gap: 8px; margin-bottom: 4px; }
    .detail-tech-id { font-family: monospace; font-size: 0.85rem; font-weight: 700; }
    .chip-sub { font-size: 0.6rem; height: 16px; }
    .detail-name { font-size: 0.88rem; font-weight: 600; margin-bottom: 8px; }

    .detail-tactics { margin-bottom: 12px; }
    .chip-tactic { font-size: 0.62rem; height: 18px; margin: 0 2px 2px 0; }

    .coverage-box { margin-bottom: 12px; padding: 8px; border-radius: 4px; }
    .coverage-label { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
    .coverage-count { font-size: 1.5rem; font-weight: 700; line-height: 1.2; }

    .actor-list-hdr { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); font-weight: 600; margin-bottom: 4px; }
    .actor-item { font-size: 0.7rem; padding: 1px 0; }
    .no-actor-msg { font-size: 0.72rem; color: #bbb; }
  `],
})
export class MitreHeatmapComponent {
  private feedsApi = inject(FeedsApiService)
  private readonly theme = inject(ThemeService)

  get intelColor() { return this.theme.isDark() ? INTEL_DARK : INTEL_LIGHT }
  readonly displayedColumns = ['tactic', 'technique_id', 'name', 'usage']

  selectedGroupIds = signal<string[]>([])
  includeSoftware = signal(true)
  showSubs = signal(true)
  selectedTech = signal<MitreHeatmapTechnique | null>(null)

  groupsQuery = injectQuery(() => ({
    queryKey: ['feeds', 'groups', 'all', 'attack_v19'],
    queryFn: () => firstValueFrom(this.feedsApi.getMitreGroups({ source: 'attack_v19', deprecated: false, per_page: 200 })),
  }))

  allGroups = computed(() => this.groupsQuery.data()?.items ?? [])

  heatmapQuery = injectQuery(() => ({
    queryKey: ['feeds', 'heatmap', 'attack_v19', this.selectedGroupIds().join(','), this.includeSoftware()],
    queryFn: () => firstValueFrom(this.feedsApi.getMitreHeatmap({
      source: 'attack_v19',
      group_ids: this.selectedGroupIds().length > 0 ? this.selectedGroupIds().join(',') : undefined,
      include_software: this.includeSoftware(),
    })),
    staleTime: 60_000,
  }))

  maxCount = computed(() => {
    const techs = this.heatmapQuery.data()?.techniques ?? []
    return Math.max(...techs.map(t => t.usage_count), 1)
  })

  coveragePct = computed(() => {
    const hm = this.heatmapQuery.data()
    return hm ? Math.round((hm.covered / Math.max(hm.total_techniques, 1)) * 100) : 0
  })

  legendSwatches = computed(() => {
    const max = this.maxCount()
    const isDark = this.theme.isDark()
    return [0, 0.1, 0.3, 0.6, 1].map((ratio, i) => {
      const count = Math.round(ratio * max)
      return {
        bg: cellBg(count, max, isDark),
        label: i === 0 ? 'Not covered' : `${count}+ actors`,
      }
    })
  })

  // Flatten techniques into tactic-indexed rows, respecting showSubs
  tableRows = computed(() => {
    const hm = this.heatmapQuery.data()
    if (!hm) return []
    const showSubs = this.showSubs()
    const rows: { tactic: string; tech: MitreHeatmapTechnique }[] = []
    for (const tac of hm.tactic_order) {
      const inTactic = hm.techniques.filter(t => t.tactics.includes(tac))
      const parents = inTactic.filter(t => !t.is_subtechnique)
        .sort((a, b) => a.technique_id.localeCompare(b.technique_id))
      if (showSubs) {
        const subs = inTactic.filter(t => t.is_subtechnique)
        for (const p of parents) {
          rows.push({ tactic: tac, tech: p })
          const mySubs = subs.filter(s => s.technique_id.startsWith(p.technique_id + '.'))
            .sort((a, b) => a.technique_id.localeCompare(b.technique_id))
          for (const s of mySubs) rows.push({ tactic: tac, tech: s })
        }
      } else {
        for (const p of parents) rows.push({ tactic: tac, tech: p })
      }
    }
    return rows
  })

  tacticLabel(tac: string): string {
    return TACTIC_LABELS[tac] ?? tac
  }

  cellBg(count: number, max: number): string {
    return cellBg(count, max, this.theme.isDark())
  }

  barWidth(count: number): number {
    return Math.round((count / Math.max(this.maxCount(), 1)) * 100)
  }

  onGroupChange(ids: string[]) {
    this.selectedGroupIds.set(ids)
    this.selectedTech.set(null)
  }

  onTechClick(tech: MitreHeatmapTechnique) {
    this.selectedTech.set(this.selectedTech()?.stix_id === tech.stix_id ? null : tech)
  }
}
