import { Component, signal, computed, inject } from '@angular/core'
import { injectQuery } from '@tanstack/angular-query-experimental'
import { HttpClient } from '@angular/common/http'
import { firstValueFrom } from 'rxjs'
import { MatIconModule } from '@angular/material/icon'
import { MatButtonModule } from '@angular/material/button'

interface HealthAlert {
  type: string
  severity: string
  message: string
  detected_at: string
  entity: string | null
}

const TYPE_LABELS: Record<string, string> = {
  feed_failure:      'Feed',
  connector_failure: 'Connector',
  opensearch_down:   'OpenSearch',
  db_error:          'Database',
}

@Component({
  selector: 'app-health-alert-banner',
  standalone: true,
  imports: [MatIconModule, MatButtonModule],
  template: `
    @if (!dismissed() && (query.data()?.length ?? 0) > 0) {
      <div class="health-banner">
        <mat-icon class="health-banner__icon">error_outline</mat-icon>
        <div class="health-banner__body">
          <div class="health-banner__title">
            {{ errorCount() }} platform health issue{{ errorCount() !== 1 ? 's' : '' }} detected in the last 24h
            @for (alert of query.data()!; track alert.type) {
              <span class="health-badge">{{ typeLabel(alert.type) }}</span>
            }
          </div>
          @if (expanded()) {
            <div class="health-banner__detail">
              @for (alert of query.data()!; track alert.type + alert.entity) {
                <div class="health-banner__row">
                  <span class="health-banner__time">{{ fmtTime(alert.detected_at) }}</span>
                  <span class="health-badge">{{ typeLabel(alert.type) }}</span>
                  <span>{{ alert.message }}</span>
                </div>
              }
            </div>
          }
        </div>
        <div class="health-banner__actions">
          <button mat-icon-button (click)="expanded.set(!expanded())">
            <mat-icon>{{ expanded() ? 'expand_less' : 'expand_more' }}</mat-icon>
          </button>
          <button mat-icon-button (click)="dismiss()">
            <mat-icon>close</mat-icon>
          </button>
        </div>
      </div>
    }
  `,
  styles: [`
    .health-banner {
      display: flex;
      align-items: flex-start;
      gap: 8px;
      padding: 8px 16px;
      background: var(--mat-sys-error-container, #4e0002);
      color: var(--mat-sys-on-error-container, #ffb4ab);
      flex-shrink: 0;
    }
    .health-banner__icon { margin-top: 2px; font-size: 18px; height: 18px; width: 18px; }
    .health-banner__body { flex: 1; font-size: 0.875rem; }
    .health-banner__title { font-weight: 600; line-height: 1.4; display: flex; align-items: center; flex-wrap: wrap; gap: 4px; }
    .health-banner__actions { display: flex; align-items: center; gap: 2px; }
    .health-banner__detail { margin-top: 6px; display: flex; flex-direction: column; gap: 4px; }
    .health-banner__row { display: flex; align-items: flex-start; gap: 8px; font-size: 0.8rem; }
    .health-banner__time { opacity: 0.7; white-space: nowrap; }
    .health-badge {
      display: inline-flex; align-items: center; padding: 0 5px; height: 16px;
      border-radius: 8px; font-size: 0.65rem; background: rgba(255,255,255,0.2); color: inherit;
    }
  `],
})
export class HealthAlertBannerComponent {
  private http = inject(HttpClient)
  dismissed = signal(
    sessionStorage.getItem('health_banner_dismissed_at') === new Date().toDateString()
  )
  expanded = signal(false)

  query = injectQuery(() => ({
    queryKey: ['health', 'alerts'],
    queryFn: () => firstValueFrom(this.http.get<HealthAlert[]>('/api/v1/health/alerts')),
    staleTime: 5 * 60_000,
    refetchInterval: 5 * 60_000,
    enabled: !this.dismissed(),
  }))

  errorCount = computed(() => (this.query.data() ?? []).filter(a => a.severity === 'error').length)

  typeLabel(type: string) { return TYPE_LABELS[type] ?? type }

  fmtTime(iso: string) {
    try { return new Date(iso).toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit' }) }
    catch { return '' }
  }

  dismiss() {
    sessionStorage.setItem('health_banner_dismissed_at', new Date().toDateString())
    this.dismissed.set(true)
  }
}
