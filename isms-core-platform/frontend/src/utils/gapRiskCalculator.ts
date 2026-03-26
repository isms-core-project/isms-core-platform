// ── Types ──────────────────────────────────────────────────────────────────

export interface BsiThreat {
  code: string
  label: string
}

export type RiskLevel  = 'LOW' | 'MEDIUM' | 'HIGH' | 'VERY_HIGH'
export type Likelihood = 'low' | 'medium' | 'high'
export type Impact     = 'limited' | 'considerable'

export interface GapRiskResult {
  section:    string      // 'A5' | 'A6' | 'A7' | 'A8' | 'unknown'
  likelihood: Likelihood
  impact:     Impact
  riskLevel:  RiskLevel
  threats:    BsiThreat[]
  treatment:  string
}

// ── BSI 200-3 elementary threat catalogue ──────────────────────────────────
// G 0.x codes from BSI Standard 200-3 (English edition)

const THREATS_BY_SECTION: Record<string, BsiThreat[]> = {
  A5: [
    { code: 'G 0.18', label: 'Faulty planning or lack of concept' },
    { code: 'G 0.29', label: 'Violation of laws or regulations' },
    { code: 'G 0.46', label: 'Loss of integrity of sensitive information' },
  ],
  A6: [
    { code: 'G 0.42', label: 'Social engineering / phishing' },
    { code: 'G 0.23', label: 'Unauthorised access to IT systems' },
    { code: 'G 0.45', label: 'Data loss' },
  ],
  A7: [
    { code: 'G 0.1',  label: 'Fire' },
    { code: 'G 0.16', label: 'Theft of devices or documents' },
    { code: 'G 0.44', label: 'Unauthorised entry to premises' },
  ],
  A8: [
    { code: 'G 0.14', label: 'Interception of information' },
    { code: 'G 0.19', label: 'Disclosure of information worth protecting' },
    { code: 'G 0.22', label: 'Manipulation of information' },
    { code: 'G 0.28', label: 'Software vulnerabilities or errors' },
    { code: 'G 0.39', label: 'Malware' },
  ],
  unknown: [
    { code: 'G 0.18', label: 'Faulty planning or lack of concept' },
  ],
}

// ── BSI 200-3 risk matrix ──────────────────────────────────────────────────
//
//               Impact
// Likelihood    limited    considerable
//   low         LOW        MEDIUM
//   medium      MEDIUM     HIGH
//   high        HIGH       VERY_HIGH

const RISK_MATRIX: Record<Likelihood, Record<Impact, RiskLevel>> = {
  low:    { limited: 'LOW',    considerable: 'MEDIUM'    },
  medium: { limited: 'MEDIUM', considerable: 'HIGH'      },
  high:   { limited: 'HIGH',   considerable: 'VERY_HIGH' },
}

// ── Treatment strings ──────────────────────────────────────────────────────

const TREATMENT: Record<RiskLevel, string> = {
  VERY_HIGH: 'Mitigate immediately — treat as priority risk requiring urgent action within 30 days',
  HIGH:      'Mitigate — include in current remediation cycle with defined owner and deadline',
  MEDIUM:    'Mitigate or monitor — schedule remediation in next planning cycle',
  LOW:       'Accept or monitor — review at next ISMS management review cycle',
}

// ── Internal helpers ───────────────────────────────────────────────────────

function getSection(code: string): string {
  try {
    const n = parseInt((code ?? '').split('-')[1] ?? '', 10)
    if (n === 5) return 'A5'
    if (n === 6) return 'A6'
    if (n === 7) return 'A7'
    if (n === 8) return 'A8'
  } catch { /* fall through */ }
  return 'unknown'
}

function getLikelihood(severity: string): Likelihood {
  if (severity === 'critical' || severity === 'high') return 'high'
  if (severity === 'medium') return 'medium'
  return 'low'
}

function getImpact(section: string): Impact {
  if (section === 'A8' || section === 'A7') return 'considerable'
  return 'limited'
}

// ── Public API ─────────────────────────────────────────────────────────────

export function calculateGapRisk(
  controlGroupCode: string,
  severity: string,
): GapRiskResult {
  const section    = getSection(controlGroupCode)
  const likelihood = getLikelihood(severity)
  const impact     = getImpact(section)
  const riskLevel  = RISK_MATRIX[likelihood][impact]
  const threats    = THREATS_BY_SECTION[section] ?? THREATS_BY_SECTION.unknown

  return { section, likelihood, impact, riskLevel, threats, treatment: TREATMENT[riskLevel] }
}
