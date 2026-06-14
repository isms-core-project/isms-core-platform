import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

export interface EbiosStudy {
  id: string
  org_id: string
  project_id: string | null
  name: string
  description: string | null
  scope: string | null
  status: string
  owner: string | null
  started_at: string | null
  reviewed_at: string | null
  created_at: string
  updated_at: string
}

export interface EbiosCreate {
  name: string
  description?: string
  scope?: string
  status?: string
  owner?: string
  project_id?: string
  started_at?: string
  reviewed_at?: string
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
  total_studies: number
  by_status: Record<string, number>
  total_feared_events: number
  total_risk_sources: number
  total_scenarios: number
  total_attack_paths: number
  total_measures: number
}

@Injectable({ providedIn: 'root' })
export class EbiosApiService {
  private http = inject(HttpClient)

  summary(): Observable<EbiosSummary> {
    return this.http.get<EbiosSummary>('/api/v1/ebios/summary')
  }

  list(params?: { status?: string; project_id?: string }): Observable<EbiosStudy[]> {
    return this.http.get<EbiosStudy[]>('/api/v1/ebios', { params })
  }

  get(id: string): Observable<EbiosStudy> {
    return this.http.get<EbiosStudy>(`/api/v1/ebios/${id}`)
  }

  create(body: EbiosCreate): Observable<EbiosStudy> {
    return this.http.post<EbiosStudy>('/api/v1/ebios', body)
  }

  update(id: string, body: Partial<EbiosCreate>): Observable<EbiosStudy> {
    return this.http.patch<EbiosStudy>(`/api/v1/ebios/${id}`, body)
  }

  delete(id: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/ebios/${id}`)
  }

  listFearedEvents(studyId: string): Observable<EbiosFearedEvent[]> {
    return this.http.get<EbiosFearedEvent[]>(`/api/v1/ebios/${studyId}/feared-events`)
  }

  createFearedEvent(studyId: string, body: object): Observable<EbiosFearedEvent> {
    return this.http.post<EbiosFearedEvent>(`/api/v1/ebios/${studyId}/feared-events`, body)
  }

  deleteFearedEvent(studyId: string, feId: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/ebios/${studyId}/feared-events/${feId}`)
  }

  listRiskSources(studyId: string): Observable<EbiosRiskSource[]> {
    return this.http.get<EbiosRiskSource[]>(`/api/v1/ebios/${studyId}/risk-sources`)
  }

  createRiskSource(studyId: string, body: object): Observable<EbiosRiskSource> {
    return this.http.post<EbiosRiskSource>(`/api/v1/ebios/${studyId}/risk-sources`, body)
  }

  deleteRiskSource(studyId: string, rsId: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/ebios/${studyId}/risk-sources/${rsId}`)
  }

  listScenarios(studyId: string): Observable<EbiosScenario[]> {
    return this.http.get<EbiosScenario[]>(`/api/v1/ebios/${studyId}/scenarios`)
  }

  createScenario(studyId: string, body: object): Observable<EbiosScenario> {
    return this.http.post<EbiosScenario>(`/api/v1/ebios/${studyId}/scenarios`, body)
  }

  deleteScenario(studyId: string, scId: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/ebios/${studyId}/scenarios/${scId}`)
  }

  listAttackPaths(studyId: string): Observable<EbiosAttackPath[]> {
    return this.http.get<EbiosAttackPath[]>(`/api/v1/ebios/${studyId}/attack-paths`)
  }

  createAttackPath(studyId: string, body: object): Observable<EbiosAttackPath> {
    return this.http.post<EbiosAttackPath>(`/api/v1/ebios/${studyId}/attack-paths`, body)
  }

  deleteAttackPath(studyId: string, apId: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/ebios/${studyId}/attack-paths/${apId}`)
  }

  listMeasures(studyId: string): Observable<EbiosMeasure[]> {
    return this.http.get<EbiosMeasure[]>(`/api/v1/ebios/${studyId}/measures`)
  }

  createMeasure(studyId: string, body: object): Observable<EbiosMeasure> {
    return this.http.post<EbiosMeasure>(`/api/v1/ebios/${studyId}/measures`, body)
  }

  updateMeasure(studyId: string, mId: string, body: object): Observable<EbiosMeasure> {
    return this.http.patch<EbiosMeasure>(`/api/v1/ebios/${studyId}/measures/${mId}`, body)
  }

  deleteMeasure(studyId: string, mId: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/ebios/${studyId}/measures/${mId}`)
  }
}
