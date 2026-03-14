import { createTheme } from '@mui/material/styles'

export const theme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#4472C4',
      light: '#6B97D8',
      dark: '#2E5099',
    },
    secondary: {
      main: '#C6EFCE',
      dark: '#375623',
    },
    background: {
      default: '#0A0F1E',
      paper: '#0F1629',
    },
    text: {
      primary: '#E8EAF0',
      secondary: '#8B9CC8',
    },
    error: { main: '#C00000' },
    warning: { main: '#FFEB9C', contrastText: '#7D6608' },
    success: { main: '#C6EFCE', contrastText: '#375623' },
    divider: 'rgba(68, 114, 196, 0.15)',
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
        head: {
          fontWeight: 600,
          backgroundColor: '#0F1629',
          color: '#8B9CC8',
          fontSize: '0.75rem',
          textTransform: 'uppercase',
          letterSpacing: '0.05em',
        },
      },
    },
    MuiLinearProgress: {
      styleOverrides: {
        root: { borderRadius: 4, height: 6 },
      },
    },
  },
})
