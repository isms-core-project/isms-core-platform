import { Component, inject, signal, computed, Input, Output, EventEmitter, OnInit } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'

import { injectQuery, injectQueryClient } from '@tanstack/angular-query-experimental'

import { MatButtonModule } from '@angular/material/button'
import { MatCardModule } from '@angular/material/card'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatIconModule } from '@angular/material/icon'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatChipsModule } from '@angular/material/chips'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatButtonToggleModule } from '@angular/material/button-toggle'
import { MatTabsModule } from '@angular/material/tabs'
import { MatTableModule } from '@angular/material/table'
import { GeneratorsApiService, GeneratorItem, GeneratorGroup, GeneratorUpdate, SheetInfo } from '../../api/generators-api.service'
import { ProductService } from '../../core/services/product.service'
import { ThemeService } from '../../core/services/theme.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

// ─── Constants ─────────────────────────────────────────────────────────────────

const SECTION_COLOR: Record<string, string> = {
  '00': '#888888',
  'A.5': '#9E9E9E',
  'A.6': '#70AD47',
  'A.7': '#ED7D31',
  'A.8': '#C00000',
}

const PRODUCT_TYPE_COLOR: Record<string, string> = {
  framework:   '#90caf9',
  operational: '#64b5f6',
  privacy:     '#ce93d8',
  cloud:       '#4db6ac',
  ai:          '#ffb74d',
}

const PRODUCT_TYPE_COLOR_LIGHT: Record<string, string> = {
  framework:   '#1565C0',
  operational: '#1565C0',
  privacy:     '#7B1FA2',
  cloud:       '#00695C',
  ai:          '#E65100',
}

const PRODUCT_TYPE_LABEL: Record<string, string> = {
  framework:   'FW',
  operational: 'OP',
  privacy:     'PRIV',
  cloud:       'CLD',
  ai:          'AI',
}

const SHEET_TYPE_COLOR: Record<string, string> = {
  instructions: '#90caf9',
  input:        '#64b5f6',
  summary:      '#81c784',
  evidence:     '#ffb74d',
  approval:     '#ef5350',
}

const SHEET_TYPE_COLOR_LIGHT: Record<string, string> = {
  instructions: '#1565C0',
  input:        '#1565C0',
  summary:      '#2E7D32',
  evidence:     '#E65100',
  approval:     '#C62828',
}

const SHEET_TYPE_LABEL: Record<string, string> = {
  instructions: 'IL',
  input:        'Data',
  summary:      'SD',
  evidence:     'ER',
  approval:     'AS',
}

const SHEET_TYPES: Array<SheetInfo['type']> = ['instructions', 'input', 'summary', 'evidence', 'approval']

function groupColor(group: GeneratorGroup): string {
  if (SECTION_COLOR[group.section]) return SECTION_COLOR[group.section]
  const pt = group.generators[0]?.product_type ?? 'framework'
  return PRODUCT_TYPE_COLOR[pt] ?? '#327df4'
}

function sectionSort(a: string, b: string): number {
  const parse = (s: string) => s.split('.').map(p => parseInt(p, 10) || p)
  const pa = parse(a), pb = parse(b)
  for (let i = 0; i < Math.max(pa.length, pb.length); i++) {
    const x = (pa[i] ?? -Infinity) as number
    const y = (pb[i] ?? -Infinity) as number
    if (x < y) return -1
    if (x > y) return 1
  }
  return 0
}

function sheetTypeColor(type: string, isDark: boolean): string {
  return isDark ? (SHEET_TYPE_COLOR[type] ?? '#888888') : (SHEET_TYPE_COLOR_LIGHT[type] ?? '#555555')
}

function sheetTypeLabel(type: string): string {
  return SHEET_TYPE_LABEL[type] ?? type
}

function productTypeColor(type: string, isDark: boolean): string {
  return isDark ? (PRODUCT_TYPE_COLOR[type] ?? '#327df4') : (PRODUCT_TYPE_COLOR_LIGHT[type] ?? '#1565C0')
}

function productTypeLabel(type: string): string {
  return PRODUCT_TYPE_LABEL[type] ?? type.toUpperCase()
}

// ─── Edit Dialog Component ──────────────────────────────────────────────────────

