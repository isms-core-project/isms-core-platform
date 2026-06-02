import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'
import { SearchResponse } from '../shared/types'

export interface SearchParams {
  q: string
  doc_type?: string
  control_group?: string
  product?: string
  limit?: number
  offset?: number
}

@Injectable({ providedIn: 'root' })
export class SearchApiService {
  private http = inject(HttpClient)

  search(params: SearchParams): Observable<SearchResponse> {
    const clean = Object.fromEntries(
      Object.entries(params).filter(([, v]) => v !== undefined && v !== null)
    ) as Record<string, string | number>
    return this.http.get<SearchResponse>('/api/v1/search', { params: clean })
  }

  status(): Observable<{ available: boolean }> {
    return this.http.get<{ available: boolean }>('/api/v1/search/status')
  }
}
