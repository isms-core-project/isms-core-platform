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
import { MatDialogModule, MatDialog } from '@angular/material/dialog'
import { MatIconModule } from '@angular/material/icon'
import { MatChipsModule } from '@angular/material/chips'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatProgressBarModule } from '@angular/material/progress-bar'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatDividerModule } from '@angular/material/divider'
import { MatSliderModule } from '@angular/material/slider'
import { MatSnackBar, MatSnackBarModule } from '@angular/material/snack-bar'

import {
  RisksApiService,
  type RiskScenario,
  type RiskScenarioCreate,
  type RiskAcceptance,
  type HeatmapCell,
  type RiskSummary,
} from '../../api/risks-api.service'
import { ProjectService } from '../../core/services/project.service'
import { ThemeService } from '../../core/services/theme.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

// ── Colour helpers ────────────────────────────────────────────────────────────

function scoreColor(score: number): string {
  if (score <= 4)  return '#00c752'
  if (score <= 9)  return '#ff9800'
  if (score <= 16) return '#f44336'
  return '#c00000'
}

function levelColor(level: string): string {
  const m: Record<string, string> = {
    low:      '#00c752',
    medium:   '#ff9800',
    high:     '#f44336',
    critical: '#c00000',
  }
  return m[level] ?? '#9e9e9e'
}

const STATUS_COLOR: Record<string, string> = {
  open:         '#f44336',
  in_treatment: '#ff9800',
  closed:       '#00c752',
  accepted:     '#9e9e9e',
}

const TREATMENT_LABEL: Record<string, string> = {
  pending:  'Pending',
  accept:   'Accept',
  mitigate: 'Mitigate',
  transfer: 'Transfer',
  avoid:    'Avoid',
}

function fmtDate(d: string | null | undefined): string {
  if (!d) return '—'
  return new Date(d).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: '2-digit' })
}

// ── Component ─────────────────────────────────────────────────────────────────

