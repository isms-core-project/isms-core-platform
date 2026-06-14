import {
  Component, inject, signal, computed, effect,
  Input, OnChanges, SimpleChanges,
} from '@angular/core'
import { FormsModule } from '@angular/forms'
import { Router, ActivatedRoute } from '@angular/router'
import { toSignal } from '@angular/core/rxjs-interop'
import { firstValueFrom } from 'rxjs'

import { injectQuery } from '@tanstack/angular-query-experimental'

import { MatCardModule } from '@angular/material/card'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatButtonModule } from '@angular/material/button'
import { MatChipsModule } from '@angular/material/chips'
import { MatIconModule } from '@angular/material/icon'
import { MatSelectModule } from '@angular/material/select'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'

import { SearchApiService } from '../../api/search-api.service'
import { SearchResult } from '../../shared/types'
import { PageHeaderComponent } from '../../shared/components/page-header.component'
import { ThemeService } from '../../core/services/theme.service'

// ─── Highlight helper ─────────────────────────────────────────────────────────

interface HighlightPart { text: string; highlight: boolean }

function parseHighlight(html: string): HighlightPart[] {
  // Strip all tags except <mark> / </mark>
  const safe = html.replace(/<(?!\/?mark\b)[^>]+>/gi, '')
  const parts = safe.split(/(<mark>.*?<\/mark>)/gi)
  return parts.map(part => {
    const m = part.match(/^<mark>(.*)<\/mark>$/i)
    return m ? { text: m[1], highlight: true } : { text: part, highlight: false }
  })
}

// ─── Highlight Component ──────────────────────────────────────────────────────

@Component({
  selector: 'app-search-highlight',
  standalone: true,
  template: `
    @for (part of parts; track $index) {
      @if (part.highlight) {
        <mark class="highlight-mark">{{ part.text }}</mark>
      } @else {
        {{ part.text }}
      }
    }
  `,
  styles: [`
    :host {
      font-size: 0.8rem; line-height: 1.6;
      color: var(--mat-sys-on-surface-variant);
    }
    .highlight-mark {
      background: rgba(68,114,196,0.35); color: inherit;
      border-radius: 2px; padding: 0 2px;
    }
  `],
})
export class SearchHighlightComponent implements OnChanges {
  @Input() snippet = ''
  parts: HighlightPart[] = []

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['snippet']) {
      this.parts = parseHighlight(this.snippet)
    }
  }
}

// ─── Main Search Component ────────────────────────────────────────────────────

