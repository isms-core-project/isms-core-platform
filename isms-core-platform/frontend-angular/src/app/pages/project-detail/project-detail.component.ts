import { Component, inject, signal, computed, effect } from '@angular/core'
import { ActivatedRoute, Router } from '@angular/router'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'

import { injectQuery, injectMutation, injectQueryClient } from '@tanstack/angular-query-experimental'

import { MatTabsModule } from '@angular/material/tabs'
import { MatCardModule } from '@angular/material/card'
import { MatButtonModule } from '@angular/material/button'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatTableModule } from '@angular/material/table'
import { MatIconModule } from '@angular/material/icon'
import { MatChipsModule } from '@angular/material/chips'
import { MatProgressBarModule } from '@angular/material/progress-bar'
import { MatDividerModule } from '@angular/material/divider'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatDialogModule } from '@angular/material/dialog'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatCheckboxModule } from '@angular/material/checkbox'
import { MatSlideToggleModule } from '@angular/material/slide-toggle'

import { HttpClient } from '@angular/common/http'
import { ProjectService } from '../../core/services/project.service'
import { ProjectRead } from '../../shared/types'
import { PageHeaderComponent } from '../../shared/components/page-header.component'
import { RichTextEditorComponent } from '../../shared/components/rich-text-editor.component'

// ── Types ─────────────────────────────────────────────────────────────────────

interface DocVars {
  ciso_name?: string
  ceo_name?: string
  dpo_name?: string
  legal_entity?: string
  effective_date?: string
  review_date?: string
  classification?: string
}

interface ProjectFull extends ProjectRead {
  product_family: string
  project_subtype?: string | null
  doc_vars?: DocVars | null
  policy_count: number
  implementation_count: number
  checklist_count: number
  assessment_count: number
  status: string
}

interface ProjectPolicyRead {
  id: string
  document_id: string | null
  title: string | null
  policy_type: string | null
  control_group_code: string | null
  is_edited: boolean
  stacking_locked: boolean
  stale_warning: boolean
  status: string
}

interface ProjectImplRead {
  id: string
  document_id: string | null
  title: string | null
  impl_type: string | null
  control_group_code: string | null
  is_edited: boolean
  stale_warning: boolean
  status: string
}

interface LibraryPolicyItem {
  id: string
  document_id: string
  title: string
  policy_type: string
  control_group_code: string
  is_stacked: boolean
  already_in_project: boolean
  language?: string
}

interface LibraryImplItem {
  id: string
  document_id: string
  title: string
  impl_type: string
  control_group_code: string
  already_in_project: boolean
}

interface LibraryChecklistItem {
  id: string
  document_id: string
  title: string
  product_type: string
  control_group_code: string
  item_count: number
  already_in_project: boolean
}

interface ProjectChecklistRead {
  id: string
  control_group_code: string
  control_group_name: string
  product_type: string
  title: string | null
  item_count: number
  na_count: number
  items?: ChecklistItem[]
}

interface ChecklistItem {
  id: string
  row_number: number
  item_text: string | null
  na: boolean
  justification: string | null
}

// ── Constants ─────────────────────────────────────────────────────────────────

const FAMILY_COLOR: Record<string, string> = {
  ISMS: '#4472C4',
  PRIVACY: '#70309f',
  CLOUD: '#0099cc',
}

const TOTAL_CG: Record<string, number> = { ISMS: 53, PRIVACY: 21, CLOUD: 12 }

const POL_TYPE_COLOR: Record<string, string> = {
  POL: '#4472C4',
  'OP-POL': '#70AD47',
  INS: '#9E9E9E',
}

const IMPL_TYPE_COLOR: Record<string, string> = {
  UG: '#4472C4',
  TG: '#ED7D31',
}

const PT_COLOR: Record<string, string> = {
  framework: '#4472C4',
  operational: '#70AD47',
  privacy: '#70309f',
  cloud: '#0099cc',
}

// ── Component ─────────────────────────────────────────────────────────────────

