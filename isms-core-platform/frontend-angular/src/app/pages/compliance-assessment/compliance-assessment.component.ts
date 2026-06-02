import { Component, inject, signal, computed, input, effect } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'

import { injectQuery, injectMutation, injectQueryClient } from '@tanstack/angular-query-experimental'

import { MatCardModule } from '@angular/material/card'
import { MatTableModule } from '@angular/material/table'
import { MatButtonModule } from '@angular/material/button'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatProgressBarModule } from '@angular/material/progress-bar'
import { MatIconModule } from '@angular/material/icon'
import { MatChipsModule } from '@angular/material/chips'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatExpansionModule } from '@angular/material/expansion'
import { MatDividerModule } from '@angular/material/divider'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'

import {
  RegulatoryApiService,
  AssessmentSummary,
  FullAssessment,
  Requirement,
  ComplianceRating,
  RatingUpsert,
} from '../../api/regulatory-api.service'
import { ProjectsApiService } from '../../api/projects-api.service'
import { ProjectService } from '../../core/services/project.service'

// ── Framework metadata ────────────────────────────────────────────────────────

interface FrameworkMeta {
  name: string
  subtitle: string
  color: string
  description: string
  scoreLabels?: Record<number, string>
}

const DEFAULT_SCORE_LABELS: Record<number, string> = {
  0: 'Non-compliant', 1: 'Initial', 2: 'Developing', 3: 'Defined', 4: 'Optimised',
}
const SEAL_SCORE_LABELS: Record<number, string> = {
  0: 'No Sovereignty', 1: 'Jurisdictional Sovereignty', 2: 'Data Sovereignty', 3: 'Digital Resilience', 4: 'Full Digital Sovereignty',
}
const COBIT_SCORE_LABELS: Record<number, string> = {
  0: 'Incomplete', 1: 'Performed', 2: 'Managed', 3: 'Established', 4: 'Optimizing',
}
const CAF_SCORE_LABELS: Record<number, string> = {
  0: 'Not Achieved', 1: 'Not Achieved +', 2: 'Partially Achieved', 3: 'Partially Achieved +', 4: 'Achieved',
}

const FRAMEWORK_META: Record<string, FrameworkMeta> = {
  NIS2:                   { name: 'NIS2 Directive',                    subtitle: 'EU 2022/2555',        color: '#003399', description: 'Network and Information Security Directive 2 — Cybersecurity measures for essential and important entities.' },
  DORA:                   { name: 'DORA',                              subtitle: 'EU 2022/2554',        color: '#1565C0', description: 'Digital Operational Resilience Act — ICT risk management for financial entities.' },
  CIS_V8:                 { name: 'CIS Controls',                      subtitle: 'v8',                  color: '#BF360C', description: 'CIS Critical Security Controls v8 — 18 controls and 153 safeguards for enterprise cyber defence.' },
  BSI_IT_GRUNDSCHUTZ:     { name: 'BSI IT-Grundschutz',               subtitle: '2023',                color: '#C62828', description: 'BSI IT-Grundschutz Kompendium — 58 Bausteine across 10 layers.' },
  TISAX:                  { name: 'TISAX / VDA ISA',                   subtitle: 'v6.0',                color: '#37474F', description: 'TISAX — Trusted Information Security Assessment Exchange. VDA ISA 6.0 for the automotive supply chain.' },
  CH_NDSG:                { name: 'Swiss nDSG',                        subtitle: '2023',                color: '#B71C1C', description: 'Swiss Federal Act on Data Protection (nDSG) — in force 1 September 2023.' },
  CH_ISG:                 { name: 'Swiss ISG (SR 128)',                subtitle: 'State 1 Oct. 2025',   color: '#C62828', description: 'Swiss Federal Act on Information Security (ISG / LSI, SR 128) — in force 1 January 2024.' },
  EU_CRA:                 { name: 'EU Cyber Resilience Act',           subtitle: '2024/2847',           color: '#0D47A1', description: 'Mandatory cybersecurity requirements for products with digital elements.' },
  EU_AI_ACT:              { name: 'EU AI Act',                         subtitle: '2024/1689',           color: '#4A148C', description: 'EU AI Act — risk-based framework for artificial intelligence systems.' },
  NIST_AI_RMF:            { name: 'NIST AI RMF 1.0',                  subtitle: 'NIST AI 100-1',       color: '#4527A0', description: 'NIST AI Risk Management Framework 1.0 — voluntary framework for managing AI risks.' },
  UK_NIS:                 { name: 'UK NIS Regulations',                subtitle: 'SI 2018/506',         color: '#003399', description: 'The Network and Information Systems (NIS) Regulations 2018 — UK cybersecurity obligations.' },
  NCSC_CAF:               { name: 'NCSC Cyber Assessment Framework',   subtitle: 'CAF v4.0',            color: '#1D3557', description: 'NCSC CAF v4.0 — Outcome-based cybersecurity assessment framework for operators of essential services.', scoreLabels: CAF_SCORE_LABELS },
  UK_OPERATIONAL_RESILIENCE:{ name: 'UK Operational Resilience',       subtitle: 'FCA PS21/3 + PRA SS1/21', color: '#1565C0', description: 'UK Financial Sector Operational Resilience.' },
  CYFUN_BE:               { name: 'CyberFundamentals (CCN/CCB)',       subtitle: 'v2025-10-01',         color: '#1A237E', description: 'Belgian CyberFundamentals Framework 2025 — mandatory for OES under NIS2 transposition.' },
  BAFIN_BAIT:             { name: 'BaFin BAIT',                        subtitle: 'Rundschreiben 10/2021',color: '#B71C1C', description: 'BaFin BAIT — Bankaufsichtliche Anforderungen an die IT.' },
  CSSF_LU:                { name: 'CSSF Circulaire 20-750',            subtitle: 'ICT Risk — Luxembourg',color: '#004494', description: 'CSSF Circular 20-750 — ICT and security risk management for Luxembourg financial entities.' },
  ACN_IT:                 { name: 'ACN Cyber Risk Management',         subtitle: 'Linee Guida 2024',    color: '#006630', description: 'ACN guidelines for cyber risk management. Applies to NIS2 subjects under D.Lgs. 138/2024.' },
  EU_CLOUD_SOV:           { name: 'EU Cloud Sovereignty Framework',    subtitle: 'v1.2.1 — Oct. 2025',  color: '#01579B', description: 'European Commission Cloud Sovereignty Framework — SEAL-0 to SEAL-4.', scoreLabels: SEAL_SCORE_LABELS },
  COBIT_2019:             { name: 'COBIT 2019',                        subtitle: 'ISACA — EGIT Framework',color: '#7B1FA2', description: 'ISACA EGIT framework — 40 governance and management objectives.', scoreLabels: COBIT_SCORE_LABELS },
  FR_NIS2_RECYF:          { name: 'ReCyF v2.5',                        subtitle: 'NIS2 FR (ANSSI)',       color: '#002395', description: 'French NIS2 transposition reference framework (Référentiel Cyber Fondamental) — ANSSI.' },
  NIST_800_53_R5:         { name: 'NIST SP 800-53 Rev 5',              subtitle: 'NIST SP 800-53',        color: '#00838F', description: 'NIST Special Publication 800-53 Rev 5 — Security and privacy controls for federal information systems.' },
  CSA_CCM_V4_1:           { name: 'CSA Cloud Controls Matrix',         subtitle: 'CCM v4.1',              color: '#0277BD', description: 'Cloud Security Alliance Cloud Controls Matrix v4.1 — security controls for cloud computing.' },
  CSA_AICM_V1:            { name: 'CSA AI Controls Matrix',            subtitle: 'AICM v1',               color: '#6A1B9A', description: 'Cloud Security Alliance AI Controls Matrix v1 — security controls for AI systems.' },
}

