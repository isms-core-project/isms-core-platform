import { Component, inject, signal, computed, Input, Output, EventEmitter } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'

import { injectQuery, injectMutation, injectQueryClient } from '@tanstack/angular-query-experimental'

import { MatButtonModule } from '@angular/material/button'
import { MatChipsModule } from '@angular/material/chips'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatIconModule } from '@angular/material/icon'
import { MatInputModule } from '@angular/material/input'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatSnackBar, MatSnackBarModule } from '@angular/material/snack-bar'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatDialogModule, MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog'

import {
  CustomFrameworksApiService,
  CustomFramework, CustomControl,
} from '../../api/custom-frameworks-api.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

// ─── Constants ────────────────────────────────────────────────────────────────

const PRIORITY_COLORS: Record<string, string> = {
  critical: '#9C27B0', high: '#F44336', medium: '#FF9800', low: '#4CAF50',
}

const STATUS_COLORS: Record<string, string> = {
  active: '#4CAF50', draft: '#FF9800', archived: '#607D8B',
}

function toLabel(s: string): string {
  return s.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase())
}

function fmtDate(iso: string): string {
  const d = new Date(iso)
  return d.toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: '2-digit' })
}

const EXAMPLE_YAML = `name: "My Framework"
short_code: "MY_FW"
version: "1.0"
description: "Optional description"
controls:
  - id: "MY.1.1"
    title: "Control title"
    category: "Access Control"
    priority: "high"
    iso_mappings: ["A.5.15", "A.5.16"]
    tags: ["identity", "access"]
  - id: "MY.1.2"
    title: "Another control"
    category: "Access Control"
    description: "Optional detailed description"
    priority: "medium"
    iso_mappings: ["A.8.2"]
    tags: ["data"]`

// ─── Controls Panel ───────────────────────────────────────────────────────────