@Component({
  selector: 'app-project-detail',
  standalone: true,
  imports: [
    FormsModule,
    MatTabsModule, MatCardModule, MatButtonModule, MatFormFieldModule,
    MatInputModule, MatSelectModule, MatTableModule, MatIconModule,
    MatChipsModule, MatProgressBarModule, MatDividerModule, MatTooltipModule,
    MatDialogModule, MatProgressSpinnerModule, MatCheckboxModule,
    MatSlideToggleModule,
    PageHeaderComponent, RichTextEditorComponent,
  ],
  styles: [`
    :host { display: block; padding-bottom: 40px; }
    .breadcrumb { display: flex; align-items: center; gap: 8px; margin-bottom: 16px; font-size: 0.8rem; }
    .breadcrumb-link { color: var(--mat-sys-on-surface-variant); cursor: pointer; }
    .breadcrumb-link:hover { color: var(--mat-sys-on-surface); }
    .breadcrumb-sep { color: var(--mat-sys-outline); }
    .breadcrumb-cur { font-weight: 600; }

    .stat-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }
    .stat-card {
      padding: 12px 16px; border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 8px; text-align: center;
      background: var(--mat-sys-surface-container);
    }
    .stat-val { font-size: 1.6rem; font-weight: 700; line-height: 1; margin-bottom: 4px; }
    .stat-label { font-size: 0.67rem; color: var(--mat-sys-on-surface-variant); }

    .completeness-card {
      padding: 16px; border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 8px; margin-bottom: 16px;
      background: var(--mat-sys-surface-container);
    }
    .completeness-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; }
    .completeness-pct { font-size: 1.4rem; font-weight: 700; line-height: 1; }
    .completeness-section-label { font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: var(--mat-sys-on-surface-variant); }
    .bar-row { margin-bottom: 8px; }
    .bar-row-header { display: flex; justify-content: space-between; margin-bottom: 3px; font-size: 0.69rem; color: var(--mat-sys-on-surface-variant); }

    .doc-vars-panel {
      border: 1px solid var(--mat-sys-outline-variant); border-radius: 8px;
      overflow: hidden; margin-bottom: 20px;
    }
    .doc-vars-panel.has-missing { border-color: #FF9800; }
    .doc-vars-header {
      display: flex; align-items: center; gap: 8px; padding: 10px 16px;
      cursor: pointer; background: rgba(255,255,255,0.02);
    }
    .doc-vars-header:hover { background: rgba(255,255,255,0.04); }
    .doc-vars-body { padding: 12px 16px 16px; }
    .doc-vars-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 12px; }
    .doc-vars-actions { display: flex; gap: 8px; flex-wrap: wrap; }

    .toolbar { display: flex; align-items: center; gap: 12px; margin-bottom: 12px; flex-wrap: wrap; }
    .filter-chip {
      display: inline-flex; align-items: center; gap: 4px;
      padding: 3px 10px; border-radius: 16px; cursor: pointer; font-size: 0.7rem;
      border: 1px solid var(--mat-sys-outline-variant); transition: background 0.15s;
    }
    .filter-chip.active { background: var(--mat-sys-primary); color: var(--mat-sys-on-primary); border-color: transparent; }
    .filter-chip.warning.active { background: #FF9800; color: #fff; border-color: transparent; }

    .bulk-bar {
      display: flex; align-items: center; gap: 8px; padding: 6px 12px; margin-bottom: 8px;
      background: var(--mat-sys-surface-variant); border-radius: 6px;
      border: 1px solid var(--mat-sys-outline-variant);
    }

    .empty-state {
      padding: 40px 16px; text-align: center;
      color: var(--mat-sys-on-surface-variant);
    }
    .empty-state mat-icon { font-size: 40px; height: 40px; width: 40px; margin-bottom: 8px; opacity: 0.5; }

    table { width: 100%; }
    .doc-id { font-family: monospace; }

    /* Checklist drawer overlay */
    .overlay-backdrop {
      position: fixed; inset: 0; background: rgba(0,0,0,0.5); z-index: 900;
    }
    .side-panel {
      position: fixed; top: 0; right: 0; bottom: 0; width: 680px; max-width: 100vw;
      background: var(--mat-sys-surface); z-index: 901; display: flex; flex-direction: column;
      box-shadow: -4px 0 24px rgba(0,0,0,0.3);
    }
    .side-panel-header {
      padding: 16px 20px; border-bottom: 1px solid var(--mat-sys-outline-variant);
      display: flex; align-items: center; gap: 12px;
    }
    .side-panel-body { flex: 1; overflow-y: auto; }

    /* Library drawer */
    .library-drawer {
      position: fixed; top: 0; right: 0; bottom: 0; width: 820px; max-width: 100vw;
      background: var(--mat-sys-surface); z-index: 901; display: flex; flex-direction: column;
      box-shadow: -4px 0 24px rgba(0,0,0,0.3);
    }
    .library-drawer-header {
      padding: 14px 24px; border-bottom: 1px solid var(--mat-sys-outline-variant);
      display: flex; align-items: center; gap: 10px;
    }
    .library-drawer-filters { padding: 12px 24px; flex-shrink: 0; }
    .library-drawer-table { flex: 1; overflow-y: auto; }
    .library-drawer-footer {
      padding: 10px 24px; border-top: 1px solid var(--mat-sys-outline-variant);
      display: flex; align-items: center; justify-content: space-between;
    }
    .type-chip {
      display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 0.62rem;
      border: 1px solid var(--mat-sys-outline-variant); cursor: pointer; margin-right: 4px; margin-bottom: 4px;
    }
    .type-chip.active { background: var(--mat-sys-primary); color: var(--mat-sys-on-primary); border-color: transparent; }
    .type-chip.lang-active { background: var(--mat-sys-secondary); color: var(--mat-sys-on-secondary); border-color: transparent; }

    .active-banner {
      display: flex; align-items: center; gap: 8px; padding: 8px 14px; margin-bottom: 16px;
      border-radius: 6px; font-size: 0.8rem;
      background: rgba(68,114,196,0.1); border: 1px solid rgba(68,114,196,0.25);
    }

    /* Loading / spinner containers */
    .loading-center { display: flex; justify-content: center; padding: 40px; }
    .tabs-body { padding-top: 16px; }

    /* Active-banner elements */
    .active-banner-icon { color: #4472C4; }
    .active-banner-deactivate { font-size: 0.72rem; margin-left: auto; }

    /* Page-header actions slot */
    .header-actions { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }

    /* Metrics row */
    .metrics-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px; }
    .stat-grid-wrap { align-content: start; }

    /* Stat value colours */
    .stat-val-blue   { color: #4472C4; }
    .stat-val-orange { color: #ED7D31; }
    .stat-val-green  { color: #70AD47; }

    /* Progress bar */
    .progress-bar-thin { height: 5px; border-radius: 3px; }

    /* Completeness footer rows */
    .missing-hint { font-size: 0.65rem; color: var(--mat-sys-on-surface-variant); margin-top: 6px; }
    .all-covered  { display: flex; align-items: center; gap: 4px; margin-top: 6px; }
    .all-covered-text { font-size: 0.65rem; color: #4CAF50; }
    .all-covered-icon { color: #4CAF50; flex-shrink: 0; }

    /* Doc-vars header elements */
    .doc-vars-expand-icon {
      font-size: 16px; color: var(--mat-sys-on-surface-variant); transition: transform 0.2s;
    }
    .doc-vars-title { font-weight: 600; font-size: 0.75rem; flex: 1; }
    .doc-vars-badge {
      font-size: 0.6rem; padding: 1px 7px; border-radius: 10px;
    }
    .doc-vars-badge-incomplete { background: #FF980018; color: #FF9800; }
    .doc-vars-badge-complete   { background: #4CAF5018; color: #4CAF50; }
    .doc-vars-hint  { font-size: 0.65rem; color: var(--mat-sys-on-surface-variant); margin-left: 8px; }
    .doc-vars-desc  { font-size: 0.68rem; color: var(--mat-sys-on-surface-variant); margin: 0 0 12px; }
    .doc-vars-field { width: 100%; }

    /* Toolbar search field + add-library button */
    .toolbar-search { flex: 1; max-width: 280px; }
    .toolbar-filter-row { display: flex; gap: 6px; }
    .toolbar-add-btn { margin-left: auto; }

    /* Bulk-bar elements */
    .bulk-count { font-weight: 600; font-size: 0.8rem; margin-right: 4px; }
    .bulk-action-btn { font-size: 0.7rem; height: 24px; line-height: 24px; }
    .bulk-clear-btn { margin-left: auto; font-size: 0.7rem; }

    /* Table: column widths */
    table .mat-column-select       { width: 40px; padding-left: 12px; }
    table .mat-column-actions      { width: 60px; }
    table .mat-column-del          { width: 50px; }
    table .mat-column-document_id  { max-width: 220px; word-break: break-all; white-space: normal; }
    table .mat-column-title        { min-width: 160px; }

    /* Table: lib-drawer column widths */
    .library-drawer table .mat-column-select { width: 44px; padding-left: 8px; }

    /* Table: checklist-lib column widths */
    .side-panel table .mat-column-items { width: 60px; }
    .side-panel table .mat-column-add   { width: 70px; }

    /* Table: checklist-detail column widths */
    .side-panel table .mat-column-num { width: 42px; }
    .side-panel table .mat-column-na-col { width: 80px; text-align: center; }

    /* Table: th/td font sizes */
    .th-xs  { font-size: 0.69rem; }
    .th-xxs { font-size: 0.68rem; }
    .td-xs  { font-size: 0.72rem; }
    .td-sm  { font-size: 0.78rem; }
    .th-right { text-align: right; }
    .td-right { text-align: right; }
    .td-center { text-align: center; }

    /* Table: cell helpers */
    .td-max-220 { max-width: 220px; }
    .td-max-240 { max-width: 240px; }
    .td-max-260 { max-width: 260px; }
    .cell-truncate { display: block; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .cell-truncate-no-wrap { display: block; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
    .td-mono-primary { font-family: monospace; color: var(--mat-sys-primary); font-size: 0.72rem; }
    .td-right-muted { text-align: right; font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }
    .td-xxs { font-size: 0.7rem; }
    .badge-muted-xs { color: var(--mat-sys-on-surface-variant); font-size: 0.65rem; }

    /* Table row */
    .row-clickable { cursor: pointer; }
    table[mat-table] { background: var(--mat-sys-surface-container); width: 100%; }
    tr[mat-header-row] { background: var(--mat-sys-surface-container-high); }
    tr[mat-row] { background: var(--mat-sys-surface-container); border-bottom: 1px solid var(--mat-sys-outline-variant); }
    tr[mat-row]:hover { background: var(--mat-sys-surface-container-high); }

    /* Inline type/status badges */
    .badge { font-size: 0.62rem; padding: 1px 7px; border-radius: 12px; }
    .badge-warn-sm {
      font-size: 0.62rem; padding: 1px 7px; border-radius: 12px;
      background: #FF980018; color: #FF9800;
    }
    .badge-muted { color: var(--mat-sys-on-surface-variant); font-size: 0.72rem; }

    /* Flags / status icons */
    .flag-icon-edited  { font-size: 14px; color: #4472C4; }
    .flag-icon-warning { font-size: 14px; color: #FF9800; }
    .lock-icon { font-size: 12px; color: #FF9800; vertical-align: middle; margin-right: 2px; }
    .lock-icon-no-margin { font-size: 12px; color: #FF9800; vertical-align: middle; }

    /* Checklist tab — top bar */
    .cl-tab-bar { display: flex; justify-content: flex-end; margin-bottom: 16px; }
    .cl-empty-hint { font-size: 0.75rem; color: var(--mat-sys-on-surface-variant); }

    /* Library drawer — info/header blocks */
    .lib-drawer-title-block { flex: 1; }
    .lib-drawer-title { font-weight: 700; font-size: 0.95rem; }
    .lib-drawer-subtitle { font-size: 0.75rem; color: var(--mat-sys-on-surface-variant); }
    .lib-drawer-search { width: 100%; margin-bottom: 8px; }
    .lib-lang-row { margin-top: 4px; }
    .lib-lang-label { font-size: 0.65rem; color: var(--mat-sys-on-surface-variant); margin-right: 4px; }
    .lib-footer-info { font-size: 0.8rem; color: var(--mat-sys-on-surface-variant); }
    .lib-footer-actions { display: flex; gap: 8px; }

    /* Library in-project check icon */
    .already-added-icon { font-size: 16px; color: #4CAF50; margin-left: 8px; }

    /* Side panel (SCR + detail drawers) */
    .side-panel-620 { width: 620px; }
    .side-panel-icon-green { color: #70AD47; }
    .side-panel-title { font-weight: 700; font-size: 0.95rem; flex: 1; }
    .side-panel-detail-title-block { flex: 1; min-width: 0; }
    .side-panel-detail-title { font-weight: 700; font-size: 0.9rem; line-height: 1.2; }
    .side-panel-detail-sub { font-size: 0.75rem; color: var(--mat-sys-on-surface-variant); }
    .panel-add-btn { font-size: 0.7rem; min-width: 60px; }

    /* Checklist detail — item cells */
    .item-text-cell { font-size: 0.78rem; line-height: 1.5; padding: 6px 8px; }
    .item-na-text { text-decoration: line-through; color: var(--mat-sys-on-surface-variant); }
    .item-justification { font-size: 0.68rem; color: #FF9800; margin-top: 3px; }
    .item-row-num { font-size: 0.7rem; color: var(--mat-sys-on-surface-variant); }

    /* Doc editor drawer */
    .editor-drawer-1100 { width: 1100px; }
    .editor-header-block { flex: 1; min-width: 0; }
    .editor-badge-row { display: flex; align-items: center; gap: 6px; margin-bottom: 3px; }
    .editor-badge { font-size: 0.6rem; padding: 1px 7px; border-radius: 12px; }
    .editor-badge-unsaved { font-size: 0.6rem; padding: 1px 7px; border-radius: 12px; background: #FF980018; color: #FF9800; }
    .editor-badge-saved   { font-size: 0.6rem; padding: 1px 7px; border-radius: 12px; background: #4CAF5018; color: #4CAF50; }
    .editor-title { font-weight: 700; font-size: 0.88rem; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .editor-body { flex: 1; overflow: auto; padding: 24px; }

    /* Activate / deactivate button size */
    .btn-sm { font-size: 0.72rem; }

    /* Muted icon button */
    .btn-icon-muted { color: var(--mat-sys-on-surface-variant); }
  `],
  template: `
    <!-- Breadcrumb -->
    <div class="breadcrumb">
      <button mat-icon-button (click)="router.navigate(['/projects'])">
        <mat-icon class="icon-md">arrow_back</mat-icon>
      </button>
      <span class="breadcrumb-link" (click)="router.navigate(['/projects'])">Projects</span>
      <span class="breadcrumb-sep">/</span>
      <span class="breadcrumb-cur">{{ projectQuery.data()?.name }}</span>
    </div>

    @if (projectQuery.isLoading()) {
      <div class="loading-center">
        <mat-spinner diameter="36"></mat-spinner>
      </div>
    }

    @if (projectQuery.data(); as proj) {
      <!-- Active project banner -->
      @if (isActive()) {
        <div class="active-banner">
          <mat-icon class="icon-md active-banner-icon">check_circle</mat-icon>
          You are working in this project
          <button mat-button color="warn" class="active-banner-deactivate"
            (click)="deactivateProject()">
            Deactivate
          </button>
        </div>
      }

      <!-- Page header -->
      <app-page-header [title]="proj.name" [subtitle]="proj.organisation_name ?? ''">
        <div actions class="header-actions">
          <span class="type-chip" [style.border-color]="familyColor(proj.product_family) + '60'"
            [style.color]="familyColor(proj.product_family)">
            {{ proj.product_family }}
          </span>
          <span class="type-chip"
            [style.background]="proj.status === 'active' ? '#4CAF5018' : '#9E9E9E18'"
            [style.color]="proj.status === 'active' ? '#4CAF50' : '#9E9E9E'">
            {{ proj.status }}
          </span>
          @if (isActive()) {
            <button mat-stroked-button (click)="deactivateProject()" class="btn-sm">
              Deactivate
            </button>
          } @else {
            <button mat-raised-button (click)="activateProject(proj)"
              [style.background]="familyColor(proj.product_family)"
              [style.color]="'#fff'"
              class="btn-sm">
              Set Active
            </button>
          }
        </div>
      </app-page-header>

      <!-- Metrics row -->
      <div class="metrics-row">

        <!-- Completeness card -->
        <div class="completeness-card">
          <div class="completeness-header">
            <span class="completeness-section-label">Project Completeness</span>
            <span class="completeness-pct" [style.color]="familyColor(proj.product_family)">
              {{ overallPct() }}%
            </span>
          </div>

          <div class="bar-row">
            <div class="bar-row-header">
              <span>Policy coverage</span>
              <span [style.color]="familyColor(proj.product_family)">
                {{ polUnique() }}/{{ totalCg(proj.product_family) }}
              </span>
            </div>
            <mat-progress-bar mode="determinate" [value]="polPct()"
              class="progress-bar-thin"></mat-progress-bar>
          </div>

          <div class="bar-row">
            <div class="bar-row-header">
              <span>Implementation coverage</span>
              <span [style.color]="familyColor(proj.product_family)">
                {{ implUnique() }}/{{ totalCg(proj.product_family) }}
              </span>
            </div>
            <mat-progress-bar mode="determinate" [value]="implPct()"
              class="progress-bar-thin"></mat-progress-bar>
          </div>

          @if (overallPct() < 100) {
            <div class="missing-hint">
              {{ totalCg(proj.product_family) - maxCovered() }} control group(s) still missing documents
            </div>
          } @else {
            <div class="all-covered">
              <mat-icon class="icon-sm all-covered-icon">check_circle</mat-icon>
              <span class="all-covered-text">All control groups covered</span>
            </div>
          }
        </div>

        <!-- Counts -->
        <div class="stat-grid stat-grid-wrap">
          <div class="stat-card">
            <div class="stat-val stat-val-blue">{{ proj.policy_count }}</div>
            <div class="stat-label">Policies</div>
          </div>
          <div class="stat-card">
            <div class="stat-val stat-val-orange">{{ proj.implementation_count }}</div>
            <div class="stat-label">Implementations</div>
          </div>
          <div class="stat-card">
            <div class="stat-val" [style.color]="proj.assessment_count > 0 ? '#ba68c8' : 'var(--mat-sys-on-surface-variant)'">{{ proj.assessment_count }}</div>
            <div class="stat-label">Assessments</div>
          </div>
          <div class="stat-card">
            <div class="stat-val stat-val-green">{{ proj.checklist_count }}</div>
            <div class="stat-label">Checklists</div>
          </div>
        </div>
      </div>

      <!-- Doc Vars panel -->
      <div class="doc-vars-panel" [class.has-missing]="docVarsMissing">
        <div class="doc-vars-header" (click)="docVarsOpen.set(!docVarsOpen())">
          <mat-icon class="doc-vars-expand-icon"
            [style.transform]="docVarsOpen() ? 'rotate(0)' : 'rotate(-90deg)'">
            expand_more
          </mat-icon>
          <span class="doc-vars-title">Document Variables</span>
          @if (docVarsMissing) {
            <span class="doc-vars-badge doc-vars-badge-incomplete">Incomplete</span>
          } @else {
            <span class="doc-vars-badge doc-vars-badge-complete">Set</span>
          }
          <span class="doc-vars-hint">
            substituted into POL &amp; IMP when added to this project
          </span>
        </div>

        @if (docVarsOpen()) {
          <div class="doc-vars-body">
            <p class="doc-vars-desc">
              These values replace <code>[CISO name]</code>, <code>[CEO Name]</code>,
              <code>[DPO name]</code>, <code>[Date to be set]</code>,
              <code>[Effective Date + 12 months]</code>, <code>[Organisation]</code> etc.
              in library documents when they are added to this project.
            </p>
            <div class="doc-vars-grid">
              <mat-form-field appearance="outline" class="doc-vars-field">
                <mat-label>Organisation</mat-label>
                <input matInput disabled value="(from project settings)">
              </mat-form-field>
              <mat-form-field appearance="outline" class="doc-vars-field">
                <mat-label>CISO name</mat-label>
                <input matInput [(ngModel)]="dvCiso" placeholder="e.g. Jane Smith">
              </mat-form-field>
              <mat-form-field appearance="outline" class="doc-vars-field">
                <mat-label>CEO name</mat-label>
                <input matInput [(ngModel)]="dvCeo" placeholder="e.g. John Smith">
              </mat-form-field>
              <mat-form-field appearance="outline" class="doc-vars-field">
                <mat-label>DPO name</mat-label>
                <input matInput [(ngModel)]="dvDpo" placeholder="e.g. John Doe">
              </mat-form-field>
              <mat-form-field appearance="outline" class="doc-vars-field">
                <mat-label>Legal entity name</mat-label>
                <input matInput [(ngModel)]="dvLegalEntity" placeholder="e.g. Acme Corp Ltd.">
              </mat-form-field>
              <mat-form-field appearance="outline" class="doc-vars-field">
                <mat-label>Effective date</mat-label>
                <input matInput [(ngModel)]="dvEffectiveDate" placeholder="DD.MM.YYYY">
                <mat-hint>e.g. 01.01.2026</mat-hint>
              </mat-form-field>
              <mat-form-field appearance="outline" class="doc-vars-field">
                <mat-label>Next review date</mat-label>
                <input matInput [(ngModel)]="dvReviewDate" placeholder="DD.MM.YYYY">
              </mat-form-field>
              <mat-form-field appearance="outline" class="doc-vars-field">
                <mat-label>Classification</mat-label>
                <input matInput [(ngModel)]="dvClassification" placeholder="Internal">
              </mat-form-field>
            </div>
            <div class="doc-vars-actions">
              <button mat-raised-button [color]="dvSaved() ? 'accent' : 'primary'"
                (click)="saveDocVars(proj.id)" [disabled]="saveDocVarsMut.isPending()">
                <mat-icon class="icon-sm">save</mat-icon>
                {{ dvSaved() ? 'Saved' : 'Save Variables' }}
              </button>
              <button mat-stroked-button [color]="reapplyResult() ? 'accent' : ''"
                (click)="reapplyDocVars(proj.id)" [disabled]="reapplyMut.isPending()"
                matTooltip="Re-apply saved variables to all library-sourced policies and implementations. Save variables first.">
                <mat-icon class="icon-sm">sync</mat-icon>
                @if (reapplyMut.isPending()) { Re-applying… }
                @else if (reapplyResult(); as r) { Done: {{ r.updated_policies }} POL · {{ r.updated_implementations }} IMP }
                @else { Re-apply to documents }
              </button>
            </div>
          </div>
        }
      </div>

      <!-- Tabs -->
      <mat-tab-group animationDuration="0" [(selectedIndex)]="activeTab">
        <mat-tab [label]="'Policies (' + proj.policy_count + ')'"></mat-tab>
        <mat-tab [label]="'Implementations (' + proj.implementation_count + ')'"></mat-tab>
        <mat-tab
          [label]="'Checklists (' + proj.checklist_count + ')'"
          [disabled]="checklistsDisabled(proj)">
        </mat-tab>
      </mat-tab-group>

      <div class="tabs-body">

        <!-- POLICIES TAB -->
        @if (activeTab === 0) {
          <div class="toolbar">
            <mat-form-field appearance="outline" class="toolbar-search" subscriptSizing="dynamic">
              <mat-icon matPrefix>search</mat-icon>
              <input matInput [(ngModel)]="polSearch" placeholder="Search policies…">
            </mat-form-field>

            <div class="toolbar-filter-row">
              <span class="filter-chip" [class.active]="polView() === 'active'"
                (click)="polView.set('active'); clearPolSelected()">
                Active ({{ polActiveAll().length }})
              </span>
              <span class="filter-chip warning" [class.active]="polView() === 'archived'"
                (click)="polView.set('archived'); clearPolSelected()">
                <mat-icon class="icon-sm">delete</mat-icon>
                Bin ({{ polRemovedAll().length }})
              </span>
            </div>

            <button mat-stroked-button (click)="openLibraryDrawer('policies')" class="toolbar-add-btn">
              <mat-icon>library_books</mat-icon>
              Add from Library
            </button>
          </div>

          @if (polSelected().size > 0) {
            <div class="bulk-bar">
              <span class="bulk-count">{{ polSelected().size }} selected</span>
              @if (polView() === 'active') {
                <button mat-stroked-button color="warn" class="bulk-action-btn"
                  [disabled]="softDelPolMut.isPending()"
                  (click)="softDelPolMut.mutate([...polSelected()])">
                  Move to Bin
                </button>
              } @else {
                <button mat-stroked-button color="accent" class="bulk-action-btn"
                  [disabled]="restorePolMut.isPending()"
                  (click)="restorePolMut.mutate([...polSelected()])">
                  Restore
                </button>
              }
              <button mat-stroked-button color="warn" class="bulk-action-btn"
                [disabled]="hardDelPolMut.isPending()"
                (click)="hardDelPolMut.mutate([...polSelected()])">
                Delete permanently
              </button>
              <button mat-button class="bulk-clear-btn"
                (click)="clearPolSelected()">Clear</button>
            </div>
          }

          @if (policiesQuery.isLoading()) {
            <div class="empty-state"><mat-spinner diameter="24"></mat-spinner></div>
          } @else if (polDisplayed().length === 0) {
            <div class="empty-state">
              <mat-icon>policy</mat-icon>
              <p>{{ polView() === 'archived' ? 'Bin is empty' : polActiveAll().length ? 'No matching policies' : 'No policies added yet — click "Add from Library" to start' }}</p>
            </div>
          } @else {
            <table mat-table [dataSource]="polDisplayed()"
              [style.opacity]="polView() === 'archived' ? '0.85' : '1'">

              <ng-container matColumnDef="select">
                <th mat-header-cell *matHeaderCellDef>
                  <mat-checkbox [checked]="polAllChecked()" [indeterminate]="polSomeChecked() && !polAllChecked()"
                    (change)="togglePolAll()"></mat-checkbox>
                </th>
                <td mat-cell *matCellDef="let p"
                  (click)="$event.stopPropagation(); togglePolRow(p.id)">
                  <mat-checkbox [checked]="polSelected().has(p.id)"></mat-checkbox>
                </td>
              </ng-container>

              <ng-container matColumnDef="document_id">
                <th mat-header-cell *matHeaderCellDef class="th-xs">Document ID</th>
                <td mat-cell *matCellDef="let p" class="doc-id td-xs">
                  @if (p.stacking_locked) {
                    <mat-icon matTooltip="Stacked control — structure locked"
                      class="lock-icon">lock</mat-icon>
                  }
                  {{ p.document_id ?? 'Custom' }}
                </td>
              </ng-container>

              <ng-container matColumnDef="title">
                <th mat-header-cell *matHeaderCellDef class="th-xs">Title</th>
                <td mat-cell *matCellDef="let p" class="td-xs td-max-220">
                  <span class="cell-truncate"
                    [style.text-decoration]="polView() === 'archived' ? 'line-through' : 'none'">
                    {{ p.title ?? '—' }}
                  </span>
                </td>
              </ng-container>

              <ng-container matColumnDef="type">
                <th mat-header-cell *matHeaderCellDef class="th-xs">Type</th>
                <td mat-cell *matCellDef="let p">
                  @if (p.policy_type) {
                    <span class="badge"
                      [style.background]="(polTypeColor(p.policy_type)) + '20'"
                      [style.color]="polTypeColor(p.policy_type)">
                      {{ p.policy_type }}
                    </span>
                  }
                </td>
              </ng-container>

              <ng-container matColumnDef="control_group">
                <th mat-header-cell *matHeaderCellDef class="th-xs">Control Group</th>
                <td mat-cell *matCellDef="let p" class="td-xs">{{ p.control_group_code ?? '—' }}</td>
              </ng-container>

              <ng-container matColumnDef="flags">
                <th mat-header-cell *matHeaderCellDef class="th-xs">Flags</th>
                <td mat-cell *matCellDef="let p">
                  @if (p.is_edited) {
                    <mat-icon matTooltip="Edited — differs from Library version"
                      class="flag-icon-edited">edit</mat-icon>
                  }
                  @if (p.stale_warning) {
                    <mat-icon matTooltip="Stale warning — cross-references may no longer match"
                      class="flag-icon-warning">warning</mat-icon>
                  }
                </td>
              </ng-container>

              <ng-container matColumnDef="actions">
                <th mat-header-cell *matHeaderCellDef></th>
                <td mat-cell *matCellDef="let p" (click)="$event.stopPropagation()">
                  @if (polView() === 'active') {
                    <button mat-icon-button [matTooltip]="'Edit document'"
                      class="btn-icon-muted"
                      (click)="openDocEditor(proj.id, p.id, 'policy', p.title, p.policy_type)">
                      <mat-icon class="icon-sm">edit</mat-icon>
                    </button>
                  } @else {
                    <button mat-icon-button matTooltip="Restore"
                      (click)="restorePolMut.mutate([p.id])">
                      <mat-icon class="icon-sm">restore_from_trash</mat-icon>
                    </button>
                  }
                </td>
              </ng-container>

              <tr mat-header-row *matHeaderRowDef="polColumns"></tr>
              <tr mat-row *matRowDef="let row; columns: polColumns"
                class="row-clickable"
                (click)="polView() === 'active' && openDocEditor(proj.id, row.id, 'policy', row.title, row.policy_type)">
              </tr>
            </table>
          }
        }

        <!-- IMPLEMENTATIONS TAB -->
        @if (activeTab === 1) {
          <div class="toolbar">
            <mat-form-field appearance="outline" class="toolbar-search" subscriptSizing="dynamic">
              <mat-icon matPrefix>search</mat-icon>
              <input matInput [(ngModel)]="implSearch" placeholder="Search implementations…">
            </mat-form-field>

            <div class="toolbar-filter-row">
              <span class="filter-chip" [class.active]="implView() === 'active'"
                (click)="implView.set('active'); clearImplSelected()">
                Active ({{ implActiveAll().length }})
              </span>
              <span class="filter-chip warning" [class.active]="implView() === 'archived'"
                (click)="implView.set('archived'); clearImplSelected()">
                <mat-icon class="icon-sm">delete</mat-icon>
                Bin ({{ implRemovedAll().length }})
              </span>
            </div>

            <button mat-stroked-button (click)="openLibraryDrawer('implementations')" class="toolbar-add-btn">
              <mat-icon>library_books</mat-icon>
              Add from Library
            </button>
          </div>

          @if (implSelected().size > 0) {
            <div class="bulk-bar">
              <span class="bulk-count">{{ implSelected().size }} selected</span>
              @if (implView() === 'active') {
                <button mat-stroked-button color="warn" class="bulk-action-btn"
                  [disabled]="softDelImplMut.isPending()"
                  (click)="softDelImplMut.mutate([...implSelected()])">
                  Move to Bin
                </button>
              } @else {
                <button mat-stroked-button color="accent" class="bulk-action-btn"
                  [disabled]="restoreImplMut.isPending()"
                  (click)="restoreImplMut.mutate([...implSelected()])">
                  Restore
                </button>
              }
              <button mat-stroked-button color="warn" class="bulk-action-btn"
                [disabled]="hardDelImplMut.isPending()"
                (click)="hardDelImplMut.mutate([...implSelected()])">
                Delete permanently
              </button>
              <button mat-button class="bulk-clear-btn"
                (click)="clearImplSelected()">Clear</button>
            </div>
          }

          @if (implsQuery.isLoading()) {
            <div class="empty-state"><mat-spinner diameter="24"></mat-spinner></div>
          } @else if (implDisplayed().length === 0) {
            <div class="empty-state">
              <mat-icon>shield</mat-icon>
              <p>{{ implView() === 'archived' ? 'Bin is empty' : implActiveAll().length ? 'No matching implementations' : 'No implementations added yet — click "Add from Library" to start' }}</p>
            </div>
          } @else {
            <table mat-table [dataSource]="implDisplayed()"
              [style.opacity]="implView() === 'archived' ? '0.85' : '1'">

              <ng-container matColumnDef="select">
                <th mat-header-cell *matHeaderCellDef>
                  <mat-checkbox [checked]="implAllChecked()" [indeterminate]="implSomeChecked() && !implAllChecked()"
                    (change)="toggleImplAll()"></mat-checkbox>
                </th>
                <td mat-cell *matCellDef="let i"
                  (click)="$event.stopPropagation(); toggleImplRow(i.id)">
                  <mat-checkbox [checked]="implSelected().has(i.id)"></mat-checkbox>
                </td>
              </ng-container>

              <ng-container matColumnDef="document_id">
                <th mat-header-cell *matHeaderCellDef class="th-xs">Document ID</th>
                <td mat-cell *matCellDef="let i" class="doc-id td-xs">
                  {{ i.document_id ?? 'Custom' }}
                </td>
              </ng-container>

              <ng-container matColumnDef="title">
                <th mat-header-cell *matHeaderCellDef class="th-xs">Title</th>
                <td mat-cell *matCellDef="let i" class="td-xs td-max-240">
                  <span class="cell-truncate"
                    [style.text-decoration]="implView() === 'archived' ? 'line-through' : 'none'">
                    {{ i.title ?? '—' }}
                  </span>
                </td>
              </ng-container>

              <ng-container matColumnDef="type">
                <th mat-header-cell *matHeaderCellDef class="th-xs">Type</th>
                <td mat-cell *matCellDef="let i">
                  @if (i.impl_type) {
                    <span class="badge"
                      [style.background]="(implTypeColor(i.impl_type)) + '20'"
                      [style.color]="implTypeColor(i.impl_type)">
                      {{ i.impl_type }}
                    </span>
                  }
                </td>
              </ng-container>

              <ng-container matColumnDef="control_group">
                <th mat-header-cell *matHeaderCellDef class="th-xs">Control Group</th>
                <td mat-cell *matCellDef="let i" class="td-xs">{{ i.control_group_code ?? '—' }}</td>
              </ng-container>

              <ng-container matColumnDef="flags">
                <th mat-header-cell *matHeaderCellDef class="th-xs">Flags</th>
                <td mat-cell *matCellDef="let i">
                  @if (i.is_edited) {
                    <mat-icon matTooltip="Edited — differs from Library version"
                      class="flag-icon-edited">edit</mat-icon>
                  }
                  @if (i.stale_warning) {
                    <mat-icon matTooltip="Stale warning — linked policy was edited"
                      class="flag-icon-warning">warning</mat-icon>
                  }
                </td>
              </ng-container>

              <ng-container matColumnDef="actions">
                <th mat-header-cell *matHeaderCellDef></th>
                <td mat-cell *matCellDef="let i" (click)="$event.stopPropagation()">
                  @if (implView() === 'active') {
                    <button mat-icon-button matTooltip="Edit document"
                      class="btn-icon-muted"
                      (click)="openDocEditor(proj.id, i.id, 'implementation', i.title, i.impl_type)">
                      <mat-icon class="icon-sm">edit</mat-icon>
                    </button>
                  } @else {
                    <button mat-icon-button matTooltip="Restore"
                      (click)="restoreImplMut.mutate([i.id])">
                      <mat-icon class="icon-sm">restore_from_trash</mat-icon>
                    </button>
                  }
                </td>
              </ng-container>

              <tr mat-header-row *matHeaderRowDef="implColumns"></tr>
              <tr mat-row *matRowDef="let row; columns: implColumns"
                class="row-clickable"
                (click)="implView() === 'active' && openDocEditor(proj.id, row.id, 'implementation', row.title, row.impl_type)">
              </tr>
            </table>
          }
        }

        <!-- CHECKLISTS TAB -->
        @if (activeTab === 2) {
          <div class="cl-tab-bar">
            <button mat-stroked-button (click)="checklistLibOpen.set(true)">
              <mat-icon>library_books</mat-icon>
              Browse Library SCRs
            </button>
          </div>

          @if (checklistsQuery.isLoading()) {
            <div class="empty-state"><mat-spinner diameter="24"></mat-spinner></div>
          } @else if (checklistsQuery.data()?.length === 0) {
            <div class="empty-state">
              <mat-icon>assignment</mat-icon>
              <p>No checklists added yet</p>
              <span class="cl-empty-hint">
                Browse the library to clone SCR checklists — then toggle N/A on items that don't apply.
              </span>
            </div>
          } @else {
            <table mat-table [dataSource]="checklistsQuery.data() ?? []">
              <ng-container matColumnDef="control_group">
                <th mat-header-cell *matHeaderCellDef class="th-xs">Control Group</th>
                <td mat-cell *matCellDef="let cl" class="td-mono-primary">
                  {{ cl.control_group_code }}
                </td>
              </ng-container>
              <ng-container matColumnDef="title">
                <th mat-header-cell *matHeaderCellDef class="th-xs">Title</th>
                <td mat-cell *matCellDef="let cl" class="td-sm td-max-260">
                  <span class="cell-truncate-no-wrap">
                    {{ cl.title ?? cl.control_group_name }}
                  </span>
                </td>
              </ng-container>
              <ng-container matColumnDef="type">
                <th mat-header-cell *matHeaderCellDef class="th-xs">Type</th>
                <td mat-cell *matCellDef="let cl">
                  <span class="badge"
                    [style.background]="(ptColor(cl.product_type)) + '18'"
                    [style.color]="ptColor(cl.product_type)">
                    {{ cl.product_type }}
                  </span>
                </td>
              </ng-container>
              <ng-container matColumnDef="items">
                <th mat-header-cell *matHeaderCellDef class="th-xs th-right">Items</th>
                <td mat-cell *matCellDef="let cl" class="td-right td-sm">{{ cl.item_count }}</td>
              </ng-container>
              <ng-container matColumnDef="na">
                <th mat-header-cell *matHeaderCellDef class="th-xs th-right">N/A</th>
                <td mat-cell *matCellDef="let cl" class="td-right">
                  @if (cl.na_count > 0) {
                    <span class="badge-warn-sm">
                      {{ cl.na_count }}
                    </span>
                  } @else {
                    <span class="badge-muted">—</span>
                  }
                </td>
              </ng-container>
              <ng-container matColumnDef="del">
                <th mat-header-cell *matHeaderCellDef></th>
                <td mat-cell *matCellDef="let cl" (click)="$event.stopPropagation()">
                  <button mat-icon-button matTooltip="Remove from project"
                    class="btn-icon-muted"
                    [disabled]="removeChecklistMut.isPending()"
                    (click)="removeChecklistMut.mutate(cl.id)">
                    <mat-icon class="icon-sm">delete</mat-icon>
                  </button>
                </td>
              </ng-container>

              <tr mat-header-row *matHeaderRowDef="clColumns"></tr>
              <tr mat-row *matRowDef="let row; columns: clColumns"
                class="row-clickable"
                (click)="selectedChecklist.set(row)">
              </tr>
            </table>
          }
        }

      </div>
    }

    <!-- ── Library Drawer ── -->
    @if (libraryDrawerOpen()) {
      <div class="overlay-backdrop" (click)="libraryDrawerOpen.set(false)"></div>
      <div class="library-drawer">
        <div class="library-drawer-header">
          <mat-icon>library_books</mat-icon>
          <div class="lib-drawer-title-block">
            <div class="lib-drawer-title">
              Library — {{ libraryMode() === 'policies' ? 'Policies' : 'Implementations' }}
            </div>
            <div class="lib-drawer-subtitle">
              Select documents to import into this project
            </div>
          </div>
          <button mat-icon-button (click)="libraryDrawerOpen.set(false)">
            <mat-icon>close</mat-icon>
          </button>
        </div>

        <div class="library-drawer-filters">
          <mat-form-field appearance="outline" class="lib-drawer-search" subscriptSizing="dynamic">
            <mat-icon matPrefix>search</mat-icon>
            <input matInput [(ngModel)]="libSearch" placeholder="Search by code, title, control group…">
          </mat-form-field>

          <div>
            @for (t of libTypeOptions(); track t) {
              <span class="type-chip" [class.active]="libTypeFilter() === t"
                (click)="libTypeFilter.set(t)">{{ t }}</span>
            }
          </div>

          @if (libraryMode() === 'policies') {
            <div class="lib-lang-row">
              <span class="lib-lang-label">Lang:</span>
              @for (l of langOptions; track l) {
                <span class="type-chip" [class.lang-active]="libLangFilter() === l"
                  (click)="libLangFilter.set(l)">{{ l }}</span>
              }
            </div>
          }
        </div>

        <mat-divider></mat-divider>

        <div class="library-drawer-table">
          @if (libPoliciesQuery.isLoading() || libImplsQuery.isLoading()) {
            <div class="empty-state"><mat-spinner diameter="24"></mat-spinner></div>
          } @else {
            <table mat-table [dataSource]="libFiltered()">
              <ng-container matColumnDef="select">
                <th mat-header-cell *matHeaderCellDef>
                  <mat-checkbox [checked]="libAllSelected()" [indeterminate]="libSomeSelected() && !libAllSelected()"
                    (change)="toggleLibAll()"></mat-checkbox>
                </th>
                <td mat-cell *matCellDef="let r">
                  @if (r.already_in_project) {
                    <mat-icon class="already-added-icon">check_circle</mat-icon>
                  } @else {
                    <mat-checkbox [checked]="libSelected().has(r.id)"
                      (change)="toggleLibRow(r.id)" (click)="$event.stopPropagation()">
                    </mat-checkbox>
                  }
                </td>
              </ng-container>
              <ng-container matColumnDef="document_id">
                <th mat-header-cell *matHeaderCellDef class="th-xs">Document ID</th>
                <td mat-cell *matCellDef="let r" class="doc-id td-xs">
                  @if (r.is_stacked) {
                    <mat-icon matTooltip="Stacked control — structure locked"
                      class="lock-icon-no-margin">lock</mat-icon>
                  }
                  {{ r.document_id }}
                </td>
              </ng-container>
              <ng-container matColumnDef="title">
                <th mat-header-cell *matHeaderCellDef class="th-xs">Title</th>
                <td mat-cell *matCellDef="let r" class="td-xs td-max-260">
                  <span class="cell-truncate">
                    {{ r.title }}
                  </span>
                </td>
              </ng-container>
              <ng-container matColumnDef="type">
                <th mat-header-cell *matHeaderCellDef class="th-xs">Type</th>
                <td mat-cell *matCellDef="let r">
                  @if (libraryMode() === 'policies') {
                    <span class="badge"
                      [style.background]="polTypeColor(r.policy_type) + '20'"
                      [style.color]="polTypeColor(r.policy_type)">{{ r.policy_type }}</span>
                  } @else {
                    <span class="badge"
                      [style.background]="implTypeColor(r.impl_type) + '20'"
                      [style.color]="implTypeColor(r.impl_type)">{{ r.impl_type }}</span>
                  }
                </td>
              </ng-container>
              <ng-container matColumnDef="control_group">
                <th mat-header-cell *matHeaderCellDef class="th-xs">Control Group</th>
                <td mat-cell *matCellDef="let r" class="td-xs">{{ r.control_group_code }}</td>
              </ng-container>

              <tr mat-header-row *matHeaderRowDef="libColumns"></tr>
              <tr mat-row *matRowDef="let row; columns: libColumns"
                [style.opacity]="row.already_in_project ? '0.5' : '1'"
                [style.cursor]="row.already_in_project ? 'default' : 'pointer'"
                (click)="!row.already_in_project && toggleLibRow(row.id)">
              </tr>
            </table>
          }
        </div>

        <div class="library-drawer-footer">
          <span class="lib-footer-info">
            {{ libSelected().size > 0 ? libSelected().size + ' selected' : libAvailableIds().length + ' available' }}
          </span>
          <div class="lib-footer-actions">
            <button mat-stroked-button
              [disabled]="libAvailableIds().length === 0 || libImporting()"
              (click)="selectAllLib()">
              Select all ({{ libAvailableIds().length }})
            </button>
            <button mat-raised-button color="primary"
              [disabled]="libSelected().size === 0 || libImporting()"
              (click)="importSelected()">
              @if (libImporting()) { Importing… } @else { Import selected ({{ libSelected().size }}) }
            </button>
          </div>
        </div>
      </div>
    }

    <!-- ── Checklist Library Drawer ── -->
    @if (checklistLibOpen()) {
      <div class="overlay-backdrop" (click)="checklistLibOpen.set(false)"></div>
      <div class="side-panel side-panel-620">
        <div class="side-panel-header">
          <mat-icon class="side-panel-icon-green">library_books</mat-icon>
          <span class="side-panel-title">Library SCR Checklists</span>
          <button mat-icon-button (click)="checklistLibOpen.set(false)">
            <mat-icon>close</mat-icon>
          </button>
        </div>
        <div class="side-panel-body">
          @if (libChecklistsQuery.isLoading()) {
            <div class="empty-state"><mat-spinner diameter="24"></mat-spinner></div>
          } @else if (!libChecklistsQuery.data()?.length) {
            <div class="empty-state">
              <mat-icon>assignment</mat-icon>
              <p>No library checklists available</p>
            </div>
          } @else {
            <table mat-table [dataSource]="libChecklistsQuery.data() ?? []">
              <ng-container matColumnDef="doc_id">
                <th mat-header-cell *matHeaderCellDef class="th-xxs">Document ID</th>
                <td mat-cell *matCellDef="let lib" class="doc-id td-xxs">{{ lib.document_id }}</td>
              </ng-container>
              <ng-container matColumnDef="title">
                <th mat-header-cell *matHeaderCellDef class="th-xxs">Title</th>
                <td mat-cell *matCellDef="let lib" class="td-sm td-max-220">
                  <span class="cell-truncate-no-wrap">
                    {{ lib.title }}
                  </span>
                  <span class="badge-muted-xs">
                    {{ lib.control_group_code }}
                  </span>
                </td>
              </ng-container>
              <ng-container matColumnDef="type">
                <th mat-header-cell *matHeaderCellDef class="th-xxs">Type</th>
                <td mat-cell *matCellDef="let lib">
                  <span class="badge"
                    [style.background]="ptColor(lib.product_type) + '18'"
                    [style.color]="ptColor(lib.product_type)">{{ lib.product_type }}</span>
                </td>
              </ng-container>
              <ng-container matColumnDef="items">
                <th mat-header-cell *matHeaderCellDef class="th-xxs th-right">Items</th>
                <td mat-cell *matCellDef="let lib" class="td-right-muted">{{ lib.item_count }}</td>
              </ng-container>
              <ng-container matColumnDef="add">
                <th mat-header-cell *matHeaderCellDef></th>
                <td mat-cell *matCellDef="let lib">
                  <button mat-stroked-button
                    [disabled]="lib.already_in_project || addChecklistMut.isPending()"
                    class="panel-add-btn"
                    (click)="addChecklistMut.mutate(lib.id)">
                    {{ lib.already_in_project ? 'Added' : 'Add' }}
                  </button>
                </td>
              </ng-container>

              <tr mat-header-row *matHeaderRowDef="libClColumns"></tr>
              <tr mat-row *matRowDef="let row; columns: libClColumns"
                [style.opacity]="row.already_in_project ? '0.5' : '1'">
              </tr>
            </table>
          }
        </div>
      </div>
    }

    <!-- ── Checklist Detail Drawer ── -->
    @if (selectedChecklist()) {
      <div class="overlay-backdrop" (click)="selectedChecklist.set(null)"></div>
      <div class="side-panel">
        <div class="side-panel-header">
          <mat-icon class="side-panel-icon-green">assignment</mat-icon>
          <div class="side-panel-detail-title-block">
            <div class="side-panel-detail-title">
              {{ selectedChecklist()!.title ?? selectedChecklist()!.control_group_name }}
            </div>
            <div class="side-panel-detail-sub">
              {{ selectedChecklist()!.control_group_code }} · {{ selectedChecklist()!.product_type }}
            </div>
          </div>
          <button mat-icon-button (click)="selectedChecklist.set(null)">
            <mat-icon class="icon-md">close</mat-icon>
          </button>
        </div>

        @if (checklistDetailQuery.isLoading()) {
          <div class="empty-state"><mat-spinner diameter="24"></mat-spinner></div>
        } @else {
          <div class="side-panel-body">
            <table mat-table [dataSource]="checklistDetailQuery.data()?.items ?? []">
              <ng-container matColumnDef="num">
                <th mat-header-cell *matHeaderCellDef class="th-xxs">#</th>
                <td mat-cell *matCellDef="let item" class="item-row-num">
                  {{ item.row_number }}
                </td>
              </ng-container>
              <ng-container matColumnDef="text">
                <th mat-header-cell *matHeaderCellDef class="th-xxs">Requirement</th>
                <td mat-cell *matCellDef="let item" class="item-text-cell">
                  @if (item.na) {
                    <span class="item-na-text">{{ item.item_text }}</span>
                    @if (item.justification) {
                      <div class="item-justification">{{ item.justification }}</div>
                    }
                  } @else {
                    {{ item.item_text }}
                  }
                </td>
              </ng-container>
              <ng-container matColumnDef="na">
                <th mat-header-cell *matHeaderCellDef class="th-xxs td-center">N/A</th>
                <td mat-cell *matCellDef="let item" class="td-center">
                  <mat-slide-toggle
                    [checked]="item.na"
                    [disabled]="patchChecklistMut.isPending()"
                    (change)="patchChecklistMut.mutate({ item_id: item.id, na: $event.checked })"
                    color="warn">
                  </mat-slide-toggle>
                </td>
              </ng-container>
              <tr mat-header-row *matHeaderRowDef="['num','text','na']"></tr>
              <tr mat-row *matRowDef="let row; columns: ['num','text','na']"
                [style.opacity]="row.na ? '0.45' : '1'"></tr>
            </table>
          </div>
        }
      </div>
    }

    <!-- ── Doc Editor Drawer ── -->
    @if (editorDoc()) {
      <div class="overlay-backdrop" (click)="closeDocEditor()"></div>
      <div class="library-drawer editor-drawer-1100">
        <div class="library-drawer-header">
          <div class="editor-header-block">
            <div class="editor-badge-row">
              @if (editorDoc()!.docType) {
                <span class="editor-badge"
                  [style.background]="editorDocTypeColor() + '18'"
                  [style.color]="editorDocTypeColor()">
                  {{ editorDoc()!.docType }}
                </span>
              }
              @if (editorDirty() && !editorSaved()) {
                <span class="editor-badge-unsaved">Unsaved</span>
              }
              @if (editorSaved()) {
                <span class="editor-badge-saved">Saved</span>
              }
            </div>
            <div class="editor-title">
              {{ editorDoc()!.title ?? 'Untitled' }}
            </div>
          </div>
          <button mat-raised-button [color]="editorSaved() ? 'accent' : 'primary'"
            [disabled]="saveDocMut.isPending() || (!editorDirty() && !editorSaved())"
            (click)="saveDocContent()">
            <mat-icon class="icon-sm">save</mat-icon>
            {{ saveDocMut.isPending() ? 'Saving…' : editorSaved() ? 'Saved' : 'Save' }}
          </button>
          <button mat-icon-button (click)="closeDocEditor()">
            <mat-icon>close</mat-icon>
          </button>
        </div>

        <div class="editor-body">
          @if (docContentQuery.isLoading()) {
            <div class="empty-state"><mat-spinner diameter="24"></mat-spinner></div>
          } @else {
            <app-rich-text-editor
              [value]="editorContent"
              (valueChange)="onEditorRteChange($event)" />
          }
        </div>
      </div>
    }
  `,
})
export class ProjectDetailComponent {
  private readonly route     = inject(ActivatedRoute)
  readonly router            = inject(Router)
  private readonly http      = inject(HttpClient)
  private readonly qc        = injectQueryClient()
  readonly projectService    = inject(ProjectService)

