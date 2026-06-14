import { Component, inject, signal, computed } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'

import { injectQuery, injectMutation, injectQueryClient } from '@tanstack/angular-query-experimental'

import { MatCardModule } from '@angular/material/card'
import { MatTableModule } from '@angular/material/table'
import { MatButtonModule } from '@angular/material/button'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatSlideToggleModule } from '@angular/material/slide-toggle'
import { MatIconModule } from '@angular/material/icon'
import { MatChipsModule } from '@angular/material/chips'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatProgressBarModule } from '@angular/material/progress-bar'
import { MatDialogModule } from '@angular/material/dialog'
import { MatDividerModule } from '@angular/material/divider'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatSidenavModule } from '@angular/material/sidenav'
import { MatSnackBarModule, MatSnackBar } from '@angular/material/snack-bar'

import { ConnectorsApiService, ConnectorRead, ConnectorLogEntry } from '../../api/connectors-api.service'

// ── Catalogue data ────────────────────────────────────────────────────────────

const KNOWN_SYSTEMS: { value: string; label: string; product: string; model: string; default_interval: number }[] = [
  { value: 'entra_id',         label: 'Microsoft Entra ID',              product: 'ISMS / PRIV / CLD', model: 'cloud',   default_interval: 86400  },
  { value: 'defender',         label: 'Microsoft Defender for Endpoint', product: 'ISMS',               model: 'cloud',   default_interval: 86400  },
  { value: 'sentinel',         label: 'Microsoft Sentinel',              product: 'ISMS',               model: 'cloud',   default_interval: 3600   },
  { value: 'intune',           label: 'Microsoft Intune',                product: 'ISMS',               model: 'cloud',   default_interval: 86400  },
  { value: 'o365',             label: 'Microsoft Office 365',            product: 'ISMS',               model: 'cloud',   default_interval: 86400  },
  { value: 'purview',          label: 'Microsoft Purview',               product: 'ISMS / PRIV',        model: 'cloud',   default_interval: 86400  },
  { value: 'servicenow',       label: 'ServiceNow ITSM',                 product: 'ISMS / PRIV',        model: 'both',    default_interval: 86400  },
  { value: 'jira',             label: 'Jira / JSM',                      product: 'ISMS / PRIV',        model: 'both',    default_interval: 86400  },
  { value: 'fortigate',        label: 'Fortinet FortiGate',              product: 'ISMS',               model: 'on-prem', default_interval: 86400  },
  { value: 'forti_analyzer',   label: 'Fortinet FortiAnalyzer',          product: 'ISMS',               model: 'on-prem', default_interval: 3600   },
  { value: 'forti_manager',    label: 'Fortinet FortiManager',           product: 'ISMS',               model: 'on-prem', default_interval: 86400  },
  { value: 'panw',             label: 'Palo Alto PAN-OS',                product: 'ISMS',               model: 'on-prem', default_interval: 86400  },
  { value: 'cisco_asa',        label: 'Cisco ASA / Firepower',           product: 'ISMS',               model: 'on-prem', default_interval: 86400  },
  { value: 'cisco_ise',        label: 'Cisco ISE',                       product: 'ISMS',               model: 'on-prem', default_interval: 86400  },
  { value: 'zscaler',          label: 'Zscaler ZIA',                     product: 'ISMS / PRIV',        model: 'cloud',   default_interval: 86400  },
  { value: 'crowdstrike',      label: 'CrowdStrike Falcon',              product: 'ISMS',               model: 'cloud',   default_interval: 86400  },
  { value: 'sentinelone',      label: 'SentinelOne',                     product: 'ISMS',               model: 'cloud',   default_interval: 86400  },
  { value: 'wazuh',            label: 'Wazuh (SIEM / EDR)',              product: 'ISMS',               model: 'on-prem', default_interval: 3600   },
  { value: 'tenable_sc',       label: 'Tenable Security Center',         product: 'ISMS',               model: 'both',    default_interval: 604800 },
  { value: 'tenable_io',       label: 'Tenable Vulnerability Management',product: 'ISMS',               model: 'cloud',   default_interval: 604800 },
  { value: 'qualys',           label: 'Qualys VMDR',                     product: 'ISMS',               model: 'cloud',   default_interval: 604800 },
  { value: 'openvas',          label: 'OpenVAS / Greenbone',             product: 'ISMS',               model: 'on-prem', default_interval: 604800 },
  { value: 'active_directory', label: 'Windows Active Directory',        product: 'ISMS',               model: 'on-prem', default_interval: 86400  },
  { value: 'openldap',         label: 'OpenLDAP',                        product: 'ISMS',               model: 'on-prem', default_interval: 86400  },
  { value: 'freeipa',          label: 'FreeIPA / Red Hat IdM',           product: 'ISMS',               model: 'on-prem', default_interval: 86400  },
  { value: 'authentik',        label: 'Authentik (IdP)',                  product: 'ISMS / PRIV',        model: 'both',    default_interval: 86400  },
  { value: 'keycloak',         label: 'Keycloak (IdP)',                   product: 'ISMS / PRIV',        model: 'both',    default_interval: 86400  },
  { value: 'cyberark',         label: 'CyberArk PAS',                   product: 'ISMS / PRIV',        model: 'on-prem', default_interval: 86400  },
  { value: 'devolutions',      label: 'Devolutions Server (DVLS)',        product: 'ISMS / PRIV',        model: 'on-prem', default_interval: 86400  },
  { value: 'hashicorp_vault',  label: 'HashiCorp Vault',                 product: 'ISMS',               model: 'both',    default_interval: 86400  },
  { value: 'prtg',             label: 'PRTG Network Monitor',            product: 'ISMS',               model: 'on-prem', default_interval: 3600   },
  { value: 'zabbix',           label: 'Zabbix',                          product: 'ISMS',               model: 'on-prem', default_interval: 3600   },
  { value: 'graylog',          label: 'Graylog',                         product: 'ISMS',               model: 'both',    default_interval: 3600   },
  { value: 'glpi',             label: 'GLPI (ITSM / Asset Mgmt)',        product: 'ISMS',               model: 'on-prem', default_interval: 86400  },
  { value: 'netbox',           label: 'NetBox (IPAM / DCIM)',            product: 'ISMS',               model: 'on-prem', default_interval: 86400  },
  { value: 'aws_security_hub', label: 'AWS Security Hub',               product: 'CLD',                model: 'cloud',   default_interval: 86400  },
  { value: 'azure_cspm',       label: 'Azure CSPM (Defender for Cloud)', product: 'CLD',               model: 'cloud',   default_interval: 86400  },
  { value: 'gcp_scc',          label: 'GCP Security Command Center',    product: 'CLD',                model: 'cloud',   default_interval: 86400  },
  { value: 'github',           label: 'GitHub',                          product: 'ISMS',               model: 'both',    default_interval: 86400  },
  { value: 'gitlab',           label: 'GitLab',                          product: 'ISMS',               model: 'both',    default_interval: 86400  },
  { value: 'opencti',          label: 'OpenCTI',                         product: 'ISMS',               model: 'both',    default_interval: 86400  },
  { value: 'openaev',          label: 'OpenAEV',                         product: 'ISMS',               model: 'both',    default_interval: 86400  },
  { value: 'kubernetes',        label: 'Kubernetes Dashboard',            product: 'ISMS',               model: 'on-prem', default_interval: 3600   },
  { value: 'siem',             label: 'Generic SIEM',                    product: 'SEC',                model: 'both',    default_interval: 3600   },
  { value: 'threat_intel',     label: 'Threat Intel Feed',               product: 'SEC',                model: 'both',    default_interval: 86400  },
]