@Component({
  selector: 'app-gen-edit-dialog',
  standalone: true,
  imports: [FormsModule, MatButtonModule, MatFormFieldModule, MatInputModule, MatSelectModule, MatIconModule],
  template: `
    <div class="overlay" (click)="onOverlayClick($event)">
      <div class="dialog">
        <div class="dialog-header">
          <div>
            <div class="dialog-title">Edit Generator Definition</div>
            <div class="dialog-doc-id">{{ gen.document_id }}</div>
          </div>
          <button mat-icon-button (click)="close.emit()">
            <mat-icon>close</mat-icon>
          </button>
        </div>

        <div class="dialog-body">
          @if (errorMsg()) {
            <div class="alert-error">{{ errorMsg() }}</div>
          }

          <mat-form-field appearance="outline" class="wb-name-field" subscriptSizing="dynamic">
            <mat-label>Workbook Name</mat-label>
            <input matInput [(ngModel)]="workbookName" />
          </mat-form-field>

          <div class="domain-row">
            <mat-form-field appearance="outline" class="domain-field" subscriptSizing="dynamic">
              <mat-label>Domain Number</mat-label>
              <input matInput type="number" [(ngModel)]="domainNumber" />
            </mat-form-field>
            <mat-form-field appearance="outline" class="domain-field" subscriptSizing="dynamic">
              <mat-label>Total Domains</mat-label>
              <input matInput type="number" [(ngModel)]="domainTotal" />
            </mat-form-field>
          </div>

          <div class="sheets-header">
            <span class="label-caption">SHEETS ({{ sheets().length }})</span>
            <button mat-button color="primary" (click)="addSheet()">
              <mat-icon>add</mat-icon> Add Sheet
            </button>
          </div>

          @for (s of sheets(); track $index) {
            <div class="sheet-row">
              <mat-form-field appearance="outline" class="sheet-name-field" subscriptSizing="dynamic">
                <input matInput [ngModel]="s.name" (ngModelChange)="updateSheetName($index, $event)" placeholder="Sheet name" />
              </mat-form-field>
              <mat-form-field appearance="outline" class="sheet-type-field" subscriptSizing="dynamic">
                <mat-select [ngModel]="s.type" (ngModelChange)="updateSheetType($index, $event)">
                  @for (t of sheetTypes; track t) {
                    <mat-option [value]="t">
                      <span class="type-dot" [style.background]="stColor(t)"></span>
                      {{ t }}
                    </mat-option>
                  }
                </mat-select>
              </mat-form-field>
              <button mat-icon-button color="warn" [disabled]="sheets().length === 1" (click)="removeSheet($index)">
                <mat-icon>delete</mat-icon>
              </button>
            </div>
          }
        </div>

        <div class="dialog-actions">
          <button mat-button [disabled]="saving()" (click)="close.emit()">Cancel</button>
          <button mat-flat-button color="primary" [disabled]="saving()" (click)="save()">
            @if (saving()) { Saving… } @else { Save & Lock }
          </button>
        </div>
      </div>
    </div>
  `,
  styles: [`
    .overlay { position:fixed;inset:0;background:rgba(0,0,0,0.5);z-index:1000;display:flex;align-items:center;justify-content:center;padding:16px }
    .dialog { background:var(--mat-sys-surface);border-radius:12px;width:100%;max-width:560px;max-height:85vh;display:flex;flex-direction:column;overflow:hidden }
    .dialog-header { display:flex;align-items:flex-start;gap:12px;padding:16px 16px 12px;border-bottom:1px solid var(--mat-sys-outline-variant) }
    .dialog-title { font-weight:700;font-size:1rem;line-height:1.3 }
    .dialog-doc-id { font-family:monospace;font-size:0.72rem;color:var(--mat-sys-on-surface-variant);margin-top:2px }
    .dialog-body { flex:1;overflow-y:auto;padding:16px }
    .dialog-actions { display:flex;justify-content:flex-end;gap:8px;padding:12px 16px;border-top:1px solid var(--mat-sys-outline-variant) }
    .alert-error { background:rgba(211,47,47,0.12);color:#d32f2f;border:1px solid rgba(211,47,47,0.3);border-radius:6px;padding:8px 12px;font-size:0.82rem;margin-bottom:12px }
    .sheets-header { display:flex;align-items:center;justify-content:space-between;margin-bottom:8px }
    .label-caption { font-size:0.72rem;font-weight:600;color:var(--mat-sys-on-surface-variant);letter-spacing:0.04em }
    .sheet-row { display:flex;gap:8px;align-items:center;margin-bottom:8px }
    .type-dot { display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:6px }
    .wb-name-field { width:100%;margin-bottom:12px }
    .domain-row { display:flex;gap:12px;margin-bottom:12px }
    .domain-field { flex:1 }
    .sheet-name-field { flex:1 }
    .sheet-type-field { min-width:130px }
  `],
})
export class GenEditDialogComponent implements OnInit {
  @Input() gen!: GeneratorItem
  @Output() close = new EventEmitter<void>()
  @Output() saved = new EventEmitter<GeneratorItem>()

  private api = inject(GeneratorsApiService)
  private queryClient = injectQueryClient()
  private theme = inject(ThemeService)

  workbookName = ''
  domainNumber: number | null = null
  domainTotal: number | null = null
  sheets = signal<SheetInfo[]>([])
  saving = signal(false)
  errorMsg = signal<string | null>(null)
  sheetTypes = SHEET_TYPES

  ngOnInit() {
    this.workbookName = this.gen.workbook_name
    this.domainNumber = this.gen.domain_number
    this.domainTotal = this.gen.domain_total
    this.sheets.set([...this.gen.sheets])
  }

