import { Component, inject, computed } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { firstValueFrom } from 'rxjs'

import { injectQuery } from '@tanstack/angular-query-experimental'

import { MatCardModule } from '@angular/material/card'
import { MatTableModule } from '@angular/material/table'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatIconModule } from '@angular/material/icon'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatChipsModule } from '@angular/material/chips'

import { PageHeaderComponent } from '../../shared/components/page-header.component'

// ─── Types ────────────────────────────────────────────────────────────────────

interface AxisRow {
  source_framework: string
  target_framework: string
  count: number
}

interface AxesResponse {
  axes: AxisRow[]
  total_mappings: number
  total_axes: number
}

interface KnownReview {
  status: 'pending' | 'review'
  note: string
  eta?: string
}

// ─── Static data ──────────────────────────────────────────────────────────────

const KNOWN_REVIEWS: Record<string, KnownReview> = {
  'NIST_800_53_R5 → MITRE_ATTACK_V19': {
    status: 'pending',
    note: 'MITRE ATT&CK v19 live 2026-04-28 — crosswalk updated to V19. Review Defense Evasion → Stealth / Defense Impairment remapping.',
    eta: '2026-04-28',
  },
  'ISO27001_2022 → ISO27017': {
    status: 'pending',
    note: 'ISO 27017:2025 revision in progress — re-validate cloud control mappings on official release.',
  },
  'ISO27017 → ISO27001_2022': {
    status: 'pending',
    note: 'ISO 27017:2025 revision in progress — re-validate reverse cloud mappings on official release.',
  },
  'ISO27017 → CSA_CCM_V4_1': {
    status: 'pending',
    note: 'ISO 27017:2025 revision in progress — review CCM cloud mappings after new ISO release.',
  },
  'ISO27017 → NIST_CSF_2.0': {
    status: 'pending',
    note: 'ISO 27017:2025 revision in progress — review NIST CSF cloud mappings after new ISO release.',
  },
}

const SOURCE_FILE: Record<string, string> = {
  ISO42001:       'iso42001_crosswalk.json',
  ISO42005:       'iso42005_crosswalk.json',
  ISO27001_2022:  'crosswalk.json',
  ISO27017:       'crosswalk.json',
  ISO27018:       'crosswalk.json',
  ISO27701:       'crosswalk.json',
  NIST_800_53_R5: 'crosswalk.json',
  NIST_AI_RMF:    'crosswalk.json',
}

const FW_LABEL: Record<string, string> = {
  ISO27001_2022:  'ISO 27001:2022',
  ISO27017:       'ISO 27017',
  ISO27018:       'ISO 27018',
  ISO27701:       'ISO 27701',
  ISO42001:       'ISO 42001:2023',
  ISO42005:       'ISO 42005:2025',
  NIST_800_53_R5: 'NIST SP 800-53 R5',
  NIST_AI_RMF:    'NIST AI RMF',
}

const FW_COLOR: Record<string, string> = {
  ISO27001_2022:  '#1565C0',
  ISO27017:       '#0277BD',
  ISO27018:       '#00838F',
  ISO27701:       '#6A1B9A',
  ISO42001:       '#E65100',
  ISO42005:       '#BF360C',
  NIST_800_53_R5: '#2E7D32',
  NIST_AI_RMF:    '#1B5E20',
}

const SOURCE_ORDER = [
  'ISO27001_2022', 'ISO27017', 'ISO27018', 'ISO27701',
  'ISO42001', 'ISO42005', 'NIST_800_53_R5', 'NIST_AI_RMF',
]

function fwColor(code: string): string {
  return FW_COLOR[code] ?? '#455A64'
}

// ─── Component ────────────────────────────────────────────────────────────────