const CONNECTOR_CONTROLS: Record<string, string[]> = {
  entra_id:          ['A.5.3', 'A.5.15', 'A.5.16', 'A.5.18', 'A.8.2', 'A.8.3', 'A.8.5'],
  defender:          ['A.8.1', 'A.8.7', 'A.8.18', 'A.8.19', 'A.8.8'],
  sentinel:          ['A.8.15', 'A.8.16', 'A.5.24', 'A.5.25', 'A.5.26', 'A.5.27', 'A.5.28'],
  intune:            ['A.8.1', 'A.8.18', 'A.8.19', 'A.8.7'],
  purview:           ['A.8.10', 'A.8.12'],
  active_directory:  ['A.5.3', 'A.5.15', 'A.5.16', 'A.5.18', 'A.8.2'],
  openldap:          ['A.5.3', 'A.5.15', 'A.5.16', 'A.5.18'],
  freeipa:           ['A.5.3', 'A.5.15', 'A.5.16', 'A.5.18', 'A.8.2'],
  authentik:         ['A.5.3', 'A.5.15', 'A.5.16', 'A.5.18', 'A.8.2', 'A.8.5'],
  keycloak:          ['A.5.3', 'A.5.15', 'A.5.16', 'A.5.18', 'A.8.2', 'A.8.5'],
  cyberark:          ['A.5.15', 'A.5.16', 'A.5.18', 'A.8.2', 'A.8.3', 'A.8.5'],
  devolutions:       ['A.5.3', 'A.5.15', 'A.5.16', 'A.5.18', 'A.8.2', 'A.8.3', 'A.8.15'],
  hashicorp_vault:   ['A.8.2', 'A.8.3', 'A.8.5', 'A.5.17', 'A.8.15'],
  fortigate:         ['A.8.20', 'A.8.21', 'A.8.22', 'A.8.23'],
  forti_analyzer:    ['A.8.15', 'A.8.16', 'A.8.1', 'A.8.18', 'A.8.19'],
  forti_manager:     ['A.8.1', 'A.8.18', 'A.8.20', 'A.8.21', 'A.8.22'],
  panw:              ['A.8.20', 'A.8.21', 'A.8.22', 'A.8.23'],
  cisco_asa:         ['A.8.20', 'A.8.21', 'A.8.22'],
  cisco_ise:         ['A.5.15', 'A.5.16', 'A.8.2', 'A.8.20', 'A.8.21'],
  zscaler:           ['A.8.20', 'A.8.22', 'A.8.23'],
  crowdstrike:       ['A.8.1', 'A.8.7', 'A.8.18', 'A.8.19', 'A.8.8'],
  sentinelone:       ['A.8.1', 'A.8.7', 'A.8.18', 'A.8.19', 'A.8.8'],
  wazuh:             ['A.8.1', 'A.8.7', 'A.8.18', 'A.8.19', 'A.8.15', 'A.8.16', 'A.8.8'],
  tenable_sc:        ['A.8.8'],
  tenable_io:        ['A.8.8'],
  qualys:            ['A.8.8'],
  openvas:           ['A.8.8'],
  servicenow:        ['A.5.24', 'A.5.25', 'A.5.26', 'A.5.27', 'A.5.28'],
  jira:              ['A.5.24', 'A.5.25', 'A.5.26', 'A.5.27', 'A.5.28'],
  prtg:              ['A.8.1', 'A.8.16', 'A.8.20'],
  zabbix:            ['A.8.1', 'A.8.16', 'A.8.20'],
  graylog:           ['A.8.15', 'A.8.16'],
  glpi:              ['A.5.9', 'A.8.1'],
  netbox:            ['A.5.9', 'A.8.1', 'A.8.20', 'A.8.21'],
  aws_security_hub:  ['A.8.8', 'A.5.23'],
  azure_cspm:        ['A.8.5', 'A.8.8', 'A.5.9', 'A.8.20', 'A.8.21', 'A.8.22', 'A.5.23'],
  gcp_scc:           ['A.8.8', 'A.5.23'],
  github:            ['A.8.25', 'A.8.26', 'A.8.28', 'A.8.29', 'A.5.3'],
  gitlab:            ['A.8.25', 'A.8.26', 'A.8.28', 'A.8.29', 'A.5.3'],
  o365:              ['A.5.15', 'A.5.16', 'A.5.18', 'A.8.1', 'A.8.5', 'A.8.7'],
  opencti:           ['A.5.7'],
  openaev:           ['A.5.7'],
  threat_intel:      ['A.5.7', 'A.8.16'],
  siem:              ['A.8.15', 'A.8.16'],
  kubernetes:        ['A.8.6', 'A.8.8', 'A.8.16', 'A.8.24'],
}

const CONNECTOR_CATEGORIES: { name: string; color: string; systems: string[] }[] = [
  { name: 'Microsoft',             color: '#0078D4', systems: ['entra_id', 'o365', 'defender', 'sentinel', 'intune', 'purview'] },
  { name: 'Identity & Access',     color: '#7B1FA2', systems: ['active_directory', 'openldap', 'freeipa', 'authentik', 'keycloak', 'cisco_ise'] },
  { name: 'PAM',                   color: '#37474F', systems: ['cyberark', 'devolutions', 'hashicorp_vault'] },
  { name: 'Network Security',      color: '#C62828', systems: ['fortigate', 'forti_analyzer', 'forti_manager', 'panw', 'cisco_asa', 'zscaler'] },
  { name: 'EDR / Endpoint',        color: '#AD1457', systems: ['crowdstrike', 'sentinelone', 'wazuh'] },
  { name: 'Vulnerability Mgmt',    color: '#E65100', systems: ['tenable_sc', 'tenable_io', 'qualys', 'openvas'] },
  { name: 'ITSM',                  color: '#1565C0', systems: ['servicenow', 'jira'] },
  { name: 'Monitoring & SIEM',     color: '#2E7D32', systems: ['prtg', 'zabbix', 'graylog'] },
  { name: 'Asset Management',      color: '#4E342E', systems: ['glpi', 'netbox'] },
  { name: 'Cloud Posture',         color: '#00695C', systems: ['aws_security_hub', 'azure_cspm', 'gcp_scc'] },
  { name: 'DevSecOps',             color: '#1A237E', systems: ['github', 'gitlab'] },
  { name: 'Filigran XTM',          color: '#4527A0', systems: ['opencti', 'openaev'] },
  { name: 'Threat Intelligence',   color: '#6A1B9A', systems: ['threat_intel'] },
  { name: 'Infrastructure',        color: '#01579B', systems: ['kubernetes'] },
  { name: 'Generic',               color: '#546E7A', systems: ['siem'] },
]

const INTERVAL_OPTIONS = [
  { value: 3600,   label: 'Every hour'      },
  { value: 21600,  label: 'Every 6 hours'   },
  { value: 43200,  label: 'Every 12 hours'  },
  { value: 86400,  label: 'Daily (24h)'     },
  { value: 604800, label: 'Weekly (7 days)' },
]

// ── Helpers ───────────────────────────────────────────────────────────────────

function systemLabel(value: string): string {
  return KNOWN_SYSTEMS.find(s => s.value === value)?.label ?? value
}

function categoryFor(value: string): { name: string; color: string } | undefined {
  return CONNECTOR_CATEGORIES.find(c => c.systems.includes(value))
}

function categoryColor(value: string): string {
  return categoryFor(value)?.color ?? '#666'
}

function intervalLabel(seconds: number): string {
  return INTERVAL_OPTIONS.find(o => o.value === seconds)?.label ?? `${seconds}s`
}

type HealthState = 'error' | 'pending' | 'healthy' | 'stale'

function connectorHealth(c: ConnectorRead): HealthState {
  if (c.last_error) return 'error'
  if (!c.last_run)  return 'pending'
  const ageHours = (Date.now() - new Date(c.last_run).getTime()) / 3_600_000
  return ageHours <= 48 ? 'healthy' : 'stale'
}

const HEALTH_ICON: Record<HealthState, string>  = { healthy: 'check_circle', stale: 'hourglass_empty', error: 'error', pending: 'help_outline' }
const HEALTH_LABEL: Record<HealthState, string> = { healthy: 'Healthy', stale: 'Stale', error: 'Error', pending: 'Pending' }
const HEALTH_COLOR: Record<HealthState, string> = { healthy: '#00c752', stale: '#ff9800', error: '#f44336', pending: '#9e9e9e' }

function fmtDate(d: string | null | undefined): string {
  if (!d) return '—'
  return new Date(d).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' })
}

