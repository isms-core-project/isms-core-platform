import { Component, inject, signal, computed } from '@angular/core'
import { CommonModule } from '@angular/common'
import { RouterLink, ActivatedRoute, Router } from '@angular/router'
import { firstValueFrom } from 'rxjs'

import { injectQuery } from '@tanstack/angular-query-experimental'

import { MatButtonModule } from '@angular/material/button'
import { MatChipsModule } from '@angular/material/chips'
import { MatIconModule } from '@angular/material/icon'
import { MatProgressBarModule } from '@angular/material/progress-bar'
import { MatTableModule } from '@angular/material/table'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatDividerModule } from '@angular/material/divider'

import { NistApiService, NistRating, FunctionScore } from '../../api/nist-api.service'

// ── Constants ──────────────────────────────────────────────────────────────────

const FUNCTION_COLORS: Record<string, string> = {
  GV: '#4472C4', ID: '#ED7D31', PR: '#70AD47',
  DE: '#FFC000', RS: '#FF5252', RC: '#9966CC',
}
const FUNCTION_NAMES: Record<string, string> = {
  GV: 'Govern', ID: 'Identify', PR: 'Protect',
  DE: 'Detect', RS: 'Respond', RC: 'Recover',
}
const TIER_LABELS: Record<number, string> = {
  1: 'Partial', 2: 'Risk Informed', 3: 'Repeatable', 4: 'Adaptive',
}
const FUNCTION_ORDER = ['GV', 'ID', 'PR', 'DE', 'RS', 'RC']

function tierColor(tier: number | null): string {
  if (!tier) return 'rgba(0,0,0,0.08)'
  if (tier === 1) return '#FF5252'
  if (tier === 2) return '#FFC000'
  if (tier === 3) return '#70AD47'
  return '#4472C4'
}

// ── SVG Radar helpers ─────────────────────────────────────────────────────────

interface RadarPoint { x: number; y: number }

function polarToXY(angleDeg: number, radius: number, cx: number, cy: number): RadarPoint {
  const rad = (angleDeg - 90) * Math.PI / 180
  return { x: cx + radius * Math.cos(rad), y: cy + radius * Math.sin(rad) }
}

function radarPoints(values: number[], max: number, cx: number, cy: number, maxR: number): RadarPoint[] {
  return values.map((v, i) => {
    const angle = (i / values.length) * 360
    const r = (v / max) * maxR
    return polarToXY(angle, r, cx, cy)
  })
}

function pointsToPath(pts: RadarPoint[]): string {
  return pts.map((p, i) => `${i === 0 ? 'M' : 'L'} ${p.x.toFixed(1)} ${p.y.toFixed(1)}`).join(' ') + ' Z'
}

