import { Component, inject, signal, computed } from '@angular/core'
import { Router } from '@angular/router'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'
import { injectQuery } from '@tanstack/angular-query-experimental'

import { DecimalPipe } from '@angular/common'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatIconModule } from '@angular/material/icon'
import { MatButtonModule } from '@angular/material/button'
import { MatProgressBarModule } from '@angular/material/progress-bar'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatChipsModule } from '@angular/material/chips'

import { DashboardApiService } from '../../api/dashboard-api.service'
import { FeedsApiService } from '../../api/feeds-api.service'
import { ProductService, PRODUCT_COLORS, PRODUCT_LABELS, PRODUCT_SUBTITLES } from '../../core/services/product.service'
import { ProjectService } from '../../core/services/project.service'
import { AuthService } from '../../core/services/auth.service'

const PLATFORM_TOOLS = [
  { label: 'Projects',    path: '/projects',    icon: 'folder_open' },
  { label: 'QA',          path: '/qa',           icon: 'verified' },
  { label: 'Search',      path: '/search',       icon: 'search' },
  { label: 'Compass',     path: '/compass',      icon: 'explore' },
  { label: 'Generators',  path: '/generators',   icon: 'code' },
  { label: 'Connectors',  path: '/connectors',   icon: 'electrical_services' },
  { label: 'Report',      path: '/report',       icon: 'summarize' },
  { label: 'Risk',        path: '/risk',         icon: 'gpp_maybe' },
  { label: 'Remediation', path: '/remediation',  icon: 'build' },
  { label: 'KPI Metrics', path: '/metrics',      icon: 'insights' },
  { label: 'TPRM',        path: '/tprm',         icon: 'handshake' },
  { label: 'BIA',         path: '/bia',          icon: 'health_and_safety' },
  { label: 'EBIOS RM',    path: '/ebios',        icon: 'psychology' },
  { label: 'Admin',       path: '/admin',        icon: 'admin_panel_settings' },
  { label: 'System',      path: '/system',       icon: 'monitor_heart' },
]

const COMPLIANCE_TOOLS = [
  { label: 'NIST CSF 2.0',       path: '/nist-csf',                        icon: 'grid_view' },
  { label: 'NIST AI RMF',        path: '/compliance/NIST-AI-RMF',          icon: 'policy' },
  { label: 'NIST 800-53 R5',     path: '/compliance/NIST-SP-800-53',       icon: 'security' },
  { label: 'NIS2',               path: '/compliance/NIS2',                 icon: 'shield' },
  { label: 'DORA',               path: '/compliance/DORA',                 icon: 'account_balance' },
  { label: 'CIS Controls',       path: '/compliance/CIS-CSC',              icon: 'security' },
  { label: 'BSI Grundschutz',    path: '/compliance/BSI-GRUNDSCHUTZ',      icon: 'shield' },
  { label: 'CSRM (NCSC CH)',     path: '/csrm',                            icon: 'lock_person' },
  { label: 'TISAX',              path: '/compliance/TISAX',                icon: 'verified' },
  { label: 'Swiss nDSG',         path: '/compliance/NDSG',                 icon: 'lock_person' },
  { label: 'EU CRA',             path: '/compliance/EU-CRA',               icon: 'security' },
  { label: 'EU AI Act',          path: '/compliance/EU-AI-ACT',            icon: 'policy' },
  { label: 'EU Cloud Sov.',      path: '/compliance/EU-CLOUD-SOVEREIGNTY', icon: 'cloud' },
  { label: 'COBIT 2019',         path: '/compliance/COBIT-2019',           icon: 'account_balance' },
  { label: 'CSA CCM v4.1',       path: '/compliance/CSA-CCM',              icon: 'cloud' },
  { label: 'CSA AICM',           path: '/compliance/CSA-AICM',             icon: 'policy' },
]

