import { client } from './client'
import type { CorrelationResultRead, ExistenceRunResult, KeywordRunResult, QASummary, SemanticRunResult, SynonymRule } from './types'

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
}
