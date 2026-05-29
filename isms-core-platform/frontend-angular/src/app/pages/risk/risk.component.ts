import { Component, inject, signal, computed } from '@angular/core'
import { ThemeService } from '../../core/services/theme.service'
import { FormsModule } from '@angular/forms'
import { DecimalPipe } from '@angular/common'

import { MatButtonModule } from '@angular/material/button'
import { MatIconModule } from '@angular/material/icon'
import { MatStepperModule } from '@angular/material/stepper'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatRadioModule } from '@angular/material/radio'
import { MatCheckboxModule } from '@angular/material/checkbox'
import { MatCardModule } from '@angular/material/card'
import { MatTableModule } from '@angular/material/table'
import { MatDividerModule } from '@angular/material/divider'

import { PageHeaderComponent } from '../../shared/components/page-header.component'

// ── Constants ─────────────────────────────────────────────────────────────────

const STEPS = [
  'Organisation Scope',
  'Asset Classification',
  'Confidentiality',
  'Integrity',
  'Availability',
  'Threat Profile',
  'Current Controls',
  'Risk Report',
]

const ASSET_TYPES = [
  'PII/Personal Data',
  'Financial Records',
  'Intellectual Property',
  'Operational Systems/SCADA',
  'Authentication Credentials',
  'Business Communications',
  'Third-party Data',
  'Audit Logs',
]

const THREAT_OPTIONS = [
  'External cyber attack',
  'Insider threat',
  'Ransomware/malware',
  'Physical theft/loss',
  'Supply chain compromise',
  'Social engineering/phishing',
  'Accidental data loss',
  'Natural disaster/outage',
  'Regulatory/compliance breach',
]

const CONTROL_OPTIONS = [
  'Access Control (A.5.15-18)',
  'Cryptography (A.8.24-25)',
  'Incident Management (A.5.24-28)',
  'Physical Security (A.7.1-14)',
  'Supplier Management (A.5.19-23)',
  'Vulnerability Management (A.8.8)',
  'Logging & Monitoring (A.8.15-16)',
  'Business Continuity (A.5.29-30)',
  'Awareness Training (A.6.3)',
]

const CIA_LABELS: Record<number, string> = {
  1: '1 — None',
  2: '2 — Low',
  3: '3 — Medium',
  4: '4 — High',
  5: '5 — Critical',
}

// ── Helpers ───────────────────────────────────────────────────────────────────

interface Recommendation {
  ref: string
  name: string
}

function deriveRecommendations(
  assets: string[], threats: string[],
  cScore: number, iScore: number, aScore: number,
): Recommendation[] {
  const seen = new Set<string>()
  const results: Recommendation[] = []

  function add(ref: string, name: string) {
    if (!seen.has(ref)) { seen.add(ref); results.push({ ref, name }) }
  }

  if (assets.includes('PII/Personal Data')) {
    add('A.5.34', 'Privacy and protection of PII')
    add('A.8.11', 'Data masking')
    add('A.8.10', 'Information deletion')
  }
  if (assets.includes('Financial Records')) {
    add('A.5.31', 'Legal, statutory, regulatory and contractual requirements')
    add('A.5.33', 'Protection of records')
  }
  if (assets.includes('Intellectual Property')) {
    add('A.5.32', 'Intellectual property rights')
    add('A.5.33', 'Protection of records')
  }
  if (assets.includes('Authentication Credentials')) {
    add('A.5.15', 'Access control policy')
    add('A.5.16', 'Identity management')
    add('A.5.17', 'Authentication information')
  }
  if (threats.includes('External cyber attack')) {
    add('A.8.7',  'Protection against malware')
    add('A.8.23', 'Web filtering')
    add('A.8.22', 'Segregation of networks')
  }
  if (threats.includes('Insider threat')) {
    add('A.6.2',  'Terms and conditions of employment')
    add('A.5.18', 'Access rights')
    add('A.8.18', 'Use of privileged utility programs')
  }
  if (threats.includes('Ransomware/malware')) {
    add('A.8.7',  'Protection against malware')
    add('A.8.13', 'Information backup')
    add('A.5.29', 'Information security during disruption')
  }
  if (threats.includes('Supply chain compromise')) {
    add('A.5.19', 'Information security in supplier relationships')
    add('A.5.21', 'Managing information security in the ICT supply chain')
  }
  if (threats.includes('Social engineering/phishing')) {
    add('A.6.3', 'Information security awareness, education and training')
    add('A.6.4', 'Disciplinary process')
  }
  if (cScore >= 4) { add('A.8.24', 'Use of cryptography'); add('A.8.11', 'Data masking') }
  if (iScore >= 4) { add('A.8.9',  'Configuration management'); add('A.5.37', 'Documented operating procedures') }
  if (aScore >= 4) {
    add('A.5.29', 'Information security during disruption')
    add('A.8.14', 'Redundancy of information processing facilities')
    add('A.8.16', 'Monitoring activities')
  }
  return results
}

