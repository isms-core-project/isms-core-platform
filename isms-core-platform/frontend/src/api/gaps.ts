import { client } from './client'
import type { EvidenceRead, GapCreate, GapPatch, GapRead } from './types'

export const gapsApi = {
  list: (params?: { severity?: string; status?: string; product?: string; control_group_id?: string; limit?: number }) =>
    client.get<GapRead[]>('/gaps/', { params }).then((r) => r.data),

  create: (body: GapCreate) =>
    client.post<GapRead>('/gaps/', body).then((r) => r.data),

  patch: (id: string, body: GapPatch) =>
    client.patch<GapRead>(`/gaps/${id}`, body).then((r) => r.data),

  delete: (id: string) =>
    client.delete(`/gaps/${id}`),

  listEvidence: (gapId: string) =>
    client.get<EvidenceRead[]>(`/gaps/${gapId}/evidence`).then((r) => r.data),

  attachEvidence: (gapId: string, evidenceId: string) =>
    client.post<GapRead>(`/gaps/${gapId}/evidence/${evidenceId}`).then((r) => r.data),

  detachEvidence: (gapId: string, evidenceId: string) =>
    client.delete<GapRead>(`/gaps/${gapId}/evidence/${evidenceId}`).then((r) => r.data),
}
