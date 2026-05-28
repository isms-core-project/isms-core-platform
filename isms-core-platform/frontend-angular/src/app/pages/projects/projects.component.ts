import { Component, inject, signal, computed } from '@angular/core'
import { Router } from '@angular/router'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'

import { injectQuery, injectMutation, injectQueryClient } from '@tanstack/angular-query-experimental'

import { MatCardModule } from '@angular/material/card'
import { MatButtonModule } from '@angular/material/button'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatDialogModule, MatDialog } from '@angular/material/dialog'
import { MatIconModule } from '@angular/material/icon'
import { MatChipsModule } from '@angular/material/chips'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatTooltipModule } from '@angular/material/tooltip'

import { ProjectsApiService, ProjectCreate } from '../../api/projects-api.service'
import { ProjectService } from '../../core/services/project.service'
import { AuthService } from '../../core/services/auth.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'
import { ProjectRead } from '../../shared/types'

// ── Constants ─────────────────────────────────────────────────────────────────

const FAMILY_COLOR: Record<string, string> = {
  ISMS:    '#4472C4',
  PRIVACY: '#7030A0',
  CLOUD:   '#00897B',
  AI:      '#ff6b35',
}

const FAMILY_ICON: Record<string, string> = {
  ISMS:    'shield',
  PRIVACY: 'lock_person',
  CLOUD:   'cloud',
  AI:      'psychology',
}

const STATUS_COLOR: Record<string, string> = {
  active:   '#4CAF50',
  inactive: '#FF9800',
  draft:    '#64B5F6',
  archived: '#9E9E9E',
}

const TOTAL_CG: Record<string, number> = {
  ISMS: 53, PRIVACY: 21, CLOUD: 12, AI: 10,
}

const FAMILIES = ['ALL', 'ISMS', 'PRIVACY', 'CLOUD', 'AI']
const STATUSES = ['ALL', 'active', 'inactive', 'draft', 'archived']

function famColor(fam: string): string {
  return FAMILY_COLOR[fam] ?? '#6B7A99'
}
function famIcon(fam: string): string {
  return FAMILY_ICON[fam] ?? 'folder'
}
function statusColor(s: string): string {
  return STATUS_COLOR[s] ?? '#9E9E9E'
}

function formatDate(iso: string | null): string {
  if (!iso) return '—'
  const d = new Date(iso)
  return d.toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' })
}

// ── Create Project Dialog ──────────────────────────────────────────────────────

@Component({
  selector: 'app-create-project-dialog',
  standalone: true,
  imports: [
    FormsModule,
    MatButtonModule, MatDialogModule, MatFormFieldModule,
    MatInputModule, MatSelectModule, MatIconModule,
    MatProgressSpinnerModule,
  ],
  template: `
    <h2 mat-dialog-title>
      New Project
      <small class="dialog-subtitle">
        Create a workspace for a specific product and organisation
      </small>
    </h2>

    <mat-dialog-content>
      @if (error()) {
        <div class="alert-error">{{ error() }}</div>
      }

      <mat-form-field appearance="outline" class="full">
        <mat-label>Project name *</mat-label>
        <input matInput [(ngModel)]="form.name" placeholder="e.g. Acme Corp ISMS 2026" />
      </mat-form-field>

      <mat-form-field appearance="outline" class="full">
        <mat-label>Product</mat-label>
        <mat-select [(ngModel)]="form.product_family" (ngModelChange)="onFamilyChange()">
          <mat-option value="ISMS">ISMS — ISO 27001:2022</mat-option>
          <mat-option value="PRIVACY">Privacy — ISO 27701:2025</mat-option>
          <mat-option value="CLOUD">Cloud — ISO 27018:2025</mat-option>
          <mat-option value="AI">AI — ISO 42001:2023</mat-option>
        </mat-select>
      </mat-form-field>

      <mat-form-field appearance="outline" class="full">
        <mat-label>Description (optional)</mat-label>
        <textarea matInput [(ngModel)]="form.description" rows="2"></textarea>
      </mat-form-field>

      <!-- Organisation selector available for super_admin via admin API -->
      @if (isSuperAdmin) {
        <div class="super-admin-note">
          <mat-icon class="icon-sm">info</mat-icon>
          Super-admin: project will be created for your organisation. Use the admin panel to reassign.
        </div>
      }
    </mat-dialog-content>

    <mat-dialog-actions align="end">
      <button mat-button [disabled]="createMutation.isPending()" mat-dialog-close>Cancel</button>
      <button mat-raised-button color="primary"
              [disabled]="createMutation.isPending()"
              (click)="submit()">
        {{ createMutation.isPending() ? 'Creating…' : 'Create' }}
      </button>
    </mat-dialog-actions>
  `,
  styles: [`
    .full { width: 100%; margin-bottom: 4px; }
    .alert-error {
      background: rgba(192,0,0,0.1);
      border: 1px solid rgba(192,0,0,0.3);
      color: var(--mat-sys-error);
      border-radius: 4px;
      padding: 8px 12px;
      font-size: 0.85rem;
      margin-bottom: 12px;
    }
    mat-dialog-content { display: flex; flex-direction: column; padding-top: 16px !important; }
    .dialog-subtitle {
      display: block;
      font-size: 0.75rem;
      font-weight: 400;
      color: var(--mat-sys-on-surface-variant);
      margin-top: 2px;
    }
    .super-admin-note {
      font-size: 0.75rem;
      color: var(--mat-sys-on-surface-variant);
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 4px;
    }
  `],
})
export class CreateProjectDialogComponent {
  private projApi = inject(ProjectsApiService)
  private dialog  = inject(MatDialog)