  stColor(type: string): string { return sheetTypeColor(type, this.theme.isDark()) }

  addSheet() {
    this.sheets.update(s => [...s, { name: '', type: 'input' }])
  }

  removeSheet(idx: number) {
    this.sheets.update(s => s.filter((_, i) => i !== idx))
  }

  updateSheetName(idx: number, name: string) {
    this.sheets.update(s => s.map((sh, i) => i === idx ? { ...sh, name } : sh))
  }

  updateSheetType(idx: number, type: SheetInfo['type']) {
    this.sheets.update(s => s.map((sh, i) => i === idx ? { ...sh, type } : sh))
  }

  onOverlayClick(e: MouseEvent) {
    if ((e.target as HTMLElement).classList.contains('overlay')) this.close.emit()
  }

  async save() {
    if (!this.workbookName.trim()) { this.errorMsg.set('Workbook name is required'); return }
    if (this.sheets().some(s => !s.name.trim())) { this.errorMsg.set('All sheet names must be filled in'); return }
    this.saving.set(true)
    this.errorMsg.set(null)
    try {
      const body: GeneratorUpdate = {
        workbook_name: this.workbookName.trim(),
        domain_number: this.domainNumber ?? null,
        domain_total: this.domainTotal ?? null,
        sheets: this.sheets(),
      }
      const updated = await firstValueFrom(this.api.update(this.gen.document_id, body))
      await this.queryClient.invalidateQueries({ queryKey: ['generators-grouped'] })
      this.saved.emit(updated)
      this.close.emit()
    } catch {
      this.errorMsg.set('Save failed — please try again')
    } finally {
      this.saving.set(false)
    }
  }
}

// ─── Workbook Preview Drawer Component ─────────────────────────────────────────

