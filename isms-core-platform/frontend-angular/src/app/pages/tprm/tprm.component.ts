import { Component, inject, signal, computed } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'

import { injectQuery, injectMutation, injectQueryClient } from '@tanstack/angular-query-experimental'

import { MatButtonModule } from '@angular/material/button'
import { MatIconModule } from '@angular/material/icon'
import { MatSelectModule } from '@angular/material/select'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatCheckboxModule } from '@angular/material/checkbox'
import { MatDialogModule, MatDialog } from '@angular/material/dialog'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatTabsModule } from '@angular/material/tabs'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { Component as NgComponent } from '@angular/core'

import {
  TprmApiService, Vendor, VendorCreate, VendorAssessment, VendorContract, VendorSummary,
} from '../../api/tprm-api.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

// ── Constants ────────────────────────────────────────────────────────────────

const CRIT_COLORS: Record<string, string> = {
  critical: '#9C27B0',
  high:     '#F44336',
  medium:   '#FF9800',
  low:      '#4CAF50',
}
const STATUS_COLORS: Record<string, string> = {
  active: '#4CAF50', under_review: '#FF9800', terminated: '#9E9E9E',
}
const STATUS_LABELS: Record<string, string> = {
  active: 'Active', under_review: 'Under Review', terminated: 'Terminated',
}
const ASSESSMENT_STATUS_COLORS: Record<string, string> = {
  planned: '#607D8B', in_progress: '#FF9800', complete: '#4CAF50',
}
const VENDOR_TYPES    = ['supplier', 'provider', 'partner', 'subprocessor']
const CRITICALITIES   = ['low', 'medium', 'high', 'critical']
const STATUSES        = ['active', 'under_review', 'terminated']
const ASSESS_STATUSES = ['planned', 'in_progress', 'complete']
const DORA_ENTITY_TYPES    = ['direct', 'sub_outsourcing', 'intra_group', 'critical', 'important']
const DORA_ICT_SERVICES    = ['cloud_computing', 'data_analytics', 'data_centre', 'software', 'hardware', 'network', 'security', 'other']
const DORA_SUBSTITUTABILITY = ['easy', 'difficult', 'not_substitutable']

function toLabel(s: string): string {
  return s.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase())
}

function fmtDate(d: string | null): string {
  if (!d) return '—'
  return new Date(d).toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: '2-digit' })
}

// ── Vendor Dialog ────────────────────────────────────────────────────────────

@NgComponent({
  selector: 'app-vendor-dialog',
  standalone: true,
  imports: [FormsModule, MatButtonModule, MatDialogModule, MatFormFieldModule, MatInputModule, MatSelectModule, MatIconModule],
  template: `
    <h2 mat-dialog-title>{{ data.existing ? 'Edit Vendor' : 'New Vendor' }}</h2>
    <mat-dialog-content class="dlg-content dlg-content--wide">

      @if (error()) {
        <div class="dlg-error">{{ error() }}</div>
      }

      <mat-form-field appearance="outline" class="field-full">
        <mat-label>Vendor name *</mat-label>
        <input matInput [(ngModel)]="form.name" />
      </mat-form-field>

      <div class="row-gap">
        <mat-form-field appearance="outline" class="field-flex">
          <mat-label>Type</mat-label>
          <mat-select [(ngModel)]="form.vendor_type">
            @for (t of vendorTypes; track t) { <mat-option [value]="t">{{ toLabel(t) }}</mat-option> }
          </mat-select>
        </mat-form-field>
        <mat-form-field appearance="outline" class="field-flex">
          <mat-label>Criticality</mat-label>
          <mat-select [(ngModel)]="form.criticality">
            @for (c of criticalities; track c) { <mat-option [value]="c">{{ toLabel(c) }}</mat-option> }
          </mat-select>
        </mat-form-field>
        <mat-form-field appearance="outline" class="field-flex">
          <mat-label>Status</mat-label>
          <mat-select [(ngModel)]="form.status">
            @for (s of statuses; track s) { <mat-option [value]="s">{{ statusLabels[s] }}</mat-option> }
          </mat-select>
        </mat-form-field>
      </div>

      <mat-form-field appearance="outline" class="field-full">
        <mat-label>Description</mat-label>
        <textarea matInput rows="2" [(ngModel)]="form.description"></textarea>
      </mat-form-field>

      <div class="row-gap">
        <mat-form-field appearance="outline" class="field-flex">
          <mat-label>Website</mat-label>
          <input matInput [(ngModel)]="form.website" />
        </mat-form-field>
        <mat-form-field appearance="outline" class="field-flex">
          <mat-label>Primary contact</mat-label>
          <input matInput [(ngModel)]="form.primary_contact" />
        </mat-form-field>
      </div>

      <div class="dora-section-header">
        DORA — Digital Operational Resilience Act (optional)
      </div>

      <mat-form-field appearance="outline" class="field-full">
        <mat-label>DORA entity type</mat-label>
        <mat-select [(ngModel)]="form.dora_entity_type">
          <mat-option value="">— Not DORA-regulated —</mat-option>
          @for (t of doraEntityTypes; track t) { <mat-option [value]="t">{{ toLabel(t) }}</mat-option> }
        </mat-select>
      </mat-form-field>

      @if (form.dora_entity_type) {
        <div class="row-gap">
          <mat-form-field appearance="outline" class="field-flex">
            <mat-label>ICT service type</mat-label>
            <mat-select [(ngModel)]="form.dora_ict_service_type">
              <mat-option value="">—</mat-option>
              @for (s of doraIctServices; track s) { <mat-option [value]="s">{{ toLabel(s) }}</mat-option> }
            </mat-select>
          </mat-form-field>
          <mat-form-field appearance="outline" class="field-flex">
            <mat-label>Substitutability</mat-label>
            <mat-select [(ngModel)]="form.dora_substitutability">
              <mat-option value="">—</mat-option>
              @for (s of doraSubstitutability; track s) { <mat-option [value]="s">{{ toLabel(s) }}</mat-option> }
            </mat-select>
          </mat-form-field>
        </div>
        <mat-form-field appearance="outline" class="field-full">
          <mat-label>DORA register ref</mat-label>
          <input matInput [(ngModel)]="form.dora_register_ref" />
        </mat-form-field>
      }
    </mat-dialog-content>
    <mat-dialog-actions align="end">
      <button mat-button mat-dialog-close>Cancel</button>
      <button mat-raised-button color="primary" [disabled]="saving()" (click)="submit()">
        {{ saving() ? 'Saving…' : (data.existing ? 'Save' : 'Create') }}
      </button>
    </mat-dialog-actions>
  `,
  styles: [`
    .dlg-content {
      padding-top: 16px;
      display: flex;
      flex-direction: column;
      gap: 0;
    }
    .dlg-content--wide  { min-width: 480px; }
    .dlg-content--narrow { min-width: 420px; }
    .dlg-error {
      color: #f44336;
      font-size: 0.8rem;
      margin-bottom: 12px;
      padding: 8px 10px;
      background: rgba(244,67,54,0.08);
      border-radius: 4px;
    }
    .field-full { width: 100%; }
    .field-flex { flex: 1; }
    .row-gap { display: flex; gap: 12px; }
    .dora-section-header {
      font-size: 0.65rem;
      font-weight: 700;
      color: #2196F3;
      text-transform: uppercase;
      padding: 4px 0 8px;
      border-bottom: 1px solid rgba(255,255,255,0.1);
      margin-bottom: 8px;
    }
  `],
})
export class VendorDialogComponent {
  private api = inject(TprmApiService)
  private qc  = injectQueryClient()
  readonly dialog = inject(MatDialog)