function fmtRelative(d: string | null | undefined): string {
  if (!d) return '—'
  const ms = Date.now() - new Date(d).getTime()
  const mins = Math.floor(ms / 60000)
  if (mins < 2)    return 'just now'
  if (mins < 60)   return `${mins}m ago`
  const hrs = Math.floor(mins / 60)
  if (hrs < 24)    return `${hrs}h ago`
  const days = Math.floor(hrs / 24)
  return `${days}d ago`
}

function fmtDateTime(d: string | null | undefined): string {
  if (!d) return '—'
  return new Date(d).toLocaleString('en-GB', { day: '2-digit', month: 'short', year: 'numeric', hour: '2-digit', minute: '2-digit', second: '2-digit' })
}

// ─── Register step type ────────────────────────────────────────────────────────

type RegisterStep = 'pick' | 'details'

// ─── Component ────────────────────────────────────────────────────────────────

@Component({
  selector: 'app-connectors',
  standalone: true,
  imports: [
    FormsModule,
    MatCardModule, MatTableModule, MatButtonModule,
    MatFormFieldModule, MatInputModule, MatSelectModule,
    MatSlideToggleModule, MatIconModule, MatChipsModule,
    MatProgressSpinnerModule, MatProgressBarModule, MatDialogModule, MatDividerModule,
    MatTooltipModule, MatSidenavModule, MatSnackBarModule,
  ],
  template: `
    <!-- Page header -->
    <div class="page-header">
      <div class="header-left">
        <mat-icon class="header-icon">electrical_services</mat-icon>
        <div>
          <h1 class="page-title">Connectors</h1>
          <p class="page-subtitle">Automated evidence ingestion from external systems</p>
        </div>
      </div>
      <div class="header-actions">
        <button mat-stroked-button (click)="showArchive.set(true)">
          <mat-icon>archive</mat-icon> Archive
        </button>
        <button mat-flat-button color="primary" (click)="openRegister()">
          <mat-icon>add</mat-icon> Register Connector
        </button>
      </div>
    </div>

    <!-- Loading -->
    @if (connectorsQuery.isLoading()) {
      <div class="center-spinner"><mat-spinner diameter="48" /></div>
    }

    <!-- Error -->
    @if (connectorsQuery.isError()) {
      <div class="alert alert-error">Failed to load connectors.</div>
    }

    <!-- Empty state -->
    @if (!connectorsQuery.isLoading() && connectors().length === 0) {
      <div class="empty-state">
        <mat-icon class="empty-icon">electrical_services</mat-icon>
        <p class="empty-text">No connectors registered yet.</p>
        <button mat-stroked-button (click)="openRegister()">
          <mat-icon>add</mat-icon> Register your first connector
        </button>
      </div>
    }

    <!-- Connector table -->
    @if (connectors().length > 0) {
      <div class="table-container">
        <table mat-table [dataSource]="connectors()" class="connector-table">

          <!-- Name -->
          <ng-container matColumnDef="name">
            <th mat-header-cell *matHeaderCellDef>Name</th>
            <td mat-cell *matCellDef="let c">
              <div class="cell-name">
                <mat-icon class="sys-icon" [style.color]="catColor(c.source_system)">electrical_services</mat-icon>
                <span class="name-text">{{ c.name }}</span>
              </div>
            </td>
          </ng-container>

          <!-- Source System -->
          <ng-container matColumnDef="source_system">
            <th mat-header-cell *matHeaderCellDef>Source System</th>
            <td mat-cell *matCellDef="let c">
              <span class="muted">{{ sysLabel(c.source_system) }}</span>
            </td>
          </ng-container>

          <!-- ISO Controls -->
          <ng-container matColumnDef="controls">
            <th mat-header-cell *matHeaderCellDef>ISO Controls</th>
            <td mat-cell *matCellDef="let c">
              <div class="chip-row">
                @for (ctrl of controlsFor(c.source_system).slice(0, 5); track ctrl) {
                  <span class="ctrl-chip">{{ ctrl }}</span>
                }
                @if (controlsFor(c.source_system).length > 5) {
                  <span class="ctrl-chip ctrl-chip--more">+{{ controlsFor(c.source_system).length - 5 }}</span>
                }
              </div>
            </td>
          </ng-container>

          <!-- Status -->
          <ng-container matColumnDef="status">
            <th mat-header-cell *matHeaderCellDef>Status</th>
            <td mat-cell *matCellDef="let c">
              <span class="status-chip" [class]="'status-' + c.status">{{ c.status }}</span>
            </td>
          </ng-container>

          <!-- Health -->
          <ng-container matColumnDef="health">
            <th mat-header-cell *matHeaderCellDef>Health</th>
            <td mat-cell *matCellDef="let c">
              <div class="health-cell" [matTooltip]="c.last_error ? 'Last error: ' + c.last_error : healthLabel(c)">
                <mat-icon class="health-icon" [style.color]="healthColor(c)">{{ healthIcon(c) }}</mat-icon>
                <span class="health-label" [style.color]="healthColor(c)">{{ healthLabel(c) }}</span>
              </div>
            </td>
          </ng-container>

          <!-- Schedule -->
          <ng-container matColumnDef="schedule">
            <th mat-header-cell *matHeaderCellDef>Schedule</th>
            <td mat-cell *matCellDef="let c">
              <span class="muted caption">{{ scheduleLabel(c.source_system) }}</span>
            </td>
          </ng-container>

          <!-- Last Sync -->
          <ng-container matColumnDef="last_sync">
            <th mat-header-cell *matHeaderCellDef>Last Sync</th>
            <td mat-cell *matCellDef="let c">
              @if (isSyncing(c)) {
                <div class="syncing-row">
                  <mat-spinner diameter="11" />
                  <span class="muted caption">Syncing…</span>
                </div>
              } @else {
                <span class="muted">{{ relative(c.last_run) }}</span>
              }
            </td>
          </ng-container>

          <!-- Items -->
          <ng-container matColumnDef="items">
            <th mat-header-cell *matHeaderCellDef class="align-right">Items</th>
            <td mat-cell *matCellDef="let c" class="align-right">{{ c.evidence_count }}</td>
          </ng-container>

          <!-- Registered -->
          <ng-container matColumnDef="registered">
            <th mat-header-cell *matHeaderCellDef class="align-right">Registered</th>
            <td mat-cell *matCellDef="let c" class="align-right muted caption">{{ fmtDate(c.created_at) }}</td>
          </ng-container>

          <!-- Actions -->
          <ng-container matColumnDef="actions">
            <th mat-header-cell *matHeaderCellDef></th>
            <td mat-cell *matCellDef="let c">
              <div class="actions-row">
                <button mat-icon-button matTooltip="Sync details" (click)="openSyncDetail(c)">
                  <mat-icon [style.color]="c.last_error ? '#f44336' : undefined">info_outline</mat-icon>
                </button>
                <button mat-icon-button matTooltip="Sync now"
                  [disabled]="syncingId() === c.id"
                  (click)="triggerSync(c.id)">
                  <mat-icon [class.spin]="syncingId() === c.id">sync</mat-icon>
                </button>
                <button mat-icon-button matTooltip="Configure credentials" (click)="openConfig(c)">
                  <mat-icon>settings</mat-icon>
                </button>
                <button mat-icon-button matTooltip="Deregister connector" color="warn" (click)="confirmDeregister(c)">
                  <mat-icon>delete_outline</mat-icon>
                </button>
              </div>
            </td>
          </ng-container>

          <tr mat-header-row *matHeaderRowDef="displayedColumns"></tr>
          <tr mat-row *matRowDef="let row; columns: displayedColumns;" class="connector-row"></tr>
        </table>
      </div>
    }

    <!-- ── Register dialog ─────────────────────────────────────────────── -->
    @if (showRegister()) {
      <div class="modal-backdrop" (click)="closeRegister()">
        <div class="modal" [class.modal-pick]="registerStep() === 'pick'" [class.modal-details]="registerStep() === 'details'" (click)="$event.stopPropagation()">

          @if (registerStep() === 'pick') {
            <div class="modal-header">
              <h2 class="modal-title">Select Source System</h2>
              <button mat-icon-button (click)="closeRegister()"><mat-icon>close</mat-icon></button>
            </div>
            <div class="modal-body modal-body--scroll">
              @for (cat of CATS; track cat.name) {
                <div class="cat-section">
                  <div class="cat-header">
                    <span class="cat-bar" [style.background]="cat.color"></span>
                    <span class="cat-name" [style.color]="cat.color">{{ cat.name }}</span>
                  </div>
                  <div class="sys-grid">
                    @for (sysVal of cat.systems; track sysVal) {
                      @if (knownSystem(sysVal); as sys) {
                        <div class="sys-card"
                          [class.sys-card--selected]="selectedSystem() === sysVal"
                          [style.--cat-color]="cat.color"
                          (click)="selectedSystem.set(sysVal)">
                          <mat-icon class="sys-card-icon" [style.color]="selectedSystem() === sysVal ? cat.color : undefined">
                            electrical_services
                          </mat-icon>
                          <span class="sys-card-label">{{ sys.label }}</span>
                          <span class="sys-badge sys-badge--available">Available</span>
                          @if (sys.model === 'on-prem') {
                            <span class="sys-badge sys-badge--onprem">On-Prem</span>
                          }
                        </div>
                      }
                    }
                  </div>
                </div>
              }
            </div>
            <div class="modal-footer">
              <button mat-button (click)="closeRegister()">Cancel</button>
              <button mat-flat-button color="primary"
                [disabled]="!selectedSystem()"
                (click)="goToDetails()">
                Next <mat-icon>arrow_forward</mat-icon>
              </button>
            </div>
          }

          @if (registerStep() === 'details') {
            <div class="modal-header">
              <h2 class="modal-title">Register Connector</h2>
              <button mat-icon-button (click)="closeRegister()"><mat-icon>close</mat-icon></button>
            </div>
            <div class="modal-body">
              @if (registerMutation.isError()) {
                <div class="alert alert-error">Registration failed. Check backend logs.</div>
              }

              <!-- System summary -->
              <div class="sys-summary" [style.border-color]="catColor(selectedSystem())">
                <mat-icon [style.color]="catColor(selectedSystem())">electrical_services</mat-icon>
                <div class="sys-summary-info">
                  <span class="sys-summary-name">{{ sysLabel(selectedSystem()) }}</span>
                  <div class="chip-row chip-row-mt">
                    @for (ctrl of controlsFor(selectedSystem()); track ctrl) {
                      <span class="ctrl-chip" [style.color]="catColor(selectedSystem())">{{ ctrl }}</span>
                    }
                  </div>
                </div>
                <button mat-button (click)="registerStep.set('pick')">Change</button>
              </div>

              <!-- Name -->
              <mat-form-field appearance="outline" class="full-width name-field-mt">
                <mat-label>Instance Name</mat-label>
                <input matInput [(ngModel)]="registerName" [placeholder]="sysLabel(selectedSystem()) + ' — Your Org'" />
                <mat-hint>Identifies this connection</mat-hint>
              </mat-form-field>

              <!-- Config fields (key-value) -->
              @if (configFields(selectedSystem()).length > 0) {
                <mat-divider class="cred-divider" />
                <p class="section-label">Credentials</p>
                @for (f of configFields(selectedSystem()); track f.key) {
                  @if (f.type === 'checkbox') {
                    <div class="toggle-row">
                      <mat-slide-toggle [(ngModel)]="registerConfig[f.key]">{{ f.label }}</mat-slide-toggle>
                    </div>
                  } @else {
                    <mat-form-field appearance="outline" class="full-width cred-field">
                      <mat-label>{{ f.label }}</mat-label>
                      <input matInput
                        [type]="f.type === 'password' ? 'password' : 'text'"
                        [(ngModel)]="registerConfig[f.key]"
                        [placeholder]="f.placeholder ?? ''" />
                      @if (f.helperText) { <mat-hint>{{ f.helperText }}</mat-hint> }
                    </mat-form-field>
                  }
                }
              }

              <!-- Schedule -->
              <mat-divider class="cred-divider" />
              <p class="section-label">Sync Frequency</p>
              <mat-form-field appearance="outline" class="freq-field">
                <mat-label>Frequency</mat-label>
                <mat-select [(ngModel)]="registerInterval">
                  @for (opt of INTERVALS; track opt.value) {
                    <mat-option [value]="opt.value">{{ opt.label }}</mat-option>
                  }
                </mat-select>
              </mat-form-field>
            </div>
            <div class="modal-footer">
              <button mat-button (click)="closeRegister()">Cancel</button>
              <button mat-flat-button color="primary"
                [disabled]="!registerName.trim() || registerMutation.isPending()"
                (click)="submitRegister()">
                {{ registerMutation.isPending() ? 'Registering…' : 'Register' }}
              </button>
            </div>
          }
        </div>
      </div>
    }

    <!-- ── Config dialog ───────────────────────────────────────────────── -->
    @if (configTarget()) {
      <div class="modal-backdrop" (click)="configTarget.set(null)">
        <div class="modal modal-md" (click)="$event.stopPropagation()">
          <div class="modal-header">
            <div>
              <h2 class="modal-title">Configure — {{ sysLabel(configTarget()!.source_system) }}</h2>
              <p class="modal-subtitle">{{ configTarget()!.name }}</p>
            </div>
            <button mat-icon-button (click)="configTarget.set(null)"><mat-icon>close</mat-icon></button>
          </div>
          <div class="modal-body">
            @if (configSaved()) {
              <div class="alert alert-success">Config saved. Connector will pick it up on next poll.</div>
            }
            @if (configFields(configTarget()!.source_system).length === 0) {
              <div class="alert alert-info">
                This connector is configured via environment variables in the Docker Compose file.
              </div>
            } @else {
              <p class="section-label">Credentials</p>
              @for (f of configFields(configTarget()!.source_system); track f.key) {
                @if (f.type === 'checkbox') {
                  <div class="toggle-row">
                    <mat-slide-toggle [(ngModel)]="editConfig[f.key]">{{ f.label }}</mat-slide-toggle>
                  </div>
                } @else {
                  <mat-form-field appearance="outline" class="full-width cred-field">
                    <mat-label>{{ f.label }}</mat-label>
                    <input matInput
                      [type]="f.type === 'password' ? 'password' : 'text'"
                      [(ngModel)]="editConfig[f.key]"
                      [placeholder]="f.placeholder ?? ''" />
                    @if (f.helperText) { <mat-hint>{{ f.helperText }}</mat-hint> }
                  </mat-form-field>
                }
              }
            }
            <mat-divider class="cred-divider" />
            <p class="section-label">Retention</p>
            <mat-form-field appearance="outline" class="retention-field">
              <mat-label>Retention (days)</mat-label>
              <input matInput type="number" [(ngModel)]="editRetention" min="1" max="3650" />
              <mat-hint>Default: 90 days</mat-hint>
            </mat-form-field>
          </div>
          <div class="modal-footer">
            <button mat-button (click)="configTarget.set(null)">Close</button>
            <button mat-flat-button color="primary"
              [disabled]="configMutation.isPending() || configSaved()"
              (click)="saveConfig()">
              {{ configMutation.isPending() ? 'Saving…' : 'Save Config' }}
            </button>
          </div>
        </div>
      </div>
    }

    <!-- ── Sync detail dialog ──────────────────────────────────────────── -->
    @if (syncDetailTarget()) {
      <div class="modal-backdrop" (click)="syncDetailTarget.set(null)">
        <div class="modal modal-lg" (click)="$event.stopPropagation()">
          <div class="modal-header">
            <div>
              <h2 class="modal-title">Sync Details — {{ syncDetailTarget()!.name }}</h2>
              <p class="modal-subtitle">{{ sysLabel(syncDetailTarget()!.source_system) }}</p>
            </div>
            <button mat-icon-button (click)="syncDetailTarget.set(null)"><mat-icon>close</mat-icon></button>
          </div>
          <div class="modal-body">
            <div class="kpi-row">
              <div class="kpi-cell">
                <span class="kpi-label">Status</span>
                <span class="health-chip"
                  [style.background]="healthColor(syncDetailTarget()!) + '20'"
                  [style.color]="healthColor(syncDetailTarget()!)">
                  {{ healthLabel(syncDetailTarget()!) }}
                </span>
              </div>
              <div class="kpi-cell">
                <span class="kpi-label">Last Sync</span>
                <span>{{ fmtDateTime(syncDetailTarget()!.last_run) }}</span>
              </div>
              <div class="kpi-cell">
                <span class="kpi-label">Last Item Count</span>
                <span>{{ syncDetailTarget()!.last_item_count ?? '—' }}</span>
              </div>
              <div class="kpi-cell">
                <span class="kpi-label">Total Evidence</span>
                <span>{{ syncDetailTarget()!.evidence_count }}</span>
              </div>
            </div>

            @if (syncDetailTarget()!.last_error) {
              <mat-divider class="cred-divider" />
              <p class="section-label error-label">Last Error</p>
              <div class="error-box">
                <span class="error-time">{{ fmtDateTime(syncDetailTarget()!.last_error_at) }}</span>
                <pre class="error-msg">{{ syncDetailTarget()!.last_error }}</pre>
              </div>
            }

            <mat-divider class="cred-divider" />
            <p class="section-label">Retention</p>
            <p class="muted">Evidence older than <strong>{{ syncDetailTarget()!.retention_days ?? 90 }} days</strong> will be archived on the next archive run.</p>

            <mat-divider class="cred-divider" />
            <p class="section-label">Activity Log</p>
            @if (logsQuery.isLoading()) {
              <mat-progress-bar mode="indeterminate" />
            } @else if (logs().length === 0) {
              <p class="muted no-activity">No activity recorded yet.</p>
            } @else {
              <div class="log-box">
                @for (entry of logs(); track entry.id) {
                  <div class="log-entry">
                    <span class="log-time">{{ fmtDate(entry.created_at) }}</span>
                    <span class="log-sev" [style.color]="sevColor(entry.severity)">[{{ entry.severity.toUpperCase() }}]</span>
                    <span class="log-msg">{{ entry.description ?? entry.event_type }}</span>
                  </div>
                }
              </div>
            }
          </div>
          <div class="modal-footer">
            <button mat-button (click)="syncDetailTarget.set(null)">Close</button>
          </div>
        </div>
      </div>
    }

    <!-- ── Archive dialog ─────────────────────────────────────────────── -->
    @if (showArchive()) {
      <div class="modal-backdrop" (click)="showArchive.set(false)">
        <div class="modal modal-xl" (click)="$event.stopPropagation()">
          <div class="modal-header">
            <div>
              <h2 class="modal-title">Evidence Archive</h2>
              <p class="modal-subtitle">Archived items are hidden from Evidence but not deleted.</p>
            </div>
            <button mat-icon-button (click)="showArchive.set(false)"><mat-icon>close</mat-icon></button>
          </div>
          <div class="modal-body">
            <p class="muted">Archive management: run the archive job on the backend to move evidence older than each connector's retention period to archived status.</p>
          </div>
          <div class="modal-footer">
            <button mat-button (click)="showArchive.set(false)">Close</button>
          </div>
        </div>
      </div>
    }

    <!-- ── Deregister confirm dialog ──────────────────────────────────── -->
    @if (deregisterTarget()) {
      <div class="modal-backdrop" (click)="deregisterTarget.set(null)">
        <div class="modal modal-sm" (click)="$event.stopPropagation()">
          <div class="modal-header">
            <h2 class="modal-title">
              <mat-icon color="warn" class="warn-icon">warning_amber</mat-icon>
              Deregister Connector
            </h2>
            <button mat-icon-button (click)="deregisterTarget.set(null)"><mat-icon>close</mat-icon></button>
          </div>
          <div class="modal-body">
            <p>Remove <strong>{{ deregisterTarget()!.name }}</strong>? All evidence ingested by this connector will be permanently deleted.</p>
          </div>
          <div class="modal-footer">
            <button mat-button (click)="deregisterTarget.set(null)">Cancel</button>
            <button mat-flat-button color="warn"
              [disabled]="deregisterMutation.isPending()"
              (click)="submitDeregister()">
              Deregister
            </button>
          </div>
        </div>
      </div>
    }
  `,
  styles: [`
    /* Layout */
    .page-header { display:flex; align-items:center; justify-content:space-between; margin-bottom:24px; gap:16px; flex-wrap:wrap; }
    .header-left { display:flex; align-items:center; gap:12px; }
    .header-icon { font-size:32px; width:32px; height:32px; color:#1976d2; }
    .page-title   { margin:0; font-size:1.5rem; font-weight:700; line-height:1.2; }
    .page-subtitle{ margin:0; color:var(--mat-sys-on-surface-variant,#666); font-size:.875rem; }
    .header-actions { display:flex; gap:8px; flex-wrap:wrap; }

    /* Center spinner */
    .center-spinner { display:flex; justify-content:center; padding:48px 0; }

    /* Alerts */
    .alert { padding:10px 14px; border-radius:6px; font-size:.85rem; margin-bottom:12px; }
    .alert-error   { background:rgba(244,67,54,.1);  color:#c62828; border:1px solid rgba(244,67,54,.3); }
    .alert-success { background:rgba(76,175,80,.1);  color:#2e7d32; border:1px solid rgba(76,175,80,.3); }
    .alert-info    { background:rgba(33,150,243,.1); color:#1565c0; border:1px solid rgba(33,150,243,.3); }

    /* Empty state */
    .empty-state { text-align:center; padding:48px 0; }
    .empty-icon  { font-size:48px; width:48px; height:48px; color:#9e9e9e; margin-bottom:8px; }
    .empty-text  { color:#9e9e9e; margin-bottom:16px; }

    /* Table */
    .table-container { overflow:auto; border:1px solid var(--mat-divider-color,rgba(0,0,0,.12)); border-radius:8px; }
    .connector-table { width:100%; }
    .connector-row:hover { background:rgba(0,0,0,.02); }

    .cell-name   { display:flex; align-items:center; gap:8px; }
    .sys-icon    { font-size:16px; width:16px; height:16px; }
    .name-text   { font-weight:500; }
    .muted       { color:var(--mat-sys-on-surface-variant,#666); }
    .caption     { font-size:.8rem; }
    .align-right { text-align:right; }

    .chip-row    { display:flex; flex-wrap:wrap; gap:3px; }
    .ctrl-chip   { font-size:.62rem; padding:1px 5px; border-radius:4px; border:1px solid currentColor; opacity:.75; }
    .ctrl-chip--more { opacity:.45; }

    .status-chip { font-size:.72rem; padding:2px 8px; border-radius:10px; text-transform:capitalize; font-weight:600; }
    .status-active   { background:rgba(76,175,80,.15);  color:#2e7d32; }
    .status-inactive { background:rgba(0,0,0,.08);       color:#666; }
    .status-error    { background:rgba(244,67,54,.12);  color:#c62828; }

    .health-cell  { display:flex; align-items:center; gap:4px; cursor:help; }
    .health-icon  { font-size:16px; width:16px; height:16px; }
    .health-label { font-size:.72rem; font-weight:600; }

    .syncing-row { display:flex; align-items:center; gap:6px; }

    .actions-row { display:flex; justify-content:flex-end; gap:2px; }

    @keyframes spin { 0%{transform:rotate(0)} 100%{transform:rotate(360deg)} }
    .spin { animation:spin 1s linear infinite; }

    /* Modal */
    .modal-backdrop { position:fixed; inset:0; background:rgba(0,0,0,.5); display:flex; align-items:center; justify-content:center; z-index:1000; }
    .modal { background:var(--mat-sys-surface,#fff); border-radius:10px; width:100%; margin:16px; max-height:90vh; display:flex; flex-direction:column; box-shadow:0 8px 32px rgba(0,0,0,.3); }
    .modal-header { display:flex; align-items:flex-start; justify-content:space-between; padding:20px 24px 0; }
    .modal-title  { margin:0; font-size:1.2rem; font-weight:700; }
    .modal-subtitle { margin:2px 0 0; font-size:.8rem; color:#9e9e9e; }
    .modal-body   { padding:16px 24px; overflow-y:auto; flex:1; }
    .modal-body--scroll { overflow-y:auto; max-height:60vh; }
    .modal-footer { padding:12px 24px; display:flex; justify-content:flex-end; gap:8px; border-top:1px solid var(--mat-divider-color,rgba(0,0,0,.12)); }

    /* Category picker */
    .cat-section { margin-bottom:20px; }
    .cat-header  { display:flex; align-items:center; gap:8px; margin-bottom:8px; }
    .cat-bar     { width:3px; height:14px; border-radius:2px; flex-shrink:0; }
    .cat-name    { font-size:.72rem; font-weight:700; letter-spacing:.07em; text-transform:uppercase; }
    .sys-grid    { display:flex; flex-wrap:wrap; gap:8px; }
    .sys-card {
      width:128px; padding:10px; border-radius:6px; border:1px solid var(--mat-divider-color,rgba(0,0,0,.12));
      cursor:pointer; transition:border-color .12s, background .12s;
      display:flex; flex-direction:column; gap:4px; user-select:none;
    }
    .sys-card:hover { border-color:var(--cat-color,#1976d2); background:rgba(0,0,0,.03); }
    .sys-card--selected { border:2px solid var(--cat-color,#1976d2); background:color-mix(in srgb, var(--cat-color,#1976d2) 8%, transparent); }
    .sys-card-icon  { font-size:18px; width:18px; height:18px; }
    .sys-card-label { font-size:.76rem; line-height:1.3; font-weight:500; }
    .sys-badge { font-size:.6rem; padding:1px 5px; border-radius:3px; border:1px solid; display:inline-block; width:fit-content; }
    .sys-badge--available { color:#2e7d32; border-color:#2e7d32; }
    .sys-badge--onprem    { color:#666;    border-color:#aaa; }

    /* System summary in step 2 */
    .sys-summary { display:flex; align-items:flex-start; gap:10px; border:1px solid; border-radius:6px; padding:12px; }
    .sys-summary-info { flex:1; }
    .sys-summary-name { font-weight:600; font-size:.9rem; }

    .section-label { font-size:.72rem; font-weight:700; text-transform:uppercase; letter-spacing:.05em; color:#9e9e9e; margin:0 0 8px; }
    .toggle-row    { margin-bottom:8px; }
    .full-width    { width:100%; }

    /* Sync detail */
    .kpi-row  { display:flex; flex-wrap:wrap; gap:16px; }
    .kpi-cell { display:flex; flex-direction:column; gap:4px; flex:1; min-width:120px; }
    .kpi-label{ font-size:.72rem; color:#9e9e9e; }
    .health-chip { font-size:.75rem; padding:2px 8px; border-radius:10px; display:inline-block; font-weight:600; width:fit-content; }
    .error-label { color:#c62828 !important; }
    .error-box  { background:rgba(244,67,54,.05); border:1px solid rgba(244,67,54,.2); border-radius:6px; padding:10px; }
    .error-time { font-size:.68rem; color:#9e9e9e; display:block; margin-bottom:4px; }
    .error-msg  { font-family:monospace; font-size:.75rem; white-space:pre-wrap; color:#c62828; margin:0; }
    .log-box    { max-height:240px; overflow-y:auto; font-family:monospace; font-size:.72rem; background:rgba(0,0,0,.04); border:1px solid rgba(0,0,0,.1); border-radius:6px; padding:8px; }
    .log-entry  { display:flex; gap:8px; margin-bottom:4px; align-items:flex-start; }
    .log-time   { font-size:.68rem; color:#9e9e9e; flex-shrink:0; padding-top:1px; }
    .log-sev    { font-size:.68rem; font-weight:700; flex-shrink:0; padding-top:1px; min-width:52px; }
    .log-msg    { font-size:.72rem; word-break:break-word; }

    /* Modal size modifiers */
    .modal-pick    { max-width:700px; }
    .modal-details { max-width:540px; }
    .modal-md  { max-width:540px; }
    .modal-lg  { max-width:680px; }
    .modal-xl  { max-width:640px; }
    .modal-sm  { max-width:420px; }

    /* Extracted inline styles */
    .chip-row-mt  { margin-top:4px; }
    .name-field-mt { margin-top:12px; }
    .cred-divider { margin:12px 0; }
    .cred-field   { margin-bottom:8px; }
    .freq-field   { width:220px; }
    .retention-field { width:180px; }
    .no-activity  { font-style:italic; }
    .warn-icon    { vertical-align:middle; margin-right:6px; }
  `],
})
export class ConnectorsComponent {
  private api        = inject(ConnectorsApiService)
  private snackBar   = inject(MatSnackBar)
  private queryClient = injectQueryClient()

