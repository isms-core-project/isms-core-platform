interface BambooIconProps {
  size?: number
}

export function BambooIcon({ size = 32 }: BambooIconProps) {
  const w = Math.round(size * 18 / 28)
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 18 28"
      width={w}
      height={size}
      style={{ flexShrink: 0, userSelect: 'none', display: 'block' }}
    >
      {/* Left stalk — 3 segments */}
      <rect x="1.5" y="0.5"  width="5" height="9.5" rx="2.5" fill="#2E8B57"/>
      <rect x="0.5" y="9.5"  width="7" height="2"   rx="1"   fill="#1a6b3f"/>
      <rect x="1.5" y="11"   width="5" height="9.5" rx="2.5" fill="#2E8B57"/>
      <rect x="0.5" y="19.5" width="7" height="2"   rx="1"   fill="#1a6b3f"/>
      <rect x="1.5" y="21"   width="5" height="6.5" rx="2.5" fill="#2E8B57"/>

      {/* Right stalk — offset by 3px, 3 segments */}
      <rect x="11.5" y="3"    width="5" height="9.5" rx="2.5" fill="#3da369"/>
      <rect x="10.5" y="12"   width="7" height="2"   rx="1"   fill="#246b45"/>
      <rect x="11.5" y="13.5" width="5" height="9.5" rx="2.5" fill="#3da369"/>
      <rect x="10.5" y="22.5" width="7" height="2"   rx="1"   fill="#246b45"/>
      <rect x="11.5" y="24"   width="5" height="4"   rx="2"   fill="#3da369"/>

      {/* Leaves */}
      <path d="M6.5 6.5 Q10 4.5 12.5 7 Q9.5 8.5 6.5 6.5Z"   fill="#3da369" opacity="0.85"/>
      <path d="M6.5 16.5 Q3 14 0.5 16.5 Q3.5 19.5 6.5 16.5Z" fill="#2E8B57" opacity="0.85"/>
      <path d="M11.5 19 Q15.5 17 17.5 20 Q14 21.5 11.5 19Z"  fill="#3da369" opacity="0.85"/>
    </svg>
  )
}
