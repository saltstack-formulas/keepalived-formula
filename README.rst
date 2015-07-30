=======
keepalived
=======

Install, configure and run ``keepalived``.

.. note::

    See the full `Salt Formulas installation and usage instructions
    <http://docs.saltstack.com/en/latest/topics/development/conventions/formulas.html>`_.

Available states
================

.. contents::
    :local:

or the jinja template and the pillar for a salt approach.

``keepalived``
-----------

Install, configure and run ``keepalived`` service.

``keepalived.install``
-------------------

Install ``keepalived`` from packages.

``keepalived.config``
------------------

Slowly adding configuration options per the documents, not everything is available

To Do:
 - LVS configuration section

``keepalived.service``
-------------------

Make sure ``keepalived`` service is running.
