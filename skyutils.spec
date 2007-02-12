Summary:	SkyUtils - a library of utility funkctions by Christophe Calmejane
Summary(pl.UTF-8):	SkyUtils - biblioteka funkcji narzędziowych Christophe'a Calmejane
Name:		skyutils
Version:	2.9
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://zekiller.skytech.org/fichiers/%{name}-%{version}.tar.gz
# Source0-md5:	e2b518f239aea5fb59f416d8c9c22213
URL:		http://zekiller.skytech.org/coders_en.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SkyUtils library by Christophe Calmejane (Ze KiLleR / SkyTech)
contains utility functions used in many projects by the same
author. From chained list to HTTP protocol, you may find many
useful functions.

%description -l pl.UTF-8
Biblioteka SkyUtils autorstwa Christophe'a Calmejane (Ze KiLleR /
SkyTech) zawiera funkcje narzędziowe używane w wielu projektach tego
samego autora. Można znaleźć tu wiele przydatnych funkcji, od listy do
protokołu HTTP.

%package devel
Summary:	Header files for SkyUtils library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SkyUtils
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for SkyUtils library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SkyUtils.

%package static
Summary:	Static version of SkyUtils library
Summary(pl.UTF-8):	Statyczna wersja biblioteki SkyUtils
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of SkyUtils library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki SkyUtils.

%prep
%setup -q -n %{name}

%build
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libskyutils*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/skyutils-config
%attr(755,root,root) %{_libdir}/libskyutils.so
%{_libdir}/libskyutils.la
%{_includedir}/skyutils.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libskyutils.a