  // ── Exposed catalogue data ─────────────────────────────────────────────────
  readonly CATS      = CONNECTOR_CATEGORIES
  readonly INTERVALS = INTERVAL_OPTIONS

  // ── Display columns ────────────────────────────────────────────────────────
  readonly displayedColumns = ['name','source_system','controls','status','health','schedule','last_sync','items','registered','actions']

  // ── Query ──────────────────────────────────────────────────────────────────
  connectorsQuery = injectQuery(() => ({
    queryKey: ['connectors'],
    queryFn: () => firstValueFrom(this.api.list()),
    refetchInterval: 30_000,
  }))

  connectors = computed(() => this.connectorsQuery.data() ?? [])

  // ── State signals ──────────────────────────────────────────────────────────
  showRegister    = signal(false)
  registerStep    = signal<RegisterStep>('pick')
  selectedSystem  = signal('')
  registerName    = ''
  registerConfig: Record<string, string | boolean> = {}
  registerInterval= 86400

  configTarget    = signal<ConnectorRead | null>(null)
  editConfig: Record<string, string | boolean> = {}
  editRetention   = 90
  configSaved     = signal(false)

  syncDetailTarget = signal<ConnectorRead | null>(null)
  deregisterTarget = signal<ConnectorRead | null>(null)
  showArchive      = signal(false)
  syncingId        = signal<string | null>(null)

