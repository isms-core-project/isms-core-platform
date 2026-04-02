import { client } from './client'

export interface ItsmTicket {
  id: string; source_type: string; source_id: string
  ticket_id: string; url: string | null; status: string
  connector_id: string; created_at: string; last_synced_at: string | null
}

export const itsmApi = {
  pushGap: (connectorId: string, gapId: string) =>
    client.post<{ ticket_id: string; url: string | null; status: string; already_exists: boolean }>(
      `/connectors/${connectorId}/push/gap/${gapId}`
    ).then(r => r.data),

  pushRemediation: (connectorId: string, actionId: string) =>
    client.post<{ ticket_id: string; url: string | null; status: string; already_exists: boolean }>(
      `/connectors/${connectorId}/push/remediation/${actionId}`
    ).then(r => r.data),

  listForSource: (sourceType: string, sourceId: string) =>
    client.get<ItsmTicket[]>(`/connectors/source/${sourceType}/${sourceId}/tickets`).then(r => r.data),

  syncTicket: (ticketId: string) =>
    client.post(`/connectors/tickets/${ticketId}/sync`).then(r => r.data),

  listConnectorTickets: (connectorId: string) =>
    client.get<ItsmTicket[]>(`/connectors/${connectorId}/tickets`).then(r => r.data),
}
