%global _topdir		%(echo $HOME)/rpmbuild-%{name}
Name: nacos
Version: 2.2.0
Release: 1
Summary: Nacos Server

Group: Applications/Internet
License: Apache License 2.0
URL: https://nacos.io
Source0: nacos-server-%{version}.tar.gz 
Source1: nacos.service


BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Nacos Server is a distributed configuration service, service discovery, and service governance platform for cloud native applications.

%define __jar_repack %{nil}

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/nacos-%{version}
cp -r * $RPM_BUILD_ROOT/opt/nacos-%{version}/
install -Dpm0640 %{SOURCE1} 		%{buildroot}%{_unitdir}/%{name}.service

%files
/opt/nacos-%{version}/target/nacos-server.jar
/opt/nacos-%{version}/LICENSE
/opt/nacos-%{version}/NOTICE
/opt/nacos-%{version}/bin/shutdown.cmd
/opt/nacos-%{version}/bin/shutdown.sh
/opt/nacos-%{version}/bin/startup.cmd
/opt/nacos-%{version}/bin/startup.sh
/opt/nacos-%{version}/conf/1.4.0-ipv6_support-update.sql
/opt/nacos-%{version}/conf/application.properties
/opt/nacos-%{version}/conf/application.properties.example
/opt/nacos-%{version}/conf/cluster.conf.example
/opt/nacos-%{version}/conf/derby-schema.sql
/opt/nacos-%{version}/conf/mysql-schema.sql
/opt/nacos-%{version}/conf/nacos-logback.xml
%{_unitdir}/%{name}.service

%post
# Manage systemd service
%systemd_post %{name}.service

echo "Nacos Server is installed."

%preun
# Manage systemd service
%systemd_preun %{name}.service

echo "Uninstalling Nacos Server."

%postun
# Manage systemd service
%systemd_postun_with_restart %{name}.service

echo "Nacos Server is uninstalled."

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sat Jan 01 2022 John Doe <john.doe@example.com> 1.0.0-1
- Initial release

