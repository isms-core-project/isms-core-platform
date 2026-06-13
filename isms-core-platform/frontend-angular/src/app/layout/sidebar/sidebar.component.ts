import { Component, signal, computed, inject, OnInit, output } from '@angular/core'
import { RouterLink, RouterLinkActive, Router, NavigationEnd } from '@angular/router'
import { filter } from 'rxjs/operators'
import { MatIconModule } from '@angular/material/icon'
import { MatButtonModule } from '@angular/material/button'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatDividerModule } from '@angular/material/divider'
import { injectQuery } from '@tanstack/angular-query-experimental'
import { HttpClient } from '@angular/common/http'
import { firstValueFrom } from 'rxjs'
import { AuthService } from '../../core/services/auth.service'
import { ThemeService } from '../../core/services/theme.service'
import { ProductService, type Product, PRODUCT_COLORS, PRODUCT_LABELS } from '../../core/services/product.service'
import { ProjectService } from '../../core/services/project.service'

export const SIDEBAR_WIDTH = 220
export const SIDEBAR_MINI_WIDTH = 52

interface NavItem {
  label: string
  path: string
  icon: string          // material icon name
  adminOnly?: boolean
  superAdminOnly?: boolean
  managerAndAbove?: boolean
  notViewer?: boolean
  disabled?: boolean
  disabledTip?: string
}

interface NavRegion { label: string; items: NavItem[] }

const PRODUCT_NAV: NavItem[] = [
  { label: 'Overview',         path: '/overview',    icon: 'dashboard' },
  { label: 'Coverage',         path: '/coverage',    icon: 'compare_arrows' },
  { label: 'Controls Library', path: '/controls',    icon: 'account_tree' },
  { label: 'Assessments',      path: '/assessments', icon: 'assignment' },
  { label: 'Policies',         path: '/policies',    icon: 'policy' },
  { label: 'Gaps',             path: '/gaps',        icon: 'find_in_page' },
  { label: 'Evidence',         path: '/evidence',    icon: 'upload_file' },
  { label: 'Graph',            path: '/graph',       icon: 'device_hub' },
]

const NAV_RISK: NavItem[] = [
  { label: 'Risk Register', path: '/risk-register', icon: 'warning_amber' },
  { label: 'Remediation',   path: '/remediation',   icon: 'assignment' },
  { label: 'KPI Metrics',   path: '/metrics',       icon: 'insights',             notViewer: true },
  { label: 'BIA',           path: '/bia',            icon: 'health_and_safety',    notViewer: true },
  { label: 'EBIOS RM',      path: '/ebios',          icon: 'psychology',           notViewer: true },
]

const NAV_TOOLS: NavItem[] = [
  { label: 'Projects',     path: '/projects',    icon: 'folder_open' },
  { label: 'QA',           path: '/qa',          icon: 'verified',         notViewer: true },
  { label: 'Search',       path: '/search',      icon: 'search' },
  { label: 'Compass',      path: '/compass',     icon: 'explore' },
  { label: 'Risk Wizard',  path: '/risk',        icon: 'calculate' },
  { label: 'Glossary',     path: '/glossary',    icon: 'menu_book' },
  { label: 'Generators',   path: '/generators',  icon: 'code',             managerAndAbove: true },
  { label: 'Report',       path: '/report',      icon: 'summarize',        notViewer: true },
  { label: 'Help',         path: '/help',        icon: 'help_outline' },
]

