#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
================================================================================
ISMS-IMP-A.8.27.4 - Zero Trust Implementation Assessment Generator
================================================================================

ISO/IEC 27001:2022 Control A.8.27: Secure System Architecture and Engineering
Assessment Domain 4 of 4: Zero Trust Implementation Assessment

Aligned with NIST SP 800-207 and CISA Zero Trust Maturity Model.

--------------------------------------------------------------------------------
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from datetime import datetime
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-IMP-A.8.27.4"
WORKBOOK_NAME = "Zero Trust Implementation Assessment"
CONTROL_ID = "A.8.27"
CONTROL_NAME = "Secure System Architecture and Engineering Principles"
CONTROL_REF = f"ISO/IEC 27001:2022 - Control {CONTROL_ID}: {CONTROL_NAME}"

GENERATED_DATE = datetime.now().strftime("%d.%m.%Y")
GENERATED_TIMESTAMP = datetime.now().strftime("%Y%m%d")
OUTPUT_FILENAME = f"{DOCUMENT_ID}_{WORKBOOK_NAME.replace(' ', '_')}_{GENERATED_TIMESTAMP}.xlsx"

CONFIG = {
    'organisation': '[Organisation]',
    'colors': {
        'header_bg': '1F4E79', 'header_text': 'FFFFFF', 'subheader_bg': '2E75B6',
        'input_cell': 'E2EFDA', 'formula_cell': 'FFF2CC',
        'traditional': 'FF6B6B', 'initial': 'FFE66D', 'advanced': '4ECDC4', 'optimal': '2ECC71',
    },
}

def get_styles():
    thin_border = Border(left=Side(style='thin'), right=Side(style='thin'), top=Side(style='thin'), bottom=Side(style='thin'))
    return {
        'header': {'font': Font(bold=True, color=CONFIG['colors']['header_text'], size=12),
                   'fill': PatternFill(start_color=CONFIG['colors']['header_bg'], end_color=CONFIG['colors']['header_bg'], fill_type='solid'),
                   'alignment': Alignment(horizontal='center', vertical='center', wrap_text=True), 'border': thin_border},
        'subheader': {'font': Font(bold=True, color=CONFIG['colors']['header_text'], size=11),
                      'fill': PatternFill(start_color=CONFIG['colors']['subheader_bg'], end_color=CONFIG['colors']['subheader_bg'], fill_type='solid'),
                      'alignment': Alignment(horizontal='left', vertical='center', wrap_text=True), 'border': thin_border},
        'input': {'font': Font(size=11), 'fill': PatternFill(start_color=CONFIG['colors']['input_cell'], end_color=CONFIG['colors']['input_cell'], fill_type='solid'),
                  'alignment': Alignment(horizontal='left', vertical='center', wrap_text=True), 'border': thin_border},
        'formula': {'font': Font(size=11), 'fill': PatternFill(start_color=CONFIG['colors']['formula_cell'], end_color=CONFIG['colors']['formula_cell'], fill_type='solid'),
                    'alignment': Alignment(horizontal='center', vertical='center'), 'border': thin_border},
        'normal': {'font': Font(size=11), 'alignment': Alignment(horizontal='left', vertical='center', wrap_text=True), 'border': thin_border},
    }

def apply_style(cell, style_dict):
    for attr in ['font', 'fill', 'alignment', 'border']:
        if attr in style_dict:
            setattr(cell, attr, style_dict[attr])

def create_instructions_sheet(ws):
    styles = get_styles()
    ws.merge_cells('A1:H1')
    ws['A1'] = f"ISMS-IMP-A.8.27.4 - Zero Trust Implementation Assessment"
    apply_style(ws['A1'], styles['header'])
    ws.row_dimensions[1].height = 30

    ws['A3'] = "Document Information"
    apply_style(ws['A3'], styles['subheader'])
    ws.merge_cells('A3:H3')

    info = [
        ('Document ID', DOCUMENT_ID),
        ('Control Reference', CONTROL_REF),
        ('Purpose', 'Evaluate Zero Trust Architecture maturity across all pillars'),
        ('Framework Reference', 'NIST SP 800-207, CISA Zero Trust Maturity Model'),
        ('Generated Date', GENERATED_DATE),
    ]
    row = 4
    for label, value in info:
        ws[f'A{row}'], ws[f'B{row}'] = label, value
        apply_style(ws[f'A{row}'], styles['normal'])
        apply_style(ws[f'B{row}'], styles['input'])
        ws.merge_cells(f'B{row}:H{row}')
        row += 1

    row += 1
    ws[f'A{row}'] = "CISA Zero Trust Maturity Levels"
    apply_style(ws[f'A{row}'], styles['subheader'])
    ws.merge_cells(f'A{row}:H{row}')
    row += 1

    maturity_levels = [
        ('Traditional', 'Perimeter-based security, implicit trust within network'),
        ('Initial', 'Basic ZT capabilities, some explicit verification'),
        ('Advanced', 'Comprehensive ZT, automated policy enforcement'),
        ('Optimal', 'Full ZT, continuous verification, dynamic policies'),
    ]
    for level, desc in maturity_levels:
        ws[f'A{row}'], ws[f'B{row}'] = level, desc
        apply_style(ws[f'A{row}'], styles['normal'])
        apply_style(ws[f'B{row}'], styles['normal'])
        ws.merge_cells(f'B{row}:H{row}')
        row += 1

    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 80


