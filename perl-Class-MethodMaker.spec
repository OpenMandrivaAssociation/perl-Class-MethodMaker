%define	upstream_name	 Class-MethodMaker
%define upstream_version 2.21

Summary:	Create generic methods for OO Perl
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel

%description
This module solves the problem of having to write a bazillion
get/set methods that are all the same. The argument to 'use'
is a hash whose keys are the names of types of generic
methods generated by MethodMaker and whose values tell method
maker what methods to make. (More precisely, the keys are the
names of MethodMaker methods (methods that write methods) and
the values are the arguments to those methods.

%prep
%setup -qn %{upstream_name}-%{upstream_version}
rm -f t/0-signature.t # debug files make it fails

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README TODO Changes
%{perl_vendorarch}/Class
%{perl_vendorarch}/auto/Class
%{_mandir}/man3/*



