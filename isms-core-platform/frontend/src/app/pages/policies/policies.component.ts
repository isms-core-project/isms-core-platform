import { Component, inject, signal, computed, effect, ElementRef, viewChild } from '@angular/core'
import { NgStyle } from '@angular/common'
import { Router } from '@angular/router'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'

import { injectQuery, injectMutation, injectQueryClient } from '@tanstack/angular-query-experimental'

import { MatCardModule } from '@angular/material/card'
import { MatTableModule } from '@angular/material/table'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatChipsModule } from '@angular/material/chips'
import { MatButtonModule } from '@angular/material/button'
import { MatIconModule } from '@angular/material/icon'
import { MatDialogModule, MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatTooltipModule } from '@angular/material/tooltip'

import { PoliciesApiService, PolicyRead } from '../../api/policies-api.service'
import { ControlsApiService } from '../../api/controls-api.service'
import { ProductService, PRODUCT_COLORS } from '../../core/services/product.service'
import { ThemeService } from '../../core/services/theme.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'
import { MetricCardComponent } from '../../shared/components/metric-card.component'

// ─── Delete Confirm Dialog ────────────────────────────────────────────────────

@Component({
  selector: 'app-policies-delete-dialog',
  standalone: true,
  imports: [MatButtonModule, MatDialogModule, MatIconModule],
  template: `
    <h2 mat-dialog-title>Delete External Document?</h2>
    <mat-dialog-content>
      <strong>{{ data.title }}</strong> will be permanently removed from the platform. This cannot be undone.
    </mat-dialog-content>
    <mat-dialog-actions>
      <button mat-stroked-button [mat-dialog-close]="false">Cancel</button>
      <button mat-raised-button color="warn" [mat-dialog-close]="true">
        <mat-icon>delete</mat-icon> Delete
      </button>
    </mat-dialog-actions>
  `,
})
export class PoliciesDeleteDialogComponent {
  readonly data = inject<{ title: string }>(MAT_DIALOG_DATA)
}

