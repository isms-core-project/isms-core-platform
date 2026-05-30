import { Component, inject, signal, computed, Input } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'

import { injectQuery, injectMutation, injectQueryClient } from '@tanstack/angular-query-experimental'

import { MatButtonModule } from '@angular/material/button'
import { MatCardModule } from '@angular/material/card'
import { MatChipsModule } from '@angular/material/chips'
import { MatDialogModule, MatDialog } from '@angular/material/dialog'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatIconModule } from '@angular/material/icon'
import { MatInputModule } from '@angular/material/input'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatSelectModule } from '@angular/material/select'
import { MatTabsModule } from '@angular/material/tabs'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatCheckboxModule } from '@angular/material/checkbox'

import {
  EbiosApiService,
  EbiosStudy, EbiosFearedEvent, EbiosRiskSource,
  EbiosScenario, EbiosAttackPath, EbiosMeasure,
} from '../../api/ebios-api.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

// ─── Constants ────────────────────────────────────────────────────────────────

const STUDY_STATUS_COLORS: Record<string, string> = {
  draft: '#607D8B',
  in_progress: '#FF9800',
  complete: '#4CAF50',
}

const MEASURE_STATUS_COLORS: Record<string, string> = {
  planned: '#607D8B',
  in_progress: '#FF9800',
  implemented: '#4CAF50',
}

const GRAVITY_LABELS: Record<number, string> = {
  1: 'Low', 2: 'Medium', 3: 'High', 4: 'Critical',
}

const GRAVITY_COLORS: Record<number, string> = {
  1: '#4CAF50', 2: '#FF9800', 3: '#F44336', 4: '#9C27B0',
}

const SCALE_OPTIONS = [1, 2, 3, 4]
const ASSET_TYPES = ['primary', 'secondary', 'supporting']
const RS_CATEGORIES = ['cybercriminal', 'state_actor', 'insider', 'hacktivist', 'competitor', 'natural']
const MEASURE_STATUSES = ['planned', 'in_progress', 'implemented']
const STUDY_STATUSES = ['draft', 'in_progress', 'complete']

function toLabel(s: string): string {
  return s.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase())
}

function gravityColor(v: number | null): string {
  if (v === null) return '#607D8B'
  return GRAVITY_COLORS[v] ?? '#607D8B'
}

function gravityLabel(v: number | null): string {
  if (v === null) return '—'
  return `${v} — ${GRAVITY_LABELS[v] ?? v}`
}

function fmtDate(iso: string): string {
  const d = new Date(iso)
  return d.toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: '2-digit' })
}

function riskLevel(likelihood: number | null, gravity: number | null): number {
  return (likelihood ?? 1) * (gravity ?? 1)
}

function riskColor(level: number): string {
  return level >= 9 ? '#F44336' : level >= 4 ? '#FF9800' : '#4CAF50'
}

// ─── Create Study Dialog ──────────────────────────────────────────────────────

@Component({
  selector: 'app-ebios-create-study-dialog',
  standalone: true,
  imports: [FormsModule, MatButtonModule, MatDialogModule, MatFormFieldModule,
    MatInputModule, MatSelectModule, MatProgressSpinnerModule],
  template: `
    <h2 mat-dialog-title>New EBIOS RM Study</h2>
    <mat-dialog-content class="dlg-content dlg-content-wide">
      @if (errorMsg()) {
        <div class="alert-error">{{ errorMsg() }}</div>
      }
      <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full">
        <mat-label>Study name *</mat-label>
        <input matInput [(ngModel)]="form.name" />
      </mat-form-field>
      <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full">
        <mat-label>Description</mat-label>
        <textarea matInput [(ngModel)]="form.description" rows="2"></textarea>
      </mat-form-field>
      <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full">
        <mat-label>Scope</mat-label>
        <textarea matInput [(ngModel)]="form.scope" rows="2" placeholder="What systems and processes are in scope"></textarea>
      </mat-form-field>
      <div class="field-row">
        <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-flex">
          <mat-label>Owner</mat-label>
          <input matInput [(ngModel)]="form.owner" />
        </mat-form-field>
        <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-flex">
          <mat-label>Status</mat-label>
          <mat-select [(ngModel)]="form.status">
            @for (s of studyStatuses; track s) {
              <mat-option [value]="s">{{ toLabel(s) }}</mat-option>
            }
          </mat-select>
        </mat-form-field>
      </div>
      <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-flex">
        <mat-label>Started at</mat-label>
        <input matInput type="date" [(ngModel)]="form.started_at" />
      </mat-form-field>
    </mat-dialog-content>
    <mat-dialog-actions align="end">
      <button mat-button mat-dialog-close>Cancel</button>
      <button mat-raised-button color="primary"
        [disabled]="createMut.isPending()"
        (click)="submit()">
        @if (createMut.isPending()) {
          <mat-spinner diameter="14" class="spinner-inline" />Creating…
        } @else { Create }
      </button>
    </mat-dialog-actions>
  `,
  styles: [
    /* Dialog layout */
    `.dlg-content { display:flex;flex-direction:column;gap:14px;padding-top:8px !important }
    .dlg-content-wide { min-width:480px }
    /* Form field helpers */
    .field-full { width:100% }
    .field-row { display:flex;gap:12px }
    .field-flex { flex:1 }
    /* Spinner */
    .spinner-inline { display:inline-block;margin-right:6px }
    /* Alert */
    .alert-error { padding:10px 14px;border-radius:6px;font-size:.85rem;
      background:rgba(192,0,0,.1);border:1px solid rgba(192,0,0,.3);color:var(--mat-sys-error) }`,
  ],
})
export class EbiosCreateStudyDialogComponent {
  private api = inject(EbiosApiService)
  private qc = injectQueryClient()
  private dialog = inject(MatDialog)

  readonly studyStatuses = STUDY_STATUSES
  readonly toLabel = toLabel

  errorMsg = signal('')

  form = {
    name: '', description: '', scope: '', owner: '', status: 'draft', started_at: '',
  }

  createMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.api.create({
      name: this.form.name,
      description: this.form.description || undefined,
      scope: this.form.scope || undefined,
      owner: this.form.owner || undefined,
      status: this.form.status,
      started_at: this.form.started_at || undefined,
    })),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['ebios-studies'] })
      this.qc.invalidateQueries({ queryKey: ['ebios-summary'] })
      this.dialog.closeAll()
    },
    onError: () => this.errorMsg.set('Failed to create study.'),
  }))

  submit(): void {
    if (!this.form.name.trim()) { this.errorMsg.set('Name is required.'); return }
    this.errorMsg.set('')
    this.createMut.mutate()
  }
}

// ─── Edit Study Dialog ────────────────────────────────────────────────────────

@Component({
  selector: 'app-ebios-edit-study-dialog',
  standalone: true,
  imports: [FormsModule, MatButtonModule, MatDialogModule, MatFormFieldModule,
    MatInputModule, MatSelectModule, MatProgressSpinnerModule],
  template: `
    <h2 mat-dialog-title>Edit Study</h2>
    <mat-dialog-content class="dlg-content dlg-content-narrow">
      @if (errorMsg()) {
        <div class="alert-error">{{ errorMsg() }}</div>
      }
      <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full">
        <mat-label>Study name *</mat-label>
        <input matInput [(ngModel)]="form.name" />
      </mat-form-field>
      <div class="field-row">
        <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-flex">
          <mat-label>Owner</mat-label>
          <input matInput [(ngModel)]="form.owner" />
        </mat-form-field>
        <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-flex">
          <mat-label>Status</mat-label>
          <mat-select [(ngModel)]="form.status">
            @for (s of studyStatuses; track s) {
              <mat-option [value]="s">{{ toLabel(s) }}</mat-option>
            }
          </mat-select>
        </mat-form-field>
      </div>
    </mat-dialog-content>
    <mat-dialog-actions align="end">
      <button mat-button mat-dialog-close>Cancel</button>
      <button mat-raised-button color="primary"
        [disabled]="saveMut.isPending()"
        (click)="submit()">
        @if (saveMut.isPending()) { Saving… } @else { Save }
      </button>
    </mat-dialog-actions>
  `,
  styles: [
    /* Dialog layout */
    `.dlg-content { display:flex;flex-direction:column;gap:14px;padding-top:8px !important }
    .dlg-content-narrow { min-width:400px }
    /* Form field helpers */
    .field-full { width:100% }
    .field-row { display:flex;gap:12px }
    .field-flex { flex:1 }
    /* Alert */
    .alert-error { padding:10px 14px;border-radius:6px;font-size:.85rem;
      background:rgba(192,0,0,.1);border:1px solid rgba(192,0,0,.3);color:var(--mat-sys-error) }`,
  ],
})
export class EbiosEditStudyDialogComponent {
  @Input() study!: EbiosStudy

  private api = inject(EbiosApiService)
  private qc = injectQueryClient()
  private dialog = inject(MatDialog)

  readonly studyStatuses = STUDY_STATUSES
  readonly toLabel = toLabel

  errorMsg = signal('')

  form = { name: '', owner: '', status: 'draft' }

  ngOnInit(): void {
    this.form = { name: this.study.name, owner: this.study.owner ?? '', status: this.study.status }
  }

  saveMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.api.update(this.study.id, {
      name: this.form.name.trim(),
      status: this.form.status,
      owner: this.form.owner.trim() || undefined,
    })),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['ebios-studies'] })
      this.dialog.closeAll()
    },
    onError: () => this.errorMsg.set('Failed to update study.'),
  }))

  submit(): void {
    if (!this.form.name.trim()) { this.errorMsg.set('Name is required.'); return }
    this.errorMsg.set('')
    this.saveMut.mutate()
  }
}

// ─── W1 Feared Events Panel ───────────────────────────────────────────────────

@Component({
  selector: 'app-ebios-w1',
  standalone: true,
  imports: [FormsModule, MatButtonModule, MatDialogModule, MatFormFieldModule,
    MatInputModule, MatSelectModule, MatIconModule, MatProgressSpinnerModule,
    MatTooltipModule, MatChipsModule],
  template: `
    <div class="toolbar-row">
      <button mat-stroked-button (click)="openDlg.set(true)">
        <mat-icon>add</mat-icon> Add Feared Event
      </button>
    </div>

    <!-- Header -->
    <div class="tbl-header">
      <span class="col-flex-3">Asset / Description</span>
      <span class="col-w100">Type</span>
      <span class="col-w130">Gravity</span>
      <span class="col-w40"></span>
    </div>
    <!-- Rows -->
    <div class="tbl-body">
      @if (q.isLoading()) {
        @for (_ of [0,1,2]; track $index) { <div class="tbl-row"><div class="skel"></div></div> }
      } @else if (!q.data()?.length) {
        <div class="empty-state">
          No feared events yet.
        </div>
      } @else {
        @for (fe of q.data()!; track fe.id) {
          <div class="tbl-row">
            <div class="col-flex-3 col-min0">
              <div class="cell-primary">{{ fe.asset_name }}</div>
              @if (fe.description) {
                <div class="cell-secondary cell-truncate">{{ fe.description }}</div>
              }
            </div>
            <div class="col-w100">
              <span class="cat-chip">{{ toLabel(fe.asset_type) }}</span>
            </div>
            <div class="col-w130">
              <span [style.color]="gravityColor(fe.gravity)" class="gravity-label">{{ gravityLabel(fe.gravity) }}</span>
            </div>
            <div class="col-w40">
              <button mat-icon-button class="btn-delete-sm"
                (click)="deleteMut.mutate(fe.id)">
                <mat-icon class="icon-sm">delete</mat-icon>
              </button>
            </div>
          </div>
        }
      }
    </div>

    <!-- Add dialog -->
    @if (openDlg()) {
      <div class="overlay" (click)="openDlg.set(false)">
        <div class="dlg-panel" (click)="$event.stopPropagation()">
          <h3 class="dlg-title">Add Feared Event</h3>
          @if (errMsg()) { <div class="alert-error dlg-error-gap">{{ errMsg() }}</div> }
          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full field-mb12">
            <mat-label>Asset name *</mat-label>
            <input matInput [(ngModel)]="f.asset_name" />
          </mat-form-field>
          <div class="field-row field-mb12">
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-flex">
              <mat-label>Asset type</mat-label>
              <mat-select [(ngModel)]="f.asset_type">
                @for (t of assetTypes; track t) { <mat-option [value]="t">{{ toLabel(t) }}</mat-option> }
              </mat-select>
            </mat-form-field>
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-flex">
              <mat-label>Gravity</mat-label>
              <mat-select [(ngModel)]="f.gravity">
                @for (v of scaleOptions; track v) { <mat-option [value]="v">{{ v }} — {{ GRAVITY_LABELS[v] }}</mat-option> }
              </mat-select>
            </mat-form-field>
          </div>
          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full field-mb16">
            <mat-label>Description</mat-label>
            <textarea matInput [(ngModel)]="f.description" rows="2"></textarea>
          </mat-form-field>
          <div class="dlg-actions">
            <button mat-button (click)="openDlg.set(false)">Cancel</button>
            <button mat-raised-button color="primary" [disabled]="createMut.isPending()" (click)="submit()">
              @if (createMut.isPending()) { Adding… } @else { Add }
            </button>
          </div>
        </div>
      </div>
    }
  `,
  styles: [`
    /* Toolbar */
    .toolbar-row { display:flex;justify-content:flex-end;margin-bottom:12px }
    /* Table */
    .tbl-header { display:flex;align-items:center;gap:8px;padding:6px 16px;
      background:var(--mat-sys-surface-variant);border-radius:8px 8px 0 0;
      border:1px solid var(--mat-sys-outline-variant);border-bottom:none;
      font-size:.7rem;font-weight:600;color:var(--mat-sys-on-surface-variant);text-transform:uppercase }
    .tbl-body { border:1px solid var(--mat-sys-outline-variant);border-radius:0 0 8px 8px;overflow:hidden }
    .tbl-row { display:flex;align-items:center;gap:8px;padding:10px 16px;
      border-bottom:1px solid var(--mat-sys-outline-variant) }
    .tbl-row:last-child { border-bottom:none }
    .tbl-row:hover { background:var(--mat-sys-surface-variant) }
    .skel { height:18px;background:var(--mat-sys-surface-variant);border-radius:4px;width:100% }
    /* Column widths */
    .col-flex-3 { flex:3 }
    .col-flex-2 { flex:2 }
    .col-flex-15 { flex:1.5 }
    .col-flex-1 { flex:1 }
    .col-min0 { min-width:0 }
    .col-w40 { width:40px }
    .col-w100 { width:100px }
    .col-w130 { width:130px }
    /* Cell text styles */
    .cell-primary { font-weight:500;font-size:.82rem;overflow:hidden;text-overflow:ellipsis;white-space:nowrap }
    .cell-secondary { font-size:.65rem;color:var(--mat-sys-on-surface-variant) }
    .cell-truncate { overflow:hidden;text-overflow:ellipsis;white-space:nowrap }
    .cell-dim { font-size:.72rem;color:var(--mat-sys-on-surface-variant) }
    .cell-dim-block { font-size:.72rem;color:var(--mat-sys-on-surface-variant);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;display:block }
    .cell-small-dim { font-size:.65rem;color:var(--mat-sys-on-surface-variant) }
    .gravity-label { font-weight:700;font-size:.72rem }
    /* Chips */
    .cat-chip { display:inline-block;padding:2px 8px;border-radius:10px;font-size:.62rem;font-weight:600;
      background:var(--mat-sys-surface-variant);color:var(--mat-sys-on-surface-variant) }
    /* Delete button */
    .btn-delete-sm { color:var(--mat-sys-error);width:28px;height:28px }
    /* Empty state */
    .empty-state { padding:40px;text-align:center;color:var(--mat-sys-on-surface-variant);font-size:.875rem }
    /* Overlay dialog */
    .overlay { position:fixed;inset:0;background:rgba(0,0,0,.4);z-index:1000;display:flex;align-items:center;justify-content:center }
    .dlg-panel { background:var(--mat-sys-surface);border-radius:12px;padding:24px;min-width:480px;max-width:560px }
    .dlg-title { margin:0 0 16px }
    .dlg-actions { display:flex;justify-content:flex-end;gap:8px }
    /* Alert */
    .alert-error { padding:10px 14px;border-radius:6px;font-size:.85rem;
      background:rgba(192,0,0,.1);border:1px solid rgba(192,0,0,.3);color:var(--mat-sys-error) }
    .dlg-error-gap { margin-bottom:12px }
    /* Form field helpers */
    .field-full { width:100% }
    .field-row { display:flex;gap:12px }
    .field-flex { flex:1 }
    .field-mb12 { margin-bottom:12px }
    .field-mb16 { margin-bottom:16px }
  `],
})
export class EbiosW1Component {
  @Input() studyId!: string

  private api = inject(EbiosApiService)
  private qc = injectQueryClient()

  readonly assetTypes = ASSET_TYPES
  readonly scaleOptions = SCALE_OPTIONS
  readonly GRAVITY_LABELS = GRAVITY_LABELS
  readonly toLabel = toLabel
  readonly gravityColor = gravityColor
  readonly gravityLabel = gravityLabel

  openDlg = signal(false)
  errMsg = signal('')
  f = { asset_name: '', asset_type: 'primary', description: '', gravity: 2 }

  q = injectQuery(() => ({
    queryKey: ['ebios-study', this.studyId, 'feared-events'],
    queryFn: () => firstValueFrom(this.api.listFearedEvents(this.studyId)),
  }))

  createMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.api.createFearedEvent(this.studyId, {
      asset_name: this.f.asset_name, asset_type: this.f.asset_type,
      description: this.f.description || undefined, gravity: this.f.gravity,
    })),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['ebios-study', this.studyId, 'feared-events'] })
      this.qc.invalidateQueries({ queryKey: ['ebios-summary'] })
      this.openDlg.set(false)
      this.f = { asset_name: '', asset_type: 'primary', description: '', gravity: 2 }
      this.errMsg.set('')
    },
    onError: () => this.errMsg.set('Failed to create.'),
  }))

  deleteMut = injectMutation(() => ({
    mutationFn: (feId: string) => firstValueFrom(this.api.deleteFearedEvent(this.studyId, feId)),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['ebios-study', this.studyId, 'feared-events'] })
      this.qc.invalidateQueries({ queryKey: ['ebios-summary'] })
    },
  }))

  submit(): void {
    if (!this.f.asset_name.trim()) { this.errMsg.set('Asset name is required.'); return }
    this.errMsg.set('')
    this.createMut.mutate()
  }
}

