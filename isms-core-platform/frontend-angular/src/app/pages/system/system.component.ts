import { Component, inject, signal, computed } from '@angular/core'
import { NgTemplateOutlet } from '@angular/common'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'
import { injectQuery, injectMutation, QueryClient } from '@tanstack/angular-query-experimental'
import { HttpClient } from '@angular/common/http'

import { MatTableModule } from '@angular/material/table'
import { MatButtonModule } from '@angular/material/button'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatIconModule } from '@angular/material/icon'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatChipsModule } from '@angular/material/chips'
import { MatSlideToggleModule } from '@angular/material/slide-toggle'
import { MatDividerModule } from '@angular/material/divider'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatDialogModule, MatDialog, MatDialogRef } from '@angular/material/dialog'

import { AdminApiService, OrphanEntry, OpenSearchDetail } from '../../api/admin-api.service'
import { AuthApiService } from '../../api/auth-api.service'
import { OrgApiService } from '../../api/org-api.service'
import { AuthService } from '../../core/services/auth.service'
import { TokenStoreService } from '../../core/services/token-store.service'
import { ThemeService } from '../../core/services/theme.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'
import { ExpandableCardComponent } from '../../shared/components/expandable-card.component'
import { ServiceHealth, SysInfoResponse, DbCounts, OrganisationRead } from '../../shared/types'

// ─── Constants ────────────────────────────────────────────────────────────────

const SERVICE_LABELS: Record<string, string> = {
  api: 'API',
  database: 'PostgreSQL',
  redis: 'Redis',
  celery: 'Celery Worker',
  opensearch: 'OpenSearch',
}

const DB_COUNT_LABELS: Record<string, string> = {
  control_groups: 'Control Groups',
  frameworks: 'Frameworks',
  framework_controls: 'Framework Controls',
  cross_framework_mappings: 'Cross-Framework Mappings',
  policies: 'Policies',
  requirements: 'Requirements',
  implementations: 'Implementations',
  assessments: 'Assessments',
  evidence: 'Evidence Items',
  automated_evidence: 'Automated Evidence',
  gaps: 'Gaps',
  users: 'Users',
  load_history_count: 'Load History Events',
}

const FIRST_RUN_STEPS = [
  { key: 'frameworks' as const,      label: 'Load Reference Frameworks',      desc: '18 bundles — ISO 27001, NIST CSF 2.0, MITRE ATT&CK, GDPR, DORA, NIS2 and more.' },
  { key: 'policies' as const,        label: 'Import Policies',                desc: 'POL, OP-POL, PRIV-POL, CLD-PII-POL, REF, CTX, FORM documents from the mounted content volumes.' },
  { key: 'implementations' as const, label: 'Import Implementations (IMP)',   desc: 'IMP-UG / IMP-TG documents — also indexed to OpenSearch for full-text search.' },
  { key: 'workbooks' as const,       label: 'Import Assessment Workbooks',    desc: 'Framework assessment workbook structures parsed from generator scripts.' },
  { key: 'operational' as const,     label: 'Import Operational Checklists',  desc: 'Operational compliance checklist structures.' },
]

type StepKey = 'frameworks' | 'policies' | 'implementations' | 'workbooks' | 'operational'
type ImportKey = StepKey | 'fullSync'

// ─── Helpers ──────────────────────────────────────────────────────────────────

function okColors(dark: boolean)   { return dark ? { bg: '#1a3a27', fg: '#C6EFCE' }  : { bg: 'rgba(46,125,50,0.15)',  fg: '#1b5e20' } }
function errColors(dark: boolean)  { return dark ? { bg: '#3a0000', fg: '#FFC7CE' }  : { bg: 'rgba(192,0,0,0.12)',    fg: '#9e0000' } }
function warnColors(dark: boolean) { return dark ? { bg: '#3a2e00', fg: '#FFEB9C' }  : { bg: 'rgba(230,145,0,0.15)', fg: '#9a6500' } }

function svcColors(status: string, dark: boolean) {
  if (status === 'ok') return okColors(dark)
  if (status === 'error') return errColors(dark)
  return warnColors(dark)
}

function syncColors(status: string | null, dark: boolean) {
  if (status === 'success' || status === 'ok') return okColors(dark)
  if (!status) return warnColors(dark)
  return errColors(dark)
}

function sevColors(sev: string, dark: boolean) {
  if (sev === 'error' || sev === 'critical') return errColors(dark)
  if (sev === 'warning') return warnColors(dark)
  return okColors(dark)
}

function fmtDate(iso: string | null | undefined): string {
  if (!iso) return '—'
  return new Date(iso).toLocaleString('en-GB', {
    day: '2-digit', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit',
  })
}

function fromNow(iso: string | null | undefined): string {
  if (!iso) return ''
  const ms = Date.now() - new Date(iso).getTime()
  const s = Math.round(ms / 1000)
  if (s < 60) return 'just now'
  const m = Math.round(s / 60)
  if (m < 60) return `${m}m ago`
  const h = Math.round(m / 60)
  if (h < 24) return `${h}h ago`
  return `${Math.round(h / 24)}d ago`
}

// ─── MFA Setup Dialog ─────────────────────────────────────────────────────────

@Component({
  selector: 'app-mfa-setup-dialog',
  standalone: true,
  imports: [MatDialogModule, MatButtonModule, MatInputModule, MatFormFieldModule,
            MatProgressSpinnerModule, MatIconModule, FormsModule],
  template: `
<h2 mat-dialog-title>
  @if (step() === 'qr')     { Set up two-factor authentication }
  @if (step() === 'verify') { Verify your authenticator }
  @if (step() === 'backup') { Save your backup codes }
</h2>

<mat-dialog-content class="dialog-content-wide">
  @if (error()) { <div class="alert alert--error">{{ error() }}</div> }

  @if (step() === 'qr') {
    @if (loading()) { <div class="spinner-row"><mat-spinner diameter="40" /></div> }
    @if (setupData()) {
      <p class="body2">Scan this QR code with Google Authenticator, Authy, or any TOTP app.</p>
      <div class="qr-center"><img [src]="setupData()!.qr_data_uri" alt="MFA QR" class="qr-img" /></div>
      <p class="caption">Can't scan? Enter this key manually:</p>
      <div class="secret-box">
        <span class="mono f1">{{ setupData()!.secret }}</span>
        <button mat-icon-button (click)="copySecret()"><mat-icon>content_copy</mat-icon></button>
      </div>
    }
  }

  @if (step() === 'verify') {
    <p class="body2">Enter the 6-digit code from your authenticator app to confirm setup.</p>
    <mat-form-field appearance="outline" class="full-width-field">
      <mat-label>Verification code</mat-label>
      <input matInput [(ngModel)]="code" maxlength="6" autocomplete="one-time-code"
        (ngModelChange)="code = $event.replace(/\\D/g, '').slice(0, 6)"
        class="code-input" />
    </mat-form-field>
  }

  @if (step() === 'backup') {
    <div class="alert alert--warn">Store these safely — they won't be shown again.</div>
    <div class="codes-grid">
      @for (c of backupCodes(); track c) { <span class="mono">{{ c }}</span> }
    </div>
    <button mat-stroked-button (click)="copyAll()" class="copy-all-btn">
      <mat-icon class="icon-sm">content_copy</mat-icon> Copy all codes
    </button>
  }
</mat-dialog-content>

<mat-dialog-actions align="end">
  @if (step() === 'qr') {
    <button mat-button mat-dialog-close>Cancel</button>
    <button mat-raised-button color="primary" [disabled]="!setupData()" (click)="step.set('verify'); error.set(null)">Next</button>
  }
  @if (step() === 'verify') {
    <button mat-button (click)="step.set('qr')">Back</button>
    <button mat-raised-button color="primary" [disabled]="code.length < 6 || enabling()" (click)="doEnable()">
      @if (enabling()) { <mat-spinner diameter="20" /> } @else { Verify & Enable }
    </button>
  }
  @if (step() === 'backup') {
    <button mat-raised-button color="primary" [mat-dialog-close]="true">Done</button>
  }
</mat-dialog-actions>
  `,
  styles: [`
    .body2 { font-size:0.875rem; color:var(--mat-sys-on-surface-variant); margin-bottom:12px }
    .caption { font-size:0.75rem; color:var(--mat-sys-on-surface-variant); margin-bottom:6px }
    .spinner-row { display:flex; justify-content:center; padding:32px 0 }
    .qr-center { display:flex; justify-content:center; margin-bottom:16px }
    .secret-box { display:flex; align-items:center; gap:8px; padding:8px; background:var(--mat-sys-surface-container); border-radius:6px }
    .mono { font-family:monospace; font-size:0.85rem; word-break:break-all; letter-spacing:0.05em }
    .f1 { flex:1 }
    .codes-grid { display:grid; grid-template-columns:1fr 1fr; gap:6px; padding:12px; background:var(--mat-sys-surface-container); border-radius:6px; margin-top:8px }
    .alert { padding:8px 12px; border-radius:6px; font-size:0.85rem; margin-bottom:12px }
    .alert--error { background:rgba(192,0,0,0.12); color:#9e0000 }
    .alert--warn  { background:rgba(230,145,0,0.15); color:#7a4800 }
    .dialog-content-wide { min-width:360px }
    .qr-img { max-width:200px; border-radius:8px }
    .full-width-field { width:100% }
    .code-input { letter-spacing:0.3em; text-align:center; font-size:1.4rem }
    .copy-all-btn { margin-top:8px; font-size:0.75rem }
  `],
})
export class MfaSetupDialogComponent {
  private authApi    = inject(AuthApiService)
  private tokenStore = inject(TokenStoreService)
  private dialogRef  = inject(MatDialogRef<MfaSetupDialogComponent>)

