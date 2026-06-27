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

interface FrameworkRow {
  id: string
  code: string
  name: string
  version: string | null
  publisher: string | null
  source_url: string | null
  jurisdiction: string | null
  controls_count: number
  loaded_at: string
}

interface KnownUpdate {
  latest: string
  status: 'pending' | 'available'
  note: string
  eta?: string
}

interface CorpusStandardRow {
  standard: string
  title: string
  domain: string
  edition: string
  status: 'current' | 'pending'
  note?: string
  eta?: string
}

// ─── Static data ──────────────────────────────────────────────────────────────

const KNOWN_UPDATES: Record<string, KnownUpdate> = {
  ISO27017: {
    latest: '2025',
    status: 'pending',
    note: 'ISO/IEC 27017:2025 revision in progress — replaces 2015 edition. New control pack planned on release.',
    eta: 'TBD (delayed past June 2026)',
  },
}

const CORPUS_STANDARDS: CorpusStandardRow[] = [
  { standard: 'ISO/IEC 27000',       title: 'Information security management — Overview and vocabulary', domain: 'ISMS',            edition: 'FDIS (replacing 2018)', status: 'pending', note: 'FDIS ballot in progress — replaces ISO/IEC 27000:2018 with updated terminology aligned to ISO 27001:2022.', eta: 'TBD (delayed past June 2026)' },
  { standard: 'ISO/IEC 22123-1:2023', title: 'Cloud computing — Vocabulary',                              domain: 'Cloud Computing', edition: '2023',              status: 'current' },
  { standard: 'ISO/IEC 22123-2:2023', title: 'Cloud computing — Concepts',                                domain: 'Cloud Computing', edition: '2023',              status: 'current' },
  { standard: 'ISO/IEC 22123-3:2023', title: 'Cloud computing — Reference Architecture (CCRA)',           domain: 'Cloud Computing', edition: '2023',              status: 'current' },
  { standard: 'ISO/IEC 42001:2023',   title: 'AI management system (AIMS)',                               domain: 'AI Management',   edition: '2023',              status: 'current' },
  { standard: 'ISO/IEC 42005:2025',   title: 'AI system impact assessment',                               domain: 'AI Management',   edition: '2025',              status: 'current' },
  { standard: 'ISO/IEC 22989:2022',   title: 'AI concepts and terminology',                               domain: 'AI Management',   edition: '2022',              status: 'current' },
  { standard: 'ISO/IEC 19395:2015',   title: 'Smart data centre resource monitoring',                     domain: 'Infrastructure',  edition: '2015',              status: 'current' },
  { standard: 'ISO/IEC 30141:2024',   title: 'IoT reference architecture',                                domain: 'IoT',             edition: '2024',              status: 'current' },
  { standard: 'ISO/IEC 24091:2019',   title: 'Data centre storage power efficiency',                      domain: 'Infrastructure',  edition: '2019',              status: 'current' },
]

const DOMAIN_COLOR: Record<string, string> = {
  'ISMS':            '#455A64',
  'Cloud Computing': '#0288d1',
  'AI Management':   '#ff6b35',
  'Infrastructure':  '#00897b',
  'IoT':             '#6d4c41',
}

const JURISDICTION_LABEL: Record<string, string> = {
  INT: 'International', EU: 'European Union', US: 'United States',
  DE: 'Germany', CH: 'Switzerland', GB: 'United Kingdom',
  BE: 'Belgium', LU: 'Luxembourg', IT: 'Italy', FR: 'France', AT: 'Austria',
}

const JURISDICTION_COLOR: Record<string, string> = {
  INT: '#455A64', EU: '#1565C0', US: '#B71C1C', DE: '#4E342E',
  CH:  '#C62828', GB: '#1A237E', BE: '#1B5E20', LU: '#4A148C',
  IT:  '#006630', FR: '#0D47A1', AT: '#E65100',
}

const JURISDICTION_ORDER = ['INT', 'EU', 'US', 'CH', 'DE', 'GB', 'BE', 'LU', 'IT', 'FR', 'AT']

function jurisColor(j: string | null): string {
  return JURISDICTION_COLOR[j ?? 'INT'] ?? '#455A64'
}

function fmtDate(iso: string): string {
  return new Date(iso).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' })
}

// ─── Component ────────────────────────────────────────────────────────────────

