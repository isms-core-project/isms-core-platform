import {
  Box,
  Drawer,
  Typography,
  IconButton,
  Chip,
  CircularProgress,
  Divider,
  Alert,
} from '@mui/material'
import { CloseOutlined, ArticleOutlined } from '@mui/icons-material'
import { useQuery } from '@tanstack/react-query'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import { client } from '../api/client'

const DRAWER_WIDTH = 900

interface DocPreviewTarget {
  id: string
  docType: 'policy' | 'implementation'
  documentId: string
  title: string
  typeLabel: string   // policy_type or impl_type
  typeColor?: string  // optional chip colour
  productType?: string
}

interface Props {
  open: boolean
  onClose: () => void
  target: DocPreviewTarget | null
}

async function fetchContent(target: DocPreviewTarget): Promise<string> {
  const path = target.docType === 'policy'
    ? `/policies/${target.id}/content`
    : `/implementations/${target.id}/content`
  const res = await client.get<{ content: string }>(path)
  return res.data.content
}

export default function DocPreviewDrawer({ open, onClose, target }: Props) {
  const isExternal = target?.productType === 'external'

  const { data: content, isLoading, isError } = useQuery({
    queryKey: ['doc-content', target?.id],
    queryFn: () => fetchContent(target!),
    enabled: open && !!target && !isExternal,
    staleTime: 5 * 60_000,
  })

  return (
    <Drawer
      anchor="right"
      open={open}
      onClose={onClose}
      variant="temporary"
      sx={{
        zIndex: 1300,
        '& .MuiDrawer-paper': {
          width: DRAWER_WIDTH,
          maxWidth: '92vw',
          bgcolor: '#0d1117',
          borderLeft: '1px solid rgba(68,114,196,0.2)',
          display: 'flex',
          flexDirection: 'column',
        },
      }}
    >
      {/* Header */}
      <Box sx={{ px: 2.5, py: 1.5, borderBottom: '1px solid rgba(255,255,255,0.06)', flexShrink: 0 }}>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
          <ArticleOutlined sx={{ color: 'primary.light', fontSize: 18 }} />
          <Box sx={{ flex: 1, minWidth: 0 }}>
            {target && (
              <>
                <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light', display: 'block' }}>
                  {target.documentId}
                </Typography>
                <Typography variant="subtitle2" fontWeight={700} sx={{ lineHeight: 1.2 }} noWrap>
                  {target.title}
                </Typography>
              </>
            )}
          </Box>
          {target && (
            <Chip
              label={target.typeLabel}
              size="small"
              sx={{
                fontSize: '0.65rem', height: 18, flexShrink: 0,
                bgcolor: target.typeColor ?? 'rgba(68,114,196,0.15)',
                color: target.typeColor ? '#000' : 'primary.light',
              }}
            />
          )}
          <IconButton size="small" onClick={onClose} sx={{ color: 'text.disabled', flexShrink: 0 }}>
            <CloseOutlined fontSize="small" />
          </IconButton>
        </Box>
      </Box>

      <Divider sx={{ borderColor: 'rgba(255,255,255,0.06)' }} />

      {/* Content */}
      <Box sx={{ flex: 1, overflowY: 'auto', px: 3, py: 2 }}>
        {isExternal && (
          <Box sx={{ mt: 3 }}>
            <Alert severity="info" sx={{ mb: 2 }}>
              External documents are stored as uploaded files and cannot be previewed inline.
            </Alert>
            <Box sx={{ p: 2, bgcolor: 'rgba(255,192,0,0.06)', border: '1px solid rgba(255,192,0,0.2)', borderRadius: 2 }}>
              <Typography variant="caption" sx={{ color: '#FFC000', fontWeight: 600, display: 'block', mb: 0.5 }}>
                External Document
              </Typography>
              <Typography variant="caption" sx={{ fontFamily: 'monospace', color: '#FFC000', display: 'block', mb: 0.5 }}>
                {target?.documentId}
              </Typography>
              <Typography variant="body2" fontWeight={600}>{target?.title}</Typography>
              <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mt: 1 }}>
                To view or delete this document, use the Policies page.
              </Typography>
            </Box>
          </Box>
        )}
        {!isExternal && isLoading && (
          <Box sx={{ display: 'flex', justifyContent: 'center', mt: 6 }}>
            <CircularProgress size={28} />
          </Box>
        )}
        {!isExternal && isError && (
          <Typography color="error" variant="body2">Failed to load document.</Typography>
        )}
        {!isExternal && content && (
          <Box
            sx={{
              '& h1': { fontSize: '1.25rem', fontWeight: 700, mt: 2, mb: 1, color: 'text.primary', borderBottom: '1px solid rgba(255,255,255,0.08)', pb: 0.5 },
              '& h2': { fontSize: '1.05rem', fontWeight: 700, mt: 2, mb: 0.75, color: 'text.primary' },
              '& h3': { fontSize: '0.95rem', fontWeight: 600, mt: 1.5, mb: 0.5, color: 'text.secondary' },
              '& h4,& h5,& h6': { fontSize: '0.85rem', fontWeight: 600, mt: 1, mb: 0.5, color: 'text.secondary' },
              '& p': { fontSize: '0.85rem', lineHeight: 1.7, mb: 1, color: 'text.primary' },
              '& ul,& ol': { pl: 2.5, mb: 1 },
              '& li': { fontSize: '0.85rem', lineHeight: 1.7, mb: 0.25, color: 'text.primary' },
              '& code': { fontFamily: 'monospace', fontSize: '0.78rem', bgcolor: 'rgba(68,114,196,0.12)', px: 0.5, borderRadius: 0.5, color: '#79b8ff' },
              '& pre': { bgcolor: 'rgba(0,0,0,0.4)', borderRadius: 1, p: 1.5, overflow: 'auto', mb: 1, '& code': { bgcolor: 'transparent', px: 0, color: '#79b8ff' } },
              '& blockquote': { borderLeft: '3px solid rgba(68,114,196,0.5)', pl: 2, ml: 0, color: 'text.secondary', fontStyle: 'italic' },
              '& table': { width: '100%', borderCollapse: 'collapse', mb: 1.5, fontSize: '0.8rem' },
              '& th': { bgcolor: 'rgba(68,114,196,0.15)', px: 1, py: 0.5, textAlign: 'left', borderBottom: '1px solid rgba(255,255,255,0.1)', fontWeight: 700 },
              '& td': { px: 1, py: 0.5, borderBottom: '1px solid rgba(255,255,255,0.05)' },
              '& hr': { borderColor: 'rgba(255,255,255,0.08)', my: 2 },
              '& a': { color: 'primary.light' },
              '& strong': { fontWeight: 700 },
            }}
          >
            <ReactMarkdown remarkPlugins={[remarkGfm]}>
              {content}
            </ReactMarkdown>
          </Box>
        )}
      </Box>
    </Drawer>
  )
}
