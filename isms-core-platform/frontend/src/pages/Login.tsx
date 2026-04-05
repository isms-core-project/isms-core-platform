import { useState, useRef, type FormEvent } from 'react'
import { useNavigate } from 'react-router-dom'
import {
  Box,
  Card,
  CardContent,
  TextField,
  Button,
  Typography,
  Alert,
  CircularProgress,
  InputAdornment,
  IconButton,
  Tooltip,
} from '@mui/material'
import {
  ShieldOutlined,
  VisibilityOutlined,
  VisibilityOffOutlined,
  LockOutlined,
  ArrowBackOutlined,
  DarkModeOutlined,
  LightModeOutlined,
} from '@mui/icons-material'
import { useAuth } from '../store/AuthContext'
import { useThemeMode } from '../store/ThemeContext'

type Step = 'credentials' | 'mfa'

export default function Login() {
  const { login, loginMfa } = useAuth()
  const navigate = useNavigate()
  const { mode, toggleTheme } = useThemeMode()
  const isDark = mode === 'dark'

  // Step 1 — credentials
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [showPassword, setShowPassword] = useState(false)
  const [forgotSent, setForgotSent] = useState(false)

  // Step 2 — MFA
  const [step, setStep] = useState<Step>('credentials')
  const [mfaToken, setMfaToken] = useState('')
  const [mfaCode, setMfaCode] = useState('')

  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const mfaInputRef = useRef<HTMLInputElement>(null)

  async function handleCredentialsSubmit(e: FormEvent) {
    e.preventDefault()
    setError(null)
    setLoading(true)
    try {
      await login(email, password)
      navigate('/')
    } catch (err: unknown) {
      const e = err as { mfa_required?: boolean; mfa_token?: string }
      if (e?.mfa_required) {
        setMfaToken(e.mfa_token ?? '')
        setMfaCode('')
        setStep('mfa')
        setTimeout(() => mfaInputRef.current?.focus(), 50)
      } else {
        setError('Invalid credentials. Please try again.')
      }
    } finally {
      setLoading(false)
    }
  }

  async function handleMfaSubmit(code: string) {
    if (!code) return
    setError(null)
    setLoading(true)
    try {
      await loginMfa(mfaToken, code)
      navigate('/')
    } catch (err: unknown) {
      const e = err as Error
      setError(e?.message ?? 'Invalid authentication code. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  function handleMfaCodeChange(raw: string) {
    const stripped = raw.replace(/[^a-zA-Z0-9]/g, '').toUpperCase()
    let formatted = stripped
    if (stripped.length > 6) {
      formatted = stripped.slice(0, 4) + (stripped.length > 4 ? '-' + stripped.slice(4, 8) : '')
    }
    setMfaCode(formatted)
    if (/^\d{6}$/.test(stripped)) {
      handleMfaSubmit(stripped)
    }
  }

  // Background — subtle dot grid pattern
  const bgStyle = isDark
    ? {
        background: 'radial-gradient(ellipse at 20% 50%, rgba(68,114,196,0.12) 0%, transparent 60%), #0A0F1E',
        backgroundImage: `radial-gradient(ellipse at 20% 50%, rgba(68,114,196,0.12) 0%, transparent 60%),
          radial-gradient(circle, rgba(68,114,196,0.06) 1px, transparent 1px)`,
        backgroundSize: 'auto, 28px 28px',
      }
    : {
        backgroundImage: `radial-gradient(ellipse at 80% 50%, rgba(68,114,196,0.08) 0%, transparent 60%),
          radial-gradient(circle, rgba(68,114,196,0.1) 1px, transparent 1px)`,
        backgroundSize: 'auto, 28px 28px',
        backgroundColor: '#F0F2F8',
      }

  const header = (
    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1.5, mb: 4 }}>
      <ShieldOutlined sx={{ color: 'primary.main', fontSize: 36 }} />
      <Box>
        <Box sx={{ display: 'flex', alignItems: 'baseline', gap: 1 }}>
          <Typography variant="h5" sx={{ lineHeight: 1 }}>ISMS CORE</Typography>
          <Typography variant="caption" sx={{ color: 'primary.main', fontWeight: 600, fontSize: '0.65rem', letterSpacing: '0.05em' }}>
            v1.0
          </Typography>
        </Box>
        <Typography variant="caption" color="text.secondary">
          Information Security &amp; Privacy Compliance
        </Typography>
      </Box>
    </Box>
  )

  return (
    <Box sx={{ minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', px: 2, ...bgStyle }}>

      {/* Theme toggle — top right */}
      <Box sx={{ position: 'fixed', top: 16, right: 16 }}>
        <Tooltip title={isDark ? 'Switch to light mode' : 'Switch to dark mode'}>
          <IconButton onClick={toggleTheme} size="small" sx={{ color: 'text.secondary' }}>
            {isDark ? <LightModeOutlined fontSize="small" /> : <DarkModeOutlined fontSize="small" />}
          </IconButton>
        </Tooltip>
      </Box>

      <Box sx={{ width: '100%', maxWidth: 400 }}>
        <Card
          sx={{
            borderTop: '3px solid',
            borderTopColor: 'primary.main',
            boxShadow: isDark
              ? '0 8px 32px rgba(0,0,0,0.4)'
              : '0 8px 32px rgba(68,114,196,0.12)',
          }}
        >
          <CardContent sx={{ p: 4 }}>
            {step === 'credentials' ? (
              <>
                {header}

                <Typography variant="h6" gutterBottom>Sign in</Typography>
                <Typography variant="body2" color="text.secondary" sx={{ mb: 3 }}>
                  Enter your credentials to access the platform.
                </Typography>

                {error && (
                  <Alert severity="error" sx={{ mb: 2 }}>
                    {error}
                  </Alert>
                )}

                <Box component="form" onSubmit={handleCredentialsSubmit} noValidate>
                  <TextField
                    fullWidth
                    label="Email"
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    autoComplete="email"
                    autoFocus
                    required
                    sx={{ mb: 2 }}
                    size="small"
                  />
                  <TextField
                    fullWidth
                    label="Password"
                    type={showPassword ? 'text' : 'password'}
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    autoComplete="current-password"
                    required
                    sx={{ mb: 1.5 }}
                    size="small"
                    InputProps={{
                      endAdornment: (
                        <InputAdornment position="end">
                          <IconButton
                            onClick={() => setShowPassword((s) => !s)}
                            edge="end"
                            size="small"
                          >
                            {showPassword ? <VisibilityOffOutlined /> : <VisibilityOutlined />}
                          </IconButton>
                        </InputAdornment>
                      ),
                    }}
                  />

                  {/* Forgot password */}
                  <Box sx={{ display: 'flex', justifyContent: 'flex-end', mb: 2.5 }}>
                    {forgotSent ? (
                      <Typography variant="caption" color="text.secondary">
                        Contact your administrator to reset your password.
                      </Typography>
                    ) : (
                      <Button
                        size="small"
                        variant="text"
                        sx={{ fontSize: '0.75rem', color: 'text.secondary', p: 0, minWidth: 0, textTransform: 'none' }}
                        onClick={() => setForgotSent(true)}
                      >
                        Forgot password?
                      </Button>
                    )}
                  </Box>

                  <Button
                    fullWidth
                    variant="contained"
                    type="submit"
                    disabled={loading || !email || !password}
                    sx={{ py: 1 }}
                  >
                    {loading ? <CircularProgress size={20} /> : 'Sign in'}
                  </Button>
                </Box>
              </>
            ) : (
              <>
                {header}

                <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', mb: 3 }}>
                  <LockOutlined sx={{ fontSize: 40, color: 'primary.main', mb: 1.5 }} />
                  <Typography variant="h6" gutterBottom>Two-factor authentication</Typography>
                  <Typography variant="body2" color="text.secondary" sx={{ textAlign: 'center' }}>
                    Enter the 6-digit code from your authenticator app, or a backup code (XXXX-XXXX).
                  </Typography>
                </Box>

                {error && (
                  <Alert severity="error" sx={{ mb: 2 }}>
                    {error}
                  </Alert>
                )}

                <TextField
                  fullWidth
                  label="Authentication code"
                  value={mfaCode}
                  onChange={(e) => handleMfaCodeChange(e.target.value)}
                  inputRef={mfaInputRef}
                  autoFocus
                  autoComplete="one-time-code"
                  inputProps={{
                    maxLength: 9,
                    style: { letterSpacing: '0.3em', textAlign: 'center', fontSize: '1.4rem' },
                  }}
                  sx={{ mb: 3 }}
                />

                <Button
                  fullWidth
                  variant="contained"
                  disabled={loading || mfaCode.length < 6}
                  onClick={() => {
                    const stripped = mfaCode.replace(/[^a-zA-Z0-9]/g, '').toUpperCase()
                    handleMfaSubmit(stripped)
                  }}
                  sx={{ py: 1, mb: 1.5 }}
                >
                  {loading ? <CircularProgress size={20} /> : 'Sign in'}
                </Button>

                <Box sx={{ display: 'flex', justifyContent: 'center' }}>
                  <Button
                    size="small"
                    startIcon={<ArrowBackOutlined />}
                    onClick={() => {
                      setStep('credentials')
                      setMfaCode('')
                      setError(null)
                    }}
                    sx={{ fontSize: '0.75rem', color: 'text.secondary' }}
                  >
                    Back
                  </Button>
                </Box>
              </>
            )}
          </CardContent>
        </Card>

        {/* Footer */}
        <Typography
          variant="caption"
          color="text.disabled"
          sx={{ display: 'block', textAlign: 'center', mt: 2.5 }}
        >
          © 2026 ISMS CORE · ISO 27001:2022 Compliance Platform
        </Typography>
      </Box>
    </Box>
  )
}
