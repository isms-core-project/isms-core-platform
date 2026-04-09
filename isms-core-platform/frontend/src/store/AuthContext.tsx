import { createContext, useContext, useState, useCallback, useEffect, type ReactNode } from 'react'
import type { UserInfo } from '../api/types'
import { login as apiLogin, verifyMfa, isMfaRequired, decodeJwtPayload, silentRefresh, logoutApi } from '../api/auth'
import { tokenStore } from '../api/tokenStore'

interface AuthState {
  user: UserInfo | null
  token: string | null
}

interface AuthContextValue extends AuthState {
  login: (email: string, password: string) => Promise<void>
  loginMfa: (mfaToken: string, code: string) => Promise<void>
  logout: () => void
  isAuthenticated: boolean
  isSuperAdmin: boolean
  isLoading: boolean
}

const AuthContext = createContext<AuthContextValue | null>(null)

function userFromToken(token: string): UserInfo {
  const payload = decodeJwtPayload(token)
  return {
    id: String(payload.sub ?? ''),
    email: String(payload.email ?? ''),
    full_name: null,
    role: String(payload.role ?? 'viewer'),
    is_active: true,
    organisation_id: String(payload.org_id ?? ''),
    active_projects: {},
  }
}

export function AuthProvider({ children }: { children: ReactNode }) {
  const [auth, setAuth] = useState<AuthState>({ token: null, user: null })
  const [isLoading, setIsLoading] = useState(true)

  // On mount: try to rehydrate from the HttpOnly refresh cookie
  useEffect(() => {
    silentRefresh()
      .then((res) => {
        if (res) {
          const user = userFromToken(res.access_token)
          tokenStore.set(res.access_token)
          setAuth({ token: res.access_token, user })
        }
      })
      .finally(() => setIsLoading(false))
  }, [])

  const login = useCallback(async (email: string, password: string) => {
    const response = await apiLogin({ email, password })
    if (isMfaRequired(response)) {
      throw { mfa_required: true, mfa_token: response.mfa_token }
    }
    const user = userFromToken(response.access_token)
    tokenStore.set(response.access_token)
    setAuth({ token: response.access_token, user })
  }, [])

  const loginMfa = useCallback(async (mfaToken: string, code: string) => {
    const response = await verifyMfa(mfaToken, code)
    const user = userFromToken(response.access_token)
    tokenStore.set(response.access_token)
    setAuth({ token: response.access_token, user })
  }, [])

  const logout = useCallback(() => {
    logoutApi()
    tokenStore.set(null)
    setAuth({ token: null, user: null })
  }, [])

  const isSuperAdmin = auth.user?.role === 'super_admin'

  return (
    <AuthContext.Provider
      value={{ ...auth, login, loginMfa, logout, isAuthenticated: !!auth.token, isSuperAdmin, isLoading }}
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
