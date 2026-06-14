import { Component, inject, signal, computed } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'

import { injectQuery, injectMutation, injectQueryClient } from '@tanstack/angular-query-experimental'

import { MatTabsModule } from '@angular/material/tabs'
import { MatCardModule } from '@angular/material/card'
import { MatTableModule } from '@angular/material/table'
import { MatButtonModule } from '@angular/material/button'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatDialogModule, MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog'
import { MatIconModule } from '@angular/material/icon'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatSlideToggleModule } from '@angular/material/slide-toggle'
import { MatChipsModule } from '@angular/material/chips'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatProgressBarModule } from '@angular/material/progress-bar'
import { MatDividerModule } from '@angular/material/divider'

import {
  AdminApiService,
  UserRead,
  UserCreate,
  UserPatch,
  GroupEntry,
  SessionEntry,
} from '../../api/admin-api.service'
import { AuthService } from '../../core/services/auth.service'
import { ThemeService } from '../../core/services/theme.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'
import { ExpandableCardComponent } from '../../shared/components/expandable-card.component'

// ── Color maps ───────────────────────────────────────────────────────────────

const ROLE_DARK: Record<string, { bg: string; fg: string }> = {
  super_admin:   { bg: 'rgba(192,0,0,0.35)',     fg: '#FF6B6B' },
  admin:         { bg: 'rgba(192,0,0,0.18)',     fg: '#FFC7CE' },
  isms_manager:  { bg: 'rgba(68,114,196,0.2)',   fg: '#9DC3E6' },
  auditor:       { bg: 'rgba(112,173,71,0.15)',  fg: '#C6EFCE' },
  control_owner: { bg: 'rgba(255,192,0,0.15)',   fg: '#FFEB9C' },
  viewer:        { bg: 'rgba(255,255,255,0.07)', fg: '#d9d9d9' },
}
const ROLE_LIGHT: Record<string, { bg: string; fg: string }> = {
  super_admin:   { bg: 'rgba(163,45,45,0.15)',    fg: '#8A1F1F' },
  admin:         { bg: 'rgba(163,45,45,0.10)',    fg: '#A32D2D' },
  isms_manager:  { bg: 'rgba(24,95,165,0.11)',    fg: '#185FA5' },
  auditor:       { bg: 'rgba(29,158,117,0.12)',   fg: '#0F6E56' },
  control_owner: { bg: 'rgba(186,117,23,0.13)',   fg: '#7A4500' },
  viewer:        { bg: 'rgba(44,44,42,0.07)',     fg: '#444441' },
}

const ALL_ROLES    = ['super_admin', 'admin', 'isms_manager', 'auditor', 'control_owner', 'viewer']
const NON_SA_ROLES = ['admin', 'isms_manager', 'auditor', 'control_owner', 'viewer']

const NOTIF_EVENTS = [
  { event_type: 'email.gap_assigned',     label: 'Gap assigned',      category: 'Workflow' },
  { event_type: 'email.evidence_expiry',  label: 'Evidence expiry',   category: 'Workflow' },
  { event_type: 'email.qa_fail',          label: 'QA check failures', category: 'System'   },
  { event_type: 'email.import_completed', label: 'Import completed',  category: 'System'   },
]

function fmtDate(iso: string | null | undefined): string {
  if (!iso) return '—'
  return new Date(iso).toLocaleDateString('en-GB', {
    day: '2-digit', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit',
  })
}

function fmtDateShort(iso: string | null | undefined): string {
  if (!iso) return '—'
  return new Date(iso).toLocaleDateString('en-GB', {
    day: '2-digit', month: 'short', year: 'numeric',
  })
}

function fmtShort(iso: string | null | undefined): string {
  if (!iso) return '—'
  return new Date(iso).toLocaleDateString('en-GB', {
    day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit',
  })
}

function fmtFull(iso: string | null | undefined): string {
  if (!iso) return ''
  return new Date(iso).toLocaleDateString('en-GB', {
    day: '2-digit', month: 'short', year: 'numeric',
    hour: '2-digit', minute: '2-digit', second: '2-digit',
  })
}

// ── Confirm Dialog ───────────────────────────────────────────────────────────

