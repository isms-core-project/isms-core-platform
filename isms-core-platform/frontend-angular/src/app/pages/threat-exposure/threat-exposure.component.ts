import { Component, inject, computed } from '@angular/core'
import { ThemeService } from '../../core/services/theme.service'
import { firstValueFrom } from 'rxjs'
import { injectQuery } from '@tanstack/angular-query-experimental'

import { MatIconModule } from '@angular/material/icon'
import { MatChipsModule } from '@angular/material/chips'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'

import { ThreatExposureApiService, ExposedControl, ExposureTechnique } from '../../api/threat-exposure-api.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

function scoreColor(score: number | null, isDark: boolean): string {
  if (score === null) return isDark ? 'rgba(255,255,255,0.15)' : 'rgba(0,0,0,0.08)'
  if (score >= 70) return '#00c752'
  if (score >= 40) return '#ff9800'
  return '#f44336'
}

function scoreTextColor(score: number | null, isDark: boolean): string {
  if (score === null) return isDark ? '#d9d9d9' : '#424242'
  return '#fff'
}

function statusLabel(status: string | null, score: number | null): string {
  if (score !== null) return `${score.toFixed(0)}%`
  if (!status) return 'Not assessed'
  return status.replace('_', ' ')
}

@Component({
  selector: 'app-threat-exposure',
  standalone: true,
  imports: [
    PageHeaderComponent,
    MatIconModule, MatChipsModule, MatTooltipModule, MatProgressSpinnerModule,
  ],
  template: `
<div class="te-page">
  <app-page-header
    title="Threat Exposure"
    subtitle="Active MITRE techniques from TI feeds mapped to ISO 27001 controls — gaps highlighted"
  />

  @if (exposureQuery.isLoading()) {
    <div class="loading-row">
      <mat-spinner diameter="20" />
      <span class="dim">Correlating TI feeds with crosswalk…</span>
    </div>
  }

  @if (exposureQuery.isError()) {
    <div class="alert alert-error">
      <mat-icon>error</mat-icon>
      Failed to load exposure data — threat-intel profile may not be active.
    </div>
  }

  @if (exposureQuery.data()?.technique_count === 0) {
    <div class="alert alert-info">
      <mat-icon>check_circle</mat-icon>
      No MITRE technique correlations found — either no IOCs with technique IDs are in the feeds,
      or the threat-intel profile is not active.
    </div>
  }

  @if (exposureQuery.data(); as data) {
    @if (data.technique_count > 0) {
      <!-- Summary bar -->
      <div class="summary-cards">
        <div class="summary-card">
          <span class="summary-val summary-val--red">{{ data.technique_count }}</span>
          <span class="summary-lbl">Active techniques</span>
        </div>
        <div class="summary-card">
          <span class="summary-val summary-val--amber">{{ data.affected_controls }}</span>
          <span class="summary-lbl">Affected controls</span>
        </div>
        <div class="summary-card">
          <span class="summary-val summary-val--red">{{ data.gap_controls }}</span>
          <span class="summary-lbl">Gaps identified</span>
        </div>
      </div>

      <!-- Technique → Control mapping table -->
      <div class="table-box">
        <div class="table-box__header">
          <div class="table-box__title-row">
            <mat-icon class="icon-md te-alert-icon">crisis_alert</mat-icon>
            <span class="table-box__title">Technique → Control Mapping</span>
          </div>
          <span class="dim">Controls coloured by assessment score · grey = not assessed</span>
        </div>
        <table>
          <thead>
            <tr>
              <th class="col-tid">Technique</th>
              <th class="col-ioc">IOC count</th>
              <th class="col-src">Sources</th>
              <th>ISO 27001 controls</th>
              <th class="col-gaps">Gaps</th>
            </tr>
          </thead>
          <tbody>
            @for (item of data.items; track item.mitre_tid) {
              <tr [class.row-gap]="gapCount(item) > 0">
                <td>
                  <div class="tid-cell">
                    @if (gapCount(item) > 0) {
                      <mat-icon class="warn-icon">warning_amber</mat-icon>
                    }
                    <span class="mono bold">{{ item.mitre_tid }}</span>
                  </div>
                </td>
                <td><span class="bold">{{ item.ioc_count.toLocaleString() }}</span></td>
                <td>
                  <div class="chip-wrap">
                    @for (s of item.sources.slice(0, 4); track s) {
                      <span class="src-chip">{{ s.replace('_misp', ' MISP') }}</span>
                    }
                  </div>
                </td>
                <td>
                  <div class="chip-wrap">
                    @for (ctrl of item.iso_controls; track ctrl.control_code) {
                      <span class="ctrl-chip"
                        [style.background]="scoreColor(ctrl.assessment_score)"
                        [style.color]="scoreTextColor(ctrl.assessment_score)"
                        [matTooltip]="ctrlTooltip(ctrl)">
                        {{ ctrlLabel(ctrl) }}
                      </span>
                    }
                  </div>
                </td>
                <td>
                  @if (gapCount(item) > 0) {
                    <span class="gap-chip">{{ gapCount(item) }}</span>
                  } @else {
                    <mat-icon class="te-ok-icon">check_circle</mat-icon>
                  }
                </td>
              </tr>
            }
          </tbody>
        </table>
      </div>
    }
  }
</div>
  `,
  styles: [`
    .te-page {
      display: flex;
      flex-direction: column;
      gap: 16px;
      padding-bottom: 24px;
    }

    .loading-row { display: flex; align-items: center; gap: 12px; padding: 32px 0; }

    .alert {
      display: flex; align-items: center; gap: 8px;
      padding: 10px 14px; border-radius: 6px; font-size: 0.82rem;
    }
    .alert mat-icon { font-size: 18px; flex-shrink: 0; }
    .alert-info  { background: var(--mat-sys-surface-container); border: 1px solid var(--mat-sys-outline-variant); }
    .alert-error { background: rgba(192,0,0,0.08); color: var(--mat-sys-error); border: 1px solid rgba(192,0,0,0.2); }

    .summary-cards {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
      gap: 12px;
    }
    .summary-card {
      border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 8px;
      padding: 14px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
    }
    .summary-val       { font-size: 2rem; font-weight: 800; line-height: 1; }
    .summary-val--red  { color: #f44336; }
    .summary-val--amber{ color: #ff9800; }
    .summary-lbl { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }

    .table-box { border: 1px solid var(--mat-sys-outline-variant); border-radius: 8px; overflow: hidden; }
    .table-box__header {
      padding: 8px 14px;
      border-bottom: 1px solid var(--mat-sys-outline-variant);
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 4px;
    }
    .table-box__title-row { display: flex; align-items: center; gap: 6px; }
    .table-box__title { font-size: 0.85rem; font-weight: 700; }

    table { width: 100%; border-collapse: collapse; }
    thead { background: var(--mat-sys-surface-container); }
    th { font-size: 0.72rem; font-weight: 700; padding: 6px 10px; text-align: left; }
    td { font-size: 0.75rem; padding: 5px 10px; border-top: 1px solid var(--mat-sys-outline-variant); vertical-align: top; }
    tr:hover td { background: var(--mat-sys-surface-container); }
    .row-gap { background: rgba(211,47,47,0.04); }

    .col-tid  { width: 110px; }
    .col-ioc  { width: 80px; }
    .col-src  { width: 200px; }
    .col-gaps { width: 70px; }

    .tid-cell { display: flex; align-items: center; gap: 4px; }
    .warn-icon    { font-size: 14px; width: 14px; height: 14px; color: #f44336; }
    .te-alert-icon{ color: #f44336; }
    .te-ok-icon   { font-size: 16px; height: 16px; width: 16px; color: #00c752; }

    .chip-wrap { display: flex; flex-wrap: wrap; gap: 3px; }

    .src-chip {
      display: inline-block; font-size: 0.6rem; padding: 1px 5px;
      border-radius: 8px; background: var(--mat-sys-surface-container-high);
      color: var(--mat-sys-on-surface-variant);
    }

    .ctrl-chip {
      display: inline-block; font-size: 0.62rem; padding: 1px 5px;
      border-radius: 8px; font-family: monospace;
      cursor: default;
    }

    .gap-chip {
      display: inline-block; font-size: 0.65rem; font-weight: 700;
      padding: 2px 7px; border-radius: 8px;
      background: #f44336; color: #fff;
    }

    .mono { font-family: monospace; }
    .bold { font-weight: 600; }
    .dim  { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
  `],
})
export class ThreatExposureComponent {
  private exposureApi = inject(ThreatExposureApiService)
  private readonly theme = inject(ThemeService)

  readonly scoreColor     = (score: number | null) => scoreColor(score, this.theme.isDark())
  readonly scoreTextColor = (score: number | null) => scoreTextColor(score, this.theme.isDark())

  readonly exposureQuery = injectQuery(() => ({
    queryKey: ['threat-exposure'],
    queryFn:  () => firstValueFrom(this.exposureApi.get()),
    staleTime: 5 * 60_000,
  }))

  gapCount(item: ExposureTechnique): number {
    return item.iso_controls.filter(c => c.gap).length
  }

  ctrlLabel(ctrl: ExposedControl): string {
    return ctrl.assessment_score != null
      ? `${ctrl.control_code} · ${ctrl.assessment_score.toFixed(0)}%`
      : ctrl.control_code
  }

  ctrlTooltip(ctrl: ExposedControl): string {
    const score = statusLabel(ctrl.framework_status, ctrl.assessment_score)
    return ctrl.control_name ? `${ctrl.control_name} — ${score}` : score
  }
}