@Component({
  selector: 'app-risk-register',
  standalone: true,
  imports: [
    FormsModule,
    MatCardModule, MatTableModule, MatButtonModule, MatFormFieldModule,
    MatInputModule, MatSelectModule, MatDialogModule, MatIconModule,
    MatChipsModule, MatTooltipModule, MatProgressBarModule, MatProgressSpinnerModule,
    MatDividerModule, MatSliderModule, MatSnackBarModule,
    PageHeaderComponent,
  ],
  template: `
<app-page-header
  title="Risk Register"
  [subtitle]="project.activeProject() ? (project.activeProject()!.name + ' · ISO 27001:2022 §6.1.2') : 'ISO 27001:2022 Clause 6.1.2 — identify, analyse, and treat information security risks'">
  <div actions>
    <button mat-flat-button color="primary"
      [disabled]="!project.activeProject()"
      [matTooltip]="!project.activeProject() ? 'Select a project first' : ''"
      (click)="openCreate()">
      <mat-icon>add</mat-icon>
      New Risk
    </button>
  </div>
</app-page-header>

@if (project.activeProject()) {
  <div class="alert alert-info alert-mb">
    Showing risks for project: <strong>{{ project.activeProject()!.name }}</strong>
  </div>
}

<!-- Summary row -->
@if (summaryQuery.isSuccess() && summaryQuery.data()) {
  @let s = summaryQuery.data()!;
  <div class="summary-row">
    @for (card of summaryCards(s); track card.label) {
      <div class="summary-card" [style.border-color]="card.color + '40'">
        <div class="sc-value" [style.color]="card.color">{{ card.value }}</div>
        <div class="sc-label">{{ card.label }}</div>
      </div>
    }
  </div>
}

<!-- Heatmap + Filters -->
<div class="top-row">
  <!-- Heatmap -->
  <mat-card class="heatmap-card">
    <mat-card-content>
      @if (heatmapQuery.isSuccess() && heatmapQuery.data()) {
        @let hm = heatmapQuery.data()!;
        <p class="heatmap-title">Risk Heatmap — open scenarios (probability × impact)</p>

        <div class="heatmap-wrap">
          <!-- Y-axis labels -->
          <div class="heatmap-y-labels">
            @for (l of hm.probability_labels.slice().reverse(); track $index) {
              <div class="axis-label">{{ l }}</div>
            }
          </div>

          <div>
            <!-- Grid (rows: high prob at top) -->
            <div class="heatmap-grid">
              @for (p of [5,4,3,2,1]; track p) {
                <div class="heatmap-row">
                  @for (i of [1,2,3,4,5]; track i) {
                    @let cell = getCell(hm.cells, p, i);
                    <div class="heatmap-cell"
                      [style.background]="cellBg(cell)"
                      [style.border-color]="cellBorder(cell)"
                      [matTooltip]="cell ? 'P' + p + '×I' + i + ': ' + cell.count + ' scenario' + (cell.count !== 1 ? 's' : '') : ''"
                      (click)="onHeatmapClick(cell)">
                      @if (cell && cell.count > 0) {
                        <span class="heatmap-count" [style.color]="cellCountColor(cell.score)">{{ cell.count }}</span>
                      }
                    </div>
                  }
                </div>
              }
            </div>
            <!-- X-axis labels -->
            <div class="heatmap-x-labels">
              @for (l of hm.impact_labels; track $index) {
                <div class="axis-label x">{{ l.split(' ')[0] }}</div>
              }
            </div>
            <div class="heatmap-axis-note">Y = Probability · X = Impact</div>
          </div>
        </div>
      } @else {
        <div class="spinner-row"><mat-spinner diameter="24" /></div>
      }
    </mat-card-content>
  </mat-card>

  <!-- Filters -->
  <div class="filters-col">
    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="filter-field">
      <mat-label>Level</mat-label>
      <mat-select [(ngModel)]="filterLevel" (ngModelChange)="filterLevel = $event">
        <mat-option value="">All</mat-option>
        @for (l of ['critical','high','medium','low']; track l) {
          <mat-option [value]="l">
            <span class="level-dot" [style.background]="levelColor(l)"></span>{{ l }}
          </mat-option>
        }
      </mat-select>
    </mat-form-field>

    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="filter-field">
      <mat-label>Treatment</mat-label>
      <mat-select [(ngModel)]="filterTreatment">
        <mat-option value="">All</mat-option>
        @for (e of treatmentEntries; track e.k) {
          <mat-option [value]="e.k">{{ e.v }}</mat-option>
        }
      </mat-select>
    </mat-form-field>

    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="filter-field">
      <mat-label>Status</mat-label>
      <mat-select [(ngModel)]="filterStatus">
        <mat-option value="">All</mat-option>
        <mat-option value="open">Open</mat-option>
        <mat-option value="in_treatment">In Treatment</mat-option>
        <mat-option value="accepted">Accepted</mat-option>
        <mat-option value="closed">Closed</mat-option>
      </mat-select>
    </mat-form-field>

    @if (filterLevel || filterTreatment || filterStatus) {
      <button mat-stroked-button (click)="clearFilters()">
        <mat-icon>filter_alt_off</mat-icon> Clear
      </button>
    }
  </div>
</div>

<!-- Table header -->
<div class="risk-table-header">
  @for (h of tableHeaders; track h) {
    <span class="th">{{ h }}</span>
  }
</div>

<!-- Rows -->
<div class="risk-table-body">
  @if (risksQuery.isLoading()) {
    @for (i of [0,1,2,3]; track i) {
      <div class="risk-row skeleton-row">
        <div class="skeleton skeleton-line"></div>
      </div>
    }
  } @else if (!risks().length) {
    <div class="empty-state">
      <mat-icon>warning_amber</mat-icon>
      <div>
        <p>No risk scenarios yet.</p>
        <p class="dim">Create your first risk to comply with ISO 27001:2022 Clause 6.1.2</p>
        <button mat-flat-button color="primary" class="btn-mt"
          [disabled]="!project.activeProject()"
          (click)="openCreate()">
          <mat-icon>add</mat-icon> New Risk
        </button>
      </div>
    </div>
  } @else {
    @for (risk of risks(); track risk.id) {
      <div class="risk-row">
        <!-- Name + threat -->
        <div class="risk-name-col">
          <span class="risk-name">{{ risk.name }}</span>
          @if (risk.threat_source) {
            <span class="dim-sm">{{ risk.threat_source }}</span>
          }
        </div>

        <!-- Inherent -->
        <div class="risk-score-col">
          <span class="dim-sm">P{{ risk.probability }}×I{{ risk.impact }}</span>
          <span class="chip" [style.background]="levelColor(risk.risk_level) + '18'" [style.color]="levelColor(risk.risk_level)" [style.border]="'1px solid ' + levelColor(risk.risk_level) + '40'">
            {{ risk.risk_level.toUpperCase() }}
          </span>
        </div>

        <!-- Residual -->
        <div class="risk-score-col">
          @if (risk.residual_level) {
            <span class="dim-sm">P{{ risk.residual_probability }}×I{{ risk.residual_impact }}</span>
            <span class="chip" [style.background]="levelColor(risk.residual_level) + '18'" [style.color]="levelColor(risk.residual_level)" [style.border]="'1px solid ' + levelColor(risk.residual_level) + '40'">
              {{ risk.residual_level.toUpperCase() }}
            </span>
          } @else {
            <span class="dim">—</span>
          }
        </div>

        <!-- Treatment -->
        <div class="risk-treatment-col">
          <span class="body-sm">{{ treatmentLabel(risk.treatment_status) }}</span>
        </div>

        <!-- Owner -->
        <div class="risk-owner-col">
          <span class="body-sm ellipsis">{{ risk.owner_name ?? '—' }}</span>
        </div>

        <!-- Target -->
        <div class="risk-date-col">
          <span class="dim-sm">{{ fmtDate(risk.target_date) }}</span>
        </div>

        <!-- Actions -->
        <div class="risk-actions-col">
          <div class="status-dot" [style.background]="STATUS_COLOR[risk.status] ?? '#9E9E9E'" [matTooltip]="risk.status.replace('_', ' ')"></div>
          <button mat-icon-button matTooltip="Record acceptance" [style.color]="risk.treatment_status === 'accept' ? '#00c752' : undefined"
            (click)="openAcceptance(risk)">
            <mat-icon class="icon-sm">how_to_reg</mat-icon>
          </button>
          <button mat-icon-button matTooltip="Edit" (click)="openEdit(risk)">
            <mat-icon class="icon-sm">edit</mat-icon>
          </button>
          <button mat-icon-button matTooltip="Delete" color="warn"
            (click)="deleteRisk(risk)">
            <mat-icon class="icon-sm">delete</mat-icon>
          </button>
        </div>
      </div>
    }
  }
</div>

<!-- ── Create / Edit dialog ──────────────────────────────────────────────────── -->
@if (dialogOpen()) {
  <div class="dialog-backdrop" (click)="dialogOpen.set(false)">
    <mat-card class="dialog-card" (click)="$event.stopPropagation()">
      <mat-card-header>
        <mat-card-title>{{ editingRisk() ? 'Edit Risk Scenario' : 'New Risk Scenario' }}</mat-card-title>
        <mat-card-subtitle>ISO 27001:2022 Clause 6.1.2 — Risk identification and assessment</mat-card-subtitle>
      </mat-card-header>
      <mat-card-content>
        @if (formError()) {
          <div class="alert alert-error">{{ formError() }}</div>
        }
        <div class="form-grid">
          <mat-form-field appearance="outline" class="full">
            <mat-label>Risk name *</mat-label>
            <input matInput [(ngModel)]="form.name" placeholder="e.g. Unauthorised access to customer data" />
          </mat-form-field>
          <mat-form-field appearance="outline" class="full">
            <mat-label>Description</mat-label>
            <textarea matInput [(ngModel)]="form.description" rows="2"></textarea>
          </mat-form-field>
          <mat-form-field appearance="outline">
            <mat-label>Threat source</mat-label>
            <input matInput [(ngModel)]="form.threat_source" placeholder="e.g. External attacker" />
          </mat-form-field>
          <mat-form-field appearance="outline">
            <mat-label>Threat event</mat-label>
            <input matInput [(ngModel)]="form.threat_event" placeholder="e.g. Phishing" />
          </mat-form-field>

          <!-- Risk sliders -->
          <div class="slider-box full">
            <p class="slider-title">Inherent Risk</p>
            <div class="slider-row">
              <label class="dim-sm">Probability: <strong>{{ form.probability }}</strong>/5</label>
              <mat-slider min="1" max="5" step="1" discrete>
                <input matSliderThumb [(ngModel)]="form.probability" />
              </mat-slider>
            </div>
            <div class="slider-row">
              <label class="dim-sm">Impact: <strong>{{ form.impact }}</strong>/5</label>
              <mat-slider min="1" max="5" step="1" discrete>
                <input matSliderThumb [(ngModel)]="form.impact" />
              </mat-slider>
            </div>
            <p class="score-preview" [style.color]="scoreColor(form.probability * form.impact)">
              Score: {{ form.probability * form.impact }} — {{ scoreLevelLabel(form.probability * form.impact) }}
            </p>
          </div>

          <mat-form-field appearance="outline">
            <mat-label>Treatment</mat-label>
            <mat-select [(ngModel)]="form.treatment_status">
              @for (e of treatmentEntries; track e.k) {
                <mat-option [value]="e.k">{{ e.v }}</mat-option>
              }
            </mat-select>
          </mat-form-field>
          <mat-form-field appearance="outline">
            <mat-label>Status</mat-label>
            <mat-select [(ngModel)]="form.status">
              <mat-option value="open">Open</mat-option>
              <mat-option value="in_treatment">In Treatment</mat-option>
              <mat-option value="accepted">Accepted</mat-option>
              <mat-option value="closed">Closed</mat-option>
            </mat-select>
          </mat-form-field>

          <mat-form-field appearance="outline" class="full">
            <mat-label>Treatment notes</mat-label>
            <textarea matInput [(ngModel)]="form.treatment_notes" rows="2"
              placeholder="Describe the treatment plan or acceptance rationale"></textarea>
          </mat-form-field>

          <mat-form-field appearance="outline" class="full">
            <mat-label>Target date</mat-label>
            <input matInput [(ngModel)]="form.target_date" placeholder="YYYY-MM-DD" />
            <mat-hint>Target date to close or complete treatment</mat-hint>
          </mat-form-field>
        </div>
      </mat-card-content>
      <mat-card-actions>
        <button mat-button (click)="dialogOpen.set(false)">Cancel</button>
        <button mat-flat-button color="primary"
          [disabled]="saveMut.isPending()"
          (click)="submitRisk()">
          {{ saveMut.isPending() ? 'Saving…' : (editingRisk() ? 'Save' : 'Create') }}
        </button>
      </mat-card-actions>
    </mat-card>
  </div>
}

<!-- ── Acceptance dialog ─────────────────────────────────────────────────────── -->
@if (acceptanceRisk()) {
  <div class="dialog-backdrop" (click)="acceptanceRisk.set(null)">
    <mat-card class="dialog-card" (click)="$event.stopPropagation()">
      <mat-card-header>
        <mat-card-title>Risk Acceptance</mat-card-title>
        <mat-card-subtitle>{{ acceptanceRisk()!.name }}</mat-card-subtitle>
      </mat-card-header>
      <mat-card-content>
        @if (acceptError()) { <div class="alert alert-error">{{ acceptError() }}</div> }

        <div class="form-grid">
          <mat-form-field appearance="outline" class="full">
            <mat-label>Justification *</mat-label>
            <textarea matInput [(ngModel)]="acceptJustification" rows="3"
              placeholder="Explain why the residual risk is acceptable and who approved it"></textarea>
          </mat-form-field>
          <mat-form-field appearance="outline" class="full">
            <mat-label>Expiry date</mat-label>
            <input matInput type="date" [(ngModel)]="acceptExpiry" />
            <mat-hint>Leave blank for permanent acceptance</mat-hint>
          </mat-form-field>
        </div>

        <button mat-stroked-button [disabled]="acceptMut.isPending()" (click)="submitAcceptance()">
          <mat-icon>how_to_reg</mat-icon>
          {{ acceptMut.isPending() ? 'Recording…' : 'Record Acceptance' }}
        </button>

        @if (acceptancesQuery.isSuccess() && acceptancesQuery.data()!.length > 0) {
          <div class="acceptance-history">
            <p class="history-title">Acceptance History</p>
            @for (a of acceptancesQuery.data()!; track a.id) {
              <div class="acceptance-item" [class.acceptance-active]="a.status === 'active'">
                <div class="accept-header">
                  <div>
                    <span class="body-sm">{{ a.approver_name }}</span>
                    <span class="dim-sm dim-sm--block">
                      {{ fmtDate(a.created_at) }}
                      @if (a.expiry_date) { · Expires {{ fmtDate(a.expiry_date) }} }
                    </span>
                  </div>
                  <div class="accept-status-row">
                    <span class="chip"
                      [style.background]="a.status === 'active' ? '#00c75218' : '#9E9E9E18'"
                      [style.color]="a.status === 'active' ? '#00c752' : '#9E9E9E'">
                      {{ a.status }}
                    </span>
                    @if (a.status === 'active') {
                      <button mat-icon-button matTooltip="Revoke" color="warn" class="btn-revoke"
                        (click)="revokeAcceptance(a)">
                        <mat-icon class="icon-xs">delete</mat-icon>
                      </button>
                    }
                  </div>
                </div>
                <p class="dim-sm accept-justification">{{ a.justification }}</p>
              </div>
            }
          </div>
        }
      </mat-card-content>
      <mat-card-actions>
        <button mat-button (click)="acceptanceRisk.set(null)">Close</button>
      </mat-card-actions>
    </mat-card>
  </div>
}
  `,
  styles: [`
    :host { display: block; padding: 24px; }

    .alert { padding: 10px 14px; border-radius: 6px; margin-top: 16px; margin-bottom: 12px; font-size: 0.85rem; }
    .alert-info  { background: color-mix(in srgb, var(--mat-sys-primary) 10%, transparent); color: var(--mat-sys-primary); border: 1px solid color-mix(in srgb, var(--mat-sys-primary) 25%, transparent); }
    .alert-error { background: rgba(192,0,0,0.12); color: #FFC7CE; border: 1px solid rgba(192,0,0,0.2); }

    .summary-row {
      display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 24px;
    }
    .summary-card {
      min-width: 72px; padding: 10px 14px;
      border: 1px solid; border-radius: 10px; text-align: center;
    }
    .sc-value { font-size: 1.2rem; font-weight: 700; line-height: 1; }
    .sc-label  { font-size: 0.65rem; color: var(--mat-sys-on-surface-variant); margin-top: 2px; }

    .top-row {
      display: grid; grid-template-columns: auto 1fr; gap: 24px;
      align-items: start; margin-bottom: 24px;
    }
    @media (max-width: 680px) { .top-row { grid-template-columns: 1fr; } }

    .heatmap-card { width: fit-content; }
    .heatmap-title { font-size: 0.7rem; color: var(--mat-sys-on-surface-variant); margin-bottom: 8px; }
    .heatmap-wrap { display: flex; gap: 6px; align-items: flex-end; }
    .heatmap-y-labels {
      display: flex; flex-direction: column; gap: 4px;
      padding-bottom: 24px;
    }
    .heatmap-grid { display: flex; flex-direction: column; gap: 4px; }
    .heatmap-row  { display: flex; gap: 4px; }
    .heatmap-cell {
      width: 36px; height: 36px; border-radius: 6px; border: 1px solid;
      display: flex; align-items: center; justify-content: center;
      cursor: pointer; transition: opacity 0.15s;
    }
    .heatmap-cell:hover { opacity: 0.75; }
    .heatmap-count { font-size: 0.7rem; font-weight: 700; }
    .heatmap-x-labels { display: flex; gap: 4px; margin-top: 4px; }
    .heatmap-axis-note { font-size: 0.58rem; color: var(--mat-sys-on-surface-variant); margin-top: 4px; }
    .axis-label { font-size: 0.55rem; color: var(--mat-sys-on-surface-variant); white-space: nowrap; }
    .axis-label.x { width: 36px; text-align: center; }

    .filters-col {
      display: flex; flex-direction: column; gap: 12px; padding-top: 8px; max-width: 300px;
    }
    .filter-field { width: 100%; }
    .level-dot {
      display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: 8px;
    }

    /* Table */
    .risk-table-header {
      display: grid;
      grid-template-columns: 1fr 90px 90px 100px 110px 80px 96px;
      gap: 12px; padding: 6px 16px;
      background: rgba(255,255,255,0.03);
      border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 8px 8px 0 0;
      border-bottom: none;
    }
    .th {
      font-size: 0.65rem; text-transform: uppercase;
      letter-spacing: 0.06em; color: var(--mat-sys-on-surface-variant); font-weight: 600;
    }
    .risk-table-body {
      border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 0 0 8px 8px; overflow: hidden;
    }
    .risk-row {
      display: grid;
      grid-template-columns: 1fr 90px 90px 100px 110px 80px 96px;
      gap: 12px; align-items: center;
      padding: 10px 16px;
      border-bottom: 1px solid var(--mat-sys-outline-variant);
    }
    .risk-row:last-child { border-bottom: none; }
    .risk-row:hover { background: rgba(255,255,255,0.02); }
    .skeleton-row { padding: 12px 16px; }

    .risk-name-col { display: flex; flex-direction: column; min-width: 0; }
    .risk-name { font-size: 0.82rem; font-weight: 500; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .risk-score-col { text-align: center; display: flex; flex-direction: column; align-items: center; gap: 3px; }
    .risk-treatment-col .body-sm { font-size: 0.78rem; color: var(--mat-sys-on-surface-variant); }
    .risk-owner-col { min-width: 0; }
    .risk-date-col {}
    .risk-actions-col { display: flex; align-items: center; gap: 2px; }

    .status-dot { width: 7px; height: 7px; border-radius: 50%; flex-shrink: 0; }

    .chip {
      display: inline-block; padding: 2px 7px; border-radius: 10px;
      font-size: 0.62rem; font-weight: 700; line-height: 1.6;
    }
    .dim     { font-size: 0.78rem; color: var(--mat-sys-on-surface-variant); }
    .dim-sm  { font-size: 0.67rem; color: var(--mat-sys-on-surface-variant); }
    .body-sm { font-size: 0.78rem; }
    .ellipsis { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; display: block; }

    .empty-state {
      display: flex; align-items: center; gap: 16px;
      padding: 48px 32px; color: var(--mat-sys-on-surface-variant);
      justify-content: center; text-align: center;
    }
    .empty-state p { margin: 4px 0; }

    .skeleton { background: rgba(255,255,255,0.06); }

    /* Dialog */
    .dialog-backdrop {
      position: fixed; inset: 0; background: rgba(0,0,0,0.5);
      display: flex; align-items: center; justify-content: center;
      z-index: 1000; padding: 24px;
    }
    .dialog-card { max-width: 540px; width: 100%; max-height: 90vh; overflow-y: auto; }
    .dialog-card mat-card-content { padding: 16px 16px 0; }
    .dialog-card mat-card-actions { padding: 12px 16px 16px; display: flex; justify-content: flex-end; gap: 8px; }

    .form-grid {
      display: grid; grid-template-columns: 1fr 1fr; gap: 12px 16px; padding-top: 8px;
    }
    .form-grid .full { grid-column: 1 / -1; }
    .form-grid mat-form-field { width: 100%; }

    .slider-box {
      border: 1px solid var(--mat-sys-outline-variant); border-radius: 8px; padding: 12px 16px;
    }
    .slider-title { font-size: 0.72rem; font-weight: 600; margin: 0 0 12px; }
    .slider-row { margin-bottom: 8px; }
    .score-preview { font-size: 0.8rem; font-weight: 600; margin: 8px 0 0; }

    /* Acceptance */
    .acceptance-history { margin-top: 20px; }
    .history-title {
      font-size: 0.7rem; font-weight: 600; text-transform: uppercase;
      letter-spacing: 0.08em; color: var(--mat-sys-on-surface-variant); margin: 0 0 10px;
    }
    .acceptance-item {
      padding: 10px 12px; border-radius: 6px; margin-bottom: 8px;
      border: 1px solid var(--mat-sys-outline-variant);
    }
    .acceptance-active { border-color: #00c75240; background: #00c75208; }
    .accept-header { display: flex; justify-content: space-between; align-items: flex-start; }

    .spinner-row { display: flex; justify-content: center; padding: 16px; }

    .alert-mb { margin-bottom: 16px; }
    .skeleton-line { width: 60%; height: 14px; border-radius: 3px; }
    .btn-mt { margin-top: 12px; }
    .dim-sm--block { display: block; }
    .accept-status-row { display: flex; align-items: center; gap: 6px; }
    .btn-revoke { width: 24px; height: 24px; }
    .icon-xs { font-size: 13px; width: 13px; height: 13px; }
    .accept-justification { margin: 4px 0 0; }
  `],
})
export class RiskRegisterComponent {
  readonly Math = Math
  readonly STATUS_COLOR = STATUS_COLOR