const NAV_FRAMEWORK_REGIONS: NavRegion[] = [
  {
    label: 'Global',
    items: [
      { label: 'NIST CSF 2.0',      path: '/nist-csf',    icon: 'grid_view' },
      { label: 'NIST AI RMF 1.0',   path: '/compliance/nist-ai-rmf', icon: 'policy' },
      { label: 'NIST SP 800-53 R5', path: '/compliance/nist-800-53', icon: 'security' },
      { label: 'CIS Controls',       path: '/compliance/cis',    icon: 'security' },
      { label: 'COBIT 2019',         path: '/compliance/cobit',  icon: 'account_balance' },
      { label: 'CSA CCM v4.1',       path: '/compliance/csa-ccm', icon: 'cloud' },
      { label: 'CSA AI Controls',    path: '/compliance/csa-aicm', icon: 'policy' },
    ],
  },
  {
    label: 'European Union',
    items: [
      { label: 'NIS2',               path: '/compliance/nis2',      icon: 'shield' },
      { label: 'DORA',               path: '/compliance/dora',      icon: 'account_balance' },
      { label: 'EU Cyber Resilience',path: '/compliance/cra',       icon: 'security' },
      { label: 'EU AI Act',          path: '/compliance/ai-act',    icon: 'policy' },
      { label: 'EU Cloud Sovereignty',path: '/compliance/eu-cloud-sov', icon: 'cloud' },
    ],
  },
  {
    label: 'Switzerland',
    items: [
      { label: 'Swiss ISG (SR 128)', path: '/compliance/isg',  icon: 'shield' },
      { label: 'CSRM (NCSC CH)',     path: '/csrm',            icon: 'lock_person' },
      { label: 'Swiss nDSG',         path: '/compliance/ndsg', icon: 'lock_person' },
    ],
  },
  {
    label: 'United Kingdom',
    items: [
      { label: 'UK NIS Regulations', path: '/compliance/uk-nis',          icon: 'shield' },
      { label: 'NCSC CAF v4.0',      path: '/compliance/ncsc-caf',        icon: 'shield' },
      { label: 'UK Op. Resilience',  path: '/compliance/uk-op-resilience', icon: 'account_balance' },
    ],
  },
  {
    label: 'Germany',
    items: [
      { label: 'BaFin BAIT',          path: '/compliance/bafin-bait',  icon: 'account_balance' },
      { label: 'BSI IT-Grundschutz',  path: '/compliance/bsi',         icon: 'shield' },
      { label: 'BSI C5:2026',         path: '/compliance/bsi-c5-2026', icon: 'cloud' },
      { label: 'BSI C3A',             path: '/compliance/bsi-c3a',     icon: 'verified_user' },
      { label: 'TISAX',               path: '/compliance/tisax',       icon: 'verified' },
    ],
  },
  {
    label: 'France',
    items: [{ label: 'ReCyF v2.5 (NIS2 FR)', path: '/compliance/fr-recyf', icon: 'shield' }],
  },
  {
    label: 'Belgium',
    items: [{ label: 'CyberFundamentals', path: '/compliance/cyfun-be', icon: 'shield' }],
  },
  {
    label: 'Luxembourg',
    items: [{ label: 'CSSF 20-750', path: '/compliance/cssf-lu', icon: 'account_balance' }],
  },
  {
    label: 'Italy',
    items: [{ label: 'ACN Guidelines', path: '/compliance/acn-it', icon: 'shield' }],
  },
]

const NAV_INTELLIGENCE: NavItem[] = [
  { label: 'Threat Feeds',    path: '/threat-feeds',   icon: 'stream' },
  { label: 'MITRE ATT&CK',   path: '/mitre-attack',   icon: 'bug_report' },
  { label: 'ATT&CK Heatmap', path: '/mitre-heatmap',  icon: 'grid_view' },
  { label: 'MITRE Groups',   path: '/mitre-groups',   icon: 'people' },
  { label: 'MITRE Software', path: '/mitre-software', icon: 'code' },
  { label: 'MITRE Campaigns',path: '/mitre-campaigns',icon: 'insights' },
  { label: 'MITRE ATLAS',    path: '/mitre-atlas',    icon: 'travel_explore' },
  { label: 'CVE Explorer',   path: '/cve-explorer',   icon: 'bug_report' },
  { label: 'CPE Explorer',   path: '/cpe-explorer',   icon: 'security' },
  { label: 'EUVD',           path: '/euvd-explorer',  icon: 'manage_search' },
]

const NAV_TI_ITEMS: NavItem[] = [
  { label: 'IOC Explorer',    path: '/ioc-explorer',   icon: 'track_changes' },
  { label: 'Malware Atlas',   path: '/malware-atlas',  icon: 'coronavirus' },
  { label: 'IP Enrichment',   path: '/ip-enrichment',  icon: 'router' },
  { label: 'Threat Exposure', path: '/threat-exposure',icon: 'crisis_alert' },
]

const NAV_SUPPLIERS: NavItem[] = [
  { label: 'TPRM', path: '/tprm', icon: 'handshake', notViewer: true },
]

const NAV_ADMIN: NavItem[] = [
  { label: 'Users',             path: '/admin',              icon: 'people',            adminOnly: true },
  { label: 'Logs',              path: '/admin/logs',         icon: 'receipt_long',      adminOnly: true },
  { label: 'Connectors',        path: '/connectors',         icon: 'electrical_services', adminOnly: true },
  { label: 'Custom Frameworks', path: '/custom-frameworks',  icon: 'app_registration',  adminOnly: true },
  { label: 'Framework Tracker', path: '/framework-tracker',  icon: 'update',            adminOnly: true },
  { label: 'Crosswalk Tracker', path: '/crosswalk-tracker',  icon: 'account_tree',      adminOnly: true },
  { label: 'System',            path: '/system',             icon: 'monitor_heart',     adminOnly: true },
  { label: 'Organisations',     path: '/organisations',      icon: 'business',          superAdminOnly: true },
]

