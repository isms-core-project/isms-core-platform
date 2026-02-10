#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
================================================================================
ISMS-IMP-A.8.27.2 - Threat Modelling Methodology Assessment Generator
================================================================================

ISO/IEC 27001:2022 Control A.8.27: Secure System Architecture and Engineering
Assessment Domain 2 of 4: Threat Modelling Methodology

This script generates a comprehensive Excel assessment workbook for evaluating
threat modelling methodology adoption and effectiveness.

--------------------------------------------------------------------------------
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment, Protection
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from datetime import datetime
import os
import logging

# =============================================================================
# LOGGING CONFIGURATION
# =============================================================================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-IMP-A.8.27.2"
WORKBOOK_NAME = "Threat Modelling Methodology"
CONTROL_ID = "A.8.27"
CONTROL_NAME = "Secure System Architecture and Engineering Principles"
CONTROL_REF = f"ISO/IEC 27001:2022 - Control {CONTROL_ID}: {CONTROL_NAME}"

GENERATED_DATE = datetime.now().strftime("%d.%m.%Y")
GENERATED_TIMESTAMP = datetime.now().strftime("%Y%m%d")
OUTPUT_FILENAME = f"{DOCUMENT_ID}_{WORKBOOK_NAME.replace(' ', '_')}_{GENERATED_TIMESTAMP}.xlsx"

# =============================================================================
# CONFIGURATION
# =============================================================================
CONFIG = {
    'organisation': '[Organisation]',
    'colors': {
        'header_bg': '1F4E79',
        'header_text': 'FFFFFF',
        'subheader_bg': '2E75B6',
        'input_cell': 'E2EFDA',
        'formula_cell': 'FFF2CC',
    },
}

# =============================================================================
# STYLE DEFINITIONS
# =============================================================================
def get_styles():
    thin_border = Border(
        left=Side(style='thin'), right=Side(style='thin'),
        top=Side(style='thin'), bottom=Side(style='thin')
    )
    return {
        'header': {
            'font': Font(bold=True, color=CONFIG['colors']['header_text'], size=12),
            'fill': PatternFill(start_color=CONFIG['colors']['header_bg'],
                               end_color=CONFIG['colors']['header_bg'], fill_type='solid'),
            'alignment': Alignment(horizontal='center', vertical='center', wrap_text=True),
            'border': thin_border,
        },
        'subheader': {
            'font': Font(bold=True, color=CONFIG['colors']['header_text'], size=11),
            'fill': PatternFill(start_color=CONFIG['colors']['subheader_bg'],
                               end_color=CONFIG['colors']['subheader_bg'], fill_type='solid'),
            'alignment': Alignment(horizontal='left', vertical='center', wrap_text=True),
            'border': thin_border,
        },
        'input': {
            'font': Font(size=11),
            'fill': PatternFill(start_color=CONFIG['colors']['input_cell'],
                               end_color=CONFIG['colors']['input_cell'], fill_type='solid'),
            'alignment': Alignment(horizontal='left', vertical='center', wrap_text=True),
            'border': thin_border,
        },
        'formula': {
            'font': Font(size=11),
            'fill': PatternFill(start_color=CONFIG['colors']['formula_cell'],
                               end_color=CONFIG['colors']['formula_cell'], fill_type='solid'),
            'alignment': Alignment(horizontal='center', vertical='center'),
            'border': thin_border,
        },
        'normal': {
            'font': Font(size=11),
            'alignment': Alignment(horizontal='left', vertical='center', wrap_text=True),
            'border': thin_border,
        },
    }

def apply_style(cell, style_dict):
    for attr in ['font', 'fill', 'alignment', 'border']:
        if attr in style_dict:
            setattr(cell, attr, style_dict[attr])

# =============================================================================
# SHEET CREATION FUNCTIONS
# =============================================================================