  private readonly projectId = signal<string>('')

  private docVarsPopulated = false

  constructor() {
    this.route.paramMap.subscribe(p => {
      const id = p.get('id')
      if (id) {
        this.projectId.set(id)
        this.docVarsPopulated = false
      }
    })
    // Populate doc-vars fields once project data loads
    effect(() => {
      const proj = this.projectQuery.data()
      if (proj && !this.docVarsPopulated) {
        this.loadDocVars(proj)
        this.docVarsPopulated = true
      }
    })

    // Populate doc editor textarea when content loads
    effect(() => {
      const data = this.docContentQuery.data()
      if (data?.custom_content != null && this.editorDoc() && !this.editorDirty()) {
        this.editorContent = (data.custom_content ?? '')
          .replace(/^<!--\s*ISMS-CORE:[^\n]*-->\s*\n?/m, '')
          .replace(/\n?<!--\s*QA_VERIFIED:[^\n]*-->\s*$/m, '')
          .trimStart()
      }
    })
  }

  // ── Queries ──────────────────────────────────────────────────────────────────

  projectQuery = injectQuery(() => ({
    queryKey: ['project', this.projectId()],
    queryFn:  () => firstValueFrom(this.http.get<ProjectFull>(`/api/v1/projects/${this.projectId()}`)),
    enabled:  !!this.projectId(),
  }))

