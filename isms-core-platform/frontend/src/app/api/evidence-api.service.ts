import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'
import { EvidenceRead, EvidenceUpdate } from '../shared/types'

export interface EvidenceListParams {
  control_group_id?: string
  project_id?: string
  evidence_type?: string
  evidence_status?: string
  limit?: number
  offset?: number
}

@Injectable({ providedIn: 'root' })
export class EvidenceApiService {
  private http = inject(HttpClient)

  list(params?: EvidenceListParams): Observable<EvidenceRead[]> {
    return this.http.get<EvidenceRead[]>('/api/v1/evidence/', { params: params as Record<string, string | number> })
  }

  get(id: string): Observable<EvidenceRead> {
    return this.http.get<EvidenceRead>(`/api/v1/evidence/${id}`)
  }

  create(data: FormData): Observable<EvidenceRead> {
    return this.http.post<EvidenceRead>('/api/v1/evidence/', data)
  }

  upload(data: FormData): Observable<EvidenceRead> {
    return this.http.post<EvidenceRead>('/api/v1/evidence/upload', data)
  }

  update(id: string, data: EvidenceUpdate): Observable<EvidenceRead> {
    return this.http.patch<EvidenceRead>(`/api/v1/evidence/${id}`, data)
  }

  delete(id: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/evidence/${id}`)
  }

  approve(id: string): Observable<EvidenceRead> {
    return this.http.post<EvidenceRead>(`/api/v1/evidence/${id}/approve`, {})
  }

  reject(id: string, reason: string): Observable<EvidenceRead> {
    return this.http.post<EvidenceRead>(`/api/v1/evidence/${id}/reject`, { reason })
  }

  archive(id: string): Observable<EvidenceRead> {
    return this.http.post<EvidenceRead>(`/api/v1/evidence/${id}/archive`, {})
  }

  getDownloadUrl(id: string): string {
    return `/api/v1/evidence/${id}/download`
  }
}
