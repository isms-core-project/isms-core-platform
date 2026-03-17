// ---------------------------------------------------------------------------
// Auth
// ---------------------------------------------------------------------------

export interface LoginRequest {
  email: string
  password: string
}

export interface TokenResponse {
  access_token: string
  refresh_token: string
  token_type: string
}

export interface UserInfo {
  id: string
  email: string
  full_name: string | null
  role: string
  is_active: boolean
}

// ---------------------------------------------------------------------------
// Control Groups
// ---------------------------------------------------------------------------

export interface ControlGroupList {
  id: string
  group_code: string
  group_name: string
  section: string
  product_type: string
  is_active: boolean
  created_at: string
}

export interface PolicySummary {
  id: string
  document_id: string
  title: string
  policy_type: string
  product_type: string
  word_count: number
  requirements_count: number
}

export interface ImplSummary {
  id: string
  document_id: string
  title: string
  impl_type: string
  product_type: string
  word_count: number
}

export interface SheetSummary {
  id: string
  sheet_name: string
  assessment_area: string
  max_score: number
  actual_score: number | null
  compliance_level: string | null
}

export interface AssessmentSummary {
  id: string
  document_id: string
  assessment_type: string
  product_type: string
  total_sheets: number
  total_items: number
  sheets: SheetSummary[]
}

export interface ExternalMappingEntry {
  framework: string
  control_ref: string
  control_name: string
  mapping_type: string
}

export interface IsoControlSummary {
  id: string
  control_ref: string
  title: string
  level: number
  external_mappings: ExternalMappingEntry[]
}

export interface GapItem {
  id: string
  gap_type: string
  severity: string
  status: string
  description: string
  detected_at: string
}

export interface EvidenceItem {
  id: string
  title: string
  evidence_type: string
  collected_date: string | null
  expires_date: string | null
  verified_by: string | null
}

export interface ControlGroupRichDetail {
  id: string
  group_code: string
  group_name: string
  section: string
  product_type: string
  is_active: boolean
  created_at: string
  policies: PolicySummary[]
  implementations: ImplSummary[]
  assessments: AssessmentSummary[]
  iso_controls: IsoControlSummary[]
  gaps: GapItem[]
  evidence: EvidenceItem[]
  requirements_total: number
  gaps_open: number
  evidence_total: number
}

// ---------------------------------------------------------------------------
// Dashboard
// ---------------------------------------------------------------------------

export interface SectionSummary {
  section: string
  total: number
  with_policy: number
  with_impl: number
  with_assessment: number
  with_evidence: number
  coverage_pct: number
}

export interface ProductCoverage {
  controls_total: number
  policies: number
  implementations: number
  assessments: number
  evidence: number
  gaps_open: number
}

export interface DashboardOverview {
  total_controls: number
  total_iso_controls: number
  total_policies: number
  total_implementations: number
  total_assessments: number
  total_evidence: number
  total_requirements: number
  total_cross_framework_mappings: number
  framework: ProductCoverage
  operational: ProductCoverage
  sections: SectionSummary[]
}

export interface CoverageRow {
  group_code: string
  group_name: string
  section: string
  iso_controls: string[]
  mappings: Record<string, string[]>
}

export interface CoverageMatrix {
  target_framework: string
  total_iso_controls: number
  mapped_count: number
  coverage_pct: number
  rows: CoverageRow[]
}

export interface GapSummary {
  total: number
  by_severity: Record<string, number>
  by_status: Record<string, number>
  items: GapItemDashboard[]
}

export interface GapItemDashboard {
  id: string
  control_group_code: string
  control_group_name: string
  gap_type: string
  severity: string
  status: string
  description: string
  product_type: string
  detected_at: string
}

export interface GapRead {
  id: string
  control_group_id: string
  control_group_code: string
  control_group_name: string
  gap_description: string
  severity: string
  status: string
  product_type: string
  owner: string | null
  due_date: string | null
  remediation_plan: string | null
  closed_date: string | null
  closed_by: string | null
  created_at: string
  evidence_count: number
}

export interface GapCreate {
  control_group_id: string
  gap_description: string
  severity: string
  product_type: string
  owner?: string
  due_date?: string
  remediation_plan?: string
  workbook_document_id?: string
}

export interface GapPatch {
  gap_description?: string
  severity?: string
  status?: string
  owner?: string | null
  due_date?: string | null
  remediation_plan?: string | null
  closed_by?: string | null
}

export interface EvidenceControlItem {
  control_group_id: string
  group_code: string
  group_name: string
  evidence_count: number
  verified_count: number
  expiring_soon: number
}

export interface EvidenceSummary {
  total_evidence: number
  verified: number
  unverified: number
  expiring_30d: number
  controls_with_evidence: number
  controls_without_evidence: number
  items: EvidenceControlItem[]
}

export interface AuditReadiness {
  composite_score: number
  status: 'green' | 'amber' | 'red'
  components: {
    policies: number
    user_guides: number
    technical_guides: number
    assessments: number
    evidence: number
    gaps: number
  }
  breakdown: {
    total_controls: number
    controls_with_policy: number
    controls_with_ug: number
    controls_with_tg: number
    controls_with_assessment: number
    controls_with_evidence: number
    open_gaps: number
  }
}

// ---------------------------------------------------------------------------
// Graph
// ---------------------------------------------------------------------------

