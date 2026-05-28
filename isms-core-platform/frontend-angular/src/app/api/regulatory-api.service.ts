import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

export interface Requirement {
  id: string
  control_id: string
  title: string
  description: string | null
  level: number
  sort_order: number
  group_id: string | null
  group_title: string | null
}

export interface ComplianceAssessment {
  id: string
  framework_code: string
  name: string
  description: string | null
  assessor: string | null
  scope: string | null
  organisation: string | null
  status: 'draft' | 'in_progress' | 'complete'
  created_at: string
  updated_at: string
  project_id: string | null
}

export interface AssessmentSummary extends ComplianceAssessment {
  rated_count: number
  total_requirements: number
  avg_current_score: number | null
  avg_target_score: number | null
  compliant_count: number
  partial_count: number
  non_compliant_count: number
  not_applicable_count: number
}

export interface ComplianceRating {
  id: string
  assessment_id: string
  requirement_id: string
  requirement_control_id: string
  requirement_title: string
  group_id: string | null
  current_score: number | null
  target_score: number | null
  rating_status: string
  notes: string | null
  evidence_ref: string | null
  updated_at: string
}

export interface RatingUpsert {
  requirement_id: string
  current_score: number | null
  target_score: number | null
  rating_status: string
  notes?: string | null
  evidence_ref?: string | null
}

export interface FullAssessment {
  assessment: ComplianceAssessment
  requirements: Requirement[]
  ratings: ComplianceRating[]
}

export interface AssessmentCreate {
  framework_code: string
  name: string
  description?: string
  assessor?: string
  scope?: string
  organisation?: string
  project_id?: string | null
}

@Injectable({ providedIn: 'root' })
export class RegulatoryApiService {
  private http = inject(HttpClient)

  listRequirements(frameworkCode: string): Observable<Requirement[]> {
    return this.http.get<Requirement[]>(`/api/v1/regulatory/${frameworkCode}/requirements`)
  }

  listAssessments(frameworkCode: string, params?: { project_id?: string }): Observable<AssessmentSummary[]> {
    return this.http.get<AssessmentSummary[]>(`/api/v1/regulatory/${frameworkCode}/assessments`, { params })
  }

  createAssessment(frameworkCode: string, data: AssessmentCreate): Observable<ComplianceAssessment> {
    return this.http.post<ComplianceAssessment>(`/api/v1/regulatory/${frameworkCode}/assessments`, data)
  }

  updateAssessment(frameworkCode: string, id: string, data: Partial<ComplianceAssessment>): Observable<ComplianceAssessment> {
    return this.http.patch<ComplianceAssessment>(`/api/v1/regulatory/${frameworkCode}/assessments/${id}`, data)
  }

  deleteAssessment(frameworkCode: string, id: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/regulatory/${frameworkCode}/assessments/${id}`)
  }

  getFullAssessment(frameworkCode: string, id: string): Observable<FullAssessment> {
    return this.http.get<FullAssessment>(`/api/v1/regulatory/${frameworkCode}/assessments/${id}`)
  }

  upsertRatings(frameworkCode: string, id: string, ratings: RatingUpsert[]): Observable<ComplianceRating[]> {
    return this.http.put<ComplianceRating[]>(`/api/v1/regulatory/${frameworkCode}/assessments/${id}/ratings`, ratings)
  }
}
