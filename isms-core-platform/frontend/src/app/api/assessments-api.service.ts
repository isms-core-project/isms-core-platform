import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

function clean(params: Record<string, unknown>): Record<string, unknown> {
  return Object.fromEntries(Object.entries(params).filter(([, v]) => v !== undefined && v !== null))
}

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

export interface AssessmentCreateMeta {
  label?: string
  assessor?: string
  scope?: string
  purpose?: string
  target_date?: string
  project_id?: string
}

@Injectable({ providedIn: 'root' })
export class AssessmentsApiService {
  private http = inject(HttpClient)

  list(params?: { product?: string; product_family?: string; project_id?: string }): Observable<AssessmentListItem[]> {
    return this.http.get<AssessmentListItem[]>('/api/v1/assessments', { params: clean((params ?? {}) as Record<string, unknown>) as any })
  }

  create(
    group_code: string,
    product_type: string,
    workbook_name = '',
    meta: AssessmentCreateMeta = {}
  ): Observable<AssessmentListItem> {
    return this.http.post<AssessmentListItem>('/api/v1/assessments', {
      group_code, product_type, workbook_name,
      label: meta.label ?? '',
      assessor: meta.assessor ?? '',
      scope: meta.scope ?? '',
      purpose: meta.purpose ?? '',
      target_date: meta.target_date ?? '',
      project_id: meta.project_id ?? null,
    })
  }

  getSheets(assessmentId: string): Observable<AssessmentSheetRead[]> {
    return this.http.get<AssessmentSheetRead[]>(`/api/v1/assessments/${assessmentId}/sheets`)
  }

  addRow(assessmentId: string, row: {
    sheet_name: string; row_number: number; item_text?: string;
    status?: string; evidence_reference?: string; notes?: string; col_data?: Record<string, string>
  }): Observable<AssessmentItemRead> {
    return this.http.post<AssessmentItemRead>(`/api/v1/assessments/${assessmentId}/rows`, row)
  }

  updateItem(itemId: string, patch: {
    item_text?: string; status?: string; evidence_reference?: string;
    notes?: string; col_data?: Record<string, string>
  }): Observable<AssessmentItemRead> {
    return this.http.patch<AssessmentItemRead>(`/api/v1/assessments/items/${itemId}`, patch)
  }

  deleteItem(itemId: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/assessments/items/${itemId}`)
  }

  delete(assessmentId: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/assessments/${assessmentId}`)
  }
}
