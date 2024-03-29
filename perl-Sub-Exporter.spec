#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Sub
%define	pnam	Exporter
Summary:	Sub::Exporter - a sophisticated exporter for custom-built routines
Summary(pl.UTF-8):	Sub::Exporter - wymyślny eksporter dla własnych funkcji
Name:		perl-Sub-Exporter
Version:	0.988
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sub/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9ccc63fd0f1d77e3e1a24bec07e05638
URL:		http://search.cpan.org/dist/Sub-Exporter/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Data-OptList >= 0.100
BuildRequires:	perl-Package-Generator
BuildRequires:	perl-Params-Util >= 0.14
BuildRequires:	perl-Sub-Install >= 0.92
BuildRequires:	perl-Test-Simple >= 0.96
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The biggest benefit of Sub::Exporter over existing exporters
(including the ubiquitous Exporter.pm) is its ability to build new
coderefs for export, rather than to simply export code identical to
that found in the exporting package.

%description -l pl.UTF-8
Największą zaletą modułu Sub::Exporter w stosunku do istniejących
wcześniej eksporterów (wraz z wszechobecnym Exporter.pm) jest
możliwość budowania nowych coderefów do exportowania zamiast zwykłego
eksportowania kodu identycznego do tego, jaki można znaleźć w
eksportowanym pakiecie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# exist as man
%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Sub/Exporter/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Sub/Exporter.pm
%dir %{perl_vendorlib}/Sub/Exporter
%{perl_vendorlib}/Sub/Exporter/*.pm
%{_mandir}/man3/Sub::Exporter*.3pm*
