import { Component, inject, signal, computed } from '@angular/core'
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
import { MatChipsModule } from '@angular/material/chips'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatIconModule } from '@angular/material/icon'
import { MatExpansionModule } from '@angular/material/expansion'
import { MatButtonToggleModule } from '@angular/material/button-toggle'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatDialogModule, MatDialog } from '@angular/material/dialog'
import { MatProgressBarModule } from '@angular/material/progress-bar'
import { MatDividerModule } from '@angular/material/divider'
import { MatSnackBar, MatSnackBarModule } from '@angular/material/snack-bar'

import {
  QaApiService,
  type CorrelationResultRead,
  type QASummaryBucket,
  type SynonymRule,
  type ReferenceCorpusStatus,
  type OrgProjectSummaryItem,
} from '../../api/qa-api.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'
import { ThemeService } from '../../core/services/theme.service'

// ── Colour helpers ────────────────────────────────────────────────────────────

const STATUS_BG: Record<string, string> = {
  pass:         'rgba(46,125,50,0.15)',
  warning:      'rgba(230,160,0,0.15)',
  fail:         'rgba(192,0,0,0.15)',
  needs_review: 'rgba(255,255,255,0.07)',
}
const STATUS_FG: Record<string, string> = {
  pass:         '#C6EFCE',
  warning:      '#FFEB9C',
  fail:         '#FFC7CE',
  needs_review: '#d9d9d9',
}

const METHOD_LABELS: Record<string, string> = {
  existence:      'Existence Check',
  keyword:        'Keyword Correlation',
  semantic:       'Semantic (Mini LLM)',
  semantic_claude:'Semantic (Claude AI)',
}
const METHOD_SUBTITLES: Record<string, string> = {
  existence:      'Verifies each control group has the required artefacts',
  keyword:        'Checks keyword coverage across all ISO standard implementations',
  semantic:       'Cosine similarity between ISO control text and implementation embeddings',
  semantic_claude:'Claude AI scores how well each implementation addresses the ISO control requirements',
}

function fmtDate(d: string): string {
  const dt = new Date(d)
  return dt.toLocaleDateString('en-GB', { day: '2-digit', month: 'short', hour: '2-digit', minute: '2-digit' })
}
function fromNow(d: string): string {
  const diff = Date.now() - new Date(d).getTime()
  const mins = Math.floor(diff / 60000)
  if (mins < 60) return `${mins}m ago`
  const hrs = Math.floor(mins / 60)
  if (hrs < 24) return `${hrs}h ago`
  return `${Math.floor(hrs / 24)}d ago`
}

// ── Component ─────────────────────────────────────────────────────────────────

