import { client } from './client'

export interface DocVars {
  ciso_name?: string
  ceo_name?: string
  dpo_name?: string
  legal_entity?: string
  effective_date?: string
  review_date?: string
  classification?: string
}

export interface ProjectRead {
  id: string
  name: string
  organisation_id: string
  organisation_name: string | null
  product_family: string
  project_subtype: string | null   // 'fw' | 'op' — only relevant for ISMS
  description: string | null
  status: string
  owner_id: string | null
  created_at: string
  updated_at: string
  doc_vars: DocVars | null
  policy_count: number
  implementation_count: number
  checklist_count: number
}

export interface ProjectCreate {
  name: string
  product_family: string
  project_subtype?: string   // 'fw' | 'op'
  description?: string
  doc_vars?: DocVars
  organisation_id?: string   // super_admin only
}

export interface ProjectPatch {
  name?: string
  description?: string
  status?: string
  project_subtype?: string
  doc_vars?: DocVars
}

export interface LibraryPolicyItem {
  id: string
  document_id: string
  title: string
  policy_type: string
  product_type: string
  control_group_code: string
  control_group_name: string
  is_stacked: boolean
  already_in_project: boolean
}

export interface LibraryImplItem {
  id: string
  document_id: string
  title: string
  impl_type: string
  control_group_code: string
  control_group_name: string
  already_in_project: boolean
}

export interface ProjectPolicyRead {
  id: string
  project_id: string
  lib_policy_id: string | null
  document_id: string | null
  title: string | null
  policy_type: string | null
  product_type: string | null
  control_group_code: string | null
  is_edited: boolean
  stacking_locked: boolean
  stale_warning: boolean
  status: string
  created_at: string
  custom_content?: string | null
}

export interface ProjectImplRead {
  id: string
  project_id: string
  lib_impl_id: string | null
  document_id: string | null
  title: string | null
  impl_type: string | null
  control_group_code: string | null
  is_edited: boolean
  stale_warning: boolean
  status: string
  created_at: string
  custom_content?: string | null
}

export interface LibraryChecklistItem {
  id: string
  document_id: string
  title: string
  product_type: string
  control_group_code: string
  control_group_name: string
  item_count: number
  already_in_project: boolean
}

export interface ProjectChecklistItem {
  id: string
  row_number: number
  item_text: string | null
  na: boolean
  justification: string | null
}

export interface ProjectChecklistRead {
  id: string
  project_id: string
  control_group_id: string
  control_group_code: string
  control_group_name: string
  product_type: string
  lib_checklist_id: string | null
  title: string | null
  item_count: number
  na_count: number
  items?: ProjectChecklistItem[] | null
  created_at: string
}

export const projectsApi = {
  list: (params?: { product_family?: string; status?: string }) =>
    client.get<ProjectRead[]>('/projects', { params }).then(r => r.data),

  create: (body: ProjectCreate) =>
    client.post<ProjectRead>('/projects', body).then(r => r.data),

  get: (id: string) =>
    client.get<ProjectRead>(`/projects/${id}`).then(r => r.data),

  update: (id: string, body: ProjectPatch) =>
    client.patch<ProjectRead>(`/projects/${id}`, body).then(r => r.data),

  delete: (id: string) =>
    client.delete(`/projects/${id}`),

  // Library browsing
  libraryPolicies: (projectId: string, params?: { product_type?: string; language?: string }) =>
    client.get<LibraryPolicyItem[]>(`/projects/${projectId}/library/policies`, { params }).then(r => r.data),

  libraryImpls: (projectId: string, params?: { impl_type?: string }) =>
    client.get<LibraryImplItem[]>(`/projects/${projectId}/library/implementations`, { params }).then(r => r.data),

  // Re-apply doc vars to all library-sourced policies/impls
  reapplyDocVars: (projectId: string) =>
    client.post<{ status: string; updated_policies: number; updated_implementations: number; errors: string[] }>(`/projects/${projectId}/reapply-doc-vars`).then(r => r.data),

  // Project policies
  listPolicies: (projectId: string) =>
    client.get<ProjectPolicyRead[]>(`/projects/${projectId}/policies`).then(r => r.data),

  getPolicy: (projectId: string, ppId: string) =>
    client.get<ProjectPolicyRead>(`/projects/${projectId}/policies/${ppId}`).then(r => r.data),

  addPolicy: (projectId: string, body: { lib_policy_id?: string; custom_content?: string; stacking_locked?: boolean }) =>
    client.post<ProjectPolicyRead>(`/projects/${projectId}/policies`, body).then(r => r.data),

  updatePolicy: (projectId: string, ppId: string, body: { custom_content?: string; is_edited?: boolean; stale_warning?: boolean; status?: string }) =>
    client.patch<ProjectPolicyRead>(`/projects/${projectId}/policies/${ppId}`, body).then(r => r.data),

  removePolicy: (projectId: string, ppId: string) =>
    client.delete(`/projects/${projectId}/policies/${ppId}`),

  // Project implementations
  listImpls: (projectId: string) =>
    client.get<ProjectImplRead[]>(`/projects/${projectId}/implementations`).then(r => r.data),

  getImpl: (projectId: string, piId: string) =>
    client.get<ProjectImplRead>(`/projects/${projectId}/implementations/${piId}`).then(r => r.data),

  addImpl: (projectId: string, body: { lib_impl_id?: string; custom_content?: string }) =>
    client.post<ProjectImplRead>(`/projects/${projectId}/implementations`, body).then(r => r.data),

  updateImpl: (projectId: string, piId: string, body: { custom_content?: string; is_edited?: boolean; stale_warning?: boolean; status?: string }) =>
    client.patch<ProjectImplRead>(`/projects/${projectId}/implementations/${piId}`, body).then(r => r.data),

  removeImpl: (projectId: string, piId: string) =>
    client.delete(`/projects/${projectId}/implementations/${piId}`),

  // Library checklists
  libraryChecklists: (projectId: string) =>
    client.get<LibraryChecklistItem[]>(`/projects/${projectId}/library/checklists`).then(r => r.data),

  // Project checklists
  listChecklists: (projectId: string) =>
    client.get<ProjectChecklistRead[]>(`/projects/${projectId}/checklists`).then(r => r.data),

  addChecklist: (projectId: string, libChecklistId: string) =>
    client.post<ProjectChecklistRead>(`/projects/${projectId}/checklists`, { lib_checklist_id: libChecklistId }).then(r => r.data),

  getChecklist: (projectId: string, cid: string) =>
    client.get<ProjectChecklistRead>(`/projects/${projectId}/checklists/${cid}`).then(r => r.data),

  patchChecklistItem: (projectId: string, cid: string, body: { item_id: string; na: boolean; justification?: string | null }) =>
    client.patch<ProjectChecklistRead>(`/projects/${projectId}/checklists/${cid}/items`, body).then(r => r.data),

  removeChecklist: (projectId: string, cid: string) =>
    client.delete(`/projects/${projectId}/checklists/${cid}`),
}
