import { client } from './client'

export interface RiskMatrix {
  id: string
  org_id: string
  name: string
  probability_labels: string[]
  impact_labels: string[]
  score_map: Record<string, number>
  colour_map: Record<string, string>
  is_default: boolean
  created_at: string
}

export interface RiskScenario {
  id: string
  org_id: string
  project_id: string | null
  control_group_id: string | null
  control_group_code: string | null
  name: string
  description: string | null
  threat_source: string | null
  threat_event: string | null
  probability: number
  impact: number
  risk_score: number
  risk_level: 'low' | 'medium' | 'high' | 'critical'
  treatment_status: 'pending' | 'accept' | 'mitigate' | 'transfer' | 'avoid'
  treatment_notes: string | null
  residual_probability: number | null
  residual_impact: number | null
  residual_score: number | null
  residual_level: string | null
  owner_id: string | null
  owner_name: string | null
  target_date: string | null
  status: 'open' | 'in_treatment' | 'closed' | 'accepted'
  created_at: string
  updated_at: string
}

export interface RiskScenarioCreate {
  name: string
  description?: string
  threat_source?: string
  threat_event?: string
  probability: number
  impact: number
  treatment_status?: string
  treatment_notes?: string
  residual_probability?: number
  residual_impact?: number
  owner_id?: string
  target_date?: string
  status?: string
  project_id?: string
  control_group_id?: string
}

export interface RiskScenarioPatch extends Partial<RiskScenarioCreate> {}

export interface RiskSummary {
  total: number
  critical: number
  high: number
  medium: number
  low: number
  open: number
  accepted: number
  in_treatment: number
  closed: number
}

export interface HeatmapCell {
  p: number
  i: number
  count: number
  score: number
  level: string
}

export interface RiskHeatmap {
  probability_labels: string[]
  impact_labels: string[]
  cells: HeatmapCell[]
}

export interface RiskAcceptance {
  id: string
  risk_scenario_id: string
  approver_id: string | null
  approver_name: string
  justification: string
  expiry_date: string | null
  status: 'active' | 'expired' | 'revoked'
  revoked_by: string | null
  revoked_at: string | null
  created_at: string
}

export interface RemediationAction {
  id: string
  org_id: string
  title: string
  description: string | null
  status: 'planned' | 'in_progress' | 'completed' | 'cancelled'
  owner_id: string | null
  owner_name: string | null
  eta: string | null
  effort: 'low' | 'medium' | 'high' | null
  cost_estimate: number | null
  progress: number
  project_id: string | null
  risk_scenario_id: string | null
  risk_name: string | null
  gap_id: string | null
  control_group_id: string | null
  evidence_id: string | null
  created_at: string
  updated_at: string
}

export interface RemediationActionCreate {
  title: string
  description?: string
  status?: string
  owner_id?: string
  eta?: string
  effort?: string
  cost_estimate?: number
  progress?: number
  project_id?: string
  risk_scenario_id?: string
  gap_id?: string
  control_group_id?: string
}

export interface RemediationSummary {
  total: number
  planned: number
  in_progress: number
  completed: number
  cancelled: number
  overdue: number
}

export interface PoamItem {
  id: string
  source: 'risk' | 'gap' | 'tprm'
  title: string
  description: string | null
  status: string
  owner: string | null
  eta: string | null
  control_code: string | null
  severity: string | null
  is_overdue: boolean
}

export interface PoamSummary {
  total: number
  overdue: number
  risk_count: number
  gap_count: number
  tprm_count: number
}

export const risksApi = {
  list: (params?: { status?: string; risk_level?: string; treatment_status?: string; project_id?: string }) =>
    client.get<RiskScenario[]>('/risks', { params }).then(r => r.data),

  create: (body: RiskScenarioCreate) =>
    client.post<RiskScenario>('/risks', body).then(r => r.data),

  get: (id: string) =>
    client.get<RiskScenario>(`/risks/${id}`).then(r => r.data),

  update: (id: string, body: RiskScenarioPatch) =>
    client.patch<RiskScenario>(`/risks/${id}`, body).then(r => r.data),

  delete: (id: string) =>
    client.delete(`/risks/${id}`),

  summary: (params?: { project_id?: string }) =>
    client.get<RiskSummary>('/risks/summary', { params }).then(r => r.data),

  heatmap: (params?: { project_id?: string }) =>
    client.get<RiskHeatmap>('/risks/heatmap', { params }).then(r => r.data),

  matrix: () =>
    client.get<RiskMatrix>('/risks/matrix').then(r => r.data),

  // Acceptances
  listAcceptances: (riskId: string) =>
    client.get<RiskAcceptance[]>(`/risks/${riskId}/acceptances`).then(r => r.data),
  createAcceptance: (riskId: string, body: { justification: string; expiry_date?: string }) =>
    client.post<RiskAcceptance>(`/risks/${riskId}/accept`, body).then(r => r.data),
  revokeAcceptance: (riskId: string, acceptId: string) =>
    client.delete(`/risks/${riskId}/accept/${acceptId}`),

  // Remediation
  remediationSummary: (params?: { project_id?: string }) =>
    client.get<RemediationSummary>('/remediation/summary', { params }).then(r => r.data),
  listRemediation: (params?: { status?: string; risk_scenario_id?: string; gap_id?: string; project_id?: string }) =>
    client.get<RemediationAction[]>('/remediation', { params }).then(r => r.data),
  createRemediation: (body: RemediationActionCreate) =>
    client.post<RemediationAction>('/remediation', body).then(r => r.data),
  updateRemediation: (id: string, body: Partial<RemediationActionCreate>) =>
    client.patch<RemediationAction>(`/remediation/${id}`, body).then(r => r.data),
  deleteRemediation: (id: string) =>
    client.delete(`/remediation/${id}`),

  // POA&M (unified across risk / gap / tprm sources)
  poamSummary: () =>
    client.get<PoamSummary>('/remediation/poam/summary').then(r => r.data),
  listPoam: (params?: { source?: string }) =>
    client.get<PoamItem[]>('/remediation/poam', { params }).then(r => r.data),
}