const PRODUCT_FAMILIES = ['ISMS', 'PRIVACY', 'CLOUD'] as const

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    FormsModule, DecimalPipe,
    MatFormFieldModule, MatInputModule, MatIconModule,
    MatButtonModule, MatProgressBarModule, MatTooltipModule, MatChipsModule,
  ],
  template: `
<div class="home">

  <!-- Header -->
  <div class="home__header">
    <div class="home__header-left">
      <h5 class="home__title"><span class="home__bamboo">🎋</span> ISMS CORE Platform</h5>
      <span class="home__date">{{ today }}</span>
    </div>
    <span class="home__user">{{ auth.user()?.email }}</span>
  </div>

  <!-- Search bar -->
  <div class="home__search">
    <mat-form-field appearance="outline" subscriptSizing="dynamic" class="home__search-field">
      <mat-label>Search</mat-label>
      <mat-icon matPrefix>search</mat-icon>
      <input matInput
        placeholder="Search policies, controls, implementations…"
        [(ngModel)]="searchQuery"
        (keydown.enter)="doSearch()" />
      <button mat-icon-button matSuffix (click)="doSearch()" [disabled]="!searchQuery">
        <mat-icon>arrow_forward</mat-icon>
      </button>
    </mat-form-field>
  </div>

  <!-- Product cards -->
  <div class="home__products">

    <!-- ISMS card (wider) -->
    <div class="product-card product-card--isms"
         [style.border-top-color]="ismsColor"
         (click)="selectProduct('isms')">
      <div class="product-card__header">
        <span class="product-card__label" [style.color]="ismsColor">ISMS</span>
        <span class="product-card__subtitle">ISO 27001:2022 + Amd.1</span>
      </div>
      @if (ismsStats()) {
        <div class="product-card__stats">
          <div class="stat">
            <div class="stat__value">{{ ismsStats()!.groups }}</div>
            <div class="stat__label">Groups</div>
          </div>
          <div class="stat">
            <div class="stat__value">{{ ismsStats()!.policies }}</div>
            <div class="stat__label">Policies</div>
          </div>
          <div class="stat">
            <div class="stat__value">{{ ismsStats()!.imps }}</div>
            <div class="stat__label">IMPs</div>
          </div>
          <div class="stat" [class.stat--warn]="ismsStats()!.open_gaps > 0" [class.stat--ok]="ismsStats()!.open_gaps === 0">
            <div class="stat__value">{{ ismsStats()!.open_gaps }}</div>
            <div class="stat__label">Open Gaps</div>
          </div>
        </div>
        <div class="product-card__bars">
          <div class="bar-row">
            <span class="bar-row__label">Framework</span>
            <mat-progress-bar mode="determinate" [value]="ismsStats()!.fw_coverage_pct"
              [style.--mat-progress-bar-active-indicator-color]="'#327df4'"
              [style.--mat-progress-bar-track-color]="'rgba(50,125,244,0.18)'" />
            <span class="bar-row__pct">{{ ismsStats()!.fw_coverage_pct | number:'1.0-0' }}%</span>
          </div>
          <div class="bar-row">
            <span class="bar-row__label">Operational</span>
            <mat-progress-bar mode="determinate" [value]="ismsStats()!.op_coverage_pct"
              [style.--mat-progress-bar-active-indicator-color]="'#00c752'"
              [style.--mat-progress-bar-track-color]="'rgba(0,199,82,0.18)'" />
            <span class="bar-row__pct">{{ ismsStats()!.op_coverage_pct | number:'1.0-0' }}%</span>
          </div>
        </div>
      } @else {
        <div class="product-card__loading">—</div>
      }
    </div>

    <!-- Privacy card -->
    <div class="product-card"
         [style.border-top-color]="privacyColor"
         (click)="selectProduct('privacy')">
      <div class="product-card__header">
        <span class="product-card__label" [style.color]="privacyColor">PRIVACY</span>
        <span class="product-card__subtitle">ISO 27701:2025 Ed. 2</span>
      </div>
      @if (privacyStats()) {
        <div class="product-card__stats product-card__stats--col">
          <div class="stat-row">
            <span class="stat-row__label">Control Groups</span>
            <span class="stat-row__value">{{ privacyStats()!.groups }}</span>
          </div>
          <div class="stat-row">
            <span class="stat-row__label">Policies</span>
            <span class="stat-row__value">{{ privacyStats()!.policies }}</span>
          </div>
          <div class="stat-row">
            <span class="stat-row__label">Implementations</span>
            <span class="stat-row__value">{{ privacyStats()!.imps }}</span>
          </div>
        </div>
        <div class="product-card__dots">
          <div class="dot-row">
            <span class="dot" [style.background]="privacyColor"></span>
            <span class="dot-row__label">ISO 27701:2025</span>
          </div>
          <div class="dot-row">
            <span class="dot" [style.background]="privacyColor"></span>
            <span class="dot-row__label">Controller + Processor</span>
          </div>
        </div>
      } @else {
        <div class="product-card__loading">—</div>
      }
    </div>

    <!-- Cloud card -->
    <div class="product-card"
         [style.border-top-color]="cloudColor"
         (click)="selectProduct('cloud')">
      <div class="product-card__header">
        <span class="product-card__label" [style.color]="cloudColor">CLOUD</span>
        <span class="product-card__subtitle">ISO 27018:2025</span>
      </div>
      @if (cloudStats()) {
        <div class="product-card__stats product-card__stats--col">
          <div class="stat-row">
            <span class="stat-row__label">Control Groups</span>
            <span class="stat-row__value">{{ cloudStats()!.groups }}</span>
          </div>
          <div class="stat-row">
            <span class="stat-row__label">Policies</span>
            <span class="stat-row__value">{{ cloudStats()!.policies }}</span>
          </div>
          <div class="stat-row">
            <span class="stat-row__label">Implementations</span>
            <span class="stat-row__value">{{ cloudStats()!.imps }}</span>
          </div>
        </div>
        <div class="product-card__dots">
          <div class="dot-row">
            <span class="dot" [style.background]="cloudColor"></span>
            <span class="dot-row__label">ISO 27018:2025</span>
          </div>
          <div class="dot-row">
            <span class="dot" [style.background]="cloudColor"></span>
            <span class="dot-row__label">Cloud PII Processor</span>
          </div>
        </div>
      } @else {
        <div class="product-card__loading">—</div>
      }
    </div>

    <!-- AI card -->
    <div class="product-card"
         [style.border-top-color]="aiColor"
         (click)="selectProduct('ai')">
      <div class="product-card__header">
        <span class="product-card__label" [style.color]="aiColor">AI</span>
        <span class="product-card__subtitle">ISO 42001:2023</span>
      </div>
      @if (aiStats()) {
        <div class="product-card__stats product-card__stats--col">
          <div class="stat-row">
            <span class="stat-row__label">Control Groups</span>
            <span class="stat-row__value">{{ aiStats()!.groups }}</span>
          </div>
          <div class="stat-row">
            <span class="stat-row__label">Policies</span>
            <span class="stat-row__value">{{ aiStats()!.policies }}</span>
          </div>
          <div class="stat-row">
            <span class="stat-row__label">Implementations</span>
            <span class="stat-row__value">{{ aiStats()!.imps }}</span>
          </div>
        </div>
        <div class="product-card__dots">
          <div class="dot-row">
            <span class="dot" [style.background]="aiColor"></span>
            <span class="dot-row__label">ISO 42001:2023</span>
          </div>
          <div class="dot-row">
            <span class="dot" [style.background]="aiColor"></span>
            <span class="dot-row__label">AI Management System</span>
          </div>
        </div>
      } @else {
        <div class="product-card__loading">—</div>
      }
    </div>

  </div>

  <!-- Connector bar -->
  <div class="info-bar info-bar--connector" (click)="router.navigate(['/connectors'])">
    <mat-icon class="info-bar__icon">electrical_services</mat-icon>
    <span class="info-bar__label">Connectors</span>
    @if (connectorStats()) {
      <span class="info-bar__badge">{{ connectorStats()!.active }} active</span>
      <span class="info-bar__sep">·</span>
      <span class="info-bar__text">{{ connectorStats()!.evidence_items | number }} evidence items collected</span>
    } @else {
      <span class="info-bar__text">—</span>
    }
    <mat-icon class="info-bar__chevron">chevron_right</mat-icon>
  </div>

  <!-- Intelligence bar -->
  <div class="intel-bar">
    <div class="intel-item" (click)="router.navigate(['/cve-explorer'])">
      <mat-icon class="intel-item__icon">bug_report</mat-icon>
      <div class="intel-item__content">
        <div class="intel-item__value">
          @if (nvdStats()) { {{ nvdStats()!.cve_total | number }} } @else { — }
        </div>
        <div class="intel-item__label">CVEs Indexed</div>
      </div>
    </div>
    <div class="intel-sep"></div>
    <div class="intel-item" (click)="router.navigate(['/threat-feeds'])">
      <mat-icon class="intel-item__icon">warning</mat-icon>
      <div class="intel-item__content">
        <div class="intel-item__value">
          @if (kevStats()) { {{ kevStats()!.total_entries | number }} } @else { — }
        </div>
        <div class="intel-item__label">CISA KEV Entries</div>
      </div>
    </div>
    <div class="intel-sep"></div>
    <div class="intel-item" (click)="router.navigate(['/mitre-attack'])">
      <mat-icon class="intel-item__icon">track_changes</mat-icon>
      <div class="intel-item__content">
        <div class="intel-item__value">
          @if (attackStats()) { {{ attackStats()!.total_techniques + attackStats()!.total_subtechniques | number }} } @else { — }
        </div>
        <div class="intel-item__label">ATT&CK Techniques</div>
      </div>
    </div>
    <div class="intel-sep"></div>
    <div class="intel-item intel-item--feeds">
      <mat-icon class="intel-item__icon">rss_feed</mat-icon>
      <div class="intel-item__content">
        <div class="intel-item__value">
          @if (feedStatus()) {
            {{ feedStatus()!.feeds.filter(f => f.last_status === 'success').length }}
            /
            {{ feedStatus()!.feeds.length }}
          } @else { — }
        </div>
        <div class="intel-item__label">Feeds OK</div>
      </div>
    </div>
  </div>

  <!-- Active project rows -->
  @for (family of projectFamilies; track family) {
    @if (project.getActiveProject(family); as proj) {
      <div class="project-row" (click)="router.navigate(['/projects', proj.id])">
        <mat-icon class="project-row__icon">folder_open</mat-icon>
        <div class="project-row__info">
          <span class="project-row__family">{{ family }}</span>
          <span class="project-row__name">{{ proj.name }}</span>
        </div>
        <span class="project-row__status" [class]="'status-' + proj.status.toLowerCase()">{{ proj.status }}</span>
        <mat-progress-bar mode="determinate" [value]="50" color="primary" class="project-row__bar" />
        <mat-icon class="project-row__chevron">chevron_right</mat-icon>
      </div>
    }
  }

  <!-- Platform Tools -->
  <div class="tools-section">
    <div class="tools-section__heading">Platform Tools</div>
    <div class="tools-section__chips">
      @for (tool of platformTools; track tool.path) {
        <div class="tool-chip" (click)="router.navigate([tool.path])">
          <mat-icon class="tool-chip__icon">{{ tool.icon }}</mat-icon>
          <span>{{ tool.label }}</span>
        </div>
      }
    </div>
  </div>

  <!-- Compliance Assessments -->
  <div class="tools-section">
    <div class="tools-section__heading">Compliance Assessments</div>
    <div class="tools-section__chips">
      @for (tool of complianceTools; track tool.path) {
        <div class="tool-chip" (click)="router.navigate([tool.path])">
          <mat-icon class="tool-chip__icon">{{ tool.icon }}</mat-icon>
          <span>{{ tool.label }}</span>
        </div>
      }
    </div>
  </div>

</div>
  `,
  styles: [`
    .home {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    /* Header */
    .home__header {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .home__header-left {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }
    .home__title {
      margin: 0;
      font-size: 1.75rem;
      font-weight: 700;
      color: var(--mat-sys-on-surface);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .home__bamboo { font-size: 1.6rem; line-height: 1; }
    .home__date {
      font-size: 0.75rem;
      color: var(--mat-sys-on-surface-variant);
    }
    .home__user {
      font-size: 0.75rem;
      color: var(--mat-sys-on-surface-variant);
    }

    /* Search */
    .home__search { width: 100%; }
    .home__search-field { width: 100%; }

    /* Product cards */
    .home__products {
      display: flex;
      gap: 12px;
      align-items: stretch;
    }
    .product-card {
      flex: 1;
      background: var(--mat-sys-surface-container);
      border-radius: 8px;
      border-top: 3px solid transparent;
      padding: 12px;
      cursor: pointer;
      transition: background 0.15s;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .product-card--isms { flex: 0 0 48%; }
    .product-card:hover { background: var(--mat-sys-surface-container-high); }

    .product-card__header {
      display: flex;
      flex-direction: column;
      gap: 2px;
    }
    .product-card__label {
      font-size: 0.7rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }
    .product-card__subtitle {
      font-size: 0.7rem;
      color: var(--mat-sys-on-surface-variant);
    }
    .product-card__loading {
      color: var(--mat-sys-on-surface-variant);
      font-size: 1.2rem;
    }

    /* Stats grid */
    .product-card__stats {
      display: flex;
      gap: 12px;
    }
    .product-card__stats--col {
      flex-direction: column;
      gap: 4px;
    }
    .stat {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .stat__value {
      font-size: 1.4rem;
      font-weight: 600;
      color: var(--mat-sys-on-surface);
    }
    .stat__label {
      font-size: 0.65rem;
      color: var(--mat-sys-on-surface-variant);
      text-align: center;
    }
    .stat--warn .stat__value { color: var(--gap-count-color); }
    .stat--ok .stat__value { color: var(--gap-count-color); }

    .stat-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .stat-row__label {
      font-size: 0.7rem;
      color: var(--mat-sys-on-surface-variant);
    }
    .stat-row__value {
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--mat-sys-on-surface);
    }

    /* Progress bars */
    .product-card__bars {
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-top: 4px;
    }
    .bar-row {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .bar-row__label {
      font-size: 0.65rem;
      color: var(--mat-sys-on-surface-variant);
      width: 68px;
      flex-shrink: 0;
    }
    .bar-row mat-progress-bar { flex: 1; }
    .bar-row__pct {
      font-size: 0.65rem;
      color: var(--mat-sys-on-surface-variant);
      width: 32px;
      text-align: right;
      flex-shrink: 0;
    }

    /* Status dots */
    .product-card__dots {
      display: flex;
      flex-direction: column;
      gap: 4px;
      margin-top: 4px;
    }
    .dot-row {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      flex-shrink: 0;
    }
    .dot--green  { background: #4caf50; }
    .dot--blue   { background: #4472C4; }
    .dot--teal   { background: #00897B; }
    .dot--orange { background: #ff6b35; }
    .dot-row__label {
      font-size: 0.7rem;
      color: var(--mat-sys-on-surface-variant);
    }

    /* Info bar (connectors) */
    .info-bar {
      display: flex;
      align-items: center;
      gap: 8px;
      background: var(--mat-sys-surface-container);
      border-radius: 8px;
      padding: 10px 14px;
      cursor: pointer;
      transition: background 0.15s;
    }
    .info-bar:hover { background: var(--mat-sys-surface-container-high); }
    .info-bar--connector { border-left: 3px solid #4472C4; }
    .info-bar__icon { color: var(--mat-sys-on-surface-variant); font-size: 18px; }
    .info-bar__label { font-size: 0.8rem; font-weight: 600; color: var(--mat-sys-on-surface); }
    .info-bar__badge {
      font-size: 0.7rem;
      background: #4472C4;
      color: #fff;
      border-radius: 10px;
      padding: 1px 8px;
    }
    .info-bar__sep { color: var(--mat-sys-on-surface-variant); }
    .info-bar__text { font-size: 0.8rem; color: var(--mat-sys-on-surface-variant); flex: 1; }
    .info-bar__chevron { color: var(--mat-sys-on-surface-variant); margin-left: auto; }

    /* Intelligence bar */
    .intel-bar {
      display: flex;
      align-items: stretch;
      background: var(--mat-sys-surface-container);
      border-radius: 8px;
      overflow: hidden;
    }
    .intel-item {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 10px 16px;
      cursor: pointer;
      flex: 1;
      transition: background 0.15s;
    }
    .intel-item:hover { background: var(--mat-sys-surface-container-high); }
    .intel-item--feeds { cursor: default; }
    .intel-item--feeds:hover { background: transparent; }
    .intel-item__icon { color: var(--mat-sys-primary); font-size: 20px; }
    .intel-item__value { font-size: 1rem; font-weight: 600; color: var(--mat-sys-on-surface); }
    .intel-item__label { font-size: 0.65rem; color: var(--mat-sys-on-surface-variant); }
    .intel-item__content { display: flex; flex-direction: column; }
    .intel-sep { width: 1px; background: var(--mat-sys-outline-variant); margin: 8px 0; flex-shrink: 0; }

    /* Project rows */
    .project-row {
      display: flex;
      align-items: center;
      gap: 10px;
      background: var(--mat-sys-surface-container);
      border-radius: 8px;
      padding: 10px 14px;
      cursor: pointer;
      transition: background 0.15s;
    }
    .project-row:hover { background: var(--mat-sys-surface-container-high); }
    .project-row__icon { color: var(--mat-sys-primary); font-size: 18px; }
    .project-row__info { display: flex; flex-direction: column; flex: 1; min-width: 0; }
    .project-row__family { font-size: 0.65rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: var(--mat-sys-on-surface-variant); }
    .project-row__name { font-size: 0.85rem; font-weight: 500; color: var(--mat-sys-on-surface); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
    .project-row__status { font-size: 0.65rem; padding: 2px 8px; border-radius: 10px; background: var(--mat-sys-surface-container-high); color: var(--mat-sys-on-surface-variant); flex-shrink: 0; }
    .project-row__bar { width: 100px; flex-shrink: 0; }
    .project-row__chevron { color: var(--mat-sys-on-surface-variant); font-size: 18px; }

    /* Tools sections */
    .tools-section { display: flex; flex-direction: column; gap: 8px; }
    .tools-section__heading {
      font-size: 0.7rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--mat-sys-on-surface-variant);
    }
    .tools-section__chips {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }
    .tool-chip {
      display: flex;
      align-items: center;
      gap: 4px;
      padding: 4px 12px;
      border-radius: 16px;
      background: var(--mat-sys-surface-container);
      cursor: pointer;
      font-size: 0.78rem;
      color: var(--mat-sys-on-surface);
      transition: background 0.15s;
      border: 1px solid var(--mat-sys-outline-variant);
    }
    .tool-chip:hover { background: var(--mat-sys-surface-container-high); }
    .tool-chip__icon { font-size: 14px; width: 14px; height: 14px; }
  `],
})
export class HomeComponent {
  readonly router  = inject(Router)
  readonly auth    = inject(AuthService)
  readonly product = inject(ProductService)
  readonly project = inject(ProjectService)