// ─── W2 Risk Sources Panel ────────────────────────────────────────────────────

@Component({
  selector: 'app-ebios-w2',
  standalone: true,
  imports: [FormsModule, MatButtonModule, MatFormFieldModule, MatInputModule,
    MatSelectModule, MatIconModule, MatProgressSpinnerModule],
  template: `
    <div class="toolbar-row">
      <button mat-stroked-button (click)="openDlg.set(true)">
        <mat-icon>add</mat-icon> Add Risk Source
      </button>
    </div>

    <div class="tbl-header">
      <span class="col-flex-3">Name / Motivation</span>
      <span class="col-w120">Category</span>
      <span class="col-w90 col-center">Pertinence</span>
      <span class="col-w80 col-center">Activity</span>
      <span class="col-w80 col-center">Resources</span>
      <span class="col-w40"></span>
    </div>
    <div class="tbl-body">
      @if (q.isLoading()) {
        @for (_ of [0,1,2]; track $index) { <div class="tbl-row"><div class="skel"></div></div> }
      } @else if (!q.data()?.length) {
        <div class="empty-state">No risk sources yet.</div>
      } @else {
        @for (rs of q.data()!; track rs.id) {
          <div class="tbl-row">
            <div class="col-flex-3 col-min0">
              <div class="cell-primary">{{ rs.name }}</div>
              @if (rs.motivation) {
                <div class="cell-secondary cell-truncate">{{ rs.motivation }}</div>
              }
            </div>
            <div class="col-w120"><span class="cat-chip">{{ toLabel(rs.category) }}</span></div>
            <div class="col-w90 col-center"><span [style.color]="gravityColor(rs.pertinence)" class="gravity-label">{{ gravityLabel(rs.pertinence) }}</span></div>
            <div class="col-w80 col-center"><span [style.color]="gravityColor(rs.activity)" class="gravity-label">{{ gravityLabel(rs.activity) }}</span></div>
            <div class="col-w80 col-center"><span [style.color]="gravityColor(rs.resources)" class="gravity-label">{{ gravityLabel(rs.resources) }}</span></div>
            <div class="col-w40">
              <button mat-icon-button class="btn-delete-sm" (click)="deleteMut.mutate(rs.id)">
                <mat-icon class="icon-sm">delete</mat-icon>
              </button>
            </div>
          </div>
        }
      }
    </div>

    @if (openDlg()) {
      <div class="overlay" (click)="openDlg.set(false)">
        <div class="dlg-panel" (click)="$event.stopPropagation()">
          <h3 class="dlg-title">Add Risk Source</h3>
          @if (errMsg()) { <div class="alert-error dlg-error-gap">{{ errMsg() }}</div> }
          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full field-mb12">
            <mat-label>Name *</mat-label>
            <input matInput [(ngModel)]="f.name" />
          </mat-form-field>
          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full field-mb12">
            <mat-label>Category</mat-label>
            <mat-select [(ngModel)]="f.category">
              @for (c of rsCategories; track c) { <mat-option [value]="c">{{ toLabel(c) }}</mat-option> }
            </mat-select>
          </mat-form-field>
          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full field-mb12">
            <mat-label>Motivation</mat-label>
            <textarea matInput [(ngModel)]="f.motivation" rows="2"></textarea>
          </mat-form-field>
          <div class="field-row field-mb16">
            @for (field of ['pertinence','activity','resources']; track field) {
              <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-flex">
                <mat-label>{{ toLabel(field) }}</mat-label>
                <mat-select [(ngModel)]="f[field]">
                  @for (v of scaleOptions; track v) { <mat-option [value]="v">{{ v }} — {{ GRAVITY_LABELS[v] }}</mat-option> }
                </mat-select>
              </mat-form-field>
            }
          </div>
          <div class="dlg-actions">
            <button mat-button (click)="openDlg.set(false)">Cancel</button>
            <button mat-raised-button color="primary" [disabled]="createMut.isPending()" (click)="submit()">
              @if (createMut.isPending()) { Adding… } @else { Add }
            </button>
          </div>
        </div>
      </div>
    }
  `,
  styles: [`
    /* Toolbar */
    .toolbar-row { display:flex;justify-content:flex-end;margin-bottom:12px }
    /* Table */
    .tbl-header{display:flex;align-items:center;gap:8px;padding:6px 16px;
      background:var(--mat-sys-surface-variant);border-radius:8px 8px 0 0;
      border:1px solid var(--mat-sys-outline-variant);border-bottom:none;
      font-size:.7rem;font-weight:600;color:var(--mat-sys-on-surface-variant);text-transform:uppercase}
    .tbl-body{border:1px solid var(--mat-sys-outline-variant);border-radius:0 0 8px 8px;overflow:hidden}
    .tbl-row{display:flex;align-items:center;gap:8px;padding:10px 16px;
      border-bottom:1px solid var(--mat-sys-outline-variant)}
    .tbl-row:last-child{border-bottom:none}
    .tbl-row:hover{background:var(--mat-sys-surface-variant)}
    .skel{height:18px;background:var(--mat-sys-surface-variant);border-radius:4px;width:100%}
    /* Column widths */
    .col-flex-3 { flex:3 }
    .col-min0 { min-width:0 }
    .col-center { text-align:center }
    .col-w40 { width:40px }
    .col-w80 { width:80px }
    .col-w90 { width:90px }
    .col-w120 { width:120px }
    /* Cell text */
    .cell-primary { font-weight:500;font-size:.82rem;overflow:hidden;text-overflow:ellipsis;white-space:nowrap }
    .cell-secondary { font-size:.65rem;color:var(--mat-sys-on-surface-variant) }
    .cell-truncate { overflow:hidden;text-overflow:ellipsis;white-space:nowrap }
    .gravity-label { font-weight:700;font-size:.72rem }
    /* Chips */
    .cat-chip{display:inline-block;padding:2px 8px;border-radius:10px;font-size:.62rem;font-weight:600;
      background:var(--mat-sys-surface-variant);color:var(--mat-sys-on-surface-variant)}
    /* Delete button */
    .btn-delete-sm { color:var(--mat-sys-error);width:28px;height:28px }
    /* Empty state */
    .empty-state { padding:40px;text-align:center;color:var(--mat-sys-on-surface-variant);font-size:.875rem }
    /* Overlay dialog */
    .overlay{position:fixed;inset:0;background:rgba(0,0,0,.4);z-index:1000;display:flex;align-items:center;justify-content:center}
    .dlg-panel{background:var(--mat-sys-surface);border-radius:12px;padding:24px;min-width:480px;max-width:560px}
    .dlg-title { margin:0 0 16px }
    .dlg-actions { display:flex;justify-content:flex-end;gap:8px }
    /* Alert */
    .alert-error{padding:10px 14px;border-radius:6px;font-size:.85rem;
      background:rgba(192,0,0,.1);border:1px solid rgba(192,0,0,.3);color:var(--mat-sys-error)}
    .dlg-error-gap { margin-bottom:12px }
    /* Form field helpers */
    .field-full { width:100% }
    .field-row { display:flex;gap:12px }
    .field-flex { flex:1 }
    .field-mb12 { margin-bottom:12px }
    .field-mb16 { margin-bottom:16px }
  `],
})
export class EbiosW2Component {
  @Input() studyId!: string

  private api = inject(EbiosApiService)
  private qc = injectQueryClient()

  readonly rsCategories = RS_CATEGORIES
  readonly scaleOptions = SCALE_OPTIONS
  readonly GRAVITY_LABELS = GRAVITY_LABELS
  readonly toLabel = toLabel
  readonly gravityColor = gravityColor
  readonly gravityLabel = gravityLabel

  openDlg = signal(false)
  errMsg = signal('')
  f: { name: string; category: string; motivation: string; pertinence: number; activity: number; resources: number; [key: string]: string | number } = { name: '', category: 'cybercriminal', motivation: '', pertinence: 2, activity: 2, resources: 2 }

  q = injectQuery(() => ({
    queryKey: ['ebios-study', this.studyId, 'risk-sources'],
    queryFn: () => firstValueFrom(this.api.listRiskSources(this.studyId)),
  }))

  createMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.api.createRiskSource(this.studyId, {
      name: this.f.name, category: this.f.category,
      motivation: this.f.motivation || undefined,
      pertinence: this.f.pertinence, activity: this.f.activity, resources: this.f.resources,
    })),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['ebios-study', this.studyId, 'risk-sources'] })
      this.qc.invalidateQueries({ queryKey: ['ebios-summary'] })
      this.openDlg.set(false)
      this.f = { name: '', category: 'cybercriminal', motivation: '', pertinence: 2, activity: 2, resources: 2 }
      this.errMsg.set('')
    },
    onError: () => this.errMsg.set('Failed to create.'),
  }))

  deleteMut = injectMutation(() => ({
    mutationFn: (rsId: string) => firstValueFrom(this.api.deleteRiskSource(this.studyId, rsId)),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['ebios-study', this.studyId, 'risk-sources'] })
      this.qc.invalidateQueries({ queryKey: ['ebios-summary'] })
    },
  }))

  submit(): void {
    if (!this.f['name'].trim()) { this.errMsg.set('Name is required.'); return }
    this.errMsg.set('')
    this.createMut.mutate()
  }
}

