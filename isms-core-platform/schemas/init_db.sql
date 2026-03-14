-- ============================================================================
-- ISMS CORE Platform — Database Schema
-- PostgreSQL 15+
-- ============================================================================
--
-- Evolved schema matching DATA-MODEL.md (15 entity types).
-- Replaces both 20_init_db.sql (core ISMS) and 21_init_frameworks_db.sql
-- (per-framework tables) with a unified model.
--
-- Key change: Instead of per-framework tables (iso27001_controls,
-- nist_csf_functions, nist_800_53_controls, mitre_attack_techniques, etc.),
-- we use a unified frameworks + framework_controls pattern with JSONB
-- metadata for framework-specific attributes. This matches our bundle format
-- and makes the schema extensible to any future framework.
--
-- Schema sections:
--   1. Extensions
--   2. Enum types
--   3. Core tables (users, sessions)
--   4. Reference framework tables (frameworks, framework_controls,
--      cross_framework_mappings)
--   5. Control group tables (control_groups)
--   6. ISMS content tables (policies, requirements, implementations)
--   7. Assessment tables (assessments, assessment_sheets, assessment_items)
--   8. Compliance tables (evidence, gaps)
--   9. QA tables (correlation_results)
--  10. Audit & system tables
--  11. Indexes
--  12. Materialized views
--  13. Functions & triggers
--  14. Seed data
--
-- Generated: 2026-02-08
-- Updated:   2026-03-08 — Synced with Alembic migrations 001–005
-- Generator: Claude Code (Opus 4.6) — Task 0.21
-- ============================================================================

-- ============================================================================
-- 1. EXTENSIONS
-- ============================================================================

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";
CREATE EXTENSION IF NOT EXISTS "btree_gin";

-- ============================================================================
-- 2. ENUM TYPES
-- ============================================================================

CREATE TYPE user_role AS ENUM (
    'admin',
    'isms_manager',
    'auditor',
    'control_owner',
    'viewer'
);

CREATE TYPE product_type AS ENUM (
    'framework',
    'operational',
    'external'
);

CREATE TYPE policy_type AS ENUM (
    'POL',
    'OP-POL',
    'INS',
    'REF',
    'CTX',
    'FORM'
);  -- INS added via migration 001; already present here for clean installs

CREATE TYPE impl_type AS ENUM (
    'UG',
    'TG'
);

CREATE TYPE compliance_status AS ENUM (
    'compliant',
    'partial',
    'non_compliant',
    'not_assessed',
    'na'
);

CREATE TYPE gap_severity AS ENUM (
    'critical',
    'high',
    'medium',
    'low'
);

CREATE TYPE gap_status AS ENUM (
    'open',
    'in_progress',
    'closed',
    'accepted'
);

CREATE TYPE assessment_type AS ENUM (
    'detailed',
    'checklist'
);

CREATE TYPE sheet_type AS ENUM (
    'executive_summary',
    'dashboard',
    'assessment',
    'reference',
    'config'
);

CREATE TYPE evidence_type AS ENUM (
    'document',
    'screenshot',
    'log_extract',
    'config_export',
    'test_result',
    'attestation'
);

CREATE TYPE mapping_type AS ENUM (
    'maps-to',
    'partially-maps-to',
    'related-to',
    'mitigates',
    'detects',
    'supports',
    'depends-on',
    'enables',
    'feeds-into',
    'implements'
);

CREATE TYPE correlation_method AS ENUM (
    'existence',
    'keyword',
    'semantic',
    'manual'
);

CREATE TYPE qa_status AS ENUM (
    'pass',
    'warning',
    'fail',
    'needs_review'
);

CREATE TYPE control_group_status AS ENUM (
    'complete',
    'partial',
    'basic',
    'incomplete'
);

CREATE TYPE governance_mode AS ENUM (
    'platform',   -- DB is master: WebUI edits → DB → MD on publish
    'local'       -- Files are master: edit locally → import → DB syncs
);

CREATE TYPE content_state AS ENUM (
    'draft',      -- Work in progress — not visible to read-only users
    'review',     -- Submitted for peer/manager review
    'approved',   -- Approved — ready to publish
    'published'   -- Live — visible to all authenticated users
);

CREATE TYPE edit_source AS ENUM (
    'import',     -- Change came from file import pipeline
    'webui',      -- Change made via platform WebUI
    'api'         -- Change made via direct API call
);

-- ============================================================================
-- 3. FUNCTIONS (must precede triggers)
-- ============================================================================

CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- ============================================================================
-- 4. CORE TABLES — Organisation, Users & Sessions
-- ============================================================================

