import { Component, inject, signal, computed } from '@angular/core'
import { ActivatedRoute, Router } from '@angular/router'
import { firstValueFrom } from 'rxjs'
import { HttpClient } from '@angular/common/http'
import { JsonPipe, DecimalPipe, NgTemplateOutlet } from '@angular/common'
import { DomSanitizer, SafeHtml } from '@angular/platform-browser'

import { injectQuery, injectMutation, injectQueryClient } from '@tanstack/angular-query-experimental'

import { MatTabsModule } from '@angular/material/tabs'
import { MatCardModule } from '@angular/material/card'
import { MatTableModule } from '@angular/material/table'
import { MatButtonModule } from '@angular/material/button'
import { MatIconModule } from '@angular/material/icon'
import { MatChipsModule } from '@angular/material/chips'
import { MatProgressBarModule } from '@angular/material/progress-bar'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatDialogModule } from '@angular/material/dialog'

import { ControlsApiService } from '../../api/controls-api.service'
import { PoliciesApiService, PolicyContentResponse } from '../../api/policies-api.service'
import { AssessmentsApiService } from '../../api/assessments-api.service'
import { BiaApiService } from '../../api/bia-api.service'
import { ConnectorsApiService, ConnectorRead, ConnectorEvidenceRead } from '../../api/connectors-api.service'
import { GeneratorsApiService } from '../../api/generators-api.service'
import { ProductService } from '../../core/services/product.service'
import { ThemeService } from '../../core/services/theme.service'
import { StatusChipComponent } from '../../shared/components/status-chip.component'

// ── Local interfaces for the rich detail shape the backend actually returns ──

interface PolicyRow {
  id: string
  document_id: string
  title: string
  policy_type: string
  product_type: string
  requirements_count: number
  word_count: number
  source_label?: string | null
}

interface ImplRow {
  id: string
  document_id: string
  title: string
  impl_type: string
  word_count: number
}

interface ItemRow {
  id: string
  row_number: number
  item_text: string | null
  status: string
  owner: string | null
  due_date: string | null
  notes: string | null
}

interface SheetRow {
  id: string
  sheet_name: string
  sheet_type: string
  row_count: number
  items: ItemRow[]
}

interface AssessmentRow {
  id: string
  document_id: string
  workbook_name: string
  file_path: string
  product_type: string
  assessment_type: string
  sheets_count: number
  overall_score: number | null
  items_total: number
  items_compliant: number
  items_partial: number
  items_non_compliant: number
  items_na: number
  sheets: SheetRow[]
}

interface MappingRow {
  framework: string
  framework_code: string
  control_id: string
  control_title: string
  mapping_type: string
  confidence: number
}

interface IsoControlRow {
  control_id: string
  title: string
  description: string | null
  mappings: MappingRow[]
}

interface GapRow {
  id: string
  gap_type: string
  severity: string
  status: string
  description: string
}

interface EvidenceRow {
  id: string
  title: string
  evidence_type: string
  collected_date: string | null
  verified_by: string | null
}

interface RealControlDetail {
  id: string
  group_code: string
  folder_name: string
  name: string
  section: string
  section_name: string
  is_stacked: boolean
  has_framework: boolean
  has_operational: boolean
  framework_status: string
  operational_status: string
  stacked_control_ids: string[]
  policies: PolicyRow[]
  implementations: ImplRow[]
  assessments: AssessmentRow[]
  iso_controls: IsoControlRow[]
  gaps: GapRow[]
  evidence: EvidenceRow[]
  requirements_total: number
  gaps_open: number
  evidence_total: number
}

// ── Status cycle ──────────────────────────────────────────────────────────────

const STATUS_CYCLE = ['not_assessed', 'compliant', 'partial', 'non_compliant', 'na']
function nextStatus(current: string): string {
  const idx = STATUS_CYCLE.indexOf(current)
  return STATUS_CYCLE[(idx === -1 ? 1 : (idx + 1)) % STATUS_CYCLE.length]
}

const ITEM_STATUS_DARK: Record<string, { bg: string; color: string; label: string }> = {
  compliant:      { bg: 'rgba(198,239,206,0.15)', color: '#C6EFCE', label: '✓' },
  partial:        { bg: 'rgba(255,235,156,0.12)', color: '#FFEB9C', label: '~' },
  non_compliant:  { bg: 'rgba(255,199,206,0.15)', color: '#FFC7CE', label: '✗' },
  na:             { bg: 'rgba(100,100,100,0.12)', color: '#888',    label: 'N/A' },
  not_applicable: { bg: 'rgba(100,100,100,0.12)', color: '#888',    label: 'N/A' },
  not_assessed:   { bg: 'transparent',             color: '#555',    label: '—' },
}
const ITEM_STATUS_LIGHT: Record<string, { bg: string; color: string; label: string }> = {
  compliant:      { bg: 'rgba(46,125,50,0.10)',  color: '#1b5e20', label: '✓' },
  partial:        { bg: 'rgba(255,152,0,0.10)',   color: '#7a4800', label: '~' },
  non_compliant:  { bg: 'rgba(192,0,0,0.10)',     color: '#9e0000', label: '✗' },
  na:             { bg: 'rgba(100,100,100,0.08)', color: '#555',    label: 'N/A' },
  not_applicable: { bg: 'rgba(100,100,100,0.08)', color: '#555',    label: 'N/A' },
  not_assessed:   { bg: 'transparent',             color: '#888',    label: '—' },
}

const SECTION_COLORS: Record<string, string> = {
  'A.5': '#4472C4',
  'A.6': '#70AD47',
  'A.7': '#FFC000',
  'A.8': '#C00000',
}

function getSectionColor(section: string): string {
  return SECTION_COLORS[section] ?? '#4472C4'
}

function fmtDate(d: string | null | undefined): string {
  if (!d) return '—'
  return new Date(d).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' })
}