// ─── W3 Strategic Scenarios Panel ────────────────────────────────────────────

@Component({
  selector: 'app-ebios-w3',
  standalone: true,
  imports: [FormsModule, MatButtonModule, MatFormFieldModule, MatInputModule,
    MatSelectModule, MatIconModule, MatProgressSpinnerModule, MatCheckboxModule],
  template: `
    <div class="toolbar-row">
      <button mat-stroked-button (click)="openDlg.set(true)">
        <mat-icon>add</mat-icon> Add Scenario
      </button>
    </div>

    <div class="tbl-header">
      <span class="col-flex-2">Name</span>
      <span class="col-flex-15">Risk Source</span>
      <span class="col-flex-15">Feared Event</span>
      <span class="col-w80 col-center">Likelihood</span>
      <span class="col-w70 col-center">Gravity</span>
      <span class="col-w70 col-center">Risk</span>
      <span class="col-w70 col-center">Retained</span>
      <span class="col-w40"></span>
    </div>
    <div class="tbl-body">
      @if (q.isLoading()) {
        @for (_ of [0,1,2]; track $index) { <div class="tbl-row"><div class="skel"></div></div> }
      } @else if (!q.data()?.length) {
        <div class="empty-state">No scenarios yet.</div>
      } @else {
        @for (sc of q.data()!; track sc.id) {
          <div class="tbl-row">
            <div class="col-flex-2 col-min0">
              <div class="cell-primary">{{ sc.name }}</div>
            </div>
            <div class="col-flex-15 col-min0">
              <span class="cell-dim-block">{{ rsName(sc.risk_source_id) }}</span>
            </div>
            <div class="col-flex-15 col-min0">
              <span class="cell-dim-block">{{ feName(sc.feared_event_id) }}</span>
            </div>
            <div class="col-w80 col-center"><span [style.color]="gravityColor(sc.likelihood)" class="gravity-label">{{ gravityLabel(sc.likelihood) }}</span></div>
            <div class="col-w70 col-center"><span [style.color]="gravityColor(sc.gravity)" class="gravity-label">{{ gravityLabel(sc.gravity) }}</span></div>
            <div class="col-w70 col-center">
              <span class="risk-chip" [style.color]="riskColor(sc.risk_level)" [style.border-color]="riskColor(sc.risk_level) + '40'" [style.background]="riskColor(sc.risk_level) + '18'">{{ sc.risk_level }}</span>
            </div>
            <div class="col-w70 col-center">
              <span [style.color]="sc.retained ? '#4CAF50' : 'var(--mat-sys-on-surface-variant)'" class="cell-dim-text">{{ sc.retained ? 'Yes' : 'No' }}</span>
            </div>
            <div class="col-w40">
              <button mat-icon-button class="btn-delete-sm" (click)="deleteMut.mutate(sc.id)">
                <mat-icon class="icon-sm">delete</mat-icon>
              </button>
            </div>
          </div>
        }
      }
    </div>

    @if (openDlg()) {
      <div class="overlay" (click)="openDlg.set(false)">
        <div class="dlg-panel" (click)="$event.stopPropagation()">
          <h3 class="dlg-title">Add Strategic Scenario</h3>
          @if (errMsg()) { <div class="alert-error dlg-error-gap">{{ errMsg() }}</div> }
          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full field-mb12">
            <mat-label>Name *</mat-label>
            <input matInput [(ngModel)]="f.name" />
          </mat-form-field>
          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full field-mb12">
            <mat-label>Description</mat-label>
            <textarea matInput [(ngModel)]="f.description" rows="2"></textarea>
          </mat-form-field>
          <div class="field-row field-mb12">
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-flex">
              <mat-label>Risk source</mat-label>
              <mat-select [(ngModel)]="f.risk_source_id">
                <mat-option value="">— None —</mat-option>
                @for (r of riskSources(); track r.id) { <mat-option [value]="r.id">{{ r.name }}</mat-option> }
              </mat-select>
            </mat-form-field>
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-flex">
              <mat-label>Feared event</mat-label>
              <mat-select [(ngModel)]="f.feared_event_id">
                <mat-option value="">— None —</mat-option>
                @for (fe of fearedEvents(); track fe.id) { <mat-option [value]="fe.id">{{ fe.asset_name }}</mat-option> }
              </mat-select>
            </mat-form-field>
          </div>
          <div class="field-row field-mb12">
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-flex">
              <mat-label>Likelihood</mat-label>
              <mat-select [(ngModel)]="f.likelihood">
                @for (v of scaleOptions; track v) { <mat-option [value]="v">{{ v }} — {{ GRAVITY_LABELS[v] }}</mat-option> }
              </mat-select>
            </mat-form-field>
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-flex">
              <mat-label>Gravity</mat-label>
              <mat-select [(ngModel)]="f.gravity">
                @for (v of scaleOptions; track v) { <mat-option [value]="v">{{ v }} — {{ GRAVITY_LABELS[v] }}</mat-option> }
              </mat-select>
            </mat-form-field>
          </div>
          <mat-checkbox [(ngModel)]="f.retained" class="checkbox-mb">Retained for treatment</mat-checkbox>
          <div class="dlg-actions">
            <button mat-button (click)="openDlg.set(false)">Cancel</button>
            <button mat-raised-button color="primary" [disabled]="createMut.isPending()" (click)="submit()">
              @if (createMut.isPending()) { Adding… } @else { Add }
            </button>
          </div>
        </div>
      </div>
    }
  `,
  styles: [`
    /* Toolbar */
    .toolbar-row { display:flex;justify-content:flex-end;margin-bottom:12px }
    /* Table */
    .tbl-header{display:flex;align-items:center;gap:8px;padding:6px 16px;
      background:var(--mat-sys-surface-variant);border-radius:8px 8px 0 0;
      border:1px solid var(--mat-sys-outline-variant);border-bottom:none;
      font-size:.7rem;font-weight:600;color:var(--mat-sys-on-surface-variant);text-transform:uppercase}
    .tbl-body{border:1px solid var(--mat-sys-outline-variant);border-radius:0 0 8px 8px;overflow:hidden}
    .tbl-row{display:flex;align-items:center;gap:8px;padding:10px 16px;border-bottom:1px solid var(--mat-sys-outline-variant)}
    .tbl-row:last-child{border-bottom:none}
    .tbl-row:hover{background:var(--mat-sys-surface-variant)}
    .skel{height:18px;background:var(--mat-sys-surface-variant);border-radius:4px;width:100%}
    /* Column widths */
    .col-flex-2 { flex:2 }
    .col-flex-15 { flex:1.5 }
    .col-min0 { min-width:0 }
    .col-center { text-align:center }
    .col-w40 { width:40px }
    .col-w70 { width:70px }
    .col-w80 { width:80px }
    /* Cell text */
    .cell-primary { font-weight:500;font-size:.82rem;overflow:hidden;text-overflow:ellipsis;white-space:nowrap }
    .cell-dim-block { font-size:.72rem;color:var(--mat-sys-on-surface-variant);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;display:block }
    .cell-dim-text { font-size:.72rem }
    .gravity-label { font-weight:700;font-size:.72rem }
    /* Chips */
    .risk-chip{display:inline-block;padding:2px 7px;border-radius:10px;font-size:.7rem;font-weight:800;border:1px solid}
    /* Delete button */
    .btn-delete-sm { color:var(--mat-sys-error);width:28px;height:28px }
    /* Empty state */
    .empty-state { padding:40px;text-align:center;color:var(--mat-sys-on-surface-variant);font-size:.875rem }
    /* Overlay dialog */
    .overlay{position:fixed;inset:0;background:rgba(0,0,0,.4);z-index:1000;display:flex;align-items:center;justify-content:center}
    .dlg-panel{background:var(--mat-sys-surface);border-radius:12px;padding:24px;min-width:520px;max-width:600px}
    .dlg-title { margin:0 0 16px }
    .dlg-actions { display:flex;justify-content:flex-end;gap:8px }
    /* Alert */
    .alert-error{padding:10px 14px;border-radius:6px;font-size:.85rem;
      background:rgba(192,0,0,.1);border:1px solid rgba(192,0,0,.3);color:var(--mat-sys-error)}
    .dlg-error-gap { margin-bottom:12px }
    /* Form field helpers */
    .field-full { width:100% }
    .field-row { display:flex;gap:12px }
    .field-flex { flex:1 }
    .field-mb12 { margin-bottom:12px }
    /* Checkbox spacing */
    .checkbox-mb { margin-bottom:16px }
  `],
})
export class EbiosW3Component {
  @Input() studyId!: string

  private api = inject(EbiosApiService)
  private qc = injectQueryClient()

  readonly scaleOptions = SCALE_OPTIONS
  readonly GRAVITY_LABELS = GRAVITY_LABELS
  readonly toLabel = toLabel
  readonly gravityColor = gravityColor
  readonly gravityLabel = gravityLabel
  readonly riskColor = riskColor

  openDlg = signal(false)
  errMsg = signal('')
  f = { name: '', description: '', risk_source_id: '', feared_event_id: '', likelihood: 2, gravity: 2, retained: false }