def create_strategy_sheet(ws):
    styles = get_styles()
    ws.merge_cells('A1:G1')
    ws['A1'] = "Zero Trust - Strategy Assessment"
    apply_style(ws['A1'], styles['header'])
    ws.row_dimensions[1].height = 30

    headers = ['Strat-ID', 'Element', 'Status', 'Evidence', 'Gap', 'Owner', 'Notes']
    widths = [10, 35, 15, 30, 30, 20, 25]

    for col, (header, width) in enumerate(zip(headers, widths), 1):
        cell = ws.cell(row=3, column=col, value=header)
        apply_style(cell, styles['header'])
        ws.column_dimensions[get_column_letter(col)].width = width

    status_dv = DataValidation(type='list', formula1='"Implemented,Partial,Not Started"', allow_blank=True)
    ws.add_data_validation(status_dv)

    strategy_elements = [
        ('STRAT-001', 'Executive sponsorship for Zero Trust'),
        ('STRAT-002', 'Zero Trust strategy documented'),
        ('STRAT-003', 'Multi-year ZT roadmap defined'),
        ('STRAT-004', 'ZT governance established'),
        ('STRAT-005', 'Budget allocated for ZT initiatives'),
        ('STRAT-006', 'Success metrics defined'),
        ('STRAT-007', 'ZT strategy communicated organisation-wide'),
        ('STRAT-008', 'ZT training programme established'),
        ('STRAT-009', 'ZT pilot projects completed'),
        ('STRAT-010', 'ZT architecture documented'),
        ('STRAT-011', 'ZT policy framework defined'),
        ('STRAT-012', 'ZT vendor/tool selection completed'),
    ]

    for row, (strat_id, element) in enumerate(strategy_elements, 4):
        ws.cell(row=row, column=1, value=strat_id)
        ws.cell(row=row, column=2, value=element)
        for col in range(1, 8):
            apply_style(ws.cell(row=row, column=col), styles['input'] if col > 2 else styles['normal'])

    status_dv.add(f'C4:C{3 + len(strategy_elements)}')
    ws.freeze_panes = 'A4'


def create_pillar_sheet(ws, pillar_name, pillar_prefix, capabilities):
    """Generic function to create pillar assessment sheets"""
    styles = get_styles()
    ws.merge_cells('A1:J1')
    ws['A1'] = f"Zero Trust - {pillar_name} Pillar Assessment"
    apply_style(ws['A1'], styles['header'])
    ws.row_dimensions[1].height = 30

    headers = [f'{pillar_prefix}-ID', 'Capability', 'Traditional', 'Initial', 'Advanced', 'Optimal', 'Current', 'Target', 'Evidence', 'Gap']
    widths = [10, 35, 12, 12, 12, 12, 12, 12, 30, 30]

    for col, (header, width) in enumerate(zip(headers, widths), 1):
        cell = ws.cell(row=3, column=col, value=header)
        apply_style(cell, styles['header'])
        ws.column_dimensions[get_column_letter(col)].width = width

    score_dv = DataValidation(type='list', formula1='"0,1,2,3"', allow_blank=True)
    ws.add_data_validation(score_dv)

    target_dv = DataValidation(type='list', formula1='"Traditional,Initial,Advanced,Optimal"', allow_blank=True)
    ws.add_data_validation(target_dv)

    for row, (cap_id, capability) in enumerate(capabilities, 4):
        ws.cell(row=row, column=1, value=cap_id)
        ws.cell(row=row, column=2, value=capability)
        # Current maturity formula
        ws.cell(row=row, column=7, value=f'=IF(F{row}>=2,"Optimal",IF(E{row}>=2,"Advanced",IF(D{row}>=2,"Initial","Traditional")))')
        for col in range(1, 11):
            if col == 7:
                apply_style(ws.cell(row=row, column=col), styles['formula'])
            elif col > 2:
                apply_style(ws.cell(row=row, column=col), styles['input'])
            else:
                apply_style(ws.cell(row=row, column=col), styles['normal'])

    score_dv.add(f'C4:F{3 + len(capabilities)}')
    target_dv.add(f'H4:H{3 + len(capabilities)}')
    ws.freeze_panes = 'A4'


