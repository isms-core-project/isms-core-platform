#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
AI-CHK-A.7.2-6 — Data for AI Systems Compliance Checklist

Controls A.7.2-6: Data Management, Data Acquisition,
                  Data Quality, Data Provenance, Data Preparation
Product: ISMS CORE AI (ISO/IEC 42001:2023)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Data Management (A.7.2) — 5 reqs
4. Data Acquisition (A.7.3) — 5 reqs
5. Data Quality (A.7.4) — 5 reqs
6. Data Provenance (A.7.5) — 4 reqs
7. Data Preparation (A.7.6) — 4 reqs

Total: 23 requirements across 5 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

_AI_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_AI_ROOT / '00-checklist-engine'))
from ai_checklist_engine import generate_checklist

DOCUMENT_ID   = "AI-CHK-A.7.2-6"
CONTROL_ID    = "A.7.2-6"
CONTROL_NAME  = "Data for AI Systems"
SOURCE_POLICY = "AI-POL-A.7.2-6"

REQUIREMENTS = OrderedDict([
    ("Data Management", [
        ("A.7.2-01", "Data Governance Framework",
         "The organisation shall establish a data governance framework for AI systems covering: data acquisition controls, quality requirements, provenance tracking, preparation documentation, and data retention and deletion. The framework shall be documented and implemented."),
        ("A.7.2-02", "Data Register",
         "The organisation shall maintain a register of all datasets used across in-scope AI systems. The register shall identify each dataset, its source category, whether it contains personal data, its current governance status, and the AI systems that use it."),
        ("A.7.2-03", "Personal Data Controls",
         "Where AI system data resources include personal data, the organisation shall confirm a documented legal basis for each processing activity, apply data minimisation, and maintain linkage between the AI system and the relevant GDPR or equivalent records."),
        ("A.7.2-04", "Prohibited Data Policy",
         "The organisation shall document and communicate a list of data sources that are prohibited from use in AI systems without explicit written approval — including data with unknown provenance, unlicensed third-party data, and personal data without a legal basis."),
        ("A.7.2-05", "Data Lifecycle",
         "The organisation shall define and implement data retention and deletion schedules for AI system datasets. Schedules shall be proportionate to legal requirements and the operational life of the AI system. Deletion events shall be recorded."),
    ]),

    ("Data Acquisition", [
        ("A.7.3-01", "Acquisition Record",
         "For every dataset used in training or fine-tuning an AI system, the organisation shall complete a Data Acquisition Record per the template in AI-IMP-A.7.2-6-TG. No dataset shall enter production use without a completed Acquisition Record."),
        ("A.7.3-02", "Licence and Rights",
         "Before acquiring a dataset, the organisation shall verify and document: the data licence or terms of use, any restrictions on commercial use, any restrictions on use in AI training, and the confirmation that use falls within the licence scope."),
        ("A.7.3-03", "Source Category Documentation",
         "The Data Acquisition Record shall document the data source category: first-party data, licensed third-party data, open dataset, synthetic data, or web-scraped data. For each category, applicable governance controls shall be confirmed."),
        ("A.7.3-04", "Personal Data Legal Basis",
         "Where a dataset contains personal data, the Data Acquisition Record shall document the legal basis for processing and reference the relevant GDPR Article 6 or Article 9 basis. Datasets with personal data and no documented legal basis shall not be used."),
        ("A.7.3-05", "Third-Party AI API Data",
         "Where the organisation sends data to a third-party AI API for inference or fine-tuning, the organisation shall document what data is sent, confirm there is no prohibited data in the inputs, and confirm the contractual data processing terms with the provider."),
    ]),

    ("Data Quality", [
        ("A.7.4-01", "Quality Gate",
         "All training datasets shall pass a documented data quality gate before use in model development. The quality gate shall evaluate accuracy, completeness, consistency, timeliness, and representativeness at a minimum."),
        ("A.7.4-02", "Quality Record",
         "The organisation shall complete a Data Quality Record per the template in AI-IMP-A.7.2-6-TG for each training dataset. The record shall document quality dimensions assessed, threshold values, actual results, and pass/fail determination."),
        ("A.7.4-03", "Representativeness Assessment",
         "The quality assessment shall include a representativeness assessment: whether the dataset adequately represents the populations the AI system will be applied to, and whether underrepresented groups are identified and documented."),
        ("A.7.4-04", "Quality Gate Failure Handling",
         "Where a dataset fails the quality gate, the organisation shall document the failure and either: remediate the quality issues and re-run assessment; acquire an alternative dataset; or escalate to the AI Governance Officer with justification if deployment is still being considered."),
        ("A.7.4-05", "Operational Data Quality",
         "The organisation shall implement monitoring of operational data quality for deployed AI systems — detecting degradation in data completeness, consistency, or representativeness that could affect system performance. Quality alerts shall feed into the AI system monitoring plan."),
    ]),

    ("Data Provenance", [
        ("A.7.5-01", "Provenance Tracking",
         "The organisation shall maintain data provenance records that trace each dataset used in an AI system from acquisition through all transformation steps to the model training run. Provenance shall be sufficient to support audit, incident investigation, and data deletion requests."),
        ("A.7.5-02", "Transformation History",
         "Every material transformation applied to a dataset — including cleaning, normalisation, augmentation, and filtering — shall be recorded with: the transformation applied, the tool/script used, the operator, and the date. Transformations shall be reproducible."),
        ("A.7.5-03", "Deletion Request Support",
         "Data provenance records shall be sufficient to identify and action deletion requests — including GDPR right to erasure requests. Where an erasure request cannot be actioned without retraining or withdrawing a model, the AI System Owner shall escalate to the AI Governance Officer."),
        ("A.7.5-04", "Provenance Record Retention",
         "Data provenance records shall be retained for the operational life of the AI system plus a minimum of 5 years after decommissioning. Provenance records shall be available to auditors and regulatory authorities on request."),
    ]),

    ("Data Preparation", [
        ("A.7.6-01", "Preparation Documentation",
         "All data preparation activities — including feature engineering, train/test/validation splitting, data augmentation, and class balancing — shall be documented in a Data Preparation Documentation record per the template in AI-IMP-A.7.2-6-TG."),
        ("A.7.6-02", "Bias-Aware Preparation",
         "Data preparation steps shall be assessed for their potential to introduce or amplify bias — including oversampling, undersampling, feature selection, and proxy variable inclusion. Bias risks identified during preparation shall be flagged in the bias assessment."),
        ("A.7.6-03", "Test Set Integrity",
         "Test and validation datasets shall be kept strictly separate from training data. Data leakage between training and test sets shall be prevented and verified. The separation method shall be documented in the Data Preparation Documentation record."),
        ("A.7.6-04", "Synthetic Data Controls",
         "Where synthetic data is generated for training or testing, the organisation shall document: the generation method, the source data used to train the generator, quality validation performed on synthetic outputs, and any privacy-preserving properties claimed."),
    ]),
])

if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS,
        iso_standard="ISO/IEC 42001:2023"
    ))

# QA_VERIFIED: [YYYY-MM-DD]
