import { createContext, useContext, useState, useCallback, type ReactNode } from 'react'
import type { UserInfo } from '../api/types'
import { login as apiLogin, decodeJwtPayload } from '../api/auth'

interface AuthState {
  user: UserInfo | null
  token: string | null
}

interface AuthContextValue extends AuthState {
  login: (email: string, password: string) => Promise<void>
  logout: () => void
  isAuthenticated: boolean
}

const AuthContext = createContext<AuthContextValue | null>(null)

function loadStoredAuth(): AuthState {
  try {
    const token = localStorage.getItem('access_token')
    const userJson = localStorage.getItem('user')
    if (token && userJson) {
      return { token, user: JSON.parse(userJson) }
    }
  } catch {
    // ignore
  }
  return { token: null, user: null }
}

function userFromToken(token: string): UserInfo {
  const payload = decodeJwtPayload(token)
  return {
    id: String(payload.sub ?? ''),
    email: String(payload.email ?? ''),
    full_name: null,
    role: String(payload.role ?? 'viewer'),
    is_active: true,
  }
}

export function AuthProvider({ children }: { children: ReactNode }) {
  const [auth, setAuth] = useState<AuthState>(loadStoredAuth)

  const login = useCallback(async (email: string, password: string) => {
    const response = await apiLogin({ email, password })
    const user = userFromToken(response.access_token)
    localStorage.setItem('access_token', response.access_token)
    localStorage.setItem('refresh_token', response.refresh_token)
    localStorage.setItem('user', JSON.stringify(user))
    setAuth({ token: response.access_token, user })
  }, [])

  const logout = useCallback(() => {
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    localStorage.removeItem('user')
    setAuth({ token: null, user: null })
  }, [])

  return (
    <AuthContext.Provider
      value={{ ...auth, login, logout, isAuthenticated: !!auth.token }}
    >
      {children}
    </AuthContext.Provider>
  )
}

export function useAuth(): AuthContextValue {
  const ctx = useContext(AuthContext)
  if (!ctx) throw new Error('useAuth must be used inside AuthProvider')
  return ctx
}
