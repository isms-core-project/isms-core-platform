import { Component, inject, signal, computed, Input, Output, EventEmitter } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { HttpClient } from '@angular/common/http'
import { firstValueFrom } from 'rxjs'

import { injectQuery, injectMutation, injectQueryClient } from '@tanstack/angular-query-experimental'

import { MatCardModule } from '@angular/material/card'
import { MatButtonModule } from '@angular/material/button'
import { MatIconModule } from '@angular/material/icon'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatChipsModule } from '@angular/material/chips'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatDialogModule, MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog'

import { AuthService } from '../../core/services/auth.service'
import { OrgApiService } from '../../api/org-api.service'
import { OrganisationRead } from '../../shared/types'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

// ─── Types ────────────────────────────────────────────────────────────────────

interface OrganisationCreate {
  name: string
  slug: string
  description?: string
  governance_mode?: string
  country?: string | null
}

interface OrganisationPatch {
  name?: string
  description?: string
  governance_mode?: string
  country?: string | null
  settings?: Record<string, unknown>
}

// ─── Country options ──────────────────────────────────────────────────────────

const COUNTRY_OPTIONS = [
  { code: '',  label: 'Switzerland (default)' },
  { code: 'fr', label: 'France' },
  { code: 'be', label: 'Belgium' },
  { code: 'lu', label: 'Luxembourg' },
  { code: 'de', label: 'Germany' },
  { code: 'at', label: 'Austria' },
  { code: 'it', label: 'Italy' },
  { code: 'gb', label: 'United Kingdom' },
]

function fmtDate(iso: string): string {
  return new Date(iso).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' })
}

function deriveSlug(name: string): string {
  return name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 60)
}

// ─── Confirm Dialog ───────────────────────────────────────────────────────────

@Component({
  selector: 'app-org-confirm-dialog',
  standalone: true,
  imports: [MatButtonModule, MatDialogModule],
  template: `
    <h2 mat-dialog-title>{{ data.title }}</h2>
    <mat-dialog-content>{{ data.message }}</mat-dialog-content>
    <mat-dialog-actions>
      <button mat-button [mat-dialog-close]="false">Cancel</button>
      <button mat-raised-button color="warn" [mat-dialog-close]="true">{{ data.confirmLabel ?? 'Confirm' }}</button>
    </mat-dialog-actions>
  `,
})
export class OrgConfirmDialogComponent {
  readonly data = inject<{ title: string; message: string; confirmLabel?: string }>(MAT_DIALOG_DATA)
}

// ─── Alert Dialog ─────────────────────────────────────────────────────────────

@Component({
  selector: 'app-org-alert-dialog',
  standalone: true,
  imports: [MatButtonModule, MatDialogModule],
  template: `
    <h2 mat-dialog-title>Error</h2>
    <mat-dialog-content>{{ data.message }}</mat-dialog-content>
    <mat-dialog-actions>
      <button mat-raised-button color="primary" mat-dialog-close>OK</button>
    </mat-dialog-actions>
  `,
})
export class OrgAlertDialogComponent {
  readonly data = inject<{ message: string }>(MAT_DIALOG_DATA)
}

// ─── Create Org Dialog ────────────────────────────────────────────────────────

