import { client } from './client'

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

export const regulatoryApi = {
  listRequirements: (frameworkCode: string) =>
    client.get<Requirement[]>(`/regulatory/${frameworkCode}/requirements`).then(r => r.data),

  listAssessments: (frameworkCode: string) =>
    client.get<AssessmentSummary[]>(`/regulatory/${frameworkCode}/assessments`).then(r => r.data),

  createAssessment: (frameworkCode: string, data: {
    framework_code: string
    name: string
    description?: string
    assessor?: string
    scope?: string
    organisation?: string
  }) =>
    client.post<ComplianceAssessment>(`/regulatory/${frameworkCode}/assessments`, data).then(r => r.data),

  updateAssessment: (frameworkCode: string, id: string, data: Partial<ComplianceAssessment>) =>
    client.patch<ComplianceAssessment>(`/regulatory/${frameworkCode}/assessments/${id}`, data).then(r => r.data),

  deleteAssessment: (frameworkCode: string, id: string) =>
    client.delete(`/regulatory/${frameworkCode}/assessments/${id}`),

  getFullAssessment: (frameworkCode: string, id: string) =>
    client.get<FullAssessment>(`/regulatory/${frameworkCode}/assessments/${id}`).then(r => r.data),

  upsertRatings: (frameworkCode: string, id: string, ratings: RatingUpsert[]) =>
    client.put<ComplianceRating[]>(`/regulatory/${frameworkCode}/assessments/${id}/ratings`, ratings).then(r => r.data),
}
