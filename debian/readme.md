# Nextcloud

beyon this structure you will find the directory with the [ nextcloud package ] (nextcloud) and a directory that will configure the webserver in a proper way for example [ nextcloud-apache ] (nextcloud-apache)

## nextcloud

the pakage structure 

After the installation, the administrator should take care of the following:

- setup ...

- restart the apache

## nextcloud-apache

this package enable a nextcloud apache site, after the installation you can reach your nextcloud installation beyon http://<root>/nextcloud

## nextcloud-nginx

TODO

# testbed

the directory testbed contains all services that may needed to test nextcloud it should test the configuration and services not a correct implementation.

## packer

this container can be used to run the toplevel build.sh without install any buildtool except [docker](https://www.docker.com/get-docker)

on windows run
```
docker run -ti --rm --workdir /root -v.:/root/ --name packer packer ./build.sh
```

on linux you can add an alias to your environment like this
alias dockerexec='docker run -ti --rm --workdir /root -v`pwd`:/root/ --name packer packer'

afterwards execute

dockerexec ./build.sh

## nextclouddb

this service provide a mysql database for nextcloud

## nextcloud-apache

the directory provide an apache server whith the nextcloud file configured in a proer way. To get access call http://localhost/nextcloud authentication names and credentials can be found in the [security directory](testbed/secrets/).
