Name:		zfs-rootfs
Version:	1.3.5
Release:	2%{?dist}
Summary:	Utils and configs for Linux on ZFS

License:	GPL
URL:		https://github.com/t0fik/zfs-rootfs
Source0:	https://github.com/t0fik/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

Requires:	systemd
Requires:       zfs-dkms

%{?systemd_requires}
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

for file in $(find src/systemd -type f);do
  install -D -pm 644 ${file} %{buildroot}%{_unitdir}${file#src/systemd}
done

%files
%defattr(-,root,root,-)
%{_sysconfdir}/*
%{_sbindir}/zmogrify
%{_unitdir}/*/*.conf

%changelog
* Tue May 30 2019 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.3.5-2
- Removed spl-dkms dependency

* Sun Aug 26 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.3.5-1
- Changed kernel modules detection

* Sun Aug 26 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.3.4-1
- Fixed typo in zmogrify

* Sun Aug 26 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.3.3-1
- Fixed building zfs modules in zmogrify

* Sat Aug 25 2018 Jerzy Drozdz <prmbuilder@jdsieci.pl> - 1.3.2-1
- Added checking if zfs modules are present in kernel

* Wed Aug 15 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.3.1-1
- Fixed checksum output file name

* Fri Nov 11 2017 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.3-1
- Added dropin files for systemd

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