@Component({
  selector: 'app-framework-tracker',
  standalone: true,
  imports: [
    MatCardModule, MatTableModule, MatTooltipModule,
    MatIconModule, MatProgressSpinnerModule, MatChipsModule,
    PageHeaderComponent,
  ],
  template: `
    <div class="page-wrap">
      <app-page-header
        title="Framework Version Tracker"
        subtitle="Loaded compliance dataset versions, update availability, and dataset health" />

      <!-- Summary cards -->
      <div class="summary-row">
        @if (fwQuery.isLoading()) {
          @for (i of [1,2,3,4]; track i) {
            <div class="summary-skel"></div>
          }
        } @else {
          <mat-card class="summary-card">
            <mat-card-content>
              <span class="card-label">Frameworks loaded</span>
              <span class="card-value">{{ fwQuery.data()?.length ?? 0 }}</span>
            </mat-card-content>
          </mat-card>
          <mat-card class="summary-card">
            <mat-card-content>
              <span class="card-label">Total controls</span>
              <span class="card-value">{{ totalControls().toLocaleString() }}</span>
            </mat-card-content>
          </mat-card>
          <mat-card class="summary-card">
            <mat-card-content>
              <span class="card-label">Updates available</span>
              <span class="card-value"
                [style.color]="updateCount() > 0 ? '#FF9800' : '#4CAF50'">{{ updateCount() }}</span>
              <span class="card-sub">datasets behind latest release</span>
            </mat-card-content>
          </mat-card>
          <mat-card class="summary-card">
            <mat-card-content>
              <span class="card-label">Pending releases</span>
              <span class="card-value"
                [style.color]="pendingCount() > 0 ? '#42A5F5' : '#9E9E9E'">{{ pendingCount() }}</span>
              <span class="card-sub">upcoming versions to watch</span>
            </mat-card-content>
          </mat-card>
        }
      </div>

      <!-- Loading skeleton for table -->
      @if (fwQuery.isLoading()) {
        <div class="table-skel"></div>
      }

      <!-- Per-jurisdiction tables -->
      @if (!fwQuery.isLoading() && fwQuery.data()) {
        @for (j of visibleJurisdictions(); track j) {
          <div class="juris-section">
            <div class="juris-header">
              <div class="juris-bar" [style.background]="jurisColor(j)"></div>
              <span class="juris-label" [style.color]="jurisColor(j)">
                {{ jurisdictionLabel(j) }}
              </span>
              <span class="juris-count">
                ({{ grouped()[j]?.length }} framework{{ grouped()[j]?.length !== 1 ? 's' : '' }})
              </span>
            </div>

            <div class="table-container">
              <table mat-table [dataSource]="grouped()[j] ?? []" class="full-table">

                <!-- Framework column -->
                <ng-container matColumnDef="framework">
                  <th mat-header-cell *matHeaderCellDef class="col-header">Framework</th>
                  <td mat-cell *matCellDef="let fw">
                    <div class="fw-name-row">
                      <span class="fw-name">{{ fw.name }}</span>
                      @if (fw.source_url) {
                        <mat-icon
                          class="icon-sm icon-link"
                          [matTooltip]="fw.source_url"
                          (click)="openUrl(fw.source_url)">open_in_new</mat-icon>
                      }
                    </div>
                    <span class="fw-code">{{ fw.code }}</span>
                  </td>
                </ng-container>

                <!-- Version column -->
                <ng-container matColumnDef="version">
                  <th mat-header-cell *matHeaderCellDef class="col-header">Version</th>
                  <td mat-cell *matCellDef="let fw">
                    <span class="mono-text">{{ fw.version ?? '—' }}</span>
                  </td>
                </ng-container>

                <!-- Controls column -->
                <ng-container matColumnDef="controls">
                  <th mat-header-cell *matHeaderCellDef class="col-header col-right">Controls</th>
                  <td mat-cell *matCellDef="let fw" class="col-right">
                    <span class="controls-count">{{ fw.controls_count.toLocaleString() }}</span>
                  </td>
                </ng-container>

                <!-- Publisher column -->
                <ng-container matColumnDef="publisher">
                  <th mat-header-cell *matHeaderCellDef class="col-header">Publisher</th>
                  <td mat-cell *matCellDef="let fw">
                    <span class="dim-text">{{ fw.publisher ?? '—' }}</span>
                  </td>
                </ng-container>

                <!-- Loaded column -->
                <ng-container matColumnDef="loaded">
                  <th mat-header-cell *matHeaderCellDef class="col-header">Loaded</th>
                  <td mat-cell *matCellDef="let fw">
                    <span class="dim-text">{{ fmtDate(fw.loaded_at) }}</span>
                  </td>
                </ng-container>

                <!-- Status column -->
                <ng-container matColumnDef="status">
                  <th mat-header-cell *matHeaderCellDef class="col-header">Status</th>
                  <td mat-cell *matCellDef="let fw">
                    @if (!knownUpdate(fw.code)) {
                      <span class="chip chip-current">
                        <mat-icon class="icon-xs icon-inline">check_circle</mat-icon>
                        Current
                      </span>
                    }
                    @if (knownUpdate(fw.code)?.status === 'available') {
                      <span class="chip chip-warn" [matTooltip]="knownUpdate(fw.code)!.note">
                        <mat-icon class="icon-xs icon-inline">warning</mat-icon>
                        Update: {{ knownUpdate(fw.code)!.latest }}
                      </span>
                    }
                    @if (knownUpdate(fw.code)?.status === 'pending') {
                      <span class="chip chip-pending"
                        [matTooltip]="knownUpdate(fw.code)!.note + (knownUpdate(fw.code)!.eta ? ' ETA: ' + knownUpdate(fw.code)!.eta : '')">
                        <mat-icon class="icon-xs icon-inline">update</mat-icon>
                        Pending: {{ knownUpdate(fw.code)!.latest }}{{ knownUpdate(fw.code)!.eta ? ' (' + knownUpdate(fw.code)!.eta + ')' : '' }}
                      </span>
                    }
                  </td>
                </ng-container>

                <tr mat-header-row *matHeaderRowDef="fwColumns"></tr>
                <tr mat-row *matRowDef="let row; columns: fwColumns" class="hover-row"></tr>
              </table>
            </div>
          </div>
        }
      }

      <!-- ISO Reference Corpus -->
      <div class="corpus-section">
        <div class="corpus-heading">ISO Reference Corpus &amp; Glossary Standards</div>
        <div class="corpus-subtitle">
          ISO/IEC normative texts indexed in the reference corpus and exposed via the Glossary page.
        </div>

        <div class="table-container">
          <table mat-table [dataSource]="corpusStandards" class="full-table">

            <!-- Standard -->
            <ng-container matColumnDef="standard">
              <th mat-header-cell *matHeaderCellDef class="col-header">Standard</th>
              <td mat-cell *matCellDef="let s">
                <span class="std-code">{{ s.standard }}</span>
              </td>
            </ng-container>

            <!-- Title -->
            <ng-container matColumnDef="title">
              <th mat-header-cell *matHeaderCellDef class="col-header">Title</th>
              <td mat-cell *matCellDef="let s">
                <span class="std-title">{{ s.title }}</span>
              </td>
            </ng-container>

            <!-- Domain -->
            <ng-container matColumnDef="domain">
              <th mat-header-cell *matHeaderCellDef class="col-header">Domain</th>
              <td mat-cell *matCellDef="let s">
                <span class="domain-chip"
                  [style.background]="domainColor(s.domain) + '22'"
                  [style.color]="domainColor(s.domain)">
                  {{ s.domain }}
                </span>
              </td>
            </ng-container>

            <!-- Edition -->
            <ng-container matColumnDef="edition">
              <th mat-header-cell *matHeaderCellDef class="col-header">Edition</th>
              <td mat-cell *matCellDef="let s">
                <span class="mono-text">{{ s.edition }}</span>
              </td>
            </ng-container>

            <!-- Status -->
            <ng-container matColumnDef="status">
              <th mat-header-cell *matHeaderCellDef class="col-header">Status</th>
              <td mat-cell *matCellDef="let s">
                @if (s.status === 'current') {
                  <span class="chip chip-current">
                    <mat-icon class="icon-xs icon-inline">check_circle</mat-icon>
                    Current
                  </span>
                }
                @if (s.status === 'pending') {
                  <span class="chip chip-pending"
                    [matTooltip]="(s.note ?? '') + (s.eta ? ' ETA: ' + s.eta : '')">
                    <mat-icon class="icon-xs icon-inline">update</mat-icon>
                    Pending{{ s.eta ? ' (' + s.eta + ')' : '' }}
                  </span>
                }
              </td>
            </ng-container>

            <tr mat-header-row *matHeaderRowDef="corpusColumns"></tr>
            <tr mat-row *matRowDef="let row; columns: corpusColumns" class="hover-row"></tr>
          </table>
        </div>
      </div>

      <div class="footer-note">
        <mat-icon class="icon-xs">info</mat-icon>
        Compliance datasets loaded from <code>datasets/data/*.json</code> on backend startup.
        ISO corpus seed files live in <code>datasets/data/iso-reference/</code>.
        Update availability tracked in <code>FrameworkTracker</code> → <code>KNOWN_UPDATES</code> and <code>CORPUS_STANDARDS</code>.
      </div>
    </div>
  `,
  styles: [`
    :host { display: block; }

    .page-wrap { padding: 24px; max-width: 1200px; }

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

    .juris-section { margin-bottom: 24px; }
    .juris-header { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; }
    .juris-count { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
    .juris-bar { width: 4px; height: 20px; border-radius: 2px; }
    .juris-label { font-size: 0.8rem; font-weight: 700; }

    .full-table { width: 100%; }

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
    .col-right { text-align: right; }
    .hover-row:hover { background: var(--mat-sys-surface-variant); }
    .hover-row:last-child td { border-bottom: none; }

    .fw-name-row { display: flex; align-items: center; gap: 6px; }
    .fw-name { display: block; font-weight: 600; font-size: 0.78rem; }
    .fw-code { display: block; font-size: 0.62rem; color: var(--mat-sys-on-surface-variant); font-family: monospace; }
    .mono-text { font-family: monospace; font-size: 0.75rem; }
    .dim-text { font-size: 0.7rem; color: var(--mat-sys-on-surface-variant); }
    .controls-count { font-size: 0.75rem; font-weight: 600; }

    .icon-xs { font-size: 11px !important; height: 11px !important; width: 11px !important; line-height: 11px !important; }
    .icon-inline { vertical-align: middle; margin-right: 3px; }
    .icon-link { color: var(--mat-sys-on-surface-variant); cursor: pointer; }

    .chip {
      display: inline-flex; align-items: center;
      height: 18px; padding: 0 6px; border-radius: 9px;
      font-size: 0.6rem; font-weight: 600; white-space: nowrap;
    }
    .chip-current { background: rgba(0,199,82,0.1); color: #00c752; }
    .chip-warn    { background: rgba(255,152,0,0.1);  color: #FF9800; }
    .chip-pending { background: rgba(66,165,245,0.1); color: #42A5F5; }

    .domain-chip {
      display: inline-block; height: 18px; line-height: 18px;
      padding: 0 6px; border-radius: 9px;
      font-size: 0.6rem; font-weight: 600;
    }

    .corpus-section { margin-top: 32px; margin-bottom: 8px; }
    .corpus-heading { font-size: 0.95rem; font-weight: 700; margin-bottom: 4px; }
    .corpus-subtitle { font-size: 0.78rem; color: var(--mat-sys-on-surface-variant); margin-bottom: 16px; }
    .std-code { font-family: monospace; font-weight: 600; font-size: 0.78rem; }
    .std-title { font-size: 0.75rem; }

    .footer-note {
      font-size: 0.62rem; color: var(--mat-sys-on-surface-variant);
      margin-top: 16px; display: flex; align-items: center; gap: 4px;
    }
  `],
})
export class FrameworkTrackerComponent {
  private http = inject(HttpClient)