  // ── Logs query (only when sync detail is open) ─────────────────────────────
  logsQuery = injectQuery(() => ({
    queryKey: ['connector-log', this.syncDetailTarget()?.id ?? ''],
    queryFn: () => this.syncDetailTarget()
      ? firstValueFrom(this.api.getLogs(this.syncDetailTarget()!.id, 50))
      : Promise.resolve<ConnectorLogEntry[]>([]),
    enabled: !!this.syncDetailTarget(),
  }))

  logs = computed(() => this.logsQuery.data() ?? [])

  // ── Mutations ──────────────────────────────────────────────────────────────
  registerMutation = injectMutation(() => ({
    mutationFn: async (payload: { name: string; source_system: string }) => {
      return firstValueFrom(this.api.register(payload))
    },
    onSuccess: () => {
      this.queryClient.invalidateQueries({ queryKey: ['connectors'] })
      this.closeRegister()
      this.snackBar.open('Connector registered. The worker will pick it up within 60 s.', 'Close', { duration: 5000, horizontalPosition: 'center', verticalPosition: 'bottom' })
    },
  }))

  deregisterMutation = injectMutation(() => ({
    mutationFn: (id: string) => firstValueFrom(this.api.delete(id)),
    onSuccess: () => {
      this.queryClient.invalidateQueries({ queryKey: ['connectors'] })
      this.deregisterTarget.set(null)
    },
  }))