@Component({
  selector: 'app-admin-confirm-dialog',
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
export class AdminConfirmDialogComponent {
  readonly data = inject<{ title: string; message: string; confirmLabel?: string }>(MAT_DIALOG_DATA)
}

// ── Create Group Dialog ──────────────────────────────────────────────────────

@Component({
  selector: 'app-create-group-dialog',
  standalone: true,
  imports: [
    FormsModule,
    MatButtonModule, MatDialogModule, MatFormFieldModule, MatInputModule, MatProgressSpinnerModule,
  ],
  template: `
    <h2 mat-dialog-title>Create Group</h2>
    <mat-dialog-content class="create-group-content">
      <mat-form-field appearance="outline" class="field-full field-mb">
        <mat-label>Group name *</mat-label>
        <input matInput [(ngModel)]="name" />
      </mat-form-field>
      <mat-form-field appearance="outline" class="field-full">
        <mat-label>Description (optional)</mat-label>
        <textarea matInput [(ngModel)]="description" rows="2"></textarea>
      </mat-form-field>
    </mat-dialog-content>
    <mat-dialog-actions>
      <button mat-button mat-dialog-close>Cancel</button>
      <button mat-raised-button color="primary"
        [disabled]="!name.trim() || pending"
        (click)="submit()">
        {{ pending ? 'Creating…' : 'Create' }}
      </button>
    </mat-dialog-actions>
  `,
  styles: [`
    .create-group-content { min-width: 340px; padding-top: 16px; }
    .field-full { width: 100%; }
    .field-mb { margin-bottom: 12px; }
  `],
})
export class CreateGroupDialogComponent {
  private dialogRef = inject(MatDialogRef<CreateGroupDialogComponent>)

  name = ''
  description = ''
  pending = false

  submit(): void {
    if (!this.name.trim()) return
    this.dialogRef.close({ name: this.name.trim(), description: this.description.trim() || undefined })
  }
}

// ── Create User Dialog ───────────────────────────────────────────────────────

@Component({
  selector: 'app-create-user-dialog',
  standalone: true,
  imports: [
    FormsModule,
    MatButtonModule, MatDialogModule, MatFormFieldModule,
    MatInputModule, MatSelectModule, MatProgressSpinnerModule,
  ],
  template: `
    <h2 mat-dialog-title>Add User</h2>
    <mat-dialog-content class="dialog-content-col dialog-content-create">
      @if (error()) {
        <div class="alert-error">{{ error() }}</div>
      }
      <mat-form-field appearance="outline" class="field-full">
        <mat-label>Email *</mat-label>
        <input matInput type="email" [(ngModel)]="form.email" />
      </mat-form-field>
      <mat-form-field appearance="outline" class="field-full">
        <mat-label>Username *</mat-label>
        <input matInput [(ngModel)]="form.username" />
      </mat-form-field>
      <mat-form-field appearance="outline" class="field-full">
        <mat-label>Full Name</mat-label>
        <input matInput [(ngModel)]="form.full_name" />
      </mat-form-field>
      <mat-form-field appearance="outline" class="field-full">
        <mat-label>Password *</mat-label>
        <input matInput type="password" [(ngModel)]="form.password" />
      </mat-form-field>
      <mat-form-field appearance="outline" class="field-full">
        <mat-label>Role</mat-label>
        <mat-select [(ngModel)]="form.role">
          @for (r of roles; track r) {
            <mat-option [value]="r">{{ r }}</mat-option>
          }
        </mat-select>
      </mat-form-field>
    </mat-dialog-content>
    <mat-dialog-actions align="end">
      <button mat-button mat-dialog-close>Cancel</button>
      <button mat-raised-button color="primary"
        [disabled]="!form.email || !form.username || !form.password || mutation.isPending()"
        (click)="submit()">
        {{ mutation.isPending() ? 'Creating…' : 'Create User' }}
      </button>
    </mat-dialog-actions>
  `,
  styles: [`
    .dialog-content-col { display: flex; flex-direction: column; gap: 14px; padding-top: 20px; }
    .dialog-content-create { min-width: 340px; }
    .field-full { width: 100%; }
    .alert-error { padding: 8px 12px; border-radius: 6px; font-size: 0.8rem; background: rgba(192,0,0,0.12); color: #FFC7CE; border: 1px solid rgba(192,0,0,0.25); }
  `],
})
export class CreateUserDialogComponent {
  private adminApi = inject(AdminApiService)
  private dialog_  = inject(MatDialog)
  private qc       = injectQueryClient()

  roles = ALL_ROLES
  error = signal<string | null>(null)
  form: UserCreate & { full_name?: string } = {
    email: '', username: '', password: '', full_name: '', role: 'viewer',
  }

  mutation = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.adminApi.createUser(this.form)),
    onSuccess:  () => {
      this.qc.invalidateQueries({ queryKey: ['admin', 'users'] })
      this.dialog_.closeAll()
    },
    onError: (err: unknown) => {
      const msg = (err as { error?: { detail?: string } })?.error?.detail ?? 'Create failed'
      this.error.set(String(msg))
    },
  }))

  submit(): void { this.mutation.mutate(undefined) }
}

// ── Edit User Dialog ─────────────────────────────────────────────────────────

@Component({
  selector: 'app-edit-user-dialog',
  standalone: true,
  imports: [
    FormsModule,
    MatButtonModule, MatDialogModule, MatFormFieldModule,
    MatInputModule, MatSelectModule, MatProgressSpinnerModule,
    MatSlideToggleModule, MatDividerModule,
  ],
  template: `
    <h2 mat-dialog-title>
      Edit User
      <small class="dialog-subtitle">
        {{ user?.email }}
      </small>
    </h2>
    <mat-dialog-content class="dialog-content-col dialog-content-edit">
      @if (error()) {
        <div class="alert-error">{{ error() }}</div>
      }
      <mat-form-field appearance="outline" class="field-full">
        <mat-label>Full Name</mat-label>
        <input matInput [(ngModel)]="fullName" />
      </mat-form-field>
      <mat-form-field appearance="outline" class="field-full">
        <mat-label>Role</mat-label>
        <mat-select [(ngModel)]="role">
          @for (r of availableRoles; track r) {
            <mat-option [value]="r">{{ r }}</mat-option>
          }
        </mat-select>
      </mat-form-field>
      <mat-slide-toggle [(ngModel)]="isActive">Active</mat-slide-toggle>
      <mat-form-field appearance="outline" class="field-full">
        <mat-label>New Password</mat-label>
        <input matInput type="password" [(ngModel)]="newPassword" />
        <mat-hint>Leave blank to keep current password</mat-hint>
      </mat-form-field>
      <mat-divider />
      <p class="notif-section-label">
        Email Notifications
      </p>
      @for (ev of notifEvents; track ev.event_type) {
        <div class="notif-row">
          <div>
            <span class="notif-label">{{ ev.label }}</span>
            <span class="notif-category">{{ ev.category }}</span>
          </div>
          <mat-slide-toggle
            [checked]="notifPrefs[ev.event_type] ?? true"
            (change)="notifPrefs[ev.event_type] = $event.checked" />
        </div>
      }
    </mat-dialog-content>
    <mat-dialog-actions align="end">
      <button mat-button mat-dialog-close>Cancel</button>
      <button mat-raised-button color="primary"
        [disabled]="mutation.isPending()"
        (click)="submit()">
        {{ mutation.isPending() ? 'Saving…' : 'Save' }}
      </button>
    </mat-dialog-actions>
  `,
  styles: [`
    .dialog-content-col { display: flex; flex-direction: column; gap: 12px; padding-top: 20px; }
    .dialog-content-edit { min-width: 340px; }
    .dialog-subtitle { display: block; font-size: 0.75rem; font-weight: 400; color: var(--mat-sys-on-surface-variant); }
    .field-full { width: 100%; }
    .notif-section-label { font-size: 0.78rem; font-weight: 600; color: var(--mat-sys-on-surface-variant); margin: 0; }
    .notif-row { display: flex; align-items: center; justify-content: space-between; }
    .notif-label { font-size: 0.85rem; }
    .notif-category { font-size: 0.75rem; color: var(--mat-sys-on-surface-variant); margin-left: 6px; }
    .alert-error { padding: 8px 12px; border-radius: 6px; font-size: 0.8rem; background: rgba(192,0,0,0.12); color: #FFC7CE; border: 1px solid rgba(192,0,0,0.25); }
  `],
})
export class EditUserDialogComponent {
  private adminApi = inject(AdminApiService)
  private dialog_  = inject(MatDialog)
  private qc       = injectQueryClient()

