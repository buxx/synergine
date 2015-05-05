HowTo Project: LifeGame
***********************

Objective
=========

This howto will help you to discover synergine with a simple implementation. We will only show you the code of main
logic. But all not displayed code here is described in main documentation. TODO: lien vers builtin modules

The howto project implement the "Conway's Game of Life".

From Wikipedia, the free encyclopedia::

   The Game of Life, also known simply as Life, is a cellular automaton devised by
   the British mathematician John Horton Conway in 1970.

   The "game" is a zero-player game, meaning that its evolution is determined by
   its initial state, requiring no further input. One interacts with the Game of
   Life by creating an initial configuration and observing how it evolves or, for
   advanced players, by creating patterns with particular properties.

Content of simulation
=====================

Our simulation will simply implement a basic pattern of "Conway's Game of Life" and visualisation tools.

Simulation
----------

.. Note::

    This project wil use some code of builtin module "xyzworld". TODO: link

The objective is to implement the rules of "Conway's Game of Life".
From Wikipedia, the free encyclopedia::

   The universe of the Game of Life is an infinite two-dimensional orthogonal
   grid of square cells, each of which is in one of two possible states, alive
   or dead. Every cell interacts with its eight neighbours, which are the
   cells that are horizontally, vertically, or diagonally adjacent. At each
   step in time, the following transitions occur:

   1. Any live cell with fewer than two live neighbours dies, as if caused by
      under-population.
   2. Any live cell with two or three live neighbours lives on to the next generation.
   3. Any live cell with more than three live neighbours dies, as if by overcrowding.
   4. Any dead cell with exactly three live neighbours becomes a live cell, as if by
      reproduction.

   The initial pattern constitutes the seed of the system. The first generation
   is created by applying the above rules simultaneously to every cell in the
   seed—births and deaths occur simultaneously, and the discrete moment at which
   this happens is sometimes called a tick (in other words, each generation is a
   pure function of the preceding one). The rules continue to be applied repeatedly
   to create further generations.

Additional features
-------------------

In additional of "Conway's Game of Life" rules, we will represent differently in our 2d graphic output:

* A just born cell
* A born cell since 2 cycles
* A born cell since more 2 cycles

SynergyObjects
--------------

We need: A Cell.

.. include:: ../../modules/lifegame/synergy/object/Cell.py
   :literal:

And no more for our SynergyObjects.

As you can see, our Cell class is a child class of xyzworld.SynergyObject.SynergyObject. Let see it's definition, just for know:

.. autoclass:: xyzworld.SynergyObject.SynergyObject
   :members:
   :undoc-members:
   :private-members:

Events and Actions
------------------

Events/Actions will be "born" and "die".

Born
++++

The born event:

.. include:: ../../modules/lifegame/synergy/event/GoodConditionToBornEvent.py
   :literal:

And his action:

.. include:: ../../modules/lifegame/synergy/event/BornAction.py
   :literal:

Die
++++

The die event:

.. include:: ../../modules/lifegame/synergy/event/NotGoodConditionToPersistEvent.py
   :literal:

And his action:

.. include:: ../../modules/lifegame/synergy/event/DieAction.py
   :literal:

AroundMechanism
+++++++++++++++

As you can see, these events uses the AroundMechanism. This mechanism prepare for events the list of object ids who are
around the observed object.

TODO: AroundMechanism

Collection
----------

Theses Cells must be contained by a Collection.

.. automodule:: lifegame.synergy.collection.LifeGameCollection
   :members:
   :undoc-members:
   :private-members:

The collection must have a configuration (to populate his synergies objects).

.. automodule:: lifegame.synergy.collection.LifeGameCollectionConfiguration
   :members:
   :undoc-members:
   :private-members:

And an Simulation class.

.. automodule:: lifegame.synergy.LifeGameSimulation
   :members:
   :undoc-members:
   :private-members:

Foo
----

Done ! All needed algorithms are here. Let's go see it:

TODO: print avec nombre de ellules en vie/morte.

Outputs
=======

2D pygame
---------

.. figure::  ../images/synergine_lifegame.gif
   :align:   center

   LifeGame simulation capture of 2D pygame output.


Curses
------

Plot
----


