import { inject } from '@angular/core'
import { CanActivateFn, Router } from '@angular/router'
import { AuthService } from '../services/auth.service'

export const authGuard: CanActivateFn = async () => {
  const auth   = inject(AuthService)
  const router = inject(Router)

  await auth.init()

  if (auth.isAuthenticated()) return true

  // Reset so the next login triggers a fresh refresh call instead of the
  // cached (failed) init promise, preventing the "works once, fails once" loop.
  auth.resetInit()
  return router.createUrlTree(['/login'])
}
