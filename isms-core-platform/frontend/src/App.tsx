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
import Cis from './pages/Cis'
import Bsi from './pages/Bsi'
import Tisax from './pages/Tisax'
import Ndsg from './pages/Ndsg'
import Cra from './pages/Cra'
import AiAct from './pages/AiAct'
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
const NistCsf = lazy(() => import('./pages/NistCsf'))
const NistCsfReport = lazy(() => import('./pages/NistCsfReport'))

function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const { isAuthenticated } = useAuth()
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
        <Route path="cis" element={<Cis />} />
        <Route path="bsi" element={<Bsi />} />
        <Route path="tisax" element={<Tisax />} />
        <Route path="ndsg" element={<Ndsg />} />
        <Route path="cra" element={<Cra />} />
        <Route path="ai-act" element={<AiAct />} />
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
        <Route path="*" element={<Navigate to="/" replace />} />
      </Route>
    </Routes>
    </ProjectProvider>
    </ProductProvider>
  )
}
