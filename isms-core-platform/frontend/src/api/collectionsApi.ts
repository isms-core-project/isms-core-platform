import { client } from './client'

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

const BASE = '/api/v1/collections'

export const collectionsApi = {
  list: (params?: { product_family?: string }) =>
    client.get<CollectionListItem[]>(BASE, { params }).then(r => r.data),

  get: (id: string) =>
    client.get<CollectionRead>(`${BASE}/${id}`).then(r => r.data),

  create: (body: CollectionCreate) =>
    client.post<CollectionRead>(BASE, body).then(r => r.data),

  patch: (id: string, body: Partial<{ name: string; description: string; due_date: string }>) =>
    client.patch<CollectionRead>(`${BASE}/${id}`, body).then(r => r.data),

  delete: (id: string) =>
    client.delete(`${BASE}/${id}`),

  addAssessment: (collectionId: string, assessmentId: string) =>
    client.post(`${BASE}/${collectionId}/assessments/${assessmentId}`),

  removeAssessment: (collectionId: string, assessmentId: string) =>
    client.delete(`${BASE}/${collectionId}/assessments/${assessmentId}`),

  exportUrl: (id: string, format: 'csv' | 'xlsx' | 'pdf') =>
    `${BASE}/${id}/export/${format}`,
}
