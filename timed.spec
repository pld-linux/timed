Summary:	Programs for maintaining networked machines' time synchronization
Summary(de):	TCP/IP-Time-of-Day-Server 
Summary(fr):	Serveur horaire TCP/IP
Summary(pl):	Serwer us³ugi umo¿liwiaj±cej synchronizacjê czasu miêdzy komputerami
Summary(tr):	TCP/IP günün saati sunucusu
Name:		timed
Version:	0.17
Release:	1
Copyright:	BSD
Group:		Daemons
Group(pl):	Serwery
Source:		ftp://ftp.linux.org.uk/pub/linux/Networking/netkit/netkit-timed-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
umo¿liwia min.:

- pomiar w ustawienaich czasu miådzy komputerami,
- odszukiwanie nadrzådnych serwerów czasu,
- w³±czanie i wy³áczanie ¶ledzenia komunikatów otrzymywanych przez timed,
- diagnostykê pracy timed.
 
%description -l tr
timed sunucusu uzak makinelerin sunucuya baðlanarak zamaný öðrenmelerini
saðlar. Bu, bir að üzerindeki çeþitli makinalarýn saatlerinin eþ
tutulabilmeleri amacýyla kullanýlýr.

%prep
%setup -q -n netkit-timed-%{version}

%build
CFLAGS=$RPM_OPT_FLAGS ; export CFLAGS
./configure --with-c-compiler=gcc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man{1,8}}

%{__make} install \
	INSTALLROOT=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}

strip --strip-unneeded $RPM_BUILD_ROOT%{_sbindir}/*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
