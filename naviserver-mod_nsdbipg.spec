#
# spec file for package naviserver nsdbipg module
#

Summary:        NaviServer nsdbipg module
Name:           naviserver-mod_nsdbipg
Version:        0.3
Release:        0
License:        MPL-1.1
Group:          Productivity/Networking/Web/Servers
Url:            http://bitbucket.org/naviserver/nsdbipg
BuildRequires:  make
BuildRequires:  naviserver
BuildRequires:  naviserver-devel
BuildRequires:  naviserver-mod_nsdbi
BuildRequires:  naviserver-mod_nsdbi-devel
BuildRequires:  postgresql-devel
Requires:       naviserver-mod_nsdbi
Requires:       naviserver
Source0:        %{name}-%{version}.tar.gz
Patch0:         nsdbipg.c.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is the nsdbipg database driver. It connects a Postgres database
to a NaviServer web server using the nsdbi interface.

%prep
%setup -q %{name}-%{version}
%patch0

%build
make NAVISERVER=/var/lib/naviserver

%install
mkdir -p %buildroot/var/lib/naviserver/bin
make DESTDIR=%buildroot install NAVISERVER=/var/lib/naviserver

%clean
rm -rf %buildroot

%post -n naviserver-mod_nsdbipg
/sbin/ldconfig

%postun -n naviserver-mod_nsdbipg
/sbin/ldconfig

%files
%defattr(-,nsadmin,nsadmin,-)
/var/lib/naviserver/bin/nsdbipg.so

%changelog