@Component({
  selector: 'app-cf-controls',
  standalone: true,
  imports: [FormsModule, MatFormFieldModule, MatInputModule, MatIconModule, MatChipsModule, MatProgressSpinnerModule],
  template: `
    <div class="ctrl-search-wrap">
      <mat-form-field appearance="outline" subscriptSizing="dynamic" class="ctrl-search-field">
        <mat-label>Search controls</mat-label>
        <input matInput [(ngModel)]="search" placeholder="Filter by title, ID…" />
        <mat-icon matPrefix class="search-prefix-icon">search</mat-icon>
        @if (search) {
          <button mat-icon-button matSuffix class="btn-sm" (click)="search=''">
            <mat-icon class="icon-sm">close</mat-icon>
          </button>
        }
      </mat-form-field>
    </div>

    <!-- Header -->
    <div class="tbl-header">
      <span class="col-ctrl-id">Control ID</span>
      <span class="col-flex-3">Title</span>
      <span class="col-flex-2">Category</span>
      <span class="col-priority">Priority</span>
      <span class="col-flex-2">ISO Mappings</span>
      <span class="col-flex-2">Tags</span>
    </div>
    <div class="tbl-body">
      @if (q.isLoading()) {
        @for (_ of [0,1,2,3]; track $index) { <div class="row"><div class="skel"></div></div> }
      } @else if (!filtered().length) {
        <div class="empty-msg">
          {{ search ? 'No controls match your search.' : 'No controls in this framework.' }}
        </div>
      } @else {
        @for (ctrl of filtered(); track ctrl.id) {
          <div class="row">
            <div class="col-ctrl-id col-pt2">
              <span class="ctrl-id-badge">{{ ctrl.control_id }}</span>
            </div>
            <div class="col-flex-3 col-min0">
              <div class="ctrl-title">{{ ctrl.title }}</div>
              @if (ctrl.description) {
                <div class="ctrl-desc">{{ ctrl.description }}</div>
              }
            </div>
            <div class="col-flex-2 col-min0">
              <span class="ctrl-category">{{ ctrl.category ?? '—' }}</span>
              @if (ctrl.subcategory) {
                <div class="ctrl-desc">{{ ctrl.subcategory }}</div>
              }
            </div>
            <div class="col-priority">
              @if (ctrl.priority) {
                <span class="prio-chip" [style.color]="priorityColor(ctrl.priority)"
                  [style.background]="priorityColor(ctrl.priority)+'18'"
                  [style.border-color]="priorityColor(ctrl.priority)+'40'">{{ toLabel(ctrl.priority) }}</span>
              } @else {
                <span class="muted-sm">—</span>
              }
            </div>
            <div class="col-flex-2 col-min0">
              @if (ctrl.iso_mappings.length > 0) {
                @for (m of ctrl.iso_mappings; track m) {
                  <span class="map-chip">{{ m }}</span>
                }
              } @else {
                <span class="muted-sm">—</span>
              }
            </div>
            <div class="col-flex-2 col-min0">
              @if (ctrl.tags.length > 0) {
                @for (t of ctrl.tags; track t) {
                  <span class="tag-chip">{{ t }}</span>
                }
              } @else {
                <span class="muted-sm">—</span>
              }
            </div>
          </div>
        }
      }
    </div>
    <div class="ctrl-count">
      {{ filtered().length }} control{{ filtered().length !== 1 ? 's' : '' }}{{ search ? ' matching "' + search + '"' : '' }}
    </div>
  `,
  styles: [`
    .ctrl-search-wrap { margin-top: 12px; margin-bottom: 8px; }
    .ctrl-search-field { width: 280px; }
    .search-prefix-icon { font-size: 16px; color: var(--mat-sys-on-surface-variant); }
    .btn-sm { width: 28px; height: 28px; }
    .tbl-header { display: flex; align-items: center; gap: 8px; padding: 6px 16px;
      background: var(--mat-sys-surface-variant); border-radius: 8px 8px 0 0;
      border: 1px solid var(--mat-sys-outline-variant); border-bottom: none;
      font-size: .7rem; font-weight: 600; color: var(--mat-sys-on-surface-variant); text-transform: uppercase; }
    .tbl-body { border: 1px solid var(--mat-sys-outline-variant); border-radius: 0 0 8px 8px; overflow: hidden; }
    .row { display: flex; align-items: flex-start; gap: 8px; padding: 10px 16px; border-bottom: 1px solid var(--mat-sys-outline-variant); }
    .row:last-child { border-bottom: none; }
    .row:hover { background: var(--mat-sys-surface-variant); }
    .skel { height: 18px; background: var(--mat-sys-surface-variant); border-radius: 4px; width: 100%; }
    .prio-chip { display: inline-block; padding: 2px 7px; border-radius: 10px; font-size: .62rem; font-weight: 700; border: 1px solid; }
    .map-chip { display: inline-block; padding: 1px 6px; border-radius: 10px; font-size: .6rem; font-weight: 600;
      background: rgba(33,150,243,.12); color: #2196F3; border: 1px solid rgba(33,150,243,.25); margin-right: 4px; margin-bottom: 2px; }
    .tag-chip { display: inline-block; padding: 1px 6px; border-radius: 10px; font-size: .6rem;
      background: var(--mat-sys-surface-variant); margin-right: 4px; margin-bottom: 2px; }
    .col-ctrl-id { width: 90px; }
    .col-pt2 { padding-top: 2px; }
    .col-flex-3 { flex: 3; }
    .col-flex-2 { flex: 2; }
    .col-priority { width: 80px; }
    .col-min0 { min-width: 0; }
    .ctrl-id-badge { font-family: monospace; font-weight: 700; font-size: .72rem; color: var(--mat-sys-primary); }
    .ctrl-title { font-weight: 500; font-size: .82rem; }
    .ctrl-desc { font-size: .65rem; color: var(--mat-sys-on-surface-variant); }
    .ctrl-category { font-size: .72rem; color: var(--mat-sys-on-surface-variant); }
    .muted-sm { font-size: .72rem; color: var(--mat-sys-on-surface-variant); }
    .empty-msg { padding: 32px; text-align: center; color: var(--mat-sys-on-surface-variant); font-size: .875rem; }
    .ctrl-count { margin-top: 6px; font-size: .65rem; color: var(--mat-sys-on-surface-variant); }
  `],
})
export class CfControlsComponent {
  @Input() frameworkId!: string

  private api = inject(CustomFrameworksApiService)

  readonly toLabel = toLabel
  readonly priorityColor = (p: string) => PRIORITY_COLORS[p.toLowerCase()] ?? '#607D8B'

  search = ''

  q = injectQuery(() => ({
    queryKey: ['custom-framework-controls', this.frameworkId, this.search],
    queryFn: () => firstValueFrom(this.api.listControls(this.frameworkId, this.search ? { search: this.search } : {})),
  }))

  filtered = computed(() => this.q.data() ?? [])
}

// ─── Confirm Dialog ───────────────────────────────────────────────────────────

@Component({
  selector: 'app-cf-confirm-dialog',
  standalone: true,
  imports: [MatButtonModule, MatDialogModule],
  template: `
    <h2 mat-dialog-title>{{ data.title }}</h2>
    <mat-dialog-content>{{ data.message }}</mat-dialog-content>
    <mat-dialog-actions>
      <button mat-button [mat-dialog-close]="false">Cancel</button>
      <button mat-raised-button color="warn" [mat-dialog-close]="true">{{ data.confirmLabel ?? 'Delete' }}</button>
    </mat-dialog-actions>
  `,
})
export class CfConfirmDialogComponent {
  readonly data = inject<{ title: string; message: string; confirmLabel?: string }>(MAT_DIALOG_DATA)
}

