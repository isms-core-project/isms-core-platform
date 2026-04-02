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
} from '@mui/material'
import { ShieldOutlined, VisibilityOutlined, VisibilityOffOutlined, LockOutlined, ArrowBackOutlined } from '@mui/icons-material'
import { useAuth } from '../store/AuthContext'

type Step = 'credentials' | 'mfa'

export default function Login() {
  const { login, loginMfa } = useAuth()
  const navigate = useNavigate()

  // Step 1 — credentials
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [showPassword, setShowPassword] = useState(false)

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
        // Focus the MFA input on next render
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
    // Strip non-alphanumeric, uppercase
    const stripped = raw.replace(/[^a-zA-Z0-9]/g, '').toUpperCase()

    // Format as XXXX-XXXX for 8-char backup codes, plain for 6-digit TOTP
    let formatted = stripped
    if (stripped.length > 6) {
      // Backup code: XXXX-XXXX, max 9 display chars (8 + dash)
      formatted = stripped.slice(0, 4) + (stripped.length > 4 ? '-' + stripped.slice(4, 8) : '')
    }

    setMfaCode(formatted)

    // Auto-submit on 6 all-numeric digits (TOTP)
    if (/^\d{6}$/.test(stripped)) {
      handleMfaSubmit(stripped)
    }
  }

  const header = (
    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1.5, mb: 4 }}>
      <ShieldOutlined sx={{ color: 'primary.main', fontSize: 36 }} />
      <Box>
        <Typography variant="h5" sx={{ lineHeight: 1 }}>ISMS CORE</Typography>
        <Typography variant="caption" color="text.secondary">
          Information Security &amp; Privacy Compliance
        </Typography>
      </Box>
    </Box>
  )

  return (
    <Box
      sx={{
        minHeight: '100vh',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        bgcolor: 'background.default',
        px: 2,
      }}
    >
      <Card sx={{ width: '100%', maxWidth: 400 }}>
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
                  sx={{ mb: 3 }}
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
    </Box>
  )
}
