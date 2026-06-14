import { Component, inject, signal, computed, effect } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'
import { HttpClient } from '@angular/common/http'

import { MatButtonModule } from '@angular/material/button'
import { MatCardModule } from '@angular/material/card'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatIconModule } from '@angular/material/icon'
import { MatInputModule } from '@angular/material/input'
import { MatProgressBarModule } from '@angular/material/progress-bar'
import { MatRadioModule } from '@angular/material/radio'
import { MatSelectModule } from '@angular/material/select'
import { MatTabsModule } from '@angular/material/tabs'
import { MatTooltipModule } from '@angular/material/tooltip'

import { PageHeaderComponent } from '../../shared/components/page-header.component'

// ─── Types ────────────────────────────────────────────────────────────────────

interface CsrmAssessmentSummary {
  id: string; name: string; description: string | null; organisation: string | null
  assessor: string | null; scope: string | null; status: string
  created_at: string; updated_at: string
  objects_count: number; elevated_count: number
  baseline_met_pct: number | null; objects_fully_assessed: number
}

interface BaselineRating {
  id: string; object_id: string; requirement_id: string
  status: 'not_assessed' | 'met' | 'partial' | 'not_met' | 'exception'
  exception_justification: string | null; notes: string | null; updated_at: string
}

interface ElevatedTom {
  id: string; object_id: string; threat_category: string; tom_description: string
  status: 'planned' | 'in_progress' | 'implemented' | 'not_applicable'
  notes: string | null; created_at: string; updated_at: string
}

interface ProtectionObject {
  id: string; assessment_id: string; name: string; description: string | null
  architecture_notes: string | null; processes_served: string | null
  data_classification: string | null; protection_level: 'standard' | 'elevated'
  elevated_rationale: string | null; sort_order: number
  created_at: string; updated_at: string
  baseline_ratings: BaselineRating[]
  elevated_toms: ElevatedTom[]
}

interface AssessmentDetail {
  id: string; name: string; description: string | null; organisation: string | null
  assessor: string | null; scope: string | null; status: string
  created_at: string; updated_at: string
  objects: ProtectionObject[]
}

// ─── Constants ────────────────────────────────────────────────────────────────

const BASELINE_REQUIREMENTS = [
  { id: 'GV.1', function: 'Govern',          title: 'Security Organisation',               description: 'An information security organisation is defined with clear roles, responsibilities, and decision-making authority.' },
  { id: 'GV.2', function: 'Govern',          title: 'Cyber Risk Management',               description: 'Cyber risks are identified, assessed, and managed as part of the overall organisational risk management process.' },
  { id: 'GV.3', function: 'Govern',          title: 'Screening of Employees',              description: 'Background checks are performed for employees in security-sensitive roles commensurate with risk and regulatory requirements.' },
  { id: 'GV.4', function: 'Govern',          title: 'Training and Awareness',              description: 'Regular security awareness training is provided to all employees; role-specific training is provided to security-relevant staff.' },
  { id: 'ID.1', function: 'Identify',        title: 'IT Protection Objects',               description: 'All IT protection objects are documented with their processes served, data flows, hardware/software components, and protection needs analysed.' },
  { id: 'ID.2', function: 'Identify',        title: 'Supply Chain',                        description: 'Supply chain dependencies are identified, assessed for risk, and monitored on an ongoing basis.' },
  { id: 'PR.1', function: 'Protect',         title: 'Physical Protection, Configuration & Operation', description: 'Physical access controls are in place; logical isolation and virtualisation are used where appropriate; technical hardening is applied.' },
  { id: 'PR.2', function: 'Protect',         title: 'Vulnerability & Weakness Management', description: 'Software and firmware vulnerabilities are monitored and patched using automated mechanisms on a risk-based schedule.' },
  { id: 'PR.3', function: 'Protect',         title: 'Identity & Access Control',           description: 'All access to systems is authenticated; authorisation follows least-privilege principles; privileged access is controlled and logged.' },
  { id: 'PR.4', function: 'Protect',         title: 'Network Security',                    description: 'Network segments are separated with perimeter protection controls, or equivalent zero/minimal trust architecture is implemented.' },
  { id: 'PR.5', function: 'Protect',         title: 'Malware Protection',                  description: 'Protection against malware and data-driven attacks is implemented and kept current on all relevant systems.' },
  { id: 'PR.6', function: 'Protect',         title: 'Encryption & Data Deletion',          description: 'Sensitive data is protected by cryptographic controls for storage, processing, and transmission; secure deletion is applied according to data classification.' },
  { id: 'PR.7', function: 'Protect',         title: 'Data Backup',                         description: 'Regular backups are performed with offline/off-site copies at multiple locations; rapid restoration capability is tested periodically.' },
  { id: 'PR.8', function: 'Protect',         title: 'Secure Development',                  description: 'Security is integrated from the start of development: threat modelling, secure coding guidelines, CI/CD security checks, safe interfaces, and separated environments.' },
  { id: 'PR.9', function: 'Protect',         title: 'Availability',                        description: 'Sufficient computing, storage, and transmission capacity is maintained; critical components have redundancy to meet availability requirements.' },
  { id: 'DE.1', function: 'Detect',          title: 'Recording & Monitoring',              description: 'Security-relevant events are logged and evaluated; SOC or equivalent monitoring capability assesses log data for anomalies.' },
  { id: 'DE.2', function: 'Detect',          title: 'Reporting Centre',                    description: 'A clear and documented process exists for employees and partners to report vulnerabilities and security incidents.' },
  { id: 'RS.1', function: 'Respond/Recover', title: 'Incident Management',                 description: 'Security incidents are triaged, escalated, and resolved according to documented procedures with defined responsibilities and timelines.' },
  { id: 'RS.2', function: 'Respond/Recover', title: 'Contingency Planning',                description: 'Emergency and recovery plans are documented, integrated into organisational plans, include IT/OT supply chain dependencies, and are tested regularly.' },
  { id: 'RS.3', function: 'Respond/Recover', title: 'Crisis Communication',                description: 'Communication responsibilities and objectives for security emergencies are defined, documented, and known to all relevant parties.' },
]

const NIST_FUNCTIONS = ['Govern', 'Identify', 'Protect', 'Detect', 'Respond/Recover']

const FUNCTION_COLORS: Record<string, string> = {
  'Govern':          '#5C6BC0',
  'Identify':        '#00897B',
  'Protect':         '#2E7D32',
  'Detect':          '#F57F17',
  'Respond/Recover': '#C62828',
}

const THREAT_CATEGORIES = [
  'Authentication', 'Integrity Check', 'Hashing', 'Message Authentication',
  'Logging', 'Encryption', 'Access Control', 'Network Segmentation',
  'Resourcing', 'High Availability', 'Least Privilege', 'Abuse/Compromise Protection',
]

const CONTROL_OBJECTIVES = [
  { id: 'CO-1', title: 'Process & Dependency Visibility',  reqs: ['ID.1', 'ID.2'] },
  { id: 'CO-2', title: 'Governance & Culture',             reqs: ['GV.1', 'GV.2', 'GV.3', 'GV.4'] },
  { id: 'CO-3', title: 'Threat & Protection Analysis',     reqs: ['ID.1', 'ID.2', 'GV.2'] },
  { id: 'CO-4', title: 'TOM Implementation',               reqs: ['PR.1', 'PR.2', 'PR.3', 'PR.4', 'PR.5', 'PR.6', 'PR.7', 'PR.8', 'PR.9'] },
  { id: 'CO-5', title: 'Detection & Recovery',             reqs: ['DE.1', 'DE.2', 'RS.1', 'RS.2', 'RS.3'] },
  { id: 'CO-6', title: 'Supply Chain Control',             reqs: ['ID.2', 'RS.2'] },
]

const RATING_STATUSES = ['not_assessed', 'met', 'partial', 'not_met', 'exception'] as const