@Component({
  selector: 'app-create-org-dialog',
  standalone: true,
  imports: [
    FormsModule,
    MatButtonModule, MatDialogModule, MatFormFieldModule, MatInputModule,
    MatSelectModule, MatIconModule, MatProgressSpinnerModule,
  ],
  template: `
    <h2 mat-dialog-title>
      New Organisation
      <small class="dialog-subtitle">Add a new tenant to the platform</small>
    </h2>

    <mat-dialog-content class="create-org-content">
      @if (errorMsg()) {
        <div class="alert-error">{{ errorMsg() }}</div>
      }

      <mat-form-field appearance="outline" class="form-field-full form-field-mb" subscriptSizing="dynamic">
        <mat-label>Organisation name</mat-label>
        <input matInput [(ngModel)]="form.name" (ngModelChange)="onNameChange($event)"
          placeholder="e.g. Acme Corporation" />
      </mat-form-field>

      <mat-form-field appearance="outline" class="form-field-full form-field-mb" subscriptSizing="dynamic">
        <mat-label>Slug</mat-label>
        <input matInput [(ngModel)]="form.slug" placeholder="e.g. acme-corporation" />
        <mat-hint>Unique identifier — lowercase letters, numbers, hyphens</mat-hint>
      </mat-form-field>

      <mat-form-field appearance="outline" class="form-field-full form-field-mb" subscriptSizing="dynamic">
        <mat-label>Description (optional)</mat-label>
        <textarea matInput [(ngModel)]="form.description" rows="2"></textarea>
      </mat-form-field>

      <mat-form-field appearance="outline" class="form-field-full" subscriptSizing="dynamic">
        <mat-label>Country / Regulatory jurisdiction</mat-label>
        <mat-select [(ngModel)]="form.country">
          @for (o of countryOptions; track o.code) {
            <mat-option [value]="o.code">{{ o.label }}</mat-option>
          }
        </mat-select>
      </mat-form-field>
    </mat-dialog-content>

    <mat-dialog-actions>
      <button mat-button mat-dialog-close>Cancel</button>
      <button mat-raised-button color="primary"
        [disabled]="createMutation.isPending()"
        (click)="submit()">
        {{ createMutation.isPending() ? 'Creating…' : 'Create' }}
      </button>
    </mat-dialog-actions>
  `,
  styles: [`
    .create-org-content { min-width: 480px; padding-top: 16px !important; }
    .dialog-subtitle { display: block; font-size: 0.75rem; font-weight: 400; color: var(--mat-sys-on-surface-variant); margin-top: 2px; }
    .form-field-full { width: 100%; }
    .form-field-mb { margin-bottom: 12px; }
    .alert-error {
      padding: 10px 14px; border-radius: 6px; font-size: 0.85rem; margin-bottom: 12px;
      background: rgba(192,0,0,0.1); border: 1px solid rgba(192,0,0,0.3); color: var(--mat-sys-error);
    }
  `],
})
export class CreateOrgDialogComponent {
  private dialogRef = inject(MatDialogRef<CreateOrgDialogComponent>)
  private http = inject(HttpClient)
  private qc = injectQueryClient()

  readonly countryOptions = COUNTRY_OPTIONS

  form: OrganisationCreate & { country: string } = { name: '', slug: '', description: '', country: '' }
  errorMsg = signal('')

  createMutation = injectMutation(() => ({
    mutationFn: (body: OrganisationCreate) =>
      firstValueFrom(this.http.post<OrganisationRead>('/api/v1/organisation/', body)),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['organisations'] })
      this.dialogRef.close()
    },
    onError: () => this.errorMsg.set('Failed to create organisation — check slug is unique.'),
  }))

  onNameChange(name: string): void {
    if (!this.form.slug) {
      this.form.slug = deriveSlug(name)
    }
  }

  submit(): void {
    if (!this.form.name.trim()) { this.errorMsg.set('Name is required.'); return }
    if (!this.form.slug.trim()) { this.errorMsg.set('Slug is required.'); return }
    if (!/^[a-z0-9-]+$/.test(this.form.slug)) {
      this.errorMsg.set('Slug must be lowercase letters, numbers, and hyphens only.')
      return
    }
    this.errorMsg.set('')
    this.createMutation.mutate({
      name: this.form.name,
      slug: this.form.slug,
      description: this.form.description || undefined,
      country: this.form.country || null,
    })
  }
}

// ─── Edit Org Dialog (inline modal) ──────────────────────────────────────────

