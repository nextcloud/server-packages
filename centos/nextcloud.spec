%define nextcloud_version 11.0.3

%define apache_serverroot /usr/share
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
%attr(0755,root,%{nc_group}) %{nc_dir}
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/occ
%attr(0750,%{nc_user},%{nc_group}) %{nc_dir}/apps
%attr(0750,%{nc_user},%{nc_group}) %{nc_dir}/assets
%attr(0750,%{nc_user},%{nc_group}) %{nc_dir}/updater
%attr(0775,%{nc_user},%{nc_group}) %{nc_data_dir}
%attr(0775,%{nc_user},%{nc_group}) %{nc_config_dir}

%config(noreplace) %attr(0644,%{nc_user},%{nc_group}) %{nc_dir}/.user.ini
%config(noreplace) %attr(0644,%{nc_user},%{nc_group}) %{nc_dir}/.htaccess
%config(noreplace) %attr(0644,root,root) /etc/httpd/conf.d/nextcloud.conf

%defattr(0644,%{nc_user},%{nc_group},0755)



%changelog
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

