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
Version: 17.0.3
Release: 1%{?dist}
License: GPL
Source: https://download.nextcloud.com/server/releases/nextcloud-%{version}.tar.bz2
Source1: https://raw.githubusercontent.com/nextcloud/server-packages/v17/centos/nextcloud.conf
Source2: https://raw.githubusercontent.com/nextcloud/server-packages/v17/centos/nextcloud-fpm.conf
Source3: https://nextcloud.com/nextcloud.asc
Source4: https://download.nextcloud.com/server/releases/nextcloud-%{version}.tar.bz2.asc
Source5: https://download.nextcloud.com/server/releases/nextcloud-%{version}.tar.bz2.md5
Source6: https://download.nextcloud.com/server/releases/nextcloud-%{version}.tar.bz2.sha256
Source7: https://download.nextcloud.com/server/releases/nextcloud-%{version}.tar.bz2.sha512
BuildArch: noarch
URL: https://nextcloud.com/

BuildRequires: httpd

Requires: httpd
# Required php packages
Requires: rh-php72
Requires: rh-php72-php-fpm
Requires: rh-php72-php-gd
Requires: rh-php72-php-pdo
Requires: rh-php72-php-mbstring
Requires: rh-php72-php-imagick

# Recommended php packages
Requires: rh-php72-php-intl

# Required php packages for specific apps
Requires: rh-php72-php-ldap

# Required php packages for MariaDB
Requires: rh-php72-php-pdo_mysql

# NextCloud does not support skipping a major version number
Conflicts: nextcloud < 16


%description
Nextcloud files and configuration.

This package installs as follows:
nc_dir:        %{nc_dir}
nc_data_dir:   %{nc_data_dir}
nc_config_dir: %{nc_config_dir}


%prep
cd %{_sourcedir}
/usr/bin/md5sum -c %{SOURCE5}
if [ $? -ne 0 ] ; then echo md5sum did not match ; exit 1 ; fi
/usr/bin/sha256sum -c %{SOURCE6}
if [ $? -ne 0 ] ; then echo sha256sum did not match ; exit 1 ; fi
/usr/bin/sha512sum -c %{SOURCE7}
if [ $? -ne 0 ] ; then echo sha512sum did not match ; exit 1 ; fi
/usr/bin/gpg --import %{SOURCE3}
/usr/bin/gpg --verify %{SOURCE4} %{SOURCE0}
if [ $? -ne 0 ] ; then echo gpg signature did not match ; exit 1 ; fi


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
mkdir -p %{buildroot}/etc/opt/rh/rh-php72/php-fpm.d/
cp %{SOURCE2} %{buildroot}/etc/opt/rh/rh-php72/php-fpm.d/nextcloud.conf


%post
YM=$(date +%Y%m)
if [ $YM -ge 202008 ] ; then
cat << EOF

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
NextCloud v17 End of Life Notice
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
This NextCloud version is stated as End of Life as of September 2020

There will no longer be security or maintenance fixes provided.

It is important to plan an upgrade schedule to NextCloud version 18
accordingly.

NextCloud does not support skipping major versions.  To keep the
database schema current, it is important to run the upgrade (such as 
through the OCC CLI) for each major version.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

EOF
fi
if [ $YM -ge 202010 ] ; then
/usr/bin/systemctl status rh-php72-php-fpm > /dev/null
if [ $? -eq 0 ] ; then
cat << EOF

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
PHP 7.2 End of Life Notice
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
This system is still running the rh-php72-php-fpm service.

As of November 2020, the primary PHP project will no longer be releasing
security updates for PHP version 7.2.

It is recommended you plan accordingly to upgrade to using PHP 7.3.
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

