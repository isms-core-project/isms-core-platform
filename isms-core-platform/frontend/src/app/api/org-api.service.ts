import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'
import { OrganisationRead } from '../shared/types'

export interface OrganisationUpdate {
  name?: string
  description?: string
  governance_mode?: string
  privacy_role?: string
  country?: string
  settings?: Record<string, unknown>
}

export interface OrganisationCreate {
  name: string
  slug: string
  description?: string
  governance_mode?: string
  country?: string | null
}

export interface OrganisationPatch {
  name?: string
  description?: string
  governance_mode?: string
  country?: string | null
  settings?: Record<string, unknown>
}

@Injectable({ providedIn: 'root' })
export class OrgApiService {
  private http = inject(HttpClient)

  // Current org (tenant-scoped)
  get(): Observable<OrganisationRead> {
    return this.http.get<OrganisationRead>('/api/v1/organisation/')
  }

  update(data: OrganisationUpdate): Observable<OrganisationRead> {
    return this.http.patch<OrganisationRead>('/api/v1/organisation/', data)
  }

  // Super-admin: all orgs
  list(): Observable<OrganisationRead[]> {
    return this.http.get<OrganisationRead[]>('/api/v1/organisation/all')
  }

  create(body: OrganisationCreate): Observable<OrganisationRead> {
    return this.http.post<OrganisationRead>('/api/v1/organisation/', body)
  }

  getById(id: string): Observable<OrganisationRead> {
    return this.http.get<OrganisationRead>(`/api/v1/organisation/${id}`)
  }

  updateById(id: string, body: OrganisationPatch): Observable<OrganisationRead> {
    return this.http.patch<OrganisationRead>(`/api/v1/organisation/${id}`, body)
  }

  archiveById(id: string): Observable<OrganisationRead> {
    return this.http.patch<OrganisationRead>(`/api/v1/organisation/${id}/archive`, {})
  }

  deleteById(id: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/organisation/${id}`)
  }
}