  step       = signal<'qr' | 'verify' | 'backup'>('qr')
  code       = ''
  setupData  = signal<{ secret: string; otpauth_uri: string; qr_data_uri: string } | null>(null)
  backupCodes = signal<string[]>([])
  error      = signal<string | null>(null)
  loading    = signal(false)
  enabling   = signal(false)

  constructor() {
    // Start setup on open
    this.loading.set(true)
    const token = this.tokenStore.get() ?? ''
    this.authApi.mfaSetup(token)
      .then(d => this.setupData.set(d))
      .catch(() => this.error.set('Failed to start MFA setup. Please try again.'))
      .finally(() => this.loading.set(false))
  }

  doEnable() {
    this.error.set(null)
    this.enabling.set(true)
    const token = this.tokenStore.get() ?? ''
    this.authApi.mfaEnable(token, this.code)
      .then(d => { this.backupCodes.set(d.backup_codes); this.step.set('backup') })
      .catch((e: Error) => this.error.set(e.message ?? 'Invalid code — try again.'))
      .finally(() => this.enabling.set(false))
  }

  copySecret() { navigator.clipboard.writeText(this.setupData()?.secret ?? '') }
  copyAll()    { navigator.clipboard.writeText(this.backupCodes().join('\n')) }
}

// ─── MFA Disable Dialog ───────────────────────────────────────────────────────

@Component({
  selector: 'app-mfa-disable-dialog',
  standalone: true,
  imports: [MatDialogModule, MatButtonModule, MatInputModule, MatFormFieldModule,
            MatProgressSpinnerModule, FormsModule],
  template: `
<h2 mat-dialog-title>Disable two-factor authentication</h2>
<mat-dialog-content class="dialog-content-mid">
  @if (error()) { <div class="alert alert--error">{{ error() }}</div> }
  <p class="body2">Enter your current TOTP code to disable MFA.</p>
  <mat-form-field appearance="outline" class="full-width-field">
    <mat-label>Authentication code</mat-label>
    <input matInput [(ngModel)]="code" maxlength="6" autocomplete="one-time-code"
      (ngModelChange)="code = $event.replace(/\\D/g, '').slice(0, 6)"
      class="code-input" />
  </mat-form-field>
</mat-dialog-content>
<mat-dialog-actions align="end">
  <button mat-button mat-dialog-close>Cancel</button>
  <button mat-raised-button color="warn" [disabled]="code.length < 6 || pending()" (click)="doDisable()">
    @if (pending()) { <mat-spinner diameter="20" /> } @else { Disable MFA }
  </button>
</mat-dialog-actions>
  `,
  styles: [`
    .body2 { font-size:0.875rem; color:var(--mat-sys-on-surface-variant); margin-bottom:12px }
    .alert { padding:8px 12px; border-radius:6px; font-size:0.85rem; margin-bottom:12px }
    .alert--error { background:rgba(192,0,0,0.12); color:#9e0000 }
    .dialog-content-mid { min-width:320px }
    .full-width-field { width:100% }
    .code-input { letter-spacing:0.3em; text-align:center; font-size:1.4rem }
  `],
})
export class MfaDisableDialogComponent {
  private authApi    = inject(AuthApiService)
  private tokenStore = inject(TokenStoreService)
  private dialogRef  = inject(MatDialogRef<MfaDisableDialogComponent>)

  code    = ''
  error   = signal<string | null>(null)
  pending = signal(false)

  doDisable() {
    this.error.set(null)
    this.pending.set(true)
    const token = this.tokenStore.get() ?? ''
    this.authApi.mfaDisable(token, this.code)
      .then(() => this.dialogRef.close(true))
      .catch((e: Error) => this.error.set(e.message ?? 'Failed to disable MFA.'))
      .finally(() => this.pending.set(false))
  }
}

// ─── MFA Backup Codes Dialog ──────────────────────────────────────────────────

@Component({
  selector: 'app-mfa-backup-dialog',
  standalone: true,
  imports: [MatDialogModule, MatButtonModule, MatInputModule, MatFormFieldModule,
            MatProgressSpinnerModule, MatIconModule, FormsModule],
  template: `
<h2 mat-dialog-title>Regenerate backup codes</h2>
<mat-dialog-content class="dialog-content-wide">
  @if (error()) { <div class="alert alert--error">{{ error() }}</div> }
  @if (!newCodes()) {
    <p class="body2">Enter your TOTP code to regenerate backup codes. Current codes will be invalidated.</p>
    <mat-form-field appearance="outline" class="full-width-field">
      <mat-label>Authentication code</mat-label>
      <input matInput [(ngModel)]="code" maxlength="6" autocomplete="one-time-code"
        (ngModelChange)="code = $event.replace(/\\D/g, '').slice(0, 6)"
        class="code-input" />
    </mat-form-field>
  } @else {
    <div class="alert alert--warn">Store these safely — they won't be shown again.</div>
    <div class="codes-grid">
      @for (c of newCodes()!; track c) { <span class="mono">{{ c }}</span> }
    </div>
    <button mat-stroked-button (click)="copyAll()" class="copy-all-btn">
      <mat-icon class="icon-sm">content_copy</mat-icon> Copy all codes
    </button>
  }
</mat-dialog-content>
<mat-dialog-actions align="end">
  @if (!newCodes()) {
    <button mat-button mat-dialog-close>Cancel</button>
    <button mat-raised-button color="primary" [disabled]="code.length < 6 || pending()" (click)="doRegen()">
      @if (pending()) { <mat-spinner diameter="20" /> } @else { Regenerate }
    </button>
  } @else {
    <button mat-raised-button color="primary" mat-dialog-close>Done</button>
  }
</mat-dialog-actions>
  `,
  styles: [`
    .body2 { font-size:0.875rem; color:var(--mat-sys-on-surface-variant); margin-bottom:12px }
    .codes-grid { display:grid; grid-template-columns:1fr 1fr; gap:6px; padding:12px; background:var(--mat-sys-surface-container); border-radius:6px; margin-top:8px }
    .mono { font-family:monospace; font-size:0.85rem }
    .alert { padding:8px 12px; border-radius:6px; font-size:0.85rem; margin-bottom:12px }
    .alert--error { background:rgba(192,0,0,0.12); color:#9e0000 }
    .alert--warn  { background:rgba(230,145,0,0.15); color:#7a4800 }
    .dialog-content-wide { min-width:360px }
    .full-width-field { width:100% }
    .code-input { letter-spacing:0.3em; text-align:center; font-size:1.4rem }
    .copy-all-btn { margin-top:8px; font-size:0.75rem }
  `],
})
export class MfaBackupDialogComponent {
  private authApi    = inject(AuthApiService)
  private tokenStore = inject(TokenStoreService)