function nextStepsForLevel(level: string): string[] {
  switch (level) {
    case 'Critical': return [
      'Initiate an immediate risk treatment plan — assign owners and deadlines within 48 hours.',
      'Escalate to senior management and document in the risk register.',
      'Implement compensating controls for the highest-impact gaps before the next assessment cycle.',
      'Schedule an emergency ISO 27001 internal review within 30 days.',
    ]
    case 'High': return [
      'Prioritise implementation of the recommended controls within the current quarter.',
      'Document identified gaps in the formal risk register with severity ratings.',
      'Engage relevant control owners and agree remediation milestones.',
      'Review supplier and third-party agreements for relevant clauses.',
    ]
    case 'Medium': return [
      'Schedule remediation activities into the next planning cycle.',
      'Review and update the ISMS scope statement if new asset types were identified.',
      'Ensure awareness training covers the identified threat vectors.',
      'Conduct a targeted internal audit on the weakest control areas.',
    ]
    default: return [
      'Maintain current controls and schedule periodic review.',
      'Continue monitoring for changes in the threat landscape.',
      'Ensure evidence of effective controls is kept up to date.',
    ]
  }
}

function riskBannerStyle(level: string, isDark: boolean): { bg: string; fg: string } {
  if (isDark) {
    if (level === 'Critical') return { bg: '#3a0000', fg: '#FFC7CE' }
    if (level === 'High')     return { bg: '#3a1a00', fg: '#FFD580' }
    if (level === 'Medium')   return { bg: '#3a2e00', fg: '#FFEB9C' }
    return                           { bg: '#1a3a27', fg: '#C6EFCE' }
  } else {
    if (level === 'Critical') return { bg: 'rgba(192,0,0,0.12)',   fg: '#9e0000' }
    if (level === 'High')     return { bg: 'rgba(192,0,0,0.08)',   fg: '#b71c1c' }
    if (level === 'Medium')   return { bg: 'rgba(230,145,0,0.15)', fg: '#7a4800' }
    return                           { bg: 'rgba(46,125,50,0.12)', fg: '#1b5e20' }
  }
}

function exportRiskCsv(data: {
  scope: string; businessFunction: string; assets: string[];
  cScore: number; iScore: number; aScore: number;
  rawRisk: number; riskLevel: string;
  threats: string[]; controls: string[];
  recommendations: Recommendation[];
}) {
  const rows = [
    ['field', 'value'],
    ['scope', data.scope.replace(/,/g, ';')],
    ['business_function', data.businessFunction.replace(/,/g, ';')],
    ['assets_in_scope', data.assets.join(' | ')],
    ['confidentiality_score', String(data.cScore)],
    ['integrity_score', String(data.iScore)],
    ['availability_score', String(data.aScore)],
    ['risk_score', data.rawRisk.toFixed(2)],
    ['risk_level', data.riskLevel],
    ['threats_identified', data.threats.join(' | ')],
    ['controls_in_place', data.controls.join(' | ')],
    ['recommended_controls', data.recommendations.map(r => `${r.ref} ${r.name}`).join(' | ')],
  ]
  const csv = rows.map(r => r.join(',')).join('\n')
  const today = new Date().toISOString().slice(0, 10).replace(/-/g, '')
  const url = URL.createObjectURL(new Blob([csv], { type: 'text/csv' }))
  const a = document.createElement('a')
  a.href = url
  a.download = `isms-risk-assessment-${today}.csv`
  a.click()
  URL.revokeObjectURL(url)
}