  q = injectQuery(() => ({
    queryKey: ['ebios-study', this.studyId, 'scenarios'],
    queryFn: () => firstValueFrom(this.api.listScenarios(this.studyId)),
  }))

  private rsQ = injectQuery(() => ({
    queryKey: ['ebios-study', this.studyId, 'risk-sources'],
    queryFn: () => firstValueFrom(this.api.listRiskSources(this.studyId)),
  }))

  private feQ = injectQuery(() => ({
    queryKey: ['ebios-study', this.studyId, 'feared-events'],
    queryFn: () => firstValueFrom(this.api.listFearedEvents(this.studyId)),
  }))

  riskSources = computed(() => this.rsQ.data() ?? [])
  fearedEvents = computed(() => this.feQ.data() ?? [])

  createMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.api.createScenario(this.studyId, {
      name: this.f.name, description: this.f.description || undefined,
      risk_source_id: this.f.risk_source_id || undefined,
      feared_event_id: this.f.feared_event_id || undefined,
      likelihood: this.f.likelihood, gravity: this.f.gravity, retained: this.f.retained,
    })),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['ebios-study', this.studyId, 'scenarios'] })
      this.qc.invalidateQueries({ queryKey: ['ebios-summary'] })
      this.openDlg.set(false)
      this.f = { name: '', description: '', risk_source_id: '', feared_event_id: '', likelihood: 2, gravity: 2, retained: false }
      this.errMsg.set('')
    },
    onError: () => this.errMsg.set('Failed to create.'),
  }))

  deleteMut = injectMutation(() => ({
    mutationFn: (scId: string) => firstValueFrom(this.api.deleteScenario(this.studyId, scId)),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['ebios-study', this.studyId, 'scenarios'] })
      this.qc.invalidateQueries({ queryKey: ['ebios-summary'] })
    },
  }))

  rsName(id: string | null): string {
    if (!id) return '—'
    return this.riskSources().find(r => r.id === id)?.name ?? '—'
  }

  feName(id: string | null): string {
    if (!id) return '—'
    return this.fearedEvents().find(f => f.id === id)?.asset_name ?? '—'
  }

  submit(): void {
    if (!this.f.name.trim()) { this.errMsg.set('Name is required.'); return }
    this.errMsg.set('')
    this.createMut.mutate()
  }
}

// ─── W4 Attack Paths Panel ────────────────────────────────────────────────────

@Component({
  selector: 'app-ebios-w4',
  standalone: true,
  imports: [FormsModule, MatButtonModule, MatFormFieldModule, MatInputModule,
    MatSelectModule, MatIconModule, MatProgressSpinnerModule, MatChipsModule, MatTooltipModule],
  template: `
    <div class="toolbar-row">
      <button mat-stroked-button (click)="openDlg.set(true)">
        <mat-icon>add</mat-icon> Add Attack Path
      </button>
    </div>

    <div class="tbl-header">
      <span class="col-flex-3">Name / Scenario</span>
      <span class="col-w100 col-center">MITRE Techs</span>
      <span class="col-w90 col-center">Difficulty</span>
      <span class="col-w110 col-center">Detectability</span>
      <span class="col-w40"></span>
    </div>
    <div class="tbl-body">
      @if (q.isLoading()) {
        @for (_ of [0,1,2]; track $index) { <div class="tbl-row"><div class="skel"></div></div> }
      } @else if (!q.data()?.length) {
        <div class="empty-state">No attack paths yet.</div>
      } @else {
        @for (ap of q.data()!; track ap.id) {
          <div class="tbl-row">
            <div class="col-flex-3 col-min0">
              <div class="cell-primary">{{ ap.name }}</div>
              <div class="cell-secondary cell-truncate">{{ scName(ap.strategic_scenario_id) }}</div>
            </div>
            <div class="col-w100 col-center">
              @if (ap.mitre_techniques.length > 0) {
                <span class="mitre-chip" [matTooltip]="ap.mitre_techniques.join(', ')">{{ ap.mitre_techniques.length }} tech{{ ap.mitre_techniques.length !== 1 ? 's' : '' }}</span>
              } @else {
                <span class="cell-dim">—</span>
              }
            </div>
            <div class="col-w90 col-center"><span [style.color]="gravityColor(ap.difficulty)" class="gravity-label">{{ gravityLabel(ap.difficulty) }}</span></div>
            <div class="col-w110 col-center"><span [style.color]="gravityColor(ap.detectability)" class="gravity-label">{{ gravityLabel(ap.detectability) }}</span></div>
            <div class="col-w40">
              <button mat-icon-button class="btn-delete-sm" (click)="deleteMut.mutate(ap.id)">
                <mat-icon class="icon-sm">delete</mat-icon>
              </button>
            </div>
          </div>
        }
      }
    </div>

    @if (openDlg()) {
      <div class="overlay" (click)="openDlg.set(false)">
        <div class="dlg-panel" (click)="$event.stopPropagation()">
          <h3 class="dlg-title">Add Attack Path</h3>
          @if (errMsg()) { <div class="alert-error dlg-error-gap">{{ errMsg() }}</div> }
          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full field-mb12">
            <mat-label>Name *</mat-label>
            <input matInput [(ngModel)]="f.name" />
          </mat-form-field>
          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full field-mb12">
            <mat-label>Description</mat-label>
            <textarea matInput [(ngModel)]="f.description" rows="2"></textarea>
          </mat-form-field>
          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full field-mb12">
            <mat-label>Linked scenario</mat-label>
            <mat-select [(ngModel)]="f.strategic_scenario_id">
              <mat-option value="">— None —</mat-option>
              @for (s of scenarios(); track s.id) { <mat-option [value]="s.id">{{ s.name }}</mat-option> }
            </mat-select>
          </mat-form-field>
          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full field-mb12">
            <mat-label>MITRE techniques (one per line, e.g. T1078)</mat-label>
            <textarea matInput [(ngModel)]="f.mitreTechniques" rows="3" placeholder="T1078&#10;T1566&#10;T1486"></textarea>
          </mat-form-field>
          <div class="field-row field-mb16">
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-flex">
              <mat-label>Difficulty</mat-label>
              <mat-select [(ngModel)]="f.difficulty">
                @for (v of scaleOptions; track v) { <mat-option [value]="v">{{ v }} — {{ GRAVITY_LABELS[v] }}</mat-option> }
              </mat-select>
            </mat-form-field>
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-flex">
              <mat-label>Detectability</mat-label>
              <mat-select [(ngModel)]="f.detectability">
                @for (v of scaleOptions; track v) { <mat-option [value]="v">{{ v }} — {{ GRAVITY_LABELS[v] }}</mat-option> }
              </mat-select>
            </mat-form-field>
          </div>
          <div class="dlg-actions">
            <button mat-button (click)="openDlg.set(false)">Cancel</button>
            <button mat-raised-button color="primary" [disabled]="createMut.isPending()" (click)="submit()">
              @if (createMut.isPending()) { Adding… } @else { Add }
            </button>
          </div>
        </div>
      </div>
    }
  `,
  styles: [`
    /* Toolbar */
    .toolbar-row { display:flex;justify-content:flex-end;margin-bottom:12px }
    /* Table */
    .tbl-header{display:flex;align-items:center;gap:8px;padding:6px 16px;
      background:var(--mat-sys-surface-variant);border-radius:8px 8px 0 0;
      border:1px solid var(--mat-sys-outline-variant);border-bottom:none;
      font-size:.7rem;font-weight:600;color:var(--mat-sys-on-surface-variant);text-transform:uppercase}
    .tbl-body{border:1px solid var(--mat-sys-outline-variant);border-radius:0 0 8px 8px;overflow:hidden}
    .tbl-row{display:flex;align-items:center;gap:8px;padding:10px 16px;border-bottom:1px solid var(--mat-sys-outline-variant)}
    .tbl-row:last-child{border-bottom:none}
    .tbl-row:hover{background:var(--mat-sys-surface-variant)}
    .skel{height:18px;background:var(--mat-sys-surface-variant);border-radius:4px;width:100%}
    /* Column widths */
    .col-flex-3 { flex:3 }
    .col-min0 { min-width:0 }
    .col-center { text-align:center }
    .col-w40 { width:40px }
    .col-w90 { width:90px }
    .col-w100 { width:100px }
    .col-w110 { width:110px }
    /* Cell text */
    .cell-primary { font-weight:500;font-size:.82rem;overflow:hidden;text-overflow:ellipsis;white-space:nowrap }
    .cell-secondary { font-size:.65rem;color:var(--mat-sys-on-surface-variant) }
    .cell-truncate { overflow:hidden;text-overflow:ellipsis;white-space:nowrap }
    .cell-dim { color:var(--mat-sys-on-surface-variant);font-size:.72rem }
    .gravity-label { font-weight:700;font-size:.72rem }
    /* Chips */
    .mitre-chip{display:inline-block;padding:2px 8px;border-radius:10px;font-size:.62rem;font-weight:600;
      background:rgba(33,150,243,.12);color:#2196F3;border:1px solid rgba(33,150,243,.25);cursor:default}
    /* Delete button */
    .btn-delete-sm { color:var(--mat-sys-error);width:28px;height:28px }
    /* Empty state */
    .empty-state { padding:40px;text-align:center;color:var(--mat-sys-on-surface-variant);font-size:.875rem }
    /* Overlay dialog */
    .overlay{position:fixed;inset:0;background:rgba(0,0,0,.4);z-index:1000;display:flex;align-items:center;justify-content:center}
    .dlg-panel{background:var(--mat-sys-surface);border-radius:12px;padding:24px;min-width:520px;max-width:600px}
    .dlg-title { margin:0 0 16px }
    .dlg-actions { display:flex;justify-content:flex-end;gap:8px }
    /* Alert */
    .alert-error{padding:10px 14px;border-radius:6px;font-size:.85rem;
      background:rgba(192,0,0,.1);border:1px solid rgba(192,0,0,.3);color:var(--mat-sys-error)}
    .dlg-error-gap { margin-bottom:12px }
    /* Form field helpers */
    .field-full { width:100% }
    .field-row { display:flex;gap:12px }
    .field-flex { flex:1 }
    .field-mb12 { margin-bottom:12px }
    .field-mb16 { margin-bottom:16px }
  `],
})
export class EbiosW4Component {
  @Input() studyId!: string