  policiesQuery = injectQuery(() => ({
    queryKey: ['project-policies', this.projectId()],
    queryFn:  () => firstValueFrom(this.http.get<ProjectPolicyRead[]>(`/api/v1/projects/${this.projectId()}/policies`)),
    enabled:  !!this.projectId(),
  }))

  implsQuery = injectQuery(() => ({
    queryKey: ['project-impls', this.projectId()],
    queryFn:  () => firstValueFrom(this.http.get<ProjectImplRead[]>(`/api/v1/projects/${this.projectId()}/implementations`)),
    enabled:  !!this.projectId(),
  }))

  checklistsQuery = injectQuery(() => ({
    queryKey: ['project-checklists', this.projectId()],
    queryFn:  () => firstValueFrom(this.http.get<ProjectChecklistRead[]>(`/api/v1/projects/${this.projectId()}/checklists`)),
    enabled:  !!this.projectId() && this.activeTab === 2,
  }))

  libChecklistsQuery = injectQuery(() => ({
    queryKey: ['project-library-checklists', this.projectId()],
    queryFn:  () => firstValueFrom(this.http.get<LibraryChecklistItem[]>(`/api/v1/projects/${this.projectId()}/library/checklists`)),
    enabled:  !!this.projectId() && this.checklistLibOpen(),
  }))