  code     = ''
  error    = signal<string | null>(null)
  pending  = signal(false)
  newCodes = signal<string[] | null>(null)

  doRegen() {
    this.error.set(null)
    this.pending.set(true)
    const token = this.tokenStore.get() ?? ''
    this.authApi.mfaRegenerateBackupCodes(token, this.code)
      .then(d => this.newCodes.set(d.backup_codes))
      .catch((e: Error) => this.error.set(e.message ?? 'Regeneration failed.'))
      .finally(() => this.pending.set(false))
  }

  copyAll() { navigator.clipboard.writeText(this.newCodes()!.join('\n')) }
}

// ─── SystemComponent ──────────────────────────────────────────────────────────

@Component({
  selector: 'app-system',
  standalone: true,
  imports: [
    NgTemplateOutlet, FormsModule,
    MatTableModule, MatButtonModule, MatFormFieldModule,
    MatInputModule, MatSelectModule, MatDialogModule,
    MatIconModule, MatProgressSpinnerModule, MatChipsModule,
    MatSlideToggleModule, MatDividerModule, MatTooltipModule,
    PageHeaderComponent,
    ExpandableCardComponent,
  ],
  template: `
<div class="sys-page">

  <!-- Non-admin: only MFA card -->
  @if (!isAdmin()) {
    <app-page-header title="System" subtitle="Account security settings" />
    <div class="non-admin-wrap">
      <ng-container [ngTemplateOutlet]="mfaCard" />
    </div>
  }

  <!-- Admin view -->
  @if (isAdmin()) {
    <app-page-header title="System Status" subtitle="Service health, database counts, and platform configuration">
      <div actions class="hdr-actions">
        @if (sysQuery.data()) {
          <span class="caption-text">Updated {{ fromNow(sysQuery.data()!.generated_at) }}</span>
        }
        <button mat-icon-button matTooltip="Refresh" (click)="refresh()" [disabled]="sysQuery.isFetching()">
          @if (sysQuery.isFetching()) { <mat-spinner diameter="16" /> } @else { <mat-icon>refresh</mat-icon> }
        </button>
      </div>
    </app-page-header>

    @if (sysQuery.isError()) {
      <div class="alert alert--error mb16">Failed to load system info.</div>
    }
    @if (reindexMsg()) {
      <div class="alert alert--success mb16">
        {{ reindexMsg() }}
        <button mat-icon-button class="close-btn" (click)="reindexMsg.set(null)"><mat-icon>close</mat-icon></button>
      </div>
    }

    @if (sysQuery.isPending()) {
      <div class="spinner-row"><mat-spinner /></div>
    }

    @if (sysQuery.data(); as d) {
      <div class="cards-col">

        <!-- Service Health -->
        <div class="svc-grid">
          @for (svc of d.services; track svc.name) {
            <div class="svc-card" [style.background]="svcBg(svc)" [style.border-color]="svcBorder(svc)">
              <div class="svc-top">
                <mat-icon [style.color]="svcColor(svc).fg">
                  {{ svc.status === 'ok' ? 'check_circle' : svc.status === 'error' ? 'error' : 'help_outline' }}
                </mat-icon>
                <span class="chip" [style.background]="svcColor(svc).bg" [style.color]="svcColor(svc).fg">
                  {{ svc.status }}
                </span>
              </div>
              <div class="svc-name">{{ svcLabel(svc.name) }}</div>
              @if (svc.latency_ms != null) { <div class="dim">{{ svc.latency_ms }} ms</div> }
              @if (svc.detail) { <div class="dim faded">{{ svc.detail }}</div> }
            </div>
          }
        </div>

        <!-- Two-column layout -->
        <div class="two-col">

          <!-- LEFT -->
          <div class="cards-col">

            <!-- DB Records -->
            <app-expandable-card [expandable]="true" [initiallyExpanded]="true">
              <span card-title>
                <mat-icon>storage</mat-icon>
                Database Records
              </span>
                <table class="dt">
                  <tbody>
                    @for (row of dbRows(d.db_counts); track row.key) {
                      <tr>
                        <td class="dim">{{ row.label }}</td>
                        <td class="right mono bold">{{ row.val.toLocaleString() }}</td>
                      </tr>
                    }
                  </tbody>
                </table>
            </app-expandable-card>

            <!-- Last Data Load -->
            <app-expandable-card [expandable]="true" [initiallyExpanded]="true">
              <span card-title>
                <mat-icon>history</mat-icon>
                Last Data Load
              </span>
                @if (d.last_sync_at) {
                  <div class="kv"><span class="dim">Type</span><span class="mono">{{ d.last_sync_type ?? '—' }}</span></div>
                  <div class="kv">
                    <span class="dim">Status</span>
                    <span class="chip sm"
                      [style.background]="syncColor(d.last_sync_status).bg"
                      [style.color]="syncColor(d.last_sync_status).fg">
                      {{ d.last_sync_status ?? '—' }}
                    </span>
                  </div>
                  <div class="kv"><span class="dim">At</span><span>{{ fmtDate(d.last_sync_at) }}</span></div>
                } @else {
                  <span class="dim">No data loads recorded.</span>
                }
            </app-expandable-card>

            <!-- OpenSearch indices (sysinfo) -->
            <app-expandable-card [expandable]="true" [initiallyExpanded]="true">
              <span card-title>
                <mat-icon>sync_alt</mat-icon>
                OpenSearch
                @if (d.opensearch_cluster_status) {
                  <span class="chip" [style.background]="osClusterColor(d.opensearch_cluster_status).bg"
                    [style.color]="osClusterColor(d.opensearch_cluster_status).fg">
                    {{ d.opensearch_cluster_status }}
                  </span>
                }
              </span>
              <button card-actions mat-stroked-button class="xs-btn"
                matTooltip="Re-parse all IMP/POL files and push to OpenSearch"
                [disabled]="reindexMut.isPending()" (click)="doReindex()">
                @if (reindexMut.isPending()) { <mat-spinner diameter="12" /> Reindexing… }
                @else { <mat-icon class="xs-icon">cloud_sync</mat-icon> Reindex }
              </button>
                @if (d.opensearch_indices) {
                  <table class="dt">
                    <thead><tr><th>Index</th><th class="right">Documents</th></tr></thead>
                    <tbody>
                      @for (idx of osIdxRows(d.opensearch_indices); track idx.name) {
                        <tr>
                          <td class="mono xs">{{ idx.name }}</td>
                          <td class="right mono bold">{{ (idx.count ?? 0).toLocaleString() }}</td>
                        </tr>
                      }
                    </tbody>
                  </table>
                } @else {
                  <span class="dim">Unavailable</span>
                }
            </app-expandable-card>

          </div>

          <!-- RIGHT -->
          <div class="cards-col">

            <!-- Platform Configuration -->
            <app-expandable-card [expandable]="true" [initiallyExpanded]="true">
              <span card-title>
                <mat-icon>settings</mat-icon>
                Platform Configuration
              </span>
                @for (row of cfgRows(d); track row.label) {
                  <div class="kv">
                    <span class="dim fs0">{{ row.label }}</span>
                    <span class="mono xs break-all right" [style.color]="row.hi ? 'var(--mat-sys-primary)' : 'var(--mat-sys-on-surface)'">
                      {{ row.value }}
                    </span>
                  </div>
                }
                <mat-divider class="my8" />
                <div class="kv">
                  <span class="dim fs0">Log Level</span>
                  <span class="mono xs">{{ d.log_level }}</span>
                </div>
            </app-expandable-card>

            <!-- Email (SMTP) -->
            <app-expandable-card [expandable]="true" [initiallyExpanded]="true">
              <span card-title>
                <mat-icon>email</mat-icon>
                Email (SMTP)
                <span class="chip sm"
                  [style.background]="d.smtp_enabled ? okC.bg : errC.bg"
                  [style.color]="d.smtp_enabled ? okC.fg : errC.fg">
                  {{ d.smtp_enabled ? 'enabled' : 'disabled' }}
                </span>
              </span>
                <div class="kv"><span class="dim">Host</span><span class="mono xs">{{ d.smtp_host || '— not configured —' }}</span></div>
                <div class="kv"><span class="dim">Port</span><span class="mono xs">{{ d.smtp_port }}</span></div>
                <div class="kv"><span class="dim">From</span><span class="mono xs">{{ d.smtp_from }}</span></div>
                <div class="kv"><span class="dim">Platform URL</span><span class="mono xs break-all">{{ d.platform_url }}</span></div>
                @if (d.smtp_enabled) {
                  <mat-divider class="my12" />
                  @if (emailResult()) {
                    <div class="alert mb12 fs072" [class.alert--success]="emailResult()!.ok" [class.alert--error]="!emailResult()!.ok">
                      {{ emailResult()!.msg }}
                      <button mat-icon-button class="close-btn" (click)="emailResult.set(null)"><mat-icon>close</mat-icon></button>
                    </div>
                  }
                  <div class="row gap8">
                    <mat-form-field appearance="outline" class="f1" subscriptSizing="dynamic">
                      <input matInput placeholder="recipient@example.com" [(ngModel)]="testEmailAddr" (keydown.enter)="doTestEmail()" />
                    </mat-form-field>
                    <button mat-stroked-button class="xs-btn nowrap"
                      matTooltip="Send a test email to verify SMTP is working"
                      [disabled]="emailMut.isPending() || !testEmailAddr.trim()" (click)="doTestEmail()">
                      @if (emailMut.isPending()) { <mat-spinner diameter="12" /> } @else { Send Test }
                    </button>
                  </div>
                }
            </app-expandable-card>

            <!-- AI Compass -->
            <app-expandable-card [expandable]="true" [initiallyExpanded]="true">
              <span card-title>
                <mat-icon>psychology</mat-icon>
                AI Compass
              </span>
                <div class="kv mb12"><span class="dim">Active Model</span><span class="mono xs">{{ d.ai_model || '—' }}</span></div>
                <mat-divider class="mb12" />
                @if (aiModelResult()) {
                  <div class="alert mb12 fs072" [class.alert--success]="aiModelResult()!.ok" [class.alert--error]="!aiModelResult()!.ok">
                    {{ aiModelResult()!.msg }}
                    <button mat-icon-button class="close-btn" (click)="aiModelResult.set(null)"><mat-icon>close</mat-icon></button>
                  </div>
                }
                @if (aiModelsQuery.isPending()) {
                  <div class="skeleton"></div>
                } @else {
                  <mat-form-field appearance="outline" class="full-width" subscriptSizing="dynamic">
                    <mat-label>Select Model</mat-label>
                    <mat-select [(ngModel)]="selectedModel" (ngModelChange)="onAiModelChange($event)"
                      [disabled]="aiModelMut.isPending()">
                      @for (m of aiModels(); track m.id) {
                        <mat-option [value]="m.id">{{ m.display_name }}</mat-option>
                      }
                    </mat-select>
                  </mat-form-field>
                }
                <p class="dim fs072 mt6">Applies to ISMS Compass gap analysis. Requires ANTHROPIC_API_KEY in platform/.env.</p>
            </app-expandable-card>

          </div>
        </div>

        <!-- OpenSearch ILM & Snapshots -->
        @if (osDetailQuery.data(); as osd) {
          <app-expandable-card [expandable]="true" [initiallyExpanded]="true">
            <span card-title>
              <mat-icon>cloud_sync</mat-icon>
              OpenSearch — ILM &amp; Snapshots
            </span>
              <div class="two-col">

                <div>
                  @if (osd.ism_policies.length > 0) {
                    <div class="section-lbl">ISM Retention Policies</div>
                    <table class="dt">
                      <thead><tr><th>Policy</th><th>States</th><th>Default State</th></tr></thead>
                      <tbody>
                        @for (p of osd.ism_policies; track p.id) {
                          <tr>
                            <td class="mono xs">{{ p.id }}</td>
                            <td class="dim xs">{{ p.states.join(' → ') }}</td>
                            <td><span class="mini-chip">{{ p.default_state }}</span></td>
                          </tr>
                        }
                      </tbody>
                    </table>
                  } @else {
                    <span class="dim">No ISM retention policies configured.</span>
                  }

                  @if (osd.snapshot_repos.length > 0) {
                    <mat-divider class="my12" />
                    <div class="section-lbl">Snapshot Repositories</div>
                    @for (r of osd.snapshot_repos; track r.name) {
                      <div class="kv">
                        <span class="mono xs">{{ r.name }}</span>
                        <span class="dim xs">{{ r.type }} · {{ r.bucket ?? '—' }}</span>
                      </div>
                    }
                  }

                  @if (osd.sm_policies.length > 0) {
                    <mat-divider class="my12" />
                    <div class="section-lbl">Snapshot Policies</div>
                    @for (p of osd.sm_policies; track p.id) {
                      <div class="kv">
                        <div>
                          <span class="mono xs">{{ p.id }}</span>
                          <span class="dim xs ml6">({{ p.creation_schedule ?? '—' }})</span>
                        </div>
                        <span class="chip xxs"
                          [style.background]="p.enabled ? okC.bg : errC.bg"
                          [style.color]="p.enabled ? okC.fg : errC.fg">
                          {{ p.enabled ? 'enabled' : 'disabled' }}
                        </span>
                      </div>
                    }
                  }
                </div>

                <div>
                  <div class="section-lbl">Evidence Indices (per org)</div>
                  @if (populatedIdx(osd).length > 0) {
                    <table class="dt">
                      <thead><tr><th>Index</th><th class="right">Docs</th><th class="right">Size</th></tr></thead>
                      <tbody>
                        @for (idx of populatedIdx(osd); track idx.index) {
                          <tr>
                            <td class="mono xs">{{ idx.index }}</td>
                            <td class="right xs">{{ idx.doc_count.toLocaleString() }}</td>
                            <td class="right dim xs">{{ idx.store_size ?? '—' }}</td>
                          </tr>
                        }
                      </tbody>
                    </table>
                    @if (hiddenIdxCount(osd) > 0) {
                      <p class="dim xs mt6">{{ hiddenIdxCount(osd) }} empty {{ hiddenIdxCount(osd) === 1 ? 'index' : 'indices' }} hidden</p>
                    }
                  } @else {
                    <span class="dim">No evidence data ingested yet.</span>
                  }
                </div>

              </div>
          </app-expandable-card>
        }

        <!-- Data Sync + Orphan Scanner -->
        <div class="two-col">

          <app-expandable-card [expandable]="true" [initiallyExpanded]="true">
            <span card-title>
              <mat-icon>sync</mat-icon>
              Data Synchronisation
            </span>
              <p class="dim xs mb12">Re-sync content after updating policies, IMPs, or workbooks.</p>
              @if (syncResult()) {
                <div class="alert mb12" [class.alert--success]="syncResult()!.ok" [class.alert--error]="!syncResult()!.ok">
                  {{ syncResult()!.msg }}
                  <button mat-icon-button class="close-btn" (click)="syncResult.set(null)"><mat-icon>close</mat-icon></button>
                </div>
              }
              <div class="row gap8 wrap">
                <button mat-raised-button color="primary"
                  [disabled]="syncNowMut.isPending() || syncBgMut.isPending() || resetMut.isPending()"
                  (click)="doSyncNow()">
                  @if (syncNowMut.isPending()) { <mat-spinner diameter="14" /> Syncing… } @else { Sync Now }
                </button>
                <button mat-stroked-button
                  [disabled]="syncNowMut.isPending() || syncBgMut.isPending() || resetMut.isPending()"
                  (click)="doSyncBg()">
                  @if (syncBgMut.isPending()) { <mat-spinner diameter="14" /> Queuing… } @else { Sync in Background }
                </button>
                <mat-divider vertical class="vsep" />
                <button mat-stroked-button color="warn"
                  matTooltip="Wipe all POLs, IMPs and assessments then re-import from source files"
                  [disabled]="syncNowMut.isPending() || syncBgMut.isPending() || resetMut.isPending()"
                  (click)="doReset()">
                  @if (resetMut.isPending()) { <mat-spinner diameter="14" /> Resetting… } @else { Reset & Re-import }
                </button>
              </div>
          </app-expandable-card>

          <app-expandable-card [expandable]="true" [initiallyExpanded]="true">
            <span card-title>
              <mat-icon>delete_sweep</mat-icon>
              Orphan Scanner
            </span>
            <button card-actions mat-stroked-button class="xs-btn"
              [disabled]="scanMut.isPending() || purgeMut.isPending()" (click)="doScan()">
              @if (scanMut.isPending()) { <mat-spinner diameter="12" /> Scanning… } @else { Scan }
            </button>
              @if (purgeResult()) { <div class="alert alert--success mb8">{{ purgeResult() }}</div> }
              @if (scanMut.isError()) { <div class="alert alert--error mb8">Scan failed.</div> }
              @if (!orphanResult() && !purgeResult()) { <span class="dim">Finds DB records whose source file no longer exists on disk.</span> }
              @if (orphanResult(); as orp) {
                @if (orp.implementations.length === 0 && orp.policies.length === 0) {
                  <div class="alert alert--success">No orphans found — DB is clean.</div>
                } @else {
                  <div class="alert alert--warn mb12">{{ orp.implementations.length + orp.policies.length }} orphaned record(s) found.</div>
                  @if (orp.implementations.length > 0) {
                    <div class="dim xs mb4">Implementations ({{ orp.implementations.length }})</div>
                    @for (o of orp.implementations; track o.document_id) {
                      <div class="mono orphan-id">{{ o.document_id }}</div>
                    }
                  }
                  @if (orp.policies.length > 0) {
                    <div class="dim xs mt8 mb4">Policies ({{ orp.policies.length }})</div>
                    @for (o of orp.policies; track o.document_id) {
                      <div class="mono orphan-id">{{ o.document_id }}</div>
                    }
                  }
                  <button mat-raised-button color="warn" class="full-width mt12 xs-btn"
                    [disabled]="purgeMut.isPending()" (click)="doPurge()">
                    @if (purgeMut.isPending()) { <mat-spinner diameter="12" /> Purging… }
                    @else { Purge {{ orp.implementations.length + orp.policies.length }} orphans }
                  </button>
                }
              }
          </app-expandable-card>

        </div>

        <!-- First-Run Setup -->
        <app-expandable-card [expandable]="true" [initiallyExpanded]="true">
          <span card-title>
            <mat-icon>downloading</mat-icon>
            First-Run Setup
          </span>
            <p class="dim xs mb12">Run steps 1–5 in order on first boot. Use Full Sync to re-run all importers at once.</p>
            @if (importResults()['fullSync']) {
              <div class="alert mb12" [class.alert--success]="importResults()['fullSync']!.ok" [class.alert--error]="!importResults()['fullSync']!.ok">
                {{ importResults()['fullSync']!.msg }}
                <button mat-icon-button class="close-btn" (click)="clearImport('fullSync')"><mat-icon>close</mat-icon></button>
              </div>
            }
            @for (step of firstRunSteps; track step.key) {
              <div class="frun-row">
                <div class="f1">
                  <div class="step-lbl">{{ step.label }}</div>
                  <div class="dim xs mb4">{{ step.desc }}</div>
                  @if (importResults()[step.key]) {
                    <div class="alert fs072" [class.alert--success]="importResults()[step.key]!.ok" [class.alert--error]="!importResults()[step.key]!.ok">
                      {{ importResults()[step.key]!.msg }}
                      <button mat-icon-button class="close-btn" (click)="clearImport(step.key)"><mat-icon>close</mat-icon></button>
                    </div>
                  }
                </div>
                <button mat-stroked-button class="xs-btn flex-shrink0"
                  [disabled]="isStepPending(step.key) || fullSyncMut.isPending()" (click)="runStep(step.key)">
                  @if (isStepPending(step.key)) { <mat-spinner diameter="10" /> Running… } @else { Run }
                </button>
              </div>
            }
            <mat-divider class="mb12" />
            <button mat-raised-button color="primary" class="full-width"
              [disabled]="fullSyncMut.isPending() || anyStepPending()" (click)="doFullSync()">
              @if (fullSyncMut.isPending()) { <mat-spinner diameter="14" /> Running Full Sync… }
              @else { <mat-icon>sync_alt</mat-icon> Full Sync (Steps 2–5) }
            </button>
            <p class="dim xs mt6 center">Runs all four importers in sequence. Load Reference Frameworks (Step 1) must be done separately first.</p>
        </app-expandable-card>

        <!-- MFA Policy -->
        <app-expandable-card [expandable]="true" [initiallyExpanded]="true">
          <span card-title>
            <mat-icon>security</mat-icon>
            MFA Policy
            <span class="chip sm"
              [style.background]="mfaRequired() ? okC.bg : 'var(--mat-sys-surface-container)'"
              [style.color]="mfaRequired() ? okC.fg : 'var(--mat-sys-on-surface-variant)'">
              {{ mfaRequired() ? 'Enforced' : 'Optional' }}
            </span>
          </span>
            <div class="row gap12">
              <mat-slide-toggle [checked]="mfaRequired()" [disabled]="toggleMfaMut.isPending()" (change)="doToggleMfa($event.checked)" />
              <div>
                <div class="sm875">Require MFA for all users</div>
                <div class="dim xs">When enabled, users without MFA set up will be blocked from accessing the platform until they enrol.</div>
              </div>
            </div>
            @if (toggleMfaMut.isError()) { <div class="alert alert--error mt12">Failed to update MFA policy.</div> }
        </app-expandable-card>

        <!-- MFA Card (Account Security) -->
        <ng-container [ngTemplateOutlet]="mfaCard" />

        <!-- System Event Log -->
        <app-expandable-card [expandable]="true" [initiallyExpanded]="true">
          <span card-title>
            <mat-icon>assignment</mat-icon>
            System Event Log
            <span class="dim xs">Last 30 system events</span>
          </span>
            @if (!logsQuery.data() || logsQuery.data()!.items.length === 0) {
              <span class="dim">No system events recorded yet. Events appear here when background jobs run.</span>
            } @else {
              <table class="dt">
                <thead>
                  <tr>
                    <th class="xs dim">Time</th>
                    <th class="xs dim">Event</th>
                    <th class="xs dim">Severity</th>
                    <th class="xs dim">Description</th>
                  </tr>
                </thead>
                <tbody>
                  @for (e of logsQuery.data()!.items; track e.id) {
                    <tr>
                      <td class="dim xs nowrap">{{ fmtDate(e.created_at) }}</td>
                      <td class="mono xs">{{ e.event_type }}</td>
                      <td>
                        <span class="chip xxs" [style.background]="sevC(e.severity).bg" [style.color]="sevC(e.severity).fg">
                          {{ e.severity }}
                        </span>
                      </td>
                      <td class="dim xs">{{ e.description ?? '—' }}</td>
                    </tr>
                  }
                </tbody>
              </table>
            }
        </app-expandable-card>

      </div>
    }
  }

</div>

<!-- MFA Card template -->
<ng-template #mfaCard>
  <app-expandable-card [expandable]="true" [initiallyExpanded]="true">
    <span card-title>
      <mat-icon>security</mat-icon>
      Two-factor authentication
      @if (mfaEnabled()) {
        <span class="chip sm" [style.background]="okC.bg" [style.color]="okC.fg">Active</span>
      }
    </span>
      @if (mfaStatusQuery.isPending()) {
        <div class="spinner-row"><mat-spinner diameter="20" /></div>
      } @else if (mfaEnabled()) {
        <div class="row gap8 mb12">
          <mat-icon class="mfa-icon-active">lock</mat-icon>
          <span class="dim sm875">Your account is protected with an authenticator app.</span>
        </div>
        <div class="row gap8">
          <button mat-stroked-button color="warn" class="xs-btn" (click)="openDisableMfa()">Disable</button>
          <button mat-stroked-button class="xs-btn" (click)="openBackupMfa()">Regenerate backup codes</button>
        </div>
      } @else {
        <div class="row gap8 mb12">
          <mat-icon class="mfa-icon-inactive">lock_open</mat-icon>
          <span class="dim sm875">Add an extra layer of security to your account.</span>
        </div>
        <button mat-raised-button color="primary" class="xs-btn" (click)="openSetupMfa()">Enable MFA</button>
      }
  </app-expandable-card>
</ng-template>
  `,
  styles: [`
    .sys-page {
    }
    .cards-col { display: flex; flex-direction: column; gap: 16px; }
    .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-items: start; }
    @media (max-width: 768px) { .two-col { grid-template-columns: 1fr; } }

    /* Service health */
    .svc-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin-top: 16px; }
    @media (max-width: 1100px) { .svc-grid { grid-template-columns: repeat(3, 1fr); } }
    @media (max-width: 600px)  { .svc-grid { grid-template-columns: repeat(2, 1fr); } }
    .svc-card { border: 1px solid; border-radius: 8px; padding: 12px; }
    .svc-top { display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 8px; }
    .svc-name { font-size: 0.8rem; font-weight: 600; margin-bottom: 2px; }
    .dim { color: var(--mat-sys-on-surface-variant); }
    .faded { opacity: 0.7; }

    /* Card internals */
    mat-card { border-radius: 8px !important; }
    mat-card-content { padding: 16px !important; }
    .card-hdr { display: flex; align-items: center; gap: 8px; margin-bottom: 12px; flex-wrap: wrap; }
    .card-title { font-size: 1rem; font-weight: 500; }
    .f1 { flex: 1; }
    .flex-shrink0 { flex-shrink: 0; }

    /* Chips */
    .chip { display: inline-flex; align-items: center; padding: 0 6px; height: 18px; border-radius: 9px; font-size: 0.65rem; font-weight: 600; text-transform: capitalize; white-space: nowrap; }
    .chip.sm  { height: 18px; font-size: 0.65rem; }
    .chip.xxs { height: 16px; font-size: 0.6rem; }
    .mini-chip { display: inline-flex; align-items: center; padding: 0 6px; height: 16px; border-radius: 8px; font-size: 0.6rem; font-weight: 600; background: var(--mat-sys-surface-container-high); color: var(--mat-sys-on-surface-variant); }

    /* Tables */
    .dt { width: 100%; border-collapse: collapse; font-size: 0.8rem; }
    .dt thead th { text-align: left; font-size: 0.7rem; color: var(--mat-sys-on-surface-variant); font-weight: 600; padding: 4px 8px 4px 0; border-bottom: 1px solid var(--mat-sys-outline-variant); }
    .dt tbody tr:hover { background: var(--mat-sys-surface-container-high); }
    .dt tbody td { padding: 6px 8px 6px 0; border-bottom: 1px solid var(--mat-sys-outline-variant); }
    .dt tbody tr:last-child td { border-bottom: none; }
    .right { text-align: right; }
    .bold  { font-weight: 600; }
    .mono  { font-family: monospace; }
    .xs    { font-size: 0.75rem; }
    .xxs   { font-size: 0.65rem; }
    .nowrap { white-space: nowrap; }
    .break-all { word-break: break-all; }

    /* KV rows */
    .kv { display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; gap: 8px; }
    .fs0 { font-size: 0.8rem; }

    .section-lbl { font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--mat-sys-on-surface-variant); margin-bottom: 8px; }

    /* Alerts */
    .alert { padding: 8px 12px; border-radius: 6px; font-size: 0.85rem; position: relative; }
    .alert--success { background: rgba(46,125,50,0.12); color: #1b5e20; }
    .alert--error   { background: rgba(192,0,0,0.12);   color: #9e0000; }
    .alert--warn    { background: rgba(230,145,0,0.15);  color: #7a4800; }
    .close-btn { position: absolute; right: 4px; top: 4px; width: 20px; height: 20px; line-height: 20px; }
    .close-btn mat-icon { font-size: 14px; }

    /* Layout helpers */
    .row { display: flex; align-items: center; }
    .gap8  { gap: 8px; }
    .gap12 { gap: 12px; }
    .wrap  { flex-wrap: wrap; }
    .mb4   { margin-bottom: 4px; }
    .mb8   { margin-bottom: 8px; }
    .mb12  { margin-bottom: 12px; }
    .mb16  { margin-bottom: 16px; }
    .mt6   { margin-top: 6px; }
    .mt8   { margin-top: 8px; }
    .mt12  { margin-top: 12px; }
    .my8   { margin: 8px 0; }
    .my12  { margin: 12px 0; }
    .ml6   { margin-left: 6px; }
    .center { text-align: center; }
    .fs072 { font-size: 0.72rem; }
    .sm875 { font-size: 0.875rem; }

    /* Buttons */
    .xs-btn { font-size: 0.7rem; }
    .xs-icon { font-size: 16px; width: 16px; height: 16px; margin-right: 4px; vertical-align: middle; line-height: 1; }
    .full-width { width: 100%; }
    .nowrap { white-space: nowrap; }

    /* Vertical divider in button row */
    .vsep { height: 24px; align-self: center; }

    /* First-run */
    .frun-row { display: flex; align-items: flex-start; gap: 12px; margin-bottom: 12px; }
    .step-lbl { font-size: 0.875rem; font-weight: 600; margin-bottom: 2px; }

    .orphan-id { font-size: 0.72rem; color: #c00; margin-bottom: 2px; }

    .spinner-row { display: flex; justify-content: center; padding: 48px 0; }
    .hdr-actions { display: flex; align-items: center; gap: 8px; }
    .caption-text { font-size: 0.75rem; color: var(--mat-sys-on-surface-variant); }
    .skeleton { height: 40px; background: var(--mat-sys-surface-container); border-radius: 6px; }
    .non-admin-wrap { max-width: 600px; display: flex; flex-direction: column; gap: 16px; }
    .mfa-icon-active   { color: var(--mat-sys-primary); font-size: 20px; width: 20px; height: 20px; }
    .mfa-icon-inactive { color: var(--mat-sys-on-surface-variant); font-size: 20px; width: 20px; height: 20px; }
  `],
})
export class SystemComponent {
  private adminApi   = inject(AdminApiService)
  private orgApi     = inject(OrgApiService)
  private authApi    = inject(AuthApiService)
  private tokenStore = inject(TokenStoreService)
  readonly auth      = inject(AuthService)
  private theme      = inject(ThemeService)
  private http       = inject(HttpClient)
  private qc         = inject(QueryClient)
  private dialog     = inject(MatDialog)