  // Injected by MatDialog.open(VendorDialogComponent, { data: ... })
  data: { existing?: Vendor } = { existing: undefined }

  vendorTypes        = VENDOR_TYPES
  criticalities      = CRITICALITIES
  statuses           = STATUSES
  statusLabels       = STATUS_LABELS
  doraEntityTypes    = DORA_ENTITY_TYPES
  doraIctServices    = DORA_ICT_SERVICES
  doraSubstitutability = DORA_SUBSTITUTABILITY
  toLabel = toLabel

  form: VendorCreate = this.data.existing ? {
    name:                 this.data.existing.name,
    vendor_type:          this.data.existing.vendor_type ?? 'supplier',
    criticality:          this.data.existing.criticality ?? 'medium',
    status:               this.data.existing.status ?? 'active',
    description:          this.data.existing.description ?? '',
    website:              this.data.existing.website ?? '',
    primary_contact:      this.data.existing.primary_contact ?? '',
    dora_entity_type:     this.data.existing.dora_entity_type ?? '',
    dora_ict_service_type:  this.data.existing.dora_ict_service_type ?? '',
    dora_substitutability:  this.data.existing.dora_substitutability ?? '',
    dora_register_ref:    this.data.existing.dora_register_ref ?? '',
  } : {
    name: '', vendor_type: 'supplier', criticality: 'medium', status: 'active',
    description: '', website: '', primary_contact: '',
    dora_entity_type: '', dora_ict_service_type: '', dora_substitutability: '', dora_register_ref: '',
  }

  error  = signal('')
  saving = signal(false)

  async submit() {
    if (!this.form.name.trim()) { this.error.set('Name is required.'); return }
    this.error.set('')
    this.saving.set(true)
    const body: VendorCreate = {
      ...this.form,
      description:          this.form.description          || undefined,
      website:              this.form.website              || undefined,
      primary_contact:      this.form.primary_contact      || undefined,
      dora_entity_type:     this.form.dora_entity_type     || undefined,
      dora_ict_service_type:  this.form.dora_ict_service_type  || undefined,
      dora_substitutability:  this.form.dora_substitutability  || undefined,
      dora_register_ref:    this.form.dora_register_ref    || undefined,
    }
    try {
      if (this.data.existing) {
        await firstValueFrom(this.api.update(this.data.existing.id, body))
      } else {
        await firstValueFrom(this.api.create(body))
      }
      this.qc.invalidateQueries({ queryKey: ['vendors'] })
      this.qc.invalidateQueries({ queryKey: ['tprm-summary'] })
      this.dialog.closeAll()
    } catch {
      this.error.set('Failed to save.')
    } finally {
      this.saving.set(false)
    }
  }
}

// ── Assessment Dialog ─────────────────────────────────────────────────────────

