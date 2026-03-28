import { createContext, useContext, useState } from 'react'
import type { ProjectRead } from '../api/projectsApi'

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
