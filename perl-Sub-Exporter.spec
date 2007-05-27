#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Sub
%define	pnam	Exporter
Summary:	Sub::Exporter - a sophisticated exporter for custom-built routines
#Summary(pl):
Name:		perl-Sub-Exporter
Version:	0.974
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	916be83adf51eb8a0412f98e72605c88
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Data::OptList) >= 0.1
BuildRequires:	perl(Params::Util) >= 0.14
BuildRequires:	perl(Sub::Install) >= 0.92
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ACHTUNG! If you're not familiar with Exporter or exporting, read
Sub::Exporter::Tutorial first!

The biggest benefit of Sub::Exporter over existing exporters
(including the ubiquitous Exporter.pm) is its ability to build new
coderefs for export, rather than to simply export code identical to
that found in the exporting package.

If your module's consumers get a routine that works like this:

use Data::Analyze qw(analyze); my $value = analyze($data, $tolerance,
$passes);

and they constantly pass only one or two different set of values for
the non-$data arguments, your code can benefit from Sub::Exporter. By
writing a simple generator, you can let them do this, instead:



# %description -l pl # TODO

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Sub/*.pm
#%%{perl_vendorlib}/Sub/Exporter
%{_mandir}/man3/*