const RATING_LABELS: Record<string, string> = {
  not_assessed: 'Not Assessed', met: 'Met', partial: 'Partial', not_met: 'Not Met', exception: 'Exception',
}

const TOM_STATUSES = ['planned', 'in_progress', 'implemented', 'not_applicable'] as const

function fmtDate(iso: string): string {
  const d = new Date(iso)
  return d.toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: '2-digit' })
}

function getRating(obj: ProtectionObject, reqId: string): BaselineRating | undefined {
  return obj.baseline_ratings.find(r => r.requirement_id === reqId)
}

function assessedCount(obj: ProtectionObject): number {
  return obj.baseline_ratings.filter(r => r.status !== 'not_assessed').length
}

function metCount(obj: ProtectionObject): number {
  return obj.baseline_ratings.filter(r => r.status === 'met').length
}

function coPct(objects: ProtectionObject[], reqs: string[]): number | null {
  if (!objects.length) return null
  const total = objects.length * reqs.length
  const met = objects.reduce((acc, o) => acc + reqs.filter(rid => getRating(o, rid)?.status === 'met').length, 0)
  return total > 0 ? Math.round(met / total * 100) : null
}

function pctColor(pct: number | null): string {
  if (pct === null) return 'var(--mat-sys-on-surface-variant)'
  return pct >= 80 ? '#4CAF50' : pct >= 50 ? '#FFC000' : '#FF7043'
}

function baselinePct(objects: ProtectionObject[]): number | null {
  if (!objects.length) return null
  const total = objects.length * 20
  const met = objects.reduce((s, o) => s + metCount(o), 0)
  return Math.round(met / total * 100)
}

// ─── Main Component ───────────────────────────────────────────────────────────

