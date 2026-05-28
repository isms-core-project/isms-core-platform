import { Component, inject, computed } from '@angular/core'
import { ActivatedRoute, Router } from '@angular/router'
import { firstValueFrom } from 'rxjs'

import { injectQuery } from '@tanstack/angular-query-experimental'

import { MatCardModule } from '@angular/material/card'
import { MatTableModule } from '@angular/material/table'
import { MatButtonModule } from '@angular/material/button'
import { MatIconModule } from '@angular/material/icon'
import { MatChipsModule } from '@angular/material/chips'
import { MatProgressBarModule } from '@angular/material/progress-bar'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatTooltipModule } from '@angular/material/tooltip'

import { ControlsApiService, FrameworkControlDetail } from '../../api/controls-api.service'
import { ProductService, PRODUCT_COLORS, PRODUCT_SUBTITLES } from '../../core/services/product.service'
import { ThemeService } from '../../core/services/theme.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

// ── Confidence colour helpers ─────────────────────────────────────────────────

function confidenceColorDark(c: number): { bg: string; color: string } {
  if (c >= 0.8) return { bg: 'rgba(198,239,206,0.15)', color: '#C6EFCE' }
  if (c >= 0.6) return { bg: 'rgba(255,235,156,0.12)', color: '#FFEB9C' }
  return { bg: 'rgba(255,199,206,0.12)', color: '#FFC7CE' }
}

function confidenceColorLight(c: number): { bg: string; color: string } {
  if (c >= 0.8) return { bg: 'rgba(27,94,32,0.1)', color: '#1b5e20' }
  if (c >= 0.6) return { bg: 'rgba(154,101,0,0.1)', color: '#9a6500' }
  return { bg: 'rgba(158,0,0,0.1)', color: '#9e0000' }
}

const SECTION_LABELS: Record<string, string> = {
  'A.1': 'PII Controller',
  'A.2': 'PII Processor',
  'A.3': 'Shared (Both)',
  'CLD.6': 'People Controls',
  'CLD.8': 'Asset Controls',
  'CLD.9': 'Access Controls',
  'CLD.12': 'Operations Controls',
  'CLD.13': 'Network Controls',
  'CSP': 'Cloud Service Provider',
  'CSC': 'Cloud Service Customer',
}

// ─────────────────────────────────────────────────────────────────────────────

