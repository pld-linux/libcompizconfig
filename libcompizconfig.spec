Summary:	Alternative configuration system for compiz
Summary(pl.UTF-8):	Alternatywny system konfiguracji dla compiza
Name:		libcompizconfig
Version:	0.9.0
Release:	2
License:	LGPL v2.1+ (library, plugin), GPL v2+ (ini backend)
Group:		Libraries
Source0:	http://releases.compiz.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	10e221d409d2114b7ce35100cc31d9c2
URL:		http://www.compiz.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	compiz-devel >= %{version}
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	protobuf
BuildRequires:	protobuf-devel
BuildRequires:	xorg-lib-libX11-devel
Requires:	compiz-libs >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libcompizconfig is an alternative configuration system for compiz and
provides the following features:

- Automatic plugin list generation.
- Import/Export of the current configuration.
- Configuration profiles.
- Parsing of Compiz metadata files to provide an easy to use API for
  configuration managers.
- Conflict handling for plugins and actions.
- Support for different configuration storage backends.
- Desktop environment integration. If a backend provides desktop
  environment integration, then Compiz will share the keybindings and
  settings with the default desktop environment window manager like
  metacity or kwin.
- Its own Compiz configuration plugin "ccp" to provide all features of
  libcompizconfig with compiz.

%description -l pl.UTF-8
Libcompizconfig jest alternatywnym systemem konfiguracyjnym dla
compiza. Posiada następujące cechy:

- automatyczne tworzenie listy wtyczek,
- import/eksport aktualnej konfiguracji,
- profile konfiguracyjne,
- przetwarzanie plików metadanych Compiza w celu zapewnienia łatwego
  do użycia API dla menedżerów konfiguracji,
- obsługa konfliktów między wtyczkami i akcjami,
- wspieranie różnych backendów przechowywania konfiguracji,
- integracja ze środowiskiem graficznym; jeżeli backend wspiera
  integrację ze środowiskiem, to Compiz będzie współdzielił skróty
  klawiszowe i ustawienia z domyślnym zarządcą okien środowiska, takim
  jak metacity, czy kwin,
- własna wtyczka konfiguracyjna "ccp", udostępniająca wszystkie opcje
  libcompizconfiga w compizie.

%package devel
Summary:	Header files for libcompizconfig library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcompizconfig
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	compiz-devel >= %{version}
Requires:	libxml2-devel >= 2.0
Requires:	protobuf-devel
Requires:	xorg-lib-libX11-devel

%description devel
The header files are only needed for development of programs using the
libcompizconfig library.

%description devel -l pl.UTF-8
W pakiecie tym znajdują się pliki nagłówkowe, przeznaczone dla
programistów używających biblioteki libcompizconfig.

%package static
Summary:	Static libcompizconfig libraries
Summary(pl.UTF-8):	Biblioteki statyczne libcompizconfig
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcompizconfig library.

%description static -l pl.UTF-8
Biblioteka statyczna libcompizconfig.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/compiz/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/compizconfig/backends/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc TODO
%attr(755,root,root) %{_libdir}/libcompizconfig.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcompizconfig.so.0
%attr(755,root,root) %{_libdir}/compiz/libccp.so
%dir %{_libdir}/compizconfig
%dir %{_libdir}/compizconfig/backends
%attr(755,root,root) %{_libdir}/compizconfig/backends/libini.so
%dir %{_sysconfdir}/compizconfig
%{_sysconfdir}/compizconfig/config
%{_datadir}/compiz/ccp.xml

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcompizconfig.so
%{_libdir}/libcompizconfig.la
%{_includedir}/compizconfig
%{_pkgconfigdir}/libcompizconfig.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcompizconfig.a
