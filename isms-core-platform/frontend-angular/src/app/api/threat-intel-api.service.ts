import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

function clean(params: Record<string, unknown>): Record<string, unknown> {
  return Object.fromEntries(Object.entries(params).filter(([, v]) => v !== undefined && v !== null))
}

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

export interface IocList { total: number; items: IocRead[] }

export interface MalwareFamilyRead {
  id: string; slug: string; name: string; aliases: string[]
  description: string | null; actor_slugs: string[]; mitre_tids: string[]; updated_at: string
}
export interface MalwareFamilyList { total: number; items: MalwareFamilyRead[] }

export interface ActorRead {
  id: string; slug: string; name: string; country: string | null
  motivation: string | null; description: string | null; actor_type: string; updated_at: string
}
export interface ActorList { total: number; items: ActorRead[] }

export interface ToolRead {
  id: string; slug: string; name: string; aliases: string[]
  description: string | null; mitre_tids: string[]; updated_at: string
}
export interface ToolList { total: number; items: ToolRead[] }

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

export interface IocStats {
  type_breakdown: { type: string; count: number }[]
  source_totals: { source: string; count: number }[]
  top_families: { family: string; count: number }[]
}

@Injectable({ providedIn: 'root' })
export class ThreatIntelApiService {
  private http = inject(HttpClient)

  getSummary(): Observable<TiSummary> {
    return this.http.get<TiSummary>('/api/v1/threat-intel/summary')
  }

  getIocs(params: { q?: string; ioc_type?: string; source?: string; family_slug?: string; actor_slug?: string; mitre_tid?: string; skip?: number; limit?: number }): Observable<IocList> {
    return this.http.get<IocList>('/api/v1/threat-intel/iocs', { params: clean(params) as any })
  }

  getMalware(params: { q?: string; actor_slug?: string; mitre_tid?: string; skip?: number; limit?: number }): Observable<MalwareFamilyList> {
    return this.http.get<MalwareFamilyList>('/api/v1/threat-intel/malware', { params: clean(params) as any })
  }

  getActors(params: { q?: string; country?: string; actor_type?: string; skip?: number; limit?: number }): Observable<ActorList> {
    return this.http.get<ActorList>('/api/v1/threat-intel/actors', { params: clean(params) as any })
  }

  getActorCountries(): Observable<{ code: string; count: number }[]> {
    return this.http.get<{ code: string; count: number }[]>('/api/v1/threat-intel/actors/countries')
  }

  getTools(params: { q?: string; mitre_tid?: string; skip?: number; limit?: number }): Observable<ToolList> {
    return this.http.get<ToolList>('/api/v1/threat-intel/tools', { params: clean(params) as any })
  }

  getIocStats(): Observable<IocStats> {
    return this.http.get<IocStats>('/api/v1/threat-intel/ioc-stats')
  }

  enrichIp(ip: string): Observable<EnrichIpResponse> {
    return this.http.post<EnrichIpResponse>('/api/v1/threat-intel/enrich/ip', { ip })
  }

  triggerFeed(source: string): Observable<{ status: string }> {
    return this.http.post<{ status: string }>('/api/v1/threat-intel/feeds/trigger', { source })
  }

  cancelFeed(source: string): Observable<{ status: string; source: string }> {
    return this.http.delete<{ status: string; source: string }>(`/api/v1/threat-intel/feeds/cancel/${source}`)
  }
}