const ADMIN_ROLES     = new Set(['super_admin', 'admin'])
const MANAGER_ROLES   = new Set(['super_admin', 'admin', 'isms_manager'])
const NON_VIEWER_ROLES = new Set(['super_admin', 'admin', 'isms_manager', 'auditor', 'control_owner'])

const RISK_PATHS       = ['/risk-register', '/remediation', '/metrics', '/bia', '/ebios']
const TOOLS_PATHS      = ['/projects', '/qa', '/search', '/compass', '/generators', '/report', '/risk', '/glossary']
const FRAMEWORK_PATHS  = ['/nist-csf', '/compliance/', '/csrm']
const SUPPLIER_PATHS   = ['/tprm']
const ADMIN_PATHS      = ['/admin', '/connectors', '/system', '/organisations', '/custom-frameworks', '/framework-tracker', '/crosswalk-tracker']
const INTELLIGENCE_PATHS = ['/threat-feeds', '/mitre-attack', '/mitre-atlas', '/mitre-groups', '/mitre-software', '/mitre-campaigns', '/mitre-heatmap', '/cve-explorer', '/cpe-explorer', '/euvd-explorer', '/ioc-explorer', '/malware-atlas', '/ip-enrichment', '/threat-exposure']
const PRODUCT_SECTIONS: { value: Product; icon: string; section?: string }[] = [
  { value: 'isms',    icon: 'shield' },
  { value: 'privacy', icon: 'lock_person' },
  { value: 'cloud',   icon: 'cloud' },
  { value: 'ai',      icon: 'psychology' },
]

