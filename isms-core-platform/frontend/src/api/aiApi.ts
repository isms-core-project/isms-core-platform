import { client } from './client'

export interface ChatMessage {
  role: 'user' | 'assistant'
  content: string
}

export type AiMode = 'assistant' | 'audit_prep' | 'gap_narrator'

export interface AiStatus {
  configured: boolean
  model: string
}

export const aiApi = {
  status: () =>
    client.get<AiStatus>('/ai/status').then((r) => r.data),

  /** Stream a chat response. Calls onChunk with each text fragment, onDone when finished. */
  streamChat: async (
    messages: ChatMessage[],
    contextId: string | null,
    mode: AiMode,
    onChunk: (text: string) => void,
    onError: (msg: string) => void,
    onDone: () => void,
    signal?: AbortSignal,
  ) => {
    const token = localStorage.getItem('access_token')
    const res = await fetch('/api/v1/ai/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        ...(token ? { Authorization: `Bearer ${token}` } : {}),
      },
      body: JSON.stringify({
        messages,
        context_type: contextId ? 'control' : 'general',
        context_id: contextId,
        mode,
      }),
      signal,
    })

    if (!res.ok) {
      onError(`HTTP ${res.status}`)
      onDone()
      return
    }

    const reader = res.body!.getReader()
    const decoder = new TextDecoder()
    let buf = ''

    while (true) {
      const { done, value } = await reader.read()
      if (done) break
      buf += decoder.decode(value, { stream: true })
      const lines = buf.split('\n')
      buf = lines.pop() ?? ''
      for (const line of lines) {
        if (!line.startsWith('data: ')) continue
        const payload = line.slice(6).trim()
        if (payload === '[DONE]') { onDone(); return }
        try {
          const obj = JSON.parse(payload)
          if (obj.text) onChunk(obj.text)
          if (obj.error) { onError(obj.error); onDone(); return }
        } catch { /* ignore malformed chunk */ }
      }
    }
    onDone()
  },
}