@Component({
  selector: 'app-nist-csf-report',
  standalone: true,
  imports: [
    CommonModule,
    RouterLink,
    MatButtonModule,
    MatChipsModule,
    MatIconModule,
    MatProgressBarModule,
    MatTableModule,
    MatTooltipModule,
    MatDividerModule,
  ],
  template: `
<div class="report-wrap">

  @if (summaryQuery.isLoading() || fullQuery.isLoading()) {
    <mat-progress-bar mode="indeterminate" />
  }

  @if (!summaryQuery.isLoading() && (!summaryQuery.data() || !fullQuery.data())) {
    <div class="not-found">Profile not found.</div>
  }

  @if (summaryQuery.data() && fullQuery.data(); as full) {
    @if (summaryQuery.data(); as summary) {

      <!-- ── Top bar ── -->
      <div class="topbar">
        <div>
          <div class="topbar-title-row">
            <div class="topbar-accent-bar"></div>
            <h2 class="topbar-title">NIST CSF 2.0 Assessment Report</h2>
          </div>
          <div class="topbar-profile-name">{{full.profile.name}}</div>
          <div class="topbar-chips">
            @if (full.profile.assessor) {
              <mat-chip class="chip-sm">Assessor: {{full.profile.assessor}}</mat-chip>
            }
            @if (full.profile.scope) {
              <mat-chip class="chip-sm">Scope: {{full.profile.scope}}</mat-chip>
            }
            <mat-chip class="chip-sm chip-status">
              {{capitalize(full.profile.status)}}
            </mat-chip>
            <mat-chip class="chip-sm">
              {{full.profile.updated_at | date:'dd MMM yyyy'}}
            </mat-chip>
          </div>
        </div>

        <div class="topbar-actions">
          <button mat-stroked-button class="btn-sm" routerLink="/nist-csf">
            <mat-icon>arrow_back</mat-icon>
            Back
          </button>
          <button mat-stroked-button class="btn-sm" (click)="exportXlsx()">
            <mat-icon>download</mat-icon>
            XLSX
          </button>
          <button mat-flat-button color="primary" class="btn-sm" (click)="print()">
            <mat-icon>print</mat-icon>
            Print / PDF
          </button>
        </div>
      </div>

      <!-- ── KPI cards ── -->
      <div class="kpi-grid">
        @for (kpi of kpiCards(summary, gapRatings(full.ratings), totalGap(full.ratings)); track kpi.label) {
          <div class="kpi-card"
            [style.borderColor]="kpi.color + '33'"
            [style.borderLeft]="'3px solid ' + kpi.color">
            <div class="kpi-label">{{kpi.label}}</div>
            <div class="kpi-value" [style.color]="kpi.color">{{kpi.value}}</div>
            <div class="kpi-sub">{{kpi.sub}}</div>
          </div>
        }
      </div>

      <!-- ── Radar + Function breakdown ── -->
      <div class="radar-grid">

        <!-- Radar chart (SVG) -->
        <div class="panel">
          <div class="panel-label">Maturity Radar</div>
          <svg [attr.width]="'100%'" viewBox="0 0 260 260" class="radar-svg">
            <!-- Grid rings -->
            @for (ring of [1,2,3,4]; track ring) {
              <polygon [attr.points]="gridRingPoints(ring, 4, 130, 130, 100)"
                fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1" />
            }
            <!-- Grid spokes -->
            @for (fc of functionOrder; track fc; let i = $index) {
              @let spoke = spokeEnd(i, functionOrder.length, 130, 130, 100);
              <line [attr.x1]="130" [attr.y1]="130" [attr.x2]="spoke.x" [attr.y2]="spoke.y"
                stroke="rgba(255,255,255,0.08)" stroke-width="1" />
            }
            <!-- Target polygon -->
            @let targetPts = radarPathTarget(summary.function_scores);
            <path [attr.d]="targetPts" fill="#70AD47" fill-opacity="0.12" stroke="#70AD47" stroke-width="1.5" stroke-dasharray="5 3" />
            <!-- Current polygon -->
            @let currentPts = radarPathCurrent(summary.function_scores);
            <path [attr.d]="currentPts" fill="#4472C4" fill-opacity="0.3" stroke="#4472C4" stroke-width="2" />
            <!-- Labels -->
            @for (fc of functionOrder; track fc; let i = $index) {
              @let lp = spokeEnd(i, functionOrder.length, 130, 130, 115);
              <text [attr.x]="lp.x" [attr.y]="lp.y"
                text-anchor="middle" dominant-baseline="central"
                [attr.fill]="funcColor(fc)" font-size="9" font-weight="700">{{funcName(fc)}}</text>
            }
          </svg>
          <div class="radar-legend">
            <div class="radar-legend-item">
              <div class="radar-legend-line radar-legend-current"></div>
              <span class="radar-legend-label">Current</span>
            </div>
            <div class="radar-legend-item">
              <div class="radar-legend-line radar-legend-target"></div>
              <span class="radar-legend-label">Target</span>
            </div>
          </div>
        </div>

        <!-- Function bar breakdown -->
        <div class="panel">
          <div class="panel-label panel-label-mb">Function Breakdown</div>
          @for (d of barData(summary.function_scores); track d.fc) {
            <div class="bar-row">
              <div class="bar-name">{{d.name}}</div>
              <div class="bar-track">
                <!-- Target bar (faint) -->
                <div class="bar-fill bar-target"
                  [style.width]="((d.target / 4) * 100) + '%'"
                  [style.background]="funcColor(d.fc)"></div>
                <!-- Current bar -->
                <div class="bar-fill bar-current"
                  [style.width]="((d.current / 4) * 100) + '%'"
                  [style.background]="funcColor(d.fc)"
                  [matTooltip]="'Current T' + d.current.toFixed(1) + ' / Target T' + d.target.toFixed(1)"></div>
              </div>
              <div class="bar-tier" [style.color]="funcColor(d.fc)">
                T{{d.current.toFixed(1)}}</div>
            </div>
          }
        </div>
      </div>

      <!-- ── Function scores table ── -->
      <div class="section">
        <div class="section-label">Function Scores</div>
        <div class="table-wrap">
          <table mat-table [dataSource]="summary.function_scores" class="full-width">

            <ng-container matColumnDef="fn">
              <th mat-header-cell *matHeaderCellDef class="th-base">Function</th>
              <td mat-cell *matCellDef="let fs" class="td-base">
                <mat-chip class="chip-fn"
                  [style.background]="funcColor(fs.function_code) + '22'"
                  [style.color]="funcColor(fs.function_code)">{{fs.function_code}}</mat-chip>
              </td>
            </ng-container>

            <ng-container matColumnDef="name">
              <th mat-header-cell *matHeaderCellDef class="th-base">Name</th>
              <td mat-cell *matCellDef="let fs" class="td-base td-name">{{fs.function_name}}</td>
            </ng-container>

            <ng-container matColumnDef="current">
              <th mat-header-cell *matHeaderCellDef class="th-base">Avg Current</th>
              <td mat-cell *matCellDef="let fs" class="td-base">
                <ng-container [ngTemplateOutlet]="tierBadge" [ngTemplateOutletContext]="{tier: fs.avg_current ? round(fs.avg_current) : null}" />
              </td>
            </ng-container>

            <ng-container matColumnDef="target">
              <th mat-header-cell *matHeaderCellDef class="th-base">Avg Target</th>
              <td mat-cell *matCellDef="let fs" class="td-base">
                <ng-container [ngTemplateOutlet]="tierBadge" [ngTemplateOutletContext]="{tier: fs.avg_target ? round(fs.avg_target) : null}" />
              </td>
            </ng-container>

            <ng-container matColumnDef="gap">
              <th mat-header-cell *matHeaderCellDef class="th-base">Gap</th>
              <td mat-cell *matCellDef="let fs" class="td-base td-gap-text"
                [style.color]="gapColor(fs.avg_current, fs.avg_target)">
                {{gapStr(fs.avg_current, fs.avg_target)}}
              </td>
            </ng-container>

            <ng-container matColumnDef="rated">
              <th mat-header-cell *matHeaderCellDef class="th-base">Rated / Total</th>
              <td mat-cell *matCellDef="let fs" class="td-base td-gap-text">
                {{fs.rated_count}} / {{fs.total_count}}</td>
            </ng-container>

            <ng-container matColumnDef="progress">
              <th mat-header-cell *matHeaderCellDef class="th-base th-progress">Progress</th>
              <td mat-cell *matCellDef="let fs" class="td-base td-progress">
                <div class="prog-track">
                  <div class="prog-fill"
                    [style.width]="min100((fs.rated_count / fs.total_count) * 100) + '%'"
                    [style.background]="funcColor(fs.function_code)"></div>
                </div>
              </td>
            </ng-container>

            <tr mat-header-row *matHeaderRowDef="fsCols"></tr>
            <tr mat-row *matRowDef="let row; columns: fsCols" class="row-36"></tr>
          </table>
        </div>
      </div>

      <!-- ── Gap analysis ── -->
      @if (gapRatings(full.ratings).length > 0) {
        <div class="section">
          <div class="section-label">
            Gap Analysis — {{gapRatings(full.ratings).length}} subcategories behind target
          </div>
          <div class="table-wrap">
            <table mat-table [dataSource]="gapRatings(full.ratings)" class="full-width">

              <ng-container matColumnDef="fn_dot">
                <th mat-header-cell *matHeaderCellDef class="th-base th-dot">Fn</th>
                <td mat-cell *matCellDef="let r" class="td-base td-dot">
                  <div class="fn-dot"
                    [style.background]="funcColor(r.function_code)"></div>
                </td>
              </ng-container>

              <ng-container matColumnDef="code">
                <th mat-header-cell *matHeaderCellDef class="th-base">Subcategory</th>
                <td mat-cell *matCellDef="let r" class="td-base td-code">
                  {{r.subcategory_code}}</td>
              </ng-container>

              <ng-container matColumnDef="title">
                <th mat-header-cell *matHeaderCellDef class="th-base">Title</th>
                <td mat-cell *matCellDef="let r" class="td-base td-title-gap">
                  {{r.subcategory_title}}</td>
              </ng-container>

              <ng-container matColumnDef="current">
                <th mat-header-cell *matHeaderCellDef class="th-base">Current</th>
                <td mat-cell *matCellDef="let r" class="td-base">
                  <ng-container [ngTemplateOutlet]="tierBadge" [ngTemplateOutletContext]="{tier: r.current_tier}" />
                </td>
              </ng-container>

              <ng-container matColumnDef="target">
                <th mat-header-cell *matHeaderCellDef class="th-base">Target</th>
                <td mat-cell *matCellDef="let r" class="td-base">
                  <ng-container [ngTemplateOutlet]="tierBadge" [ngTemplateOutletContext]="{tier: r.target_tier}" />
                </td>
              </ng-container>

              <ng-container matColumnDef="gap">
                <th mat-header-cell *matHeaderCellDef class="th-base">Gap</th>
                <td mat-cell *matCellDef="let r" class="td-base">
                  <mat-chip class="chip-gap">
                    +{{r.target_tier! - r.current_tier!}}
                  </mat-chip>
                </td>
              </ng-container>

              <ng-container matColumnDef="iso">
                <th mat-header-cell *matHeaderCellDef class="th-base">ISO 27001</th>
                <td mat-cell *matCellDef="let r" class="td-base td-iso">
                  {{r.iso_mappings.slice(0,3).join(', ')}}{{r.iso_mappings.length > 3 ? ' +' + (r.iso_mappings.length - 3) : ''}}
                </td>
              </ng-container>

              <tr mat-header-row *matHeaderRowDef="gapCols"></tr>
              <tr mat-row *matRowDef="let row; columns: gapCols" class="row-36"></tr>
            </table>
          </div>
        </div>
      }

      <!-- ── Full assessment ── -->
      <mat-divider class="divider" />
      <div class="section-label">
        Full Assessment — 106 Subcategories
      </div>
      <div class="table-wrap">
        <table mat-table [dataSource]="fullRows(full.ratings)" class="full-width">

          <ng-container matColumnDef="fn">
            <th mat-header-cell *matHeaderCellDef class="th-base th-fn">Fn</th>
            <td mat-cell *matCellDef="let r" class="td-base td-fn">
              <mat-chip class="chip-fn"
                [style.background]="funcColor(r.function_code) + '22'"
                [style.color]="funcColor(r.function_code)">{{r.function_code}}</mat-chip>
            </td>
          </ng-container>

          <ng-container matColumnDef="code">
            <th mat-header-cell *matHeaderCellDef class="th-base">Code</th>
            <td mat-cell *matCellDef="let r" class="td-base td-code">
              {{r.subcategory_code}}</td>
          </ng-container>

          <ng-container matColumnDef="title">
            <th mat-header-cell *matHeaderCellDef class="th-base">Title</th>
            <td mat-cell *matCellDef="let r" class="td-base td-title-full">{{r.subcategory_title}}</td>
          </ng-container>

          <ng-container matColumnDef="current">
            <th mat-header-cell *matHeaderCellDef class="th-base">Current</th>
            <td mat-cell *matCellDef="let r" class="td-base">
              <ng-container [ngTemplateOutlet]="tierBadge" [ngTemplateOutletContext]="{tier: r.current_tier}" />
            </td>
          </ng-container>

          <ng-container matColumnDef="target">
            <th mat-header-cell *matHeaderCellDef class="th-base">Target</th>
            <td mat-cell *matCellDef="let r" class="td-base">
              <ng-container [ngTemplateOutlet]="tierBadge" [ngTemplateOutletContext]="{tier: r.target_tier}" />
            </td>
          </ng-container>

          <ng-container matColumnDef="gap">
            <th mat-header-cell *matHeaderCellDef class="th-base">Gap</th>
            <td mat-cell *matCellDef="let r" class="td-base td-gap-bold"
              [style.color]="ratingGapColor(r)">
              {{ratingGap(r)}}
            </td>
          </ng-container>

          <ng-container matColumnDef="progress">
            <th mat-header-cell *matHeaderCellDef class="th-base th-progress-full">Progress</th>
            <td mat-cell *matCellDef="let r" class="td-base td-progress-full">
              @if (r.current_tier !== null) {
                <div class="prog-track-tall">
                  <div class="prog-fill prog-fill-animated"
                    [style.width]="((r.current_tier / 4) * 100) + '%'"
                    [style.background]="tierColor(r.current_tier)"></div>
                  @if (r.target_tier) {
                    <div class="prog-target-marker"
                      [style.marginLeft]="((r.target_tier / 4) * 100) + '%'"></div>
                  }
                </div>
              } @else {
                <span class="no-rating">—</span>
              }
            </td>
          </ng-container>

          <ng-container matColumnDef="iso">
            <th mat-header-cell *matHeaderCellDef class="th-base">ISO 27001</th>
            <td mat-cell *matCellDef="let r" class="td-base td-iso">
              {{r.iso_mappings.slice(0,2).join(', ')}}{{r.iso_mappings.length > 2 ? ' +' + (r.iso_mappings.length - 2) : ''}}
            </td>
          </ng-container>

          <tr mat-header-row *matHeaderRowDef="fullCols" class="row-36 sticky-header"></tr>
          <tr mat-row *matRowDef="let row; columns: fullCols" class="row-34"></tr>
        </table>
      </div>
    }
  }
</div>

<!-- TierBadge template -->
<ng-template #tierBadge let-tier="tier">
  @if (tier) {
    <div class="tier-badge"
      [style.background]="tierColor(tier) + '22'"
      [style.border]="'1px solid ' + tierColor(tier) + '44'">
      <div class="tier-dot"
        [style.background]="tierColor(tier)"></div>
      <span class="tier-label" [style.color]="tierColor(tier)">T{{tier}}</span>
    </div>
  } @else {
    <span class="no-rating">—</span>
  }
</ng-template>
  `,
  styles: [`
    .mat-mdc-row:hover { background: rgba(255,255,255,0.015); }

    /* Page wrapper */
    .report-wrap { padding: 24px; max-width: 1200px; margin: 0 auto; }

    /* Not found */
    .not-found { padding: 32px; color: #d32f2f; }

    /* Top bar */
    .topbar { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 24px; }
    .topbar-title-row { display: flex; align-items: center; gap: 8px; margin-bottom: 4px; }
    .topbar-accent-bar { width: 3px; height: 32px; background: #4472C4; border-radius: 2px; }
    .topbar-title { margin: 0; font-size: 1.4rem; font-weight: 700; letter-spacing: -0.02em; }
    .topbar-profile-name { font-size: 1.1rem; color: #888; font-weight: 400; margin-left: 11px; }
    .topbar-chips { display: flex; gap: 8px; margin-top: 8px; margin-left: 11px; flex-wrap: wrap; }
    .topbar-actions { display: flex; gap: 8px; flex-shrink: 0; }
    .btn-sm { font-size: 0.72rem; }

    /* Chips */
    .chip-sm { font-size: 0.68rem; height: 20px; }
    .chip-status { background: #4472C422; color: #4472C4; }
    .chip-fn { font-size: 0.65rem; height: 18px; font-weight: 700; }
    .chip-gap { font-size: 0.62rem; height: 16px; font-weight: 700; background: #FFC00022; color: #FFC000; }

    /* KPI cards */
    .kpi-grid { display: grid; grid-template-columns: repeat(auto-fit,minmax(200px,1fr)); gap: 16px; margin-bottom: 24px; }
    .kpi-card { padding: 16px; border-radius: 8px; background: rgba(255,255,255,0.03); border: 1px solid; }
    .kpi-label { font-size: 0.62rem; color: #888; text-transform: uppercase; letter-spacing: 0.08em; }
    .kpi-value { font-size: 1.8rem; font-weight: 700; line-height: 1.2; margin-top: 4px; }
    .kpi-sub { font-size: 0.65rem; color: #888; }

    /* Radar / breakdown grid */
    .radar-grid { display: grid; grid-template-columns: 1fr 1.6fr; gap: 16px; margin-bottom: 24px; }
    .panel { padding: 16px; border-radius: 8px; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06); }
    .panel-label { font-size: 0.62rem; color: #888; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 8px; }
    .panel-label-mb { margin-bottom: 12px; }
    .radar-svg { max-height: 260px; }
    .radar-legend { display: flex; gap: 12px; margin-top: 4px; justify-content: center; }
    .radar-legend-item { display: flex; align-items: center; gap: 4px; }
    .radar-legend-line { width: 16px; height: 3px; border-radius: 2px; }
    .radar-legend-current { background: #4472C4; }
    .radar-legend-target { background: #70AD47; border-top: 1px dashed #70AD47; }
    .radar-legend-label { font-size: 0.68rem; color: #888; }

    /* Bar breakdown */
    .bar-row { display: flex; align-items: center; gap: 8px; margin-bottom: 10px; }
    .bar-name { width: 60px; font-size: 0.75rem; text-align: right; color: #8B9CC8; }
    .bar-track { flex: 1; position: relative; height: 14px; }
    .bar-fill { position: absolute; top: 0; left: 0; height: 14px; border-radius: 0 3px 3px 0; }
    .bar-target { opacity: 0.35; }
    .bar-tier { width: 32px; font-size: 0.7rem; font-family: monospace; }

    /* Sections */
    .section { margin-bottom: 24px; }
    .section-label { font-size: 0.62rem; color: #888; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 8px; }
    .table-wrap { border-radius: 8px; border: 1px solid rgba(255,255,255,0.06); overflow: hidden; }
    .full-width { width: 100%; }

    /* Table shared */
    .th-base { font-size: 0.68rem; font-weight: 700; color: #888; padding: 6px 8px; background: rgba(255,255,255,0.04); }
    .td-base { padding: 5px 8px; }
    .th-dot  { width: 24px; }
    .td-dot  { width: 24px; }
    .th-fn   { width: 40px; }
    .td-fn   { width: 40px; }
    .th-progress  { width: 120px; }
    .td-progress  { width: 120px; }
    .th-progress-full { width: 80px; }
    .td-progress-full { width: 80px; }
    .td-name  { font-size: 0.78rem; }
    .td-gap-text { font-size: 0.75rem; }
    .td-gap-bold { font-size: 0.7rem; font-weight: 700; }
    .td-code  { font-size: 0.72rem; font-family: monospace; color: #8B9CC8; white-space: nowrap; }
    .td-title-gap  { font-size: 0.72rem; max-width: 320px; }
    .td-title-full { font-size: 0.72rem; max-width: 280px; }
    .td-iso   { font-size: 0.62rem; color: #888; max-width: 120px; }

    /* Table rows */
    .row-36 { height: 36px; }
    .row-34 { height: 34px; }
    .sticky-header { position: sticky; top: 0; z-index: 2; }

    /* Progress bars */
    .prog-track { height: 4px; border-radius: 2px; background: rgba(255,255,255,0.08); overflow: hidden; }
    .prog-fill  { height: 100%; border-radius: 2px; }
    .prog-track-tall { height: 6px; border-radius: 2px; background: rgba(255,255,255,0.08); overflow: hidden; position: relative; }
    .prog-fill-animated { transition: width 0.2s; }
    .prog-target-marker { position: absolute; top: 0; left: 0; height: 100%; width: 2px; background: #70AD47; }

    /* Dot */
    .fn-dot { width: 6px; height: 6px; border-radius: 50%; }

    /* No rating placeholder */
    .no-rating { color: #bbb; font-size: 0.7rem; }

    /* Tier badge */
    .tier-badge { display: inline-flex; align-items: center; gap: 4px; padding: 2px 8px; border-radius: 4px; }
    .tier-dot { width: 6px; height: 6px; border-radius: 50%; }
    .tier-label { font-size: 0.7rem; font-weight: 700; }

    /* Divider */
    .divider { margin-bottom: 16px; opacity: 0.2; }
  `],
})
export class NistCsfReportComponent {
  private nistApi = inject(NistApiService)
  private route = inject(ActivatedRoute)
  private router = inject(Router)

