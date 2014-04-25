%define upstream_name    String-Random
%define upstream_version 0.26

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Perl module to generate random strings based

License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/String/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Module::Build)
BuildArch: noarch

%description
This module makes it trivial to generate random strings.

As an example, let's say you are writing a script that needs to generate a
random password for a user. The relevant code might look something like
this:

  use String::Random;
  $pass = new String::Random;
  print "Your password is ", $pass->randpattern("CCcc!ccn"), "\n";

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%clean

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/String



