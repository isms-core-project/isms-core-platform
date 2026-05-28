import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

export interface ItsmTicketCreate {
  control_group_id: string
  gap_id?: string
  title: string
  description: string
  priority?: string
}

export interface ItsmTicketRead {
  id: string
  external_id: string
  control_group_id: string
  gap_id: string | null
  title: string
  status: string
  priority: string
  external_url: string | null
  created_at: string
  updated_at: string
}

@Injectable({ providedIn: 'root' })
export class ItsmApiService {
  private http = inject(HttpClient)

  createTicket(data: ItsmTicketCreate): Observable<ItsmTicketRead> {
    return this.http.post<ItsmTicketRead>('/api/v1/itsm/tickets', data)
  }

  getTicket(id: string): Observable<ItsmTicketRead> {
    return this.http.get<ItsmTicketRead>(`/api/v1/itsm/tickets/${id}`)
  }

  listTickets(controlId: string): Observable<ItsmTicketRead[]> {
    return this.http.get<ItsmTicketRead[]>('/api/v1/itsm/tickets', {
      params: { control_group_id: controlId }
    })
  }
}
