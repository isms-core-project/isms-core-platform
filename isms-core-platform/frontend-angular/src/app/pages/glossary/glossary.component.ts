import { Component, inject, signal, computed } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { HttpClient } from '@angular/common/http'
import { firstValueFrom } from 'rxjs'

import { injectQuery } from '@tanstack/angular-query-experimental'

import { MatCardModule } from '@angular/material/card'
import { MatButtonModule } from '@angular/material/button'
import { MatIconModule } from '@angular/material/icon'
import { MatChipsModule } from '@angular/material/chips'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatTabsModule } from '@angular/material/tabs'

import { PageHeaderComponent } from '../../shared/components/page-header.component'
import { ThemeService } from '../../core/services/theme.service'
import { TokenStoreService } from '../../core/services/token-store.service'

// ── Types ─────────────────────────────────────────────────────────────────────

interface RemoteGlossaryEntry {
  clause_id: string
  title: string
  text: string
}

interface RemoteGlossaryResponse {
  standard: string
  part: string
  query: string | null
  entries: RemoteGlossaryEntry[]
  results_text?: string
}

// ── Constants ─────────────────────────────────────────────────────────────────

const CLOUD_ACCENT  = '#0288d1'
const AI_ACCENT     = '#ff6b35'
const INFRA_ACCENT  = '#00897b'

type Domain = 'cloud' | 'ai' | 'infrastructure'

const CLOUD_PARTS = [
  { key: 'vocabulary',   label: 'Vocabulary',   subtitle: 'ISO/IEC 22123-1:2023 — Terms and definitions' },
  { key: 'concepts',     label: 'Concepts',     subtitle: 'ISO/IEC 22123-2:2023 — Cloud computing concepts' },
  { key: 'architecture', label: 'Architecture', subtitle: 'ISO/IEC 22123-3:2023 — Cloud Computing Reference Architecture (CCRA)' },
]
const AI_PARTS = [
  { key: 'iso42001', label: 'ISO 42001:2023', subtitle: 'ISO/IEC 42001:2023 — AI Management System — Terms and definitions (Clause 3, 26 terms)' },
  { key: 'iso42005', label: 'ISO 42005:2025', subtitle: 'ISO/IEC 42005:2025 — AI System Impact Assessment — Terms and definitions (9 terms + abbreviated terms)' },
  { key: 'iso22989', label: 'ISO 22989:2022', subtitle: 'ISO/IEC 22989:2022 — AI Concepts and Terminology — 117 terms across 7 categories' },
]
const INFRA_PARTS = [
  { key: 'iso19395', label: 'ISO 19395:2015', subtitle: 'ISO/IEC 19395:2015 — Smart Data Centre Resource Monitoring — Terms, acronyms, and domain taxonomy' },
  { key: 'iso30141', label: 'ISO 30141:2024', subtitle: 'ISO/IEC 30141:2024 — IoT Reference Architecture' },
  { key: 'iso24091', label: 'ISO 24091:2019', subtitle: 'ISO/IEC 24091:2019 — Data Centre Storage Power Efficiency' },
]

const DOMAIN_CONFIG: Record<Domain, { accent: string; icon: string; label: string; parts: typeof CLOUD_PARTS; defaultPart: string }> = {
  cloud:          { accent: CLOUD_ACCENT,  icon: 'cloud',       label: 'Cloud Computing',     parts: CLOUD_PARTS,  defaultPart: 'vocabulary' },
  ai:             { accent: AI_ACCENT,     icon: 'psychology',  label: 'AI Management System', parts: AI_PARTS,     defaultPart: 'iso42001' },
  infrastructure: { accent: INFRA_ACCENT,  icon: 'dns',         label: 'Infrastructure & IoT', parts: INFRA_PARTS,  defaultPart: 'iso19395' },
}

// ── Component ─────────────────────────────────────────────────────────────────