  user: UserRead | null = null
  isSuperAdmin = false
  notifEvents  = NOTIF_EVENTS

  error       = signal<string | null>(null)
  fullName    = ''
  role        = 'viewer'
  isActive    = true
  newPassword = ''
  notifPrefs: Record<string, boolean> = {}

  get availableRoles() { return this.isSuperAdmin ? ALL_ROLES : NON_SA_ROLES }

  init(u: UserRead, isSuperAdmin: boolean): void {
    this.user        = u
    this.isSuperAdmin = isSuperAdmin
    this.fullName    = u.full_name ?? ''
    this.role        = u.role
    this.isActive    = u.is_active
    this.newPassword = ''
    this.notifPrefs  = {}
  }

  mutation = injectMutation(() => ({
    mutationFn: () => {
      if (!this.user) return Promise.reject('No user')
      const patch: UserPatch = {
        full_name: this.fullName || undefined,
        role:      this.role,
        is_active: this.isActive,
      }
      if (this.newPassword) patch.password = this.newPassword
      return firstValueFrom(this.adminApi.updateUser(this.user.id, patch))
    },
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['admin', 'users'] })
      this.dialog_.closeAll()
    },
    onError: (err: unknown) => {
      const msg = (err as { error?: { detail?: string } })?.error?.detail ?? 'Update failed'
      this.error.set(String(msg))
    },
  }))

  submit(): void { this.mutation.mutate(undefined) }
}

// ── Manage Members Dialog ────────────────────────────────────────────────────

@Component({
  selector: 'app-manage-members-dialog',
  standalone: true,
  imports: [
    FormsModule,
    MatButtonModule, MatDialogModule, MatFormFieldModule,
    MatSelectModule, MatIconModule, MatProgressBarModule, MatTooltipModule,
  ],
  template: `
    <h2 mat-dialog-title>
      Manage Members
      <small class="dialog-subtitle">
        {{ group?.name }}
      </small>
    </h2>
    <mat-dialog-content class="members-dialog-content">
      @if (membersQuery.isLoading()) {
        <mat-progress-bar mode="indeterminate" class="members-loading-bar" />
      }
      <div class="members-add-row">
        <mat-form-field appearance="outline" class="field-flex">
          <mat-label>Add user</mat-label>
          <mat-select [(ngModel)]="addUserId">
            <mat-option value="">Select user…</mat-option>
            @for (u of nonMembers(); track u.id) {
              <mat-option [value]="u.id">{{ u.email }} · {{ u.role }}</mat-option>
            }
          </mat-select>
        </mat-form-field>
        <button mat-raised-button color="primary"
          [disabled]="!addUserId || addMutation.isPending()"
          (click)="addMember()">
          <mat-icon>group_add</mat-icon> Add
        </button>
      </div>
      <p class="members-section-label">
        Current members ({{ membersQuery.data()?.length ?? 0 }})
      </p>
      @if ((membersQuery.data()?.length ?? 0) === 0) {
        <p class="members-empty">No members yet.</p>
      }
      @for (m of membersQuery.data() ?? []; track m.user_id) {
        <div class="member-row">
          <div>
            <div class="member-email">{{ m.email }}</div>
            @if (m.full_name) {
              <div class="member-name">{{ m.full_name }}</div>
            }
          </div>
          <div class="member-actions">
            <span class="member-role-pill"
              [style.background]="roleColor(m.role).bg"
              [style.color]="roleColor(m.role).fg">
              {{ m.role }}
            </span>
            <button mat-icon-button class="btn-error"
              matTooltip="Remove from group"
              [disabled]="removeMutation.isPending()"
              (click)="removeMember(m.user_id)">
              <mat-icon>person_remove</mat-icon>
            </button>
          </div>
        </div>
      }
    </mat-dialog-content>
    <mat-dialog-actions align="end">
      <button mat-button mat-dialog-close>Close</button>
    </mat-dialog-actions>
  `,
  styles: [`
    .dialog-subtitle { display: block; font-size: 0.75rem; font-weight: 400; color: var(--mat-sys-on-surface-variant); }
    .members-dialog-content { min-width: 420px; padding-top: 12px; }
    .members-loading-bar { margin-bottom: 8px; }
    .members-add-row { display: flex; gap: 8px; margin-bottom: 16px; }
    .field-flex { flex: 1; }
    .members-section-label { font-size: 0.78rem; font-weight: 600; color: var(--mat-sys-on-surface-variant); margin: 0 0 6px; }
    .members-empty { font-size: 0.85rem; color: var(--mat-sys-on-surface-variant); }
    .member-row { display: flex; align-items: center; justify-content: space-between; padding: 6px 0; border-bottom: 1px solid rgba(255,255,255,0.06); }
    .member-email { font-family: monospace; font-size: 0.8rem; }
    .member-name { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
    .member-actions { display: flex; align-items: center; gap: 8px; }
    .member-role-pill { display: inline-block; padding: 1px 8px; border-radius: 9px; font-size: 0.6rem; height: 16px; line-height: 14px; }
    .btn-error { color: var(--mat-sys-error); }
  `],
})
export class ManageMembersDialogComponent {
  private adminApi = inject(AdminApiService)
  private qc       = injectQueryClient()

  group: GroupEntry | null = null
  allUsers: UserRead[]     = []
  addUserId = ''

  membersQuery = injectQuery(() => ({
    queryKey: ['admin', 'groups', this.group?.id, 'members'],
    queryFn:  () => this.group
      ? firstValueFrom(this.adminApi.getGroupMembers(this.group.id))
      : Promise.resolve([]),
    enabled:  !!this.group?.id,
  }))

  nonMembers = () => {
    const memberIds = new Set((this.membersQuery.data() ?? []).map(m => m.user_id))
    return this.allUsers.filter(u => !memberIds.has(u.id))
  }

  addMutation = injectMutation(() => ({
    mutationFn: (userId: string) =>
      firstValueFrom(this.adminApi.addGroupMember(this.group!.id, userId)),
    onSuccess:  () => {
      this.qc.invalidateQueries({ queryKey: ['admin', 'groups', this.group!.id, 'members'] })
      this.addUserId = ''
    },
  }))

