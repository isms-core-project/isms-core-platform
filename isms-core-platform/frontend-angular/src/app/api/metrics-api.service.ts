import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

export interface MetricSnapshot {
  id: string
  project_id: string
  snapshot_date: string
  total_controls: number
  controls_with_policy: number
  controls_with_impl: number
  controls_with_assessment: number
  controls_with_evidence: number
  open_gaps: number
  closed_gaps: number
  audit_readiness_score: number
  created_at: string
}

@Injectable({ providedIn: 'root' })
export class MetricsApiService {
  private http = inject(HttpClient)

  getSnapshots(projectId: string, days?: number): Observable<MetricSnapshot[]> {
    const params: Record<string, string | number> = { project_id: projectId }
    if (days !== undefined) params['days'] = days
    return this.http.get<MetricSnapshot[]>('/api/v1/metrics/snapshots', { params })
  }

  createSnapshot(projectId: string): Observable<MetricSnapshot> {
    return this.http.post<MetricSnapshot>('/api/v1/metrics/snapshots', { project_id: projectId })
  }
}