// ── Component ─────────────────────────────────────────────────────────────────

@Component({
  selector: 'app-risk',
  standalone: true,
  imports: [
    FormsModule, DecimalPipe,
    MatButtonModule, MatIconModule, MatStepperModule,
    MatFormFieldModule, MatInputModule, MatRadioModule,
    MatCheckboxModule, MatCardModule, MatTableModule, MatDividerModule,
    PageHeaderComponent,
  ],
  template: `
    <div class="risk-page">
    <app-page-header
      title="Risk Assessment Wizard"
      subtitle="CIA-based risk classification · ISO/IEC 27001:2022">
    </app-page-header>

    <mat-card>
      <mat-card-content>

        <!-- Stepper header -->
        <div class="stepper-header">
          @for (step of steps; track $index) {
            <div class="step-item">
              <!-- connector line (left) -->
              @if ($index > 0) {
                <div class="step-connector step-connector-left"
                     [style.background]="$index <= activeStep() ? 'var(--mat-sys-primary)' : 'rgba(255,255,255,0.12)'"></div>
              }
              <!-- connector line (right) -->
              @if ($index < steps.length - 1) {
                <div class="step-connector step-connector-right"
                     [style.background]="$index < activeStep() ? 'var(--mat-sys-primary)' : 'rgba(255,255,255,0.12)'"></div>
              }
              <!-- circle -->
              <div class="step-circle"
                   [style.background]="$index < activeStep() ? 'var(--mat-sys-primary)' : $index === activeStep() ? 'var(--mat-sys-primary)' : 'rgba(255,255,255,0.12)'"
                   [style.color]="$index <= activeStep() ? 'var(--mat-sys-on-primary)' : 'var(--mat-sys-on-surface-variant)'">
                @if ($index < activeStep()) {
                  <mat-icon class="step-check-icon">check</mat-icon>
                } @else {
                  {{ $index + 1 }}
                }
              </div>
              <div class="step-label"
                   [style.color]="$index === activeStep() ? 'var(--mat-sys-primary)' : 'var(--mat-sys-on-surface-variant)'"
                   [style.font-weight]="$index === activeStep() ? '600' : '400'">
                {{ step }}
              </div>
            </div>
          }
        </div>

        <!-- Step content -->
        <div class="step-content">
          <h6 class="step-title">{{ steps[activeStep()] }}</h6>

          <!-- Step 0: Org scope -->
          @if (activeStep() === 0) {
            <div class="step-col-gap">
              <mat-form-field appearance="outline" class="field-full">
                <mat-label>Systems / processes in scope</mat-label>
                <textarea matInput [(ngModel)]="scope" rows="3"
                  placeholder="e.g. HR platform, payroll system, customer database"
                  required></textarea>
              </mat-form-field>
              <mat-form-field appearance="outline" class="field-full">
                <mat-label>Primary business function</mat-label>
                <input matInput [(ngModel)]="businessFunction"
                  placeholder="e.g. Financial services, healthcare administration, e-commerce"
                  required />
              </mat-form-field>
            </div>
          }

          <!-- Step 1: Asset classification -->
          @if (activeStep() === 1) {
            <div>
              <div class="step-hint">
                Select all asset types present in scope
              </div>
              <div class="grid-2col">
                @for (a of assetTypes; track a) {
                  <mat-checkbox
                    [checked]="assets().includes(a)"
                    (change)="toggleItem(assets, a)">
                    <span class="cb-label">{{ a }}</span>
                  </mat-checkbox>
                }
              </div>
            </div>
          }

          <!-- Step 2: Confidentiality -->
          @if (activeStep() === 2) {
            <div>
              <div class="step-hint">
                How sensitive is the data if disclosed?
              </div>
              <mat-radio-group [ngModel]="cScore()" (ngModelChange)="cScore.set($event)" class="radio-col">
                @for (v of ciaValues; track v) {
                  <mat-radio-button [value]="v"><span class="cb-label">{{ ciaLabels[v] }}</span></mat-radio-button>
                }
              </mat-radio-group>
            </div>
          }

          <!-- Step 3: Integrity -->
          @if (activeStep() === 3) {
            <div>
              <div class="step-hint">
                How severe is the impact if data is altered or corrupted?
              </div>
              <mat-radio-group [ngModel]="iScore()" (ngModelChange)="iScore.set($event)" class="radio-col">
                @for (v of ciaValues; track v) {
                  <mat-radio-button [value]="v"><span class="cb-label">{{ ciaLabels[v] }}</span></mat-radio-button>
                }
              </mat-radio-group>
            </div>
          }

          <!-- Step 4: Availability -->
          @if (activeStep() === 4) {
            <div>
              <div class="step-hint">
                How severe is the impact if systems are unavailable?
              </div>
              <mat-radio-group [ngModel]="aScore()" (ngModelChange)="aScore.set($event)" class="radio-col">
                @for (v of ciaValues; track v) {
                  <mat-radio-button [value]="v"><span class="cb-label">{{ ciaLabels[v] }}</span></mat-radio-button>
                }
              </mat-radio-group>
            </div>
          }

          <!-- Step 5: Threat profile -->
          @if (activeStep() === 5) {
            <div>
              <div class="step-hint">
                Select all applicable threats to your environment
              </div>
              <div class="grid-2col">
                @for (t of threatOptions; track t) {
                  <mat-checkbox
                    [checked]="threats().includes(t)"
                    (change)="toggleItem(threats, t)">
                    <span class="cb-label">{{ t }}</span>
                  </mat-checkbox>
                }
              </div>
            </div>
          }

          <!-- Step 6: Current controls -->
          @if (activeStep() === 6) {
            <div>
              <div class="step-hint">
                Which ISO 27001 control areas are already in place?
              </div>
              <div class="col-gap-4">
                @for (c of controlOptions; track c) {
                  <mat-checkbox
                    [checked]="controls().includes(c)"
                    (change)="toggleItem(controls, c)">
                    <span class="cb-label">{{ c }}</span>
                  </mat-checkbox>
                }
              </div>
            </div>
          }

          <!-- Step 7: Risk report -->
          @if (activeStep() === 7) {
            <div>
              <!-- Risk score banner -->
              <div class="risk-banner"
                   [style.background]="riskColors().bg"
                   [style.border]="'1px solid ' + riskColors().fg + '40'">
                <div class="risk-score-block">
                  <div class="risk-score-num" [style.color]="riskColors().fg">{{ rawRisk() | number:'1.1-1' }}</div>
                  <div class="risk-score-lbl" [style.color]="riskColors().fg">Risk Score</div>
                </div>
                <div>
                  <span class="risk-level-badge"
                        [style.background]="riskColors().bg"
                        [style.color]="riskColors().fg"
                        [style.border]="'1px solid ' + riskColors().fg + '80'">
                    {{ riskLevel() }}
                  </span>
                  <div class="risk-summary" [style.color]="riskColors().fg">
                    CIA max {{ ciaMax() }} · {{ threats().length }} threat{{ threats().length !== 1 ? 's' : '' }} · {{ controls().length }} control{{ controls().length !== 1 ? 's' : '' }} in place
                  </div>
                </div>
              </div>

              <!-- CIA breakdown -->
              <div class="section-label">CIA Breakdown</div>
              <table class="cia-table">
                <tbody>
                  @for (row of ciaBreakdown(); track row.label) {
                    <tr class="cia-row">
                      <td class="cia-td cia-td-label">{{ row.label }}</td>
                      <td class="cia-td">{{ ciaLabels[row.score] }}</td>
                    </tr>
                  }
                </tbody>
              </table>

              <mat-divider class="divider-mb"></mat-divider>

              <!-- Recommendations -->
              <div class="section-label section-label-mb">
                Top Recommended ISO 27001 Controls
              </div>
              @if (recommendations().length === 0) {
                <div class="no-recs">
                  No specific recommendations — current profile is low risk with controls in place.
                </div>
              } @else {
                <div class="rec-chips">
                  @for (r of recommendations(); track r.ref) {
                    <span class="rec-chip">
                      {{ r.ref }} — {{ r.name }}
                    </span>
                  }
                </div>
              }

              <mat-divider class="divider-mb"></mat-divider>

              <!-- Next steps -->
              <div class="section-label section-label-mb">Next Steps</div>
              <ul class="next-steps-list">
                @for (step of nextSteps(); track $index) {
                  <li class="next-step-item">{{ step }}</li>
                }
              </ul>

              <!-- Export -->
              <div class="export-row">
                <button mat-stroked-button (click)="exportCsv()">
                  <mat-icon>file_download</mat-icon>
                  Export CSV
                </button>
                <button mat-button class="start-over-btn" (click)="reset()">
                  <mat-icon>restart_alt</mat-icon>
                  Start Over
                </button>
              </div>
            </div>
          }
        </div>

        <!-- Navigation -->
        @if (activeStep() < steps.length - 1) {
          <div class="nav-row">
            <button mat-stroked-button [disabled]="activeStep() === 0" (click)="back()">Back</button>
            <button mat-raised-button color="primary" [disabled]="!canAdvance()" (click)="next()">
              {{ activeStep() === steps.length - 2 ? 'Calculate Risk' : 'Next' }}
            </button>
          </div>
        } @else {
          <button mat-stroked-button class="back-btn-mt" (click)="back()">Back</button>
        }

      </mat-card-content>
    </mat-card>
    </div>
  `,
  styles: [`
    :host { display: block; }
    .risk-page { display: flex; flex-direction: column; gap: 16px; }

    /* Stepper */
    .stepper-header { display: flex; gap: 0; margin-bottom: 32px; overflow-x: auto; }
    .step-item { display: flex; flex-direction: column; align-items: center; flex: 1; min-width: 80px; position: relative; }
    .step-connector { position: absolute; top: 14px; height: 2px; }
    .step-connector-left { right: 50%; left: -1px; }
    .step-connector-right { left: 50%; right: -1px; }
    .step-circle { width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.72rem; font-weight: 700; z-index: 1; }
    .step-check-icon { font-size: 14px; width: 14px; height: 14px; }
    .step-label { margin-top: 6px; font-size: 0.7rem; text-align: center; line-height: 1.2; }

    /* Step content */
    .step-content { min-height: 280px; margin-bottom: 24px; }
    .step-title { margin: 0 0 20px; font-size: 1rem; font-weight: 500; }
    .step-col-gap { display: flex; flex-direction: column; gap: 20px; }
    .field-full { width: 100%; }
    .step-hint { font-size: 0.88rem; color: var(--mat-sys-on-surface-variant); margin-bottom: 12px; }
    .grid-2col { display: grid; grid-template-columns: 1fr 1fr; gap: 4px; }
    .radio-col { display: flex; flex-direction: column; gap: 4px; }
    .col-gap-4 { display: flex; flex-direction: column; gap: 4px; }
    .cb-label { font-size: 0.88rem; }

    /* Risk banner */
    .risk-banner { display: flex; align-items: center; gap: 24px; margin-bottom: 24px; padding: 20px; border-radius: 8px; }
    .risk-score-block { text-align: center; min-width: 80px; }
    .risk-score-num { font-size: 3rem; font-weight: 800; line-height: 1; }
    .risk-score-lbl { font-size: 0.65rem; opacity: 0.7; margin-top: 2px; }
    .risk-level-badge { font-size: 1rem; font-weight: 800; padding: 4px 12px; border-radius: 16px; display: inline-block; margin-bottom: 4px; }
    .risk-summary { font-size: 0.8rem; opacity: 0.8; }

    /* CIA breakdown */
    .section-label { font-size: 0.72rem; font-weight: 600; color: var(--mat-sys-on-surface-variant); text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 8px; }
    .section-label-mb { margin-bottom: 12px; }
    .cia-table { width: 100%; border-collapse: collapse; margin-bottom: 24px; font-size: 0.82rem; }
    .cia-row { border-bottom: 1px solid rgba(68,114,196,0.15); }
    .cia-td { padding: 6px 0; }
    .cia-td-label { font-weight: 600; width: 160px; }

    /* Divider spacing */
    .divider-mb { margin-bottom: 16px; }

    /* Recommendations */
    .no-recs { font-size: 0.88rem; color: var(--mat-sys-on-surface-variant); }
    .rec-chips { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 24px; }
    .rec-chip { font-size: 0.72rem; font-weight: 600; padding: 2px 8px; border-radius: 4px; height: 22px; line-height: 18px; background: rgba(21,101,192,0.12); color: #9fc8f0; border: 1px solid rgba(33,150,243,0.2); }

    /* Next steps */
    .next-steps-list { margin: 0; padding-left: 20px; }
    .next-step-item { margin-bottom: 6px; font-size: 0.88rem; }

    /* Export */
    .export-row { margin-top: 24px; display: flex; gap: 12px; }
    .start-over-btn { color: var(--mat-sys-on-surface-variant); }

    /* Navigation */
    .nav-row { display: flex; gap: 12px; }
    .back-btn-mt { margin-top: 8px; }
  `],
})
export class RiskComponent {
  private readonly theme = inject(ThemeService)
  private readonly isDark = computed(() => this.theme.isDark())