// ─── Import External Dialog ───────────────────────────────────────────────────
@Component({
  selector: 'app-import-external-dialog',
  standalone: true,
  imports: [
    FormsModule,
    MatButtonModule, MatDialogModule, MatFormFieldModule, MatInputModule,
    MatSelectModule, MatIconModule, MatProgressSpinnerModule,
  ],
  template: `
    <h2 mat-dialog-title>
      Import External Document
      <small class="dialog-subtitle">
        PDF, DOCX, or Markdown — any format, no ISMS CORE watermark required
      </small>
    </h2>

    <mat-dialog-content>
      @if (result()) {
        <div class="import-success">
          <mat-icon class="success-icon">check_circle</mat-icon>
          <div>
            <div class="result-title">{{ result()!.title }}</div>
            <div class="result-doc-id">{{ result()!.document_id }}</div>
            <div class="result-meta">
              {{ result()!.word_count.toLocaleString() }} words · {{ result()!.requirements_extracted }} requirements extracted
            </div>
          </div>
        </div>
      } @else {
        @if (importMutation.isError()) {
          <div class="alert-error">Import failed. Check file format and try again.</div>
        }

        <div
          class="file-drop"
          [class.file-drop--active]="selectedFile()"
          (click)="fileInput.click()"
        >
          <input
            #fileInput
            type="file"
            accept=".pdf,.docx,.doc,.md"
            class="file-input-hidden"
            (change)="onFileChange($event)"
          />
          <mat-icon class="upload-icon">upload_file</mat-icon>
          <span [style.color]="selectedFile() ? 'var(--mat-sys-primary)' : 'var(--mat-sys-on-surface-variant)'">
            {{ selectedFile() ? selectedFile()!.name : 'Click to select a file (.pdf, .docx, .md)' }}
          </span>
          @if (selectedFile()) {
            <small class="file-size-hint">{{ (selectedFile()!.size / 1024).toFixed(1) }} KB</small>
          }
        </div>

        <mat-form-field appearance="outline" class="full-width">
          <mat-label>Control Group *</mat-label>
          <mat-select [(ngModel)]="groupCode">
            <mat-option value=""><em>Select control group…</em></mat-option>
            @for (g of controlGroups.data() ?? []; track g.id) {
              <mat-option [value]="g.group_code">
                <span class="group-code-option">{{ g.group_code.toUpperCase() }}</span>
                {{ g.group_name }}
              </mat-option>
            }
          </mat-select>
        </mat-form-field>

        <mat-form-field appearance="outline" class="full-width">
          <mat-label>Source / Organisation *</mat-label>
          <input matInput [(ngModel)]="sourceLabel" placeholder="e.g. Previous consultant, Acme Corp" />
          <mat-hint>Shown as amber 'External — [source]' label throughout the platform</mat-hint>
        </mat-form-field>

        <mat-form-field appearance="outline" class="lang-select-field">
          <mat-label>Language</mat-label>
          <mat-select [(ngModel)]="language">
            <mat-option value="en">EN — English</mat-option>
            <mat-option value="de">DE — Deutsch</mat-option>
            <mat-option value="fr">FR — Français</mat-option>
            <mat-option value="it">IT — Italiano</mat-option>
          </mat-select>
        </mat-form-field>
      }
    </mat-dialog-content>

    <mat-dialog-actions align="end">
      @if (result()) {
        <button mat-button (click)="matDialog.closeAll()">Close</button>
        <button mat-raised-button color="primary" (click)="matDialog.closeAll()">View in Policies</button>
      } @else {
        <button mat-button [disabled]="importMutation.isPending()" (click)="matDialog.closeAll()">Cancel</button>
        <button mat-raised-button color="primary" [disabled]="!canSubmit()" (click)="doImport()">
          @if (importMutation.isPending()) {
            Importing…
          } @else {
            <ng-container>
              <mat-icon>upload_file</mat-icon>
              Import
            </ng-container>
          }
        </button>
      }
    </mat-dialog-actions>
  `,
  styles: [`
    mat-dialog-content {
      display: flex; flex-direction: column; gap: 16px;
      padding-top: 8px !important; min-width: 460px;
    }
    .full-width { width: 100%; }
    .lang-select-field { width: 160px; }
    .dialog-subtitle {
      display: block; font-size: 0.75rem; font-weight: 400;
      color: var(--mat-sys-on-surface-variant); margin-top: 2px;
    }
    .file-input-hidden { display: none; }
    .upload-icon { color: var(--mat-sys-on-surface-variant); }
    .file-size-hint { color: var(--mat-sys-on-surface-variant); }
    .group-code-option {
      font-family: monospace; font-size: 0.75rem;
      color: var(--mat-sys-primary); margin-right: 8px;
    }
    .success-icon { color: var(--mat-sys-primary); }
    .result-title { font-weight: 600; font-size: 0.9rem; }
    .result-doc-id { font-family: monospace; font-size: 0.75rem; color: var(--mat-sys-on-surface-variant); }
    .result-meta { font-size: 0.78rem; color: var(--mat-sys-on-surface-variant); }
    .file-drop {
      display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px;
      border: 1px dashed var(--mat-sys-outline); border-radius: 8px; padding: 20px;
      cursor: pointer; text-align: center; transition: border-color 0.2s, background 0.2s;
    }
    .file-drop:hover { border-color: var(--mat-sys-primary); background: color-mix(in srgb, var(--mat-sys-primary) 5%, transparent); }
    .file-drop--active { border-color: var(--mat-sys-primary); background: color-mix(in srgb, var(--mat-sys-primary) 7%, transparent); }
    .import-success {
      display: flex; align-items: flex-start; gap: 12px;
      background: rgba(46,125,50,0.1); border: 1px solid rgba(46,125,50,0.3);
      border-radius: 6px; padding: 14px;
    }
    .alert-error {
      background: rgba(192,0,0,0.1); border: 1px solid rgba(192,0,0,0.3);
      border-radius: 6px; padding: 10px 14px; font-size: 0.85rem;
      color: var(--mat-sys-error);
    }
  `],
})
export class ImportExternalDialogComponent {
  matDialog = inject(MatDialog)
  private policiesApi = inject(PoliciesApiService)
  private controlsApi = inject(ControlsApiService)
  private queryClient = injectQueryClient()

