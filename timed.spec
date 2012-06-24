Summary:	Programs for maintaining networked machines' time synchronization
Summary(de):	TCP/IP-Time-of-Day-Server 
Summary(fr):	Serveur horaire TCP/IP
Summary(pl):	Serwer us�ugi umo�liwiaj�cej synchronizacj� czasu mi�dzy komputerami
Summary(tr):	TCP/IP g�n�n saati sunucusu
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
Dieser Server mit Zeitgeber erm�glicht es einem entfernten Rechner, die
Uhrzeit des Rechners abzufragen, auf dem der Server l�uft. So k�nnen Sie auf
einfache Weise die Uhrzeit im gesamten Netzwerk synchronisieren.

%description -l fr
Ce serveur timed permet aux machines distantes de demander la date du jour �
la machine sur laquelle tourne le serveur. Ceci permet une synchronisation
simple du temps � travers un r�seau.

%description -l pl
Pakiet timed zawiera serwer us�ugi serwujacej bierz�cy czas o nazwie timed i
program timedc umo�liwiaj�ce kontrol� programu timed. Program timedc
umo�liwia min.:

- pomiar w ustawienaich czasu mi�dzy komputerami,
- odszukiwanie nadrz�dnych serwer�w czasu,
- w��czanie i wy��czanie �ledzenia komunikat�w otrzymywanych przez timed,
- diagnostyk� pracy timed.
 
%description -l tr
timed sunucusu uzak makinelerin sunucuya ba�lanarak zaman� ��renmelerini
sa�lar. Bu, bir a� �zerindeki �e�itli makinalar�n saatlerinin e�
tutulabilmeleri amac�yla kullan�l�r.

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
