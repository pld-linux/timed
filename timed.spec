Summary:	Programs for maintaining networked machines' time synchronization.
Name:		timed
Version:	0.10
Release:	24
Copyright:	BSD
Group:		System Environment/Daemons
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/admin/time/netkit-timed-%{version}.tar.gz
Source1:	timedt.inetd
Source2:	timedu.inetd
Patch0:		netkit-timed-0.10-misc.patch
Patch1:		timed-0.10-ifr.patch
Patch2:		timed-0.10-maint.patch
Prereq:		rc-inetd
Buildroot:	/tmp/%{name}-%{version}-root

%description
The timed package contains the timed daemon and the timedc program
for controlling the timed program.  Timed synchronizes its host
machine's time with the time on other local network machines.  The
timedc program is used to control and configure the operation of
timed.

Install the timed package if you need a system for keeping networked
machines' times in synchronization.

%prep
%setup -q -n netkit-timed-0.10
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man{1,8}}
install -d $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd

make install \
	INSTALLROOT=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/timedt
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/timedu

strip --strip-unneeded $RPM_BUILD_ROOT%{_sbindir}/*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd restart 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet sever" 1>&2
fi

%postun
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd restart
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/timed
%attr(700,root,root) %{_sbindir}/timedc
%attr(640,root,root) %config(noreplace) %verify(not mtime md5 size) /etc/sysconfig/rc-inetd/*
%{_mandir}/man8/timed.8*
%{_mandir}/man8/timedc.8*