@Component({
  selector: 'app-crosswalk-tracker',
  standalone: true,
  imports: [
    MatCardModule, MatTableModule, MatTooltipModule,
    MatIconModule, MatProgressSpinnerModule, MatChipsModule,
    PageHeaderComponent,
  ],
  template: `
    <div class="page-wrap">
      <app-page-header
        title="Crosswalk Tracker"
        subtitle="Cross-framework mapping axes — coverage, sprint history, and pending update flags" />

      <!-- Summary cards -->
      <div class="summary-row">
        @if (axesQuery.isLoading()) {
          @for (i of [1,2,3,4]; track i) {
            <div class="summary-skel"></div>
          }
        } @else {
          <mat-card class="summary-card">
            <mat-card-content>
              <span class="card-label">Total axes</span>
              <span class="card-value">{{ axesQuery.data()?.total_axes ?? 0 }}</span>
              <span class="card-sub">source → target pairs</span>
            </mat-card-content>
          </mat-card>
          <mat-card class="summary-card">
            <mat-card-content>
              <span class="card-label">Total mappings</span>
              <span class="card-value">{{ (axesQuery.data()?.total_mappings ?? 0).toLocaleString() }}</span>
              <span class="card-sub">across all 3 crosswalk files</span>
            </mat-card-content>
          </mat-card>
          <mat-card class="summary-card">
            <mat-card-content>
              <span class="card-label">Review flagged</span>
              <span class="card-value"
                [style.color]="reviewCount() > 0 ? '#FF9800' : '#4CAF50'">{{ reviewCount() }}</span>
              <span class="card-sub">axes needing manual review</span>
            </mat-card-content>
          </mat-card>
          <mat-card class="summary-card">
            <mat-card-content>
              <span class="card-label">Pending releases</span>
              <span class="card-value"
                [style.color]="pendingCount() > 0 ? '#42A5F5' : '#9E9E9E'">{{ pendingCount() }}</span>
              <span class="card-sub">axes pending source update</span>
            </mat-card-content>
          </mat-card>
        }
      </div>

      @if (axesQuery.isLoading()) {
        <div class="table-skel"></div>
      }

      <!-- Per-source-framework tables -->
      @if (!axesQuery.isLoading() && axesQuery.data()) {
        @for (src of visibleSources(); track src) {
          <div class="src-block">
            <div class="src-header">
              <div class="src-bar" [style.background]="fwColor(src)"></div>
              <span class="src-label" [style.color]="fwColor(src)">
                {{ fwLabel(src) }}
              </span>
              <span class="src-axis-count">
                ({{ grouped()[src]?.length }} ax{{ grouped()[src]?.length !== 1 ? 'es' : 'is' }}
                · {{ srcTotal(src).toLocaleString() }} mappings)
              </span>
              <span class="file-chip">{{ sourceFile(src) }}</span>
            </div>

            <div class="table-container">
              <table mat-table [dataSource]="grouped()[src] ?? []" class="full-width-table">

                <!-- Axis column -->
                <ng-container matColumnDef="axis">
                  <th mat-header-cell *matHeaderCellDef class="col-header">Axis</th>
                  <td mat-cell *matCellDef="let axis">
                    <div class="axis-cell">
                      <mat-icon class="icon-sm axis-icon">account_tree</mat-icon>
                      <span class="axis-src">{{ axis.source_framework }}</span>
                      <span class="axis-arrow">→</span>
                      <span class="axis-tgt">{{ axis.target_framework }}</span>
                    </div>
                  </td>
                </ng-container>

                <!-- Mappings column -->
                <ng-container matColumnDef="mappings">
                  <th mat-header-cell *matHeaderCellDef class="col-header col-right">Mappings</th>
                  <td mat-cell *matCellDef="let axis" class="col-right">
                    <span class="mapping-count">{{ axis.count.toLocaleString() }}</span>
                  </td>
                </ng-container>

                <!-- Last sprint column -->
                <ng-container matColumnDef="sprint">
                  <th mat-header-cell *matHeaderCellDef class="col-header">Last Sprint</th>
                  <td mat-cell *matCellDef="let axis">
                    <span class="sprint-date">2026-04-17</span>
                  </td>
                </ng-container>

                <!-- Status column -->
                <ng-container matColumnDef="status">
                  <th mat-header-cell *matHeaderCellDef class="col-header">Status</th>
                  <td mat-cell *matCellDef="let axis">
                    @if (!axisReview(axis)) {
                      <span class="chip chip-current">
                        <mat-icon class="chip-icon">check_circle</mat-icon>
                        Current
                      </span>
                    }
                    @if (axisReview(axis)?.status === 'review') {
                      <span class="chip chip-warn" [matTooltip]="axisReview(axis)!.note">
                        <mat-icon class="chip-icon">warning</mat-icon>
                        Review due
                      </span>
                    }
                    @if (axisReview(axis)?.status === 'pending') {
                      <span class="chip chip-pending"
                        [matTooltip]="axisReview(axis)!.note + (axisReview(axis)!.eta ? ' ETA: ' + axisReview(axis)!.eta : '')">
                        <mat-icon class="chip-icon">update</mat-icon>
                        {{ axisReview(axis)!.eta ? 'Pending (' + axisReview(axis)!.eta + ')' : 'Pending release' }}
                      </span>
                    }
                  </td>
                </ng-container>

                <tr mat-header-row *matHeaderRowDef="axisColumns"></tr>
                <tr mat-row *matRowDef="let row; columns: axisColumns" class="hover-row"></tr>
              </table>
            </div>
          </div>
        }
      }

      <div class="footer-note">
        <mat-icon class="icon-sm">info</mat-icon>
        Axis counts are live from the database. Review flags are tracked in
        <code>CrosswalkTracker</code> → <code>KNOWN_REVIEWS</code>.
        Sprint dates update manually after each mapping sprint.
        Files: <code>crosswalk.json</code> · <code>iso42001_crosswalk.json</code> · <code>iso42005_crosswalk.json</code>.
      </div>
    </div>
  `,
  styles: [`
    :host { display: block; }

    .summary-row { display: flex; gap: 16px; margin-top: 16px; margin-bottom: 24px; flex-wrap: wrap; }
    .summary-card { flex: 1; min-width: 140px; }
    .summary-card mat-card-content { padding-bottom: 12px !important; display: flex; flex-direction: column; }
    .card-label {
      font-size: 0.68rem; text-transform: uppercase; letter-spacing: 0.06em;
      color: var(--mat-sys-on-surface-variant); margin-bottom: 4px;
    }
    .card-value { font-size: 1.5rem; font-weight: 700; line-height: 1.2; }
    .card-sub { font-size: 0.65rem; color: var(--mat-sys-on-surface-variant); margin-top: 2px; }

    .summary-skel { flex: 1; min-width: 140px; height: 80px; border-radius: 4px; background: var(--mat-sys-surface-variant); }
    .table-skel { height: 200px; border-radius: 4px; background: var(--mat-sys-surface-variant); margin-bottom: 24px; }

    .src-bar { width: 4px; height: 20px; border-radius: 2px; flex-shrink: 0; }
    .src-label { font-size: 0.8rem; font-weight: 700; }
    .file-chip {
      font-family: monospace; font-size: 0.58rem;
      height: 16px; line-height: 16px; padding: 0 6px; border-radius: 8px;
      background: var(--mat-sys-surface-variant); color: var(--mat-sys-on-surface-variant);
      display: inline-block;
    }

    .table-container {
      border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 4px;
      overflow: hidden;
      background: var(--mat-sys-surface-container);
    }
    .col-header {
      font-size: 0.68rem !important; font-weight: 700 !important;
      text-transform: uppercase; color: var(--mat-sys-on-surface-variant) !important;
      letter-spacing: 0.04em;
    }
    .hover-row:hover { background: var(--mat-sys-surface-variant); }
    .hover-row:last-child td { border-bottom: none; }

    .chip {
      display: inline-flex; align-items: center;
      height: 18px; padding: 0 6px; border-radius: 9px;
      font-size: 0.6rem; font-weight: 600; white-space: nowrap;
    }
    .chip-current { background: rgba(76,175,80,0.1); color: #4CAF50; }
    .chip-warn    { background: rgba(255,152,0,0.1);  color: #FF9800; }
    .chip-pending { background: rgba(66,165,245,0.1); color: #42A5F5; }

    /* Extracted from inline */
    .page-wrap { padding:24px; max-width:1200px; }
    .src-block  { margin-bottom:24px; }
    .src-header { display:flex; align-items:center; gap:8px; margin-bottom:8px; flex-wrap:wrap; }
    .src-axis-count { font-size:0.72rem; color:var(--mat-sys-on-surface-variant); }
    .full-width-table { width:100%; }
    .axis-cell { display:flex; align-items:center; gap:6px; }
    .axis-icon { color:var(--mat-sys-on-surface-variant); }
    .axis-src  { font-weight:600; font-size:0.78rem; }
    .axis-arrow { font-size:0.7rem; color:var(--mat-sys-on-surface-variant); }
    .axis-tgt  { font-size:0.78rem; }
    .col-right  { text-align:right; }
    .mapping-count { font-size:0.75rem; font-weight:600; }
    .sprint-date { font-size:0.7rem; font-family:monospace; color:var(--mat-sys-on-surface-variant); }
    .chip-icon  { font-size:11px; width:11px; height:11px; vertical-align:middle; margin-right:3px; }
    .footer-note { font-size:0.62rem; color:var(--mat-sys-on-surface-variant); margin-top:16px; display:flex; align-items:center; gap:4px; }
  `],
})
export class CrosswalkTrackerComponent {
  private http = inject(HttpClient)