  project      = inject(ProjectService)
  private theme    = inject(ThemeService)
  private risksApi = inject(RisksApiService)
  private snackBar  = inject(MatSnackBar)
  private qc = injectQueryClient()

  cellBg(cell: HeatmapCell | undefined): string {
    if (!cell) return this.theme.isDark() ? '#ffffff10' : 'rgba(0,0,0,0.05)'
    const c = scoreColor(cell.score)
    return c + (cell.count > 0 ? (this.theme.isDark() ? '30' : '55') : (this.theme.isDark() ? '10' : '22'))
  }

  cellBorder(cell: HeatmapCell | undefined): string {
    if (!cell) return this.theme.isDark() ? '#ffffff20' : 'rgba(0,0,0,0.1)'
    const c = scoreColor(cell.score)
    return c + (cell.count > 0 ? (this.theme.isDark() ? '60' : '99') : (this.theme.isDark() ? '20' : '50'))
  }

  cellCountColor(score: number): string {
    return this.theme.isDark() ? scoreColor(score) : '#fff'
  }

  // ── Filters ────────────────────────────────────────────────────────────────
  filterLevel     = ''
  filterTreatment = ''
  filterStatus    = ''

  // ── Dialog state ───────────────────────────────────────────────────────────
  dialogOpen    = signal(false)
  editingRisk   = signal<RiskScenario | null>(null)
  formError     = signal<string | null>(null)
  form: RiskScenarioCreate = this.blankForm()