  fileInput = viewChild.required<ElementRef<HTMLInputElement>>('fileInput')

  selectedFile = signal<File | null>(null)
  groupCode = ''
  sourceLabel = ''
  language = 'en'
  result = signal<{ document_id: string; title: string; word_count: number; requirements_extracted: number } | null>(null)

  controlGroups = injectQuery(() => ({
    queryKey: ['control-groups-list'],
    queryFn: () => firstValueFrom(this.controlsApi.list()),
  }))

  importMutation = injectMutation(() => ({
    mutationFn: () => firstValueFrom(
      this.policiesApi.importExternal(this.selectedFile()!, this.groupCode, this.sourceLabel, this.language)
    ),
    onSuccess: (data: any) => {
      this.result.set(data)
      this.queryClient.invalidateQueries({ queryKey: ['policies'] })
    },
  }))

  canSubmit = computed(() =>
    !!this.selectedFile() && !!this.groupCode && !!this.sourceLabel && !this.importMutation.isPending()
  )

  onFileChange(event: Event): void {
    const input = event.target as HTMLInputElement
    this.selectedFile.set(input.files?.[0] ?? null)
  }

  doImport(): void {
    if (!this.canSubmit()) return
    this.importMutation.mutate(undefined)
  }
}

// ─── Main Component ───────────────────────────────────────────────────────────
@Component({
  selector: 'app-policies',
  standalone: true,
  imports: [
    NgStyle, FormsModule,
    MatCardModule, MatTableModule, MatFormFieldModule, MatInputModule,
    MatSelectModule, MatChipsModule, MatButtonModule, MatIconModule,
    MatDialogModule, MatProgressSpinnerModule, MatTooltipModule,
    PageHeaderComponent, MetricCardComponent,
  ],
  template: `
    <app-page-header [title]="'Policies'" [subtitle]="headerSubtitle()">
      <div actions>
        <button mat-stroked-button (click)="openImport()">
          <mat-icon>upload_file</mat-icon>
          Import External Doc
        </button>
      </div>
    </app-page-header>

    <!-- Metric cards -->
    @if (!policiesQuery.isLoading()) {
      <div class="metrics-row">
        <app-metric-card title="Total" [value]="allPolicies().length" icon="policy" />
        @if (product() === 'isms') {
          <app-metric-card title="Framework" [value]="frameworkCount()" />
          <app-metric-card title="Operational" [value]="operationalCount()" />
        }
        @if (product() === 'privacy') {
          <app-metric-card title="Privacy" [value]="privacyCount()" />
        }
        @if (product() === 'cloud') {
          <app-metric-card title="Cloud" [value]="cloudCount()" />
        }
        @if (product() === 'ai') {
          <app-metric-card title="AI" [value]="aiCount()" />
        }
        <app-metric-card title="External" [value]="externalCount()" />
      </div>
    }

    <!-- Filters -->
    <mat-card class="filter-card">
      <mat-card-content>
        <div class="filter-row">

          <!-- External only toggle chip -->
          <div
            class="ext-chip"
            [class.ext-chip--active]="externalOnly()"
            (click)="toggleExternalOnly()"
          >
            <span class="dot" [style.background]="isDark() ? '#FFC000' : '#9a6500'"></span>
            External only
          </div>

          <!-- Type -->
          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="type-filter-field">
            <mat-label>Type</mat-label>
            <mat-select [ngModel]="typeFilter()" (ngModelChange)="typeFilter.set($event)">
              <mat-option value="">All types</mat-option>
              @if (product() === 'isms') {
                <mat-option value="POL">POL</mat-option>
                <mat-option value="OP-POL">OP-POL</mat-option>
                <mat-option value="INS">INS</mat-option>
                <mat-option value="REF">REF</mat-option>
                <mat-option value="CTX">CTX</mat-option>
                <mat-option value="FORM">FORM</mat-option>
              }
              @if (product() === 'privacy') { <mat-option value="PRIV-POL">PRIV-POL</mat-option> }
              @if (product() === 'cloud')   { <mat-option value="CLD-PII-POL">CLD-PII-POL</mat-option> }
              @if (product() === 'ai')      { <mat-option value="AI-POL">AI-POL</mat-option> }
            </mat-select>
          </mat-form-field>

          <!-- Search -->
          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="search-field">
            <mat-label>Search policies</mat-label>
            <mat-icon matPrefix class="icon-md">search</mat-icon>
            <input matInput [ngModel]="search()" (ngModelChange)="search.set($event)" placeholder="document ID, title, group…" />
          </mat-form-field>

          <!-- Language chips — only when multi-lang -->
          @if (hasMultiLang()) {
            <div class="lang-chips">
              @for (l of langOptions(); track l.value) {
                <div
                  class="lang-chip"
                  [class.lang-chip--active]="langFilter() === l.value"
                  (click)="langFilter.set(l.value)"
                >{{ l.label }} {{ l.count }}</div>
              }
            </div>
          }
        </div>
      </mat-card-content>
    </mat-card>

    <!-- Error banner -->
    @if (policiesQuery.isError()) {
      <div class="alert-error alert-error-banner">Failed to load policies.</div>
    }

    <!-- Table -->
    <mat-card class="table-card">
      <table mat-table [dataSource]="tableData()" class="full-table">

        <!-- Control Group -->
        <ng-container matColumnDef="group">
          <th mat-header-cell *matHeaderCellDef>Control Group</th>
          <td mat-cell *matCellDef="let p" class="clickable" (click)="navigateToControl(p)">
            <span class="group-code" [style.color]="groupCodeColor(p)">
              {{ p.group_code === '00' ? '00' : (p.group_code ?? '—').toUpperCase() }}
            </span>
            <span class="group-name">{{ p.group_name ?? '' }}</span>
          </td>
        </ng-container>

        <!-- Document -->
        <ng-container matColumnDef="document">
          <th mat-header-cell *matHeaderCellDef>Document</th>
          <td mat-cell *matCellDef="let p" class="clickable" (click)="navigateToControl(p)">
            <span class="doc-id"
              [style.color]="p.product_type === 'external' ? (isDark() ? '#FFC000' : '#7a4800') : 'var(--mat-sys-on-surface-variant)'">
              {{ p.document_id }}
            </span>
            <span class="doc-title">{{ p.title }}</span>
            @if (p.product_type === 'external' && p.source_label) {
              <span class="source-lbl" [style.color]="isDark() ? '#FFC000' : '#7a4800'">External — {{ p.source_label }}</span>
            }
            @if (p.language && p.language !== 'en') {
              <span class="lang-badge">{{ p.language.toUpperCase() }}</span>
            }
          </td>
        </ng-container>

        <!-- Product -->
        <ng-container matColumnDef="product">
          <th mat-header-cell *matHeaderCellDef class="col-product">Product</th>
          <td mat-cell *matCellDef="let p" class="clickable" (click)="navigateToControl(p)">
            <span class="product-chip" [ngStyle]="productChipStyle(p.product_type)">{{ p.product_type }}</span>
          </td>
        </ng-container>

        <!-- Type -->
        <ng-container matColumnDef="type">
          <th mat-header-cell *matHeaderCellDef class="col-type">Type</th>
          <td mat-cell *matCellDef="let p" class="clickable" (click)="navigateToControl(p)">
            <span class="type-chip">{{ p.policy_type.toUpperCase() }}</span>
          </td>
        </ng-container>

        <!-- Words -->
        <ng-container matColumnDef="words">
          <th mat-header-cell *matHeaderCellDef class="col-words col-right">Words</th>
          <td mat-cell *matCellDef="let p" class="col-right clickable" (click)="navigateToControl(p)">
            <span class="cell-secondary">{{ p.word_count != null ? p.word_count.toLocaleString() : '—' }}</span>
          </td>
        </ng-container>

        <!-- Reqs -->
        <ng-container matColumnDef="reqs">
          <th mat-header-cell *matHeaderCellDef class="col-reqs col-right">Reqs</th>
          <td mat-cell *matCellDef="let p" class="col-right clickable" (click)="navigateToControl(p)">
            <span class="reqs-value"
              [style.color]="(p.requirements_count ?? 0) > 0 ? 'var(--mat-sys-primary)' : 'var(--mat-sys-on-surface-variant)'"
              [style.font-weight]="(p.requirements_count ?? 0) > 0 ? '600' : '400'"
            >{{ (p.requirements_count ?? 0) > 0 ? p.requirements_count : '—' }}</span>
          </td>
        </ng-container>

        <!-- Actions -->
        <ng-container matColumnDef="actions">
          <th mat-header-cell *matHeaderCellDef class="col-actions"></th>
          <td mat-cell *matCellDef="let p">
            @if (p.product_type === 'external') {
              <button mat-icon-button class="del-btn"
                matTooltip="Delete external document"
                (click)="$event.stopPropagation(); openDelete(p)">
                <mat-icon class="icon-sm">delete</mat-icon>
              </button>
            }
          </td>
        </ng-container>

        <tr mat-header-row *matHeaderRowDef="displayedColumns"></tr>
        <tr mat-row *matRowDef="let p; columns: displayedColumns"
          class="policy-row"
          [class.policy-row--external]="p.product_type === 'external'"></tr>

        <tr class="mat-row" *matNoDataRow>
          <td [attr.colspan]="displayedColumns.length" class="no-data-cell">
            @if (policiesQuery.isLoading()) {
              <span class="no-data-text">Loading…</span>
            } @else {
              <span class="no-data-text">No policies match the current filters.</span>
            }
          </td>
        </tr>
      </table>
    </mat-card>

  `,
  styles: [`
    :host { display: block; }

    .metrics-row { display: flex; gap: 16px; margin-top: 16px; margin-bottom: 16px; }
    .metrics-row > * { flex: 1; }

    .filter-card { margin-bottom: 16px; }
    .filter-card mat-card-content { padding-bottom: 12px !important; }
    .filter-row { display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }

    .type-filter-field { width: 160px; }
    .search-field { flex: 1; min-width: 200px; }

    .ext-chip {
      display: flex; align-items: center; gap: 6px;
      height: 28px; padding: 0 12px; border-radius: 14px; cursor: pointer;
      font-size: 0.75rem; border: 1px solid var(--mat-sys-outline-variant);
      color: var(--mat-sys-on-surface-variant); white-space: nowrap;
      transition: all 0.15s;
    }
    .ext-chip:hover { background: rgba(255,192,0,0.1); color: #FFC000; }
    .ext-chip--active { background: rgba(255,192,0,0.15); color: #FFC000; border-color: rgba(255,192,0,0.5); font-weight: 700; }
    .dot { width: 6px; height: 6px; border-radius: 50%; flex-shrink: 0; }

    .lang-chips { display: flex; gap: 4px; align-items: center; }
    .lang-chip {
      height: 22px; padding: 0 8px; border-radius: 11px; cursor: pointer;
      font-size: 0.68rem; border: 1px solid transparent;
      background: rgba(0,0,0,0.04); color: var(--mat-sys-on-surface-variant);
      display: flex; align-items: center; white-space: nowrap;
    }
    .lang-chip--active { background: color-mix(in srgb, var(--mat-sys-primary) 22%, transparent); color: var(--mat-sys-primary); border-color: color-mix(in srgb, var(--mat-sys-primary) 40%, transparent); }

    .table-card { overflow: hidden; }
    .full-table { width: 100%; }

    .clickable { cursor: pointer; }
    .col-right { text-align: right; }
    .col-product { width: 110px; }
    .col-type { width: 70px; }
    .col-words { width: 80px; }
    .col-reqs { width: 80px; }
    .col-actions { width: 40px; }

    .no-data-cell { text-align: center; padding: 24px; }
    .no-data-text { color: var(--mat-sys-on-surface-variant); font-size: 0.875rem; }
    .reqs-value { font-size: 0.78rem; }

    .group-code { display: block; font-family: monospace; font-weight: 700; font-size: 0.78rem; }
    .group-name { display: block; font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); line-height: 1.3; }
    .doc-id { display: block; font-family: monospace; font-size: 0.68rem; }
    .doc-title { display: block; font-weight: 600; font-size: 0.875rem; line-height: 1.3; }
    .source-lbl { display: block; font-size: 0.65rem; }
    .lang-badge {
      display: inline-block; font-size: 0.6rem; height: 14px; padding: 0 4px;
      border-radius: 3px; background: rgba(0,0,0,0.05); color: var(--mat-sys-on-surface-variant);
      vertical-align: middle; margin-top: 2px; line-height: 14px;
    }
    .product-chip {
      font-size: 0.65rem; height: 18px; line-height: 18px; padding: 0 6px;
      border-radius: 9px; display: inline-block; font-weight: 600;
    }
    .type-chip {
      font-size: 0.65rem; height: 18px; line-height: 18px; padding: 0 6px;
      border-radius: 9px; display: inline-block;
      background: var(--mat-sys-surface-variant); color: var(--mat-sys-on-surface-variant);
    }
    .cell-secondary { font-size: 0.78rem; color: var(--mat-sys-on-surface-variant); }

    .policy-row:hover td { background: rgba(255,255,255,0.04); }
    .policy-row--external { background: rgba(255,192,0,0.03); }

    .del-btn { color: var(--mat-sys-error); opacity: 0.5; }
    .del-btn:hover { opacity: 1; }

    .alert-error {
      padding: 10px 14px; border-radius: 6px; font-size: 0.85rem;
      background: rgba(192,0,0,0.1); border: 1px solid rgba(192,0,0,0.3); color: var(--mat-sys-error);
    }
    .alert-error-banner { margin-bottom: 16px; }
    .alert-error-mb { margin-bottom: 12px; }
  `],
})
export class PoliciesComponent {
  private router = inject(Router)
  private dialog = inject(MatDialog)
  private policiesApi = inject(PoliciesApiService)
  private productService = inject(ProductService)
  private themeService = inject(ThemeService)
  private queryClient = injectQueryClient()

