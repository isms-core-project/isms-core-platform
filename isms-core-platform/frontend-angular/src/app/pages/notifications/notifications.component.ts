import { Component, inject, signal, computed } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'

import { injectQuery, injectMutation, injectQueryClient } from '@tanstack/angular-query-experimental'

import { MatCardModule } from '@angular/material/card'
import { MatButtonModule } from '@angular/material/button'
import { MatIconModule } from '@angular/material/icon'
import { MatChipsModule } from '@angular/material/chips'
import { MatSlideToggleModule } from '@angular/material/slide-toggle'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatTableModule } from '@angular/material/table'
import { MatSelectModule } from '@angular/material/select'
import { MatCheckboxModule } from '@angular/material/checkbox'
import { MatTabsModule } from '@angular/material/tabs'
import { MatSnackBar, MatSnackBarModule } from '@angular/material/snack-bar'

import { AdminApiService } from '../../api/admin-api.service'
import { AuthService } from '../../core/services/auth.service'
import { ThemeService } from '../../core/services/theme.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'
import { NotificationPref } from '../../shared/types'

// ── Constants ─────────────────────────────────────────────────────────────────

const CAT_LABEL: Record<string, string> = {
  workflow: 'Workflow', system: 'System', infrastructure: 'Infrastructure',
}
const CAT_COLOR_DARK: Record<string, string>  = { workflow: '#1a3a27', system: '#1a2a3a', infrastructure: '#2a1a3a' }
const CAT_TEXT_DARK: Record<string, string>   = { workflow: '#C6EFCE', system: '#9fc8f0', infrastructure: '#d4b8f0' }
const CAT_COLOR_LIGHT: Record<string, string> = { workflow: 'rgba(27,94,32,.1)', system: 'rgba(21,101,192,.1)', infrastructure: 'rgba(106,27,154,.1)' }
const CAT_TEXT_LIGHT: Record<string, string>  = { workflow: '#1b5e20', system: '#1565c0', infrastructure: '#6a1b9a' }

const ALL_ROLES = ['super_admin', 'admin', 'isms_manager', 'auditor', 'control_owner', 'viewer']
const ROLE_LABEL: Record<string, string> = {
  super_admin: 'Super Admin', admin: 'Admin', isms_manager: 'ISMS Manager',
  auditor: 'Auditor', control_owner: 'Control Owner', viewer: 'Viewer',
}

// ── Component ─────────────────────────────────────────────────────────────────