@Component({
  selector: 'app-framework-control-detail',
  standalone: true,
  imports: [
    MatCardModule, MatTableModule,
    MatButtonModule, MatIconModule, MatChipsModule,
    MatProgressBarModule, MatProgressSpinnerModule, MatTooltipModule,
    PageHeaderComponent,
  ],
  template: `
<div class="fcd-page">

  <!-- Back row -->
  <div class="fcd-back-row">
    <button mat-icon-button (click)="goBack()">
      <mat-icon>arrow_back</mat-icon>
    </button>
    <span class="fcd-back-row__label">
      {{ productSubtitle() }}{{ ctrl() ? ' · ' + ctrl()!.framework_name : '' }}
    </span>
  </div>

  <!-- Loading -->
  @if (ctrlQuery.isLoading()) {
    <div class="fcd-loading">
      <app-page-header title="Control Detail" subtitle="Loading…" />
      <mat-card><mat-card-content>
        <div class="fcd-skeleton"></div>
      </mat-card-content></mat-card>
    </div>
  }

  <!-- Error -->
  @if (ctrlQuery.isError()) {
    <div>
      <app-page-header title="Control Detail" />
      <div class="fcd-error">Control not found or failed to load.</div>
    </div>
  }

  @if (ctrlQuery.isSuccess() && ctrl()) {
    <app-page-header [title]="ctrl()!.control_id" [subtitle]="ctrl()!.title" />

    <div class="fcd-top-row">

      <!-- Control info card -->
      <mat-card class="fcd-info-card" [style.border-left]="'3px solid ' + productColor()">
        <mat-card-content>
          <div class="fcd-info-card__subtitle">Control Details</div>

          <div class="fcd-info-card__chips">
            <mat-chip-set>
              <mat-chip [style.background]="productColor() + '20'" [style.color]="productColor()">
                {{ ctrl()!.framework_name }}
              </mat-chip>
              <mat-chip class="fcd-chip--section">{{ sectionLabel() }}</mat-chip>
            </mat-chip-set>
          </div>

          @if (ctrl()!.description) {
            <div class="fcd-info-card__desc">{{ ctrl()!.description }}</div>
          }

          @if (ctrl()!.control_type.length > 0) {
            <div class="fcd-info-card__block">
              <div class="fcd-info-card__lbl">Control Type</div>
              <div class="fcd-info-card__chips">
                <mat-chip-set>
                  @for (t of ctrl()!.control_type; track t) {
                    <mat-chip [style.background]="productColor() + '15'" [style.color]="productColor()">
                      {{ t }}
                    </mat-chip>
                  }
                </mat-chip-set>
              </div>
            </div>
          }

          @if (ctrl()!.security_properties.length > 0) {
            <div class="fcd-info-card__block">
              <div class="fcd-info-card__lbl">Security Properties</div>
              <div class="fcd-info-card__chips">
                <mat-chip-set>
                  @for (p of ctrl()!.security_properties; track p) {
                    <mat-chip class="fcd-chip--sec-prop">{{ p }}</mat-chip>
                  }
                </mat-chip-set>
              </div>
            </div>
          }
        </mat-card-content>
      </mat-card>

      <!-- Mapping summary card -->
      <mat-card class="fcd-summary-card">
        <mat-card-content>
          <div class="fcd-info-card__subtitle">Mappings</div>
          <div class="fcd-summary-card__count" [style.color]="productColor()">
            {{ ctrl()!.mappings.length }}
          </div>
          <div class="fcd-summary-card__sub">
            across {{ frameworkCount() }} framework{{ frameworkCount() !== 1 ? 's' : '' }}
          </div>
        </mat-card-content>
      </mat-card>

    </div>

    <!-- Mappings table -->
    @if (ctrl()!.mappings.length > 0) {
      <mat-card class="fcd-table-card">
        <mat-card-content class="fcd-card-content">
          <div class="fcd-table-card__title">Cross-Framework Mappings</div>
        </mat-card-content>
        <div class="fcd-table-wrap">
          <table>
            <thead>
              <tr>
                <th class="fcd-th-fw">Framework</th>
                <th class="fcd-th-ctrl">Control ID</th>
                <th>Title</th>
                <th class="fcd-th-type">Type</th>
                <th class="fcd-th-conf">Confidence</th>
              </tr>
            </thead>
            <tbody>
              @for (m of ctrl()!.mappings; track $index) {
                <tr>
                  <td class="fcd-td--secondary">{{ m.framework }}</td>
                  <td>
                    <span class="fcd-mono fcd-mono--primary">{{ m.control_id }}</span>
                  </td>
                  <td class="fcd-td--secondary fcd-td--wrap">{{ m.control_title }}</td>
                  <td>
                    <mat-chip-set>
                      <mat-chip class="fcd-chip--mapping-type">{{ m.mapping_type }}</mat-chip>
                    </mat-chip-set>
                  </td>
                  <td>
                    <div class="fcd-conf">
                      <div class="fcd-conf__bar">
                        <div class="fcd-conf__fill"
                             [style.width.%]="m.confidence * 100"
                             [style.background]="confidenceColor(m.confidence).color">
                        </div>
                      </div>
                      <span class="fcd-conf__pct" [style.color]="confidenceColor(m.confidence).color">
                        {{ (m.confidence * 100).toFixed(0) }}%
                      </span>
                    </div>
                  </td>
                </tr>
              }
            </tbody>
          </table>
        </div>
      </mat-card>
    } @else {
      <div class="fcd-alert fcd-alert--info">No cross-framework mappings found for this control.</div>
    }
  }

</div>
  `,
  styles: [`
    .fcd-page { padding: 0; }

    .fcd-back-row { display:flex; align-items:center; gap:8px; margin-bottom:8px; }
    .fcd-back-row__label { font-size:0.8rem; color:#888; }

    .fcd-loading { }
    .fcd-skeleton { height:200px; background:rgba(255,255,255,0.06); border-radius:8px; }
    .fcd-error { padding:16px; color:#f44336; border-radius:6px; background:rgba(192,0,0,0.1); }

    .fcd-top-row { display:flex; gap:16px; flex-wrap:wrap; margin-bottom:24px; }

    .fcd-info-card { flex: 1 1 340px; }
    .fcd-info-card__subtitle { font-size:0.85rem; color:#888; font-weight:500; margin-bottom:12px; }
    .fcd-info-card__chips { margin-bottom:12px; }
    .fcd-info-card__desc { font-size:0.88rem; color:#aaa; line-height:1.6; margin-bottom:12px; }
    .fcd-info-card__block { margin-bottom:10px; }
    .fcd-info-card__lbl { font-size:0.75rem; color:#666; margin-bottom:4px; }

    .fcd-summary-card { flex: 0 0 200px; }
    .fcd-summary-card__count { font-size:2.2rem; font-weight:800; line-height:1; margin:8px 0 4px; }
    .fcd-summary-card__sub { font-size:0.78rem; color:#888; }

    .fcd-table-card { }
    .fcd-table-card__title { font-size:0.88rem; font-weight:600; }
    .fcd-card-content { padding-bottom: 4px; }
    .fcd-table-wrap { overflow-x:auto; }
    .fcd-th-fw   { width: 200px; }
    .fcd-th-ctrl { width: 130px; }
    .fcd-th-type, .fcd-th-conf { width: 110px; }

    table { width:100%; border-collapse:collapse; font-size:0.82rem; }
    th { text-align:left; padding:6px 12px; font-weight:600; font-size:0.75rem; border-bottom:1px solid rgba(255,255,255,0.08); color:#888; white-space:nowrap; }
    td { padding:6px 12px; border-bottom:1px solid rgba(255,255,255,0.04); vertical-align:middle; }
    tr:hover td { background:rgba(255,255,255,0.03); }

    .fcd-td--secondary { color:#888; font-size:0.78rem; }
    .fcd-td--wrap { max-width:260px; white-space:normal; line-height:1.3; }

    .fcd-mono { font-family:monospace; font-size:0.75rem; font-weight:700; }
    .fcd-mono--primary { color:var(--mat-sys-primary); }

    .fcd-conf { display:flex; align-items:center; gap:6px; }
    .fcd-conf__bar { flex:1; height:4px; border-radius:2px; background:rgba(255,255,255,0.06); overflow:hidden; min-width:50px; }
    .fcd-conf__fill { height:100%; border-radius:2px; }
    .fcd-conf__pct { font-size:0.72rem; min-width:32px; text-align:right; flex-shrink:0; font-weight:600; }

    .fcd-alert { padding:12px 16px; border-radius:6px; font-size:0.85rem; }
    .fcd-alert--info { background:rgba(21,101,192,0.12); color:#64b5f6; }

    .fcd-chip--section { background:rgba(255,255,255,0.06) !important; color:#888 !important; font-size:0.7rem !important; }
    .fcd-chip--sec-prop { background:rgba(68,114,196,0.12) !important; color:#8B9CC8 !important; font-size:0.65rem !important; }
    .fcd-chip--mapping-type { background:rgba(68,114,196,0.1) !important; color:#8B9CC8 !important; font-size:0.62rem !important; height:16px !important; }
  `],
})
export class FrameworkControlDetailComponent {
  private route = inject(ActivatedRoute)
  readonly router = inject(Router)
  private controlsApi = inject(ControlsApiService)
  private product = inject(ProductService)
  private theme = inject(ThemeService)