@Component({
  selector: 'app-sidebar',
  standalone: true,
  imports: [RouterLink, RouterLinkActive, MatIconModule, MatButtonModule, MatTooltipModule, MatDividerModule],
  template: `
    <aside class="sidebar" [style.width.px]="collapsed() ? MINI : FULL">
      <!-- Logo -->
      <div class="sidebar__logo" [class.sidebar__logo--mini]="collapsed()">
        <a routerLink="/" class="sidebar__brand">
          <mat-icon class="sidebar__shield" [style.color]="productColor()">shield</mat-icon>
          @if (!collapsed()) {
            <div>
              <div class="sidebar__title" [style.color]="productColor()">ISMS CORE</div>
              <div class="sidebar__sub">IS &amp; Privacy Compliance</div>
            </div>
          }
        </a>
        <button class="sidebar__toggle" (click)="toggleCollapse()" [matTooltip]="collapsed() ? 'Expand sidebar' : ''" matTooltipPosition="right">
          <mat-icon>{{ collapsed() ? 'chevron_right' : 'chevron_left' }}</mat-icon>
        </button>
      </div>

      <mat-divider />

      <!-- Scrollable nav -->
      <div class="sidebar__scroll">

        <!-- Home -->
        <div class="sidebar__section">
          <a routerLink="/" routerLinkActive="nav-item--active" [routerLinkActiveOptions]="{exact:true}"
             class="nav-item" [class.nav-item--mini]="collapsed()"
             [matTooltip]="collapsed() ? 'Home' : ''" matTooltipPosition="right">
            <mat-icon class="nav-icon">home</mat-icon>
            @if (!collapsed()) { <span class="nav-label">Home</span> }
          </a>
        </div>

        <!-- Active project chip -->
        @if (!collapsed()) {
          <div class="sidebar__project">
            @if (auth.user()?.id) {
              <a routerLink="/projects" class="project-chip">
                <mat-icon class="project-chip__icon">folder_open</mat-icon>
                <span class="project-chip__name">{{ activeProjectName() }}</span>
              </a>
            }
          </div>
        }

        <!-- Product sections -->
        @for (ps of PRODUCT_SECTIONS; track ps.value) {
          <div class="sidebar__section">
            <button class="nav-group__header"
              [class.nav-group__header--mini]="collapsed()"
              [class.nav-group__header--active]="product.product() === ps.value"
              [style.--group-color]="getProductColor(ps.value)"
              (click)="toggleProduct(ps.value)"
              [matTooltip]="collapsed() ? getProductLabel(ps.value) : ''" matTooltipPosition="right">
              <mat-icon class="nav-icon" [style.color]="product.product() === ps.value ? getProductColor(ps.value) : null">{{ ps.icon }}</mat-icon>
              @if (!collapsed()) {
                <span class="nav-group__label" [style.color]="product.product() === ps.value ? getProductColor(ps.value) : null">
                  {{ getProductLabel(ps.value) }}
                </span>
                <mat-icon class="nav-group__arrow" [class.nav-group__arrow--open]="expandedProduct() === ps.value">expand_more</mat-icon>
              }
            </button>

            @if (expandedProduct() === ps.value && !collapsed()) {
              <div class="nav-group__items">
                @for (item of getProductNav(ps.value); track item.path) {
                  <a class="nav-item nav-item--indented"
                     [class.nav-item--active]="isProductActive(item.path, ps.value)"
                     [style.--item-color]="getProductColor(ps.value)"
                     (click)="navigateProduct(item.path, ps.value)">
                    <mat-icon class="nav-icon">{{ item.icon }}</mat-icon>
                    <span class="nav-label">{{ item.label }}</span>
                  </a>
                }
              </div>
            }
          </div>
        }

        <mat-divider class="sidebar__divider" />

        <!-- Risk & Compliance -->
        @if (filterItems(NAV_RISK).length > 0) {
          <div class="sidebar__section">
            <button class="nav-group__header" [class.nav-group__header--mini]="collapsed()"
              [style.--group-color]="'#ff9800'"
              (click)="riskOpen.set(!riskOpen())"
              [matTooltip]="collapsed() ? 'Risk & Compliance' : ''" matTooltipPosition="right">
              <mat-icon class="nav-icon">warning_amber</mat-icon>
              @if (!collapsed()) {
                <span class="nav-group__label">Risk &amp; Compliance</span>
                <mat-icon class="nav-group__arrow" [class.nav-group__arrow--open]="riskOpen()">expand_more</mat-icon>
              }
            </button>
            @if (riskOpen() && !collapsed()) {
              <div class="nav-group__items">
                @for (item of filterItems(NAV_RISK); track item.path) {
                  <a class="nav-item nav-item--indented" routerLink="{{ item.path }}"
                     routerLinkActive="nav-item--active" [style.--item-color]="'#ff9800'">
                    <mat-icon class="nav-icon">{{ item.icon }}</mat-icon>
                    <span class="nav-label">{{ item.label }}</span>
                  </a>
                }
              </div>
            }
          </div>
        }

        <!-- Tools -->
        <div class="sidebar__section">
          <button class="nav-group__header" [class.nav-group__header--mini]="collapsed()"
            [style.--group-color]="'#607d8b'"
            (click)="toolsOpen.set(!toolsOpen())"
            [matTooltip]="collapsed() ? 'Tools' : ''" matTooltipPosition="right">
            <mat-icon class="nav-icon">tune</mat-icon>
            @if (!collapsed()) {
              <span class="nav-group__label">Tools</span>
              <mat-icon class="nav-group__arrow" [class.nav-group__arrow--open]="toolsOpen()">expand_more</mat-icon>
            }
          </button>
          @if (toolsOpen() && !collapsed()) {
            <div class="nav-group__items">
              @for (item of filterItems(NAV_TOOLS); track item.path) {
                <a class="nav-item nav-item--indented" routerLink="{{ item.path }}"
                   routerLinkActive="nav-item--active" [style.--item-color]="'#607d8b'">
                  <mat-icon class="nav-icon">{{ item.icon }}</mat-icon>
                  <span class="nav-label">{{ item.label }}</span>
                </a>
              }
            </div>
          }
        </div>

        <!-- Compliance Frameworks -->
        <div class="sidebar__section">
          <button class="nav-group__header" [class.nav-group__header--mini]="collapsed()"
            [style.--group-color]="'#5c6bc0'"
            (click)="frameworksOpen.set(!frameworksOpen())"
            [matTooltip]="collapsed() ? 'Frameworks' : ''" matTooltipPosition="right">
            <mat-icon class="nav-icon">grid_view</mat-icon>
            @if (!collapsed()) {
              <span class="nav-group__label">Frameworks</span>
              <mat-icon class="nav-group__arrow" [class.nav-group__arrow--open]="frameworksOpen()">expand_more</mat-icon>
            }
          </button>
          @if (frameworksOpen() && !collapsed()) {
            <div class="nav-group__items">
              @for (region of NAV_FRAMEWORK_REGIONS; track region.label) {
                <div class="nav-region">
                  <button class="nav-region__header" (click)="toggleRegion(region.label)">
                    <span>{{ region.label }}</span>
                    <mat-icon class="nav-region__arrow" [class.nav-region__arrow--open]="openRegions().has(region.label)">expand_more</mat-icon>
                  </button>
                  @if (openRegions().has(region.label)) {
                    @for (item of region.items; track item.path) {
                      <a class="nav-item nav-item--indented nav-item--deep" routerLink="{{ item.path }}"
                         routerLinkActive="nav-item--active" [style.--item-color]="'#5c6bc0'">
                        <mat-icon class="nav-icon nav-icon--sm">{{ item.icon }}</mat-icon>
                        <span class="nav-label">{{ item.label }}</span>
                      </a>
                    }
                  }
                </div>
              }
            </div>
          }
        </div>

        <!-- Intelligence -->
        <div class="sidebar__section">
          <button class="nav-group__header" [class.nav-group__header--mini]="collapsed()"
            [style.--group-color]="'#29b6f6'"
            (click)="intelOpen.set(!intelOpen())"
            [matTooltip]="collapsed() ? 'Intelligence' : ''" matTooltipPosition="right">
            <mat-icon class="nav-icon">stream</mat-icon>
            @if (!collapsed()) {
              <span class="nav-group__label">Intelligence</span>
              @if (hasIntelAlert()) {
                <span class="nav-badge"></span>
              }
              <mat-icon class="nav-group__arrow" [class.nav-group__arrow--open]="intelOpen()">expand_more</mat-icon>
            }
          </button>
          @if (intelOpen() && !collapsed()) {
            <div class="nav-group__items">
              @for (item of allIntelItems(); track item.path) {
                @if (item.disabled) {
                  <span class="nav-item nav-item--indented nav-item--disabled" [matTooltip]="item.disabledTip ?? ''" matTooltipPosition="right">
                    <mat-icon class="nav-icon">{{ item.icon }}</mat-icon>
                    <span class="nav-label">{{ item.label }}</span>
                  </span>
                } @else {
                  <a class="nav-item nav-item--indented" routerLink="{{ item.path }}"
                     routerLinkActive="nav-item--active" [style.--item-color]="'#29b6f6'">
                    <mat-icon class="nav-icon">{{ item.icon }}</mat-icon>
                    <span class="nav-label">{{ item.label }}</span>
                  </a>
                }
              }
            </div>
          }
        </div>

        <!-- Suppliers -->
        @if (filterItems(NAV_SUPPLIERS).length > 0) {
          <div class="sidebar__section">
            <button class="nav-group__header" [class.nav-group__header--mini]="collapsed()"
              [style.--group-color]="'#26a69a'"
              (click)="suppliersOpen.set(!suppliersOpen())"
              [matTooltip]="collapsed() ? 'Suppliers' : ''" matTooltipPosition="right">
              <mat-icon class="nav-icon">handshake</mat-icon>
              @if (!collapsed()) {
                <span class="nav-group__label">Suppliers</span>
                <mat-icon class="nav-group__arrow" [class.nav-group__arrow--open]="suppliersOpen()">expand_more</mat-icon>
              }
            </button>
            @if (suppliersOpen() && !collapsed()) {
              <div class="nav-group__items">
                @for (item of filterItems(NAV_SUPPLIERS); track item.path) {
                  <a class="nav-item nav-item--indented" routerLink="{{ item.path }}"
                     routerLinkActive="nav-item--active" [style.--item-color]="'#26a69a'">
                    <mat-icon class="nav-icon">{{ item.icon }}</mat-icon>
                    <span class="nav-label">{{ item.label }}</span>
                  </a>
                }
              </div>
            }
          </div>
        }

        <!-- Admin -->
        @if (filterItems(NAV_ADMIN).length > 0) {
          <mat-divider class="sidebar__divider" />
          <div class="sidebar__section">
            <button class="nav-group__header" [class.nav-group__header--mini]="collapsed()"
              [style.--group-color]="'#ef5350'"
              (click)="adminOpen.set(!adminOpen())"
              [matTooltip]="collapsed() ? 'Admin' : ''" matTooltipPosition="right">
              <mat-icon class="nav-icon">admin_panel_settings</mat-icon>
              @if (!collapsed()) {
                <span class="nav-group__label">Admin</span>
                <mat-icon class="nav-group__arrow" [class.nav-group__arrow--open]="adminOpen()">expand_more</mat-icon>
              }
            </button>
            @if (adminOpen() && !collapsed()) {
              <div class="nav-group__items">
                @for (item of filterItems(NAV_ADMIN); track item.path) {
                  <a class="nav-item nav-item--indented" routerLink="{{ item.path }}"
                     routerLinkActive="nav-item--active" [style.--item-color]="'#ef5350'">
                    <mat-icon class="nav-icon">{{ item.icon }}</mat-icon>
                    <span class="nav-label">{{ item.label }}</span>
                  </a>
                }
              </div>
            }
          </div>
        }

      </div><!-- /scroll -->

      <mat-divider />

      <!-- Footer -->
      <div class="sidebar__footer" [class.sidebar__footer--mini]="collapsed()">
        @if (!collapsed()) {
          <div class="footer-user">
            <mat-icon class="footer-user__icon">person</mat-icon>
            <div class="footer-user__info">
              <div class="footer-user__name">{{ auth.user()?.full_name || auth.user()?.email }}</div>
              <div class="footer-user__role">{{ (auth.user()?.role ?? '').replace(/_/g, ' ') }}</div>
            </div>
          </div>
        }
        <div class="footer-actions">
          <button mat-icon-button (click)="theme.toggle()"
            [matTooltip]="theme.isDark() ? 'Switch to light mode' : 'Switch to dark mode'" matTooltipPosition="right">
            <mat-icon>{{ theme.isDark() ? 'light_mode' : 'dark_mode' }}</mat-icon>
          </button>
          <button mat-icon-button (click)="logout()"
            matTooltip="Log out" matTooltipPosition="right">
            <mat-icon>logout</mat-icon>
          </button>
        </div>
      </div>
    </aside>
  `,
  styles: [`
    :host { display: block; }

    .sidebar {
      display: flex;
      flex-direction: column;
      background: var(--mat-sys-surface-container-low, #1a1f2e);
      border-right: 1px solid var(--mat-sys-outline-variant, rgba(255,255,255,0.12));
      height: 100vh;
      position: fixed;
      left: 0; top: 0;
      z-index: 100;
      overflow: hidden;
      transition: width 0.2s ease;
    }

    /* Logo */
    .sidebar__logo {
      position: relative;
      padding: 20px 20px 12px;
      display: flex;
      align-items: center;
      flex-shrink: 0;
    }
    .sidebar__logo--mini { padding: 20px 0 12px; justify-content: center; }
    .sidebar__brand {
      display: flex; align-items: center; gap: 8px;
      text-decoration: none; cursor: pointer;
      &:hover { opacity: 0.8; }
    }
    .sidebar__shield { font-size: 26px; width: 26px; height: 26px; transition: color 0.2s; }
    .sidebar__title { font-size: 1rem; font-weight: 600; line-height: 1; white-space: nowrap; transition: color 0.2s; }
    .sidebar__sub { font-size: 0.6rem; color: var(--mat-sys-on-surface-variant); letter-spacing: 0.04em; white-space: nowrap; }

    .sidebar__toggle {
      position: absolute; right: -14px; top: 50%; transform: translateY(-50%);
      width: 28px; height: 28px; border-radius: 50%;
      background: var(--mat-sys-surface-container-low, #1a1f2e);
      border: 1px solid var(--mat-sys-outline-variant, rgba(255,255,255,0.18));
      box-shadow: 0 2px 6px rgba(0,0,0,0.3);
      display: flex; align-items: center; justify-content: center;
      cursor: pointer; z-index: 101;
      color: var(--mat-sys-on-surface-variant);
      transition: background 0.15s;
      &:hover { background: var(--mat-sys-surface-container, #242938); }
    }
    .sidebar__toggle mat-icon { font-size: 16px; width: 16px; height: 16px; }

    /* Scroll area */
    .sidebar__scroll {
      flex: 1; overflow-y: auto; overflow-x: hidden;
      padding: 4px 0;
      scrollbar-width: thin;
      scrollbar-color: rgba(255,255,255,0.1) transparent;
    }
    .sidebar__section { margin-bottom: 2px; }
    .sidebar__divider { margin: 6px 0 !important; }

    /* Project chip */
    .sidebar__project { padding: 0 8px 4px; }
    .project-chip {
      display: flex; align-items: center; gap: 6px;
      padding: 4px 10px; border-radius: 6px;
      border: 1px solid var(--mat-sys-outline-variant, rgba(255,255,255,0.08));
      text-decoration: none; cursor: pointer;
      &:hover { background: rgba(255,255,255,0.05); }
    }
    .project-chip__icon { font-size: 14px; width: 14px; height: 14px; color: var(--mat-sys-on-surface-variant); }
    .project-chip__name { font-size: 0.72rem; color: var(--mat-sys-on-surface-variant); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 150px; }

    /* Nav items */
    .nav-item {
      display: flex; align-items: center; gap: 10px;
      padding: 5px 12px; border-radius: 6px;
      margin: 0 4px 1px;
      text-decoration: none;
      color: var(--mat-sys-on-surface-variant);
      cursor: pointer; user-select: none;
      transition: background 0.12s, color 0.12s;
      &:hover { background: rgba(255,255,255,0.06); color: var(--mat-sys-on-surface); }
    }
    .nav-item--mini { justify-content: center; padding: 8px 0; margin: 0 4px; }
    .nav-item--indented { padding-left: 14px; }
    .nav-item--deep { padding-left: 20px; }
    .nav-item--active {
      background: color-mix(in srgb, var(--item-color, #6B7A99) 15%, transparent);
      color: var(--item-color, #6B7A99);
      font-weight: 600;
    }
    .nav-item--disabled { opacity: 0.4; cursor: default; &:hover { background: none; } }

    .nav-label { font-size: 0.8rem; white-space: nowrap; }
    .nav-icon { font-size: 18px; width: 18px; height: 18px; flex-shrink: 0; }
    .nav-icon--sm { font-size: 16px; width: 16px; height: 16px; }
    .nav-group__header .nav-icon { color: var(--group-color, var(--mat-sys-on-surface-variant)); }

    /* Nav groups */
    .nav-group__header {
      display: flex; align-items: center; gap: 8px;
      width: calc(100% - 8px); margin: 0 4px;
      padding: 5px 10px; border-radius: 6px;
      background: none; border: none;
      color: var(--mat-sys-on-surface-variant);
      cursor: pointer; user-select: none;
      transition: background 0.12s;
      &:hover { background: color-mix(in srgb, var(--group-color, #6B7A99) 8%, transparent); }
    }
    .nav-group__header--mini { justify-content: center; padding: 8px 0; width: calc(100% - 8px); }
    .nav-group__label {
      flex: 1; text-align: left;
      font-size: 0.8rem; font-weight: 500;
      letter-spacing: 0.01em;
      color: var(--mat-sys-on-surface-variant);
    }
    .nav-group__arrow {
      font-size: 14px; width: 14px; height: 14px;
      color: var(--mat-sys-on-surface-variant);
      transition: transform 0.2s;
      transform: rotate(-90deg);
    }
    .nav-group__arrow--open { transform: rotate(0deg); }
    .nav-group__items { padding-bottom: 4px; }

    /* Nav badge */
    .nav-badge {
      width: 7px; height: 7px; border-radius: 50%;
      background: #f44336; flex-shrink: 0; margin-right: 4px;
    }

    /* Region sub-groups */
    .nav-region {}
    .nav-region__header {
      display: flex; align-items: center; gap: 4px;
      width: 100%; padding: 3px 14px 3px 20px;
      background: none; border: none;
      color: var(--mat-sys-on-surface-variant);
      font-size: 0.6rem; font-weight: 500;
      text-transform: uppercase; letter-spacing: 0.06em;
      cursor: pointer;
      &:hover { color: var(--mat-sys-on-surface); }
    }
    .nav-region__arrow {
      font-size: 11px; width: 11px; height: 11px;
      transition: transform 0.15s;
      transform: rotate(-90deg);
    }
    .nav-region__arrow--open { transform: rotate(0deg); }

    /* Footer */
    .sidebar__footer {
      padding: 8px 8px;
      display: flex; align-items: center; flex-shrink: 0;
      gap: 4px;
    }
    .sidebar__footer--mini { justify-content: center; flex-direction: column; }
    .footer-user {
      display: flex; align-items: center; gap: 8px; flex: 1; min-width: 0;
    }
    .footer-user__icon { font-size: 18px; width: 18px; height: 18px; color: var(--mat-sys-on-surface-variant); }
    .footer-user__info { min-width: 0; }
    .footer-user__name {
      font-size: 0.75rem; font-weight: 500;
      color: var(--mat-sys-on-surface);
      white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 120px;
    }
    .footer-user__role { font-size: 0.65rem; color: var(--mat-sys-on-surface-variant); text-transform: capitalize; }
    .footer-actions { display: flex; align-items: center; flex-shrink: 0; }
  `],
})
export class SidebarComponent implements OnInit {
  auth = inject(AuthService)
  theme = inject(ThemeService)
  product = inject(ProductService)
  project = inject(ProjectService)
  private router = inject(Router)
  private http = inject(HttpClient)

