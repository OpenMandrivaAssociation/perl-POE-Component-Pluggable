%define module   POE-Component-Pluggable
%define version    1.06
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    A base class for creating plugin enabled POE Components
Source:     http://www.cpan.org/modules/by-module/POE/%{module}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{module}
BuildRequires: perl(Carp)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(POE)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
POE::Component::Pluggable is a base class for creating plugin enabled POE
Components. It is a generic port of POE::Component::IRC's plugin system.

If your component dispatches events to registered POE sessions, then
POE::Component::Pluggable may be a good fit for you.

Basic use would involve subclassing POE::Component::Pluggable, then
overriding '_pluggable_event()' and inserting '_pluggable_process()'
wherever you dispatch events from.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README LICENSE
%{_mandir}/man3/*
%perl_vendorlib/POE

