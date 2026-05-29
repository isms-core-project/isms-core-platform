import { Component, inject, signal, computed, effect, OnDestroy } from '@angular/core'
import { FormsModule } from '@angular/forms'
import { firstValueFrom } from 'rxjs'
import cytoscape from 'cytoscape'

import { injectQuery } from '@tanstack/angular-query-experimental'

import { MatCardModule } from '@angular/material/card'
import { MatButtonModule } from '@angular/material/button'
import { MatIconModule } from '@angular/material/icon'
import { MatChipsModule } from '@angular/material/chips'
import { MatFormFieldModule } from '@angular/material/form-field'
import { MatInputModule } from '@angular/material/input'
import { MatSelectModule } from '@angular/material/select'
import { MatSliderModule } from '@angular/material/slider'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatTooltipModule } from '@angular/material/tooltip'

import { GraphApiService } from '../../api/graph-api.service'
import { ProductService, PRODUCT_SUBTITLES } from '../../core/services/product.service'
import { TokenStoreService } from '../../core/services/token-store.service'
import { PageHeaderComponent } from '../../shared/components/page-header.component'
import { GraphNode, GraphEdge, GraphResponse } from '../../shared/types'

// ── Constants ─────────────────────────────────────────────────────────────────

const NODE_COLORS: Record<string, string> = {
  control_group: '#4472C4',
  iso_control:   '#70AD47',
  external_ref:  '#FFC000',
}

const PRODUCT_SOURCE_FRAMEWORK: Record<string, string> = {
  isms: 'ISO27001', privacy: 'ISO27701', cloud: 'ISO27017', ai: 'ISO42001',
}

const PRODUCT_SECTIONS: Record<string, { label: string; value: string }[]> = {
  isms: [
    { label: 'A.5 — Organisational', value: 'A.5' },
    { label: 'A.6 — People',         value: 'A.6' },
    { label: 'A.7 — Physical',       value: 'A.7' },
    { label: 'A.8 — Technological',  value: 'A.8' },
  ],
  privacy: [
    { label: 'A.1 — PII Controller', value: 'A.1' },
    { label: 'A.2 — PII Processor',  value: 'A.2' },
    { label: 'A.3 — Both',           value: 'A.3' },
  ],
  cloud: [],
  ai: [
    { label: 'A.2 — AI Policies',          value: 'A.2' },
    { label: 'A.3 — Roles & Resources',    value: 'A.3' },
    { label: 'A.4 — AI Resources',         value: 'A.4' },
    { label: 'A.5 — Planning & Operation', value: 'A.5' },
    { label: 'A.6 — Operation',            value: 'A.6' },
    { label: 'A.7 — Data for AI',          value: 'A.7' },
    { label: 'A.8 — Information',          value: 'A.8' },
    { label: 'A.9 — Responsible Use',      value: 'A.9' },
    { label: 'A.10 — Third-Party',         value: 'A.10' },
  ],
}

interface GraphParams {
  source_framework: string
  center?: string
  depth: number
  section?: string
  max_nodes: number
}

function shortId(id: string): string {
  const parts = id.split(':')
  const last = parts[parts.length - 1]
  return last.length <= 20 ? last : last.slice(0, 18) + '…'
}

// ── Component ─────────────────────────────────────────────────────────────────

