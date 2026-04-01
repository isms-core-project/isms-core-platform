import { client } from './client'
import type { OrganisationRead } from './types'

export interface OrganisationCreate {
  name: string
  slug: string
  description?: string
  governance_mode?: string
}

export interface OrganisationPatch {
  name?: string
  description?: string
  governance_mode?: string
  settings?: Record<string, unknown>
}

export const orgApi = {
  // Current user's org (GET /organisation/)
  get: () =>
    client.get<OrganisationRead>('/organisation/').then(r => r.data),

  update: (body: OrganisationPatch) =>
    client.patch<OrganisationRead>('/organisation/', body).then(r => r.data),

  // Super-admin: list all orgs
  list: () =>
    client.get<OrganisationRead[]>('/organisations').then(r => r.data),

  create: (body: OrganisationCreate) =>
    client.post<OrganisationRead>('/organisations', body).then(r => r.data),

  getById: (id: string) =>
    client.get<OrganisationRead>(`/organisations/${id}`).then(r => r.data),

  updateById: (id: string, body: OrganisationPatch) =>
    client.patch<OrganisationRead>(`/organisations/${id}`, body).then(r => r.data),
}
