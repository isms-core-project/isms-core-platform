import { Injectable } from '@angular/core'

@Injectable({ providedIn: 'root' })
export class TokenStoreService {
  private _token: string | null = null

  get(): string | null { return this._token }
  set(token: string | null): void { this._token = token }
}
