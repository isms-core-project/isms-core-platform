import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'
import { ControlGroupList, ControlGroupRichDetail } from '../shared/types'

export interface FrameworkControlItem {
  id: string
  control_id: string
  title: string
  description: string | null
  level: number
  sort_order: number
  parent_id: string | null
  control_type: string[]
  security_properties: string[]
}

export interface FrameworkControlDetail extends FrameworkControlItem {
  framework_code: string
  framework_name: string
  mappings: {
    framework: string
    framework_code: string
    control_id: string
    control_title: string
    mapping_type: string
    confidence: number
  }[]
}

export interface ControlListParams {
  section?: string
  product?: string
  product_family?: string
}

@Injectable({ providedIn: 'root' })
export class ControlsApiService {
  private http = inject(HttpClient)

  list(params?: ControlListParams): Observable<ControlGroupList[]> {
    return this.http.get<ControlGroupList[]>('/api/v1/controls/', { params: params as Record<string, string> })
  }

  get(id: string): Observable<ControlGroupRichDetail> {
    return this.http.get<ControlGroupRichDetail>(`/api/v1/controls/${id}`)
  }

  getByCode(code: string): Observable<ControlGroupRichDetail> {
    return this.http.get<ControlGroupRichDetail>(`/api/v1/controls/code/${code}`)
  }

  listByFrameworkCode(code: string, level?: number): Observable<FrameworkControlItem[]> {
    const params: Record<string, string | number> = { code }
    if (level !== undefined) params['level'] = level
    return this.http.get<FrameworkControlItem[]>('/api/v1/frameworks/by-code/controls', { params })
  }

  getByFrameworkCode(code: string, controlId: string): Observable<FrameworkControlDetail> {
    return this.http.get<FrameworkControlDetail>('/api/v1/frameworks/by-code/control', {
      params: { code, control_id: controlId }
    })
  }
}
