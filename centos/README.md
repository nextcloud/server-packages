Nextcloud
=========

This repository can be used to build a very basic RPM suited for CentOS 7.
It uses Apache 2.4 with PHP-FPM to avoid conflicts with existing 
PHP 5.4 applications.  This also allows running Apache with a 
multi-threaded MPM while using mod_php a multi-threaded MPM is 
not recommended.

The package has been built following official Nextcloud documentation and
guidelines about strong directory permissions. See: https://docs.nextcloud.org/
and https://help.nextcloud.com if you get in trouble.

After the installation, the administrator should take care of the following:

* check Apache configuration and restart the httpd daemon
* if needed, install and configure MariaDB/MySQL database
* configure Nextcloud following the official documentation


Building RPM
------------

Before building the RPM, you should make sure that rpm-build and
rpmdevtools packages are installed.  This can be done by running:

  yum -y install rpm-build rpmdevtools

Then download the required source files by running:

  spectool -g -R nextcloud.spec

And finally building the nextcloud RPM by running:

  rpmbuild -bb nextcloud.spec


Dependencies
------------

The following dependencies are installed:

* Apache HTTP server
* PHP required packages (from SCL)
* PHP recommended packages (php-intl)
* PHP packages for builtin apps (php-ldap)
* PHP packages for MariaDB/MySQL connection

You need to enable EPEL and SCL repositories.

On CentOS this can be done by running:

  yum -y install epel-release centos-release-scl
 
On Red Hat Enterprise Linux run:

  yum -y install epel-release
  yum-config-manager --enable rhel-server-rhscl-7-rpms

The administrator can enable extra features installing following RPMs 
(from centos-sclo-sclo repository):

 * sclo-php71-php-smbclient
 * rh-php71-php-imap


Installing RPM
--------------

Once the RPM is built, it can be found in the following directory:
  rpmbuild/RPMS/noarch

It can be installed by running:
  yum -y rpmbuild/RPMS/noarch/nextcloud-x.x.x-x.el7.noarch.rpm

Replace the x characters with the actual version.


SELinux
-------

It's all on your own, please follow official documentation if you have 
SELinux enabled (which is the default on CentOS 7).


Alternatives RPMs
-----------------

If PHP-FPM doesn't fit your environment, please see also @mbevc1 packages:

https://github.com/mbevc1/nextcloud

