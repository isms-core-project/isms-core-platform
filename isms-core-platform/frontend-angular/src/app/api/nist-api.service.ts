import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

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

@Injectable({ providedIn: 'root' })
export class NistApiService {
  private http = inject(HttpClient)

  listProfiles(): Observable<NistProfileSummary[]> {
    return this.http.get<NistProfileSummary[]>('/api/v1/nist/profiles')
  }

  createProfile(data: { name: string; description?: string; assessor?: string; scope?: string }): Observable<NistProfile> {
    return this.http.post<NistProfile>('/api/v1/nist/profiles', data)
  }

  updateProfile(id: string, data: Partial<NistProfile>): Observable<NistProfile> {
    return this.http.patch<NistProfile>(`/api/v1/nist/profiles/${id}`, data)
  }

  deleteProfile(id: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/nist/profiles/${id}`)
  }

  getFullProfile(id: string): Observable<NistFullProfile> {
    return this.http.get<NistFullProfile>(`/api/v1/nist/profiles/${id}`)
  }

  getProfileSummary(id: string): Observable<NistProfileSummary> {
    return this.http.get<NistProfileSummary>(`/api/v1/nist/profiles/${id}/summary`)
  }

  upsertRatings(id: string, ratings: NistRatingUpsert[]): Observable<NistRating[]> {
    return this.http.put<NistRating[]>(`/api/v1/nist/profiles/${id}/ratings`, ratings)
  }

  exportCsv(id: string): Observable<Blob> {
    return this.http.get(`/api/v1/nist/profiles/${id}/export`, { responseType: 'blob' }) as Observable<Blob>
  }

  exportXlsx(id: string): Observable<Blob> {
    return this.http.get(`/api/v1/nist/profiles/${id}/export/xlsx`, { responseType: 'blob' }) as Observable<Blob>
  }

  importXlsx(id: string, file: File): Observable<NistImportResult> {
    const form = new FormData()
    form.append('file', file)
    return this.http.post<NistImportResult>(`/api/v1/nist/profiles/${id}/import`, form)
  }

  listSubcategories(): Observable<NistSubcategory[]> {
    return this.http.get<NistSubcategory[]>('/api/v1/nist/subcategories')
  }
}
