Name:		zfs-rootfs
Version:	1.2.4
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
install -d %{buildroot}%{_sysconfdir}/kernel/postinst.d
install -pm 755 src/zmogrify %{buildroot}%{_sbindir}/
install -D -pm 644 src/profile-zfs.sh %{buildroot}%{_sysconfdir}/profile.d/zfs.sh
ln -sf %{_sbindir}/zmogrify %{buildroot}%{_sysconfdir}/kernel/postinst.d/zzz_zmogrify

%files
%defattr(-,root,root,-)
%{_sysconfdir}
%{_sbindir}/zmogrify

%changelog
* Fri Nov 11 2017 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.2.5-1
- Added recreating rescue initramfs

* Sun Nov 05 2017 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.2.4-1
- Added setting ZPOOL_VDEV_NAME_PATH variable

* Tue Oct 31 2017 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.2.3-1
- Added saving checksum of initramfs

* Sat Oct 28 2017 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.2.2-1
- Fix: bug in detection if efi partition mounted

* Sun Oct 22 2017 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.2.1-1
- Zmogrify uses current kernel version if run without parameters

* Sun Oct 22 2017 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.2-2
- Spec file fixes

* Sun Oct 22 2017 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.2-1
- Package name changed
- Added profile environment variable export

* Thu Oct 12 2017 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1-1
- Fixed adding module
- Changed script order

* Thu Oct 12 2017 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.0-1
- initial build
