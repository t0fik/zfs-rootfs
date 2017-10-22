Name:		zfs-rootfs
Version:	1.2
Release:	1%{?dist}
Summary:	Utils and configs for Linux on ZFS

License:	GPL
URL:		https://github.com/t0fik/zfs-rootfs
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
install -d %{buildroot}%{_sbindir}
install -pm 755 src/zmogrify %{buildroot}%{_sbindir}/
install -D -pm 644 src/profile-zfs.sh %{buildroot}%{_sysconfdir}/profile.d/zfs.sh

%files
%defattr(-,root,root,-)
%{_usr}/lib/kernel/install.d/10-dkms-zfs.install

%changelog
* Sun Oct 22 2017 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.2-1
- package name changed
- added profile environment variable export

* Thu Oct 12 2017 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1-1
- Fixed adding module
- Changed script order

* Thu Oct 12 2017 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.0-1
- initial build