  // Acceptance dialog
  acceptanceRisk      = signal<RiskScenario | null>(null)
  acceptJustification = ''
  acceptExpiry        = ''
  acceptError         = signal<string | null>(null)

  // ── Queries ────────────────────────────────────────────────────────────────

  summaryQuery = injectQuery(() => ({
    queryKey: ['risk-summary', this.project.activeProjectId()] as const,
    queryFn: () => firstValueFrom(this.risksApi.summary({ project_id: this.project.activeProjectId()! })),
    enabled: !!this.project.activeProjectId(),
  }))

  risksQuery = injectQuery(() => ({
    queryKey: ['risks', this.filterLevel, this.filterTreatment, this.filterStatus, this.project.activeProjectId()] as const,
    queryFn: () => firstValueFrom(this.risksApi.list({
      risk_level:       this.filterLevel     || undefined,
      treatment_status: this.filterTreatment || undefined,
      status:           this.filterStatus    || undefined,
      project_id:       this.project.activeProjectId()!,
    })),
    enabled: !!this.project.activeProjectId(),
  }))

  heatmapQuery = injectQuery(() => ({
    queryKey: ['risk-heatmap', this.project.activeProjectId()] as const,
    queryFn: () => firstValueFrom(this.risksApi.heatmap({ project_id: this.project.activeProjectId()! })),
    enabled: !!this.project.activeProjectId(),
  }))

