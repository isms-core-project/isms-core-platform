import { client } from './client'

export interface EbiosStudy {
  id: string; org_id: string; project_id: string | null
  name: string; description: string | null; scope: string | null
  status: string; owner: string | null
  started_at: string | null; reviewed_at: string | null
  created_at: string; updated_at: string
}

export interface EbiosCreate {
  name: string; description?: string; scope?: string
  status?: string; owner?: string; project_id?: string
  started_at?: string; reviewed_at?: string
}

export interface EbiosFearedEvent {
  id: string; study_id: string; asset_name: string; asset_type: string
  description: string | null; gravity: number | null; created_at: string
}

export interface EbiosRiskSource {
  id: string; study_id: string; name: string; category: string
  motivation: string | null; pertinence: number | null
  activity: number | null; resources: number | null; created_at: string
}

export interface EbiosScenario {
  id: string; study_id: string; name: string; description: string | null
  risk_source_id: string | null; feared_event_id: string | null
  likelihood: number | null; gravity: number | null; risk_level: number
  retained: boolean; created_at: string
}

export interface EbiosAttackPath {
  id: string; study_id: string; strategic_scenario_id: string | null
  name: string; description: string | null
  mitre_techniques: string[]; difficulty: number | null
  detectability: number | null; created_at: string
}

export interface EbiosMeasure {
  id: string; study_id: string; scenario_id: string | null
  name: string; description: string | null; status: string
  iso_control_ref: string | null; control_group_id: string | null
  effectiveness: number | null; due_date: string | null
  owner: string | null; created_at: string
}

export interface EbiosSummary {
  total_studies: number; by_status: Record<string, number>
  total_feared_events: number; total_risk_sources: number
  total_scenarios: number; total_attack_paths: number; total_measures: number
}

export const ebiosApi = {
  summary: () => client.get<EbiosSummary>('/ebios/summary').then(r => r.data),
  list: (params?: { status?: string; project_id?: string }) =>
    client.get<EbiosStudy[]>('/ebios', { params }).then(r => r.data),
  get: (id: string) => client.get<EbiosStudy>(`/ebios/${id}`).then(r => r.data),
  create: (body: EbiosCreate) => client.post<EbiosStudy>('/ebios', body).then(r => r.data),
  update: (id: string, body: Partial<EbiosCreate>) => client.patch<EbiosStudy>(`/ebios/${id}`, body).then(r => r.data),
  delete: (id: string) => client.delete(`/ebios/${id}`),

  listFearedEvents: (studyId: string) => client.get<EbiosFearedEvent[]>(`/ebios/${studyId}/feared-events`).then(r => r.data),
  createFearedEvent: (studyId: string, body: object) => client.post(`/ebios/${studyId}/feared-events`, body).then(r => r.data),
  deleteFearedEvent: (studyId: string, feId: string) => client.delete(`/ebios/${studyId}/feared-events/${feId}`),

  listRiskSources: (studyId: string) => client.get<EbiosRiskSource[]>(`/ebios/${studyId}/risk-sources`).then(r => r.data),
  createRiskSource: (studyId: string, body: object) => client.post(`/ebios/${studyId}/risk-sources`, body).then(r => r.data),
  deleteRiskSource: (studyId: string, rsId: string) => client.delete(`/ebios/${studyId}/risk-sources/${rsId}`),

  listScenarios: (studyId: string) => client.get<EbiosScenario[]>(`/ebios/${studyId}/scenarios`).then(r => r.data),
  createScenario: (studyId: string, body: object) => client.post(`/ebios/${studyId}/scenarios`, body).then(r => r.data),
  deleteScenario: (studyId: string, scId: string) => client.delete(`/ebios/${studyId}/scenarios/${scId}`),

  listAttackPaths: (studyId: string) => client.get<EbiosAttackPath[]>(`/ebios/${studyId}/attack-paths`).then(r => r.data),
  createAttackPath: (studyId: string, body: object) => client.post(`/ebios/${studyId}/attack-paths`, body).then(r => r.data),
  deleteAttackPath: (studyId: string, apId: string) => client.delete(`/ebios/${studyId}/attack-paths/${apId}`),

  listMeasures: (studyId: string) => client.get<EbiosMeasure[]>(`/ebios/${studyId}/measures`).then(r => r.data),
  createMeasure: (studyId: string, body: object) => client.post(`/ebios/${studyId}/measures`, body).then(r => r.data),
  updateMeasure: (studyId: string, mId: string, body: object) => client.patch(`/ebios/${studyId}/measures/${mId}`, body).then(r => r.data),
  deleteMeasure: (studyId: string, mId: string) => client.delete(`/ebios/${studyId}/measures/${mId}`),
}