@Component({
  selector: 'app-csrm',
  standalone: true,
  imports: [
    FormsModule,
    MatButtonModule, MatCardModule, MatFormFieldModule, MatIconModule,
    MatInputModule, MatProgressBarModule, MatRadioModule, MatSelectModule,
    MatTabsModule, MatTooltipModule,
    PageHeaderComponent,
  ],
  template: `
    <app-page-header
      title="CSRM"
      subtitle="Swiss NCSC Cyber Security Risk Management — object-centric baseline & elevated TOM assessment">
      <div class="csrm-badge">NCSC CH</div>
      @if (!selectedId()) {
        <button mat-raised-button color="primary" (click)="newAssessmentOpen.set(true)">
          <mat-icon>add</mat-icon> New Assessment
        </button>
      } @else {
        <button mat-button (click)="closeDetail()">
          <mat-icon>arrow_back</mat-icon> All Assessments
        </button>
      }
    </app-page-header>

    <!-- Disclaimer banner -->
    <div class="disclaimer" (click)="disclaimerOpen.set(!disclaimerOpen())">
      <div class="disclaimer-header">
        <strong>CSRM 2025 — Framework in Development</strong>
        <mat-icon class="icon-md">{{ disclaimerOpen() ? 'expand_less' : 'expand_more' }}</mat-icon>
      </div>
      <div class="disclaimer-subtext">NCSC BACS publishes this methodology as a work in progress.</div>
      @if (disclaimerOpen()) {
        <div class="disclaimer-body">
          <div class="disclaimer-note"><strong>ISMS CORE note:</strong> Uses NIST CSF 2.0 structure (Govern / Identify / Protect / Detect / Respond+Recover). BACS comparison document references ICT Minimum Standard (NIST CSF 1.1).</div>
          <strong>Known gaps (NCSC Vergleich-Managementsysteme_EN.pdf):</strong>
          <ul class="disclaimer-gaps-list">
            <li>IEC 62443 alignment pending — OT coverage not yet demonstrated</li>
            <li>10 ICT Minimum Standard gaps incl. threat intel sharing, hardware integrity, forensics</li>
            <li>"No policies needed" is misleading — operational policies remain necessary</li>
            <li>Continuous improvement optional — unlike ISO 27001 PDCA</li>
            <li>Parallel implementation with ISO 27001 creates reporting duplication</li>
          </ul>
        </div>
      }
    </div>

    <!-- ── LIST VIEW ──────────────────────────────────────────────────────────── -->
    @if (!selectedId()) {
      @if (listLoading()) {
        <div class="col-gap-12">
          @for (_ of [0,1,2]; track $index) { <div class="skel skel-lg"></div> }
        </div>
      } @else if (!assessments().length) {
        <div class="empty-state">
          <div class="empty-state-text">No assessments yet</div>
          <button mat-stroked-button (click)="newAssessmentOpen.set(true)"><mat-icon>add</mat-icon> New Assessment</button>
        </div>
      } @else {
        <div class="col-gap-12">
          @for (a of assessments(); track a.id) {
            <mat-card class="card-default">
              <mat-card-content class="card-content-16">
                <div class="row-gap-16-start">
                  <div class="flex-1-min0">
                    <div class="row-gap-8-center mb-4">
                      <span class="text-name">{{ a.name }}</span>
                      <span class="status-badge status-{{ a.status }}">{{ a.status }}</span>
                    </div>
                    @if (a.organisation) {
                      <div class="text-sm-muted mb-4">{{ a.organisation }}</div>
                    }
                    <div class="row-wrap-gap-16">
                      <span class="text-xs-muted">{{ a.objects_count }} protection objects</span>
                      @if (a.elevated_count > 0) {
                        <span class="text-xs-elevated">{{ a.elevated_count }} elevated</span>
                      }
                      <span class="text-xs-muted">{{ a.objects_fully_assessed }}/{{ a.objects_count }} fully assessed</span>
                      @if (a.baseline_met_pct !== null) {
                        <div class="row-gap-6-center">
                          <mat-progress-bar mode="determinate" [value]="a.baseline_met_pct" class="pbar-80" />
                          <span class="text-xs-bold" [style.color]="pctColor(a.baseline_met_pct)">{{ a.baseline_met_pct }}%</span>
                        </div>
                      }
                    </div>
                  </div>
                  <div class="row-gap-8-center flex-shrink-0">
                    <button mat-icon-button class="btn-delete-soft" (click)="confirmDelete(a)">
                      <mat-icon>delete</mat-icon>
                    </button>
                    <button mat-stroked-button (click)="openAssessment(a.id)">Open</button>
                  </div>
                </div>
              </mat-card-content>
            </mat-card>
          }
        </div>
      }
    }

    <!-- ── DETAIL VIEW ────────────────────────────────────────────────────────── -->
    @if (selectedId()) {
      @if (detailLoading() || !detail()) {
        <div class="col-gap-12">
          @for (_ of [0,1,2]; track $index) { <div class="skel skel-sm"></div> }
        </div>
      } @else {
        <mat-tab-group [(selectedIndex)]="activeTabIdx" animationDuration="150ms">
          <mat-tab label="Overview"></mat-tab>
          <mat-tab [label]="'Protection Objects (' + detail()!.objects.length + ')'"></mat-tab>
          <mat-tab label="Report"></mat-tab>
        </mat-tab-group>

        <!-- Overview tab -->
        @if (activeTabIdx === 0) {
          <div class="tab-content">
            <mat-card class="card-mb-20">
              <mat-card-content class="card-content-16">
                <div class="row-between mb-12">
                  <span class="text-bold">Assessment Details</span>
                  <button mat-icon-button (click)="editMeta.set(!editMeta())">
                    <mat-icon class="icon-edit">edit</mat-icon>
                  </button>
                </div>
                @if (editMeta()) {
                  <div class="col-gap-12">
                    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full">
                      <mat-label>Name</mat-label><input matInput [(ngModel)]="metaForm.name" />
                    </mat-form-field>
                    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full">
                      <mat-label>Description</mat-label><textarea matInput [(ngModel)]="metaForm.description" rows="2"></textarea>
                    </mat-form-field>
                    <div class="row-gap-12">
                      <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-flex-1">
                        <mat-label>Organisation</mat-label><input matInput [(ngModel)]="metaForm.organisation" />
                      </mat-form-field>
                      <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-flex-1">
                        <mat-label>Assessor</mat-label><input matInput [(ngModel)]="metaForm.assessor" />
                      </mat-form-field>
                    </div>
                    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full">
                      <mat-label>Scope</mat-label><textarea matInput [(ngModel)]="metaForm.scope" rows="2"></textarea>
                    </mat-form-field>
                    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-status">
                      <mat-label>Status</mat-label>
                      <mat-select [(ngModel)]="metaForm.status">
                        <mat-option value="draft">Draft</mat-option>
                        <mat-option value="in_progress">In Progress</mat-option>
                        <mat-option value="complete">Complete</mat-option>
                      </mat-select>
                    </mat-form-field>
                    <div class="row-end-gap-8">
                      <button mat-button (click)="editMeta.set(false)">Cancel</button>
                      <button mat-raised-button color="primary" (click)="saveAssessmentMeta()">Save</button>
                    </div>
                  </div>
                } @else {
                  <div class="row-wrap-gap-16">
                    @if (detail()!.scope) {
                      <div><div class="label-xs-muted">Scope</div><div class="text-sm">{{ detail()!.scope }}</div></div>
                    }
                    @if (detail()!.description) {
                      <div class="flex-1-min200"><div class="label-xs-muted">Description</div><div class="text-sm">{{ detail()!.description }}</div></div>
                    }
                  </div>
                }
              </mat-card-content>
            </mat-card>

            <div class="section-title">Control Objectives</div>
            @if (!detail()!.objects.length) {
              <div class="info-banner">Add protection objects to begin assessing control objectives.</div>
            } @else {
              <div class="grid-3-gap-12">
                @for (co of controlObjectives; track co.id) {
                  <mat-card>
                    <mat-card-content class="card-content-12">
                      <div class="co-card-header">
                        <div>
                          <div class="co-id" [style.color]="pctColor(coPctFor(co.reqs))">{{ co.id }}</div>
                          <div class="co-title">{{ co.title }}</div>
                        </div>
                        <span class="co-pct flex-shrink-0" [style.color]="pctColor(coPctFor(co.reqs))">
                          {{ coPctFor(co.reqs) !== null ? coPctFor(co.reqs) + '%' : '—' }}
                        </span>
                      </div>
                      @if (coPctFor(co.reqs) !== null) {
                        <mat-progress-bar mode="determinate" [value]="coPctFor(co.reqs)!" class="pbar-thin" />
                      }
                    </mat-card-content>
                  </mat-card>
                }
              </div>
            }
          </div>
        }

        <!-- Objects tab -->
        @if (activeTabIdx === 1) {
          <div class="objects-layout">
            <div class="objects-sidebar">
              <button mat-stroked-button class="btn-full btn-mb-12" (click)="newObjectOpen.set(true)">
                <mat-icon>add</mat-icon> Add Protection Object
              </button>
              @if (!detail()!.objects.length) {
                <div class="sidebar-empty">No protection objects yet.</div>
              } @else {
                <div class="col-gap-6">
                  @for (obj of detail()!.objects; track obj.id) {
                    <div class="obj-card" [class.obj-active]="selectedObjectId()===obj.id"
                      (click)="selectedObjectId.set(selectedObjectId()===obj.id ? null : obj.id)">
                      <div class="row-between-start-gap-4">
                        <span class="obj-name" [style.font-weight]="selectedObjectId()===obj.id?600:400">{{ obj.name }}</span>
                        <button mat-icon-button class="btn-delete-xs"
                          (click)="$event.stopPropagation();deleteObject(obj.id)">
                          <mat-icon class="icon-sm">delete</mat-icon>
                        </button>
                      </div>
                      <div class="row-gap-6-center mt-4">
                        <span class="prot-chip" [class.elevated]="obj.protection_level==='elevated'">{{ obj.protection_level==='elevated'?'Elevated':'Standard' }}</span>
                        <span class="text-xxs-muted">{{ assessedCount(obj) }}/20 · {{ metCount(obj) }} met</span>
                      </div>
                      <mat-progress-bar mode="determinate" [value]="assessedCount(obj)/20*100" class="pbar-mt-6" />
                    </div>
                  }
                </div>
              }
            </div>

            <div class="obj-panel">
              @if (!selectedObjectId() || !selectedObject()) {
                <div class="panel-empty-state">
                  Select a protection object to assess its baseline requirements.
                </div>
              } @else {
                <div class="panel-scroll">
                  <div class="row-gap-8-center mb-16">
                    <button mat-icon-button (click)="selectedObjectId.set(null)"><mat-icon>arrow_back</mat-icon></button>
                    <div class="flex-1">
                      <div class="text-object-name">{{ selectedObject()!.name }}</div>
                      <div class="row-gap-8-center mt-2">
                        <span class="prot-chip" [class.elevated]="selectedObject()!.protection_level==='elevated'">
                          {{ selectedObject()!.protection_level==='elevated' ? 'Elevated Protection' : 'Standard Protection' }}
                        </span>
                        <span class="text-xxs-muted">{{ assessedCount(selectedObject()!) }}/20 assessed · {{ metCount(selectedObject()!) }} met</span>
                      </div>
                    </div>
                    <button mat-icon-button (click)="toggleObjEdit()"><mat-icon class="icon-edit">edit</mat-icon></button>
                  </div>

                  @if (editObjMeta()) {
                    <div class="meta-box mb-16">
                      <div class="section-label mb-12">Object Properties</div>
                      <div class="col-gap-12">
                        <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full"><mat-label>Name</mat-label><input matInput [(ngModel)]="objMetaForm.name" /></mat-form-field>
                        <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full"><mat-label>Description</mat-label><textarea matInput [(ngModel)]="objMetaForm.description" rows="2"></textarea></mat-form-field>
                        <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full"><mat-label>Architecture notes</mat-label><textarea matInput [(ngModel)]="objMetaForm.architecture_notes" rows="2"></textarea></mat-form-field>
                        <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full"><mat-label>Processes served</mat-label><textarea matInput [(ngModel)]="objMetaForm.processes_served" rows="2"></textarea></mat-form-field>
                        <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full">
                          <mat-label>Data Classification</mat-label>
                          <mat-select [(ngModel)]="objMetaForm.data_classification">
                            <mat-option value="standard">Standard</mat-option>
                            <mat-option value="confidential">Confidential</mat-option>
                            <mat-option value="restricted">Restricted</mat-option>
                          </mat-select>
                        </mat-form-field>
                        <div>
                          <div class="text-sm-muted mb-4">Protection Level</div>
                          <mat-radio-group [(ngModel)]="objMetaForm.protection_level" class="radio-group-row">
                            <mat-radio-button value="standard">Standard</mat-radio-button>
                            <mat-radio-button value="elevated"><span class="text-elevated">Elevated</span></mat-radio-button>
                          </mat-radio-group>
                        </div>
                        @if (objMetaForm.protection_level==='elevated') {
                          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full"><mat-label>Rationale for elevated protection</mat-label><textarea matInput [(ngModel)]="objMetaForm.elevated_rationale" rows="2"></textarea></mat-form-field>
                        }
                        <div class="row-end-gap-8">
                          <button mat-button (click)="editObjMeta.set(false)">Cancel</button>
                          <button mat-raised-button color="primary" (click)="saveObjMeta()">Save</button>
                        </div>
                      </div>
                    </div>
                  }

                  <!-- Baseline requirements by NIST function -->
                  <div class="section-label mb-8">Baseline Requirements (20)</div>
                  @for (fn of nistFunctions; track fn) {
                    <div class="fn-group">
                      <div class="fn-header" [style.border-bottom]="'2px solid ' + fnColor(fn) + '30'">
                        <div class="fn-dot flex-shrink-0" [style.background]="fnColor(fn)"></div>
                        <span class="fn-label" [style.color]="fnColor(fn)">{{ fn }}</span>
                      </div>
                      @for (req of reqsForFn(fn); track req.id) {
                        <div class="req-row">
                          <div class="row-wrap-gap-8">
                            <span class="req-id-chip" [style.background]="fnColor(fn)+'20'" [style.color]="fnColor(fn)" [style.border-color]="fnColor(fn)+'40'">{{ req.id }}</span>
                            <span class="req-title">{{ req.title }}</span>
                            <mat-icon class="icon-info flex-shrink-0" [matTooltip]="req.description">info_outline</mat-icon>
                            <div class="rating-btns">
                              @for (s of ratingStatuses; track s) {
                                <div class="rating-btn"
                                  [class.active]="(getRatingFor(req.id)?.status ?? 'not_assessed')===s"
                                  [attr.data-status]="s"
                                  (click)="updateRating(req.id, s)">
                                  {{ RATING_LABELS[s] }}
                                </div>
                              }
                            </div>
                            <button mat-icon-button class="btn-notes flex-shrink-0"
                              (click)="toggleNotes(req.id)">
                              <mat-icon class="icon-chevron" [style.color]="hasNotes(req.id)?'#FFC000':'var(--mat-sys-on-surface-variant)'">
                                {{ notesOpen().has(req.id) ? 'expand_less' : 'expand_more' }}
                              </mat-icon>
                            </button>
                          </div>
                          @if (notesOpen().has(req.id)) {
                            <div class="notes-panel">
                              <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full">
                                <mat-label>Notes</mat-label>
                                <textarea matInput rows="2" [(ngModel)]="notesDraft[req.id]" (blur)="saveNotes(req.id)"></textarea>
                              </mat-form-field>
                              @if ((getRatingFor(req.id)?.status ?? 'not_assessed')==='exception') {
                                <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full">
                                  <mat-label>Exception justification</mat-label>
                                  <textarea matInput rows="2" [(ngModel)]="justDraft[req.id]" (blur)="saveNotes(req.id)"></textarea>
                                </mat-form-field>
                              }
                            </div>
                          }
                        </div>
                      }
                    </div>
                  }

                  <!-- Elevated TOMs -->
                  @if (selectedObject()!.protection_level==='elevated') {
                    <div class="toms-section">
                      <div class="row-between mb-12">
                        <div>
                          <div class="toms-label">Additional TOMs</div>
                          <div class="toms-subtitle">Elevated objects require additional threat-specific measures</div>
                        </div>
                        <button mat-button (click)="newTomOpen.set(!newTomOpen())"><mat-icon class="icon-sm">add</mat-icon> Add TOM</button>
                      </div>
                      @if (newTomOpen()) {
                        <div class="new-tom-box">
                          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full field-mb-10">
                            <mat-label>Threat Category</mat-label>
                            <mat-select [(ngModel)]="newTomForm.threat_category">
                              @for (c of threatCategories; track c) { <mat-option [value]="c">{{ c }}</mat-option> }
                            </mat-select>
                          </mat-form-field>
                          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full field-mb-10">
                            <mat-label>TOM description</mat-label>
                            <textarea matInput [(ngModel)]="newTomForm.tom_description" rows="2"></textarea>
                          </mat-form-field>
                          <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full field-mb-10">
                            <mat-label>Notes (optional)</mat-label>
                            <input matInput [(ngModel)]="newTomForm.notes" />
                          </mat-form-field>
                          <div class="row-end-gap-8">
                            <button mat-button (click)="newTomOpen.set(false)">Cancel</button>
                            <button mat-raised-button color="primary" [disabled]="!newTomForm.threat_category||!newTomForm.tom_description" (click)="addTom()">Add</button>
                          </div>
                        </div>
                      }
                      @if (!selectedObject()!.elevated_toms.length) {
                        <div class="toms-empty">No TOMs defined yet.</div>
                      } @else {
                        @for (tom of selectedObject()!.elevated_toms; track tom.id) {
                          <div class="tom-card">
                            <div class="row-gap-8-start">
                              <span class="cat-chip flex-shrink-0">{{ tom.threat_category }}</span>
                              <div class="flex-1-min0">
                                <div class="tom-desc">{{ tom.tom_description }}</div>
                                @if (tom.notes) { <div class="text-xxs-muted">{{ tom.notes }}</div> }
                              </div>
                              <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-tom-status">
                                <mat-select [value]="tom.status" (selectionChange)="patchTom(tom.id, {status:$event.value})">
                                  @for (s of tomStatuses; track s) { <mat-option [value]="s">{{ s }}</mat-option> }
                                </mat-select>
                              </mat-form-field>
                              <button mat-icon-button class="btn-delete-sm" (click)="deleteTom(tom.id)">
                                <mat-icon class="icon-sm">delete</mat-icon>
                              </button>
                            </div>
                          </div>
                        }
                      }
                    </div>
                  }
                </div>
              }
            </div>
          </div>
        }

        <!-- Report tab -->
        @if (activeTabIdx === 2) {
          <div class="tab-content">
            <div class="warn-banner mb-20">
              <strong>Report Disclaimer:</strong> CSRM 2025 is in active development. Verify coverage against the ICT Minimum Standard for the 10 gap areas listed in the disclaimer above.
            </div>
            <div class="grid-4-gap-12 mb-24">
              @for (c of reportCards(); track c.label) {
                <mat-card>
                  <mat-card-content class="card-content-12">
                    <div class="report-card-label">{{ c.label }}</div>
                    <div class="report-card-value" [style.color]="c.color ?? 'inherit'">{{ c.value }}</div>
                  </mat-card-content>
                </mat-card>
              }
            </div>

            <div class="section-title">Control Objectives</div>
            <div class="col-gap-8 mb-24">
              @for (co of controlObjectives; track co.id) {
                <div class="report-co-row">
                  <span class="report-co-id flex-shrink-0">{{ co.id }}</span>
                  <span class="report-co-title">{{ co.title }}</span>
                  <mat-progress-bar mode="determinate" [value]="coPctFor(co.reqs)??0" class="pbar-160 flex-shrink-0" />
                  <span class="report-co-pct flex-shrink-0" [style.color]="pctColor(coPctFor(co.reqs))">
                    {{ coPctFor(co.reqs) !== null ? coPctFor(co.reqs)+'%' : '—' }}
                  </span>
                </div>
              }
            </div>

            @if (reportGaps().length > 0) {
              <div class="section-title">Gap Analysis ({{ reportGaps().length }} items)</div>
              <div class="gap-table">
                <div class="gap-row gap-header"><span>Object</span><span>Req</span><span>Status</span><span>Requirement</span></div>
                @for (g of reportGaps(); track $index) {
                  <div class="gap-row">
                    <span class="gap-object-cell">{{ g.object }}</span>
                    <span class="gap-req-id" [style.color]="fnColor(g.fn)">{{ g.reqId }}</span>
                    <span class="req-status-chip" [attr.data-status]="g.status">{{ RATING_LABELS[g.status] }}</span>
                    <span class="gap-req-title">{{ g.title }}</span>
                  </div>
                }
              </div>
            } @else if (detail()!.objects.length > 0) {
              <div class="success-banner">No gaps identified — all assessed requirements are met.</div>
            }
          </div>
        }
      }
    }

    <!-- New Assessment Dialog -->
    @if (newAssessmentOpen()) {
      <div class="overlay" (click)="newAssessmentOpen.set(false)">
        <div class="dlg-panel" (click)="$event.stopPropagation()">
          <h3 class="dialog-title">New CSRM Assessment</h3>
          <div class="col-gap-12">
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full"><mat-label>Assessment name *</mat-label><input matInput [(ngModel)]="newAssessForm.name" /></mat-form-field>
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full"><mat-label>Description</mat-label><textarea matInput [(ngModel)]="newAssessForm.description" rows="2"></textarea></mat-form-field>
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full"><mat-label>Organisation</mat-label><input matInput [(ngModel)]="newAssessForm.organisation" /></mat-form-field>
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full"><mat-label>Assessor</mat-label><input matInput [(ngModel)]="newAssessForm.assessor" /></mat-form-field>
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full"><mat-label>Scope</mat-label><textarea matInput [(ngModel)]="newAssessForm.scope" rows="2"></textarea></mat-form-field>
          </div>
          <div class="row-end-gap-8 mt-16">
            <button mat-button (click)="newAssessmentOpen.set(false)">Cancel</button>
            <button mat-raised-button color="primary" [disabled]="!newAssessForm.name.trim()||savingAssess()" (click)="createAssessment()">Create</button>
          </div>
        </div>
      </div>
    }

    <!-- New Object Dialog -->
    @if (newObjectOpen()) {
      <div class="overlay" (click)="newObjectOpen.set(false)">
        <div class="dlg-panel" (click)="$event.stopPropagation()">
          <h3 class="dialog-title">Add Protection Object</h3>
          <div class="col-gap-12">
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full"><mat-label>Name *</mat-label><input matInput [(ngModel)]="newObjForm.name" /></mat-form-field>
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full"><mat-label>Description</mat-label><textarea matInput [(ngModel)]="newObjForm.description" rows="2"></textarea></mat-form-field>
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full"><mat-label>Architecture notes</mat-label><textarea matInput [(ngModel)]="newObjForm.architecture_notes" rows="2"></textarea></mat-form-field>
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full"><mat-label>Processes served</mat-label><textarea matInput [(ngModel)]="newObjForm.processes_served" rows="2"></textarea></mat-form-field>
            <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full">
              <mat-label>Data Classification</mat-label>
              <mat-select [(ngModel)]="newObjForm.data_classification">
                <mat-option value="standard">Standard</mat-option><mat-option value="confidential">Confidential</mat-option><mat-option value="restricted">Restricted</mat-option>
              </mat-select>
            </mat-form-field>
            <div>
              <div class="text-sm-muted mb-4">Protection Level</div>
              <mat-radio-group [(ngModel)]="newObjForm.protection_level" class="radio-group-row">
                <mat-radio-button value="standard">Standard</mat-radio-button>
                <mat-radio-button value="elevated"><span class="text-elevated">Elevated</span></mat-radio-button>
              </mat-radio-group>
            </div>
            @if (newObjForm.protection_level==='elevated') {
              <mat-form-field appearance="outline" subscriptSizing="dynamic" class="field-full"><mat-label>Rationale for elevated protection</mat-label><textarea matInput [(ngModel)]="newObjForm.elevated_rationale" rows="2"></textarea></mat-form-field>
            }
          </div>
          <div class="row-end-gap-8 mt-16">
            <button mat-button (click)="newObjectOpen.set(false)">Cancel</button>
            <button mat-raised-button color="primary" [disabled]="!newObjForm.name.trim()||savingObj()" (click)="createObject()">Add</button>
          </div>
        </div>
      </div>
    }
  `,
  styles: [`
    /* ── Host ─────────────────────────────────────────────────────────────────── */
    :host { display:block }

    .csrm-badge {
      font-size:.72rem; font-weight:600; padding:2px 10px; border-radius:10px;
      background:rgba(196,40,40,.18); color:#C62828;
    }
    html[data-theme='light'] .csrm-badge { background:rgba(196,40,40,.12); color:#B71C1C; }

    /* ── Skeleton loader ──────────────────────────────────────────────────────── */
    .skel { background:var(--mat-sys-surface-variant); border-radius:4px }
    .skel-lg { height:100px; border-radius:8px }
    .skel-sm { height:60px; border-radius:8px }

    /* ── Layout helpers ───────────────────────────────────────────────────────── */
    .col-gap-6  { display:flex; flex-direction:column; gap:6px }
    .col-gap-8  { display:flex; flex-direction:column; gap:8px }
    .col-gap-12 { display:flex; flex-direction:column; gap:12px }
    .row-gap-8-center  { display:flex; align-items:center; gap:8px }
    .row-gap-8-start   { display:flex; align-items:flex-start; gap:8px }
    .row-gap-6-center  { display:flex; align-items:center; gap:6px }
    .row-gap-12        { display:flex; gap:12px }
    .row-gap-16        { display:flex; gap:16px }
    .row-gap-16-start  { display:flex; align-items:flex-start; gap:16px }
    .row-wrap-gap-8    { display:flex; align-items:center; gap:8px; flex-wrap:wrap }
    .row-wrap-gap-16   { display:flex; gap:16px; align-items:center; flex-wrap:wrap }
    .row-between       { display:flex; align-items:center; justify-content:space-between }
    .row-between-start-gap-4 { display:flex; align-items:flex-start; justify-content:space-between; gap:4px }
    .row-end-gap-8     { display:flex; gap:8px; justify-content:flex-end }
    .flex-1     { flex:1 }
    .flex-1-min0    { flex:1; min-width:0 }
    .flex-1-min200  { flex:1; min-width:200px }
    .flex-shrink-0  { flex-shrink:0 }
    .grid-3-gap-12 { display:grid; grid-template-columns:repeat(3,1fr); gap:12px }
    .grid-4-gap-12 { display:grid; grid-template-columns:repeat(4,1fr); gap:12px }

    /* ── Spacing utilities ────────────────────────────────────────────────────── */
    .mb-4  { margin-bottom:4px }
    .mb-8  { margin-bottom:8px }
    .mb-12 { margin-bottom:12px }
    .mb-16 { margin-bottom:16px }
    .mb-20 { margin-bottom:20px }
    .mb-24 { margin-bottom:24px }
    .mt-2  { margin-top:2px }
    .mt-4  { margin-top:4px }
    .mt-16 { margin-top:16px }

    /* ── Form field widths ────────────────────────────────────────────────────── */
    .field-full   { width:100% }
    .field-flex-1 { flex:1 }
    .field-status { max-width:180px }
    .field-mb-10  { margin-bottom:10px }
    .field-tom-status { min-width:120px; flex-shrink:0 }

    /* ── Typography ───────────────────────────────────────────────────────────── */
    .text-bold      { font-weight:600 }
    .text-name      { font-weight:600; font-size:.95rem }
    .text-sm        { font-size:.82rem }
    .text-sm-muted  { font-size:.82rem; color:var(--mat-sys-on-surface-variant) }
    .text-xs-muted  { font-size:.78rem; color:var(--mat-sys-on-surface-variant) }
    .text-xs-bold   { font-size:.78rem; font-weight:600 }
    .text-xs-elevated { font-size:.78rem; color:#FF7043 }
    .text-xxs-muted { font-size:.68rem; color:var(--mat-sys-on-surface-variant) }
    .text-object-name { font-size:1rem; font-weight:600 }
    .text-elevated  { color:#FF7043 }
    .label-xs-muted { font-size:.72rem; color:var(--mat-sys-on-surface-variant) }

    /* ── Section / panel labels ───────────────────────────────────────────────── */
    .section-title { font-weight:600; margin-bottom:12px }
    .section-label {
      font-size:.65rem; font-weight:600; text-transform:uppercase;
      letter-spacing:.05em; color:var(--mat-sys-on-surface-variant)
    }

    /* ── Disclaimer banner ────────────────────────────────────────────────────── */
    .disclaimer {
      padding:12px 16px; border-radius:8px; border:1px solid rgba(255,152,0,.3);
      background:rgba(255,152,0,.08); margin-top:16px; margin-bottom:20px; cursor:pointer; font-size:.82rem
    }
    .disclaimer-header { display:flex; align-items:center; justify-content:space-between }
    .disclaimer-subtext { font-size:.82rem }
    .disclaimer-body    { margin-top:10px; font-size:.78rem }
    .disclaimer-note    { color:#4CAF50; margin-bottom:6px }
    .disclaimer-gaps-list { margin:6px 0 0 16px; padding:0 }

    /* ── Status badges ────────────────────────────────────────────────────────── */
    .status-badge { display:inline-block; padding:2px 8px; border-radius:10px; font-size:.7rem; font-weight:500 }
    .status-draft       { background:rgba(21,101,192,.1); color:#1565c0 }
    .status-in_progress { background:rgba(133,100,4,.1); color:#856404 }
    .status-complete    { background:rgba(27,94,32,.1); color:#1b5e20 }

    /* ── Protection chips ─────────────────────────────────────────────────────── */
    .prot-chip {
      display:inline-block; padding:2px 8px; border-radius:10px; font-size:.6rem; font-weight:600;
      background:rgba(144,202,249,.1); color:var(--mat-sys-primary)
    }
    .prot-chip.elevated { background:rgba(255,112,67,.1); color:#FF7043 }
    .cat-chip {
      display:inline-block; padding:2px 8px; border-radius:10px; font-size:.65rem; font-weight:600;
      background:var(--mat-sys-surface-variant); color:var(--mat-sys-on-surface-variant)
    }

    /* ── Cards ────────────────────────────────────────────────────────────────── */
    .card-default   { cursor:default }
    .card-mb-20     { margin-bottom:20px }
    .card-content-12 { padding:12px }
    .card-content-16 { padding:16px }

    /* ── Progress bars ────────────────────────────────────────────────────────── */
    .pbar-80   { width:80px }
    .pbar-160  { width:160px }
    .pbar-thin { height:3px }
    .pbar-mt-6 { margin-top:6px }

    /* ── Icon sizes (icons not in global styles.scss) ─────────────────────────── */
    .icon-edit    { font-size:17px }
    .icon-info    { font-size:13px; color:var(--mat-sys-on-surface-variant); cursor:help }
    .icon-chevron { font-size:15px }

    /* ── Buttons ──────────────────────────────────────────────────────────────── */
    .btn-full  { width:100% }
    .btn-mb-12 { margin-bottom:12px }
    .btn-delete-soft { color:rgba(255,82,82,.5) }
    .btn-delete-xs   { color:rgba(255,82,82,.4); flex-shrink:0; width:20px; height:20px; padding:0 }
    .btn-delete-sm   { color:rgba(255,82,82,.5); width:28px; height:28px }
    .btn-notes       { width:24px; height:24px }

    /* ── Empty states ─────────────────────────────────────────────────────────── */
    .empty-state      { text-align:center; padding:64px 0 }
    .empty-state-text { font-size:1.1rem; color:var(--mat-sys-on-surface-variant); margin-bottom:8px }
    .sidebar-empty    { text-align:center; padding:32px 0; font-size:.875rem; color:var(--mat-sys-on-surface-variant) }
    .panel-empty-state {
      flex:1; display:flex; align-items:center; justify-content:center;
      color:var(--mat-sys-on-surface-variant); font-size:.875rem
    }
    .toms-empty { text-align:center; padding:16px 0; font-size:.78rem; color:var(--mat-sys-on-surface-variant) }

    /* ── Tab content wrapper ──────────────────────────────────────────────────── */
    .tab-content { margin-top:20px }

    /* ── Objects tab layout ───────────────────────────────────────────────────── */
    .objects-layout  { display:flex; gap:16px; min-height:500px; margin-top:20px }
    .objects-sidebar { width:280px; flex-shrink:0 }
    .obj-card {
      padding:10px; border-radius:8px; cursor:pointer;
      border:1px solid var(--mat-sys-outline-variant); transition:all .12s
    }
    .obj-card:hover { background:var(--mat-sys-surface-variant) }
    .obj-active { border-color:var(--mat-sys-primary)!important; background:rgba(0,120,255,.04) }
    .obj-name   {
      font-size:.82rem; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; flex:1
    }
    .obj-panel  {
      flex:1; border:1px solid var(--mat-sys-outline-variant); border-radius:8px;
      min-height:400px; overflow:hidden; display:flex
    }
    .panel-scroll { flex:1; overflow:auto; padding:20px }

    /* ── NIST function headers ────────────────────────────────────────────────── */
    .fn-group  { margin-bottom:16px }
    .fn-header {
      display:flex; align-items:center; gap:8px;
      margin-bottom:6px; padding-bottom:4px
    }
    .fn-dot   { width:8px; height:8px; border-radius:50%; flex-shrink:0 }
    .fn-label {
      font-size:.72rem; font-weight:700; text-transform:uppercase; letter-spacing:.05em
    }

    /* ── Requirement rows ─────────────────────────────────────────────────────── */
    .req-row { border-bottom:1px solid var(--mat-sys-outline-variant); padding:6px 0 }
    .req-row:last-child { border-bottom:none }
    .req-id-chip {
      display:inline-block; padding:2px 6px; border-radius:4px;
      font-size:.65rem; font-weight:700; border:1px solid
    }
    .req-title { font-size:.8rem; font-weight:500; flex:1; min-width:120px }
    .rating-btns { display:flex; gap:3px; flex-shrink:0; flex-wrap:wrap }
    .rating-btn {
      padding:3px 8px; border-radius:4px; cursor:pointer; font-size:.68rem; font-weight:400;
      border:1px solid var(--mat-sys-outline-variant); color:var(--mat-sys-on-surface-variant);
      transition:all .1s; white-space:nowrap
    }
    .rating-btn:hover { background:var(--mat-sys-surface-variant) }
    .rating-btn.active[data-status="met"]          { border-color:#4CAF5060; background:#4CAF5018; color:#4CAF50; font-weight:700 }
    .rating-btn.active[data-status="partial"]      { border-color:#FFC00060; background:#FFC00018; color:#856404; font-weight:700 }
    .rating-btn.active[data-status="not_met"]      { border-color:#FF704360; background:#FF704318; color:#FF7043; font-weight:700 }
    .rating-btn.active[data-status="exception"]    { border-color:#CE93D860; background:#CE93D818; color:#CE93D8; font-weight:700 }
    .rating-btn.active[data-status="not_assessed"] { border-color:rgba(0,0,0,.3); background:rgba(0,0,0,.05); font-weight:700 }
    .notes-panel { margin-top:8px; padding-left:52px; display:flex; flex-direction:column; gap:8px }

    /* ── Radio groups ─────────────────────────────────────────────────────────── */
    .radio-group-row { display:flex; gap:16px }

    /* ── Meta / edit boxes ────────────────────────────────────────────────────── */
    .meta-box {
      padding:16px; background:var(--mat-sys-surface-variant);
      border-radius:8px; border:1px solid var(--mat-sys-outline-variant)
    }

    /* ── Control Objectives card ──────────────────────────────────────────────── */
    .co-card-header {
      display:flex; align-items:flex-start; justify-content:space-between; gap:8px; margin-bottom:6px
    }
    .co-id    { font-weight:700; font-size:.7rem }
    .co-title { font-weight:600; font-size:.82rem; line-height:1.3 }
    .co-pct   { font-size:.72rem; font-weight:700 }

    /* ── Elevated TOMs section ────────────────────────────────────────────────── */
    .toms-section { margin-top:24px }
    .toms-label   { font-size:.65rem; font-weight:600; text-transform:uppercase; letter-spacing:.05em; color:#FF7043 }
    .toms-subtitle { font-size:.7rem; color:var(--mat-sys-on-surface-variant) }
    .new-tom-box {
      padding:12px; background:rgba(255,112,67,.04);
      border:1px solid rgba(255,112,67,.15); border-radius:8px; margin-bottom:12px
    }
    .tom-card { padding:10px; border:1px solid var(--mat-sys-outline-variant); border-radius:8px; margin-bottom:8px }
    .tom-desc { font-size:.8rem; margin-bottom:2px }

    /* ── Report tab ───────────────────────────────────────────────────────────── */
    .report-card-label { font-size:.68rem; color:var(--mat-sys-on-surface-variant) }
    .report-card-value { font-size:1.4rem; font-weight:700; margin-top:2px }
    .report-co-row   { display:flex; align-items:center; gap:16px }
    .report-co-id    { width:40px; font-weight:600; font-size:.78rem; color:var(--mat-sys-on-surface-variant) }
    .report-co-title { flex:1; font-size:.78rem }
    .report-co-pct   { width:36px; text-align:right; font-weight:600; font-size:.78rem }

    /* ── Gap table ────────────────────────────────────────────────────────────── */
    .gap-table { border:1px solid var(--mat-sys-outline-variant); border-radius:8px; overflow:hidden }
    .gap-row {
      display:grid; grid-template-columns:160px 80px 100px 1fr;
      gap:0; padding:6px 12px; border-bottom:1px solid var(--mat-sys-outline-variant)
    }
    .gap-row:last-child  { border-bottom:none }
    .gap-header          { background:var(--mat-sys-surface-variant); font-size:.7rem; font-weight:600 }
    .gap-object-cell     { overflow:hidden; text-overflow:ellipsis; white-space:nowrap; font-size:.78rem }
    .gap-req-id          { font-weight:600; font-size:.78rem }
    .gap-req-title       { font-size:.78rem; color:var(--mat-sys-on-surface-variant) }
    .req-status-chip     { display:inline-block; padding:2px 6px; border-radius:4px; font-size:.65rem }
    .req-status-chip[data-status="not_met"]   { background:#FF704318; color:#FF7043 }
    .req-status-chip[data-status="partial"]   { background:#FFC00018; color:#856404 }
    .req-status-chip[data-status="exception"] { background:#CE93D818; color:#CE93D8 }

    /* ── Banners ──────────────────────────────────────────────────────────────── */
    .info-banner    { padding:12px 16px; border-radius:8px; background:rgba(33,150,243,.08); border:1px solid rgba(33,150,243,.2); font-size:.82rem }
    .warn-banner    { padding:12px 16px; border-radius:8px; background:rgba(255,152,0,.08); border:1px solid rgba(255,152,0,.2); font-size:.82rem }
    .success-banner { padding:12px 16px; border-radius:8px; background:rgba(76,175,80,.08); border:1px solid rgba(76,175,80,.2); font-size:.82rem }

    /* ── Dialog ───────────────────────────────────────────────────────────────── */
    .overlay   { position:fixed; inset:0; background:rgba(0,0,0,.4); z-index:1000; display:flex; align-items:center; justify-content:center }
    .dlg-panel { background:var(--mat-sys-surface); border-radius:12px; padding:24px; min-width:480px; max-width:560px; max-height:90vh; overflow:auto }
    .dialog-title { margin:0 0 16px }
  `],
})
export class CsrmComponent {
  private http = inject(HttpClient)

