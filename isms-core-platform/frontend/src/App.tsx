import { lazy, Suspense } from 'react'
import { Navigate, Route, Routes } from 'react-router-dom'
import { useAuth } from './store/AuthContext'
import { ProductProvider } from './store/ProductContext'
import { ProjectProvider } from './store/ProjectContext'
import Layout from './components/Layout'
import Login from './pages/Login'
import Home from './pages/Home'
import Overview from './pages/Overview'
import Coverage from './pages/Coverage'
import Gaps from './pages/Gaps'
import Controls from './pages/Controls'
import ControlDetail from './pages/ControlDetail'
import Assessments from './pages/Assessments'
import CollectionDetail from './pages/CollectionDetail'
import Policies from './pages/Policies'
import Search from './pages/Search'
import Evidence from './pages/Evidence'
import Graph from './pages/Graph'
import Admin from './pages/Admin'
import System from './pages/System'
import QA from './pages/QA'
import Generators from './pages/Generators'
import Compass from './pages/Compass'
import FrameworkControlDetail from './pages/FrameworkControlDetail'
import Report from './pages/Report'
import Risk from './pages/Risk'
import Connectors from './pages/Connectors'
import Nis2 from './pages/Nis2'
import Dora from './pages/Dora'
import UkNis from './pages/UkNis'
import UkOperationalResilience from './pages/UkOperationalResilience'
import CyfunBe from './pages/CyfunBe'
import BafinBait from './pages/BafinBait'
import CssfLu from './pages/CssfLu'
import AcnIt from './pages/AcnIt'
import Cis from './pages/Cis'
import Bsi from './pages/Bsi'
import Tisax from './pages/Tisax'
import Ndsg from './pages/Ndsg'
import Isg from './pages/Isg'
import Cra from './pages/Cra'
import AiAct from './pages/AiAct'
import NistAiRmf from './pages/NistAiRmf'
import CloudSovereignty from './pages/CloudSovereignty'
import Csrm from './pages/Csrm'
import Projects from './pages/Projects'
import ProjectDetail from './pages/ProjectDetail'
import Organisations from './pages/Organisations'
import RiskRegister from './pages/RiskRegister'
import Remediation from './pages/Remediation'
import Metrics from './pages/Metrics'
import Bia from './pages/Bia'
import Ebios from './pages/Ebios'
import Tprm from './pages/Tprm'
import CustomFrameworks from './pages/CustomFrameworks'
import FrameworkTracker from './pages/FrameworkTracker'
import Help from './pages/Help'
import ThreatFeeds from './pages/ThreatFeeds'
import MitreAttack from './pages/MitreAttack'
import MitreAtlas from './pages/MitreAtlas'
import MitreGroups from './pages/MitreGroups'
import MitreSoftware from './pages/MitreSoftware'
import MitreCampaigns from './pages/MitreCampaigns'
import MitreHeatmap from './pages/MitreHeatmap'
import CVEExplorer from './pages/CVEExplorer'
import Glossary from './pages/Glossary'
import Cobit from './pages/Cobit'
import CsaCcm from './pages/CsaCcm'
import CsaAicm from './pages/CsaAicm'
import NistSp80053 from './pages/NistSp80053'
const NistCsf = lazy(() => import('./pages/NistCsf'))
const NistCsfReport = lazy(() => import('./pages/NistCsfReport'))

function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const { isAuthenticated, isLoading } = useAuth()
  if (isLoading) return null   // wait for silent refresh before deciding
  return isAuthenticated ? <>{children}</> : <Navigate to="/login" replace />
}

