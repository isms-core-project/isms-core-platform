import { Component, inject, signal, computed } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { Router, RouterLink } from '@angular/router'
import { firstValueFrom } from 'rxjs'

import { injectQuery, injectMutation, injectQueryClient } from '@tanstack/angular-query-experimental'

import { MatCardModule } from '@angular/material/card'
import { MatButtonModule } from '@angular/material/button'
import { MatIconModule } from '@angular/material/icon'
import { MatChipsModule } from '@angular/material/chips'
import { MatProgressBarModule } from '@angular/material/progress-bar'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatTableModule } from '@angular/material/table'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatDialogModule, MatDialog } from '@angular/material/dialog'
import { MatSnackBar, MatSnackBarModule } from '@angular/material/snack-bar'

import {
  NistApiService,
  NistProfileSummary,
  NistFullProfile,
  NistRating,
  NistRatingUpsert,
  NistImportResult,
} from '../../api/nist-api.service'
import { ThemeService } from '../../core/services/theme.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'

// ── Constants ─────────────────────────────────────────────────────────────────

const FUNCTION_COLORS_DARK: Record<string, string> = {
  GV: '#4472C4', ID: '#ED7D31', PR: '#70AD47',
  DE: '#FFC000', RS: '#FF5252', RC: '#9966CC',
}
const FUNCTION_COLORS_LIGHT: Record<string, string> = {
  GV: '#2E5099', ID: '#c05800', PR: '#375623',
  DE: '#9a6500', RS: '#c62828', RC: '#6a3aaa',
}
const FUNCTION_NAMES: Record<string, string> = {
  GV: 'Govern', ID: 'Identify', PR: 'Protect',
  DE: 'Detect', RS: 'Respond', RC: 'Recover',
}
const TIER_LABELS: Record<number, string> = {
  1: 'Partial', 2: 'Risk Informed', 3: 'Repeatable', 4: 'Adaptive',
}
const FUNCTION_ORDER = ['GV', 'ID', 'PR', 'DE', 'RS', 'RC']

function tierColor(tier: number | null, dark: boolean): string {
  if (!tier) return dark ? 'rgba(255,255,255,0.1)' : 'rgba(0,0,0,0.12)'
  if (!dark) {
    if (tier === 1) return '#c62828'
    if (tier === 2) return '#9a6500'
    if (tier === 3) return '#375623'
    return '#2E5099'
  }
  if (tier === 1) return '#FF5252'
  if (tier === 2) return '#FFC000'
  if (tier === 3) return '#70AD47'
  return '#5c6bc0'
}

function gapColor(gap: number, isLight: boolean): string {
  if (gap <= 0) return isLight ? '#1b5e20' : '#C6EFCE'
  if (gap === 1) return isLight ? '#9a6500' : '#FFC000'
  return isLight ? '#c62828' : '#FF5252'
}

function pct(rated: number, total: number): number {
  return total > 0 ? Math.min(100, (rated / total) * 100) : 0
}

// ── Component ─────────────────────────────────────────────────────────────────

