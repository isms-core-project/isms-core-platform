import { createContext, useContext, useState } from 'react'

export type Product = 'isms' | 'privacy' | 'cloud'

// ISMS-only tier filter — only meaningful when product === 'isms'
export type IsmsTier = 'all' | 'framework' | 'operational'

export const PRODUCT_COLORS: Record<Product, string> = {
  isms:    '#4472C4',
  privacy: '#7030A0',
  cloud:   '#00897B',
}

export const PRODUCT_LABELS: Record<Product, string> = {
  isms:    'ISMS',
  privacy: 'PRIVACY',
  cloud:   'CLOUD',
}

export const PRODUCT_SUBTITLES: Record<Product, string> = {
  isms:    'ISO 27001:2022 + Amd.1',
  privacy: 'ISO 27701:2025 Ed. 2',
  cloud:   'ISO 27017:2015',
}

interface ProductContextValue {
  product: Product
  setProduct: (p: Product) => void
  ismsTier: IsmsTier
  setIsmsTier: (t: IsmsTier) => void
}

const ProductContext = createContext<ProductContextValue>({
  product: 'isms',
  setProduct: () => {},
  ismsTier: 'all',
  setIsmsTier: () => {},
})

const VALID: Product[] = ['isms', 'privacy', 'cloud']
const VALID_TIER: IsmsTier[] = ['all', 'framework', 'operational']

export function ProductProvider({ children }: { children: React.ReactNode }) {
  const [product, setProductState] = useState<Product>(() => {
    const stored = localStorage.getItem('isms_product') as Product
    return VALID.includes(stored) ? stored : 'isms'
  })

  const [ismsTier, setIsmsTierState] = useState<IsmsTier>(() => {
    const stored = localStorage.getItem('isms_tier') as IsmsTier
    return VALID_TIER.includes(stored) ? stored : 'all'
  })

  function setProduct(p: Product) {
    setProductState(p)
    localStorage.setItem('isms_product', p)
  }

  function setIsmsTier(t: IsmsTier) {
    setIsmsTierState(t)
    localStorage.setItem('isms_tier', t)
  }

  return (
    <ProductContext.Provider value={{ product, setProduct, ismsTier, setIsmsTier }}>
      {children}
    </ProductContext.Provider>
  )
}

export function useProduct() {
  return useContext(ProductContext)
}