// ─── Import Dialog ────────────────────────────────────────────────────────────

@Component({
  selector: 'app-cf-import-dialog',
  standalone: true,
  imports: [FormsModule, MatButtonModule, MatDialogModule, MatFormFieldModule, MatInputModule, MatIconModule, MatProgressSpinnerModule],
  template: `
    <h2 mat-dialog-title>Import Custom Framework</h2>

    <mat-dialog-content class="import-dialog-content">
      @if (errMsg()) {
        <div class="alert-error dlg-error-mb">{{ errMsg() }}</div>
      }

      <div class="dlg-hint-row">
        <span class="dlg-hint">Paste your framework YAML below.</span>
        <button mat-button class="dlg-example-btn" (click)="showExample.set(!showExample())">
          <mat-icon class="icon-sm">{{ showExample() ? 'expand_less' : 'code' }}</mat-icon>
          {{ showExample() ? 'Hide example' : 'Show example' }}
        </button>
      </div>

      @if (showExample()) {
        <div class="example-box">
          <pre class="example-pre">{{ EXAMPLE_YAML }}</pre>
          <button mat-button class="example-use-btn" (click)="useExample()">Use this example</button>
        </div>
      }

      <mat-form-field appearance="outline" subscriptSizing="dynamic" class="yaml-field">
        <mat-label>YAML content</mat-label>
        <textarea matInput [(ngModel)]="yamlContent" rows="18"
          class="yaml-textarea"
          [placeholder]="EXAMPLE_YAML"></textarea>
      </mat-form-field>
    </mat-dialog-content>

    <mat-dialog-actions>
      <button mat-button [disabled]="importMut.isPending()" mat-dialog-close>Cancel</button>
      <button mat-raised-button color="primary" [disabled]="importMut.isPending()" (click)="doImport()">
        {{ importMut.isPending() ? 'Importing…' : 'Import Framework' }}
      </button>
    </mat-dialog-actions>
  `,
  styles: [`
    .import-dialog-content { min-width: 600px; max-width: 720px; padding-top: 8px !important; }
    .dlg-error-mb { margin-bottom: 12px; }
    .dlg-hint-row { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; }
    .dlg-hint { font-size: .78rem; color: var(--mat-sys-on-surface-variant); }
    .dlg-example-btn { margin-left: auto; font-size: .72rem; }
    .example-box { padding: 12px; border-radius: 6px; border: 1px solid var(--mat-sys-outline-variant); background: var(--mat-sys-surface-container); margin-bottom: 12px; }
    .example-pre { font-size: .72rem; color: var(--mat-sys-on-surface-variant); margin: 0; white-space: pre-wrap; }
    .example-use-btn { margin-top: 8px; font-size: .72rem; }
    .yaml-field { width: 100%; margin-bottom: 4px; }
    .yaml-textarea { font-family: monospace; font-size: .78rem; }
    .alert-error { padding: 10px 14px; border-radius: 6px; font-size: .85rem; background: rgba(192,0,0,.1); border: 1px solid rgba(192,0,0,.3); color: var(--mat-sys-error); }
  `],
})
export class CfImportDialogComponent {
  private dialogRef = inject(MatDialogRef<CfImportDialogComponent>)
  private api = inject(CustomFrameworksApiService)
  private qc = injectQueryClient()

  readonly EXAMPLE_YAML = EXAMPLE_YAML

  showExample = signal(false)
  errMsg = signal('')
  yamlContent = ''

  importMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.api.importYaml(this.yamlContent)),
    onSuccess: (fw: CustomFramework) => {
      this.qc.invalidateQueries({ queryKey: ['custom-frameworks'] })
      this.dialogRef.close(`Framework imported: ${fw.control_count} control${fw.control_count !== 1 ? 's' : ''}`)
      this.yamlContent = ''
      this.errMsg.set('')
    },
    onError: (e: unknown) => {
      const msg = (e as { error?: { detail?: string } })?.error?.detail
      this.errMsg.set(msg ?? 'Import failed. Check your YAML format.')
    },
  }))

  doImport(): void {
    if (!this.yamlContent.trim()) { this.errMsg.set('YAML content is required.'); return }
    this.errMsg.set('')
    this.importMut.mutate()
  }

  useExample(): void { this.yamlContent = EXAMPLE_YAML; this.showExample.set(false) }
}

