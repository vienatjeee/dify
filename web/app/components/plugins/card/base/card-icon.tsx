import { RiCheckLine } from '@remixicon/react'
import cn from '@/utils/classnames'

const Icon = ({
  className,
  src,
  installed = false,
}: {
  className?: string
  src: string
  installed?: boolean
}) => {
  return (
    <div
      className={cn('shrink-0 relative w-10 h-10 rounded-md bg-center bg-no-repeat bg-contain', className)}
      style={{
        backgroundImage: `url(${src})`,
      }}
    >
      {installed
        && <div className='flex justify-center items-center gap-2 absolute bottom-[-4px] right-[-4px] w-[18px] h-[18px] rounded-full border-2 border-components-panel-bg bg-state-success-solid'>
          <RiCheckLine className='w-3 h-3 text-text-primary-on-surface' />
        </div>
      }
    </div>
  )
}

export default Icon