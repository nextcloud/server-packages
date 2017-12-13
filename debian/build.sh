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

#unzip downloads/nextcloud-12.0.4.zip -d usr/share/
unzip downloads/nextcloud-12.0.4.zip -d usr/share/ -x "nextcloud/config/*"
#rm usr/share/nextcloud/config/
#cd usr/share/nextcloud
if [ -s usr/share/nextcloud/config ];then
	ln -s /etc/nextcloud/config usr/share/nextcloud/config
fi
fakeroot dpkg -b . testbed/nextcloud


docker-compose -f testbed/docker-compose.yml build
docker-compose -f testbed/docker-compose.yml up
