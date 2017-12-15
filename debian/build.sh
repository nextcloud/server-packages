#!/bin/bash
set -e
set -x

version=12.0.4
downloadurl='https://download.nextcloud.com/server/releases'

if [ -f downloads/nextcloud-${version}.zip ];then
	echo "already downloaded nextcloud $version"
else
	curl ${downloadurl}/nextcloud-${version}.zip -o downloads/nextcloud-${version}.zip
fi
if [ -f downloads/nextcloud-${version}.zip.sha256 ];then
	echo "already downloaded nextcloud $version"
else
	curl ${downloadurl}/nextcloud-${version}.zip.sha256 -o downloads/nextcloud-${version}.zip.sha256
fi
#check the sha256 sum
SHA256SUM=`cat downloads/nextcloud-${version}.zip.sha256|cut -f1 -d' '`
#this migth just run on mac?
MYSUM=`shasum -a 256 downloads/nextcloud-12.0.4.zip|cut -f1 -d' '`

if [ "$MYSUM" == "$SHA256SUM" ];then 
	echo "hash match"
else
	echo "sha256 mismatch press key to continue"
	read line 
fi

unzip downloads/nextcloud-12.0.4.zip -d nextcloud/usr/share/ -x "nextcloud/config/*" -x "nextcloud/data"
if [ ! -h nextcloud/usr/share/nextcloud/config ];then
	ln -s /etc/nextcloud/config nextcloud/usr/share/nextcloud/config
fi
fakeroot dpkg -b nextcloud testbed/nextcloud


docker-compose -f testbed/docker-compose.yml build
docker-compose -f testbed/docker-compose.yml up
