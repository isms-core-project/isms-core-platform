import { createContext, useContext, useState, useMemo, type ReactNode } from 'react'
import { ThemeProvider, CssBaseline } from '@mui/material'
import type { PaletteMode } from '@mui/material'
import { createAppTheme } from '../theme'

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
    setMode(m => {
      const next: PaletteMode = m === 'dark' ? 'light' : 'dark'
      localStorage.setItem('themeMode', next)
      return next
    })
  }

  const theme = useMemo(() => createAppTheme(mode), [mode])

  return (
    <ThemeModeContext.Provider value={{ mode, toggleTheme }}>
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