@Component({
  selector: 'app-nist-csf',
  standalone: true,
  imports: [
    FormsModule, RouterLink,
    MatCardModule, MatButtonModule, MatIconModule, MatChipsModule,
    MatProgressBarModule, MatProgressSpinnerModule, MatTooltipModule,
    MatTableModule, MatFormFieldModule, MatInputModule, MatSelectModule,
    MatDialogModule, MatSnackBarModule,
  ],
  template: `
<div class="page-wrap">
  <!-- Header -->
  <div class="nist-header">
    <div class="nist-header__left">
      <div class="nist-header__title-row">
        <h1 class="nist-header__title">NIST CSF 2.0</h1>
        <span class="nist-header__badge">NIST CSF v2.0</span>
      </div>
      <p class="nist-header__sub">Cybersecurity Framework assessments — 106 subcategories, Tier 1–4, ISO 27001 crosswalk</p>
    </div>
    @if (!selectedProfileId()) {
      <button mat-flat-button color="primary" (click)="openCreate()">
        <mat-icon>add</mat-icon> New Assessment
      </button>
    }
  </div>

  <!-- ── Detail view ── -->
  @if (selectedProfileId()) {
    @let fd = fullProfile.data();
    <div class="detail-header">
      <button mat-icon-button (click)="selectedProfileId.set(null)" matTooltip="Back to profiles">
        <mat-icon>arrow_back</mat-icon>
      </button>
      <div class="detail-title-wrap">
        @if (editingName()) {
          <div class="edit-name-row">
            <mat-form-field appearance="outline" class="edit-name-field" subscriptSizing="dynamic">
              <input matInput [(ngModel)]="nameVal" (keydown.enter)="saveName()" (keydown.escape)="editingName.set(false)">
            </mat-form-field>
            <button mat-icon-button (click)="saveName()"><mat-icon>save</mat-icon></button>
          </div>
        } @else {
          <div class="profile-name-row">
            <span class="profile-name">{{ fd?.profile?.name }}</span>
            <button mat-icon-button (click)="startEditName()" matTooltip="Rename" class="edit-name-btn">
              <mat-icon class="icon-sm">edit</mat-icon>
            </button>
          </div>
        }
        <span class="profile-meta">
          NIST CSF 2.0{{ fd?.profile?.assessor ? ' · ' + fd?.profile?.assessor : '' }}{{ fd?.profile?.scope ? ' · ' + fd?.profile?.scope : '' }}
        </span>
      </div>
      <div class="detail-actions">
        @if (upsertPending()) {
          <mat-spinner diameter="14"></mat-spinner>
        }
        <mat-chip class="rated-chip">
          {{ ratedCount() }}/106
        </mat-chip>
        <input #importInput type="file" accept=".xlsx" class="hidden-input" (change)="onImportFile($event)">
        <button mat-icon-button (click)="importInput.click()" matTooltip="Import NIST XLSX" class="btn-import">
          <mat-icon class="icon-md">upload_file</mat-icon>
        </button>
        <button mat-icon-button (click)="exportXlsx()" matTooltip="Export XLSX" class="btn-export-xlsx">
          <mat-icon class="icon-md">download</mat-icon>
        </button>
        <button mat-icon-button (click)="exportCsv()" matTooltip="Export CSV" class="btn-export-csv">
          <mat-icon class="icon-sm">file_download</mat-icon>
        </button>
        <button mat-icon-button [routerLink]="['/nist-csf', selectedProfileId(), 'report']" matTooltip="View report"
          class="btn-report">
          <mat-icon class="icon-md">summarize</mat-icon>
        </button>
        <button mat-icon-button (click)="confirmDelete()" color="warn" matTooltip="Delete" class="btn-delete-detail">
          <mat-icon class="icon-md">delete</mat-icon>
        </button>
      </div>
    </div>

    @if (fullProfile.isLoading()) {
      <div class="spinner-center"><mat-spinner></mat-spinner></div>
    }
    @if (fullProfile.isError()) {
      <div class="error-msg">Failed to load profile.</div>
    }

    @if (fd) {
      <div class="autosave-hint">Changes auto-save after 1.2 s.</div>

      @for (fc of functionOrder; track fc) {
        @let ratings = byFunction()[fc] ?? [];
        @if (ratings.length > 0) {
          <mat-card class="fn-card"
            [style.border-color]="fcColor(fc) + '22'"
            [style.background]="fcColor(fc) + '05'">
            <!-- Function header -->
            <div (click)="toggleFn(fc)" class="fn-header"
              [style.border-bottom-color]="fcColor(fc) + '22'">
              <div class="fn-icon-box"
                [style.background]="fcColor(fc) + '22'">
                <span class="fn-code" [style.color]="fcColor(fc)">{{ fc }}</span>
              </div>
              <div class="fn-info">
                <div class="fn-name" [style.color]="fcColor(fc)">{{ fnName(fc) }}</div>
                <div class="fn-rated-label">{{ ratedInFn(fc) }} of {{ ratings.length }} rated</div>
              </div>
              <mat-progress-bar mode="determinate" [value]="fnPct(fc)"
                class="fn-progress" [style.--mat-progress-bar-active-indicator-color]="fcColor(fc)">
              </mat-progress-bar>
              <mat-icon class="icon-md fn-toggle-icon">{{ openFunctions()[fc] ? 'expand_less' : 'expand_more' }}</mat-icon>
            </div>

            <!-- Ratings table -->
            @if (openFunctions()[fc]) {
              <div class="table-scroll">
                <table class="ratings-table">
                  <thead>
                    <tr class="table-header-row">
                      <th class="th-base th-id">ID</th>
                      <th class="th-base">Title</th>
                      <th class="th-base th-tier">Current Tier</th>
                      <th class="th-base th-tier">Target Tier</th>
                      <th class="th-base th-gap">Gap</th>
                      <th class="th-base th-notes">Notes</th>
                      <th class="th-base th-iso">ISO 27001</th>
                    </tr>
                  </thead>
                  <tbody>
                    @for (r of ratings; track r.subcategory_id) {
                      @let ov = overrides()[r.subcategory_id];
                      @let cur = (ov && 'current_tier' in ov) ? ov['current_tier'] : r.current_tier;
                      @let tgt = (ov && 'target_tier' in ov) ? ov['target_tier'] : r.target_tier;
                      @let gap = (cur != null && tgt != null) ? +tgt - +cur : null;
                      <tr class="table-data-row">
                        <td class="td-base">
                          <span class="subcat-code" [style.color]="fcColor(fc)">{{ r.subcategory_code }}</span>
                        </td>
                        <td class="td-base">
                          <span class="subcat-title">{{ r.subcategory_title }}</span>
                        </td>
                        <td class="td-base">
                          <select [value]="cur ?? 0" (change)="onTierChange(r.subcategory_id, 'current_tier', $event)"
                            class="tier-select">
                            <option value="0">Not Rated</option>
                            @for (t of [1,2,3,4]; track t) {
                              <option [value]="t">T{{ t }} — {{ tierLabel(t) }}</option>
                            }
                          </select>
                        </td>
                        <td class="td-base">
                          <select [value]="tgt ?? 0" (change)="onTierChange(r.subcategory_id, 'target_tier', $event)"
                            class="tier-select">
                            <option value="0">Not Rated</option>
                            @for (t of [1,2,3,4]; track t) {
                              <option [value]="t">T{{ t }} — {{ tierLabel(t) }}</option>
                            }
                          </select>
                        </td>
                        <td class="td-base td-gap-center">
                          @if (gap != null) {
                            <span class="gap-badge"
                              [style.background]="gapColor(gap) + '22'"
                              [style.color]="gapColor(gap)">
                              {{ gap > 0 ? '+' + gap : gap === 0 ? '✓' : gap }}
                            </span>
                          } @else {
                            <span class="gap-empty">—</span>
                          }
                        </td>
                        <td class="td-base">
                          <input type="text" [value]="(ov && ov['notes'] !== undefined ? ov['notes'] : r.notes) ?? ''"
                            (blur)="onNoteBlur(r, $event)"
                            placeholder="Notes…"
                            class="notes-input">
                        </td>
                        <td class="td-base">
                          <div class="iso-tags">
                            @for (iso of r.iso_mappings.slice(0,3); track iso) {
                              <span class="iso-tag">{{ iso }}</span>
                            }
                            @if (r.iso_mappings.length > 3) {
                              <span class="iso-more">+{{ r.iso_mappings.length - 3 }}</span>
                            }
                          </div>
                        </td>
                      </tr>
                    }
                  </tbody>
                </table>
              </div>
            }
          </mat-card>
        }
      }
    }
  }

  <!-- ── List view ── -->
  @if (!selectedProfileId()) {
    <!-- Function legend -->
    <div class="legend-row">
      @for (fc of functionOrder; track fc) {
        <span class="legend-chip" [style.background]="fcColorVal(fc) + '22'" [style.color]="fcColorVal(fc)" [style.border-color]="fcColorVal(fc) + '50'">
          {{ fc }} — {{ fnName(fc) }}
        </span>
      }
    </div>
    <!-- Tier legend -->
    <div class="legend-row legend-tier">
      @for (t of [1,2,3,4]; track t) {
        <span class="legend-chip" [style.background]="tierColorVal(t) + '22'" [style.color]="tierColorVal(t)" [style.border-color]="tierColorVal(t) + '50'">
          T{{ t }} — {{ tierLabel(t) }}
        </span>
      }
    </div>

    @if (profilesQuery.isLoading()) {
      @for (i of [1,2]; track i) {
        <div class="skeleton-card"></div>
      }
    }

    @if (!profilesQuery.isLoading() && (profilesQuery.data()?.length ?? 0) === 0) {
      <div class="empty-state">
        <p class="empty-title">No assessments yet</p>
        <p class="empty-text">Create your first NIST CSF 2.0 assessment to get started.</p>
        <button mat-stroked-button (click)="openCreate()">
          <mat-icon>add</mat-icon> New Assessment
        </button>
      </div>
    }

    @for (p of profilesQuery.data() ?? []; track p.id) {
      <mat-card class="profile-card" (click)="openProfile(p.id)">
        <mat-card-content class="profile-card-content">
          <div class="profile-row">
            <!-- Ring -->
            <div class="ring-wrap">
              <mat-spinner mode="determinate" [value]="100" diameter="52" strokeWidth="3" class="ring-bg"></mat-spinner>
              <mat-spinner mode="determinate" [value]="profilePct(p)" diameter="52" strokeWidth="3" class="ring-fg"></mat-spinner>
              <div class="ring-label">
                <div class="ring-count">{{ p.rated_count }}</div>
                <div class="ring-total">/{{ p.total_subcategories }}</div>
              </div>
            </div>
            <!-- Info -->
            <div class="profile-info">
              <div class="profile-name-row">
                <span class="profile-title">{{ p.name }}</span>
                <span class="status-badge"
                  [style.background]="statusBg(p)"
                  [style.color]="statusFg(p)">
                  {{ statusLabel(p) }}
                </span>
              </div>
              @if (p.description) {
                <div class="profile-description">{{ p.description }}</div>
              }
              <div class="profile-meta-row">
                @if (p.assessor) {
                  <span class="meta-item">Assessor: <span class="meta-value">{{ p.assessor }}</span></span>
                }
                @if (p.avg_current_tier != null) {
                  <span class="meta-item">Avg: <span [style.color]="tierColorVal(Math.round(p.avg_current_tier))">T{{ p.avg_current_tier.toFixed(1) }}</span></span>
                }
              </div>
              @if ((p.function_scores?.length ?? 0) > 0) {
                <div class="fn-scores-grid">
                  @for (fc of functionOrder; track fc) {
                    @let fs = getFunctionScore(p, fc);
                    @if (fs) {
                      <div>
                        <div class="fn-score-header">
                          <span class="fn-score-code" [style.color]="fcColorVal(fc)">{{ fc }}</span>
                          <span class="fn-score-meta">{{ fs.avg_current != null ? 'T' + fs.avg_current.toFixed(1) : '—' }} {{ fs.rated_count }}/{{ fs.total_count }}</span>
                        </div>
                        <mat-progress-bar mode="determinate" [value]="pct(fs.rated_count, fs.total_count)"
                          class="fn-score-bar" [style.--mat-progress-bar-active-indicator-color]="fcColorVal(fc)">
                        </mat-progress-bar>
                      </div>
                    }
                  }
                </div>
              }
            </div>
            <!-- Delete -->
            <div (click)="$event.stopPropagation()">
              <button mat-icon-button color="warn" (click)="deleteProfile(p)" matTooltip="Delete profile" class="btn-delete-list">
                <mat-icon class="icon-md">delete</mat-icon>
              </button>
            </div>
          </div>
        </mat-card-content>
      </mat-card>
    }
  }

  <!-- Create dialog -->
  @if (createOpen()) {
    <div class="dialog-overlay" (click)="createOpen.set(false)">
      <mat-card class="dialog-card dialog-card-create" (click)="$event.stopPropagation()">
        <mat-card-content class="dialog-content">
          <h3 class="dialog-title">New NIST CSF 2.0 Assessment</h3>
          <div class="dialog-form">
            <mat-form-field appearance="outline" class="form-field-full" subscriptSizing="dynamic">
              <mat-label>Profile Name</mat-label>
              <input matInput [(ngModel)]="newName" required autofocus>
            </mat-form-field>
            <mat-form-field appearance="outline" class="form-field-full" subscriptSizing="dynamic">
              <mat-label>Description</mat-label>
              <textarea matInput [(ngModel)]="newDescription" rows="2"></textarea>
            </mat-form-field>
            <mat-form-field appearance="outline" class="form-field-full" subscriptSizing="dynamic">
              <mat-label>Assessor</mat-label>
              <input matInput [(ngModel)]="newAssessor">
            </mat-form-field>
            <mat-form-field appearance="outline" class="form-field-full" subscriptSizing="dynamic">
              <mat-label>Scope</mat-label>
              <input matInput [(ngModel)]="newScope">
            </mat-form-field>
            @if (createMutation.isError()) {
              <div class="form-error">Failed to create profile.</div>
            }
          </div>
          <div class="dialog-actions">
            <button mat-button (click)="createOpen.set(false)">Cancel</button>
            <button mat-flat-button color="primary" [disabled]="!newName.trim() || createMutation.isPending()"
              (click)="submitCreate()">
              {{ createMutation.isPending() ? 'Creating…' : 'Create' }}
            </button>
          </div>
        </mat-card-content>
      </mat-card>
    </div>
  }

  <!-- Delete confirm dialog -->
  @if (deleteTarget()) {
    <div class="dialog-overlay" (click)="deleteTarget.set(null)">
      <mat-card class="dialog-card dialog-card-delete" (click)="$event.stopPropagation()">
        <mat-card-content class="dialog-content">
          <h3 class="dialog-title dialog-title-sm">Delete NIST CSF Profile?</h3>
          <p class="dialog-body"><strong>{{ deleteTarget()!.name }}</strong> and all its ratings will be permanently removed.</p>
          @if (deleteMutation.isError()) {
            <div class="form-error form-error-mb">Delete failed.</div>
          }
          <div class="dialog-actions">
            <button mat-button (click)="deleteTarget.set(null)">Cancel</button>
            <button mat-flat-button color="warn" [disabled]="deleteMutation.isPending()" (click)="submitDelete()">
              <mat-icon>delete</mat-icon> {{ deleteMutation.isPending() ? 'Deleting…' : 'Delete' }}
            </button>
          </div>
        </mat-card-content>
      </mat-card>
    </div>
  }
</div>
`,
  styles: [`
    :host { display: block; }
    @keyframes pulse { 0%,100% { opacity:.5 } 50% { opacity:1 } }

    .legend-chip {
      display: inline-flex; align-items: center; height: 22px;
      padding: 0 8px; border-radius: 11px; font-size: 0.65rem; font-weight: 600;
      border: 1px solid; cursor: default; white-space: nowrap;
    }

    /* Page wrapper */
    .page-wrap { padding: 0 4px; }

    /* Header */
    .nist-header { display:flex; align-items:flex-start; justify-content:space-between; gap:16px; margin-top:16px; margin-bottom:20px; flex-wrap:wrap; }
    .nist-header__left { flex:1; }
    .nist-header__title-row { display:flex; align-items:center; gap:10px; flex-wrap:wrap; }
    .nist-header__title { margin:0; font-size:1.75rem; font-weight:700; line-height:1.2; }
    .nist-header__badge { font-size:.72rem; font-weight:600; padding:2px 10px; border-radius:10px; background:rgba(92,107,192,.22); color:#5c6bc0; }
    .nist-header__sub { margin:4px 0 0; font-size:.875rem; color:var(--mat-sys-on-surface-variant); }
    html[data-theme='light'] .nist-header__badge { background:rgba(92,107,192,.15); color:#3949AB; }

    /* Detail header */
    .detail-header {
      display: flex; align-items: center; gap: 8px;
      margin-bottom: 24px; flex-wrap: wrap;
    }
    .detail-title-wrap { flex: 1; min-width: 0; }
    .edit-name-row { display: flex; align-items: center; gap: 8px; }
    .edit-name-field { flex: 1; }
    .profile-name-row { display: flex; align-items: center; gap: 6px; }
    .profile-name { font-size: 1.1rem; font-weight: 700; }
    .edit-name-btn { opacity: .4; }
    .profile-meta { font-size: 0.72rem; opacity: .6; }
    .detail-actions { display: flex; gap: 6px; align-items: center; }

    /* Rated chip */
    .rated-chip { font-size: .65rem; height: 20px; background: rgba(92,107,192,.12); color: #9FA8DA; }

    /* Hidden file input */
    .hidden-input { display: none; }

    /* Action buttons */
    .btn-import    { color: #5c6bc0; background: rgba(92,107,192,.1); }
    .btn-export-xlsx { color: #70AD47; background: rgba(112,173,71,.1); }
    .btn-export-csv  { color: #8B9CC8; background: rgba(139,156,200,.08); }
    .btn-report    { color: #FFC000; background: rgba(255,192,0,.1); }
    .btn-delete-detail { opacity: .5; }

    /* Spinner / error */
    .spinner-center { display: flex; justify-content: center; padding: 40px; }
    .error-msg { color: #f44336; padding: 16px; }

    /* Autosave hint */
    .autosave-hint { font-size: .72rem; opacity: .5; margin-bottom: 16px; font-style: italic; }

    /* Function card */
    .fn-card { margin-bottom: 12px; border-width: 1px; border-style: solid; }
    .fn-header {
      display: flex; align-items: center; gap: 12px;
      padding: 10px 16px; cursor: pointer;
      border-bottom-width: 1px; border-bottom-style: solid;
    }
    .fn-icon-box {
      width: 28px; height: 28px; border-radius: 4px;
      display: flex; align-items: center; justify-content: center; flex-shrink: 0;
    }
    .fn-code { font-size: .7rem; font-weight: 800; line-height: 1; }
    .fn-info { flex: 1; }
    .fn-name { font-size: .82rem; font-weight: 700; }
    .fn-rated-label { font-size: .62rem; opacity: .5; }
    .fn-progress { width: 80px; }
    .fn-toggle-icon { opacity: .4; }

    /* Ratings table */
    .table-scroll { overflow-x: auto; }
    .ratings-table { width: 100%; border-collapse: collapse; font-size: .72rem; }
    .table-header-row { border-bottom: 1px solid rgba(255,255,255,.06); }
    .th-base { padding: 6px 8px; text-align: left; font-size: .65rem; opacity: .5; }
    .th-id    { width: 100px; }
    .th-tier  { width: 145px; }
    .th-gap   { width: 50px; text-align: center; }
    .th-notes { width: 160px; }
    .th-iso   { width: 90px; }
    .table-data-row { border-bottom: 1px solid rgba(255,255,255,.04); }
    .td-base { padding: 5px 8px; }
    .td-gap-center { text-align: center; }
    .subcat-code { font-family: monospace; font-size: .68rem; font-weight: 600; }
    .subcat-title { font-size: .72rem; line-height: 1.35; }
    .tier-select {
      font-size: .72rem; height: 26px; min-width: 130px;
      background: transparent; border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 4px; color: inherit; padding: 0 6px;
    }
    .gap-badge {
      font-size: .6rem; font-weight: 700;
      padding: 1px 4px; border-radius: 8px;
    }
    .gap-empty { opacity: .3; }
    .notes-input {
      width: 100%; font-size: .68rem; background: transparent;
      border: none; border-bottom: 1px solid var(--mat-sys-outline-variant);
      color: inherit; padding: 2px 0; outline: none;
    }
    .iso-tags { display: flex; flex-wrap: wrap; gap: 2px; }
    .iso-tag {
      font-size: .55rem; padding: 0 4px; height: 14px; border-radius: 7px;
      background: rgba(92,107,192,.15); color: #9FA8DA;
      display: inline-flex; align-items: center;
    }
    .iso-more { font-size: .55rem; opacity: .5; }

    /* Legend */
    .legend-row { display: flex; gap: 8px; margin-bottom: 12px; flex-wrap: wrap; }
    .legend-tier { margin-bottom: 24px; }

    /* Skeleton */
    .skeleton-card {
      height: 120px; border-radius: 8px;
      background: rgba(0,0,0,0.04);
      margin-bottom: 12px; animation: pulse 1.4s infinite;
    }

    /* Empty state */
    .empty-state { text-align: center; padding: 64px 0; }
    .empty-title { font-size: 1.1rem; color: var(--mat-sys-on-surface-variant); margin: 0 0 8px; font-weight: 600; }
    .empty-text { color: var(--mat-sys-on-surface-variant); margin: 0 0 24px; }

    /* Profile card */
    .profile-card {
      margin-bottom: 12px;
      background: var(--mat-sys-surface-container);
      border: 1px solid var(--mat-sys-outline-variant);
      cursor: pointer;
    }
    .profile-card-content { padding: 14px 16px; }
    .profile-row { display: flex; gap: 16px; }

    /* Ring spinner */
    .ring-wrap {
      position: relative; width: 52px; height: 52px;
      flex-shrink: 0; display: flex; align-items: center; justify-content: center;
    }
    .ring-bg { position: absolute; }
    .ring-fg { position: absolute; }
    .ring-label { text-align: center; }
    .ring-count { font-size: .7rem; font-weight: 700; line-height: 1; color: var(--mat-sys-on-surface); }
    .ring-total { font-size: .52rem; opacity: .5; line-height: 1; color: var(--mat-sys-on-surface-variant); }

    /* Profile info */
    .profile-info { flex: 1; min-width: 0; }
    .profile-name-row {
      display: flex; align-items: center; gap: 8px;
      margin-bottom: 4px; flex-wrap: wrap;
    }
    .profile-title {
      font-weight: 700; font-size: .85rem; flex: 1; min-width: 0;
      overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
    }
    .status-badge {
      font-size: .6rem; font-weight: 600; padding: 0 6px; height: 16px;
      border-radius: 8px; display: inline-flex; align-items: center;
    }
    .profile-description {
      font-size: .72rem; opacity: .5; margin-bottom: 6px;
      overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
    }
    .profile-meta-row { display: flex; gap: 16px; flex-wrap: wrap; }
    .meta-item { font-size: .65rem; opacity: .4; }
    .meta-value { opacity: 1; }

    /* Function scores mini grid */
    .fn-scores-grid {
      display: grid; grid-template-columns: repeat(3,1fr);
      gap: 4px 12px; margin-top: 8px;
    }
    .fn-score-header { display: flex; justify-content: space-between; margin-bottom: 2px; }
    .fn-score-code { font-size: .65rem; font-weight: 600; }
    .fn-score-meta { font-size: .6rem; opacity: .4; }
    .fn-score-bar { height: 3px; }

    /* Delete list button */
    .btn-delete-list { opacity: .4; }

    /* Dialog overlay */
    .dialog-overlay {
      position: fixed; inset: 0; background: rgba(0,0,0,.6);
      z-index: 1000; display: flex; align-items: center; justify-content: center;
    }
    .dialog-card { max-width: 90vw; }
    .dialog-card-create { width: 400px; }
    .dialog-card-delete { width: 360px; }
    .dialog-content { padding: 20px; }
    .dialog-title { margin: 0 0 16px; }
    .dialog-title-sm { margin: 0 0 12px; }
    .dialog-body { font-size: .85rem; margin: 0 0 12px; }
    .dialog-form { display: flex; flex-direction: column; gap: 12px; }
    .form-field-full { width: 100%; }
    .form-error { color: #f44336; font-size: .82rem; }
    .form-error-mb { margin-bottom: 8px; }
    .dialog-actions { display: flex; justify-content: flex-end; gap: 8px; margin-top: 16px; }
  `],
})
export class NistCsfComponent {
  private nist        = inject(NistApiService)
  private queryClient = injectQueryClient()
  private snack       = inject(MatSnackBar)
  readonly theme      = inject(ThemeService)