  readonly fsCols = ['fn', 'name', 'current', 'target', 'gap', 'rated', 'progress']
  readonly gapCols = ['fn_dot', 'code', 'title', 'current', 'target', 'gap', 'iso']
  readonly fullCols = ['fn', 'code', 'title', 'current', 'target', 'gap', 'progress', 'iso']
  readonly functionOrder = FUNCTION_ORDER

  private id = this.route.snapshot.paramMap.get('id') ?? ''

  summaryQuery = injectQuery(() => ({
    queryKey: ['nist-summary', this.id],
    queryFn: () => firstValueFrom(this.nistApi.getProfileSummary(this.id)),
    enabled: !!this.id,
  }))

  fullQuery = injectQuery(() => ({
    queryKey: ['nist-full', this.id],
    queryFn: () => firstValueFrom(this.nistApi.getFullProfile(this.id)),
    enabled: !!this.id,
  }))

  // ── Helpers ──────────────────────────────────────────────────────────────────

  funcColor(fc: string): string { return FUNCTION_COLORS[fc] ?? '#8B9CC8' }
  funcName(fc: string): string { return FUNCTION_NAMES[fc] ?? fc }
  tierColor(tier: number | null): string { return tierColor(tier) }
  capitalize(s: string): string { return s ? s.charAt(0).toUpperCase() + s.slice(1) : '' }
  round(n: number): number { return Math.round(n) }
  min100(n: number): number { return Math.min(100, n) }