const SLUG_TO_CODE: Record<string, string> = {
  'nis2':             'NIS2',
  'dora':             'DORA',
  'cis':              'CIS_V8',
  'bsi':              'BSI_IT_GRUNDSCHUTZ',
  'tisax':            'TISAX',
  'ndsg':             'CH_NDSG',
  'isg':              'CH_ISG',
  'cra':              'EU_CRA',
  'ai-act':           'EU_AI_ACT',
  'eu-cloud-sov':     'EU_CLOUD_SOV',
  'cobit':            'COBIT_2019',
  'nist-ai-rmf':      'NIST_AI_RMF',
  'ncsc-caf':         'NCSC_CAF',
  'fr-recyf':         'FR_NIS2_RECYF',
  'uk-nis':           'UK_NIS',
  'uk-op-resilience': 'UK_OPERATIONAL_RESILIENCE',
  'bafin-bait':       'BAFIN_BAIT',
  'cyfun-be':         'CYFUN_BE',
  'cssf-lu':          'CSSF_LU',
  'acn-it':           'ACN_IT',
  'nist-800-53':      'NIST_800_53_R5',
  'csa-ccm':          'CSA_CCM_V4_1',
  'csa-aicm':         'CSA_AICM_V1',
}

function resolveMeta(frameworkCode: string): FrameworkMeta {
  return FRAMEWORK_META[frameworkCode] ?? { name: frameworkCode, subtitle: '', color: '#1976d2', description: '' }
}

function resolveScoreLabels(frameworkCode: string): Record<number, string> {
  return FRAMEWORK_META[frameworkCode]?.scoreLabels ?? DEFAULT_SCORE_LABELS
}

// ── Status config ─────────────────────────────────────────────────────────────

interface StatusCfg { label: string; color: string; icon: string }

const STATUS_CONFIG: Record<string, StatusCfg> = {
  not_assessed:   { label: 'Not Assessed', color: '#9e9e9e', icon: 'radio_button_unchecked' },
  not_applicable: { label: 'N/A',          color: '#607d8b', icon: 'remove_circle_outline' },
  non_compliant:  { label: 'Non-Compliant',color: '#f44336', icon: 'cancel' },
  partial:        { label: 'Partial',      color: '#FF9800', icon: 'pause_circle' },
  compliant:      { label: 'Compliant',    color: '#00c752', icon: 'check_circle' },
}

const SCORE_COLORS: Record<number, string> = {
  0: '#f44336', 1: '#FF9800', 2: '#FFC107', 3: '#8BC34A', 4: '#4CAF50',
}

// ── Grouping ──────────────────────────────────────────────────────────────────

interface GroupedReq {
  groupId: string
  groupTitle: string
  requirements: Requirement[]
}

function groupRequirements(reqs: Requirement[], frameworkCode: string): GroupedReq[] {
  if (frameworkCode === 'EU_CLOUD_SOV') {
    return [{ groupId: 'all', groupTitle: 'Cloud Sovereignty Objectives — SOV-1 to SOV-8', requirements: reqs }]
  }
  const groupedFrameworks = ['DORA', 'CIS_V8', 'BSI_IT_GRUNDSCHUTZ', 'COBIT_2019', 'NIST_AI_RMF', 'NCSC_CAF']
  if (groupedFrameworks.includes(frameworkCode)) {
    const map = new Map<string, GroupedReq>()
    for (const r of reqs) {
      const gid    = r.group_id ?? 'Other'
      const gtitle = r.group_title ?? 'Other'
      if (!map.has(gid)) map.set(gid, { groupId: gid, groupTitle: gtitle, requirements: [] })
      map.get(gid)!.requirements.push(r)
    }
    return Array.from(map.values())
  }
  // NIS2 default — split by article prefix
  const measures: Requirement[]  = []
  const reporting: Requirement[] = []
  for (const r of reqs) {
    if (r.control_id.startsWith('Art. 23')) reporting.push(r)
    else measures.push(r)
  }
  const groups: GroupedReq[] = [
    { groupId: 'Art21', groupTitle: 'Security Measures — Article 21(2)', requirements: measures },
    { groupId: 'Art23', groupTitle: 'Reporting Obligations — Article 23', requirements: reporting },
  ]
  return groups.filter(g => g.requirements.length > 0)
}

// ── Helpers ───────────────────────────────────────────────────────────────────

function fmtDate(d: string): string {
  return new Date(d).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' })
}

// ─── Component ────────────────────────────────────────────────────────────────

