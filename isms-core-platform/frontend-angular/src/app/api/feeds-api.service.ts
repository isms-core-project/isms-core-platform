import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

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
  id: string; stix_id: string; technique_id: string; source: string
  name: string; description: string | null; tactics: string[]
  platforms: string[]; is_subtechnique: boolean; deprecated: boolean; url: string | null
}

export interface MitreTechniqueList { items: MitreTechnique[]; total: number; page: number; per_page: number }

export interface MitreAttackStats {
  total_techniques: number; total_subtechniques: number; deprecated_count: number
  tactic_counts: Record<string, number>; platform_counts: Record<string, number>; sources: string[]
}

export interface CisaKevEntry {
  id: string; cve_id: string; vendor_project: string | null; product: string | null
  vulnerability_name: string | null; date_added: string | null; short_description: string | null
  required_action: string | null; due_date: string | null; known_ransomware: boolean; notes: string | null
}

export interface CisaKevList { items: CisaKevEntry[]; total: number; page: number; per_page: number }
export interface CisaKevStats { total_entries: number; ransomware_count: number; recent_30d: number; by_month: { month: string; count: number }[] }

export interface EpssScore { id: string; cve_id: string; score: number; percentile: number; score_date: string | null }
export interface EpssScoreList { items: EpssScore[]; total: number; page: number; per_page: number }

export interface KevAuditEntry {
  cve_id: string; vulnerability_name: string | null; vendor_project: string | null
  product: string | null; date_added: string | null; due_date: string | null
  known_ransomware: boolean; evidence_status: string; evidence_id: string | null; evidence_title: string | null
}

export interface KevAuditReport {
  total: number; covered: number; uncovered: number; ransomware_uncovered: number
  months: number; generated_at: string; entries: KevAuditEntry[]
}

export interface MitreGroup {
  id: string; stix_id: string; source: string; group_id: string; name: string
  description: string | null; aliases: string[]; deprecated: boolean; url: string | null
}
export interface MitreGroupList { items: MitreGroup[]; total: number; page: number; per_page: number }
export interface MitreGroupStats { total_groups: number; deprecated_count: number; sources: string[] }

export interface MitreSoftware {
  id: string; stix_id: string; source: string; software_id: string; name: string
  software_type: string; description: string | null; aliases: string[]
  platforms: string[]; deprecated: boolean; url: string | null
}
export interface MitreSoftwareList { items: MitreSoftware[]; total: number; page: number; per_page: number }
export interface MitreSoftwareStats { total_software: number; malware_count: number; tool_count: number; deprecated_count: number; sources: string[] }

export interface MitreCampaign {
  id: string; stix_id: string; source: string; campaign_id: string; name: string
  description: string | null; aliases: string[]; first_seen: string | null; last_seen: string | null
  deprecated: boolean; url: string | null
}
export interface MitreCampaignList { items: MitreCampaign[]; total: number; page: number; per_page: number }

export interface MitreHeatmapTechnique {
  technique_id: string; stix_id: string; name: string; tactics: string[]
  is_subtechnique: boolean; usage_count: number; used_by: string[]
}
export interface MitreHeatmapResponse {
  tactic_order: string[]; techniques: MitreHeatmapTechnique[]
  covered: number; total_techniques: number; selected_actors: number
}

export interface NvdCveEntry {
  cve_id: string; published: string | null; last_modified: string | null; vuln_status: string | null
  description: string | null; cvss_v4_score: number | null; cvss_v4_severity: string | null
  cvss_v4_vector: string | null; cvss_v3_score: number | null; cvss_v3_severity: string | null
  cvss_v3_vector: string | null; cvss_v2_score: number | null; cwe_ids: string[]
  cpe_affected: string[]; in_kev: boolean; in_euvd: boolean; euvd_id: string | null
  edb_id: number | null; edb_verified: boolean; epss_score: number | null; references: string[]
}
export interface NvdCveList { items: NvdCveEntry[]; total: number; page: number; per_page: number }
export interface NvdCveStats {
  total: number; critical: number; high: number; medium: number; low: number
  in_kev: number; with_epss: number; last_indexed: string | null
}
export interface NvdCpeEntry {
  cpe_uri: string; part: string | null; vendor: string | null; product: string | null
  version: string | null; title: string | null; in_kev: boolean; source: string | null
}
export interface NvdCpeList { items: NvdCpeEntry[]; total: number; page: number; per_page: number }
export interface NvdCpeStats {
  total: number; kev_vendor: number; cve_config: number; applications: number; operating_systems: number; hardware: number
}
export interface NvdIndexStats {
  cve_total: number; cpe_total: number; kev_total: number; edb_total: number
  last_cve_sync: string | null; last_cpe_sync: string | null
  nist_api_key_configured: boolean; cpe_full_enabled: boolean
}