  gapStr(current: number | null, target: number | null): string {
    if (current == null || target == null) return '—'
    const g = target - current
    return g > 0 ? `+${g.toFixed(2)}` : g.toFixed(2)
  }

  gapColor(current: number | null, target: number | null): string {
    if (current == null || target == null) return '#bbb'
    const g = target - current
    return g > 0 ? '#FFC000' : g === 0 ? '#70AD47' : '#bbb'
  }

  totalGap(ratings: NistRating[]): number {
    return ratings.reduce((acc, r) => {
      if (r.current_tier !== null && r.target_tier !== null) acc += r.target_tier - r.current_tier
      return acc
    }, 0)
  }

  gapRatings(ratings: NistRating[]): NistRating[] {
    return ratings
      .filter(r => r.current_tier !== null && r.target_tier !== null && r.target_tier > r.current_tier)
      .sort((a, b) => (b.target_tier! - b.current_tier!) - (a.target_tier! - a.current_tier!))
  }

  fullRows(ratings: NistRating[]): NistRating[] {
    const out: NistRating[] = []
    for (const fc of FUNCTION_ORDER) {
      out.push(...ratings.filter(r => r.function_code === fc))
    }
    return out
  }

  kpiCards(summary: any, gapR: NistRating[], tGap: number): { label: string; value: string; sub: string; color: string }[] {
    return [
      {
        label: 'Avg Current Tier',
        value: summary.avg_current_tier ? `T${summary.avg_current_tier.toFixed(1)}` : '—',
        sub: summary.avg_current_tier ? (TIER_LABELS[Math.round(summary.avg_current_tier)] ?? '') : 'No ratings yet',
        color: tierColor(summary.avg_current_tier ? Math.round(summary.avg_current_tier) : null),
      },
      {
        label: 'Avg Target Tier',
        value: summary.avg_target_tier ? `T${summary.avg_target_tier.toFixed(1)}` : '—',
        sub: summary.avg_target_tier ? (TIER_LABELS[Math.round(summary.avg_target_tier)] ?? '') : 'No targets set',
        color: tierColor(summary.avg_target_tier ? Math.round(summary.avg_target_tier) : null),
      },
      {
        label: 'Coverage',
        value: `${summary.rated_count}/${summary.total_subcategories}`,
        sub: `${Math.round((summary.rated_count / summary.total_subcategories) * 100)}% rated`,
        color: '#4472C4',
      },
      {
        label: 'Total Gap Score',
        value: tGap > 0 ? `+${tGap}` : (tGap === 0 && summary.rated_count > 0 ? '0' : '—'),
        sub: gapR.length > 0 ? `${gapR.length} subcategories behind target` : 'No gaps identified',
        color: tGap > 0 ? '#FFC000' : '#70AD47',
      },
    ]
  }