@Component({
  selector: 'app-glossary',
  standalone: true,
  imports: [
    FormsModule,
    MatCardModule, MatButtonModule, MatIconModule, MatChipsModule,
    MatFormFieldModule, MatInputModule, MatProgressSpinnerModule, MatTabsModule,
    PageHeaderComponent,
  ],
  template: `
<div class="glossary-page">
  <app-page-header
    title="Glossary"
    subtitle="ISO/IEC standard terminology — Cloud (ISO 22123), AI (ISO 42001 · ISO 42005 · ISO 22989), Infrastructure & IoT (ISO 19395 · ISO 30141 · ISO 24091)">
  </app-page-header>

  <!-- Domain selector tabs -->
  <div class="glossary-domains">
    @for (d of domains; track d.key) {
      <div class="glossary-domain-tab"
        [class.active]="activeDomain() === d.key"
        [style.border-bottom-color]="activeDomain() === d.key ? d.accent : 'transparent'"
        [style.color]="activeDomain() === d.key ? d.accent : null"
        (click)="activeDomain.set(d.key)">
        <mat-icon class="glossary-tab-icon">{{ d.icon }}</mat-icon>
        {{ d.label }}
      </div>
    }
  </div>

  <!-- Part sub-tabs -->
  @let cfg = domainConfig();
  <div class="glossary-parts">
    @for (p of cfg.parts; track p.key) {
      <div class="glossary-part-tab"
        [class.active]="activePart() === p.key"
        [style.border-bottom-color]="activePart() === p.key ? cfg.accent : 'transparent'"
        [style.color]="activePart() === p.key ? cfg.accent : null"
        (click)="activePart.set(p.key); clearSearch()">
        {{ p.label }}
      </div>
    }
  </div>

  <!-- Subtitle -->
  <div class="glossary-subtitle">{{ currentSubtitle() }}</div>

  <!-- Search bar -->
  <form (submit)="onSearch($event)" class="glossary-search">
    <mat-form-field appearance="outline" class="glossary-search-field" subscriptSizing="dynamic">
      <mat-label>Search terms…</mat-label>
      <input matInput [(ngModel)]="searchInput" name="q" placeholder="e.g. encryption, data subject">
      <mat-icon matSuffix class="glossary-search-icon">search</mat-icon>
    </mat-form-field>
    <button mat-flat-button type="submit" [style.background]="cfg.accent" class="glossary-search-btn">
      Search
    </button>
  </form>

  @if (activeQuery()) {
    <div class="glossary-query-row">
      <span class="glossary-results-for">Results for:</span>
      <div class="glossary-query-badge"
        [style.background]="cfg.accent + '20'"
        [style.color]="cfg.accent">
        {{ activeQuery() }}
        <mat-icon class="glossary-close-icon" (click)="clearSearch()">close</mat-icon>
      </div>
    </div>
  }

  <!-- Loading -->
  @if (glossaryQuery.isLoading()) {
    <div class="glossary-loading">
      <mat-spinner [diameter]="28" [style.color]="cfg.accent"></mat-spinner>
    </div>
  }

  <!-- Error -->
  @if (glossaryQuery.isError()) {
    <div class="glossary-error">
      Failed to load glossary data.
    </div>
  }

  <!-- Search results text -->
  @if (glossaryQuery.data() && activeQuery() && glossaryQuery.data()!.results_text) {
    <div class="glossary-results-text">
      <div class="glossary-results-label" [style.color]="cfg.accent">
        Search results — {{ glossaryQuery.data()!.standard }}
      </div>
      <div class="glossary-results-body">
        {{ glossaryQuery.data()!.results_text }}
      </div>
    </div>
  }

  <!-- Entry list -->
  @if (glossaryQuery.data() && !glossaryQuery.data()!.results_text) {
    @let entries = glossaryQuery.data()!.entries;
    <div class="glossary-count">
      <div class="glossary-count-badge"
        [style.background]="cfg.accent + '20'"
        [style.color]="cfg.accent">
        {{ entries.length }} entries
      </div>
      <div class="glossary-count-sep"></div>
      <span class="glossary-std-label">{{ glossaryQuery.data()!.standard }}</span>
    </div>

    <div class="glossary-entries">
      @for (entry of entries; track entry.clause_id) {
        <div class="glossary-entry"
          [class.hovered]="hoveredEntry() === entry.clause_id"
          [style.--entry-accent]="cfg.accent"
          (mouseenter)="hoveredEntry.set(entry.clause_id)"
          (mouseleave)="hoveredEntry.set(null)">
          <div class="glossary-entry-header">
            <span class="glossary-clause-badge"
              [style.background]="cfg.accent + '20'"
              [style.color]="cfg.accent"
              [style.border-color]="cfg.accent + '40'">
              {{ entry.clause_id }}
            </span>
            <span class="glossary-entry-title">{{ entry.title }}</span>
          </div>
          <div class="glossary-entry-text">{{ entry.text }}</div>
        </div>
      }
    </div>

    @if (entries.length === 0) {
      <div class="glossary-empty">No entries found.</div>
    }
  }
</div>
`,
  styles: [`
    :host { display: block; }

    .glossary-page {
      padding: 0 4px;
      max-width: 1100px;
      display: flex;
      flex-direction: column;
      gap: 0;
    }

    .glossary-domains {
      display: flex;
      border-bottom: 1px solid var(--mat-sys-outline-variant);
      margin-bottom: 24px;
    }

    .glossary-domain-tab {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 8px 16px;
      cursor: pointer;
      font-size: .85rem;
      opacity: 0.6;
      border-bottom: 2px solid transparent;
      transition: opacity .15s;
    }
    .glossary-domain-tab.active {
      opacity: 1;
      font-weight: 600;
    }

    .glossary-parts {
      display: flex;
      border-bottom: 1px solid var(--mat-sys-outline-variant);
      margin-bottom: 12px;
    }

    .glossary-part-tab {
      padding: 6px 14px;
      cursor: pointer;
      font-size: .82rem;
      opacity: 0.6;
      border-bottom: 2px solid transparent;
    }
    .glossary-part-tab.active {
      opacity: 1;
    }

    .glossary-subtitle {
      font-size: .72rem;
      opacity: .5;
      margin-bottom: 16px;
    }

    .glossary-search {
      display: flex;
      gap: 8px;
      margin-bottom: 20px;
      align-items: flex-start;
    }
    .glossary-search-field {
      flex: 1;
      max-width: 480px;
    }
    .glossary-search-btn {
      color: var(--mat-sys-on-surface);
      align-self: flex-start;
      margin-top: 4px;
    }

    .glossary-query-row {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 16px;
    }
    .glossary-query-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 2px 10px;
      border-radius: 12px;
      font-size: .8rem;
    }

    .glossary-count {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 16px;
    }
    .glossary-count-badge {
      padding: 2px 10px;
      border-radius: 12px;
      font-size: .72rem;
    }
    .glossary-count-sep {
      width: 1px;
      height: 16px;
      background: rgba(0,0,0,0.08);
    }
    .glossary-std-label {
      font-size: .72rem;
      opacity: .4;
    }

    .glossary-entries {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .glossary-entry {
      padding: 16px;
      border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 6px;
      background: rgba(0,0,0,.15);
      transition: border-color .15s;
    }
    .glossary-entry.hovered {
      border-color: var(--entry-accent, #327df4);
    }

    .glossary-entry-header {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 6px;
    }

    .glossary-clause-badge {
      font-family: monospace;
      font-size: .68rem;
      font-weight: 600;
      padding: 0 6px;
      height: 18px;
      border-radius: 9px;
      display: inline-flex;
      align-items: center;
      border: 1px solid;
    }

    .glossary-entry-title {
      font-weight: 600;
      font-size: .88rem;
    }

    .glossary-entry-text {
      font-size: .82rem;
      opacity: .7;
      line-height: 1.6;
      white-space: pre-line;
    }

    .glossary-results-text {
      padding: 20px;
      background: rgba(0,0,0,.2);
      border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 6px;
    }
    .glossary-results-label {
      font-size: .72rem;
      font-weight: 600;
      margin-bottom: 8px;
    }
    .glossary-results-body {
      font-size: .82rem;
      opacity: .75;
      line-height: 1.7;
      white-space: pre-line;
    }

    .glossary-empty {
      text-align: center;
      padding: 40px;
      opacity: .4;
      font-size: .88rem;
    }

    .glossary-tab-icon {
      font-size: 16px;
      width: 16px;
      height: 16px;
    }

    .glossary-search-icon {
      opacity: .4;
    }

    .glossary-close-icon {
      font-size: 14px;
      cursor: pointer;
    }

    .glossary-results-for {
      font-size: .82rem;
      opacity: .6;
    }

    .glossary-loading {
      display: flex;
      justify-content: center;
      padding: 48px;
    }

    .glossary-error {
      color: #f44336;
      padding: 12px;
      background: rgba(244,67,54,.1);
      border-radius: 6px;
    }
  `],
})
export class GlossaryComponent {
  private theme      = inject(ThemeService)
  private tokenStore = inject(TokenStoreService)
  private http       = inject(HttpClient)