@Component({
  selector: 'app-notifications',
  standalone: true,
  imports: [
    FormsModule,
    MatCardModule, MatButtonModule, MatIconModule, MatChipsModule,
    MatSlideToggleModule, MatProgressSpinnerModule, MatTooltipModule,
    MatTableModule, MatSelectModule, MatCheckboxModule, MatTabsModule,
    MatSnackBarModule,
    PageHeaderComponent,
  ],
  template: `
<app-page-header
  title="Notifications"
  subtitle="Manage email notification preferences and routing rules">
</app-page-header>

<mat-tab-group [selectedIndex]="tabIndex()" (selectedIndexChange)="tabIndex.set($event)" animationDuration="0ms" class="notif-tab-group">

  <!-- ── Tab 0: My Preferences ── -->
  <mat-tab label="My Preferences">
    <div class="notif-tab-body notif-prefs-root">
      <p class="notif-intro">Choose which email notifications you receive. Changes take effect immediately.</p>

      @if (prefsMutation.isError()) {
        <div class="notif-alert notif-alert--error">Failed to save — try again.</div>
      }
      @if (testResult(); as tr) {
        <div class="notif-alert" [class.notif-alert--success]="tr.ok" [class.notif-alert--error]="!tr.ok">
          {{ tr.msg }}
          <span class="notif-alert-dismiss" (click)="testResult.set(null)">✕</span>
        </div>
      }

      @if (myPrefsQuery.isLoading()) {
        <div class="loading-center"><mat-spinner diameter="24"></mat-spinner></div>
      }

      @for (cat of byCategory(); track cat.key) {
        <div class="notif-cat-group">
          <div class="notif-cat-heading">
            <span class="notif-cat-badge"
              [style.--cat-bg]="catColor(cat.key)"
              [style.--cat-text]="catText(cat.key)">
              {{ catLabel(cat.key) }}
            </span>
          </div>
          @for (pref of cat.prefs; track pref.event_type) {
            <div class="notif-pref-row">
              <div class="notif-pref-body">
                <mat-slide-toggle
                  [checked]="pref.enabled"
                  [disabled]="prefsMutation.isPending()"
                  (change)="togglePref(pref.event_type, pref.enabled)">
                  <div>
                    <div class="notif-pref-label">{{ pref.label }}</div>
                    <div class="notif-pref-desc">{{ pref.description }}</div>
                  </div>
                </mat-slide-toggle>
              </div>
              <button mat-icon-button class="notif-test-btn"
                [disabled]="testingEvent() !== null"
                (click)="sendTest(pref.event_type)"
                matTooltip="Send test email to yourself">
                @if (testingEvent() === pref.event_type) {
                  <mat-spinner diameter="14"></mat-spinner>
                } @else {
                  <mat-icon class="notif-send-icon">send</mat-icon>
                }
              </button>
            </div>
          }
        </div>
      }
    </div>
  </mat-tab>

  <!-- ── Tab 1: Routing Rules (admin only) ── -->
  @if (isAdmin()) {
    <mat-tab label="Routing Rules">
      <div class="notif-tab-body">
        <p class="notif-intro">Control which roles receive each notification type. Changes take effect on the next event.</p>

        @if (routingMutation.isError()) {
          <div class="notif-alert notif-alert--error">Failed to save — try again.</div>
        }
        @if (routingQuery.isLoading()) {
          <div class="loading-center"><mat-spinner diameter="24"></mat-spinner></div>
        }

        <mat-card>
          <div class="table-scroll">
            <table class="notif-table">
              <thead>
                <tr>
                  <th class="notif-th">Event</th>
                  <th class="notif-th notif-th--cat">Category</th>
                  <th class="notif-th notif-th--roles">Target Roles</th>
                  <th class="notif-th notif-th--center notif-th--always">Always Include</th>
                </tr>
              </thead>
              <tbody>
                @for (row of routingQuery.data() ?? []; track row.event_type) {
                  <tr class="notif-tr">
                    <td class="notif-td">
                      <div class="notif-event-label">{{ row.label }}</div>
                      <div class="notif-event-desc">{{ row.description }}</div>
                    </td>
                    <td class="notif-td">
                      <span class="notif-cat-mini">{{ catLabel(row.category) }}</span>
                    </td>
                    <td class="notif-td">
                      <div class="notif-role-chips">
                        @for (role of allRoles; track role) {
                          <div class="notif-role-chip"
                            [class.active]="row.target_roles.includes(role)"
                            (click)="toggleRoutingRole(row.event_type, role, row.target_roles)">
                            {{ roleLabel(role) }}
                          </div>
                        }
                      </div>
                    </td>
                    <td class="notif-td notif-td--center">
                      <mat-slide-toggle size="small"
                        [checked]="row.always_include_override"
                        (change)="toggleAlwaysInclude(row.event_type, row.always_include_override)">
                      </mat-slide-toggle>
                    </td>
                  </tr>
                }
              </tbody>
            </table>
          </div>
        </mat-card>
      </div>
    </mat-tab>

    <!-- ── Tab 2: User Overview (admin only) ── -->
    <mat-tab label="User Overview">
      <div class="notif-tab-body">
        <p class="notif-intro">Override any user's notification preferences. Click a cell to toggle.</p>

        @if (userPrefsQuery.isLoading()) {
          <div class="loading-center"><mat-spinner diameter="24"></mat-spinner></div>
        }
        @if (!userPrefsQuery.isLoading() && (userPrefsQuery.data()?.length ?? 0) === 0) {
          <div class="notif-empty">No active users.</div>
        }
        @if ((userPrefsQuery.data()?.length ?? 0) > 0) {
          @let rows = userPrefsQuery.data()!;
          @let eventTypes = objectKeys(rows[0].prefs);
          <mat-card>
            <div class="table-scroll">
              <table class="notif-table">
                <thead>
                  <tr>
                    <th class="notif-th notif-th--user">User</th>
                    <th class="notif-th notif-th--cat">Role</th>
                    @for (et of eventTypes; track et) {
                      <th class="notif-th notif-th--center">{{ labelForEvent(et) }}</th>
                    }
                  </tr>
                </thead>
                <tbody>
                  @for (row of rows; track row.user_id) {
                    <tr class="notif-tr">
                      <td class="notif-td">
                        <div class="notif-user-email">{{ row.email }}</div>
                        @if (row.full_name) {
                          <div class="notif-user-meta">{{ row.full_name }}</div>
                        }
                      </td>
                      <td class="notif-td notif-user-meta">{{ roleLabel(row.role) }}</td>
                      @for (et of eventTypes; track et) {
                        <td class="notif-td notif-td--center notif-td--click"
                          (click)="toggleUserPref(row.user_id, et, row.prefs[et])"
                          [matTooltip]="row.prefs[et] ? 'Enabled — click to disable' : 'Disabled — click to enable'">
                          <mat-icon [class.notif-icon-on]="row.prefs[et]" [class.notif-icon-off]="!row.prefs[et]">
                            {{ row.prefs[et] ? 'check_circle' : 'remove_circle_outline' }}
                          </mat-icon>
                        </td>
                      }
                    </tr>
                  }
                </tbody>
              </table>
            </div>
          </mat-card>
        }
      </div>
    </mat-tab>
  }

</mat-tab-group>
`,
  styles: [`
    :host { display: block; }

    /* ── mat-tab-group overrides ── */
    .notif-tab-group {
      margin-bottom: 0;
    }
    .notif-tab-body {
      padding-top: 24px;
    }

    /* ── Prefs tab ── */
    .notif-prefs-root { max-width: 520px; }
    .notif-intro { font-size: 0.85rem; opacity: 0.6; margin-bottom: 16px; }

    .notif-cat-group { margin-bottom: 24px; }
    .notif-cat-heading { margin-bottom: 12px; }
    .notif-cat-badge {
      font-size: 0.68rem; font-weight: 600; padding: 2px 8px;
      height: 20px; border-radius: 10px;
      display: inline-flex; align-items: center;
      background: var(--cat-bg, rgba(0,0,0,0.08));
      color: var(--cat-text, inherit);
    }

    .notif-pref-row { display: flex; align-items: flex-start; margin-bottom: 12px; }
    .notif-pref-body { flex: 1; }
    .notif-pref-label { font-size: 0.85rem; }
    .notif-pref-desc  { font-size: 0.72rem; opacity: 0.5; margin-top: 1px; }
    .notif-test-btn   { margin-top: 2px; opacity: 0.4; flex-shrink: 0; }
    .notif-send-icon  { font-size: 14px; }

    /* ── Tables ── */
    .table-scroll { overflow-x: auto; }
    .notif-table {
      width: 100%; border-collapse: collapse; font-size: 0.8rem;
    }
    .notif-th {
      padding: 10px 12px; text-align: left;
      font-size: 0.72rem; font-weight: 600; opacity: 0.6;
      border-bottom: 1px solid var(--mat-sys-outline-variant);
    }
    .notif-th--center { text-align: center; white-space: nowrap; min-width: 80px; }
    .notif-th--cat    { width: 100px; }
    .notif-th--roles  { min-width: 260px; }
    .notif-th--always { width: 140px; }
    .notif-th--user   { min-width: 160px; }
    .notif-tr { border-bottom: 1px solid var(--mat-sys-outline-variant); }
    .notif-tr:last-child { border-bottom: none; }
    .notif-td { padding: 8px 12px; vertical-align: middle; }
    .notif-td--center { text-align: center; }
    .notif-td--click  { cursor: pointer; }

    .notif-event-label { font-weight: 500; font-size: 0.82rem; }
    .notif-event-desc  { font-size: 0.72rem; opacity: 0.5; }
    .notif-cat-mini {
      font-size: 0.65rem; padding: 2px 6px; border-radius: 8px;
      background: var(--mat-sys-surface-container-high);
    }

    /* ── Role chips ── */
    .notif-role-chips { display: flex; flex-wrap: wrap; gap: 4px; }
    .notif-role-chip {
      cursor: pointer; padding: 2px 8px; border-radius: 8px; font-size: 0.68rem;
      background: var(--mat-sys-surface-container);
      border: 1px solid transparent;
    }
    .notif-role-chip.active {
      background: rgba(68,114,196,0.3);
      color: #9DC3E6;
      border-color: rgba(68,114,196,0.3);
    }

    /* ── User overview ── */
    .notif-user-email { font-size: 0.82rem; }
    .notif-user-meta  { font-size: 0.72rem; opacity: 0.5; }

    /* ── Status icons ── */
    .notif-icon-on  { font-size: 16px; color: #4caf50; }
    .notif-icon-off { font-size: 16px; opacity: 0.3; }

    /* ── Alerts ── */
    .notif-alert {
      padding: 10px 14px; border-radius: 6px;
      margin-bottom: 12px; font-size: 0.82rem;
      display: flex; align-items: center; gap: 8px;
      background: var(--mat-sys-surface-container);
    }
    .notif-alert--success { background: rgba(46,125,50,0.12); color: #C6EFCE; }
    .notif-alert--error   { background: rgba(244,67,54,0.1);  color: #f44336; }
    .notif-alert-dismiss  { margin-left: auto; cursor: pointer; opacity: 0.6; }

    /* ── Misc ── */
    .loading-center { display: flex; justify-content: center; padding: 40px; }
    .notif-empty    { opacity: 0.4; font-size: 0.85rem; }
  `],
})
export class NotificationsComponent {
  private admin       = inject(AdminApiService)
  private queryClient = injectQueryClient()
  private snack       = inject(MatSnackBar)
  readonly auth       = inject(AuthService)
  private theme       = inject(ThemeService)

