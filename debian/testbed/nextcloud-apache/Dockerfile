FROM debian
ENV nextclodversion 12.0.3
#just a local proxy ENV http_proxy=http://192.168.0.1:3128
RUN apt-get update
COPY nextcloud_"${nextclodversion}"_amd64.deb /tmp
COPY nextcloud-apache_"${nextclodversion}"_amd64.deb /tmp
RUN apt-get -y --fix-broken install \
	/tmp/nextcloud_*_amd64.deb \
	/tmp/nextcloud-apache_*_amd64.deb \
	sudo
COPY start.sh /start.sh
RUN chmod u+rx /start.sh
EXPOSE 80 443
CMD ["/start.sh"]