  isSuperAdmin = false
  onCreated: () => void = () => {}

  form: ProjectCreate = { name: '', product_family: 'ISMS' }
  error = signal('')

  readonly createMutation = injectMutation(() => ({
    mutationFn: (body: ProjectCreate) => firstValueFrom(this.projApi.create(body)),
    onSuccess: () => {
      this.onCreated()
      this.dialog.closeAll()
    },
    onError: () => this.error.set('Failed to create project — try again.'),
  }))

  onFamilyChange(): void {
    // nothing extra needed — form binding handles it
  }

  submit(): void {
    if (!this.form.name.trim()) {
      this.error.set('Project name is required.')
      return
    }
    this.createMutation.mutate({ ...this.form })
  }
}

// ── Confirm Archive Dialog ─────────────────────────────────────────────────────

@Component({
  selector: 'app-archive-project-dialog',
  standalone: true,
  imports: [MatButtonModule, MatDialogModule, MatProgressSpinnerModule],
  template: `
    <h2 mat-dialog-title>Archive project?</h2>
    <mat-dialog-content>
      <p><strong>{{ projectName }}</strong> will be moved to the Archived filter.
         All policies, implementations and checklists are preserved.</p>
      <p class="note-text">
        You can restore it at any time by setting its status back to active.
      </p>
    </mat-dialog-content>
    <mat-dialog-actions align="end">
      <button mat-button mat-dialog-close>Cancel</button>
      <button mat-raised-button color="warn"
              [disabled]="archiveMutation.isPending()"
              (click)="archive()">
        Archive
      </button>
    </mat-dialog-actions>
  `,
  styles: [`.note-text { font-size: 0.85rem; color: var(--mat-sys-on-surface-variant); }`],
})
export class ArchiveProjectDialogComponent {
  private projApi = inject(ProjectsApiService)
  private dialog  = inject(MatDialog)

  projectId   = ''
  projectName = ''
  onArchived: () => void = () => {}

  readonly archiveMutation = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.projApi.update(this.projectId, { status: 'archived' })),
    onSuccess: () => { this.onArchived(); this.dialog.closeAll() },
  }))

  archive(): void { this.archiveMutation.mutate(undefined) }
}

// ── Confirm Delete Dialog ──────────────────────────────────────────────────────

@Component({
  selector: 'app-delete-project-dialog',
  standalone: true,
  imports: [MatButtonModule, MatDialogModule],
  template: `
    <h2 mat-dialog-title>Permanently delete project?</h2>
    <mat-dialog-content>
      <p><strong>{{ projectName }}</strong> and all its policies, implementations and checklists
         will be permanently deleted. This cannot be undone.</p>
      <p class="note-text">
        Assessments, gaps and evidence linked to this project will be unlinked but not deleted.
      </p>
    </mat-dialog-content>
    <mat-dialog-actions align="end">
      <button mat-button mat-dialog-close>Cancel</button>
      <button mat-raised-button color="warn"
              [disabled]="deleteMutation.isPending()"
              (click)="doDelete()">
        Delete permanently
      </button>
    </mat-dialog-actions>
  `,
  styles: [`.note-text { font-size: 0.85rem; color: var(--mat-sys-on-surface-variant); }`],
})
export class DeleteProjectDialogComponent {
  private projApi = inject(ProjectsApiService)
  private dialog  = inject(MatDialog)