export interface EuvdEntry {
  euvd_id: string; cve_id: string | null; description: string | null
  date_published: string | null; date_updated: string | null
  base_score: number | null; base_score_version: string | null; epss_score: number | null
  assigner: string | null; is_exploited: boolean; is_critical: boolean; is_eu_assigned: boolean
  aliases: string[]; vendors: string[]; products: string[]
}
export interface EuvdList { items: EuvdEntry[]; total: number; page: number; per_page: number }
export interface EuvdStats {
  total: number; exploited: number; critical: number; eu_assigned: number; with_cvss: number; last_indexed: string | null
}

export interface ExploitDbEntry {
  edb_id: number; description: string | null; type: string | null; platform: string | null
  verified: boolean; has_msf: boolean; date_published: string | null; author: string | null
  tags: string[]; cve_refs: string[]; file_path: string | null
}
export interface ExploitDbList { items: ExploitDbEntry[]; total: number; page: number; per_page: number }
export interface ExploitDbStats {
  total: number; verified: number; with_msf: number; with_cve: number; last_indexed: string | null
}

function clean(params: Record<string, unknown>): Record<string, unknown> {
  return Object.fromEntries(Object.entries(params).filter(([, v]) => v !== undefined && v !== null))
}

@Injectable({ providedIn: 'root' })
export class FeedsApiService {
  private http = inject(HttpClient)

  getStatus(): Observable<FeedStatusResponse> {
    return this.http.get<FeedStatusResponse>('/api/v1/feeds/status')
  }

  getAttackTechniques(params: { source?: string; tactic?: string; search?: string; subtechniques?: boolean; deprecated?: boolean; page?: number; per_page?: number }): Observable<MitreTechniqueList> {
    return this.http.get<MitreTechniqueList>('/api/v1/feeds/mitre/attack', { params: clean(params) as any })
  }

  getAttackStats(): Observable<MitreAttackStats> {
    return this.http.get<MitreAttackStats>('/api/v1/feeds/mitre/attack/stats')
  }

  getAtlasTechniques(params: { tactic?: string; search?: string; page?: number; per_page?: number }): Observable<MitreTechniqueList> {
    return this.http.get<MitreTechniqueList>('/api/v1/feeds/mitre/atlas', { params: clean(params) as any })
  }

  getAtlasStats(): Observable<{ total_techniques: number; tactic_counts: Record<string, number> }> {
    return this.http.get<{ total_techniques: number; tactic_counts: Record<string, number> }>('/api/v1/feeds/mitre/atlas/stats')
  }

  getKev(params: { search?: string; ransomware_only?: boolean; page?: number; per_page?: number }): Observable<CisaKevList> {
    return this.http.get<CisaKevList>('/api/v1/feeds/kev', { params: clean(params) as any })
  }

  getKevStats(): Observable<CisaKevStats> {
    return this.http.get<CisaKevStats>('/api/v1/feeds/kev/stats')
  }

  getEpss(params: { min_score?: number; page?: number; per_page?: number }): Observable<EpssScoreList> {
    return this.http.get<EpssScoreList>('/api/v1/feeds/epss', { params: clean(params) as any })
  }

  getKevAuditReport(months = 12): Observable<KevAuditReport> {
    return this.http.get<KevAuditReport>('/api/v1/feeds/kev/audit-report', { params: { months } })
  }

  getMitreGroups(params: { source?: string; search?: string; deprecated?: boolean; page?: number; per_page?: number }): Observable<MitreGroupList> {
    return this.http.get<MitreGroupList>('/api/v1/feeds/mitre/groups', { params: clean(params) as any })
  }

  getMitreGroupStats(): Observable<MitreGroupStats> {
    return this.http.get<MitreGroupStats>('/api/v1/feeds/mitre/groups/stats')
  }

  getMitreSoftware(params: { source?: string; software_type?: string; search?: string; deprecated?: boolean; page?: number; per_page?: number }): Observable<MitreSoftwareList> {
    return this.http.get<MitreSoftwareList>('/api/v1/feeds/mitre/software', { params: clean(params) as any })
  }