@Component({
  selector: 'app-graph',
  standalone: true,
  imports: [
    FormsModule,
    MatCardModule, MatButtonModule, MatIconModule, MatChipsModule,
    MatFormFieldModule, MatInputModule, MatSelectModule, MatSliderModule,
    MatProgressSpinnerModule, MatTooltipModule,
    PageHeaderComponent,
  ],
  template: `
<div class="page-wrap">
  <app-page-header
    title="Control Dependency Graph"
    [subtitle]="subtitle()">
  </app-page-header>

  <!-- Controls -->
  <mat-card class="controls-card">
    <mat-card-content class="controls-content">
      <div class="controls-row">
        <mat-form-field appearance="outline" class="field-center" subscriptSizing="dynamic">
          <mat-label>Centre node (code)</mat-label>
          <input matInput [(ngModel)]="centerInput" placeholder="e.g. a.5.1-2">
        </mat-form-field>

        @if (sectionOptions().length > 0) {
          <mat-form-field appearance="outline" class="field-section" subscriptSizing="dynamic">
            <mat-label>Section</mat-label>
            <mat-select [(ngModel)]="sectionInput">
              <mat-option value="">All</mat-option>
              @for (opt of sectionOptions(); track opt.value) {
                <mat-option [value]="opt.value">{{ opt.label }}</mat-option>
              }
            </mat-select>
          </mat-form-field>
        }

        <div class="depth-wrap">
          <div class="depth-label">Depth: {{ depthInput }}</div>
          <mat-slider min="1" max="3" step="1" class="depth-slider">
            <input matSliderThumb [(ngModel)]="depthInput">
          </mat-slider>
        </div>

        <button mat-flat-button color="primary" (click)="loadGraph()">
          <mat-icon>refresh</mat-icon> Load Graph
        </button>
      </div>
    </mat-card-content>
  </mat-card>

  <!-- Legend -->
  <div class="legend-row">
    @for (entry of nodeColorEntries; track entry.type) {
      <div class="legend-entry">
        <div class="legend-dot" [style.background]="entry.color"></div>
        <span class="legend-text">{{ entry.label }}</span>
      </div>
    }
    @if (graphQuery.data()) {
      <mat-chip class="stats-chip">
        {{ graphQuery.data()!.total_nodes }} nodes · {{ graphQuery.data()!.total_edges }} edges
      </mat-chip>
    }
  </div>

  <!-- Canvas + info panel -->
  <mat-card class="data-card">
    <mat-card-content class="data-content">

      @if (!submitted()) {
        <div class="placeholder-wrap">
          <mat-icon class="placeholder-icon">account_tree</mat-icon>
          <div class="placeholder-text">Control Dependency Graph</div>
          <div class="placeholder-hint">Click "Load Graph" to visualise the control dependency network.</div>
        </div>
      }

      @if (submitted() && graphQuery.isLoading()) {
        <div class="spinner-center"><mat-spinner></mat-spinner></div>
      }

      @if (submitted() && graphQuery.isError()) {
        <div class="error-msg">Failed to load graph data.</div>
      }

      @if (submitted() && graphQuery.data()) {
        <!-- Cytoscape canvas -->
        <div class="cyto-layout">
          <div id="cytoscape-graph-container" class="cyto-canvas"></div>

          @if (selectedNode()) {
            <div class="node-panel">
              <div class="np-type-dot" [style.background]="nodeColor(selectedNode()!.node_type)"></div>
              <div class="np-id">{{ selectedNode()!.id }}</div>
              <div class="np-label">{{ selectedNode()!.label }}</div>
              @if (selectedNode()!.section) {
                <div class="np-section">Section: {{ selectedNode()!.section }}</div>
              }
              <div class="np-type">{{ selectedNode()!.node_type.replace('_', ' ') }}</div>
              <button mat-icon-button class="np-close" (click)="selectedNode.set(null)">
                <mat-icon>close</mat-icon>
              </button>
            </div>
          }
        </div>

        <!-- Hint -->
        <div class="canvas-hint">Click a node to inspect · Scroll to zoom · Drag to pan</div>

        <!-- Collapsed data tables -->
        <details class="data-details">
          <summary class="data-summary">Raw data — {{ graphQuery.data()!.nodes.length }} nodes, {{ graphQuery.data()!.edges.length }} edges</summary>

          <div class="table-section">
            <div class="table-scroll-nodes">
              <table class="data-table">
                <thead class="sticky-head">
                  <tr class="thead-row">
                    <th class="th-cell th-type">Type</th>
                    <th class="th-cell th-id">ID</th>
                    <th class="th-cell">Label</th>
                    <th class="th-cell th-section">Section</th>
                  </tr>
                </thead>
                <tbody>
                  @for (node of graphQuery.data()!.nodes; track node.id) {
                    <tr class="tbody-row">
                      <td class="td-cell"><div class="node-dot" [style.background]="nodeColor(node.node_type)"></div></td>
                      <td class="td-cell td-mono td-blue">{{ node.id }}</td>
                      <td class="td-cell td-label">{{ node.label }}</td>
                      <td class="td-cell td-muted">{{ node.section ?? '—' }}</td>
                    </tr>
                  }
                </tbody>
              </table>
            </div>
          </div>

          @if (graphQuery.data()!.edges.length > 0) {
            <div class="table-section">
              <div class="table-scroll-edges">
                <table class="data-table">
                  <thead class="sticky-head">
                    <tr class="thead-row">
                      <th class="th-cell">Source</th>
                      <th class="th-cell">Target</th>
                      <th class="th-cell th-edge-type">Type</th>
                      <th class="th-cell th-edge-label">Label</th>
                    </tr>
                  </thead>
                  <tbody>
                    @for (edge of graphQuery.data()!.edges; track ($index)) {
                      <tr class="tbody-row">
                        <td class="td-cell td-mono td-blue">{{ edge.source }}</td>
                        <td class="td-cell td-mono td-blue">{{ edge.target }}</td>
                        <td class="td-cell td-muted">{{ edge.edge_type }}</td>
                        <td class="td-cell td-muted">{{ edge.label }}</td>
                      </tr>
                    }
                  </tbody>
                </table>
              </div>
            </div>
          }
        </details>
      }
    </mat-card-content>
  </mat-card>
</div>
`,
  styles: [`:host { display: block; }

  .page-wrap { padding: 0 4px; }

  .controls-card { margin-top: 16px; margin-bottom: 16px; }
  .controls-content { padding-bottom: 12px !important; }
  .controls-row { display: flex; gap: 16px; flex-wrap: wrap; align-items: center; }
  .field-center { min-width: 180px; }
  .field-section { min-width: 160px; }
  .depth-wrap { min-width: 180px; }
  .depth-label { font-size: .72rem; opacity: .6; margin-bottom: 4px; }
  .depth-slider { width: 100%; }

  .legend-row { display: flex; gap: 12px; margin-bottom: 12px; flex-wrap: wrap; align-items: center; }
  .legend-entry { display: flex; align-items: center; gap: 6px; }
  .legend-dot { width: 12px; height: 12px; border-radius: 50%; }
  .legend-text { font-size: .72rem; opacity: .6; }
  .stats-chip { margin-left: auto; font-size: .7rem; height: 20px; }

  .data-card { }
  .data-content { padding-bottom: 16px !important; }

  .placeholder-wrap {
    display: flex; flex-direction: column; align-items: center;
    justify-content: center; min-height: 200px; opacity: .4;
  }
  .placeholder-icon { font-size: 48px; margin-bottom: 12px; }
  .placeholder-text { font-size: .9rem; font-weight: 600; }
  .placeholder-hint { font-size: .72rem; margin-top: 6px; }

  .spinner-center { display: flex; justify-content: center; padding: 40px; }
  .error-msg { color: #f44336; padding: 16px; }

  .cyto-layout { position: relative; }

  .cyto-canvas {
    width: 100%;
    height: 560px;
    border-radius: 8px;
    background: var(--mat-sys-surface-container);
    border: 1px solid rgba(128,128,128,0.2);
  }

  .node-panel {
    position: absolute;
    top: 12px; right: 12px;
    width: 220px;
    background: var(--mat-sys-surface);
    border: 1px solid var(--mat-sys-outline-variant);
    border-radius: 8px;
    padding: 12px 14px;
    z-index: 10;
  }
  .np-type-dot { width: 10px; height: 10px; border-radius: 50%; margin-bottom: 8px; }
  .np-id { font-family: monospace; font-size: .72rem; color: #9DC3E6; margin-bottom: 4px; word-break: break-all; }
  .np-label { font-size: .82rem; font-weight: 600; margin-bottom: 6px; }
  .np-section { font-size: .68rem; opacity: .6; margin-bottom: 2px; }
  .np-type { font-size: .65rem; opacity: .5; text-transform: capitalize; }
  .np-close { position: absolute; top: 4px; right: 4px; width: 24px; height: 24px; line-height: 24px; }

  .canvas-hint { font-size: .65rem; opacity: .4; text-align: center; margin-top: 6px; margin-bottom: 14px; }

  .data-details { border: 1px solid rgba(255,255,255,0.06); border-radius: 6px; overflow: hidden; }
  .data-summary {
    font-size: .72rem; font-weight: 600; opacity: .5;
    padding: 8px 12px; cursor: pointer; user-select: none;
    text-transform: uppercase; letter-spacing: .04em;
    list-style: none;
  }
  .data-summary::-webkit-details-marker { display: none; }
  .data-summary::before { content: '▶ '; font-size: .6rem; }
  details[open] .data-summary::before { content: '▼ '; }

  .table-section { padding: 0 4px 8px; }
  .table-scroll-nodes { overflow-x: auto; max-height: 280px; overflow-y: auto; }
  .table-scroll-edges { overflow-x: auto; max-height: 220px; overflow-y: auto; }

  .data-table { width: 100%; border-collapse: collapse; font-size: .78rem; }
  .sticky-head { position: sticky; top: 0; z-index: 1; background: var(--mat-sys-surface-container); }
  .thead-row { border-bottom: 1px solid rgba(255,255,255,.1); }
  .th-cell { padding: 6px 10px; text-align: left; font-size: .7rem; font-weight: 600; opacity: .6; }
  .th-type { width: 48px; }
  .th-id { width: 160px; }
  .th-section { width: 80px; }
  .th-edge-type { width: 100px; }
  .th-edge-label { width: 120px; }

  .tbody-row { border-bottom: 1px solid rgba(255,255,255,.04); }
  .td-cell { padding: 5px 10px; }
  .td-mono { font-family: monospace; font-size: .7rem; }
  .td-blue { color: #9DC3E6; }
  .td-label { font-size: .75rem; }
  .td-muted { font-size: .7rem; opacity: .5; }
  .node-dot { width: 10px; height: 10px; border-radius: 50%; }
`],
})
export class GraphComponent implements OnDestroy {
  private graphApi   = inject(GraphApiService)
  readonly product   = inject(ProductService)
  private tokenStore = inject(TokenStoreService)