  removeMutation = injectMutation(() => ({
    mutationFn: (userId: string) =>
      firstValueFrom(this.adminApi.removeGroupMember(this.group!.id, userId)),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['admin', 'groups', this.group!.id, 'members'] })
      this.qc.invalidateQueries({ queryKey: ['admin', 'groups'] })
    },
  }))

  addMember():               void { if (this.addUserId) this.addMutation.mutate(this.addUserId) }
  removeMember(uid: string): void { this.removeMutation.mutate(uid) }
  roleColor = (r: string) => ROLE_DARK[r] ?? ROLE_DARK['viewer']
}

// ── Main Admin Component ─────────────────────────────────────────────────────

@Component({
  selector: 'app-admin',
  standalone: true,
  imports: [
    FormsModule,
    MatTabsModule, MatCardModule, MatTableModule, MatButtonModule,
    MatFormFieldModule, MatInputModule, MatSelectModule,
    MatDialogModule, MatIconModule, MatProgressSpinnerModule,
    MatSlideToggleModule, MatChipsModule, MatTooltipModule,
    MatProgressBarModule, MatDividerModule,
    PageHeaderComponent,
    AdminConfirmDialogComponent, CreateGroupDialogComponent,
    CreateUserDialogComponent, EditUserDialogComponent,
    ManageMembersDialogComponent,
    ExpandableCardComponent,
  ],
  template: `
    @if (!canAccess()) {
      <div class="access-denied-wrap">
        <div class="alert-error">Admin role required to access this page.</div>
      </div>
    } @else {
      <app-page-header title="Administration"
        subtitle="User management, groups, MFA, and active sessions" />

      <mat-tab-group [(selectedIndex)]="activeTab" animationDuration="0" style="margin-top: 16px">

        <!-- ── Users tab ────────────────────────────────────────────────── -->
        <mat-tab>
          <ng-template mat-tab-label>
            <mat-icon class="tab-icon">people</mat-icon>
            Users
          </ng-template>
          <div class="tab-body">
            <app-expandable-card [expandable]="true" [initiallyExpanded]="true">
              <span card-title>
                <mat-icon>people</mat-icon>
                Users
                @if (usersQuery.data()) {
                  <span class="count-chip">{{ usersQuery.data()!.length }}</span>
                }
              </span>
              <button card-actions mat-stroked-button (click)="openCreateUser()">
                <mat-icon>person_add</mat-icon> Add User
              </button>

                <div class="table-scroll">
                  <table mat-table [dataSource]="usersQuery.data() ?? []" class="full-width">

                    <ng-container matColumnDef="email">
                      <th mat-header-cell *matHeaderCellDef>Email</th>
                      <td mat-cell *matCellDef="let u">
                        <span class="text-mono-sm">{{ u.email }}</span>
                      </td>
                    </ng-container>

                    <ng-container matColumnDef="username">
                      <th mat-header-cell *matHeaderCellDef>Username</th>
                      <td mat-cell *matCellDef="let u">
                        <span class="text-muted-sm">{{ u.username }}</span>
                      </td>
                    </ng-container>

                    <ng-container matColumnDef="full_name">
                      <th mat-header-cell *matHeaderCellDef>Name</th>
                      <td mat-cell *matCellDef="let u">
                        <span class="text-sm">{{ u.full_name ?? '—' }}</span>
                      </td>
                    </ng-container>

                    <ng-container matColumnDef="role">
                      <th mat-header-cell *matHeaderCellDef>Role</th>
                      <td mat-cell *matCellDef="let u">
                        <span class="chip-pill"
                          [style.background]="roleColor(u.role).bg"
                          [style.color]="roleColor(u.role).fg">
                          {{ u.role }}
                        </span>
                      </td>
                    </ng-container>

                    <ng-container matColumnDef="status">
                      <th mat-header-cell *matHeaderCellDef>Status</th>
                      <td mat-cell *matCellDef="let u">
                        <span class="chip-pill"
                          [style.background]="activeStyle(u.is_active).bg"
                          [style.color]="activeStyle(u.is_active).fg">
                          {{ u.is_active ? 'Active' : 'Inactive' }}
                        </span>
                      </td>
                    </ng-container>

                    <ng-container matColumnDef="mfa">
                      <th mat-header-cell *matHeaderCellDef>MFA</th>
                      <td mat-cell *matCellDef="let u">
                        <mat-icon
                          [matTooltip]="u.mfa_enabled ? 'MFA enabled' : 'MFA not set up'"
                          [style.color]="mfaIconColor(u.mfa_enabled)"
                          class="icon-16">
                          {{ u.mfa_enabled ? 'lock' : 'lock_open' }}
                        </mat-icon>
                      </td>
                    </ng-container>

                    <ng-container matColumnDef="last_login">
                      <th mat-header-cell *matHeaderCellDef>Last Login</th>
                      <td mat-cell *matCellDef="let u">
                        <span class="text-muted-xs">
                          {{ fmtDate(u.last_login) }}
                        </span>
                      </td>
                    </ng-container>

                    <ng-container matColumnDef="created_at">
                      <th mat-header-cell *matHeaderCellDef>Created</th>
                      <td mat-cell *matCellDef="let u">
                        <span class="text-muted-xs">
                          {{ fmtDateShort(u.created_at) }}
                        </span>
                      </td>
                    </ng-container>

                    <ng-container matColumnDef="actions">
                      <th mat-header-cell *matHeaderCellDef class="col-actions">Actions</th>
                      <td mat-cell *matCellDef="let u" class="col-actions">
                        <button mat-icon-button matTooltip="Edit" (click)="openEditUser(u)">
                          <mat-icon>edit</mat-icon>
                        </button>
                        @if (u.mfa_enabled) {
                          <button mat-icon-button matTooltip="Reset MFA"
                            class="btn-tertiary"
                            [disabled]="resetMfaMutation.isPending()"
                            (click)="resetMfa(u)">
                            <mat-icon>lock_reset</mat-icon>
                          </button>
                        }
                        <button mat-icon-button matTooltip="Delete"
                          class="btn-error"
                          [disabled]="deleteMutation.isPending()"
                          (click)="deleteUser(u)">
                          <mat-icon>delete</mat-icon>
                        </button>
                      </td>
                    </ng-container>

                    <tr mat-header-row *matHeaderRowDef="userColumns"></tr>
                    <tr mat-row *matRowDef="let row; columns: userColumns;" class="hover-row"></tr>
                  </table>
                </div>

                @if (usersQuery.isLoading()) {
                  <div class="loading-rows">
                    @for (_ of [1,2,3]; track $index) {
                      <div class="skeleton-row"></div>
                    }
                  </div>
                }
            </app-expandable-card>
          </div>
        </mat-tab>

        <!-- ── Groups tab ───────────────────────────────────────────────── -->
        <mat-tab>
          <ng-template mat-tab-label>
            <mat-icon class="tab-icon">groups</mat-icon>
            Groups
          </ng-template>
          <div class="tab-body">
            <app-expandable-card [expandable]="true" [initiallyExpanded]="true">
              <span card-title>
                <mat-icon>groups</mat-icon>
                Groups
                @if (groupsQuery.data()) {
                  <span class="count-chip">{{ groupsQuery.data()!.length }}</span>
                }
              </span>
              <button card-actions mat-stroked-button (click)="openCreateGroup()">
                <mat-icon>group_add</mat-icon> New Group
              </button>

                <div class="table-scroll">
                  <table mat-table [dataSource]="groupsQuery.data() ?? []" class="full-width">
                    <ng-container matColumnDef="name">
                      <th mat-header-cell *matHeaderCellDef>Name</th>
                      <td mat-cell *matCellDef="let g">
                        <span class="group-name">{{ g.name }}</span>
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="description">
                      <th mat-header-cell *matHeaderCellDef>Description</th>
                      <td mat-cell *matCellDef="let g">
                        <span class="text-muted-sm2">
                          {{ g.description ?? '—' }}
                        </span>
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="members">
                      <th mat-header-cell *matHeaderCellDef>Members</th>
                      <td mat-cell *matCellDef="let g">
                        <span class="count-chip">{{ g.member_count }}</span>
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="created_at">
                      <th mat-header-cell *matHeaderCellDef>Created</th>
                      <td mat-cell *matCellDef="let g">
                        <span class="text-muted-xs">
                          {{ fmtDateShort(g.created_at) }}
                        </span>
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="actions">
                      <th mat-header-cell *matHeaderCellDef class="col-actions">Actions</th>
                      <td mat-cell *matCellDef="let g" class="col-actions">
                        <button mat-icon-button matTooltip="Manage members"
                          (click)="openManageMembers(g)">
                          <mat-icon>people</mat-icon>
                        </button>
                        <button mat-icon-button matTooltip="Delete group"
                          class="btn-error"
                          [disabled]="deleteGroupMutation.isPending()"
                          (click)="deleteGroup(g)">
                          <mat-icon>delete</mat-icon>
                        </button>
                      </td>
                    </ng-container>
                    <tr mat-header-row *matHeaderRowDef="groupColumns"></tr>
                    <tr mat-row *matRowDef="let row; columns: groupColumns;" class="hover-row"></tr>
                  </table>
                </div>

                @if (!groupsQuery.isLoading() && (groupsQuery.data()?.length ?? 0) === 0) {
                  <div class="empty-state">
                    No groups yet. Create one to assign users.
                  </div>
                }
            </app-expandable-card>
          </div>
        </mat-tab>

        <!-- ── MFA Status tab ───────────────────────────────────────────── -->
        <mat-tab>
          <ng-template mat-tab-label>
            <mat-icon class="tab-icon">lock</mat-icon>
            MFA Status
          </ng-template>
          <div class="tab-body">
            <app-expandable-card [expandable]="true" [initiallyExpanded]="true">
              <span card-title>
                <mat-icon>lock</mat-icon>
                MFA Status
                @if (usersQuery.data()) {
                  <span class="count-chip"
                    [style.background]="mfaPctStyle().bg"
                    [style.color]="mfaPctStyle().fg">
                    {{ mfaEnrolled() }}/{{ usersQuery.data()!.length }} enrolled
                  </span>
                }
              </span>

                @if ((usersQuery.data()?.length ?? 0) > 0) {
                  <div class="mfa-progress-wrap">
                    <div class="mfa-progress-header">
                      <span class="text-muted-xs">MFA adoption</span>
                      <span class="text-muted-xs">{{ mfaPct() }}%</span>
                    </div>
                    <mat-progress-bar mode="determinate" [value]="mfaPct()"
                      class="mfa-progress-bar" />
                  </div>
                }

                <div class="filter-row">
                  @for (v of mfaFilters; track v.key) {
                    <button mat-stroked-button
                      [color]="mfaFilter() === v.key ? 'primary' : undefined"
                      (click)="mfaFilter.set(v.key)">
                      {{ v.label }}
                    </button>
                  }
                </div>

                <div class="table-scroll">
                  <table mat-table [dataSource]="filteredMfaUsers()" class="full-width">
                    <ng-container matColumnDef="email">
                      <th mat-header-cell *matHeaderCellDef>Email</th>
                      <td mat-cell *matCellDef="let u">
                        <span class="text-mono-xs">{{ u.email }}</span>
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="full_name">
                      <th mat-header-cell *matHeaderCellDef>Name</th>
                      <td mat-cell *matCellDef="let u">
                        <span class="text-sm">{{ u.full_name ?? '—' }}</span>
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="role">
                      <th mat-header-cell *matHeaderCellDef>Role</th>
                      <td mat-cell *matCellDef="let u">
                        <span class="chip-pill"
                          [style.background]="roleColor(u.role).bg"
                          [style.color]="roleColor(u.role).fg">
                          {{ u.role }}
                        </span>
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="mfa_status">
                      <th mat-header-cell *matHeaderCellDef>MFA Status</th>
                      <td mat-cell *matCellDef="let u">
                        <div class="mfa-status-cell">
                          <mat-icon class="icon-15"
                            [style.color]="mfaIconColor(u.mfa_enabled)">
                            {{ u.mfa_enabled ? 'lock' : 'lock_open' }}
                          </mat-icon>
                          <span class="text-xs"
                            [style.color]="mfaIconColor(u.mfa_enabled)">
                            {{ u.mfa_enabled ? 'Enrolled' : 'Not enrolled' }}
                          </span>
                        </div>
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="last_login">
                      <th mat-header-cell *matHeaderCellDef>Last Login</th>
                      <td mat-cell *matCellDef="let u">
                        <span class="text-muted-xs">
                          {{ fmtDate(u.last_login) }}
                        </span>
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="actions">
                      <th mat-header-cell *matHeaderCellDef class="col-actions">Actions</th>
                      <td mat-cell *matCellDef="let u" class="col-actions">
                        @if (u.mfa_enabled) {
                          <button mat-icon-button matTooltip="Reset MFA — user must re-enroll"
                            class="btn-tertiary"
                            [disabled]="resetMfaMutation.isPending()"
                            (click)="resetMfa(u)">
                            <mat-icon>lock_reset</mat-icon>
                          </button>
                        }
                      </td>
                    </ng-container>
                    <tr mat-header-row *matHeaderRowDef="mfaColumns"></tr>
                    <tr mat-row *matRowDef="let row; columns: mfaColumns;" class="hover-row"></tr>
                  </table>
                </div>
            </app-expandable-card>
          </div>
        </mat-tab>

        <!-- ── Sessions tab ─────────────────────────────────────────────── -->
        <mat-tab>
          <ng-template mat-tab-label>
            <mat-icon class="tab-icon">devices</mat-icon>
            Sessions
          </ng-template>
          <div class="tab-body">
            <app-expandable-card [expandable]="true" [initiallyExpanded]="true">
              <span card-title>
                <mat-icon>devices</mat-icon>
                Active Sessions
                @if (sessionsQuery.data()) {
                  <span class="count-chip">{{ sessionsQuery.data()!.length }}</span>
                }
                <span class="auto-refresh-label">
                  Auto-refreshes every 60s
                </span>
              </span>

                <div class="sessions-filter-wrap">
                  <mat-form-field appearance="outline" subscriptSizing="dynamic" class="sessions-filter-field">
                    <mat-label>Filter by email</mat-label>
                    <input matInput [(ngModel)]="sessionEmailFilter" />
                  </mat-form-field>
                </div>

                <div class="table-scroll">
                  <table mat-table [dataSource]="filteredSessions()" class="full-width">
                    <ng-container matColumnDef="user">
                      <th mat-header-cell *matHeaderCellDef>User</th>
                      <td mat-cell *matCellDef="let s">
                        <span class="text-mono-xs">
                          {{ s.user_email ?? s.user_id.slice(0,8) + '…' }}
                        </span>
                        @if (s.user_username) {
                          <span class="session-username">
                            {{ s.user_username }}
                          </span>
                        }
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="ip_address">
                      <th mat-header-cell *matHeaderCellDef>IP Address</th>
                      <td mat-cell *matCellDef="let s">
                        <span class="text-mono-xs text-muted">
                          {{ s.ip_address ?? '—' }}
                        </span>
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="user_agent">
                      <th mat-header-cell *matHeaderCellDef>User Agent</th>
                      <td mat-cell *matCellDef="let s" class="col-user-agent">
                        <span [matTooltip]="s.user_agent ?? ''"
                          class="user-agent-cell">
                          {{ s.user_agent ? s.user_agent.slice(0,60) + (s.user_agent.length > 60 ? '…' : '') : '—' }}
                        </span>
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="created_at">
                      <th mat-header-cell *matHeaderCellDef>Created</th>
                      <td mat-cell *matCellDef="let s">
                        <span class="text-muted-xs text-nowrap">
                          {{ fmtShort(s.created_at) }}
                        </span>
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="expires_at">
                      <th mat-header-cell *matHeaderCellDef>Expires</th>
                      <td mat-cell *matCellDef="let s">
                        <span [matTooltip]="fmtFull(s.expires_at)"
                          class="text-muted-xs text-nowrap">
                          {{ fmtShort(s.expires_at) }}
                        </span>
                      </td>
                    </ng-container>
                    <ng-container matColumnDef="actions">
                      <th mat-header-cell *matHeaderCellDef class="col-actions">Actions</th>
                      <td mat-cell *matCellDef="let s" class="col-actions">
                        <button mat-icon-button matTooltip="Revoke this session"
                          class="btn-tertiary"
                          [disabled]="revokeSessionMutation.isPending()"
                          (click)="revokeSession(s)">
                          <mat-icon>logout</mat-icon>
                        </button>
                        <button mat-icon-button
                          [matTooltip]="'Revoke all sessions for ' + (s.user_email ?? 'this user')"
                          class="btn-error"
                          [disabled]="revokeUserSessionsMutation.isPending()"
                          (click)="revokeUserSessions(s)">
                          <mat-icon>devices</mat-icon>
                        </button>
                      </td>
                    </ng-container>
                    <tr mat-header-row *matHeaderRowDef="sessionColumns"></tr>
                    <tr mat-row *matRowDef="let row; columns: sessionColumns;" class="hover-row"></tr>
                  </table>
                </div>

                @if (!sessionsQuery.isLoading() && filteredSessions().length === 0) {
                  <div class="empty-state">
                    No active sessions.
                  </div>
                }
            </app-expandable-card>
          </div>
        </mat-tab>

      </mat-tab-group>

    }
  `,
  styles: [`
    :host { display: block; }

    /* ── Layout helpers ─────────────────────────────────────────────── */
    .access-denied-wrap { padding: 24px; }
    .tab-body { padding-top: 16px; }
    .table-scroll { overflow-x: auto; }
    .full-width { width: 100%; }
    .empty-state { padding: 24px; text-align: center; color: var(--mat-sys-on-surface-variant); font-size: 0.85rem; }

    /* ── Tab labels ─────────────────────────────────────────────────── */
    .tab-icon { font-size: 18px; margin-right: 6px; }

    /* ── Card headers ───────────────────────────────────────────────── */
    .card-header-row { display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; }
    .card-title-group { display: flex; align-items: center; gap: 8px; }
    .card-title-group--mb { margin-bottom: 16px; }
    .card-title { margin: 0; font-size: 1.1rem; }
    .icon-primary { color: var(--mat-sys-primary); }

    /* ── Chips ──────────────────────────────────────────────────────── */
    .count-chip {
      display: inline-block; padding: 1px 8px; border-radius: 10px;
      background: rgba(255,255,255,0.08); color: var(--mat-sys-on-surface-variant);
      font-size: 0.65rem; height: 18px; line-height: 16px;
    }
    .chip-pill {
      display: inline-block; padding: 1px 8px; border-radius: 9px;
      font-size: 0.65rem; height: 18px; line-height: 16px; font-weight: 500;
    }

    /* ── Table col helpers ──────────────────────────────────────────── */
    .col-actions { text-align: center; }
    .col-user-agent { max-width: 220px; }

    /* ── Text helpers ───────────────────────────────────────────────── */
    .text-sm       { font-size: 0.85rem; }
    .text-xs       { font-size: 0.78rem; }
    .text-muted    { color: var(--mat-sys-on-surface-variant); }
    .text-muted-sm { font-size: 0.85rem; color: var(--mat-sys-on-surface-variant); }
    .text-muted-sm2 { font-size: 0.8rem; color: var(--mat-sys-on-surface-variant); }
    .text-muted-xs { font-size: 0.78rem; color: var(--mat-sys-on-surface-variant); }
    .text-mono-sm  { font-family: monospace; font-size: 0.8rem; }
    .text-mono-xs  { font-family: monospace; font-size: 0.78rem; }
    .text-nowrap   { white-space: nowrap; }

    /* ── Icon sizes ─────────────────────────────────────────────────── */
    .icon-16 { font-size: 16px; height: 16px; width: 16px; line-height: 16px; }
    .icon-15 { font-size: 15px; height: 15px; width: 15px; line-height: 15px; }

    /* ── Button colour overrides ────────────────────────────────────── */
    .btn-error    { color: var(--mat-sys-error); }
    .btn-tertiary { color: var(--mat-sys-tertiary); }

    /* ── Group name ─────────────────────────────────────────────────── */
    .group-name { font-weight: 500; font-size: 0.9rem; }

    /* ── MFA tab ────────────────────────────────────────────────────── */
    .mfa-progress-wrap { margin-bottom: 16px; }
    .mfa-progress-header { display: flex; justify-content: space-between; margin-bottom: 4px; }
    .mfa-progress-bar { height: 6px; border-radius: 3px; }
    .mfa-status-cell { display: flex; align-items: center; gap: 6px; }
    .filter-row { display: flex; gap: 8px; margin-bottom: 16px; }

    /* ── Sessions tab ───────────────────────────────────────────────── */
    .auto-refresh-label { font-size: 0.75rem; color: var(--mat-sys-on-surface-variant); margin-left: auto; }
    .sessions-filter-wrap { margin-bottom: 16px; }
    .sessions-filter-field { width: 260px; }
    .session-username { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); display: block; }
    .user-agent-cell { font-size: 0.75rem; color: var(--mat-sys-on-surface-variant); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; display: block; max-width: 200px; }

    /* ── Rows ───────────────────────────────────────────────────────── */
    .hover-row:hover { background: rgba(255,255,255,0.03); }
    .loading-rows { padding: 8px 0; }
    .skeleton-row {
      height: 36px; border-radius: 4px; margin-bottom: 4px;
      background: rgba(255,255,255,0.05);
      animation: pulse 1.5s ease-in-out infinite;
    }
    @keyframes pulse {
      0%, 100% { opacity: 1; }
      50%       { opacity: 0.4; }
    }

    /* ── Alert ──────────────────────────────────────────────────────── */
    .alert-error {
      padding: 10px 14px; border-radius: 6px; font-size: 0.85rem;
      background: rgba(192,0,0,0.12); color: #FFC7CE;
      border: 1px solid rgba(192,0,0,0.25);
    }

    .compact-field { font-size: 0.85rem; }
    ::ng-deep .compact-field .mat-mdc-form-field-subscript-wrapper { display: none; }
  `],
})
export class AdminComponent {
  private adminApi    = inject(AdminApiService)
  private authService = inject(AuthService)
  private readonly theme = inject(ThemeService)
  private qc          = injectQueryClient()
  private dialog      = inject(MatDialog)