-- Single-tenant organisation record. One row expected per deployment.
-- governance_mode controls policy content authority:
--   platform = WebUI is master (DB → MD on publish)
--   local    = files are master (import → DB sync)
CREATE TABLE organisations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    slug VARCHAR(100) UNIQUE NOT NULL,
    governance_mode governance_mode NOT NULL DEFAULT 'platform',
    description TEXT,
    settings JSONB NOT NULL DEFAULT '{}',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TRIGGER trg_organisations_updated_at
    BEFORE UPDATE ON organisations
    FOR EACH ROW EXECUTE FUNCTION update_updated_at();

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(200),
    role user_role NOT NULL DEFAULT 'viewer',
    is_active BOOLEAN NOT NULL DEFAULT true,
    assigned_groups UUID[] DEFAULT '{}',
    last_login TIMESTAMPTZ,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE sessions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    token VARCHAR(500) UNIQUE NOT NULL,
    expires_at TIMESTAMPTZ NOT NULL,
    ip_address INET,
    user_agent TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ============================================================================
-- 4. REFERENCE FRAMEWORK TABLES
-- ============================================================================

-- A reference standard or framework loaded into the platform.
-- Replaces: iso27001_controls header, nist_csf_functions, nist_800_53_families,
-- mitre_attack_tactics (top-level), swiss_ndsg, eu_gdpr, etc.
CREATE TABLE frameworks (
    id UUID PRIMARY KEY,  -- Deterministic UUID5 from bundle
    code VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(200) NOT NULL,
    version VARCHAR(20),
    publisher VARCHAR(100),
    source_url TEXT,
    description TEXT,
    jurisdiction VARCHAR(10),  -- CH, EU, US (nullable for non-regulatory)
    controls_count INTEGER NOT NULL DEFAULT 0,
    loaded_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    bundle_hash VARCHAR(64),
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- An individual control, category, function, or technique from any framework.
-- Replaces: iso27001_controls, nist_csf_categories, nist_csf_subcategories,
-- nist_800_53_controls, mitre_attack_techniques, mitre_attack_mitigations,
-- swiss_ndsg_requirements, eu_gdpr_requirements, etc.
-- Framework-specific attributes go in metadata (JSONB).
CREATE TABLE framework_controls (
    id UUID PRIMARY KEY,  -- Deterministic UUID5 from bundle
    framework_id UUID NOT NULL REFERENCES frameworks(id) ON DELETE CASCADE,
    control_id VARCHAR(50) NOT NULL,
    parent_id UUID REFERENCES framework_controls(id) ON DELETE SET NULL,
    title VARCHAR(500) NOT NULL,
    description TEXT,
    control_type VARCHAR(50)[] DEFAULT '{}',
    security_properties VARCHAR(50)[] DEFAULT '{}',
    level INTEGER NOT NULL DEFAULT 1,
    sort_order INTEGER NOT NULL DEFAULT 0,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),

    UNIQUE (framework_id, control_id)
);

-- Cross-framework mapping relationships.
-- Replaces: framework_mappings (the wide table with per-framework FK columns).
-- Now a normalised many-to-many: any framework_control → any framework_control.
CREATE TABLE cross_framework_mappings (
    id UUID PRIMARY KEY,  -- Deterministic UUID5 from bundle
    source_control_id UUID NOT NULL REFERENCES framework_controls(id) ON DELETE CASCADE,
    target_control_id UUID NOT NULL REFERENCES framework_controls(id) ON DELETE CASCADE,
    mapping_type mapping_type NOT NULL DEFAULT 'maps-to',
    confidence DECIMAL(3,2) NOT NULL DEFAULT 0.85
        CHECK (confidence >= 0.00 AND confidence <= 1.00),
    source_reference VARCHAR(200),
    notes TEXT,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),

    -- Prevent duplicate mappings (same source, target, type)
    UNIQUE (source_control_id, target_control_id, mapping_type)
);

-- ============================================================================
-- 5. CONTROL GROUP TABLES
-- ============================================================================

-- One of the 53 ISMS CORE control groups (our stacking model).
-- Maps ISO 27001 controls to our product structure.
CREATE TABLE control_groups (
    id UUID PRIMARY KEY,  -- Deterministic UUID5 from bundle
    group_code VARCHAR(30) UNIQUE NOT NULL,
    name VARCHAR(200) NOT NULL,
    section VARCHAR(10) NOT NULL,
    section_name VARCHAR(50) NOT NULL,
    folder_name VARCHAR(100) NOT NULL,
    is_stacked BOOLEAN NOT NULL DEFAULT false,
    stacked_control_ids VARCHAR(10)[] DEFAULT '{}',
    has_framework BOOLEAN NOT NULL DEFAULT true,
    has_operational BOOLEAN NOT NULL DEFAULT true,
    framework_status control_group_status NOT NULL DEFAULT 'incomplete',
    operational_status control_group_status NOT NULL DEFAULT 'incomplete',
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Junction: which ISO 27001 framework_controls belong to which control_group
CREATE TABLE control_group_controls (
    control_group_id UUID NOT NULL REFERENCES control_groups(id) ON DELETE CASCADE,
    framework_control_id UUID NOT NULL REFERENCES framework_controls(id) ON DELETE CASCADE,
    PRIMARY KEY (control_group_id, framework_control_id)
);

-- ============================================================================
-- 6. ISMS CONTENT TABLES
-- ============================================================================

-- A governance or operational policy document.
CREATE TABLE policies (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    control_group_id UUID NOT NULL REFERENCES control_groups(id) ON DELETE CASCADE,
    product_type product_type NOT NULL,
    policy_type policy_type NOT NULL,
    document_id VARCHAR(120) NOT NULL,
    title VARCHAR(300) NOT NULL,
    file_path TEXT NOT NULL,
    content_hash VARCHAR(64),
    word_count INTEGER,
    requirements_count INTEGER DEFAULT 0,
    last_parsed TIMESTAMPTZ,
    -- Phase 6: language code ('en', 'de', 'fr', 'it') and optional origin label for external docs
    language VARCHAR(5) NOT NULL DEFAULT 'en',
    source_label VARCHAR(200),
    -- Phase 7.17: approval workflow state (default 'published' for import pipeline)
    content_state content_state NOT NULL DEFAULT 'published',
    -- Phase 7.18: audit trail
    edit_source edit_source NOT NULL DEFAULT 'import',
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),

    UNIQUE (document_id)
);

