import { createContext, useContext, useState, useMemo, type ReactNode } from 'react'
import { ThemeProvider, CssBaseline } from '@mui/material'
import type { PaletteMode } from '@mui/material'
import { createAppTheme, createBambooTheme } from '../theme'

const SECRET_THEME = import.meta.env.VITE_SECRET_THEME

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
    if (SECRET_THEME === 'bamboo') return
    setMode(m => {
      const next: PaletteMode = m === 'dark' ? 'light' : 'dark'
      localStorage.setItem('themeMode', next)
      return next
    })
  }

  const theme = useMemo(
    () => SECRET_THEME === 'bamboo' ? createBambooTheme() : createAppTheme(mode),
    [mode]
  )

  return (
    <ThemeModeContext.Provider value={{ mode: SECRET_THEME === 'bamboo' ? 'dark' : mode, toggleTheme }}>
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
