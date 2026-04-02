import { client } from './client'

export interface MetricResult {
  name: string
  label: string
  value: number
  unit: 'percent' | 'numeric' | 'count'
  computed_at: string
}

export interface MetricHistory {
  name: string
  label: string
  unit: string
  history: { date: string; value: number }[]
}

export const metricsApi = {
  list: (params?: { project_id?: string }) =>
    client.get<MetricResult[]>('/metrics', { params }).then(r => r.data),

  get: (name: string, params?: { project_id?: string; days?: number }) =>
    client.get<MetricHistory>(`/metrics/${name}`, { params }).then(r => r.data),
}