  // ── State ──────────────────────────────────────────────────────────────────
  selectedProfileId = signal<string | null>(null)
  createOpen        = signal(false)
  deleteTarget      = signal<{ id: string; name: string } | null>(null)
  editingName       = signal(false)
  nameVal           = ''
  newName           = ''
  newDescription    = ''
  newAssessor       = ''
  newScope          = ''
  openFunctions     = signal<Record<string, boolean>>({
    GV: true, ID: true, PR: true, DE: true, RS: true, RC: true,
  })
  overrides         = signal<Record<string, Record<string, number | null | string>>>({})
  private saveTimer: ReturnType<typeof setTimeout> | null = null

  readonly functionOrder = FUNCTION_ORDER
  readonly Math = Math

  // ── Queries ────────────────────────────────────────────────────────────────
  profilesQuery = injectQuery(() => ({
    queryKey: ['nist-profiles'],
    queryFn: () => firstValueFrom(this.nist.listProfiles()),
  }))

  fullProfile = injectQuery(() => ({
    queryKey: ['nist-full-profile', this.selectedProfileId()],
    queryFn: () => firstValueFrom(this.nist.getFullProfile(this.selectedProfileId()!)),
    enabled: !!this.selectedProfileId(),
  }))

  // ── Mutations ──────────────────────────────────────────────────────────────
  createMutation = injectMutation(() => ({
    mutationFn: (data: { name: string; description?: string; assessor?: string; scope?: string }) =>
      firstValueFrom(this.nist.createProfile(data)),
    onSuccess: (created) => {
      this.queryClient.invalidateQueries({ queryKey: ['nist-profiles'] })
      this.createOpen.set(false)
      this.newName = ''; this.newDescription = ''; this.newAssessor = ''; this.newScope = ''
      this.selectedProfileId.set(created.id)
    },
  }))

