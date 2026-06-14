import { Injectable, inject, signal, computed } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { ProjectRead } from '../../shared/types'

type ActiveProjectsMap = Record<string, ProjectRead | null>
const STORAGE_KEY = 'isms_active_projects'

function loadStored(): ActiveProjectsMap {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    return raw ? JSON.parse(raw) : {}
  } catch { return {} }
}

@Injectable({ providedIn: 'root' })
export class ProjectService {
  private http = inject(HttpClient)
  private _map = signal<ActiveProjectsMap>(loadStored())

  readonly activeProjectsMap = computed(() => this._map())

  readonly activeProject   = computed(() => this._map()['ISMS'] ?? null)
  readonly activeProjectId = computed(() => this._map()['ISMS']?.id ?? null)

  validateStoredProjects(): void {
    const map = loadStored()
    Object.entries(map).forEach(([family, p]) => {
      if (!p) return
      this.http.get<ProjectRead>(`/api/v1/projects/${p.id}`).subscribe({
        error: () => this._removeFamily(family),
      })
    })
  }

  getActiveProject(family: string): ProjectRead | null {
    return this._map()[family.toUpperCase()] ?? null
  }

  setActiveProject(family: string, project: ProjectRead | null): void {
    const key = family.toUpperCase()
    this._map.update(m => {
      const next = { ...m }
      if (project) next[key] = project
      else delete next[key]
      localStorage.setItem(STORAGE_KEY, JSON.stringify(next))
      return next
    })
  }

  private _removeFamily(family: string): void {
    this._map.update(m => {
      const next = { ...m }
      delete next[family.toUpperCase()]
      localStorage.setItem(STORAGE_KEY, JSON.stringify(next))
      return next
    })
  }
}
