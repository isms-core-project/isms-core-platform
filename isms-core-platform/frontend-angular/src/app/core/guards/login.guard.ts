import { inject } from '@angular/core'
import { CanActivateFn, Router } from '@angular/router'
import { AuthService } from '../services/auth.service'

export const loginGuard: CanActivateFn = async () => {
  const auth   = inject(AuthService)
  const router = inject(Router)

  await auth.init()

  // Already authenticated — send straight to home, no login form needed.
  return auth.isAuthenticated() ? router.createUrlTree(['/']) : true
}
