%define upstream_name    String-Random
Name:       perl-%{upstream_name}
Version:    0.32
Release:    2

Summary:    Perl module to generate random strings based

License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://github.com/shlomif/string-random
Source0:    https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/String-Random-%{version}.tar.gz

BuildRequires: perl(Module::Build)
BuildRequires: perl(JSON::PP)
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
%setup -q -n %{upstream_name}-%{version}

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