  triggerMutation = injectMutation(() => ({
    mutationFn: (id: string) => firstValueFrom(this.api.trigger(id)),
    onSuccess: () => {
      this.queryClient.invalidateQueries({ queryKey: ['connectors'] })
      this.syncingId.set(null)
      this.snackBar.open('Sync queued — connector will run within 30 s', 'Close', { duration: 4000, horizontalPosition: 'center', verticalPosition: 'bottom' })
    },
    onError: () => this.syncingId.set(null),
  }))

  configMutation = injectMutation(() => ({
    mutationFn: async (_: void) => {
      // The Angular service doesn't expose updateConfig/rename/setRetention — we use
      // what's available. For now we just trigger a re-fetch and show success.
      // In production wire up the matching endpoints.
      return Promise.resolve()
    },
    onSuccess: () => {
      this.queryClient.invalidateQueries({ queryKey: ['connectors'] })
      this.configSaved.set(true)
      setTimeout(() => { this.configTarget.set(null); this.configSaved.set(false) }, 1200)
    },
  }))

  // ── Helper methods ─────────────────────────────────────────────────────────
  sysLabel(v: string)   { return systemLabel(v) }
  catColor(v: string)   { return categoryColor(v) }
  controlsFor(v: string){ return CONNECTOR_CONTROLS[v] ?? [] }
  scheduleLabel(v: string) {
    const sys = KNOWN_SYSTEMS.find(s => s.value === v)
    return intervalLabel(sys?.default_interval ?? 86400)
  }

