import { Injectable, inject, signal, computed } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { firstValueFrom } from 'rxjs'
import { TokenStoreService } from './token-store.service'
import { UserInfo } from '../../shared/types'

interface TokenResponse { access_token: string; token_type: string }
interface MfaLoginResponse { mfa_required: true; mfa_token: string }
type LoginResponse = TokenResponse | MfaLoginResponse

function isMfaRequired(r: LoginResponse): r is MfaLoginResponse {
  return (r as MfaLoginResponse).mfa_required === true
}

function decodeJwtPayload(token: string): Record<string, unknown> {
  try {
    const payload = token.split('.')[1]
    const decoded = atob(payload.replace(/-/g, '+').replace(/_/g, '/'))
    return JSON.parse(decoded)
  } catch { return {} }
}

function userFromToken(token: string): UserInfo {
  const p = decodeJwtPayload(token)
  return {
    id: String(p['sub'] ?? ''),
    email: String(p['email'] ?? ''),
    full_name: null,
    role: String(p['role'] ?? 'viewer'),
    is_active: true,
    organisation_id: String(p['org_id'] ?? ''),
    active_projects: {},
  }
}

@Injectable({ providedIn: 'root' })
export class AuthService {
  private http       = inject(HttpClient)
  private tokenStore = inject(TokenStoreService)

  readonly user            = signal<UserInfo | null>(null)
  readonly isAuthenticated = computed(() => !!this.tokenStore.get())
  readonly isSuperAdmin    = computed(() => this.user()?.role === 'super_admin')

  private _initPromise: Promise<void> | null = null

  init(): Promise<void> {
    if (!this._initPromise) this._initPromise = this._doInit()
    return this._initPromise
  }

  resetInit(): void {
    this._initPromise = null
  }

  private async _doInit(): Promise<void> {
    try {
      const res = await firstValueFrom(
        this.http.post<TokenResponse>('/api/v1/auth/refresh', {}, { withCredentials: true })
      )
      this.tokenStore.set(res.access_token)
      this.user.set(userFromToken(res.access_token))
    } catch {
      // No valid cookie — user must log in
    }
  }

  async login(email: string, password: string): Promise<void> {
    const res = await firstValueFrom(
      this.http.post<LoginResponse>('/api/v1/auth/login', { email, password }, { withCredentials: true })
    )
    if (isMfaRequired(res)) {
      throw { mfa_required: true, mfa_token: res.mfa_token }
    }
    this.tokenStore.set((res as TokenResponse).access_token)
    this.user.set(userFromToken((res as TokenResponse).access_token))
  }

  async loginMfa(mfaToken: string, code: string): Promise<void> {
    const res = await firstValueFrom(
      this.http.post<TokenResponse>('/api/v1/auth/mfa/verify', { mfa_token: mfaToken, code }, { withCredentials: true })
    )
    this.tokenStore.set(res.access_token)
    this.user.set(userFromToken(res.access_token))
  }

  logout(): void {
    this.http.post('/api/v1/auth/logout', {}, { withCredentials: true }).subscribe()
    this.tokenStore.set(null)
    this.user.set(null)
    this._initPromise = null          // reset so next login gets a fresh guard init
    window.location.href = '/login'   // full reload — consistent with interceptor, clears all state
  }
}
