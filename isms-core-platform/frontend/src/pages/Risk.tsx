import { useState } from 'react'
import {
  Box,
  Card,
  CardContent,
  Typography,
  Stepper,
  Step,
  StepLabel,
  Button,
  TextField,
  Radio,
  RadioGroup,
  FormControlLabel,
  FormControl,
  FormLabel,
  Checkbox,
  FormGroup,
  Chip,
  Table,
  TableBody,
  TableRow,
  TableCell,
  Divider,
} from '@mui/material'
import { FileDownloadOutlined, RestartAltOutlined } from '@mui/icons-material'
import PageHeader from '../components/PageHeader'

const STEPS = [
  'Organisation Scope',
  'Asset Classification',
  'Confidentiality',
  'Integrity',
  'Availability',
  'Threat Profile',
  'Current Controls',
  'Risk Report',
]

const ASSET_TYPES = [
  'PII/Personal Data',
  'Financial Records',
  'Intellectual Property',
  'Operational Systems/SCADA',
  'Authentication Credentials',
  'Business Communications',
  'Third-party Data',
  'Audit Logs',
]

const THREAT_OPTIONS = [
  'External cyber attack',
  'Insider threat',
  'Ransomware/malware',
  'Physical theft/loss',
  'Supply chain compromise',
  'Social engineering/phishing',
  'Accidental data loss',
  'Natural disaster/outage',
  'Regulatory/compliance breach',
]

const CONTROL_OPTIONS = [
  'Access Control (A.5.15-18)',
  'Cryptography (A.8.24-25)',
  'Incident Management (A.5.24-28)',
  'Physical Security (A.7.1-14)',
  'Supplier Management (A.5.19-23)',
  'Vulnerability Management (A.8.8)',
  'Logging & Monitoring (A.8.15-16)',
  'Business Continuity (A.5.29-30)',
  'Awareness Training (A.6.3)',
]

const CIA_LABELS: Record<number, string> = {
  1: '1 — None',
  2: '2 — Low',
  3: '3 — Medium',
  4: '4 — High',
  5: '5 — Critical',
}

interface Recommendation {
  ref: string
  name: string
}

function deriveRecommendations(
  assets: string[],
  threats: string[],
  cScore: number,
  iScore: number,
  aScore: number
): Recommendation[] {
  const seen = new Set<string>()
  const results: Recommendation[] = []

  function add(ref: string, name: string) {
    if (!seen.has(ref)) {
      seen.add(ref)
      results.push({ ref, name })
    }
  }

  if (assets.includes('PII/Personal Data')) {
    add('A.5.34', 'Privacy and protection of PII')
    add('A.8.11', 'Data masking')
    add('A.8.10', 'Information deletion')
  }
  if (assets.includes('Financial Records')) {
    add('A.5.31', 'Legal, statutory, regulatory and contractual requirements')
    add('A.5.33', 'Protection of records')
  }
  if (assets.includes('Intellectual Property')) {
    add('A.5.32', 'Intellectual property rights')
    add('A.5.33', 'Protection of records')
  }
  if (assets.includes('Authentication Credentials')) {
    add('A.5.15', 'Access control policy')
    add('A.5.16', 'Identity management')
    add('A.5.17', 'Authentication information')
  }
  if (threats.includes('External cyber attack')) {
    add('A.8.7',  'Protection against malware')
    add('A.8.23', 'Web filtering')
    add('A.8.22', 'Segregation of networks')
  }
  if (threats.includes('Insider threat')) {
    add('A.6.2',  'Terms and conditions of employment')
    add('A.5.18', 'Access rights')
    add('A.8.18', 'Use of privileged utility programs')
  }
  if (threats.includes('Ransomware/malware')) {
    add('A.8.7',  'Protection against malware')
    add('A.8.13', 'Information backup')
    add('A.5.29', 'Information security during disruption')
  }
  if (threats.includes('Supply chain compromise')) {
    add('A.5.19', 'Information security in supplier relationships')
    add('A.5.21', 'Managing information security in the ICT supply chain')
  }
  if (threats.includes('Social engineering/phishing')) {
    add('A.6.3', 'Information security awareness, education and training')
    add('A.6.4', 'Disciplinary process')
  }
  if (cScore >= 4) {
    add('A.8.24', 'Use of cryptography')
    add('A.8.11', 'Data masking')
  }
  if (iScore >= 4) {
    add('A.8.9',  'Configuration management')
    add('A.5.37', 'Documented operating procedures')
  }
  if (aScore >= 4) {
    add('A.5.29', 'Information security during disruption')
    add('A.8.14', 'Redundancy of information processing facilities')
    add('A.8.16', 'Monitoring activities')
  }

  return results
}