@Component({
  selector: 'app-gen-preview-drawer',
  standalone: true,
  imports: [MatButtonModule, MatIconModule, MatChipsModule, MatTabsModule, MatTableModule, MatTooltipModule],
  template: `
    @if (open) {
      <div class="backdrop" (click)="close.emit()"></div>
      <div class="drawer">
        <div class="drawer-header">
          <div class="drawer-title-wrap">
            <div class="wb-name">{{ gen.workbook_name }}</div>
            <div class="wb-docid">{{ gen.document_id }}</div>
          </div>
          <button mat-icon-button (click)="close.emit()">
            <mat-icon>close</mat-icon>
          </button>
        </div>

        @if (gen.sheet_schemas.length === 0) {
          <div class="drawer-body">
            <div class="info-alert">Detailed column schema not yet extracted. Showing sheet structure from generator metadata.</div>
            <div class="label-caption label-caption-mb">SHEETS ({{ gen.sheet_count }})</div>
            @for (s of gen.sheets; track s.name) {
              <div class="sheet-meta-row" [style.border-color]="stColor(s.type) + '30'" [style.background]="stColor(s.type) + '0a'">
                <span class="dot" [style.background]="stColor(s.type)"></span>
                <span class="sheet-name-text">{{ s.name }}</span>
                <span class="type-badge" [style.background]="stColor(s.type) + '20'" [style.color]="stColor(s.type)">{{ s.type }}</span>
              </div>
            }
            @if (gen.is_stacked && gen.stacked_control_ids) {
              <div class="label-caption label-caption-covers">COVERS CONTROLS</div>
              <div class="chip-row">
                @for (cid of gen.stacked_control_ids; track cid) {
                  <span class="mono-chip">{{ cid }}</span>
                }
              </div>
            }
          </div>
        } @else {
          <mat-tab-group [selectedIndex]="activeTab()" (selectedIndexChange)="activeTab.set($event)"
            class="drawer-tab-group"
            animationDuration="0">
            @for (schema of gen.sheet_schemas; track schema.sheet_name) {
              <mat-tab>
                <ng-template mat-tab-label>
                  <span class="dot sm" [style.background]="stColor(schema.sheet_type)"></span>
                  <span class="tab-label-text">{{ schema.sheet_name }}</span>
                </ng-template>
                <div class="schema-panel">
                  <div class="schema-meta-row">
                    @if (schema.freeze_panes) {
                      <span class="mini-chip">Freeze: {{ schema.freeze_panes }}</span>
                    }
                    @if (schema.status_column_letter) {
                      <span class="mini-chip status-col-chip">Status col: {{ schema.status_column_letter }}</span>
                    }
                    @if (schema.header_row) {
                      <span class="mini-chip">Header row: {{ schema.header_row }}</span>
                    }
                  </div>
                  @if (schema.columns.length === 0) {
                    <div class="no-col-msg">No column data extracted.</div>
                  } @else {
                    <div class="schema-table-wrap">
                      <table class="schema-table">
                        <thead>
                          <tr>
                            @for (h of ['#','Col','Header','Width','DV Values','Flags']; track h) {
                              <th>{{ h }}</th>
                            }
                          </tr>
                        </thead>
                        <tbody>
                          @for (col of schema.columns; track col.index) {
                            <tr [class.status-row]="col.is_status_col">
                              <td class="mono">{{ col.index }}</td>
                              <td class="mono bold-col">{{ col.letter }}</td>
                              <td class="col-header" [class.bold]="col.is_status_col">
                                {{ col.header }}
                                @if (col.required) { <span class="req-marker">*</span> }
                              </td>
                              <td class="dim">{{ col.width }}</td>
                              <td class="dv-cell">
                                @if (col.dv_values.length > 0) {
                                  @for (v of col.dv_values.slice(0, 6); track v) {
                                    <span class="dv-chip">{{ v }}</span>
                                  }
                                  @if (col.dv_values.length > 6) {
                                    <span class="dim small">+{{ col.dv_values.length - 6 }} more</span>
                                  }
                                } @else {
                                  <span class="dim">—</span>
                                }
                              </td>
                              <td>
                                @if (col.is_status_col) {
                                  <span class="status-flag">STATUS</span>
                                }
                              </td>
                            </tr>
                          }
                        </tbody>
                      </table>
                    </div>
                  }
                </div>
              </mat-tab>
            }
          </mat-tab-group>

          <div class="drawer-footer">
            <span class="dim small">{{ gen.sheet_schemas.length }} sheets · {{ totalColumns() }} columns total</span>
            <span class="dim small">{{ schemasWithStatus() }} sheets with status column</span>
          </div>
        }
      </div>
    }
  `,
  styles: [`
    .backdrop { position:fixed;inset:0;background:rgba(0,0,0,0.4);z-index:900 }
    .drawer { position:fixed;top:0;right:0;bottom:0;width:720px;max-width:100%;background:var(--mat-sys-surface);z-index:901;display:flex;flex-direction:column;box-shadow:-4px 0 24px rgba(0,0,0,0.2) }
    .drawer-header { display:flex;align-items:flex-start;gap:8px;padding:14px 16px;border-bottom:1px solid var(--mat-sys-outline-variant) }
    .wb-name { font-weight:700;font-size:0.95rem;line-height:1.3 }
    .wb-docid { font-family:monospace;font-size:0.7rem;color:var(--mat-sys-on-surface-variant);margin-top:2px }
    .drawer-body { flex:1;overflow-y:auto;padding:16px }
    .drawer-footer { display:flex;gap:16px;padding:8px 16px;border-top:1px solid var(--mat-sys-outline-variant) }
    .info-alert { background:rgba(21,101,192,0.1);border:1px solid rgba(21,101,192,0.25);border-radius:6px;padding:8px 12px;font-size:0.8rem;margin-bottom:14px;color:var(--mat-sys-on-surface-variant) }
    .label-caption { font-size:0.72rem;font-weight:600;color:var(--mat-sys-on-surface-variant);letter-spacing:0.04em }
    .sheet-meta-row { display:flex;align-items:center;gap:8px;padding:6px 8px;border-radius:6px;border:1px solid;margin-bottom:4px }
    .sheet-name-text { flex:1;font-size:0.8rem }
    .type-badge { font-size:0.62rem;padding:2px 6px;border-radius:4px }
    .dot { display:inline-block;width:8px;height:8px;border-radius:50%;flex-shrink:0 }
    .dot.sm { width:6px;height:6px;margin-right:4px;flex-shrink:0 }
    .chip-row { display:flex;flex-wrap:wrap;gap:4px }
    .mono-chip { font-family:monospace;font-size:0.65rem;padding:2px 6px;background:var(--mat-sys-surface-variant);border-radius:4px }
    .mini-chip { font-size:0.65rem;padding:2px 7px;background:var(--mat-sys-surface-variant);border-radius:4px;border:1px solid var(--mat-sys-outline-variant) }
    .status-col-chip { background:rgba(255,192,0,0.12);color:#ffca28;border-color:rgba(255,192,0,0.4) }
    .schema-panel { height:100%;overflow:auto }
    .schema-meta-row { display:flex;gap:6px;flex-wrap:wrap;padding:8px 12px }
    .schema-table-wrap { overflow:auto }
    .schema-table { width:100%;border-collapse:collapse;font-size:0.72rem }
    .schema-table th { font-weight:700;font-size:0.7rem;padding:4px 8px;white-space:nowrap;background:var(--mat-sys-surface-variant);border-bottom:1px solid var(--mat-sys-outline-variant) }
    .schema-table td { padding:3px 8px;border-bottom:1px solid var(--mat-sys-outline-variant) }
    .schema-table tr.status-row { background:rgba(255,192,0,0.06) }
    .mono { font-family:monospace }
    .bold-col { font-weight:700;color:var(--mat-sys-primary);font-family:monospace }
    .col-header.bold { font-weight:700 }
    .dim { color:var(--mat-sys-on-surface-variant) }
    .small { font-size:0.68rem }
    .req-marker { font-size:0.62rem;background:rgba(239,83,80,0.12);color:#ef5350;padding:0 3px;border-radius:3px;margin-left:3px }
    .dv-cell { display:flex;flex-wrap:wrap;gap:2px;align-items:center }
    .dv-chip { font-size:0.6rem;padding:1px 5px;background:var(--mat-sys-surface-variant);border-radius:3px;max-width:160px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap }
    .status-flag { font-size:0.6rem;padding:1px 5px;background:rgba(239,83,80,0.1);color:#ef5350;border-radius:3px }
    .drawer-title-wrap { flex:1;min-width:0 }
    .label-caption-mb { margin-bottom:6px }
    .label-caption-covers { margin-top:12px;margin-bottom:6px }
    .drawer-tab-group { flex:1;min-height:0;display:flex;flex-direction:column }
    .tab-label-text { max-width:120px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-size:0.72rem }
    .no-col-msg { padding:12px;color:var(--mat-sys-on-surface-variant);font-size:0.82rem }
  `],
})
export class GenPreviewDrawerComponent {
  @Input() gen!: GeneratorItem
  @Input() open = false
  @Output() close = new EventEmitter<void>()

