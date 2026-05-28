import { Injectable, signal } from '@angular/core'

export type Product = 'isms' | 'privacy' | 'cloud' | 'ai'
export type IsmsTier = 'all' | 'framework' | 'operational'

export const PRODUCT_COLORS: Record<Product, string> = {
  isms:    '#327df4',
  privacy: '#ba68c8',
  cloud:   '#29b6f6',
  ai:      '#ffa726',
}

export const PRODUCT_LABELS: Record<Product, string> = {
  isms:    'ISMS',
  privacy: 'PRIVACY',
  cloud:   'CLOUD',
  ai:      'AI',
}

export const PRODUCT_SUBTITLES: Record<Product, string> = {
  isms:    'ISO 27001:2022 + Amd.1',
  privacy: 'ISO 27701:2025 Ed. 2',
  cloud:   'ISO 27018:2025',
  ai:      'ISO 42001:2023',
}

const VALID_PRODUCTS: Product[] = ['isms', 'privacy', 'cloud', 'ai']
const VALID_TIERS: IsmsTier[]   = ['all', 'framework', 'operational']

@Injectable({ providedIn: 'root' })
export class ProductService {
  readonly product = signal<Product>(
    (() => {
      const s = localStorage.getItem('isms_product') as Product
      return VALID_PRODUCTS.includes(s) ? s : 'isms'
    })()
  )

  readonly ismsTier = signal<IsmsTier>(
    (() => {
      const s = localStorage.getItem('isms_tier') as IsmsTier
      return VALID_TIERS.includes(s) ? s : 'all'
    })()
  )

  setProduct(p: Product): void {
    this.product.set(p)
    localStorage.setItem('isms_product', p)
  }

  setIsmsTier(t: IsmsTier): void {
    this.ismsTier.set(t)
    localStorage.setItem('isms_tier', t)
  }
}