  barData(fs: FunctionScore[]): { fc: string; name: string; current: number; target: number }[] {
    return FUNCTION_ORDER.map(fc => {
      const s = fs.find(f => f.function_code === fc)
      return { fc, name: FUNCTION_NAMES[fc], current: s?.avg_current ?? 0, target: s?.avg_target ?? 0 }
    })
  }

  // ── SVG Radar helpers ────────────────────────────────────────────────────────

  spokeEnd(i: number, total: number, cx: number, cy: number, r: number): { x: number; y: number } {
    return polarToXY((i / total) * 360, r, cx, cy)
  }

  gridRingPoints(ring: number, maxRing: number, cx: number, cy: number, maxR: number): string {
    const r = (ring / maxRing) * maxR
    return FUNCTION_ORDER.map((_, i) => {
      const p = polarToXY((i / FUNCTION_ORDER.length) * 360, r, cx, cy)
      return `${p.x.toFixed(1)},${p.y.toFixed(1)}`
    }).join(' ')
  }

  radarPathCurrent(fs: FunctionScore[]): string {
    const vals = FUNCTION_ORDER.map(fc => fs.find(f => f.function_code === fc)?.avg_current ?? 0)
    const pts = radarPoints(vals, 4, 130, 130, 100)
    return pointsToPath(pts)
  }

