Nextcloud
=========

This repository can be used to build a very basic RPM suited for CentOS 7.
It uses Apache 2.4 with PHP-FPM to avoid conflicts with existing PHP 5.4 applications.

The package has been built following official Nextcloud documentation and
guidelines about strong directory permissions. See: https://docs.nextcloud.org/
and https://help.nextcloud.com if you get in trouble.

After the installation, the administrator should take care of the following:

* check Apache configuration and restart the httpd daemon
* if needed, install and configure MariaDB/MySQL database
* configure Nextcloud following the official documentation

Dependencies
------------

The following dependencies are installed:

* Apache HTTP server
* PHP required packages (from SCL)
* PHP recommended packages (php-intl)
* PHP packages for builtin apps (php-ldap)
* PHP packages for MariaDB/MySQL connection

You need to enable EPEL repository.

The administrator can enable extra features installing following RPMs (from centos-sclo-sclo repository):

* rh-php56-php-mcrypt
* sclo-php56-php-smbclient
* rh-php56-php-imap

SELinux
-------

It's all on your own, please follow official documentation if you have SELinux enabled
(which is the default on CentOS 7).

Alternatives RPMs
-----------------

If PHP-FPM doesn't fit your environment, please see also @mbevc1 packages:

https://github.com/mbevc1/nextcloud
