import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'

export interface Vendor {
  id: string
  org_id: string
  name: string
  vendor_type: string
  criticality: string
  status: string
  description: string | null
  website: string | null
  primary_contact: string | null
  dora_entity_type: string | null
  dora_ict_service_type: string | null
  dora_substitutability: string | null
  dora_register_ref: string | null
  assessment_count: number
  contract_count: number
  last_assessment_date: string | null
  contracts_expiring_soon: number
  created_at: string
}

export interface VendorCreate {
  name: string
  vendor_type?: string
  criticality?: string
  status?: string
  description?: string
  website?: string
  primary_contact?: string
  dora_entity_type?: string
  dora_ict_service_type?: string
  dora_substitutability?: string
  dora_register_ref?: string
}

export interface VendorAssessment {
  id: string
  vendor_id: string
  score: number | null
  status: string
  notes: string | null
  assessment_date: string | null
  next_review_date: string | null
  control_group_id: string | null
  created_at: string
}

export interface VendorContract {
  id: string
  vendor_id: string
  title: string
  contract_ref: string | null
  start_date: string | null
  expiry_date: string | null
  auto_renews: boolean
  security_clauses_present: boolean
  is_expired: boolean
  expiring_soon: boolean
  created_at: string
}

export interface VendorSummary {
  total: number
  active: number
  critical: number
  dora_regulated: number
  contracts_expiring_soon: number
}

@Injectable({ providedIn: 'root' })
export class TprmApiService {
  private http = inject(HttpClient)

  summary(): Observable<VendorSummary> {
    return this.http.get<VendorSummary>('/api/v1/vendors/summary')
  }

  list(params?: { criticality?: string; status?: string }): Observable<Vendor[]> {
    return this.http.get<Vendor[]>('/api/v1/vendors', { params })
  }

  get(id: string): Observable<Vendor> {
    return this.http.get<Vendor>(`/api/v1/vendors/${id}`)
  }

  create(body: VendorCreate): Observable<Vendor> {
    return this.http.post<Vendor>('/api/v1/vendors', body)
  }

  update(id: string, body: Partial<VendorCreate>): Observable<Vendor> {
    return this.http.patch<Vendor>(`/api/v1/vendors/${id}`, body)
  }

  delete(id: string): Observable<void> {
    return this.http.delete<void>(`/api/v1/vendors/${id}`)
  }

  doraRegister(): Observable<Vendor[]> {
    return this.http.get<Vendor[]>('/api/v1/vendors/dora')
  }

  listAssessments(vendorId: string): Observable<VendorAssessment[]> {
    return this.http.get<VendorAssessment[]>(`/api/v1/vendors/${vendorId}/assessments`)
  }

  createAssessment(vendorId: string, body: object): Observable<VendorAssessment> {
    return this.http.post<VendorAssessment>(`/api/v1/vendors/${vendorId}/assessments`, body)
  }

  listContracts(vendorId: string): Observable<VendorContract[]> {
    return this.http.get<VendorContract[]>(`/api/v1/vendors/${vendorId}/contracts`)
  }

  createContract(vendorId: string, body: object): Observable<VendorContract> {
    return this.http.post<VendorContract>(`/api/v1/vendors/${vendorId}/contracts`, body)
  }
}
