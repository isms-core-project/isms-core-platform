import { client } from './client'

export interface NistProfile {
  id: string
  name: string
  description: string | null
  assessor: string | null
  scope: string | null
  status: 'draft' | 'in_progress' | 'complete'
  created_at: string
  updated_at: string
}

export interface FunctionScore {
  function_code: string
  function_name: string
  avg_current: number | null
  avg_target: number | null
  rated_count: number
  total_count: number
}

export interface NistProfileSummary extends NistProfile {
  rated_count: number
  total_subcategories: number
  avg_current_tier: number | null
  avg_target_tier: number | null
  function_scores: FunctionScore[]
}

export interface NistRating {
  id: string
  profile_id: string
  subcategory_id: string
  subcategory_code: string
  subcategory_title: string
  function_code: string
  category_code: string
  current_tier: number | null
  target_tier: number | null
  notes: string | null
  iso_mappings: string[]
}

export interface NistFullProfile {
  profile: NistProfile
  ratings: NistRating[]
}

export interface NistRatingUpsert {
  subcategory_id: string
  current_tier: number | null
  target_tier: number | null
  notes?: string | null
}

export interface NistImportResult {
  imported: number
  skipped: number
  not_found: string[]
}

export interface NistSubcategory {
  id: string
  control_id: string
  title: string
  function_code: string
  category_code: string
  sort_order: number
  iso_mappings: string[]
}

export const nistApi = {
  listProfiles: () =>
    client.get<NistProfileSummary[]>('/nist/profiles').then(r => r.data),

  createProfile: (data: { name: string; description?: string; assessor?: string; scope?: string }) =>
    client.post<NistProfile>('/nist/profiles', data).then(r => r.data),

  updateProfile: (id: string, data: Partial<NistProfile>) =>
    client.patch<NistProfile>(`/nist/profiles/${id}`, data).then(r => r.data),

  deleteProfile: (id: string) =>
    client.delete(`/nist/profiles/${id}`),

  getFullProfile: (id: string) =>
    client.get<NistFullProfile>(`/nist/profiles/${id}`).then(r => r.data),

  getProfileSummary: (id: string) =>
    client.get<NistProfileSummary>(`/nist/profiles/${id}/summary`).then(r => r.data),

  upsertRatings: (id: string, ratings: NistRatingUpsert[]) =>
    client.put<NistRating[]>(`/nist/profiles/${id}/ratings`, ratings).then(r => r.data),

  exportCsv: (id: string) =>
    client.get(`/nist/profiles/${id}/export`, { responseType: 'blob' }).then(r => r.data as Blob),

  exportXlsx: (id: string) =>
    client.get(`/nist/profiles/${id}/export/xlsx`, { responseType: 'blob' }).then(r => r.data as Blob),

  importXlsx: (id: string, file: File) => {
    const form = new FormData()
    form.append('file', file)
    return client.post<NistImportResult>(`/nist/profiles/${id}/import`, form, {
      headers: { 'Content-Type': 'multipart/form-data' },
    }).then(r => r.data)
  },

  listSubcategories: () =>
    client.get<NistSubcategory[]>('/nist/subcategories').then(r => r.data),
}
