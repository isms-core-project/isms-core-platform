import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

export interface PolicyRead {
  id: string
  document_id: string
  title: string
  policy_type: string
  product_type: string
  control_group_id: string | null
  group_code: string | null
  group_name: string | null
  source_label: string | null
  language: string | null
  word_count: number
  requirements_count: number
  is_published: boolean
  published_at: string | null
  created_at: string
  updated_at: string
}

export interface PolicyDetail extends PolicyRead {
  content: string
  requirements: PolicyRequirement[]
}

export interface PolicyContentResponse {
  document_id: string
  title: string
  policy_type: string
  content: string
  country: string | null
}

export interface PolicyRequirement {
  id: string
  req_code: string
  text: string
  priority: string
}

export interface PolicyListParams {
  product?: string
  policy_type?: string
  control_group_id?: string
  project_id?: string
}

export interface PolicyUpdate {
  title?: string
  content?: string
}

export interface ImportExternalResult {
  document_id: string
  title: string
  word_count: number
  requirements_extracted: number
}

@Injectable({ providedIn: 'root' })
export class PoliciesApiService {
  private http = inject(HttpClient)

  list(params?: PolicyListParams): Observable<PolicyRead[]> {
    const p = params ? Object.fromEntries(Object.entries(params).filter(([, v]) => v != null && v !== '')) : {}
    return this.http.get<PolicyRead[]>('/api/v1/policies/', { params: p as any })
  }

  get(id: string): Observable<PolicyDetail> {
    return this.http.get<PolicyDetail>(`/api/v1/policies/${id}`)
  }

  getContent(id: string): Observable<PolicyContentResponse> {
    return this.http.get<PolicyContentResponse>(`/api/v1/policies/${id}/content`)
  }

  getImplContent(id: string): Observable<PolicyContentResponse> {
    return this.http.get<PolicyContentResponse>(`/api/v1/implementations/${id}/content`)
  }

  update(id: string, data: PolicyUpdate): Observable<PolicyRead> {
    return this.http.patch<PolicyRead>(`/api/v1/policies/${id}`, data)
  }

  publish(id: string): Observable<PolicyRead> {
    return this.http.post<PolicyRead>(`/api/v1/policies/${id}/publish`, {})
  }

  delete(id: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/policies/${id}`)
  }

  importExternal(file: File, groupCode: string, sourceLabel: string, language: string): Observable<ImportExternalResult> {
    const form = new FormData()
    form.append('file', file)
    form.append('group_code', groupCode)
    form.append('source_label', sourceLabel)
    form.append('language', language)
    return this.http.post<ImportExternalResult>('/api/v1/admin/import-external', form)
  }
}
