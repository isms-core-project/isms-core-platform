import { Injectable } from '@angular/core'
import { TokenStoreService } from '../core/services/token-store.service'

export interface LoginRequest {
  username: string
  password: string
}

export interface TokenResponse {
  access_token: string
  token_type: string
}

export interface MfaLoginResponse {
  mfa_required: true
  mfa_token: string
}

export type LoginResponse = TokenResponse | MfaLoginResponse

export function isMfaRequired(r: LoginResponse): r is MfaLoginResponse {
  return (r as MfaLoginResponse).mfa_required === true
}

@Injectable({ providedIn: 'root' })
export class AuthApiService {
  async login(data: LoginRequest): Promise<LoginResponse> {
    const res = await fetch('/api/v1/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
      body: JSON.stringify(data),
    })
    if (!res.ok) {
      const err = await res.json().catch(() => ({}))
      throw new Error(err.detail ?? `HTTP ${res.status}`)
    }
    return res.json()
  }

  async silentRefresh(): Promise<TokenResponse | null> {
    try {
      const res = await fetch('/api/v1/auth/refresh', {
        method: 'POST',
        credentials: 'include',
      })
      if (!res.ok) return null
      return res.json()
    } catch {
      return null
    }
  }

  async logout(): Promise<void> {
    await fetch('/api/v1/auth/logout', { method: 'POST', credentials: 'include' }).catch(() => {})
  }

  async verifyMfa(mfa_token: string, code: string): Promise<TokenResponse> {
    const res = await fetch('/api/v1/auth/mfa/verify', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
      body: JSON.stringify({ mfa_token, code }),
    })
    if (!res.ok) {
      const err = await res.json().catch(() => ({}))
      throw new Error(err.detail ?? 'Invalid MFA code')
    }
    return res.json()
  }

  async mfaSetup(token: string): Promise<{ secret: string; otpauth_uri: string; qr_data_uri: string }> {
    const res = await fetch('/api/v1/auth/mfa/setup', {
      method: 'POST',
      headers: { Authorization: `Bearer ${token}` },
    })
    if (!res.ok) throw new Error('Setup failed')
    return res.json()
  }

  async mfaEnable(token: string, code: string): Promise<{ backup_codes: string[] }> {
    const res = await fetch('/api/v1/auth/mfa/enable', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
      body: JSON.stringify({ code }),
    })
    if (!res.ok) {
      const err = await res.json().catch(() => ({}))
      throw new Error(err.detail ?? 'Enable failed')
    }
    return res.json()
  }

  async mfaDisable(token: string, code: string): Promise<void> {
    const res = await fetch('/api/v1/auth/mfa/disable', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
      body: JSON.stringify({ code }),
    })
    if (!res.ok) {
      const err = await res.json().catch(() => ({}))
      throw new Error(err.detail ?? 'Disable failed')
    }
  }

  async mfaRegenerateBackupCodes(token: string, code: string): Promise<{ backup_codes: string[] }> {
    const res = await fetch('/api/v1/auth/mfa/backup-codes/regenerate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
      body: JSON.stringify({ code }),
    })
    if (!res.ok) {
      const err = await res.json().catch(() => ({}))
      throw new Error(err.detail ?? 'Regeneration failed')
    }
    return res.json()
  }

  async getMfaStatus(token: string): Promise<{ mfa_enabled: boolean; has_backup_codes: boolean }> {
    const res = await fetch('/api/v1/auth/mfa/status', {
      headers: { Authorization: `Bearer ${token}` },
    })
    if (!res.ok) throw new Error('Failed to fetch MFA status')
    return res.json()
  }

  decodeJwtPayload(token: string): Record<string, unknown> {
    try {
      const payload = token.split('.')[1]
      const decoded = atob(payload.replace(/-/g, '+').replace(/_/g, '/'))
      return JSON.parse(decoded)
    } catch {
      return {}
    }
  }
}