  private api = inject(EbiosApiService)
  private qc = injectQueryClient()

  readonly scaleOptions = SCALE_OPTIONS
  readonly GRAVITY_LABELS = GRAVITY_LABELS
  readonly gravityColor = gravityColor
  readonly gravityLabel = gravityLabel

  openDlg = signal(false)
  errMsg = signal('')
  f = { name: '', description: '', strategic_scenario_id: '', mitreTechniques: '', difficulty: 2, detectability: 2 }

  q = injectQuery(() => ({
    queryKey: ['ebios-study', this.studyId, 'attack-paths'],
    queryFn: () => firstValueFrom(this.api.listAttackPaths(this.studyId)),
  }))

  private scQ = injectQuery(() => ({
    queryKey: ['ebios-study', this.studyId, 'scenarios'],
    queryFn: () => firstValueFrom(this.api.listScenarios(this.studyId)),
  }))

  scenarios = computed(() => this.scQ.data() ?? [])

  createMut = injectMutation(() => ({
    mutationFn: () => {
      const techniques = this.f.mitreTechniques.split('\n').map(t => t.trim()).filter(Boolean)
      return firstValueFrom(this.api.createAttackPath(this.studyId, {
        name: this.f.name, description: this.f.description || undefined,
        strategic_scenario_id: this.f.strategic_scenario_id || undefined,
        mitre_techniques: techniques, difficulty: this.f.difficulty, detectability: this.f.detectability,
      }))
    },
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['ebios-study', this.studyId, 'attack-paths'] })
      this.qc.invalidateQueries({ queryKey: ['ebios-summary'] })
      this.openDlg.set(false)
      this.f = { name: '', description: '', strategic_scenario_id: '', mitreTechniques: '', difficulty: 2, detectability: 2 }
      this.errMsg.set('')
    },
    onError: () => this.errMsg.set('Failed to create.'),
  }))

  deleteMut = injectMutation(() => ({
    mutationFn: (apId: string) => firstValueFrom(this.api.deleteAttackPath(this.studyId, apId)),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['ebios-study', this.studyId, 'attack-paths'] })
      this.qc.invalidateQueries({ queryKey: ['ebios-summary'] })
    },
  }))

  scName(id: string | null): string {
    if (!id) return '—'
    return this.scenarios().find(s => s.id === id)?.name ?? '—'
  }

  submit(): void {
    if (!this.f.name.trim()) { this.errMsg.set('Name is required.'); return }
    this.errMsg.set('')
    this.createMut.mutate()
  }
}

// ─── W5 Security Measures Panel ──────────────────────────────────────────────

@Component({
  selector: 'app-ebios-w5',
  standalone: true,
  imports: [FormsModule, MatButtonModule, MatFormFieldModule, MatInputModule,
    MatSelectModule, MatIconModule, MatProgressSpinnerModule, MatChipsModule],
  template: `
    <div class="toolbar-row">
      <button mat-stroked-button (click)="openDlg.set(true)">
        <mat-icon>add</mat-icon> Add Measure
      </button>
    </div>

    <div class="tbl-header">
      <span class="col-flex-3">Measure / Scenario</span>
      <span class="col-w110">Status</span>
      <span class="col-flex-15">ISO Control</span>
      <span class="col-w90 col-center">Effectiveness</span>
      <span class="col-w90 col-center">Due</span>
      <span class="col-flex-1">Owner</span>
      <span class="col-w40"></span>
    </div>
    <div class="tbl-body">
      @if (q.isLoading()) {
        @for (_ of [0,1,2]; track $index) { <div class="tbl-row"><div class="skel"></div></div> }
      } @else if (!q.data()?.length) {
        <div class="empty-state">No measures yet.</div>
      } @else {
        @for (m of q.data()!; track m.id) {
          <div class="tbl-row">
            <div class="col-flex-3 col-min0">
              <div class="cell-primary">{{ m.name }}</div>
              <div class="cell-secondary cell-truncate">{{ scName(m.scenario_id) }}</div>
            </div>
            <div class="col-w110">
              <span class="status-chip" [style.color]="measureStatusColor(m.status)" [style.border-color]="measureStatusColor(m.status)+'40'" [style.background]="measureStatusColor(m.status)+'18'">{{ toLabel(m.status) }}</span>
            </div>
            <div class="col-flex-15 col-min0">
              <span class="cell-dim">{{ m.iso_control_ref ?? '—' }}</span>
            </div>
            <div class="col-w90 col-center"><span [style.color]="gravityColor(m.effectiveness)" class="gravity-label">{{ gravityLabel(m.effectiveness) }}</span></div>
            <div class="col-w90 col-center">
              <span class="cell-dim">{{ m.due_date ? fmtDate(m.due_date) : '—' }}</span>
            </div>
            <div class="col-flex-1 col-min0">
              <span class="cell-dim-block">{{ m.owner ?? '—' }}</span>
            </div>
            <div class="col-w40">
              <button mat-icon-button class="btn-delete-sm" (click)="deleteMut.mutate(m.id)">
                <mat-icon class="icon-sm">delete</mat-icon>
              </button>
            </div>
          </div>
        }
      }
    </div>

    @if (openDlg()) {
      <div class="overlay" (click)="openDlg.set(false)">
        <div class="dlg-panel" (click)="$event.stopPropagation()">
          <h3 class="dlg-title">Add Security Measure</h3>
          @if (errMsg()) { <div class="alert-error dlg-error-gap">{{ errMsg() }}</div> }
          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full field-mb12">
            <mat-label>Name *</mat-label>
            <input matInput [(ngModel)]="f.name" />
          </mat-form-field>
          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full field-mb12">
            <mat-label>Description</mat-label>
            <textarea matInput [(ngModel)]="f.description" rows="2"></textarea>
          </mat-form-field>
          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full field-mb12">
            <mat-label>Linked scenario</mat-label>
            <mat-select [(ngModel)]="f.scenario_id">
              <mat-option value="">— None —</mat-option>
              @for (s of scenarios(); track s.id) { <mat-option [value]="s.id">{{ s.name }}</mat-option> }
            </mat-select>
          </mat-form-field>
          <div class="field-row field-mb12">
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-flex">
              <mat-label>Status</mat-label>
              <mat-select [(ngModel)]="f.status">
                @for (s of measureStatuses; track s) { <mat-option [value]="s">{{ toLabel(s) }}</mat-option> }
              </mat-select>
            </mat-form-field>
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-flex">
              <mat-label>ISO control ref</mat-label>
              <input matInput [(ngModel)]="f.iso_control_ref" placeholder="e.g. A.8.7" />
            </mat-form-field>
          </div>
          <div class="field-row field-mb12">
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-flex">
              <mat-label>Effectiveness</mat-label>
              <mat-select [(ngModel)]="f.effectiveness">
                @for (v of scaleOptions; track v) { <mat-option [value]="v">{{ v }} — {{ GRAVITY_LABELS[v] }}</mat-option> }
              </mat-select>
            </mat-form-field>
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-flex">
              <mat-label>Due date</mat-label>
              <input matInput type="date" [(ngModel)]="f.due_date" />
            </mat-form-field>
          </div>
          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full field-mb16">
            <mat-label>Owner</mat-label>
            <input matInput [(ngModel)]="f.owner" />
          </mat-form-field>
          <div class="dlg-actions">
            <button mat-button (click)="openDlg.set(false)">Cancel</button>
            <button mat-raised-button color="primary" [disabled]="createMut.isPending()" (click)="submit()">
              @if (createMut.isPending()) { Adding… } @else { Add }
            </button>
          </div>
        </div>
      </div>
    }
  `,
  styles: [`
    /* Toolbar */
    .toolbar-row { display:flex;justify-content:flex-end;margin-bottom:12px }
    /* Table */
    .tbl-header{display:flex;align-items:center;gap:8px;padding:6px 16px;
      background:var(--mat-sys-surface-variant);border-radius:8px 8px 0 0;
      border:1px solid var(--mat-sys-outline-variant);border-bottom:none;
      font-size:.7rem;font-weight:600;color:var(--mat-sys-on-surface-variant);text-transform:uppercase}
    .tbl-body{border:1px solid var(--mat-sys-outline-variant);border-radius:0 0 8px 8px;overflow:hidden}
    .tbl-row{display:flex;align-items:center;gap:8px;padding:10px 16px;border-bottom:1px solid var(--mat-sys-outline-variant)}
    .tbl-row:last-child{border-bottom:none}
    .tbl-row:hover{background:var(--mat-sys-surface-variant)}
    .skel{height:18px;background:var(--mat-sys-surface-variant);border-radius:4px;width:100%}
    /* Column widths */
    .col-flex-3 { flex:3 }
    .col-flex-15 { flex:1.5 }
    .col-flex-1 { flex:1 }
    .col-min0 { min-width:0 }
    .col-center { text-align:center }
    .col-w40 { width:40px }
    .col-w90 { width:90px }
    .col-w110 { width:110px }
    /* Cell text */
    .cell-primary { font-weight:500;font-size:.82rem;overflow:hidden;text-overflow:ellipsis;white-space:nowrap }
    .cell-secondary { font-size:.65rem;color:var(--mat-sys-on-surface-variant) }
    .cell-truncate { overflow:hidden;text-overflow:ellipsis;white-space:nowrap }
    .cell-dim { font-size:.72rem;color:var(--mat-sys-on-surface-variant) }
    .cell-dim-block { font-size:.72rem;color:var(--mat-sys-on-surface-variant);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;display:block }
    .gravity-label { font-weight:700;font-size:.72rem }
    /* Chips */
    .status-chip{display:inline-block;padding:2px 8px;border-radius:10px;font-size:.62rem;font-weight:700;border:1px solid}
    /* Delete button */
    .btn-delete-sm { color:var(--mat-sys-error);width:28px;height:28px }
    /* Empty state */
    .empty-state { padding:40px;text-align:center;color:var(--mat-sys-on-surface-variant);font-size:.875rem }
    /* Overlay dialog */
    .overlay{position:fixed;inset:0;background:rgba(0,0,0,.4);z-index:1000;display:flex;align-items:center;justify-content:center}
    .dlg-panel{background:var(--mat-sys-surface);border-radius:12px;padding:24px;min-width:520px;max-width:600px}
    .dlg-title { margin:0 0 16px }
    .dlg-actions { display:flex;justify-content:flex-end;gap:8px }
    /* Alert */
    .alert-error{padding:10px 14px;border-radius:6px;font-size:.85rem;
      background:rgba(192,0,0,.1);border:1px solid rgba(192,0,0,.3);color:var(--mat-sys-error)}
    .dlg-error-gap { margin-bottom:12px }
    /* Form field helpers */
    .field-full { width:100% }
    .field-row { display:flex;gap:12px }
    .field-flex { flex:1 }
    .field-mb12 { margin-bottom:12px }
    .field-mb16 { margin-bottom:16px }
  `],
})
export class EbiosW5Component {
  @Input() studyId!: string