  readonly FULL = SIDEBAR_WIDTH
  readonly MINI = SIDEBAR_MINI_WIDTH
  readonly PRODUCT_SECTIONS = PRODUCT_SECTIONS
  readonly NAV_RISK = NAV_RISK
  readonly NAV_TOOLS = NAV_TOOLS
  readonly NAV_FRAMEWORK_REGIONS = NAV_FRAMEWORK_REGIONS
  readonly NAV_SUPPLIERS = NAV_SUPPLIERS
  readonly NAV_ADMIN = NAV_ADMIN

  collapsedChange = output<boolean>()
  collapsed = signal(localStorage.getItem('sidebarCollapsed') === 'true')
  expandedProduct = signal<Product | null>(null)
  riskOpen = signal(false)
  toolsOpen = signal(false)
  frameworksOpen = signal(false)
  suppliersOpen = signal(false)
  adminOpen = signal(false)
  intelOpen = signal(false)
  openRegions = signal<Set<string>>(new Set(['Global']))

  private currentPath = signal(this.router.url)

  private healthQuery = injectQuery(() => ({
    queryKey: ['health', 'alerts'],
    queryFn: () => firstValueFrom(this.http.get<{ type: string }[]>('/api/v1/health/alerts')),
    staleTime: 5 * 60_000,
    refetchInterval: 5 * 60_000,
    enabled: !!this.auth.user(),
  }))

