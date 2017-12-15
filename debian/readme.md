# Nextcloud

<!-- TOC -->

- [Nextcloud](#nextcloud)
    - [Packages](#packages)
        - [The nextcloud Package](#the-nextcloud-package)
        - [The nextcloud-apache Package](#the-nextcloud-apache-package)
        - [nextcloud-nginx](#nextcloud-nginx)
    - [testbed](#testbed)
        - [packer](#packer)
        - [nextclouddb](#nextclouddb)
        - [nextcloud-apache](#nextcloud-apache)

<!-- /TOC -->
beyon this structure you will find the directory with the [nextcloud package](./nextcloud/DEBIAN/control) and a directory that will configure the webserver in a proper way like [nextcloud-apache package](nextcloud-apache/DEBIAN/control)

## Packages

in this section all packages will be described in general.

### The nextcloud Package

This Package contains all needed files for nexcloud this will be placed with the build.sh at the location usr/share. The only dependecy for this package is the dependency to a webserver variant for example nextcloud-apache [see section Depends](nextcloud/DEBIAN/control)
After the installation, the administrator should take care of the following:

### The nextcloud-apache Package

this package enable a nextcloud apache site, after the installation you have to setup your owncloud installation.

- setup owncloud

```bash
sudo -u www-data php occ maintenance:install --database "mysql" --database-host myhost \
--database-name mydb \
--database-user dbuser \
--database-pass dbpass \
--admin-user "admin" \
--admin-pass "password" \
--data-dir /var/lib/nextcloud
```

the context of the installation is nextcloud.

### nextcloud-nginx

TODO: not implemented yet

## testbed

the directory testbed contains all services that may needed to test the nextcloud packages it should test the configuration and services not a correct implementation.
to get the infrastructure up and running it uses Docker. The subdirectory packer did not belong to the compose file it just provide a docker machine to build the debian packages in case that you will not use a linux machine to build the packages.

### packer

this container can be used to run the toplevel build.sh without install any buildtool except [docker](https://www.docker.com/get-docker)

on windows run

```bash
docker run -ti --rm --workdir /root -v.:/root/ --name packer packer ./build.sh
```

on linux you can add an alias to your environment like this
alias dockerexec='docker run -ti --rm --workdir /root -v`pwd`:/root/ --name packer packer'

afterwards execute

dockerexec ./build.sh

### nextclouddb

this service provide a mysql database for nextcloud

### nextcloud-apache

the directory provide an apache server whith the nextcloud file configured in a prper way includ the setup rotine. To get access call just open [nextcloud](http://localhost/nextcloud).
Authentication names and credentials can be found in the [security directory](testbed/secrets/).
