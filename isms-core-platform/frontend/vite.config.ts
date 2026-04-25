import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

const bambooFaviconPlugin = {
  name: 'bamboo-favicon',
  transformIndexHtml(html: string) {
    if (process.env.VITE_SECRET_THEME === 'bamboo') {
      return html.replace('/favicon.svg', '/favicon-bamboo.svg')
    }
    return html
  },
}

export default defineConfig({
  plugins: [react(), bambooFaviconPlugin],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    host: '0.0.0.0',
    port: 3000,
    proxy: {
      '/api': {
        target: process.env.VITE_BACKEND_URL || 'http://localhost:8000',
        changeOrigin: true,
      },
      '/health': {
        target: process.env.VITE_BACKEND_URL || 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
  build: {
    outDir: 'dist',
    sourcemap: false,
  },
})