@Component({
  selector: 'app-compliance-assessment',
  standalone: true,
  imports: [
    FormsModule,
    MatCardModule, MatTableModule, MatButtonModule,
    MatFormFieldModule, MatInputModule, MatSelectModule,
    MatProgressBarModule, MatIconModule, MatChipsModule,
    MatTooltipModule, MatExpansionModule, MatDividerModule, MatProgressSpinnerModule,
  ],
  template: `
    @if (selectedId()) {
    <!-- ── Detail view ────────────────────────────────────────────────── -->
    @if (fullQuery.isLoading()) {
      <mat-progress-bar mode="indeterminate" class="detail-loading-bar" />
    } @else if (fullQuery.isError()) {
      <div class="alert alert-error">Failed to load assessment.</div>
    } @else if (fullQuery.data()) {
      <div class="detail-header">
        <button mat-icon-button (click)="selectedId.set(null)">
          <mat-icon>arrow_back</mat-icon>
        </button>
        <div class="detail-header-content">
          @if (editingMeta()) {
            <div class="meta-edit-form">
              <mat-form-field appearance="outline" class="meta-name-field">
                <mat-label>Name</mat-label>
                <input matInput [(ngModel)]="metaName" />
              </mat-form-field>
              <div class="meta-edit-row">
                <mat-form-field appearance="outline" class="meta-org-field">
                  <mat-label>Organisation</mat-label>
                  <input matInput [(ngModel)]="metaOrg" />
                </mat-form-field>
                <mat-form-field appearance="outline" class="meta-assessor-field">
                  <mat-label>Assessor</mat-label>
                  <input matInput [(ngModel)]="metaAssessor" />
                </mat-form-field>
                <mat-form-field appearance="outline" class="meta-scope-field">
                  <mat-label>Scope</mat-label>
                  <input matInput [(ngModel)]="metaScope" />
                </mat-form-field>
              </div>
              <div class="meta-edit-actions">
                <button mat-flat-button color="primary" [disabled]="!metaName || updateMutation.isPending()" (click)="saveMeta()">Save</button>
                <button mat-button (click)="editingMeta.set(false)">Cancel</button>
              </div>
            </div>
          } @else {
            <div class="detail-name-row">
              <div>
                <h2 class="detail-title">{{ fullQuery.data()!.assessment.name }}</h2>
                @if (fullQuery.data()!.assessment.organisation || fullQuery.data()!.assessment.assessor) {
                  <p class="detail-org">
                    {{ [fullQuery.data()!.assessment.organisation, fullQuery.data()!.assessment.assessor ? 'Assessor: ' + fullQuery.data()!.assessment.assessor : null].join(' · ') }}
                  </p>
                }
              </div>
              <button mat-icon-button (click)="startEdit()">
                <mat-icon class="icon-sm">edit</mat-icon>
              </button>
            </div>
          }
        </div>
        <div class="detail-status-select">
          <mat-form-field appearance="outline" class="status-select-field">
            <mat-label>Status</mat-label>
            <mat-select [ngModel]="fullQuery.data()!.assessment.status"
              (ngModelChange)="updateMutation.mutate({status: $event})">
              <mat-option value="draft">Draft</mat-option>
              <mat-option value="in_progress">In Progress</mat-option>
              <mat-option value="complete">Complete</mat-option>
            </mat-select>
          </mat-form-field>
        </div>
      </div>

      <!-- KPI strip -->
      <div class="kpi-strip">
        @for (kpi of detailKpis(); track kpi.label) {
          <div class="kpi-card" [style.border-top]="'3px solid ' + kpi.color">
            <span class="kpi-label">{{ kpi.label }}</span>
            <span class="kpi-big" [style.color]="kpi.color">{{ kpi.value }}</span>
            @if (kpi.sub) { <span class="kpi-sub">{{ kpi.sub }}</span> }
          </div>
        }
      </div>

      <!-- Progress bar -->
      <mat-progress-bar mode="determinate" [value]="detailProgress()"
        class="detail-progress-bar"
        [style.--mat-progress-bar-active-indicator-color]="meta().color" />

      <!-- Requirement groups -->
      @for (group of groups(); track group.groupId) {
        <div class="req-group">
          <div class="req-group-header" (click)="toggleGroup(group.groupId)">
            <mat-icon class="icon-md">
              {{ expandedGroups().has(group.groupId) ? 'expand_less' : 'expand_more' }}
            </mat-icon>
            <span class="group-bar" [style.background]="meta().color"></span>
            <span class="group-title" [style.color]="meta().color">{{ group.groupTitle }}</span>
            <span class="group-count">{{ group.requirements.length }} items</span>
            @if (groupAvgScore(group) !== null) {
              <span class="group-avg"
                [style.background]="scoreColor(Math.round(groupAvgScore(group)!)) + '22'"
                [style.color]="scoreColor(Math.round(groupAvgScore(group)!))">
                Avg: {{ groupAvgScore(group)!.toFixed(1) }} — {{ scoreLabels()[Math.round(groupAvgScore(group)!)] }}
              </span>
            }
          </div>

          @if (expandedGroups().has(group.groupId)) {
            <div class="req-table-wrap">
              <table class="req-table">
                <thead>
                  <tr>
                    <th class="col-code">Code</th>
                    <th>Requirement</th>
                    <th class="col-score">Current Score</th>
                    <th class="col-score">Target Score</th>
                    <th class="col-status">Status</th>
                    <th class="col-notes">Notes</th>
                  </tr>
                </thead>
                <tbody>
                  @for (req of group.requirements; track req.id) {
                    <tr class="req-row">
                      <td>
                        <span class="req-code" [matTooltip]="req.description ?? ''" matTooltipPosition="right">
                          {{ req.control_id }}
                        </span>
                      </td>
                      <td>
                        <div class="req-title-cell">
                          <span class="req-title">{{ req.title }}</span>
                          @if (req.description) {
                            <button mat-icon-button class="expand-btn" (click)="toggleReq(req.id)">
                              <mat-icon class="icon-sm">
                                {{ expandedReqs().has(req.id) ? 'expand_less' : 'expand_more' }}
                              </mat-icon>
                            </button>
                          }
                          @if (expandedReqs().has(req.id) && req.description) {
                            <p class="req-desc">{{ req.description }}</p>
                          }
                        </div>
                      </td>
                      <td>
                        <mat-form-field appearance="outline" class="score-field">
                          <mat-select [ngModel]="getCurrentScore(req.id)" (ngModelChange)="setCurrentScore(req.id, $event)">
                            <mat-option value="">Not set</mat-option>
                            @for (s of SCORES; track s) {
                              <mat-option [value]="s">
                                <span class="score-dot" [style.background]="scoreColor(s)"></span>
                                {{ s }} — {{ scoreLabels()[s] }}
                              </mat-option>
                            }
                          </mat-select>
                        </mat-form-field>
                      </td>
                      <td>
                        <mat-form-field appearance="outline" class="score-field">
                          <mat-select [ngModel]="getTargetScore(req.id)" (ngModelChange)="setTargetScore(req.id, $event)">
                            <mat-option value="">Not set</mat-option>
                            @for (s of SCORES; track s) {
                              <mat-option [value]="s">
                                <span class="score-dot" [style.background]="scoreColor(s)"></span>
                                {{ s }} — {{ scoreLabels()[s] }}
                              </mat-option>
                            }
                          </mat-select>
                        </mat-form-field>
                      </td>
                      <td>
                        <mat-form-field appearance="outline" class="status-field">
                          <mat-select [ngModel]="getRatingStatus(req.id)" (ngModelChange)="setRatingStatus(req.id, $event)">
                            @for (entry of STATUS_ENTRIES; track entry.key) {
                              <mat-option [value]="entry.key">
                                <mat-icon class="icon-sm status-opt-icon"
                                  [style.color]="entry.cfg.color">{{ entry.cfg.icon }}</mat-icon>
                                {{ entry.cfg.label }}
                              </mat-option>
                            }
                          </mat-select>
                        </mat-form-field>
                      </td>
                      <td>
                        <textarea class="notes-input"
                          [value]="getNotes(req.id)"
                          (blur)="setNotes(req.id, $any($event.target).value)"
                          placeholder="Notes…"
                          rows="2"></textarea>
                      </td>
                    </tr>
                  }
                </tbody>
              </table>
            </div>
          }
        </div>
      }
    }

    } @else {
    <!-- ── List view ──────────────────────────────────────────────────── -->
    <div class="page-header">
      <div class="header-left">
        <div>
          <div class="title-row">
            <h1 class="page-title">{{ meta().name }}</h1>
            <span class="framework-chip" [style.background]="meta().color + '22'" [style.color]="meta().color">
              {{ meta().subtitle }}
            </span>
          </div>
          <p class="page-subtitle">{{ meta().description }}</p>
        </div>
      </div>
      <div class="header-right">
        <mat-form-field appearance="outline" subscriptSizing="dynamic" class="proj-select-field">
          <mat-label>Project</mat-label>
          <mat-select [(ngModel)]="selectedProjectId">
            @if (projects.isPending()) {
              <mat-option disabled>Loading…</mat-option>
            }
            @for (p of projects.data() ?? []; track p.id) {
              <mat-option [value]="p.id">{{ p.name }}</mat-option>
            }
          </mat-select>
        </mat-form-field>
        <button mat-flat-button [style.background]="meta().color" class="btn-white-text"
          [disabled]="!selectedProjectId"
          (click)="showCreate.set(true)">
          <mat-icon>add</mat-icon> New Assessment
        </button>
      </div>
    </div>

    <mat-divider class="section-divider" />

    @if (selectedProjectId) {
    @if (listQuery.isLoading()) {
      <mat-progress-bar mode="indeterminate" />
    } @else if (listQuery.isError()) {
      <div class="alert alert-error">Failed to load assessments.</div>
    } @else if (assessments().length === 0) {
      <div class="empty-state">
        <p class="empty-title">No assessments yet</p>
        <p class="empty-text">Create your first {{ meta().name }} assessment to get started.</p>
        <button mat-stroked-button [disabled]="!selectedProjectId" (click)="showCreate.set(true)">
          <mat-icon>add</mat-icon> New Assessment
        </button>
      </div>
    } @else {
      <div class="card-grid">
        @for (a of assessments(); track a.id) {
          <div class="assessment-card" (click)="selectedId.set(a.id)"
            [style.--fw-color]="meta().color">
            <div class="card-top">
              <div>
                <p class="card-name">{{ a.name }}</p>
                @if (a.organisation) {
                  <p class="card-org">{{ a.organisation }}</p>
                }
              </div>
              <div class="card-top-right">
                <span class="status-badge">{{ a.status.replace('_', ' ') }}</span>
                <button mat-icon-button class="del-btn"
                  (click)="$event.stopPropagation(); deleteId.set(a.id)">
                  <mat-icon class="icon-sm">delete_outline</mat-icon>
                </button>
              </div>
            </div>

            <div class="card-kpis">
              <div class="kpi">
                <span class="kpi-label">Current Score</span>
                <span class="kpi-value"
                  [style.color]="a.avg_current_score !== null ? scoreColor(Math.round(a.avg_current_score)) : '#9e9e9e'">
                  {{ a.avg_current_score !== null ? a.avg_current_score.toFixed(1) : '—' }}
                </span>
              </div>
              <div class="kpi">
                <span class="kpi-label">Compliant</span>
                <span class="kpi-value kpi-compliant">{{ a.compliant_count }} / {{ a.total_requirements }}</span>
              </div>
              <div class="kpi">
                <span class="kpi-label">Gaps</span>
                <span class="kpi-value"
                  [style.color]="(a.non_compliant_count + a.partial_count) > 0 ? '#f44336' : '#9e9e9e'">
                  {{ a.non_compliant_count + a.partial_count }}
                </span>
              </div>
            </div>

            <div class="progress-section">
              <div class="progress-header">
                <span class="kpi-label">Progress</span>
                <span class="kpi-label">{{ progressPct(a) }}%</span>
              </div>
              <mat-progress-bar mode="determinate" [value]="progressPct(a)"
                [style.--mat-progress-bar-active-indicator-color]="meta().color" />
            </div>

            @if (a.assessor) {
              <p class="card-assessor">Assessor: {{ a.assessor }}</p>
            }
          </div>
        }
      </div>
    }
    } <!-- end @if activeProject list section -->

    } <!-- end @else (list view) -->

    <!-- ── Create dialog ──────────────────────────────────────────────── -->
    @if (showCreate()) {
      <div class="modal-backdrop" (click)="showCreate.set(false)">
        <div class="modal" (click)="$event.stopPropagation()">
          <div class="modal-header">
            <h2 class="modal-title">New {{ meta().name }} Assessment</h2>
            <button mat-icon-button (click)="showCreate.set(false)"><mat-icon>close</mat-icon></button>
          </div>
          <div class="modal-body">
            @if (createMutation.isError()) {
              <div class="alert alert-error">Failed to create assessment.</div>
            }
            <mat-form-field appearance="outline" class="full-width modal-field">
              <mat-label>Assessment Name</mat-label>
              <input matInput [(ngModel)]="createName" required />
            </mat-form-field>
            <mat-form-field appearance="outline" class="full-width modal-field">
              <mat-label>Organisation</mat-label>
              <input matInput [(ngModel)]="createOrg" />
            </mat-form-field>
            <mat-form-field appearance="outline" class="full-width modal-field">
              <mat-label>Assessor</mat-label>
              <input matInput [(ngModel)]="createAssessor" />
            </mat-form-field>
            <mat-form-field appearance="outline" class="full-width">
              <mat-label>Scope</mat-label>
              <textarea matInput [(ngModel)]="createScope" rows="2"></textarea>
            </mat-form-field>
          </div>
          <div class="modal-footer">
            <button mat-button (click)="showCreate.set(false)">Cancel</button>
            <button mat-flat-button color="primary"
              [disabled]="!createName || createMutation.isPending()"
              (click)="submitCreate()">
              {{ createMutation.isPending() ? 'Creating…' : 'Create' }}
            </button>
          </div>
        </div>
      </div>
    }

    <!-- ── Delete confirm ─────────────────────────────────────────────── -->
    @if (deleteId()) {
      <div class="modal-backdrop" (click)="deleteId.set(null)">
        <div class="modal modal-sm" (click)="$event.stopPropagation()">
          <div class="modal-header">
            <h2 class="modal-title">Delete Assessment</h2>
            <button mat-icon-button (click)="deleteId.set(null)"><mat-icon>close</mat-icon></button>
          </div>
          <div class="modal-body">
            <p>This will permanently delete the assessment and all ratings. This cannot be undone.</p>
          </div>
          <div class="modal-footer">
            <button mat-button (click)="deleteId.set(null)">Cancel</button>
            <button mat-flat-button color="warn"
              [disabled]="deleteMutation.isPending()"
              (click)="submitDelete()">
              Delete
            </button>
          </div>
        </div>
      </div>
    }
  `,
  styles: [`
    /* Layout */
    .page-header  { display:flex; align-items:flex-start; justify-content:space-between; margin-bottom:16px; gap:16px; flex-wrap:wrap; }
    .header-left  { flex:1; }
    .title-row    { display:flex; align-items:center; gap:10px; flex-wrap:wrap; }
    .page-title   { margin:0; font-size:1.75rem; font-weight:700; line-height:1.2; }
    .page-subtitle{ margin:4px 0 0; color:var(--mat-sys-on-surface-variant,#666); font-size:.875rem; max-width:600px; }
    .framework-chip { font-size:.72rem; font-weight:600; padding:2px 10px; border-radius:10px; }

    .header-right { display:flex; align-items:center; gap:12px; flex-shrink:0; }
    .proj-select-field { min-width:200px; }

    /* Alerts */
    .alert { padding:10px 14px; border-radius:6px; font-size:.85rem; margin-bottom:12px; }
    .alert-error   { background:rgba(244,67,54,.1);  color:#c62828; border:1px solid rgba(244,67,54,.3); }
    .alert-success { background:rgba(76,175,80,.1);  color:#2e7d32; border:1px solid rgba(76,175,80,.3); }
    .alert-warn    { background:rgba(255,152,0,.1);  color:#e65100; border:1px solid rgba(255,152,0,.3); }
    .alert-link    { color:inherit; font-weight:600; margin-left:8px; }

    /* Empty state */
    .empty-state { text-align:center; padding:64px 0; }
    .empty-title { font-size:1.1rem; color:#9e9e9e; margin:0 0 8px; font-weight:600; }
    .empty-text  { color:#9e9e9e; margin:0 0 24px; }

    /* Assessment cards */
    .card-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(340px,1fr)); gap:16px; }
    .assessment-card {
      padding:20px; border:1px solid var(--mat-divider-color,rgba(0,0,0,.12)); border-radius:10px;
      cursor:pointer; transition:border-color .15s, background .15s;
    }
    .assessment-card:hover { border-color:var(--fw-color,#1976d2); background:color-mix(in srgb, var(--fw-color,#1976d2) 4%, transparent); }
    .card-top  { display:flex; align-items:flex-start; justify-content:space-between; margin-bottom:12px; }
    .card-name { margin:0; font-weight:600; font-size:1rem; }
    .card-org  { margin:2px 0 0; font-size:.8rem; color:#9e9e9e; }
    .card-top-right { display:flex; align-items:center; gap:6px; }
    .status-badge { font-size:.65rem; padding:2px 8px; border-radius:8px; background:rgba(0,0,0,.06); text-transform:capitalize; }
    .del-btn { width:24px; height:24px; line-height:24px; color:#9e9e9e; }
    .del-btn:hover { color:#f44336; }
    .card-kpis { display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px; margin-bottom:12px; }
    .kpi { display:flex; flex-direction:column; gap:2px; }
    .kpi-label { font-size:.72rem; color:var(--mat-sys-on-surface-variant); }
    .kpi-value { font-size:.95rem; font-weight:700; }
    .progress-section { margin-bottom:8px; }
    .progress-header  { display:flex; justify-content:space-between; margin-bottom:4px; }
    .card-assessor { margin:8px 0 0; font-size:.75rem; color:var(--mat-sys-on-surface-variant); }

    /* Detail view */
    .detail-header { display:flex; align-items:flex-start; gap:12px; margin-bottom:20px; }
    .detail-header-content { flex:1; }
    .detail-name-row { display:flex; align-items:flex-start; gap:6px; }
    .detail-title { margin:0; font-size:1.4rem; font-weight:700; }
    .detail-org   { margin:2px 0 0; font-size:.8rem; color:#9e9e9e; }
    .detail-status-select { flex-shrink:0; padding-top:4px; }
    .meta-edit-form  { display:flex; flex-direction:column; gap:8px; }
    .meta-edit-row   { display:flex; gap:12px; flex-wrap:wrap; }
    .meta-edit-actions { display:flex; gap:8px; }

    /* KPI strip */
    .kpi-strip { display:grid; grid-template-columns:repeat(5,1fr); gap:12px; margin-bottom:20px; }
    @media(max-width:700px){ .kpi-strip { grid-template-columns:repeat(2,1fr); } }
    .kpi-card   { padding:12px; border:1px solid var(--mat-divider-color,rgba(0,0,0,.12)); border-radius:8px; display:flex; flex-direction:column; gap:2px; }
    .kpi-big    { font-size:1.3rem; font-weight:700; line-height:1.2; }
    .kpi-sub    { font-size:.72rem; color:var(--mat-sys-on-surface-variant); }

    /* Requirement groups */
    .req-group { margin-bottom:24px; }
    .req-group-header {
      display:flex; align-items:center; gap:10px; margin-bottom:12px;
      cursor:pointer; user-select:none;
    }
    .group-bar   { width:4px; height:14px; border-radius:2px; flex-shrink:0; }
    .group-title { font-size:.9rem; font-weight:700; }
    .group-count { font-size:.72rem; padding:1px 6px; background:rgba(0,0,0,.06); border-radius:6px; }
    .group-avg   { font-size:.68rem; padding:1px 8px; border-radius:8px; font-weight:600; }

    /* Requirement table */
    .req-table-wrap { overflow:auto; border:1px solid var(--mat-divider-color,rgba(0,0,0,.12)); border-radius:8px; }
    .req-table { width:100%; border-collapse:collapse; font-size:.8rem; }
    .req-table th { padding:8px 10px; font-weight:600; text-align:left; background:rgba(0,0,0,.02); border-bottom:1px solid var(--mat-divider-color,rgba(0,0,0,.12)); white-space:nowrap; }
    .req-table td { padding:6px 10px; border-bottom:1px solid var(--mat-divider-color,rgba(0,0,0,.06)); vertical-align:top; }
    .req-row:last-child td { border-bottom:none; }
    .req-row:hover { background:rgba(0,0,0,.02); }
    .req-code  { font-family:monospace; font-size:.78rem; color:#1976d2; cursor:help; }
    .req-title-cell { display:flex; flex-wrap:wrap; align-items:flex-start; gap:4px; }
    .req-title { line-height:1.4; }
    .req-desc  { margin:4px 0 0; font-size:.75rem; color:#9e9e9e; line-height:1.5; width:100%; }
    .expand-btn { width:20px; height:20px; line-height:20px; flex-shrink:0; }

    /* Score / status fields */
    .score-field  { width:100%; font-size:.75rem; }
    .score-field .mat-mdc-text-field-wrapper { padding:0 6px; }
    .score-field .mat-mdc-select { font-size:.75rem; }
    .status-field { width:100%; font-size:.75rem; }
    .status-field .mat-mdc-select { font-size:.75rem; }
    .score-dot  { display:inline-block; width:8px; height:8px; border-radius:50%; margin-right:4px; vertical-align:middle; }

    /* Notes textarea */
    .notes-input {
      width:100%; resize:vertical; font-size:.75rem; padding:4px 6px;
      border:1px solid var(--mat-divider-color,rgba(0,0,0,.2));
      border-radius:4px; background:transparent; color:inherit;
      font-family:inherit; line-height:1.4;
      box-sizing:border-box;
    }
    .notes-input:focus { outline:none; border-color:#1976d2; }

    /* Chip row (controls) */
    .ctrl-chip   { font-size:.62rem; padding:1px 5px; border-radius:4px; border:1px solid currentColor; opacity:.75; }

    /* Modal */
    .modal-backdrop { position:fixed; inset:0; background:rgba(0,0,0,.5); display:flex; align-items:center; justify-content:center; z-index:1000; }
    .modal { background:var(--mat-sys-surface,#fff); border-radius:10px; width:100%; max-width:540px; margin:16px; max-height:90vh; display:flex; flex-direction:column; box-shadow:0 8px 32px rgba(0,0,0,.3); }
    .modal-sm { max-width:400px; }
    .modal-header { display:flex; align-items:center; justify-content:space-between; padding:20px 24px 0; }
    .modal-title  { margin:0; font-size:1.2rem; font-weight:700; }
    .modal-body   { padding:16px 24px; overflow-y:auto; flex:1; }
    .modal-footer { padding:12px 24px; display:flex; justify-content:flex-end; gap:8px; border-top:1px solid var(--mat-divider-color,rgba(0,0,0,.12)); }
    .full-width   { width:100%; }
    .modal-field  { margin-bottom:8px; }

    /* Misc extracted */
    .detail-loading-bar { margin-top:16px; }
    .detail-progress-bar { height:5px; margin-bottom:24px; border-radius:3px; }
    .meta-name-field     { max-width:400px; }
    .meta-org-field      { width:220px; }
    .meta-assessor-field { width:180px; }
    .meta-scope-field    { width:280px; }
    .status-select-field { width:140px; }
    .section-divider     { margin:16px 0; }
    .btn-white-text      { color:#fff; }
    .kpi-compliant       { color: var(--compliant-count-color); }
    .status-opt-icon     { vertical-align:middle; margin-right:4px; }
    .col-code   { width:110px; }
    .col-score  { width:160px; }
    .col-status { width:150px; }
    .col-notes  { width:210px; }
  `],
})
export class ComplianceAssessmentComponent {
  private api          = inject(RegulatoryApiService)
  private projectsApi  = inject(ProjectsApiService)
  private projectSvc   = inject(ProjectService)
  private queryClient  = injectQueryClient()