  externalOnly = signal(false)
  typeFilter   = signal('')
  langFilter   = signal('')
  search       = signal('')

  product   = this.productService.product
  ismsTier  = this.productService.ismsTier
  isDark    = computed(() => this.themeService.isDark())

  displayedColumns = ['group', 'document', 'product', 'type', 'words', 'reqs', 'actions']

  private STANDARD_LABELS: Record<string, string> = {
    isms: 'ISO 27001:2022', privacy: 'ISO 27701:2025', cloud: 'ISO 27018:2025', ai: 'ISO 42001:2023',
  }

  effectiveProduct = computed(() => {
    if (this.externalOnly()) return 'external'
    const p = this.product()
    if (p === 'isms') {
      const tier = this.ismsTier()
      return tier !== 'all' ? tier : 'isms'
    }
    return p
  })

  private prevProduct = this.product()
  constructor() {
    effect(() => {
      const p = this.product()
      if (p !== this.prevProduct) {
        this.prevProduct = p
        this.typeFilter.set('')
      }
    })
  }

  policiesQuery = injectQuery(() => ({
    queryKey: ['policies', this.effectiveProduct(), this.typeFilter()],
    queryFn: () => firstValueFrom(this.policiesApi.list({
      product: this.effectiveProduct(),
      policy_type: this.typeFilter() || undefined,
    })),
  }))

