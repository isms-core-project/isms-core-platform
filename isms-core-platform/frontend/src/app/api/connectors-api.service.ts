import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

export interface ConnectorRead {
  id: string
  name: string
  source_system: string
  status: string
  last_run: string | null
  last_item_count: number | null
  sync_requested_at: string | null
  last_error: string | null
  last_error_at: string | null
  evidence_count: number
  retention_days: number | null
  created_at: string
}

export interface ConnectorRegistered extends ConnectorRead {
  api_token: string
}

export interface ConnectorRegisterPayload {
  name: string
  source_system: string
}

export interface ConnectorLogEntry {
  id: string
  event_type: string
  severity: string
  description: string | null
  created_at: string
}

export interface ConnectorEvidenceRead {
  id: string
  connector_id: string
  control_group_id: string
  group_code: string | null
  source_ref: string | null
  title: string
  classification: string | null
  status: string | null
  event_date: string | null
  created_at: string
  raw: Record<string, unknown> | null
}

@Injectable({ providedIn: 'root' })
export class ConnectorsApiService {
  private http = inject(HttpClient)

  list(): Observable<ConnectorRead[]> {
    return this.http.get<ConnectorRead[]>('/api/v1/connectors/')
  }

  get(id: string): Observable<ConnectorRead> {
    return this.http.get<ConnectorRead>(`/api/v1/connectors/${id}`)
  }

  register(data: ConnectorRegisterPayload): Observable<ConnectorRegistered> {
    return this.http.post<ConnectorRegistered>('/api/v1/connectors/', data)
  }

  delete(id: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/connectors/${id}`)
  }

  trigger(id: string): Observable<void> {
    return this.http.post<void>(`/api/v1/connectors/${id}/trigger`, {})
  }

  rotateToken(id: string): Observable<{ api_token: string }> {
    return this.http.post<{ api_token: string }>(`/api/v1/connectors/${id}/rotate-token`, {})
  }

  getLogs(id: string, limit?: number): Observable<ConnectorLogEntry[]> {
    const params: Record<string, number> = {}
    if (limit !== undefined) params['limit'] = limit
    return this.http.get<ConnectorLogEntry[]>(`/api/v1/connectors/${id}/logs`, { params })
  }

  getEvidence(id: string, params?: { limit?: number; offset?: number }): Observable<ConnectorEvidenceRead[]> {
    return this.http.get<ConnectorEvidenceRead[]>(`/api/v1/connectors/${id}/evidence`, { params })
  }

  archiveEvidence(id: string, retentionDays: number): Observable<{ archived: number }> {
    return this.http.post<{ archived: number }>(`/api/v1/connectors/${id}/archive`, { retention_days: retentionDays })
  }
}
