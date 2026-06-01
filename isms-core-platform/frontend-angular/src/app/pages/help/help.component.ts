import { Component, inject, signal, computed, ElementRef, viewChild } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { DomSanitizer, SafeHtml } from '@angular/platform-browser'
import { firstValueFrom } from 'rxjs'
import { Router } from '@angular/router'

import { MatButtonModule } from '@angular/material/button'
import { MatIconModule } from '@angular/material/icon'
import { MatListModule } from '@angular/material/list'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatSidenavModule } from '@angular/material/sidenav'

// ── Types ─────────────────────────────────────────────────────────────────────

interface TocEntry {
  id: string
  label: string
  level: number
}

// ── Helpers ───────────────────────────────────────────────────────────────────

function extractToc(md: string): TocEntry[] {
  const entries: TocEntry[] = []
  for (const line of md.split('\n')) {
    const m = line.match(/^(#{1,3})\s+(.+?)(?:\s+\{#[\w-]+\})?$/)
    if (!m) continue
    const level = m[1].length
    const rawLabel = m[2].replace(/\*\*/g, '').replace(/`/g, '').trim()
    const anchorMatch = line.match(/\{#([\w-]+)\}/)
    const id = anchorMatch
      ? anchorMatch[1]
      : rawLabel.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '')
    entries.push({ id, label: rawLabel, level })
  }
  return entries
}

/**
 * Convert markdown to lightweight HTML.
 * Only handles the constructs used in the ISMS user manual:
 * headings, bold, code spans, code blocks, blockquotes, tables,
 * ordered/unordered lists, horizontal rules, paragraphs.
 */
function markdownToHtml(md: string): string {
  const lines = md.split('\n')
  const out: string[] = []
  let inCodeBlock = false
  let inTable = false
  let inList = false
  let listType = ''

  const closePending = () => {
    if (inTable)  { out.push('</tbody></table>'); inTable = false }
    if (inList)   { out.push(`</${listType}>`);   inList = false; listType = '' }
  }

  const escape = (s: string) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')

  const inline = (s: string): string => {
    s = s
      .replace(/`([^`]+)`/g, '<code>$1</code>')
      .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.+?)\*/g, '<em>$1</em>')
      .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>')
    return s
  }

  for (let i = 0; i < lines.length; i++) {
    const raw = lines[i]

    if (raw.startsWith('```')) {
      if (!inCodeBlock) { closePending(); out.push('<pre><code>'); inCodeBlock = true }
      else              { out.push('</code></pre>'); inCodeBlock = false }
      continue
    }
    if (inCodeBlock) { out.push(escape(raw)); continue }

    // blank line
    if (raw.trim() === '') { closePending(); continue }

    // headings
    const hm = raw.match(/^(#{1,3})\s+(.+?)(?:\s+\{#[\w-]+\})?$/)
    if (hm) {
      closePending()
      const level = hm[1].length
      const text = hm[2].replace(/\{#[\w-]+\}/g, '').trim()
      const anchorMatch = raw.match(/\{#([\w-]+)\}/)
      const id = anchorMatch
        ? anchorMatch[1]
        : text.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '')
      out.push(`<h${level} id="${id}" style="scroll-margin-top:80px">${inline(text)}</h${level}>`)
      continue
    }

    // horizontal rule
    if (/^---+$/.test(raw.trim())) { closePending(); out.push('<hr>'); continue }

    // blockquote
    if (raw.startsWith('> ')) { closePending(); out.push(`<blockquote>${inline(raw.slice(2))}</blockquote>`); continue }

    // table row
    if (raw.includes('|')) {
      const cells = raw.split('|').map(c => c.trim()).filter((_, i, a) => i > 0 && i < a.length - 1)
      if (/^[\s|:-]+$/.test(raw)) { /* separator row — skip */ continue }
      if (!inTable) {
        closePending()
        out.push('<table><thead><tr>')
        cells.forEach(c => out.push(`<th>${inline(c)}</th>`))
        out.push('</tr></thead><tbody>')
        inTable = true
        // peek: if next line is separator, skip it
        if (i + 1 < lines.length && /^[\s|:-]+$/.test(lines[i + 1])) i++
      } else {
        out.push('<tr>')
        cells.forEach(c => out.push(`<td>${inline(c)}</td>`))
        out.push('</tr>')
      }
      continue
    }

    // unordered list
    const ulm = raw.match(/^[-*+]\s+(.+)/)
    if (ulm) {
      if (!inList || listType !== 'ul') { closePending(); out.push('<ul>'); inList = true; listType = 'ul' }
      out.push(`<li>${inline(ulm[1])}</li>`)
      continue
    }

    // ordered list
    const olm = raw.match(/^\d+\.\s+(.+)/)
    if (olm) {
      if (!inList || listType !== 'ol') { closePending(); out.push('<ol>'); inList = true; listType = 'ol' }
      out.push(`<li>${inline(olm[1])}</li>`)
      continue
    }

    // paragraph
    closePending()
    out.push(`<p>${inline(raw)}</p>`)
  }
  closePending()
  return out.join('\n')
}

// ── Component ─────────────────────────────────────────────────────────────────

@Component({
  selector: 'app-help',
  standalone: true,
  imports: [
    MatButtonModule, MatIconModule, MatListModule,
    MatProgressSpinnerModule, MatTooltipModule, MatSidenavModule,
  ],
  template: `
<div class="help-layout">

  <!-- Sidebar TOC -->
  <div class="toc-sidebar" [class.toc-sidebar--collapsed]="tocCollapsed()">

    <!-- Header row: label + toggle -->
    <div class="toc-header">
      @if (!tocCollapsed()) {
        <span class="toc-label">Contents</span>
      }
      <button mat-icon-button class="toc-toggle-btn"
        (click)="tocCollapsed.set(!tocCollapsed())"
        [matTooltip]="tocCollapsed() ? 'Show contents' : 'Hide contents'">
        <mat-icon>{{ tocCollapsed() ? 'chevron_right' : 'chevron_left' }}</mat-icon>
      </button>
    </div>

    <!-- Accordion nav — hidden when collapsed -->
    @if (!tocCollapsed()) {
      <nav class="toc-nav">
        @for (sec of sections(); track sec.entry.id) {

          <!-- H1 section header — click to expand/collapse -->
          <div class="toc-sec-hdr" (click)="onSectionClick(sec.entry.id)"
            [class.toc-sec-hdr--active]="activeId() === sec.entry.id">
            <span class="toc-sec-lbl"
              [style.color]="activeId() === sec.entry.id ? '#9DC3E6' : 'inherit'">
              {{ sec.entry.label }}
            </span>
            <mat-icon class="toc-sec-chevron"
              [class.toc-sec-chevron--open]="expandedSections().has(sec.entry.id)">
              expand_more
            </mat-icon>
          </div>

          <!-- H2 / H3 children — shown when section is open -->
          @if (expandedSections().has(sec.entry.id)) {
            @for (child of sec.children; track child.id) {
              <div class="toc-entry"
                (click)="scrollTo(child.id)"
                [style.padding-left.px]="child.level === 2 ? 16 : 28"
                [style.background]="activeId() === child.id ? 'color-mix(in srgb, var(--mat-sys-primary) 14%, transparent)' : 'transparent'"
                [style.border-left-color]="activeId() === child.id ? 'var(--mat-sys-primary)' : 'transparent'"
                [style.color]="activeId() === child.id ? 'var(--mat-sys-primary)' : 'inherit'">
                {{ child.label }}
              </div>
            }
          }
        }
      </nav>
    }
  </div>

  <!-- Main content -->
  <div #contentArea class="content-area">
    <!-- Header -->
    <div class="content-header">
      <h4 class="content-title">User Guide</h4>
      <span class="content-version">v1.0</span>
    </div>
    <hr class="content-divider">

    @if (error()) {
      <div class="error-msg">{{ error() }}</div>
    }

    @if (!html() && !error()) {
      <div class="spinner-wrap">
        <mat-spinner></mat-spinner>
      </div>
    }

    @if (html()) {
      <div [innerHTML]="html()" class="user-manual"></div>
    }
  </div>
</div>
`,
  styles: [`
    /* Escape layout__content padding (24px top/sides, 48px bottom = 72px vertical total) */
    :host { display: block; margin: -24px -24px -48px; height: calc(100% + 72px); overflow: hidden; }
    .user-manual h1 { font-size: 1.6rem; font-weight: 700; margin: 32px 0 12px; }
    .user-manual h2 { font-size: 1.25rem; font-weight: 700; margin: 28px 0 8px; padding-bottom: 4px; border-bottom: 1px solid rgba(255,255,255,.08); }
    .user-manual h3 { font-size: 1.05rem; font-weight: 700; margin: 20px 0 6px; }
    .user-manual p  { line-height: 1.7; margin-bottom: 12px; opacity: .75; }
    .user-manual ul, .user-manual ol { padding-left: 24px; margin-bottom: 12px; }
    .user-manual li { line-height: 1.6; margin-bottom: 4px; opacity: .75; }
    .user-manual code { font-family: monospace; font-size: .82rem; background: rgba(255,255,255,.08); padding: 1px 5px; border-radius: 3px; color: #9DC3E6; }
    .user-manual pre { background: rgba(0,0,0,.3); border: 1px solid rgba(255,255,255,.1); border-radius: 6px; padding: 16px; overflow: auto; margin-bottom: 16px; }
    .user-manual pre code { background: transparent; color: inherit; }
    .user-manual table { border-collapse: collapse; width: 100%; margin-bottom: 16px; font-size: .82rem; }
    .user-manual th { text-align: left; padding: 6px 12px; border-bottom: 2px solid rgba(255,255,255,.1); font-size: .75rem; font-weight: 600; opacity: .6; text-transform: uppercase; }
    .user-manual td { padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,.06); opacity: .75; }
    .user-manual blockquote { border-left: 3px solid #4472C4; padding-left: 16px; margin: 16px 0; font-style: italic; opacity: .7; }
    .user-manual a { color: #9DC3E6; text-decoration: none; }
    .user-manual a:hover { text-decoration: underline; }
    .user-manual hr { border: none; border-top: 1px solid rgba(255,255,255,.08); margin: 24px 0; }
    .user-manual strong { font-weight: 700; }

    /* ── Layout ── */
    /* Escape layout__content's 24px/48px padding so help fills edge-to-edge */
    .help-layout { display: flex; height: 100%; overflow: hidden; }

    .toc-sidebar {
      width: 260px;
      flex-shrink: 0;
      display: flex;
      flex-direction: column;
      border-right: 1px solid var(--mat-sys-outline-variant);
      overflow: hidden;
      transition: width 0.2s ease;
    }
    .toc-sidebar--collapsed { width: 48px; }

    .toc-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 12px 4px 4px 16px;
      flex-shrink: 0;
    }
    .toc-sidebar--collapsed .toc-header { justify-content: center; padding: 12px 0 4px; }

    .toc-label {
      font-size: .65rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: .1em;
      opacity: .4;
    }
    .toc-toggle-btn { flex-shrink: 0; }

    .toc-nav { padding: 0 8px 16px; overflow-y: auto; flex: 1; }

    /* Section header (H1) — mirrors .nav-group__header from sidebar */
    .toc-sec-hdr {
      display: flex; align-items: center; gap: 8px;
      width: calc(100% - 8px); margin: 0 4px 1px;
      padding: 5px 10px; border-radius: 6px;
      background: none; border: none;
      color: var(--mat-sys-on-surface-variant);
      cursor: pointer; user-select: none;
      transition: background 0.12s;
    }
    .toc-sec-hdr:hover { background: rgba(255,255,255,0.06); }
    .toc-sec-hdr--active { background: color-mix(in srgb, var(--mat-sys-primary) 11%, transparent); }

    .toc-sec-lbl {
      flex: 1; font-size: 0.8rem; font-weight: 500;
      letter-spacing: 0.01em; white-space: nowrap;
      overflow: hidden; text-overflow: ellipsis;
    }

    /* Arrow — mirrors .nav-group__arrow: collapsed = -90deg, open = 0deg */
    .toc-sec-chevron {
      font-size: 14px; width: 14px; height: 14px; flex-shrink: 0;
      color: var(--mat-sys-on-surface-variant);
      transition: transform 0.2s;
      transform: rotate(-90deg);
    }
    .toc-sec-chevron--open { transform: rotate(0deg); }

    /* H2 / H3 leaf entries — mirrors .nav-item indented */
    .toc-entry {
      display: block;
      padding: 5px 12px; border-radius: 6px; margin: 0 4px 1px;
      font-size: 0.8rem; color: var(--mat-sys-on-surface-variant);
      cursor: pointer; user-select: none;
      white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
      transition: background 0.12s, color 0.12s;
      border-left: 2px solid transparent;
    }
    .toc-entry:hover { background: rgba(255,255,255,0.06); color: var(--mat-sys-on-surface); }
    .content-area {
      flex: 1;
      overflow-y: auto;
      padding: 32px 40px;
    }
    .content-header { display: flex; align-items: center; gap: 8px; margin-bottom: 16px; }
    .content-title { margin: 0; font-weight: 700; }
    .content-version { font-size: .72rem; opacity: .4; margin-top: 4px; }
    .content-divider { border: none; border-top: 1px solid rgba(255,255,255,.08); margin-bottom: 24px; }
    .error-msg {
      color: #f44336;
      padding: 12px;
      background: rgba(244,67,54,.1);
      border-radius: 6px;
      margin-bottom: 16px;
    }
    .spinner-wrap { display: flex; justify-content: center; padding: 64px; }
  `],
})
export class HelpComponent {
  private http      = inject(HttpClient)
  private router    = inject(Router)
  private sanitizer = inject(DomSanitizer)

  toc          = signal<TocEntry[]>([])
  html         = signal<SafeHtml>('')
  error        = signal<string | null>(null)
  activeId     = signal<string>('')
  tocCollapsed = signal(false)

  // Group flat toc entries into accordion sections (H2 = chapter/section, H3 = children)
  // H1 is the document title — shown separately, not part of accordion
  sections = computed(() => {
    const result: Array<{ entry: TocEntry; children: TocEntry[] }> = []
    for (const entry of this.toc()) {
      if (entry.level === 2) result.push({ entry, children: [] })
      else if (entry.level === 3 && result.length > 0) result[result.length - 1].children.push(entry)
    }
    return result
  })

  expandedSections = signal<Set<string>>(new Set())

  readonly contentArea = viewChild<ElementRef<HTMLDivElement>>('contentArea')

  constructor() {
    firstValueFrom(this.http.get('/docs/user-manual.md', { responseType: 'text' }))
      .then(text => {
        this.toc.set(extractToc(text))
        // bypassSecurityTrustHtml: we own the HTML (generated from markdown),
        // ensures id and style attributes survive Angular's sanitizer
        this.html.set(this.sanitizer.bypassSecurityTrustHtml(markdownToHtml(text)))
        setTimeout(() => {
          const hash = window.location.hash.replace('#', '')
          if (hash) this.scrollTo(hash)
          this.setupObserver()
        }, 150)
      })
      .catch(e => this.error.set(`Failed to load manual: ${e.message}`))
  }

  // Click on H1 section header: expand + scroll if was collapsed, collapse if was open
  onSectionClick(id: string): void {
    const wasExpanded = this.expandedSections().has(id)
    this.toggleSection(id)
    if (!wasExpanded) this.scrollTo(id)
  }

  toggleSection(id: string): void {
    this.expandedSections.update(s => {
      const n = new Set(s)
      n.has(id) ? n.delete(id) : n.add(id)
      return n
    })
  }

  private expandSectionForId(id: string): void {
    const parent = this.sections().find(s =>
      s.entry.id === id || s.children.some(c => c.id === id)
    )
    if (parent) {
      this.expandedSections.update(s =>
        s.has(parent.entry.id) ? s : new Set([...s, parent.entry.id])
      )
    }
  }

  scrollTo(id: string): void {
    this.activeId.set(id)
    this.expandSectionForId(id)
    this.router.navigate([], { fragment: id, replaceUrl: true })
    const container = this.contentArea()?.nativeElement
    if (!container) return
    const el = container.querySelector<HTMLElement>(`[id="${id}"]`)
    if (!el) return
    const top = container.scrollTop
      + el.getBoundingClientRect().top
      - container.getBoundingClientRect().top
      - 24
    container.scrollTo({ top: Math.max(0, top), behavior: 'smooth' })
  }

  private setupObserver(): void {
    const container = this.contentArea()?.nativeElement
    if (!container) return
    const observer = new IntersectionObserver(
      entries => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            this.activeId.set(entry.target.id)
            this.expandSectionForId(entry.target.id)
          }
        }
      },
      { root: container, rootMargin: '-10% 0px -80% 0px' }
    )
    container.querySelectorAll<HTMLElement>('h1[id], h2[id], h3[id]')
      .forEach(h => observer.observe(h))
  }
}