@Component({
  selector: 'app-qa',
  standalone: true,
  imports: [
    FormsModule,
    MatTabsModule, MatCardModule, MatButtonModule, MatFormFieldModule,
    MatInputModule, MatSelectModule, MatTableModule, MatChipsModule,
    MatProgressSpinnerModule, MatIconModule, MatExpansionModule,
    MatButtonToggleModule, MatTooltipModule, MatDialogModule,
    MatProgressBarModule, MatDividerModule, MatSnackBarModule,
    PageHeaderComponent,
  ],
  template: `
<app-page-header
  title="QA Engine"
  [subtitle]="currentSubtitle()">
  <div actions>
    @if (activeTab() === 0) {
      <div class="run-buttons">
        <button mat-stroked-button [disabled]="isRunning()"
          (click)="runCheck('existence')">
          @if (existenceMut.isPending()) { <mat-spinner diameter="14" /> }
          @else { <mat-icon>play_arrow</mat-icon> }
          Existence
        </button>
        <button mat-stroked-button [disabled]="isRunning()"
          (click)="runCheck('keyword')">
          @if (keywordMut.isPending()) { <mat-spinner diameter="14" /> }
          @else { <mat-icon>play_arrow</mat-icon> }
          Keyword
        </button>
        <button mat-stroked-button [disabled]="isRunning()"
          (click)="runCheck('semantic')">
          @if (semanticMiniMut.isPending()) { <mat-spinner diameter="14" /> }
          @else { <mat-icon>psychology</mat-icon> }
          Mini LLM
        </button>
        <button mat-stroked-button [disabled]="isRunning()"
          (click)="runCheck('semantic_claude')">
          @if (semanticClaudeMut.isPending()) { <mat-spinner diameter="14" /> }
          @else { <mat-icon>auto_awesome</mat-icon> }
          Claude AI
        </button>
      </div>
    }
  </div>
</app-page-header>

@if (runResult()) {
  <div class="alert alert-success">
    <mat-icon>check_circle</mat-icon>
    {{ runResult() }}
    <button mat-icon-button (click)="runResult.set(null)"><mat-icon>close</mat-icon></button>
  </div>
}

<mat-tab-group [selectedIndex]="activeTab()" (selectedIndexChange)="activeTab.set($event)">

  <!-- ── TAB 0: Results ─────────────────────────────────────────────────────── -->
  <mat-tab label="Results">
    <div class="tab-content">

      <!-- Method toggle -->
      <div class="filter-row">
        <mat-button-toggle-group [value]="method()" (change)="onMethodChange($event.value)">
          <mat-button-toggle value="existence">Existence</mat-button-toggle>
          <mat-button-toggle value="keyword">Keyword</mat-button-toggle>
          <mat-button-toggle value="semantic">Mini LLM</mat-button-toggle>
          <mat-button-toggle value="semantic_claude">Claude AI</mat-button-toggle>
        </mat-button-toggle-group>
      </div>

      <mat-divider class="results-divider" />

      <!-- Summary cards -->
      @if (summaryQuery.isSuccess() && summary()) {
        <div class="summary-grid">
          <mat-card class="summary-card summary-card--overall">
            <mat-card-content>
              <div class="sc-header">
                <span class="sc-label">Overall</span>
                <span class="sc-pct" [style.color]="overallColor()">{{ overallPct() }}%</span>
              </div>
              <mat-progress-bar mode="determinate" [value]="overallPct()" class="summary-bar" />
              <div class="chips-row">
                <span class="chip chip-present">{{ totalPassing() }} pass</span>
                <span class="dim-sm">/ {{ totalChecks() }}</span>
              </div>
            </mat-card-content>
          </mat-card>
          @if (showFw()) {
            <mat-card class="summary-card">
              <mat-card-content>
                <div class="sc-header"><span class="sc-label">Framework</span><span class="sc-pct sc-pct--fw">{{ Math.round(summary()!.framework.pass_rate * 100) }}%</span></div>
                <mat-progress-bar mode="determinate" [value]="Math.round(summary()!.framework.pass_rate * 100)" class="summary-bar" />
                <div class="chips-row">
                  <span class="chip chip-present">{{ summary()!.framework.pass_count }} pass</span>
                  @if (summary()!.framework.warning_count > 0) { <span class="chip chip-warn">{{ summary()!.framework.warning_count }} warn</span> }
                  @if (summary()!.framework.fail_count > 0) { <span class="chip chip-missing">{{ summary()!.framework.fail_count }} fail</span> }
                  <span class="dim-sm">/ {{ summary()!.framework.total }}</span>
                </div>
              </mat-card-content>
            </mat-card>
          }
          @if (showOp()) {
            <mat-card class="summary-card">
              <mat-card-content>
                <div class="sc-header"><span class="sc-label">Operational</span><span class="sc-pct sc-pct--op">{{ Math.round(summary()!.operational.pass_rate * 100) }}%</span></div>
                <mat-progress-bar mode="determinate" [value]="Math.round(summary()!.operational.pass_rate * 100)" class="summary-bar" />
                <div class="chips-row">
                  <span class="chip chip-present">{{ summary()!.operational.pass_count }} pass</span>
                  @if (summary()!.operational.warning_count > 0) { <span class="chip chip-warn">{{ summary()!.operational.warning_count }} warn</span> }
                  @if (summary()!.operational.fail_count > 0) { <span class="chip chip-missing">{{ summary()!.operational.fail_count }} fail</span> }
                  <span class="dim-sm">/ {{ summary()!.operational.total }}</span>
                </div>
              </mat-card-content>
            </mat-card>
          }
          @if (showPrv()) {
            <mat-card class="summary-card">
              <mat-card-content>
                <div class="sc-header"><span class="sc-label">Privacy</span><span class="sc-pct sc-pct--prv">{{ Math.round(summary()!.privacy.pass_rate * 100) }}%</span></div>
                <mat-progress-bar mode="determinate" [value]="Math.round(summary()!.privacy.pass_rate * 100)" class="summary-bar" />
                <div class="chips-row">
                  <span class="chip chip-present">{{ summary()!.privacy.pass_count }} pass</span>
                  @if (summary()!.privacy.warning_count > 0) { <span class="chip chip-warn">{{ summary()!.privacy.warning_count }} warn</span> }
                  @if (summary()!.privacy.fail_count > 0) { <span class="chip chip-missing">{{ summary()!.privacy.fail_count }} fail</span> }
                  <span class="dim-sm">/ {{ summary()!.privacy.total }}</span>
                </div>
              </mat-card-content>
            </mat-card>
          }
          @if (showCld()) {
            <mat-card class="summary-card">
              <mat-card-content>
                <div class="sc-header"><span class="sc-label">Cloud</span><span class="sc-pct sc-pct--cld">{{ Math.round(summary()!.cloud.pass_rate * 100) }}%</span></div>
                <mat-progress-bar mode="determinate" [value]="Math.round(summary()!.cloud.pass_rate * 100)" class="summary-bar" />
                <div class="chips-row">
                  <span class="chip chip-present">{{ summary()!.cloud.pass_count }} pass</span>
                  @if (summary()!.cloud.warning_count > 0) { <span class="chip chip-warn">{{ summary()!.cloud.warning_count }} warn</span> }
                  @if (summary()!.cloud.fail_count > 0) { <span class="chip chip-missing">{{ summary()!.cloud.fail_count }} fail</span> }
                  <span class="dim-sm">/ {{ summary()!.cloud.total }}</span>
                </div>
              </mat-card-content>
            </mat-card>
          }
          @if (showAi()) {
            <mat-card class="summary-card">
              <mat-card-content>
                <div class="sc-header"><span class="sc-label">AI</span><span class="sc-pct sc-pct--ai">{{ Math.round(summary()!.ai.pass_rate * 100) }}%</span></div>
                <mat-progress-bar mode="determinate" [value]="Math.round(summary()!.ai.pass_rate * 100)" class="summary-bar" />
                <div class="chips-row">
                  <span class="chip chip-present">{{ summary()!.ai.pass_count }} pass</span>
                  @if (summary()!.ai.warning_count > 0) { <span class="chip chip-warn">{{ summary()!.ai.warning_count }} warn</span> }
                  @if (summary()!.ai.fail_count > 0) { <span class="chip chip-missing">{{ summary()!.ai.fail_count }} fail</span> }
                  <span class="dim-sm">/ {{ summary()!.ai.total }}</span>
                </div>
              </mat-card-content>
            </mat-card>
          }
        </div>
      }

      <!-- Filters -->
      <div class="filter-row filter-row--mt">
        <mat-button-toggle-group [value]="product()" (change)="product.set($event.value)">
          <mat-button-toggle value="all">All</mat-button-toggle>
          @if (method() === 'existence') {
            <mat-button-toggle value="framework">Framework</mat-button-toggle>
            <mat-button-toggle value="operational">Operational</mat-button-toggle>
          }
          @if (method() !== 'existence') {
            <mat-button-toggle value="isms">ISMS</mat-button-toggle>
          }
          <mat-button-toggle value="privacy">Privacy</mat-button-toggle>
          <mat-button-toggle value="cloud">Cloud</mat-button-toggle>
          <mat-button-toggle value="ai">AI</mat-button-toggle>
        </mat-button-toggle-group>

        <mat-button-toggle-group [value]="statusFilter()" (change)="statusFilter.set($event.value)">
          <mat-button-toggle value="all">All</mat-button-toggle>
          <mat-button-toggle value="pass">Pass</mat-button-toggle>
          <mat-button-toggle value="warning">Warning</mat-button-toggle>
          <mat-button-toggle value="fail">Fail</mat-button-toggle>
          <mat-button-toggle value="needs_review">Review</mat-button-toggle>
        </mat-button-toggle-group>

        @if (resultsQuery.isSuccess()) {
          <span class="count-label">{{ results().length }} result{{ results().length !== 1 ? 's' : '' }}</span>
        }
      </div>

      <!-- No results -->
      @if (resultsQuery.isSuccess() && results().length === 0 && !resultsQuery.isFetching()) {
        <div class="empty-state">
          <mat-icon>info_outline</mat-icon>
          @if (totalChecks() === 0) {
            No {{ methodLabels[method()] }} results yet. Click the Run button above.
          } @else {
            0 results for the selected filter.
          }
        </div>
      }

      <!-- Results table -->
      @if (results().length > 0) {
        <div class="table-wrapper">
          <table mat-table [dataSource]="results()" class="qa-table">

            <ng-container matColumnDef="control_group">
              <th mat-header-cell *matHeaderCellDef>Control Group</th>
              <td mat-cell *matCellDef="let row">
                <div class="control-group-cell">
                  <span class="code">{{ row.control_group_code }}</span>
                  <span class="name">{{ row.control_group_name }}</span>
                </div>
              </td>
            </ng-container>

            <ng-container matColumnDef="product">
              <th mat-header-cell *matHeaderCellDef>Product</th>
              <td mat-cell *matCellDef="let row">
                <span class="chip chip-product">{{ row.product_type }}</span>
              </td>
            </ng-container>

            <ng-container matColumnDef="status">
              <th mat-header-cell *matHeaderCellDef>Status</th>
              <td mat-cell *matCellDef="let row">
                <span class="chip"
                  [style.background]="statusBg(row.qa_status)"
                  [style.color]="statusFg(row.qa_status)">
                  {{ row.qa_status.replace('_', ' ') }}
                </span>
              </td>
            </ng-container>

            <ng-container matColumnDef="strength">
              <th mat-header-cell *matHeaderCellDef>Strength</th>
              <td mat-cell *matCellDef="let row">
                <div class="strength-cell">
                  <mat-progress-bar mode="determinate"
                    [value]="(row.correlation_strength ?? 0) * 100"
                    [color]="row.qa_status === 'pass' ? 'primary' : row.qa_status === 'fail' ? 'warn' : 'accent'" />
                  <span class="strength-pct">{{ Math.round((row.correlation_strength ?? 0) * 100) }}%</span>
                </div>
              </td>
            </ng-container>

            <ng-container matColumnDef="details">
              <th mat-header-cell *matHeaderCellDef>Details</th>
              <td mat-cell *matCellDef="let row">
                <div class="chips-row">
                  @for (kw of getPresent(row); track kw) {
                    <span class="chip chip-present">{{ kw }}</span>
                  }
                  @if (getPresent(row).length === 0) {
                    <span class="dim">—</span>
                  }
                </div>
              </td>
            </ng-container>

            <ng-container matColumnDef="missing">
              <th mat-header-cell *matHeaderCellDef>Missing / Gaps</th>
              <td mat-cell *matCellDef="let row">
                <div class="chips-row">
                  @for (kw of getMissing(row); track kw) {
                    <span class="chip chip-missing">{{ kw }}</span>
                  }
                  @if (getMissing(row).length === 0) {
                    <span class="dim">—</span>
                  }
                </div>
              </td>
            </ng-container>

            <ng-container matColumnDef="run">
              <th mat-header-cell *matHeaderCellDef>Run</th>
              <td mat-cell *matCellDef="let row">
                <span class="dim-sm">{{ fmtDate(row.run_date) }}</span>
              </td>
            </ng-container>

            <tr mat-header-row *matHeaderRowDef="displayedCols()"></tr>
            <tr mat-row *matRowDef="let row; columns: displayedCols();" class="qa-row"></tr>
          </table>
        </div>
      }

      @if (resultsQuery.isFetching()) {
        <div class="spinner-row"><mat-spinner diameter="32" /></div>
      }
    </div>
  </mat-tab>

  <!-- ── TAB 1: Synonyms ────────────────────────────────────────────────────── -->
  <mat-tab label="Synonyms">
    <div class="tab-content">
      <div class="section-header">
        <span class="dim">{{ synonymsQuery.data()?.length ?? 0 }} rules — used by the keyword correlation engine.</span>
        <button mat-flat-button color="primary" (click)="openAddSynonymDialog()">
          <mat-icon>add</mat-icon> Add Rule
        </button>
      </div>

      @if (synonymsQuery.isLoading()) {
        <mat-spinner diameter="24" />
      }

      @if (synonymsQuery.isSuccess()) {
        <div class="table-wrapper">
          <table mat-table [dataSource]="synonymsQuery.data()!" class="qa-table">

            <ng-container matColumnDef="keyword">
              <th mat-header-cell *matHeaderCellDef>Keyword</th>
              <td mat-cell *matCellDef="let rule">
                <span class="mono primary">{{ rule.keyword }}</span>
              </td>
            </ng-container>

            <ng-container matColumnDef="synonyms">
              <th mat-header-cell *matHeaderCellDef>Synonyms</th>
              <td mat-cell *matCellDef="let rule">
                <div class="chips-row">
                  @for (s of rule.synonyms; track s) {
                    <span class="chip chip-neutral">{{ s }}</span>
                  }
                </div>
              </td>
            </ng-container>

            <ng-container matColumnDef="notes">
              <th mat-header-cell *matHeaderCellDef>Notes</th>
              <td mat-cell *matCellDef="let rule">
                <span class="dim">{{ rule.notes ?? '—' }}</span>
              </td>
            </ng-container>

            <ng-container matColumnDef="actions">
              <th mat-header-cell *matHeaderCellDef class="col-actions">Actions</th>
              <td mat-cell *matCellDef="let rule" class="col-actions">
                <button mat-icon-button matTooltip="Edit" (click)="openEditSynonymDialog(rule)">
                  <mat-icon>edit</mat-icon>
                </button>
                <button mat-icon-button matTooltip="Delete" color="warn"
                  (click)="deleteSynonym(rule.id)">
                  <mat-icon>delete</mat-icon>
                </button>
              </td>
            </ng-container>

            <tr mat-header-row *matHeaderRowDef="synonymCols"></tr>
            <tr mat-row *matRowDef="let row; columns: synonymCols;"></tr>
          </table>
        </div>
      }

      <!-- Add dialog (inline, shown as expansion) -->
      @if (showAddSynonym()) {
        <mat-card class="inline-dialog">
          <mat-card-header><mat-card-title>Add Synonym Rule</mat-card-title></mat-card-header>
          <mat-card-content>
            <div class="dialog-form">
              <mat-form-field appearance="outline">
                <mat-label>Keyword</mat-label>
                <input matInput [(ngModel)]="newKeyword" placeholder="e.g. addressing" />
                <mat-hint>The ISO term to match</mat-hint>
              </mat-form-field>
              <mat-form-field appearance="outline">
                <mat-label>Synonyms</mat-label>
                <input matInput [(ngModel)]="newSynonymsText" placeholder="e.g. handling, managing, treating" />
                <mat-hint>Comma-separated equivalents</mat-hint>
              </mat-form-field>
              <mat-form-field appearance="outline">
                <mat-label>Notes (optional)</mat-label>
                <input matInput [(ngModel)]="newNotes" />
              </mat-form-field>
            </div>
          </mat-card-content>
          <mat-card-actions>
            <button mat-button (click)="showAddSynonym.set(false)">Cancel</button>
            <button mat-flat-button color="primary"
              [disabled]="!newKeyword.trim() || !newSynonymsText.trim() || createSynonymMut.isPending()"
              (click)="submitNewSynonym()">
              {{ createSynonymMut.isPending() ? 'Saving…' : 'Save' }}
            </button>
          </mat-card-actions>
        </mat-card>
      }

      <!-- Edit dialog (inline) -->
      @if (editingRule()) {
        <mat-card class="inline-dialog">
          <mat-card-header>
            <mat-card-title>Edit — <em>{{ editingRule()!.keyword }}</em></mat-card-title>
          </mat-card-header>
          <mat-card-content>
            <div class="dialog-form">
              <mat-form-field appearance="outline">
                <mat-label>Synonyms</mat-label>
                <input matInput [(ngModel)]="editSynonymsText" placeholder="Comma-separated equivalents" />
              </mat-form-field>
              <mat-form-field appearance="outline">
                <mat-label>Notes (optional)</mat-label>
                <input matInput [(ngModel)]="editNotes" />
              </mat-form-field>
            </div>
          </mat-card-content>
          <mat-card-actions>
            <button mat-button (click)="editingRule.set(null)">Cancel</button>
            <button mat-flat-button color="primary"
              [disabled]="!editSynonymsText.trim() || updateSynonymMut.isPending()"
              (click)="submitEditSynonym()">
              {{ updateSynonymMut.isPending() ? 'Saving…' : 'Save' }}
            </button>
          </mat-card-actions>
        </mat-card>
      }
    </div>
  </mat-tab>

  <!-- ── TAB 2: Reference Corpus ────────────────────────────────────────────── -->
  <mat-tab label="Reference Corpus">
    <div class="tab-content">
      <div class="section-header">
        <div>
          <p class="section-title">ISO &amp; Regulatory Reference Corpus</p>
          <p class="dim corpus-desc">
            Normative text from all ISO/regulatory standards — indexed automatically on first boot.
            Use Reload only after updating seed files and rebuilding the container.
          </p>
        </div>
        <button mat-flat-button color="primary"
          [disabled]="reloadCorpusMut.isPending() || corpusQuery.data()?.available === false"
          (click)="reloadCorpus()">
          @if (reloadCorpusMut.isPending()) { <mat-spinner diameter="14" /> }
          @else { <mat-icon>play_arrow</mat-icon> }
          {{ reloadCorpusMut.isPending() ? 'Reloading…' : 'Reload from Seeds' }}
        </button>
      </div>

      @if (reloadCorpusMut.isPending()) {
        <div class="alert alert-info">Reloading from seed files — this takes a few seconds…</div>
      }
      @if (corpusLoadResult()) {
        <div class="alert alert-success">{{ corpusLoadResult() }}</div>
      }

      @if (corpusQuery.isLoading()) {
        <mat-spinner diameter="24" />
      }

      @if (corpusQuery.isSuccess() && corpusQuery.data()) {
        @let cs = corpusQuery.data()!;
        @if (!cs.available) {
          <div class="alert alert-warn">OpenSearch not available — reference corpus cannot be loaded.</div>
        }
        @if (cs.available && !cs.indexed) {
          <div class="alert alert-info">No reference corpus indexed yet. Click "Reload from Seeds" to index all ISO documents.</div>
        }
        @if (cs.indexed) {
          <p class="dim">{{ cs.total_chunks.toLocaleString() }} chunks indexed across {{ cs.standards.length }} standards</p>
        }
        @if (cs.standards.length > 0) {
          <div class="table-wrapper">
            <table mat-table [dataSource]="cs.standards" class="qa-table">
              <ng-container matColumnDef="standard">
                <th mat-header-cell *matHeaderCellDef>Standard</th>
                <td mat-cell *matCellDef="let s"><strong>{{ s.standard }}</strong></td>
              </ng-container>
              <ng-container matColumnDef="chunks">
                <th mat-header-cell *matHeaderCellDef class="col-right">Chunks</th>
                <td mat-cell *matCellDef="let s" class="col-right">
                  <span class="chip chip-neutral">{{ s.chunks.toLocaleString() }}</span>
                </td>
              </ng-container>
              <tr mat-header-row *matHeaderRowDef="['standard','chunks']"></tr>
              <tr mat-row *matRowDef="let row; columns: ['standard','chunks'];"></tr>
            </table>
          </div>
        }
      }
    </div>
  </mat-tab>

  <!-- ── TAB 3: Projects ────────────────────────────────────────────────────── -->
  <mat-tab label="Projects">
    <div class="tab-content">
      <div class="filter-row">
        <mat-button-toggle-group [value]="projectsMethod()" (change)="projectsMethod.set($event.value)">
          <mat-button-toggle value="existence">Existence</mat-button-toggle>
          <mat-button-toggle value="keyword">Keyword</mat-button-toggle>
          <mat-button-toggle value="semantic">Mini LLM</mat-button-toggle>
        </mat-button-toggle-group>
        @if (orgProjectsQuery.isSuccess() && orgProjectsQuery.data()!.length > 0) {
          <span class="dim">
            {{ orgProjectsQuery.data()!.length }} project{{ orgProjectsQuery.data()!.length !== 1 ? 's' : '' }}
            — avg {{ avgPassRate() }}%
          </span>
        }
      </div>

      @if (orgProjectsQuery.isLoading()) {
        <div class="spinner-row"><mat-spinner diameter="32" /></div>
      }

      @if (orgProjectsQuery.isSuccess() && orgProjectsQuery.data()!.length === 0) {
        <div class="empty-state">
          <mat-icon>info_outline</mat-icon>
          No projects found for this organisation.
        </div>
      }

      @if (orgProjectsQuery.isSuccess() && orgProjectsQuery.data()!.length > 0) {
        <div class="project-cards-grid">
          @for (p of orgProjectsQuery.data()!; track p.project_id) {
            <mat-card class="project-health-card" [class.phc-expanded]="expandedProjectId() === p.project_id">
              <mat-card-content>
                <div class="phc-header">
                  <div class="phc-info">
                    <p class="phc-name">{{ p.project_name }}</p>
                    <span class="chip chip-family">{{ p.product_family }}</span>
                  </div>
                  <span class="phc-pct" [style.color]="p.total > 0 ? projectColor(p.pass_rate) : 'var(--mat-sys-on-surface-variant)'">
                    {{ p.total > 0 ? Math.round(p.pass_rate * 100) + '%' : '—' }}
                  </span>
                </div>
                @if (p.total > 0) {
                  <mat-progress-bar mode="determinate"
                    [value]="Math.round(p.pass_rate * 100)"
                    class="project-bar" />
                  <div class="chips-row phc-chips-row">
                    <span class="chip chip-present">{{ p.pass }} pass</span>
                    @if (p.warning > 0) {
                      <span class="chip chip-warn phc-chip-btn"
                        (click)="toggleProjectDetail(p.project_id)">{{ p.warning }} warn</span>
                    }
                    @if (p.fail > 0) {
                      <span class="chip chip-missing phc-chip-btn"
                        (click)="toggleProjectDetail(p.project_id)">{{ p.fail }} fail</span>
                    }
                    @if (p.needs_review > 0) {
                      <span class="chip chip-neutral phc-chip-btn"
                        (click)="toggleProjectDetail(p.project_id)">{{ p.needs_review }} review</span>
                    }
                    <span class="dim-sm">/ {{ p.total }}</span>
                    @if (p.fail > 0 || p.warning > 0 || p.needs_review > 0) {
                      <mat-icon class="phc-expand-icon"
                        (click)="toggleProjectDetail(p.project_id)">
                        {{ expandedProjectId() === p.project_id ? 'expand_less' : 'expand_more' }}
                      </mat-icon>
                    }
                  </div>
                  @if (p.last_run) {
                    <p class="phc-last-run">{{ fromNow(p.last_run) }} · {{ methodLabels[projectsMethod()] }}</p>
                  }
                  <!-- Detail panel -->
                  @if (expandedProjectId() === p.project_id) {
                    <div class="phc-detail">
                      @if (projectDetailQuery.isFetching()) {
                        <div class="phc-detail-loading"><mat-spinner diameter="16" /></div>
                      } @else {
                        @for (r of projectDetailFails(); track r.id) {
                          <div class="phc-detail-row">
                            <span class="phc-detail-code">{{ r.control_group_code }}</span>
                            <span class="phc-detail-name">{{ r.control_group_name }}</span>
                            <span class="chip phc-detail-status"
                              [style.background]="statusBg(r.qa_status)"
                              [style.color]="statusFg(r.qa_status)">
                              {{ r.qa_status.replace('_', ' ') }}
                            </span>
                          </div>
                        }
                        @if (projectDetailFails().length === 0) {
                          <p class="dim" style="font-size:.7rem;padding:4px 0">No non-passing results found.</p>
                        }
                      }
                    </div>
                  }
                } @else {
                  <p class="phc-not-run">No QA results yet</p>
                }
                <button mat-stroked-button class="phc-run-btn"
                  [disabled]="runningProjectId() === p.project_id"
                  (click)="runProjectCheck(p.project_id)">
                  @if (runningProjectId() === p.project_id) {
                    <mat-spinner diameter="12" />
                  } @else {
                    <mat-icon>{{ p.total > 0 ? 'refresh' : 'play_arrow' }}</mat-icon>
                  }
                  {{ p.total > 0 ? 'Re-run' : 'Run QA' }}
                </button>
              </mat-card-content>
            </mat-card>
          }
        </div>
      }
    </div>
  </mat-tab>

</mat-tab-group>

  `,
  styles: [`
    :host { display: block; padding: 24px; }

    .run-buttons { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
    .last-run { font-size: 0.75rem; color: var(--mat-sys-on-surface-variant); }

    .tab-content { padding: 12px 0; }

    .filter-row {
      display: flex; align-items: center; gap: 12px; flex-wrap: wrap; margin-bottom: 8px;
    }

    .summary-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
      gap: 10px;
      margin-bottom: 14px;
    }
    .summary-card { }
    .sc-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 2px; }
    .sc-label { font-size: 0.78rem; color: var(--mat-sys-on-surface-variant); }
    .sc-pct { font-size: 1.4rem; font-weight: 700; }

    .table-wrapper {
      overflow-x: auto; margin-top: 12px;
      background: var(--mat-sys-surface-container);
      border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 8px;
      overflow: hidden;
    }
    .qa-table { width: 100%; }
    .qa-row:hover { background: rgba(255,255,255,0.02); }

    .control-group-cell { display: flex; flex-direction: column; }
    .control-group-cell .code { font-weight: 600; font-size: 0.82rem; }
    .control-group-cell .name { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); }

    .strength-cell { display: flex; align-items: center; gap: 8px; min-width: 100px; }
    .strength-pct { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); min-width: 30px; }

    .chips-row { display: flex; gap: 4px; flex-wrap: wrap; align-items: center; }
    .chip {
      display: inline-block; padding: 2px 7px; border-radius: 10px;
      font-size: 0.62rem; font-weight: 600; line-height: 1.6;
    }
    .chip-product { background: rgba(68,114,196,0.15); color: #93bbf5; }
    .chip-present { background: rgba(46,125,50,0.15); color: #C6EFCE; }
    .chip-missing { background: rgba(192,0,0,0.15); color: #FFC7CE; }
    .chip-warn    { background: rgba(230,160,0,0.15); color: #FFEB9C; }
    .chip-neutral { background: rgba(255,255,255,0.07); color: #d9d9d9; }
    .chip-family  { background: rgba(68,114,196,0.15); color: #93bbf5; }

    :host-context([data-theme='light']) {
      .chip-product { background: rgba(68,114,196,0.12); color: #1565c0; }
      .chip-present { background: rgba(46,125,50,0.12); color: #1b5e20; }
      .chip-missing { background: rgba(192,0,0,0.12);   color: #9e0000; }
      .chip-warn    { background: rgba(230,145,0,0.15);  color: #7a4800; }
      .chip-neutral { background: rgba(0,0,0,0.07);      color: #424242; }
      .chip-family  { background: rgba(68,114,196,0.12); color: #1565c0; }
      .sc-pct--op  { color: #2e7d32; }
      .sc-pct--cld { color: #0277bd; }
      .sc-pct--ai  { color: #bf360c; }
    }

    .mono { font-family: monospace; }
    .primary { color: var(--mat-sys-primary); }
    .dim { font-size: 0.78rem; color: var(--mat-sys-on-surface-variant); }
    .dim-sm { font-size: 0.65rem; color: var(--mat-sys-on-surface-variant); }

    .count-label { font-size: 0.78rem; color: var(--mat-sys-on-surface-variant); }

    .section-header {
      display: flex; justify-content: space-between; align-items: flex-start;
      margin-bottom: 16px; gap: 16px;
    }
    .section-title { font-weight: 600; font-size: 0.9rem; margin: 0; }

    .spinner-row { display: flex; justify-content: center; padding: 32px; }
    .empty-state {
      display: flex; align-items: center; gap: 8px; padding: 32px;
      color: var(--mat-sys-on-surface-variant); font-size: 0.9rem;
      justify-content: center;
    }

    .alert {
      display: flex; align-items: center; gap: 8px;
      padding: 10px 14px; border-radius: 6px; margin-bottom: 16px;
      font-size: 0.85rem;
    }
    .alert-success { background: rgba(46,125,50,0.12); color: #C6EFCE; }
    .alert-info    { background: rgba(21,101,192,0.12); color: #9fc8f0; }
    .alert-warn    { background: rgba(230,160,0,0.12);  color: #FFEB9C; }

    .inline-dialog {
      margin-top: 16px; max-width: 480px;
    }
    .dialog-form {
      display: flex; flex-direction: column; gap: 12px; padding-top: 8px;
    }
    .dialog-form mat-form-field { width: 100%; }

    .project-cards-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 12px;
      margin-top: 16px;
    }
    .project-health-card { cursor: default; }
    .phc-expanded { outline: 1px solid var(--mat-sys-primary); }
    .phc-header { display: flex; justify-content: space-between; align-items: flex-start; }
    .phc-info { flex: 1; min-width: 0; }
    .phc-name {
      font-weight: 600; font-size: 0.82rem; margin: 0 0 4px;
      overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
    }
    .phc-pct { font-size: 1.4rem; font-weight: 700; line-height: 1; margin-left: 8px; }
    .phc-last-run { font-size: 0.62rem; color: var(--mat-sys-on-surface-variant); margin: 4px 0 0; }
    .phc-chips-row { cursor: default; }
    .phc-chip-btn { cursor: pointer; }
    .phc-chip-btn:hover { opacity: 0.8; }
    .phc-expand-icon {
      font-size: 16px; height: 16px; width: 16px; cursor: pointer;
      color: var(--mat-sys-on-surface-variant); margin-left: auto;
    }
    .phc-detail {
      margin-top: 8px;
      border-top: 1px solid var(--mat-sys-outline-variant);
      padding-top: 6px;
      max-height: 220px;
      overflow-y: auto;
    }
    .phc-detail-loading { display: flex; justify-content: center; padding: 8px; }
    .phc-detail-row {
      display: flex; align-items: center; gap: 6px;
      padding: 3px 0; border-bottom: 1px solid rgba(255,255,255,0.04);
    }
    .phc-detail-code { font-size: 0.68rem; font-weight: 700; min-width: 52px; color: var(--mat-sys-primary); }
    .phc-detail-name { font-size: 0.68rem; flex: 1; color: var(--mat-sys-on-surface-variant); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .phc-detail-status { font-size: 0.6rem; white-space: nowrap; }

    /* Extracted inline styles */
    .results-divider { margin-bottom:10px; }
    .summary-bar { margin:6px 0 10px; height:6px; border-radius:3px; }
    .sc-pct--fw  { color:#327df4; }
    .sc-pct--op  { color:#00c752; }
    .sc-pct--prv { color:#ba68c8; }
    .sc-pct--cld { color:#29b6f6; }
    .sc-pct--ai  { color:#ff6b35; }
    .filter-row--mt { margin-top:8px; }
    .col-actions { text-align:right; }
    .col-right   { text-align:right; }
    .corpus-desc { font-size:0.8rem; margin-top:4px; }
    .project-bar { margin:8px 0 10px; }
    .phc-not-run { font-size:0.65rem; color:var(--mat-sys-on-surface-variant); font-style:italic; margin:4px 0 2px; }
    .phc-run-btn { font-size:0.7rem; height:26px; line-height:26px; padding:0 10px; margin-top:4px;
      .mat-icon { font-size:14px; height:14px; width:14px; margin-right:4px; } }
  `],
})
export class QaComponent {
  readonly Math = Math
  readonly methodLabels = METHOD_LABELS

