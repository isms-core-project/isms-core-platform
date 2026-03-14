import { client } from './client'
import type { GraphResponse } from './types'

export const graphApi = {
  get: (params?: {
    source_framework?: string
    center?: string
    depth?: number
    edge_types?: string
    section?: string
    max_nodes?: number
  }) =>
    client.get<GraphResponse>('/graph', { params }).then((r) => r.data),
}