  allPolicies = computed(() => this.policiesQuery.data() ?? [])

  tableData = computed(() => {
    const lf = this.langFilter()
    const s = this.search().toLowerCase()
    const list = this.allPolicies()
    if (!lf && !s) return list
    return list.filter(p => {
      if (lf && (p.language ?? 'en') !== lf) return false
      if (!s) return true
      return (
        (p.document_id ?? '').toLowerCase().includes(s) ||
        (p.title ?? '').toLowerCase().includes(s) ||
        (p.group_code ?? '').toLowerCase().includes(s)
      )
    })
  })

  langCounts = computed(() =>
    this.allPolicies().reduce<Record<string, number>>((acc, p) => {
      const l = p.language ?? 'en'
      acc[l] = (acc[l] ?? 0) + 1
      return acc
    }, {})
  )

  hasMultiLang  = computed(() => Object.keys(this.langCounts()).length > 1)

  langOptions = computed(() => {
    const counts = this.langCounts()
    const total  = this.allPolicies().length
    const opts: { value: string; label: string; count: number }[] = [{ value: '', label: 'All', count: total }]
    for (const l of ['en', 'de', 'fr', 'it']) {
      if (counts[l]) opts.push({ value: l, label: l.toUpperCase(), count: counts[l] })
    }
    return opts
  })

