Name: nacos
Version: 2.2.0
Release: 1
Summary: Nacos Server

Group: Applications/Internet
License: Apache License 2.0
URL: https://nacos.io
Source0: nacos-server-2.2.0.tar.gz 


BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Nacos Server is a distributed configuration service, service discovery, and service governance platform for cloud native applications.

%define __jar_repack %{nil}

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/nacos-2.2.0
cp -r * $RPM_BUILD_ROOT/opt/nacos-2.2.0/

%files
/opt/nacos-2.2.0/target/nacos-server.jar
/opt/nacos-2.2.0/LICENSE
/opt/nacos-2.2.0/NOTICE
/opt/nacos-2.2.0/bin/shutdown.cmd
/opt/nacos-2.2.0/bin/shutdown.sh
/opt/nacos-2.2.0/bin/startup.cmd
/opt/nacos-2.2.0/bin/startup.sh
/opt/nacos-2.2.0/conf/1.4.0-ipv6_support-update.sql
/opt/nacos-2.2.0/conf/application.properties
/opt/nacos-2.2.0/conf/application.properties.example
/opt/nacos-2.2.0/conf/cluster.conf.example
/opt/nacos-2.2.0/conf/derby-schema.sql
/opt/nacos-2.2.0/conf/mysql-schema.sql
/opt/nacos-2.2.0/conf/nacos-logback.xml

%post
echo "Nacos Server is installed."

%preun
echo "Uninstalling Nacos Server."

%postun
echo "Nacos Server is uninstalled."

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sat Jan 01 2022 John Doe <john.doe@example.com> 1.0.0-1
- Initial release