  centerInput  = ''
  sectionInput = ''
  depthInput   = 2
  submitted    = signal(false)
  selectedNode = signal<GraphNode | null>(null)

  submittedParams = signal<GraphParams | null>(null)

  private cy: cytoscape.Core | null = null

  readonly nodeColorEntries = Object.entries(NODE_COLORS).map(([type, color]) => ({
    type,
    color,
    label: type.replace(/_/g, ' '),
  }))

  sectionOptions = computed(() => PRODUCT_SECTIONS[this.product.product()] ?? [])

  subtitle = computed((): string => {
    const sub = PRODUCT_SUBTITLES[this.product.product()] ?? ''
    return `${sub} — cross-framework relationships`
  })

  graphQuery = injectQuery(() => ({
    queryKey: ['graph', this.submittedParams()],
    queryFn: () => {
      const p = this.submittedParams()!
      const srcFw = PRODUCT_SOURCE_FRAMEWORK[this.product.product()] ?? 'ISO27001'
      const url = new URL('/api/v1/graph', window.location.origin)
      url.searchParams.set('source_framework', p.source_framework || srcFw)
      url.searchParams.set('depth', String(p.depth))
      url.searchParams.set('max_nodes', String(p.max_nodes))
      if (p.center)  url.searchParams.set('center', p.center)
      if (p.section) url.searchParams.set('section', p.section)
      return fetch(url.toString(), {
        headers: { Authorization: 'Bearer ' + (this.tokenStore.get() ?? '') },
      }).then(r => {
        if (!r.ok) throw new Error(`Graph API error ${r.status}`)
        return r.json() as Promise<GraphResponse>
      })
    },
    enabled: !!this.submittedParams(),
    staleTime: 300_000,
  }))