  frameworkCount   = computed(() => this.allPolicies().filter(p => p.product_type === 'framework').length)
  operationalCount = computed(() => this.allPolicies().filter(p => p.product_type === 'operational').length)
  privacyCount     = computed(() => this.allPolicies().filter(p => p.product_type === 'privacy').length)
  cloudCount       = computed(() => this.allPolicies().filter(p => p.product_type === 'cloud').length)
  aiCount          = computed(() => this.allPolicies().filter(p => p.product_type === 'ai').length)
  externalCount    = computed(() => this.allPolicies().filter(p => p.product_type === 'external').length)

  headerSubtitle = computed(() =>
    `${this.allPolicies().length} policy documents · ${this.STANDARD_LABELS[this.product()] ?? 'ISO 27001:2022'}`
  )

  deleteMutation = injectMutation(() => ({
    mutationFn: (id: string) => firstValueFrom(this.policiesApi.delete(id)),
    onSuccess: () => this.queryClient.invalidateQueries({ queryKey: ['policies'] }),
  }))

  productChipStyle(type: string): Record<string, string> {
    const dark = this.isDark()
    if (type === 'external')    return { background: dark ? 'rgba(255,192,0,0.15)' : 'rgba(230,160,0,0.15)', color: dark ? '#FFC000' : '#7a4800' }
    if (type === 'framework')   return { background: 'rgba(50,125,244,0.15)',            color: '#327df4' }
    if (type === 'operational') return { background: 'rgba(112,173,71,0.15)',             color: '#70AD47' }
    if (type === 'privacy')     return { background: `${PRODUCT_COLORS.privacy}22`,       color: PRODUCT_COLORS.privacy }
    if (type === 'cloud')       return { background: `${PRODUCT_COLORS.cloud}22`,         color: PRODUCT_COLORS.cloud }
    if (type === 'ai')          return { background: `${PRODUCT_COLORS.ai}22`,            color: PRODUCT_COLORS.ai }
    return { background: 'rgba(112,173,71,0.15)', color: '#70AD47' }
  }