  deleteMutation = injectMutation(() => ({
    mutationFn: (id: string) => firstValueFrom(this.nist.deleteProfile(id)),
    onSuccess: () => {
      this.deleteTarget.set(null)
      this.selectedProfileId.set(null)
      this.queryClient.invalidateQueries({ queryKey: ['nist-profiles'] })
    },
  }))

  updateNameMutation = injectMutation(() => ({
    mutationFn: ({ id, name }: { id: string; name: string }) =>
      firstValueFrom(this.nist.updateProfile(id, { name })),
    onSuccess: () => {
      this.editingName.set(false)
      this.queryClient.invalidateQueries({ queryKey: ['nist-full-profile', this.selectedProfileId()] })
      this.queryClient.invalidateQueries({ queryKey: ['nist-profiles'] })
    },
  }))

  upsertMutation = injectMutation(() => ({
    mutationFn: (ratings: NistRatingUpsert[]) =>
      firstValueFrom(this.nist.upsertRatings(this.selectedProfileId()!, ratings)),
    onSuccess: () => {
      this.queryClient.invalidateQueries({ queryKey: ['nist-full-profile', this.selectedProfileId()] })
      this.queryClient.invalidateQueries({ queryKey: ['nist-profiles'] })
    },
  }))

  upsertPending = computed(() => this.upsertMutation.isPending())