@Component({
  selector: 'app-edit-org-dialog',
  standalone: true,
  imports: [
    FormsModule,
    MatButtonModule, MatDialogModule, MatFormFieldModule, MatInputModule,
    MatSelectModule, MatIconModule, MatProgressSpinnerModule,
  ],
  template: `
    <h2 mat-dialog-title>Edit Organisation</h2>

    <mat-dialog-content class="edit-org-content">
      @if (errorMsg()) {
        <div class="alert-error">{{ errorMsg() }}</div>
      }

      <mat-form-field appearance="outline" class="form-field-full form-field-mb" subscriptSizing="dynamic">
        <mat-label>Name</mat-label>
        <input matInput [(ngModel)]="form.name" />
      </mat-form-field>

      <mat-form-field appearance="outline" class="form-field-full form-field-mb" subscriptSizing="dynamic">
        <mat-label>Description</mat-label>
        <textarea matInput [(ngModel)]="form.description" rows="2"></textarea>
      </mat-form-field>

      <mat-form-field appearance="outline" class="form-field-full" subscriptSizing="dynamic">
        <mat-label>Country / Regulatory jurisdiction</mat-label>
        <mat-select [(ngModel)]="form.country">
          @for (o of countryOptions; track o.code) {
            <mat-option [value]="o.code">{{ o.label }}</mat-option>
          }
        </mat-select>
      </mat-form-field>
    </mat-dialog-content>

    <mat-dialog-actions>
      <button mat-button mat-dialog-close>Cancel</button>
      <button mat-raised-button color="primary"
        [disabled]="saveMutation.isPending()"
        (click)="save()">
        {{ saveMutation.isPending() ? 'Saving…' : 'Save' }}
      </button>
    </mat-dialog-actions>
  `,
  styles: [`
    .edit-org-content { min-width: 480px; padding-top: 16px !important; }
    .form-field-full { width: 100%; }
    .form-field-mb { margin-bottom: 12px; }
    .alert-error {
      padding: 10px 14px; border-radius: 6px; font-size: 0.85rem; margin-bottom: 12px;
      background: rgba(192,0,0,0.1); border: 1px solid rgba(192,0,0,0.3); color: var(--mat-sys-error);
    }
  `],
})
export class EditOrgDialogComponent {
  private dialogRef = inject(MatDialogRef<EditOrgDialogComponent>)
  readonly data = inject<{ org: OrganisationRead }>(MAT_DIALOG_DATA)

  private http = inject(HttpClient)
  private qc = injectQueryClient()

  readonly countryOptions = COUNTRY_OPTIONS

  form: { name: string; description: string; country: string } = {
    name: this.data.org.name,
    description: this.data.org.description ?? '',
    country: this.data.org.country ?? '',
  }
  errorMsg = signal('')

  saveMutation = injectMutation(() => ({
    mutationFn: (body: OrganisationPatch) =>
      firstValueFrom(this.http.patch<OrganisationRead>(`/api/v1/organisation/${this.data.org.id}`, body)),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['organisations'] })
      this.dialogRef.close()
    },
    onError: () => this.errorMsg.set('Failed to update organisation.'),
  }))

  save(): void {
    this.errorMsg.set('')
    this.saveMutation.mutate({
      name: this.form.name,
      description: this.form.description || undefined,
      country: this.form.country || null,
    })
  }
}

// ─── Org Card ─────────────────────────────────────────────────────────────────

