import { Injectable, signal } from '@angular/core'

export type ThemeMode = 'dark' | 'light'

@Injectable({ providedIn: 'root' })
export class ThemeService {
  readonly mode = signal<ThemeMode>(
    (localStorage.getItem('themeMode') as ThemeMode) ?? 'dark'
  )

  applyStoredTheme(): void {
    this._apply(this.mode())
  }

  isDark(): boolean { return this.mode() === 'dark' }

  toggle(): void {
    const next: ThemeMode = this.mode() === 'dark' ? 'light' : 'dark'
    this.mode.set(next)
    localStorage.setItem('themeMode', next)
    this._apply(next)
  }

  private _apply(mode: ThemeMode): void {
    const html = document.documentElement
    if (mode === 'light') {
      html.setAttribute('data-theme', 'light')
      html.style.colorScheme = 'light'
    } else {
      html.removeAttribute('data-theme')
      html.style.colorScheme = 'dark'
    }
  }
}
