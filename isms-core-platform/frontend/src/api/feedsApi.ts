import { client } from './client'

export interface FeedStatusItem {
  feed_name: string
  display_name: string
  enabled: boolean
  last_run: string | null
  last_status: string | null
  item_count: number | null
  error_message: string | null
}

export interface FeedStatusResponse {
  feeds: FeedStatusItem[]
}

export interface MitreTechnique {
  id: string
  stix_id: string
  technique_id: string
  source: string
  name: string
  description: string | null
  tactics: string[]
  platforms: string[]
  is_subtechnique: boolean
  deprecated: boolean
  url: string | null
}

export interface MitreTechniqueList {
  items: MitreTechnique[]
  total: number
  page: number
  per_page: number
}

export interface MitreAttackStats {
  total_techniques: number
  total_subtechniques: number
  deprecated_count: number
  tactic_counts: Record<string, number>
  platform_counts: Record<string, number>
  sources: string[]
}

export interface CisaKevEntry {
  id: string
  cve_id: string
  vendor_project: string | null
  product: string | null
  vulnerability_name: string | null
  date_added: string | null
  short_description: string | null
  required_action: string | null
  due_date: string | null
  known_ransomware: boolean
  notes: string | null
}

export interface CisaKevList {
  items: CisaKevEntry[]
  total: number
  page: number
  per_page: number
}

export interface CisaKevStats {
  total_entries: number
  ransomware_count: number
  recent_30d: number
  by_month: { month: string; count: number }[]
}

export interface EpssScore {
  id: string
  cve_id: string
  score: number
  percentile: number
  score_date: string | null
}

export interface EpssScoreList {
  items: EpssScore[]
  total: number
  page: number
  per_page: number
}

export interface KevAuditEntry {
  cve_id: string
  vulnerability_name: string | null
  vendor_project: string | null
  product: string | null
  date_added: string | null
  due_date: string | null
  known_ransomware: boolean
  evidence_status: string
  evidence_id: string | null
  evidence_title: string | null
}

export interface KevAuditReport {
  total: number
  covered: number
  uncovered: number
  ransomware_uncovered: number
  months: number
  generated_at: string
  entries: KevAuditEntry[]
}

export const feedsApi = {
  getStatus: () =>
    client.get<FeedStatusResponse>('/feeds/status').then(r => r.data),

  getAttackTechniques: (params: {
    source?: string
    tactic?: string
    search?: string
    subtechniques?: boolean
    deprecated?: boolean
    page?: number
    per_page?: number
  }) =>
    client.get<MitreTechniqueList>('/feeds/mitre/attack', { params }).then(r => r.data),

  getAttackStats: () =>
    client.get<MitreAttackStats>('/feeds/mitre/attack/stats').then(r => r.data),

  getAtlasTechniques: (params: {
    tactic?: string
    search?: string
    page?: number
    per_page?: number
  }) =>
    client.get<MitreTechniqueList>('/feeds/mitre/atlas', { params }).then(r => r.data),

  getAtlasStats: () =>
    client.get<{ total_techniques: number; tactic_counts: Record<string, number> }>('/feeds/mitre/atlas/stats').then(r => r.data),

  getKev: (params: {
    search?: string
    ransomware_only?: boolean
    page?: number
    per_page?: number
  }) =>
    client.get<CisaKevList>('/feeds/kev', { params }).then(r => r.data),

  getKevStats: () =>
    client.get<CisaKevStats>('/feeds/kev/stats').then(r => r.data),

  getEpss: (params: {
    min_score?: number
    page?: number
    per_page?: number
  }) =>
    client.get<EpssScoreList>('/feeds/epss', { params }).then(r => r.data),

  getKevAuditReport: (months = 12) =>
    client.get<KevAuditReport>('/feeds/kev/audit-report', { params: { months } }).then(r => r.data),
}
