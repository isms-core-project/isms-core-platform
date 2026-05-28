import { Component, input } from '@angular/core'
import { MatCardModule } from '@angular/material/card'
import { MatProgressBarModule } from '@angular/material/progress-bar'
import { MatIconModule } from '@angular/material/icon'

@Component({
  selector: 'app-metric-card',
  standalone: true,
  imports: [MatCardModule, MatProgressBarModule, MatIconModule],
  template: `
    <mat-card class="metric-card">
      <mat-card-content>
        <div class="metric-card__header">
          <span class="metric-card__label">{{ title() }}</span>
          @if (icon()) {
            <mat-icon class="metric-card__icon">{{ icon() }}</mat-icon>
          }
        </div>
        <div class="metric-card__value">{{ value() }}</div>
        @if (subtitle()) {
          <div class="metric-card__subtitle">{{ subtitle() }}</div>
        }
        @if (progress() !== undefined) {
          <mat-progress-bar
            mode="determinate"
            [value]="progress()!"
            [color]="progressColor()"
            class="metric-card__progress"
          />
        }
      </mat-card-content>
    </mat-card>
  `,
  styles: [`
    .metric-card { height: 100%; }
    mat-card-content { padding-bottom: 12px !important; }
    .metric-card__header {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 4px;
      margin-bottom: 8px;
      overflow: hidden;
    }
    .metric-card__label {
      font-size: 0.7rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--mat-sys-on-surface-variant);
      min-width: 0;
      overflow: hidden;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      line-height: 1.2;
    }
    .metric-card__icon {
      color: var(--mat-sys-primary);
      opacity: 0.7;
      font-size: 18px;
      width: 18px;
      height: 18px;
      line-height: 18px;
      flex-shrink: 0;
    }
    .metric-card__value {
      font-size: 2rem;
      font-weight: 500;
      color: var(--mat-sys-on-surface);
    }
    .metric-card__subtitle {
      font-size: 0.7rem;
      color: var(--mat-sys-on-surface-variant);
      margin-top: 4px;
    }
    .metric-card__progress {
      margin-top: 8px;
      border-radius: 2px;
    }
  `],
})
export class MetricCardComponent {
  title = input.required<string>()
  value = input.required<string | number>()
  subtitle = input<string>('')
  icon = input<string>('')
  progress = input<number | undefined>(undefined)
  progressColor = input<'primary' | 'accent' | 'warn'>('primary')
}
