import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

export interface CompassRead {
  project_id: string
  frameworks: CompassFramework[]
  generated_at: string
}

export interface CompassFramework {
  framework_code: string
  framework_name: string
  total_controls: number
  mapped_controls: number
  coverage_pct: number
  avg_score: number | null
  status: string
}

@Injectable({ providedIn: 'root' })
export class CompassApiService {
  private http = inject(HttpClient)

  get(projectId: string): Observable<CompassRead> {
    return this.http.get<CompassRead>('/api/v1/compass/', {
      params: { project_id: projectId }
    })
  }
}
