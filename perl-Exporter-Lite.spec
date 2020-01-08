#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Exporter-Lite
Version  : 0.08
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Exporter-Lite-0.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Exporter-Lite-0.08.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Exporter-Lite-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This module is a lightweight version of the core Exporter module,
providing a subset of that module's functionality.

%package dev
Summary: dev components for the perl-Exporter-Lite package.
Group: Development
Provides: perl-Exporter-Lite-devel = %{version}-%{release}
Requires: perl-Exporter-Lite = %{version}-%{release}

%description dev
dev components for the perl-Exporter-Lite package.


%package perl
Summary: perl components for the perl-Exporter-Lite package.
Group: Default
Requires: perl-Exporter-Lite = %{version}-%{release}

%description perl
perl components for the perl-Exporter-Lite package.


%prep
%setup -q -n Exporter-Lite-0.08
cd %{_builddir}/Exporter-Lite-0.08

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Exporter::Lite.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.1/Exporter/Lite.pm
