import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

export interface CollectionStats {
  total: number
  started: number
  completion_pct: number
  items_total: number
  items_compliant: number
  items_non_compliant: number
  compliance_pct: number
  status: 'not_started' | 'in_progress' | 'complete'
}

export interface CollectionMember {
  assessment_id: string
  document_id: string
  workbook_name: string
  group_code: string
  group_name: string
  product_type: string
  items_total: number
  items_compliant: number
  items_non_compliant: number
  compliance_pct: number
}

export interface CollectionListItem {
  id: string
  name: string
  description: string | null
  product_family: string
  product_type: string | null
  due_date: string | null
  created_at: string
  updated_at: string
  stats: CollectionStats
}

export interface CollectionRead extends CollectionListItem {
  members: CollectionMember[]
}

export interface CollectionCreate {
  name: string
  description?: string
  product_family: string
  product_type?: string
  due_date?: string
}

@Injectable({ providedIn: 'root' })
export class CollectionsApiService {
  private http = inject(HttpClient)

  list(params?: { product_family?: string }): Observable<CollectionListItem[]> {
    return this.http.get<CollectionListItem[]>('/api/v1/collections', { params })
  }

  get(id: string): Observable<CollectionRead> {
    return this.http.get<CollectionRead>(`/api/v1/collections/${id}`)
  }

  create(body: CollectionCreate): Observable<CollectionRead> {
    return this.http.post<CollectionRead>('/api/v1/collections', body)
  }

  patch(id: string, body: Partial<{ name: string; description: string; due_date: string }>): Observable<CollectionRead> {
    return this.http.patch<CollectionRead>(`/api/v1/collections/${id}`, body)
  }

  delete(id: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/collections/${id}`)
  }

  addAssessment(collectionId: string, assessmentId: string): Observable<void> {
    return this.http.post<void>(`/api/v1/collections/${collectionId}/assessments/${assessmentId}`, {})
  }

  removeAssessment(collectionId: string, assessmentId: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/collections/${collectionId}/assessments/${assessmentId}`)
  }

  exportUrl(id: string, format: 'csv' | 'xlsx' | 'pdf'): string {
    return `/api/v1/collections/${id}/export/${format}`
  }
}