  projectId   = ''
  projectName = ''
  onDeleted: () => void = () => {}

  readonly deleteMutation = injectMutation(() => ({
    mutationFn: () => firstValueFrom(this.projApi.delete(this.projectId)),
    onSuccess: () => { this.onDeleted(); this.dialog.closeAll() },
  }))

  doDelete(): void { this.deleteMutation.mutate(undefined) }
}

// ── Main Projects Component ────────────────────────────────────────────────────

@Component({
  selector: 'app-projects',
  standalone: true,
  imports: [
    FormsModule,
    MatCardModule, MatButtonModule, MatFormFieldModule,
    MatInputModule, MatSelectModule, MatDialogModule,
    MatIconModule, MatChipsModule, MatProgressSpinnerModule, MatTooltipModule,
    PageHeaderComponent,
  ],
  template: `
<div class="projects-page">

  <app-page-header
    title="Projects"
    subtitle="Compliance workspaces — each project tracks policies, implementations and evidence for one organisation"
  >
    <div actions>
      <button mat-raised-button color="primary" (click)="openCreate()">
        <mat-icon>add</mat-icon>
        New Project
      </button>
    </div>
  </app-page-header>

  <!-- Filters -->
  <div class="filters">
    <div class="filter-group">
      @for (fam of families; track fam) {
        <button class="filter-chip"
                [class.filter-chip--active]="familyFilter() === fam"
                [style.--chip-color]="famColor(fam)"
                (click)="familyFilter.set(fam)">
          @if (fam !== 'ALL') {
            <mat-icon class="filter-chip-icon">{{ famIcon(fam) }}</mat-icon>
          }
          {{ fam }}
        </button>
      }
    </div>
    <div class="filter-sep"></div>
    <div class="filter-group">
      @for (st of statuses; track st) {
        <button class="filter-chip"
                [class.filter-chip--active]="statusFilter() === st"
                [style.--chip-color]="statusColor(st)"
                (click)="statusFilter.set(st)">
          {{ st }}
        </button>
      }
    </div>
  </div>

  <!-- Loading -->
  @if (projectsQuery.isLoading()) {
    <div class="projects-grid">
      @for (n of [1,2,3,4,5,6]; track n) {
        <div class="skeleton-card"></div>
      }
    </div>
  }

  <!-- Error -->
  @if (projectsQuery.isError()) {
    <div class="empty-state">
      <mat-icon color="warn">error_outline</mat-icon>
      <span>Failed to load projects.</span>
    </div>
  }

  <!-- Empty state -->
  @if (projectsQuery.isSuccess() && (projectsQuery.data()?.length ?? 0) === 0) {
    <div class="empty-state">
      <mat-icon>folder_open</mat-icon>
      <div>
        <div class="empty-title">
          No projects yet
        </div>
        <div class="empty-subtitle">
          Create your first project to start building your compliance workspace.
        </div>
        <button mat-raised-button color="primary" (click)="openCreate()">
          <mat-icon>add</mat-icon>
          New Project
        </button>
      </div>
    </div>
  }

  <!-- Project cards -->
  @if (projectsQuery.isSuccess() && (projectsQuery.data()?.length ?? 0) > 0) {
    <div class="projects-grid">
      @for (p of projectsQuery.data()!; track p.id) {
        <mat-card class="project-card"
                  [class.project-card--selected]="isSelected(p)"
                  [style.--card-color]="famColor(p.product_family)">
          <mat-card-content (click)="router.navigate(['/projects', p.id])">
            <!-- Header row -->
            <div class="pc-header">
              <div class="pc-header__left">
                <mat-icon class="pc-family-icon" [style.color]="famColor(p.product_family)">
                  {{ famIcon(p.product_family) }}
                </mat-icon>
                <div>
                  <div class="pc-name">{{ p.name }}</div>
                  <div class="pc-org">{{ p.organisation_name ?? '—' }}</div>
                </div>
              </div>
              <div class="pc-chips">
                <span class="mini-chip"
                      [style.background]="famColor(p.product_family) + '20'"
                      [style.color]="famColor(p.product_family)"
                      [style.border-color]="famColor(p.product_family) + '50'">
                  <mat-icon class="icon-sm chip-icon">{{ famIcon(p.product_family) }}</mat-icon>
                  {{ p.product_family }}
                </span>
                <span class="mini-chip"
                      [style.background]="statusColor(p.status) + '20'"
                      [style.color]="statusColor(p.status)"
                      [style.border-color]="statusColor(p.status) + '40'">
                  {{ p.status }}
                </span>
              </div>
            </div>

            <!-- Counts row -->
            <div class="pc-counts">
              <div class="pc-count">
                <span class="pc-count__num" [style.color]="famColor(p.product_family)">
                  {{ $any(p).policy_count ?? 0 }}
                </span>
                <span class="pc-count__lbl">Policies</span>
              </div>
              <div class="pc-count">
                <span class="pc-count__num" [style.color]="famColor(p.product_family)">
                  {{ $any(p).implementation_count ?? 0 }}
                </span>
                <span class="pc-count__lbl">Implementations</span>
              </div>
              <div class="pc-count">
                <span class="pc-count__num" [style.color]="famColor(p.product_family)">
                  {{ $any(p).checklist_count ?? 0 }}
                </span>
                <span class="pc-count__lbl">Checklists</span>
              </div>
            </div>

            <!-- Completeness bar -->
            <div class="pc-bar-wrap">
              <div class="pc-bar-label">
                <span>Control groups with policies</span>
                <span [style.color]="famColor(p.product_family)">
                  {{ minVal($any(p).policy_count ?? 0, totalCg(p.product_family)) }}/{{ totalCg(p.product_family) }}
                </span>
              </div>
              <div class="progress-track">
                <div class="progress-fill"
                     [style.width.%]="polPct(p)"
                     [style.background]="famColor(p.product_family)">
                </div>
              </div>
            </div>
          </mat-card-content>

          <!-- Footer row (outside click area to avoid navigate) -->
          <div class="pc-footer" (click)="$event.stopPropagation()">
            <span class="pc-date">Created {{ formatDate(p.created_at) }}</span>
            <div class="pc-actions">
              @if (isSelected(p)) {
                <span class="mini-chip mini-chip--selected"
                      [style.background]="famColor(p.product_family) + '20'"
                      [style.color]="famColor(p.product_family)">
                  Selected
                </span>
              }

              <!-- Toggle active -->
              <button mat-icon-button
                      [matTooltip]="isSelected(p) ? 'Deactivate' : 'Set as active project'"
                      [style.color]="isSelected(p) ? famColor(p.product_family) : ''"
                      (click)="toggleActive(p)">
                <mat-icon class="icon-md">folder_open</mat-icon>
              </button>

              @if (p.status === 'archived') {
                <!-- Restore -->
                <button mat-icon-button matTooltip="Restore project (set to draft)"
                        (click)="restoreProject(p)">
                  <mat-icon class="icon-md">restore_from_trash</mat-icon>
                </button>
                <!-- Permanent delete -->
                <button mat-icon-button matTooltip="Delete permanently"
                        (click)="openDelete(p)">
                  <mat-icon class="icon-md">delete</mat-icon>
                </button>
              } @else {
                <!-- Archive -->
                <button mat-icon-button matTooltip="Archive project"
                        (click)="openArchive(p)">
                  <mat-icon class="icon-md">archive</mat-icon>
                </button>
              }

              <mat-icon class="pc-arrow-icon"
                        (click)="router.navigate(['/projects', p.id])">
                arrow_forward
              </mat-icon>
            </div>
          </div>
        </mat-card>
      }
    </div>
  }

</div>

  `,
  styles: [`
    .projects-page {
      display: flex;
      flex-direction: column;
      gap: 16px;
      height: 100%;
      overflow-y: auto;
      box-sizing: border-box;
    }

    /* ── Filters ── */
    .filters {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    .filter-group { display: flex; gap: 4px; flex-wrap: wrap; }
    .filter-sep {
      width: 1px;
      height: 24px;
      background: var(--mat-sys-outline-variant);
      flex-shrink: 0;
    }
    .filter-chip {
      display: inline-flex; align-items: center; gap: 4px;
      height: 26px;
      padding: 0 10px;
      border-radius: 13px;
      border: 1px solid var(--mat-sys-outline-variant);
      background: transparent;
      color: var(--mat-sys-on-surface-variant);
      font-size: 0.72rem;
      cursor: pointer;
      transition: background 0.12s, border-color 0.12s, color 0.12s;
    }
    .filter-chip:hover { background: rgba(var(--chip-color-rgb, 100,100,100),0.08); }
    .filter-chip-icon { font-size: 14px; width: 14px; height: 14px; line-height: 1; }
    .filter-chip--active {
      background: color-mix(in srgb, var(--chip-color, #4472C4) 16%, transparent);
      color: var(--chip-color, #4472C4);
      border-color: color-mix(in srgb, var(--chip-color, #4472C4) 50%, transparent);
    }

    /* ── Grid ── */
    .projects-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 12px;
    }

    /* ── Skeleton ── */
    .skeleton-card {
      height: 190px;
      border-radius: 8px;
      background: var(--mat-sys-surface-container-high);
      animation: pulse 1.5s ease-in-out infinite;
    }
    @keyframes pulse { 0%,100% { opacity:1 } 50% { opacity:0.45 } }

    /* ── Project card ── */
    .project-card {
      display: flex;
      flex-direction: column;
      border: 1px solid var(--mat-sys-outline-variant) !important;
      transition: border-color 0.15s, box-shadow 0.15s;
    }
    .project-card:hover {
      border-color: color-mix(in srgb, var(--card-color, #4472C4) 40%, transparent) !important;
    }
    .project-card--selected {
      border-color: color-mix(in srgb, var(--card-color, #4472C4) 60%, transparent) !important;
      box-shadow: 0 0 0 1px color-mix(in srgb, var(--card-color, #4472C4) 30%, transparent) !important;
    }
    .project-card mat-card-content {
      padding: 12px !important;
      cursor: pointer;
      flex: 1;
    }

    /* ── Card content ── */
    .pc-header {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      margin-bottom: 12px;
    }
    .pc-header__left { display: flex; align-items: flex-start; gap: 8px; }
    .pc-family-icon { font-size: 22px; width: 22px; height: 22px; flex-shrink: 0; margin-top: 2px; }
    .pc-name { font-size: 0.88rem; font-weight: 700; line-height: 1.2; color: var(--mat-sys-on-surface); }
    .pc-org { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); margin-top: 2px; }

    .pc-chips { display: flex; flex-direction: column; gap: 4px; align-items: flex-end; }
    .mini-chip {
      display: inline-flex;
      align-items: center;
      padding: 0 6px;
      height: 18px;
      border-radius: 9px;
      border: 1px solid;
      font-size: 0.62rem;
      font-weight: 600;
      white-space: nowrap;
    }
    .mini-chip--selected { font-size: 0.6rem; }

    .pc-counts { display: flex; gap: 16px; margin-bottom: 10px; }
    .pc-count { text-align: center; }
    .pc-count__num { display: block; font-size: 1.1rem; font-weight: 700; line-height: 1; }
    .pc-count__lbl { display: block; font-size: 0.65rem; color: var(--mat-sys-on-surface-variant); margin-top: 2px; }

    .pc-bar-wrap { display: flex; flex-direction: column; gap: 3px; }
    .pc-bar-label {
      display: flex; justify-content: space-between;
      font-size: 0.65rem; color: var(--mat-sys-on-surface-variant);
    }
    .progress-track {
      height: 4px; border-radius: 2px;
      background: var(--mat-sys-surface-container-high);
      overflow: hidden;
    }
    .progress-fill { height: 100%; border-radius: 2px; transition: width 0.3s; }

    /* ── Footer ── */
    .pc-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 6px 12px 8px;
      border-top: 1px solid var(--mat-sys-outline-variant);
    }
    .pc-date { font-size: 0.65rem; color: var(--mat-sys-on-surface-variant); }
    .pc-actions { display: flex; align-items: center; gap: 2px; }

    /* ── Empty state ── */
    .empty-state {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 12px;
      padding: 64px 24px;
      text-align: center;
      color: var(--mat-sys-on-surface-variant);
    }
    .empty-state mat-icon { font-size: 48px; width: 48px; height: 48px; opacity: 0.4; }
    .empty-title { font-size: 1rem; font-weight: 600; color: var(--mat-sys-on-surface); margin-bottom: 4px; }
    .empty-subtitle { font-size: 0.85rem; color: var(--mat-sys-on-surface-variant); margin-bottom: 16px; }
    .chip-icon { font-size: 11px; width: 11px; height: 11px; margin-right: 2px; }
    .pc-arrow-icon { font-size: 14px; width: 14px; height: 14px; color: var(--mat-sys-on-surface-variant); opacity: 0.4; }
  `],
})
export class ProjectsComponent {
  readonly router = inject(Router)
  private projApi = inject(ProjectsApiService)
  private projSvc = inject(ProjectService)
  private authSvc = inject(AuthService)
  private dialog  = inject(MatDialog)

