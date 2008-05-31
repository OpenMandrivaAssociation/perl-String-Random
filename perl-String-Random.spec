%define module   String-Random
%define version    0.22
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Perl module to generate random strings based
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/String/%{module}-%{version}.tar.gz
BuildRequires: perl(Module::Build)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This module makes it trivial to generate random strings.

As an example, let's say you are writing a script that needs to generate a
random password for a user. The relevant code might look something like
this:

  use String::Random;
  $pass = new String::Random;
  print "Your password is ", $pass->randpattern("CCcc!ccn"), "\n";

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/String

