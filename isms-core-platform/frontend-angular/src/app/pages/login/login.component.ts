import { Component, inject, signal, computed } from '@angular/core'
import { ReactiveFormsModule, FormsModule, FormBuilder, Validators } from '@angular/forms'
import { Router } from '@angular/router'

import { MatCardModule } from '@angular/material/card'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatButtonModule } from '@angular/material/button'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatIconModule } from '@angular/material/icon'
import { MatTooltipModule } from '@angular/material/tooltip'

import { AuthService } from '../../core/services/auth.service'
import { ThemeService } from '../../core/services/theme.service'

type Step = 'credentials' | 'mfa'

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [
    ReactiveFormsModule, FormsModule,
    MatCardModule, MatFormFieldModule, MatInputModule,
    MatButtonModule, MatProgressSpinnerModule, MatIconModule, MatTooltipModule,
  ],
  template: `
<div class="login-bg" [class.login-bg--dark]="isDark()" [class.login-bg--light]="!isDark()">

  <!-- Theme toggle -->
  <div class="theme-toggle">
    <button mat-icon-button [matTooltip]="isDark() ? 'Switch to light mode' : 'Switch to dark mode'"
      (click)="toggleTheme()">
      <mat-icon>{{ isDark() ? 'light_mode' : 'dark_mode' }}</mat-icon>
    </button>
  </div>

  <div class="login-wrap">
    <mat-card class="login-card" [class.login-card--dark]="isDark()">
      <mat-card-content class="login-card-content">

        <!-- Header -->
        <div class="brand">
          <mat-icon class="brand-icon" color="primary">shield</mat-icon>
          <div>
            <div class="brand-name-row">
              <span class="brand-name">ISMS CORE</span>
              <span class="brand-version">v1.0</span>
            </div>
            <div class="brand-subtitle">Information Security &amp; Privacy Compliance</div>
          </div>
        </div>

        <!-- Step: credentials -->
        @if (step() === 'credentials') {
          <h2 class="form-title">Sign in</h2>
          <p class="form-subtitle">Enter your credentials to access the platform.</p>

          @if (error()) {
            <div class="alert alert--error">{{ error() }}</div>
          }

          <form [formGroup]="credForm" (ngSubmit)="submitCredentials()" novalidate>
            <mat-form-field appearance="outline" class="field-full">
              <mat-label>Email</mat-label>
              <input matInput type="email" formControlName="email" autocomplete="email" />
            </mat-form-field>

            <mat-form-field appearance="outline" class="field-full">
              <mat-label>Password</mat-label>
              <input matInput [type]="showPassword() ? 'text' : 'password'"
                formControlName="password" autocomplete="current-password" />
              <button mat-icon-button matSuffix type="button" (click)="showPassword.set(!showPassword())">
                <mat-icon>{{ showPassword() ? 'visibility_off' : 'visibility' }}</mat-icon>
              </button>
            </mat-form-field>

            <!-- Forgot password -->
            <div class="forgot-row">
              @if (forgotSent()) {
                <span class="forgot-msg">Contact your administrator to reset your password.</span>
              } @else {
                <button mat-button type="button" class="forgot-btn" (click)="forgotSent.set(true)">
                  Forgot password?
                </button>
              }
            </div>

            <button mat-raised-button color="primary" type="submit" class="submit-btn"
              [disabled]="loading() || credForm.invalid">
              @if (loading()) { <mat-spinner diameter="20" /> } @else { Sign in }
            </button>
          </form>
        }

        <!-- Step: MFA -->
        @if (step() === 'mfa') {
          <div class="mfa-header">
            <mat-icon class="mfa-icon" color="primary">lock</mat-icon>
            <h2 class="form-title mfa-title">Two-factor authentication</h2>
            <p class="form-subtitle mfa-subtitle">
              Enter the 6-digit code from your authenticator app, or a backup code (XXXX-XXXX).
            </p>
          </div>

          @if (error()) {
            <div class="alert alert--error">{{ error() }}</div>
          }

          <mat-form-field appearance="outline" class="field-full mfa-field">
            <mat-label>Authentication code</mat-label>
            <input matInput #mfaInput
              [value]="mfaCode()"
              (input)="onMfaInput($event)"
              maxlength="9"
              autocomplete="one-time-code"
              class="mfa-code-input" />
          </mat-form-field>

          <button mat-raised-button color="primary" class="submit-btn"
            [disabled]="loading() || mfaCode().length < 6"
            (click)="submitMfa()">
            @if (loading()) { <mat-spinner diameter="20" /> } @else { Sign in }
          </button>

          <div class="back-row">
            <button mat-button class="back-btn" (click)="goBack()">
              <mat-icon class="back-icon">arrow_back</mat-icon>
              Back
            </button>
          </div>
        }

      </mat-card-content>
    </mat-card>

    <p class="footer">© 2026 ISMS CORE · ISO 27001:2022 Compliance Platform</p>
  </div>

</div>
  `,
  styles: [`
    /* Background */
    .login-bg {
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 16px;
      position: relative;
    }
    .login-bg--dark {
      background: #1d1d1d;
    }
    .login-bg--light {
      background: #D3D1C7;
    }

    /* Theme toggle */
    .theme-toggle {
      position: fixed;
      top: 16px;
      right: 16px;
    }

    /* Card container */
    .login-wrap {
      width: 100%;
      max-width: 400px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    mat-card.login-card {
      width: 100%;
      border-radius: 12px !important;
      border-top: 3px solid var(--mat-sys-primary);
      box-shadow: 0 8px 32px rgba(44,44,42,0.15) !important;
    }
    .login-card mat-card-content.login-card-content { padding: 32px !important; }
    mat-card.login-card--dark {
      box-shadow: 0 8px 32px rgba(0,0,0,0.4) !important;
    }

    /* Brand header */
    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 32px;
    }
    .brand-icon { font-size: 36px; width: 36px; height: 36px; }
    .brand-name-row {
      display: flex;
      align-items: baseline;
      gap: 8px;
    }
    .brand-name {
      font-size: 1.25rem;
      font-weight: 600;
      color: var(--mat-sys-on-surface);
      line-height: 1;
    }
    .brand-version {
      font-size: 0.65rem;
      font-weight: 600;
      color: var(--mat-sys-primary);
      letter-spacing: 0.05em;
    }
    .brand-subtitle {
      font-size: 0.75rem;
      color: var(--mat-sys-on-surface-variant);
    }

    /* Form */
    .form-title {
      font-size: 1.125rem;
      font-weight: 500;
      margin: 0 0 4px;
      color: var(--mat-sys-on-surface);
    }
    .form-subtitle {
      font-size: 0.875rem;
      color: var(--mat-sys-on-surface-variant);
      margin-bottom: 20px;
    }

    .field-full { width: 100%; display: block; margin-bottom: 8px; }

    .forgot-row {
      display: flex;
      justify-content: flex-end;
      margin-bottom: 20px;
    }
    .forgot-btn {
      font-size: 0.75rem;
      color: var(--mat-sys-on-surface-variant);
      padding: 0;
      min-width: 0;
      text-transform: none;
    }
    .forgot-msg {
      font-size: 0.75rem;
      color: var(--mat-sys-on-surface-variant);
    }

    .submit-btn {
      width: 100%;
      padding: 8px 0;
      font-size: 0.95rem;
    }

    /* MFA step overrides */
    .mfa-title { margin: 0 0 4px; }
    .mfa-subtitle { text-align: center; }
    .mfa-field { margin-bottom: 24px; }
    .mfa-code-input { letter-spacing: 0.3em; text-align: center; font-size: 1.4rem; }
    .back-icon { font-size: 16px; margin-right: 4px; }

    /* MFA */
    .mfa-header {
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-bottom: 20px;
    }
    .mfa-icon {
      font-size: 40px;
      width: 40px;
      height: 40px;
      margin-bottom: 12px;
    }

    .back-row {
      display: flex;
      justify-content: center;
      margin-top: 12px;
    }
    .back-btn {
      font-size: 0.75rem;
      color: var(--mat-sys-on-surface-variant);
    }

    /* Alert */
    .alert {
      padding: 10px 14px;
      border-radius: 6px;
      font-size: 0.875rem;
      margin-bottom: 16px;
    }
    .alert--error { background: rgba(192,0,0,0.12); color: #9e0000; }

    /* Footer */
    .footer {
      margin-top: 20px;
      font-size: 0.72rem;
      color: var(--mat-sys-on-surface-variant);
      opacity: 0.6;
      text-align: center;
    }
  `],
})
export class LoginComponent {
  private auth   = inject(AuthService)
  private router = inject(Router)
  private fb     = inject(FormBuilder)
  private theme  = inject(ThemeService)