function nextStepsForLevel(level: string): string[] {
  switch (level) {
    case 'Critical':
      return [
        'Initiate an immediate risk treatment plan — assign owners and deadlines within 48 hours.',
        'Escalate to senior management and document in the risk register.',
        'Implement compensating controls for the highest-impact gaps before the next assessment cycle.',
        'Schedule an emergency ISO 27001 internal review within 30 days.',
      ]
    case 'High':
      return [
        'Prioritise implementation of the recommended controls within the current quarter.',
        'Document identified gaps in the formal risk register with severity ratings.',
        'Engage relevant control owners and agree remediation milestones.',
        'Review supplier and third-party agreements for relevant clauses.',
      ]
    case 'Medium':
      return [
        'Schedule remediation activities into the next planning cycle.',
        'Review and update the ISMS scope statement if new asset types were identified.',
        'Ensure awareness training covers the identified threat vectors.',
        'Conduct a targeted internal audit on the weakest control areas.',
      ]
    default:
      return [
        'Maintain current controls and schedule periodic review.',
        'Continue monitoring for changes in the threat landscape.',
        'Ensure evidence of effective controls is kept up to date.',
      ]
  }
}

function exportRiskCsv(data: {
  scope: string
  businessFunction: string
  assets: string[]
  cScore: number
  iScore: number
  aScore: number
  rawRisk: number
  riskLevel: string
  threats: string[]
  controls: string[]
  recommendations: Recommendation[]
}) {
  const rows: string[][] = [
    ['field', 'value'],
    ['scope', data.scope.replace(/,/g, ';')],
    ['business_function', data.businessFunction.replace(/,/g, ';')],
    ['assets_in_scope', data.assets.join(' | ')],
    ['confidentiality_score', String(data.cScore)],
    ['integrity_score', String(data.iScore)],
    ['availability_score', String(data.aScore)],
    ['risk_score', data.rawRisk.toFixed(2)],
    ['risk_level', data.riskLevel],
    ['threats_identified', data.threats.join(' | ')],
    ['controls_in_place', data.controls.join(' | ')],
    ['recommended_controls', data.recommendations.map((r) => `${r.ref} ${r.name}`).join(' | ')],
  ]
  const csv = rows.map((r) => r.join(',')).join('\n')
  const today = new Date().toISOString().slice(0, 10).replace(/-/g, '')
  const url = URL.createObjectURL(new Blob([csv], { type: 'text/csv' }))
  const a = document.createElement('a')
  a.href = url
  a.download = `isms-risk-assessment-${today}.csv`
  a.click()
  URL.revokeObjectURL(url)
}

const RISK_COLOR = (level: string) => {
  if (level === 'Critical') return { bg: '#3a0000', fg: '#FFC7CE' }
  if (level === 'High')     return { bg: '#3a1a00', fg: '#FFD580' }
  if (level === 'Medium')   return { bg: '#3a2e00', fg: '#FFEB9C' }
  return { bg: '#1a3a27', fg: '#C6EFCE' }
}

const TD = { fontSize: '0.82rem', borderBottom: '1px solid rgba(68,114,196,0.15)' }

