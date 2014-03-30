How to add, update or delete a staff information
################################################

The information of all staffs are stored at :file:`/data/staffs` in the SDO
format defined in :doc:`development`.

Individual Staff Data
=====================

The SDO file will contain the following keys:

- title
- biography (optional)
- publication (optional)
- performance (optional)
- website (optional)
- twitter (optional)
- facebook (optional)
- google_plus (optional)

The naming convention is :file:`<priority_index>-<firstname>-<lastname>.txt`
where **priority_index** is an integer (``0`` is only used by *Ajarn Pratak*),
**firstname** and **lastname** are the lowercase firstname and lastname in English.

For example, the information of **Ajarn Pratak Faisupagarn** will be stored at
:file:`0-pratak-faisupagarn.txt` and contains the following information in the
SDO file::

    Pratak Faisupagarn

    :title:
    Founder, Instructor

    :biography:
    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat
    non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

    :publication:
    - ฤๅจะร้อนเร่าเท่าแจ๊ส (Le Jazz Hot), ร้านบราวชูการ์, 2533, ISBN 9748865967
    - ฤาจะอ่อนหวานปานแจ๊ส (Le Jazz Sweet), สามัญชน, 2545, ISBN 9747607441
    - ศิลปินแจ๊สหญิงชื่อดัง (Renowned Female Jazz Artists), สื่อดี, 2550, ISBN 978-974-8195-18-6

    :facebook:
    pratak.faisupagarn

Ordering in the staff list
==========================

The order goes by the alphanumeric order of the filenames.

.. note:: **priority_index** is reserved for the founder.