  readonly isDark = computed(() => this.theme.isDark())

  // Form state
  credForm = this.fb.nonNullable.group({
    email:    ['', [Validators.required, Validators.email]],
    password: ['', Validators.required],
  })

  step        = signal<Step>('credentials')
  loading     = signal(false)
  error       = signal<string | null>(null)
  showPassword = signal(false)
  forgotSent  = signal(false)
  mfaToken    = signal('')
  mfaCode     = signal('')

  // Synchronous guard — signals are reactive but DOM disabled update lags one
  // change-detection cycle, so rapid double-taps on mobile bypass loading().
  private _inFlight = false

  toggleTheme() { this.theme.toggle() }

  // ── Step 1: email + password ─────────────────────────────────────────────────

  async submitCredentials() {
    if (this.credForm.invalid || this._inFlight) return
    this._inFlight = true
    this.error.set(null)
    this.loading.set(true)
    const { email, password } = this.credForm.getRawValue()
    try {
      await this.auth.login(email, password)
      const ok = await this.router.navigate(['/'])
      // If Angular router fails to navigate (NavigationCancel/NavigationError),
      // fall back to a full page reload which reliably triggers a clean auth cycle.
      if (!ok) window.location.href = '/'
    } catch (err: unknown) {
      this.loading.set(false)
      const e = err as { mfa_required?: boolean; mfa_token?: string }
      if (e?.mfa_required) {
        this.mfaToken.set(e.mfa_token ?? '')
        this.mfaCode.set('')
        this.step.set('mfa')
      } else {
        this.error.set('Invalid credentials. Please try again.')
      }
    } finally {
      this._inFlight = false
    }
  }