  private qaApi = inject(QaApiService)
  private snackBar = inject(MatSnackBar)
  private qc = injectQueryClient()
  readonly theme = inject(ThemeService)

  // ── State ──────────────────────────────────────────────────────────────────
  activeTab    = signal(0)
  method       = signal<string>('existence')
  product      = signal<string>('all')
  statusFilter = signal<string>('all')
  projectsMethod = signal<string>('existence')

  runResult          = signal<string | null>(null)
  showAddSynonym     = signal(false)
  editingRule        = signal<SynonymRule | null>(null)
  corpusLoadResult   = signal<string | null>(null)
  runningProjectId   = signal<string | null>(null)
  expandedProjectId  = signal<string | null>(null)

  newKeyword      = ''
  newSynonymsText = ''
  newNotes        = ''
  editSynonymsText = ''
  editNotes        = ''

  // ── Queries ────────────────────────────────────────────────────────────────

  summaryQuery = injectQuery(() => ({
    queryKey: ['qa', 'summary', this.method(), this.product()] as const,
    queryFn: () => firstValueFrom(this.qaApi.getSummary(this.method(), this.product() !== 'all' ? this.product() : undefined)),
  }))

  resultsQuery = injectQuery(() => ({
    queryKey: ['qa', 'results', this.method(), this.product(), this.statusFilter()] as const,
    queryFn: () => firstValueFrom(this.qaApi.getResults({
      method:       this.method(),
      product_type: this.product() !== 'all' ? this.product() : undefined,
      status:       this.statusFilter() !== 'all' ? this.statusFilter() : undefined,
      limit: 200,
    })),
  }))