  hasIntelAlert = computed(() => (this.healthQuery.data() ?? []).some(a => a.type === 'feed_failure'))

  allIntelItems = computed(() => [...NAV_INTELLIGENCE, ...NAV_TI_ITEMS])

  productColor = computed(() => PRODUCT_COLORS[this.product.product()])

  activeProjectName = computed(() => {
    const p = this.project.getActiveProject(this.product.product().toUpperCase())
    return p?.name ?? 'No active project'
  })

  ngOnInit() {
    this.router.events.pipe(filter(e => e instanceof NavigationEnd)).subscribe((e: any) => {
      this.currentPath.set(e.urlAfterRedirects)
      this._autoOpenSections(e.urlAfterRedirects)
    })
    this._autoOpenSections(this.router.url)
  }

  private _autoOpenSections(path: string) {
    if (RISK_PATHS.some(p => path.startsWith(p))) this.riskOpen.set(true)
    if (TOOLS_PATHS.some(p => path.startsWith(p))) this.toolsOpen.set(true)
    if (FRAMEWORK_PATHS.some(p => path.startsWith(p))) this.frameworksOpen.set(true)
    if (SUPPLIER_PATHS.some(p => path.startsWith(p))) this.suppliersOpen.set(true)
    if (ADMIN_PATHS.some(p => path.startsWith(p))) this.adminOpen.set(true)
    if (INTELLIGENCE_PATHS.some(p => path.startsWith(p))) this.intelOpen.set(true)
  }