@Component({
  selector: 'app-search',
  standalone: true,
  imports: [
    FormsModule,
    MatCardModule, MatFormFieldModule, MatInputModule,
    MatButtonModule, MatChipsModule, MatIconModule,
    MatSelectModule, MatProgressSpinnerModule,
    PageHeaderComponent, SearchHighlightComponent,
  ],
  template: `
    <app-page-header
      title="Search"
      subtitle="Full-text search across policies and implementation guides" />

    <!-- Search bar -->
    <mat-card class="search-bar-card">
      <mat-card-content class="search-bar-content">
        <div class="search-row">
          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="search-query-field">
            <mat-label>Search policies, implementations…</mat-label>
            <mat-icon matPrefix>search</mat-icon>
            <input
              matInput
              [(ngModel)]="queryText"
              (keydown.enter)="submitSearch()"
              placeholder="e.g. access control, encryption, risk…"
            />
            @if (queryText) {
              <button matSuffix mat-icon-button (click)="clearSearch()">
                <mat-icon>clear</mat-icon>
              </button>
            }
          </mat-form-field>

          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="type-filter-field">
            <mat-label>Type</mat-label>
            <mat-select [ngModel]="docTypeFilter()" (ngModelChange)="docTypeFilter.set($event)">
              <mat-option value="">All types</mat-option>
              <mat-option value="policy">Policies</mat-option>
              <mat-option value="implementation">Implementations</mat-option>
            </mat-select>
          </mat-form-field>

          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="product-filter-field">
            <mat-label>Product</mat-label>
            <mat-select [ngModel]="productFilter()" (ngModelChange)="productFilter.set($event)">
              <mat-option value="">All products</mat-option>
              <mat-option value="framework">ISMS Framework</mat-option>
              <mat-option value="operational">ISMS Operational</mat-option>
              <mat-option value="privacy">Privacy (27701)</mat-option>
              <mat-option value="cloud">Cloud (27018)</mat-option>
            </mat-select>
          </mat-form-field>

          <button mat-raised-button color="primary" (click)="submitSearch()">
            <mat-icon>search</mat-icon>
            Search
          </button>
        </div>
      </mat-card-content>
    </mat-card>

    <!-- OpenSearch unavailable warning -->
    @if (!(statusQuery.data()?.available ?? true)) {
      <div class="warning-banner">
        <mat-icon class="warning-icon">warning</mat-icon>
        <span class="warning-text">
          OpenSearch is not available. Full-text search requires the OpenSearch container to be running.
          Retrying automatically every 15s.
        </span>
        <button mat-icon-button class="warning-refresh-btn" (click)="statusQuery.refetch()">
          <mat-icon class="icon-md">refresh</mat-icon>
        </button>
      </div>
    }

    <!-- Results count -->
    @if (submittedQuery() && !searchQuery.isLoading() && searchQuery.data()) {
      <div class="results-count-row">
        @if (searchQuery.data()!.available) {
          <span class="results-count-text">
            {{ searchQuery.data()!.total }} results for
            "<strong class="results-query-strong">{{ submittedQuery() }}</strong>"
            @if (searchQuery.data()!.took_ms != null) {
              &nbsp;— {{ searchQuery.data()!.took_ms }}ms
            }
          </span>
        } @else {
          <span class="results-count-text">
            OpenSearch not available — search is offline
          </span>
        }
      </div>
    }

    <!-- Loading skeletons -->
    @if (searchQuery.isLoading()) {
      @for (i of [1,2,3,4,5]; track i) {
        <mat-card class="skeleton-card">
          <mat-card-content>
            <div class="skel skel-sm skel-mb"></div>
            <div class="skel skel-md skel-mb"></div>
            <div class="skel skel-lg"></div>
          </mat-card-content>
        </mat-card>
      }
    }

    <!-- No results -->
    @if (!searchQuery.isLoading() && submittedQuery() && (searchQuery.data()?.hits?.length ?? 0) === 0 && !searchQuery.isLoading()) {
      <div class="info-banner">
        No results found for "<strong>{{ submittedQuery() }}</strong>". Try different keywords.
      </div>
    }

    <!-- Empty / prompt state -->
    @if (!submittedQuery() && !searchQuery.isLoading()) {
      <div class="empty-state">
        <mat-icon class="empty-state-icon">manage_search</mat-icon>
        <p class="empty-state-text">
          Enter a search term above and press Enter or click Search
        </p>
      </div>
    }

    <!-- Results -->
    @for (hit of searchQuery.data()?.hits ?? []; track hit.document_id) {
      <mat-card class="result-card">
        <mat-card-content class="result-card-content">
          <div class="result-header">
            <!-- Left: id + type chips + title -->
            <div class="result-left">
              <div class="result-id-row">
                <span class="doc-id">{{ hit.document_id }}</span>
                <span class="type-chip"
                  [style.background]="hit.type === 'policy' ? 'rgba(68,114,196,0.18)' : 'rgba(112,173,71,0.15)'"
                  [style.color]="hit.type === 'policy' ? 'var(--mat-sys-primary)' : (isDark() ? '#C6EFCE' : '#1b5e20')">
                  {{ hit.type }}
                </span>
                @if (hit.impl_type) {
                  <span class="type-chip type-chip--neutral">
                    {{ hit.impl_type }}
                  </span>
                }
              </div>
              <span class="result-title">{{ hit.title }}</span>
            </div>
            <!-- Right: group code + score -->
            <div class="result-right">
              @if (hit.control_group_code) {
                <span class="group-code">{{ hit.control_group_code }}</span>
              }
              <span class="score-text">score: {{ hit.score.toFixed(2) }}</span>
            </div>
          </div>

          <!-- Snippet with highlights -->
          @if (hit.snippet) {
            <div class="snippet-box">
              <app-search-highlight [snippet]="hit.snippet" />
            </div>
          }

          <!-- Navigation link -->
          @if (hit.control_group_code) {
            <div class="nav-link-row">
              <button mat-button class="nav-link-btn" (click)="viewInControls(hit)">
                <mat-icon class="icon-sm">open_in_new</mat-icon>
                View in Controls Library
              </button>
            </div>
          }
        </mat-card-content>
      </mat-card>
    }
  `,
  styles: [`
    :host { display: block; }

    /* Search bar card */
    .search-bar-card { margin-top: 16px; margin-bottom: 20px; }
    .search-bar-content { padding-bottom: 12px !important; }
    .search-row { display: flex; gap: 12px; align-items: flex-start; flex-wrap: wrap; }
    .search-query-field { flex: 1; min-width: 200px; }
    .type-filter-field { min-width: 150px; }
    .product-filter-field { min-width: 160px; }

    /* Warning banner */
    .warning-banner {
      display: flex; align-items: center;
      padding: 10px 14px; margin-bottom: 16px; border-radius: 6px;
      background: rgba(230,145,0,0.12); border: 1px solid rgba(230,145,0,0.35);
      color: var(--mat-sys-on-surface); font-size: 0.875rem;
    }
    .warning-icon { font-size: 20px; height: 20px; width: 20px; margin-right: 8px; flex-shrink: 0; }
    .warning-text { flex: 1; }
    .warning-refresh-btn { margin-left: 8px; }

    /* Results count */
    .results-count-row { margin-bottom: 12px; }
    .results-count-text { font-size: 0.875rem; color: var(--mat-sys-on-surface-variant); }
    .results-query-strong { color: var(--mat-sys-on-surface); }

    /* Skeletons */
    .skeleton-card { margin-bottom: 12px; }
    .skel-mb { margin-bottom: 6px; }

    .info-banner {
      padding: 10px 14px; border-radius: 6px; font-size: 0.875rem;
      background: rgba(68,114,196,0.1); border: 1px solid rgba(68,114,196,0.3);
    }
    .empty-state {
      text-align: center; padding: 60px 24px;
      color: var(--mat-sys-on-surface-variant);
    }
    .empty-state-icon { font-size: 52px; height: 52px; width: 52px; opacity: 0.25; }
    .empty-state-text { margin: 12px 0 0; color: var(--mat-sys-on-surface-variant); font-size: 0.875rem; }

    /* Result cards */
    .result-card { margin-bottom: 12px; }
    .result-card:last-child { margin-bottom: 0; }
    .result-card-content { padding-bottom: 12px !important; }

    .result-header {
      display: flex; justify-content: space-between;
      align-items: flex-start; margin-bottom: 4px; gap: 12px;
    }
    .result-left  { flex: 1; min-width: 0; }
    .result-right { flex-shrink: 0; text-align: right; }

    .result-id-row {
      display: flex; align-items: center; gap: 6px; margin-bottom: 3px; flex-wrap: wrap;
    }
    .doc-id {
      font-family: monospace; font-size: 0.72rem; font-weight: 700;
      color: var(--mat-sys-primary);
    }
    .result-title {
      display: block; font-weight: 600; font-size: 0.925rem; line-height: 1.35;
    }

    .type-chip {
      font-size: 0.65rem; height: 16px; line-height: 16px; padding: 0 6px;
      border-radius: 8px; display: inline-block; font-weight: 600;
    }
    .type-chip--neutral { background: var(--mat-sys-surface-variant); color: var(--mat-sys-on-surface-variant); }

    .group-code {
      display: block; font-family: monospace; font-size: 0.7rem;
      color: var(--mat-sys-on-surface-variant); margin-bottom: 2px;
    }
    .score-text {
      display: block; font-size: 0.68rem; color: var(--mat-sys-on-surface-variant);
    }

    .snippet-box {
      margin-top: 6px; padding: 8px 10px;
      background: rgba(68,114,196,0.05); border-radius: 4px;
      border-left: 2px solid rgba(68,114,196,0.3);
    }

    .nav-link-row { margin-top: 8px; }
    .nav-link-btn { font-size: 0.72rem; height: 24px; line-height: 24px; padding: 0 8px; min-width: 0; }

    .skel {
      height: 12px; border-radius: 6px;
      background: var(--mat-sys-surface-variant);
      animation: pulse 1.4s infinite;
    }
    .skel-sm { width: 40%; }
    .skel-md { width: 65%; }
    .skel-lg { width: 90%; }
    @keyframes pulse {
      0%, 100% { opacity: 0.5; }
      50%       { opacity: 1; }
    }
  `],
})
export class SearchComponent {
  private searchApi = inject(SearchApiService)
  private router    = inject(Router)
  private route     = inject(ActivatedRoute)
  private themeSvc  = inject(ThemeService)

