import { HttpInterceptorFn, HttpRequest, HttpHandlerFn, HttpErrorResponse } from '@angular/common/http'
import { inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { catchError, switchMap, throwError, BehaviorSubject, filter, take } from 'rxjs'
import { TokenStoreService } from '../services/token-store.service'

interface TokenResponse { access_token: string }

let isRefreshing = false
const refreshSubject = new BehaviorSubject<string | null>(null)

export const authInterceptor: HttpInterceptorFn = (req: HttpRequest<unknown>, next: HttpHandlerFn) => {
  const tokenStore = inject(TokenStoreService)
  const token = tokenStore.get()

  const authedReq = token
    ? req.clone({ setHeaders: { Authorization: `Bearer ${token}` } })
    : req

  return next(authedReq).pipe(
    catchError((err: HttpErrorResponse) => {
      if (err.status !== 401) return throwError(() => err)
      // Don't retry when the refresh endpoint itself returns 401
      if (req.url.includes('/auth/refresh')) return throwError(() => err)

      if (isRefreshing) {
        return refreshSubject.pipe(
          filter(t => t !== null),
          take(1),
          switchMap(newToken =>
            next(req.clone({ setHeaders: { Authorization: `Bearer ${newToken!}` } }))
          )
        )
      }

      isRefreshing = true
      refreshSubject.next(null)

      const http = inject(HttpClient)
      return http.post<TokenResponse>('/api/v1/auth/refresh', {}, { withCredentials: true }).pipe(
        switchMap(res => {
          tokenStore.set(res.access_token)
          isRefreshing = false
          refreshSubject.next(res.access_token)
          return next(req.clone({ setHeaders: { Authorization: `Bearer ${res.access_token}` } }))
        }),
        catchError(refreshErr => {
          isRefreshing = false
          tokenStore.set(null)
          window.location.href = '/login'
          return throwError(() => refreshErr)
        })
      )
    })
  )
}
