import { Component, signal, computed, inject } from '@angular/core'
import { RouterOutlet, Router } from '@angular/router'
import { injectQuery } from '@tanstack/angular-query-experimental'
import { HttpClient } from '@angular/common/http'
import { firstValueFrom } from 'rxjs'
import { MatIconModule } from '@angular/material/icon'
import { MatButtonModule } from '@angular/material/button'
import { MatCardModule } from '@angular/material/card'
import { AuthService } from '../core/services/auth.service'
import { AuthApiService } from '../api/auth-api.service'
import { TokenStoreService } from '../core/services/token-store.service'
import { SidebarComponent, SIDEBAR_WIDTH, SIDEBAR_MINI_WIDTH } from './sidebar/sidebar.component'
import { HealthAlertBannerComponent } from '../shared/components/health-alert-banner.component'

@Component({
  selector: 'app-layout',
  standalone: true,
  imports: [RouterOutlet, MatIconModule, MatButtonModule, MatCardModule, SidebarComponent, HealthAlertBannerComponent],
  template: `
    <div class="layout">
      <app-sidebar (collapsedChange)="onCollapsedChange($event)" />

      <main class="layout__main" [style.margin-left.px]="mainMargin()">
        <!-- MFA enforcement screen -->
        @if (showEnforcement()) {
          <div class="layout__enforcement">
            <mat-card class="enforcement-card">
              <mat-card-content>
                <mat-icon class="enforcement-card__icon">lock</mat-icon>
                <h2>Two-factor authentication required</h2>
                <p>Your organisation requires all accounts to be protected with two-factor authentication before accessing the platform.</p>
                <button mat-flat-button color="primary" (click)="router.navigate(['/system'])">
                  Set up two-factor authentication
                </button>
              </mat-card-content>
            </mat-card>
          </div>
        } @else {
          <!-- MFA nudge banner -->
          @if (showMfaBanner()) {
            <div class="mfa-banner">
              <span>Your account is not protected with two-factor authentication.</span>
              <button mat-button color="primary" size="small" (click)="router.navigate(['/system'])">Set up now</button>
              <button mat-icon-button (click)="dismissMfaBanner()"><mat-icon>close</mat-icon></button>
            </div>
          }

          <app-health-alert-banner />

          <div class="layout__content">
            <router-outlet />
          </div>
        }
      </main>
    </div>
  `,
  styles: [`
    .layout {
      display: flex;
      height: 100vh;
      overflow: hidden;
      background: var(--mat-sys-surface);
    }

    .layout__main {
      flex: 1;
      min-width: 0;
      height: 100%;
      display: flex;
      flex-direction: column;
      transition: margin-left 0.2s ease;
      overflow: hidden;
    }

    .layout__content {
      flex: 1;
      overflow-y: auto;
      padding: 24px 24px 48px;
    }

    .layout__enforcement {
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }

    .enforcement-card {
      max-width: 440px;
      width: 100%;
      text-align: center;
    }
    mat-card-content {
      padding: 32px !important;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 16px;
    }
    .enforcement-card__icon {
      font-size: 48px; width: 48px; height: 48px;
      color: var(--mat-sys-error);
    }
    .enforcement-card h2 { margin: 0; font-size: 1.25rem; }
    .enforcement-card p { margin: 0; color: var(--mat-sys-on-surface-variant); font-size: 0.875rem; }

    .mfa-banner {
      display: flex; align-items: center; gap: 8px;
      padding: 6px 16px;
      background: var(--mat-sys-warning-container, #3d3200);
      color: var(--mat-sys-on-warning-container, #FFEB9C);
      font-size: 0.875rem;
      flex-shrink: 0;
    }
    .mfa-banner span { flex: 1; }
  `],
})
export class LayoutComponent {
  auth = inject(AuthService)
  router = inject(Router)
  private http = inject(HttpClient)
  private authApi = inject(AuthApiService)
  private tokenStore = inject(TokenStoreService)

  sidebarCollapsed = signal(localStorage.getItem('sidebarCollapsed') === 'true')
  mfaBannerDismissed = signal(sessionStorage.getItem('mfa_banner_dismissed') === 'true')

  mainMargin = computed(() => this.sidebarCollapsed() ? SIDEBAR_MINI_WIDTH : SIDEBAR_WIDTH)

  private mfaQuery = injectQuery(() => ({
    queryKey: ['mfa-status'],
    queryFn: () => this.authApi.getMfaStatus(this.tokenStore.get() ?? ''),
    enabled: !!this.auth.user(),
    staleTime: 5 * 60_000,
  }))

  private orgQuery = injectQuery(() => ({
    queryKey: ['organisation'],
    queryFn: () => firstValueFrom(this.http.get<{ settings: Record<string, unknown> }>('/api/v1/organisation/')),
    enabled: !!this.auth.user(),
    staleTime: 5 * 60_000,
  }))

  mfaEnforced = computed(() => Boolean(this.orgQuery.data()?.settings?.['mfa_required']))
  mfaEnabled = computed(() => this.mfaQuery.data()?.mfa_enabled ?? true)

  showEnforcement = computed(() => {
    if (!this.mfaEnforced()) return false
    if (this.mfaQuery.data() === undefined) return false
    if (this.mfaEnabled()) return false
    return !this.router.url.startsWith('/system')
  })

  showMfaBanner = computed(() => {
    if (this.mfaEnforced()) return false
    if (this.mfaBannerDismissed()) return false
    if (this.mfaQuery.data() === undefined) return false
    return !this.mfaEnabled()
  })

  onCollapsedChange(collapsed: boolean) {
    this.sidebarCollapsed.set(collapsed)
  }

  dismissMfaBanner() {
    sessionStorage.setItem('mfa_banner_dismissed', 'true')
    this.mfaBannerDismissed.set(true)
  }
}
