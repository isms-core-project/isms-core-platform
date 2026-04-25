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

export function createBambooTheme() {
  return createTheme({
    palette: {
      mode: 'dark',
      primary: {
        main:  '#2E8B57',
        light: '#3da369',
        dark:  '#246b45',
      },
      secondary: {
        main: '#4ade80',
        dark: '#22c55e',
      },
      background: {
        default: '#0a0f0d',
        paper:   '#141e19',
      },
      text: {
        primary:   '#e8efe9',
        secondary: '#9ca89e',
        disabled:  'rgba(232,239,233,0.38)',
      },
      error:   { main: '#C00000' },
      warning: {
        main:        '#FF6600',
        contrastText: '#ffffff',
      },
      success: {
        main:        '#32CD32',
        contrastText: '#0a0f0d',
      },
      divider: 'rgba(46,139,87,0.15)',
      action: {
        hover:    'rgba(46,139,87,0.08)',
        selected: 'rgba(46,139,87,0.16)',
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
      MuiCssBaseline: {
        styleOverrides: {
          'input:-webkit-autofill, input:-webkit-autofill:hover, input:-webkit-autofill:focus, input:-webkit-autofill:active': {
            WebkitBoxShadow: '0 0 0 1000px #141e19 inset !important',
            WebkitTextFillColor: '#e8efe9 !important',
            caretColor: '#e8efe9',
          },
        },
      },
      MuiCard: {
        styleOverrides: {
          root: {
            backgroundImage: 'none',
            border: '1px solid rgba(46,139,87,0.15)',
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
          tooltip: {
            backgroundColor: 'rgba(20,30,25,0.97)',
            fontSize: '0.75rem',
          },
        },
      },
    },
  })
}

export function createAuditorTheme() {
  return createTheme({
    palette: {
      mode: 'dark',
      primary: {
        main:  '#546E7A',
        light: '#78909C',
        dark:  '#37474F',
      },
      secondary: {
        main: '#90A4AE',
        dark: '#607D8B',
      },
      background: {
        default: '#09090b',
        paper:   '#101214',
      },
      text: {
        primary:   '#CFD8DC',
        secondary: '#78909C',
        disabled:  'rgba(207,216,220,0.38)',
      },
      error:   { main: '#C00000' },
      warning: {
        main:        '#FFA000',
        contrastText: '#ffffff',
      },
      success: {
        main:        '#66BB6A',
        contrastText: '#09090b',
      },
      divider: 'rgba(84,110,122,0.15)',
      action: {
        hover:    'rgba(84,110,122,0.08)',
        selected: 'rgba(84,110,122,0.16)',
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
      MuiCssBaseline: {
        styleOverrides: {
          'input:-webkit-autofill, input:-webkit-autofill:hover, input:-webkit-autofill:focus, input:-webkit-autofill:active': {
            WebkitBoxShadow: '0 0 0 1000px #101214 inset !important',
            WebkitTextFillColor: '#CFD8DC !important',
            caretColor: '#CFD8DC',
          },
        },
      },
      MuiCard: {
        styleOverrides: {
          root: {
            backgroundImage: 'none',
            border: '1px solid rgba(84,110,122,0.15)',
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
          tooltip: {
            backgroundColor: 'rgba(16,18,20,0.97)',
            fontSize: '0.75rem',
          },
        },
      },
    },
  })
}

// Keep a default export for backward compatibility during migration
export const theme = createAppTheme('dark')