  // ── Route params ──────────────────────────────────────────────────────────

  private readonly code = this.route.snapshot.paramMap.get('code') ?? ''
  private readonly controlId = this.route.snapshot.paramMap.get('controlId') ?? ''

  // ── Query ─────────────────────────────────────────────────────────────────

  readonly ctrlQuery = injectQuery(() => ({
    queryKey: ['fw-ctrl-detail', this.code, this.controlId],
    queryFn: () => firstValueFrom(this.controlsApi.getByFrameworkCode(this.code, this.controlId)),
    enabled: !!(this.code && this.controlId),
  }))

  readonly ctrl = computed<FrameworkControlDetail | null>(() => this.ctrlQuery.data() ?? null)

  // ── Computed ──────────────────────────────────────────────────────────────

  readonly productColor = computed(() => PRODUCT_COLORS[this.product.product()] ?? '#4472C4')
  readonly productSubtitle = computed(() => PRODUCT_SUBTITLES[this.product.product()] ?? '')

  readonly sectionLabel = computed(() => {
    const c = this.ctrl()
    if (!c) return ''
    const parts = c.control_id.split('.')
    const sectionKey = parts[0].length >= 3 && /^[A-Za-z]+$/.test(parts[0]) && parts[0] !== 'A'
      ? parts[0]
      : `${parts[0]}.${parts[1] ?? ''}`
    return SECTION_LABELS[sectionKey] ?? sectionKey
  })

  readonly frameworkCount = computed(() => {
    const c = this.ctrl()
    if (!c) return 0
    return new Set(c.mappings.map(m => m.framework)).size
  })

  // ── Methods ───────────────────────────────────────────────────────────────

  confidenceColor(c: number): { bg: string; color: string } {
    return this.theme.isDark() ? confidenceColorDark(c) : confidenceColorLight(c)
  }

  goBack(): void {
    if (this.code) {
      this.router.navigate(['/compliance', this.code])
    } else {
      this.router.navigate(['/controls'])
    }
  }
}