  private api = inject(EbiosApiService)
  private qc = injectQueryClient()

  readonly measureStatuses = MEASURE_STATUSES
  readonly scaleOptions = SCALE_OPTIONS
  readonly GRAVITY_LABELS = GRAVITY_LABELS
  readonly toLabel = toLabel
  readonly gravityColor = gravityColor
  readonly gravityLabel = gravityLabel
  readonly fmtDate = fmtDate

  openDlg = signal(false)
  errMsg = signal('')
  f = { name: '', description: '', scenario_id: '', status: 'planned', iso_control_ref: '', effectiveness: 2, due_date: '', owner: '' }

  q = injectQuery(() => ({
    queryKey: ['ebios-study', this.studyId, 'measures'],
    queryFn: () => firstValueFrom(this.api.listMeasures(this.studyId)),
  }))

  private scQ = injectQuery(() => ({
    queryKey: ['ebios-study', this.studyId, 'scenarios'],
    queryFn: () => firstValueFrom(this.api.listScenarios(this.studyId)),
  }))

  scenarios = computed(() => this.scQ.data() ?? [])

  measureStatusColor(s: string): string { return MEASURE_STATUS_COLORS[s] ?? '#607D8B' }

  createMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.api.createMeasure(this.studyId, {
      name: this.f.name, description: this.f.description || undefined,
      scenario_id: this.f.scenario_id || undefined, status: this.f.status,
      iso_control_ref: this.f.iso_control_ref || undefined, effectiveness: this.f.effectiveness,
      due_date: this.f.due_date || undefined, owner: this.f.owner || undefined,
    })),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['ebios-study', this.studyId, 'measures'] })
      this.qc.invalidateQueries({ queryKey: ['ebios-summary'] })
      this.openDlg.set(false)
      this.f = { name: '', description: '', scenario_id: '', status: 'planned', iso_control_ref: '', effectiveness: 2, due_date: '', owner: '' }
      this.errMsg.set('')
    },
    onError: () => this.errMsg.set('Failed to create.'),
  }))

  deleteMut = injectMutation(() => ({
    mutationFn: (mId: string) => firstValueFrom(this.api.deleteMeasure(this.studyId, mId)),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['ebios-study', this.studyId, 'measures'] })
      this.qc.invalidateQueries({ queryKey: ['ebios-summary'] })
    },
  }))

  scName(id: string | null): string {
    if (!id) return '—'
    return this.scenarios().find(s => s.id === id)?.name ?? '—'
  }

  submit(): void {
    if (!this.f.name.trim()) { this.errMsg.set('Name is required.'); return }
    this.errMsg.set('')
    this.createMut.mutate()
  }
}

// ─── Main EBIOS Component ─────────────────────────────────────────────────────

const WORKSHOP_TABS = [
  { label: 'W1 — Feared Events',  hint: 'Assets and feared events' },
  { label: 'W2 — Risk Sources',   hint: 'Threat actors and motivation' },
  { label: 'W3 — Scenarios',      hint: 'Strategic risk scenarios' },
  { label: 'W4 — Attack Paths',   hint: 'Operational attack paths' },
  { label: 'W5 — Measures',       hint: 'Security measures and treatment' },
]

