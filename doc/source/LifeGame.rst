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

.. Note::

    Cell class is a child class of `xyzworld.SynergyObject.SynergyObject <ModuleXyzworld.html#xyzworld.SynergyObject.SynergyObject>`_.

And no more for our SynergyObjects.

Events and Actions
------------------

AliveAroundEvent
++++++++++++++++

Events/Actions will be "born" and "die". These actions will need to know how many alice cells are around the concerned
cell. So we write AliveAroundEvent event:

.. include:: ../../modules/lifegame/synergy/event/AliveAroundEvent.py
   :literal:

Ou born and die event will be child of this event.

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

As you can see, these events uses the `AroundMechanism <ModuleXyzworld.html#xyzworld.mechanism.AroundMechanism.AroundMechanism>`_. This mechanism prepare a list of object ids who are around the observed object.

Collection
----------

Our Cells must be contained by a Collection.

.. include:: ../../modules/lifegame/synergy/collection/LifeGameCollection.py
   :literal:

The collection must have a configuration (to populate his synergies objects).

.. include:: ../../modules/lifegame/synergy/collection/LifeGameCollectionConfiguration.py
   :literal:

And a Simulation container.

.. include:: ../../modules/lifegame/synergy/LifeGameSimulation.py
   :literal:

Additional features
-------------------

According to our additional features::

    In additional of "Conway's Game of Life" rules, we will represent differently in our 2d graphic output:

    * A just born cell
    * A born cell since 2 cycles
    * A born cell since more 2 cycles

We must add an Action who have to increment age of alive cells:

.. include:: ../../modules/lifegame/synergy/event/TimePassAction.py
   :literal:

Who listen a simple event:

.. include:: ../../modules/lifegame/synergy/event/TimePassEvent.py
   :literal:

Simple terminal
---------------

All needed algorithms are here. To be able to see something, we write a very simple output like this:

.. include:: ../../modules/lifegame/PrintTerminal.py
   :literal:

Let's go
--------

We now need to prepare configuration and run script for our simulation::

    from os import getcwd
    from sys import path as ppath
    from synergine.core.Core import Core

    # For now we update the python path. It will change in future version.
    ppath.insert(1, getcwd()+'/modules')

    from lifegame.PrintTerminal import PrintTerminal
    from lifegame.synergy.collection.LifeGameCollection import LifeGameCollection
    from lifegame.synergy.LifeGameSimulation import LifeGameSimulation
    from lifegame.synergy.collection.LifeGameCollectionConfiguration import LifeGameCollectionConfiguration
    from xyzworld.Context import Context as XyzContext

    # For now we update the python path. It will change in future version.
    ppath.insert(1, getcwd()+'/modules')

    config = {
        'app': {
            'name': 'LifeGame simulation',
            'classes': {
                'Context': XyzContext
            }
        },
        'engine': {
            'fpsmax': 5,
        },
        'simulations': [LifeGameSimulation([LifeGameCollection(LifeGameCollectionConfiguration())])],
        'connections': [PrintTerminal]
    }

    if __name__ == '__main__':
        # Run simulation
        Core.start_core(config, modules_path='modules')

We execute script and, tadaaa::

    python3.4 run_lifegame.py
    Cycle 0: 7 cells alive, 1993 cells died.
    Cycle 1: 7 cells alive, 1993 cells died.
    Cycle 2: 9 cells alive, 1991 cells died.
    Cycle 3: 9 cells alive, 1991 cells died.
    Cycle 4: 10 cells alive, 1990 cells died.
    Cycle 5: 12 cells alive, 1988 cells died.
    Cycle 6: 11 cells alive, 1989 cells died.
    Cycle 7: 16 cells alive, 1984 cells died.
    Cycle 8: 15 cells alive, 1985 cells died.
    Cycle 9: 23 cells alive, 1977 cells died.
    Cycle 10: 20 cells alive, 1980 cells died.

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


