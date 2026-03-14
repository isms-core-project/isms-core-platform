import { useState, useEffect } from 'react'
import { useSearchParams } from 'react-router-dom'
import {
  Alert,
  Box,
  Button,
  Card,
  CardContent,
  Chip,
  CircularProgress,
  Divider,
  FormControl,
  InputLabel,
  LinearProgress,
  MenuItem,
  Select,
  TextField,
  Tooltip,
  Typography,
} from '@mui/material'
import {
  ExploreOutlined,
  InfoOutlined,
  WarningAmberOutlined,
  CheckCircleOutlined,
  ErrorOutlined,
} from '@mui/icons-material'
import { useMutation, useQuery } from '@tanstack/react-query'
import { compassApi } from '../api/compass'
import type { CompassReport, CompassGap } from '../api/compass'
import { controlsApi } from '../api/controls'
import type { ControlGroupList } from '../api/types'
import PageHeader from '../components/PageHeader'

const SEV_COLOR: Record<string, { bg: string; fg: string; icon: React.ReactNode }> = {
  high:   { bg: 'rgba(192,0,0,0.15)',    fg: '#FFC7CE', icon: <ErrorOutlined sx={{ fontSize: 14 }} /> },
  medium: { bg: 'rgba(255,192,0,0.12)',  fg: '#FFEB9C', icon: <WarningAmberOutlined sx={{ fontSize: 14 }} /> },
  low:    { bg: 'rgba(112,173,71,0.12)', fg: '#C6EFCE', icon: <InfoOutlined sx={{ fontSize: 14 }} /> },
}

function ScoreGauge({ score }: { score: number }) {
  const color =
    score >= 80 ? '#C6EFCE' :
    score >= 60 ? '#FFEB9C' :
    score >= 40 ? '#FF9900' : '#FFC7CE'

  const bgColor =
    score >= 80 ? 'rgba(198,239,206,0.12)' :
    score >= 60 ? 'rgba(255,235,156,0.12)' :
    score >= 40 ? 'rgba(255,153,0,0.12)'   : 'rgba(255,199,206,0.12)'

  return (
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        width: 120,
        height: 120,
        borderRadius: '50%',
        border: `4px solid ${color}`,
        bgcolor: bgColor,
        flexShrink: 0,
      }}
    >
      <Typography variant="h3" fontWeight={700} sx={{ color, lineHeight: 1 }}>
        {score}
      </Typography>
      <Typography variant="caption" color="text.secondary">
        / 100
      </Typography>
    </Box>
  )
}

function GapCard({ gap }: { gap: CompassGap }) {
  const sev = SEV_COLOR[gap.severity] ?? SEV_COLOR.low
  return (
    <Box
      sx={{
        border: '1px solid',
        borderColor: 'rgba(255,255,255,0.08)',
        borderRadius: 1,
        p: 1.5,
        mb: 1,
        bgcolor: sev.bg,
      }}
    >
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 0.5, flexWrap: 'wrap' }}>
        <Chip
          label={gap.severity}
          size="small"
          icon={sev.icon as React.ReactElement}
          sx={{ fontSize: '0.65rem', height: 18, bgcolor: 'transparent', color: sev.fg, border: `1px solid ${sev.fg}` }}
        />
        <Typography variant="body2" fontWeight={600}>{gap.topic}</Typography>
        <Chip
          label={gap.iso_clause}
          size="small"
          sx={{ fontSize: '0.62rem', height: 16, ml: 'auto', opacity: 0.7 }}
        />
      </Box>
      <Typography variant="body2" color="text.secondary" sx={{ mb: 0.75, fontSize: '0.8rem' }}>
        {gap.description}
      </Typography>
      <Box sx={{ display: 'flex', gap: 0.5, alignItems: 'flex-start' }}>
        <CheckCircleOutlined sx={{ fontSize: 13, color: '#C6EFCE', mt: 0.2, flexShrink: 0 }} />
        <Typography variant="caption" sx={{ color: '#C6EFCE', fontSize: '0.75rem' }}>
          {gap.recommendation}
        </Typography>
      </Box>
    </Box>
  )
}