  getProductColor(p: Product) { return PRODUCT_COLORS[p] }
  getProductLabel(p: Product) { return PRODUCT_LABELS[p] }

  getProductNav(p: Product): NavItem[] {
    const role = this.auth.user()?.role ?? ''
    const isSuperAdmin = this.auth.isSuperAdmin()
    return PRODUCT_NAV.filter(item => this._visibleFor(item, role, isSuperAdmin))
  }

  filterItems(items: NavItem[]): NavItem[] {
    const role = this.auth.user()?.role ?? ''
    const isSuperAdmin = this.auth.isSuperAdmin()
    return items.filter(item => this._visibleFor(item, role, isSuperAdmin))
  }

  private _visibleFor(item: NavItem, role: string, isSuperAdmin: boolean): boolean {
    if (item.superAdminOnly) return isSuperAdmin
    if (item.adminOnly)      return ADMIN_ROLES.has(role)
    if (item.managerAndAbove) return MANAGER_ROLES.has(role)
    if (item.notViewer)      return NON_VIEWER_ROLES.has(role)
    return true
  }

  isProductActive(path: string, p: Product): boolean {
    const cur = this.currentPath()
    const pathMatch = cur === path || (path !== '/overview' && cur.startsWith(path))
    return pathMatch && this.product.product() === p
  }

  toggleProduct(p: Product) {
    if (this.collapsed()) {
      this.product.setProduct(p)
      this.expandedProduct.set(p)
      this.router.navigate(['/overview'])
      return
    }
    if (this.expandedProduct() === p) {
      this.expandedProduct.set(null)
    } else {
      this.expandedProduct.set(p)
      this.product.setProduct(p)
    }
  }

  navigateProduct(path: string, p: Product) {
    this.product.setProduct(p)
    this.expandedProduct.set(p)
    this.router.navigate([path])
  }

  toggleRegion(label: string) {
    this.openRegions.update(prev => {
      const next = new Set(prev)
      next.has(label) ? next.delete(label) : next.add(label)
      return next
    })
  }

  toggleCollapse() {
    const next = !this.collapsed()
    this.collapsed.set(next)
    localStorage.setItem('sidebarCollapsed', String(next))
    this.collapsedChange.emit(next)
  }

  logout() { this.auth.logout() }
}
