import { Component, input } from '@angular/core'

@Component({
  selector: 'app-page-header',
  standalone: true,
  imports: [],
  template: `
    <div class="page-header">
      <div class="page-header__left">
        <h4 class="page-header__title">{{ title() }}</h4>
        @if (subtitle()) {
          <p class="page-header__subtitle">{{ subtitle() }}</p>
        }
      </div>
      <div class="page-header__actions">
        <ng-content select="[actions]" />
      </div>
    </div>
  `,
  styles: [`
    .page-header {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      margin-bottom: 24px;
    }
    .page-header__title {
      margin: 0;
      font-size: 1.2rem;
      font-weight: 500;
      color: var(--mat-sys-on-surface);
    }
    .page-header__subtitle {
      margin: 4px 0 0;
      font-size: 0.875rem;
      color: var(--mat-sys-on-surface-variant);
    }
    .page-header__actions {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-shrink: 0;
    }
  `],
})
export class PageHeaderComponent {
  title = input.required<string>()
  subtitle = input<string>('')
}