  readonly axisColumns = ['axis', 'mappings', 'sprint', 'status']

  axesQuery = injectQuery(() => ({
    queryKey: ['crosswalk-axes'],
    queryFn: () => firstValueFrom(this.http.get<AxesResponse>('/api/v1/frameworks/crosswalk/axes')),
  }))

  grouped = computed((): Record<string, AxisRow[]> => {
    const axes = this.axesQuery.data()?.axes ?? []
    const g: Record<string, AxisRow[]> = {}
    for (const axis of axes) {
      const src = axis.source_framework
      if (!g[src]) g[src] = []
      g[src].push(axis)
    }
    return g
  })

  visibleSources = computed(() =>
    SOURCE_ORDER.filter(src => (this.grouped()[src]?.length ?? 0) > 0)
  )

  reviewCount = computed(() => {
    let count = 0
    for (const axes of Object.values(this.grouped())) {
      for (const axis of axes) {
        if (KNOWN_REVIEWS[`${axis.source_framework} → ${axis.target_framework}`]?.status === 'review') count++
      }
    }
    return count
  })

  pendingCount = computed(() => {
    let count = 0
    for (const axes of Object.values(this.grouped())) {
      for (const axis of axes) {
        if (KNOWN_REVIEWS[`${axis.source_framework} → ${axis.target_framework}`]?.status === 'pending') count++
      }
    }
    return count
  })

  srcTotal(src: string): number {
    return (this.grouped()[src] ?? []).reduce((s, a) => s + a.count, 0)
  }

  axisReview(axis: AxisRow): KnownReview | undefined {
    return KNOWN_REVIEWS[`${axis.source_framework} → ${axis.target_framework}`]
  }

  fwLabel(code: string): string { return FW_LABEL[code] ?? code }
  fwColor(code: string): string { return fwColor(code) }
  sourceFile(code: string): string { return SOURCE_FILE[code] ?? 'crosswalk.json' }
}