// ─── Main Component ───────────────────────────────────────────────────────────

@Component({
  selector: 'app-custom-frameworks',
  standalone: true,
  imports: [
    FormsModule,
    MatButtonModule, MatChipsModule, MatFormFieldModule, MatIconModule,
    MatInputModule, MatProgressSpinnerModule, MatSnackBarModule, MatTooltipModule,
    MatDialogModule,
    PageHeaderComponent,
    CfControlsComponent,
  ],
  template: `
    <app-page-header
      title="Custom Frameworks"
      subtitle="Import sector-specific or custom control frameworks via YAML">
      <button mat-raised-button color="primary" size="small" (click)="openImportDialog()">
        <mat-icon>add</mat-icon> Import Framework
      </button>
    </app-page-header>

    @if (q.isError()) {
      <div class="error-banner">Failed to load frameworks.</div>
    }

    <!-- Stats strip -->
    @if (!q.isLoading() && q.data()?.length) {
      <div class="stats-strip">
        @for (c of statsCards(); track c.label) {
          <div class="stat-card" [style.border-color]="c.color+'30'" [style.background]="c.color+'08'">
            <div class="stat-value" [style.color]="c.color">{{ c.value }}</div>
            <div class="stat-label">{{ c.label }}</div>
          </div>
        }
      </div>
    }

    <!-- Loading -->
    @if (q.isLoading()) {
      @for (_ of [0,1,2]; track $index) {
        <div class="skel-card">
          <div class="skel skel-title"></div>
          <div class="skel skel-subtitle"></div>
        </div>
      }
    }

    <!-- Empty -->
    @if (!q.isLoading() && !q.data()?.length) {
      <div class="empty-state">
        <div class="empty-msg">
          No custom frameworks yet. Import one using the button above.
        </div>
        <button mat-stroked-button (click)="openImportDialog()"><mat-icon>add</mat-icon> Import first framework</button>
      </div>
    }

    <!-- Framework cards -->
    @for (fw of q.data() ?? []; track fw.id) {
      <div class="fw-card fw-card-mb">
        <!-- Card header -->
        <div class="fw-header" (click)="toggleExpanded(fw.id)">
          <span class="short-code-badge">{{ fw.short_code }}</span>
          <div class="fw-meta">
            <div class="fw-name-row">
              <span class="fw-name">{{ fw.name }}</span>
              <span class="fw-version">v{{ fw.version }}</span>
            </div>
            @if (fw.description) {
              <div class="fw-desc">{{ fw.description }}</div>
            }
          </div>
          <span [matTooltip]="fw.control_count + ' controls'" class="count-chip">{{ fw.control_count }} ctrl{{ fw.control_count !== 1 ? 's' : '' }}</span>
          <span class="status-chip" [style.color]="statusColor(fw.status)" [style.background]="statusColor(fw.status)+'18'" [style.border-color]="statusColor(fw.status)+'40'">{{ toLabel(fw.status) }}</span>
          <span class="fw-date">{{ fmtDate(fw.created_at) }}</span>
          <button mat-icon-button class="btn-sm btn-shrink" (click)="$event.stopPropagation();toggleExpanded(fw.id)">
            <mat-icon class="icon-md">{{ expandedIds().has(fw.id) ? 'expand_less' : 'expand_more' }}</mat-icon>
          </button>
          <button mat-icon-button class="btn-sm btn-shrink btn-danger"
            (click)="$event.stopPropagation();confirmDelete(fw)">
            <mat-icon class="icon-sm">delete</mat-icon>
          </button>
        </div>

        <!-- Expanded controls -->
        @if (expandedIds().has(fw.id)) {
          <div class="fw-controls-panel">
            <app-cf-controls [frameworkId]="fw.id" />
          </div>
        }
      </div>
    }

  `,
  styles: [`
    :host { display: block; padding: 24px; }
    .skel { background: var(--mat-sys-surface-variant); border-radius: 4px; }
    .skel-card { border: 1px solid var(--mat-sys-outline-variant); border-radius: 8px; padding: 16px; margin-bottom: 12px; }
    .skel-title { width: 40%; height: 22px; margin-bottom: 8px; }
    .skel-subtitle { width: 60%; height: 14px; }
    .stat-card { min-width: 90px; padding: 12px; border-radius: 8px; border: 1px solid; }
    .stats-strip { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 20px; }
    .stat-value { font-size: 1.4rem; font-weight: 700; line-height: 1; }
    .stat-label { font-size: .65rem; color: var(--mat-sys-on-surface-variant); }
    .fw-card { border: 1px solid var(--mat-sys-outline-variant); border-radius: 8px; overflow: hidden; }
    .fw-card-mb { margin-bottom: 12px; }
    .fw-header { display: flex; align-items: center; gap: 12px; padding: 16px; cursor: pointer; transition: background .12s; }
    .fw-header:hover { background: var(--mat-sys-surface-variant); }
    .fw-meta { flex: 1; min-width: 0; }
    .fw-name-row { display: flex; align-items: center; gap: 8px; }
    .fw-name { font-weight: 700; font-size: .88rem; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .fw-version { font-size: .65rem; color: var(--mat-sys-on-surface-variant); }
    .fw-desc { font-size: .72rem; color: var(--mat-sys-on-surface-variant); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .fw-date { font-size: .65rem; color: var(--mat-sys-on-surface-variant); min-width: 70px; text-align: right; }
    .short-code-badge { padding: 2px 8px; border-radius: 4px; background: var(--mat-sys-primary); color: var(--mat-sys-on-primary);
      font-family: monospace; font-size: .65rem; font-weight: 700; white-space: nowrap; flex-shrink: 0; }
    .count-chip { display: inline-block; padding: 2px 8px; border-radius: 10px; font-size: .62rem; font-weight: 600;
      background: rgba(96,125,139,.12); color: #607D8B; border: 1px solid rgba(96,125,139,.25); cursor: default; }
    .status-chip { display: inline-block; padding: 2px 8px; border-radius: 10px; font-size: .62rem; font-weight: 700; border: 1px solid; flex-shrink: 0; }
    .btn-sm { width: 28px; height: 28px; }
    .btn-shrink { flex-shrink: 0; }
    .btn-danger { color: var(--mat-sys-error); }
    .fw-controls-panel { padding: 0 16px 16px; border-top: 1px solid var(--mat-sys-outline-variant); }
    .error-banner { padding: 10px 14px; border-radius: 6px; font-size: .85rem; background: rgba(192,0,0,.08); border: 1px solid rgba(192,0,0,.2); margin-bottom: 16px; }
    .empty-state { padding: 64px; text-align: center; border: 1px dashed rgba(255,255,255,0.18); border-radius: 8px; background: var(--mat-sys-surface-container); }
    .empty-msg { font-size: .875rem; color: var(--mat-sys-on-surface-variant); margin-bottom: 12px; }
  `],
})
export class CustomFrameworksComponent {
  private api = inject(CustomFrameworksApiService)
  private qc = injectQueryClient()
  private snackBar = inject(MatSnackBar)
  private dialog = inject(MatDialog)

