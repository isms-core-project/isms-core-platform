import { client } from './client'
import type { EvidenceRead, EvidenceUpdate } from './types'

export interface EvidenceAssign {
  group_code?: string
  control_group_id?: string
  require_approval?: boolean
}

export interface EvidenceReview {
  reason?: string
}

export const evidenceApi = {
  list: (params?: { control_group_id?: string; group_code?: string; evidence_type?: string; evidence_status?: string; limit?: number; offset?: number }) =>
    client.get<EvidenceRead[]>('/evidence/', { params }).then((r) => r.data),

  get: (id: string) =>
    client.get<EvidenceRead>(`/evidence/${id}`).then((r) => r.data),

  upload: (formData: FormData) =>
    client.post<EvidenceRead>('/evidence/upload', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    }).then((r) => r.data),

  bulkDraft: (formData: FormData) =>
    client.post<EvidenceRead[]>('/evidence/bulk-draft', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    }).then((r) => r.data),

  update: (id: string, data: EvidenceUpdate) =>
    client.patch<EvidenceRead>(`/evidence/${id}`, data).then((r) => r.data),

  assign: (id: string, data: EvidenceAssign) =>
    client.patch<EvidenceRead>(`/evidence/${id}/assign`, data).then((r) => r.data),

  submit: (id: string) =>
    client.patch<EvidenceRead>(`/evidence/${id}/submit`).then((r) => r.data),

  approve: (id: string, data?: EvidenceReview) =>
    client.patch<EvidenceRead>(`/evidence/${id}/approve`, data ?? {}).then((r) => r.data),

  reject: (id: string, data?: EvidenceReview) =>
    client.patch<EvidenceRead>(`/evidence/${id}/reject`, data ?? {}).then((r) => r.data),

  delete: (id: string) =>
    client.delete(`/evidence/${id}`),

  downloadUrl: (id: string) => `/api/v1/evidence/${id}/download`,

  exportCsvUrl: (params?: { group_code?: string; evidence_type?: string; evidence_status?: string }) => {
    const q = new URLSearchParams()
    if (params?.group_code) q.set('group_code', params.group_code)
    if (params?.evidence_type) q.set('evidence_type', params.evidence_type)
    if (params?.evidence_status) q.set('evidence_status', params.evidence_status)
    return `/api/v1/evidence/export${q.toString() ? '?' + q.toString() : ''}`
  },
}