  // ── Framework code from route (reactive — withComponentInputBinding updates on navigation) ───
  protected readonly _slug     = input('', { alias: 'frameworkCode' })
  readonly frameworkCode     = computed(() => {
    const slug = this._slug()
    return SLUG_TO_CODE[slug] ?? slug.toUpperCase().replace(/-/g, '_')
  })

  // ── Metadata ───────────────────────────────────────────────────────────────
  readonly meta          = computed(() => resolveMeta(this.frameworkCode()))

  // ── Project selector ───────────────────────────────────────────────────────
  selectedProjectId = this.projectSvc.activeProjectId() ?? ''

  projects = injectQuery(() => ({
    queryKey: ['projects-list'],
    queryFn: () => firstValueFrom(this.projectsApi.list()),
  }))

  // ── Constants ──────────────────────────────────────────────────────────────
  readonly SCORES        = [0, 1, 2, 3, 4]
  readonly STATUS_ENTRIES = Object.entries(STATUS_CONFIG).map(([key, cfg]) => ({ key, cfg }))
  readonly Math          = Math

  // ── Signals ────────────────────────────────────────────────────────────────
  selectedId   = signal<string | null>(null)
  showCreate   = signal(false)
  deleteId     = signal<string | null>(null)
  editingMeta  = signal(false)