  // Expose constants to template
  steps          = STEPS
  assetTypes     = ASSET_TYPES
  threatOptions  = THREAT_OPTIONS
  controlOptions = CONTROL_OPTIONS
  ciaLabels      = CIA_LABELS
  ciaValues      = [1, 2, 3, 4, 5]

  // State
  activeStep = signal(0)

  scope            = ''
  businessFunction = ''

  assets   = signal<string[]>([])
  cScore   = signal(3)
  iScore   = signal(3)
  aScore   = signal(3)
  threats  = signal<string[]>([])
  controls = signal<string[]>([])

  // ── Computed risk values ───────────────────────────────────────────────────

  ciaMax = (): number => Math.max(this.cScore(), this.iScore(), this.aScore())

  rawRisk = (): number => {
    const threatScore      = Math.min(this.threats().length  * 0.3, 2.0)
    const controlsDiscount = Math.min(this.controls().length * 0.2, 1.5)
    return Math.max(1, Math.min(5, this.ciaMax() + threatScore - controlsDiscount))
  }

  riskLevel = (): string => {
    const r = this.rawRisk()
    if (r >= 4.5) return 'Critical'
    if (r >= 3.5) return 'High'
    if (r >= 2.5) return 'Medium'
    if (r >= 1.5) return 'Low'
    return 'Minimal'
  }