  readonly familyFilter = signal('ALL')
  readonly statusFilter = signal('active')

  readonly families = FAMILIES
  readonly statuses = STATUSES

  // ── Query client for invalidation ───────────────────────────────────────────
  private qc = injectQueryClient()

  // ── Projects list query ──────────────────────────────────────────────────────
  readonly projectsQuery = injectQuery(() => ({
    queryKey: ['projects', this.familyFilter(), this.statusFilter()],
    queryFn: () => firstValueFrom(this.projApi.list({
      product_family: this.familyFilter() === 'ALL' ? undefined : this.familyFilter(),
      status:         this.statusFilter() === 'ALL' ? undefined : this.statusFilter(),
    })),
    staleTime: 30_000,
  }))

  // ── Status toggle mutation ───────────────────────────────────────────────────
  readonly statusMutation = injectMutation(() => ({
    mutationFn: ({ id, status }: { id: string; status: string }) =>
      firstValueFrom(this.projApi.update(id, { status })),
    onSuccess: () => this.qc.invalidateQueries({ queryKey: ['projects'] }),
  }))

  // ── Helpers ──────────────────────────────────────────────────────────────────
  famColor(fam: string):   string { return famColor(fam) }
  famIcon(fam: string):    string { return famIcon(fam) }
  statusColor(st: string): string { return statusColor(st) }
  formatDate(iso: string | null): string { return formatDate(iso) }

