import { Component, inject, signal, effect, ElementRef, viewChild } from '@angular/core'
import { HttpClient } from '@angular/common/http'
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
  <div class="toc-sidebar">
    <div class="toc-inner">
      <div class="toc-label">Contents</div>
      <nav>
        @for (entry of toc(); track entry.id) {
          <div class="toc-entry"
            (click)="scrollTo(entry.id)"
            [style.padding-left.px]="entry.level === 1 ? 8 : entry.level === 2 ? 16 : 24"
            [style.font-size]="entry.level === 1 ? '0.82rem' : '0.77rem'"
            [style.font-weight]="entry.level === 1 ? '600' : '400'"
            [style.background]="activeId() === entry.id ? 'rgba(68,114,196,.15)' : 'transparent'"
            [style.border-left-color]="activeId() === entry.id ? '#4472C4' : 'transparent'"
            [style.color]="activeId() === entry.id ? '#9DC3E6' : 'inherit'"
            [style.opacity]="entry.level === 1 ? 1 : 0.7">
            {{ entry.label }}
          </div>
        }
      </nav>
    </div>
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
    :host { display: flex; height: 100%; }
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
    .help-layout { display: flex; height: 100%; overflow: hidden; }
    .toc-sidebar {
      width: 260px;
      flex-shrink: 0;
      border-right: 1px solid var(--mat-sys-outline-variant);
      overflow-y: auto;
      height: 100%;
    }
    .toc-inner { padding: 16px; }
    .toc-label {
      font-size: .65rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: .1em;
      opacity: .4;
      margin-bottom: 8px;
      padding-left: 8px;
    }
    .toc-entry {
      cursor: pointer;
      padding-top: 4px;
      padding-bottom: 4px;
      border-radius: 4px;
      margin-bottom: 1px;
      border-left: 2px solid transparent;
    }
    .content-area {
      flex: 1;
      overflow-y: auto;
      padding: 32px 40px;
      max-width: 860px;
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
  private http   = inject(HttpClient)
  private router = inject(Router)

  toc      = signal<TocEntry[]>([])
  html     = signal<string>('')
  error    = signal<string | null>(null)
  activeId = signal<string>('')

  readonly contentArea = viewChild<ElementRef<HTMLDivElement>>('contentArea')

  constructor() {
    // Load markdown on init
    firstValueFrom(this.http.get('/docs/user-manual.md', { responseType: 'text' }))
      .then(text => {
        this.toc.set(extractToc(text))
        this.html.set(markdownToHtml(text))
        // scroll to hash after render
        setTimeout(() => {
          const hash = window.location.hash.replace('#', '')
          if (hash) { this.scrollTo(hash) }
          this.setupObserver()
        }, 150)
      })
      .catch(e => this.error.set(`Failed to load manual: ${e.message}`))
  }

  scrollTo(id: string): void {
    this.activeId.set(id)
    const el = document.getElementById(id)
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' })
    this.router.navigate([], { fragment: id, replaceUrl: true })
  }

  private setupObserver(): void {
    const observer = new IntersectionObserver(
      entries => {
        for (const entry of entries) {
          if (entry.isIntersecting) this.activeId.set(entry.target.id)
        }
      },
      { rootMargin: '-10% 0px -80% 0px' }
    )
    document.querySelectorAll('h1[id], h2[id], h3[id]').forEach(h => observer.observe(h))
  }
}