function ReportView({ report }: { report: CompassReport }) {
  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2, mt: 2 }}>
      {/* Disclaimer */}
      <Alert
        severity="info"
        icon={<InfoOutlined />}
        sx={{ fontSize: '0.78rem' }}
      >
        <strong>Guidance only — not a compliance guarantee.</strong> {report.disclaimer}
      </Alert>

      {/* Score + Summary */}
      <Card>
        <CardContent>
          <Box sx={{ display: 'flex', gap: 3, alignItems: 'flex-start', flexWrap: 'wrap' }}>
            <ScoreGauge score={report.coverage_score} />
            <Box sx={{ flex: 1 }}>
              <Typography variant="h6" gutterBottom>
                {report.control_group_name}
                <Typography component="span" variant="caption" color="text.secondary" sx={{ ml: 1 }}>
                  {report.control_group_code.toUpperCase()}
                </Typography>
              </Typography>
              <Typography variant="body2" color="text.secondary" sx={{ mb: 1 }}>
                {report.summary}
              </Typography>
              <Box sx={{ display: 'flex', gap: 1, flexWrap: 'wrap' }}>
                <Chip label={`${report.gaps.filter(g => g.severity === 'high').length} high gaps`} size="small" sx={{ bgcolor: 'rgba(192,0,0,0.15)', color: '#FFC7CE', fontSize: '0.65rem', height: 18 }} />
                <Chip label={`${report.gaps.filter(g => g.severity === 'medium').length} medium gaps`} size="small" sx={{ bgcolor: 'rgba(255,192,0,0.12)', color: '#FFEB9C', fontSize: '0.65rem', height: 18 }} />
                <Chip label={`${report.strengths.length} strengths`} size="small" sx={{ bgcolor: 'rgba(112,173,71,0.15)', color: '#C6EFCE', fontSize: '0.65rem', height: 18 }} />
                <Tooltip title={`Model: ${report.model_used}`}>
                  <Chip label={`${report.tokens_used.toLocaleString()} tokens`} size="small" sx={{ fontSize: '0.62rem', height: 18, opacity: 0.5 }} />
                </Tooltip>
              </Box>
            </Box>
          </Box>
        </CardContent>
      </Card>

      {/* Gaps */}
      {report.gaps.length > 0 && (
        <Card>
          <CardContent sx={{ pb: '12px !important' }}>
            <Typography variant="h6" gutterBottom>
              Gaps ({report.gaps.length})
            </Typography>
            <Divider sx={{ mb: 1.5 }} />
            {['high', 'medium', 'low'].map((sev) => {
              const sevGaps = report.gaps.filter((g) => g.severity === sev)
              if (sevGaps.length === 0) return null
              return (
                <Box key={sev} sx={{ mb: 1 }}>
                  {sevGaps.map((gap, i) => <GapCard key={i} gap={gap} />)}
                </Box>
              )
            })}
          </CardContent>
        </Card>
      )}

      {/* Strengths */}
      {report.strengths.length > 0 && (
        <Card>
          <CardContent sx={{ pb: '12px !important' }}>
            <Typography variant="h6" gutterBottom>
              Strengths ({report.strengths.length})
            </Typography>
            <Divider sx={{ mb: 1.5 }} />
            {report.strengths.map((s, i) => (
              <Box key={i} sx={{ display: 'flex', gap: 1, mb: 1, alignItems: 'flex-start' }}>
                <CheckCircleOutlined sx={{ fontSize: 16, color: '#C6EFCE', mt: 0.2, flexShrink: 0 }} />
                <Box>
                  <Typography variant="body2" fontWeight={600}>{s.topic}</Typography>
                  <Typography variant="caption" color="text.secondary">{s.detail}</Typography>
                </Box>
              </Box>
            ))}
          </CardContent>
        </Card>
      )}
    </Box>
  )
}

