Name:		zfs-utils
Version:	1.1
Release:	1%{?dist}
Summary:	Utils and configs for Linux on ZFS

License:	GPL
URL:		https://github.com/t0fik/zfs-utils
Source0:	https://github.com/t0fik/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

Requires:	systemd zfs-dkms spl-dkms

BuildRequires:	systemd

%description
Utils and configs for Linux on ZFS

%prep
%setup -q

%build

%install
install -d 755 %{buildroot}%{_usr}/lib/kernel/install.d
install -pm 755 src/10-dkms-zfs.install %{buildroot}%{_usr}/lib/kernel/install.d

%files
%defattr(-,root,root,-)
%{_usr}/lib/kernel/install.d/10-dkms-zfs.install

%changelog
* Thu Oct 12 2017 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1-1
- Fixed adding module
- Changed script order

* Thu Oct 12 2017 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.0-1
- initial build
