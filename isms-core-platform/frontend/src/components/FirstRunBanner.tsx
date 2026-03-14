/**
 * FirstRunBanner — step-by-step onboarding for new deployments.
 *
 * Shows on the Overview page until all 5 steps are done OR the user dismisses it.
 * Dismissal is stored in org.settings.onboarding_dismissed = true.
 *
 * Steps checked against real DB state:
 *   1. Change admin password       — can't detect; checkbox manual
 *   2. Name your organisation      — org.settings.org_name set
 *   3. Framework data loaded       — total_controls > 0
 *   4. ISMS documents imported     — total_policies > 0 && total_implementations > 0
 *   5. SMTP configured (optional)  — smtp_enabled === true
 */

import {
  Alert,
  Box,
  Button,
  Chip,
  Collapse,
  IconButton,
  Paper,
  Step,
  StepContent,
  StepLabel,
  Stepper,
  TextField,
  Tooltip,
  Typography,
} from '@mui/material'
import {
  CheckCircleOutlined,
  CloseOutlined,
  ExpandLessOutlined,
  ExpandMoreOutlined,
  KeyOutlined,
  BusinessOutlined,
  StorageOutlined,
  FolderOutlined,
  MailOutlined,
} from '@mui/icons-material'
import { useState } from 'react'
import { useMutation, useQueryClient } from '@tanstack/react-query'
import { useNavigate } from 'react-router-dom'
import { adminApi } from '../api/admin'

interface Props {
  totalControls: number
  totalPolicies: number
  totalImplementations: number
  smtpEnabled: boolean
  orgSettings: Record<string, unknown>
}

interface StepDef {
  label: string
  icon: React.ReactNode
  done: boolean
  optional: boolean
  description: string
  action?: { label: string; onClick: () => void }
  inlineForm?: React.ReactNode
}