  readonly firstRunSteps = FIRST_RUN_STEPS

  readonly isAdmin = computed(() => {
    const r = this.auth.user()?.role
    return r === 'super_admin' || r === 'admin'
  })

  // ── Local UI state ───────────────────────────────────────────────────────────
  reindexMsg    = signal<string | null>(null)
  syncResult    = signal<{ ok: boolean; msg: string } | null>(null)
  emailResult   = signal<{ ok: boolean; msg: string } | null>(null)
  aiModelResult = signal<{ ok: boolean; msg: string } | null>(null)
  orphanResult  = signal<{ implementations: OrphanEntry[]; policies: OrphanEntry[] } | null>(null)
  purgeResult   = signal<string | null>(null)
  importResults = signal<Record<ImportKey, { ok: boolean; msg: string } | null>>({
    frameworks: null, policies: null, implementations: null,
    workbooks: null, operational: null, fullSync: null,
  })
  testEmailAddr = ''
  selectedModel = ''

  // ── Queries ──────────────────────────────────────────────────────────────────

  readonly sysQuery = injectQuery(() => ({
    queryKey: ['admin', 'sysinfo'],
    queryFn: () => firstValueFrom(this.adminApi.getSysInfo()),
    refetchInterval: 30_000, staleTime: 25_000, enabled: this.isAdmin(),
  }))