  readonly ratingStatuses = RATING_STATUSES
  readonly RATING_LABELS = RATING_LABELS
  readonly tomStatuses = TOM_STATUSES
  readonly nistFunctions = NIST_FUNCTIONS
  readonly controlObjectives = CONTROL_OBJECTIVES
  readonly threatCategories = THREAT_CATEGORIES
  readonly assessedCount = assessedCount
  readonly metCount = metCount
  readonly pctColor = pctColor

  listLoading = signal(false)
  detailLoading = signal(false)
  savingAssess = signal(false)
  savingObj = signal(false)
  assessments = signal<CsrmAssessmentSummary[]>([])
  selectedId = signal<string | null>(null)
  detail = signal<AssessmentDetail | null>(null)
  selectedObjectId = signal<string | null>(null)
  activeTabIdx = 0

  disclaimerOpen = signal(false)
  editMeta = signal(false)
  editObjMeta = signal(false)
  newAssessmentOpen = signal(false)
  newObjectOpen = signal(false)
  newTomOpen = signal(false)
  notesOpen = signal<Set<string>>(new Set())

  notesDraft: Record<string, string> = {}
  justDraft: Record<string, string> = {}

  metaForm = { name: '', description: '', organisation: '', assessor: '', scope: '', status: 'draft' }
  objMetaForm = { name: '', description: '', architecture_notes: '', processes_served: '', data_classification: 'standard', protection_level: 'standard', elevated_rationale: '' }
  newAssessForm = { name: '', description: '', organisation: '', assessor: '', scope: '' }
  newObjForm = { name: '', description: '', architecture_notes: '', processes_served: '', data_classification: 'standard', protection_level: 'standard', elevated_rationale: '' }
  newTomForm = { threat_category: '', tom_description: '', notes: '' }