@NgComponent({
  selector: 'app-assessment-dialog',
  standalone: true,
  imports: [FormsModule, MatButtonModule, MatDialogModule, MatFormFieldModule, MatInputModule, MatSelectModule],
  template: `
    <h2 mat-dialog-title>New Assessment</h2>
    <mat-dialog-content class="dlg-content dlg-content--narrow">
      @if (error()) {
        <div class="dlg-error">{{ error() }}</div>
      }
      <div class="row-gap">
        <mat-form-field appearance="outline" class="field-flex">
          <mat-label>Score (0–100)</mat-label>
          <input matInput type="number" min="0" max="100" [(ngModel)]="score" />
        </mat-form-field>
        <mat-form-field appearance="outline" class="field-flex">
          <mat-label>Status</mat-label>
          <mat-select [(ngModel)]="status">
            @for (s of assessStatuses; track s) { <mat-option [value]="s">{{ toLabel(s) }}</mat-option> }
          </mat-select>
        </mat-form-field>
      </div>
      <mat-form-field appearance="outline" class="field-full">
        <mat-label>Notes</mat-label>
        <textarea matInput rows="3" [(ngModel)]="notes"></textarea>
      </mat-form-field>
      <div class="row-gap">
        <mat-form-field appearance="outline" class="field-flex">
          <mat-label>Assessment date</mat-label>
          <input matInput type="date" [(ngModel)]="assessmentDate" />
        </mat-form-field>
        <mat-form-field appearance="outline" class="field-flex">
          <mat-label>Next review date</mat-label>
          <input matInput type="date" [(ngModel)]="nextReviewDate" />
        </mat-form-field>
      </div>
      <mat-form-field appearance="outline" class="field-full">
        <mat-label>Control group (optional)</mat-label>
        <input matInput placeholder="e.g. A.5.19" [(ngModel)]="controlGroupId" />
      </mat-form-field>
    </mat-dialog-content>
    <mat-dialog-actions align="end">
      <button mat-button mat-dialog-close>Cancel</button>
      <button mat-raised-button color="primary" [disabled]="saving()" (click)="submit()">
        {{ saving() ? 'Saving…' : 'Save' }}
      </button>
    </mat-dialog-actions>
  `,
  styles: [`
    .dlg-content {
      padding-top: 16px;
      display: flex;
      flex-direction: column;
      gap: 0;
    }
    .dlg-content--narrow { min-width: 420px; }
    .dlg-error {
      color: #f44336;
      font-size: 0.8rem;
      margin-bottom: 12px;
      padding: 8px 10px;
      background: rgba(244,67,54,0.08);
      border-radius: 4px;
    }
    .field-full { width: 100%; }
    .field-flex { flex: 1; }
    .row-gap { display: flex; gap: 12px; }
  `],
})
export class AssessmentDialogComponent {
  private api = inject(TprmApiService)
  private qc  = injectQueryClient()
  readonly dialog = inject(MatDialog)

  data: { vendorId: string } = { vendorId: '' }

  assessStatuses = ASSESS_STATUSES
  toLabel = toLabel

  score          = ''
  status         = 'planned'
  notes          = ''
  assessmentDate = ''
  nextReviewDate = ''
  controlGroupId = ''
  error  = signal('')
  saving = signal(false)

  async submit() {
    this.error.set('')
    this.saving.set(true)
    try {
      await firstValueFrom(this.api.createAssessment(this.data.vendorId, {
        score:            this.score !== '' ? Number(this.score) : undefined,
        status:           this.status,
        notes:            this.notes   || undefined,
        assessment_date:  this.assessmentDate || undefined,
        next_review_date: this.nextReviewDate  || undefined,
        control_group_id: this.controlGroupId  || undefined,
      }))
      this.qc.invalidateQueries({ queryKey: ['vendor-assessments', this.data.vendorId] })
      this.dialog.closeAll()
    } catch {
      this.error.set('Failed to save assessment.')
    } finally {
      this.saving.set(false)
    }
  }
}

// ── Contract Dialog ───────────────────────────────────────────────────────────

@NgComponent({
  selector: 'app-contract-dialog',
  standalone: true,
  imports: [FormsModule, MatButtonModule, MatDialogModule, MatFormFieldModule, MatInputModule, MatCheckboxModule],
  template: `
    <h2 mat-dialog-title>New Contract</h2>
    <mat-dialog-content class="dlg-content dlg-content--narrow">
      @if (error()) {
        <div class="dlg-error">{{ error() }}</div>
      }
      <mat-form-field appearance="outline" class="field-full">
        <mat-label>Title *</mat-label>
        <input matInput [(ngModel)]="title" />
      </mat-form-field>
      <mat-form-field appearance="outline" class="field-full">
        <mat-label>Contract reference</mat-label>
        <input matInput [(ngModel)]="contractRef" />
      </mat-form-field>
      <div class="row-gap">
        <mat-form-field appearance="outline" class="field-flex">
          <mat-label>Start date</mat-label>
          <input matInput type="date" [(ngModel)]="startDate" />
        </mat-form-field>
        <mat-form-field appearance="outline" class="field-flex">
          <mat-label>Expiry date</mat-label>
          <input matInput type="date" [(ngModel)]="expiryDate" />
        </mat-form-field>
      </div>
      <div class="checkbox-row">
        <mat-checkbox [(ngModel)]="autoRenews"><span class="checkbox-label">Auto-renews</span></mat-checkbox>
        <mat-checkbox [(ngModel)]="securityClauses"><span class="checkbox-label">Security clauses present</span></mat-checkbox>
      </div>
    </mat-dialog-content>
    <mat-dialog-actions align="end">
      <button mat-button mat-dialog-close>Cancel</button>
      <button mat-raised-button color="primary" [disabled]="saving()" (click)="submit()">
        {{ saving() ? 'Saving…' : 'Save' }}
      </button>
    </mat-dialog-actions>
  `,
  styles: [`
    .dlg-content {
      padding-top: 16px;
      display: flex;
      flex-direction: column;
      gap: 0;
    }
    .dlg-content--narrow { min-width: 420px; }
    .dlg-error {
      color: #f44336;
      font-size: 0.8rem;
      margin-bottom: 12px;
      padding: 8px 10px;
      background: rgba(244,67,54,0.08);
      border-radius: 4px;
    }
    .field-full { width: 100%; }
    .field-flex { flex: 1; }
    .row-gap { display: flex; gap: 12px; }
    .checkbox-row { display: flex; gap: 24px; padding: 4px 0; }
    .checkbox-label { font-size: 0.82rem; }
  `],
})
export class ContractDialogComponent {
  private api = inject(TprmApiService)
  private qc  = injectQueryClient()
  readonly dialog = inject(MatDialog)

