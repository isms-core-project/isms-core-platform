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

  syncFull: () =>
    client.post<SyncResult>('/sync/full').then((r) => r.data),

  syncAsync: () =>
    client.post<{ task_id: string; status: string }>('/sync/full/async').then((r) => r.data),

  getTaskStatus: (taskId: string) =>
    client.get<{ task_id: string; status: string; result?: unknown }>(`/sync/status/${taskId}`).then((r) => r.data),

  getSysInfo: () =>
    client.get<SysInfoResponse>('/admin/sysinfo').then((r) => r.data),

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

  getMyNotificationPrefs: () =>
    client.get<NotificationPrefsResponse>('/auth/me/notification-prefs').then((r) => r.data),

  updateMyNotificationPrefs: (prefs: Record<string, boolean>) =>
    client.patch<NotificationPrefsResponse>('/auth/me/notification-prefs', { prefs }).then((r) => r.data),

  getOrganisation: () =>
    client.get<{ settings: Record<string, unknown> }>('/organisation/').then((r) => r.data),

  patchOrganisationSettings: (settings: Record<string, unknown>) =>
    client.patch<{ settings: Record<string, unknown> }>('/organisation/', { settings }).then((r) => r.data),
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