  readonly logsQuery = injectQuery(() => ({
    queryKey: ['admin', 'system-logs'],
    queryFn: () => firstValueFrom(this.adminApi.getAuditLog({ category: 'system', page_size: 30 })),
    refetchInterval: 60_000, staleTime: 55_000, enabled: this.isAdmin(),
  }))

  readonly osDetailQuery = injectQuery(() => ({
    queryKey: ['admin', 'opensearch-detail'],
    queryFn: () => firstValueFrom(this.adminApi.getOpenSearchDetail()),
    refetchInterval: 60_000, staleTime: 55_000, enabled: this.isAdmin(),
  }))

  readonly orgQuery = injectQuery(() => ({
    queryKey: ['organisation'],
    queryFn: () => firstValueFrom(this.orgApi.get()),
    staleTime: 60_000,
  }))

  readonly mfaStatusQuery = injectQuery(() => ({
    queryKey: ['mfa-status'],
    queryFn: () => this.authApi.getMfaStatus(this.tokenStore.get() ?? ''),
    staleTime: 60_000,
  }))

  readonly aiModelsQuery = injectQuery(() => ({
    queryKey: ['ai-models'],
    queryFn: () => firstValueFrom(
      this.http.get<{ models: { id: string; display_name: string }[] }>('/api/v1/ai/models')
    ),
    staleTime: 5 * 60_000, enabled: this.isAdmin(),
  }))