export default function Risk() {
  const [activeStep, setActiveStep] = useState(0)

  // Step 1
  const [scope, setScope] = useState('')
  const [businessFunction, setBusinessFunction] = useState('')

  // Step 2
  const [assets, setAssets] = useState<string[]>([])

  // Steps 3-5
  const [cScore, setCScore] = useState<number>(3)
  const [iScore, setIScore] = useState<number>(3)
  const [aScore, setAScore] = useState<number>(3)

  // Step 6
  const [threats, setThreats] = useState<string[]>([])

  // Step 7
  const [controls, setControls] = useState<string[]>([])

  function toggleItem(list: string[], setList: (v: string[]) => void, item: string) {
    setList(list.includes(item) ? list.filter((x) => x !== item) : [...list, item])
  }

  function canAdvance(): boolean {
    if (activeStep === 0) return scope.trim().length > 0 && businessFunction.trim().length > 0
    return true
  }

  function handleNext() {
    if (activeStep < STEPS.length - 1) setActiveStep((s) => s + 1)
  }

  function handleBack() {
    if (activeStep > 0) setActiveStep((s) => s - 1)
  }

  function handleReset() {
    setActiveStep(0)
    setScope('')
    setBusinessFunction('')
    setAssets([])
    setCScore(3)
    setIScore(3)
    setAScore(3)
    setThreats([])
    setControls([])
  }

  // Risk score computation
  const ciaMax = Math.max(cScore, iScore, aScore)
  const threatScore = Math.min(threats.length * 0.3, 2.0)
  const controlsDiscount = Math.min(controls.length * 0.2, 1.5)
  const rawRisk = Math.max(1, Math.min(5, ciaMax + threatScore - controlsDiscount))
  const riskLevel =
    rawRisk >= 4.5 ? 'Critical' :
    rawRisk >= 3.5 ? 'High' :
    rawRisk >= 2.5 ? 'Medium' :
    rawRisk >= 1.5 ? 'Low' : 'Minimal'

  const recommendations = deriveRecommendations(assets, threats, cScore, iScore, aScore)
  const nextSteps = nextStepsForLevel(riskLevel)
  const riskColors = RISK_COLOR(riskLevel)

  function renderStepContent() {
    switch (activeStep) {
      case 0:
        return (
          <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2.5 }}>
            <TextField
              label="Systems / processes in scope"
              placeholder="e.g. HR platform, payroll system, customer database"
              value={scope}
              onChange={(e) => setScope(e.target.value)}
              multiline
              rows={3}
              fullWidth
              required
            />
            <TextField
              label="Primary business function"
              placeholder="e.g. Financial services, healthcare administration, e-commerce"
              value={businessFunction}
              onChange={(e) => setBusinessFunction(e.target.value)}
              fullWidth
              required
            />
          </Box>
        )

      case 1:
        return (
          <FormControl component="fieldset" fullWidth>
            <FormLabel component="legend" sx={{ mb: 1.5, color: 'text.secondary' }}>
              Select all asset types present in scope
            </FormLabel>
            <FormGroup>
              <Box sx={{ display: 'grid', gridTemplateColumns: { xs: '1fr', sm: '1fr 1fr' }, gap: 0.5 }}>
                {ASSET_TYPES.map((a) => (
                  <FormControlLabel
                    key={a}
                    control={
                      <Checkbox
                        checked={assets.includes(a)}
                        onChange={() => toggleItem(assets, setAssets, a)}
                        size="small"
                      />
                    }
                    label={<Typography variant="body2">{a}</Typography>}
                  />
                ))}
              </Box>
            </FormGroup>
          </FormControl>
        )

      case 2:
        return (
          <FormControl>
            <FormLabel sx={{ mb: 1.5, color: 'text.secondary' }}>
              How sensitive is the data if disclosed?
            </FormLabel>
            <RadioGroup value={cScore} onChange={(e) => setCScore(Number(e.target.value))}>
              {[1, 2, 3, 4, 5].map((v) => (
                <FormControlLabel key={v} value={v} control={<Radio size="small" />} label={CIA_LABELS[v]} />
              ))}
            </RadioGroup>
          </FormControl>
        )

      case 3:
        return (
          <FormControl>
            <FormLabel sx={{ mb: 1.5, color: 'text.secondary' }}>
              How severe is the impact if data is altered or corrupted?
            </FormLabel>
            <RadioGroup value={iScore} onChange={(e) => setIScore(Number(e.target.value))}>
              {[1, 2, 3, 4, 5].map((v) => (
                <FormControlLabel key={v} value={v} control={<Radio size="small" />} label={CIA_LABELS[v]} />
              ))}
            </RadioGroup>
          </FormControl>
        )

      case 4:
        return (
          <FormControl>
            <FormLabel sx={{ mb: 1.5, color: 'text.secondary' }}>
              How severe is the impact if systems are unavailable?
            </FormLabel>
            <RadioGroup value={aScore} onChange={(e) => setAScore(Number(e.target.value))}>
              {[1, 2, 3, 4, 5].map((v) => (
                <FormControlLabel key={v} value={v} control={<Radio size="small" />} label={CIA_LABELS[v]} />
              ))}
            </RadioGroup>
          </FormControl>
        )

      case 5:
        return (
          <FormControl component="fieldset" fullWidth>
            <FormLabel component="legend" sx={{ mb: 1.5, color: 'text.secondary' }}>
              Select all applicable threats to your environment
            </FormLabel>
            <FormGroup>
              <Box sx={{ display: 'grid', gridTemplateColumns: { xs: '1fr', sm: '1fr 1fr' }, gap: 0.5 }}>
                {THREAT_OPTIONS.map((t) => (
                  <FormControlLabel
                    key={t}
                    control={
                      <Checkbox
                        checked={threats.includes(t)}
                        onChange={() => toggleItem(threats, setThreats, t)}
                        size="small"
                      />
                    }
                    label={<Typography variant="body2">{t}</Typography>}
                  />
                ))}
              </Box>
            </FormGroup>
          </FormControl>
        )

      case 6:
        return (
          <FormControl component="fieldset" fullWidth>
            <FormLabel component="legend" sx={{ mb: 1.5, color: 'text.secondary' }}>
              Which ISO 27001 control areas are already in place?
            </FormLabel>
            <FormGroup>
              <Box sx={{ display: 'flex', flexDirection: 'column', gap: 0.5 }}>
                {CONTROL_OPTIONS.map((c) => (
                  <FormControlLabel
                    key={c}
                    control={
                      <Checkbox
                        checked={controls.includes(c)}
                        onChange={() => toggleItem(controls, setControls, c)}
                        size="small"
                      />
                    }
                    label={<Typography variant="body2">{c}</Typography>}
                  />
                ))}
              </Box>
            </FormGroup>
          </FormControl>
        )

      case 7:
        return (
          <Box>
            {/* Risk score */}
            <Box
              sx={{
                display: 'flex', alignItems: 'center', gap: 3, mb: 3,
                p: 2.5, borderRadius: 2,
                bgcolor: riskColors.bg,
                border: `1px solid ${riskColors.fg}40`,
              }}
            >
              <Box sx={{ textAlign: 'center', minWidth: 80 }}>
                <Typography sx={{ fontSize: '3rem', fontWeight: 800, color: riskColors.fg, lineHeight: 1 }}>
                  {rawRisk.toFixed(1)}
                </Typography>
                <Typography sx={{ fontSize: '0.65rem', color: riskColors.fg, opacity: 0.7, mt: 0.25 }}>
                  Risk Score
                </Typography>
              </Box>
              <Box>
                <Chip
                  label={riskLevel}
                  sx={{
                    bgcolor: riskColors.bg, color: riskColors.fg, fontWeight: 800,
                    fontSize: '1rem', height: 32, border: `1px solid ${riskColors.fg}80`,
                    mb: 0.5,
                  }}
                />
                <Typography variant="caption" sx={{ color: riskColors.fg, opacity: 0.8, display: 'block' }}>
                  CIA max {ciaMax} · {threats.length} threat{threats.length !== 1 ? 's' : ''} · {controls.length} control{controls.length !== 1 ? 's' : ''} in place
                </Typography>
              </Box>
            </Box>

            {/* CIA breakdown */}
            <Typography variant="subtitle2" sx={{ mb: 1, color: 'text.secondary', textTransform: 'uppercase', letterSpacing: '0.06em', fontSize: '0.72rem' }}>
              CIA Breakdown
            </Typography>
            <Table size="small" sx={{ mb: 3 }}>
              <TableBody>
                {[
                  { label: 'Confidentiality', score: cScore },
                  { label: 'Integrity',       score: iScore },
                  { label: 'Availability',    score: aScore },
                ].map(({ label, score }) => (
                  <TableRow key={label}>
                    <TableCell sx={{ ...TD, fontWeight: 600, width: 160 }}>{label}</TableCell>
                    <TableCell sx={TD}>{CIA_LABELS[score]}</TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>

            <Divider sx={{ mb: 2 }} />

            {/* Recommendations */}
            <Typography variant="subtitle2" sx={{ mb: 1.5, color: 'text.secondary', textTransform: 'uppercase', letterSpacing: '0.06em', fontSize: '0.72rem' }}>
              Top Recommended ISO 27001 Controls
            </Typography>
            {recommendations.length === 0 ? (
              <Typography variant="body2" color="text.secondary">
                No specific recommendations — current profile is low risk with controls in place.
              </Typography>
            ) : (
              <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 1, mb: 3 }}>
                {recommendations.map((r) => (
                  <Chip
                    key={r.ref}
                    label={`${r.ref} — ${r.name}`}
                    size="small"
                    sx={{
                      bgcolor: '#1a2a3a', color: '#9fc8f0',
                      fontSize: '0.72rem', height: 22, fontWeight: 600,
                    }}
                  />
                ))}
              </Box>
            )}

            <Divider sx={{ mb: 2 }} />

            {/* Next Steps */}
            <Typography variant="subtitle2" sx={{ mb: 1.5, color: 'text.secondary', textTransform: 'uppercase', letterSpacing: '0.06em', fontSize: '0.72rem' }}>
              Next Steps
            </Typography>
            <Box component="ul" sx={{ m: 0, pl: 2.5 }}>
              {nextSteps.map((step, i) => (
                <Box component="li" key={i} sx={{ mb: 0.75 }}>
                  <Typography variant="body2">{step}</Typography>
                </Box>
              ))}
            </Box>

            {/* Export */}
            <Box sx={{ mt: 3, display: 'flex', gap: 1.5 }}>
              <Button
                variant="outlined"
                size="small"
                startIcon={<FileDownloadOutlined />}
                onClick={() =>
                  exportRiskCsv({ scope, businessFunction, assets, cScore, iScore, aScore, rawRisk, riskLevel, threats, controls, recommendations })
                }
              >
                Export CSV
              </Button>
              <Button
                variant="text"
                size="small"
                startIcon={<RestartAltOutlined />}
                onClick={handleReset}
                sx={{ color: 'text.secondary' }}
              >
                Start Over
              </Button>
            </Box>
          </Box>
        )

      default:
        return null
    }
  }

  return (
    <Box>
      <PageHeader
        title="Risk Assessment Wizard"
        subtitle="CIA-based risk classification · ISO/IEC 27001:2022"
      />

      <Card>
        <CardContent>
          <Stepper activeStep={activeStep} alternativeLabel sx={{ mb: 4 }}>
            {STEPS.map((label) => (
              <Step key={label}>
                <StepLabel
                  sx={{
                    '& .MuiStepLabel-label': { fontSize: '0.7rem' },
                    '& .Mui-active': { color: 'primary.main' },
                    '& .Mui-completed': { color: 'primary.main' },
                  }}
                >
                  {label}
                </StepLabel>
              </Step>
            ))}
          </Stepper>

          <Box sx={{ minHeight: 280, mb: 3 }}>
            <Typography variant="h6" sx={{ mb: 2.5 }}>{STEPS[activeStep]}</Typography>
            {renderStepContent()}
          </Box>

          {activeStep < STEPS.length - 1 && (
            <Box sx={{ display: 'flex', gap: 1.5 }}>
              <Button
                variant="outlined"
                onClick={handleBack}
                disabled={activeStep === 0}
              >
                Back
              </Button>
              <Button
                variant="contained"
                onClick={handleNext}
                disabled={!canAdvance()}
              >
                {activeStep === STEPS.length - 2 ? 'Calculate Risk' : 'Next'}
              </Button>
            </Box>
          )}
          {activeStep === STEPS.length - 1 && (
            <Button variant="outlined" onClick={handleBack} sx={{ mt: 1 }}>
              Back
            </Button>
          )}
        </CardContent>
      </Card>
    </Box>
  )
}