  libPoliciesQuery = injectQuery(() => ({
    queryKey: ['library', 'policies', this.projectId(), this.libLangFilter()],
    queryFn: () => {
      const params: Record<string, string> = {}
      if (this.libLangFilter() !== 'ALL') params['language'] = this.libLangFilter()
      return firstValueFrom(this.http.get<LibraryPolicyItem[]>(
        `/api/v1/projects/${this.projectId()}/library/policies`, { params }))
    },
    enabled: !!this.projectId() && this.libraryDrawerOpen() && this.libraryMode() === 'policies',
  }))

  libImplsQuery = injectQuery(() => ({
    queryKey: ['library', 'implementations', this.projectId()],
    queryFn:  () => firstValueFrom(this.http.get<LibraryImplItem[]>(`/api/v1/projects/${this.projectId()}/library/implementations`)),
    enabled:  !!this.projectId() && this.libraryDrawerOpen() && this.libraryMode() === 'implementations',
  }))

  checklistDetailQuery = injectQuery(() => ({
    queryKey: ['project-checklist-detail', this.projectId(), this.selectedChecklist()?.id],
    queryFn:  () => firstValueFrom(this.http.get<ProjectChecklistRead>(
      `/api/v1/projects/${this.projectId()}/checklists/${this.selectedChecklist()!.id}`)),
    enabled:  !!this.selectedChecklist(),
  }))