  data: { vendorId: string } = { vendorId: '' }

  title           = ''
  contractRef     = ''
  startDate       = ''
  expiryDate      = ''
  autoRenews      = false
  securityClauses = false
  error  = signal('')
  saving = signal(false)

  async submit() {
    if (!this.title.trim()) { this.error.set('Title is required.'); return }
    this.error.set('')
    this.saving.set(true)
    try {
      await firstValueFrom(this.api.createContract(this.data.vendorId, {
        title:                    this.title,
        contract_ref:             this.contractRef  || undefined,
        start_date:               this.startDate    || undefined,
        expiry_date:              this.expiryDate   || undefined,
        auto_renews:              this.autoRenews,
        security_clauses_present: this.securityClauses,
      }))
      this.qc.invalidateQueries({ queryKey: ['vendor-contracts', this.data.vendorId] })
      this.dialog.closeAll()
    } catch {
      this.error.set('Failed to save contract.')
    } finally {
      this.saving.set(false)
    }
  }
}

// ── Main Component ────────────────────────────────────────────────────────────

@Component({
  selector: 'app-tprm',
  standalone: true,
  imports: [
    FormsModule,
    MatButtonModule, MatIconModule, MatSelectModule,
    MatFormFieldModule, MatInputModule, MatTooltipModule,
    MatTabsModule, MatProgressSpinnerModule,
    PageHeaderComponent,
  ],
  template: `
    <app-page-header
      title="Third-Party Risk"
      subtitle="Vendor &amp; supplier risk register — ISO 27001:2022 §A.5.19–22 · DORA Art. 28">
      <div actions>
        <button mat-raised-button color="primary" (click)="openCreate()">
          <mat-icon>add</mat-icon>
          New Vendor
        </button>
      </div>
    </app-page-header>

    <!-- Summary cards -->
    <div class="summary-cards">
      @for (c of summaryCards(); track c.label) {
        <div [style]="'min-width:100px;padding:12px;border-radius:6px;border:1px solid ' + c.color + '30;background:' + c.color + '08'">
          @if (summaryQ.isLoading()) {
            <div class="skeleton-value"></div>
          } @else {
            <div [style]="'font-size:1.4rem;font-weight:700;color:' + c.color + ';line-height:1'">{{ c.value }}</div>
          }
          <div class="card-label">{{ c.label }}</div>
        </div>
      }
    </div>

    <!-- Tabs -->
    <mat-tab-group [(selectedIndex)]="activeTab" animationDuration="0" style="margin-top: 16px">

      <!-- Vendors tab -->
      <mat-tab label="Vendors">
        <div class="tab-content">

          <!-- Filters -->
          <div class="filter-row">
            <mat-form-field appearance="outline" class="filter-field" subscriptSizing="dynamic">
              <mat-label>Criticality</mat-label>
              <mat-select [(ngModel)]="critFilter" (ngModelChange)="refetchVendors()">
                <mat-option value="">All</mat-option>
                @for (c of criticalities; track c) { <mat-option [value]="c">{{ toLabel(c) }}</mat-option> }
              </mat-select>
            </mat-form-field>
            <mat-form-field appearance="outline" class="filter-field" subscriptSizing="dynamic">
              <mat-label>Status</mat-label>
              <mat-select [(ngModel)]="statusFilter" (ngModelChange)="refetchVendors()">
                <mat-option value="">All</mat-option>
                @for (s of statuses; track s) { <mat-option [value]="s">{{ statusLabels[s] }}</mat-option> }
              </mat-select>
            </mat-form-field>
            @if (critFilter() || statusFilter()) {
              <button mat-button (click)="clearFilters()" class="btn-clear">Clear</button>
            }
            <span class="vendor-count">
              {{ (vendorsQ.data() ?? []).length }} vendor{{ (vendorsQ.data() ?? []).length !== 1 ? 's' : '' }}
            </span>
          </div>

          <!-- Table header -->
          <div class="table-header">
            <span class="col-name-contact th-cell">Name / Contact</span>
            <span class="col-type th-cell">Type</span>
            <span class="col-criticality th-cell">Criticality</span>
            <span class="col-status th-cell">Status</span>
            <span class="col-dora th-cell th-cell--center">DORA</span>
            <span class="col-last-assessed th-cell th-cell--right">Last Assessed</span>
            <span class="col-contracts th-cell th-cell--center">Contracts</span>
            <span class="col-actions"></span>
          </div>

          <div class="table-body">
            @if (vendorsQ.isLoading()) {
              @for (i of [0,1,2,3]; track i) {
                <div class="skeleton-row">
                  <div class="skeleton-line"></div>
                </div>
              }
            } @else if (!vendorsQ.data() || vendorsQ.data()!.length === 0) {
              <div class="empty-state">
                <div class="empty-state-text">No vendors yet.</div>
                <button mat-stroked-button class="btn-add-first" (click)="openCreate()">
                  <mat-icon>add</mat-icon> Add first vendor
                </button>
              </div>
            } @else {
              @for (v of vendorsQ.data()!; track v.id) {
                <div>
                  <!-- Vendor row -->
                  <div class="vendor-row"
                       [style.background]="expandedVendor() === v.id ? 'rgba(255,255,255,0.03)' : ''">

                    <!-- Name / contact -->
                    <div class="col-name-contact cell-name">
                      <div class="name-line">
                        <span class="vendor-name">{{ v.name }}</span>
                        @if (v.website) {
                          <a [href]="v.website" target="_blank" class="website-link"
                             [matTooltip]="v.website">
                            <mat-icon class="icon-sm">language</mat-icon>
                          </a>
                        }
                      </div>
                      @if (v.primary_contact) {
                        <div class="text-meta">{{ v.primary_contact }}</div>
                      }
                    </div>

                    <!-- Type -->
                    <div class="col-type text-muted-sm">{{ toLabel(v.vendor_type ?? '—') }}</div>

                    <!-- Criticality chip -->
                    <div class="col-criticality">
                      <span [style]="critChipStyle(v.criticality)">{{ toLabel(v.criticality) }}</span>
                    </div>

                    <!-- Status chip -->
                    <div class="col-status">
                      <span [style]="statusChipStyle(v.status)">{{ statusLabels[v.status] ?? toLabel(v.status) }}</span>
                    </div>

                    <!-- DORA badge -->
                    <div class="col-dora col-center">
                      @if (v.dora_entity_type) {
                        <span [matTooltip]="'DORA: ' + toLabel(v.dora_entity_type)"
                              class="badge-dora">
                          DORA
                        </span>
                      }
                    </div>

                    <!-- Last assessed -->
                    <div class="col-last-assessed text-meta col-right">
                      {{ fmtDate(v.last_assessment_date) }}
                    </div>

                    <!-- Contracts -->
                    <div class="col-contracts col-center text-sm"
                         [style.color]="v.contracts_expiring_soon > 0 ? '#FF9800' : 'var(--mat-sys-on-surface-variant)'">
                      {{ v.contract_count }}{{ v.contracts_expiring_soon > 0 ? ' (' + v.contracts_expiring_soon + '⚠)' : '' }}
                    </div>

                    <!-- Actions -->
                    <div class="col-actions action-btns">
                      <button mat-icon-button class="btn-icon-sm" (click)="toggleExpand(v.id)">
                        <mat-icon class="icon-row-action">{{ expandedVendor() === v.id ? 'expand_less' : 'expand_more' }}</mat-icon>
                      </button>
                      <button mat-icon-button class="btn-icon-sm" (click)="openEdit(v)">
                        <mat-icon class="icon-row-action">edit</mat-icon>
                      </button>
                      <button mat-icon-button class="btn-icon-sm btn-delete" (click)="deleteVendor(v)">
                        <mat-icon class="icon-row-action">delete</mat-icon>
                      </button>
                    </div>
                  </div>

                  <!-- Expanded: assessments + contracts -->
                  @if (expandedVendor() === v.id) {
                    <div class="expand-panel">

                      <!-- Assessments -->
                      <div class="expand-col">
                        <div class="expand-col-header">
                          <span class="expand-col-title">Assessments</span>
                          <button mat-icon-button class="btn-icon-xs" (click)="openAssessDialog(v.id)">
                            <mat-icon class="icon-sm">add</mat-icon>
                          </button>
                        </div>
                        @if (getAssessments(v.id).isLoading()) {
                          <div class="skeleton-line-sm"></div>
                        } @else if (!getAssessments(v.id).data() || getAssessments(v.id).data()!.length === 0) {
                          <span class="text-meta">No assessments yet.</span>
                        } @else {
                          @for (a of getAssessments(v.id).data()!; track a.id) {
                            <div class="assess-row">
                              <span [style]="scoreChipStyle(a.score)">{{ a.score ?? '—' }}</span>
                              <span [style]="assessStatusStyle(a.status)">{{ toLabel(a.status) }}</span>
                              <span class="text-xs-muted">{{ fmtDate(a.assessment_date) }}</span>
                              @if (a.next_review_date) {
                                <span class="text-xs-muted">→ {{ fmtDate(a.next_review_date) }}</span>
                              }
                            </div>
                          }
                        }
                      </div>

                      <div class="expand-divider"></div>

                      <!-- Contracts -->
                      <div class="expand-col">
                        <div class="expand-col-header">
                          <span class="expand-col-title">Contracts</span>
                          <button mat-icon-button class="btn-icon-xs" (click)="openContractDialog(v.id)">
                            <mat-icon class="icon-sm">add</mat-icon>
                          </button>
                        </div>
                        @if (getContracts(v.id).isLoading()) {
                          <div class="skeleton-line-sm"></div>
                        } @else if (!getContracts(v.id).data() || getContracts(v.id).data()!.length === 0) {
                          <span class="text-meta">No contracts yet.</span>
                        } @else {
                          @for (c of getContracts(v.id).data()!; track c.id) {
                            <div class="contract-row">
                              <span class="contract-title">{{ c.title }}</span>
                              @if (c.contract_ref) {
                                <span class="text-xs-muted">{{ c.contract_ref }}</span>
                              }
                              @if (c.expiry_date) {
                                <span [style]="'font-size:0.63rem;color:' + (c.is_expired ? '#F44336' : c.expiring_soon ? '#FF9800' : 'var(--mat-sys-on-surface-variant)')">
                                  exp {{ fmtDate(c.expiry_date) }}
                                </span>
                              }
                              @if (c.auto_renews) {
                                <span class="badge-auto-renew">Auto-renew</span>
                              }
                              @if (c.security_clauses_present) {
                                <span class="badge-sec-clauses">Sec clauses</span>
                              }
                            </div>
                          }
                        }
                      </div>
                    </div>
                  }
                </div>
              }
            }
          </div>
        </div>
      </mat-tab>

      <!-- DORA Register tab -->
      <mat-tab label="DORA Register">
        <div class="tab-content">
          @if (doraQ.isLoading()) {
            <div class="dora-loading">
              <mat-spinner diameter="32"></mat-spinner>
            </div>
          } @else if (!doraQ.data() || doraQ.data()!.length === 0) {
            <div class="empty-state">
              <mat-icon class="empty-state-icon">verified_user</mat-icon>
              <div class="empty-state-muted">No DORA-regulated vendors.</div>
              <div class="empty-state-hint">Assign a DORA entity type to vendors to populate this register.</div>
            </div>
          } @else {
            <!-- DORA table header -->
            <div class="table-header table-header--dora">
              <span class="dora-col-vendor th-cell">Vendor</span>
              <span class="dora-col-entity th-cell">Entity Type</span>
              <span class="dora-col-ict th-cell">ICT Service</span>
              <span class="dora-col-sub th-cell">Substitutability</span>
              <span class="dora-col-ref th-cell">Register Ref</span>
              <span class="dora-col-crit th-cell">Criticality</span>
            </div>
            <div class="table-body">
              @for (v of doraQ.data()!; track v.id) {
                <div class="vendor-row">
                  <div class="dora-col-vendor">
                    <div class="vendor-name-bold">{{ v.name }}</div>
                    @if (v.primary_contact) {
                      <div class="text-meta">{{ v.primary_contact }}</div>
                    }
                  </div>
                  <div class="dora-col-entity dora-entity-type">{{ toLabel(v.dora_entity_type ?? '—') }}</div>
                  <div class="dora-col-ict text-muted-sm">{{ toLabel(v.dora_ict_service_type ?? '—') }}</div>
                  <div class="dora-col-sub text-muted-sm">{{ toLabel(v.dora_substitutability ?? '—') }}</div>
                  <div class="dora-col-ref text-muted-sm">{{ v.dora_register_ref || '—' }}</div>
                  <div class="dora-col-crit"><span [style]="critChipStyle(v.criticality)">{{ toLabel(v.criticality) }}</span></div>
                </div>
              }
            </div>
          }
        </div>
      </mat-tab>
    </mat-tab-group>
  `,
  styles: [`
    :host { display: block; padding: 24px; }

    /* ── Summary cards ─────────────────────────────────────────── */
    .summary-cards {
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
      margin-top: 16px;
      margin-bottom: 20px;
    }
    .skeleton-value {
      width: 32px;
      height: 28px;
      background: rgba(255,255,255,0.06);
      border-radius: 4px;
    }
    .card-label {
      font-size: 0.65rem;
      color: var(--mat-sys-on-surface-variant);
    }

    /* ── Tab content ───────────────────────────────────────────── */
    .tab-content { padding-top: 16px; }

    /* ── Filters ───────────────────────────────────────────────── */
    .filter-row {
      display: flex;
      gap: 12px;
      margin-bottom: 16px;
      align-items: center;
    }
    .filter-field { min-width: 140px; }
    .btn-clear { font-size: 0.75rem; }
    .vendor-count {
      margin-left: auto;
      font-size: 0.72rem;
      color: var(--mat-sys-on-surface-variant);
    }

    /* ── Table shared ──────────────────────────────────────────── */
    .table-header {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 6px 16px;
      background: var(--mat-sys-surface-variant);
      border-radius: 8px 8px 0 0;
      border: 1px solid rgba(255,255,255,0.08);
      border-bottom: none;
    }
    .th-cell {
      font-size: 0.68rem;
      font-weight: 600;
      color: var(--mat-sys-on-surface-variant);
      text-transform: uppercase;
    }
    .th-cell--center { text-align: center; }
    .th-cell--right  { text-align: right; }
    .table-body {
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 0 0 8px 8px;
      overflow: hidden;
    }

    /* ── Vendor table columns ──────────────────────────────────── */
    .col-name-contact  { flex: 3; }
    .col-type          { flex: 1.2; }
    .col-criticality   { width: 80px; }
    .col-status        { width: 100px; }
    .col-dora          { width: 60px; }
    .col-last-assessed { min-width: 90px; }
    .col-contracts     { width: 70px; }
    .col-actions       { width: 82px; }

    /* ── Vendor row ────────────────────────────────────────────── */
    .vendor-row {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 10px 16px;
      border-bottom: 1px solid rgba(255,255,255,0.06);
      cursor: default;
    }
    .cell-name    { min-width: 0; }
    .name-line    { display: flex; align-items: center; gap: 4px; }
    .vendor-name  {
      font-weight: 500;
      font-size: 0.82rem;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .vendor-name-bold { font-weight: 500; font-size: 0.82rem; }
    .website-link {
      color: var(--mat-sys-on-surface-variant);
      display: flex;
    }
    .col-center { text-align: center; }
    .col-right  { text-align: right; }

    /* ── Skeleton ──────────────────────────────────────────────── */
    .skeleton-row {
      padding: 12px 16px;
      border-bottom: 1px solid rgba(255,255,255,0.06);
    }
    .skeleton-line {
      height: 20px;
      background: rgba(255,255,255,0.06);
      border-radius: 4px;
    }
    .skeleton-line-sm {
      height: 16px;
      background: rgba(255,255,255,0.06);
      border-radius: 4px;
    }

    /* ── Empty state ───────────────────────────────────────────── */
    .empty-state      { padding: 48px; text-align: center; }
    .empty-state-text { font-size: 0.9rem; color: var(--mat-sys-on-surface-variant); }
    .btn-add-first    { margin-top: 12px; }
    .empty-state-icon {
      font-size: 32px;
      width: 32px;
      height: 32px;
      color: var(--mat-sys-on-surface-variant);
    }
    .empty-state-muted { margin-top: 8px; color: var(--mat-sys-on-surface-variant); }
    .empty-state-hint  {
      font-size: 0.8rem;
      color: var(--mat-sys-on-surface-variant);
      margin-top: 4px;
    }

    /* ── DORA badge ────────────────────────────────────────────── */
    .badge-dora {
      font-size: 0.6rem;
      font-weight: 700;
      padding: 2px 5px;
      border-radius: 10px;
      background: rgba(33,150,243,0.12);
      color: #2196F3;
      border: 1px solid rgba(33,150,243,0.3);
    }

    /* ── Action buttons ────────────────────────────────────────── */
    .action-btns   { display: flex; gap: 2px; justify-content: flex-end; }
    .btn-icon-sm   { width: 28px; height: 28px; }
    .btn-delete    { color: var(--mat-sys-error); }
    .icon-row-action { font-size: 15px; }

    /* ── Expanded panel ────────────────────────────────────────── */
    .expand-panel {
      display: flex;
      gap: 16px;
      padding: 12px 16px;
      background: rgba(255,255,255,0.03);
      border-bottom: 1px solid rgba(255,255,255,0.06);
    }
    .expand-col        { flex: 1; min-width: 0; }
    .expand-col-header {
      display: flex;
      align-items: center;
      margin-bottom: 6px;
      gap: 4px;
    }
    .expand-col-title {
      font-size: 0.68rem;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--mat-sys-on-surface-variant);
      flex: 1;
    }
    .btn-icon-xs { width: 22px; height: 22px; padding: 0; }
    .expand-divider {
      width: 1px;
      background: rgba(255,255,255,0.08);
    }

    /* ── Assess / contract rows ────────────────────────────────── */
    .assess-row   { display: flex; align-items: center; gap: 6px; padding: 3px 0; }
    .contract-row { display: flex; align-items: center; gap: 6px; padding: 3px 0; flex-wrap: wrap; }
    .contract-title { font-size: 0.72rem; font-weight: 600; }

    /* ── Contract badges ───────────────────────────────────────── */
    .badge-auto-renew {
      font-size: 0.58rem;
      padding: 1px 5px;
      border-radius: 10px;
      background: rgba(33,150,243,0.12);
      color: #2196F3;
      border: 1px solid rgba(33,150,243,0.3);
    }
    .badge-sec-clauses {
      font-size: 0.58rem;
      padding: 1px 5px;
      border-radius: 10px;
      background: rgba(76,175,80,0.12);
      color: #4CAF50;
      border: 1px solid rgba(76,175,80,0.3);
    }

    /* ── DORA Register table columns ───────────────────────────── */
    .table-header--dora { gap: 8px; }
    .dora-col-vendor { flex: 3; }
    .dora-col-entity { flex: 1.5; }
    .dora-col-ict    { flex: 1.5; }
    .dora-col-sub    { flex: 1; }
    .dora-col-ref    { flex: 1.5; }
    .dora-col-crit   { width: 80px; }
    .dora-entity-type { font-size: 0.75rem; color: #2196F3; }

    /* ── DORA loading state ────────────────────────────────────── */
    .dora-loading {
      height: 200px;
      background: rgba(255,255,255,0.04);
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    /* ── Typography helpers ────────────────────────────────────── */
    .text-meta    { font-size: 0.65rem; color: var(--mat-sys-on-surface-variant); }
    .text-xs-muted { font-size: 0.63rem; color: var(--mat-sys-on-surface-variant); }
    .text-muted-sm { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
    .text-sm       { font-size: 0.72rem; }
  `],
})
export class TprmComponent {
  private api    = inject(TprmApiService)
  private dialog = inject(MatDialog)
  private qc     = injectQueryClient()