  private dashApi  = inject(DashboardApiService)
  private feedsApi = inject(FeedsApiService)

  readonly platformTools   = PLATFORM_TOOLS
  readonly complianceTools = COMPLIANCE_TOOLS
  readonly projectFamilies = PRODUCT_FAMILIES

  searchQuery = ''

  readonly today = new Date().toLocaleDateString('en-GB', {
    weekday: 'long', day: 'numeric', month: 'long', year: 'numeric',
  })

  readonly ismsColor    = PRODUCT_COLORS['isms']
  readonly privacyColor = PRODUCT_COLORS['privacy']
  readonly cloudColor   = PRODUCT_COLORS['cloud']
  readonly aiColor      = PRODUCT_COLORS['ai']

  private summaryQuery = injectQuery(() => ({
    queryKey: ['home-summary'],
    queryFn: () => firstValueFrom(this.dashApi.getHomeSummary()),
    staleTime: 30_000,
  }))

  private kevQuery = injectQuery(() => ({
    queryKey: ['kev-stats'],
    queryFn: () => firstValueFrom(this.feedsApi.getKevStats()),
    staleTime: 60_000,
  }))

  private nvdQuery = injectQuery(() => ({
    queryKey: ['nvd-index-stats'],
    queryFn: () => firstValueFrom(this.feedsApi.getNvdIndexStats()),
    staleTime: 60_000,
  }))