  getMitreSoftwareStats(): Observable<MitreSoftwareStats> {
    return this.http.get<MitreSoftwareStats>('/api/v1/feeds/mitre/software/stats')
  }

  getMitreCampaigns(params: { source?: string; search?: string; deprecated?: boolean; page?: number; per_page?: number }): Observable<MitreCampaignList> {
    return this.http.get<MitreCampaignList>('/api/v1/feeds/mitre/campaigns', { params: clean(params) as any })
  }

  getMitreHeatmap(params: { source?: string; group_ids?: string; include_software?: boolean }): Observable<MitreHeatmapResponse> {
    return this.http.get<MitreHeatmapResponse>('/api/v1/feeds/mitre/heatmap', { params: clean(params) as any })
  }

  getNvdIndexStats(): Observable<NvdIndexStats> {
    return this.http.get<NvdIndexStats>('/api/v1/feeds/cve/index-stats')
  }

  getCveStats(): Observable<NvdCveStats> {
    return this.http.get<NvdCveStats>('/api/v1/feeds/cve/stats')
  }

  getCve(params: { search?: string; severity?: string; kev_only?: boolean; edb_only?: boolean; min_epss?: number; year?: number; page?: number; per_page?: number }): Observable<NvdCveList> {
    return this.http.get<NvdCveList>('/api/v1/feeds/cve', { params: clean(params) as any })
  }

  getCveDetail(cveId: string): Observable<NvdCveEntry> {
    return this.http.get<NvdCveEntry>(`/api/v1/feeds/cve/${cveId}`)
  }

  getCpeStats(): Observable<NvdCpeStats> {
    return this.http.get<NvdCpeStats>('/api/v1/feeds/cpe/stats')
  }

  getCpe(params: { search?: string; vendor?: string; product?: string; part?: string; source?: string; kev_only?: boolean; page?: number; per_page?: number }): Observable<NvdCpeList> {
    return this.http.get<NvdCpeList>('/api/v1/feeds/cpe', { params: clean(params) as any })
  }

  getFeedSettings(): Observable<{ feeds_cpe_full: boolean }> {
    return this.http.get<{ feeds_cpe_full: boolean }>('/api/v1/feeds/settings')
  }

  patchFeedSettings(payload: { feeds_cpe_full: boolean }): Observable<{ feeds_cpe_full: boolean }> {
    return this.http.patch<{ feeds_cpe_full: boolean }>('/api/v1/feeds/settings', payload)
  }

  triggerFeed(feedName: string, mode: 'full' | 'delta' = 'full'): Observable<{ status: string; feed: string; mode: string | null }> {
    const params = feedName === 'nist_cve' ? { mode } : undefined
    return this.http.post<{ status: string; feed: string; mode: string | null }>(`/api/v1/feeds/trigger/${feedName}`, null, { params })
  }

  cancelFeed(feedName: string): Observable<{ status: string; feed: string }> {
    return this.http.delete<{ status: string; feed: string }>(`/api/v1/feeds/cancel/${feedName}`)
  }

  getEuvdStats(): Observable<EuvdStats> {
    return this.http.get<EuvdStats>('/api/v1/feeds/euvd/stats')
  }

  getEuvd(params: { search?: string; exploited_only?: boolean; critical_only?: boolean; eu_assigned_only?: boolean; min_score?: number; page?: number; per_page?: number }): Observable<EuvdList> {
    return this.http.get<EuvdList>('/api/v1/feeds/euvd', { params: clean(params) as any })
  }

  getEuvdEntry(euvdId: string): Observable<EuvdEntry> {
    return this.http.get<EuvdEntry>(`/api/v1/feeds/euvd/${euvdId}`)
  }

  getExploitDbStats(): Observable<ExploitDbStats> {
    return this.http.get<ExploitDbStats>('/api/v1/feeds/exploitdb/stats')
  }

  listExploitDb(params: { search?: string; verified_only?: boolean; msf_only?: boolean; type?: string; platform?: string; cve_id?: string; page?: number; per_page?: number }): Observable<ExploitDbList> {
    return this.http.get<ExploitDbList>('/api/v1/feeds/exploitdb', { params: clean(params) as any })
  }

  getExploitDbEntry(edbId: number): Observable<ExploitDbEntry> {
    return this.http.get<ExploitDbEntry>(`/api/v1/feeds/exploitdb/${edbId}`)
  }
}
