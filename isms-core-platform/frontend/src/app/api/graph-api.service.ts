import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'
import { GraphResponse } from '../shared/types'

@Injectable({ providedIn: 'root' })
export class GraphApiService {
  private http = inject(HttpClient)

  get(projectId: string, product: string): Observable<GraphResponse> {
    return this.http.get<GraphResponse>('/api/v1/graph/', {
      params: { project_id: projectId, product }
    })
  }
}