  constructor() {
    effect(() => {
      const data = this.graphQuery.data()
      if (!data) return
      // Let @if render the canvas div first
      setTimeout(() => this.renderCytoscape(data), 0)
    })
  }

  ngOnDestroy() {
    this.cy?.destroy()
  }

  loadGraph(): void {
    const srcFw = PRODUCT_SOURCE_FRAMEWORK[this.product.product()] ?? 'ISO27001'
    this.selectedNode.set(null)
    this.submittedParams.set({
      source_framework: srcFw,
      center: this.centerInput || undefined,
      depth: this.depthInput,
      section: this.sectionInput || undefined,
      max_nodes: 150,
    })
    this.submitted.set(true)
  }

  nodeColor(type: string): string {
    return NODE_COLORS[type] ?? '#888'
  }

  private renderCytoscape(data: GraphResponse): void {
    const container = document.getElementById('cytoscape-graph-container')
    if (!container) return

    this.cy?.destroy()
    this.selectedNode.set(null)

    const isLight = document.documentElement.getAttribute('data-theme') === 'light'

    const elements: cytoscape.ElementDefinition[] = [
      ...data.nodes.map(n => ({
        group: 'nodes' as const,
        data: {
          id: n.id, label: shortId(n.id), fullLabel: n.label,
          type: n.node_type, section: n.section ?? '',
          nodeColor: NODE_COLORS[n.node_type] ?? '#888',
        },
      })),
      ...data.edges.map((e, i) => ({
        group: 'edges' as const,
        data: { id: `e${i}`, source: e.source, target: e.target, etype: e.edge_type },
      })),
    ]

    this.cy = cytoscape({
      container,
      elements,
      style: [
        {
          selector: 'node',
          style: {
            'background-color': 'data(nodeColor)',
            'label': 'data(label)',
            'font-size': '9px',
            'color': isLight ? '#333333' : '#e0e0e0',
            'text-valign': 'bottom',
            'text-halign': 'center',
            'text-margin-y': 2,
            'width': 18,
            'height': 18,
            'text-wrap': 'ellipsis',
            'text-max-width': '70px',
            'border-width': 0,
          } as any,
        },
        {
          selector: 'node:selected',
          style: {
            'border-width': 2,
            'border-color': isLight ? '#333333' : '#ffffff',
            'width': 24,
            'height': 24,
          },
        },
        {
          selector: 'edge',
          style: {
            'width': 1,
            'line-color': isLight ? 'rgba(0,0,0,0.2)' : 'rgba(255,255,255,0.15)',
            'target-arrow-color': isLight ? 'rgba(0,0,0,0.3)' : 'rgba(255,255,255,0.25)',
            'target-arrow-shape': 'triangle',
            'curve-style': 'bezier',
            'arrow-scale': 0.7,
          },
        },
        {
          selector: 'edge:selected',
          style: {
            'line-color': isLight ? 'rgba(0,0,0,0.6)' : 'rgba(255,255,255,0.5)',
            'width': 2,
          },
        },
      ],
      layout: {
        name: 'cose',
        animate: false,
        randomize: true,
        nodeRepulsion: () => 450000,
        idealEdgeLength: () => 80,
        numIter: 300,
        fit: true,
        padding: 24,
      } as any,
      wheelSensitivity: 0.3,
    })

    // Wire up node click → inspector panel
    const self = this
    const cy = this.cy
    if (!cy) return
    cy.on('tap', 'node', function(this: cytoscape.NodeSingular) {
      const d = this.data()
      const node = data.nodes.find(n => n.id === d.id) ?? null
      self.selectedNode.set(node)
    })
    cy.on('tap', function(e: cytoscape.EventObject) {
      if (e.target === self.cy) self.selectedNode.set(null)
    })
  }
}
