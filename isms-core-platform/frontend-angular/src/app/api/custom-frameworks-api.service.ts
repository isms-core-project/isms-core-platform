import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

export interface CustomFramework {
  id: string
  org_id: string
  name: string
  short_code: string
  version: string
  description: string | null
  control_count: number
  status: string
  created_at: string
  updated_at: string
}

export interface CustomControl {
  id: string
  framework_id: string
  control_id: string
  title: string
  description: string | null
  category: string | null
  subcategory: string | null
  priority: string | null
  iso_mappings: string[]
  tags: string[]
  created_at: string
}

export interface CustomFrameworkDetail extends CustomFramework {
  controls: CustomControl[]
}

@Injectable({ providedIn: 'root' })
export class CustomFrameworksApiService {
  private http = inject(HttpClient)

  list(): Observable<CustomFramework[]> {
    return this.http.get<CustomFramework[]>('/api/v1/custom-frameworks')
  }

  get(id: string): Observable<CustomFrameworkDetail> {
    return this.http.get<CustomFrameworkDetail>(`/api/v1/custom-frameworks/${id}`)
  }

  importYaml(yaml_content: string): Observable<CustomFramework> {
    return this.http.post<CustomFramework>('/api/v1/custom-frameworks', { yaml_content })
  }

  delete(id: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/custom-frameworks/${id}`)
  }

  listControls(id: string, params?: { category?: string; search?: string }): Observable<CustomControl[]> {
    return this.http.get<CustomControl[]>(`/api/v1/custom-frameworks/${id}/controls`, { params })
  }
}