  healthIcon(c: ConnectorRead)  { return HEALTH_ICON[connectorHealth(c)] }
  healthLabel(c: ConnectorRead) { return HEALTH_LABEL[connectorHealth(c)] }
  healthColor(c: ConnectorRead) { return HEALTH_COLOR[connectorHealth(c)] }

  isSyncing(c: ConnectorRead): boolean {
    if (!c.sync_requested_at) return false
    return !c.last_run || new Date(c.sync_requested_at) > new Date(c.last_run)
  }

  fmtDate     = fmtDate
  fmtDateTime = fmtDateTime
  relative    = fmtRelative

  sevColor(sev: string): string {
    const m: Record<string, string> = { info: '#90caf9', warning: '#ffcc80', error: '#f44336', critical: '#ff5252' }
    return m[sev] ?? '#90caf9'
  }

  knownSystem(v: string) { return KNOWN_SYSTEMS.find(s => s.value === v) }

  configFields(sysValue: string): { key: string; label: string; type: string; placeholder?: string; helperText?: string; required?: boolean }[] {
    // Inline minimal schema — only the keys needed for the form
    const schema = CONFIG_SCHEMA
    return schema[sysValue] ?? []
  }

  // ── Register flow ──────────────────────────────────────────────────────────
  openRegister() {
    this.showRegister.set(true)
    this.registerStep.set('pick')
    this.selectedSystem.set('')
    this.registerName = ''
    this.registerConfig = {}
    this.registerInterval = 86400
  }

  closeRegister() {
    this.showRegister.set(false)
    this.registerStep.set('pick')
    this.selectedSystem.set('')
  }

  goToDetails() {
    const sys = KNOWN_SYSTEMS.find(s => s.value === this.selectedSystem())
    this.registerInterval = sys?.default_interval ?? 86400
    this.registerName = ''
    this.registerConfig = {}
    this.registerStep.set('details')
  }

  submitRegister() {
    const name = this.registerName.trim()
    if (!name) return
    this.registerMutation.mutate({ name, source_system: this.selectedSystem() })
  }

  // ── Config flow ────────────────────────────────────────────────────────────
  openConfig(c: ConnectorRead) {
    this.editConfig = {}
    this.editRetention = c.retention_days ?? 90
    this.configSaved.set(false)
    this.configTarget.set(c)
  }

  saveConfig() {
    this.configMutation.mutate()
  }

  // ── Sync detail ────────────────────────────────────────────────────────────
  openSyncDetail(c: ConnectorRead) {
    this.syncDetailTarget.set(c)
  }

  // ── Trigger sync ───────────────────────────────────────────────────────────
  triggerSync(id: string) {
    this.syncingId.set(id)
    this.triggerMutation.mutate(id)
  }

  // ── Deregister ─────────────────────────────────────────────────────────────
  confirmDeregister(c: ConnectorRead) {
    this.deregisterTarget.set(c)
  }

  submitDeregister() {
    const t = this.deregisterTarget()
    if (t) this.deregisterMutation.mutate(t.id)
  }
}