  totalCg(fam: string): number { return TOTAL_CG[fam] ?? 53 }
  minVal(a: number, b: number): number { return Math.min(a, b) }

  polPct(p: ProjectRead): number {
    const count = (p as any).policy_count ?? 0
    const total = TOTAL_CG[p.product_family] ?? 53
    return Math.min(100, Math.round((count / Math.max(1, total)) * 100))
  }

  isSelected(p: ProjectRead): boolean {
    return this.projSvc.getActiveProject(p.product_family)?.id === p.id
  }

  // ── Actions ──────────────────────────────────────────────────────────────────
  openCreate(): void {
    const ref = this.dialog.open(CreateProjectDialogComponent, { maxWidth: '520px', width: '100%' })
    const instance = ref.componentInstance
    instance.isSuperAdmin = this.authSvc.isSuperAdmin()
    instance.onCreated = () => this.qc.invalidateQueries({ queryKey: ['projects'] })
  }

  toggleActive(p: ProjectRead): void {
    const fam = p.product_family
    if (this.isSelected(p)) {
      this.projSvc.setActiveProject(fam, null)
    } else {
      this.projSvc.setActiveProject(fam, p)
    }
  }

  restoreProject(p: ProjectRead): void {
    this.statusMutation.mutate({ id: p.id, status: 'draft' })
  }

  openArchive(p: ProjectRead): void {
    const ref = this.dialog.open(ArchiveProjectDialogComponent, { maxWidth: '420px', width: '100%' })
    const inst = ref.componentInstance
    inst.projectId   = p.id
    inst.projectName = p.name
    inst.onArchived  = () => this.qc.invalidateQueries({ queryKey: ['projects'] })
  }

  openDelete(p: ProjectRead): void {
    const ref = this.dialog.open(DeleteProjectDialogComponent, { maxWidth: '420px', width: '100%' })
    const inst = ref.componentInstance
    inst.projectId  = p.id
    inst.projectName = p.name
    inst.onDeleted  = () => this.qc.invalidateQueries({ queryKey: ['projects'] })
  }
}
