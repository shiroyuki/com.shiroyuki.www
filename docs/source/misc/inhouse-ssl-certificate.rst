In-house SSL Certificates and Certificate Authority
###################################################

Due to the annoying increase in cyberattack, all homebrew services are now
protected by an in-house SSL certificate.

Why in-house?
=============

As most of homebrew services are either personal or experimental, until the
traffice is high enough, I cannot afford to invest into a trusted certificate.

How to get the certificate?
===========================

For normal users, please download the certificate from http://home.shiroyuki.com/share/com.shiroyuki.cert
and install manually.

How to install the certificate?
===============================

There are many ways to install the certificate. This page will only provide the
instruction for Apple OS X and Chrome / Chrome OS.

Apple OS X
----------

1. Open **Keychain.app.**
2. Drag the downloaded certificate to **Keychain.app**.
3. In the dialog, expand the first section (**Trust**).
4. Click on the **always trust** button (bottom-right corner).

Chrome / Chrome OS
------------------

1. Open **Settings**.
2. In **Advanced Settings -> HTTPS/SSL**, click on **manage certificates**.
3. Click **Server** tab.
4. Click **Import**.