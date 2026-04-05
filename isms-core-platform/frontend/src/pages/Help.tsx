import { useState, useEffect, useRef } from 'react'
import { useLocation, useNavigate } from 'react-router-dom'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import {
  Box,
  Typography,
  CircularProgress,
  Alert,
  Divider,
  List,
  ListItemButton,
  ListItemText,
  useTheme,
  useMediaQuery,
  IconButton,
  Drawer,
  Tooltip,
} from '@mui/material'
import { MenuOutlined } from '@mui/icons-material'

interface TocEntry {
  id: string
  label: string
  level: number
}

// Extract TOC from markdown text
function extractToc(md: string): TocEntry[] {
  const entries: TocEntry[] = []
  const lines = md.split('\n')
  for (const line of lines) {
    const m = line.match(/^(#{1,3})\s+(.+?)(?:\s+\{#[\w-]+\})?$/)
    if (m) {
      const level = m[1].length
      const rawLabel = m[2].replace(/\*\*/g, '').replace(/`/g, '').trim()
      // Extract explicit anchor or derive from label
      const anchorMatch = line.match(/\{#([\w-]+)\}/)
      const id = anchorMatch
        ? anchorMatch[1]
        : rawLabel.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '')
      entries.push({ id, label: rawLabel, level })
    }
  }
  return entries
}

// Custom heading renderer — strips {#anchor} syntax, adds id
function HeadingRenderer(level: number) {
  return function Heading({ children }: { children?: React.ReactNode }) {
    const raw = String(children ?? '')
    // Extract explicit anchor if present, e.g. "Getting Started {#getting-started}"
    const anchorMatch = raw.match(/\{#([\w-]+)\}/)
    const id = anchorMatch
      ? anchorMatch[1]
      : raw.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '')
    // Strip {#...} from displayed text
    const display = raw.replace(/\s*\{#[\w-]+\}/g, '')
    const Tag = `h${level}` as keyof JSX.IntrinsicElements
    return (
      <Tag id={id} style={{ scrollMarginTop: '80px' }}>
        {display}
      </Tag>
    )
  }
}

export default function Help() {
  const [markdown, setMarkdown] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [toc, setToc] = useState<TocEntry[]>([])
  const [activeId, setActiveId] = useState<string>('')
  const [drawerOpen, setDrawerOpen] = useState(false)
  const contentRef = useRef<HTMLDivElement>(null)
  const location = useLocation()
  const navigate = useNavigate()
  const theme = useTheme()
  const isNarrow = useMediaQuery(theme.breakpoints.down('lg'))

  // Load markdown
  useEffect(() => {
    fetch('/docs/user-manual.md')
      .then(r => {
        if (!r.ok) throw new Error(`Failed to load manual (${r.status})`)
        return r.text()
      })
      .then(text => {
        setMarkdown(text)
        setToc(extractToc(text))
      })
      .catch(e => setError(e.message))
  }, [])

  // Scroll to hash after markdown loads
  useEffect(() => {
    if (!markdown) return
    const hash = location.hash.replace('#', '')
    if (!hash) return
    // Short delay to let DOM render
    setTimeout(() => {
      const el = document.getElementById(hash)
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'start' })
        setActiveId(hash)
      }
    }, 100)
  }, [markdown, location.hash])

  // Track active heading via IntersectionObserver
  useEffect(() => {
    if (!markdown) return
    const observer = new IntersectionObserver(
      entries => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            setActiveId(entry.target.id)
          }
        }
      },
      { rootMargin: '-10% 0px -80% 0px' }
    )
    const headings = document.querySelectorAll('h1[id], h2[id], h3[id]')
    headings.forEach(h => observer.observe(h))
    return () => observer.disconnect()
  }, [markdown])

  function handleTocClick(id: string) {
    navigate(`/help#${id}`, { replace: true })
    const el = document.getElementById(id)
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' })
    setActiveId(id)
    setDrawerOpen(false)
  }

  const tocContent = (
    <Box sx={{ width: 260, flexShrink: 0, p: 2 }}>
      <Typography variant="overline" color="text.secondary" sx={{ px: 1, display: 'block', mb: 1 }}>
        Contents
      </Typography>
      <List dense disablePadding>
        {toc.map(entry => (
          <ListItemButton
            key={entry.id}
            selected={activeId === entry.id}
            onClick={() => handleTocClick(entry.id)}
            sx={{
              borderRadius: 1,
              py: 0.4,
              pl: entry.level === 1 ? 1 : entry.level === 2 ? 2 : 3,
              '&.Mui-selected': {
                bgcolor: 'action.selected',
                borderLeft: '2px solid',
                borderLeftColor: 'primary.main',
              },
            }}
          >
            <ListItemText
              primary={entry.label}
              primaryTypographyProps={{
                variant: 'body2',
                sx: {
                  fontSize: entry.level === 1 ? '0.82rem' : '0.77rem',
                  fontWeight: entry.level === 1 ? 600 : 400,
                  color: activeId === entry.id ? 'primary.main' : 'text.secondary',
                  lineHeight: 1.4,
                },
              }}
            />
          </ListItemButton>
        ))}
      </List>
    </Box>
  )

  return (
    <Box sx={{ display: 'flex', height: '100%', overflow: 'hidden' }}>
      {/* Sidebar TOC — fixed on large screens */}
      {!isNarrow ? (
        <Box
          sx={{
            width: 260,
            flexShrink: 0,
            borderRight: '1px solid',
            borderColor: 'divider',
            overflowY: 'auto',
            height: '100%',
            position: 'sticky',
            top: 0,
          }}
        >
          {tocContent}
        </Box>
      ) : (
        <Drawer
          open={drawerOpen}
          onClose={() => setDrawerOpen(false)}
          PaperProps={{ sx: { bgcolor: 'background.paper' } }}
        >
          {tocContent}
        </Drawer>
      )}

      {/* Main content */}
      <Box
        ref={contentRef}
        sx={{
          flex: 1,
          overflowY: 'auto',
          px: { xs: 2, md: 5 },
          py: 4,
          maxWidth: 860,
        }}
      >
        {/* Header */}
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 3 }}>
          {isNarrow && (
            <Tooltip title="Table of contents">
              <IconButton onClick={() => setDrawerOpen(true)} size="small">
                <MenuOutlined />
              </IconButton>
            </Tooltip>
          )}
          <Typography variant="h4" sx={{ fontWeight: 700 }}>
            User Guide
          </Typography>
          <Typography variant="caption" color="text.secondary" sx={{ ml: 1, mt: 0.5 }}>
            v1.0
          </Typography>
        </Box>
        <Divider sx={{ mb: 3 }} />

        {error && (
          <Alert severity="error" sx={{ mb: 2 }}>
            {error}
          </Alert>
        )}

        {!markdown && !error && (
          <Box sx={{ display: 'flex', justifyContent: 'center', pt: 8 }}>
            <CircularProgress />
          </Box>
        )}

        {markdown && (
          <Box
            sx={{
              '& h1': { ...theme.typography.h3, mt: 4, mb: 1.5, color: 'text.primary' },
              '& h2': { ...theme.typography.h4, mt: 3.5, mb: 1, color: 'text.primary', borderBottom: '1px solid', borderColor: 'divider', pb: 0.5 },
              '& h3': { ...theme.typography.h5, mt: 2.5, mb: 0.75, color: 'text.primary' },
              '& p': { ...theme.typography.body1, mb: 1.5, lineHeight: 1.7, color: 'text.secondary' },
              '& ul, & ol': { pl: 3, mb: 1.5 },
              '& li': { ...theme.typography.body1, mb: 0.5, color: 'text.secondary' },
              '& table': { borderCollapse: 'collapse', width: '100%', mb: 2, fontSize: '0.82rem' },
              '& th': {
                textAlign: 'left',
                p: '6px 12px',
                bgcolor: 'background.paper',
                borderBottom: '2px solid',
                borderColor: 'divider',
                fontWeight: 600,
                color: 'text.secondary',
                fontSize: '0.75rem',
                textTransform: 'uppercase',
                letterSpacing: '0.04em',
              },
              '& td': {
                p: '6px 12px',
                borderBottom: '1px solid',
                borderColor: 'divider',
                color: 'text.secondary',
              },
              '& tr:last-child td': { borderBottom: 'none' },
              '& code': {
                fontFamily: 'monospace',
                fontSize: '0.82rem',
                bgcolor: 'action.hover',
                px: 0.6,
                py: 0.2,
                borderRadius: 0.5,
                color: 'primary.main',
              },
              '& pre': {
                bgcolor: 'background.paper',
                border: '1px solid',
                borderColor: 'divider',
                borderRadius: 1,
                p: 2,
                overflow: 'auto',
                mb: 2,
                '& code': { bgcolor: 'transparent', px: 0, py: 0, color: 'text.primary' },
              },
              '& blockquote': {
                borderLeft: '3px solid',
                borderColor: 'primary.main',
                pl: 2,
                ml: 0,
                my: 2,
                color: 'text.secondary',
                fontStyle: 'italic',
              },
              '& a': { color: 'primary.main', textDecoration: 'none', '&:hover': { textDecoration: 'underline' } },
              '& hr': { border: 'none', borderTop: '1px solid', borderColor: 'divider', my: 3 },
            }}
          >
            <ReactMarkdown
              remarkPlugins={[remarkGfm]}
              components={{
                h1: HeadingRenderer(1),
                h2: HeadingRenderer(2),
                h3: HeadingRenderer(3),
              }}
            >
              {markdown}
            </ReactMarkdown>
          </Box>
        )}
      </Box>
    </Box>
  )
}
