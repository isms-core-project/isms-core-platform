import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'
import { TokenStoreService } from '../core/services/token-store.service'

export interface ChatMessage {
  role: 'user' | 'assistant'
  content: string
}

export type AiMode = 'assistant' | 'audit_prep' | 'gap_narrator'

export interface AiStatus {
  configured: boolean
  model: string
}

@Injectable({ providedIn: 'root' })
export class AiApiService {
  private http = inject(HttpClient)
  private tokenStore = inject(TokenStoreService)

  status(): Observable<AiStatus> {
    return this.http.get<AiStatus>('/api/v1/ai/status')
  }

  async streamChat(
    messages: ChatMessage[],
    contextId: string | null,
    mode: AiMode,
    onChunk: (text: string) => void,
    onError: (msg: string) => void,
    onDone: () => void,
    signal?: AbortSignal,
  ): Promise<void> {
    const token = this.tokenStore.get()
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
  }
}
