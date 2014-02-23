import toast.salt_entry

__virtualname__ = 'toast'

def __virtual__():
    import toast
    return __virtualname__

def ext_pillar(minion_id, pillar, **kwargs):
    return toast.salt_entry.pillar(
        __opts__=__opts__,
        minion_id=minion_id,
        pillar=pillar,
        **kwargs
    )

