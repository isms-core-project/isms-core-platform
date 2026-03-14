import axios from 'axios'
import type { LoginRequest, TokenResponse } from './types'

export async function login(data: LoginRequest): Promise<TokenResponse> {
  const res = await axios.post<TokenResponse>('/api/v1/auth/login', data)
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