export interface GraphNode {
  id: string
  label: string
  type: 'control_group' | 'iso_control' | 'external_ref'
  section?: string
  product_type?: string
  framework?: string
}

export interface GraphEdge {
  source: string
  target: string
  edge_type: string
  label: string
}

export interface GraphResponse {
  nodes: GraphNode[]
  edges: GraphEdge[]
  total_nodes: number
  total_edges: number
}

// ---------------------------------------------------------------------------
// Search
// ---------------------------------------------------------------------------

export interface SearchResult {
  document_id: string
  title: string
  type: 'implementation' | 'policy'
  score: number
  control_group_code: string
  control_group_name: string
  product_type: string
  impl_type?: string
  policy_type?: string
  word_count: number
  snippet: string
  highlights: Record<string, string[]>
}

export interface SearchResponse {
  total: number
  hits: SearchResult[]
  took_ms: number
  available: boolean
  error?: string
}

// ---------------------------------------------------------------------------
// Evidence
// ---------------------------------------------------------------------------

export interface EvidenceRead {
  id: string
  control_group_id: string | null
  requirement_id: string | null
  assessment_item_id: string | null
  evidence_type: string
  evidence_status: 'draft' | 'pending_review' | 'approved' | 'rejected' | 'active'
  title: string
  file_path: string
  collected_date: string | null
  expires_date: string | null
  verified_by: string | null
  verified_date: string | null
  created_at: string
  metadata: {
    original_filename: string
    file_size: number
    file_ext: string
    content_hash: string
    word_count: number
    notes: string
    text_preview: string
    rejection_reason?: string
    approval_note?: string
  }
}

export interface EvidenceUpdate {
  title?: string
  evidence_type?: string
  collected_date?: string
  expires_date?: string
  verified_by?: string
  verified_date?: string
  notes?: string
}

// ---------------------------------------------------------------------------
// Admin / Sync
// ---------------------------------------------------------------------------

export interface SyncResult {
  status: string
  total_imported: number
  errors: number
  details: Record<string, unknown>
}

export interface UserRead {
  id: string
  email: string
  username: string
  full_name: string | null
  role: string
  is_active: boolean
  last_login: string | null
  created_at: string
  notification_prefs: Record<string, boolean>
}

export interface UserCreate {
  email: string
  username: string
  full_name?: string
  password: string
  role: string
}

export interface UserPatch {
  full_name?: string | null
  role?: string
  is_active?: boolean
  password?: string
  notification_prefs?: Record<string, boolean>
}

export interface NotificationPref {
  event_type: string
  label: string
  category: string
  description: string
  enabled: boolean
}

export interface NotificationPrefsResponse {
  prefs: NotificationPref[]
}

// ---------------------------------------------------------------------------
// QA / Correlation Engine
// ---------------------------------------------------------------------------

export interface ExistenceRunResult {
  total: number
  pass_count: number
  warning_count: number
  fail_count: number
  needs_review_count: number
  duration_ms: number
  run_date: string
}

export interface SynonymRule {
  id: string
  keyword: string
  synonyms: string[]
  notes: string | null
  created_at: string
  updated_at: string
}

export interface KeywordRunResult {
  total: number
  pass_count: number
  warning_count: number
  fail_count: number
  needs_review_count: number
  duration_ms: number
  run_date: string
}

export interface SemanticRunResult {
  total: number
  pass_count: number
  warning_count: number
  fail_count: number
  needs_review_count: number
  duration_ms: number
  run_date: string
  method: string
}

export interface CorrelationResultRead {
  id: string
  control_group_id: string
  control_group_code: string
  control_group_name: string
  document_id: string
  product_type: 'framework' | 'operational'
  correlation_method: string
  correlation_strength: number
  qa_status: 'pass' | 'warning' | 'fail' | 'needs_review'
  coverage_keywords: string[]
  missing_keywords: string[]
  run_date: string
  metadata: Record<string, unknown>
}

export interface QASummaryBucket {
  total: number
  pass_count: number
  warning_count: number
  fail_count: number
  needs_review_count: number
  pass_rate: number
}

export interface QASummary {
  last_run: string | null
  framework: QASummaryBucket
  operational: QASummaryBucket
  privacy: QASummaryBucket
  cloud: QASummaryBucket
  overall_pass_rate: number
}

// ---------------------------------------------------------------------------
// System Info
// ---------------------------------------------------------------------------

export interface ServiceHealth {
  name: string
  status: 'ok' | 'error' | 'unavailable'
  latency_ms: number | null
  detail: string | null
}

export interface DbCounts {
  frameworks: number
  framework_controls: number
  cross_framework_mappings: number
  control_groups: number
  policies: number
  requirements: number
  implementations: number
  assessments: number
  evidence: number
  gaps: number
  users: number
  load_history_count: number
}

export interface SysInfoResponse {
  generated_at: string
  services: ServiceHealth[]
  db_counts: DbCounts
  opensearch_cluster_status: string | null
  opensearch_indices: Record<string, number | null> | null
  platform: string
  standard: string
  api_version: string
  framework_path: string
  operational_path: string
  privacy_path: string
  cloud_path: string
  external_path: string
  datasets_path: string
  opensearch_url: string
  log_level: string
  debug: boolean
  last_sync_at: string | null
  last_sync_type: string | null
  last_sync_status: string | null
  smtp_enabled: boolean
  smtp_host: string
  smtp_port: number
  smtp_from: string
  platform_url: string
  ai_model: string
}
