.. Toast documentation master file, created by
   sphinx-quickstart on Sun Feb 23 18:48:34 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Toast's documentation!
=================================

Toast is an extension for salt. It contains a external_tops extension and an
external_pillar extension. The main purpose of toast is to provide a completely
customisable way of including states depending on the grains of minions. Toast
is more powerful than the normal pillar state files, as it exposes a full
python interface to you. This allows you to create a hierachy of minions,
simply by implementing classes and subclasses. The sky is the limit, as long as
you still return a list of states and a pillar dictionary!

Contents:

.. toctree::
    :maxdepth: 2

    installation
    api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

