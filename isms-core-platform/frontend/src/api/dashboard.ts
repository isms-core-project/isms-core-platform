import { client } from './client'
import type {
  DashboardOverview,
  CoverageMatrix,
  GapSummary,
  EvidenceSummary,
  AuditReadiness,
} from './types'

export const dashboardApi = {
  getOverview: () =>
    client.get<DashboardOverview>('/dashboard/overview').then((r) => r.data),

  getCoverage: (params?: { source_framework?: string; target_framework?: string }) =>
    client.get<CoverageMatrix>('/dashboard/coverage', { params }).then((r) => r.data),

  getGaps: (params?: { severity?: string; status?: string; product?: string; limit?: number }) =>
    client.get<GapSummary>('/dashboard/gaps', { params }).then((r) => r.data),

  getEvidence: () =>
    client.get<EvidenceSummary>('/dashboard/evidence').then((r) => r.data),

  getAuditReadiness: () =>
    client.get<AuditReadiness>('/dashboard/audit-readiness').then((r) => r.data),

  getCoverageGaps: (product: 'framework' | 'operational') =>
    client.get<CoverageGap[]>('/dashboard/coverage-gaps', { params: { product } }).then((r) => r.data),

  getFrameworkOverview: (source_framework: string) =>
    client.get<FrameworkOverview>('/dashboard/framework-overview', { params: { source_framework } }).then((r) => r.data),

  getHomeSummary: () =>
    client.get<HomeSummary>('/dashboard/home-summary').then((r) => r.data),
}

export interface HomeSummary {
  isms:    { groups: number; policies: number; imps: number; fw_coverage_pct: number; op_coverage_pct: number; open_gaps: number }
  privacy: { groups: number; policies: number; imps: number }
  cloud:   { groups: number; policies: number; imps: number }
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
}

export interface CoverageGap {
  id: string
  group_code: string
  name: string
  section: string
  section_name: string
  missing: string[]
}