  private theme = inject(ThemeService)
  activeTab = signal(0)

  stColor(type: string): string { return sheetTypeColor(type, this.theme.isDark()) }

  totalColumns(): number {
    return this.gen.sheet_schemas.reduce((s, sh) => s + sh.columns.length, 0)
  }

  schemasWithStatus(): number {
    return this.gen.sheet_schemas.filter(s => s.status_column_index != null).length
  }
}

// ─── Generator Card Component ───────────────────────────────────────────────────

@Component({
  selector: 'app-generator-card',
  standalone: true,
  imports: [
    MatButtonModule, MatIconModule, MatTooltipModule, MatChipsModule,
    MatProgressSpinnerModule, GenEditDialogComponent, GenPreviewDrawerComponent,
  ],
  template: `
    <div class="gen-card" [class.override]="gen().user_override">
      <div class="card-top">
        <div class="card-info">
          <div class="gen-name">{{ gen().workbook_name }}</div>
          <div class="gen-docid">{{ gen().document_id }}</div>
        </div>
        <div class="card-actions">
          @if (gen().product_type !== 'framework') {
            <span class="type-chip" [style.color]="ptColor(gen().product_type)" [style.background]="ptColor(gen().product_type) + '18'" [style.border-color]="ptColor(gen().product_type) + '40'">
              {{ ptLabel(gen().product_type) }}
            </span>
          }
          @if (gen().user_override) {
            <span class="override-chip" matTooltip="Manually edited — importer will not overwrite. Click to reset." matTooltipPosition="above" (click)="clearOverride()">Override</span>
          }
          @if (gen().is_stacked) {
            <span class="stacked-chip" [matTooltip]="'Stacked: ' + (gen().stacked_control_ids?.join(', ') ?? '')" matTooltipPosition="above">Stacked</span>
          }
          @if (domainLabel()) {
            <span class="domain-chip">{{ domainLabel() }}</span>
          }
          <span class="sheet-count-chip">
            <mat-icon class="table-icon">table_chart</mat-icon>
            {{ gen().sheet_count }} sheets
          </span>

          <button mat-icon-button [matTooltip]="'Workbook preview'" class="icon-btn" (click)="previewOpen.set(true)">
            <mat-icon class="card-action-icon">grid_view</mat-icon>
          </button>
          <button mat-icon-button [matTooltip]="gen().product_type === 'framework' ? 'Generate .py script' : 'Download source script'" class="icon-btn"
            [disabled]="generating() || generatingWb()" (click)="generateScript()">
            <mat-icon class="card-action-icon">code</mat-icon>
          </button>
          <button mat-icon-button matTooltip="Download .xlsx workbook (generated server-side)" class="icon-btn"
            [disabled]="generating() || generatingWb()" (click)="generateWorkbook()">
            @if (generatingWb()) {
              <mat-spinner diameter="14"></mat-spinner>
            } @else {
              <mat-icon class="card-action-icon">download</mat-icon>
            }
          </button>
          <button mat-icon-button matTooltip="Edit" class="icon-btn" (click)="editOpen.set(true)">
            <mat-icon class="card-action-icon">edit</mat-icon>
          </button>
          <button mat-icon-button class="icon-btn" (click)="expanded.update(v => !v)">
            <mat-icon class="card-action-icon">{{ expanded() ? 'expand_less' : 'expand_more' }}</mat-icon>
          </button>
        </div>
      </div>

      <!-- Collapsed: compact sheet type strip -->
      @if (!expanded()) {
        <div class="sheet-strip">
          @for (s of gen().sheets; track s.name) {
            <span class="st-chip"
              [style.color]="stColor(s.type)"
              [style.background]="stColor(s.type) + '18'"
              [style.border-color]="stColor(s.type) + '40'"
              [matTooltip]="s.name" matTooltipPosition="above">
              {{ stLabel(s.type) }}
            </span>
          }
        </div>
      }

      <!-- Expanded: full sheet list -->
      @if (expanded()) {
        <div class="divider"></div>
        <div class="label-caption">Sheets ({{ gen().sheet_count }})</div>
        @for (s of gen().sheets; track s.name) {
          <div class="sheet-row-exp">
            <span class="st-type-badge" [style.background]="stColor(s.type) + '18'" [style.color]="stColor(s.type)" [style.border-color]="stColor(s.type) + '40'">
              {{ s.type }}
            </span>
            <span class="sheet-name-label">{{ s.name }}</span>
          </div>
        }
        @if (gen().is_stacked && gen().stacked_control_ids) {
          <div class="label-caption label-caption-covers-exp">Covers controls:</div>
          <div class="chip-row">
            @for (cid of gen().stacked_control_ids; track cid) {
              <span class="mono-chip">{{ cid }}</span>
            }
          </div>
        }
      }
    </div>

    @if (editOpen()) {
      <app-gen-edit-dialog
        [gen]="gen()"
        (close)="editOpen.set(false)"
        (saved)="onSaved($event)">
      </app-gen-edit-dialog>
    }

    <app-gen-preview-drawer
      [gen]="gen()"
      [open]="previewOpen()"
      (close)="previewOpen.set(false)">
    </app-gen-preview-drawer>
  `,
  styles: [`
    .gen-card { background:var(--mat-sys-surface-container);border:1px solid var(--mat-sys-outline-variant);border-radius:8px;padding:10px 14px;margin-bottom:8px;transition:border-color 0.12s,box-shadow 0.12s }
    .gen-card:hover { border-color:var(--mat-sys-primary);box-shadow:0 1px 4px rgba(0,0,0,0.1) }
    .gen-card.override { border-color:#FFC000 }
    .gen-card.override:hover { border-color:#FFC000 }
    .card-top { display:flex;align-items:flex-start;gap:8px }
    .card-info { flex:1;min-width:0 }
    .gen-name { font-weight:700;font-size:0.82rem;line-height:1.3 }
    .gen-docid { font-family:monospace;font-size:0.7rem;color:var(--mat-sys-on-surface-variant) }
    .card-actions { display:flex;align-items:center;gap:4px;flex-shrink:0;flex-wrap:wrap;justify-content:flex-end }
    .icon-btn { width:28px;height:28px;line-height:28px }
    .type-chip { font-size:0.65rem;font-weight:700;padding:2px 6px;border-radius:4px;border:1px solid;line-height:1.4 }
    .override-chip { font-size:0.65rem;padding:2px 6px;border-radius:4px;background:rgba(255,192,0,0.12);color:#ffca28;border:1px solid rgba(255,192,0,0.35);cursor:pointer }
    .stacked-chip { font-size:0.65rem;padding:2px 6px;border-radius:4px;background:rgba(239,83,80,0.1);color:#ef5350;border:1px solid rgba(239,83,80,0.3) }
    .domain-chip { font-size:0.65rem;padding:2px 6px;border-radius:4px;background:var(--gen-domain-chip-bg);color:var(--gen-domain-chip-color);border:1px solid var(--gen-domain-chip-border) }
    .sheet-count-chip { font-size:0.65rem;padding:2px 6px;border-radius:4px;background:var(--mat-sys-surface-variant);display:flex;align-items:center }
    .sheet-strip { display:flex;flex-wrap:wrap;gap:4px;margin-top:6px }
    .st-chip { font-size:0.65rem;font-weight:700;padding:1px 5px;border-radius:3px;border:1px solid;line-height:1.6;cursor:default }
    .divider { border-top:1px solid var(--mat-sys-outline-variant);margin:8px 0 }
    .label-caption { font-size:0.72rem;font-weight:600;color:var(--mat-sys-on-surface-variant);letter-spacing:0.04em;margin-bottom:4px }
    .sheet-row-exp { display:flex;align-items:center;gap:8px;padding:2px 0 }
    .st-type-badge { font-size:0.6rem;padding:1px 6px;border-radius:3px;border:1px solid;width:80px;text-align:center;flex-shrink:0 }
    .sheet-name-label { font-size:0.75rem }
    .chip-row { display:flex;flex-wrap:wrap;gap:4px;margin-top:2px }
    .mono-chip { font-family:monospace;font-size:0.65rem;padding:2px 6px;background:var(--mat-sys-surface-variant);border-radius:4px }
    .table-icon { font-size:12px;width:12px;height:12px;vertical-align:middle;margin-right:2px }
    .card-action-icon { font-size:1rem }
    .label-caption-covers-exp { margin-top:8px }
  `],
})
export class GeneratorCardComponent {
  @Input() set genItem(v: GeneratorItem) { this.gen.set(v) }

