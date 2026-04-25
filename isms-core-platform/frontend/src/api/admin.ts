import { client } from './client'
import type { UserCreate, UserPatch, UserRead, SyncResult, SysInfoResponse, NotificationPrefsResponse } from './types'

export const adminApi = {
  listUsers: () =>
    client.get<UserRead[]>('/admin/users').then((r) => r.data),

  createUser: (body: UserCreate) =>
    client.post<UserRead>('/admin/users', body).then((r) => r.data),

  updateUser: (id: string, body: UserPatch) =>
    client.patch<UserRead>(`/admin/users/${id}`, body).then((r) => r.data),

  deleteUser: (id: string) =>
    client.delete(`/admin/users/${id}`),

  resetUserMfa: (id: string) =>
    client.delete(`/admin/users/${id}/mfa`),

  syncFull: () =>
    client.post<SyncResult>('/sync/full').then((r) => r.data),

  syncAsync: () =>
    client.post<{ task_id: string; status: string }>('/sync/full/async').then((r) => r.data),

  getTaskStatus: (taskId: string) =>
    client.get<{ task_id: string; status: string; result?: unknown }>(`/sync/status/${taskId}`).then((r) => r.data),

  getSysInfo: () =>
    client.get<SysInfoResponse>('/admin/sysinfo').then((r) => r.data),

  getOpenSearchDetail: () =>
    client.get<{
      ism_policies: Array<{ id: string; description: string; default_state: string; states: string[]; last_updated_time: number | null }>;
      ism_managed: Array<{ index: string; policy_id: string; state: string | null; action: string | null }>;
      sm_policies: Array<{ id: string; description: string; repository: string | null; creation_schedule: string | null; enabled: boolean; last_creation: string | null; last_creation_time: number | null }>;
      snapshot_repos: Array<{ name: string; type: string; bucket: string | null; endpoint: string | null }>;
      evidence_indices: Array<{ index: string; doc_count: number; store_size: string | null }>;
    }>('/admin/opensearch').then((r) => r.data),

  resetContent: () =>
    client.post<{ status: string; deleted: Record<string, number>; reimport: Record<string, unknown> }>('/admin/reset-content').then((r) => r.data),

  reindexOpenSearch: () =>
    client.post<{ status: string; stats: { implementations: number; policies: number; errors: number } }>('/admin/reindex').then((r) => r.data),

  scanOrphans: () =>
    client.get<{ total: number; implementations: OrphanEntry[]; policies: OrphanEntry[] }>('/admin/orphans').then((r) => r.data),

  purgeOrphans: () =>
    client.delete<{ status: string; deleted: { implementations: number; policies: number } }>('/admin/orphans').then((r) => r.data),

  loadFrameworkBundles: () =>
    client.post<{ status: string; stats: unknown }>('/admin/load').then((r) => r.data),

  importPolicies: () =>
    client.post<{ status: string; stats: Record<string, number> }>('/admin/import-policies').then((r) => r.data),

  importImplementations: () =>
    client.post<{ status: string; stats: Record<string, number> }>('/admin/import-implementations').then((r) => r.data),

  importWorkbooks: () =>
    client.post<{ status: string; stats: Record<string, number> }>('/admin/import-framework-workbooks').then((r) => r.data),

  importOperational: () =>
    client.post<{ status: string; stats: Record<string, number> }>('/admin/import-operational').then((r) => r.data),

  getAuditLog: (params: AuditLogParams) =>
    client.get<AuditLogPage>('/admin/audit-log', { params }).then((r) => r.data),

  sendTestEmail: (recipient: string) =>
    client.post<{ ok: boolean; recipient: string }>('/admin/email/test', { recipient }).then((r) => r.data),

  sendTestNotification: (event_type: string) =>
    client.post<{ ok: boolean; recipient: string; event_type: string }>('/admin/notification/test', { event_type }).then((r) => r.data),

  getMyNotificationPrefs: () =>
    client.get<NotificationPrefsResponse>('/auth/me/notification-prefs').then((r) => r.data),

  updateMyNotificationPrefs: (prefs: Record<string, boolean>) =>
    client.patch<NotificationPrefsResponse>('/auth/me/notification-prefs', { prefs }).then((r) => r.data),

  getOrganisation: () =>
    client.get<{ settings: Record<string, unknown> }>('/organisation/').then((r) => r.data),

  patchOrganisationSettings: (settings: Record<string, unknown>) =>
    client.patch<{ settings: Record<string, unknown> }>('/organisation/', { settings }).then((r) => r.data),

  // --- Logs (Phase 39) ---
  getFeedRuns: (params?: { feed_name?: string; status?: string; limit?: number }) =>
    client.get<FeedRunEntry[]>('/admin/logs/feed-runs', { params }).then((r) => r.data),

  getConnectorRuns: (params?: { connector_id?: string; status?: string; limit?: number }) =>
    client.get<ConnectorRunEntry[]>('/admin/logs/connector-runs', { params }).then((r) => r.data),

  // --- Sessions (Phase 39) ---
  listSessions: (params?: { user_id?: string; include_expired?: boolean }) =>
    client.get<SessionEntry[]>('/admin/sessions', { params }).then((r) => r.data),

  revokeSession: (id: string) =>
    client.delete(`/admin/sessions/${id}`),

  revokeUserSessions: (userId: string) =>
    client.delete(`/admin/sessions/user/${userId}`),

  // --- Groups (Phase 39) ---
  listGroups: () =>
    client.get<GroupEntry[]>('/admin/groups').then((r) => r.data),

  createGroup: (body: { name: string; description?: string }) =>
    client.post<GroupEntry>('/admin/groups', body).then((r) => r.data),

  updateGroup: (id: string, body: { name?: string; description?: string }) =>
    client.patch<GroupEntry>(`/admin/groups/${id}`, body).then((r) => r.data),

  deleteGroup: (id: string) =>
    client.delete(`/admin/groups/${id}`),

  getGroupMembers: (groupId: string) =>
    client.get<GroupMemberEntry[]>(`/admin/groups/${groupId}/members`).then((r) => r.data),

  addGroupMember: (groupId: string, userId: string) =>
    client.post(`/admin/groups/${groupId}/members`, { user_id: userId }),

  removeGroupMember: (groupId: string, userId: string) =>
    client.delete(`/admin/groups/${groupId}/members/${userId}`),
}

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
  history_limited?: boolean
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