def create_identity_sheet(ws):
    capabilities = [
        ('ID-001', 'Password-based to MFA enforcement'),
        ('ID-002', 'Phishing-resistant MFA deployment'),
        ('ID-003', 'Passwordless authentication'),
        ('ID-004', 'Static RBAC to dynamic ABAC'),
        ('ID-005', 'Risk-based conditional access'),
        ('ID-006', 'Manual to automated identity lifecycle'),
        ('ID-007', 'Just-in-time (JIT) privileged access'),
        ('ID-008', 'Zero standing privilege'),
        ('ID-009', 'Federation and modern protocols'),
        ('ID-010', 'Continuous identity verification'),
    ]
    create_pillar_sheet(ws, 'Identity', 'ID', capabilities)


def create_device_sheet(ws):
    capabilities = [
        ('DEV-001', 'Device inventory completeness'),
        ('DEV-002', 'Real-time device inventory'),
        ('DEV-003', 'Device compliance checking'),
        ('DEV-004', 'Continuous device posture assessment'),
        ('DEV-005', 'Device health-based access decisions'),
        ('DEV-006', 'EDR deployment'),
        ('DEV-007', 'XDR integration'),
        ('DEV-008', 'Autonomous threat response'),
    ]
    create_pillar_sheet(ws, 'Device', 'DEV', capabilities)


def create_network_sheet(ws):
    capabilities = [
        ('NET-001', 'Network segmentation (VLANs)'),
        ('NET-002', 'Micro-segmentation'),
        ('NET-003', 'Application-level segmentation'),
        ('NET-004', 'TLS for external traffic'),
        ('NET-005', 'TLS everywhere (internal)'),
        ('NET-006', 'mTLS service-to-service'),
        ('NET-007', 'ZTNA basic implementation'),
        ('NET-008', 'Software-defined perimeter'),
    ]
    create_pillar_sheet(ws, 'Network', 'NET', capabilities)


def create_workload_sheet(ws):
    capabilities = [
        ('WL-001', 'Service account management'),
        ('WL-002', 'Managed identities for workloads'),
        ('WL-003', 'SPIFFE/SPIRE workload attestation'),
        ('WL-004', 'API authentication (API keys to OAuth)'),
        ('WL-005', 'Workload isolation (VMs to containers)'),
        ('WL-006', 'Serverless isolation'),
        ('WL-007', 'SAST/DAST integration'),
        ('WL-008', 'DevSecOps pipeline security'),
        ('WL-009', 'Runtime application protection'),
        ('WL-010', 'Continuous security validation'),
    ]
    create_pillar_sheet(ws, 'Workload', 'WL', capabilities)


def create_data_sheet(ws):
    capabilities = [
        ('DATA-001', 'Manual data classification'),
        ('DATA-002', 'Policy-based classification'),
        ('DATA-003', 'Automated data labelling'),
        ('DATA-004', 'ML-based classification'),
        ('DATA-005', 'Selective encryption'),
        ('DATA-006', 'Encryption at rest and transit'),
        ('DATA-007', 'Per-field encryption'),
        ('DATA-008', 'Data access controls (ABAC)'),
        ('DATA-009', 'Basic DLP'),
        ('DATA-010', 'AI-powered DLP'),
    ]
    create_pillar_sheet(ws, 'Data', 'DATA', capabilities)


def create_visibility_sheet(ws):
    capabilities = [
        ('VIS-001', 'Perimeter logging'),
        ('VIS-002', 'Centralised logging'),
        ('VIS-003', 'Full telemetry collection'),
        ('VIS-004', 'SIEM deployment'),
        ('VIS-005', 'UEBA integration'),
        ('VIS-006', 'ML-based analytics'),
        ('VIS-007', 'Behaviour-based detection'),
        ('VIS-008', 'Guided investigation'),
    ]
    create_pillar_sheet(ws, 'Visibility', 'VIS', capabilities)


