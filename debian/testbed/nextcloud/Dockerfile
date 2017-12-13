FROM debian
RUN apt-get update
#just to speedup after changing the deb
RUN apt-get install -y php7.0-xml php7.0 php7.0-cgi php7.0-cli php7.0-gd php7.0-curl php7.0-zip php7.0-mysql php7.0-mbstring
COPY nextcloud_12.0.3_amd64.deb /tmp
RUN apt-get -y --fix-broken install /tmp/nextcloud_12.0.3_amd64.deb
RUN apt-get -y install less vim sudo
COPY start.sh /start.sh
RUN chmod u+rx /start.sh
EXPOSE 80 443
CMD ["/start.sh"]