  canAccess = () => {
    const role = this.authService.user()?.role
    return role === 'super_admin' || role === 'admin'
  }

  activeTab          = 0
  userColumns        = ['email', 'username', 'full_name', 'role', 'status', 'mfa', 'last_login', 'created_at', 'actions']
  groupColumns       = ['name', 'description', 'members', 'created_at', 'actions']
  mfaColumns         = ['email', 'full_name', 'role', 'mfa_status', 'last_login', 'actions']
  sessionColumns     = ['user', 'ip_address', 'user_agent', 'created_at', 'expires_at', 'actions']
  sessionEmailFilter = ''

  mfaFilter  = signal<'all' | 'enrolled' | 'not_enrolled'>('all')
  mfaFilters = [
    { key: 'all'          as const, label: 'All'          },
    { key: 'enrolled'     as const, label: 'Enrolled'     },
    { key: 'not_enrolled' as const, label: 'Not Enrolled' },
  ]

  managingGroup   = signal<GroupEntry | null>(null)

  // ── Queries ──────────────────────────────────────────────────────────────

  usersQuery = injectQuery(() => ({
    queryKey: ['admin', 'users'],
    queryFn:  () => firstValueFrom(this.adminApi.listUsers()),
  }))

  groupsQuery = injectQuery(() => ({
    queryKey: ['admin', 'groups'],
    queryFn:  () => firstValueFrom(this.adminApi.listGroups()),
  }))

