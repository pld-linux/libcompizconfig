Summary:	Alternative configuration system for compiz
Summary(pl.UTF-8):	Alternatywny system konfiguracji dla compiza
Name:		libcompizconfig
Version:	0.5.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://releases.compiz-fusion.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	75b523f00b92986b4b6df0544112b141
URL:		http://forum.compiz-fusion.org/
BuildRequires:	compiz-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
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
- import/export aktualnej konfiguracji,
- profile konfiguracyjne,
- przetwarzanie plików metadanych Compiza w celu zapewnienia łatwego
  do użycia API dla menedżerów konfiguracji,
- obsługa konfliktów między wtyczkami i akcjami,
- wspieranie różnych backendów przechowywania konfiguracji,
- integracja ze środowiskiem graficznym; jeżeli backend wspiera
  integrację ze środowiskiem, to Compiz będzie współdzielił skróty
  klawiszowe i ustawienia z domyślnym menedżerem okien środowiska,
  takim jak metacity, czy kwin,
- własna wtyczka konfiguracyjna "ccp", udostępniająca wszystkie opcje
  libcompizconfiga w compizie.

%package devel
Summary:	Header files for %{name}
Summary(pl.UTF-8):	Pliki nagłówkowe %{name}
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
The header files are only needed for development of programs using the
%{name} library.

%description devel -l pl.UTF-8
W pakiecie tym znajdują się pliki nagłówkowe, przeznaczone dla
programistów używających bibliotek %{name}.

%package static
Summary:	Static %{name} libraries
Summary(pl.UTF-8):	Biblioteki statyczne %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static %{name} libraries.

%description static -l pl.UTF-8
Biblioteki statyczne %{name}.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.0
%attr(755,root,root) %{_libdir}/compiz/*.so
%dir %{_libdir}/compizconfig
%dir %{_libdir}/compizconfig/backends
%attr(755,root,root) %{_libdir}/compizconfig/backends/*.so
%{_datadir}/compizconfig

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_pkgconfigdir}/*.pc
%{_includedir}/compizconfig

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