def create_instructions_sheet(ws):
    styles = get_styles()
    ws.merge_cells('A1:H1')
    ws['A1'] = f"ISMS-IMP-A.8.27.2 - Threat Modelling Methodology Assessment"
    apply_style(ws['A1'], styles['header'])
    ws.row_dimensions[1].height = 30

    ws['A3'] = "Document Information"
    apply_style(ws['A3'], styles['subheader'])
    ws.merge_cells('A3:H3')

    info = [
        ('Document ID', DOCUMENT_ID),
        ('Control Reference', CONTROL_REF),
        ('Purpose', 'Evaluate threat modelling methodology adoption and effectiveness'),
        ('Generated Date', GENERATED_DATE),
    ]

    row = 4
    for label, value in info:
        ws[f'A{row}'] = label
        ws[f'B{row}'] = value
        apply_style(ws[f'A{row}'], styles['normal'])
        apply_style(ws[f'B{row}'], styles['input'])
        ws.merge_cells(f'B{row}:H{row}')
        row += 1

    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 80


def create_methodology_sheet(ws):
    styles = get_styles()
    ws.merge_cells('A1:H1')
    ws['A1'] = "Threat Modelling - Methodology Assessment"
    apply_style(ws['A1'], styles['header'])
    ws.row_dimensions[1].height = 30

    headers = ['Meth-ID', 'Category', 'Requirement', 'Adopted', 'Documented', 'Effective', 'Evidence', 'Gaps']
    widths = [10, 25, 40, 10, 12, 12, 30, 30]

    for col, (header, width) in enumerate(zip(headers, widths), 1):
        cell = ws.cell(row=3, column=col, value=header)
        apply_style(cell, styles['header'])
        ws.column_dimensions[get_column_letter(col)].width = width

    yes_no_dv = DataValidation(type='list', formula1='"Yes,Partial,No"', allow_blank=True)
    ws.add_data_validation(yes_no_dv)

    rating_dv = DataValidation(type='list', formula1='"1,2,3,4,5"', allow_blank=True)
    ws.add_data_validation(rating_dv)

    methodology_reqs = [
        ('METH-001', 'Selection', 'Threat modelling methodology selected and documented'),
        ('METH-002', 'Selection', 'Methodology rationale documented'),
        ('METH-003', 'Scope', 'Threat model scope definition process'),
        ('METH-004', 'Assets', 'Asset identification methodology'),
        ('METH-005', 'Threats', 'STRIDE threat identification approach'),
        ('METH-006', 'Threats', 'Attack tree analysis capability'),
        ('METH-007', 'AttackSurface', 'Attack surface mapping methodology'),
        ('METH-008', 'TrustBoundaries', 'Trust boundary identification process'),
        ('METH-009', 'DataFlows', 'Data flow diagram creation'),
        ('METH-010', 'Prioritisation', 'Threat prioritisation methodology (DREAD, CVSS)'),
        ('METH-011', 'Countermeasures', 'Mitigation mapping process'),
        ('METH-012', 'Documentation', 'Threat model documentation standards'),
        ('METH-013', 'Documentation', 'Threat model template availability'),
        ('METH-014', 'Review', 'Threat model review and approval process'),
        ('METH-015', 'Review', 'Peer review of threat models'),
        ('METH-016', 'Maintenance', 'Threat model update triggers defined'),
        ('METH-017', 'Maintenance', 'Threat model version control'),
        ('METH-018', 'ATT&CK', 'MITRE ATT&CK integration'),
        ('METH-019', 'ATT&CK', 'Technique coverage tracking'),
        ('METH-020', 'Training', 'Threat modelling training programme'),
    ]

    for row, (meth_id, category, requirement) in enumerate(methodology_reqs, 4):
        ws.cell(row=row, column=1, value=meth_id)
        ws.cell(row=row, column=2, value=category)
        ws.cell(row=row, column=3, value=requirement)
        for col in range(1, 9):
            apply_style(ws.cell(row=row, column=col), styles['input'] if col > 3 else styles['normal'])

    yes_no_dv.add(f'D4:E{3 + len(methodology_reqs)}')
    rating_dv.add(f'F4:F{3 + len(methodology_reqs)}')
    ws.freeze_panes = 'A4'