  private api = inject(GeneratorsApiService)
  private queryClient = injectQueryClient()
  private theme = inject(ThemeService)

  gen = signal<GeneratorItem>({ } as GeneratorItem)
  expanded = signal(false)
  editOpen = signal(false)
  previewOpen = signal(false)
  generating = signal(false)
  generatingWb = signal(false)

  domainLabel = computed(() => {
    const g = this.gen()
    if (g.domain_number == null) return null
    return g.domain_total != null ? `Domain ${g.domain_number} of ${g.domain_total}` : `Domain ${g.domain_number}`
  })

  stColor(type: string): string { return sheetTypeColor(type, this.theme.isDark()) }
  stLabel(type: string): string { return sheetTypeLabel(type) }
  ptColor(type: string): string { return productTypeColor(type, this.theme.isDark()) }
  ptLabel(type: string): string { return productTypeLabel(type) }

  async clearOverride() {
    const updated = await firstValueFrom(this.api.clearOverride(this.gen().document_id))
    this.gen.set(updated)
    await this.queryClient.invalidateQueries({ queryKey: ['generators-grouped'] })
  }

  async generateScript() {
    this.generating.set(true)
    try {
      const blob = await firstValueFrom(this.api.generateScript(this.gen().document_id))
      const filename = `${this.gen().document_id}.py`
      const url = URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url; a.download = filename; a.click()
      URL.revokeObjectURL(url)
    } finally {
      this.generating.set(false)
    }
  }

