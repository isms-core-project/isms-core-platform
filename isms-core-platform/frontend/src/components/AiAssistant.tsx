import { useState, useRef, useEffect, useCallback } from 'react'
import {
  Box,
  Drawer,
  Typography,
  TextField,
  IconButton,
  Chip,
  CircularProgress,
  Divider,
  ToggleButtonGroup,
  ToggleButton,
  Tooltip,
} from '@mui/material'
import {
  AutoAwesomeOutlined,
  SendOutlined,
  CloseOutlined,
  DeleteOutlineOutlined,
  GavelOutlined,
  SummarizeOutlined,
} from '@mui/icons-material'
import { useQuery } from '@tanstack/react-query'
import { aiApi, type ChatMessage, type AiMode } from '../api/aiApi'

const DRAWER_WIDTH = 420

const MODE_CONFIG: Record<AiMode, { label: string; icon: React.ReactNode; color: string; placeholder: string }> = {
  assistant: {
    label: 'Assistant',
    icon: <AutoAwesomeOutlined fontSize="small" />,
    color: '#4472C4',
    placeholder: 'Ask anything about this control…',
  },
  audit_prep: {
    label: 'Audit Prep',
    icon: <GavelOutlined fontSize="small" />,
    color: '#FFC7CE',
    placeholder: 'I\'ll ask you audit questions about this control…',
  },
  gap_narrator: {
    label: 'Gap Narrative',
    icon: <SummarizeOutlined fontSize="small" />,
    color: '#FFEB9C',
    placeholder: 'Ask me to draft the executive gap narrative…',
  },
}

interface Props {
  open: boolean
  onClose: () => void
  controlId: string | null
  controlName?: string
}