  radarPathTarget(fs: FunctionScore[]): string {
    const vals = FUNCTION_ORDER.map(fc => fs.find(f => f.function_code === fc)?.avg_target ?? 0)
    const pts = radarPoints(vals, 4, 130, 130, 100)
    return pointsToPath(pts)
  }

  // ── Rating row helpers ───────────────────────────────────────────────────────

  ratingGap(r: NistRating): string {
    if (r.current_tier == null) return '—'
    if (r.target_tier == null) return '—'
    const g = r.target_tier - r.current_tier
    return g > 0 ? `+${g}` : `${g}`
  }

  ratingGapColor(r: NistRating): string {
    if (r.current_tier == null || r.target_tier == null) return '#bbb'
    const g = r.target_tier - r.current_tier
    return g > 0 ? '#FFC000' : g === 0 ? '#70AD47' : '#FF5252'
  }

  // ── Actions ──────────────────────────────────────────────────────────────────

  print() {
    window.print()
  }

  async exportXlsx() {
    const blob = await firstValueFrom(this.nistApi.exportXlsx(this.id))
    const profile = this.fullQuery.data()?.profile
    const name = profile?.name?.replace(/\s+/g, '-') ?? 'profile'
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `NIST-CSF-${name}.xlsx`
    a.click()
    URL.revokeObjectURL(url)
  }
}