-- A "shall" statement extracted from a policy — the atomic unit of compliance.
CREATE TABLE requirements (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    policy_id UUID NOT NULL REFERENCES policies(id) ON DELETE CASCADE,
    control_group_id UUID NOT NULL REFERENCES control_groups(id) ON DELETE CASCADE,
    requirement_text TEXT NOT NULL,
    section_heading VARCHAR(200),
    requirement_type VARCHAR(15) NOT NULL DEFAULT 'mandatory'
        CHECK (requirement_type IN ('mandatory', 'recommended')),
    domain_area VARCHAR(100),
    sort_order INTEGER NOT NULL DEFAULT 0,
    compliance_status compliance_status NOT NULL DEFAULT 'not_assessed',
    evidence_count INTEGER NOT NULL DEFAULT 0,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- An implementation guide document (Framework product only).
CREATE TABLE implementations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    control_group_id UUID NOT NULL REFERENCES control_groups(id) ON DELETE CASCADE,
    impl_type impl_type NOT NULL,
    document_id VARCHAR(120) NOT NULL,
    title VARCHAR(300) NOT NULL,
    file_path TEXT NOT NULL,
    content_hash VARCHAR(64),
    word_count INTEGER,
    last_parsed TIMESTAMPTZ,
    -- Phase 6: language code for FR/IT translation files
    language VARCHAR(5) NOT NULL DEFAULT 'en',
    -- Phase 7.17: approval workflow state
    content_state content_state NOT NULL DEFAULT 'published',
    -- Phase 7.18: audit trail
    edit_source edit_source NOT NULL DEFAULT 'import',
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),

    UNIQUE (document_id)
);

-- ============================================================================
-- 6b. GENERATOR DEFINITION TABLE (Phase 7)
-- ============================================================================

-- Structural metadata extracted from each QA'd Python generator script.
-- One row per generator file (one per assessment domain / workbook).
-- Populated by the generator import pipeline (Phase 7.2) from 188 Framework
-- + 53 Operational generator scripts.  Used by the WebUI form renderer (7.7)
-- and the script regeneration engine (7.11).
CREATE TABLE generator_definitions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    -- Unique key — e.g. ISMS-IMP-A.8.17.1, ISMS-IMP-A.5.1-2-6.1-2.S1
    document_id VARCHAR(80) UNIQUE NOT NULL,
    workbook_name VARCHAR(200) NOT NULL,
    -- CONTROL_ID constant from the generator (e.g. "A.8.17", "A.5.1-2-6.1-2")
    control_id VARCHAR(80) NOT NULL,
    control_name VARCHAR(300) NOT NULL,
    -- Parsed group code — matches control_groups.group_code where resolvable
    group_code VARCHAR(80) NOT NULL,
    -- FK resolved at import time; nullable if group_code not found in DB
    control_group_id UUID REFERENCES control_groups(id) ON DELETE SET NULL,
    domain_number INTEGER,
    domain_total INTEGER,
    is_stacked BOOLEAN NOT NULL DEFAULT false,
    -- ["A.5.1", "A.5.2", ...] for stacked generators; null for simple ones
    stacked_control_ids JSONB,
    -- [{"name": "Time Sources", "type": "input"}, ...]
    sheets JSONB NOT NULL DEFAULT '[]',
    sheet_count INTEGER NOT NULL DEFAULT 0,
    -- "docstring" or "code" — how sheet names were extracted
    sheet_source VARCHAR(20),
    -- Relative path from 50-isms-core-framework/ root
    source_file TEXT,
    parsed_at TIMESTAMPTZ,
    -- When true, the importer will not overwrite this record on re-import
    user_override BOOLEAN NOT NULL DEFAULT false,
    -- Full workbook schema extracted from produced .xlsx (Phase 7.5)
    -- [{sheet_name, sheet_type, position, header_row, data_start_row, freeze_panes,
    --   hide_gridlines, status_column_index, status_column_letter,
    --   columns: [{index, letter, header, header_raw, width, dv_values, required, is_status_col}]}]
    sheet_schemas JSONB NOT NULL DEFAULT '[]',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ============================================================================
