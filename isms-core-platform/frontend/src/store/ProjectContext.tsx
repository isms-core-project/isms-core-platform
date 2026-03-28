import { createContext, useContext, useEffect, useState } from 'react'
import { projectsApi, type ProjectRead } from '../api/projectsApi'

interface ProjectContextValue {
  activeProjectId: string | null
  activeProject: ProjectRead | null
  setActiveProject: (p: ProjectRead | null) => void
}

const ProjectContext = createContext<ProjectContextValue>({
  activeProjectId: null,
  activeProject: null,
  setActiveProject: () => {},
})

export function ProjectProvider({ children }: { children: React.ReactNode }) {
  const [activeProject, setActiveProjectState] = useState<ProjectRead | null>(() => {
    try {
      const stored = localStorage.getItem('isms_active_project')
      return stored ? (JSON.parse(stored) as ProjectRead) : null
    } catch {
      return null
    }
  })

  // Validate stored project still exists in DB on mount
  useEffect(() => {
    const stored = localStorage.getItem('isms_active_project')
    if (!stored) return
    try {
      const p = JSON.parse(stored) as ProjectRead
      projectsApi.get(p.id).catch(() => {
        localStorage.removeItem('isms_active_project')
        setActiveProjectState(null)
      })
    } catch {
      localStorage.removeItem('isms_active_project')
      setActiveProjectState(null)
    }
  }, [])

  function setActiveProject(p: ProjectRead | null) {
    setActiveProjectState(p)
    if (p) {
      localStorage.setItem('isms_active_project', JSON.stringify(p))
    } else {
      localStorage.removeItem('isms_active_project')
    }
  }

  return (
    <ProjectContext.Provider value={{ activeProjectId: activeProject?.id ?? null, activeProject, setActiveProject }}>
      {children}
    </ProjectContext.Provider>
  )
}

export function useProject() {
  return useContext(ProjectContext)
}
