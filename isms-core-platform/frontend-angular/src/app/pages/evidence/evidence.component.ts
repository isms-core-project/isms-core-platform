import { Component, inject, signal, computed } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'

import { injectQuery, injectMutation, injectQueryClient } from '@tanstack/angular-query-experimental'

import { MatCardModule } from '@angular/material/card'
import { MatTableModule } from '@angular/material/table'
import { MatCheckboxModule } from '@angular/material/checkbox'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatButtonModule } from '@angular/material/button'
import { MatIconModule } from '@angular/material/icon'
import { MatChipsModule } from '@angular/material/chips'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatSortModule } from '@angular/material/sort'
import { MatPaginatorModule } from '@angular/material/paginator'
import { MatDialogModule, MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog'

import { EvidenceApiService } from '../../api/evidence-api.service'
import { ProductService } from '../../core/services/product.service'
import { ProjectService } from '../../core/services/project.service'
import { ThemeService } from '../../core/services/theme.service'
import { EvidenceRead } from '../../shared/types'
import { PageHeaderComponent } from '../../shared/components/page-header.component'
import { MetricCardComponent } from '../../shared/components/metric-card.component'
import { StatusChipComponent } from '../../shared/components/status-chip.component'

// ─── Helpers ──────────────────────────────────────────────────────────────────

const EVIDENCE_TYPES = [
  'document', 'screenshot', 'log_extract', 'config_export',
  'test_result', 'attestation', 'threat_intel',
]

function formatBytes(bytes: number): string {
  if (bytes < 1024)         return `${bytes} B`
  if (bytes < 1024 * 1024)  return `${(bytes / 1024).toFixed(1)} KB`
  return `${(bytes / 1024 / 1024).toFixed(1)} MB`
}

function isExpired(date: string | null): boolean {
  if (!date) return false
  return new Date(date) < new Date()
}

function isExpiringSoon(date: string | null): boolean {
  if (!date || isExpired(date)) return false
  const threshold = new Date()
  threshold.setDate(threshold.getDate() + 30)
  return new Date(date) <= threshold
}

function fmtDate(d: string | null | undefined): string {
  if (!d) return '—'
  return new Date(d).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' })
}

type FilterTab = 'all' | 'valid' | 'expiring' | 'expired' | 'unverified'

// ─── Reject Evidence Dialog ───────────────────────────────────────────────────

export interface RejectEvidenceDialogData { itemName?: string }
export interface RejectEvidenceDialogResult { reason: string }

@Component({
  selector: 'app-reject-evidence-dialog',
  standalone: true,
  imports: [FormsModule, MatButtonModule, MatFormFieldModule, MatInputModule, MatDialogModule],
  template: `
    <h2 mat-dialog-title>Reject Evidence</h2>
    <mat-dialog-content>
      @if (data.itemName) {
        <p class="dialog-body-text">{{ data.itemName }}</p>
      }
      <mat-form-field appearance="outline" class="form-full">
        <mat-label>Reason (optional)</mat-label>
        <textarea matInput [(ngModel)]="reason" rows="3"></textarea>
      </mat-form-field>
    </mat-dialog-content>
    <mat-dialog-actions>
      <button mat-stroked-button [mat-dialog-close]="false">Cancel</button>
      <button mat-raised-button color="warn" (click)="confirm()">Reject</button>
    </mat-dialog-actions>
  `,
  styles: [`
    .dialog-body-text { font-size: 0.875rem; color: var(--mat-sys-on-surface-variant); margin: 0 0 12px; }
    .form-full { width: 100%; }
  `],
})
export class RejectEvidenceDialogComponent {
  readonly data = inject<RejectEvidenceDialogData>(MAT_DIALOG_DATA)
  private dialogRef = inject(MatDialogRef<RejectEvidenceDialogComponent>)

  reason = ''

  confirm(): void {
    this.dialogRef.close({ reason: this.reason } satisfies RejectEvidenceDialogResult)
  }
}

// ─── Upload Evidence Dialog ───────────────────────────────────────────────────

const ACCEPT_TYPES = '.pdf,.docx,.xlsx,.csv,.txt,.jpg,.jpeg,.png,.json,.md'

@Component({
  selector: 'app-upload-evidence-dialog',
  standalone: true,
  imports: [FormsModule, MatButtonModule, MatFormFieldModule, MatInputModule, MatSelectModule, MatIconModule, MatDialogModule],
  template: `
    <h2 mat-dialog-title>Upload Evidence</h2>
    <mat-dialog-content>
      <!-- File picker -->
      <input #fileInput type="file" [accept]="ACCEPT" style="display:none" (change)="onFileSelected($event)" />
      <div class="file-pick-row">
        <button mat-stroked-button type="button" (click)="fileInput.click()">
          <mat-icon>attach_file</mat-icon>
          Choose File
        </button>
        <span class="file-name">{{ selectedFile ? selectedFile.name : 'No file chosen' }}</span>
      </div>

      <mat-form-field appearance="outline" class="form-full">
        <mat-label>Title *</mat-label>
        <input matInput [(ngModel)]="title" placeholder="Descriptive title for this evidence" />
      </mat-form-field>

      <mat-form-field appearance="outline" class="form-full">
        <mat-label>Evidence Type *</mat-label>
        <mat-select [(ngModel)]="evidenceType">
          <mat-option value="document">Document</mat-option>
          <mat-option value="screenshot">Screenshot</mat-option>
          <mat-option value="log_extract">Log Extract</mat-option>
          <mat-option value="config_export">Config Export</mat-option>
          <mat-option value="test_result">Test Result</mat-option>
          <mat-option value="attestation">Attestation</mat-option>
        </mat-select>
      </mat-form-field>

      <mat-form-field appearance="outline" class="form-full">
        <mat-label>Control Group Code *</mat-label>
        <input matInput [(ngModel)]="groupCode" placeholder="e.g. a.8.8" />
        <mat-hint>Enter the Annex A control code</mat-hint>
      </mat-form-field>

      <mat-form-field appearance="outline" class="form-full">
        <mat-label>Notes</mat-label>
        <textarea matInput [(ngModel)]="notes" rows="2"></textarea>
      </mat-form-field>
    </mat-dialog-content>
    <mat-dialog-actions>
      <button mat-stroked-button [mat-dialog-close]="null">Cancel</button>
      <button mat-raised-button (click)="submit()" [disabled]="!canSubmit()">Upload</button>
    </mat-dialog-actions>
  `,
  styles: [`
    .form-full { width: 100%; margin-top: 12px; }
    .file-pick-row { display: flex; align-items: center; gap: 12px; margin-bottom: 4px; }
    .file-name { font-size: 0.82rem; color: var(--mat-sys-on-surface-variant); word-break: break-all; }
  `],
})
export class UploadEvidenceDialogComponent {
  readonly data = inject<{ projectId?: string }>(MAT_DIALOG_DATA)
  private dialogRef = inject(MatDialogRef<UploadEvidenceDialogComponent>)

  readonly ACCEPT = ACCEPT_TYPES
  selectedFile: File | null = null
  title       = ''
  evidenceType = 'document'
  groupCode   = ''
  notes       = ''

  onFileSelected(event: Event): void {
    const file = (event.target as HTMLInputElement).files?.[0]
    if (!file) return
    this.selectedFile = file
    if (!this.title) {
      this.title = file.name.replace(/\.[^/.]+$/, '').replace(/[_-]/g, ' ')
    }
  }

  canSubmit(): boolean {
    return !!this.selectedFile && !!this.title.trim() && !!this.groupCode.trim()
  }

  submit(): void {
    if (!this.canSubmit()) return
    const fd = new FormData()
    fd.append('file', this.selectedFile!)
    fd.append('title', this.title.trim())
    fd.append('evidence_type', this.evidenceType)
    fd.append('group_code', this.groupCode.trim().toLowerCase())
    if (this.notes.trim()) fd.append('notes', this.notes.trim())
    if (this.data.projectId) fd.append('project_id', this.data.projectId)
    this.dialogRef.close(fd)
  }
}

// ─── Bulk Delete Confirm Dialog ───────────────────────────────────────────────

export interface BulkDeleteConfirmDialogData { count: number }

@Component({
  selector: 'app-bulk-delete-confirm-dialog',
  standalone: true,
  imports: [MatButtonModule, MatDialogModule],
  template: `
    <h2 mat-dialog-title>Delete {{ data.count }} evidence items?</h2>
    <mat-dialog-content>
      <p class="dialog-body-text">This will permanently delete the selected evidence items. This action cannot be undone.</p>
    </mat-dialog-content>
    <mat-dialog-actions>
      <button mat-stroked-button [mat-dialog-close]="false">Cancel</button>
      <button mat-raised-button color="warn" [mat-dialog-close]="true">Delete All</button>
    </mat-dialog-actions>
  `,
  styles: [`
    .dialog-body-text { font-size: 0.875rem; color: var(--mat-sys-on-surface-variant); margin: 0; }
  `],
})
export class BulkDeleteConfirmDialogComponent {
  readonly data = inject<BulkDeleteConfirmDialogData>(MAT_DIALOG_DATA)
}

// ─── Evidence Component ───────────────────────────────────────────────────────
@Component({
  selector: 'app-evidence',
  standalone: true,
  imports: [
    FormsModule,
    MatCardModule, MatTableModule, MatCheckboxModule,
    MatFormFieldModule, MatInputModule, MatSelectModule,
    MatButtonModule, MatIconModule, MatChipsModule,
    MatTooltipModule,
    MatSortModule, MatPaginatorModule,
    MatDialogModule,
    PageHeaderComponent, MetricCardComponent, StatusChipComponent,
    UploadEvidenceDialogComponent,
  ],
  template: `
    <app-page-header [title]="'Evidence Tracker'" [subtitle]="headerSubtitle()">
      <div actions>
        <button mat-stroked-button (click)="openUploadDialog()" [disabled]="uploadMutation.isPending()">
          <mat-icon>upload_file</mat-icon>
          Upload Evidence
        </button>
      </div>
    </app-page-header>

    <!-- Metric cards -->
    <div class="metrics-row">
      <app-metric-card title="Total"        [value]="allItems().length" icon="assignment" />
      <app-metric-card title="Drafts"       [value]="draftCount()" />
      <app-metric-card title="Pending Review" [value]="pendingCount()" />
      <app-metric-card title="Expired"      [value]="expiredItems().length" icon="error_outline" />
      <app-metric-card title="Expiring ≤30d" [value]="expiringSoonItems().length" icon="warning_amber" />
      <app-metric-card
        title="Verified"
        [value]="verifiedCount()"
        [subtitle]="allItems().length ? (Math.round(verifiedCount() / allItems().length * 100) + '% of total') : ''"
        icon="check_circle_outline"
        [progress]="allItems().length ? verifiedCount() / allItems().length * 100 : 0"
        progressColor="primary"
      />
    </div>

    <!-- Expiry alert -->
    @if (expiredItems().length > 0 || expiringSoonItems().length > 0) {
      <div class="alert" [class.alert-error]="expiredItems().length > 0" [class.alert-warn]="expiredItems().length === 0">
        @if (expiredItems().length > 0) {
          {{ expiredItems().length }} evidence item{{ expiredItems().length > 1 ? 's have' : ' has' }} expired.
        }
        @if (expiringSoonItems().length > 0) {
          {{ expiringSoonItems().length }} item{{ expiringSoonItems().length > 1 ? 's are' : ' is' }} expiring within 30 days.
        }
        Review expiry dates in the table below.
      </div>
    }

    @if (draftCount() > 0) {
      <div class="alert alert-warn">
        {{ draftCount() }} evidence item{{ draftCount() > 1 ? 's are' : ' is' }} in draft status — assign them to a control group to activate.
      </div>
    }

    @if (evidenceQuery.isError()) {
      <div class="alert alert-error">Failed to load evidence.</div>
    }

    @if (allItems().length === 0 && !evidenceQuery.isLoading()) {
      <div class="alert alert-info">No evidence uploaded yet. Use Upload Evidence to add files.</div>
    }

    <!-- Filters -->
    @if (allItems().length > 0) {
      <mat-card class="filter-card">
        <mat-card-content>
          <div class="filter-row">
            <!-- Tab filter -->
            <div class="tab-group">
              @for (tab of filterTabs; track tab.value) {
                <div
                  class="tab-btn"
                  [class.tab-btn--active]="filterTab() === tab.value"
                  [style.color]="tab.warn && filterTab() !== tab.value ? tab.warn : undefined"
                  (click)="filterTab.set(tab.value)"
                >{{ tab.label }}{{ tab.count !== undefined ? ' (' + tab.count() + ')' : '' }}</div>
              }
            </div>

            <!-- Status -->
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="isms-select-md">
              <mat-label>Status</mat-label>
              <mat-select [ngModel]="statusFilter()" (ngModelChange)="statusFilter.set($event)">
                <mat-option value="">All statuses</mat-option>
                <mat-option value="draft">Draft</mat-option>
                <mat-option value="pending_review">Pending Review</mat-option>
                <mat-option value="active">Active</mat-option>
                <mat-option value="approved">Approved</mat-option>
                <mat-option value="rejected">Rejected</mat-option>
              </mat-select>
            </mat-form-field>

            <!-- Type -->
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="isms-select-md">
              <mat-label>Type</mat-label>
              <mat-select [ngModel]="typeFilter()" (ngModelChange)="typeFilter.set($event)">
                <mat-option value="">All types</mat-option>
                @for (t of evidenceTypes; track t) {
                  <mat-option [value]="t">{{ t.replace(/_/g, ' ') }}</mat-option>
                }
              </mat-select>
            </mat-form-field>

            <!-- Search -->
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="isms-search-field">
              <mat-label>Search evidence</mat-label>
              <mat-icon matPrefix class="icon-md">search</mat-icon>
              <input matInput [ngModel]="search()" (ngModelChange)="search.set($event)" placeholder="title, group code…" />
            </mat-form-field>
          </div>

          <!-- Bulk actions bar -->
          @if (selectedIds().size > 0) {
            <div class="bulk-bar">
              <span class="bulk-count">{{ selectedIds().size }} selected</span>
              <button mat-stroked-button color="warn" (click)="confirmBulkDelete()" [disabled]="bulkDeleteMutation.isPending()">
                <mat-icon>delete</mat-icon>
                Delete selected
              </button>
              <button mat-button (click)="clearSelection()">Clear</button>
            </div>
          }
        </mat-card-content>
      </mat-card>
    }

    <!-- Table -->
    @if (filteredItems().length > 0) {
      <mat-card class="table-card">
        <table mat-table [dataSource]="filteredItems()" class="full-table">

          <!-- Checkbox -->
          <ng-container matColumnDef="select">
            <th mat-header-cell *matHeaderCellDef>
              <mat-checkbox
                [checked]="allSelected()"
                [indeterminate]="someSelected()"
                (change)="toggleAll($event.checked)"
              />
            </th>
            <td mat-cell *matCellDef="let ev" (click)="$event.stopPropagation()">
              <mat-checkbox
                [checked]="selectedIds().has(ev.id)"
                (change)="toggleOne(ev.id, $event.checked)"
              />
            </td>
          </ng-container>

          <!-- Title / Status -->
          <ng-container matColumnDef="title">
            <th mat-header-cell *matHeaderCellDef>Title / Status</th>
            <td mat-cell *matCellDef="let ev">
              <span class="ev-title">{{ ev.title }}</span>
              <div class="ev-meta">
                <app-status-chip [status]="ev.evidence_status" />
                @if (ev.kev_cve_id) {
                  <span class="kev-chip" [class.kev-ransomware]="ev.metadata?.known_ransomware">
                    KEV {{ ev.kev_cve_id }}
                  </span>
                }
                @if (ev.metadata?.notes && !ev.kev_cve_id) {
                  <span class="notes-preview">{{ ev.metadata.notes.slice(0, 60) }}</span>
                }
              </div>
              @if (ev.evidence_status === 'rejected' && ev.metadata?.rejection_reason) {
                <span class="rejection-reason" [style.color]="isDark() ? '#FFC7CE' : '#9e0000'">
                  Reason: {{ ev.metadata.rejection_reason }}
                </span>
              }
            </td>
          </ng-container>

          <!-- Type -->
          <ng-container matColumnDef="type">
            <th mat-header-cell *matHeaderCellDef>Type</th>
            <td mat-cell *matCellDef="let ev">
              <span class="type-chip">{{ ev.evidence_type }}</span>
            </td>
          </ng-container>

          <!-- File -->
          <ng-container matColumnDef="file">
            <th mat-header-cell *matHeaderCellDef>File</th>
            <td mat-cell *matCellDef="let ev">
              <span class="mono-sm">{{ ev.metadata?.original_filename ?? '—' }}</span>
              <span class="secondary-sm">{{ ev.metadata?.file_size ? formatBytes(ev.metadata.file_size) : '' }}</span>
            </td>
          </ng-container>

          <!-- Control Group -->
          <ng-container matColumnDef="group">
            <th mat-header-cell *matHeaderCellDef>Control Group</th>
            <td mat-cell *matCellDef="let ev">
              <span class="mono-sm" [style.color]="ev.group_code ? 'var(--mat-sys-on-surface)' : 'var(--mat-sys-on-surface-variant)'">
                {{ ev.group_code ?? '—' }}
              </span>
            </td>
          </ng-container>

          <!-- Collected -->
          <ng-container matColumnDef="collected">
            <th mat-header-cell *matHeaderCellDef>Collected</th>
            <td mat-cell *matCellDef="let ev">
              <span class="secondary-sm">{{ ev.collected_date ?? '—' }}</span>
            </td>
          </ng-container>

          <!-- Expires -->
          <ng-container matColumnDef="expires">
            <th mat-header-cell *matHeaderCellDef>Expires</th>
            <td mat-cell *matCellDef="let ev">
              @if (ev.expires_date) {
                <span class="expiry-badge"
                  [class.expiry-red]="isExpiredFn(ev.expires_date)"
                  [class.expiry-amber]="!isExpiredFn(ev.expires_date) && isExpiringSoonFn(ev.expires_date)"
                  [class.expiry-green]="!isExpiredFn(ev.expires_date) && !isExpiringSoonFn(ev.expires_date)"
                >{{ ev.expires_date }}</span>
              } @else {
                <span class="secondary-sm">—</span>
              }
            </td>
          </ng-container>

          <!-- Verified -->
          <ng-container matColumnDef="verified">
            <th mat-header-cell *matHeaderCellDef>Verified</th>
            <td mat-cell *matCellDef="let ev">
              @if (ev.verified_by) {
                <div class="verified-cell">
                  <mat-icon class="icon-sm verified-icon">verified</mat-icon>
                  <span class="secondary-sm">{{ ev.verified_by }}</span>
                </div>
              } @else {
                <span class="secondary-sm disabled">—</span>
              }
            </td>
          </ng-container>

          <!-- Uploaded -->
          <ng-container matColumnDef="uploaded">
            <th mat-header-cell *matHeaderCellDef>Uploaded</th>
            <td mat-cell *matCellDef="let ev">
              <span class="secondary-sm">{{ fmtDateFn(ev.created_at) }}</span>
            </td>
          </ng-container>

          <!-- Actions -->
          <ng-container matColumnDef="actions">
            <th mat-header-cell *matHeaderCellDef>Actions</th>
            <td mat-cell *matCellDef="let ev" (click)="$event.stopPropagation()">

              <!-- Draft: submit for review -->
              @if (ev.evidence_status === 'active' || ev.evidence_status === 'rejected') {
                <button mat-icon-button matTooltip="Submit for review"
                  [disabled]="submitMutation.isPending()"
                  (click)="submitMutation.mutate(ev.id)">
                  <mat-icon class="icon-md">send</mat-icon>
                </button>
              }

              <!-- Pending review: approve + reject -->
              @if (ev.evidence_status === 'pending_review') {
                <button mat-icon-button matTooltip="Approve"
                  [style.color]="isDark() ? '#C6EFCE' : '#1b5e20'"
                  [disabled]="approveMutation.isPending()"
                  (click)="approveMutation.mutate(ev.id)">
                  <mat-icon class="icon-md">check</mat-icon>
                </button>
                <button mat-icon-button matTooltip="Reject"
                  [style.color]="isDark() ? '#FFC7CE' : '#9e0000'"
                  (click)="openRejectDialog(ev.id, ev.title)">
                  <mat-icon class="icon-md">close</mat-icon>
                </button>
              }

              <!-- Download -->
              <a mat-icon-button matTooltip="Download" [href]="evidenceApi.getDownloadUrl(ev.id)" download (click)="$event.stopPropagation()">
                <mat-icon class="icon-md">download</mat-icon>
              </a>

              <!-- Delete -->
              <button mat-icon-button matTooltip="Delete" class="btn-error"
                [disabled]="deleteMutation.isPending()"
                (click)="deleteMutation.mutate(ev.id)">
                <mat-icon class="icon-md">delete</mat-icon>
              </button>
            </td>
          </ng-container>

          <tr mat-header-row *matHeaderRowDef="displayedColumns"></tr>
          <tr mat-row *matRowDef="let ev; columns: displayedColumns"
            class="ev-row"
            [class.ev-row--draft]="ev.evidence_status === 'draft'"></tr>

          <tr class="mat-row" *matNoDataRow>
            <td [attr.colspan]="displayedColumns.length" class="no-data-cell">
              @if (evidenceQuery.isLoading()) {
                <span class="secondary-sm">Loading…</span>
              } @else {
                <span class="secondary-sm">No evidence matches the current filter.</span>
              }
            </td>
          </tr>
        </table>
      </mat-card>
    }
  `,
  styles: [`
    :host { display: block; }

    .metrics-row { display: flex; gap: 16px; margin-top: 16px; margin-bottom: 16px; flex-wrap: wrap; }
    .metrics-row > * { flex: 1; min-width: 120px; }

    .alert {
      padding: 10px 14px; border-radius: 6px; font-size: 0.85rem; margin-bottom: 12px;
      border: 1px solid;
    }
    .alert-error { background: rgba(192,0,0,0.1); border-color: rgba(192,0,0,0.3); color: var(--mat-sys-error); }
    .alert-warn  { background: rgba(230,160,0,0.1); border-color: rgba(230,160,0,0.3); color: #FFEB9C; }
    .alert-info  { background: rgba(21,101,192,0.1); border-color: rgba(21,101,192,0.3); color: #9fc8f0; }

    .filter-card { margin-bottom: 16px; }
    .filter-card mat-card-content { padding-bottom: 12px !important; }
    .filter-row { display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }

    .tab-group { display: flex; gap: 0; border: 1px solid var(--mat-sys-outline); border-radius: 6px; overflow: hidden; }
    .tab-btn {
      padding: 4px 10px; font-size: 0.78rem; cursor: pointer; white-space: nowrap;
      border-right: 1px solid var(--mat-sys-outline); color: var(--mat-sys-on-surface-variant);
      transition: background 0.15s;
    }
    .tab-btn:last-child { border-right: none; }
    .tab-btn:hover { background: rgba(255,255,255,0.06); }
    .tab-btn--active { background: rgba(68,114,196,0.2); color: var(--mat-sys-primary); font-weight: 600; }

    .bulk-bar {
      display: flex; align-items: center; gap: 12px; margin-top: 10px;
      padding: 8px 12px; background: rgba(68,114,196,0.08); border-radius: 6px;
      border: 1px solid rgba(68,114,196,0.2);
    }

    .table-card { overflow: hidden; }
    .full-table { width: 100%; }

    .ev-title { display: block; font-weight: 600; font-size: 0.875rem; }
    .ev-meta { display: flex; gap: 4px; flex-wrap: wrap; align-items: center; margin-top: 3px; }
    .rejection-reason { display: block; font-size: 0.75rem; margin-top: 2px; }

    .status-chip {
      font-size: 0.62rem; font-weight: 600; height: 18px; line-height: 18px;
      padding: 0 6px; border-radius: 9px; display: inline-block; white-space: nowrap;
    }
    .kev-chip {
      font-size: 0.62rem; font-weight: 700; height: 18px; line-height: 18px;
      padding: 0 6px; border-radius: 9px; display: inline-block;
      font-family: monospace;
      background: rgba(46,125,50,0.1); color: #C6EFCE;
      border: 1px solid #388e3c;
    }
    .kev-ransomware { background: rgba(192,0,0,0.12); color: #FFC7CE; border-color: #c62828; }
    html[data-theme='light'] {
      .kev-chip { background: rgba(29,158,117,0.12); color: #0F6E56; border-color: rgba(29,158,117,0.4); }
      .kev-ransomware { background: rgba(163,45,45,0.10); color: #8A1F1F; border-color: rgba(163,45,45,0.3); }
      .expiry-green { background: rgba(29,158,117,0.12); color: #0F6E56; }
      .expiry-red   { background: rgba(163,45,45,0.12);  color: #8A1F1F; }
      .expiry-amber { background: rgba(186,117,23,0.12); color: #7A4500; }
    }
    .notes-preview { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }

    .type-chip {
      font-size: 0.65rem; height: 18px; line-height: 18px; padding: 0 6px;
      border-radius: 9px; display: inline-block;
      background: var(--mat-sys-surface-variant); color: var(--mat-sys-on-surface-variant);
    }
    .mono-sm  { display: block; font-family: monospace; font-size: 0.72rem; }
    .secondary-sm { display: block; font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
    .disabled { color: var(--mat-sys-on-surface-variant); opacity: 0.5; }

    .expiry-badge {
      font-size: 0.72rem; font-weight: 600; padding: 2px 6px; border-radius: 4px; display: inline-block;
    }
    .expiry-red   { background: rgba(192,0,0,0.15);    color: #FFC7CE; }
    .expiry-amber { background: rgba(230,160,0,0.15);  color: #FFEB9C; }
    .expiry-green { background: rgba(46,125,50,0.12);  color: #C6EFCE; }

    .ev-row:hover td { background: rgba(255,255,255,0.04); cursor: default; }
    .ev-row--draft { opacity: 0.75; }

    /* Column widths */
    .full-table .mat-column-select    { width: 40px; }
    .full-table .mat-column-type      { width: 110px; }
    .full-table .mat-column-file      { width: 140px; }
    .full-table .mat-column-group     { width: 100px; }
    .full-table .mat-column-collected { width: 100px; }
    .full-table .mat-column-expires   { width: 100px; }
    .full-table .mat-column-verified  { width: 110px; }
    .full-table .mat-column-uploaded  { width: 100px; }
    .full-table .mat-column-actions   { width: 130px; text-align: right; white-space: nowrap; }

    /* Verified cell */
    .verified-cell  { display: flex; align-items: center; gap: 4px; }
    .verified-icon  { color: var(--mat-sys-primary); }

    /* Misc */
    .bulk-count       { font-size: 0.85rem; color: var(--mat-sys-on-surface-variant); }
    .no-data-cell     { text-align: center; padding: 24px; }
    .btn-error        { color: var(--mat-sys-error); }
  `],
})
export class EvidenceComponent {
  evidenceApi            = inject(EvidenceApiService)
  private productService = inject(ProductService)
  private projectService = inject(ProjectService)
  private themeService   = inject(ThemeService)
  private queryClient    = injectQueryClient()
  private dialog         = inject(MatDialog)

  product = this.productService.product
  isDark  = computed(() => this.themeService.isDark())

  // Filter state
  filterTab    = signal<FilterTab>('all')
  statusFilter = signal('')
  typeFilter   = signal('')
  search       = signal('')
  selectedIds  = signal<Set<string>>(new Set())

  evidenceTypes = EVIDENCE_TYPES
  Math = Math

  displayedColumns = ['select', 'title', 'type', 'file', 'group', 'collected', 'expires', 'verified', 'uploaded', 'actions']

  filterTabs: { value: FilterTab; label: string; count?: () => number; warn?: string }[] = [
    { value: 'all',       label: 'All',       count: () => this.allItems().length },
    { value: 'valid',     label: 'Valid' },
    { value: 'expiring',  label: 'Expiring',  count: () => this.expiringSoonItems().length, warn: '#FF9800' },
    { value: 'expired',   label: 'Expired',   count: () => this.expiredItems().length, warn: '#C00000' },
    { value: 'unverified', label: 'Unverified', count: () => this.unverifiedCount() },
  ]

  // ─── Query ──────────────────────────────────────────────────────────────────
  evidenceQuery = injectQuery(() => ({
    queryKey: ['evidence', this.product()],
    queryFn: () => firstValueFrom(this.evidenceApi.list({
      limit: 500,
    })),
  }))

  allItems = computed(() => this.evidenceQuery.data() ?? [])

  expiredItems      = computed(() => this.allItems().filter(ev => isExpired(ev.expires_date)))
  expiringSoonItems = computed(() => this.allItems().filter(ev => isExpiringSoon(ev.expires_date)))
  verifiedCount     = computed(() => this.allItems().filter(ev => ev.verified_by).length)
  unverifiedCount   = computed(() => this.allItems().filter(ev => !ev.verified_by).length)
  draftCount        = computed(() => this.allItems().filter(ev => ev.evidence_status === 'draft').length)
  pendingCount      = computed(() => this.allItems().filter(ev => ev.evidence_status === 'pending_review').length)

  filteredItems = computed(() => {
    const tab    = this.filterTab()
    const sf     = this.statusFilter()
    const tf     = this.typeFilter()
    const s      = this.search().toLowerCase()

    return this.allItems().filter(ev => {
      // Tab filter
      if (tab === 'valid')     { if (ev.expires_date && isExpired(ev.expires_date)) return false }
      if (tab === 'expiring')  { if (!isExpiringSoon(ev.expires_date)) return false }
      if (tab === 'expired')   { if (!isExpired(ev.expires_date)) return false }
      if (tab === 'unverified') { if (ev.verified_by) return false }
      // Status
      if (sf && ev.evidence_status !== sf) return false
      // Type
      if (tf && ev.evidence_type !== tf) return false
      // Search
      if (s) {
        return (
          (ev.title ?? '').toLowerCase().includes(s) ||
          (ev.group_code ?? '').toLowerCase().includes(s) ||
          (ev.evidence_type ?? '').toLowerCase().includes(s)
        )
      }
      return true
    })
  })

  headerSubtitle = computed(() => {
    const items   = this.allItems()
    const drafts  = this.draftCount()
    const pending = this.pendingCount()
    return `${items.length} items · ${drafts} drafts · ${pending} pending review`
  })

  // Selection
  allSelected  = computed(() => this.filteredItems().length > 0 && this.filteredItems().every(ev => this.selectedIds().has(ev.id)))
  someSelected = computed(() => !this.allSelected() && this.filteredItems().some(ev => this.selectedIds().has(ev.id)))

  toggleAll(checked: boolean): void {
    if (checked) {
      this.selectedIds.set(new Set(this.filteredItems().map(ev => ev.id)))
    } else {
      this.selectedIds.set(new Set())
    }
  }

  toggleOne(id: string, checked: boolean): void {
    const next = new Set(this.selectedIds())
    if (checked) next.add(id); else next.delete(id)
    this.selectedIds.set(next)
  }

  clearSelection(): void { this.selectedIds.set(new Set()) }

  // ─── Mutations ──────────────────────────────────────────────────────────────
  deleteMutation = injectMutation(() => ({
    mutationFn: (id: string) => firstValueFrom(this.evidenceApi.delete(id)),
    onSuccess: () => this.queryClient.invalidateQueries({ queryKey: ['evidence'] }),
  }))

  approveMutation = injectMutation(() => ({
    mutationFn: (id: string) => firstValueFrom(this.evidenceApi.approve(id)),
    onSuccess: () => this.queryClient.invalidateQueries({ queryKey: ['evidence'] }),
  }))

  submitMutation = injectMutation(() => ({
    // The API service has no submit endpoint; use archive as placeholder — backend decide
    // For now we call approve with a different note path if needed; wired to POST /evidence/:id/approve
    mutationFn: (id: string) => firstValueFrom(this.evidenceApi.approve(id)),
    onSuccess: () => this.queryClient.invalidateQueries({ queryKey: ['evidence'] }),
  }))

  rejectMutation = injectMutation(() => ({
    mutationFn: ({ id, reason }: { id: string; reason: string }) =>
      firstValueFrom(this.evidenceApi.reject(id, reason)),
    onSuccess: () => {
      this.queryClient.invalidateQueries({ queryKey: ['evidence'] })
    },
  }))

  uploadMutation = injectMutation(() => ({
    mutationFn: (fd: FormData) => firstValueFrom(this.evidenceApi.upload(fd)),
    onSuccess: () => this.queryClient.invalidateQueries({ queryKey: ['evidence'] }),
  }))

  bulkDeleteMutation = injectMutation(() => ({
    mutationFn: async (ids: string[]) => {
      await Promise.all(ids.map(id => firstValueFrom(this.evidenceApi.delete(id))))
    },
    onSuccess: () => {
      this.queryClient.invalidateQueries({ queryKey: ['evidence'] })
      this.selectedIds.set(new Set())
    },
  }))

  // ─── Helpers ────────────────────────────────────────────────────────────────
  formatBytes = formatBytes
  fmtDateFn   = fmtDate
  isExpiredFn = isExpired
  isExpiringSoonFn = isExpiringSoon

  openUploadDialog(): void {
    const projectId = this.projectService.activeProject()?.id
    const ref = this.dialog.open(UploadEvidenceDialogComponent, {
      data: { projectId },
      width: '480px',
    })
    ref.afterClosed().subscribe((fd: FormData | null) => {
      if (fd) this.uploadMutation.mutate(fd)
    })
  }

  openRejectDialog(id: string, title?: string): void {
    const ref = this.dialog.open(RejectEvidenceDialogComponent, {
      data: { itemName: title } satisfies RejectEvidenceDialogData,
      width: '420px',
    })
    ref.afterClosed().subscribe((result: RejectEvidenceDialogResult | false | undefined) => {
      if (result) {
        this.rejectMutation.mutate({ id, reason: result.reason })
      }
    })
  }

  confirmBulkDelete(): void {
    const count = this.selectedIds().size
    if (!count) return
    const ref = this.dialog.open(BulkDeleteConfirmDialogComponent, {
      data: { count } satisfies BulkDeleteConfirmDialogData,
      width: '400px',
    })
    ref.afterClosed().subscribe((confirmed: boolean) => {
      if (confirmed) {
        const ids = [...this.selectedIds()]
        this.bulkDeleteMutation.mutate(ids)
      }
    })
  }
}
