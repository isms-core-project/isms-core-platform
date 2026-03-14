import { client } from './client'

export interface AssessmentListItem {
  id: string
  control_group_id: string
  group_code: string
  group_name: string
  product_type: string
  assessment_type: string
  document_id: string
  workbook_name: string
  file_path: string
  sheets_count: number
  summary: Record<string, string>
  overall_score: number | null
  items_total: number
  items_compliant: number
  items_partial: number
  items_non_compliant: number
  items_na: number
  gaps_count: number
  last_parsed: string | null
}

export interface FormColumn {
  index: number
  letter: string
  header: string
  dv_values: string[]
  is_status_col: boolean
  required: boolean
  width: number
}

export interface FormSheet {
  generator_document_id: string
  sheet_name: string
  title_text: string
  subtitle_text: string | null
  columns: FormColumn[]
  sample_row: string[]
  status_column_letter: string | null
}

export interface AssessmentItemRead {
  id: string
  sheet_id: string
  status: string
  row_number: number
  item_text: string | null
  evidence_reference: string | null
  notes: string | null
  col_data: Record<string, string>
}

export interface AssessmentSheetRead {
  id: string
  sheet_name: string
  sheet_type: string
  row_count: number
  items: AssessmentItemRead[]
}

export const assessmentsApi = {
  list: (params?: { product?: string; product_family?: string }) =>
    client
      .get<AssessmentListItem[]>('/assessments/', { params: params ?? undefined })
      .then((r) => r.data),

  create: (
    group_code: string,
    product_type: string,
    workbook_name?: string,
    meta?: { label?: string; assessor?: string; scope?: string; purpose?: string; target_date?: string }
  ) =>
    client.post<AssessmentListItem>('/assessments/', {
      group_code, product_type, workbook_name: workbook_name ?? '',
      label: meta?.label ?? '',
      assessor: meta?.assessor ?? '',
      scope: meta?.scope ?? '',
      purpose: meta?.purpose ?? '',
      target_date: meta?.target_date ?? '',
    }).then((r) => r.data),

  getSheets: (assessmentId: string) =>
    client.get<AssessmentSheetRead[]>(`/assessments/${assessmentId}/sheets`).then((r) => r.data),

  addRow: (assessmentId: string, row: {
    sheet_name: string; row_number: number; item_text?: string;
    status?: string; evidence_reference?: string; notes?: string; col_data?: Record<string, string>
  }) =>
    client.post<AssessmentItemRead>(`/assessments/${assessmentId}/rows`, row).then((r) => r.data),

  updateItem: (itemId: string, patch: {
    item_text?: string; status?: string; evidence_reference?: string;
    notes?: string; col_data?: Record<string, string>
  }) =>
    client.patch<AssessmentItemRead>(`/assessments/items/${itemId}`, patch).then((r) => r.data),

  deleteItem: (itemId: string) =>
    client.delete(`/assessments/items/${itemId}`),

  deleteAssessment: (assessmentId: string) =>
    client.delete(`/assessments/${assessmentId}`),

  patchItem: (itemId: string, status: string) =>
    client.patch(`/assessments/items/${itemId}`, { status }).then((r) => r.data),

  getFormSchema: (groupCode: string, productType = 'framework', generatorId?: string) =>
    client.get<FormSheet[]>(`/generators/form/${groupCode}`, {
      params: { product_type: productType, ...(generatorId ? { generator_id: generatorId } : {}) },
    }).then((r) => r.data),

  getGeneratorsForGroup: (groupCode: string) =>
    client.get<{ document_id: string; workbook_name: string; sheet_count: number }[]>(
      `/generators/`, { params: { group_code: groupCode } }
    ).then((r) => r.data),
}