  // ── Computed ───────────────────────────────────────────────────────────────
  byFunction = computed((): Record<string, NistRating[]> => {
    const data = this.fullProfile.data()
    if (!data) return {}
    const map: Record<string, NistRating[]> = {}
    for (const r of data.ratings) {
      if (!map[r.function_code]) map[r.function_code] = []
      map[r.function_code].push(r)
    }
    return map
  })

  ratedCount = computed((): number => {
    const data = this.fullProfile.data()
    if (!data) return 0
    return data.ratings.filter(r => {
      const ov = this.overrides()[r.subcategory_id]
      const cur = ov && 'current_tier' in ov ? ov['current_tier'] : r.current_tier
      return cur != null
    }).length
  })

  // ── Helpers ────────────────────────────────────────────────────────────────
  isDark = computed(() => this.theme.isDark())

  fcColor(fc: string): string {
    return this.isDark() ? (FUNCTION_COLORS_DARK[fc] ?? '#888') : (FUNCTION_COLORS_LIGHT[fc] ?? '#888')
  }
  fcColorVal(fc: string): string { return this.fcColor(fc) }
  fnName(fc: string): string { return FUNCTION_NAMES[fc] ?? fc }
  tierLabel(t: number): string { return TIER_LABELS[t] ?? '' }
  tierColorVal(t: number): string { return tierColor(t, this.isDark()) }
  pct = pct
  gapColor(gap: number): string { return gapColor(gap, !this.isDark()) }