def create_mitre_attack_sheet(ws):
    styles = get_styles()
    ws.merge_cells('A1:G1')
    ws['A1'] = "Threat Modelling - MITRE ATT&CK Coverage Assessment"
    apply_style(ws['A1'], styles['header'])
    ws.row_dimensions[1].height = 30

    headers = ['ATT-ID', 'Tactic', 'Technique', 'Relevance', 'Covered', 'DetectionMap', 'Gap']
    widths = [10, 20, 35, 12, 10, 35, 30]

    for col, (header, width) in enumerate(zip(headers, widths), 1):
        cell = ws.cell(row=3, column=col, value=header)
        apply_style(cell, styles['header'])
        ws.column_dimensions[get_column_letter(col)].width = width

    relevance_dv = DataValidation(type='list', formula1='"High,Medium,Low,N/A"', allow_blank=True)
    ws.add_data_validation(relevance_dv)

    covered_dv = DataValidation(type='list', formula1='"Yes,Partial,No"', allow_blank=True)
    ws.add_data_validation(covered_dv)

    # Top MITRE ATT&CK techniques
    attack_techniques = [
        ('T1566', 'Initial Access', 'Phishing'),
        ('T1566.001', 'Initial Access', 'Spearphishing Attachment'),
        ('T1566.002', 'Initial Access', 'Spearphishing Link'),
        ('T1190', 'Initial Access', 'Exploit Public-Facing Application'),
        ('T1133', 'Initial Access', 'External Remote Services'),
        ('T1078', 'Initial Access', 'Valid Accounts'),
        ('T1059', 'Execution', 'Command and Scripting Interpreter'),
        ('T1059.001', 'Execution', 'PowerShell'),
        ('T1204', 'Execution', 'User Execution'),
        ('T1053', 'Persistence', 'Scheduled Task/Job'),
        ('T1136', 'Persistence', 'Create Account'),
        ('T1547', 'Persistence', 'Boot or Logon Autostart Execution'),
        ('T1068', 'Privilege Escalation', 'Exploitation for Privilege Escalation'),
        ('T1548', 'Privilege Escalation', 'Abuse Elevation Control Mechanism'),
        ('T1055', 'Defence Evasion', 'Process Injection'),
        ('T1562', 'Defence Evasion', 'Impair Defenses'),
        ('T1070', 'Defence Evasion', 'Indicator Removal'),
        ('T1110', 'Credential Access', 'Brute Force'),
        ('T1555', 'Credential Access', 'Credentials from Password Stores'),
        ('T1003', 'Credential Access', 'OS Credential Dumping'),
        ('T1087', 'Discovery', 'Account Discovery'),
        ('T1083', 'Discovery', 'File and Directory Discovery'),
        ('T1021', 'Lateral Movement', 'Remote Services'),
        ('T1550', 'Lateral Movement', 'Use Alternate Authentication Material'),
        ('T1570', 'Lateral Movement', 'Lateral Tool Transfer'),
        ('T1005', 'Collection', 'Data from Local System'),
        ('T1114', 'Collection', 'Email Collection'),
        ('T1039', 'Collection', 'Data from Network Shared Drive'),
        ('T1041', 'Exfiltration', 'Exfiltration Over C2 Channel'),
        ('T1567', 'Exfiltration', 'Exfiltration Over Web Service'),
        ('T1486', 'Impact', 'Data Encrypted for Impact'),
        ('T1489', 'Impact', 'Service Stop'),
        ('T1490', 'Impact', 'Inhibit System Recovery'),
    ]

    for row, (att_id, tactic, technique) in enumerate(attack_techniques, 4):
        ws.cell(row=row, column=1, value=att_id)
        ws.cell(row=row, column=2, value=tactic)
        ws.cell(row=row, column=3, value=technique)
        for col in range(1, 8):
            apply_style(ws.cell(row=row, column=col), styles['input'] if col > 3 else styles['normal'])

    relevance_dv.add(f'D4:D{3 + len(attack_techniques)}')
    covered_dv.add(f'E4:E{3 + len(attack_techniques)}')
    ws.freeze_panes = 'A4'