export default function Compass() {
  const [searchParams] = useSearchParams()
  const [groupCode, setGroupCode] = useState(searchParams.get('group') ?? '')
  const [docText, setDocText] = useState('')
  const [report, setReport] = useState<CompassReport | null>(null)

  useEffect(() => {
    const g = searchParams.get('group')
    if (g) setGroupCode(g)
  }, [searchParams])

  const { data: statusData } = useQuery({
    queryKey: ['compass', 'status'],
    queryFn: compassApi.status,
  })

  const { data: controlGroups } = useQuery({
    queryKey: ['controls', 'list'],
    queryFn: () => controlsApi.list(),
  })

  const analyseMutation = useMutation({
    mutationFn: () => compassApi.analyse(groupCode, docText),
    onSuccess: (data) => setReport(data),
  })

  const isAvailable = statusData?.available ?? false

  return (
    <Box>
      <PageHeader
        title="ISMS Compass"
        subtitle="AI-powered gap analysis — compare any document against the ISMS CORE Gold Standard"
      />

      {statusData && !isAvailable && (
        <Alert severity="warning" sx={{ mb: 2 }}>
          ANTHROPIC_API_KEY is not configured. Add it to <code>platform/.env</code> and restart the backend.
        </Alert>
      )}

      <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
        {/* Input card */}
        <Card>
          <CardContent>
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 2 }}>
              <ExploreOutlined sx={{ color: 'primary.main' }} />
              <Typography variant="h6">Analyse a Document</Typography>
            </Box>

            <FormControl fullWidth size="small" sx={{ mb: 2 }}>
              <InputLabel>Control Group</InputLabel>
              <Select
                value={groupCode}
                onChange={(e) => setGroupCode(e.target.value)}
                label="Control Group"
                disabled={!isAvailable}
              >
                {(controlGroups ?? []).map((cg: ControlGroupList) => (
                  <MenuItem key={cg.group_code} value={cg.group_code}>
                    {cg.group_code.toUpperCase()} — {cg.group_name}
                  </MenuItem>
                ))}
              </Select>
            </FormControl>

            <TextField
              fullWidth
              multiline
              rows={10}
              label="Paste document text here"
              placeholder="Paste the full text of the policy, procedure, or control document you want to analyse…"
              value={docText}
              onChange={(e) => setDocText(e.target.value)}
              disabled={!isAvailable}
              sx={{ mb: 2, fontFamily: 'monospace' }}
              inputProps={{ style: { fontFamily: 'monospace', fontSize: '0.8rem' } }}
            />

            <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
              <Button
                variant="contained"
                startIcon={
                  analyseMutation.isPending
                    ? <CircularProgress size={14} sx={{ color: 'inherit' }} />
                    : <ExploreOutlined />
                }
                disabled={!isAvailable || !groupCode || !docText.trim() || analyseMutation.isPending}
                onClick={() => { setReport(null); analyseMutation.mutate() }}
              >
                {analyseMutation.isPending ? 'Analysing…' : 'Analyse with Compass'}
              </Button>
              {docText.trim() && (
                <Typography variant="caption" color="text.secondary">
                  {docText.trim().length.toLocaleString()} chars
                </Typography>
              )}
            </Box>

            {analyseMutation.isPending && (
              <Box sx={{ mt: 2 }}>
                <LinearProgress />
                <Typography variant="caption" color="text.secondary" sx={{ mt: 0.5, display: 'block' }}>
                  Retrieving Gold Standard reference · Calling Claude · Parsing gap report…
                </Typography>
              </Box>
            )}

            {analyseMutation.isError && (
              <Alert severity="error" sx={{ mt: 2 }}>
                {(analyseMutation.error as { response?: { data?: { detail?: string } } })?.response?.data?.detail
                  ?? 'Analysis failed — check server logs.'}
              </Alert>
            )}
          </CardContent>
        </Card>

        {/* Results */}
        {report && <ReportView report={report} />}
      </Box>
    </Box>
  )
}
