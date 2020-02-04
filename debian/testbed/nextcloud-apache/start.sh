#!/bin/bash
#we need a check wether or nor the db is ok
sleep 20
#check if nexcloud is configured...
cd /usr/share/nextcloud
sudo -u www-data php occ check|grep "Nextcloud is not installed"
if [ $? -eq 0 ];then
	echo "configure owncloud...."
	sudo -u www-data php occ maintenance:install --database "mysql" --database-host ${MYSQL_HOST} \
--database-name `cat /run/secrets/mysql_db_name`  --database-user `cat /run/secrets/mysql_user` --database-pass `cat /run/secrets/mysql_password` \
--admin-user "sladmin" --admin-pass "password" --data-dir /var/lib/nextcloud
fi
source /etc/apache2/envvars 
/usr/sbin/apachectl configtest
/usr/sbin/apache2 -DFOREGROUND

