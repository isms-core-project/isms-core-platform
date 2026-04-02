import { client } from './client'

export interface CustomFramework {
  id: string; org_id: string; name: string; short_code: string
  version: string; description: string | null
  control_count: number; status: string
  created_at: string; updated_at: string
}

export interface CustomControl {
  id: string; framework_id: string; control_id: string; title: string
  description: string | null; category: string | null; subcategory: string | null
  priority: string | null; iso_mappings: string[]; tags: string[]
  created_at: string
}

export const customFrameworksApi = {
  list: () => client.get<CustomFramework[]>('/custom-frameworks').then(r => r.data),
  get: (id: string) => client.get<CustomFramework & { controls: CustomControl[] }>(`/custom-frameworks/${id}`).then(r => r.data),
  importYaml: (yaml_content: string) => client.post<CustomFramework>('/custom-frameworks', { yaml_content }).then(r => r.data),
  delete: (id: string) => client.delete(`/custom-frameworks/${id}`),
  listControls: (id: string, params?: { category?: string; search?: string }) =>
    client.get<CustomControl[]>(`/custom-frameworks/${id}/controls`, { params }).then(r => r.data),
}
