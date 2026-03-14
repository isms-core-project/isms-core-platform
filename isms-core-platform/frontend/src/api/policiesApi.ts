import { client } from './client'

export interface PolicyListItem {
  id: string
  control_group_id: string
  group_code: string
  group_name: string
  product_type: string
  policy_type: string
  document_id: string
  title: string
  word_count: number | null
  requirements_count: number
  last_parsed: string | null
  source_label: string | null
  language: string | null
}

export const policiesApi = {
  list: (params?: { product?: string; policy_type?: string }) =>
    client
      .get<PolicyListItem[]>('/policies/', { params })
      .then((r) => r.data),

  delete: (id: string) =>
    client.delete(`/policies/${id}`),

  importExternal: (file: File, groupCode: string, sourceLabel: string, language: string) => {
    const form = new FormData()
    form.append('file', file)
    form.append('group_code', groupCode)
    form.append('source_label', sourceLabel)
    form.append('language', language)
    return client
      .post<{ document_id: string; title: string; word_count: number; requirements_extracted: number }>('/admin/import-external', form, {
        headers: { 'Content-Type': 'multipart/form-data' },
      })
      .then((r) => r.data)
  },
}
