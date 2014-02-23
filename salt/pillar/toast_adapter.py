import toast.salt_entry

__virtualname__ = 'toast'

def __virtual__():
    import toast
    return __virtualname__

def ext_pillar(minion_id, pillar, **kwargs):
    path = __opts__['master_tops']['toast']['path']
    return toast.salt_entry.pillar(path, minion_id, pillar, **kwargs)