@Component({
  selector: 'app-org-card',
  standalone: true,
  imports: [
    MatCardModule, MatButtonModule, MatIconModule, MatTooltipModule, MatChipsModule,
    MatDialogModule,
  ],
  template: `
    <mat-card [style.opacity]="archived() ? '0.55' : '1'" class="org-card">
      <mat-card-content>
        <div class="card-header-row">
          <div class="card-name-row">
            <mat-icon [style.color]="archived() ? 'var(--mat-sys-on-surface-variant)' : '#4472C4'"
              class="org-icon">business</mat-icon>
            <span class="org-name"
              [style.color]="archived() ? 'var(--mat-sys-on-surface-variant)' : 'inherit'">
              {{ org.name }}
            </span>
            @if (archived()) {
              <span class="chip chip-archived">archived</span>
            }
          </div>

          @if (isSuperAdmin) {
            <div class="card-actions-row">
              <button mat-icon-button class="card-action-btn"
                matTooltip="Edit" (click)="openEdit()">
                <mat-icon class="card-action-icon">edit</mat-icon>
              </button>
              <button mat-icon-button class="card-action-btn"
                [matTooltip]="archived() ? 'Restore' : 'Archive'"
                [disabled]="archiveMutation.isPending()"
                (click)="archiveMutation.mutate(undefined)">
                <mat-icon class="card-action-icon">{{ archived() ? 'unarchive' : 'archive' }}</mat-icon>
              </button>
              <button mat-icon-button class="card-action-btn card-action-btn--danger"
                matTooltip="Delete"
                [disabled]="deleteMutation.isPending()"
                (click)="confirmDelete()">
                <mat-icon class="card-action-icon">delete</mat-icon>
              </button>
            </div>
          }
        </div>

        <div class="org-slug">
          {{ org.slug }}
        </div>

        @if (org.description) {
          <div class="org-description">
            {{ org.description }}
          </div>
        }

        <div class="chip-row">
          <span class="chip"
            [style.background]="org.governance_mode === 'platform' ? 'rgba(68,114,196,0.1)' : 'rgba(255,152,0,0.1)'"
            [style.color]="org.governance_mode === 'platform' ? '#4472C4' : '#FF9800'">
            {{ org.governance_mode }}
          </span>
          <span class="chip chip-privacy">{{ org.privacy_role }}</span>
          <span class="chip chip-country">{{ org.country ? org.country.toUpperCase() : 'CH' }}</span>
        </div>

        <div class="org-created-date">
          Created {{ fmtDate(org.created_at) }}
        </div>
      </mat-card-content>
    </mat-card>
  `,
  styles: [`
    .org-card { height: 100%; border: 1px solid var(--mat-sys-outline-variant); }
    .card-header-row { display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 8px; }
    .card-name-row { display: flex; align-items: center; gap: 8px; }
    .org-icon { font-size: 20px; width: 20px; height: 20px; }
    .org-name { font-weight: 600; font-size: 0.9rem; }
    .card-actions-row { display: flex; gap: 2px; }
    .card-action-btn { width: 28px; height: 28px; line-height: 28px; }
    .card-action-btn--danger { color: var(--mat-sys-error); }
    .card-action-icon { font-size: 14px; }
    .org-slug { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); margin-bottom: 8px; }
    .org-description { font-size: 0.8rem; color: var(--mat-sys-on-surface-variant); margin-bottom: 12px; }
    .chip-row { display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 12px; }
    .org-created-date { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
    .chip {
      display: inline-block; height: 20px; line-height: 20px;
      padding: 0 8px; border-radius: 10px; font-size: 0.68rem; font-weight: 500;
    }
    .chip-archived { background: rgba(158,158,158,0.15); color: var(--mat-sys-on-surface-variant); }
    .chip-privacy  { background: rgba(112,48,160,0.1); color: #7030A0; }
    .chip-country  { background: rgba(0,150,136,0.1); color: #00897B; }
  `],
})
export class OrgCardComponent {
  @Input() org!: OrganisationRead
  @Input() isSuperAdmin = false

  private http = inject(HttpClient)
  private qc = injectQueryClient()
  private dialog = inject(MatDialog)

  archived = computed(() => !this.org.is_active)

