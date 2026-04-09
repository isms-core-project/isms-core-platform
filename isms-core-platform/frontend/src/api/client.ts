import axios from 'axios'
import { tokenStore } from './tokenStore'

export const client = axios.create({
  baseURL: '/api/v1',
  headers: { 'Content-Type': 'application/json' },
  withCredentials: true,   // send HttpOnly cookies (needed for same-origin refresh)
})

// Attach access token from memory on every request
client.interceptors.request.use((config) => {
  const token = tokenStore.get()
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// 401 handling: try silent refresh once, replay the original request, then give up
let isRefreshing = false
let failedQueue: Array<{ resolve: (t: string) => void; reject: (e: unknown) => void }> = []

function processQueue(err: unknown, token: string | null) {
  failedQueue.forEach((p) => (err ? p.reject(err) : p.resolve(token!)))
  failedQueue = []
}

client.interceptors.response.use(
  (res) => res,
  async (err) => {
    const original = err.config
    if (err.response?.status !== 401 || original._retry) {
      return Promise.reject(err)
    }

    if (isRefreshing) {
      // Queue this request until the in-flight refresh completes
      return new Promise<string>((resolve, reject) => {
        failedQueue.push({ resolve, reject })
      })
        .then((token) => {
          original.headers.Authorization = `Bearer ${token}`
          return client(original)
        })
        .catch((e) => Promise.reject(e))
    }

    original._retry = true
    isRefreshing = true

    try {
      const { data } = await axios.post<{ access_token: string }>(
        '/api/v1/auth/refresh',
        {},
        { withCredentials: true },
      )
      tokenStore.set(data.access_token)
      processQueue(null, data.access_token)
      original.headers.Authorization = `Bearer ${data.access_token}`
      return client(original)
    } catch (refreshErr) {
      processQueue(refreshErr, null)
      tokenStore.set(null)
      window.location.href = '/login'
      return Promise.reject(refreshErr)
    } finally {
      isRefreshing = false
    }
  },
)