export default function FirstRunBanner({
  totalControls,
  totalPolicies,
  totalImplementations,
  smtpEnabled,
  orgSettings,
}: Props) {
  const navigate = useNavigate()
  const qc = useQueryClient()
  const [expanded, setExpanded] = useState(true)
  const [orgName, setOrgName] = useState((orgSettings.org_name as string) ?? '')
  const [passwordAcked, setPasswordAcked] = useState(!!(orgSettings.password_changed_acked))

  const dismissed = !!(orgSettings.onboarding_dismissed)

  const patchMutation = useMutation({
    mutationFn: (patch: Record<string, unknown>) =>
      adminApi.patchOrganisationSettings({ ...orgSettings, ...patch }),
    onSuccess: () => qc.invalidateQueries({ queryKey: ['organisation'] }),
  })

  function saveOrgName() {
    if (!orgName.trim()) return
    patchMutation.mutate({ org_name: orgName.trim() })
  }

  function ackPassword() {
    patchMutation.mutate({ password_changed_acked: true })
    setPasswordAcked(true)
  }

  function dismiss() {
    patchMutation.mutate({ onboarding_dismissed: true })
  }

  if (dismissed) return null

  const steps: StepDef[] = [
    {
      label: 'Change the admin password',
      icon: <KeyOutlined fontSize="small" />,
      done: passwordAcked,
      optional: false,
      description: 'The default password is admin123. Change it immediately in Admin → Users before exposing the platform on your network.',
      action: { label: 'Go to Admin', onClick: () => navigate('/admin') },
      inlineForm: !passwordAcked ? (
        <Button size="small" variant="outlined" onClick={ackPassword} sx={{ mt: 1 }}>
          ✓ Done — I changed the password
        </Button>
      ) : undefined,
    },
    {
      label: 'Name your organisation',
      icon: <BusinessOutlined fontSize="small" />,
      done: !!(orgSettings.org_name),
      optional: false,
      description: 'Set your organisation name. This appears in reports and email notifications.',
      inlineForm: (
        <Box sx={{ display: 'flex', gap: 1, mt: 1, alignItems: 'center' }}>
          <TextField
            size="small"
            label="Organisation Name"
            value={orgName}
            onChange={(e) => setOrgName(e.target.value)}
            sx={{ minWidth: 240 }}
          />
          <Button size="small" variant="contained" onClick={saveOrgName} disabled={!orgName.trim() || patchMutation.isPending}>
            Save
          </Button>
        </Box>
      ),
    },
    {
      label: 'Load reference framework data',
      icon: <StorageOutlined fontSize="small" />,
      done: totalControls > 0,
      optional: false,
      description: `ISO 27001 controls, crosswalk mappings, and framework data must be loaded into the database. ${totalControls > 0 ? `✓ ${totalControls} controls loaded.` : 'Go to Admin → Sync to run the initial import.'}`,
      action: totalControls === 0 ? { label: 'Go to Admin → Sync', onClick: () => navigate('/admin') } : undefined,
    },
    {
      label: 'Import ISMS documents',
      icon: <FolderOutlined fontSize="small" />,
      done: totalPolicies > 0 && totalImplementations > 0,
      optional: false,
      description: totalPolicies > 0 && totalImplementations > 0
        ? `✓ ${totalPolicies} policies and ${totalImplementations} implementation guides loaded.`
        : 'Import your policies (POL) and implementation guides (IMP) from the mounted framework/operational paths. Go to Admin → Import.',
      action: (totalPolicies === 0 || totalImplementations === 0)
        ? { label: 'Go to Admin → Import', onClick: () => navigate('/admin') }
        : undefined,
    },
    {
      label: 'Configure email notifications',
      icon: <MailOutlined fontSize="small" />,
      done: smtpEnabled,
      optional: true,
      description: smtpEnabled
        ? '✓ SMTP configured. Email notifications are active.'
        : 'Optional — set MAIL_HOST in your .env to enable gap alerts, evidence expiry warnings, and workflow notifications. Restart the stack after changing.',
      action: !smtpEnabled ? { label: 'View System Config', onClick: () => navigate('/system') } : undefined,
    },
  ]

  const doneCount = steps.filter((s) => s.done).length
  const requiredDone = steps.filter((s) => !s.optional && s.done).length
  const requiredTotal = steps.filter((s) => !s.optional).length
  const allRequiredDone = requiredDone === requiredTotal

  // Find first incomplete required step for the stepper active index
  const activeStep = steps.findIndex((s) => !s.done && !s.optional)

  return (
    <Paper
      variant="outlined"
      sx={{
        mb: 3,
        borderColor: allRequiredDone ? 'success.dark' : 'primary.dark',
        bgcolor: allRequiredDone ? 'rgba(198,239,206,0.05)' : 'rgba(68,114,196,0.06)',
        overflow: 'hidden',
      }}
    >
      {/* Header */}
      <Box
        sx={{
          display: 'flex',
          alignItems: 'center',
          gap: 1.5,
          px: 2.5,
          py: 1.5,
          borderBottom: expanded ? '1px solid' : 'none',
          borderColor: 'divider',
          cursor: 'pointer',
        }}
        onClick={() => setExpanded((v) => !v)}
      >
        <Typography variant="subtitle2" fontWeight={700} sx={{ flex: 1 }}>
          🚀 Getting Started — Platform Setup
        </Typography>
        <Chip
          label={`${doneCount} / ${steps.length} steps complete`}
          size="small"
          sx={{
            height: 20,
            fontSize: '0.65rem',
            bgcolor: allRequiredDone ? '#1a3a27' : '#1a2a3a',
            color: allRequiredDone ? '#C6EFCE' : '#9fc8f0',
          }}
        />
        <Tooltip title="Dismiss permanently">
          <IconButton
            size="small"
            onClick={(e) => { e.stopPropagation(); dismiss() }}
            sx={{ ml: 0.5 }}
          >
            <CloseOutlined sx={{ fontSize: 16 }} />
          </IconButton>
        </Tooltip>
        <IconButton size="small">
          {expanded ? <ExpandLessOutlined fontSize="small" /> : <ExpandMoreOutlined fontSize="small" />}
        </IconButton>
      </Box>

      {/* Stepper body */}
      <Collapse in={expanded}>
        <Box sx={{ px: 2.5, py: 2 }}>
          {allRequiredDone && (
            <Alert severity="success" sx={{ mb: 2 }}>
              All required steps complete — your platform is ready. You can dismiss this banner.
            </Alert>
          )}
          <Stepper activeStep={activeStep === -1 ? steps.length : activeStep} orientation="vertical" nonLinear>
            {steps.map((step, idx) => (
              <Step key={idx} completed={step.done}>
                <StepLabel
                  icon={
                    step.done
                      ? <CheckCircleOutlined sx={{ color: '#C6EFCE', fontSize: 20 }} />
                      : <Box sx={{
                          width: 20, height: 20, borderRadius: '50%',
                          bgcolor: idx === activeStep ? 'primary.main' : 'action.disabled',
                          display: 'flex', alignItems: 'center', justifyContent: 'center',
                        }}>
                          {step.icon}
                        </Box>
                  }
                  optional={step.optional ? <Typography variant="caption" color="text.secondary">Optional</Typography> : undefined}
                >
                  <Typography variant="body2" fontWeight={step.done ? 400 : 600}
                    sx={{ textDecoration: step.done ? 'line-through' : 'none', color: step.done ? 'text.secondary' : 'text.primary' }}>
                    {step.label}
                  </Typography>
                </StepLabel>
                <StepContent>
                  <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 1 }}>
                    {step.description}
                  </Typography>
                  {step.action && (
                    <Button size="small" variant="outlined" onClick={step.action.onClick} sx={{ mr: 1 }}>
                      {step.action.label}
                    </Button>
                  )}
                  {step.inlineForm}
                </StepContent>
              </Step>
            ))}
          </Stepper>
        </Box>
      </Collapse>
    </Paper>
  )
}
