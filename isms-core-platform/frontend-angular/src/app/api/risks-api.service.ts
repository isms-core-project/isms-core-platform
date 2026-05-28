import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

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

@Injectable({ providedIn: 'root' })
export class RisksApiService {
  private http = inject(HttpClient)

  list(params?: { status?: string; risk_level?: string; treatment_status?: string; project_id?: string }): Observable<RiskScenario[]> {
    const p = Object.fromEntries(Object.entries(params ?? {}).filter(([, v]) => v != null && v !== '' && v !== 'undefined'))
    return this.http.get<RiskScenario[]>('/api/v1/risks', Object.keys(p).length ? { params: p } : {})
  }

  create(body: RiskScenarioCreate): Observable<RiskScenario> {
    return this.http.post<RiskScenario>('/api/v1/risks', body)
  }

  get(id: string): Observable<RiskScenario> {
    return this.http.get<RiskScenario>(`/api/v1/risks/${id}`)
  }

  update(id: string, body: Partial<RiskScenarioCreate>): Observable<RiskScenario> {
    return this.http.patch<RiskScenario>(`/api/v1/risks/${id}`, body)
  }

  delete(id: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/risks/${id}`)
  }

  summary(params?: { project_id?: string }): Observable<RiskSummary> {
    return this.http.get<RiskSummary>('/api/v1/risks/summary', { params })
  }

  heatmap(params?: { project_id?: string }): Observable<RiskHeatmap> {
    return this.http.get<RiskHeatmap>('/api/v1/risks/heatmap', { params })
  }

  matrix(): Observable<RiskMatrix> {
    return this.http.get<RiskMatrix>('/api/v1/risks/matrix')
  }

  listAcceptances(riskId: string): Observable<RiskAcceptance[]> {
    return this.http.get<RiskAcceptance[]>(`/api/v1/risks/${riskId}/acceptances`)
  }

  createAcceptance(riskId: string, body: { justification: string; expiry_date?: string }): Observable<RiskAcceptance> {
    return this.http.post<RiskAcceptance>(`/api/v1/risks/${riskId}/accept`, body)
  }

  revokeAcceptance(riskId: string, acceptId: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/risks/${riskId}/accept/${acceptId}`)
  }

  remediationSummary(params?: { project_id?: string }): Observable<RemediationSummary> {
    return this.http.get<RemediationSummary>('/api/v1/remediation/summary', { params })
  }

  listRemediation(params?: { status?: string; risk_scenario_id?: string; gap_id?: string; project_id?: string }): Observable<RemediationAction[]> {
    return this.http.get<RemediationAction[]>('/api/v1/remediation', { params })
  }

  createRemediation(body: RemediationActionCreate): Observable<RemediationAction> {
    return this.http.post<RemediationAction>('/api/v1/remediation', body)
  }

  updateRemediation(id: string, body: Partial<RemediationActionCreate>): Observable<RemediationAction> {
    return this.http.patch<RemediationAction>(`/api/v1/remediation/${id}`, body)
  }

  deleteRemediation(id: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/remediation/${id}`)
  }

  poamSummary(): Observable<PoamSummary> {
    return this.http.get<PoamSummary>('/api/v1/remediation/poam/summary')
  }

  listPoam(params?: { source?: string }): Observable<PoamItem[]> {
    return this.http.get<PoamItem[]>('/api/v1/remediation/poam', { params })
  }
}
