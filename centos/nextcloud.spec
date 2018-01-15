%define nextcloud_version 12.0.4

%define apache_serverroot /usr/share
%define apache_confdir /etc/httpd/conf.d
%define nc_dir  %{apache_serverroot}/nextcloud
%define nc_config_dir   %{nc_dir}/config
%define nc_data_dir     %{nc_dir}/data

%define nc_user apache
%define nc_group apache

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')


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
Requires: rh-php56, rh-php56-php-fpm
Requires: rh-php56-php-gd, rh-php56-php-pdo, rh-php56-php-pear, rh-php56-php-mbstring, rh-php56-php-xml
# Recommended php packages
Requires: rh-php56-php-intl
# Required php packages for specific apps
Requires: rh-php56-php-ldap
# Required php packages for MariaDB
Requires: rh-php56-php-mysqlnd


%description
Nextcloud files and configuration.

This package installs as follows:
nc_dir:        %{nc_dir}
nc_data_dir:   %{nc_data_dir}
nc_config_dir: %{nc_config_dir}


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{nc_data_dir}
mkdir -p %{buildroot}/usr/share
tar xf %{SOURCE0} -C %{buildroot}/usr/share

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
%dir %attr(0755,root,%{nc_group}) %{nc_dir}
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/occ
%attr(0750,%{nc_user},%{nc_group}) %{nc_dir}/apps
%attr(0750,%{nc_user},%{nc_group}) %{nc_dir}/assets
%attr(0750,%{nc_user},%{nc_group}) %{nc_dir}/updater
%attr(0775,%{nc_user},%{nc_group}) %{nc_data_dir}
%attr(0775,%{nc_user},%{nc_group}) %{nc_config_dir}
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/lib
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/core
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/settings
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/3rdparty
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/resources
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/themes
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/ocs*
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/l10n
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/*.php
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/AUTHORS
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/db_structure.xml
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/index.html
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/robots.txt
%attr(0644,%{nc_user},%{nc_group}) %{nc_dir}/.htaccess

%config(noreplace) %attr(0644,%{nc_user},%{nc_group}) %{nc_dir}/.user.ini
%config(noreplace) %attr(0644,root,root) /etc/httpd/conf.d/nextcloud.conf

%defattr(0644,%{nc_user},%{nc_group},0755)


%changelog
* Mon Jan 15 2018 Alessandro Polidori <alessandro.polidori@nethesis.it> - centos-12.0.4-2
- Spec: remove "config" sign from .htaccess

* Thu Dec 14 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - centos-12.0.4-1
- Update to release 12.0.4

* Wed Sep 27 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 12.0.3
- Update to release 12.0.3

* Tue Aug 29 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 12.0.2-2
- Avoid security warnings on python compiled files

* Wed Aug 23 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 12.0.2
- Update to release 12.0.2

* Wed May 24 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 12.0.0
- Update to release 12.0.0
- Fix spec warnings - Thanks to @mbevc1

* Wed May 17 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 11.0.3-2
- Fix WebDAV authentication - Thanks to Davide Principi

* Wed May 17 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 11.0.3
- Update to release 11.0.3

* Wed Mar 15 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 11.0.2
- Update to release 11.0.2
- Move installation inside /usr/share/nextcloud
- Switch to php-fpm

* Thu Dec 15 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 10.0.2
- Bump release: 10.0.2

* Mon Aug 01 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 9.0.53-2
- First Nextcloud release - NethServer/dev#5055