  toLabel      = toLabel
  fmtDate      = fmtDate
  criticalities = CRITICALITIES
  statuses      = STATUSES
  statusLabels  = STATUS_LABELS

  activeTab      = signal(0)
  critFilter     = signal('')
  statusFilter   = signal('')
  expandedVendor = signal<string | null>(null)

  // ── Queries ──────────────────────────────────────────────────────────────

  summaryQ = injectQuery(() => ({
    queryKey: ['tprm-summary'],
    queryFn: () => firstValueFrom(this.api.summary()),
  }))

  vendorsQ = injectQuery(() => ({
    queryKey: ['vendors', this.critFilter(), this.statusFilter()],
    queryFn: () => firstValueFrom(this.api.list({
      ...(this.critFilter()  ? { criticality: this.critFilter()  } : {}),
      ...(this.statusFilter() ? { status: this.statusFilter() } : {}),
    })),
  }))

  doraQ = injectQuery(() => ({
    queryKey: ['dora-register'],
    queryFn:  () => firstValueFrom(this.api.doraRegister()),
    enabled:  this.activeTab() === 1,
  }))

  // Per-vendor sub-queries (lazy, enabled only when expanded)
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  private assessmentQueries = new Map<string, any>()
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  private contractQueries   = new Map<string, any>()