  docContentQuery = injectQuery(() => ({
    queryKey: ['project-doc', this.projectId(), this.editorDoc()?.id, this.editorDoc()?.mode],
    queryFn:  () => {
      const d = this.editorDoc()!
      const url = d.mode === 'policy'
        ? `/api/v1/projects/${this.projectId()}/policies/${d.id}`
        : `/api/v1/projects/${this.projectId()}/implementations/${d.id}`
      return firstValueFrom(this.http.get<{ custom_content?: string | null }>(url))
    },
    enabled: !!this.editorDoc(),
  }))

  // ── Mutations ────────────────────────────────────────────────────────────────

  saveDocVarsMut = injectMutation(() => ({
    mutationFn: (vars: DocVars) => firstValueFrom(
      this.http.patch<ProjectFull>(`/api/v1/projects/${this.projectId()}`, { doc_vars: vars })),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['project', this.projectId()] })
      this.dvSaved.set(true)
      setTimeout(() => this.dvSaved.set(false), 2000)
    },
  }))

  reapplyMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(
      this.http.post<{ updated_policies: number; updated_implementations: number }>(
        `/api/v1/projects/${this.projectId()}/reapply-doc-vars`, {})),
    onSuccess: r => this.reapplyResult.set(r),
  }))

  softDelPolMut = injectMutation(() => ({
    mutationFn: (ids: string[]) => Promise.all(ids.map(id =>
      firstValueFrom(this.http.patch(`/api/v1/projects/${this.projectId()}/policies/${id}`, { status: 'archived' })))),
    onSuccess: () => this.invalidatePolicies(),
  }))

  restorePolMut = injectMutation(() => ({
    mutationFn: (ids: string[]) => Promise.all(ids.map(id =>
      firstValueFrom(this.http.patch(`/api/v1/projects/${this.projectId()}/policies/${id}`, { status: 'active' })))),
    onSuccess: () => this.invalidatePolicies(),
  }))

  hardDelPolMut = injectMutation(() => ({
    mutationFn: (ids: string[]) => Promise.all(ids.map(id =>
      firstValueFrom(this.http.delete(`/api/v1/projects/${this.projectId()}/policies/${id}`)))),
    onSuccess: () => this.invalidatePolicies(),
  }))

  softDelImplMut = injectMutation(() => ({
    mutationFn: (ids: string[]) => Promise.all(ids.map(id =>
      firstValueFrom(this.http.patch(`/api/v1/projects/${this.projectId()}/implementations/${id}`, { status: 'archived' })))),
    onSuccess: () => this.invalidateImpls(),
  }))

  restoreImplMut = injectMutation(() => ({
    mutationFn: (ids: string[]) => Promise.all(ids.map(id =>
      firstValueFrom(this.http.patch(`/api/v1/projects/${this.projectId()}/implementations/${id}`, { status: 'active' })))),
    onSuccess: () => this.invalidateImpls(),
  }))

  hardDelImplMut = injectMutation(() => ({
    mutationFn: (ids: string[]) => Promise.all(ids.map(id =>
      firstValueFrom(this.http.delete(`/api/v1/projects/${this.projectId()}/implementations/${id}`)))),
    onSuccess: () => this.invalidateImpls(),
  }))

  addPolMut = injectMutation(() => ({
    mutationFn: (id: string) => firstValueFrom(
      this.http.post(`/api/v1/projects/${this.projectId()}/policies`, { lib_policy_id: id })),
  }))

  addImplMut = injectMutation(() => ({
    mutationFn: (id: string) => firstValueFrom(
      this.http.post(`/api/v1/projects/${this.projectId()}/implementations`, { lib_impl_id: id })),
  }))

  addChecklistMut = injectMutation(() => ({
    mutationFn: (libId: string) => firstValueFrom(
      this.http.post(`/api/v1/projects/${this.projectId()}/checklists`, { lib_checklist_id: libId })),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['project-checklists', this.projectId()] })
      this.qc.invalidateQueries({ queryKey: ['project-library-checklists', this.projectId()] })
      this.qc.invalidateQueries({ queryKey: ['project', this.projectId()] })
    },
  }))

  removeChecklistMut = injectMutation(() => ({
    mutationFn: (cid: string) => firstValueFrom(
      this.http.delete(`/api/v1/projects/${this.projectId()}/checklists/${cid}`)),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['project-checklists', this.projectId()] })
      this.qc.invalidateQueries({ queryKey: ['project', this.projectId()] })
    },
  }))

  patchChecklistMut = injectMutation(() => ({
    mutationFn: (body: { item_id: string; na: boolean }) => firstValueFrom(
      this.http.patch<ProjectChecklistRead>(
        `/api/v1/projects/${this.projectId()}/checklists/${this.selectedChecklist()!.id}/items`, body)),
    onSuccess: updated => {
      this.qc.setQueryData(
        ['project-checklist-detail', this.projectId(), this.selectedChecklist()?.id], updated)
      this.qc.invalidateQueries({ queryKey: ['project-checklists', this.projectId()] })
    },
  }))

  saveDocMut = injectMutation(() => ({
    mutationFn: (content: string) => {
      const d = this.editorDoc()!
      const url = d.mode === 'policy'
        ? `/api/v1/projects/${this.projectId()}/policies/${d.id}`
        : `/api/v1/projects/${this.projectId()}/implementations/${d.id}`
      return firstValueFrom(this.http.patch(url, { custom_content: content }))
    },
    onSuccess: () => {
      const d = this.editorDoc()!
      this.qc.invalidateQueries({ queryKey: [d.mode === 'policy' ? 'project-policies' : 'project-impls', this.projectId()] })
      this.editorSaved.set(true)
      this.editorDirty.set(false)
      setTimeout(() => this.editorSaved.set(false), 3000)
    },
  }))

  // ── Local state ──────────────────────────────────────────────────────────────

  activeTab      = 0

  // Doc vars
  docVarsOpen    = signal(false)
  dvSaved        = signal(false)
  dvCiso         = ''
  dvCeo          = ''
  dvDpo          = ''
  dvLegalEntity  = ''
  dvEffectiveDate = ''
  dvReviewDate   = ''
  dvClassification = ''
  reapplyResult  = signal<{ updated_policies: number; updated_implementations: number } | null>(null)

  // Policies
  polSearch      = ''
  polView        = signal<'active' | 'archived'>('active')
  polSelected    = signal<Set<string>>(new Set())

  // Impls
  implSearch     = ''
  implView       = signal<'active' | 'archived'>('active')
  implSelected   = signal<Set<string>>(new Set())

  // Checklists
  selectedChecklist = signal<ProjectChecklistRead | null>(null)
  checklistLibOpen  = signal(false)

  // Library drawer
  libraryDrawerOpen = signal(false)
  libraryMode       = signal<'policies' | 'implementations'>('policies')
  libSearch         = ''
  libTypeFilter     = signal('ALL')
  libLangFilter     = signal('ALL')
  libSelected       = signal<Set<string>>(new Set())
  libImporting      = signal(false)
  langOptions       = ['ALL', 'EN', 'DE', 'FR', 'IT']
  libColumns        = ['select', 'document_id', 'title', 'type', 'control_group']

  // Doc editor
  editorDoc     = signal<{ id: string; mode: 'policy' | 'implementation'; title: string | null; docType: string | null } | null>(null)
  editorContent = ''
  editorDirty   = signal(false)
  editorSaved   = signal(false)

  // Table columns
  polColumns    = ['select', 'document_id', 'title', 'type', 'control_group', 'flags', 'actions']
  implColumns   = ['select', 'document_id', 'title', 'type', 'control_group', 'flags', 'actions']
  clColumns     = ['control_group', 'title', 'type', 'items', 'na', 'del']
  libClColumns  = ['doc_id', 'title', 'type', 'items', 'add']

  // ── Computed ─────────────────────────────────────────────────────────────────

  isActive = computed(() => {
    const proj = this.projectQuery.data()
    if (!proj) return false
    return this.projectService.getActiveProject(proj.product_family)?.id === proj.id
  })

  get docVarsMissing() { return !this.dvCiso || !this.dvEffectiveDate }

  polActiveAll   = computed(() => (this.policiesQuery.data() ?? []).filter(p => p.status !== 'archived'))
  polRemovedAll  = computed(() => (this.policiesQuery.data() ?? []).filter(p => p.status === 'archived'))
  polDisplayed   = computed(() => {
    const base  = this.polView() === 'active' ? this.polActiveAll() : this.polRemovedAll()
    const q     = this.polSearch.toLowerCase()
    return !q ? base : base.filter(p =>
      (p.document_id ?? '').toLowerCase().includes(q) ||
      (p.title ?? '').toLowerCase().includes(q) ||
      (p.control_group_code ?? '').toLowerCase().includes(q))
  })
  polDisplayedIds = computed(() => this.polDisplayed().map(p => p.id))
  polAllChecked   = computed(() => this.polDisplayedIds().length > 0 && this.polDisplayedIds().every(id => this.polSelected().has(id)))
  polSomeChecked  = computed(() => this.polDisplayedIds().some(id => this.polSelected().has(id)))

  implActiveAll   = computed(() => (this.implsQuery.data() ?? []).filter(i => i.status !== 'archived'))
  implRemovedAll  = computed(() => (this.implsQuery.data() ?? []).filter(i => i.status === 'archived'))
  implDisplayed   = computed(() => {
    const base  = this.implView() === 'active' ? this.implActiveAll() : this.implRemovedAll()
    const q     = this.implSearch.toLowerCase()
    return !q ? base : base.filter(i =>
      (i.document_id ?? '').toLowerCase().includes(q) ||
      (i.title ?? '').toLowerCase().includes(q) ||
      (i.control_group_code ?? '').toLowerCase().includes(q))
  })
  implDisplayedIds = computed(() => this.implDisplayed().map(i => i.id))
  implAllChecked   = computed(() => this.implDisplayedIds().length > 0 && this.implDisplayedIds().every(id => this.implSelected().has(id)))
  implSomeChecked  = computed(() => this.implDisplayedIds().some(id => this.implSelected().has(id)))

  polCodes    = computed(() => (this.policiesQuery.data() ?? []).map(p => p.control_group_code ?? ''))
  implCodes   = computed(() => (this.implsQuery.data() ?? []).map(i => i.control_group_code ?? ''))
  polUnique   = computed(() => new Set(this.polCodes().filter(Boolean)).size)
  implUnique  = computed(() => new Set(this.implCodes().filter(Boolean)).size)

  totalCg = (family: string): number => TOTAL_CG[family] ?? 53
  polPct  = computed(() => Math.min(100, Math.round((this.polUnique() / (this.totalCg(this.projectQuery.data()?.product_family ?? 'ISMS'))) * 100)))
  implPct = computed(() => Math.min(100, Math.round((this.implUnique() / (this.totalCg(this.projectQuery.data()?.product_family ?? 'ISMS'))) * 100)))
  overallPct = computed(() => Math.round((this.polPct() + this.implPct()) / 2))
  maxCovered = computed(() => Math.max(this.polUnique(), this.implUnique()))

  libTypeOptions = computed(() => {
    if (this.libraryMode() === 'implementations') return ['ALL', 'UG', 'TG']
    const pols = this.libPoliciesQuery.data()
    if (!pols) return ['ALL']
    return ['ALL', ...Array.from(new Set(pols.map(p => p.policy_type)))]
  })

  libRawRows = computed<(LibraryPolicyItem | LibraryImplItem)[]>(() =>
    this.libraryMode() === 'policies'
      ? (this.libPoliciesQuery.data() ?? [])
      : (this.libImplsQuery.data() ?? []))

  libFiltered = computed(() => {
    const rows  = this.libRawRows()
    const q     = this.libSearch.toLowerCase()
    const type  = this.libTypeFilter()
    return rows.filter((r: any) => {
      const matchSearch = !q || r.document_id.toLowerCase().includes(q) ||
        r.title.toLowerCase().includes(q) || r.control_group_code.toLowerCase().includes(q)
      const matchType = type === 'ALL' ||
        (this.libraryMode() === 'policies' ? r.policy_type === type : r.impl_type === type)
      return matchSearch && matchType
    })
  })

  libAvailableIds = computed(() =>
    this.libFiltered().filter((r: any) => !r.already_in_project).map((r: any) => r.id as string))

  libAllSelected = computed(() =>
    this.libAvailableIds().length > 0 &&
    this.libAvailableIds().every(id => this.libSelected().has(id)))

  libSomeSelected = computed(() =>
    this.libAvailableIds().some(id => this.libSelected().has(id)))

  editorDocTypeColor = computed(() => {
    const d = this.editorDoc()
    if (!d) return '#9E9E9E'
    if (d.mode === 'policy') return POL_TYPE_COLOR[d.docType ?? ''] ?? '#4472C4'
    return IMPL_TYPE_COLOR[d.docType ?? ''] ?? '#9E9E9E'
  })

  // ── Helpers ──────────────────────────────────────────────────────────────────

  familyColor = (family: string): string => FAMILY_COLOR[family] ?? '#4472C4'
  polTypeColor  = (t: string): string => POL_TYPE_COLOR[t] ?? '#9E9E9E'
  implTypeColor = (t: string): string => IMPL_TYPE_COLOR[t] ?? '#9E9E9E'
  ptColor       = (t: string): string => PT_COLOR[t] ?? '#9E9E9E'

  checklistsDisabled = (proj: ProjectFull): boolean =>
    proj.product_family === 'ISMS' && proj.project_subtype !== 'op'

  activateProject(proj: ProjectFull) {
    this.projectService.setActiveProject(proj.product_family, proj as unknown as ProjectRead)
  }

  deactivateProject() {
    const proj = this.projectQuery.data()
    if (proj) this.projectService.setActiveProject(proj.product_family, null)
  }

  // Doc vars
  private loadDocVars(proj: ProjectFull) {
    const dv = proj.doc_vars ?? {}
    this.dvCiso           = dv.ciso_name ?? ''
    this.dvCeo            = dv.ceo_name ?? ''
    this.dvDpo            = dv.dpo_name ?? ''
    this.dvLegalEntity    = dv.legal_entity ?? ''
    this.dvEffectiveDate  = dv.effective_date ?? ''
    this.dvReviewDate     = dv.review_date ?? ''
    this.dvClassification = dv.classification ?? ''
  }

  saveDocVars(projectId: string) {
    const vars: DocVars = {}
    if (this.dvCiso)           vars.ciso_name        = this.dvCiso
    if (this.dvCeo)            vars.ceo_name         = this.dvCeo
    if (this.dvDpo)            vars.dpo_name         = this.dvDpo
    if (this.dvLegalEntity)    vars.legal_entity     = this.dvLegalEntity
    if (this.dvEffectiveDate)  vars.effective_date   = this.dvEffectiveDate
    if (this.dvReviewDate)     vars.review_date      = this.dvReviewDate
    if (this.dvClassification) vars.classification   = this.dvClassification
    this.saveDocVarsMut.mutate(vars)
  }

  reapplyDocVars(projectId: string) {
    this.reapplyMut.mutate()
  }

  // Policies
  togglePolRow(id: string) {
    this.polSelected.update(s => {
      const n = new Set(s)
      n.has(id) ? n.delete(id) : n.add(id)
      return n
    })
  }
  togglePolAll() {
    if (this.polAllChecked()) this.polSelected.set(new Set())
    else this.polSelected.set(new Set(this.polDisplayedIds()))
  }

  // Impls
  toggleImplRow(id: string) {
    this.implSelected.update(s => {
      const n = new Set(s)
      n.has(id) ? n.delete(id) : n.add(id)
      return n
    })
  }
  toggleImplAll() {
    if (this.implAllChecked()) this.implSelected.set(new Set())
    else this.implSelected.set(new Set(this.implDisplayedIds()))
  }

  // Library drawer
  openLibraryDrawer(mode: 'policies' | 'implementations') {
    this.libraryMode.set(mode)
    this.libSearch    = ''
    this.libTypeFilter.set('ALL')
    this.libLangFilter.set('ALL')
    this.libSelected.set(new Set())
    this.libraryDrawerOpen.set(true)
  }

  toggleLibRow(id: string) {
    this.libSelected.update(s => {
      const n = new Set(s)
      n.has(id) ? n.delete(id) : n.add(id)
      return n
    })
  }
  toggleLibAll() {
    if (this.libAllSelected()) {
      this.libSelected.update(s => {
        const n = new Set(s)
        this.libAvailableIds().forEach(id => n.delete(id))
        return n
      })
    } else {
      this.libSelected.update(s => new Set([...s, ...this.libAvailableIds()]))
    }
  }
  selectAllLib() {
    this.libSelected.set(new Set(this.libAvailableIds()))
  }

  async importSelected() {
    const ids = [...this.libSelected()]
    if (!ids.length) return
    this.libImporting.set(true)
    try {
      for (const id of ids) {
        if (this.libraryMode() === 'policies') await this.addPolMut.mutateAsync(id)
        else await this.addImplMut.mutateAsync(id)
      }
      const mode = this.libraryMode()
      this.qc.invalidateQueries({ queryKey: [mode === 'policies' ? 'project-policies' : 'project-impls', this.projectId()] })
      this.qc.invalidateQueries({ queryKey: ['project', this.projectId()] })
      this.qc.invalidateQueries({ queryKey: ['library', mode === 'policies' ? 'policies' : 'implementations', this.projectId()] })
      this.libSelected.set(new Set())
      this.libraryDrawerOpen.set(false)
    } finally {
      this.libImporting.set(false)
    }
  }

  // Doc editor
  openDocEditor(
    _projectId: string,
    docId: string,
    mode: 'policy' | 'implementation',
    title: string | null,
    docType: string | null
  ) {
    this.editorDirty.set(false)
    this.editorSaved.set(false)
    this.editorContent = ''
    this.editorDoc.set({ id: docId, mode, title, docType })
  }

  closeDocEditor() {
    this.editorDoc.set(null)
    this.editorContent = ''
    this.editorDirty.set(false)
    this.editorSaved.set(false)
  }

  onEditorChange() {
    this.editorDirty.set(true)
    this.editorSaved.set(false)
  }

  onEditorRteChange(value: string) {
    this.editorContent = value
    this.editorDirty.set(true)
    this.editorSaved.set(false)
  }

  saveDocContent() {
    // Strip ISMS-CORE watermark and QA footer before saving
    const cleaned = this.editorContent
      .replace(/^<!--\s*ISMS-CORE:[^\n]*-->\s*\n?/m, '')
      .replace(/\n?<!--\s*QA_VERIFIED:[^\n]*-->\s*$/m, '')
      .trimStart()
    this.saveDocMut.mutate(cleaned)
  }


  // Invalidate helpers
  private invalidatePolicies() {
    this.qc.invalidateQueries({ queryKey: ['project-policies', this.projectId()] })
    this.qc.invalidateQueries({ queryKey: ['project', this.projectId()] })
    this.qc.invalidateQueries({ queryKey: ['library', 'policies', this.projectId()] })
    this.polSelected.set(new Set())
  }

  private invalidateImpls() {
    this.qc.invalidateQueries({ queryKey: ['project-impls', this.projectId()] })
    this.qc.invalidateQueries({ queryKey: ['project', this.projectId()] })
    this.qc.invalidateQueries({ queryKey: ['library', 'implementations', this.projectId()] })
    this.implSelected.set(new Set())
  }

  clearPolSelected() { this.polSelected.set(new Set()) }
  clearImplSelected() { this.implSelected.set(new Set()) }
}