  groupCodeColor(p: PolicyRead): string {
    if (p.group_code === '00') return this.isDark() ? '#FFC000' : '#7a4800'
    const prod = this.product()
    const c = (p.group_code ?? '').toUpperCase()
    if (prod === 'isms') {
      if (c.startsWith('A.5')) return '#9E9E9E'
      if (c.startsWith('A.6')) return '#70AD47'
      if (c.startsWith('A.7')) return '#FFC000'
      if (c.startsWith('A.8')) return '#C00000'
    }
    if (prod === 'privacy') {
      if (c.startsWith('A.1')) return '#ba68c8'
      if (c.startsWith('A.2')) return '#5c6bc0'
      if (c.startsWith('A.3')) return '#4db6ac'
    }
    return PRODUCT_COLORS[prod] ?? 'var(--mat-sys-primary)'
  }

  navigateToControl(p: PolicyRead): void {
    if (p.control_group_id) this.router.navigate(['/controls', p.control_group_id])
  }

  toggleExternalOnly(): void { this.externalOnly.update(v => !v) }

  openDelete(p: PolicyRead): void {
    const ref = this.dialog.open(PoliciesDeleteDialogComponent, { data: { title: p.title } })
    ref.afterClosed().subscribe((ok: boolean) => { if (ok) this.deleteMutation.mutate(p.id) })
  }

  openImport(): void {
    this.dialog.open(ImportExternalDialogComponent, { maxWidth: '560px', width: '100%' })
  }
}
