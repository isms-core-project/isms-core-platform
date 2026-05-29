import { Component, inject, computed } from '@angular/core'
import { NgClass } from '@angular/common'
import { Router } from '@angular/router'
import { firstValueFrom } from 'rxjs'
import { injectQuery, injectMutation } from '@tanstack/angular-query-experimental'

import { MatIconModule } from '@angular/material/icon'
import { MatButtonModule } from '@angular/material/button'
import { MatChipsModule } from '@angular/material/chips'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'

import { ThreatIntelApiService } from '../../api/threat-intel-api.service'
import { AuthService } from '../../core/services/auth.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

const INTEL_COLOR = '#FFA726'

function fmt(iso: string | null): string {
  if (!iso) return '—'
  return new Date(iso).toLocaleString(undefined, {
    year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit',
  })
}

function statusLabel(s: string | null): string {
  if (!s) return 'Never run'
  if (s === 'success') return 'OK'
  if (s === 'running') return 'Running'
  return 'Error'
}

function statusClass(s: string | null): string {
  if (!s) return 'chip-default'
  if (s === 'success') return 'chip-success'
  if (s === 'running') return 'chip-info'
  return 'chip-error'
}

function statusIcon(s: string | null): string {
  if (!s) return 'schedule'
  if (s === 'success') return 'check_circle'
  if (s === 'running') return 'sync'
  return 'error'
}