  recommendations = (): Recommendation[] =>
    deriveRecommendations(this.assets(), this.threats(), this.cScore(), this.iScore(), this.aScore())

  nextSteps = (): string[] => nextStepsForLevel(this.riskLevel())

  riskColors = (): { bg: string; fg: string } => riskBannerStyle(this.riskLevel(), this.isDark())

  ciaBreakdown = (): { label: string; score: number }[] => [
    { label: 'Confidentiality', score: this.cScore() },
    { label: 'Integrity',       score: this.iScore() },
    { label: 'Availability',    score: this.aScore() },
  ]

  // ── Navigation ────────────────────────────────────────────────────────────

  canAdvance(): boolean {
    if (this.activeStep() === 0) {
      return this.scope.trim().length > 0 && this.businessFunction.trim().length > 0
    }
    return true
  }

  next() {
    if (this.activeStep() < STEPS.length - 1) this.activeStep.update(s => s + 1)
  }

  back() {
    if (this.activeStep() > 0) this.activeStep.update(s => s - 1)
  }

  reset() {
    this.activeStep.set(0)
    this.scope            = ''
    this.businessFunction = ''
    this.assets.set([])
    this.cScore.set(3)
    this.iScore.set(3)
    this.aScore.set(3)
    this.threats.set([])
    this.controls.set([])
  }

  // ── Toggle helpers ────────────────────────────────────────────────────────

  toggleItem(list: ReturnType<typeof signal<string[]>>, item: string) {
    list.update(prev =>
      prev.includes(item) ? prev.filter(x => x !== item) : [...prev, item]
    )
  }

  // ── Export ────────────────────────────────────────────────────────────────

  exportCsv() {
    exportRiskCsv({
      scope:            this.scope,
      businessFunction: this.businessFunction,
      assets:           this.assets(),
      cScore:           this.cScore(),
      iScore:           this.iScore(),
      aScore:           this.aScore(),
      rawRisk:          this.rawRisk(),
      riskLevel:        this.riskLevel(),
      threats:          this.threats(),
      controls:         this.controls(),
      recommendations:  this.recommendations(),
    })
  }
}
