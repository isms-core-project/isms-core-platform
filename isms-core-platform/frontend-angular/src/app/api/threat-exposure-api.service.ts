import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

export interface ExposedControl {
  control_code: string
  control_name: string | null
  framework_status: string | null
  assessment_score: number | null
  gap: boolean
}

export interface ExposureTechnique {
  mitre_tid: string
  ioc_count: number
  sources: string[]
  iso_controls: ExposedControl[]
  max_gap_score: number | null
}

export interface ThreatExposureResponse {
  technique_count: number
  affected_controls: number
  gap_controls: number
  items: ExposureTechnique[]
}

@Injectable({ providedIn: 'root' })
export class ThreatExposureApiService {
  private http = inject(HttpClient)

  get(): Observable<ThreatExposureResponse> {
    return this.http.get<ThreatExposureResponse>('/api/v1/threat-intel/exposure')
  }
}