  archiveMutation = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.http.patch<OrganisationRead>(`/api/v1/organisation/${this.org.id}/archive`, {})),
    onSuccess: () => this.qc.invalidateQueries({ queryKey: ['organisations'] }),
  }))

  deleteMutation = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.http.delete(`/api/v1/organisation/${this.org.id}`)),
    onSuccess: () => this.qc.invalidateQueries({ queryKey: ['organisations'] }),
    onError: (e: unknown) => {
      const detail = (e as { error?: { detail?: string } })?.error?.detail
      this.dialog.open(OrgAlertDialogComponent, {
        data: { message: detail ?? 'Delete failed — organisation may have users or projects.' },
      })
    },
  }))

  openEdit(): void {
    this.dialog.open(EditOrgDialogComponent, { data: { org: this.org }, width: '560px' })
  }

  confirmDelete(): void {
    const ref = this.dialog.open(OrgConfirmDialogComponent, {
      data: {
        title: 'Delete Organisation',
        message: `Permanently delete "${this.org.name}"? This cannot be undone.`,
        confirmLabel: 'Delete',
      },
    })
    ref.afterClosed().subscribe((ok: boolean) => { if (ok) this.deleteMutation.mutate(undefined) })
  }

  fmtDate(iso: string): string { return fmtDate(iso) }
}

// ─── Main Page ────────────────────────────────────────────────────────────────

@Component({
  selector: 'app-organisations',
  standalone: true,
  imports: [
    MatButtonModule, MatIconModule, MatProgressSpinnerModule, MatChipsModule,
    MatDialogModule,
    PageHeaderComponent, OrgCardComponent,
  ],
  template: `
    <div class="page-wrap">
      <app-page-header
        [title]="'Organisations'"
        [subtitle]="isSuperAdmin() ? 'All tenants on this platform' : 'Your organisation'">
        <div actions class="header-actions">
          <button mat-stroked-button (click)="qc.invalidateQueries({ queryKey: ['organisations'] })">
            <mat-icon>refresh</mat-icon>
            Refresh
          </button>
          @if (isSuperAdmin()) {
            <button mat-raised-button color="primary" (click)="openCreate()">
              <mat-icon>add</mat-icon>
              New Organisation
            </button>
          }
        </div>
      </app-page-header>

      <!-- Access guard -->
      @if (!hasAccess()) {
        <div class="alert-error">Admin or Super Admin role required.</div>
      }

      <!-- Error -->
      @if (orgsQuery.isError()) {
        <div class="alert-error alert-error-mb">Failed to load organisations.</div>
      }

      <!-- Grid -->
      <div class="org-grid">
        @if (orgsQuery.isLoading()) {
          @for (i of [1,2,3]; track i) {
            <div class="org-skel"></div>
          }
        } @else {
          @for (org of orgsQuery.data() ?? []; track org.id) {
            <app-org-card [org]="org" [isSuperAdmin]="isSuperAdmin()" />
          }
        }
      </div>
    </div>

  `,
  styles: [`
    :host { display: block; }

    .page-wrap { padding: 24px; }
    .header-actions { display: flex; gap: 8px; }

    .org-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 16px;
    }
    .org-skel { height: 160px; border-radius: 4px; background: var(--mat-sys-surface-variant); }

    .alert-error {
      padding: 10px 14px; border-radius: 6px; font-size: 0.875rem; margin-bottom: 16px;
      background: rgba(192,0,0,0.1); border: 1px solid rgba(192,0,0,0.3); color: var(--mat-sys-error);
    }
    .alert-error-mb { margin-bottom: 16px; }
  `],
})
export class OrganisationsComponent {
  private auth = inject(AuthService)
  private orgApi = inject(OrgApiService)
  private http = inject(HttpClient)
  private dialog = inject(MatDialog)
  readonly qc = injectQueryClient()

  isSuperAdmin = computed(() => this.auth.isSuperAdmin())
  hasAccess = computed(() => {
    const role = this.auth.user()?.role
    return role === 'super_admin' || role === 'admin'
  })

  orgsQuery = injectQuery(() => ({
    queryKey: ['organisations', this.isSuperAdmin()],
    queryFn: () => this.isSuperAdmin()
      ? firstValueFrom(this.http.get<OrganisationRead[]>('/api/v1/organisation/all'))
      : firstValueFrom(this.orgApi.get()).then(o => [o]),
    enabled: this.hasAccess(),
  }))

  openCreate(): void {
    this.dialog.open(CreateOrgDialogComponent, { width: '560px' })
  }
}