  async generateWorkbook() {
    this.generatingWb.set(true)
    try {
      const blob = await firstValueFrom(this.api.generateWorkbook(this.gen().document_id))
      const filename = `${this.gen().document_id}.xlsx`
      const url = URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url; a.download = filename; a.click()
      URL.revokeObjectURL(url)
    } finally {
      this.generatingWb.set(false)
    }
  }

  onSaved(updated: GeneratorItem) {
    this.gen.set(updated)
  }
}

// ─── Main Generators Component ──────────────────────────────────────────────────

@Component({
  selector: 'app-generators',
  standalone: true,
  imports: [
    FormsModule,
    MatButtonModule, MatCardModule, MatFormFieldModule, MatInputModule,
    MatIconModule, MatChipsModule, MatProgressSpinnerModule,
    MatButtonToggleModule,
    PageHeaderComponent,
    GeneratorCardComponent,
  ],
  template: `
    <div class="gen-page">
    <app-page-header
      title="Generators"
      [subtitle]="headerSubtitle()">
    </app-page-header>

    <!-- Metric strip -->
    <div class="metric-strip">
      @for (m of metrics(); track m.label) {
        <div class="metric-card">
          @if (grouped.isPending()) {
            <div class="metric-skeleton"></div>
          } @else {
            <div class="metric-value">{{ m.value }}</div>
          }
          <div class="metric-label">{{ m.label }}</div>
        </div>
      }
    </div>

    <!-- Filters -->
    <div class="filter-bar">
      <mat-form-field appearance="outline" subscriptSizing="dynamic" class="search-field">
        <mat-label>Search controls or workbooks</mat-label>
        <input matInput [(ngModel)]="search" />
        <mat-icon matSuffix>search</mat-icon>
      </mat-form-field>

      <div class="section-toggle-row">
        @for (s of sections(); track s) {
          <button
            [class.active]="sectionFilter() === s"
            class="section-btn"
            (click)="sectionFilter.set(s)">
            {{ s }}
          </button>
        }
      </div>
    </div>

    <!-- Error -->
    @if (grouped.isError()) {
      <div class="error-alert">Failed to load generator registry.</div>
    }

    <!-- Loading skeletons -->
    @if (grouped.isPending()) {
      @for (i of [0,1,2,3,4,5]; track i) {
        <div class="skeleton-group">
          <div class="skeleton-title"></div>
          <div class="skeleton-card"></div>
          <div class="skeleton-card"></div>
        </div>
      }
    }

    <!-- Generator groups -->
    @if (!grouped.isPending()) {
      @if (filtered().length === 0 && !grouped.isError()) {
        <div class="empty-state">No generators match your filter.</div>
      }
      @for (group of filtered(); track group.group_code) {
        <div class="group-block">
          <div class="group-header">
            <div class="group-accent" [style.background]="groupAccentColor(group)"></div>
            <div>
              <div class="group-title">{{ group.group_code.toUpperCase() }} — {{ group.control_name }}</div>
              <div class="group-subtitle">
                {{ group.generators.length }} workbook{{ group.generators.length !== 1 ? 's' : '' }}
                @if (group.total_domains > 1) { · {{ group.total_domains }} assessment domains }
              </div>
            </div>
          </div>
          @for (gen of group.generators; track gen.document_id) {
            <app-generator-card [genItem]="gen"></app-generator-card>
          }
        </div>
      }
    }
    </div>
  `,
  styles: [`
    .gen-page { display:flex;flex-direction:column;gap:16px }
    .metric-strip { display:flex;gap:16px;flex-wrap:wrap }
    .metric-card { background:var(--mat-sys-surface-container);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:10px 16px;min-width:120px }
    .metric-value { font-size:1.5rem;font-weight:700;color:var(--mat-sys-on-surface) }
    .metric-label { font-size:0.72rem;color:var(--mat-sys-on-surface-variant) }
    .metric-skeleton { width:40px;height:28px;background:var(--mat-sys-surface-variant);border-radius:4px;animation:pulse 1.5s ease-in-out infinite }
    .filter-bar { display:flex;gap:16px;flex-wrap:wrap;align-items:center }
    .section-toggle-row { display:flex;flex-wrap:wrap;gap:4px }
    .section-btn { padding:4px 14px;border:1px solid var(--mat-sys-outline-variant);border-radius:4px;background:transparent;cursor:pointer;font-size:0.75rem;color:var(--mat-sys-on-surface-variant);transition:all 0.12s }
    .section-btn.active { background:var(--mat-sys-primary);color:white;border-color:var(--mat-sys-primary) }
    .section-btn:hover:not(.active) { background:var(--mat-sys-surface-variant) }
    .error-alert { background:rgba(211,47,47,0.1);color:#d32f2f;border:1px solid rgba(211,47,47,0.25);border-radius:6px;padding:10px 14px;margin-bottom:16px;font-size:0.85rem }
    .empty-state { background:rgba(21,101,192,0.06);border:1px solid rgba(21,101,192,0.2);border-radius:6px;padding:12px 16px;color:var(--mat-sys-on-surface-variant);font-size:0.85rem }
    .group-block { margin-bottom:28px }
    .group-header { display:flex;align-items:center;gap:10px;margin-bottom:8px }
    .group-accent { width:4px;height:32px;border-radius:2px;flex-shrink:0 }
    .group-title { font-weight:700;font-size:0.9rem;line-height:1.2 }
    .group-subtitle { font-size:0.72rem;color:var(--mat-sys-on-surface-variant) }
    .skeleton-group { margin-bottom:28px }
    .skeleton-title { width:300px;height:22px;background:var(--mat-sys-surface-variant);border-radius:4px;margin-bottom:6px;animation:pulse 1.5s ease-in-out infinite }
    .skeleton-card { height:64px;background:var(--mat-sys-surface-variant);border-radius:8px;margin-bottom:8px;animation:pulse 1.5s ease-in-out infinite }
    @keyframes pulse { 0%,100% { opacity:1 } 50% { opacity:0.5 } }
    .search-field { width:300px }
  `],
})
export class GeneratorsComponent {
  private api = inject(GeneratorsApiService)
  private productSvc = inject(ProductService)

