import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

export interface ExistenceRunResult {
  total: number
  pass_count: number
  warning_count: number
  fail_count: number
  needs_review_count: number
  duration_ms: number
  run_date: string
}

export interface SynonymRule {
  id: string
  keyword: string
  synonyms: string[]
  notes: string | null
  created_at: string
}

export interface KeywordRunResult {
  total: number
  pass_count: number
  warning_count: number
  fail_count: number
  needs_review_count: number
  duration_ms: number
  run_date: string
}

export interface SemanticRunResult {
  total: number
  pass_count: number
  warning_count: number
  fail_count: number
  needs_review_count: number
  duration_ms: number
  run_date: string
  method: string
}

export interface CorrelationResultRead {
  id: string
  control_group_id: string
  control_group_code: string
  control_group_name: string
  document_id: string
  product_type: string
  correlation_method: string
  correlation_strength: number
  qa_status: string
  coverage_keywords: string[]
  missing_keywords: string[]
  run_date: string
  metadata: Record<string, unknown>
  reference_library: string | null
  result_view: string
}

export interface QASummaryBucket {
  total: number
  pass_count: number
  warning_count: number
  fail_count: number
  needs_review_count: number
  pass_rate: number
}

export interface QASummary {
  framework: QASummaryBucket
  operational: QASummaryBucket
  privacy: QASummaryBucket
  cloud: QASummaryBucket
  ai: QASummaryBucket
}

export interface ReferenceCorpusStatus {
  available: boolean
  indexed: boolean
  total_chunks: number
  standards: { standard: string; chunks: number }[]
  error?: string
}

export interface ReferenceCorpusLoadResult {
  loaded_files: number
  failed_files: number
  total_chunks: number
  standards: { standard: string; chunks: number }[]
  duration_ms: number
  loaded_at?: string
  error?: string
}

export interface ProjectQASummary {
  total: number
  pass: number
  warning: number
  fail: number
  needs_review: number
  pass_rate: number
  last_run: string | null
  method: string
}

export interface OrgProjectSummaryItem extends ProjectQASummary {
  project_id: string
  project_name: string
  product_family: string
}

@Injectable({ providedIn: 'root' })
export class QaApiService {
  private http = inject(HttpClient)

  runExistence(): Observable<ExistenceRunResult> {
    return this.http.post<ExistenceRunResult>('/api/v1/qa/run-existence', {})
  }

  runKeyword(): Observable<KeywordRunResult> {
    return this.http.post<KeywordRunResult>('/api/v1/qa/run-keyword', {})
  }

  runSemanticMini(): Observable<SemanticRunResult> {
    return this.http.post<SemanticRunResult>('/api/v1/qa/run-semantic', {})
  }

  runSemanticClaude(): Observable<SemanticRunResult> {
    return this.http.post<SemanticRunResult>('/api/v1/qa/run-semantic-claude', {})
  }

  getResults(params?: { product_type?: string; status?: string; method?: string; limit?: number }): Observable<CorrelationResultRead[]> {
    const p = params ? Object.fromEntries(Object.entries(params).filter(([, v]) => v != null && v !== '')) : {}
    return this.http.get<CorrelationResultRead[]>('/api/v1/qa/results', { params: p as any })
  }

  getSummary(method?: string, product_type?: string): Observable<QASummary> {
    const params: Record<string, string> = {}
    if (method) params['method'] = method
    if (product_type && product_type !== 'all') params['product_type'] = product_type
    return this.http.get<QASummary>('/api/v1/qa/summary', { params })
  }

  getSynonyms(): Observable<SynonymRule[]> {
    return this.http.get<SynonymRule[]>('/api/v1/qa/synonyms')
  }

  createSynonym(body: { keyword: string; synonyms: string[]; notes?: string }): Observable<SynonymRule> {
    return this.http.post<SynonymRule>('/api/v1/qa/synonyms', body)
  }

  updateSynonym(id: string, body: { synonyms?: string[]; notes?: string }): Observable<SynonymRule> {
    return this.http.patch<SynonymRule>(`/api/v1/qa/synonyms/${id}`, body)
  }

  deleteSynonym(id: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/qa/synonyms/${id}`)
  }

  getReferenceCorpusStatus(): Observable<ReferenceCorpusStatus> {
    return this.http.get<ReferenceCorpusStatus>('/api/v1/qa/reference-corpus/status')
  }

  reloadReferenceCorpus(): Observable<ReferenceCorpusLoadResult> {
    return this.http.post<ReferenceCorpusLoadResult>('/api/v1/qa/reference-corpus/reload', {})
  }

  runProjectExistence(projectId: string): Observable<ExistenceRunResult> {
    return this.http.post<ExistenceRunResult>(`/api/v1/qa/project/${projectId}/run-existence`, {})
  }

  runProjectKeyword(projectId: string, referenceLibrary = 'iso_corpus', language = 'en', frameworkCodes?: string[]): Observable<KeywordRunResult> {
    const params: Record<string, string | string[]> = { reference_library: referenceLibrary, language }
    if (frameworkCodes?.length) params['framework_codes'] = frameworkCodes
    return this.http.post<KeywordRunResult>(`/api/v1/qa/project/${projectId}/run-keyword`, null, { params })
  }

  runProjectSemantic(projectId: string, referenceLibrary = 'iso_corpus', language = 'en', frameworkCodes?: string[]): Observable<SemanticRunResult> {
    const params: Record<string, string | string[]> = { reference_library: referenceLibrary, language }
    if (frameworkCodes?.length) params['framework_codes'] = frameworkCodes
    return this.http.post<SemanticRunResult>(`/api/v1/qa/project/${projectId}/run-semantic`, null, { params })
  }

  runProjectSemanticClaude(projectId: string, referenceLibrary = 'iso_corpus', language = 'en', frameworkCodes?: string[]): Observable<SemanticRunResult> {
    const params: Record<string, string | string[]> = { reference_library: referenceLibrary, language }
    if (frameworkCodes?.length) params['framework_codes'] = frameworkCodes
    return this.http.post<SemanticRunResult>(`/api/v1/qa/project/${projectId}/run-semantic-claude`, null, { params })
  }

  getProjectResults(projectId: string, params?: { method?: string; status?: string; limit?: number }): Observable<CorrelationResultRead[]> {
    const p = params ? Object.fromEntries(Object.entries(params).filter(([, v]) => v != null && v !== '')) : {}
    return this.http.get<CorrelationResultRead[]>(`/api/v1/qa/project/${projectId}/results`, { params: p as any })
  }

  getProjectSummary(projectId: string, method = 'existence'): Observable<ProjectQASummary> {
    return this.http.get<ProjectQASummary>(`/api/v1/qa/project/${projectId}/summary`, { params: { method } })
  }

  getOrgProjectSummaries(method = 'existence'): Observable<OrgProjectSummaryItem[]> {
    return this.http.get<OrgProjectSummaryItem[]>('/api/v1/qa/org/projects', { params: { method } })
  }

  seedKeywordTranslations(): Observable<unknown> {
    return this.http.post('/api/v1/qa/seed-keyword-translations', {})
  }
}