def create_threat_catalogue_sheet(ws):
    styles = get_styles()
    ws.merge_cells('A1:H1')
    ws['A1'] = "Threat Modelling - Organisational Threat Catalogue"
    apply_style(ws['A1'], styles['header'])
    ws.row_dimensions[1].height = 30

    headers = ['Threat-ID', 'Category', 'ThreatActor', 'Motivation', 'Capability', 'ATT&CK_Ref', 'Likelihood', 'Countermeasures']
    widths = [10, 20, 25, 20, 15, 25, 15, 35]

    for col, (header, width) in enumerate(zip(headers, widths), 1):
        cell = ws.cell(row=3, column=col, value=header)
        apply_style(cell, styles['header'])
        ws.column_dimensions[get_column_letter(col)].width = width

    motivation_dv = DataValidation(type='list', formula1='"Financial,Espionage,Disruption,Ideology,Revenge"', allow_blank=True)
    ws.add_data_validation(motivation_dv)

    capability_dv = DataValidation(type='list', formula1='"Low,Moderate,High,Nation-State"', allow_blank=True)
    ws.add_data_validation(capability_dv)

    likelihood_dv = DataValidation(type='list', formula1='"Rare,Unlikely,Possible,Likely,Almost Certain"', allow_blank=True)
    ws.add_data_validation(likelihood_dv)

    threat_actors = [
        ('THR-001', 'Nation-State', 'APT Groups', 'Espionage', 'Nation-State'),
        ('THR-002', 'Nation-State', 'State-Sponsored Hackers', 'Disruption', 'Nation-State'),
        ('THR-003', 'Cybercriminal', 'Ransomware Operators', 'Financial', 'High'),
        ('THR-004', 'Cybercriminal', 'Data Brokers', 'Financial', 'Moderate'),
        ('THR-005', 'Cybercriminal', 'Credential Thieves', 'Financial', 'Moderate'),
        ('THR-006', 'Hacktivist', 'Ideological Groups', 'Ideology', 'Moderate'),
        ('THR-007', 'Hacktivist', 'Environmental Activists', 'Ideology', 'Low'),
        ('THR-008', 'Insider', 'Malicious Employee', 'Financial', 'Moderate'),
        ('THR-009', 'Insider', 'Negligent Employee', 'N/A', 'Low'),
        ('THR-010', 'Insider', 'Departing Employee', 'Revenge', 'Moderate'),
        ('THR-011', 'Competitor', 'Corporate Espionage', 'Espionage', 'Moderate'),
        ('THR-012', 'Competitor', 'IP Theft', 'Financial', 'Moderate'),
        ('THR-013', 'Script Kiddie', 'Opportunistic Attacker', 'Financial', 'Low'),
        ('THR-014', 'Supply Chain', 'Compromised Vendor', 'Financial', 'Moderate'),
        ('THR-015', 'Supply Chain', 'Third-Party Breach', 'Financial', 'Moderate'),
    ]

    for row, (threat_id, category, actor, motivation, capability) in enumerate(threat_actors, 4):
        ws.cell(row=row, column=1, value=threat_id)
        ws.cell(row=row, column=2, value=category)
        ws.cell(row=row, column=3, value=actor)
        ws.cell(row=row, column=4, value=motivation)
        ws.cell(row=row, column=5, value=capability)
        for col in range(1, 9):
            apply_style(ws.cell(row=row, column=col), styles['input'] if col > 5 else styles['normal'])

    motivation_dv.add(f'D4:D{3 + len(threat_actors)}')
    capability_dv.add(f'E4:E{3 + len(threat_actors)}')
    likelihood_dv.add(f'G4:G{3 + len(threat_actors)}')
    ws.freeze_panes = 'A4'


