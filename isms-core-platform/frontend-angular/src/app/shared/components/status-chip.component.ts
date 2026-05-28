import { Component, input, inject } from '@angular/core'
import { ThemeService } from '../../core/services/theme.service'

const DARK: Record<string, { bg: string; color: string }> = {
  // green family
  green:         { bg: '#1a3a27', color: '#C6EFCE' },
  compliant:     { bg: '#1a3a27', color: '#C6EFCE' },
  closed:        { bg: '#1a3a27', color: '#C6EFCE' },
  complete:      { bg: '#1a3a27', color: '#C6EFCE' },
  approved:      { bg: '#1a3a27', color: '#C6EFCE' },
  active:        { bg: '#1a3a27', color: '#C6EFCE' },
  // amber family
  amber:         { bg: '#3d3200', color: '#FFEB9C' },
  partial:       { bg: '#3d3200', color: '#FFEB9C' },
  accepted:      { bg: '#3d3200', color: '#FFEB9C' },
  in_treatment:  { bg: '#3d3200', color: '#FFEB9C' },
  in_progress:   { bg: '#3d3200', color: '#FFEB9C' },
  pending_review:{ bg: '#3d3200', color: '#FFEB9C' },
  basic:         { bg: '#3d3200', color: '#FFEB9C' },
  draft:         { bg: '#1a1f30', color: '#8B9CC8' },
  // red family
  red:           { bg: '#3a0000', color: '#FFC7CE' },
  open:          { bg: '#3a0000', color: '#FFC7CE' },
  non_compliant: { bg: '#3a0000', color: '#FFC7CE' },
  critical:      { bg: '#3a0000', color: '#FFC7CE' },
  rejected:      { bg: '#3a0000', color: '#FFC7CE' },
  incomplete:    { bg: '#3a0000', color: '#FFC7CE' },
  // severity
  very_high:     { bg: '#3a0000', color: '#FFC7CE' },
  high:          { bg: '#3a1a00', color: '#FFDDC7' },
  medium:        { bg: '#3d3200', color: '#FFEB9C' },
  low:           { bg: '#1a2d1a', color: '#B8E0B8' },
  // neutral / not started
  not_assessed:  { bg: '#1a1f30', color: '#8B9CC8' },
  not_started:   { bg: '#1a1f30', color: '#8B9CC8' },
  // feed statuses
  success:       { bg: '#1a3a27', color: '#C6EFCE' },
  running:       { bg: '#1a2d3a', color: '#90CAF9' },
  never_run:     { bg: '#1a1f30', color: '#8B9CC8' },
  error:         { bg: '#3a0000', color: '#FFC7CE' },
}

const LIGHT: Record<string, { bg: string; color: string }> = {
  // green family
  green:         { bg: 'rgba(46,125,50,0.15)',  color: '#1b5e20' },
  compliant:     { bg: 'rgba(46,125,50,0.15)',  color: '#1b5e20' },
  closed:        { bg: 'rgba(46,125,50,0.15)',  color: '#1b5e20' },
  complete:      { bg: 'rgba(46,125,50,0.15)',  color: '#1b5e20' },
  approved:      { bg: 'rgba(46,125,50,0.15)',  color: '#1b5e20' },
  active:        { bg: 'rgba(46,125,50,0.15)',  color: '#1b5e20' },
  // amber family
  amber:         { bg: 'rgba(230,145,0,0.15)',  color: '#7a4800' },
  partial:       { bg: 'rgba(230,145,0,0.15)',  color: '#7a4800' },
  accepted:      { bg: 'rgba(230,145,0,0.15)',  color: '#7a4800' },
  in_treatment:  { bg: 'rgba(230,145,0,0.15)',  color: '#7a4800' },
  in_progress:   { bg: 'rgba(230,145,0,0.15)',  color: '#7a4800' },
  pending_review:{ bg: 'rgba(230,145,0,0.15)',  color: '#7a4800' },
  basic:         { bg: 'rgba(230,145,0,0.15)',  color: '#7a4800' },
  draft:         { bg: 'rgba(68,114,196,0.12)', color: '#2E5099' },
  // red family
  red:           { bg: 'rgba(192,0,0,0.12)',    color: '#9e0000' },
  open:          { bg: 'rgba(192,0,0,0.12)',    color: '#9e0000' },
  non_compliant: { bg: 'rgba(192,0,0,0.12)',    color: '#9e0000' },
  critical:      { bg: 'rgba(192,0,0,0.12)',    color: '#9e0000' },
  rejected:      { bg: 'rgba(192,0,0,0.12)',    color: '#9e0000' },
  incomplete:    { bg: 'rgba(192,0,0,0.12)',    color: '#9e0000' },
  // severity
  very_high:     { bg: 'rgba(192,0,0,0.12)',    color: '#9e0000' },
  high:          { bg: 'rgba(200,80,0,0.12)',   color: '#7a2800' },
  medium:        { bg: 'rgba(230,145,0,0.12)',  color: '#7a4800' },
  low:           { bg: 'rgba(46,125,50,0.1)',   color: '#2e7d32' },
  // neutral / not started
  not_assessed:  { bg: 'rgba(68,114,196,0.12)', color: '#2E5099' },
  not_started:   { bg: 'rgba(68,114,196,0.12)', color: '#2E5099' },
  // feed statuses
  success:       { bg: 'rgba(46,125,50,0.15)',  color: '#1b5e20' },
  running:       { bg: 'rgba(21,101,192,0.15)', color: '#1565c0' },
  never_run:     { bg: 'rgba(68,114,196,0.12)', color: '#2E5099' },
  error:         { bg: 'rgba(192,0,0,0.12)',    color: '#9e0000' },
}

@Component({
  selector: 'app-status-chip',
  standalone: true,
  template: `
    <span class="status-chip" [style.background]="colors.bg" [style.color]="colors.color" [style.border-color]="colors.color + '50'">
      {{ label }}
    </span>
  `,
  styles: [`
    .status-chip {
      display: inline-flex;
      align-items: center;
      padding: 0 8px;
      height: 20px;
      border-radius: 10px;
      border: 1px solid;
      font-size: 0.7rem;
      font-weight: 600;
      text-transform: capitalize;
      white-space: nowrap;
    }
  `],
})
export class StatusChipComponent {
  status = input.required<string>()
  private theme = inject(ThemeService)

  get label() { return this.status().replace(/_/g, ' ') }

  get colors() {
    const map = this.theme.isDark() ? DARK : LIGHT
    const key = this.status()
    const fallback = this.theme.isDark()
      ? { bg: '#1a1f30', color: '#8B9CC8' }
      : { bg: 'rgba(68,114,196,0.12)', color: '#2E5099' }
    return map[key] ?? fallback
  }
}