  ratedInFn(fc: string): number {
    const ratings = this.byFunction()[fc] ?? []
    return ratings.filter(r => {
      const ov = this.overrides()[r.subcategory_id]
      const cur = ov && 'current_tier' in ov ? ov['current_tier'] : r.current_tier
      return cur != null
    }).length
  }

  fnPct(fc: string): number {
    const ratings = this.byFunction()[fc] ?? []
    return pct(this.ratedInFn(fc), ratings.length)
  }

  profilePct(p: NistProfileSummary): number {
    return pct(p.rated_count, p.total_subcategories)
  }

  statusLabel(p: NistProfileSummary): string {
    return p.status === 'complete' ? 'Complete' : p.status === 'in_progress' ? 'In Progress' : 'Draft'
  }
  statusBg(p: NistProfileSummary): string {
    const d = this.isDark()
    if (p.status === 'complete')    return d ? 'rgba(198,239,206,.12)' : 'rgba(46,125,50,.12)'
    if (p.status === 'in_progress') return d ? 'rgba(255,192,0,.1)'   : 'rgba(230,160,0,.12)'
    return d ? 'rgba(255,255,255,.05)' : 'rgba(0,0,0,.07)'
  }
  statusFg(p: NistProfileSummary): string {
    const d = this.isDark()
    if (p.status === 'complete')    return d ? '#C6EFCE' : '#1b5e20'
    if (p.status === 'in_progress') return d ? '#FFC000' : '#9a6500'
    return d ? '#888' : '#555'
  }

