import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

export interface GlossaryEntry {
  id: string
  term: string
  definition: string
  product: string | null
  iso_reference: string | null
  created_at: string
}

@Injectable({ providedIn: 'root' })
export class GlossaryApiService {
  private http = inject(HttpClient)

  list(params?: { product?: string; search?: string }): Observable<GlossaryEntry[]> {
    return this.http.get<GlossaryEntry[]>('/api/v1/glossary/', { params })
  }
}
