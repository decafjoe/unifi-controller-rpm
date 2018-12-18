%global __jar_repack 0
%global debug_package %{nil}
%global unifi_group unifi
%global unifi_user unifi
%global unifi_prefix /opt/unifi

Summary: UniFi WAP, routing, and switching controller
Name: unifi
Version: 5.7.20
Release: 1
License: Proprietary
Group: System Environment/Daemons
URL: https://www.ubnt.com/download/unifi/
Source0: %{name}-%{version}.zip
Source1: unifid.init
Source2: unifid
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: java-1.8.0-openjdk-headless
Requires: python-argparse

%description
Ubiquiti UniFi wireless access point, routing, and switching controller.

This package is built using a process largely cribbed from the unofficial
EL7 packages available on the Ubiquiti forum. If you're on 7, use that one.
The only reason this package exists is for EL6 users.

%prep
%setup -q -n UniFi
rm -f readme.txt
rm -rf lib/native/Mac
rm -rf lib/native/Windows
rm -rf lib/native/Linux/armhf
rmdir conf

%build

%install
mkdir -p %{buildroot}%{unifi_prefix}
mv * %{buildroot}%{unifi_prefix}/
mkdir -p %{buildroot}%{unifi_prefix}/{data,logs,run,work}
mkdir -p %{buildroot}%{_initrddir}
install -m 755 %{S:1} %{buildroot}%{_initrddir}/unifid
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{S:2} %{buildroot}%{_bindir}/unifid

%check
echo -n "Checking installed version... "
grep -E ^%{version} %{buildroot}%{unifi_prefix}/webapps/ROOT/app-unifi/.version

%clean
rm -rf $RPM_BUILD_ROOT

%pre
/usr/bin/getent group %{unifi_group} >/dev/null \
  || /usr/sbin/groupadd -r %{unifi_group}
/usr/bin/getent passwd %{unifi_user} >/dev/null \
  || /usr/sbin/useradd \
       -MNrg %{unifi_group} -d %{unifi_prefix} -s /sbin/nologin %{unifi_user}

%files
%attr(0755,root,root) %{_bindir}/unifid
%attr(0755,root,root) %{_initrddir}/unifid
%attr(0750,%{unifi_user},%{unifi_group}) %{unifi_prefix}/bin/
%attr(0750,%{unifi_user},%{unifi_group}) %{unifi_prefix}/data/
%attr(0750,%{unifi_user},%{unifi_group}) %{unifi_prefix}/dl/
%attr(0750,%{unifi_user},%{unifi_group}) %{unifi_prefix}/lib/
%attr(0750,%{unifi_user},%{unifi_group}) %{unifi_prefix}/logs/
%attr(0755,%{unifi_user},%{unifi_group}) %{unifi_prefix}/run/
%attr(0750,%{unifi_user},%{unifi_group}) %{unifi_prefix}/webapps/
%attr(0750,%{unifi_user},%{unifi_group}) %{unifi_prefix}/work/

%changelog
* Fri May 18 2018 Joe Joyce <joe@decafjoe.com> 5.7.20-1
- Initial build.
