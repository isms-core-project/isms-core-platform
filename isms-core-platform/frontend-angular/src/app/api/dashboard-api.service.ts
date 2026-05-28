import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'
import { DashboardOverview, AuditReadiness } from '../shared/types'

export interface ProductSummary {
  groups: number
  policies: number
  imps: number
  pol_coverage_pct: number
  impl_coverage_pct: number
  evidence_coverage_pct: number
  coverage_gaps: number
}

export interface HomeSummary {
  isms:       ProductSummary & { fw_coverage_pct: number; op_coverage_pct: number; open_gaps: number }
  privacy:    ProductSummary
  cloud:      ProductSummary
  ai:         ProductSummary
  connectors: { active: number; evidence_items: number }
}

export interface FrameworkOverview {
  framework_code: string
  framework_name: string
  total_controls: number
  controls_with_mappings: number
  total_mappings: number
  coverage_pct: number
  by_target_framework: Record<string, number>
  sections: { section: string; count: number; mapped_count: number }[]
  total_policies: number
  total_implementations: number
  total_assessments: number
}

export interface CoverageGap {
  id: string
  group_code: string
  name: string
  section: string
  section_name: string
  missing: string[]
}

export interface DashboardData {
  overview: DashboardOverview
  audit_readiness: AuditReadiness
}

@Injectable({ providedIn: 'root' })
export class DashboardApiService {
  private http = inject(HttpClient)

  get(projectId: string, product: string): Observable<DashboardData> {
    return this.http.get<DashboardData>('/api/v1/dashboard/', {
      params: { project_id: projectId, product }
    })
  }

  getOverview(projectId?: string | null): Observable<unknown> {
    const params: Record<string, string> = {}
    if (projectId) params['project_id'] = projectId
    return this.http.get('/api/v1/dashboard/overview', { params })
  }

  getAuditReadiness(projectId?: string | null): Observable<unknown> {
    const params: Record<string, string> = {}
    if (projectId) params['project_id'] = projectId
    return this.http.get('/api/v1/dashboard/audit-readiness', { params })
  }

  getHomeSummary(): Observable<HomeSummary> {
    return this.http.get<HomeSummary>('/api/v1/dashboard/home-summary')
  }

  getFrameworkOverview(sourceFramework: string): Observable<FrameworkOverview> {
    return this.http.get<FrameworkOverview>('/api/v1/dashboard/framework-overview', {
      params: { source_framework: sourceFramework }
    })
  }

  getCoverageGaps(product: 'framework' | 'operational'): Observable<CoverageGap[]> {
    return this.http.get<CoverageGap[]>('/api/v1/dashboard/coverage-gaps', { params: { product } })
  }
}
