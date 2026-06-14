import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'
import {
  SysInfoResponse,
  NotificationRoutingRule,
  UserNotificationPrefs,
  NotificationPrefsResponse,
} from '../shared/types'

export interface UserRead {
  id: string
  email: string
  username: string
  full_name: string | null
  role: string
  is_active: boolean
  mfa_enabled: boolean
  created_at: string
  last_login: string | null
  organisation_id: string | null
  organisation_name: string | null
  notification_prefs: Record<string, boolean>
}

export interface UserCreate {
  email: string
  username: string
  password: string
  full_name?: string
  role?: string
}

export interface UserPatch {
  email?: string
  username?: string
  full_name?: string | null
  role?: string
  is_active?: boolean
  password?: string
}

export interface SyncResult {
  status: string
  stats: Record<string, number>
}


// NotificationPrefsResponse, NotificationRoutingRule, UserNotificationPrefs
// are imported from ../shared/types (richer definitions with label, category, etc.)

export interface OrphanEntry {
  document_id: string
  file_path: string
}

export interface AuditLogParams {
  page?: number
  page_size?: number
  category?: string
  severity?: string
  event_type?: string
  actor_email?: string
  date_from?: string
  date_to?: string
}

export interface AuditLogEntry {
  id: string
  event_type: string
  category: string
  severity: string
  user_id: string | null
  actor_email: string | null
  target_type: string | null
  target_id: string | null
  description: string | null
  ip_address: string | null
  metadata_: Record<string, unknown>
  created_at: string
}

export interface AuditLogPage {
  items: AuditLogEntry[]
  total: number
  page: number
  page_size: number
  pages: number
}

export interface FeedRunEntry {
  id: string
  feed_name: string
  status: string
  started_at: string | null
  finished_at: string | null
  duration_seconds: number | null
  item_count: number | null
  error_message: string | null
}

export interface ConnectorRunEntry {
  connector_name?: string
  connector_id: string
  started_at: string | null
  finished_at: string | null
  evidence_count?: number | null
  item_count?: number | null
  status: string
  error_message: string | null
}

export interface SessionEntry {
  id: string
  user_id: string
  user_email: string | null
  user_username: string | null
  expires_at: string
  ip_address: string | null
  user_agent: string | null
  created_at: string
  is_expired: boolean
}

export interface GroupEntry {
  id: string
  name: string
  description: string | null
  member_count: number
  created_at: string
}

export interface GroupMemberEntry {
  user_id: string
  email: string
  username: string
  full_name: string | null
  role: string
}

export interface OpenSearchDetail {
  ism_policies: Array<{ id: string; description: string; default_state: string; states: string[]; last_updated_time: number | null }>
  ism_managed: Array<{ index: string; policy_id: string; state: string | null; action: string | null }>
  sm_policies: Array<{ id: string; description: string; repository: string | null; creation_schedule: string | null; enabled: boolean; last_creation: string | null; last_creation_time: number | null }>
  snapshot_repos: Array<{ name: string; type: string; bucket: string | null; endpoint: string | null }>
  evidence_indices: Array<{ index: string; doc_count: number; store_size: string | null }>
}

@Injectable({ providedIn: 'root' })
export class AdminApiService {
  private http = inject(HttpClient)

  listUsers(): Observable<UserRead[]> {
    return this.http.get<UserRead[]>('/api/v1/admin/users')
  }

  createUser(body: UserCreate): Observable<UserRead> {
    return this.http.post<UserRead>('/api/v1/admin/users', body)
  }

  updateUser(id: string, body: UserPatch): Observable<UserRead> {
    return this.http.patch<UserRead>(`/api/v1/admin/users/${id}`, body)
  }

