import { client } from './client'

export interface CompassGap {
  topic: string
  severity: 'high' | 'medium' | 'low'
  description: string
  iso_clause: string
  recommendation: string
}

export interface CompassStrength {
  topic: string
  detail: string
}

export interface CompassReport {
  control_group_code: string
  control_group_name: string
  coverage_score: number
  summary: string
  strengths: CompassStrength[]
  gaps: CompassGap[]
  disclaimer: string
  model_used: string
  tokens_used: number
}

export const compassApi = {
  status: () =>
    client.get<{ available: boolean; model: string }>('/compass/status').then((r) => r.data),

  analyse: (group_code: string, document_text: string) =>
    client
      .post<CompassReport>('/compass/analyse', { group_code, document_text })
      .then((r) => r.data),
}
