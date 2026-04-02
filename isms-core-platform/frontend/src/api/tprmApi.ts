import { client } from './client'

export interface Vendor {
  id: string; org_id: string; name: string; vendor_type: string
  criticality: string; status: string; description: string | null
  website: string | null; primary_contact: string | null
  dora_entity_type: string | null; dora_ict_service_type: string | null
  dora_substitutability: string | null; dora_register_ref: string | null
  assessment_count: number; contract_count: number
  last_assessment_date: string | null; contracts_expiring_soon: number
  created_at: string
}

export interface VendorCreate {
  name: string; vendor_type?: string; criticality?: string; status?: string
  description?: string; website?: string; primary_contact?: string
  dora_entity_type?: string; dora_ict_service_type?: string
  dora_substitutability?: string; dora_register_ref?: string
}

export interface VendorAssessment {
  id: string; vendor_id: string; score: number | null; status: string
  notes: string | null; assessment_date: string | null
  next_review_date: string | null; control_group_id: string | null; created_at: string
}

export interface VendorContract {
  id: string; vendor_id: string; title: string; contract_ref: string | null
  start_date: string | null; expiry_date: string | null
  auto_renews: boolean; security_clauses_present: boolean
  is_expired: boolean; expiring_soon: boolean; created_at: string
}

export interface VendorSummary {
  total: number; active: number; critical: number
  dora_regulated: number; contracts_expiring_soon: number
}

export const tprmApi = {
  summary: () => client.get<VendorSummary>('/vendors/summary').then(r => r.data),
  list: (params?: { criticality?: string; status?: string }) =>
    client.get<Vendor[]>('/vendors', { params }).then(r => r.data),
  get: (id: string) => client.get<Vendor>(`/vendors/${id}`).then(r => r.data),
  create: (body: VendorCreate) => client.post<Vendor>('/vendors', body).then(r => r.data),
  update: (id: string, body: Partial<VendorCreate>) => client.patch<Vendor>(`/vendors/${id}`, body).then(r => r.data),
  delete: (id: string) => client.delete(`/vendors/${id}`),
  doraRegister: () => client.get<Vendor[]>('/vendors/dora').then(r => r.data),
  listAssessments: (vendorId: string) => client.get<VendorAssessment[]>(`/vendors/${vendorId}/assessments`).then(r => r.data),
  createAssessment: (vendorId: string, body: object) => client.post(`/vendors/${vendorId}/assessments`, body).then(r => r.data),
  listContracts: (vendorId: string) => client.get<VendorContract[]>(`/vendors/${vendorId}/contracts`).then(r => r.data),
  createContract: (vendorId: string, body: object) => client.post(`/vendors/${vendorId}/contracts`, body).then(r => r.data),
}