  getFunctionScore(p: NistProfileSummary, fc: string) {
    return p.function_scores?.find(f => f.function_code === fc) ?? null
  }

  toggleFn(fc: string): void {
    this.openFunctions.update(m => ({ ...m, [fc]: !m[fc] }))
  }

  // ── Actions ────────────────────────────────────────────────────────────────
  openCreate(): void { this.createOpen.set(true) }

  submitCreate(): void {
    if (!this.newName.trim()) return
    this.createMutation.mutate({
      name: this.newName.trim(),
      description: this.newDescription || undefined,
      assessor: this.newAssessor || undefined,
      scope: this.newScope || undefined,
    })
  }

  openProfile(id: string): void {
    this.overrides.set({})
    this.selectedProfileId.set(id)
  }

  deleteProfile(p: { id: string; name: string }): void {
    this.deleteTarget.set({ id: p.id, name: p.name })
  }

  submitDelete(): void {
    const t = this.deleteTarget()
    if (t) this.deleteMutation.mutate(t.id)
  }

  confirmDelete(): void {
    const data = this.fullProfile.data()
    if (data) this.deleteTarget.set({ id: data.profile.id, name: data.profile.name })
  }

  startEditName(): void {
    const data = this.fullProfile.data()
    if (data) { this.nameVal = data.profile.name; this.editingName.set(true) }
  }

