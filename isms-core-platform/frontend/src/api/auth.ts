import axios from 'axios'
import type { LoginRequest, TokenResponse } from './types'

export interface MfaLoginResponse {
  mfa_required: true
  mfa_token: string
}

export type LoginResponse = TokenResponse | MfaLoginResponse

export function isMfaRequired(r: LoginResponse): r is MfaLoginResponse {
  return (r as MfaLoginResponse).mfa_required === true
}

export async function login(data: LoginRequest): Promise<LoginResponse> {
  const res = await axios.post<LoginResponse>('/api/v1/auth/login', data)
  return res.data
}

// Decode JWT payload (no signature verification — client-side only)
export function decodeJwtPayload(token: string): Record<string, unknown> {
  try {
    const payload = token.split('.')[1]
    const decoded = atob(payload.replace(/-/g, '+').replace(/_/g, '/'))
    return JSON.parse(decoded)
  } catch {
    return {}
  }
}

// Complete MFA login step
export async function verifyMfa(mfa_token: string, code: string): Promise<TokenResponse> {
  const res = await fetch('/api/v1/auth/mfa/verify', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ mfa_token, code }),
  })
  if (!res.ok) {
    const err = await res.json().catch(() => ({}))
    throw new Error(err.detail ?? 'Invalid MFA code')
  }
  return res.json()
}

// MFA setup — get QR code
export async function mfaSetup(token: string): Promise<{ secret: string; otpauth_uri: string; qr_data_uri: string }> {
  const res = await fetch('/api/v1/auth/mfa/setup', {
    method: 'POST',
    headers: { Authorization: `Bearer ${token}` },
  })
  if (!res.ok) throw new Error('Setup failed')
  return res.json()
}

// Enable MFA after confirming TOTP code
export async function mfaEnable(token: string, code: string): Promise<{ backup_codes: string[] }> {
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

// Disable MFA
export async function mfaDisable(token: string, code: string): Promise<void> {
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

// Regenerate backup codes
export async function mfaRegenerateBackupCodes(token: string, code: string): Promise<{ backup_codes: string[] }> {
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

// Get MFA status for the current user
export async function getMfaStatus(token: string): Promise<{ mfa_enabled: boolean; has_backup_codes: boolean }> {
  const res = await fetch('/api/v1/auth/mfa/status', {
    headers: { Authorization: `Bearer ${token}` },
  })
  if (!res.ok) throw new Error('Failed to fetch MFA status')
  return res.json()
}