  deleteUser(id: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/admin/users/${id}`)
  }

  resetUserMfa(id: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/admin/users/${id}/mfa`)
  }

  syncFull(): Observable<SyncResult> {
    return this.http.post<SyncResult>('/api/v1/sync/full', {})
  }

  syncAsync(): Observable<{ task_id: string; status: string }> {
    return this.http.post<{ task_id: string; status: string }>('/api/v1/sync/full/async', {})
  }

  getTaskStatus(taskId: string): Observable<{ task_id: string; status: string; result?: unknown }> {
    return this.http.get<{ task_id: string; status: string; result?: unknown }>(`/api/v1/sync/status/${taskId}`)
  }

  getSysInfo(): Observable<SysInfoResponse> {
    return this.http.get<SysInfoResponse>('/api/v1/admin/sysinfo')
  }

  getOpenSearchDetail(): Observable<OpenSearchDetail> {
    return this.http.get<OpenSearchDetail>('/api/v1/admin/opensearch')
  }

  resetContent(): Observable<{ status: string; deleted: Record<string, number>; reimport: Record<string, unknown> }> {
    return this.http.post<{ status: string; deleted: Record<string, number>; reimport: Record<string, unknown> }>('/api/v1/admin/reset-content', {})
  }

  reindexOpenSearch(): Observable<{ status: string; stats: { implementations: number; policies: number; errors: number } }> {
    return this.http.post<{ status: string; stats: { implementations: number; policies: number; errors: number } }>('/api/v1/admin/reindex', {})
  }

  scanOrphans(): Observable<{ total: number; implementations: OrphanEntry[]; policies: OrphanEntry[] }> {
    return this.http.get<{ total: number; implementations: OrphanEntry[]; policies: OrphanEntry[] }>('/api/v1/admin/orphans')
  }

  purgeOrphans(): Observable<{ status: string; deleted: { implementations: number; policies: number } }> {
    return this.http.delete<{ status: string; deleted: { implementations: number; policies: number } }>('/api/v1/admin/orphans')
  }

  loadFrameworkBundles(): Observable<{ status: string; stats: unknown }> {
    return this.http.post<{ status: string; stats: unknown }>('/api/v1/admin/load', {})
  }

  importPolicies(): Observable<{ status: string; stats: Record<string, number> }> {
    return this.http.post<{ status: string; stats: Record<string, number> }>('/api/v1/admin/import-policies', {})
  }

  importImplementations(): Observable<{ status: string; stats: Record<string, number> }> {
    return this.http.post<{ status: string; stats: Record<string, number> }>('/api/v1/admin/import-implementations', {})
  }

  importWorkbooks(): Observable<{ status: string; stats: Record<string, number> }> {
    return this.http.post<{ status: string; stats: Record<string, number> }>('/api/v1/admin/import-framework-workbooks', {})
  }

  importOperational(): Observable<{ status: string; stats: Record<string, number> }> {
    return this.http.post<{ status: string; stats: Record<string, number> }>('/api/v1/admin/import-operational', {})
  }

  getAuditLog(params: AuditLogParams): Observable<AuditLogPage> {
    const p = Object.fromEntries(Object.entries(params).filter(([, v]) => v != null && v !== ''))
    return this.http.get<AuditLogPage>('/api/v1/admin/audit-log', { params: p as Record<string, string | number> })
  }

  sendTestEmail(recipient: string): Observable<{ ok: boolean; recipient: string }> {
    return this.http.post<{ ok: boolean; recipient: string }>('/api/v1/admin/email/test', { recipient })
  }

  sendTestNotification(event_type: string): Observable<{ ok: boolean; recipient: string; event_type: string }> {
    return this.http.post<{ ok: boolean; recipient: string; event_type: string }>('/api/v1/admin/notification/test', { event_type })
  }

  getMyNotificationPrefs(): Observable<NotificationPrefsResponse> {
    return this.http.get<NotificationPrefsResponse>('/api/v1/auth/me/notification-prefs')
  }

  updateMyNotificationPrefs(prefs: Record<string, boolean>): Observable<NotificationPrefsResponse> {
    return this.http.patch<NotificationPrefsResponse>('/api/v1/auth/me/notification-prefs', { prefs })
  }

  getNotificationRouting(): Observable<NotificationRoutingRule[]> {
    return this.http.get<NotificationRoutingRule[]>('/api/v1/admin/notifications/routing')
  }

  updateNotificationRouting(event_type: string, body: Partial<NotificationRoutingRule>): Observable<NotificationRoutingRule> {
    return this.http.patch<NotificationRoutingRule>(`/api/v1/admin/notifications/routing/${event_type}`, body)
  }

  getAllUserNotificationPrefs(): Observable<UserNotificationPrefs[]> {
    return this.http.get<UserNotificationPrefs[]>('/api/v1/admin/notifications/users')
  }

  updateUserNotificationPrefs(user_id: string, prefs: Record<string, boolean>): Observable<{ user_id: string; prefs: Record<string, boolean> }> {
    return this.http.patch<{ user_id: string; prefs: Record<string, boolean> }>(`/api/v1/admin/notifications/users/${user_id}`, { prefs })
  }

  getFeedRuns(params?: { feed_name?: string; status?: string; limit?: number }): Observable<FeedRunEntry[]> {
    const p = params ? Object.fromEntries(Object.entries(params).filter(([, v]) => v != null && v !== '')) : {}
    return this.http.get<FeedRunEntry[]>('/api/v1/admin/logs/feed-runs', { params: p as any })
  }

  getConnectorRuns(params?: { connector_id?: string; status?: string; limit?: number }): Observable<ConnectorRunEntry[]> {
    const p = params ? Object.fromEntries(Object.entries(params).filter(([, v]) => v != null && v !== '')) : {}
    return this.http.get<ConnectorRunEntry[]>('/api/v1/admin/logs/connector-runs', { params: p as any })
  }

  listSessions(params?: { user_id?: string; include_expired?: boolean }): Observable<SessionEntry[]> {
    const p = params ? Object.fromEntries(Object.entries(params).filter(([, v]) => v != null && v !== '')) : {}
    return this.http.get<SessionEntry[]>('/api/v1/admin/sessions', { params: p as any })
  }

  revokeSession(id: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/admin/sessions/${id}`)
  }

  revokeUserSessions(userId: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/admin/sessions/user/${userId}`)
  }

  listGroups(): Observable<GroupEntry[]> {
    return this.http.get<GroupEntry[]>('/api/v1/admin/groups')
  }

  createGroup(body: { name: string; description?: string }): Observable<GroupEntry> {
    return this.http.post<GroupEntry>('/api/v1/admin/groups', body)
  }

  updateGroup(id: string, body: { name?: string; description?: string }): Observable<GroupEntry> {
    return this.http.patch<GroupEntry>(`/api/v1/admin/groups/${id}`, body)
  }

  deleteGroup(id: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/admin/groups/${id}`)
  }

  getGroupMembers(groupId: string): Observable<GroupMemberEntry[]> {
    return this.http.get<GroupMemberEntry[]>(`/api/v1/admin/groups/${groupId}/members`)
  }

  addGroupMember(groupId: string, userId: string): Observable<void> {
    return this.http.post<void>(`/api/v1/admin/groups/${groupId}/members`, { user_id: userId })
  }

  removeGroupMember(groupId: string, userId: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/admin/groups/${groupId}/members/${userId}`)
  }
}