  saveName(): void {
    const id = this.selectedProfileId()
    if (id && this.nameVal.trim()) this.updateNameMutation.mutate({ id, name: this.nameVal.trim() })
  }

  onTierChange(subcategoryId: string, field: 'current_tier' | 'target_tier', event: Event): void {
    const val = Number((event.target as HTMLSelectElement).value)
    const v = val === 0 ? null : val
    this.overrides.update(prev => ({
      ...prev,
      [subcategoryId]: { ...(prev[subcategoryId] ?? {}), [field]: v },
    }))
    this.scheduleSave()
  }

  onNoteBlur(r: NistRating, event: Event): void {
    const v = ((event.target as HTMLInputElement).value.trim()) || null
    const ov = this.overrides()[r.subcategory_id]
    const existing = ov && 'notes' in ov ? ov['notes'] : r.notes ?? null
    if (v !== existing) {
      this.overrides.update(prev => ({
        ...prev,
        [r.subcategory_id]: { ...(prev[r.subcategory_id] ?? {}), notes: v },
      }))
      this.scheduleSave()
    }
  }

  private scheduleSave(): void {
    if (this.saveTimer) clearTimeout(this.saveTimer)
    this.saveTimer = setTimeout(() => {
      const cur = this.overrides()
      const entries = Object.entries(cur)
      if (entries.length === 0) return
      const fd = this.fullProfile.data()
      const ratings: NistRatingUpsert[] = entries.map(([id, ov]) => {
        const orig = fd?.ratings.find(r => r.subcategory_id === id)
        return {
          subcategory_id: id,
          current_tier: 'current_tier' in ov ? ov['current_tier'] as number | null : (orig?.current_tier ?? null),
          target_tier:  'target_tier'  in ov ? ov['target_tier']  as number | null : (orig?.target_tier  ?? null),
          notes:        'notes'        in ov ? ov['notes']         as string | null : (orig?.notes        ?? null),
        }
      })
      this.overrides.set({})
      this.upsertMutation.mutate(ratings)
    }, 1200)
  }

  exportCsv(): void {
    const id = this.selectedProfileId()
    if (!id) return
    firstValueFrom(this.nist.exportCsv(id)).then(blob => {
      const url = URL.createObjectURL(blob)
      const a = document.createElement('a'); a.href = url; a.download = `NIST-CSF-Assessment-${id}.csv`; a.click()
      URL.revokeObjectURL(url)
    })
  }

  exportXlsx(): void {
    const id = this.selectedProfileId()
    if (!id) return
    firstValueFrom(this.nist.exportXlsx(id)).then(blob => {
      const url = URL.createObjectURL(blob)
      const a = document.createElement('a'); a.href = url; a.download = `NIST-CSF-Assessment-${id}.xlsx`; a.click()
      URL.revokeObjectURL(url)
    })
  }

  onImportFile(event: Event): void {
    const file = (event.target as HTMLInputElement).files?.[0]
    if (!file) return
    ;(event.target as HTMLInputElement).value = ''
    const id = this.selectedProfileId()
    if (!id) return
    firstValueFrom(this.nist.importXlsx(id, file)).then((result: NistImportResult) => {
      this.queryClient.invalidateQueries({ queryKey: ['nist-full-profile', id] })
      this.queryClient.invalidateQueries({ queryKey: ['nist-profiles'] })
      this.snack.open(`Imported ${result.imported} ratings. Skipped: ${result.skipped}.`, 'Close', { duration: 6000 })
    }).catch(() => {
      this.snack.open('Import failed — check the file is a NIST CSF 2.0 template (.xlsx).', 'Close', { duration: 6000 })
    })
  }
}
