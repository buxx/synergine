How it's working
****************

Introduction
============

Synergine is designed to simulate interaction between object in time. With iterations (``cycles``) synergine execute your events and associated actions.

Synergies object
================

Your simulation have to be populated by ``SynergyObject``. These objects will evolute according of your events.

You can found usage example in :ref:`LifeGame HowTo <LifeGame.Cell>`.

Cycles
------

Each cycle, synergine will repeat this procedure::

    # Main process
    actions = empty list

    # Sub processes
    for each mechanism in mechanisms:
        for each event in events associated to mechanism:
            if event is trig:
                add event actions to actions

    # Main processes
    for each action in actions:
        execute action

Mechanisms, Events and Actions
==============================

Your synergies objects will evolute according of your event, when actions are executed. To optimize compute timing, mechanisms have been introduced. The principle: One mechanism compute once what multiple events need.

You can found usage example in :ref:`LifeGame HowTo <LifeGame.EventActions>`.

Context, Metas
==============

.. _HowItsWorkrking.Context_Metas:

To optimize parallel computing, simulation information have to be stored in :ref:`metas data <Components.Metas>`. The data are used by Mechanisms and Event to do their job.

You can find usage example of metas data in:

* :ref:`LifeGame Cell <LifeGame.Cell>` where metas data are feed (see ``self.add_col``, ``self.remove_col``, ``self.add_state``, ``self.remove_state`` usages).
* :ref:`LifeGame Born Event <LifeGame.Event.Born>` where ``Event`` concern the ``COL_DIED`` collection of synergies object.
* :ref:`LifeGame AliveAroundEvent <LifeGame.Event.AliveAroundEvent>` where ``_get_alive_cell_around_count`` method read metas data (see ``context.metas`` usage)
