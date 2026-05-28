import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'
import { CoverageMatrix } from '../shared/types'

export interface CoverageResult {
  matrices: CoverageMatrix[]
  product: string
  project_id: string
  generated_at: string
}

export interface InferenceResult {
  inferred: number
  duration_ms: number
}

@Injectable({ providedIn: 'root' })
export class CoverageApiService {
  private http = inject(HttpClient)

  get(projectId: string, product: string): Observable<CoverageResult> {
    return this.http.get<CoverageResult>('/api/v1/coverage/', {
      params: { project_id: projectId, product }
    })
  }

  infer(projectId: string): Observable<InferenceResult> {
    return this.http.post<InferenceResult>('/api/v1/coverage/infer', { project_id: projectId })
  }
}