  selectedObject = computed(() => this.detail()?.objects.find(o => o.id === this.selectedObjectId()) ?? null)

  coPctFor(reqs: string[]): number | null { return coPct(this.detail()?.objects ?? [], reqs) }

  reportCards = computed(() => {
    const objs = this.detail()?.objects ?? []
    const totalObjs = objs.length
    const elevated = objs.filter(o => o.protection_level === 'elevated').length
    const fullyAssessed = objs.filter(o => assessedCount(o) === 20).length
    const pct = baselinePct(objs)
    return [
      { label: 'Protection Objects', value: totalObjs, color: undefined },
      { label: 'Elevated Objects', value: elevated, color: elevated > 0 ? '#FF7043' : undefined },
      { label: 'Fully Assessed', value: `${fullyAssessed}/${totalObjs}`, color: undefined },
      { label: 'Baseline Compliance', value: pct !== null ? `${pct}%` : '—', color: pctColor(pct) },
    ]
  })

  reportGaps = computed(() => {
    const objs = this.detail()?.objects ?? []
    const gaps: { object: string; fn: string; reqId: string; status: string; title: string }[] = []
    for (const obj of objs) {
      for (const req of BASELINE_REQUIREMENTS) {
        const r = getRating(obj, req.id)
        if (r && (r.status === 'not_met' || r.status === 'partial' || r.status === 'exception')) {
          gaps.push({ object: obj.name, fn: req.function, reqId: req.id, status: r.status, title: req.title })
        }
      }
    }
    return gaps
  })