  private attackQuery = injectQuery(() => ({
    queryKey: ['attack-stats'],
    queryFn: () => firstValueFrom(this.feedsApi.getAttackStats()),
    staleTime: 60_000,
  }))

  private feedStatusQuery = injectQuery(() => ({
    queryKey: ['feed-status'],
    queryFn: () => firstValueFrom(this.feedsApi.getStatus()),
    staleTime: 30_000,
  }))

  readonly ismsStats      = computed(() => this.summaryQuery.data()?.isms ?? null)
  readonly privacyStats   = computed(() => this.summaryQuery.data()?.privacy ?? null)
  readonly cloudStats     = computed(() => this.summaryQuery.data()?.cloud ?? null)
  readonly aiStats        = computed(() => this.summaryQuery.data()?.ai ?? null)
  readonly connectorStats = computed(() => this.summaryQuery.data()?.connectors ?? null)
  readonly kevStats       = computed(() => this.kevQuery.data() ?? null)
  readonly nvdStats       = computed(() => this.nvdQuery.data() ?? null)
  readonly attackStats    = computed(() => this.attackQuery.data() ?? null)
  readonly feedStatus     = computed(() => this.feedStatusQuery.data() ?? null)

  selectProduct(p: 'isms' | 'privacy' | 'cloud' | 'ai'): void {
    this.product.setProduct(p)
    this.router.navigate(['/overview'])
  }

  doSearch(): void {
    const q = this.searchQuery.trim()
    if (!q) return
    this.router.navigate(['/search'], { queryParams: { q } })
  }
}
