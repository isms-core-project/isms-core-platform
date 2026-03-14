import { useState } from 'react'
import { Box, Typography, Skeleton, LinearProgress, Tooltip, TextField, InputAdornment, IconButton } from '@mui/material'
import {
  ShieldOutlined,
  LockPersonOutlined,
  CloudOutlined,
  VerifiedOutlined,
  ExploreOutlined,
  CodeOutlined,
  SummarizeOutlined,
  GppMaybeOutlined,
  AdminPanelSettingsOutlined,
  MonitorHeartOutlined,
  ArrowForwardOutlined,
  CheckCircleOutlined,
  RadioButtonUncheckedOutlined,
  SearchOutlined,
  ElectricalServicesOutlined,
} from '@mui/icons-material'
import { useQuery } from '@tanstack/react-query'
import { useNavigate } from 'react-router-dom'
import { dashboardApi, type HomeSummary } from '../api/dashboard'
import { useProduct, PRODUCT_COLORS, PRODUCT_LABELS } from '../store/ProductContext'
import { useAuth } from '../store/AuthContext'

const PLATFORM_TOOLS = [
  { label: 'QA',           path: '/qa',           icon: <VerifiedOutlined sx={{ fontSize: 17 }} /> },
  { label: 'Search',       path: '/search',       icon: <SearchOutlined sx={{ fontSize: 17 }} /> },
  { label: 'Compass',      path: '/compass',      icon: <ExploreOutlined sx={{ fontSize: 17 }} /> },
  { label: 'Generators',   path: '/generators',   icon: <CodeOutlined sx={{ fontSize: 17 }} /> },
  { label: 'Connectors',   path: '/connectors',   icon: <ElectricalServicesOutlined sx={{ fontSize: 17 }} /> },
  { label: 'Report',       path: '/report',       icon: <SummarizeOutlined sx={{ fontSize: 17 }} /> },
  { label: 'Risk',         path: '/risk',         icon: <GppMaybeOutlined sx={{ fontSize: 17 }} /> },
  { label: 'Admin',        path: '/admin',        icon: <AdminPanelSettingsOutlined sx={{ fontSize: 17 }} /> },
  { label: 'System',       path: '/system',       icon: <MonitorHeartOutlined sx={{ fontSize: 17 }} /> },
]

const PRODUCT_STANDARDS = {
  isms:    'ISO/IEC 27001:2022',
  privacy: 'ISO/IEC 27701:2025',
  cloud:   'ISO/IEC 27018:2025',
}

const PRODUCT_ICONS = {
  isms:    <ShieldOutlined />,
  privacy: <LockPersonOutlined />,
  cloud:   <CloudOutlined />,
}

function Num({ value, color, loading }: { value?: number; color: string; loading: boolean }) {
  if (loading) return <Skeleton variant="text" width={32} height={32} />
  return (
    <Typography variant="h5" sx={{ fontWeight: 700, color, lineHeight: 1, fontSize: '1.4rem' }}>
      {value ?? '—'}
    </Typography>
  )
}

function CoverageBar({ label, pct, color, loading }: { label: string; pct?: number; color: string; loading: boolean }) {
  return (
    <Box sx={{ mb: 0.9 }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.3 }}>
        <Typography variant="caption" sx={{ fontSize: '0.69rem', color: 'text.secondary' }}>{label}</Typography>
        {loading
          ? <Skeleton variant="text" width={30} />
          : <Typography variant="caption" sx={{ fontSize: '0.69rem', fontWeight: 600, color }}>{pct ?? 0}%</Typography>
        }
      </Box>
      {loading
        ? <Skeleton variant="rectangular" height={5} sx={{ borderRadius: 3 }} />
        : <LinearProgress
            variant="determinate"
            value={Math.min(pct ?? 0, 100)}
            sx={{
              height: 5, borderRadius: 3,
              bgcolor: `${color}20`,
              '& .MuiLinearProgress-bar': { bgcolor: color, borderRadius: 3 },
            }}
          />
      }
    </Box>
  )
}

