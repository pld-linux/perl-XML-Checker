#
# Conditional build:
%bcond_without tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Checker
Summary:	XML::Checker - a Perl module for validating XML
Summary(pl):	XML::Checker - modu� Perla do sprawdzania poprawno�ci XML-a
Name:		perl-XML-Checker
Version:	0.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6fddcc489b4d9a5063e3a34d72400da9
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-Parser >= 2.30
BuildRequires:	perl(XML::DOM) >= 1.29
BuildRequires:	perl-libxml >= 0.07
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Checker can be used in different ways to validate XML. See the
manual pages of XML::Checker::Parser and XML::DOM::ValParser for more
information.

%description -l pl
XML::Checker mo�e by� u�ywany w r�ny spos�b do sprawdzania
poprawno�ci XML-a. Wi�cej informacji znajduje si� w stronach manuala
XML::Checker::Parser i XML::DOM::ValParser.

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
%{perl_vendorlib}/XML/Checker*
%{perl_vendorlib}/XML/DOM/*
%{_mandir}/man3/*
