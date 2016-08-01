%define nextcloud_version 9.0.53

%define apache_serverroot       /var/www/html
%define apache_confdir /etc/httpd/conf.d
%define nc_dir  %{apache_serverroot}/nextcloud
%define nc_config_dir   %{nc_dir}/config
%define nc_data_dir     %{nc_dir}/data

%define nc_user apache
%define nc_group apache


Summary: Nextcloud package
Name: nextcloud
Version: %nextcloud_version
Release: 2%{?dist}
License: GPL
Source: https://download.nextcloud.com/server/releases/nextcloud-%{nextcloud_version}.tar.bz2
Source1: nextcloud.conf
BuildArch: noarch
URL: https://nextcloud.com/

BuildRequires: httpd

Requires: httpd
# Required php packages
Requires: php-gd, php-pdo, php-pear, php-mbstring, php-xml
# Recommended php packages
Requires: php-pear-Net-Curl, php-mcrypt, php-intl
# Required php packages for specific apps
Requires: php-ldap, php-smbclient, php-imap
# Required php packages for MariaDB
Requires: php-mysql, php-pear-MDB2, php-pear-MDB2-Driver-mysqli


%description
Nextcloud files and configuration.

This package installs as follows:
nc_dir:        %{nc_dir}
nc_data_dir:   %{nc_data_dir}
nc_config_dir: %{nc_config_dir}


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{nc_data_dir}
mkdir -p %{buildroot}/var/www/html
tar xf %{SOURCE0} -C %{buildroot}/var/www/html

mkdir -p %{buildroot}/%{nc_dir}
mkdir -p %{buildroot}/%{nc_dir}/etc
mkdir -p %{buildroot}/%{nc_data_dir}
mkdir -p %{buildroot}/%{nc_config_dir}
mkdir -p %{buildroot}/%{nc_dir}/assets
mkdir -p %{buildroot}/%{nc_dir}/updater

mkdir -p %{buildroot}/etc/httpd/conf.d
cp %{SOURCE1} %{buildroot}/etc/httpd/conf.d


%files 
%defattr(0640,root,%{nc_group},0750)
%attr(0755,root,%{nc_group}) %{nc_dir}
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/occ
%attr(0750,%{nc_user},%{nc_group}) %{nc_dir}/apps
%attr(0750,%{nc_user},%{nc_group}) %{nc_dir}/assets
%attr(0750,%{nc_user},%{nc_group}) %{nc_dir}/updater
%attr(0775,%{nc_user},%{nc_group}) %{nc_data_dir}
%attr(0775,%{nc_user},%{nc_group}) %{nc_config_dir}

%config %attr(0644,%{nc_user},%{nc_group}) %{nc_dir}/.htaccess
/etc/httpd/conf.d/nextcloud.conf

%defattr(0644,%{nc_user},%{nc_group},0755)



%changelog
* Mon Aug 01 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 9.0.53-2
- First Nextcloud release - NethServer/dev#5055

