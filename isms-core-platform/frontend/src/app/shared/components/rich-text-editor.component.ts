import {
  Component, Input, Output, EventEmitter, OnInit, OnDestroy,
  ViewEncapsulation, ChangeDetectionStrategy,
} from '@angular/core'
import { Editor } from '@tiptap/core'
import StarterKit from '@tiptap/starter-kit'
import { Table } from '@tiptap/extension-table'
import { TableCell } from '@tiptap/extension-table-cell'
import { TableHeader } from '@tiptap/extension-table-header'
import { TableRow } from '@tiptap/extension-table-row'
import { Markdown } from '@tiptap/markdown'
import { TiptapEditorDirective } from 'ngx-tiptap'
import { MatIconModule } from '@angular/material/icon'
import { MatButtonModule } from '@angular/material/button'
import { MatTooltipModule } from '@angular/material/tooltip'
import { MatDividerModule } from '@angular/material/divider'

@Component({
  selector: 'app-rich-text-editor',
  standalone: true,
  imports: [TiptapEditorDirective, MatIconModule, MatButtonModule, MatTooltipModule, MatDividerModule],
  encapsulation: ViewEncapsulation.None,
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <div class="rte-wrap">
      <!-- Toolbar -->
      <div class="rte-toolbar">
        <button mat-icon-button type="button" matTooltip="Bold (Ctrl+B)"
          [class.rte-btn--active]="editor.isActive('bold')"
          (click)="editor.chain().focus().toggleBold().run()">
          <mat-icon>format_bold</mat-icon>
        </button>
        <button mat-icon-button type="button" matTooltip="Italic (Ctrl+I)"
          [class.rte-btn--active]="editor.isActive('italic')"
          (click)="editor.chain().focus().toggleItalic().run()">
          <mat-icon>format_italic</mat-icon>
        </button>
        <button mat-icon-button type="button" matTooltip="Strikethrough"
          [class.rte-btn--active]="editor.isActive('strike')"
          (click)="editor.chain().focus().toggleStrike().run()">
          <mat-icon>format_strikethrough</mat-icon>
        </button>
        <button mat-icon-button type="button" matTooltip="Code"
          [class.rte-btn--active]="editor.isActive('code')"
          (click)="editor.chain().focus().toggleCode().run()">
          <mat-icon>code</mat-icon>
        </button>

        <mat-divider vertical class="toolbar-divider" />

        <button mat-icon-button type="button" matTooltip="Heading 1"
          [class.rte-btn--active]="editor.isActive('heading', {level:1})"
          (click)="editor.chain().focus().toggleHeading({level:1}).run()">
          <mat-icon>format_h1</mat-icon>
        </button>
        <button mat-icon-button type="button" matTooltip="Heading 2"
          [class.rte-btn--active]="editor.isActive('heading', {level:2})"
          (click)="editor.chain().focus().toggleHeading({level:2}).run()">
          <mat-icon>format_h2</mat-icon>
        </button>
        <button mat-icon-button type="button" matTooltip="Heading 3"
          [class.rte-btn--active]="editor.isActive('heading', {level:3})"
          (click)="editor.chain().focus().toggleHeading({level:3}).run()">
          <mat-icon>format_h3</mat-icon>
        </button>

        <mat-divider vertical class="toolbar-divider" />

        <button mat-icon-button type="button" matTooltip="Bullet list"
          [class.rte-btn--active]="editor.isActive('bulletList')"
          (click)="editor.chain().focus().toggleBulletList().run()">
          <mat-icon>format_list_bulleted</mat-icon>
        </button>
        <button mat-icon-button type="button" matTooltip="Ordered list"
          [class.rte-btn--active]="editor.isActive('orderedList')"
          (click)="editor.chain().focus().toggleOrderedList().run()">
          <mat-icon>format_list_numbered</mat-icon>
        </button>
        <button mat-icon-button type="button" matTooltip="Block quote"
          [class.rte-btn--active]="editor.isActive('blockquote')"
          (click)="editor.chain().focus().toggleBlockquote().run()">
          <mat-icon>format_quote</mat-icon>
        </button>
        <button mat-icon-button type="button" matTooltip="Code block"
          [class.rte-btn--active]="editor.isActive('codeBlock')"
          (click)="editor.chain().focus().toggleCodeBlock().run()">
          <mat-icon>data_object</mat-icon>
        </button>

        <mat-divider vertical class="toolbar-divider" />

        <button mat-icon-button type="button" matTooltip="Undo (Ctrl+Z)"
          [disabled]="!editor.can().undo()"
          (click)="editor.chain().focus().undo().run()">
          <mat-icon>undo</mat-icon>
        </button>
        <button mat-icon-button type="button" matTooltip="Redo (Ctrl+Y)"
          [disabled]="!editor.can().redo()"
          (click)="editor.chain().focus().redo().run()">
          <mat-icon>redo</mat-icon>
        </button>
      </div>

      <!-- Editor area -->
      <div class="rte-editor-wrap">
        <tiptap-editor [editor]="editor" outputFormat="html" />
      </div>
    </div>
  `,
  styles: [`
    .rte-wrap {
      border: 1px solid var(--mat-sys-outline-variant);
      border-radius: 8px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }

    .rte-toolbar {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 2px;
      padding: 4px 8px;
      border-bottom: 1px solid var(--mat-sys-outline-variant);
      background: var(--mat-sys-surface-container);
    }

    .rte-toolbar .mat-mdc-icon-button {
      width: 32px;
      height: 32px;
      line-height: 32px;
      --mdc-icon-button-state-layer-size: 32px;
    }

    .rte-toolbar .mat-mdc-icon-button .mat-icon {
      font-size: 18px;
      width: 18px;
      height: 18px;
    }

    .toolbar-divider { height: 24px; margin: 0 4px; }

    .rte-btn--active {
      color: var(--mat-sys-primary) !important;
      background: color-mix(in srgb, var(--mat-sys-primary) 12%, transparent) !important;
      border-radius: 4px;
    }

    .rte-editor-wrap {
      flex: 1;
      overflow-y: auto;
      padding: 16px;
      background: var(--mat-sys-surface);
      min-height: 400px;
    }

    /* ProseMirror content styles */
    .ProseMirror {
      outline: none;
      font-size: 0.875rem;
      line-height: 1.7;
      color: var(--mat-sys-on-surface);
      min-height: 380px;
    }

    .ProseMirror > * + * { margin-top: 0.75em; }

    .ProseMirror h1, .ProseMirror h2, .ProseMirror h3,
    .ProseMirror h4, .ProseMirror h5, .ProseMirror h6 {
      line-height: 1.3;
      margin-top: 1.2em;
      margin-bottom: 0.4em;
      color: var(--mat-sys-on-surface);
    }
    .ProseMirror h1 { font-size: 1.5rem; font-weight: 700; }
    .ProseMirror h2 { font-size: 1.25rem; font-weight: 700; }
    .ProseMirror h3 { font-size: 1.1rem; font-weight: 600; }

    .ProseMirror p { margin: 0; }
    .ProseMirror p + p { margin-top: 0.6em; }

    .ProseMirror ul, .ProseMirror ol {
      padding-left: 1.4em;
      margin: 0.5em 0;
    }
    .ProseMirror li { margin: 0.2em 0; }

    .ProseMirror blockquote {
      border-left: 3px solid var(--mat-sys-primary);
      padding-left: 1em;
      margin: 0.75em 0;
      color: var(--mat-sys-on-surface-variant);
      font-style: italic;
    }

    .ProseMirror code {
      background: rgba(255,255,255,0.08);
      border-radius: 3px;
      padding: 0.1em 0.3em;
      font-family: 'Roboto Mono', monospace;
      font-size: 0.85em;
    }

    .ProseMirror pre {
      background: rgba(0,0,0,0.3);
      border-radius: 6px;
      padding: 12px 16px;
      overflow-x: auto;
      margin: 0.75em 0;
    }
    .ProseMirror pre code {
      background: none;
      padding: 0;
      font-size: 0.82rem;
      color: var(--mat-sys-on-surface);
    }

    .ProseMirror hr {
      border: none;
      border-top: 1px solid var(--mat-sys-outline-variant);
      margin: 1em 0;
    }

    .ProseMirror table {
      border-collapse: collapse;
      width: 100%;
      margin: 0.75em 0;
    }
    .ProseMirror th, .ProseMirror td {
      border: 1px solid rgba(255,255,255,0.12);
      padding: 6px 10px;
      font-size: 0.82rem;
    }
    .ProseMirror th {
      background: rgba(255,255,255,0.05);
      font-weight: 600;
    }

    .ProseMirror .selectedCell:after {
      background: rgba(50,125,244,0.15);
      content: "";
      inset: 0;
      pointer-events: none;
      position: absolute;
      z-index: 2;
    }

    .ProseMirror p.is-editor-empty:first-child::before {
      content: attr(data-placeholder);
      color: var(--mat-sys-on-surface-variant);
      float: left;
      height: 0;
      pointer-events: none;
    }
  `],
})
export class RichTextEditorComponent implements OnInit, OnDestroy {
  @Input() set value(v: string) {
    if (this._lastEmitted === v) return
    if (this.editor && v !== undefined) {
      this.editor.commands.setContent(v ?? '')
    }
    this._initValue = v
  }
  @Output() valueChange = new EventEmitter<string>()

  private _initValue = ''
  private _lastEmitted = ''

  editor!: Editor

  ngOnInit(): void {
    this.editor = new Editor({
      extensions: [
        StarterKit,
        Markdown,
        Table.configure({ resizable: false }),
        TableRow,
        TableHeader,
        TableCell,
      ],
      content: this._initValue,
      onUpdate: ({ editor }) => {
        const md = editor.getMarkdown()
        if (md !== this._lastEmitted) {
          this._lastEmitted = md
          this.valueChange.emit(md)
        }
      },
    })
  }

  ngOnDestroy(): void {
    this.editor?.destroy()
  }
}
