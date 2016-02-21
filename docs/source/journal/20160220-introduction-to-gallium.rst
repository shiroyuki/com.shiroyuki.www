Introduction to Gallium
#######################

Let's stop doing the same thing concentrate on making a great application.

In the world of software development, there are always chances that someone
has to write at least one or two command line interfaces in their line of work.
Usually, the scripts, usually written in **shell script** or any scripting
languages (e.g., **Python**), starts from something very simple. However,
over time, the scripts turn into complex ones and maintainability suddently
becomes an issue.

Even if someone succeeds in controlling that variable, the documentation and
argument parsing can be messy and inconsistent. Not to mention input validation
and so forth.

This is where Gallium comes.

What is Gallium?
================

**Gallium** is a microframework designed for CLI application development, and
focuses on handling the following areas:

* Gallium standardizes the way to parse arguments with `ArgParse <https://docs.python.org/3/library/argparse.html>`_
  (Python built-in library).
* Gallium allows easy dependency injection (DI) and aspect-oriented programming (AOP) with
  `Imagination Framework <https://github.com/shiroyuki/Imagination>`_ which the
  core of Gallium relies heavily on it.
  
.. note::

    You can ignore the DI/AOP part if you want to. It is very useful and make
    you focus less on wiring things together and more on writing business logic,
    although the XML configuration file might make you very unhappy.

* Gallium is to minimize the learning curve as everything used in the core development of
  Gallium is built into Python, except the Imagination Framework.
* Gallium is to provide the extendability with extensions to allow developers do whatever
  they want.

Additionally, Gallium is designed in a way that **does not need developers to
write the bootstrap code or learn how to define arguments**.

What is not Gallium?
====================

Gallium is not yet another web framework but you can build your own on top of it.

Design Principles and Tackling Problems
=======================================

Here are my usual scenarios.

* I usually have to write a startup/bootstrap code.
* Then, I often have to rely on arguments in order to allow more control on the
  code without updating code or configuration to do what I want.
* Then, either I have to go with the old-school way of manually parsing arguments
  or relying on an argument parser.
* Even if I have a parent class to standardize the way I implement a CLI script,
  each script might have to either work with a bootstrap/startup script or define
  the main function (for example, ``__name__ == '__main__'``.
* Somehow, even those points mentioned above are really big deal, the command
  discovery has to be done manually.
* Even if I dogde all points above, as this type of software is usually designed
  and used internally, when I have to work in different projects, I have to either
  waste time on rewriting the same bloody code with the slightly improved design
  or copy code around or painfully abstract the code to something like a common
  library.
* Then, I need the extendability and reusability of anything I write in order to
  allow me to enable or disable features at will.

So, I decide to make Gallium to:

* supplies the bootstrap script on installation when it is installed with ``pip``,
* unifies the way to define the command arguments and the short name of the command,
* automatically discovers and registers commands, implemented ``gallium.interface.ICommand``,
  by fully qualified **module name** or **class name**,
* be extendable and reusable to allow more applications to utilize the capability
  of Gallium Core.

It sounds great. How can I get and use it?
==========================================

While I am planning on writing detailed documentations, I cannot seem to find
time to do so. However, as I spend time to write a pretty detailed README file,
hence, you can read more details on `GitHub <https://github.com/shiroyuki/gallium>`_
which includes the instruction on how to install the package (via ``pip``).

I hope that in the coming months, I can finish the proper documentation.

Next steps?
===========

* Go to `GitHub <https://github.com/shiroyuki/gallium>`_ and start using it.
