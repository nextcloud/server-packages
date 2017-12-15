FROM debian
RUN apt-get update
COPY nextcloud_12.0.3_amd64.deb /tmp
RUN apt-get -y --fix-broken install /tmp/nextcloud_12.0.3_amd64.deb sudo
COPY start.sh /start.sh
RUN chmod u+rx /start.sh
EXPOSE 80 443
CMD ["/start.sh"]