  // ── State ──────────────────────────────────────────────────────────────────
  tabIndex     = signal(0)
  testingEvent = signal<string | null>(null)
  testResult   = signal<{ ok: boolean; msg: string } | null>(null)

  isAdmin = computed(() => {
    const u = this.auth.user()
    return this.auth.isSuperAdmin() || u?.role === 'admin'
  })

  readonly allRoles = ALL_ROLES

  // ── Queries ────────────────────────────────────────────────────────────────
  myPrefsQuery = injectQuery(() => ({
    queryKey: ['my', 'notification-prefs'],
    queryFn: () => firstValueFrom(this.admin.getMyNotificationPrefs()),
  }))

  routingQuery = injectQuery(() => ({
    queryKey: ['admin', 'notification-routing'],
    queryFn: () => firstValueFrom(this.admin.getNotificationRouting()),
    enabled: this.isAdmin() && this.tabIndex() === 1,
  }))

  userPrefsQuery = injectQuery(() => ({
    queryKey: ['admin', 'notification-users'],
    queryFn: () => firstValueFrom(this.admin.getAllUserNotificationPrefs()),
    enabled: this.isAdmin() && this.tabIndex() === 2,
  }))

  // ── Mutations ──────────────────────────────────────────────────────────────
  prefsMutation = injectMutation(() => ({
    mutationFn: (prefs: Record<string, boolean>) => firstValueFrom(this.admin.updateMyNotificationPrefs(prefs)),
    onSuccess: () => this.queryClient.invalidateQueries({ queryKey: ['my', 'notification-prefs'] }),
  }))

