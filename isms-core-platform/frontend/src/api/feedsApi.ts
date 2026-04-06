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

  // Phase 27 — NVD CVE / CPE
  getNvdIndexStats: () =>
    client.get<NvdIndexStats>('/feeds/cve/index-stats').then(r => r.data),

  getCveStats: () =>
    client.get<NvdCveStats>('/feeds/cve/stats').then(r => r.data),

  getCve: (params: {
    search?: string
    severity?: string
    kev_only?: boolean
    min_epss?: number
    year?: number
    page?: number
    per_page?: number
  }) =>
    client.get<NvdCveList>('/feeds/cve', { params }).then(r => r.data),

  getCveDetail: (cveId: string) =>
    client.get<NvdCveEntry>(`/feeds/cve/${cveId}`).then(r => r.data),

  getCpeStats: () =>
    client.get<NvdCpeStats>('/feeds/cpe/stats').then(r => r.data),

  getCpe: (params: {
    search?: string
    vendor?: string
    product?: string
    part?: string
    source?: string
    kev_only?: boolean
    page?: number
    per_page?: number
  }) =>
    client.get<NvdCpeList>('/feeds/cpe', { params }).then(r => r.data),
}

// ── Phase 27 types ────────────────────────────────────────────────────────────

export interface NvdCveEntry {
  cve_id: string
  published: string | null
  last_modified: string | null
  vuln_status: string | null
  description: string | null
  cvss_v3_score: number | null
  cvss_v3_severity: string | null
  cvss_v3_vector: string | null
  cvss_v2_score: number | null
  cwe_ids: string[]
  cpe_affected: string[]
  in_kev: boolean
  epss_score: number | null
  references: string[]
}

export interface NvdCveList {
  items: NvdCveEntry[]
  total: number
  page: number
  per_page: number
}

export interface NvdCveStats {
  total: number
  critical: number
  high: number
  medium: number
  low: number
  in_kev: number
  with_epss: number
  last_indexed: string | null
}

export interface NvdCpeEntry {
  cpe_uri: string
  part: string | null
  vendor: string | null
  product: string | null
  version: string | null
  title: string | null
  in_kev: boolean
  source: string | null
}

export interface NvdCpeList {
  items: NvdCpeEntry[]
  total: number
  page: number
  per_page: number
}

export interface NvdCpeStats {
  total: number
  kev_vendor: number
  cve_config: number
  applications: number
  operating_systems: number
  hardware: number
}

export interface NvdIndexStats {
  cve_total: number
  cpe_total: number
  kev_total: number
  last_cve_sync: string | null
  last_cpe_sync: string | null
  nist_api_key_configured: boolean
  cpe_full_enabled: boolean
}