  // ── Step 2: MFA code ─────────────────────────────────────────────────────────

  onMfaInput(event: Event) {
    const raw = (event.target as HTMLInputElement).value
    const stripped = raw.replace(/[^a-zA-Z0-9]/g, '').toUpperCase()
    // Format: 6 digits TOTP or XXXX-XXXX backup code
    let formatted = stripped
    if (stripped.length > 6) {
      formatted = stripped.slice(0, 4) + (stripped.length > 4 ? '-' + stripped.slice(4, 8) : '')
    }
    this.mfaCode.set(formatted)
    // Auto-submit on 6 digits
    if (/^\d{6}$/.test(stripped)) {
      this.doMfaSubmit(stripped)
    }
  }

  submitMfa() {
    const stripped = this.mfaCode().replace(/[^a-zA-Z0-9]/g, '').toUpperCase()
    this.doMfaSubmit(stripped)
  }

  private async doMfaSubmit(code: string) {
    if (!code || this._inFlight) return
    this._inFlight = true
    this.error.set(null)
    this.loading.set(true)
    try {
      await this.auth.loginMfa(this.mfaToken(), code)
      const ok = await this.router.navigate(['/'])
      if (!ok) window.location.href = '/'
    } catch (err: unknown) {
      const e = err as Error
      this.error.set(e?.message ?? 'Invalid authentication code. Please try again.')
    } finally {
      this.loading.set(false)
      this._inFlight = false
    }
  }

  goBack() {
    this.step.set('credentials')
    this.mfaCode.set('')
    this.error.set(null)
  }
}
