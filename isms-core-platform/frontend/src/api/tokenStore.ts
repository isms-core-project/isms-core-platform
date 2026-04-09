/**
 * In-memory access token store.
 * The access token is never written to localStorage — only held in memory
 * so it cannot be stolen via XSS. Survives React re-renders but not page reloads;
 * silent refresh (HttpOnly cookie) rehydrates it on reload.
 */
let _token: string | null = null

export const tokenStore = {
  get: (): string | null => _token,
  set: (token: string | null): void => { _token = token },
}