  constructor() {
    this.loadList()
    effect(() => {
      const id = this.selectedId()
      if (id) this.loadDetail(id)
    })
  }

  private async loadList(): Promise<void> {
    this.listLoading.set(true)
    try {
      const data = await firstValueFrom(this.http.get<CsrmAssessmentSummary[]>('/api/v1/csrm/assessments'))
      this.assessments.set(data)
    } catch { } finally { this.listLoading.set(false) }
  }

  private async loadDetail(id: string): Promise<void> {
    this.detailLoading.set(true)
    this.selectedObjectId.set(null)
    try {
      const d = await firstValueFrom(this.http.get<AssessmentDetail>(`/api/v1/csrm/assessments/${id}`))
      this.detail.set(d)
      this.metaForm = { name: d.name, description: d.description ?? '', organisation: d.organisation ?? '', assessor: d.assessor ?? '', scope: d.scope ?? '', status: d.status }
    } catch { } finally { this.detailLoading.set(false) }
  }

  openAssessment(id: string): void { this.selectedId.set(id); this.activeTabIdx = 0 }

  closeDetail(): void { this.selectedId.set(null); this.detail.set(null); this.editMeta.set(false) }

  async createAssessment(): Promise<void> {
    if (!this.newAssessForm.name.trim()) return
    this.savingAssess.set(true)
    try {
      const a = await firstValueFrom(this.http.post<CsrmAssessmentSummary>('/api/v1/csrm/assessments', {
        name: this.newAssessForm.name, description: this.newAssessForm.description || null,
        organisation: this.newAssessForm.organisation || null, assessor: this.newAssessForm.assessor || null,
        scope: this.newAssessForm.scope || null,
      }))
      this.assessments.set([a, ...this.assessments()])
      this.newAssessmentOpen.set(false)
      this.newAssessForm = { name: '', description: '', organisation: '', assessor: '', scope: '' }
    } catch { } finally { this.savingAssess.set(false) }
  }

