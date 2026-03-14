import { client } from './client'

export interface SheetInfo {
  name: string
  type: 'instructions' | 'input' | 'summary' | 'evidence' | 'approval'
}

export interface SheetColumn {
  index: number
  letter: string
  header: string
  header_raw: string
  width: number
  dv_values: string[]
  dv_allow_blank: boolean
  required: boolean
  is_status_col: boolean
}

export interface SheetSchema {
  sheet_name: string
  sheet_type: string
  position: number
  title_text: string | null
  subtitle_text: string | null
  header_row: number | null
  data_start_row: number | null
  freeze_panes: string | null
  hide_gridlines: boolean
  columns: SheetColumn[]
  status_column_index: number | null
  status_column_letter: string | null
  sample_row: string[]
}

export interface GeneratorItem {
  id: string
  document_id: string
  workbook_name: string
  control_id: string
  control_name: string
  group_code: string
  control_group_id: string | null
  domain_number: number | null
  domain_total: number | null
  is_stacked: boolean
  stacked_control_ids: string[] | null
  sheets: SheetInfo[]
  sheet_count: number
  sheet_schemas: SheetSchema[]
  product_type: string
  source_file: string | null
  parsed_at: string | null
  user_override: boolean
}

export interface GeneratorUpdate {
  workbook_name: string
  domain_number: number | null
  domain_total: number | null
  sheets: SheetInfo[]
}

export interface GeneratorGroup {
  group_code: string
  control_name: string
  section: string
  generators: GeneratorItem[]
  total_domains: number
}

export const generatorsApi = {
  list: (params?: { section?: string; group_code?: string; product?: string }) =>
    client.get<GeneratorItem[]>('/generators/', { params }).then(r => r.data),

  grouped: (params?: { section?: string; product?: string }) =>
    client.get<GeneratorGroup[]>('/generators/grouped', { params }).then(r => r.data),

  get: (documentId: string) =>
    client.get<GeneratorItem>(`/generators/${documentId}`).then(r => r.data),

  update: (documentId: string, body: GeneratorUpdate) =>
    client.put<GeneratorItem>(`/generators/${documentId}`, body).then(r => r.data),

  clearOverride: (documentId: string) =>
    client.delete<GeneratorItem>(`/generators/${documentId}/override`).then(r => r.data),

  generateScript: (documentId: string) =>
    client.post(`/generators/${documentId}/generate`, null, { responseType: 'blob' }).then(r => ({
      blob: r.data as Blob,
      filename: (r.headers['content-disposition'] as string | undefined)?.match(/filename="(.+)"/)?.[1] ?? `${documentId}.py`,
    })),
}
