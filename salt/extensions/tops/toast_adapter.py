import toast.salt_entry

__virtualname__ = 'toast'

def __virtual__():
    import toast
    return __virtualname__

def top(**kwargs):
    return toast.salt_entry.top(__opts__=__opts__, **kwargs)
