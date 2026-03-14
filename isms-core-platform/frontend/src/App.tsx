import { Navigate, Route, Routes } from 'react-router-dom'
import { useAuth } from './store/AuthContext'
import { ProductProvider } from './store/ProductContext'
import Layout from './components/Layout'
import Login from './pages/Login'
import Home from './pages/Home'
import Overview from './pages/Overview'
import Coverage from './pages/Coverage'
import Gaps from './pages/Gaps'
import Controls from './pages/Controls'
import ControlDetail from './pages/ControlDetail'
import Assessments from './pages/Assessments'
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

function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const { isAuthenticated } = useAuth()
  return isAuthenticated ? <>{children}</> : <Navigate to="/login" replace />
}

export default function App() {
  return (
    <ProductProvider>
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
        <Route path="*" element={<Navigate to="/" replace />} />
      </Route>
    </Routes>
    </ProductProvider>
  )
}