def create_automation_sheet(ws):
    capabilities = [
        ('AUTO-001', 'Manual policy deployment'),
        ('AUTO-002', 'Scripted policy automation'),
        ('AUTO-003', 'Policy as code'),
        ('AUTO-004', 'Intent-based policy'),
        ('AUTO-005', 'Basic response playbooks'),
        ('AUTO-006', 'SOAR integration'),
        ('AUTO-007', 'Auto-remediation'),
        ('AUTO-008', 'Self-healing security'),
    ]
    create_pillar_sheet(ws, 'Automation', 'AUTO', capabilities)


def create_compliance_sheet(ws):
    styles = get_styles()
    ws.merge_cells('A1:G1')
    ws['A1'] = "Zero Trust - Policy Compliance Scoring"
    apply_style(ws['A1'], styles['header'])
    ws.row_dimensions[1].height = 30

    headers = ['Comp-ID', 'Requirement', 'Source', 'Compliant', 'Evidence', 'Score', 'Notes']
    widths = [10, 40, 20, 12, 35, 10, 25]

    for col, (header, width) in enumerate(zip(headers, widths), 1):
        cell = ws.cell(row=3, column=col, value=header)
        apply_style(cell, styles['header'])
        ws.column_dimensions[get_column_letter(col)].width = width

    compliant_dv = DataValidation(type='list', formula1='"Yes,Partial,No"', allow_blank=True)
    ws.add_data_validation(compliant_dv)

    compliance_reqs = [
        ('COMP-001', 'Never trust, always verify principle implemented', 'POL-A.8.27 §2.1'),
        ('COMP-002', 'No implicit trust based on network location', 'POL-A.8.27 §2.1'),
        ('COMP-003', 'Every access request authenticated', 'POL-A.8.27 §2.1'),
        ('COMP-004', 'Trust continuously evaluated', 'POL-A.8.27 §2.1'),
        ('COMP-005', 'Assume breach design principle', 'POL-A.8.27 §2.1'),
        ('COMP-006', 'Internal traffic treated as potentially hostile', 'POL-A.8.27 §2.1'),
        ('COMP-007', 'Lateral movement restricted', 'POL-A.8.27 §2.1'),
        ('COMP-008', 'Access decisions based on multiple data points', 'POL-A.8.27 §2.1'),
        ('COMP-009', 'JIT/JEA access implemented', 'POL-A.8.27 §2.1'),
        ('COMP-010', 'Risk-based conditional access', 'POL-A.8.27 §2.1'),
        ('COMP-011', 'Continuous access evaluation', 'POL-A.8.27 §2.1'),
        ('COMP-012', 'Data in transit encrypted (TLS 1.2+)', 'POL-A.8.27 §2.1'),
        ('COMP-013', 'Data at rest encrypted (CONFIDENTIAL+)', 'POL-A.8.27 §2.1'),
        ('COMP-014', 'Service-to-service encryption', 'POL-A.8.27 §2.1'),
        ('COMP-015', 'ZT maturity assessment conducted annually', 'POL-A.8.27 §4'),
    ]

    for row, (comp_id, requirement, source) in enumerate(compliance_reqs, 4):
        ws.cell(row=row, column=1, value=comp_id)
        ws.cell(row=row, column=2, value=requirement)
        ws.cell(row=row, column=3, value=source)
        ws.cell(row=row, column=6, value=f'=IF(D{row}="Yes",100,IF(D{row}="Partial",50,0))')
        for col in range(1, 8):
            if col == 6:
                apply_style(ws.cell(row=row, column=col), styles['formula'])
            elif col > 3:
                apply_style(ws.cell(row=row, column=col), styles['input'])
            else:
                apply_style(ws.cell(row=row, column=col), styles['normal'])

    compliant_dv.add(f'D4:D{3 + len(compliance_reqs)}')

    last_row = 3 + len(compliance_reqs) + 2
    ws.cell(row=last_row, column=5, value="Overall Compliance:")
    ws.cell(row=last_row, column=6, value=f'=AVERAGE(F4:F{3 + len(compliance_reqs)})')
    apply_style(ws.cell(row=last_row, column=5), styles['subheader'])
    apply_style(ws.cell(row=last_row, column=6), styles['formula'])

    ws.freeze_panes = 'A4'