  synonymsQuery = injectQuery(() => ({
    queryKey: ['qa', 'synonyms'] as const,
    queryFn: () => firstValueFrom(this.qaApi.getSynonyms()),
    enabled: this.activeTab() === 1,
  }))

  corpusQuery = injectQuery(() => ({
    queryKey: ['qa', 'corpus-status'] as const,
    queryFn: () => firstValueFrom(this.qaApi.getReferenceCorpusStatus()),
    enabled: this.activeTab() === 2,
    refetchInterval: 30_000,
  }))

  orgProjectsQuery = injectQuery(() => ({
    queryKey: ['qa', 'org-projects', this.projectsMethod()] as const,
    queryFn: () => firstValueFrom(this.qaApi.getOrgProjectSummaries(this.projectsMethod())),
    enabled: this.activeTab() === 3,
  }))

  projectDetailQuery = injectQuery(() => ({
    queryKey: ['qa', 'project-detail', this.expandedProjectId(), this.projectsMethod()] as const,
    queryFn: () => firstValueFrom(this.qaApi.getProjectResults(this.expandedProjectId()!, {
      method: this.projectsMethod(), limit: 100,
    })),
    enabled: this.expandedProjectId() !== null && this.activeTab() === 3,
  }))

  projectDetailFails = computed(() =>
    (this.projectDetailQuery.data() ?? []).filter(r => r.qa_status !== 'pass').sort((a, b) => {
      const order: Record<string, number> = { fail: 0, needs_review: 1, warning: 2 }
      return (order[a.qa_status] ?? 9) - (order[b.qa_status] ?? 9)
    })
  )