export default function App() {
  return (
    <ProductProvider>
    <ProjectProvider>
    <Routes>
      <Route path="/login" element={<Login />} />

      <Route
        path="/"
        element={
          <ProtectedRoute>
            <Layout />
          </ProtectedRoute>
        }
      >
        <Route index element={<Home />} />
        <Route path="overview" element={<Overview />} />
        <Route path="coverage" element={<Coverage />} />
        <Route path="gaps" element={<Gaps />} />
        <Route path="controls" element={<Controls />} />
        <Route path="controls/code/:code" element={<ControlDetail />} />
        <Route path="framework-controls/:code/:controlId" element={<FrameworkControlDetail />} />
        <Route path="controls/:id" element={<ControlDetail />} />
        <Route path="assessments" element={<Assessments />} />
        <Route path="collections/:id" element={<CollectionDetail />} />
        <Route path="policies" element={<Policies />} />
        <Route path="search" element={<Search />} />
        <Route path="evidence" element={<Evidence />} />
        <Route path="graph" element={<Graph />} />
        <Route path="admin" element={<Admin />} />
        <Route path="system" element={<System />} />
        <Route path="connectors" element={<Connectors />} />
        <Route path="qa" element={<QA />} />
        <Route path="generators" element={<Generators />} />
        <Route path="compass" element={<Compass />} />
        <Route path="report" element={<Report />} />
        <Route path="risk" element={<Risk />} />
        <Route path="nist-csf" element={<Suspense fallback={null}><NistCsf /></Suspense>} />
        <Route path="nist-csf/:id/report" element={<Suspense fallback={null}><NistCsfReport /></Suspense>} />
        <Route path="nis2" element={<Nis2 />} />
        <Route path="dora" element={<Dora />} />
        <Route path="uk-nis" element={<UkNis />} />
        <Route path="uk-op-resilience" element={<UkOperationalResilience />} />
        <Route path="cyfun-be" element={<CyfunBe />} />
        <Route path="bafin-bait" element={<BafinBait />} />
        <Route path="cssf-lu" element={<CssfLu />} />
        <Route path="acn-it" element={<AcnIt />} />
        <Route path="cis" element={<Cis />} />
        <Route path="bsi" element={<Bsi />} />
        <Route path="tisax" element={<Tisax />} />
        <Route path="ndsg" element={<Ndsg />} />
        <Route path="isg" element={<Isg />} />
        <Route path="cra" element={<Cra />} />
        <Route path="ai-act" element={<AiAct />} />
        <Route path="nist-ai-rmf" element={<NistAiRmf />} />
        <Route path="csa-ccm" element={<CsaCcm />} />
        <Route path="csa-aicm" element={<CsaAicm />} />
        <Route path="nist-800-53" element={<NistSp80053 />} />
        <Route path="eu-cloud-sov" element={<CloudSovereignty />} />
        <Route path="csrm" element={<Csrm />} />
        <Route path="projects" element={<Projects />} />
        <Route path="projects/:id" element={<ProjectDetail />} />
        <Route path="organisations" element={<Organisations />} />
        <Route path="risk-register" element={<RiskRegister />} />
        <Route path="remediation" element={<Remediation />} />
        <Route path="metrics" element={<Metrics />} />
        <Route path="bia" element={<Bia />} />
        <Route path="ebios" element={<Ebios />} />
        <Route path="tprm" element={<Tprm />} />
        <Route path="custom-frameworks" element={<CustomFrameworks />} />
        <Route path="framework-tracker" element={<FrameworkTracker />} />
        <Route path="help" element={<Help />} />
        <Route path="threat-feeds" element={<ThreatFeeds />} />
        <Route path="mitre-attack" element={<MitreAttack />} />
        <Route path="mitre-atlas" element={<MitreAtlas />} />
        <Route path="mitre-groups" element={<MitreGroups />} />
        <Route path="mitre-software" element={<MitreSoftware />} />
        <Route path="mitre-campaigns" element={<MitreCampaigns />} />
        <Route path="mitre-heatmap" element={<MitreHeatmap />} />
        <Route path="cve-explorer" element={<CVEExplorer />} />
        <Route path="glossary" element={<Glossary />} />
        <Route path="cobit" element={<Cobit />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Route>
    </Routes>
    </ProjectProvider>
    </ProductProvider>
  )
}
