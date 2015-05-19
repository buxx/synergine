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

**_mechanism**

:ref:`Mechanism <Components.Mechanism>` class can be specified in ``_mechanism`` class attribute. Event parameters will be prepared by this Mechanism.

**_concern**

Event can observe specified objects. You can specify :ref:`COL <Components.COL>` identifier in the ``_concern`` class attribute. By default, ``Event`` observe all synergies objects.

**_prepare**

Write here conditions who determine if looked object is concerned by this event. If yes, you must return parameters given to :ref:`Action <Components.Action>`. If event is not concerned, you must raise :ref:`NotConcernedEvent exception <Components.Exceptions>`.

The Event class
+++++++++++++++

Events must be child class of ``synergine.synergy.event.Event.Event``:

.. autoclass:: synergine.synergy.event.Event.Event
   :members:
   :undoc-members:
   :private-members:

Example
+++++++

You can found :ref:`here <LifeGame.Event.Born>` an example of implemented ``Event``:

.. include:: ../../modules/lifegame/synergy/event/GoodConditionToBornEvent.py
   :literal:

.. _Components.Action:

Action
------

``Action`` own the code intended for modify synergies objects.

**_listen**

They have to listen an :ref:`Event <Components.Event>`. Action ``_listen`` class attribute must be contain an :ref:`Event <Components.Event>` class.

**_depend**

If the ``Action`` must be executed after other actions, you can list them in Action ``_depend`` class attribute.

**run**

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

You can found :ref:`here <LifeGame.Action.Born>` an example of implemented ``Action``:

.. include:: ../../modules/lifegame/synergy/event/BornAction.py
   :literal:

Mechanism
=========

Mechanism prepare data for associated :ref:`Events <Components.Event>`. It's role is to compute once what multiple :ref:`Events <Components.Event>` will need.

Mechanisms must be child of:

.. autoclass:: synergine.core.simulation.mechanism.Mechanism.Mechanism
   :members:
   :undoc-members:
   :private-members:

Example
-------

You can found :ref:`here <LifeGame.Action.Born>` an example of implemented ``Mechanism``:

.. include:: ../../modules/xyzworld/mechanism/AroundMechanism.py
   :literal:

.. _Components.Context:
.. _Components.Metas:

Context, Metas
==============

Context is designed to contain data (in ``metas attribute``) and method representing simulation. You can found information about it :ref:`here <HowItsWorkrking.Context_Metas>`, example of Context class :ref:`here <ModuleXyzworld.Context>` and usage example in :ref:`HowTo documentation<LifeGame>`.

.. _Components.COL:

COL
----

For performance reason, an event can compute for specified list of :ref:`SynergyObject <Components.SynergyObject>`. When his ``_concern`` attribute is configured with a ``COL_XXX``, only ``SynergyObjects`` contained in this ``COL_XXX`` will be concerned.

You can see ``_concern`` usage example :ref:`here <LifeGame.EventActions>`.

.. _Components.SynergyObject:

SynergyObject
=============

SynergyObject is a representation of your simulation subject.

.. autoclass:: synergine.synergy.object.SynergyObject.SynergyObject
   :members:
   :undoc-members:
   :private-members:


.. autoclass:: synergine.core.Test.Test
   :members:
   :undoc-members:
   :private-members:

Display
=======

Ready-to-use DisplayObjects are available:

* xyzworld.display.Pygame.Pygame (you can found example usage :ref:`here <LifeGame.Pygame>`)
* xywold.display.CursesDisplay.CursesDisplay

.. _Components.Signals:

Signals
=======

Hook are available. To trig hook:

>>> Signals.signal(<HOOK NAME>).send(<PARAMETERS>)

Where ``<HOOK NAME>`` is anything you want and ``<PARAMETERS>`` according your callbacks parameters definitions.

To define callback:

>>> Signals.signal(<HOOK NAME>).connect(<A CALLABLE>)

Existing signals are (list of hook names):

* An ``Action`` class: Trig just after ``Action`` have been executed. Callback parameters definition is ``.send(obj: SynergyObject, context: Context)``
* synergine.synergy.collection.SynergyCollection.SynergyCollection.SIGNAL_ADD_OBJECT: When object add to a ``SynergyCollection``. Callback parameters definition is ``.send(collection:: SynergyCollection, obj: SynergyObject)``
* synergine.synergy.collection.SynergyCollection.SynergyCollection.SIGNAL_REMOVE_OBJECT: When object removed from a ``SynergyCollection``. Callback parameters definition is ``.send(collection:: SynergyCollection, obj: SynergyObject)``

.. _Components.Exceptions:


Exceptions
==========

Available Exception:

.. automodule:: synergine.core.exceptions
   :members:
   :undoc-members:
