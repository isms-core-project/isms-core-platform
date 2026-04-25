import { createContext, useContext, useState, useMemo, type ReactNode } from 'react'
import { ThemeProvider, CssBaseline } from '@mui/material'
import type { PaletteMode } from '@mui/material'
import { createAppTheme, createAuditorTheme, createBambooTheme } from '../theme'

const SECRET_THEME = import.meta.env.VITE_SECRET_THEME
const IS_FIXED_THEME = SECRET_THEME === 'bamboo' || SECRET_THEME === 'auditor'

interface ThemeModeCtx {
  mode: PaletteMode
  toggleTheme: () => void
}

const ThemeModeContext = createContext<ThemeModeCtx>({
  mode: 'dark',
  toggleTheme: () => {},
})

export function ThemeModeProvider({ children }: { children: ReactNode }) {
  const [mode, setMode] = useState<PaletteMode>(
    () => (localStorage.getItem('themeMode') as PaletteMode) ?? 'dark'
  )

  function toggleTheme() {
    if (IS_FIXED_THEME) return
    setMode(m => {
      const next: PaletteMode = m === 'dark' ? 'light' : 'dark'
      localStorage.setItem('themeMode', next)
      return next
    })
  }

  const theme = useMemo(() => {
    if (SECRET_THEME === 'bamboo')  return createBambooTheme()
    if (SECRET_THEME === 'auditor') return createAuditorTheme()
    return createAppTheme(mode)
  }, [mode])

  return (
    <ThemeModeContext.Provider value={{ mode: IS_FIXED_THEME ? 'dark' : mode, toggleTheme }}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        {children}
      </ThemeProvider>
    </ThemeModeContext.Provider>
  )
}

export function useThemeMode() {
  return useContext(ThemeModeContext)
}