  async saveAssessmentMeta(): Promise<void> {
    if (!this.selectedId()) return
    await firstValueFrom(this.http.patch(`/api/v1/csrm/assessments/${this.selectedId()}`, {
      name: this.metaForm.name, description: this.metaForm.description || null,
      organisation: this.metaForm.organisation || null, assessor: this.metaForm.assessor || null,
      scope: this.metaForm.scope || null, status: this.metaForm.status,
    }))
    this.detail.update(d => d ? { ...d, ...this.metaForm } : d)
    this.assessments.update(prev => prev.map(a => a.id === this.selectedId() ? { ...a, name: this.metaForm.name, status: this.metaForm.status } : a))
    this.editMeta.set(false)
  }

  async confirmDelete(a: CsrmAssessmentSummary): Promise<void> {
    if (!confirm(`Delete assessment "${a.name}"? This cannot be undone.`)) return
    await firstValueFrom(this.http.delete(`/api/v1/csrm/assessments/${a.id}`))
    this.assessments.update(prev => prev.filter(x => x.id !== a.id))
    if (this.selectedId() === a.id) this.closeDetail()
  }

  async createObject(): Promise<void> {
    if (!this.selectedId() || !this.newObjForm.name.trim()) return
    this.savingObj.set(true)
    try {
      const obj = await firstValueFrom(this.http.post<ProtectionObject>(`/api/v1/csrm/assessments/${this.selectedId()}/objects`, {
        ...this.newObjForm,
        description: this.newObjForm.description || null,
        architecture_notes: this.newObjForm.architecture_notes || null,
        processes_served: this.newObjForm.processes_served || null,
        elevated_rationale: this.newObjForm.elevated_rationale || null,
        sort_order: this.detail()?.objects.length ?? 0,
      }))
      this.detail.update(d => d ? { ...d, objects: [...d.objects, obj] } : d)
      this.newObjectOpen.set(false)
      this.newObjForm = { name: '', description: '', architecture_notes: '', processes_served: '', data_classification: 'standard', protection_level: 'standard', elevated_rationale: '' }
    } catch { } finally { this.savingObj.set(false) }
  }

