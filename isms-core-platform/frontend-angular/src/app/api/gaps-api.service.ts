import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'
import { GapRead, GapCreate, GapPatch, EvidenceRead } from '../shared/types'

export interface GapListParams {
  severity?: string
  status?: string
  product?: string
  control_group_id?: string
  project_id?: string
  limit?: number
}

@Injectable({ providedIn: 'root' })
export class GapsApiService {
  private http = inject(HttpClient)

  list(params?: GapListParams): Observable<GapRead[]> {
    const p = params ? Object.fromEntries(Object.entries(params).filter(([, v]) => v != null && v !== '')) : {}
    return this.http.get<GapRead[]>('/api/v1/gaps/', { params: p as any })
  }

  create(data: GapCreate): Observable<GapRead> {
    return this.http.post<GapRead>('/api/v1/gaps/', data)
  }

  update(id: string, data: GapPatch): Observable<GapRead> {
    return this.http.patch<GapRead>(`/api/v1/gaps/${id}`, data)
  }

  delete(id: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/gaps/${id}`)
  }

  listEvidence(gapId: string): Observable<EvidenceRead[]> {
    return this.http.get<EvidenceRead[]>(`/api/v1/gaps/${gapId}/evidence`)
  }

  attachEvidence(gapId: string, evidenceId: string): Observable<GapRead> {
    return this.http.post<GapRead>(`/api/v1/gaps/${gapId}/evidence/${evidenceId}`, {})
  }

  detachEvidence(gapId: string, evidenceId: string): Observable<GapRead> {
    return this.http.delete<GapRead>(`/api/v1/gaps/${gapId}/evidence/${evidenceId}`)
  }
}
