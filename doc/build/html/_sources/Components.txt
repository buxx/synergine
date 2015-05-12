.. _Components:

Components
**********

Event and Action
================

Event job is to trig Actions when wanted conditions are here [TODO réunis]. You can found here an example of implemented
Event.

_mechanism
---------

Mechanism class must be specified in ``_mechanism`` class attribute. Event parameters will be prepared by this Mechanism.

_concern
--------

Event only observe concerned objects. You must specify COL identifier in the ``_concern`` class attribute.

_prepare
--------

You must override this method and write your conditions to trig associated Actions. If event is not concerned, you
must raise NotConcernedEvent.

Mechanism
=========

Context
=======

Why a Context representation ?
------------------------------

SynergyObject
=============

Display
=======

Signals
=======

Exceptions
==========
