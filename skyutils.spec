Summary:	SkyUtils - a library of utility funkctions by Christophe Calmejane
Summary(pl):	SkyUtils - biblioteka funkcji narzêdziowych Christophe'a Calmejane
Name:		skyutils
Version:	2.6
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://zekiller.skytech.org/fichiers/%{name}-%{version}.tar.gz
# Source0-md5:	ff04d28365ba9c18a1c5fdad41b5d4cc
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

%description -l pl
Biblioteka SkyUtils autorstwa Christophe'a Calmejane (Ze KiLleR /
SkyTech) zawiera funkcje narzêdziowe u¿ywane w wielu projektach tego
samego autora. Mo¿na znale¼æ tu wiele przydatnych funkcji, od listy do
protoko³u HTTP.

%package devel
Summary:	Header files for SkyUtils library
Summary(pl):	Pliki nag³ówkowe biblioteki SkyUtils
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for SkyUtils library.

%description devel -l pl
Pliki nag³ówkowe biblioteki SkyUtils.

%package static
Summary:	Static version of SkyUtils library
Summary(pl):	Statyczna wersja biblioteki SkyUtils
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of SkyUtils library.

%description static -l pl
Statyczna wersja biblioteki SkyUtils.

%prep
%setup -q

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
%doc AUTHORS ChangeLog NEWS README
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