  // Create form
  createName     = ''
  createOrg      = ''
  createAssessor = ''
  createScope    = ''

  // Meta edit form
  metaName     = ''
  metaOrg      = ''
  metaAssessor = ''
  metaScope    = ''

  // Inline rating store: { reqId -> { current_score, target_score, rating_status, notes } }
  private ratingDraft = signal<Record<string, { current_score: number | null; target_score: number | null; rating_status: string; notes: string }>>({})

  // Group / row expand state
  expandedGroups = signal<Set<string>>(new Set<string>())
  expandedReqs   = signal<Set<string>>(new Set<string>())

  constructor() {
    // Reset detail view when navigating between frameworks (Angular reuses component instance)
    effect(() => {
      this.frameworkCode()
      this.selectedId.set(null)
      this.expandedGroups.set(new Set())
      this.expandedReqs.set(new Set())
    })
    // Auto-expand all groups when assessment data first loads
    effect(() => {
      const d = this.fullQuery.data()
      if (!d) return
      const gs = groupRequirements(d.requirements, this.frameworkCode())
      if (gs.length > 0 && this.expandedGroups().size === 0) {
        this.expandedGroups.set(new Set(gs.map(g => g.groupId)))
      }
    })
  }

  // ── Queries ────────────────────────────────────────────────────────────────
  listQuery = injectQuery(() => ({
    queryKey: ['regulatory', this.frameworkCode(), 'assessments', this.selectedProjectId],
    queryFn: () => firstValueFrom(
      this.api.listAssessments(this.frameworkCode(),
        this.selectedProjectId ? { project_id: this.selectedProjectId } : undefined)
    ),
    enabled: !!this.selectedProjectId,
  }))