EOF
fi
fi

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
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/ocm-provider
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/core
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/settings
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/3rdparty
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/resources
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/themes
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/ocs*
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/*.php
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/AUTHORS
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/COPYING
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/index.html
%attr(0755,%{nc_user},%{nc_group}) %{nc_dir}/robots.txt
%attr(0644,%{nc_user},%{nc_group}) %{nc_dir}/.htaccess

%config(noreplace) %attr(0644,%{nc_user},%{nc_group}) %{nc_dir}/.user.ini
%config(noreplace) %attr(0644,root,root) /etc/httpd/conf.d/nextcloud.conf
%config(noreplace) %attr(0644,root,root) /etc/opt/rh/rh-php72/php-fpm.d/nextcloud.conf

%defattr(0644,%{nc_user},%{nc_group},0755)


%changelog
* Wed Feb 05 2020 B Galliart <ben@steadfast.net> - 17.0.3-1
- Update to release 17.0.3
- Added hash/gpg validity checking of nextcloud tar.bz2 file
- Added sanity checking for end of life dates

* Wed Jan 08 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it>- 17.0.2-1
- Update to release 17.0.2

* Tue Nov 26 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it>- 17.0.1-1
- Update to release 17.0.1

* Mon Sep 02 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it>- 16.0.4-1
- Update to release 16.0.4

* Thu Aug 1 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it>- 16.0.3-1
- Update to release 16.0.3

* Fri Jul 5 2019 Alessandro Polidori <alessandro.polidori@nethesis.it> - 16.0.2-1
- Update to release 16.0.2

* Tue May 21 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 16.0.1-1
- Update to release 16.0.1

* Tue Apr 30 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 16.0.0-1
- Update to release 16.0.0

* Wed Apr 24 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 15.0.7-1
- Update to release 15.0.7

* Fri Mar 1 2019 Alessandro Polidori <alessandro.polidori@nethesis.it> - 15.0.5-1
- Update to release 15.0.5

* Thu Feb 7 2019 Alessandro Polidori <alessandro.polidori@nethesis.it> - 15.0.4-1
- Update to release 15.0.4

* Mon Jan 14 2019 Alessandro Polidori <alessandro.polidori@nethesis.it> - 15.0.2-1
- Update to release 15.0.2

* Tue Dec 18 2018 Alessandro Polidori <alessandro.polidori@nethesis.it> - 15.0.0-1
- Update to release 15.0.0

* Mon Nov 26 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 14.0.4-1
- Update to release 14.0.4

* Mon Oct 15 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 14.0.3-1
- Update to release 14.0.3

* Thu Oct 11 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 14.0.2-1
- Update to release 14.0.2

* Wed Sep 26 2018 Alessandro Polidori <alessandro.polidori@nethesis.it> - 14.0.1-1
- Update to release 14.0.1

* Thu Sep 6 2018 Alessandro Polidori <alessandro.polidori@nethesis.it> - 14.0.0-1
- Update to release 14.0.0

* Wed Sep 5 2018 Alessandro Polidori <alessandro.polidori@nethesis.it> - 13.0.6-1
- Update to release 13.0.6

* Wed Aug 1 2018 Alessandro Polidori <alessandro.polidori@nethesis.it> - 13.0.5-1
- Update to release 13.0.5

* Mon Jun 11 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 13.0.4-1
- Update to release 13.0.4

* Fri Jun 08 2018 Stephane de Labrusse <stephdl@de-labrusse.fr> - 13.0.3-1
- Update to release 13.0.3

* Thu Apr 26 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 13.0.2-1
- Update to release 13.0.2

* Mon Mar 19 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 13.0.1-1
- Update to release 13.0.1

* Tue Mar 06 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 13.0.0-1
- Update to release 13.0.0

* Thu Jan 25 2018 Alessandro Polidori <alessandro.polidori@nethesis.it> - 12.0.5-1
- Update to release 12.0.5

* Mon Jan 15 2018 Alessandro Polidori <alessandro.polidori@nethesis.it> - 12.0.4-2
- Spec: remove "config" sign from .htaccess

* Thu Dec 14 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 12.0.4-1
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