  sectionFilter = signal('All')
  search = ''

  private get apiProduct(): string {
    const product = this.productSvc.product()
    const ismsTier = this.productSvc.ismsTier()
    if (product === 'privacy') return 'privacy'
    if (product === 'cloud') return 'cloud'
    if (product === 'ai') return 'ai'
    if (ismsTier === 'framework') return 'framework'
    if (ismsTier === 'operational') return 'operational'
    return 'isms'
  }

  grouped = injectQuery(() => ({
    queryKey: ['generators-grouped', this.apiProduct, this.sectionFilter()],
    queryFn: () => firstValueFrom(this.api.grouped({
      product: this.apiProduct,
      ...(this.sectionFilter() !== 'All' ? { section: this.sectionFilter() } : {}),
    })),
  }))

  sections = computed(() => {
    const data = this.grouped.data() ?? []
    const unique = Array.from(new Set(data.map(g => g.section))).sort(sectionSort)
    return ['All', ...unique]
  })

  filtered = computed(() => {
    const data = this.grouped.data() ?? []
    const q = this.search.trim().toLowerCase()
    if (!q) return data
    return data.filter(g =>
      g.group_code.toLowerCase().includes(q) ||
      g.control_name.toLowerCase().includes(q) ||
      g.generators.some(gen =>
        gen.workbook_name.toLowerCase().includes(q) ||
        gen.document_id.toLowerCase().includes(q)
      )
    )
  })

  metrics = computed(() => {
    const data = this.grouped.data() ?? []
    const totalGroups = data.length
    const totalGenerators = data.reduce((s, g) => s + g.generators.length, 0)
    const totalSheets = data.reduce((s, g) => s + g.generators.reduce((ss, gen) => ss + gen.sheet_count, 0), 0)
    const totalStacked = data.reduce((s, g) => s + g.generators.filter(gen => gen.is_stacked).length, 0)
    return [
      { label: 'Control Groups', value: totalGroups },
      { label: 'Generators', value: totalGenerators },
      { label: 'Total Sheets', value: totalSheets },
      { label: 'Stacked', value: totalStacked },
    ]
  })

  headerSubtitle = computed(() => {
    if (this.grouped.isPending()) return 'Loading generators…'
    const m = this.metrics()
    const g = m[0].value, gen = m[1].value
    return `${gen} generator${gen !== 1 ? 's' : ''} · ${g} control group${g !== 1 ? 's' : ''}`
  })

  groupAccentColor(group: GeneratorGroup): string {
    return groupColor(group)
  }
}
