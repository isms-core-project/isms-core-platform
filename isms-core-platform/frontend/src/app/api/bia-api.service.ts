import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

export interface BIARecord {
  id: string
  org_id: string
  project_id: string | null
  asset_name: string
  asset_type: string
  rto_hours: number | null
  rpo_hours: number | null
  mtpd_hours: number | null
  financial_impact: number | null
  operational_impact: number | null
  reputational_impact: number | null
  regulatory_impact: number | null
  avg_impact: number
  recovery_tested: boolean
  last_tested_date: string | null
  continuity_plan_ref: string | null
  notes: string | null
  created_at: string
}

export interface BIACreate {
  asset_name: string
  asset_type?: string
  project_id?: string
  rto_hours?: number
  rpo_hours?: number
  mtpd_hours?: number
  financial_impact?: number
  operational_impact?: number
  reputational_impact?: number
  regulatory_impact?: number
  recovery_tested?: boolean
  last_tested_date?: string
  continuity_plan_ref?: string
  notes?: string
}

export interface BIASummary {
  total: number
  tested: number
  tested_pct: number
  rto_missing: number
  high_impact: number
}

@Injectable({ providedIn: 'root' })
export class BiaApiService {
  private http = inject(HttpClient)

  summary(params?: { project_id?: string }): Observable<BIASummary> {
    return this.http.get<BIASummary>('/api/v1/bia/summary', { params })
  }

  list(params?: { project_id?: string; asset_type?: string }): Observable<BIARecord[]> {
    return this.http.get<BIARecord[]>('/api/v1/bia', { params })
  }

  create(body: BIACreate): Observable<BIARecord> {
    return this.http.post<BIARecord>('/api/v1/bia', body)
  }

  update(id: string, body: Partial<BIACreate>): Observable<BIARecord> {
    return this.http.patch<BIARecord>(`/api/v1/bia/${id}`, body)
  }

  delete(id: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/bia/${id}`)
  }
}
