import { client } from './client'

// ── Types ─────────────────────────────────────────────────────────────────────

export interface TiSourceStatus {
  source: string
  display_name: string
  enabled: boolean
  last_run_at: string | null
  last_run_status: string | null
  ioc_count: number
}

export interface TiSummary {
  active: boolean
  sources: TiSourceStatus[]
  total_iocs: number
  total_families: number
  total_actors: number
  total_tools: number
}

export interface IocRead {
  id: string
  ioc_type: string
  value: string
  source: string
  confidence: number | null
  tlp: string | null
  tags: string[]
  mitre_tids: string[]
  family_slugs: string[]
  actor_slugs: string[]
  first_seen: string | null
  last_seen: string | null
}

export interface IocList {
  total: number
  items: IocRead[]
}

export interface MalwareFamilyRead {
  id: string
  slug: string
  name: string
  aliases: string[]
  description: string | null
  actor_slugs: string[]
  mitre_tids: string[]
  updated_at: string
}

export interface MalwareFamilyList {
  total: number
  items: MalwareFamilyRead[]
}

export interface ActorRead {
  id: string
  slug: string
  name: string
  country: string | null
  motivation: string | null
  description: string | null
  actor_type: string
  updated_at: string
}

export interface ToolRead {
  id: string
  slug: string
  name: string
  aliases: string[]
  description: string | null
  mitre_tids: string[]
  updated_at: string
}

export interface ToolList {
  total: number
  items: ToolRead[]
}

export interface ActorList {
  total: number
  items: ActorRead[]
}

export interface EnrichIpResponse {
  ip: string
  abuseipdb: Record<string, unknown> | null
  shodan: Record<string, unknown> | null
  google_dns: Record<string, unknown> | null
  maxmind: Record<string, unknown> | null
  ipinfo: Record<string, unknown> | null
  cached: boolean
  cache_age_minutes: number | null
  ioc_hits: IocRead[]
}

// ── API client ────────────────────────────────────────────────────────────────

export const threatIntelApi = {
  getSummary: () =>
    client.get<TiSummary>('/threat-intel/summary').then(r => r.data),

  getIocs: (params: {
    q?: string; ioc_type?: string; source?: string
    family_slug?: string; actor_slug?: string; mitre_tid?: string
    skip?: number; limit?: number
  }) =>
    client.get<IocList>('/threat-intel/iocs', { params }).then(r => r.data),

  getMalware: (params: { q?: string; actor_slug?: string; mitre_tid?: string; skip?: number; limit?: number }) =>
    client.get<MalwareFamilyList>('/threat-intel/malware', { params }).then(r => r.data),

  getActors: (params: { q?: string; country?: string; actor_type?: string; skip?: number; limit?: number }) =>
    client.get<ActorList>('/threat-intel/actors', { params }).then(r => r.data),

  getTools: (params: { q?: string; mitre_tid?: string; skip?: number; limit?: number }) =>
    client.get<ToolList>('/threat-intel/tools', { params }).then(r => r.data),

  getIocStats: () =>
    client.get<{
      type_breakdown: { type: string; count: number }[]
      source_totals:  { source: string; count: number }[]
      top_families:   { family: string; count: number }[]
    }>('/threat-intel/ioc-stats').then(r => r.data),

  enrichIp: (ip: string) =>
    client.post<EnrichIpResponse>('/threat-intel/enrich/ip', { ip }).then(r => r.data),

  triggerFeed: (source: string) =>
    client.post<{ status: string }>('/threat-intel/feeds/trigger', { source }).then(r => r.data),

  cancelFeed: (source: string) =>
    client.delete<{ status: string; source: string }>(`/threat-intel/feeds/cancel/${source}`).then(r => r.data),
}