  isDark = computed(() => this.themeSvc.isDark())

  // Read URL ?q= param as a signal
  private queryParams = toSignal(this.route.queryParamMap, { initialValue: null })

  // Local state
  queryText = ''

  // Signals drive reactivity for TanStack Query keys
  docTypeFilter  = signal('')
  productFilter  = signal('')
  submittedQuery = signal('')

  constructor() {
    // Sync URL ?q= param → local state on navigation
    effect(() => {
      const params = this.queryParams()
      if (!params) return
      const q = params.get('q') ?? ''
      if (q && q !== this.submittedQuery()) {
        this.queryText = q
        this.submittedQuery.set(q)
      }
    })
  }

  // OpenSearch availability probe — polls every 15s when unavailable
  statusQuery = injectQuery(() => ({
    queryKey: ['search', 'status'],
    queryFn: () => firstValueFrom(this.searchApi.status()),
    refetchInterval: (query: { state: { data?: { available?: boolean } } }) =>
      query.state.data?.available === false ? 15_000 : false,
  }))

  // Main search query — only runs when submittedQuery has ≥ 2 chars
  searchQuery = injectQuery(() => ({
    queryKey: ['search', 'results', this.submittedQuery(), this.docTypeFilter(), this.productFilter()],
    queryFn: () => firstValueFrom(this.searchApi.search({
      q:        this.submittedQuery(),
      doc_type: this.docTypeFilter() || undefined,
      product:  this.productFilter() || undefined,
      limit:    30,
    })),
    enabled: this.submittedQuery().length >= 2,
  }))

  submitSearch(): void {
    const q = this.queryText.trim()
    if (!q) return
    // Reflect in URL
    this.router.navigate([], {
      relativeTo: this.route,
      queryParams: { q },
      queryParamsHandling: 'merge',
    })
    this.submittedQuery.set(q)
  }

  clearSearch(): void {
    this.queryText = ''
    this.submittedQuery.set('')
    this.router.navigate([], {
      relativeTo: this.route,
      queryParams: { q: null },
      queryParamsHandling: 'merge',
    })
  }

  viewInControls(hit: SearchResult): void {
    if (hit.control_group_code) {
      this.router.navigate(['/controls'], {
        queryParams: { code: hit.control_group_code },
      })
    }
  }
}