  acceptancesQuery = injectQuery(() => ({
    queryKey: ['acceptances', this.acceptanceRisk()?.id] as const,
    queryFn: () => firstValueFrom(this.risksApi.listAcceptances(this.acceptanceRisk()!.id)),
    enabled: !!this.acceptanceRisk(),
  }))

  // ── Mutations ──────────────────────────────────────────────────────────────

  saveMut = injectMutation(() => ({
    mutationFn: (payload: { body: RiskScenarioCreate; id?: string }) =>
      payload.id
        ? firstValueFrom(this.risksApi.update(payload.id, payload.body))
        : firstValueFrom(this.risksApi.create(payload.body)),
    onSuccess: () => {
      this.invalidateRisks()
      this.dialogOpen.set(false)
    },
    onError: () => this.formError.set('Failed to save risk scenario.'),
  }))

  deleteMut = injectMutation(() => ({
    mutationFn: (id: string) => firstValueFrom(this.risksApi.delete(id)),
    onSuccess: () => this.invalidateRisks(),
  }))

  acceptMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.risksApi.createAcceptance(
      this.acceptanceRisk()!.id,
      { justification: this.acceptJustification, expiry_date: this.acceptExpiry || undefined }
    )),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['acceptances', this.acceptanceRisk()?.id] })
      this.qc.invalidateQueries({ queryKey: ['risks'] })
      this.acceptJustification = ''
      this.acceptExpiry = ''
    },
    onError: () => this.acceptError.set('Failed to record acceptance.'),
  }))

  revokeMut = injectMutation(() => ({
    mutationFn: ({ riskId, acceptId }: { riskId: string; acceptId: string }) =>
      firstValueFrom(this.risksApi.revokeAcceptance(riskId, acceptId)),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['acceptances', this.acceptanceRisk()?.id] })
      this.qc.invalidateQueries({ queryKey: ['risks'] })
    },
  }))

  // ── Computed ───────────────────────────────────────────────────────────────

  risks = computed(() => this.risksQuery.data() ?? [])

  treatmentEntries = Object.entries(TREATMENT_LABEL).map(([k, v]) => ({ k, v }))

  tableHeaders = ['Risk', 'Inherent', 'Residual', 'Treatment', 'Owner', 'Target', '']

  summaryCards(s: RiskSummary) {
    return [
      { label: 'Total',        value: s.total,        color: 'var(--mat-sys-on-surface-variant)' },
      { label: 'Critical',     value: s.critical,     color: '#c00000' },
      { label: 'High',         value: s.high,         color: '#F44336' },
      { label: 'Medium',       value: s.medium,       color: '#FF9800' },
      { label: 'Low',          value: s.low,          color: '#00c752' },
      { label: 'Open',         value: s.open,         color: STATUS_COLOR['open'] },
      { label: 'In Treatment', value: s.in_treatment, color: STATUS_COLOR['in_treatment'] },
      { label: 'Closed',       value: s.closed,       color: STATUS_COLOR['closed'] },
    ]
  }

  // ── Methods ────────────────────────────────────────────────────────────────

  private invalidateRisks() {
    this.qc.invalidateQueries({ queryKey: ['risks'] })
    this.qc.invalidateQueries({ queryKey: ['risk-heatmap'] })
    this.qc.invalidateQueries({ queryKey: ['risk-summary'] })
  }

  private blankForm(): RiskScenarioCreate {
    return { name: '', probability: 1, impact: 1, treatment_status: 'pending', status: 'open' }
  }

  openCreate() {
    this.editingRisk.set(null)
    this.form = this.blankForm()
    this.formError.set(null)
    this.dialogOpen.set(true)
  }

  openEdit(risk: RiskScenario) {
    this.editingRisk.set(risk)
    this.form = {
      name: risk.name,
      description: risk.description ?? undefined,
      threat_source: risk.threat_source ?? undefined,
      threat_event: risk.threat_event ?? undefined,
      probability: risk.probability,
      impact: risk.impact,
      treatment_status: risk.treatment_status,
      treatment_notes: risk.treatment_notes ?? undefined,
      residual_probability: risk.residual_probability ?? undefined,
      residual_impact: risk.residual_impact ?? undefined,
      target_date: risk.target_date ?? undefined,
      status: risk.status,
    }
    this.formError.set(null)
    this.dialogOpen.set(true)
  }

  submitRisk() {
    if (!this.form.name.trim()) { this.formError.set('Name is required.'); return }
    this.saveMut.mutate({ body: this.form, id: this.editingRisk()?.id })
  }

  deleteRisk(risk: RiskScenario) {
    if (confirm(`Delete risk "${risk.name}"?`)) this.deleteMut.mutate(risk.id)
  }

  openAcceptance(risk: RiskScenario) {
    this.acceptJustification = ''
    this.acceptExpiry = ''
    this.acceptError.set(null)
    this.acceptanceRisk.set(risk)
  }

  submitAcceptance() {
    if (!this.acceptJustification.trim()) { this.acceptError.set('Justification is required.'); return }
    this.acceptError.set(null)
    this.acceptMut.mutate(undefined)
  }

  revokeAcceptance(a: RiskAcceptance) {
    const risk = this.acceptanceRisk()
    if (!risk) return
    if (confirm('Revoke this acceptance?')) this.revokeMut.mutate({ riskId: risk.id, acceptId: a.id })
  }

  clearFilters() {
    this.filterLevel = ''
    this.filterTreatment = ''
    this.filterStatus = ''
  }

  onHeatmapClick(cell: HeatmapCell | undefined) {
    if (!cell || cell.count === 0) return
    // Filter to show risks at that score
    this.filterLevel = cell.level
  }

  getCell(cells: HeatmapCell[], p: number, i: number): HeatmapCell | undefined {
    return cells.find(c => c.p === p && c.i === i)
  }

  scoreColor   = scoreColor
  levelColor   = levelColor
  treatmentLabel(t: string) { return TREATMENT_LABEL[t] ?? t }
  scoreLevelLabel(score: number) {
    if (score <= 4)  return 'Low'
    if (score <= 9)  return 'Medium'
    if (score <= 16) return 'High'
    return 'Critical'
  }
  fmtDate = fmtDate
}
