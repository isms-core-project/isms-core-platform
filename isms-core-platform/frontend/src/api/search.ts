import { client } from './client'
import type { SearchResponse } from './types'

export const searchApi = {
  search: (params: {
    q: string
    doc_type?: string
    control_group?: string
    product?: string
    limit?: number
    offset?: number
  }) =>
    client.get<SearchResponse>('/search', { params }).then((r) => r.data),

  status: () =>
    client.get<{ available: boolean }>('/search/status').then((r) => r.data),
}