@Component({
  selector: 'app-ebios',
  standalone: true,
  imports: [
    FormsModule,
    MatButtonModule, MatCardModule, MatChipsModule, MatDialogModule,
    MatFormFieldModule, MatIconModule, MatInputModule, MatProgressSpinnerModule,
    MatSelectModule, MatTabsModule, MatTooltipModule,
    PageHeaderComponent,
    EbiosCreateStudyDialogComponent,
    EbiosEditStudyDialogComponent,
    EbiosW1Component,
    EbiosW2Component,
    EbiosW3Component,
    EbiosW4Component,
    EbiosW5Component,
  ],
  template: `
    <app-page-header
      title="EBIOS RM"
      subtitle="ANSSI 5-workshop risk methodology — feared events, risk sources, strategic scenarios, attack paths, security measures">
      @if (!selectedStudy()) {
        <button mat-raised-button color="primary" (click)="createOpen.set(true)">
          <mat-icon>add</mat-icon> New Study
        </button>
      }
    </app-page-header>

    @if (!selectedStudy()) {
      <!-- Summary cards -->
      <div class="summary-row">
        @for (c of summaryCards(); track c.label) {
          <div class="sum-card" [style.border-color]="c.color+'30'" [style.background]="c.color+'08'">
            @if (summaryQ.isLoading()) {
              <div class="skel sum-card-skel"></div>
            } @else {
              <div class="sum-card-value" [style.color]="c.color">{{ c.value }}</div>
            }
            <div class="sum-card-label">{{ c.label }}</div>
          </div>
        }
      </div>

      <!-- Filter row -->
      <div class="filter-row">
        <mat-form-field appearance="outline" subscriptSizing="dynamic" class="filter-status">
          <mat-label>Status</mat-label>
          <mat-select [(ngModel)]="statusFilter" (ngModelChange)="onStatusFilter()">
            <mat-option value="">All</mat-option>
            @for (s of studyStatuses; track s) { <mat-option [value]="s">{{ toLabel(s) }}</mat-option> }
          </mat-select>
        </mat-form-field>
        @if (statusFilter()) {
          <button mat-button (click)="statusFilter.set('');onStatusFilter()">Clear</button>
        }
        <span class="filter-count">
          {{ studiesQ.data()?.length ?? 0 }} stud{{ studiesQ.data()?.length !== 1 ? 'ies' : 'y' }}
        </span>
      </div>

      <!-- Studies table -->
      <div class="tbl-header">
        <span class="col-flex-3">Study name</span>
        <span class="col-w110">Status</span>
        <span class="col-flex-15">Owner</span>
        <span class="col-w110 col-right">Created</span>
        <span class="col-w76"></span>
      </div>
      <div class="tbl-body">
        @if (studiesQ.isLoading()) {
          @for (_ of [0,1,2,3]; track $index) { <div class="tbl-row"><div class="skel"></div></div> }
        } @else if (!studiesQ.data()?.length) {
          <div class="empty-state-lg">
            <div class="empty-state-text">No EBIOS RM studies yet.</div>
            <button mat-stroked-button (click)="createOpen.set(true)"><mat-icon>add</mat-icon> Create first study</button>
          </div>
        } @else {
          @for (s of studiesQ.data()!; track s.id) {
            <div class="tbl-row tbl-row-click" (click)="selectedStudy.set(s)">
              <div class="col-flex-3 col-min0">
                <div class="cell-primary-bold">{{ s.name }}</div>
                @if (s.description) {
                  <div class="cell-secondary cell-truncate">{{ s.description }}</div>
                }
              </div>
              <div class="col-w110">
                <span class="status-chip" [style.color]="statusColor(s.status)" [style.border-color]="statusColor(s.status)+'40'" [style.background]="statusColor(s.status)+'18'">{{ toLabel(s.status) }}</span>
              </div>
              <div class="col-flex-15 col-min0">
                <span class="cell-dim">{{ s.owner ?? '—' }}</span>
              </div>
              <div class="col-w110 col-right">
                <span class="cell-small-dim">{{ fmtDate(s.created_at) }}</span>
              </div>
              <div class="col-w76 col-actions" (click)="$event.stopPropagation()">
                <button mat-icon-button class="btn-icon-sm" (click)="editStudy.set(s)">
                  <mat-icon class="icon-sm">edit</mat-icon>
                </button>
                <button mat-icon-button class="btn-icon-sm btn-icon-error"
                  (click)="confirmDelete(s)">
                  <mat-icon class="icon-sm">delete</mat-icon>
                </button>
              </div>
            </div>
          }
        }
      </div>
    } @else {
      <!-- Study detail view -->
      <div class="detail-header">
        <button mat-button (click)="selectedStudy.set(null)">
          <mat-icon>arrow_back</mat-icon> Back to Studies
        </button>
        <div class="detail-meta">
          <div class="detail-title-row">
            <span class="detail-title">{{ selectedStudy()!.name }}</span>
            <span class="status-chip"
              [style.color]="statusColor(selectedStudy()!.status)"
              [style.border-color]="statusColor(selectedStudy()!.status)+'40'"
              [style.background]="statusColor(selectedStudy()!.status)+'18'">
              {{ toLabel(selectedStudy()!.status) }}
            </span>
          </div>
          @if (selectedStudy()!.scope) {
            <div class="cell-dim">Scope: {{ selectedStudy()!.scope }}</div>
          }
        </div>
        @if (selectedStudy()!.owner) {
          <span class="cell-dim">Owner: {{ selectedStudy()!.owner }}</span>
        }
      </div>

      <mat-tab-group [selectedIndex]="activeTab()" (selectedIndexChange)="activeTab.set($event)"
        animationDuration="150ms" style="margin-top: 16px">
        @for (wt of workshopTabs; track $index) {
          <mat-tab [label]="wt.label"></mat-tab>
        }
      </mat-tab-group>

      <div class="workshop-hint">
        {{ workshopTabs[activeTab()].hint }}
      </div>

      @if (activeTab() === 0) { <app-ebios-w1 [studyId]="selectedStudy()!.id" /> }
      @if (activeTab() === 1) { <app-ebios-w2 [studyId]="selectedStudy()!.id" /> }
      @if (activeTab() === 2) { <app-ebios-w3 [studyId]="selectedStudy()!.id" /> }
      @if (activeTab() === 3) { <app-ebios-w4 [studyId]="selectedStudy()!.id" /> }
      @if (activeTab() === 4) { <app-ebios-w5 [studyId]="selectedStudy()!.id" /> }
    }

    <!-- Create dialog -->
    @if (createOpen()) {
      <app-ebios-create-study-dialog />
    }

    <!-- Edit dialog -->
    @if (editStudy()) {
      <app-ebios-edit-study-dialog [study]="editStudy()!" />
    }
  `,
  styles: [`
    :host { display:block;padding:24px }
    /* Summary cards */
    .summary-row { display:flex;gap:12px;flex-wrap:wrap;margin-top:16px;margin-bottom:20px }
    .sum-card { min-width:90px;padding:12px;border-radius:8px;border:1px solid }
    .sum-card-skel { width:36px;height:26px;margin-bottom:4px }
    .sum-card-value { font-size:1.4rem;font-weight:700;line-height:1 }
    .sum-card-label { font-size:.65rem;color:var(--mat-sys-on-surface-variant) }
    /* Filter row */
    .filter-row { display:flex;gap:12px;margin-bottom:16px;align-items:center }
    .filter-status { min-width:150px }
    .filter-count { margin-left:auto;font-size:.72rem;color:var(--mat-sys-on-surface-variant) }
    /* Table */
    .tbl-header { display:flex;align-items:center;gap:8px;padding:6px 16px;
      background:var(--mat-sys-surface-variant);border-radius:8px 8px 0 0;
      border:1px solid var(--mat-sys-outline-variant);border-bottom:none;
      font-size:.7rem;font-weight:600;color:var(--mat-sys-on-surface-variant);text-transform:uppercase }
    .tbl-body { border:1px solid var(--mat-sys-outline-variant);border-radius:0 0 8px 8px;overflow:hidden }
    .tbl-row { display:flex;align-items:center;gap:8px;padding:10px 16px;
      border-bottom:1px solid var(--mat-sys-outline-variant) }
    .tbl-row:last-child { border-bottom:none }
    .tbl-row:hover { background:var(--mat-sys-surface-variant) }
    .tbl-row-click { cursor:pointer }
    .skel { height:18px;background:var(--mat-sys-surface-variant);border-radius:4px;width:100% }
    /* Column widths */
    .col-flex-3 { flex:3 }
    .col-flex-15 { flex:1.5 }
    .col-min0 { min-width:0 }
    .col-right { text-align:right }
    .col-w76 { width:76px }
    .col-w110 { width:110px }
    .col-actions { display:flex;justify-content:flex-end;gap:2px }
    /* Cell text */
    .cell-primary-bold { font-weight:600;font-size:.82rem;overflow:hidden;text-overflow:ellipsis;white-space:nowrap }
    .cell-secondary { font-size:.65rem;color:var(--mat-sys-on-surface-variant) }
    .cell-truncate { overflow:hidden;text-overflow:ellipsis;white-space:nowrap }
    .cell-dim { font-size:.72rem;color:var(--mat-sys-on-surface-variant) }
    .cell-small-dim { font-size:.65rem;color:var(--mat-sys-on-surface-variant) }
    /* Chips */
    .status-chip { display:inline-block;padding:2px 8px;border-radius:10px;
      font-size:.62rem;font-weight:700;border:1px solid }
    /* Icon buttons */
    .btn-icon-sm { width:28px;height:28px }
    .btn-icon-error { color:var(--mat-sys-error) }
    /* Empty states */
    .empty-state-lg { padding:48px;text-align:center }
    .empty-state-text { font-size:.875rem;color:var(--mat-sys-on-surface-variant);margin-bottom:12px }
    /* Study detail header */
    .detail-header { display:flex;align-items:center;gap:16px;margin-bottom:20px }
    .detail-meta { flex:1 }
    .detail-title-row { display:flex;align-items:center;gap:12px }
    .detail-title { font-size:1.1rem;font-weight:700 }
    /* Workshop hint */
    .workshop-hint { font-size:.72rem;color:var(--mat-sys-on-surface-variant);margin:12px 0 16px }
  `],
})
export class EbiosComponent {
  private api = inject(EbiosApiService)
  private qc = injectQueryClient()
  private dialog = inject(MatDialog)

  readonly workshopTabs = WORKSHOP_TABS
  readonly studyStatuses = STUDY_STATUSES
  readonly toLabel = toLabel
  readonly fmtDate = fmtDate

  selectedStudy = signal<EbiosStudy | null>(null)
  activeTab = signal(0)
  createOpen = signal(false)
  editStudy = signal<EbiosStudy | null>(null)
  statusFilter = signal('')

  summaryQ = injectQuery(() => ({
    queryKey: ['ebios-summary'],
    queryFn: () => firstValueFrom(this.api.summary()),
  }))

  studiesQ = injectQuery(() => ({
    queryKey: ['ebios-studies', this.statusFilter()],
    queryFn: () => firstValueFrom(this.api.list(this.statusFilter() ? { status: this.statusFilter() } : {})),
  }))

  summaryCards = computed(() => {
    const d = this.summaryQ.data()
    return [
      { label: 'Studies',       value: d?.total_studies ?? 0,      color: '#607D8B' },
      { label: 'Feared Events', value: d?.total_feared_events ?? 0, color: '#9C27B0' },
      { label: 'Risk Sources',  value: d?.total_risk_sources ?? 0,  color: '#F44336' },
      { label: 'Scenarios',     value: d?.total_scenarios ?? 0,     color: '#FF9800' },
      { label: 'Attack Paths',  value: d?.total_attack_paths ?? 0,  color: '#2196F3' },
      { label: 'Measures',      value: d?.total_measures ?? 0,      color: '#4CAF50' },
    ]
  })

  onStatusFilter(): void {
    this.qc.invalidateQueries({ queryKey: ['ebios-studies'] })
  }

  statusColor(s: string): string { return STUDY_STATUS_COLORS[s] ?? '#607D8B' }

  deleteMut = injectMutation(() => ({
    mutationFn: (id: string) => firstValueFrom(this.api.delete(id)),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['ebios-studies'] })
      this.qc.invalidateQueries({ queryKey: ['ebios-summary'] })
    },
  }))

  confirmDelete(s: EbiosStudy): void {
    if (confirm(`Delete study "${s.name}"?`)) this.deleteMut.mutate(s.id)
  }
}