def create_tools_sheet(ws):
    styles = get_styles()
    ws.merge_cells('A1:H1')
    ws['A1'] = "Threat Modelling - Tools Assessment"
    apply_style(ws['A1'], styles['header'])
    ws.row_dimensions[1].height = 30

    headers = ['Tool-ID', 'Tool', 'Purpose', 'Licensed', 'Users', 'Integration', 'Effectiveness', 'Gaps']
    widths = [10, 30, 35, 10, 10, 25, 12, 30]

    for col, (header, width) in enumerate(zip(headers, widths), 1):
        cell = ws.cell(row=3, column=col, value=header)
        apply_style(cell, styles['header'])
        ws.column_dimensions[get_column_letter(col)].width = width

    licensed_dv = DataValidation(type='list', formula1='"Yes,No,OSS"', allow_blank=True)
    ws.add_data_validation(licensed_dv)

    rating_dv = DataValidation(type='list', formula1='"1,2,3,4,5"', allow_blank=True)
    ws.add_data_validation(rating_dv)

    tools = [
        ('TOOL-001', 'Microsoft Threat Modeling Tool', 'DFD-based threat modelling'),
        ('TOOL-002', 'OWASP Threat Dragon', 'Open source threat modelling'),
        ('TOOL-003', 'IriusRisk', 'Enterprise threat modelling'),
        ('TOOL-004', 'Threagile', 'Threat model as code'),
        ('TOOL-005', 'ThreatModeler', 'Cloud-native threat modelling'),
        ('TOOL-006', 'MITRE ATT&CK Navigator', 'Technique coverage mapping'),
        ('TOOL-007', 'Draw.io / Lucidchart', 'Architecture diagramming'),
        ('TOOL-008', 'Custom Internal Tool', 'Organisation-specific tool'),
    ]

    for row, (tool_id, tool, purpose) in enumerate(tools, 4):
        ws.cell(row=row, column=1, value=tool_id)
        ws.cell(row=row, column=2, value=tool)
        ws.cell(row=row, column=3, value=purpose)
        for col in range(1, 9):
            apply_style(ws.cell(row=row, column=col), styles['input'] if col > 3 else styles['normal'])

    licensed_dv.add(f'D4:D{3 + len(tools)}')
    rating_dv.add(f'G4:G{3 + len(tools)}')
    ws.freeze_panes = 'A4'


def create_competency_sheet(ws):
    styles = get_styles()
    ws.merge_cells('A1:H1')
    ws['A1'] = "Threat Modelling - Team Competency Assessment"
    apply_style(ws['A1'], styles['header'])
    ws.row_dimensions[1].height = 30

    headers = ['Comp-ID', 'Role', 'Competency', 'Required', 'Training', 'Certified', 'Target', 'Gap']
    widths = [10, 25, 30, 12, 10, 10, 10, 25]

    for col, (header, width) in enumerate(zip(headers, widths), 1):
        cell = ws.cell(row=3, column=col, value=header)
        apply_style(cell, styles['header'])
        ws.column_dimensions[get_column_letter(col)].width = width

    required_dv = DataValidation(type='list', formula1='"Mandatory,Recommended"', allow_blank=True)
    ws.add_data_validation(required_dv)

    training_dv = DataValidation(type='list', formula1='"Yes,Partial,No"', allow_blank=True)
    ws.add_data_validation(training_dv)

    competencies = [
        ('COMP-001', 'Security Architect', 'STRIDE Methodology'),
        ('COMP-002', 'Security Architect', 'PASTA Framework'),
        ('COMP-003', 'Security Architect', 'Attack Tree Analysis'),
        ('COMP-004', 'Security Architect', 'MITRE ATT&CK Framework'),
        ('COMP-005', 'Security Architect', 'Data Flow Diagramming'),
        ('COMP-006', 'Security Architect', 'Risk Assessment'),
        ('COMP-007', 'Senior Developer', 'STRIDE Basics'),
        ('COMP-008', 'Senior Developer', 'Secure Design Principles'),
        ('COMP-009', 'SOC Analyst', 'MITRE ATT&CK Navigation'),
        ('COMP-010', 'SOC Analyst', 'Threat Detection Mapping'),
        ('COMP-011', 'Red Team', 'Attack Path Analysis'),
        ('COMP-012', 'Red Team', 'MITRE ATT&CK Adversary Emulation'),
    ]

    for row, (comp_id, role, competency) in enumerate(competencies, 4):
        ws.cell(row=row, column=1, value=comp_id)
        ws.cell(row=row, column=2, value=role)
        ws.cell(row=row, column=3, value=competency)
        for col in range(1, 9):
            apply_style(ws.cell(row=row, column=col), styles['input'] if col > 3 else styles['normal'])

    required_dv.add(f'D4:D{3 + len(competencies)}')
    training_dv.add(f'E4:E{3 + len(competencies)}')
    ws.freeze_panes = 'A4'


