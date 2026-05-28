import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

export interface NotificationRead {
  id: string
  event_type: string
  title: string
  message: string
  is_read: boolean
  created_at: string
  metadata: Record<string, unknown>
}

@Injectable({ providedIn: 'root' })
export class NotificationsApiService {
  private http = inject(HttpClient)

  list(): Observable<NotificationRead[]> {
    return this.http.get<NotificationRead[]>('/api/v1/notifications/')
  }

  markRead(id: string): Observable<void> {
    return this.http.post<void>(`/api/v1/notifications/${id}/read`, {})
  }

  markAllRead(): Observable<void> {
    return this.http.post<void>('/api/v1/notifications/read-all', {})
  }
}