  sessionsQuery = injectQuery(() => ({
    queryKey: ['admin', 'sessions'],
    queryFn:  () => firstValueFrom(this.adminApi.listSessions()),
    refetchInterval: 60_000,
  }))

  // ── Mutations ────────────────────────────────────────────────────────────

  deleteMutation = injectMutation(() => ({
    mutationFn: (id: string) => firstValueFrom(this.adminApi.deleteUser(id)),
    onSuccess:  () => this.qc.invalidateQueries({ queryKey: ['admin', 'users'] }),
  }))

  resetMfaMutation = injectMutation(() => ({
    mutationFn: (id: string) => firstValueFrom(this.adminApi.resetUserMfa(id)),
    onSuccess:  () => this.qc.invalidateQueries({ queryKey: ['admin', 'users'] }),
  }))

  createGroupMutation = injectMutation(() => ({
    mutationFn: (payload: { name: string; description?: string }) =>
      firstValueFrom(this.adminApi.createGroup(payload)),
    onSuccess: () => this.qc.invalidateQueries({ queryKey: ['admin', 'groups'] }),
  }))

  deleteGroupMutation = injectMutation(() => ({
    mutationFn: (id: string) => firstValueFrom(this.adminApi.deleteGroup(id)),
    onSuccess:  () => this.qc.invalidateQueries({ queryKey: ['admin', 'groups'] }),
  }))