  // ── Mutations ──────────────────────────────────────────────────────────────

  existenceMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.qaApi.runExistence()),
    onSuccess: (data) => {
      this.qc.invalidateQueries({ queryKey: ['qa'] })
      this.runResult.set(`Existence check complete in ${data.duration_ms}ms — ${data.pass_count} pass, ${data.fail_count} fail`)
    },
  }))

  keywordMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.qaApi.runKeyword()),
    onSuccess: (data) => {
      this.qc.invalidateQueries({ queryKey: ['qa'] })
      this.runResult.set(`Keyword check complete in ${data.duration_ms}ms — ${data.pass_count} pass, ${data.warning_count} warning, ${data.fail_count} fail`)
    },
  }))

  semanticMiniMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.qaApi.runSemanticMini()),
    onSuccess: (data) => {
      this.qc.invalidateQueries({ queryKey: ['qa'] })
      this.runResult.set(`Mini LLM check complete in ${data.duration_ms}ms — ${data.pass_count} pass, ${data.warning_count} warning, ${data.fail_count} fail`)
    },
  }))

  semanticClaudeMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.qaApi.runSemanticClaude()),
    onSuccess: (data) => {
      this.qc.invalidateQueries({ queryKey: ['qa'] })
      this.runResult.set(`Claude AI check complete in ${data.duration_ms}ms — ${data.pass_count} pass, ${data.warning_count} warning, ${data.fail_count} fail`)
    },
    onError: (e: Error) => {
      this.snackBar.open(e.message || 'Claude AI check failed.', 'Dismiss', { duration: 5000 })
    },
  }))

  projectExistenceMut = injectMutation(() => ({
    mutationFn: (projectId: string) => firstValueFrom(this.qaApi.runProjectExistence(projectId)),
    onSuccess: (data) => {
      this.runningProjectId.set(null)
      this.qc.invalidateQueries({ queryKey: ['qa'] })
      this.runResult.set(`Project QA complete in ${data.duration_ms}ms — ${data.pass_count} pass, ${data.fail_count} fail`)
    },
    onError: () => {
      this.runningProjectId.set(null)
      this.snackBar.open('Project QA run failed.', 'Dismiss', { duration: 4000 })
    },
  }))

  projectKeywordMut = injectMutation(() => ({
    mutationFn: (projectId: string) => firstValueFrom(this.qaApi.runProjectKeyword(projectId)),
    onSuccess: (data) => {
      this.runningProjectId.set(null)
      this.qc.invalidateQueries({ queryKey: ['qa'] })
      this.runResult.set(`Project keyword check complete in ${data.duration_ms}ms — ${data.pass_count} pass, ${data.warning_count} warning, ${data.fail_count} fail`)
    },
    onError: () => {
      this.runningProjectId.set(null)
      this.snackBar.open('Project keyword check failed.', 'Dismiss', { duration: 4000 })
    },
  }))

  projectSemanticMut = injectMutation(() => ({
    mutationFn: (projectId: string) => firstValueFrom(this.qaApi.runProjectSemantic(projectId)),
    onSuccess: (data) => {
      this.runningProjectId.set(null)
      this.qc.invalidateQueries({ queryKey: ['qa'] })
      this.runResult.set(`Project Mini LLM check complete in ${data.duration_ms}ms — ${data.pass_count} pass, ${data.warning_count} warning, ${data.fail_count} fail`)
    },
    onError: () => {
      this.runningProjectId.set(null)
      this.snackBar.open('Project Mini LLM check failed.', 'Dismiss', { duration: 4000 })
    },
  }))

  createSynonymMut = injectMutation(() => ({
    mutationFn: (body: { keyword: string; synonyms: string[]; notes?: string }) =>
      firstValueFrom(this.qaApi.createSynonym(body)),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['qa', 'synonyms'] })
      this.showAddSynonym.set(false)
      this.newKeyword = ''; this.newSynonymsText = ''; this.newNotes = ''
    },
  }))

  updateSynonymMut = injectMutation(() => ({
    mutationFn: ({ id, body }: { id: string; body: { synonyms: string[]; notes?: string } }) =>
      firstValueFrom(this.qaApi.updateSynonym(id, body)),
    onSuccess: () => {
      this.qc.invalidateQueries({ queryKey: ['qa', 'synonyms'] })
      this.editingRule.set(null)
    },
  }))

  deleteSynonymMut = injectMutation(() => ({
    mutationFn: (id: string) => firstValueFrom(this.qaApi.deleteSynonym(id)),
    onSuccess: () => this.qc.invalidateQueries({ queryKey: ['qa', 'synonyms'] }),
  }))

  reloadCorpusMut = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.qaApi.reloadReferenceCorpus()),
    onSuccess: (data) => {
      this.qc.invalidateQueries({ queryKey: ['qa', 'corpus-status'] })
      this.corpusLoadResult.set(
        `Loaded ${data.loaded_files} files — ${data.total_chunks.toLocaleString()} chunks in ${(data.duration_ms / 1000).toFixed(1)}s.` +
        (data.failed_files > 0 ? ` (${data.failed_files} failed)` : '')
      )
    },
  }))

  // ── Computed ───────────────────────────────────────────────────────────────

  isRunning = computed(() =>
    this.existenceMut.isPending() || this.keywordMut.isPending() ||
    this.semanticMiniMut.isPending() || this.semanticClaudeMut.isPending() ||
    this.projectExistenceMut.isPending() || this.projectKeywordMut.isPending() ||
    this.projectSemanticMut.isPending()
  )

  summary = computed(() => this.summaryQuery.data() ?? null)
  results = computed(() => this.resultsQuery.data() ?? [])

  overallPct = computed(() => {
    const s = this.summary()
    if (!s) return 0
    const total = s.framework.total + s.operational.total + s.privacy.total + s.cloud.total + s.ai.total
    if (!total) return 0
    const passing = s.framework.pass_count + s.operational.pass_count + s.privacy.pass_count + s.cloud.pass_count + s.ai.pass_count
    return Math.round(passing / total * 100)
  })

  overallColor = computed(() => {
    const p = this.overallPct()
    if (this.theme.isDark()) return p >= 80 ? '#C6EFCE' : p >= 50 ? '#FFEB9C' : '#FFC7CE'
    return p >= 80 ? '#1b5e20' : p >= 50 ? '#7a4800' : '#9e0000'
  })

  totalPassing = computed(() => {
    const s = this.summary()
    if (!s) return 0
    return s.framework.pass_count + s.operational.pass_count + s.privacy.pass_count + s.cloud.pass_count + s.ai.pass_count
  })

  totalChecks = computed(() => {
    const s = this.summary()
    if (!s) return 0
    return s.framework.total + s.operational.total + s.privacy.total + s.cloud.total + s.ai.total
  })

  showFw  = computed(() => this.product() === 'all' || this.product() === 'framework' || this.product() === 'isms')
  showOp  = computed(() => this.method() === 'existence' && (this.product() === 'all' || this.product() === 'operational'))
  showPrv = computed(() => this.product() === 'all' || this.product() === 'privacy')
  showCld = computed(() => this.product() === 'all' || this.product() === 'cloud')
  showAi  = computed(() => this.product() === 'all' || this.product() === 'ai')

  currentSubtitle = computed(() => {
    if (this.activeTab() === 1) return 'Manage the synonym dictionary used by keyword correlation'
    if (this.activeTab() === 2) return 'ISO & regulatory normative corpus'
    if (this.activeTab() === 3) return 'Per-project QA health'
    return METHOD_SUBTITLES[this.method()] ?? ''
  })

  avgPassRate = computed(() => {
    const ps = this.orgProjectsQuery.data()
    if (!ps?.length) return 0
    return Math.round(ps.reduce((s, p) => s + p.pass_rate, 0) / ps.length * 100)
  })

  displayedCols = computed(() => {
    const isSemantic = this.method() === 'semantic' || this.method() === 'semantic_claude'
    return isSemantic
      ? ['control_group', 'status', 'strength', 'details', 'missing', 'run']
      : ['control_group', 'product', 'status', 'strength', 'details', 'missing', 'run']
  })

  synonymCols = ['keyword', 'synonyms', 'notes', 'actions']

  // ── Methods ────────────────────────────────────────────────────────────────

  onMethodChange(v: string) {
    this.method.set(v)
    this.product.set('all')
    this.statusFilter.set('all')
  }

  runCheck(type: 'existence' | 'keyword' | 'semantic' | 'semantic_claude') {
    this.runResult.set(null)
    this.method.set(type)
    if (type === 'existence')       this.existenceMut.mutate(undefined)
    else if (type === 'keyword')    this.keywordMut.mutate(undefined)
    else if (type === 'semantic')   this.semanticMiniMut.mutate(undefined)
    else                            this.semanticClaudeMut.mutate(undefined)
  }

  toggleProjectDetail(projectId: string) {
    this.expandedProjectId.set(this.expandedProjectId() === projectId ? null : projectId)
  }

  runProjectCheck(projectId: string) {
    this.runResult.set(null)
    this.runningProjectId.set(projectId)
    const m = this.projectsMethod()
    if (m === 'keyword')        this.projectKeywordMut.mutate(projectId)
    else if (m === 'semantic')  this.projectSemanticMut.mutate(projectId)
    else                        this.projectExistenceMut.mutate(projectId)
  }

  statusBg(s: string): string {
    if (!this.theme.isDark()) {
      const LIGHT: Record<string, string> = {
        pass: 'rgba(46,125,50,0.12)', warning: 'rgba(230,145,0,0.15)', fail: 'rgba(192,0,0,0.12)', needs_review: 'rgba(0,0,0,0.06)',
      }
      return LIGHT[s] ?? LIGHT['needs_review']
    }
    return STATUS_BG[s] ?? STATUS_BG['needs_review']
  }
  statusFg(s: string): string {
    if (!this.theme.isDark()) {
      const LIGHT: Record<string, string> = {
        pass: '#1b5e20', warning: '#7a4800', fail: '#9e0000', needs_review: '#424242',
      }
      return LIGHT[s] ?? LIGHT['needs_review']
    }
    return STATUS_FG[s] ?? STATUS_FG['needs_review']
  }

  getPresent(row: CorrelationResultRead): string[] {
    if (this.method() === 'semantic_claude') return []
    if (this.method() === 'semantic') return []
    return row.coverage_keywords ?? []
  }

  getMissing(row: CorrelationResultRead): string[] {
    if (this.method() === 'semantic') return []
    if (this.method() === 'semantic_claude') return (row.metadata?.['gaps'] as string[] | undefined) ?? []
    return row.missing_keywords ?? []
  }

  projectColor(passRate: number): string {
    const p = Math.round(passRate * 100)
    return this.theme.isDark()
      ? (p >= 80 ? '#C6EFCE' : p >= 50 ? '#FFEB9C' : '#FFC7CE')
      : (p >= 80 ? '#1b5e20' : p >= 50 ? '#7a4800' : '#9e0000')
  }

  openAddSynonymDialog() {
    this.editingRule.set(null)
    this.showAddSynonym.set(true)
  }

  openEditSynonymDialog(rule: SynonymRule) {
    this.showAddSynonym.set(false)
    this.editSynonymsText = rule.synonyms.join(', ')
    this.editNotes = rule.notes ?? ''
    this.editingRule.set(rule)
  }

  deleteSynonym(id: string) {
    if (confirm('Delete this synonym rule?')) this.deleteSynonymMut.mutate(id)
  }

  submitNewSynonym() {
    const synonyms = this.newSynonymsText.split(',').map(s => s.trim().toLowerCase()).filter(Boolean)
    this.createSynonymMut.mutate({
      keyword: this.newKeyword.trim().toLowerCase(),
      synonyms,
      notes: this.newNotes.trim() || undefined,
    })
  }

  submitEditSynonym() {
    const rule = this.editingRule()
    if (!rule) return
    const synonyms = this.editSynonymsText.split(',').map(s => s.trim().toLowerCase()).filter(Boolean)
    this.updateSynonymMut.mutate({
      id: rule.id,
      body: { synonyms, notes: this.editNotes.trim() || undefined },
    })
  }

  reloadCorpus() {
    this.corpusLoadResult.set(null)
    this.reloadCorpusMut.mutate(undefined)
  }

  fmtDate = fmtDate
  fromNow = fromNow
}
