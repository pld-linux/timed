Summary: Programs for maintaining networked machines' time synchronization.
Name: timed
Version: 0.10
Release: 23
Copyright: BSD
Group: System Environment/Daemons
Source: ftp://sunsite.unc.edu/pub/Linux/system/admin/time/netkit-timed-0.10.tar.gz
Patch0: netkit-timed-0.10-misc.patch
Patch1: timed-0.10-ifr.patch
Patch2: timed-0.10-maint.patch
Requires: inetd
Buildroot: /var/tmp/%{name}-root

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
%patch0 -p1 -b .misc
%patch1 -p1 -b .ifr
%patch2 -p1 -b .maint

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,sbin}
mkdir -p $RPM_BUILD_ROOT/usr/man/man{1,8}
make INSTALLROOT=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/man/man8/timed.8
/usr/man/man8/timedc.8
/usr/sbin/timed
/usr/sbin/timedc
