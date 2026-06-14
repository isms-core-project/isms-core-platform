import { Component, inject, OnInit } from '@angular/core'
import { RouterOutlet } from '@angular/router'
import { ThemeService } from './core/services/theme.service'

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  template: `<router-outlet />`,
})
export class App implements OnInit {
  private theme = inject(ThemeService)

  ngOnInit() {
    this.theme.applyStoredTheme()
  }
}