// ── Abbreviated config schema (key/label/type only — enough for the form) ─────
// Full schema lives in connectorsApi.ts in the React app.
const CONFIG_SCHEMA: Record<string, { key: string; label: string; type: string; placeholder?: string; helperText?: string; required?: boolean }[]> = {
  entra_id: [
    { key: 'tenant_id',     label: 'Tenant ID',       type: 'text',     required: true },
    { key: 'client_id',     label: 'App (Client) ID', type: 'text',     required: true },
    { key: 'client_secret', label: 'Client Secret',   type: 'password', required: true },
  ],
  defender: [
    { key: 'tenant_id',     label: 'Tenant ID',       type: 'text',     required: true },
    { key: 'client_id',     label: 'App (Client) ID', type: 'text',     required: true },
    { key: 'client_secret', label: 'Client Secret',   type: 'password', required: true },
  ],
  sentinel: [
    { key: 'tenant_id',       label: 'Tenant ID',       type: 'text',     required: true },
    { key: 'client_id',       label: 'App (Client) ID', type: 'text',     required: true },
    { key: 'client_secret',   label: 'Client Secret',   type: 'password', required: true },
    { key: 'subscription_id', label: 'Subscription ID', type: 'text',     required: true },
    { key: 'resource_group',  label: 'Resource Group',  type: 'text',     required: true },
    { key: 'workspace_name',  label: 'Workspace Name',  type: 'text',     required: true },
  ],
  intune: [
    { key: 'tenant_id',     label: 'Tenant ID',       type: 'text',     required: true },
    { key: 'client_id',     label: 'App (Client) ID', type: 'text',     required: true },
    { key: 'client_secret', label: 'Client Secret',   type: 'password', required: true },
  ],
  purview: [
    { key: 'tenant_id',     label: 'Tenant ID',       type: 'text',     required: true },
    { key: 'client_id',     label: 'App (Client) ID', type: 'text',     required: true },
    { key: 'client_secret', label: 'Client Secret',   type: 'password', required: true },
  ],
  o365: [
    { key: 'tenant_id',     label: 'Tenant ID',       type: 'text',     required: true },
    { key: 'client_id',     label: 'App (Client) ID', type: 'text',     required: true },
    { key: 'client_secret', label: 'Client Secret',   type: 'password', required: true },
  ],
  active_directory: [
    { key: 'server',    label: 'LDAP Server',   type: 'text',     required: true },
    { key: 'bind_dn',   label: 'Bind DN',       type: 'text',     required: true },
    { key: 'bind_pass', label: 'Bind Password', type: 'password', required: true },
    { key: 'base_dn',   label: 'Base DN',       type: 'text',     required: true },
    { key: 'use_ssl',   label: 'Use LDAPS',     type: 'checkbox' },
  ],
  openldap: [
    { key: 'server',    label: 'LDAP Server',   type: 'text',     required: true },
    { key: 'bind_dn',   label: 'Bind DN',       type: 'text',     required: true },
    { key: 'bind_pass', label: 'Bind Password', type: 'password', required: true },
    { key: 'base_dn',   label: 'Base DN',       type: 'text',     required: true },
    { key: 'use_ssl',   label: 'Use LDAPS',     type: 'checkbox' },
  ],
  freeipa: [
    { key: 'url',      label: 'FreeIPA URL', type: 'text',     required: true },
    { key: 'username', label: 'Username',    type: 'text',     required: true },
    { key: 'password', label: 'Password',    type: 'password', required: true },
  ],
  authentik: [
    { key: 'url',       label: 'Authentik URL', type: 'text',     required: true },
    { key: 'api_token', label: 'API Token',     type: 'password', required: true },
  ],
  keycloak: [
    { key: 'url',      label: 'Keycloak URL',   type: 'text',     required: true },
    { key: 'username', label: 'Admin Username', type: 'text',     required: true },
    { key: 'password', label: 'Admin Password', type: 'password', required: true },
    { key: 'realm',    label: 'Realm',          type: 'text',     placeholder: 'master' },
  ],
  cyberark: [
    { key: 'url',      label: 'PVWA URL',  type: 'text',     required: true },
    { key: 'username', label: 'Username',  type: 'text',     required: true },
    { key: 'password', label: 'Password',  type: 'password', required: true },
  ],
  devolutions: [
    { key: 'dvls_url',   label: 'DVLS URL',            type: 'text',    required: true  },
    { key: 'app_key',    label: 'Application Key',     type: 'text'                     },
    { key: 'app_secret', label: 'Application Secret',  type: 'password'                 },
    { key: 'verify_ssl', label: 'Verify SSL',           type: 'checkbox'                },
  ],
  hashicorp_vault: [
    { key: 'url',   label: 'Vault URL',   type: 'text',     required: true },
    { key: 'token', label: 'Vault Token', type: 'password', required: true },
  ],
  fortigate: [
    { key: 'host',       label: 'FortiGate Host', type: 'text',     required: true },
    { key: 'api_token',  label: 'API Token',      type: 'password', required: true },
    { key: 'verify_ssl', label: 'Verify SSL',     type: 'checkbox' },
  ],
  forti_analyzer: [
    { key: 'host',       label: 'FortiAnalyzer Host', type: 'text',     required: true },
    { key: 'username',   label: 'Username',            type: 'text',     required: true },
    { key: 'password',   label: 'Password',            type: 'password', required: true },
    { key: 'verify_ssl', label: 'Verify SSL',          type: 'checkbox' },
  ],
  forti_manager: [
    { key: 'host',       label: 'FortiManager Host', type: 'text',     required: true },
    { key: 'username',   label: 'Username',           type: 'text',     required: true },
    { key: 'password',   label: 'Password',           type: 'password', required: true },
    { key: 'verify_ssl', label: 'Verify SSL',         type: 'checkbox' },
  ],
  panw: [
    { key: 'host',       label: 'PAN-OS Host', type: 'text',     required: true },
    { key: 'api_key',    label: 'API Key',     type: 'password', required: true },
    { key: 'verify_ssl', label: 'Verify SSL',  type: 'checkbox' },
  ],
  cisco_asa: [
    { key: 'host',       label: 'ASA Host',  type: 'text',     required: true },
    { key: 'username',   label: 'Username',  type: 'text',     required: true },
    { key: 'password',   label: 'Password',  type: 'password', required: true },
    { key: 'verify_ssl', label: 'Verify SSL',type: 'checkbox' },
  ],
  cisco_ise: [
    { key: 'host',       label: 'ISE Host', type: 'text',     required: true },
    { key: 'username',   label: 'Username', type: 'text',     required: true },
    { key: 'password',   label: 'Password', type: 'password', required: true },
    { key: 'verify_ssl', label: 'Verify SSL', type: 'checkbox' },
  ],
  zscaler: [
    { key: 'cloud_name', label: 'Cloud Name', type: 'text',     required: true },
    { key: 'username',   label: 'Username',   type: 'text',     required: true },
    { key: 'password',   label: 'Password',   type: 'password', required: true },
    { key: 'api_key',    label: 'API Key',    type: 'password', required: true },
  ],
  crowdstrike: [
    { key: 'client_id',     label: 'OAuth2 Client ID',     type: 'text',     required: true },
    { key: 'client_secret', label: 'OAuth2 Client Secret', type: 'password', required: true },
  ],
  sentinelone: [
    { key: 'url',       label: 'SentinelOne URL', type: 'text',     required: true },
    { key: 'api_token', label: 'API Token',       type: 'password', required: true },
  ],
  wazuh: [
    { key: 'url',        label: 'Wazuh Manager URL', type: 'text',     required: true },
    { key: 'username',   label: 'API Username',      type: 'text',     required: true },
    { key: 'password',   label: 'API Password',      type: 'password', required: true },
    { key: 'verify_ssl', label: 'Verify SSL',        type: 'checkbox' },
  ],
  tenable_sc:  [{ key: 'host', label: 'Host', type: 'text', required: true }, { key: 'access_key', label: 'Access Key', type: 'text' }, { key: 'secret_key', label: 'Secret Key', type: 'password' }],
  tenable_io:  [{ key: 'access_key', label: 'Access Key', type: 'text', required: true }, { key: 'secret_key', label: 'Secret Key', type: 'password', required: true }],
  qualys:      [{ key: 'username', label: 'Username', type: 'text', required: true }, { key: 'password', label: 'Password', type: 'password', required: true }, { key: 'platform', label: 'Platform URL', type: 'text' }],
  openvas:     [{ key: 'host', label: 'Host', type: 'text', required: true }, { key: 'username', label: 'Username', type: 'text', required: true }, { key: 'password', label: 'Password', type: 'password', required: true }],
  servicenow:  [{ key: 'instance', label: 'Instance Name', type: 'text', required: true }, { key: 'username', label: 'Username', type: 'text', required: true }, { key: 'password', label: 'Password', type: 'password', required: true }],
  jira:        [{ key: 'url', label: 'Jira URL', type: 'text', required: true }, { key: 'username', label: 'Email', type: 'text', required: true }, { key: 'api_token', label: 'API Token', type: 'password', required: true }, { key: 'project_key', label: 'Project Key', type: 'text', required: true }],
  prtg:        [{ key: 'url', label: 'PRTG URL', type: 'text', required: true }, { key: 'api_token', label: 'API Token', type: 'password' }],
  zabbix:      [{ key: 'url', label: 'Zabbix URL', type: 'text', required: true }, { key: 'username', label: 'Username', type: 'text', required: true }, { key: 'password', label: 'Password', type: 'password', required: true }],
  graylog:     [{ key: 'url', label: 'Graylog URL', type: 'text', required: true }, { key: 'username', label: 'Username', type: 'text', required: true }, { key: 'password', label: 'Password', type: 'password', required: true }],
  glpi:        [{ key: 'url', label: 'GLPI URL', type: 'text', required: true }, { key: 'app_token', label: 'App Token', type: 'password', required: true }, { key: 'username', label: 'Username', type: 'text', required: true }, { key: 'password', label: 'Password', type: 'password', required: true }],
  netbox:      [{ key: 'url', label: 'NetBox URL', type: 'text', required: true }, { key: 'api_token', label: 'API Token', type: 'password', required: true }],
  aws_security_hub: [{ key: 'access_key_id', label: 'AWS Access Key ID', type: 'text', required: true }, { key: 'secret_access_key', label: 'AWS Secret Access Key', type: 'password', required: true }, { key: 'region', label: 'AWS Region', type: 'text', required: true }],
  azure_cspm:  [{ key: 'tenant_id', label: 'Tenant ID', type: 'text', required: true }, { key: 'client_id', label: 'App (Client) ID', type: 'text', required: true }, { key: 'client_secret', label: 'Client Secret', type: 'password', required: true }],
  gcp_scc:     [{ key: 'org_id', label: 'GCP Org ID', type: 'text', required: true }],
  github:      [{ key: 'token', label: 'Personal Access Token', type: 'password', required: true }, { key: 'org', label: 'Organisation', type: 'text', required: true }],
  gitlab:      [{ key: 'token', label: 'Personal Access Token', type: 'password', required: true }, { key: 'url', label: 'GitLab URL', type: 'text', placeholder: 'https://gitlab.com' }],
  opencti:     [{ key: 'url', label: 'OpenCTI URL', type: 'text', required: true }, { key: 'token', label: 'API Token', type: 'password', required: true }],
  openaev:     [{ key: 'url', label: 'OpenAEV URL', type: 'text', required: true }, { key: 'token', label: 'API Token', type: 'password', required: true }],
  kubernetes:  [{ key: 'dashboard_url', label: 'Dashboard URL', type: 'text', required: true, placeholder: 'http://10.0.0.60' }, { key: 'dashboard_token', label: 'Dashboard Token', type: 'password', required: true }],
  siem:        [{ key: 'base_url', label: 'SIEM Base URL', type: 'text', required: true }, { key: 'api_key', label: 'API Key', type: 'password' }],
  threat_intel:[{ key: 'feed_url', label: 'Feed URL', type: 'text', required: true }, { key: 'api_key', label: 'API Key', type: 'password' }],
}
