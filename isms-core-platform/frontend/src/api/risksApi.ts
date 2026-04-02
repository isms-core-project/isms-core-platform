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

  summary: () =>
    client.get<RiskSummary>('/risks/summary').then(r => r.data),

  heatmap: () =>
    client.get<RiskHeatmap>('/risks/heatmap').then(r => r.data),

  matrix: () =>
    client.get<RiskMatrix>('/risks/matrix').then(r => r.data),
}
