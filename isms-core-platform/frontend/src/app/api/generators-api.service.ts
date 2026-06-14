import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

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

export interface GeneratorBlob {
  blob: Blob
  filename: string
}

@Injectable({ providedIn: 'root' })
export class GeneratorsApiService {
  private http = inject(HttpClient)

  list(params?: { section?: string; group_code?: string; product?: string }): Observable<GeneratorItem[]> {
    return this.http.get<GeneratorItem[]>('/api/v1/generators/', { params })
  }

  grouped(params?: { section?: string; product?: string }): Observable<GeneratorGroup[]> {
    return this.http.get<GeneratorGroup[]>('/api/v1/generators/grouped', { params })
  }

  get(documentId: string): Observable<GeneratorItem> {
    return this.http.get<GeneratorItem>(`/api/v1/generators/${documentId}`)
  }

  update(documentId: string, body: GeneratorUpdate): Observable<GeneratorItem> {
    return this.http.put<GeneratorItem>(`/api/v1/generators/${documentId}`, body)
  }

  clearOverride(documentId: string): Observable<GeneratorItem> {
    return this.http.delete<GeneratorItem>(`/api/v1/generators/${documentId}/override`)
  }

  generateScript(documentId: string): Observable<Blob> {
    return this.http.post(`/api/v1/generators/${documentId}/generate`, null, { responseType: 'blob' }) as Observable<Blob>
  }

  generateWorkbook(documentId: string): Observable<Blob> {
    return this.http.post(`/api/v1/generators/${documentId}/workbook`, null, { responseType: 'blob' }) as Observable<Blob>
  }
}
