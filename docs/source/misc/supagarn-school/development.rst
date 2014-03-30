Development
###########

The development of supagarn.ac.th is modeled after http://shiroyuki.com (revision 14).

Simple Data Object Format (SDO)
===============================

Any data stored as a text will use the following pattern:

.. code-block:: django

    {{ The title or the name of the data object }}

    :{{ key_1 }}:
    {{ value_1 }}

    :{{ key_2 }}:
    {{ value_2 }}

    ...

where **key_x** is case-insensitive and