  readonly toLabel = toLabel
  readonly fmtDate = fmtDate
  readonly statusColor = (s: string) => STATUS_COLORS[s] ?? '#607D8B'

  expandedIds = signal<Set<string>>(new Set())

  q = injectQuery(() => ({
    queryKey: ['custom-frameworks'],
    queryFn: () => firstValueFrom(this.api.list()),
  }))

  statsCards = computed(() => {
    const data = this.q.data() ?? []
    return [
      { label: 'Frameworks',    value: data.length,                              color: '#607D8B' },
      { label: 'Total Controls', value: data.reduce((s, f) => s + f.control_count, 0), color: '#2196F3' },
      { label: 'Active',        value: data.filter(f => f.status === 'active').length, color: '#4CAF50' },
    ]
  })

  deleteMut = injectMutation(() => ({
    mutationFn: (id: string) => firstValueFrom(this.api.delete(id)),
    onSuccess: () => this.qc.invalidateQueries({ queryKey: ['custom-frameworks'] }),
  }))

  toggleExpanded(id: string): void {
    const s = new Set(this.expandedIds())
    if (s.has(id)) s.delete(id)
    else s.add(id)
    this.expandedIds.set(s)
  }

  confirmDelete(fw: CustomFramework): void {
    const ref = this.dialog.open(CfConfirmDialogComponent, {
      data: {
        title: 'Delete Framework',
        message: `Delete framework "${fw.name}"? This will remove all ${fw.control_count} controls.`,
        confirmLabel: 'Delete',
      },
    })
    ref.afterClosed().subscribe((confirmed: boolean) => {
      if (confirmed) this.deleteMut.mutate(fw.id)
    })
  }

  openImportDialog(): void {
    const ref = this.dialog.open(CfImportDialogComponent, { maxWidth: '760px', width: '100%' })
    ref.afterClosed().subscribe((msg: string | undefined) => {
      if (msg) this.snackBar.open(msg, 'Dismiss', { duration: 4000, horizontalPosition: 'center', verticalPosition: 'bottom' })
    })
  }
}