  revokeSessionMutation = injectMutation(() => ({
    mutationFn: (id: string) => firstValueFrom(this.adminApi.revokeSession(id)),
    onSuccess:  () => this.qc.invalidateQueries({ queryKey: ['admin', 'sessions'] }),
  }))

  revokeUserSessionsMutation = injectMutation(() => ({
    mutationFn: (userId: string) => firstValueFrom(this.adminApi.revokeUserSessions(userId)),
    onSuccess:  () => this.qc.invalidateQueries({ queryKey: ['admin', 'sessions'] }),
  }))

  // ── Computed ─────────────────────────────────────────────────────────────

  mfaEnrolled = () => (this.usersQuery.data() ?? []).filter(u => u.mfa_enabled).length
  mfaPct      = () => {
    const total = this.usersQuery.data()?.length ?? 0
    return total > 0 ? Math.round((this.mfaEnrolled() / total) * 100) : 0
  }

  filteredMfaUsers = () => {
    const users = this.usersQuery.data() ?? []
    const f     = this.mfaFilter()
    if (f === 'enrolled')     return users.filter(u => u.mfa_enabled)
    if (f === 'not_enrolled') return users.filter(u => !u.mfa_enabled)
    return users
  }

  filteredSessions = () => {
    const sessions = this.sessionsQuery.data() ?? []
    const email    = this.sessionEmailFilter.toLowerCase()
    return email
      ? sessions.filter(s => (s.user_email ?? '').toLowerCase().includes(email))
      : sessions
  }

