.. _Components:

Components
**********

.. _Components.Event_Actions:

Event and Action
================

.. _Components.Event:

Event
-----

Event job is to trig Actions when conditions matches.

_mechanism
++++++++++

:ref:`Mechanism <Components.Mechanism>` class must be specified in ``_mechanism`` class attribute. Event parameters will be prepared by this Mechanism.

_concern
++++++++

Event only observe concerned objects. You must specify :ref:`COL <Components.COL>` identifier in the ``_concern`` class attribute.

TODO: COL

_prepare
++++++++

You must override this method and write your conditions to trig associated Actions. If event is not concerned, you
must raise :ref:`NotConcernedEvent exception <Components.Exceptions>`.

The Event class
+++++++++++++++

Events must be child class of ``synergine.synergy.event.Event.Event``:

.. autoclass:: synergine.synergy.event.Event.Event
   :members:
   :undoc-members:
   :private-members:

.. _Components.Action:

Example
+++++++

You can found :ref:`here <LifeGame.Event.Born>` an example of implemented Event:

.. include:: ../../modules/lifegame/synergy/event/GoodConditionToBornEvent.py
   :literal:

Action
------

``Action`` own the code intended for modify synergies objects.

_listen
+++++++

They have to listen an :ref:`Event <Components.Event>`. Action ``_listen`` class attribute must be contain an :ref:`Event <Components.Event>` class.

_depend
+++++++

If the ``Action`` must be executed after other actions, you can list them in Action ``_depend`` class attribute.

Run
++++

The execution code of ``Action`` have to be write in ``run`` method.

The Action class
++++++++++++++++

Actions must be child class of ``synergine.synergy.event.Action.Action``.

.. autoclass:: synergine.synergy.event.Action.Action
   :members:
   :undoc-members:
   :private-members:

.. _Components.Mechanism:

Example
+++++++

You can found :ref:`here <LifeGame.Action.Born>` an example of implemented Event:

.. include:: ../../modules/lifegame/synergy/event/BornAction.py
   :literal:

Mechanism
=========

Mechanism prepare data for associated :ref:`Events <Components.Event>`. It's role is to compute once what multiple :ref:`Events <Components.Event>` will need.

.. _Components.Context:

Context
=======

See [LINK] here for more details.

.. _Components.Metas:

Metas
-----

.. _Components.COL:

COL
----


SynergyObject
=============

Display
=======

Signals
=======

.. _Components.Exceptions:

Exceptions
==========
