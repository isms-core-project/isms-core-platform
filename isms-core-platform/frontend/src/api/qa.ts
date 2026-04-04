import { client } from './client'
import type { CorrelationResultRead, ExistenceRunResult, KeywordRunResult, QASummary, SemanticRunResult, SynonymRule } from './types'

export type { CorrelationResultRead } from './types'

export const qaApi = {
  runExistence: () =>
    client.post<ExistenceRunResult>('/qa/run-existence').then((r) => r.data),

  runKeyword: () =>
    client.post<KeywordRunResult>('/qa/run-keyword').then((r) => r.data),

  runSemanticMini: () =>
    client.post<SemanticRunResult>('/qa/run-semantic').then((r) => r.data),

  runSemanticClaude: () =>
    client.post<SemanticRunResult>('/qa/run-semantic-claude').then((r) => r.data),

  getResults: (params?: { product_type?: string; status?: string; method?: string; limit?: number }) =>
    client.get<CorrelationResultRead[]>('/qa/results', { params }).then((r) => r.data),

  getSummary: (method?: string, product_type?: string) =>
    client.get<QASummary>('/qa/summary', { params: { ...(method ? { method } : {}), ...(product_type && product_type !== 'all' ? { product_type } : {}) } }).then((r) => r.data),

  getSynonyms: () =>
    client.get<SynonymRule[]>('/qa/synonyms').then((r) => r.data),

  createSynonym: (body: { keyword: string; synonyms: string[]; notes?: string }) =>
    client.post<SynonymRule>('/qa/synonyms', body).then((r) => r.data),

  updateSynonym: (id: string, body: { synonyms?: string[]; notes?: string }) =>
    client.patch<SynonymRule>(`/qa/synonyms/${id}`, body).then((r) => r.data),

  deleteSynonym: (id: string) =>
    client.delete(`/qa/synonyms/${id}`),

  getReferenceCorpusStatus: () =>
    client.get<ReferenceCorpusStatus>('/qa/reference-corpus/status').then((r) => r.data),

  reloadReferenceCorpus: () =>
    client.post<ReferenceCorpusLoadResult>('/qa/reference-corpus/reload').then((r) => r.data),

  // Phase 21 — project-scoped QA
  runProjectExistence: (projectId: string) =>
    client.post<ExistenceRunResult>(`/qa/project/${projectId}/run-existence`).then((r) => r.data),

  runProjectKeyword: (projectId: string, referenceLibrary = 'iso_corpus', language = 'en', frameworkCodes?: string[]) =>
    client.post<KeywordRunResult>(`/qa/project/${projectId}/run-keyword`, null, {
      params: { reference_library: referenceLibrary, language, ...(frameworkCodes?.length ? { framework_codes: frameworkCodes } : {}) },
    }).then((r) => r.data),

  runProjectSemantic: (projectId: string, referenceLibrary = 'iso_corpus', language = 'en', frameworkCodes?: string[]) =>
    client.post<SemanticRunResult>(`/qa/project/${projectId}/run-semantic`, null, {
      params: { reference_library: referenceLibrary, language, ...(frameworkCodes?.length ? { framework_codes: frameworkCodes } : {}) },
    }).then((r) => r.data),

  runProjectSemanticClaude: (projectId: string, referenceLibrary = 'iso_corpus', language = 'en', frameworkCodes?: string[]) =>
    client.post<SemanticRunResult>(`/qa/project/${projectId}/run-semantic-claude`, null, {
      params: { reference_library: referenceLibrary, language, ...(frameworkCodes?.length ? { framework_codes: frameworkCodes } : {}) },
    }).then((r) => r.data),

  getProjectResults: (projectId: string, params?: { method?: string; status?: string; limit?: number }) =>
    client.get<CorrelationResultRead[]>(`/qa/project/${projectId}/results`, { params }).then((r) => r.data),

  getProjectSummary: (projectId: string, method = 'existence') =>
    client.get<ProjectQASummary>(`/qa/project/${projectId}/summary`, { params: { method } }).then((r) => r.data),

  getOrgProjectSummaries: (method = 'existence') =>
    client.get<OrgProjectSummaryItem[]>('/qa/org/projects', { params: { method } }).then((r) => r.data),

  seedKeywordTranslations: () =>
    client.post('/qa/seed-keyword-translations').then((r) => r.data),
}

export interface ReferenceCorpusStatus {
  available: boolean
  indexed: boolean
  total_chunks: number
  standards: { standard: string; chunks: number }[]
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

export interface ReferenceCorpusLoadResult {
  loaded_files: number
  failed_files: number
  total_chunks: number
  standards: { standard: string; chunks: number }[]
  duration_ms: number
  loaded_at?: string
  error?: string
}
