import { createContext, useContext, useEffect, useState } from 'react'
import { projectsApi, type ProjectRead } from '../api/projectsApi'

// Keyed by UPPERCASE product family: ISMS | PRIVACY | CLOUD | SEC
type ActiveProjectsMap = Record<string, ProjectRead | null>

interface ProjectContextValue {
  getActiveProject: (family: string) => ProjectRead | null
  setActiveProject: (family: string, project: ProjectRead | null) => void
  activeProjectsMap: ActiveProjectsMap   // all active projects by family
  // Backward-compat helpers used by components that don't need per-family resolution
  activeProjectId: string | null
  activeProject: ProjectRead | null
}

const ProjectContext = createContext<ProjectContextValue>({
  getActiveProject: () => null,
  setActiveProject: () => {},
  activeProjectsMap: {},
  activeProjectId: null,
  activeProject: null,
})

const STORAGE_KEY = 'isms_active_projects'

function loadStored(): ActiveProjectsMap {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    return raw ? (JSON.parse(raw) as ActiveProjectsMap) : {}
  } catch {
    return {}
  }
}

export function ProjectProvider({ children }: { children: React.ReactNode }) {
  const [activeProjects, setActiveProjectsState] = useState<ActiveProjectsMap>(loadStored)

  // Validate stored projects still exist in DB on mount
  useEffect(() => {
    const stored = loadStored()
    const families = Object.keys(stored)
    if (!families.length) return

    families.forEach(family => {
      const p = stored[family]
      if (!p) return
      projectsApi.get(p.id).catch(() => {
        setActiveProjectsState(prev => {
          const next = { ...prev }
          delete next[family]
          localStorage.setItem(STORAGE_KEY, JSON.stringify(next))
          return next
        })
      })
    })
  }, [])

  function getActiveProject(family: string): ProjectRead | null {
    return activeProjects[family.toUpperCase()] ?? null
  }

  function setActiveProject(family: string, project: ProjectRead | null) {
    const key = family.toUpperCase()
    setActiveProjectsState(prev => {
      const next = { ...prev }
      if (project) {
        next[key] = project
      } else {
        delete next[key]
      }
      localStorage.setItem(STORAGE_KEY, JSON.stringify(next))
      return next
    })
  }

  // Backward-compat: expose ISMS project as the "default" active project
  const ismsProject = activeProjects['ISMS'] ?? null

  return (
    <ProjectContext.Provider value={{
      getActiveProject,
      setActiveProject,
      activeProjectsMap: activeProjects,
      activeProjectId: ismsProject?.id ?? null,
      activeProject: ismsProject,
    }}>
      {children}
    </ProjectContext.Provider>
  )
}

export function useProject() {
  return useContext(ProjectContext)
}
