Summary:	bbkeys, a completely configurable key-combo grabber for blackbox
Summary(pl):	Ca³kowicie konfigurowalny przechwytywacz klawiszy dla blackboksa
Name:		bbkeys
Version:	0.8.6
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/bbkeys/%{name}-%{version}.tar.gz
# Source0-md5:	6df58a99d136f21682b859b823d31b7d
Patch0:		%{name}-sysconfdir.patch
Patch1:		%{name}-ac_fixes.patch
Patch2:		%{name}-etc_dir.patch
URL:		http://bbkeys.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir		/etc/default

%description
bbkeys is a configurable key-grabber designed for the blackbox window
manager which is written by Brad Hughes. It is based on the bbtools
object code created by John Kennis and re-uses some of the blackbox
window manager classes as well. bbkeys is easily configurable via
directly hand-editing the user's ~/.bbkeysrc file, or by using the
provided gui configuration tool, bbkeysconf (for lack of a better name
yet).

%description -l pl
bbkeys jest konfigurowalnym programem do przechwytywania klawiszy
zaprojektowanym dla zarz±dcy okien blackbox, napisanego przez Brada
Hughesa. Bazuje na kodzie obiektowym bbtools napisanym przez Johna
Kennisa, u¿ywa tak¿e niektórych klas blackboksa. bbkeys s± ³atwo
konfigurowalne przez bezpo¶redni± edycjê pliku u¿ytkownika ~/.bbkeysrc,
albo poprzez graficzny interfejs bbkeysconf (z braku lepszej nazwy).

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog NEWS TODO
%dir %{_sysconfdir}/bbtools
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/bbtools/%{name}.*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
