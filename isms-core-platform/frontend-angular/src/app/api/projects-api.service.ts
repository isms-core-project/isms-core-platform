import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'
import { ProjectRead } from '../shared/types'

export interface ProjectDetail extends ProjectRead {
  members: ProjectMemberRead[]
  evidence_count: number
  gap_count: number
  assessment_count: number
}

export interface ProjectCreate {
  name: string
  description?: string
  product_family: string
}

export interface ProjectUpdate {
  name?: string
  description?: string | null
  status?: string
  owner?: string | null
}

export interface ProjectListParams {
  product_family?: string
  status?: string
}

export interface ProjectMemberRead {
  id: string
  user_id: string
  email: string
  full_name: string | null
  role: string
  joined_at: string
}

@Injectable({ providedIn: 'root' })
export class ProjectsApiService {
  private http = inject(HttpClient)

  list(params?: ProjectListParams): Observable<ProjectRead[]> {
    const p = params ? Object.fromEntries(Object.entries(params).filter(([, v]) => v != null && v !== '')) : {}
    return this.http.get<ProjectRead[]>('/api/v1/projects', { params: p as any })
  }

  get(id: string): Observable<ProjectDetail> {
    return this.http.get<ProjectDetail>(`/api/v1/projects/${id}`)
  }

  create(data: ProjectCreate): Observable<ProjectRead> {
    return this.http.post<ProjectRead>('/api/v1/projects', data)
  }

  update(id: string, data: ProjectUpdate): Observable<ProjectRead> {
    return this.http.patch<ProjectRead>(`/api/v1/projects/${id}`, data)
  }

  delete(id: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/projects/${id}`)
  }

  archive(id: string): Observable<ProjectRead> {
    return this.http.post<ProjectRead>(`/api/v1/projects/${id}/archive`, {})
  }

  listMembers(projectId: string): Observable<ProjectMemberRead[]> {
    return this.http.get<ProjectMemberRead[]>(`/api/v1/projects/${projectId}/members`)
  }

  addMember(projectId: string, userId: string, role: string): Observable<ProjectMemberRead> {
    return this.http.post<ProjectMemberRead>(`/api/v1/projects/${projectId}/members`, { user_id: userId, role })
  }

  removeMember(projectId: string, userId: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/projects/${projectId}/members/${userId}`)
  }
}