  assessments = computed(() => this.listQuery.data() ?? [])

  fullQuery = injectQuery(() => ({
    queryKey: ['regulatory', this.frameworkCode(), 'assessment', this.selectedId() ?? ''],
    queryFn: () => this.selectedId()
      ? firstValueFrom(this.api.getFullAssessment(this.frameworkCode(), this.selectedId()!))
      : Promise.resolve<FullAssessment | null>(null),
    enabled: !!this.selectedId(),
  }))

  // Derived detail signals
  groups = computed<GroupedReq[]>(() => {
    const d = this.fullQuery.data()
    if (!d) return []
    return groupRequirements(d.requirements, this.frameworkCode())
  })

  scoreLabels = computed(() => resolveScoreLabels(this.frameworkCode()))

  detailProgress = computed(() => {
    const d = this.fullQuery.data()
    if (!d || d.requirements.length === 0) return 0
    const draft    = this.ratingDraft()
    const ratedIds = new Set<string>()
    // rated from server
    for (const r of d.ratings) {
      if (r.current_score !== null) ratedIds.add(r.requirement_id)
    }
    // overridden in draft
    for (const [reqId, val] of Object.entries(draft)) {
      if (val.current_score !== null) ratedIds.add(reqId)
      else ratedIds.delete(reqId)
    }
    return Math.round((ratedIds.size / d.requirements.length) * 100)
  })

