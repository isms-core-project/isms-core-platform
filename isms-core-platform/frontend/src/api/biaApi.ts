import { client } from './client'

export interface BIARecord {
  id: string; org_id: string; project_id: string | null
  asset_name: string; asset_type: string
  rto_hours: number | null; rpo_hours: number | null; mtpd_hours: number | null
  financial_impact: number | null; operational_impact: number | null
  reputational_impact: number | null; regulatory_impact: number | null
  avg_impact: number; recovery_tested: boolean
  last_tested_date: string | null; continuity_plan_ref: string | null
  notes: string | null; created_at: string
}

export interface BIACreate {
  asset_name: string; asset_type?: string; project_id?: string
  rto_hours?: number; rpo_hours?: number; mtpd_hours?: number
  financial_impact?: number; operational_impact?: number
  reputational_impact?: number; regulatory_impact?: number
  recovery_tested?: boolean; last_tested_date?: string
  continuity_plan_ref?: string; notes?: string
}

export interface BIASummary {
  total: number; tested: number; tested_pct: number
  rto_missing: number; high_impact: number
}

export const biaApi = {
  summary: (params?: { project_id?: string }) =>
    client.get<BIASummary>('/bia/summary', { params }).then(r => r.data),
  list: (params?: { project_id?: string; asset_type?: string }) =>
    client.get<BIARecord[]>('/bia', { params }).then(r => r.data),
  create: (body: BIACreate) => client.post<BIARecord>('/bia', body).then(r => r.data),
  update: (id: string, body: Partial<BIACreate>) => client.patch<BIARecord>(`/bia/${id}`, body).then(r => r.data),
  delete: (id: string) => client.delete(`/bia/${id}`),
}