def create_samples_sheet(ws):
    styles = get_styles()
    ws.merge_cells('A1:J1')
    ws['A1'] = "Threat Modelling - Sample Quality Review"
    apply_style(ws['A1'], styles['header'])
    ws.row_dimensions[1].height = 30

    headers = ['Sample-ID', 'System', 'Date', 'Author', 'Methodology', 'Completeness', 'Quality', 'ATT&CK_Mapped', 'Findings', 'Mitigated']
    widths = [10, 25, 12, 20, 15, 12, 12, 12, 10, 10]

    for col, (header, width) in enumerate(zip(headers, widths), 1):
        cell = ws.cell(row=3, column=col, value=header)
        apply_style(cell, styles['header'])
        ws.column_dimensions[get_column_letter(col)].width = width

    methodology_dv = DataValidation(type='list', formula1='"STRIDE,PASTA,OCTAVE,Other"', allow_blank=True)
    ws.add_data_validation(methodology_dv)

    rating_dv = DataValidation(type='list', formula1='"1,2,3,4,5"', allow_blank=True)
    ws.add_data_validation(rating_dv)

    mapped_dv = DataValidation(type='list', formula1='"Yes,Partial,No"', allow_blank=True)
    ws.add_data_validation(mapped_dv)

    # Pre-populate 10 sample rows
    for row in range(4, 14):
        ws.cell(row=row, column=1, value=f'SAMP-{row-3:03d}')
        for col in range(1, 11):
            apply_style(ws.cell(row=row, column=col), styles['input'] if col > 1 else styles['normal'])

    methodology_dv.add('E4:E13')
    rating_dv.add('F4:G13')
    mapped_dv.add('H4:H13')
    ws.freeze_panes = 'A4'


def create_compliance_sheet(ws):
    styles = get_styles()
    ws.merge_cells('A1:G1')
    ws['A1'] = "Threat Modelling - Policy Compliance Scoring"
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
        ('COMP-001', 'Threat modelling methodology adopted', 'POL-A.8.27 §2.2.1'),
        ('COMP-002', 'STRIDE or equivalent methodology used', 'POL-A.8.27 §2.2.1'),
        ('COMP-003', 'Threat models created for new systems', 'POL-A.8.27 §2.2.1'),
        ('COMP-004', 'Threat models updated for major changes', 'POL-A.8.27 §2.2.1'),
        ('COMP-005', 'MITRE ATT&CK integrated into threat analysis', 'POL-A.8.27 §2.2.1'),
        ('COMP-006', 'Threat model documentation standards defined', 'POL-A.8.27 §2.2.1'),
        ('COMP-007', 'Threat model review process established', 'POL-A.8.27 §2.2.1'),
        ('COMP-008', 'Threat modelling training available', 'POL-A.8.27 §4'),
        ('COMP-009', 'Threat modelling tools provided', 'POL-A.8.27 §4'),
        ('COMP-010', 'Organisational threat catalogue maintained', 'POL-A.8.27 §2.1'),
        ('COMP-011', 'Threat model findings tracked', 'POL-A.8.27 §2.2.1'),
        ('COMP-012', 'Countermeasures mapped to threats', 'POL-A.8.27 §2.2.1'),
        ('COMP-013', 'Threat model quality reviews conducted', 'POL-A.8.27 §4'),
        ('COMP-014', 'ATT&CK coverage measured', 'POL-A.8.27 §4'),
        ('COMP-015', 'Threat modelling effectiveness tracked', 'POL-A.8.27 §4'),
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
    ws.cell(row=last_row, column=5, value="Overall Compliance Score:")
    ws.cell(row=last_row, column=6, value=f'=AVERAGE(F4:F{3 + len(compliance_reqs)})')
    apply_style(ws.cell(row=last_row, column=5), styles['subheader'])
    apply_style(ws.cell(row=last_row, column=6), styles['formula'])

    ws.freeze_panes = 'A4'


