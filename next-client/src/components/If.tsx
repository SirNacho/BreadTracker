import { PropsWithChildren } from 'react'

type Props = { condition: unknown }

export function If({ condition, children }: PropsWithChildren<Props>) {
  return !!condition ? <>{children}</> : null
}