  // ── Actions ──────────────────────────────────────────────────────────────

  openCreateUser(): void {
    this.dialog.open(CreateUserDialogComponent, { width: '420px' })
  }

  openEditUser(u: UserRead): void {
    const ref  = this.dialog.open(EditUserDialogComponent, { width: '460px' })
    const inst = ref.componentInstance as EditUserDialogComponent
    inst.init(u, this.authService.isSuperAdmin())
  }

  deleteUser(u: UserRead): void {
    const ref = this.dialog.open(AdminConfirmDialogComponent, {
      data: { title: 'Delete User', message: `Delete user ${u.email}? This cannot be undone.`, confirmLabel: 'Delete' },
    })
    ref.afterClosed().subscribe((ok: boolean) => { if (ok) this.deleteMutation.mutate(u.id) })
  }

  resetMfa(u: UserRead): void {
    const ref = this.dialog.open(AdminConfirmDialogComponent, {
      data: { title: 'Reset MFA', message: `Reset MFA for ${u.email}? They will need to re-enroll.`, confirmLabel: 'Reset' },
    })
    ref.afterClosed().subscribe((ok: boolean) => { if (ok) this.resetMfaMutation.mutate(u.id) })
  }

  openManageMembers(g: GroupEntry): void {
    this.managingGroup.set(g)
    const ref  = this.dialog.open(ManageMembersDialogComponent, { width: '540px' })
    const inst = ref.componentInstance as ManageMembersDialogComponent
    inst.group    = g
    inst.allUsers = this.usersQuery.data() ?? []
    ref.afterClosed().subscribe(() => this.managingGroup.set(null))
  }

  deleteGroup(g: GroupEntry): void {
    const ref = this.dialog.open(AdminConfirmDialogComponent, {
      data: { title: 'Delete Group', message: `Delete group "${g.name}"? This cannot be undone.`, confirmLabel: 'Delete' },
    })
    ref.afterClosed().subscribe((ok: boolean) => { if (ok) this.deleteGroupMutation.mutate(g.id) })
  }

  openCreateGroup(): void {
    const ref = this.dialog.open(CreateGroupDialogComponent, { width: '420px' })
    ref.afterClosed().subscribe((result: { name: string; description?: string } | undefined) => {
      if (result) this.createGroupMutation.mutate(result)
    })
  }

  revokeSession(s: SessionEntry): void {
    const ref = this.dialog.open(AdminConfirmDialogComponent, {
      data: { title: 'Revoke Session', message: 'Revoke this session? The user will be signed out.', confirmLabel: 'Revoke' },
    })
    ref.afterClosed().subscribe((ok: boolean) => { if (ok) this.revokeSessionMutation.mutate(s.id) })
  }

  revokeUserSessions(s: SessionEntry): void {
    const ref = this.dialog.open(AdminConfirmDialogComponent, {
      data: { title: 'Revoke All Sessions', message: `Revoke ALL sessions for ${s.user_email ?? 'this user'}?`, confirmLabel: 'Revoke All' },
    })
    ref.afterClosed().subscribe((ok: boolean) => { if (ok) this.revokeUserSessionsMutation.mutate(s.user_id) })
  }

  // ── Template helpers ─────────────────────────────────────────────────────
  roleColor = (r: string) => { const m = this.theme.isDark() ? ROLE_DARK : ROLE_LIGHT; return m[r] ?? m['viewer'] }

  activeStyle = (is_active: boolean) => this.theme.isDark()
    ? { bg: is_active ? 'rgba(112,173,71,0.15)'  : 'rgba(192,0,0,0.12)',  fg: is_active ? '#C6EFCE' : '#FFC7CE' }
    : { bg: is_active ? 'rgba(29,158,117,0.12)'  : 'rgba(163,45,45,0.11)', fg: is_active ? '#0F6E56' : '#8A1F1F' }

  mfaIconColor = (mfa_enabled: boolean) =>
    mfa_enabled ? (this.theme.isDark() ? '#C6EFCE' : '#0F6E56') : 'var(--mat-sys-on-surface-variant)'

  mfaPctStyle = () => {
    const pct = this.mfaPct()
    return this.theme.isDark()
      ? { bg: pct === 100 ? 'rgba(112,173,71,0.15)'  : pct >= 50 ? 'rgba(255,192,0,0.15)'   : 'rgba(192,0,0,0.18)',   fg: pct === 100 ? '#C6EFCE' : pct >= 50 ? '#FFEB9C' : '#FFC7CE' }
      : { bg: pct === 100 ? 'rgba(29,158,117,0.12)'  : pct >= 50 ? 'rgba(186,117,23,0.13)'  : 'rgba(163,45,45,0.11)', fg: pct === 100 ? '#0F6E56' : pct >= 50 ? '#7A4500' : '#8A1F1F' }
  }

  fmtDate      = fmtDate
  fmtDateShort = fmtDateShort
  fmtShort     = fmtShort
  fmtFull      = fmtFull
}
