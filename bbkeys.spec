Summary:	bbkeys, a completely configurable key-combo grabber for blackbox
Summary(pl):	Ca³kowicie konfigurowalny przechwytywacz klawiszy dla blackboksa
Name:		bbkeys
Version:	0.8.3
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	http://movingparts.thelinuxcommunity.org/bbkeys/%{name}-%{version}.tar.gz
URL:		http://movingparts.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	XFree86-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
bbkeys is a configurable key-grabber designed for the blackbox window
manager which is written by Brad Hughes. It is based on the bbtools
object code created by John Kennis and re-uses some of the blackbox
window manager classes as well. bbkeys is easily configurable via
directly hand-editting the user's ~/.bbkeysrc file, or by using the
provided gui configuration tool, bbkeysconf (for lack of a better name
yet).

%description -l pl
bbkeys jest konfigurowalnym programem do przechwytywania klawiszy
zaprojektowanym dla zarz±dcy okien blackbox, napisanego przez Brada
Hughesa. Bazuje na kodzie obiektowym bbtools napisanym przez Johna
Kennisa, u¿ywa tak¿e niektórych klas blackboksa. bbkeys s± ³atwo
konfigurowalne przez bezpo¶redni±edycjê pliku u¿ytkownika ~/.bbkeysrc,
albo poprzez graficzny interfejs bbkeysconf (z braku lepszej nazwy).

%prep
%setup -q
aclocal
autoconf
automake -a -c
%configure
%build
%{__make} CXX="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/bbtools/%{name}.*