  // ── State ──────────────────────────────────────────────────────────────────
  activeDomain  = signal<Domain>('cloud')
  activePart    = signal<string>('vocabulary')
  searchInput   = ''
  activeQuery   = signal<string>('')
  hoveredEntry  = signal<string | null>(null)

  readonly domains: { key: Domain; accent: string; icon: string; label: string }[] = [
    { key: 'cloud',          accent: CLOUD_ACCENT,  icon: 'cloud',      label: 'Cloud Computing'      },
    { key: 'ai',             accent: AI_ACCENT,     icon: 'psychology', label: 'AI Management System' },
    { key: 'infrastructure', accent: INFRA_ACCENT,  icon: 'dns',        label: 'Infrastructure & IoT' },
  ]

  // ── Computed ───────────────────────────────────────────────────────────────
  domainConfig = computed(() => DOMAIN_CONFIG[this.activeDomain()])

  currentSubtitle = computed((): string => {
    const cfg = this.domainConfig()
    return cfg.parts.find(p => p.key === this.activePart())?.subtitle ?? ''
  })

  // ── Query ──────────────────────────────────────────────────────────────────
  glossaryQuery = injectQuery(() => ({
    queryKey: ['glossary', this.activeDomain(), this.activePart(), this.activeQuery()],
    queryFn: () => {
      const domain = this.activeDomain()
      const q = this.activeQuery()
      const params: Record<string, string> = { part: this.activePart() }
      if (q) params['q'] = q
      return firstValueFrom(
        this.http.get<RemoteGlossaryResponse>(`/api/v1/glossary/${domain}`, { params })
      )
    },
    staleTime: 5 * 60_000,
  }))

  // ── Actions ────────────────────────────────────────────────────────────────
  onSearch(e: Event): void {
    e.preventDefault()
    this.activeQuery.set(this.searchInput.trim())
  }

  clearSearch(): void {
    this.activeQuery.set('')
    this.searchInput = ''
  }
}
