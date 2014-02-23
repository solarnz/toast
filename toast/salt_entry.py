""" This module contains the entry points for the salt adapters.
"""

import toast

def top(__opts__=None, grains=None, **kwargs):
    """ The main entry point for the external_tops extension
    """
    path = __opts__['master_tops']['toast']['path']
    grains = grains if grains else {}
    toaster = toast.Toaster(path, grains)
    return toaster.states()

def pillar(__opts__=None, minion_id=None, pillar=None, grains=None, **kwargs):
    """ The main entry point for the ext_pillar extension
    """
    # TODO: This should be read from the pillar config, not the master_tops
    # config.
    path = __opts__['master_tops']['toast']['path']
    grains = grains if grains else {}
    toaster = toast.Toaster(path, grains)
    return toaster.pillars()
