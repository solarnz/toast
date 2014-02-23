import toast.salt_entry

__virtualname__ = 'toast'

def __virtual__():
    import toast
    return __virtualname__

def top(**kwargs):
    path = __opts__['master_tops']['toast']['path']
    return toast.salt_entry.top(path, **kwargs)
