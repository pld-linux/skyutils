Summary:	its need for smssend-3.5
Summary(pl):	potrzebne do smssend-3.5
Name:		skyutils
Version:	2.5
Release:	0.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://zekiller.skytech.org/fichiers/%{name}-%{version}.tar.gz
# Source0-md5:	8edd6e5220283b6dd0a77080a1e06bee
URL:		http://zekiller.skytech.org/coders_en.html
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BLANK

%description -l pl
BRAK

%prep
%setup -q

%build
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README

%attr(755,root,root) %{_bindir}/skyutils-config
%{_libdir}/libskyutils*