  readonly fwColumns = ['framework', 'version', 'controls', 'publisher', 'loaded', 'status']
  readonly corpusColumns = ['standard', 'title', 'domain', 'edition', 'status']
  readonly corpusStandards = CORPUS_STANDARDS

  fwQuery = injectQuery(() => ({
    queryKey: ['framework-tracker'],
    queryFn: () => firstValueFrom(this.http.get<FrameworkRow[]>('/api/v1/frameworks/')),
  }))

  grouped = computed((): Record<string, FrameworkRow[]> => {
    const fws = this.fwQuery.data() ?? []
    const g: Record<string, FrameworkRow[]> = {}
    for (const fw of fws) {
      const raw = fw.jurisdiction ?? 'INT'
      const j = (raw === 'Global' || raw === 'global') ? 'INT' : raw
      if (!g[j]) g[j] = []
      g[j].push(fw)
    }
    return g
  })

  visibleJurisdictions = computed(() =>
    JURISDICTION_ORDER.filter(j => (this.grouped()[j]?.length ?? 0) > 0)
  )

  totalControls = computed(() =>
    (this.fwQuery.data() ?? []).reduce((sum, fw) => sum + fw.controls_count, 0)
  )

  updateCount = computed(() =>
    (this.fwQuery.data() ?? []).filter(fw => KNOWN_UPDATES[fw.code]?.status === 'available').length
  )

  pendingCount = computed(() =>
    (this.fwQuery.data() ?? []).filter(fw => KNOWN_UPDATES[fw.code]?.status === 'pending').length
  )

  knownUpdate(code: string): KnownUpdate | undefined {
    return KNOWN_UPDATES[code]
  }

  jurisColor(j: string): string { return jurisColor(j) }
  jurisdictionLabel(j: string): string { return JURISDICTION_LABEL[j] ?? j }
  fmtDate(iso: string): string { return fmtDate(iso) }
  domainColor(d: string): string { return DOMAIN_COLOR[d] ?? '#455A64' }

  openUrl(url: string | null): void {
    if (url) window.open(url, '_blank')
  }
}
