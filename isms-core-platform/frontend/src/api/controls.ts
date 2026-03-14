import { client } from './client'
import type { ControlGroupList, ControlGroupRichDetail } from './types'

export interface FrameworkControlDetail {
  id: string
  control_id: string
  title: string
  description: string | null
  level: number
  sort_order: number
  control_type: string[]
  security_properties: string[]
  framework_code: string
  framework_name: string
  mappings: {
    framework: string
    framework_code: string
    control_id: string
    control_title: string
    mapping_type: string
    confidence: number
  }[]
}

export interface FrameworkControlItem {
  id: string
  control_id: string
  title: string
  description: string | null
  level: number
  sort_order: number
  parent_id: string | null
  control_type: string[]
  security_properties: string[]
}

export const controlsApi = {
  list: (params?: { section?: string; product?: string; product_family?: string }) =>
    client.get<ControlGroupList[]>('/controls/', { params }).then((r) => r.data),

  listByFrameworkCode: (code: string, level?: number) =>
    client.get<FrameworkControlItem[]>('/frameworks/by-code/controls', {
      params: { code, ...(level !== undefined ? { level } : {}) },
    }).then((r) => r.data),

  getByFrameworkCode: (code: string, controlId: string) =>
    client.get<FrameworkControlDetail>('/frameworks/by-code/control', {
      params: { code, control_id: controlId },
    }).then((r) => r.data),

  getById: (id: string) =>
    client.get<ControlGroupRichDetail>(`/controls/${id}`).then((r) => r.data),

  getByCode: (code: string) =>
    client.get<ControlGroupRichDetail>(`/controls/code/${code}`).then((r) => r.data),
}
