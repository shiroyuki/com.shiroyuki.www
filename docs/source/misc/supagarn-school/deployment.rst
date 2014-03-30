How to Deploy the Website
#########################

This section is to illustrate how the deployment works in general.

Assuming that the website is ready to deploy, as an editor,

# he or she SHOULD test locally.
# he or she MUST creates a deployment ticket at https://github.com/shiroyuki/supagarn.www/issues.

As a system administrator,

# he verifies the changes and edits if necessary.
# he makes a release tag from the changes.
# he deploys the website by the release tag.

Develop and/or test locally
===========================

:Prerequisite: Python 2.7 or higher, Sphinx
:Supported OS: Mac OS X 10.7+, Linux

Once the changes are made, he or she should run:

.. code-block:: bash

    make

to compile the website. Then,

.. code-block:: bash

    make service

to run the built-in web server.