function markdownToHtml(md: string): string {
  const lines = md.split('\n')
  const out: string[] = []
  let inCodeBlock = false, inTable = false, inList = false, listType = ''
  const closePending = () => {
    if (inTable) { out.push('</tbody></table>'); inTable = false }
    if (inList)  { out.push(`</${listType}>`);   inList = false; listType = '' }
  }
  const escape = (s: string) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
  const inline = (s: string) => s
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.+?)\*/g, '<em>$1</em>')
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>')
  for (let i = 0; i < lines.length; i++) {
    const raw = lines[i]
    if (raw.startsWith('```')) {
      if (!inCodeBlock) { closePending(); out.push('<pre><code>'); inCodeBlock = true }
      else              { out.push('</code></pre>'); inCodeBlock = false }
      continue
    }
    if (inCodeBlock) { out.push(escape(raw)); continue }
    if (raw.trim() === '') { closePending(); continue }
    const hm = raw.match(/^(#{1,3})\s+(.+?)(?:\s+\{#[\w-]+\})?$/)
    if (hm) {
      closePending()
      out.push(`<h${hm[1].length}>${inline(hm[2].replace(/\{#[\w-]+\}/g, '').trim())}</h${hm[1].length}>`)
      continue
    }
    if (/^---+$/.test(raw.trim())) { closePending(); out.push('<hr>'); continue }
    if (raw.startsWith('> ')) { closePending(); out.push(`<blockquote>${inline(raw.slice(2))}</blockquote>`); continue }
    if (raw.includes('|')) {
      const cells = raw.split('|').map(c => c.trim()).filter((_, i, a) => i > 0 && i < a.length - 1)
      if (/^[\s|:-]+$/.test(raw)) continue
      if (!inTable) {
        closePending(); out.push('<table><thead><tr>')
        cells.forEach(c => out.push(`<th>${inline(c)}</th>`))
        out.push('</tr></thead><tbody>'); inTable = true
        if (i + 1 < lines.length && /^[\s|:-]+$/.test(lines[i + 1])) i++
      } else { out.push('<tr>'); cells.forEach(c => out.push(`<td>${inline(c)}</td>`)); out.push('</tr>') }
      continue
    }
    const ulm = raw.match(/^[-*+]\s+(.+)/)
    if (ulm) { if (!inList || listType !== 'ul') { closePending(); out.push('<ul>'); inList = true; listType = 'ul' } out.push(`<li>${inline(ulm[1])}</li>`); continue }
    const olm = raw.match(/^\d+\.\s+(.+)/)
    if (olm) { if (!inList || listType !== 'ol') { closePending(); out.push('<ol>'); inList = true; listType = 'ol' } out.push(`<li>${inline(olm[1])}</li>`); continue }
    closePending(); out.push(`<p>${inline(raw)}</p>`)
  }
  closePending()
  return out.join('\n')
}

// ─────────────────────────────────────────────────────────────────────────────

@Component({
  selector: 'app-control-detail',
  standalone: true,
  imports: [
    JsonPipe, DecimalPipe, NgTemplateOutlet,
    MatTabsModule, MatCardModule, MatTableModule,
    MatButtonModule, MatIconModule, MatChipsModule,
    MatProgressBarModule, MatProgressSpinnerModule,
    MatTooltipModule, MatDialogModule,
    StatusChipComponent,
  ],
  template: `
<div class="cd-page">

  <!-- Loading -->
  @if (controlQuery.isLoading()) {
    <div class="cd-loading">
      <mat-spinner diameter="40" />
    </div>
  }

  <!-- Error -->
  @if (controlQuery.isError()) {
    <div class="cd-error">Control not found or failed to load.</div>
  }

  @if (controlQuery.isSuccess() && cg()) {
    <!-- Breadcrumb -->
    <div class="cd-breadcrumb">
      <span class="cd-breadcrumb__link" (click)="router.navigate(['/'])">Overview</span>
      <span class="cd-breadcrumb__sep">›</span>
      <span class="cd-breadcrumb__link" (click)="router.navigate(['/controls'])">Controls</span>
      <span class="cd-breadcrumb__sep">›</span>
      <span class="cd-breadcrumb__current">{{ displayGroupCode() }}</span>
    </div>

    <!-- Header -->
    <div class="cd-header">
      <button mat-icon-button (click)="router.navigate(['/controls'])">
        <mat-icon>arrow_back</mat-icon>
      </button>

      <div class="cd-header__info">
        <div class="cd-header__chips">
          <span class="cd-mono" [style.color]="sectionColor()">{{ displayGroupCode() }}</span>
          <mat-chip-set>
            <mat-chip>{{ cg()!.section }}</mat-chip>
            <mat-chip>{{ cg()!.section_name }}</mat-chip>
            @if (cg()!.is_stacked) {
              <mat-chip class="cd-chip--stacked">Stacked: {{ cg()!.stacked_control_ids.join(', ') }}</mat-chip>
            }
          </mat-chip-set>
          <app-status-chip [status]="cg()!.framework_status" />
        </div>
        <h1 class="cd-header__title">{{ cg()!.name }}</h1>
      </div>

      <!-- Action buttons -->
      <div class="cd-header__actions">
        <button mat-icon-button
                [matTooltip]="'ISMS AI Assistant'"
                [class.cd-ai-btn--active]="aiOpen()"
                (click)="aiOpen.set(!aiOpen())">
          <mat-icon>auto_awesome</mat-icon>
        </button>
        <button mat-icon-button
                [matTooltip]="'Analyse with ISMS Compass'"
                (click)="router.navigate(['/compass'], { queryParams: { group: cg()!.group_code } })">
          <mat-icon>explore</mat-icon>
        </button>
      </div>

      <!-- Stats -->
      <div class="cd-header__stats">
        @for (stat of headerStats(); track stat.label) {
          <div class="cd-stat" [class.cd-stat--danger]="stat.danger">
            <span class="cd-stat__val">{{ stat.value }}</span>
            <span class="cd-stat__lbl">{{ stat.label }}</span>
          </div>
        }
      </div>
    </div>

    <!-- AI Placeholder -->
    @if (aiOpen()) {
      <div class="cd-ai-panel">
        <div class="cd-ai-panel__inner">
          <mat-icon class="cd-ai-panel__icon">auto_awesome</mat-icon>
          <div>
            <div class="cd-ai-panel__title">ISMS AI Assistant</div>
            <div class="cd-ai-panel__sub">Context: {{ cg()!.name }}</div>
          </div>
          <button mat-stroked-button disabled class="cd-ai-panel__chat-btn">Chat with AI</button>
        </div>
      </div>
    }

    <!-- Tabs -->
    <mat-card class="cd-tabs-card">
      <mat-tab-group [(selectedIndex)]="activeTab" animationDuration="0ms">

        <!-- 0: Policies -->
        <mat-tab [label]="'Policies (' + visiblePolicies().length + ')'">
          <div class="cd-tab-content">
            @if (visiblePolicies().length === 0) {
              <div class="cd-alert cd-alert--warn">No policies for the selected product.</div>
            }
            @for (pol of visiblePolicies(); track pol.id) {
              <div class="cd-doc-card" [class.cd-doc-card--external]="pol.product_type === 'external'" (click)="openPolicy(pol)">
                @if (pol.product_type === 'external') {
                  <div class="cd-doc-card__ext-label">
                    External Document{{ pol.source_label ? ' — ' + pol.source_label : '' }}
                  </div>
                }
                <div class="cd-doc-card__row">
                  <div>
                    <div class="cd-mono" [style.color]="pol.product_type === 'external' ? '#FFC000' : 'var(--mat-sys-primary)'">{{ pol.document_id }}</div>
                    <div class="cd-doc-card__name">{{ pol.title }}</div>
                  </div>
                  <div class="cd-doc-card__chips">
                    <mat-chip-set>
                      <mat-chip>{{ pol.policy_type }}</mat-chip>
                      @if (pol.product_type === 'external') {
                        <mat-chip class="cd-chip--ext">external</mat-chip>
                      } @else {
                        <mat-chip>{{ pol.product_type }}</mat-chip>
                      }
                      <mat-chip>{{ pol.word_count | number }}w</mat-chip>
                      @if (pol.requirements_count > 0) {
                        <mat-chip class="cd-chip--reqs">{{ pol.requirements_count }} reqs</mat-chip>
                      }
                    </mat-chip-set>
                  </div>
                </div>
              </div>
            }
          </div>
        </mat-tab>

        <!-- 1: Instructions -->
        <mat-tab [label]="'Instructions (' + visibleInstructions().length + ')'">
          <div class="cd-tab-content">
            @if (visibleInstructions().length === 0) {
              <div class="cd-alert cd-alert--info">No implementation guides (INS) for this control group.</div>
            }
            @for (ins of visibleInstructions(); track ins.id) {
              <div class="cd-doc-card cd-doc-card--ins" (click)="openPolicy(ins)">
                <div class="cd-doc-card__row">
                  <div>
                    <div class="cd-mono cd-mono--ins">{{ ins.document_id }}</div>
                    <div class="cd-doc-card__name">{{ ins.title }}</div>
                  </div>
                  <div class="cd-doc-card__chips">
                    <mat-chip-set>
                      <mat-chip class="cd-chip--ins">INS</mat-chip>
                      <mat-chip>{{ ins.word_count | number }}w</mat-chip>
                    </mat-chip-set>
                  </div>
                </div>
              </div>
            }
          </div>
        </mat-tab>

        <!-- 2: Implementations -->
        <mat-tab [label]="'Implementations (' + cg()!.implementations.length + ')'">
          <div class="cd-tab-content">
            @if (cg()!.implementations.length === 0) {
              <div class="cd-alert cd-alert--warn">No implementations for the selected product.</div>
            }
            <div class="cd-impl-grid">
              @for (impl of cg()!.implementations; track impl.id) {
                <div class="cd-impl-card" (click)="openImpl(impl)">
                  <div class="cd-impl-card__top">
                    <span class="cd-mono cd-mono--primary">{{ impl.document_id }}</span>
                    <mat-chip-set>
                      <mat-chip [class]="impl.impl_type === 'UG' ? 'cd-chip--ug' : 'cd-chip--tg'">{{ impl.impl_type }}</mat-chip>
                      <mat-chip>{{ impl.word_count | number }}w</mat-chip>
                    </mat-chip-set>
                  </div>
                  <div class="cd-impl-card__name">{{ impl.title }}</div>
                </div>
              }
            </div>
          </div>
        </mat-tab>

        <!-- 3: Assessments -->
        <mat-tab [label]="'Assessments (' + visibleAssessments().length + ')'">
          <div class="cd-tab-content">
            <!-- Platform Assessments section -->
            <div class="cd-section-header">
              <mat-icon class="cd-section-icon cd-section-icon--primary icon-md">assignment</mat-icon>
              <span class="cd-section-header__title">Conduct Assessment</span>
              <button mat-raised-button color="primary" class="cd-section-header__btn"
                      (click)="openNewAssessmentDialog()">
                <mat-icon>add</mat-icon>
                New Assessment
              </button>
            </div>

            @if (platformAssessments().length === 0) {
              <div class="cd-empty-cta" (click)="openNewAssessmentDialog()">
                <mat-icon class="cd-empty-cta__icon">add</mat-icon>
                <div class="cd-empty-cta__msg">No platform assessments yet — fill in your data directly, no Excel required.</div>
                <div class="cd-empty-cta__action">Click to start</div>
              </div>
            }

            @for (asmnt of platformAssessments(); track asmnt.id) {
              <div class="cd-assessment-card">
                <div class="cd-assessment-card__header">
                  <div class="cd-assessment-card__info">
                    <div class="cd-mono cd-mono--primary">{{ asmnt.document_id }}</div>
                    <div class="cd-assessment-card__name">{{ asmnt.workbook_name }}</div>
                    <div class="cd-assessment-card__chips">
                      <mat-chip-set>
                        <mat-chip class="cd-chip--platform">platform</mat-chip>
                        <mat-chip>{{ asmnt.items_total }} items</mat-chip>
                        @if (asmnt.overall_score != null) {
                          <mat-chip class="cd-chip--score">{{ asmnt.overall_score }}%</mat-chip>
                        }
                      </mat-chip-set>
                    </div>
                  </div>
                  <button mat-icon-button color="warn" [matTooltip]="'Delete assessment'"
                          (click)="confirmDeleteAssessment(asmnt.id, asmnt.workbook_name)">
                    <mat-icon class="icon-md">delete</mat-icon>
                  </button>
                </div>
                @if (asmnt.items_total > 0) {
                  <div class="cd-compliance-bar-wrap">
                    <ng-container *ngTemplateOutlet="complianceBarTpl; context: {
                      total: asmnt.items_total,
                      compliant: asmnt.items_compliant,
                      partial: asmnt.items_partial,
                      nonCompliant: asmnt.items_non_compliant,
                      na: asmnt.items_na
                    }" />
                  </div>
                } @else {
                  <div class="cd-assessment-card__no-items">No items yet — open assessment to start</div>
                }
              </div>
            }

            <!-- Imported Workbooks -->
            @if (uploadedAssessments().length > 0) {
              <div class="cd-section-header cd-section-header--mt">
                <mat-icon class="cd-section-icon cd-section-icon--muted icon-md">folder_open</mat-icon>
                <span class="cd-section-header__title cd-section-header__title--muted">Imported Workbooks</span>
              </div>
              @for (asmnt of uploadedAssessments(); track asmnt.id) {
                <div class="cd-assessment-card cd-assessment-card--imported">
                  <div class="cd-mono cd-mono--primary">{{ asmnt.document_id }}</div>
                  <div class="cd-assessment-card__name">{{ asmnt.workbook_name }}</div>
                  <div class="cd-assessment-card__chips cd-assessment-card__chips--spaced">
                    <mat-chip-set>
                      <mat-chip>{{ asmnt.assessment_type }}</mat-chip>
                      <mat-chip>{{ asmnt.product_type }}</mat-chip>
                      <mat-chip>{{ asmnt.sheets_count }} sheets</mat-chip>
                    </mat-chip-set>
                  </div>
                  <ng-container *ngTemplateOutlet="complianceBarTpl; context: {
                    total: asmnt.items_total,
                    compliant: asmnt.items_compliant,
                    partial: asmnt.items_partial,
                    nonCompliant: asmnt.items_non_compliant,
                    na: asmnt.items_na
                  }" />
                  <!-- Sheets -->
                  @for (sheet of asmnt.sheets; track sheet.id) {
                    <div class="cd-sheet">
                      <div class="cd-sheet__header">
                        <span class="cd-sheet__name">{{ sheet.sheet_name }}</span>
                        <mat-chip-set>
                          <mat-chip [class]="sheet.sheet_type === 'assessment' ? 'cd-chip--platform' : ''">{{ sheet.sheet_type }}</mat-chip>
                        </mat-chip-set>
                        @if (sheet.row_count > 0) {
                          <span class="cd-sheet__rows">{{ sheet.row_count }} rows</span>
                        }
                      </div>
                      @if (sheet.items.length > 0) {
                        <div class="cd-sheet__toggle" (click)="toggleSheet(sheet.id)">
                          <mat-icon class="icon-sm">{{ expandedSheets().has(sheet.id) ? 'expand_less' : 'expand_more' }}</mat-icon>
                          <span>{{ sheet.items.length }} checklist items</span>
                          <span class="cd-sheet__cycle-hint">click item to cycle status</span>
                        </div>
                        @if (expandedSheets().has(sheet.id)) {
                          <div class="cd-items-list">
                            @for (item of sheet.items; track item.id) {
                              <div class="cd-item"
                                   [style.background]="itemStatusColor(item.status).bg"
                                   [style.border-left-color]="itemStatusColor(item.status).color + '60'"
                                   (click)="cycleItemStatus(item)">
                                <span class="cd-item__label" [style.color]="itemStatusColor(item.status).color">
                                  {{ itemStatusColor(item.status).label }}
                                </span>
                                <span class="cd-item__text">{{ item.item_text ?? '—' }}</span>
                                @if (item.owner) {
                                  <span class="cd-item__owner">{{ item.owner }}</span>
                                }
                              </div>
                            }
                          </div>
                        }
                      }
                    </div>
                  }
                </div>
              }
            }
          </div>
        </mat-tab>

        <!-- 4: ISO Mappings -->
        <mat-tab [label]="'ISO Mappings (' + cg()!.iso_controls.length + ')'">
          <div class="cd-tab-content">
            @if (cg()!.is_stacked && cg()!.stacked_control_ids.length > 1) {
              <div class="cd-stacked-filter">
                <span class="cd-filter-label">Filter:</span>
                @for (sid of ['all', ...cg()!.stacked_control_ids]; track sid) {
                  <button mat-button
                          [class.cd-filter-btn--active]="stackedFilter() === sid"
                          (click)="stackedFilter.set(sid)">
                    {{ sid === 'all' ? 'All' : sid }}
                  </button>
                }
              </div>
            }
            @if (cg()!.iso_controls.length === 0) {
              <div class="cd-alert cd-alert--info">No ISO controls linked.</div>
            }
            @for (iso of filteredIsoControls(); track iso.control_id) {
              <div class="cd-iso-block">
                <div class="cd-iso-block__header">
                  <span class="cd-mono cd-mono--iso-id">{{ iso.control_id }}</span>
                  <span class="cd-iso-block__title">{{ iso.title }}</span>
                </div>
                @if (iso.description) {
                  <div class="cd-iso-block__desc">{{ iso.description }}</div>
                }
                @if (iso.mappings.length > 0) {
                  <div class="cd-iso-block__mappings">
                    <mat-chip-set>
                      @for (m of iso.mappings; track $index) {
                        <mat-chip class="cd-chip--mapping" [matTooltip]="m.framework + ': ' + m.control_title">
                          {{ m.control_id }}
                        </mat-chip>
                      }
                    </mat-chip-set>
                    <span class="cd-iso-block__count">
                      {{ iso.mappings.length }} mappings across {{ frameworkCount(iso.mappings) }} frameworks
                    </span>
                  </div>
                }
              </div>
            }
          </div>
        </mat-tab>

        <!-- 5: Evidence -->
        <mat-tab [label]="'Evidence (' + (cg()!.evidence_total + connectorEvidenceCount()) + ')'">
          <div class="cd-tab-content">

            <!-- Automated evidence -->
            <div class="cd-section-header">
              <mat-icon class="cd-section-icon cd-section-icon--primary icon-md">electrical_services</mat-icon>
              <span class="cd-section-header__title">Automated Evidence</span>
              <mat-chip-set class="cd-section-header__chip-set">
                <mat-chip class="cd-chip--platform">{{ connectorEvidenceCount() }} items</mat-chip>
              </mat-chip-set>
            </div>

            @if (connectorEvQuery.isLoading()) {
              <mat-progress-bar mode="indeterminate" />
            }

            @if (connectorEvidenceCount() === 0 && !connectorEvQuery.isLoading()) {
              <div class="cd-alert cd-alert--info">
                No automated evidence yet. Register a connector in <strong>Admin → Connectors</strong> to start pulling evidence automatically.
              </div>
            }

            @for (item of connectorEvidence(); track item.id) {
              <div class="cd-conn-ev">
                <div class="cd-conn-ev__header">
                  <div class="cd-conn-ev__info">
                    <div class="cd-conn-ev__title">{{ item.title }}</div>
                    <div class="cd-conn-ev__chips">
                      <mat-chip-set>
                        <mat-chip class="cd-chip--platform">
                          <mat-icon class="cd-conn-ev__chip-icon">electrical_services</mat-icon>
                          {{ resolveConnectorLabel(item.connector_id) }}
                        </mat-chip>
                        @if (item.classification) {
                          <mat-chip [style.color]="classColor(item.classification)">{{ item.classification }}</mat-chip>
                        }
                        @if (item.status) {
                          <mat-chip [style.color]="connStatusColor(item.status)">{{ item.status }}</mat-chip>
                        }
                        @if (item.source_ref) {
                          <span class="cd-mono cd-mono--source-ref">{{ item.source_ref }}</span>
                        }
                      </mat-chip-set>
                    </div>
                  </div>
                  <div class="cd-conn-ev__date">
                    {{ fmtDate(item.event_date ?? item.created_at) }}
                  </div>
                </div>
                <!-- View details toggle -->
                <div class="cd-conn-ev__toggle" (click)="toggleConnEv(item.id)">
                  <mat-icon class="icon-sm">{{ expandedConnEv().has(item.id) ? 'expand_less' : 'expand_more' }}</mat-icon>
                  <span>{{ expandedConnEv().has(item.id) ? 'Hide details' : 'View details' }}</span>
                </div>
                @if (expandedConnEv().has(item.id)) {
                  <div class="cd-conn-ev__detail">
                    <ng-container *ngTemplateOutlet="evidenceDetailTpl; context: { item: item }" />
                  </div>
                }
              </div>
            }

            <!-- Manual evidence -->
            <div class="cd-section-header cd-section-header--mt">
              <mat-icon class="cd-section-icon cd-section-icon--muted icon-md">folder_open</mat-icon>
              <span class="cd-section-header__title cd-section-header__title--muted">Manual Evidence</span>
              <mat-chip-set class="cd-section-header__chip-set">
                <mat-chip>{{ cg()!.evidence.length }} items</mat-chip>
              </mat-chip-set>
            </div>

            @if (cg()!.evidence.length === 0) {
              <div class="cd-alert cd-alert--info">No manual evidence linked yet. Upload evidence via the Evidence page.</div>
            }
            @for (ev of cg()!.evidence; track ev.id) {
              <div class="cd-ev-row">
                <div class="cd-ev-row__top">
                  <span class="cd-ev-row__title">{{ ev.title }}</span>
                  <app-status-chip [status]="ev.verified_by ? 'green' : 'not_assessed'" />
                </div>
                <div class="cd-ev-row__chips">
                  <mat-chip-set>
                    <mat-chip>{{ ev.evidence_type }}</mat-chip>
                  </mat-chip-set>
                  @if (ev.collected_date) {
                    <span class="cd-ev-row__date">{{ ev.collected_date }}</span>
                  }
                </div>
              </div>
            }
          </div>
        </mat-tab>

        <!-- 6: Gaps (conditional) -->
        @if (cg()!.gaps.length > 0) {
          <mat-tab [label]="'Gaps (' + cg()!.gaps.length + ')'">
            <div class="cd-tab-content">
              @for (gap of cg()!.gaps; track gap.id) {
                <div class="cd-gap-card">
                  <div class="cd-gap-card__chips">
                    <app-status-chip [status]="gap.severity" />
                    <app-status-chip [status]="gap.status" />
                    <span class="cd-gap-card__type">{{ gap.gap_type }}</span>
                  </div>
                  <div class="cd-gap-card__desc">{{ gap.description }}</div>
                </div>
              }
            </div>
          </mat-tab>
        }

        <!-- 7: BIA (conditional) -->
        @if (isBiaControl()) {
          <mat-tab [label]="'BIA (' + (biaQuery.data()?.length ?? 0) + ')'">
            <div class="cd-tab-content">
              @if (biaQuery.isLoading()) {
                <mat-progress-bar mode="indeterminate" />
              }
              @if (!biaQuery.data()?.length) {
                <div class="cd-empty cd-empty--bia">No BIA records. Add assets in the BIA module.</div>
              }
              @for (r of biaQuery.data() ?? []; track r.id) {
                <div class="cd-bia-card">
                  <div class="cd-bia-card__top">
                    <div>
                      <div class="cd-bia-card__name">{{ r.asset_name }}</div>
                      <div class="cd-bia-card__type">{{ r.asset_type }}</div>
                    </div>
                    <mat-chip-set>
                      <mat-chip [style.background]="r.recovery_tested ? '#4CAF5020' : '#FF980020'"
                                [style.color]="r.recovery_tested ? '#4CAF50' : '#FF9800'">
                        {{ r.recovery_tested ? 'Tested' : 'Not Tested' }}
                      </mat-chip>
                    </mat-chip-set>
                  </div>
                  <div class="cd-bia-card__metrics">
                    @if (r.rto_hours != null) { <span>RTO: <strong>{{ r.rto_hours }}h</strong></span> }
                    @if (r.rpo_hours != null) { <span>RPO: <strong>{{ r.rpo_hours }}h</strong></span> }
                    @if (r.mtpd_hours != null) { <span>MTPD: <strong>{{ r.mtpd_hours }}h</strong></span> }
                    <span>Avg Impact: <strong>{{ r.avg_impact.toFixed(1) }}</strong></span>
                  </div>
                </div>
              }
            </div>
          </mat-tab>
        }

      </mat-tab-group>
    </mat-card>

  }<!-- end isSuccess -->

</div><!-- cd-page -->

<!-- ── Compliance bar template ──────────────────────────────────────────────── -->
<ng-template #complianceBarTpl let-total="total" let-compliant="compliant" let-partial="partial" let-nonCompliant="nonCompliant" let-na="na">
  @if (total > 0) {
    <div class="cd-cbar">
      <div class="cd-cbar__track">
        @if (compliant > 0) { <div class="cd-cbar__seg cd-cbar__seg--compliant" [style.flex]="compliant"></div> }
        @if (partial > 0)   { <div class="cd-cbar__seg cd-cbar__seg--partial"   [style.flex]="partial"></div> }
        @if (nonCompliant > 0) { <div class="cd-cbar__seg cd-cbar__seg--nc"     [style.flex]="nonCompliant"></div> }
        @if (na > 0)        { <div class="cd-cbar__seg cd-cbar__seg--na"        [style.flex]="na"></div> }
      </div>
      <div class="cd-cbar__labels">
        <span>{{ total }} items</span>
        @if (compliant > 0) { <span class="cd-cbar__lbl--c">{{ compliant }} ✓</span> }
        @if (partial > 0)   { <span class="cd-cbar__lbl--p">{{ partial }} ~</span> }
        @if (nonCompliant > 0) { <span class="cd-cbar__lbl--nc">{{ nonCompliant }} ✗</span> }
        @if (na > 0)        { <span class="cd-cbar__lbl--na">{{ na }} N/A</span> }
      </div>
    </div>
  }
</ng-template>

<!-- ── Evidence detail template (simplified: JSON toggle) ──────────────────── -->
<ng-template #evidenceDetailTpl let-item="item">
  @if (item.raw) {
    <div class="cd-ev-detail">
      <button mat-button class="cd-ev-detail__toggle-btn" (click)="toggleRawJson(item.id)">
        <mat-icon class="icon-sm">{{ expandedJsonViews().has(item.id) ? 'expand_less' : 'expand_more' }}</mat-icon>
        {{ expandedJsonViews().has(item.id) ? 'Hide raw JSON' : 'View raw JSON' }}
      </button>
      @if (expandedJsonViews().has(item.id)) {
        <pre class="cd-ev-detail__json">{{ item.raw | json }}</pre>
      }
    </div>
  } @else {
    <div class="cd-ev-detail__no-data">No raw data available.</div>
  }
</ng-template>

<!-- ── Delete Assessment Dialog ─────────────────────────────────────────────── -->
@if (deleteTarget()) {
  <div class="cd-overlay" (click)="deleteTarget.set(null)">
    <div class="cd-dialog" (click)="$event.stopPropagation()">
      <h3 class="cd-dialog__title">Delete Platform Assessment?</h3>
      <p class="cd-dialog__body">
        <strong>{{ deleteTarget()!.name }}</strong> and all its data will be permanently removed.
        This cannot be undone.
      </p>
      @if (deleteMutation.isError()) {
        <div class="cd-alert cd-alert--error">Delete failed. Try again.</div>
      }
      <div class="cd-dialog__actions">
        <button mat-button (click)="deleteTarget.set(null)" [disabled]="deleteMutation.isPending()">Cancel</button>
        <button mat-raised-button color="warn"
                [disabled]="deleteMutation.isPending()"
                (click)="executeDelete()">
          <mat-icon>delete</mat-icon>
          {{ deleteMutation.isPending() ? 'Deleting…' : 'Delete' }}
        </button>
      </div>
    </div>
  </div>
}

<!-- ── Generator Picker Dialog ──────────────────────────────────────────────── -->
@if (generatorPickerOpen()) {
  <div class="cd-overlay" (click)="generatorPickerOpen.set(false)">
    <div class="cd-dialog" (click)="$event.stopPropagation()">
      <h3 class="cd-dialog__title">Choose Workbook to Assess</h3>
      <p class="cd-dialog__body cd-dialog__body--muted">This control group has multiple workbooks. Select which one to assess:</p>
      <div class="cd-picker-list">
        @for (gen of generatorsQuery.data() ?? []; track gen.document_id) {
          <div class="cd-picker-item"
               [class.cd-picker-item--selected]="pickerGeneratorId() === gen.document_id"
               (click)="pickerGeneratorId.set(gen.document_id)">
            <div class="cd-mono cd-mono--primary">{{ gen.document_id }}</div>
            <div class="cd-picker-item__name">{{ gen.workbook_name }}</div>
            <div class="cd-picker-item__meta">{{ gen.sheet_count }} sheets</div>
          </div>
        }
      </div>
      <div class="cd-dialog__actions">
        <button mat-button (click)="generatorPickerOpen.set(false)">Cancel</button>
        <button mat-raised-button color="primary"
                [disabled]="!pickerGeneratorId()"
                (click)="generatorPickerOpen.set(false); showNewAssessmentInfo()">
          Continue
        </button>
      </div>
    </div>
  </div>
}

<!-- ── Policy Reader Overlay ────────────────────────────────────────────────── -->
@if (policyReaderTarget()) {
  <div class="cd-overlay cd-overlay--reader" (click)="policyReaderTarget.set(null)">
    <div class="cd-reader" (click)="$event.stopPropagation()">
      <div class="cd-reader__header">
        <div class="cd-reader__title">
          <span class="cd-mono cd-mono--reader-id">{{ policyReaderTarget()!.docId }}</span>
          {{ policyReaderTarget()!.title }}
        </div>
        <button mat-icon-button (click)="policyReaderTarget.set(null)"><mat-icon>close</mat-icon></button>
      </div>
      @if (policyDetailQuery.isLoading()) {
        <div class="cd-reader__spinner"><mat-spinner diameter="28" /></div>
      }
      @if (policyDetailQuery.isError()) {
        <div class="cd-alert cd-alert--error">Failed to load policy content.</div>
      }
      @if (policyDetailQuery.data()) {
        <div class="cd-reader__body" [innerHTML]="policyHtml()"></div>
      }
    </div>
  </div>
}
  `,
  styles: [`
    .cd-page { padding: 0; }
    .cd-loading { display:flex; justify-content:center; padding:48px; }
    .cd-error { padding:24px; color:#f44336; }

    .cd-breadcrumb { display:flex; align-items:center; gap:6px; margin-bottom:16px; font-size:0.78rem; }
    .cd-breadcrumb__link { color:#888; cursor:pointer; }
    .cd-breadcrumb__link:hover { color:var(--mat-sys-primary); }
    .cd-breadcrumb__sep { color:#555; }
    .cd-breadcrumb__current { color:var(--mat-sys-primary); font-weight:600; }

    .cd-header { display:flex; align-items:flex-start; gap:12px; margin-bottom:24px; flex-wrap:wrap; }
    .cd-header__info { flex:1; min-width:0; }
    .cd-header__chips { display:flex; align-items:center; gap:8px; flex-wrap:wrap; margin-bottom:6px; }
    .cd-header__title { margin:0; font-size:1.4rem; font-weight:500; }
    .cd-header__actions { display:flex; gap:4px; flex-shrink:0; margin-top:4px; }
    .cd-header__stats { display:flex; gap:20px; flex-shrink:0; flex-wrap:wrap; }

    .cd-stat { text-align:center; }
    .cd-stat__val { display:block; font-size:1.4rem; font-weight:700; color:var(--mat-sys-primary); }
    .cd-stat__lbl { display:block; font-size:0.72rem; color:#888; }
    .cd-stat--danger .cd-stat__val { color:#f44336; }

    .cd-mono { font-family:monospace; font-size:0.8rem; }
    .cd-mono--primary { color:var(--mat-sys-primary); }
    .cd-mono--ins { color:#FFEB9C; }
    .cd-mono--iso-id { color:var(--mat-sys-primary); font-size:0.85rem; font-weight:700; }
    .cd-mono--source-ref { font-size:0.6rem; color:#666; align-self:center; }
    .cd-mono--reader-id { color:var(--mat-sys-primary); margin-right:8px; }

    .cd-ai-btn--active { color:#4472C4 !important; background:rgba(68,114,196,0.15) !important; }

    .cd-ai-panel { margin-bottom:16px; border:1px solid rgba(68,114,196,0.3); border-radius:8px; background:rgba(68,114,196,0.06); padding:12px 16px; }
    .cd-ai-panel__inner { display:flex; align-items:center; gap:12px; }
    .cd-ai-panel__icon { color:#4472C4; }
    .cd-ai-panel__title { font-weight:600; }
    .cd-ai-panel__sub { font-size:0.78rem; color:#888; }
    .cd-ai-panel__chat-btn { margin-left:auto; }

    .cd-tabs-card { overflow:hidden; }
    .cd-tab-content { padding:16px 0; }

    .cd-doc-card { margin-bottom:12px; padding:12px 16px; border-radius:8px; background:rgba(68,114,196,0.07); cursor:pointer; }
    .cd-doc-card:hover { background:rgba(68,114,196,0.14); }
    .cd-doc-card--external { background:rgba(255,192,0,0.06); border:1px solid rgba(255,192,0,0.25); }
    .cd-doc-card--external:hover { background:rgba(255,192,0,0.12); }
    .cd-doc-card--ins { background:rgba(255,192,0,0.06); border:1px solid rgba(255,192,0,0.15); }
    .cd-doc-card--ins:hover { background:rgba(255,192,0,0.10); }
    .cd-doc-card__ext-label { font-size:0.65rem; font-weight:600; color:#FFC000; margin-bottom:4px; }
    .cd-doc-card__row { display:flex; justify-content:space-between; align-items:flex-start; gap:8px; }
    .cd-doc-card__name { font-weight:600; font-size:0.9rem; margin-top:2px; }
    .cd-doc-card__chips { flex-shrink:0; }

    .cd-impl-grid { display:grid; grid-template-columns:repeat(auto-fill, minmax(280px,1fr)); gap:8px; }
    .cd-impl-card { padding:12px; background:rgba(68,114,196,0.07); border-radius:8px; cursor:pointer; }
    .cd-impl-card:hover { background:rgba(68,114,196,0.14); }
    .cd-impl-card__top { display:flex; justify-content:space-between; margin-bottom:4px; }
    .cd-impl-card__name { font-weight:600; font-size:0.88rem; line-height:1.3; }

    .cd-section-header { display:flex; align-items:center; gap:8px; margin-bottom:12px; }
    .cd-section-header--mt { margin-top:24px; }
    .cd-section-header__title { font-size:0.7rem; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; color:var(--mat-sys-primary); flex:1; }
    .cd-section-header__title--muted { color:#888; }
    .cd-section-header__btn { font-size:0.75rem; font-weight:600; }
    .cd-section-header__chip-set { margin-left:auto; }
    .cd-section-icon--primary { color:var(--mat-sys-primary); }
    .cd-section-icon--muted { color:#888; }

    .cd-empty-cta { padding:20px; border-radius:8px; border:1px dashed rgba(68,114,196,0.3); background:rgba(68,114,196,0.03); text-align:center; cursor:pointer; margin-bottom:12px; }
    .cd-empty-cta:hover { background:rgba(68,114,196,0.08); border-color:rgba(68,114,196,0.5); }
    .cd-empty-cta__icon { color:#888; display:block; margin-bottom:8px; }
    .cd-empty-cta__msg { color:#aaa; }
    .cd-empty-cta__action { color:var(--mat-sys-primary); margin-top:4px; font-size:0.8rem; }

    .cd-assessment-card { margin-bottom:12px; padding:12px 16px; background:rgba(68,114,196,0.06); border-radius:8px; border:1px solid rgba(68,114,196,0.12); }
    .cd-assessment-card--imported { background:rgba(68,114,196,0.05); border:none; }
    .cd-assessment-card__header { display:flex; align-items:flex-start; gap:8px; }
    .cd-assessment-card__info { flex:1; }
    .cd-assessment-card__name { font-weight:600; font-size:0.9rem; }
    .cd-assessment-card__chips { margin-top:4px; }
    .cd-assessment-card__chips--spaced { margin:4px 0 8px; }
    .cd-assessment-card__no-items { color:#666; font-size:0.78rem; margin-top:6px; }

    .cd-cbar { margin-top:8px; }
    .cd-cbar__track { display:flex; height:5px; border-radius:3px; overflow:hidden; background:rgba(255,255,255,0.06); }
    .cd-cbar__seg { flex-shrink:0; }
    .cd-cbar__seg--compliant { background:#4caf50; }
    .cd-cbar__seg--partial { background:#ff9800; }
    .cd-cbar__seg--nc { background:#f44336; }
    .cd-cbar__seg--na { background:#444; }
    .cd-cbar__labels { display:flex; gap:12px; margin-top:3px; font-size:0.72rem; color:#888; }
    .cd-cbar__lbl--c { color:#4caf50; }
    .cd-cbar__lbl--p { color:#ff9800; }
    .cd-cbar__lbl--nc { color:#f44336; }
    .cd-cbar__lbl--na { color:#666; }

    .cd-sheet { margin-top:6px; }
    .cd-sheet__header { display:flex; align-items:center; gap:8px; }
    .cd-sheet__name { font-weight:600; font-size:0.85rem; flex:1; }
    .cd-sheet__rows { font-size:0.75rem; color:#666; }
    .cd-sheet__toggle { display:flex; align-items:center; gap:4px; cursor:pointer; color:#666; font-size:0.78rem; padding:2px 4px; border-radius:4px; background:rgba(68,114,196,0.06); margin-top:2px; }
    .cd-sheet__toggle:hover { background:rgba(68,114,196,0.12); }
    .cd-sheet__cycle-hint { margin-left:auto; font-size:0.6rem; color:#444; }

    .cd-items-list { margin-top:4px; }
    .cd-item { display:flex; gap:8px; padding:3px 8px; border-bottom:1px solid rgba(255,255,255,0.04); cursor:pointer; border-left:2px solid transparent; }
    .cd-item:hover { background:rgba(68,114,196,0.08) !important; }
    .cd-item__label { font-weight:700; flex-shrink:0; min-width:20px; font-size:0.75rem; }
    .cd-item__text { flex:1; font-size:0.75rem; line-height:1.4; }
    .cd-item__owner { font-size:0.72rem; color:#666; flex-shrink:0; }

    .cd-stacked-filter { display:flex; align-items:center; gap:6px; flex-wrap:wrap; margin-bottom:12px; }
    .cd-filter-btn--active { color:var(--mat-sys-primary) !important; font-weight:700 !important; background:rgba(68,114,196,0.2) !important; }
    .cd-filter-label { font-size:0.8rem; color:#888; }

    .cd-iso-block { margin-bottom:16px; padding:12px 16px; background:rgba(68,114,196,0.07); border-radius:8px; }
    .cd-iso-block__header { display:flex; align-items:center; gap:8px; margin-bottom:4px; }
    .cd-iso-block__title { font-weight:600; font-size:0.9rem; }
    .cd-iso-block__desc { font-size:0.78rem; color:#888; font-style:italic; line-height:1.6; margin-bottom:8px; }
    .cd-iso-block__mappings { display:flex; flex-wrap:wrap; align-items:center; gap:6px; }
    .cd-iso-block__count { font-size:0.75rem; color:#888; }

    .cd-conn-ev { margin-bottom:8px; padding:12px 16px; border-radius:8px; background:rgba(68,114,196,0.06); border:1px solid rgba(68,114,196,0.12); }
    .cd-conn-ev__header { display:flex; align-items:flex-start; gap:8px; }
    .cd-conn-ev__info { flex:1; min-width:0; }
    .cd-conn-ev__title { font-weight:600; font-size:0.9rem; }
    .cd-conn-ev__chips { margin-top:4px; }
    .cd-conn-ev__date { font-size:0.72rem; color:#666; white-space:nowrap; flex-shrink:0; }
    .cd-conn-ev__toggle { display:flex; align-items:center; gap:4px; cursor:pointer; color:#666; font-size:0.75rem; margin-top:6px; }
    .cd-conn-ev__toggle:hover { color:#aaa; }
    .cd-conn-ev__detail { margin-top:6px; }
    .cd-conn-ev__chip-icon { font-size:11px; margin-right:2px; }

    .cd-ev-detail { }
    .cd-ev-detail__json { font-family:monospace; font-size:0.6rem; color:#C6EFCE; line-height:1.5; white-space:pre-wrap; word-break:break-all; background:rgba(0,0,0,0.35); border:1px solid rgba(255,255,255,0.06); border-radius:4px; padding:8px; max-height:240px; overflow:auto; margin-top:4px; }
    .cd-ev-detail__toggle-btn { font-size:0.7rem; color:#888; padding:0; }
    .cd-ev-detail__no-data { font-size:0.75rem; color:#666; }

    .cd-ev-row { margin-bottom:8px; padding:12px 16px; background:rgba(68,114,196,0.07); border-radius:8px; }
    .cd-ev-row__top { display:flex; justify-content:space-between; align-items:center; }
    .cd-ev-row__title { font-weight:600; font-size:0.9rem; }
    .cd-ev-row__chips { display:flex; gap:8px; margin-top:4px; align-items:center; }
    .cd-ev-row__date { font-size:0.78rem; color:#888; align-self:center; }

    .cd-gap-card { margin-bottom:8px; padding:12px 16px; background:rgba(192,0,0,0.08); border:1px solid rgba(255,199,206,0.15); border-radius:8px; }
    .cd-gap-card__chips { display:flex; gap:6px; align-items:center; margin-bottom:4px; }
    .cd-gap-card__desc { font-size:0.88rem; }
    .cd-gap-card__type { font-size:0.78rem; color:#888; }

    .cd-bia-card { margin-bottom:8px; padding:12px 16px; border:1px solid rgba(255,255,255,0.08); border-radius:8px; }
    .cd-bia-card__top { display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:8px; }
    .cd-bia-card__name { font-weight:600; }
    .cd-bia-card__type { font-size:0.78rem; color:#888; }
    .cd-bia-card__metrics { display:flex; gap:16px; font-size:0.78rem; color:#888; flex-wrap:wrap; }

    .cd-empty { }
    .cd-empty--bia { color:#888; font-size:0.9rem; }

    .cd-compliance-bar-wrap { }

    .cd-alert { padding:10px 14px; border-radius:6px; font-size:0.85rem; margin-bottom:8px; }
    .cd-alert--info { background:rgba(21,101,192,0.12); color:#64b5f6; }
    .cd-alert--warn { background:rgba(255,152,0,0.12); color:#ffb74d; }
    .cd-alert--error { background:rgba(192,0,0,0.12); color:#ef9a9a; margin-top:8px; }

    .cd-chip--stacked { background:rgba(255,192,0,0.15) !important; color:#FFEB9C !important; }
    .cd-chip--ext { background:rgba(255,192,0,0.15) !important; color:#FFC000 !important; }
    .cd-chip--ins { background:rgba(255,192,0,0.15) !important; color:#FFEB9C !important; }
    .cd-chip--reqs { background:rgba(46,125,50,0.12) !important; color:#C6EFCE !important; }
    .cd-chip--ug { background:rgba(46,125,50,0.12) !important; color:#C6EFCE !important; }
    .cd-chip--tg { background:rgba(230,160,0,0.12) !important; color:#FFEB9C !important; }
    .cd-chip--platform { background:rgba(68,114,196,0.2) !important; color:var(--mat-sys-primary) !important; }
    .cd-chip--score { background:rgba(46,125,50,0.12) !important; color:#C6EFCE !important; }
    .cd-chip--mapping { background:rgba(112,173,71,0.12) !important; color:#C6EFCE !important; font-size:0.68rem !important; }

    .cd-overlay { position:fixed; inset:0; background:rgba(0,0,0,0.6); z-index:1000; display:flex; align-items:center; justify-content:center; }
    .cd-dialog { background:#1e1e2e; border-radius:12px; padding:24px; max-width:480px; width:100%; box-shadow:0 8px 32px rgba(0,0,0,0.5); }
    .cd-dialog__title { margin:0 0 12px; font-size:1.1rem; font-weight:600; }
    .cd-dialog__body { margin:0 0 16px; font-size:0.9rem; color:#aaa; }
    .cd-dialog__body--muted { color:#888; }
    .cd-dialog__actions { display:flex; justify-content:flex-end; gap:8px; margin-top:16px; }

    .cd-picker-list { display:flex; flex-direction:column; gap:8px; margin-bottom:8px; }
    .cd-picker-item { padding:12px; border-radius:8px; cursor:pointer; border:1px solid rgba(255,255,255,0.08); background:rgba(68,114,196,0.05); }
    .cd-picker-item:hover { background:rgba(68,114,196,0.12); }
    .cd-picker-item--selected { border-color:var(--mat-sys-primary) !important; background:rgba(68,114,196,0.18) !important; }
    .cd-picker-item__name { font-weight:600; }
    .cd-picker-item__meta { font-size:0.78rem; color:#888; }

    .cd-overlay--reader { align-items:stretch; justify-content:flex-end; }
    .cd-reader { background:var(--mat-sys-surface); border-radius:12px 0 0 12px; padding:28px 32px; width:min(960px,75vw); box-shadow:-8px 0 32px rgba(0,0,0,0.5); display:flex; flex-direction:column; overflow:hidden; }
    .cd-reader__header { display:flex; align-items:center; gap:8px; margin-bottom:16px; border-bottom:1px solid var(--mat-sys-outline-variant); padding-bottom:12px; flex-shrink:0; }
    .cd-reader__title { font-size:0.95rem; font-weight:600; flex:1; }
    .cd-reader__body { font-size:0.82rem; line-height:1.8; overflow-y:auto; flex:1; }
    .cd-reader__spinner { display:flex; justify-content:center; padding:40px; }
    .cd-reader__body h1 { font-size:1rem; font-weight:700; margin:16px 0 8px; }
    .cd-reader__body h2 { font-size:0.9rem; font-weight:700; margin:14px 0 6px; border-bottom:1px solid var(--mat-sys-outline-variant); padding-bottom:4px; }
    .cd-reader__body h3 { font-size:0.82rem; font-weight:700; margin:12px 0 4px; }
    .cd-reader__body p { margin:0 0 10px; }
    .cd-reader__body ul, .cd-reader__body ol { margin:0 0 10px; padding-left:20px; }
    .cd-reader__body li { margin-bottom:3px; }
    .cd-reader__body code { background:rgba(68,114,196,0.12); padding:1px 5px; border-radius:3px; font-family:monospace; font-size:0.78rem; }
    .cd-reader__body pre { background:rgba(0,0,0,0.3); padding:10px; border-radius:6px; overflow-x:auto; margin:0 0 10px; }
    .cd-reader__body pre code { background:none; padding:0; }
    .cd-reader__body blockquote { border-left:3px solid var(--mat-sys-primary); padding-left:12px; color:var(--mat-sys-on-surface-variant); margin:0 0 10px; }
    .cd-reader__body table { width:100%; border-collapse:collapse; margin:0 0 10px; font-size:0.78rem; }
    .cd-reader__body th, .cd-reader__body td { border:1px solid var(--mat-sys-outline-variant); padding:4px 8px; text-align:left; }
    .cd-reader__body th { background:var(--mat-sys-surface-container); font-weight:600; }
    .cd-reader__body hr { border:none; border-top:1px solid var(--mat-sys-outline-variant); margin:16px 0; }
    .cd-reader__body a { color:var(--mat-sys-primary); }
  `],
})
export class ControlDetailComponent {
  private route = inject(ActivatedRoute)
  readonly router = inject(Router)
  private controlsApi = inject(ControlsApiService)
  private policiesApi = inject(PoliciesApiService)
  private assessmentsApi = inject(AssessmentsApiService)
  private biaApi = inject(BiaApiService)
  private connectorsApi = inject(ConnectorsApiService)
  private generatorsApi = inject(GeneratorsApiService)
  private product = inject(ProductService)
  private theme = inject(ThemeService)
  private sanitizer = inject(DomSanitizer)
  private http = inject(HttpClient)
  private queryClient = injectQueryClient()

  // ── Route resolution ──────────────────────────────────────────────────────

  private readonly routeId = this.route.snapshot.paramMap.get('id')
  private readonly routeCode = this.route.snapshot.paramMap.get('code')
  private readonly identifier = this.routeCode ?? this.routeId ?? ''
  private readonly isCode = !!this.routeCode

  // ── State ─────────────────────────────────────────────────────────────────

  activeTab = 0
  readonly expandedSheets = signal<Set<string>>(new Set())
  readonly stackedFilter = signal<string>('all')
  readonly aiOpen = signal(false)
  readonly deleteTarget = signal<{ id: string; name: string } | null>(null)
  readonly generatorPickerOpen = signal(false)
  readonly pickerGeneratorId = signal('')
  readonly expandedConnEv = signal<Set<string>>(new Set())
  readonly expandedJsonViews = signal<Set<string>>(new Set())
  readonly policyReaderTarget = signal<{ id: string; title: string; docId: string; kind: 'policy' | 'impl' } | null>(null)

  // ── Queries ───────────────────────────────────────────────────────────────

  readonly controlQuery = injectQuery(() => ({
    queryKey: ['control', this.identifier],
    queryFn: () => this.isCode
      ? firstValueFrom(this.controlsApi.getByCode(this.identifier))
      : firstValueFrom(this.controlsApi.get(this.identifier)),
    enabled: !!this.identifier,
  }))

  readonly cg = computed<RealControlDetail | null>(() => {
    const d = this.controlQuery.data()
    return d ? (d as unknown as RealControlDetail) : null
  })

  readonly generatorsQuery = injectQuery(() => ({
    queryKey: ['generators-for-group', this.cg()?.group_code ?? ''],
    queryFn: () => firstValueFrom(this.generatorsApi.list({ group_code: this.cg()!.group_code })),
    enabled: !!this.cg(),
  }))

  readonly connectorEvQuery = injectQuery(() => ({
    queryKey: ['connector-evidence', this.cg()?.group_code ?? ''],
    queryFn: () => firstValueFrom(
      this.http.get<ConnectorEvidenceRead[]>(
        `/api/v1/connectors/evidence/${this.cg()!.group_code}`,
        { params: { limit: 100 } }
      )
    ),
    enabled: !!this.cg(),
    refetchInterval: 60_000,
  }))

  readonly connectorListQuery = injectQuery(() => ({
    queryKey: ['connectors-list'],
    queryFn: () => firstValueFrom(this.connectorsApi.list()),
    staleTime: 30_000,
  }))

  readonly biaQuery = injectQuery(() => ({
    queryKey: ['bia-for-control', this.cg()?.id ?? ''],
    queryFn: () => firstValueFrom(this.biaApi.list()),
    enabled: !!this.cg() && this.isBiaControl(),
  }))

  // ── Mutations ─────────────────────────────────────────────────────────────

  readonly statusMutation = injectMutation(() => ({
    mutationFn: ({ itemId, status }: { itemId: string; status: string }) =>
      firstValueFrom(this.assessmentsApi.updateItem(itemId, { status })),
    onSuccess: () => this.queryClient.invalidateQueries({ queryKey: ['control', this.identifier] }),
  }))

  readonly deleteMutation = injectMutation(() => ({
    mutationFn: (id: string) => firstValueFrom(this.assessmentsApi.delete(id)),
    onSuccess: () => {
      this.deleteTarget.set(null)
      this.queryClient.invalidateQueries({ queryKey: ['control', this.identifier] })
    },
  }))

  readonly policyDetailQuery = injectQuery(() => ({
    queryKey: ['doc-content', this.policyReaderTarget()?.id],
    queryFn: () => {
      const t = this.policyReaderTarget()!
      return firstValueFrom(t.kind === 'impl' ? this.policiesApi.getImplContent(t.id) : this.policiesApi.getContent(t.id))
    },
    enabled: !!this.policyReaderTarget(),
    staleTime: 300_000,
  }))

  readonly policyHtml = computed<SafeHtml>(() => {
    const content = (this.policyDetailQuery.data() as PolicyContentResponse | undefined)?.content ?? ''
    return this.sanitizer.bypassSecurityTrustHtml(markdownToHtml(content))
  })

  // ── Computed ──────────────────────────────────────────────────────────────

  readonly connectorEvidence = computed<ConnectorEvidenceRead[]>(() => this.connectorEvQuery.data() ?? [])
  readonly connectorEvidenceCount = computed(() => this.connectorEvidence().length)
  readonly connectorList = computed<ConnectorRead[]>(() => this.connectorListQuery.data() ?? [])

  readonly isBiaControl = computed(() => {
    const gc = this.cg()?.group_code ?? ''
    return gc.startsWith('a.5.29') || gc.startsWith('a.5.30')
  })

  readonly sectionColor = computed(() => getSectionColor(this.cg()?.section ?? ''))

  readonly displayGroupCode = computed(() => {
    const cg = this.cg()
    if (!cg) return ''
    const stripped = (cg.folder_name ?? '').replace(/^isms-/i, '')
    const m = stripped.match(/^(a\.[\d.]+(?:-[\d.]+)*)/i)
    if (!m) return cg.group_code.toUpperCase()
    const folderCode = m[1].toUpperCase()
    return folderCode !== cg.group_code.toUpperCase() ? folderCode : cg.group_code.toUpperCase()
  })

  readonly productView = this.product.product

  readonly visiblePolicies = computed(() => {
    const cg = this.cg()
    if (!cg) return []
    const pv = this.productView()
    return cg.policies.filter(p =>
      p.policy_type !== 'INS' && (
        pv === 'isms'
          ? ['framework', 'operational'].includes(p.product_type)
          : p.product_type === pv
      )
    )
  })

  readonly visibleInstructions = computed(() =>
    this.cg()?.policies.filter(p => p.policy_type === 'INS') ?? []
  )

  readonly visibleAssessments = computed(() => {
    const cg = this.cg()
    if (!cg) return []
    const pv = this.productView()
    return cg.assessments.filter(a => pv === 'isms' || a.product_type === pv)
  })

  readonly platformAssessments = computed(() =>
    this.visibleAssessments().filter(a =>
      a.file_path === 'platform:webui' || a.document_id.startsWith('ISMS-ASS-')
    )
  )

  readonly uploadedAssessments = computed(() =>
    this.visibleAssessments().filter(a =>
      !(a.file_path === 'platform:webui' || a.document_id.startsWith('ISMS-ASS-'))
    )
  )

  readonly filteredIsoControls = computed(() => {
    const cg = this.cg()
    if (!cg) return []
    const f = this.stackedFilter()
    if (f === 'all') return cg.iso_controls
    return cg.iso_controls.filter(iso => iso.control_id.startsWith(f))
  })

  readonly headerStats = computed(() => {
    const cg = this.cg()
    if (!cg) return []
    return [
      { label: 'Policies',     value: cg.policies.length,                          danger: false },
      { label: 'Impls',        value: cg.implementations.length,                   danger: false },
      { label: 'Assessments',  value: cg.assessments.length,                       danger: false },
      { label: 'ISO Controls', value: cg.iso_controls.length,                      danger: false },
      { label: 'Evidence',     value: cg.evidence_total + this.connectorEvidenceCount(), danger: false },
      { label: 'Open Gaps',    value: cg.gaps_open,                                danger: cg.gaps_open > 0 },
    ]
  })

  // ── Methods ───────────────────────────────────────────────────────────────

  readonly fmtDate = fmtDate

  itemStatusColor(status: string): { bg: string; color: string; label: string } {
    const map = this.theme.isDark() ? ITEM_STATUS_DARK : ITEM_STATUS_LIGHT
    return map[status] ?? map['not_assessed']
  }

  cycleItemStatus(item: ItemRow): void {
    const next = nextStatus(item.status)
    this.statusMutation.mutate({ itemId: item.id, status: next })
    // Optimistically update the local model
    item.status = next
  }

  toggleSheet(sheetId: string): void {
    this.expandedSheets.update(set => {
      const next = new Set(set)
      next.has(sheetId) ? next.delete(sheetId) : next.add(sheetId)
      return next
    })
  }

  toggleConnEv(id: string): void {
    this.expandedConnEv.update(set => {
      const next = new Set(set)
      next.has(id) ? next.delete(id) : next.add(id)
      return next
    })
  }

  toggleRawJson(id: string): void {
    this.expandedJsonViews.update(set => {
      const next = new Set(set)
      next.has(id) ? next.delete(id) : next.add(id)
      return next
    })
  }

  frameworkCount(mappings: MappingRow[]): number {
    return new Set(mappings.map(m => m.framework)).size
  }

  resolveConnectorLabel(connectorId: string): string {
    const conn = this.connectorList().find(c => c.id === connectorId)
    return conn?.name ?? connectorId.slice(0, 8) + '…'
  }

  classColor(cls: string): string {
    const DARK: Record<string, string> = {
      incident: '#FFC7CE', change: '#FFEB9C', asset: '#C6EFCE',
      user: '#BDD7EE', vulnerability: '#F4CCFF', network: '#FFD966', policy: '#CFE2F3',
    }
    const LIGHT: Record<string, string> = {
      incident: '#9e0000', change: '#7a4800', asset: '#1b5e20',
      user: '#1565c0', vulnerability: '#6a1b9a', network: '#e65100', policy: '#0d47a1',
    }
    const map = this.theme.isDark() ? DARK : LIGHT
    return map[cls] ?? (this.theme.isDark() ? '#BDD7EE' : '#1565c0')
  }

  connStatusColor(status: string): string {
    const DARK: Record<string, string> = {
      active: '#C6EFCE', compliant: '#C6EFCE', 'attention-required': '#FFEB9C',
      'non-compliant': '#FFC7CE', open: '#FFC7CE', resolved: '#C6EFCE',
    }
    const LIGHT: Record<string, string> = {
      active: '#1b5e20', compliant: '#1b5e20', 'attention-required': '#7a4800',
      'non-compliant': '#9e0000', open: '#9e0000', resolved: '#1b5e20',
    }
    const map = this.theme.isDark() ? DARK : LIGHT
    return map[status] ?? (this.theme.isDark() ? '#BDD7EE' : '#1565c0')
  }

  openPolicy(pol: PolicyRow): void {
    this.policyReaderTarget.set({ id: pol.id, title: pol.title, docId: pol.document_id, kind: 'policy' })
  }

  openImpl(impl: ImplRow): void {
    this.policyReaderTarget.set({ id: impl.id, title: impl.title, docId: impl.document_id, kind: 'impl' })
  }

  confirmDeleteAssessment(id: string, name: string): void {
    this.deleteTarget.set({ id, name })
  }

  executeDelete(): void {
    const t = this.deleteTarget()
    if (t) this.deleteMutation.mutate(t.id)
  }

  openNewAssessmentDialog(): void {
    const gens = this.generatorsQuery.data() ?? []
    if (gens.length > 1) {
      this.pickerGeneratorId.set('')
      this.generatorPickerOpen.set(true)
    } else {
      this.showNewAssessmentInfo()
    }
  }

  showNewAssessmentInfo(): void {
    // AssessmentFormDrawer is a complex React component not yet ported.
    // For now, navigate to the generators page for the group.
    const cg = this.cg()
    if (cg) {
      this.router.navigate(['/generators'], { queryParams: { group_code: cg.group_code } })
    }
  }
}