@Component({
  selector: 'app-threat-intel-dashboard',
  standalone: true,
  imports: [
    NgClass,
    PageHeaderComponent,
    MatIconModule, MatButtonModule, MatChipsModule,
    MatTooltipModule, MatProgressSpinnerModule,
  ],
  template: `
<div class="tid-page">
  <app-page-header
    title="Threat Intelligence"
    subtitle="OSINT IOC feeds · Malware families · Actor attribution"
  />

  @if (summaryQuery.isLoading()) {
    <div class="loading-center">
      <mat-spinner diameter="32" />
    </div>
  }

  @if (!summaryQuery.isLoading() && !summaryQuery.data()?.active) {
    <div class="alert alert-info">
      <mat-icon>info</mat-icon>
      Threat Intelligence module is not active.
      Start the platform with <code>--profile threat-intel</code> and set
      <code>THREAT_INTEL_ENABLED=true</code> to enable it.
    </div>
  }

  @if (summaryQuery.isError()) {
    <div class="alert alert-error">
      <mat-icon>error</mat-icon> Could not load threat intelligence data.
    </div>
  }

  @if (summaryQuery.data()?.active) {
    <!-- Stat cards -->
    <div class="stat-cards">
      <div class="stat-card clickable" (click)="router.navigate(['/ioc-explorer'])">
        <mat-icon class="stat-icon stat-icon-ioc">track_changes</mat-icon>
        <div>
          <div class="stat-val">{{ (summaryQuery.data()?.total_iocs ?? 0).toLocaleString() }}</div>
          <div class="stat-lbl">Total IOCs</div>
        </div>
      </div>
      <div class="stat-card clickable" (click)="router.navigate(['/malware-atlas'])">
        <mat-icon class="stat-icon stat-icon-malware">coronavirus</mat-icon>
        <div>
          <div class="stat-val">{{ (summaryQuery.data()?.total_families ?? 0).toLocaleString() }}</div>
          <div class="stat-lbl">Malware Families</div>
        </div>
      </div>
      <div class="stat-card clickable" (click)="router.navigate(['/malware-atlas'])">
        <mat-icon class="stat-icon stat-icon-actor">person_outline</mat-icon>
        <div>
          <div class="stat-val">{{ (summaryQuery.data()?.total_actors ?? 0).toLocaleString() }}</div>
          <div class="stat-lbl">Threat Actors</div>
        </div>
      </div>
      <div class="stat-card">
        <mat-icon class="stat-icon stat-icon-tools">build</mat-icon>
        <div>
          <div class="stat-val">{{ (summaryQuery.data()?.total_tools ?? 0).toLocaleString() }}</div>
          <div class="stat-lbl">Tools</div>
        </div>
      </div>
    </div>

    <!-- Source table -->
    <div class="table-box">
      <div class="table-box__header">
        <span class="table-box__title" [style.color]="INTEL_COLOR">Feed Sources</span>
      </div>
      <table>
        <thead>
          <tr>
            <th>Source</th>
            <th>Enabled</th>
            <th>Last Run</th>
            <th>Last Run At</th>
            <th>IOCs</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          @for (src of summaryQuery.data()?.sources ?? []; track src.source) {
            <tr>
              <td>
                <div class="src-cell">
                  <mat-icon class="src-icon">stream</mat-icon>
                  <div>
                    <div class="src-name">{{ src.display_name }}</div>
                    <div class="src-slug">{{ src.source }}</div>
                  </div>
                </div>
              </td>
              <td>
                <span class="chip" [class.chip-success]="src.enabled" [class.chip-default]="!src.enabled">
                  {{ src.enabled ? 'Enabled' : 'Disabled' }}
                </span>
              </td>
              <td>
                <span class="chip" [ngClass]="statusClass(src.last_run_status)">
                  <mat-icon>{{ statusIcon(src.last_run_status) }}</mat-icon>
                  {{ statusLabel(src.last_run_status) }}
                </span>
              </td>
              <td class="mono dim">{{ fmt(src.last_run_at) }}</td>
              <td class="bold">{{ src.ioc_count.toLocaleString() }}</td>
              <td>
                @if (isAdmin() && src.enabled) {
                  <button mat-icon-button class="run-btn"
                    [disabled]="triggerMutation.isPending()"
                    [matTooltip]="'Trigger ' + src.display_name + ' now'"
                    (click)="triggerFeed(src.source)">
                    <mat-icon>play_arrow</mat-icon>
                  </button>
                }
              </td>
            </tr>
          }
        </tbody>
      </table>
    </div>

    @if (triggerMutation.isSuccess()) {
      <div class="alert alert-success">
        <mat-icon>check_circle</mat-icon>
        Feed triggered — check status in a few minutes.
      </div>
    }
    @if (triggerMutation.isError()) {
      <div class="alert alert-error">
        <mat-icon>error</mat-icon> Could not reach TI trigger server.
      </div>
    }
  }
</div>
  `,
  styles: [`
    .tid-page {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .loading-center { display: flex; justify-content: center; margin-top: 48px; }

    .alert {
      display: flex; align-items: center; gap: 8px;
      padding: 10px 14px; border-radius: 6px; font-size: 0.82rem;
    }
    .alert mat-icon { font-size: 18px; flex-shrink: 0; }
    .alert code { background: var(--mat-sys-surface-container-high); padding: 1px 5px; border-radius: 3px; font-size: 0.78rem; }
    .alert-info    { background: var(--mat-sys-surface-container); border: 1px solid var(--mat-sys-outline-variant); }
    .alert-error   { background: rgba(192,0,0,0.08); color: var(--mat-sys-error); border: 1px solid rgba(192,0,0,0.2); }
    .alert-success { background: rgba(46,125,50,0.08); color: #2e7d32; border: 1px solid rgba(46,125,50,0.2); }

    .stat-cards {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 12px;
    }
    .stat-card {
      border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 8px;
      padding: 14px;
      display: flex;
      align-items: center;
      gap: 12px;
      transition: border-color 0.15s;
    }
    .stat-card.clickable { cursor: pointer; }
    .stat-card.clickable:hover { border-color: #FFA726; background: rgba(184,79,0,0.04); }
    .stat-icon { font-size: 32px; width: 32px; height: 32px; flex-shrink: 0; }
    .stat-icon-ioc    { color: #FFA726; }
    .stat-icon-malware{ color: #6a0dad; }
    .stat-icon-actor  { color: #c62828; }
    .stat-icon-tools  { color: #1565c0; }
    .stat-val { font-size: 1.5rem; font-weight: 700; line-height: 1; }
    .stat-lbl { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); margin-top: 2px; }

    .table-box { border: 1px solid var(--mat-sys-outline-variant); border-radius: 8px; overflow: hidden; }
    .table-box__header { padding: 8px 14px; border-bottom: 1px solid var(--mat-sys-outline-variant); }
    .table-box__title { font-size: 0.85rem; font-weight: 700; }

    table { width: 100%; border-collapse: collapse; }
    thead { background: var(--mat-sys-surface-container); }
    th { font-size: 0.72rem; font-weight: 700; padding: 6px 10px; text-align: left; }
    td { font-size: 0.78rem; padding: 6px 10px; border-top: 1px solid var(--mat-sys-outline-variant); }
    tr:hover td { background: var(--mat-sys-surface-container); }

    .src-cell { display: flex; align-items: center; gap: 8px; }
    .src-icon { font-size: 20px; width: 20px; height: 20px; color: var(--mat-sys-on-surface-variant); }
    .src-name { font-size: 0.82rem; font-weight: 600; }
    .src-slug { font-family: monospace; font-size: 0.7rem; color: var(--mat-sys-on-surface-variant); }

    .chip {
      display: inline-flex; align-items: center; gap: 2px;
      font-size: 0.68rem; height: 20px; padding: 0 6px; border-radius: 10px;
    }
    .chip mat-icon { font-size: 12px; width: 12px; height: 12px; }
    .chip-default { background: var(--mat-sys-surface-container-high); color: var(--mat-sys-on-surface-variant); }
    .chip-success { background: rgba(46,125,50,0.15); color: #2e7d32; }
    .chip-info    { background: rgba(21,101,192,0.15); color: #1565c0; }
    .chip-error   { background: rgba(192,0,0,0.15); color: #9e0000; }

    .run-btn { width: 28px; height: 28px; }

    .mono  { font-family: monospace; }
    .dim   { color: var(--mat-sys-on-surface-variant); font-size: 0.75rem; }
    .bold  { font-weight: 600; }
  `],
})
export class ThreatIntelDashboardComponent {
  readonly router = inject(Router)
  private tiApi   = inject(ThreatIntelApiService)
  private auth    = inject(AuthService)

  readonly INTEL_COLOR = INTEL_COLOR
  readonly fmt = fmt
  readonly statusLabel = statusLabel
  readonly statusClass = statusClass
  readonly statusIcon  = statusIcon

  readonly isAdmin = computed(() => {
    const role = this.auth.user()?.role
    return role === 'admin' || role === 'super_admin'
  })

  readonly summaryQuery = injectQuery(() => ({
    queryKey: ['threat-intel', 'summary'],
    queryFn:  () => firstValueFrom(this.tiApi.getSummary()),
    staleTime: 60_000,
    refetchInterval: 60_000,
  }))

  readonly triggerMutation = injectMutation(() => ({
    mutationFn: (source: string) => firstValueFrom(this.tiApi.triggerFeed(source)),
  }))

  triggerFeed(source: string) { this.triggerMutation.mutate(source) }
}
