Summary:	Programs for maintaining networked machines' time synchronization
Summary(de):	TCP/IP-Time-of-Day-Server 
Summary(fr):	Serveur horaire TCP/IP
Summary(pl):	Serwer us³ugi umo¿liwiaj±cej synchronizacjê czasu miêdzy komputerami
Summary(tr):	TCP/IP günün saati sunucusu
Name:		timed
Version:	0.10
Release:	24
Copyright:	BSD
Group:		Daemons
Group(pl):	Servery
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/admin/time/netkit-timed-%{version}.tar.gz
Source1:	timedt.inetd
Source2:	timedu.inetd
Patch0:		netkit-timed-misc.patch
Patch1:		timed-ifr.patch
Patch2:		timed-maint.patch
Prereq:		rc-inetd
Buildroot:	/tmp/%{name}-%{version}-root

%description
The timed package contains the timed daemon and the timedc program for
controlling the timed program. Timed synchronizes its host machine's time
with the time on other local network machines. The timedc program is used
to control and configure the operation of timed and allow:

 - measure the differences between machines' clocks,
 - find the location where the master time server is running,
 - enable or disable tracing of messages received by timed,
 - perform various debugging actions.

%description -l de
Dieser Server mit Zeitgeber ermöglicht es einem entfernten Rechner, die
Uhrzeit des Rechners abzufragen, auf dem der Server läuft. So können Sie auf
einfache Weise die Uhrzeit im gesamten Netzwerk synchronisieren.

%description -l fr
Ce serveur timed permet aux machines distantes de demander la date du jour à
la machine sur laquelle tourne le serveur. Ceci permet une synchronisation
simple du temps à travers un réseau.

%description -l pl
Pakiet timed zawiera serwer us³ugi serwujacej bierz±cy czas o nazwie timed i
program timedc umo¿liwiaj±ce kontrolê programu timed. Program timedc
umozliwia min.:

- pomiar w ustawienaich czas miedzy komputerami,
- odszukiwanie nadrzednych serwerów czau,
- w³±czanie i wy³aczanie ¶ledzenia komunikatów otrzymywanych przez timed,
- diagnostykê pracy timed.
 
%description -l tr
timed sunucusu uzak makinelerin sunucuya baðlanarak zamaný öðrenmelerini
saðlar. Bu, bir að üzerindeki çeþitli makinalarýn saatlerinin eþ
tutulabilmeleri amacýyla kullanýlýr.

%prep
%setup -q -n netkit-timed-0.10
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man{1,8}} \
	$RPM_BUILD_ROOT/etc/sysconfig/rc-inetd

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