  getAssessments(vendorId: string) {
    if (!this.assessmentQueries.has(vendorId)) {
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      const q = injectQuery(() => ({
        queryKey: ['vendor-assessments', vendorId],
        queryFn:  () => firstValueFrom(this.api.listAssessments(vendorId)),
        enabled:  this.expandedVendor() === vendorId,
      })) as any
      this.assessmentQueries.set(vendorId, q)
    }
    return this.assessmentQueries.get(vendorId)!
  }

  getContracts(vendorId: string) {
    if (!this.contractQueries.has(vendorId)) {
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      const q = injectQuery(() => ({
        queryKey: ['vendor-contracts', vendorId],
        queryFn:  () => firstValueFrom(this.api.listContracts(vendorId)),
        enabled:  this.expandedVendor() === vendorId,
      })) as any
      this.contractQueries.set(vendorId, q)
    }
    return this.contractQueries.get(vendorId)!
  }

  // ── Mutation ─────────────────────────────────────────────────────────────

  deleteMut = injectMutation(() => ({
    mutationFn: (id: string) => firstValueFrom(this.api.delete(id)),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['vendors'] })
      this.qc.invalidateQueries({ queryKey: ['tprm-summary'] })
    },
  }))

  // ── Summary cards ─────────────────────────────────────────────────────────

  summaryCards = computed(() => {
    const d = this.summaryQ.data()
    return [
      { label: 'Total Vendors',      value: d?.total                   ?? 0, color: '#607D8B' },
      { label: 'Active',             value: d?.active                  ?? 0, color: '#4CAF50' },
      { label: 'Critical',           value: d?.critical                ?? 0, color: '#9C27B0' },
      { label: 'DORA-Regulated',     value: d?.dora_regulated          ?? 0, color: '#2196F3' },
      { label: 'Contracts Expiring', value: d?.contracts_expiring_soon ?? 0, color: '#FF9800' },
    ]
  })

  // ── Actions ───────────────────────────────────────────────────────────────

  toggleExpand(id: string) {
    this.expandedVendor.set(this.expandedVendor() === id ? null : id)
  }

  openCreate() {
    const ref = this.dialog.open(VendorDialogComponent, { maxWidth: '560px', width: '100%' })
    ref.componentInstance.data = {}
  }

  openEdit(v: Vendor) {
    const ref = this.dialog.open(VendorDialogComponent, { maxWidth: '560px', width: '100%' })
    ref.componentInstance.data = { existing: v }
  }

  deleteVendor(v: Vendor) {
    if (!confirm(`Delete "${v.name}"?`)) return
    this.deleteMut.mutate(v.id)
  }

  openAssessDialog(vendorId: string) {
    const ref = this.dialog.open(AssessmentDialogComponent, { maxWidth: '480px', width: '100%' })
    ref.componentInstance.data = { vendorId }
  }

  openContractDialog(vendorId: string) {
    const ref = this.dialog.open(ContractDialogComponent, { maxWidth: '480px', width: '100%' })
    ref.componentInstance.data = { vendorId }
  }

  refetchVendors() {
    this.qc.invalidateQueries({ queryKey: ['vendors'] })
  }

  clearFilters() {
    this.critFilter.set('')
    this.statusFilter.set('')
  }

  // ── Style helpers ─────────────────────────────────────────────────────────

  critChipStyle(crit: string): string {
    const color = CRIT_COLORS[crit] ?? '#9E9E9E'
    return `font-size:0.62rem;font-weight:700;padding:2px 6px;border-radius:10px;background:${color}18;color:${color};border:1px solid ${color}40`
  }

  statusChipStyle(status: string): string {
    const color = STATUS_COLORS[status] ?? '#9E9E9E'
    const label = STATUS_LABELS[status] ?? toLabel(status)
    void label
    return `font-size:0.62rem;font-weight:600;padding:2px 6px;border-radius:10px;background:${color}18;color:${color};border:1px solid ${color}40`
  }

  scoreChipStyle(score: number | null): string {
    if (score == null) return 'font-size:0.62rem;color:var(--mat-sys-on-surface-variant)'
    const color = score >= 75 ? '#4CAF50' : score >= 50 ? '#FF9800' : '#F44336'
    return `font-size:0.62rem;font-weight:700;padding:1px 5px;border-radius:10px;min-width:22px;text-align:center;background:${color}18;color:${color};border:1px solid ${color}40`
  }

  assessStatusStyle(status: string): string {
    const color = ASSESSMENT_STATUS_COLORS[status] ?? '#607D8B'
    return `font-size:0.6rem;font-weight:600;padding:1px 5px;border-radius:10px;background:${color}18;color:${color};border:1px solid ${color}40`
  }
}
