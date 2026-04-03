import { createTheme, type PaletteMode } from '@mui/material/styles'

export function createAppTheme(mode: PaletteMode) {
  const isDark = mode === 'dark'

  return createTheme({
    palette: {
      mode,
      primary: {
        main: '#4472C4',
        light: '#6B97D8',
        dark: '#2E5099',
      },
      secondary: {
        main: isDark ? '#C6EFCE' : '#375623',
        dark: '#375623',
      },
      background: {
        default: isDark ? '#0A0F1E' : '#F0F2F8',
        paper:   isDark ? '#0F1629' : '#FFFFFF',
      },
      text: {
        primary:   isDark ? '#E8EAF0' : '#1C2638',
        secondary: isDark ? '#8B9CC8' : '#5568A0',
        disabled:  isDark ? 'rgba(232,234,240,0.38)' : 'rgba(28,38,56,0.38)',
      },
      error:   { main: '#C00000' },
      warning: {
        main:        isDark ? '#FFEB9C' : '#FF9800',
        contrastText: isDark ? '#7D6608' : '#FFFFFF',
      },
      success: {
        main:        isDark ? '#C6EFCE' : '#4CAF50',
        contrastText: isDark ? '#375623' : '#FFFFFF',
      },
      divider: 'rgba(68, 114, 196, 0.15)',
      action: {
        hover:    isDark ? 'rgba(68,114,196,0.08)' : 'rgba(68,114,196,0.06)',
        selected: isDark ? 'rgba(68,114,196,0.16)' : 'rgba(68,114,196,0.12)',
      },
    },
    typography: {
      fontFamily: '"Inter", "Roboto", "Helvetica Neue", sans-serif',
      h1: { fontWeight: 700, fontSize: '2rem' },
      h2: { fontWeight: 700, fontSize: '1.6rem' },
      h3: { fontWeight: 600, fontSize: '1.3rem' },
      h4: { fontWeight: 600, fontSize: '1.1rem' },
      h5: { fontWeight: 600, fontSize: '1rem' },
      h6: { fontWeight: 600, fontSize: '0.9rem' },
      body1: { fontSize: '0.875rem' },
      body2: { fontSize: '0.8rem' },
      caption: { fontSize: '0.75rem' },
    },
    shape: { borderRadius: 8 },
    components: {
      MuiCard: {
        styleOverrides: {
          root: {
            backgroundImage: 'none',
            border: '1px solid rgba(68, 114, 196, 0.12)',
          },
        },
      },
      MuiPaper: {
        styleOverrides: {
          root: { backgroundImage: 'none' },
        },
      },
      MuiChip: {
        styleOverrides: {
          root: { fontSize: '0.75rem' },
        },
      },
      MuiTableCell: {
        styleOverrides: {
          head: ({ theme }) => ({
            fontWeight: 600,
            backgroundColor: theme.palette.background.paper,
            color: theme.palette.text.secondary,
            fontSize: '0.75rem',
            textTransform: 'uppercase' as const,
            letterSpacing: '0.05em',
            borderBottom: `1px solid ${theme.palette.divider}`,
          }),
          root: ({ theme }) => ({
            borderColor: theme.palette.divider,
          }),
        },
      },
      MuiLinearProgress: {
        styleOverrides: {
          root: { borderRadius: 4, height: 6 },
        },
      },
      MuiDrawer: {
        styleOverrides: {
          paper: ({ theme }) => ({
            backgroundImage: 'none',
            backgroundColor: theme.palette.background.paper,
            borderColor: theme.palette.divider,
          }),
        },
      },
      MuiDialog: {
        styleOverrides: {
          paper: { backgroundImage: 'none' },
        },
      },
      MuiInputBase: {
        styleOverrides: {
          input: ({ theme }) => ({
            '&:-webkit-autofill, &:-webkit-autofill:hover, &:-webkit-autofill:focus, &:-webkit-autofill:active': {
              WebkitBoxShadow: `0 0 0 100px ${theme.palette.background.paper} inset`,
              WebkitTextFillColor: theme.palette.text.primary,
              caretColor: theme.palette.text.primary,
            },
          }),
        },
      },
      MuiAlert: {
        styleOverrides: {
          root: { fontSize: '0.82rem' },
        },
      },
      MuiTooltip: {
        styleOverrides: {
          tooltip: ({ theme }) => ({
            backgroundColor: theme.palette.mode === 'dark'
              ? 'rgba(30,40,80,0.96)'
              : 'rgba(28,38,56,0.92)',
            fontSize: '0.75rem',
          }),
        },
      },
    },
  })
}

// Keep a default export for backward compatibility during migration
export const theme = createAppTheme('dark')
