%define upstream_name    POE-Component-Pluggable
%define upstream_version 1.26

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	A base class for creating plugin enabled POE Components
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(POE)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
POE::Component::Pluggable is a base class for creating plugin enabled POE
Components. It is a generic port of POE::Component::IRC's plugin system.

If your component dispatches events to registered POE sessions, then
POE::Component::Pluggable may be a good fit for you.

Basic use would involve subclassing POE::Component::Pluggable, then
overriding '_pluggable_event()' and inserting '_pluggable_process()'
wherever you dispatch events from.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/POE

%changelog
* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.260.0-1mdv2011.0
+ Revision: 552483
- update to 1.26

* Wed Aug 19 2009 Jérôme Quelin <jquelin@mandriva.org> 1.240.0-1mdv2010.0
+ Revision: 418122
- update to 1.24

* Fri Jul 24 2009 Jérôme Quelin <jquelin@mandriva.org> 1.220.0-1mdv2010.0
+ Revision: 399263
- update to 1.22
- using %%perl_convert_version
- fixed license field

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.20-1mdv2010.0
+ Revision: 371734
- update to new version 1.20

* Thu Mar 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.16-1mdv2009.1
+ Revision: 348832
- update to new version 1.16

* Fri Jan 30 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.14-1mdv2009.1
+ Revision: 335512
- update to new version 1.14

* Sun Jan 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-1mdv2009.1
+ Revision: 333406
- update to new version 1.12

* Fri Jun 27 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-1mdv2009.0
+ Revision: 229494
- update to new version 1.10

* Mon Jun 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-1mdv2009.0
+ Revision: 220160
- update to new version 1.08

* Tue Jun 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-1mdv2009.0
+ Revision: 214509
- import perl-POE-Component-Pluggable


* Tue Jun 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-1mdv2009.0
- first mdv release
