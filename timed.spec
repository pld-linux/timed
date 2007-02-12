Summary:	Programs for maintaining networked machines' time synchronization
Summary(de.UTF-8):   TCP/IP-Time-of-Day-Server
Summary(fr.UTF-8):   Serveur horaire TCP/IP
Summary(pl.UTF-8):   Serwer usługi umożliwiającej synchronizację czasu między komputerami
Summary(tr.UTF-8):   TCP/IP günün saati sunucusu
Name:		timed
Version:	0.17
Release:	5
License:	BSD
Group:		Daemons
Source0:	ftp://ftp.linux.org.uk/pub/linux/Networking/netkit/netkit-%{name}-%{version}.tar.gz
# Source0-md5:	1bffb4db753d9e5be227e444cf119bfe
Patch0:		%{name}-gcc2.96.patch
Patch1:		%{name}-DoS.patch
Obsoletes:	intimed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The timed package contains the timed daemon and the timedc program for
controlling the timed program. Timed synchronizes its host machine's
time with the time on other local network machines. The timedc program
is used to control and configure the operation of timed and allow:

 - measure the differences between machines' clocks,
 - find the location where the master time server is running,
 - enable or disable tracing of messages received by timed,
 - perform various debugging actions.

%description -l de.UTF-8
Dieser Server mit Zeitgeber ermöglicht es einem entfernten Rechner,
die Uhrzeit des Rechners abzufragen, auf dem der Server läuft. So
können Sie auf einfache Weise die Uhrzeit im gesamten Netzwerk
synchronisieren.

%description -l fr.UTF-8
Ce serveur timed permet aux machines distantes de demander la date du
jour à la machine sur laquelle tourne le serveur. Ceci permet une
synchronisation simple du temps à travers un réseau.

%description -l pl.UTF-8
Pakiet timed zawiera serwer usługi serwującej bieżący czas o nazwie
timed i program timedc umożliwiające kontrolę programu timed. Program
timedc umożliwia m.in.:

- pomiar w ustawieniach czasu między komputerami,
- odszukiwanie nadrzędnych serwerów czasu,
- włączanie i wyłączanie śledzenia komunikatów otrzymywanych przez
  timed,
- diagnostykę pracy timed.

%description -l tr.UTF-8
timed sunucusu uzak makinelerin sunucuya bağlanarak zamanı
öğrenmelerini sağlar. Bu, bir ağ üzerindeki çeşitli makinaların
saatlerinin eş tutulabilmeleri amacıyla kullanılır.

%prep
%setup -q -n netkit-timed-%{version}
%patch0 -p1
%patch1 -p1

%build
CFLAGS="%{rpmcflags}"; export CFLAGS
./configure
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man{1,8}}

%{__make} install \
	INSTALLROOT=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS ChangeLog README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