  routingMutation = injectMutation(() => ({
    mutationFn: ({ event_type, body }: { event_type: string; body: Record<string, unknown> }) =>
      firstValueFrom(this.admin.updateNotificationRouting(event_type, body)),
    onSuccess: () => this.queryClient.invalidateQueries({ queryKey: ['admin', 'notification-routing'] }),
  }))

  userPrefsMutation = injectMutation(() => ({
    mutationFn: ({ user_id, prefs }: { user_id: string; prefs: Record<string, boolean> }) =>
      firstValueFrom(this.admin.updateUserNotificationPrefs(user_id, prefs)),
    onSuccess: () => this.queryClient.invalidateQueries({ queryKey: ['admin', 'notification-users'] }),
  }))

  // ── Computed ───────────────────────────────────────────────────────────────
  isDark = computed(() => this.theme.isDark())

  byCategory = computed((): { key: string; prefs: NotificationPref[] }[] => {
    const data = this.myPrefsQuery.data()
    if (!data) return []
    const map: Record<string, NotificationPref[]> = {}
    for (const p of data.prefs) {
      if (!map[p.category]) map[p.category] = []
      map[p.category].push(p)
    }
    return Object.entries(map).map(([key, prefs]) => ({ key, prefs }))
  })

  // ── Helpers ────────────────────────────────────────────────────────────────
  catLabel(cat: string): string { return CAT_LABEL[cat] ?? cat }
  roleLabel(role: string): string { return ROLE_LABEL[role] ?? role }

  catColor(cat: string): string {
    return this.isDark() ? (CAT_COLOR_DARK[cat] ?? '#222') : (CAT_COLOR_LIGHT[cat] ?? 'rgba(0,0,0,.07)')
  }
  catText(cat: string): string {
    return this.isDark() ? (CAT_TEXT_DARK[cat] ?? '#fff') : (CAT_TEXT_LIGHT[cat] ?? '#333')
  }

  labelForEvent(et: string): string {
    const routing = this.routingQuery.data()
    return routing?.find(r => r.event_type === et)?.label ?? et.replace('email.', '')
  }

  objectKeys(obj: Record<string, unknown>): string[] { return Object.keys(obj) }

  // ── Actions ────────────────────────────────────────────────────────────────
  togglePref(event_type: string, current: boolean): void {
    this.prefsMutation.mutate({ [event_type]: !current })
  }

  sendTest(event_type: string): void {
    this.testingEvent.set(event_type)
    this.testResult.set(null)
    firstValueFrom(this.admin.sendTestNotification(event_type))
      .then(res => {
        this.testResult.set({ ok: true, msg: `Test sent to ${res.recipient}` })
        this.testingEvent.set(null)
      })
      .catch(() => {
        this.testResult.set({ ok: false, msg: 'Send failed — check SMTP config' })
        this.testingEvent.set(null)
      })
  }

  toggleRoutingRole(event_type: string, role: string, currentRoles: string[]): void {
    const next = currentRoles.includes(role)
      ? currentRoles.filter(r => r !== role)
      : [...currentRoles, role]
    this.routingMutation.mutate({ event_type, body: { target_roles: next } })
  }

  toggleAlwaysInclude(event_type: string, current: boolean): void {
    this.routingMutation.mutate({ event_type, body: { always_include_override: !current } })
  }

  toggleUserPref(user_id: string, event_type: string, current: boolean): void {
    this.userPrefsMutation.mutate({ user_id, prefs: { [event_type]: !current } })
  }
}