  detailKpis = computed(() => {
    const d = this.fullQuery.data()
    if (!d) return []
    const draft    = this.ratingDraft()
    const reqs     = d.requirements
    const ratings  = d.ratings

    const ratingMap = new Map<string, ComplianceRating>(ratings.map(r => [r.requirement_id, r]))

    let ratedCount = 0, compliant = 0, partial = 0, nonCompliant = 0, scoreSum = 0, scoreCount = 0
    for (const req of reqs) {
      const dr     = draft[req.id]
      const cs     = dr ? dr.current_score : (ratingMap.get(req.id)?.current_score ?? null)
      const status = dr ? dr.rating_status : (ratingMap.get(req.id)?.rating_status ?? 'not_assessed')
      if (cs !== null) { ratedCount++; scoreSum += cs; scoreCount++ }
      if (status === 'compliant')     compliant++
      if (status === 'partial')       partial++
      if (status === 'non_compliant') nonCompliant++
    }
    const avg     = scoreCount > 0 ? scoreSum / scoreCount : null
    const pct     = reqs.length > 0 ? Math.round((ratedCount / reqs.length) * 100) : 0
    const fwColor = this.meta().color
    const labels  = this.scoreLabels()

    return [
      { label: 'Assessed',       value: `${ratedCount} / ${reqs.length}`, sub: `${pct}%`,      color: fwColor },
      { label: 'Avg Score',      value: avg !== null ? avg.toFixed(1) : '—', sub: avg !== null ? labels[Math.round(avg)] : '', color: avg !== null ? SCORE_COLORS[Math.round(avg)] : '#9e9e9e' },
      { label: 'Compliant',      value: compliant,    sub: reqs.length > 0 ? `${Math.round(compliant/reqs.length*100)}%` : '', color: '#00c752' },
      { label: 'Partial',        value: partial,      sub: '',             color: '#FF9800' },
      { label: 'Non-Compliant',  value: nonCompliant, sub: '',             color: '#f44336' },
    ]
  })