  readonly mfaEnabled  = computed(() => this.mfaStatusQuery.data()?.mfa_enabled ?? false)
  readonly mfaRequired = computed(() => Boolean(this.orgQuery.data()?.settings?.['mfa_required']))
  readonly aiModels    = computed(() => this.aiModelsQuery.data()?.models ?? [])

  // ── Mutations ────────────────────────────────────────────────────────────────

  readonly reindexMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.adminApi.reindexOpenSearch()),
    onSuccess: (data) => {
      const s = data.stats
      this.reindexMsg.set(`Reindex complete — ${s.implementations} implementations, ${s.policies} policies indexed.${s.errors ? ` ${s.errors} errors.` : ''}`)
    },
  }))

  readonly syncNowMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.adminApi.syncFull()),
    onSuccess: () => { this.syncResult.set({ ok: true, msg: 'Sync complete — all importers ran successfully.' }); this.qc.invalidateQueries({ queryKey: ['admin', 'sysinfo'] }) },
    onError:   () => this.syncResult.set({ ok: false, msg: 'Sync failed — check server logs.' }),
  }))

  readonly syncBgMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.adminApi.syncAsync()),
    onSuccess: (d) => this.syncResult.set({ ok: true, msg: `Background sync queued. Task ID: ${d.task_id}` }),
    onError:   () => this.syncResult.set({ ok: false, msg: 'Failed to queue background sync.' }),
  }))

  readonly resetMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.adminApi.resetContent()),
    onSuccess: (data) => {
      const del = data.deleted
      const pol = (data.reimport?.['policies'] as { imported?: number })?.imported ?? '?'
      const imp = (data.reimport?.['implementations'] as { imported?: number })?.imported ?? '?'
      const wkbk = (data.reimport?.['workbooks'] as { imported?: number })?.imported ?? '?'
      this.syncResult.set({ ok: true, msg: `Reset complete. Deleted: ${del['policies'] ?? 0} POLs, ${del['implementations'] ?? 0} IMPs, ${del['assessments'] ?? 0} assessments. Re-imported: ${pol} POLs, ${imp} IMPs, ${wkbk} workbooks.` })
      this.qc.invalidateQueries({ queryKey: ['admin', 'sysinfo'] })
    },
    onError: () => this.syncResult.set({ ok: false, msg: 'Reset failed — check server logs.' }),
  }))

  readonly scanMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.adminApi.scanOrphans()),
    onSuccess: (data) => { this.orphanResult.set({ implementations: data.implementations, policies: data.policies }); this.purgeResult.set(null) },
  }))

  readonly purgeMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.adminApi.purgeOrphans()),
    onSuccess: (data) => { this.purgeResult.set(`Purged ${data.deleted.implementations} implementations + ${data.deleted.policies} policies.`); this.orphanResult.set(null) },
  }))

  readonly emailMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.adminApi.sendTestEmail(this.testEmailAddr)),
    onSuccess: (r) => this.emailResult.set({ ok: true, msg: `Test email sent to ${r.recipient}.` }),
    onError:   () => this.emailResult.set({ ok: false, msg: 'Send failed — check server logs.' }),
  }))

  readonly aiModelMut = injectMutation(() => ({
    mutationFn: (model: string) => firstValueFrom(
      this.orgApi.update({ settings: { ...(this.orgQuery.data()?.settings ?? {}), ai_model: model } })
    ),
    onSuccess: (_, model) => { this.aiModelResult.set({ ok: true, msg: `Model updated to ${model}.` }); this.qc.invalidateQueries({ queryKey: ['admin', 'sysinfo'] }) },
    onError:   () => this.aiModelResult.set({ ok: false, msg: 'Failed to update model — check server logs.' }),
  }))

  readonly toggleMfaMut = injectMutation(() => ({
    mutationFn: (v: boolean) => firstValueFrom(
      this.orgApi.update({ settings: { ...(this.orgQuery.data()?.settings ?? {}), mfa_required: v } })
    ),
    onSuccess: () => this.qc.invalidateQueries({ queryKey: ['organisation'] }),
  }))

  readonly loadFwMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.adminApi.loadFrameworkBundles()),
    onSuccess: () => this.setImport('frameworks', true, 'Framework bundles loaded successfully.'),
    onError:   () => this.setImport('frameworks', false, 'Failed — check server logs.'),
  }))
  readonly importPolMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.adminApi.importPolicies()),
    onSuccess: (d) => { const n = d.stats?.['imported'] ?? d.stats?.['policies'] ?? ''; this.setImport('policies', true, `Policies imported.${n != null ? ` (${n} records)` : ''}`) },
    onError:   () => this.setImport('policies', false, 'Failed — check server logs.'),
  }))
  readonly importImpMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.adminApi.importImplementations()),
    onSuccess: (d) => { const n = d.stats?.['imported'] ?? d.stats?.['implementations'] ?? ''; this.setImport('implementations', true, `Implementations imported.${n != null ? ` (${n} records)` : ''}`) },
    onError:   () => this.setImport('implementations', false, 'Failed — check server logs.'),
  }))
  readonly importWkMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.adminApi.importWorkbooks()),
    onSuccess: (d) => { const n = d.stats?.['imported'] ?? d.stats?.['assessments'] ?? ''; this.setImport('workbooks', true, `Workbook structures imported.${n != null ? ` (${n} records)` : ''}`) },
    onError:   () => this.setImport('workbooks', false, 'Failed — check server logs.'),
  }))
  readonly importOpMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.adminApi.importOperational()),
    onSuccess: (d) => { const n = d.stats?.['imported'] ?? d.stats?.['assessments'] ?? ''; this.setImport('operational', true, `Operational checklists imported.${n != null ? ` (${n} records)` : ''}`) },
    onError:   () => this.setImport('operational', false, 'Failed — check server logs.'),
  }))
  readonly fullSyncMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.adminApi.syncFull()),
    onSuccess: () => this.setImport('fullSync', true, 'Full sync complete — all importers ran successfully.'),
    onError:   () => this.setImport('fullSync', false, 'Full sync failed — check server logs.'),
  }))

  // ── Color helpers ────────────────────────────────────────────────────────────

  get dark() { return this.theme.isDark() }
  get okC()  { return okColors(this.dark) }
  get errC() { return errColors(this.dark) }

  svcColor(svc: ServiceHealth)    { return svcColors(svc.status, this.dark) }
  svcBg(svc: ServiceHealth) {
    const ok = svc.status === 'ok', err = svc.status === 'error'
    return this.dark
      ? (ok ? 'rgba(198,239,206,0.08)' : err ? 'rgba(255,199,206,0.08)' : 'rgba(255,235,156,0.08)')
      : (ok ? 'rgba(46,125,50,0.08)'   : err ? 'rgba(192,0,0,0.08)'    : 'rgba(230,145,0,0.08)')
  }
  svcBorder(svc: ServiceHealth) {
    return svc.status === 'ok' ? 'rgba(198,239,206,0.2)' : svc.status === 'error' ? 'rgba(255,199,206,0.2)' : 'rgba(255,235,156,0.2)'
  }
  svcLabel(name: string) { return SERVICE_LABELS[name] ?? name }

  syncColor(s: string | null) { return syncColors(s, this.dark) }
  sevC(s: string)             { return sevColors(s, this.dark) }

  osClusterColor(s: string) {
    if (s === 'green')  return okColors(this.dark)
    if (s === 'yellow') return warnColors(this.dark)
    return errColors(this.dark)
  }

  // ── Data helpers ─────────────────────────────────────────────────────────────

  fmtDate(iso: string | null | undefined) { return fmtDate(iso) }
  fromNow(iso: string)                    { return fromNow(iso) }

  dbRows(counts: DbCounts) {
    const c = counts as unknown as Record<string, number>
    return Object.entries(DB_COUNT_LABELS).map(([k, label]) => ({ key: k, label, val: c[k] ?? 0 }))
  }

  osIdxRows(indices: Record<string, number | null>) {
    return Object.entries(indices).map(([name, count]) => ({ name, count }))
  }

  cfgRows(d: SysInfoResponse) {
    return [
      { label: 'Platform',      value: d.platform,        hi: false },
      { label: 'API Version',   value: d.api_version,     hi: false },
      { label: 'Standards',     value: d.standard,        hi: true  },
      { label: 'Framework',     value: d.framework_path,  hi: false },
      { label: 'Operational',   value: d.operational_path, hi: false },
      ...(d.privacy_path ? [{ label: 'Privacy', value: d.privacy_path, hi: false }] : []),
      ...(d.cloud_path   ? [{ label: 'Cloud',   value: d.cloud_path,   hi: false }] : []),
      { label: 'Datasets',      value: d.datasets_path,   hi: false },
      { label: 'OpenSearch URL', value: d.opensearch_url, hi: false },
    ]
  }

  populatedIdx(osd: OpenSearchDetail) { return osd.evidence_indices.filter(i => i.doc_count > 0) }
  hiddenIdxCount(osd: OpenSearchDetail) { return osd.evidence_indices.length - this.populatedIdx(osd).length }

  // ── Actions ──────────────────────────────────────────────────────────────────

  refresh() {
    this.qc.invalidateQueries({ queryKey: ['admin', 'sysinfo'] })
    this.qc.invalidateQueries({ queryKey: ['admin', 'system-logs'] })
  }

  doReindex() { this.reindexMsg.set(null); this.reindexMut.mutate(undefined) }
  doSyncNow() { this.syncResult.set(null); this.syncNowMut.mutate(undefined) }
  doSyncBg()  { this.syncResult.set(null); this.syncBgMut.mutate(undefined)  }
  doReset() {
    if (!window.confirm('This will DELETE all imported policies, implementations, assessments and QA results, then re-import from source files.\n\nControl groups, framework data, users, evidence and gaps are NOT affected.\n\nProceed?')) return
    this.syncResult.set(null)
    this.resetMut.mutate(undefined)
  }
  doScan()  { this.orphanResult.set(null); this.purgeResult.set(null); this.scanMut.mutate(undefined) }
  doPurge() { this.purgeMut.mutate(undefined) }
  doTestEmail() { this.emailResult.set(null); this.emailMut.mutate(undefined) }
  doToggleMfa(v: boolean) { this.toggleMfaMut.mutate(v) }
  doFullSync() { this.clearImport('fullSync'); this.fullSyncMut.mutate(undefined) }

  onAiModelChange(model: string) {
    this.aiModelResult.set(null)
    this.aiModelMut.mutate(model)
  }

  setImport(key: ImportKey, ok: boolean, msg: string) {
    this.importResults.update(p => ({ ...p, [key]: { ok, msg } }))
  }
  clearImport(key: ImportKey) {
    this.importResults.update(p => ({ ...p, [key]: null }))
  }

  runStep(key: StepKey) {
    this.clearImport(key)
    const map: Record<StepKey, () => void> = {
      frameworks:      () => this.loadFwMut.mutate(undefined),
      policies:        () => this.importPolMut.mutate(undefined),
      implementations: () => this.importImpMut.mutate(undefined),
      workbooks:       () => this.importWkMut.mutate(undefined),
      operational:     () => this.importOpMut.mutate(undefined),
    }
    map[key]()
  }

  isStepPending(key: string): boolean {
    const map: Record<string, boolean> = {
      frameworks:      this.loadFwMut.isPending(),
      policies:        this.importPolMut.isPending(),
      implementations: this.importImpMut.isPending(),
      workbooks:       this.importWkMut.isPending(),
      operational:     this.importOpMut.isPending(),
    }
    return map[key] ?? false
  }

  anyStepPending() {
    return this.loadFwMut.isPending() || this.importPolMut.isPending() ||
      this.importImpMut.isPending() || this.importWkMut.isPending() || this.importOpMut.isPending()
  }

  // ── MFA Dialogs ──────────────────────────────────────────────────────────────

  openSetupMfa() {
    const ref = this.dialog.open(MfaSetupDialogComponent, { width: '420px', disableClose: false })
    ref.afterClosed().subscribe(enabled => {
      if (enabled) this.qc.invalidateQueries({ queryKey: ['mfa-status'] })
    })
  }

  openDisableMfa() {
    const ref = this.dialog.open(MfaDisableDialogComponent, { width: '360px' })
    ref.afterClosed().subscribe(disabled => {
      if (disabled) this.qc.invalidateQueries({ queryKey: ['mfa-status'] })
    })
  }

  openBackupMfa() {
    this.dialog.open(MfaBackupDialogComponent, { width: '420px' })
  }
}