  async deleteObject(oid: string): Promise<void> {
    await firstValueFrom(this.http.delete(`/api/v1/csrm/objects/${oid}`))
    this.detail.update(d => d ? { ...d, objects: d.objects.filter(o => o.id !== oid) } : d)
    if (this.selectedObjectId() === oid) this.selectedObjectId.set(null)
  }

  toggleObjEdit(): void {
    const obj = this.selectedObject()
    if (obj) this.objMetaForm = {
      name: obj.name, description: obj.description ?? '', architecture_notes: obj.architecture_notes ?? '',
      processes_served: obj.processes_served ?? '', data_classification: obj.data_classification ?? 'standard',
      protection_level: obj.protection_level, elevated_rationale: obj.elevated_rationale ?? '',
    }
    this.editObjMeta.update(v => !v)
  }

  async saveObjMeta(): Promise<void> {
    const obj = this.selectedObject()
    if (!obj) return
    const updated = await firstValueFrom(this.http.patch<ProtectionObject>(`/api/v1/csrm/objects/${obj.id}`, {
      ...this.objMetaForm,
      description: this.objMetaForm.description || null,
      architecture_notes: this.objMetaForm.architecture_notes || null,
      processes_served: this.objMetaForm.processes_served || null,
      elevated_rationale: this.objMetaForm.elevated_rationale || null,
    }))
    this.detail.update(d => d ? { ...d, objects: d.objects.map(o => o.id === obj.id ? { ...updated, baseline_ratings: o.baseline_ratings, elevated_toms: o.elevated_toms } : o) } : d)
    this.editObjMeta.set(false)
  }

  async updateRating(reqId: string, status: string): Promise<void> {
    const obj = this.selectedObject()
    if (!obj) return
    const updated = await firstValueFrom(this.http.put<BaselineRating[]>(`/api/v1/csrm/objects/${obj.id}/ratings`, [{
      requirement_id: reqId, status, notes: this.notesDraft[reqId] ?? null, exception_justification: this.justDraft[reqId] ?? null,
    }]))
    this.detail.update(d => d ? { ...d, objects: d.objects.map(o => o.id === obj.id ? { ...o, baseline_ratings: updated } : o) } : d)
  }

  async saveNotes(reqId: string): Promise<void> {
    const obj = this.selectedObject()
    if (!obj) return
    const r = getRating(obj, reqId)
    if (!r) return
    const updated = await firstValueFrom(this.http.put<BaselineRating[]>(`/api/v1/csrm/objects/${obj.id}/ratings`, [{
      requirement_id: reqId, status: r.status, notes: this.notesDraft[reqId] || null, exception_justification: this.justDraft[reqId] || null,
    }]))
    this.detail.update(d => d ? { ...d, objects: d.objects.map(o => o.id === obj.id ? { ...o, baseline_ratings: updated } : o) } : d)
  }

  async addTom(): Promise<void> {
    const obj = this.selectedObject()
    if (!obj || !this.newTomForm.threat_category || !this.newTomForm.tom_description) return
    const tom = await firstValueFrom(this.http.post<ElevatedTom>(`/api/v1/csrm/objects/${obj.id}/toms`, {
      threat_category: this.newTomForm.threat_category, tom_description: this.newTomForm.tom_description, notes: this.newTomForm.notes || null,
    }))
    this.detail.update(d => d ? { ...d, objects: d.objects.map(o => o.id === obj.id ? { ...o, elevated_toms: [...o.elevated_toms, tom] } : o) } : d)
    this.newTomOpen.set(false)
    this.newTomForm = { threat_category: '', tom_description: '', notes: '' }
  }

  async patchTom(tomId: string, data: object): Promise<void> {
    const updated = await firstValueFrom(this.http.patch<ElevatedTom>(`/api/v1/csrm/toms/${tomId}`, data))
    const objId = updated.object_id
    this.detail.update(d => d ? { ...d, objects: d.objects.map(o => o.id === objId ? { ...o, elevated_toms: o.elevated_toms.map(t => t.id === tomId ? updated : t) } : o) } : d)
  }

  async deleteTom(tomId: string): Promise<void> {
    const obj = this.selectedObject()
    if (!obj) return
    await firstValueFrom(this.http.delete(`/api/v1/csrm/toms/${tomId}`))
    this.detail.update(d => d ? { ...d, objects: d.objects.map(o => o.id === obj.id ? { ...o, elevated_toms: o.elevated_toms.filter(t => t.id !== tomId) } : o) } : d)
  }

  toggleNotes(reqId: string): void {
    const s = new Set(this.notesOpen())
    if (s.has(reqId)) { s.delete(reqId) } else {
      s.add(reqId)
      const obj = this.selectedObject()
      const r = obj ? getRating(obj, reqId) : undefined
      this.notesDraft[reqId] = r?.notes ?? ''
      this.justDraft[reqId] = r?.exception_justification ?? ''
    }
    this.notesOpen.set(s)
  }

  hasNotes(reqId: string): boolean {
    const obj = this.selectedObject()
    if (!obj) return false
    const r = getRating(obj, reqId)
    return !!(r?.notes || r?.exception_justification)
  }

  getRatingFor(reqId: string): BaselineRating | undefined {
    const obj = this.selectedObject()
    return obj ? getRating(obj, reqId) : undefined
  }

  reqsForFn(fn: string) { return BASELINE_REQUIREMENTS.filter(r => r.function === fn) }
  fnColor(fn: string): string { return FUNCTION_COLORS[fn] ?? '#888' }
}