  // ── Mutations ──────────────────────────────────────────────────────────────
  createMutation = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.api.createAssessment(this.frameworkCode(), {
      framework_code: this.frameworkCode(),
      name:         this.createName,
      assessor:     this.createAssessor || undefined,
      organisation: this.createOrg || undefined,
      scope:        this.createScope || undefined,
      project_id:   this.selectedProjectId || null,
    })),
    onSuccess: () => {
      this.queryClient.invalidateQueries({ queryKey: ['regulatory', this.frameworkCode(), 'assessments'] })
      this.createName = this.createOrg = this.createAssessor = this.createScope = ''
      this.showCreate.set(false)
    },
  }))

  deleteMutation = injectMutation(() => ({
    mutationFn: (id: string) => firstValueFrom(this.api.deleteAssessment(this.frameworkCode(), id)),
    onSuccess: () => {
      this.queryClient.invalidateQueries({ queryKey: ['regulatory', this.frameworkCode(), 'assessments'] })
      if (this.deleteId() === this.selectedId()) this.selectedId.set(null)
      this.deleteId.set(null)
    },
  }))

  updateMutation = injectMutation(() => ({
    mutationFn: (upd: Partial<{ name: string; assessor: string | null; organisation: string | null; scope: string | null; status: 'draft' | 'complete' | 'in_progress' }>) =>
      firstValueFrom(this.api.updateAssessment(this.frameworkCode(), this.selectedId()!, upd as any)),
    onSuccess: () => {
      this.queryClient.invalidateQueries({ queryKey: ['regulatory', this.frameworkCode(), 'assessment', this.selectedId() ?? ''] })
      this.queryClient.invalidateQueries({ queryKey: ['regulatory', this.frameworkCode(), 'assessments'] })
      this.editingMeta.set(false)
    },
  }))

  // Debounced upsert — fires 800 ms after last change
  private saveTimers: Record<string, ReturnType<typeof setTimeout>> = {}

  upsertMutation = injectMutation(() => ({
    mutationFn: (ratings: RatingUpsert[]) =>
      firstValueFrom(this.api.upsertRatings(this.frameworkCode(), this.selectedId()!, ratings)),
    onSuccess: () => {
      this.queryClient.invalidateQueries({ queryKey: ['regulatory', this.frameworkCode(), 'assessments'] })
    },
  }))

  // ── Detail helpers ─────────────────────────────────────────────────────────
  private getServerRating(reqId: string): ComplianceRating | undefined {
    return this.fullQuery.data()?.ratings.find(r => r.requirement_id === reqId)
  }

  getCurrentScore(reqId: string): number | '' {
    const dr = this.ratingDraft()[reqId]
    if (dr) return dr.current_score ?? ''
    return this.getServerRating(reqId)?.current_score ?? ''
  }

  getTargetScore(reqId: string): number | '' {
    const dr = this.ratingDraft()[reqId]
    if (dr) return dr.target_score ?? ''
    return this.getServerRating(reqId)?.target_score ?? ''
  }

  getRatingStatus(reqId: string): string {
    const dr = this.ratingDraft()[reqId]
    if (dr) return dr.rating_status
    return this.getServerRating(reqId)?.rating_status ?? 'not_assessed'
  }

  getNotes(reqId: string): string {
    const dr = this.ratingDraft()[reqId]
    if (dr !== undefined) return dr.notes
    return this.getServerRating(reqId)?.notes ?? ''
  }

  private updateDraft(reqId: string, patch: Partial<{ current_score: number | null; target_score: number | null; rating_status: string; notes: string }>) {
    this.ratingDraft.update(d => {
      const existing = d[reqId] ?? {
        current_score:  this.getServerRating(reqId)?.current_score ?? null,
        target_score:   this.getServerRating(reqId)?.target_score  ?? null,
        rating_status:  this.getServerRating(reqId)?.rating_status ?? 'not_assessed',
        notes:          this.getServerRating(reqId)?.notes         ?? '',
      }
      return { ...d, [reqId]: { ...existing, ...patch } }
    })
    this.scheduleUpsert(reqId)
  }

  private scheduleUpsert(reqId: string) {
    if (this.saveTimers[reqId]) clearTimeout(this.saveTimers[reqId])
    this.saveTimers[reqId] = setTimeout(() => {
      const d = this.ratingDraft()[reqId]
      if (!d || !this.selectedId()) return
      this.upsertMutation.mutate([{
        requirement_id: reqId,
        current_score:  d.current_score,
        target_score:   d.target_score,
        rating_status:  d.rating_status,
        notes:          d.notes || null,
      }])
    }, 800)
  }

  setCurrentScore(reqId: string, v: number | '') {
    this.updateDraft(reqId, { current_score: v !== '' ? v as number : null })
  }

  setTargetScore(reqId: string, v: number | '') {
    this.updateDraft(reqId, { target_score: v !== '' ? v as number : null })
  }

  setRatingStatus(reqId: string, v: string) {
    this.updateDraft(reqId, { rating_status: v })
  }

  setNotes(reqId: string, v: string) {
    this.updateDraft(reqId, { notes: v })
  }

  scoreColor(s: number): string { return SCORE_COLORS[s] ?? '#9e9e9e' }

  progressPct(a: AssessmentSummary): number {
    return a.total_requirements > 0
      ? Math.round((a.rated_count / a.total_requirements) * 100)
      : 0
  }

  groupAvgScore(group: GroupedReq): number | null {
    const d    = this.fullQuery.data()
    const draft = this.ratingDraft()
    if (!d) return null
    const ratingMap = new Map(d.ratings.map(r => [r.requirement_id, r]))
    const scores: number[] = []
    for (const req of group.requirements) {
      const dr = draft[req.id]
      const cs = dr ? dr.current_score : (ratingMap.get(req.id)?.current_score ?? null)
      if (cs !== null) scores.push(cs)
    }
    return scores.length > 0 ? scores.reduce((a, b) => a + b, 0) / scores.length : null
  }

  toggleGroup(id: string) {
    this.expandedGroups.update(s => {
      const next = new Set(s)
      if (next.has(id)) next.delete(id); else next.add(id)
      return next
    })
  }

  toggleReq(id: string) {
    this.expandedReqs.update(s => {
      const next = new Set(s)
      if (next.has(id)) next.delete(id); else next.add(id)
      return next
    })
  }

  // ── Create / delete / update ───────────────────────────────────────────────
  submitCreate() {
    if (!this.createName) return
    this.createMutation.mutate()
  }

  submitDelete() {
    const id = this.deleteId()
    if (id) this.deleteMutation.mutate(id)
  }

  startEdit() {
    const d = this.fullQuery.data()
    if (!d) return
    this.metaName     = d.assessment.name
    this.metaAssessor = d.assessment.assessor    ?? ''
    this.metaOrg      = d.assessment.organisation ?? ''
    this.metaScope    = d.assessment.scope        ?? ''
    this.editingMeta.set(true)
  }

  saveMeta() {
    this.updateMutation.mutate({
      name:         this.metaName,
      assessor:     this.metaAssessor || null,
      organisation: this.metaOrg      || null,
      scope:        this.metaScope    || null,
    })
  }
}