-- 7. ASSESSMENT TABLES
-- ============================================================================

-- An Excel workbook containing compliance assessment data.
CREATE TABLE assessments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    control_group_id UUID NOT NULL REFERENCES control_groups(id) ON DELETE CASCADE,
    product_type product_type NOT NULL,
    assessment_type assessment_type NOT NULL,
    document_id VARCHAR(120) NOT NULL,
    workbook_name VARCHAR(200) NOT NULL,
    file_path TEXT NOT NULL,
    file_hash VARCHAR(64),
    file_size BIGINT,
    sheets_count INTEGER DEFAULT 0,
    -- Compliance scoring
    overall_score DECIMAL(5,2)
        CHECK (overall_score IS NULL OR (overall_score >= 0.00 AND overall_score <= 100.00)),
    items_total INTEGER DEFAULT 0,
    items_compliant INTEGER DEFAULT 0,
    items_partial INTEGER DEFAULT 0,
    items_non_compliant INTEGER DEFAULT 0,
    items_na INTEGER DEFAULT 0,
    gaps_count INTEGER DEFAULT 0,
    -- Timestamps
    last_generated TIMESTAMPTZ,
    last_parsed TIMESTAMPTZ,
    summary JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),

    UNIQUE (document_id)
);

-- An individual sheet within a workbook.
CREATE TABLE assessment_sheets (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    assessment_id UUID NOT NULL REFERENCES assessments(id) ON DELETE CASCADE,
    sheet_name VARCHAR(50) NOT NULL,
    sheet_type sheet_type NOT NULL DEFAULT 'assessment',
    row_count INTEGER DEFAULT 0,
    column_count INTEGER DEFAULT 0,
    compliance_score DECIMAL(5,2)
        CHECK (compliance_score IS NULL OR (compliance_score >= 0.00 AND compliance_score <= 100.00)),
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- An individual row/finding within an assessment sheet.
CREATE TABLE assessment_items (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    sheet_id UUID NOT NULL REFERENCES assessment_sheets(id) ON DELETE CASCADE,
    assessment_id UUID NOT NULL REFERENCES assessments(id) ON DELETE CASCADE,
    control_group_id UUID NOT NULL REFERENCES control_groups(id) ON DELETE CASCADE,
    row_number INTEGER NOT NULL,
    item_text TEXT,
    status compliance_status NOT NULL DEFAULT 'not_assessed',
    evidence_reference TEXT,
    owner VARCHAR(100),
    due_date DATE,
    notes TEXT,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ============================================================================
-- 8. COMPLIANCE TABLES
-- ============================================================================

-- An artifact proving a requirement is met.
CREATE TABLE evidence (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    control_group_id UUID NOT NULL REFERENCES control_groups(id) ON DELETE CASCADE,
    requirement_id UUID REFERENCES requirements(id) ON DELETE SET NULL,
    assessment_item_id UUID REFERENCES assessment_items(id) ON DELETE SET NULL,
    evidence_type evidence_type NOT NULL,
    title VARCHAR(300) NOT NULL,
    file_path TEXT,
    collected_date DATE,
    expires_date DATE,
    verified_by VARCHAR(100),
    verified_date DATE,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- A compliance gap or non-conformity.
CREATE TABLE gaps (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    control_group_id UUID NOT NULL REFERENCES control_groups(id) ON DELETE CASCADE,
    requirement_id UUID REFERENCES requirements(id) ON DELETE SET NULL,
    assessment_item_id UUID REFERENCES assessment_items(id) ON DELETE SET NULL,
    product_type VARCHAR(15) NOT NULL DEFAULT 'both'
        CHECK (product_type IN ('framework', 'operational', 'both')),
    gap_description TEXT NOT NULL,
    severity gap_severity NOT NULL DEFAULT 'medium',
    status gap_status NOT NULL DEFAULT 'open',
    owner VARCHAR(100),
    due_date DATE,
    remediation_plan TEXT,
    closed_date DATE,
    closed_by VARCHAR(100),
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ============================================================================
-- 9. QA TABLES
-- ============================================================================

-- QA correlation between claimed scores and verified content.
CREATE TABLE correlation_results (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    control_group_id UUID NOT NULL REFERENCES control_groups(id) ON DELETE CASCADE,
    framework_control_id UUID REFERENCES framework_controls(id) ON DELETE SET NULL,
    document_id VARCHAR(120) NOT NULL,
    correlation_method correlation_method NOT NULL,
    correlation_strength DECIMAL(3,2) NOT NULL DEFAULT 0.00
        CHECK (correlation_strength >= 0.00 AND correlation_strength <= 1.00),
    claimed_score DECIMAL(5,2),
    verified_score DECIMAL(5,2),
    qa_status qa_status NOT NULL DEFAULT 'needs_review',
    coverage_keywords TEXT[] DEFAULT '{}',
    missing_keywords TEXT[] DEFAULT '{}',
    run_date TIMESTAMPTZ NOT NULL DEFAULT now(),
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ============================================================================
-- 10. AUDIT & SYSTEM TABLES
-- ============================================================================

-- All platform actions for compliance audit trail.
CREATE TABLE audit_log (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    action VARCHAR(30) NOT NULL,
    resource_type VARCHAR(30),
    resource_id UUID,
    ip_address INET,
    user_agent TEXT,
    details JSONB DEFAULT '{}',
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Tracks dataset bundle imports and framework data loads.
CREATE TABLE data_load_history (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    bundle_type VARCHAR(50) NOT NULL,
    bundle_file VARCHAR(100),
    framework_code VARCHAR(50),
    version VARCHAR(50),
    objects_loaded INTEGER DEFAULT 0,
    relationships_loaded INTEGER DEFAULT 0,
    bundle_hash VARCHAR(64),
    load_status VARCHAR(20) NOT NULL DEFAULT 'pending'
        CHECK (load_status IN ('pending', 'running', 'success', 'failed')),
    load_started TIMESTAMPTZ DEFAULT now(),
    load_completed TIMESTAMPTZ,
    error_message TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ============================================================================
-- 11. INDEXES
-- ============================================================================

-- Users
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_role ON users(role);

-- Sessions
CREATE INDEX idx_sessions_user_id ON sessions(user_id);
CREATE INDEX idx_sessions_token ON sessions(token);
CREATE INDEX idx_sessions_expires ON sessions(expires_at);

-- Frameworks
CREATE INDEX idx_frameworks_code ON frameworks(code);

-- Framework controls
CREATE INDEX idx_fc_framework_id ON framework_controls(framework_id);
CREATE INDEX idx_fc_control_id ON framework_controls(control_id);
CREATE INDEX idx_fc_parent_id ON framework_controls(parent_id);
CREATE INDEX idx_fc_level ON framework_controls(level);
CREATE INDEX idx_fc_sort_order ON framework_controls(sort_order);
CREATE INDEX idx_fc_title_trgm ON framework_controls USING gin(title gin_trgm_ops);
CREATE INDEX idx_fc_metadata ON framework_controls USING gin(metadata);

-- Cross-framework mappings
CREATE INDEX idx_cfm_source ON cross_framework_mappings(source_control_id);
CREATE INDEX idx_cfm_target ON cross_framework_mappings(target_control_id);
CREATE INDEX idx_cfm_type ON cross_framework_mappings(mapping_type);
CREATE INDEX idx_cfm_confidence ON cross_framework_mappings(confidence);

-- Control groups
CREATE INDEX idx_cg_group_code ON control_groups(group_code);
CREATE INDEX idx_cg_section ON control_groups(section);
CREATE INDEX idx_cg_framework_status ON control_groups(framework_status);
CREATE INDEX idx_cg_operational_status ON control_groups(operational_status);

-- Control group ↔ controls junction
CREATE INDEX idx_cgc_control ON control_group_controls(framework_control_id);

-- Policies
CREATE INDEX idx_policies_control_group ON policies(control_group_id);
CREATE INDEX idx_policies_product_type ON policies(product_type);
CREATE INDEX idx_policies_document_id ON policies(document_id);
CREATE INDEX idx_policies_title_search ON policies USING gin(to_tsvector('english', title));

-- Requirements
CREATE INDEX idx_req_policy ON requirements(policy_id);
CREATE INDEX idx_req_control_group ON requirements(control_group_id);
CREATE INDEX idx_req_status ON requirements(compliance_status);
CREATE INDEX idx_req_text_search ON requirements USING gin(to_tsvector('english', requirement_text));

-- Implementations
CREATE INDEX idx_impl_control_group ON implementations(control_group_id);
CREATE INDEX idx_impl_type ON implementations(impl_type);
CREATE INDEX idx_impl_document_id ON implementations(document_id);

-- Assessments
CREATE INDEX idx_assess_control_group ON assessments(control_group_id);
CREATE INDEX idx_assess_product_type ON assessments(product_type);
CREATE INDEX idx_assess_document_id ON assessments(document_id);
CREATE INDEX idx_assess_score ON assessments(overall_score);

-- Assessment sheets
CREATE INDEX idx_asheet_assessment ON assessment_sheets(assessment_id);
CREATE INDEX idx_asheet_type ON assessment_sheets(sheet_type);

-- Assessment items
CREATE INDEX idx_aitem_sheet ON assessment_items(sheet_id);
CREATE INDEX idx_aitem_assessment ON assessment_items(assessment_id);
CREATE INDEX idx_aitem_control_group ON assessment_items(control_group_id);
CREATE INDEX idx_aitem_status ON assessment_items(status);

-- Evidence
CREATE INDEX idx_evidence_control_group ON evidence(control_group_id);
CREATE INDEX idx_evidence_requirement ON evidence(requirement_id);
CREATE INDEX idx_evidence_type ON evidence(evidence_type);
CREATE INDEX idx_evidence_expires ON evidence(expires_date);

-- Gaps
CREATE INDEX idx_gaps_control_group ON gaps(control_group_id);
CREATE INDEX idx_gaps_severity ON gaps(severity);
CREATE INDEX idx_gaps_status ON gaps(status);
CREATE INDEX idx_gaps_due_date ON gaps(due_date);

-- Correlation results
CREATE INDEX idx_corr_control_group ON correlation_results(control_group_id);
CREATE INDEX idx_corr_qa_status ON correlation_results(qa_status);
CREATE INDEX idx_corr_run_date ON correlation_results(run_date);

-- Audit log
CREATE INDEX idx_audit_user ON audit_log(user_id);
CREATE INDEX idx_audit_action ON audit_log(action);
CREATE INDEX idx_audit_resource ON audit_log(resource_type, resource_id);
CREATE INDEX idx_audit_created ON audit_log(created_at);

-- Data load history
CREATE INDEX idx_dlh_framework ON data_load_history(framework_code);
CREATE INDEX idx_dlh_status ON data_load_history(load_status);

-- Generator definitions
CREATE INDEX ix_generator_definitions_group_code ON generator_definitions(group_code);
CREATE INDEX ix_generator_definitions_control_group_id ON generator_definitions(control_group_id);

-- ============================================================================
-- 12. MATERIALIZED VIEWS
-- ============================================================================

-- Per-control-group compliance summary (dashboard main view).
CREATE MATERIALIZED VIEW v_control_group_summary AS
SELECT
    cg.id,
    cg.group_code,
    cg.name,
    cg.section,
    cg.section_name,
    cg.framework_status,
    cg.operational_status,
    -- Framework product
    COUNT(DISTINCT p_fw.id) AS framework_policies,
    COUNT(DISTINCT imp.id) AS framework_implementations,
    COUNT(DISTINCT a_fw.id) AS framework_assessments,
    AVG(a_fw.overall_score) AS framework_avg_score,
    -- Operational product
    COUNT(DISTINCT p_op.id) AS operational_policies,
    COUNT(DISTINCT a_op.id) AS operational_assessments,
    AVG(a_op.overall_score) AS operational_avg_score,
    -- Combined
    COUNT(DISTINCT g.id) FILTER (WHERE g.status = 'open') AS open_gaps,
    COUNT(DISTINCT e.id) AS evidence_count,
    COUNT(DISTINCT r.id) AS requirements_count,
    COUNT(DISTINCT r.id) FILTER (WHERE r.compliance_status = 'compliant') AS requirements_met
FROM control_groups cg
LEFT JOIN policies p_fw ON p_fw.control_group_id = cg.id AND p_fw.product_type = 'framework'
LEFT JOIN policies p_op ON p_op.control_group_id = cg.id AND p_op.product_type = 'operational'
LEFT JOIN implementations imp ON imp.control_group_id = cg.id
LEFT JOIN assessments a_fw ON a_fw.control_group_id = cg.id AND a_fw.product_type = 'framework'
LEFT JOIN assessments a_op ON a_op.control_group_id = cg.id AND a_op.product_type = 'operational'
LEFT JOIN gaps g ON g.control_group_id = cg.id
LEFT JOIN evidence e ON e.control_group_id = cg.id
LEFT JOIN requirements r ON r.control_group_id = cg.id
GROUP BY cg.id, cg.group_code, cg.name, cg.section, cg.section_name,
         cg.framework_status, cg.operational_status;

-- Unique index for concurrent refresh
CREATE UNIQUE INDEX idx_vcgs_id ON v_control_group_summary(id);

-- Compliance dashboard by product and section.
CREATE MATERIALIZED VIEW v_dashboard_compliance AS
SELECT
    'framework'::text AS product,
    cg.section,
    cg.section_name,
    COUNT(*) AS total_groups,
    COUNT(*) FILTER (WHERE cg.framework_status = 'complete') AS complete,
    COUNT(*) FILTER (WHERE cg.framework_status = 'partial') AS partial,
    COUNT(*) FILTER (WHERE cg.framework_status = 'basic') AS basic,
    COUNT(*) FILTER (WHERE cg.framework_status = 'incomplete') AS incomplete,
    ROUND(AVG(a.overall_score), 1) AS avg_compliance_score
FROM control_groups cg
LEFT JOIN assessments a ON a.control_group_id = cg.id AND a.product_type = 'framework'
WHERE cg.has_framework = true
GROUP BY cg.section, cg.section_name

UNION ALL

SELECT
    'operational'::text AS product,
    cg.section,
    cg.section_name,
    COUNT(*) AS total_groups,
    COUNT(*) FILTER (WHERE cg.operational_status = 'complete') AS complete,
    COUNT(*) FILTER (WHERE cg.operational_status = 'partial') AS partial,
    COUNT(*) FILTER (WHERE cg.operational_status = 'basic') AS basic,
    COUNT(*) FILTER (WHERE cg.operational_status = 'incomplete') AS incomplete,
    ROUND(AVG(a.overall_score), 1) AS avg_compliance_score
FROM control_groups cg
LEFT JOIN assessments a ON a.control_group_id = cg.id AND a.product_type = 'operational'
WHERE cg.has_operational = true
GROUP BY cg.section, cg.section_name;

-- Framework coverage matrix (how well each loaded framework maps to ISO controls).
CREATE MATERIALIZED VIEW v_framework_coverage AS
SELECT
    f.id AS framework_id,
    f.code AS framework_code,
    f.name AS framework_name,
    COUNT(DISTINCT fc.id) AS total_controls,
    COUNT(DISTINCT cfm.id) AS mapped_controls,
    COUNT(DISTINCT cfm.id) FILTER (WHERE cfm.confidence >= 0.80) AS high_confidence,
    COUNT(DISTINCT cfm.id) FILTER (WHERE cfm.confidence < 0.80 AND cfm.confidence >= 0.50) AS medium_confidence,
    COUNT(DISTINCT cfm.id) FILTER (WHERE cfm.confidence < 0.50) AS low_confidence,
    ROUND(
        COUNT(DISTINCT cfm.id)::NUMERIC / NULLIF(COUNT(DISTINCT fc.id), 0) * 100, 1
    ) AS coverage_pct
FROM frameworks f
JOIN framework_controls fc ON fc.framework_id = f.id
LEFT JOIN cross_framework_mappings cfm ON cfm.target_control_id = fc.id
GROUP BY f.id, f.code, f.name;

-- Unique index for concurrent refresh
CREATE UNIQUE INDEX idx_vfc_framework_id ON v_framework_coverage(framework_id);

-- ============================================================================
-- 13. TRIGGERS
-- ============================================================================

-- Apply update_updated_at() trigger to all tables with updated_at.
CREATE TRIGGER trg_users_updated_at
    BEFORE UPDATE ON users FOR EACH ROW EXECUTE FUNCTION update_updated_at();
CREATE TRIGGER trg_frameworks_updated_at
    BEFORE UPDATE ON frameworks FOR EACH ROW EXECUTE FUNCTION update_updated_at();
CREATE TRIGGER trg_fc_updated_at
    BEFORE UPDATE ON framework_controls FOR EACH ROW EXECUTE FUNCTION update_updated_at();
CREATE TRIGGER trg_cg_updated_at
    BEFORE UPDATE ON control_groups FOR EACH ROW EXECUTE FUNCTION update_updated_at();
CREATE TRIGGER trg_policies_updated_at
    BEFORE UPDATE ON policies FOR EACH ROW EXECUTE FUNCTION update_updated_at();
CREATE TRIGGER trg_requirements_updated_at
    BEFORE UPDATE ON requirements FOR EACH ROW EXECUTE FUNCTION update_updated_at();
CREATE TRIGGER trg_impl_updated_at
    BEFORE UPDATE ON implementations FOR EACH ROW EXECUTE FUNCTION update_updated_at();
CREATE TRIGGER trg_assessments_updated_at
    BEFORE UPDATE ON assessments FOR EACH ROW EXECUTE FUNCTION update_updated_at();
CREATE TRIGGER trg_aitems_updated_at
    BEFORE UPDATE ON assessment_items FOR EACH ROW EXECUTE FUNCTION update_updated_at();
CREATE TRIGGER trg_evidence_updated_at
    BEFORE UPDATE ON evidence FOR EACH ROW EXECUTE FUNCTION update_updated_at();
CREATE TRIGGER trg_gaps_updated_at
    BEFORE UPDATE ON gaps FOR EACH ROW EXECUTE FUNCTION update_updated_at();
CREATE TRIGGER trg_gendef_updated_at
    BEFORE UPDATE ON generator_definitions FOR EACH ROW EXECUTE FUNCTION update_updated_at();

-- Refresh all materialized views.
CREATE OR REPLACE FUNCTION refresh_materialized_views()
RETURNS void AS $$
BEGIN
    REFRESH MATERIALIZED VIEW CONCURRENTLY v_control_group_summary;
    REFRESH MATERIALIZED VIEW v_dashboard_compliance;
    REFRESH MATERIALIZED VIEW CONCURRENTLY v_framework_coverage;
END;
$$ LANGUAGE plpgsql;

-- Get all cross-framework mappings for an ISO 27001 control.
-- Returns mappings where this control is either source or target.
CREATE OR REPLACE FUNCTION get_control_mappings(p_control_id VARCHAR)
RETURNS TABLE (
    target_framework VARCHAR,
    target_control_id VARCHAR,
    target_title VARCHAR,
    cfm_mapping_type mapping_type,
    cfm_confidence DECIMAL
) AS $$
BEGIN
    RETURN QUERY
    -- Outbound: this control → other frameworks
    SELECT
        f.code::VARCHAR,
        fc_target.control_id::VARCHAR,
        fc_target.title::VARCHAR,
        cfm.mapping_type,
        cfm.confidence
    FROM cross_framework_mappings cfm
    JOIN framework_controls fc_source ON cfm.source_control_id = fc_source.id
    JOIN framework_controls fc_target ON cfm.target_control_id = fc_target.id
    JOIN frameworks f ON fc_target.framework_id = f.id
    WHERE fc_source.control_id = p_control_id

    UNION ALL

    -- Inbound: other frameworks → this control
    SELECT
        f.code::VARCHAR,
        fc_source.control_id::VARCHAR,
        fc_source.title::VARCHAR,
        cfm.mapping_type,
        cfm.confidence
    FROM cross_framework_mappings cfm
    JOIN framework_controls fc_source ON cfm.source_control_id = fc_source.id
    JOIN framework_controls fc_target ON cfm.target_control_id = fc_target.id
    JOIN frameworks f ON fc_source.framework_id = f.id
    WHERE fc_target.control_id = p_control_id;
END;
$$ LANGUAGE plpgsql;

-- ============================================================================
-- 14. SEED DATA
-- ============================================================================

-- Default organisation (single-tenant — one row).
-- UUID5 deterministic: uuid5(DNS, 'isms-core.organisation.default')
-- governance_mode = 'platform' (WebUI master) — change to 'local' for file-master deployments.
INSERT INTO organisations (id, name, slug, governance_mode, description, settings)
VALUES (
    'c1b6cbcf-1e65-55fb-a389-4c863e208e05',
    'ISMS CORE',
    'isms-core',
    'platform',
    'Default ISMS CORE organisation — update name and governance mode as required.',
    '{}'
) ON CONFLICT DO NOTHING;

-- Default admin user (password: admin123 — CHANGE ON FIRST LOGIN).
INSERT INTO users (email, username, hashed_password, full_name, role)
VALUES (
    'admin@isms-core.dev',
    'admin',
    '$2b$12$uVAdzc0JwdXXMJHJePXM..imqoN/PVCAkgE0A0z5qTyK1BstplfQy',
    'Administrator',
    'admin'
) ON CONFLICT (email) DO NOTHING;

-- Foundation control group (group_code '00') — seeded permanently.
-- Not in control_groups.json (53 ISO Annex A groups).  This group holds
-- ISMS CORE foundation documents: ISMS-POL-00/01, ISMS-INS-*, ISMS-REF-* etc.
-- UUID5 deterministic: uuid5(DNS, 'isms-core.control-group.00-foundation')
INSERT INTO control_groups (
    id, group_code, name, section, section_name,
    folder_name, is_stacked, has_framework, has_operational,
    framework_status, operational_status, metadata,
    created_at, updated_at
) VALUES (
    'd811cb3b-959f-5d42-923d-100714c192ec',
    '00',
    'Foundation Policies',
    '00',
    'Foundation Policies',
    '00-foundation-policies',
    false,
    true,
    false,
    'complete',
    'incomplete',
    '{}',
    now(),
    now()
) ON CONFLICT (group_code) DO NOTHING;

-- ============================================================================
-- PERMISSIONS
-- ============================================================================

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO isms_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO isms_user;
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO isms_user;

-- ============================================================================
-- COMPLETION
-- ============================================================================

DO $$
BEGIN
    RAISE NOTICE '============================================================';
    RAISE NOTICE 'ISMS CORE Platform — Database Schema Initialized';
    RAISE NOTICE 'Schema version: 2026-03-08 (migrations 001–005 incorporated)';
    RAISE NOTICE '============================================================';
    RAISE NOTICE '';
    RAISE NOTICE 'Tables (16 entities + 2 system):';
    RAISE NOTICE '  Core:       users, sessions';
    RAISE NOTICE '  Reference:  frameworks, framework_controls, cross_framework_mappings';
    RAISE NOTICE '  Groups:     control_groups, control_group_controls';
    RAISE NOTICE '  Content:    policies, requirements, implementations';
    RAISE NOTICE '  Generator:  generator_definitions  (Phase 7)';
    RAISE NOTICE '  Assessment: assessments, assessment_sheets, assessment_items';
    RAISE NOTICE '  Compliance: evidence, gaps';
    RAISE NOTICE '  QA:         correlation_results';
    RAISE NOTICE '  System:     audit_log, data_load_history';
    RAISE NOTICE '';
    RAISE NOTICE 'Materialized Views (3):';
    RAISE NOTICE '  v_control_group_summary, v_dashboard_compliance, v_framework_coverage';
    RAISE NOTICE '';
    RAISE NOTICE 'Enum Types (14):';
    RAISE NOTICE '  user_role, product_type (framework/operational/external),';
    RAISE NOTICE '  policy_type (POL/OP-POL/INS/REF/CTX/FORM), impl_type,';
    RAISE NOTICE '  compliance_status, gap_severity, gap_status, assessment_type,';
    RAISE NOTICE '  sheet_type, evidence_type, mapping_type, correlation_method,';
    RAISE NOTICE '  qa_status, control_group_status';
    RAISE NOTICE '';
    RAISE NOTICE 'Seed data: admin user + Foundation Policies control group (00)';
    RAISE NOTICE 'Default admin: admin@isms-core.dev / admin123';
    RAISE NOTICE 'CHANGE THE DEFAULT PASSWORD ON FIRST LOGIN!';
    RAISE NOTICE '';
    RAISE NOTICE 'Next: Load Phase 0 bundles with framework_loader task.';
    RAISE NOTICE '============================================================';
END $$;
