import { Component, OnInit, input, signal } from '@angular/core'
import { MatCardModule } from '@angular/material/card'
import { MatIconModule } from '@angular/material/icon'
import { MatButtonModule } from '@angular/material/button'
import { MatTooltipModule } from '@angular/material/tooltip'
import { animate, state, style, transition, trigger } from '@angular/animations'

@Component({
  selector: 'app-expandable-card',
  standalone: true,
  imports: [MatCardModule, MatIconModule, MatButtonModule, MatTooltipModule],
  animations: [
    trigger('expandCollapse', [
      state('expanded', style({ height: '*', opacity: 1, overflow: 'hidden' })),
      state('collapsed', style({ height: '0px', opacity: 0, overflow: 'hidden' })),
      transition('expanded <=> collapsed', animate('180ms ease-in-out')),
    ]),
  ],
  template: `
    <mat-card class="ec-card">
      <div class="ec-header"
        [class.ec-header--clickable]="expandable()"
        [attr.tabindex]="expandable() ? 0 : null"
        (click)="expandable() && toggle()"
        (keydown.enter)="expandable() && toggle()">
        <div class="ec-title">
          <ng-content select="[card-title]" />
        </div>
        <div class="ec-actions">
          <ng-content select="[card-actions]" />
          @if (expandable()) {
            <button mat-icon-button class="ec-expand-btn"
              [matTooltip]="expanded() ? 'Collapse' : 'Expand'"
              (click)="$event.stopPropagation(); toggle()">
              <mat-icon>{{ expanded() ? 'expand_less' : 'expand_more' }}</mat-icon>
            </button>
          }
        </div>
      </div>

      <div [@expandCollapse]="expanded() ? 'expanded' : 'collapsed'">
        <mat-card-content class="ec-content">
          <ng-content />
        </mat-card-content>
      </div>
    </mat-card>
  `,
  styles: [`
    .ec-card { }

    .ec-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 16px;
    }
    .ec-header--clickable {
      cursor: pointer;
      border-radius: 12px 12px 0 0;
    }
    .ec-header--clickable:hover {
      background: rgba(255,255,255,0.02);
    }

    .ec-title {
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--mat-sys-on-surface);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .ec-actions {
      display: flex;
      align-items: center;
      gap: 4px;
    }

    .ec-expand-btn { opacity: 0.6; }
    .ec-expand-btn:hover { opacity: 1; }

    .ec-content { padding-top: 0 !important; }
  `],
})
export class ExpandableCardComponent implements OnInit {
  expandable = input(false)
  initiallyExpanded = input(true)

  private _expanded = signal(true)
  readonly expanded = this._expanded.asReadonly()

  ngOnInit(): void {
    this._expanded.set(this.initiallyExpanded())
  }

  toggle(): void { this._expanded.update(v => !v) }
}