export default function AiAssistant({ open, onClose, controlId, controlName }: Props) {
  const [messages, setMessages] = useState<ChatMessage[]>([])
  const [input, setInput] = useState('')
  const [streaming, setStreaming] = useState(false)
  const [mode, setMode] = useState<AiMode>('assistant')
  const abortRef = useRef<AbortController | null>(null)
  const bottomRef = useRef<HTMLDivElement | null>(null)

  const { data: aiStatus } = useQuery({
    queryKey: ['ai-status'],
    queryFn: aiApi.status,
    staleTime: 60_000,
  })

  // Scroll to bottom when messages update
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  // Reset on mode change
  useEffect(() => {
    setMessages([])
  }, [mode])

  const send = useCallback(async () => {
    const text = input.trim()
    if (!text || streaming) return

    const userMsg: ChatMessage = { role: 'user', content: text }
    const newMessages = [...messages, userMsg]
    setMessages(newMessages)
    setInput('')
    setStreaming(true)

    // Placeholder for streaming assistant message
    const assistantMsg: ChatMessage = { role: 'assistant', content: '' }
    setMessages([...newMessages, assistantMsg])

    abortRef.current = new AbortController()

    await aiApi.streamChat(
      newMessages,
      controlId,
      mode,
      (chunk) => {
        setMessages((prev) => {
          const updated = [...prev]
          updated[updated.length - 1] = {
            ...updated[updated.length - 1],
            content: updated[updated.length - 1].content + chunk,
          }
          return updated
        })
      },
      (err) => {
        setMessages((prev) => {
          const updated = [...prev]
          updated[updated.length - 1] = { role: 'assistant', content: `⚠ ${err}` }
          return updated
        })
      },
      () => setStreaming(false),
      abortRef.current.signal,
    )
  }, [input, messages, streaming, controlId, mode])

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      send()
    }
  }

  const modeColor = MODE_CONFIG[mode].color

  return (
    <Drawer
      anchor="right"
      open={open}
      onClose={onClose}
      variant="persistent"
      sx={{
        width: open ? DRAWER_WIDTH : 0,
        flexShrink: 0,
        '& .MuiDrawer-paper': {
          width: DRAWER_WIDTH,
          bgcolor: '#0d1117',
          borderLeft: `1px solid rgba(68,114,196,0.2)`,
          display: 'flex',
          flexDirection: 'column',
        },
      }}
    >
      {/* Header */}
      <Box sx={{ px: 2, py: 1.5, borderBottom: '1px solid rgba(255,255,255,0.06)', flexShrink: 0 }}>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1 }}>
          <AutoAwesomeOutlined sx={{ color: modeColor, fontSize: 18 }} />
          <Typography variant="subtitle2" fontWeight={700} sx={{ flex: 1, color: modeColor }}>
            ISMS AI
          </Typography>
          {controlName && (
            <Typography variant="caption" color="text.disabled" sx={{ maxWidth: 160, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
              {controlName}
            </Typography>
          )}
          <Tooltip title="Clear conversation">
            <IconButton size="small" onClick={() => setMessages([])} sx={{ color: 'text.disabled' }}>
              <DeleteOutlineOutlined fontSize="small" />
            </IconButton>
          </Tooltip>
          <IconButton size="small" onClick={onClose} sx={{ color: 'text.disabled' }}>
            <CloseOutlined fontSize="small" />
          </IconButton>
        </Box>

        {/* Mode selector */}
        <ToggleButtonGroup
          value={mode}
          exclusive
          onChange={(_, v) => v && setMode(v)}
          size="small"
          fullWidth
          sx={{
            '& .MuiToggleButton-root': {
              py: 0.3, fontSize: '0.7rem', fontWeight: 600, borderColor: 'rgba(255,255,255,0.08)',
              color: 'text.disabled', gap: 0.5,
              '&.Mui-selected': { color: modeColor, bgcolor: `${modeColor}18`, borderColor: `${modeColor}40` },
            },
          }}
        >
          {(Object.entries(MODE_CONFIG) as [AiMode, typeof MODE_CONFIG[AiMode]][]).map(([key, cfg]) => (
            <ToggleButton key={key} value={key}>
              {cfg.icon}{cfg.label}
            </ToggleButton>
          ))}
        </ToggleButtonGroup>

        {aiStatus && !aiStatus.configured && (
          <Box sx={{ mt: 1, px: 1, py: 0.5, bgcolor: 'rgba(255,199,206,0.08)', borderRadius: 1, border: '1px solid rgba(255,199,206,0.2)' }}>
            <Typography variant="caption" sx={{ color: '#FFC7CE' }}>
              ⚠ API key not configured — add ANTHROPIC_API_KEY to .env
            </Typography>
          </Box>
        )}
      </Box>

      {/* Messages */}
      <Box sx={{ flex: 1, overflowY: 'auto', px: 2, py: 1.5, display: 'flex', flexDirection: 'column', gap: 1.5 }}>
        {messages.length === 0 && (
          <Box sx={{ mt: 4, textAlign: 'center' }}>
            <AutoAwesomeOutlined sx={{ fontSize: 32, color: 'rgba(68,114,196,0.3)', mb: 1 }} />
            <Typography variant="body2" color="text.disabled">
              {MODE_CONFIG[mode].placeholder}
            </Typography>
            {mode === 'assistant' && controlId && (
              <Box sx={{ mt: 2, display: 'flex', flexDirection: 'column', gap: 0.75, alignItems: 'center' }}>
                {[
                  'What evidence should I collect for audit readiness?',
                  'Summarise the current compliance posture',
                  'What are the highest priority gaps?',
                ].map((q) => (
                  <Chip
                    key={q}
                    label={q}
                    size="small"
                    onClick={() => { setInput(q) }}
                    sx={{ cursor: 'pointer', fontSize: '0.7rem', bgcolor: 'rgba(68,114,196,0.08)', color: 'text.secondary',
                          '&:hover': { bgcolor: 'rgba(68,114,196,0.18)' } }}
                  />
                ))}
              </Box>
            )}
          </Box>
        )}

        {messages.map((msg, idx) => (
          <Box
            key={idx}
            sx={{
              alignSelf: msg.role === 'user' ? 'flex-end' : 'flex-start',
              maxWidth: '90%',
            }}
          >
            {msg.role === 'assistant' && (
              <Typography variant="caption" sx={{ color: modeColor, fontWeight: 700, display: 'block', mb: 0.25, fontSize: '0.65rem' }}>
                ISMS AI
              </Typography>
            )}
            <Box
              sx={{
                px: 1.5, py: 1,
                borderRadius: msg.role === 'user' ? '12px 12px 2px 12px' : '2px 12px 12px 12px',
                bgcolor: msg.role === 'user'
                  ? 'rgba(68,114,196,0.2)'
                  : 'rgba(255,255,255,0.04)',
                border: msg.role === 'assistant' ? `1px solid rgba(255,255,255,0.06)` : 'none',
              }}
            >
              <Typography
                variant="body2"
                sx={{
                  whiteSpace: 'pre-wrap', lineHeight: 1.6, fontSize: '0.82rem',
                  color: msg.content.startsWith('⚠') ? '#FFC7CE' : 'text.primary',
                }}
              >
                {msg.content}
                {streaming && idx === messages.length - 1 && msg.role === 'assistant' && (
                  <Box component="span" sx={{ display: 'inline-block', width: 6, height: 12, bgcolor: modeColor, ml: 0.5, verticalAlign: 'middle',
                    animation: 'blink 1s step-end infinite', '@keyframes blink': { '0%,100%': { opacity: 1 }, '50%': { opacity: 0 } } }} />
                )}
              </Typography>
            </Box>
          </Box>
        ))}
        <div ref={bottomRef} />
      </Box>

      <Divider sx={{ borderColor: 'rgba(255,255,255,0.06)' }} />

      {/* Input */}
      <Box sx={{ px: 2, py: 1.5, flexShrink: 0 }}>
        <Box sx={{ display: 'flex', gap: 1, alignItems: 'flex-end' }}>
          <TextField
            multiline
            maxRows={4}
            size="small"
            fullWidth
            placeholder={MODE_CONFIG[mode].placeholder}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            disabled={streaming}
            sx={{
              '& .MuiOutlinedInput-root': {
                fontSize: '0.85rem',
                '& fieldset': { borderColor: `rgba(68,114,196,0.25)` },
                '&:hover fieldset': { borderColor: `rgba(68,114,196,0.5)` },
                '&.Mui-focused fieldset': { borderColor: modeColor },
              },
            }}
          />
          <IconButton
            onClick={send}
            disabled={!input.trim() || streaming}
            sx={{
              bgcolor: streaming ? 'transparent' : `${modeColor}25`,
              color: modeColor,
              border: `1px solid ${modeColor}40`,
              '&:hover': { bgcolor: `${modeColor}40` },
              '&.Mui-disabled': { opacity: 0.3 },
              flexShrink: 0,
            }}
          >
            {streaming ? <CircularProgress size={18} sx={{ color: modeColor }} /> : <SendOutlined fontSize="small" />}
          </IconButton>
        </Box>
        <Typography variant="caption" color="text.disabled" sx={{ mt: 0.5, display: 'block', fontSize: '0.62rem' }}>
          ↵ Send · Shift+↵ New line · Context: {controlId ? 'this control' : 'general ISMS'}
        </Typography>
      </Box>
    </Drawer>
  )
}