def create_gap_register_sheet(ws):
    styles = get_styles()
    ws.merge_cells('A1:J1')
    ws['A1'] = "Threat Modelling - Gap Register"
    apply_style(ws['A1'], styles['header'])
    ws.row_dimensions[1].height = 30

    headers = ['Gap-ID', 'Source', 'Description', 'Risk', 'Remediation', 'Owner', 'Due Date', 'Status', 'Closure Date', 'Notes']
    widths = [10, 15, 40, 10, 40, 20, 12, 12, 12, 25]

    for col, (header, width) in enumerate(zip(headers, widths), 1):
        cell = ws.cell(row=3, column=col, value=header)
        apply_style(cell, styles['header'])
        ws.column_dimensions[get_column_letter(col)].width = width

    risk_dv = DataValidation(type='list', formula1='"High,Medium,Low"', allow_blank=True)
    ws.add_data_validation(risk_dv)

    status_dv = DataValidation(type='list', formula1='"Open,In Progress,Closed"', allow_blank=True)
    ws.add_data_validation(status_dv)

    for row in range(4, 24):
        ws.cell(row=row, column=1, value=f'GAP-{row-3:03d}')
        for col in range(1, 11):
            apply_style(ws.cell(row=row, column=col), styles['input'] if col > 1 else styles['normal'])

    risk_dv.add('D4:D23')
    status_dv.add('H4:H23')
    ws.freeze_panes = 'A4'


def create_dashboard_sheet(ws):
    styles = get_styles()
    ws.merge_cells('A1:F1')
    ws['A1'] = "Threat Modelling - Assessment Dashboard"
    apply_style(ws['A1'], styles['header'])
    ws.row_dimensions[1].height = 30

    ws['A3'] = "Assessment Summary"
    apply_style(ws['A3'], styles['subheader'])
    ws.merge_cells('A3:F3')

    summary = [
        ('Assessment Date', GENERATED_DATE),
        ('Organisation', CONFIG['organisation']),
        ('Control Reference', CONTROL_REF),
        ('Overall Compliance Score', '=Compliance!F20'),
    ]

    row = 4
    for label, value in summary:
        ws[f'A{row}'] = label
        ws[f'B{row}'] = value
        apply_style(ws[f'A{row}'], styles['normal'])
        apply_style(ws[f'B{row}'], styles['formula'] if '=' in str(value) else styles['input'])
        row += 1

    ws.column_dimensions['A'].width = 30
    ws.column_dimensions['B'].width = 20


def main():
    logger.info("=" * 80)
    logger.info(f"ISMS Control {CONTROL_ID} - {WORKBOOK_NAME} Generator")
    logger.info("=" * 80)
    logger.info("")
    logger.info("Generating assessment workbook...")

    wb = Workbook()
    if "Sheet" in wb.sheetnames:
        wb.remove(wb["Sheet"])

    sheets = [
        ("Instructions", create_instructions_sheet),
        ("Methodology", create_methodology_sheet),
        ("MITRE_ATT&CK", create_mitre_attack_sheet),
        ("ThreatCatalogue", create_threat_catalogue_sheet),
        ("Tools", create_tools_sheet),
        ("Competency", create_competency_sheet),
        ("Samples", create_samples_sheet),
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
