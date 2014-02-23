""" This module contains the entry points for the salt adapters.
"""

import toast

def top(path, grains=None, **kwargs):
    """ The main entry point for the external_tops extension
    """
    grains = grains if grains else {}
    toaster = toast.Toaster(path, grains)
    return toaster.states()

def pillar(path, grains=None, **kwargs):
    """ The main entry point for the ext_pillar extension
    """
    grains = grains if grains else {}
    toaster = toast.Toaster(path, grains)
    return toaster.pillars()