function StatusDot({ ok, label, loading }: { ok: boolean; label: string; loading: boolean }) {
  if (loading) return <Skeleton variant="text" width={120} height={20} sx={{ mb: 0.5 }} />
  return (
    <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.75, mb: 0.5 }}>
      {ok
        ? <CheckCircleOutlined sx={{ fontSize: 13, color: '#70AD47' }} />
        : <RadioButtonUncheckedOutlined sx={{ fontSize: 13, color: 'text.disabled' }} />
      }
      <Typography variant="caption" sx={{ fontSize: '0.71rem', color: ok ? 'text.primary' : 'text.disabled' }}>
        {label}
      </Typography>
    </Box>
  )
}

function ProductCard({
  product,
  loading,
  onClick,
  children,
}: {
  product: 'isms' | 'privacy' | 'cloud'
  loading: boolean
  onClick: () => void
  children: React.ReactNode
}) {
  const color = PRODUCT_COLORS[product]
  return (
    <Box
      onClick={onClick}
      sx={{
        p: 2, borderRadius: 2, cursor: 'pointer', height: '100%',
        border: `1px solid ${color}28`,
        borderLeft: `4px solid ${color}`,
        bgcolor: `${color}07`,
        transition: 'all 0.15s',
        display: 'flex', flexDirection: 'column',
        '&:hover': { bgcolor: `${color}12`, borderColor: `${color}55` },
      }}
    >
      {/* Header */}
      <Box sx={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', mb: 2 }}>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
          <Box sx={{ color, fontSize: 20, display: 'flex' }}>{PRODUCT_ICONS[product]}</Box>
          <Box>
            <Typography variant="subtitle2" sx={{ fontWeight: 700, color, lineHeight: 1.2, fontSize: '0.85rem' }}>
              {PRODUCT_LABELS[product]}
            </Typography>
            <Typography variant="caption" sx={{ color: 'text.disabled', fontSize: '0.63rem' }}>
              {PRODUCT_STANDARDS[product]}
            </Typography>
          </Box>
        </Box>
        <ArrowForwardOutlined sx={{ fontSize: 15, color: 'text.disabled', mt: 0.25 }} />
      </Box>

      {children}
    </Box>
  )
}

export default function Home() {
  const navigate = useNavigate()
  const { user } = useAuth()
  const { setProduct } = useProduct()
  const [searchQuery, setSearchQuery] = useState('')

  function handleSearch() {
    const q = searchQuery.trim()
    if (q.length >= 2) navigate(`/search?q=${encodeURIComponent(q)}`)
  }

  const { data: summary, isLoading } = useQuery({
    queryKey: ['home-summary'],
    queryFn: dashboardApi.getHomeSummary,
    staleTime: 30_000,
    retry: 2,
  })

  const now = new Date()
  const dateStr = now.toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' })

  function goTo(product: 'isms' | 'privacy' | 'cloud') {
    setProduct(product)
    navigate('/overview')
  }

  const ismsColor = PRODUCT_COLORS.isms
  const privColor = PRODUCT_COLORS.privacy
  const cloudColor = PRODUCT_COLORS.cloud

  return (
    <Box sx={{
      height: 'calc(100vh - 48px)',
      display: 'flex',
      flexDirection: 'column',
      gap: 2,
      overflow: 'hidden',
    }}>
      {/* Header */}
      <Box sx={{ display: 'flex', alignItems: 'flex-end', justifyContent: 'space-between', flexShrink: 0 }}>
        <Box>
          <Typography variant="h5" sx={{ fontWeight: 700, lineHeight: 1, mb: 0.3, fontSize: '1.2rem' }}>
            ISMS CORE Platform
          </Typography>
          <Typography variant="caption" sx={{ color: 'text.secondary', fontSize: '0.74rem' }}>
            Information Security &amp; Privacy Compliance — {dateStr}
          </Typography>
        </Box>
        {user && (
          <Typography variant="caption" sx={{ color: 'text.disabled', fontSize: '0.68rem' }}>
            {user.email}
          </Typography>
        )}
      </Box>

      {/* Search bar */}
      <Box sx={{ flexShrink: 0 }}>
        <TextField
          fullWidth
          placeholder="Search policies and implementation guides across all standards…"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleSearch()}
          size="small"
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <SearchOutlined fontSize="small" sx={{ color: 'text.disabled' }} />
              </InputAdornment>
            ),
            endAdornment: (
              <InputAdornment position="end">
                <IconButton size="small" onClick={handleSearch} disabled={searchQuery.trim().length < 2}>
                  <SearchOutlined fontSize="small" />
                </IconButton>
              </InputAdornment>
            ),
          }}
          sx={{
            '& .MuiOutlinedInput-root': {
              bgcolor: 'background.paper',
              fontSize: '0.88rem',
            },
          }}
        />
      </Box>

      {/* 3 product cards */}
      <Box sx={{ display: 'flex', gap: 2, flexShrink: 0 }}>

        {/* ISMS — wider (50%) */}
        <Box sx={{ flex: '0 0 48%' }}>
          <ProductCard product="isms" loading={isLoading} onClick={() => goTo('isms')}>
            {/* Stats row */}
            <Box sx={{ display: 'flex', gap: 2.5, mb: 2 }}>
              <Box>
                <Num value={summary?.isms.groups} color={ismsColor} loading={isLoading} />
                <Typography variant="caption" sx={{ fontSize: '0.63rem', color: 'text.secondary' }}>Control Groups</Typography>
              </Box>
              <Box>
                <Num value={summary?.isms.policies} color={ismsColor} loading={isLoading} />
                <Typography variant="caption" sx={{ fontSize: '0.63rem', color: 'text.secondary' }}>Policies</Typography>
              </Box>
              <Box>
                <Num value={summary?.isms.imps} color={ismsColor} loading={isLoading} />
                <Typography variant="caption" sx={{ fontSize: '0.63rem', color: 'text.secondary' }}>Impl. Guides</Typography>
              </Box>
              <Box>
                <Num
                  value={summary?.isms.open_gaps}
                  color={(summary?.isms.open_gaps ?? 0) > 0 ? '#FFC000' : '#70AD47'}
                  loading={isLoading}
                />
                <Typography variant="caption" sx={{ fontSize: '0.63rem', color: 'text.secondary' }}>Open Gaps</Typography>
              </Box>
            </Box>

            {/* Coverage bars */}
            <CoverageBar label="Framework coverage" pct={summary?.isms.fw_coverage_pct} color={ismsColor} loading={isLoading} />
            <CoverageBar label="Operational coverage" pct={summary?.isms.op_coverage_pct} color="#70AD47" loading={isLoading} />
          </ProductCard>
        </Box>

        {/* Privacy */}
        <Box sx={{ flex: 1 }}>
          <ProductCard product="privacy" loading={isLoading} onClick={() => goTo('privacy')}>
            <Box sx={{ display: 'flex', gap: 2.5, mb: 2 }}>
              <Box>
                <Num value={summary?.privacy.groups} color={privColor} loading={isLoading} />
                <Typography variant="caption" sx={{ fontSize: '0.63rem', color: 'text.secondary' }}>Control Groups</Typography>
              </Box>
              <Box>
                <Num value={summary?.privacy.policies} color={privColor} loading={isLoading} />
                <Typography variant="caption" sx={{ fontSize: '0.63rem', color: 'text.secondary' }}>Policies</Typography>
              </Box>
              <Box>
                <Num value={summary?.privacy.imps} color={privColor} loading={isLoading} />
                <Typography variant="caption" sx={{ fontSize: '0.63rem', color: 'text.secondary' }}>Impl. Guides</Typography>
              </Box>
            </Box>
            <StatusDot ok={(summary?.privacy.policies ?? 0) > 0} label={`Policies (${summary?.privacy.policies ?? '…'})`} loading={isLoading} />
            <StatusDot ok={(summary?.privacy.imps ?? 0) > 0} label={`Implementation Guides (${summary?.privacy.imps ?? '…'})`} loading={isLoading} />
          </ProductCard>
        </Box>

        {/* Cloud */}
        <Box sx={{ flex: 1 }}>
          <ProductCard product="cloud" loading={isLoading} onClick={() => goTo('cloud')}>
            <Box sx={{ display: 'flex', gap: 2.5, mb: 2 }}>
              <Box>
                <Num value={summary?.cloud.groups} color={cloudColor} loading={isLoading} />
                <Typography variant="caption" sx={{ fontSize: '0.63rem', color: 'text.secondary' }}>Control Groups</Typography>
              </Box>
              <Box>
                <Num value={summary?.cloud.policies} color={cloudColor} loading={isLoading} />
                <Typography variant="caption" sx={{ fontSize: '0.63rem', color: 'text.secondary' }}>Policies</Typography>
              </Box>
              <Box>
                <Num value={summary?.cloud.imps} color={cloudColor} loading={isLoading} />
                <Typography variant="caption" sx={{ fontSize: '0.63rem', color: 'text.secondary' }}>Impl. Guides</Typography>
              </Box>
            </Box>
            <StatusDot ok={(summary?.cloud.policies ?? 0) > 0} label={`Policies (${summary?.cloud.policies ?? '…'})`} loading={isLoading} />
            <StatusDot ok={(summary?.cloud.imps ?? 0) > 0} label={`Implementation Guides (${summary?.cloud.imps ?? '…'})`} loading={isLoading} />
          </ProductCard>
        </Box>

      </Box>

      {/* Connector summary bar */}
      <Box
        onClick={() => navigate('/connectors')}
        sx={{
          flexShrink: 0,
          display: 'flex', alignItems: 'center', gap: 2.5,
          px: 2, py: 1, borderRadius: 1.5, cursor: 'pointer',
          border: '1px solid', borderColor: 'divider',
          bgcolor: 'background.paper',
          transition: 'all 0.12s',
          '&:hover': { borderColor: 'text.secondary', bgcolor: 'action.hover' },
        }}
      >
        <ElectricalServicesOutlined sx={{ fontSize: 18, color: 'text.secondary', flexShrink: 0 }} />
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.75 }}>
          {isLoading
            ? <Skeleton variant="text" width={16} height={22} />
            : <Typography variant="subtitle2" sx={{ fontWeight: 700, fontSize: '1rem', lineHeight: 1, color: (summary?.connectors?.active ?? 0) > 0 ? '#70AD47' : 'text.disabled' }}>
                {summary?.connectors?.active ?? 0}
              </Typography>
          }
          <Typography variant="caption" sx={{ fontSize: '0.7rem', color: 'text.secondary' }}>Active Connectors</Typography>
        </Box>
        <Box sx={{ width: '1px', height: 18, bgcolor: 'divider' }} />
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.75 }}>
          {isLoading
            ? <Skeleton variant="text" width={24} height={22} />
            : <Typography variant="subtitle2" sx={{ fontWeight: 700, fontSize: '1rem', lineHeight: 1, color: 'text.primary' }}>
                {summary?.connectors?.evidence_items ?? 0}
              </Typography>
          }
          <Typography variant="caption" sx={{ fontSize: '0.7rem', color: 'text.secondary' }}>Evidence Items</Typography>
        </Box>
        <Box sx={{ flex: 1 }} />
        <ArrowForwardOutlined sx={{ fontSize: 14, color: 'text.disabled' }} />
      </Box>

      {/* Platform tools */}
      <Box sx={{ flexShrink: 0 }}>
        <Typography variant="caption" sx={{ color: 'text.disabled', fontSize: '0.63rem', textTransform: 'uppercase', letterSpacing: '0.08em', display: 'block', mb: 0.75 }}>
          Platform Tools
        </Typography>
        <Box sx={{ display: 'flex', gap: 1, flexWrap: 'wrap' }}>
          {PLATFORM_TOOLS.map((tool) => (
            <Tooltip key={tool.path} title={tool.label}>
              <Box
                onClick={() => navigate(tool.path)}
                sx={{
                  display: 'flex', alignItems: 'center', gap: 0.75,
                  px: 1.5, py: 0.7, borderRadius: 1.5, cursor: 'pointer',
                  border: '1px solid', borderColor: 'divider',
                  bgcolor: 'background.paper',
                  transition: 'all 0.12s',
                  '&:hover': { borderColor: 'text.secondary', bgcolor: 'action.hover' },
                }}
              >
                <Box sx={{ color: 'text.secondary', display: 'flex' }}>{tool.icon}</Box>
                <Typography variant="caption" sx={{ fontSize: '0.73rem', color: 'text.secondary', fontWeight: 500 }}>
                  {tool.label}
                </Typography>
              </Box>
            </Tooltip>
          ))}
        </Box>
      </Box>

    </Box>
  )
}