def create_gap_register_sheet(ws):
    styles = get_styles()
    ws.merge_cells('A1:J1')
    ws['A1'] = "Zero Trust - Gap Register"
    apply_style(ws['A1'], styles['header'])
    ws.row_dimensions[1].height = 30

    headers = ['Gap-ID', 'Pillar', 'Description', 'Risk', 'Remediation', 'Owner', 'Due Date', 'Status', 'Closure Date', 'Notes']
    widths = [10, 15, 40, 10, 40, 20, 12, 12, 12, 25]

    for col, (header, width) in enumerate(zip(headers, widths), 1):
        cell = ws.cell(row=3, column=col, value=header)
        apply_style(cell, styles['header'])
        ws.column_dimensions[get_column_letter(col)].width = width

    pillar_dv = DataValidation(type='list', formula1='"Strategy,Identity,Device,Network,Workload,Data,Visibility,Automation"', allow_blank=True)
    risk_dv = DataValidation(type='list', formula1='"High,Medium,Low"', allow_blank=True)
    status_dv = DataValidation(type='list', formula1='"Open,In Progress,Closed"', allow_blank=True)
    ws.add_data_validation(pillar_dv)
    ws.add_data_validation(risk_dv)
    ws.add_data_validation(status_dv)

    for row in range(4, 24):
        ws.cell(row=row, column=1, value=f'GAP-{row-3:03d}')
        for col in range(1, 11):
            apply_style(ws.cell(row=row, column=col), styles['input'] if col > 1 else styles['normal'])

    pillar_dv.add('B4:B23')
    risk_dv.add('D4:D23')
    status_dv.add('H4:H23')
    ws.freeze_panes = 'A4'


def create_dashboard_sheet(ws):
    styles = get_styles()
    ws.merge_cells('A1:F1')
    ws['A1'] = "Zero Trust - Maturity Dashboard"
    apply_style(ws['A1'], styles['header'])
    ws.row_dimensions[1].height = 30

    ws['A3'] = "Assessment Summary"
    apply_style(ws['A3'], styles['subheader'])
    ws.merge_cells('A3:F3')

    summary = [
        ('Assessment Date', GENERATED_DATE),
        ('Organisation', CONFIG['organisation']),
        ('Framework Reference', 'NIST SP 800-207, CISA ZT Maturity Model'),
        ('Overall Compliance Score', '=Compliance!F20'),
    ]

    row = 4
    for label, value in summary:
        ws[f'A{row}'], ws[f'B{row}'] = label, value
        apply_style(ws[f'A{row}'], styles['normal'])
        apply_style(ws[f'B{row}'], styles['formula'] if '=' in str(value) else styles['input'])
        row += 1

    row += 1
    ws[f'A{row}'] = "Pillar Maturity Summary"
    apply_style(ws[f'A{row}'], styles['subheader'])
    ws.merge_cells(f'A{row}:F{row}')
    row += 1

    pillars = ['Identity', 'Device', 'Network', 'Workload', 'Data', 'Visibility', 'Automation']
    for pillar in pillars:
        ws[f'A{row}'] = pillar
        ws[f'B{row}'] = '[Enter current maturity]'
        ws[f'C{row}'] = '[Enter target maturity]'
        apply_style(ws[f'A{row}'], styles['normal'])
        apply_style(ws[f'B{row}'], styles['input'])
        apply_style(ws[f'C{row}'], styles['input'])
        row += 1

    ws.column_dimensions['A'].width = 20
    ws.column_dimensions['B'].width = 25
    ws.column_dimensions['C'].width = 25


def main():
    logger.info("=" * 80)
    logger.info(f"ISMS Control {CONTROL_ID} - {WORKBOOK_NAME} Generator")
    logger.info("=" * 80)

    wb = Workbook()
    if "Sheet" in wb.sheetnames:
        wb.remove(wb["Sheet"])

    sheets = [
        ("Instructions", create_instructions_sheet),
        ("Strategy", create_strategy_sheet),
        ("Identity", create_identity_sheet),
        ("Device", create_device_sheet),
        ("Network", create_network_sheet),
        ("Workload", create_workload_sheet),
        ("Data", create_data_sheet),
        ("Visibility", create_visibility_sheet),
        ("Automation", create_automation_sheet),
        ("Compliance", create_compliance_sheet),
        ("GapRegister", create_gap_register_sheet),
        ("Dashboard", create_dashboard_sheet),
    ]

    for sheet_name, create_func in sheets:
        ws = wb.create_sheet(title=sheet_name)
        create_func(ws)
        logger.info(f"  ✓ Created sheet: {sheet_name}")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, '..', '90_workbooks')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, OUTPUT_FILENAME)

    wb.save(output_path)
    logger.info(f"Workbook saved: {output_path}")
    logger.info("Generation complete!")


if __name__ == "__main__":
    main()


# =============================================================================
# QA_VERIFIED: 2026-02-02
# QA_STATUS: PASSED - STANDARDIZATION COMPLETE
# QA_TOOL: Claude Code Standardization
# CHANGES: Initial creation with standard structure
# =============================================================================
