Summary:	Perl interface to IDEA block cipher
Name:		perl-Crypt-IDEA
Version:	1.08
Release:	9%{?dist}
License:	BSD with advertising
Group:		Development/Libraries
Url:		http://search.cpan.org/dist/Crypt-IDEA/
Source0:	http://search.cpan.org/CPAN/authors/id/D/DP/DPARIS/Crypt-IDEA-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -nu)
BuildRequires:	perl(Carp)
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More)
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

# Don't provide private perl libs
%{?perl_default_filter}

%description
This perl extension is an implementation of the IDEA block cipher algorithm.
The module implements the Crypt::BlockCipher interface.

The IDEA algorithm is patented in Europe and the United States by Ascom-Tech
AG. This implementation is copyright Systemics Ltd (http://www.systemics.com/).

%prep
%setup -q -n Crypt-IDEA-%{version}

# Remove unnecessary shellbang that points to the wrong perl interpreter anyway
sed -i -e '\|^#! */usr/local/bin/perl |d' IDEA.pm

# Remove file we don't want packaged
rm -f ._test.pl

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} \;
%{_fixperms} %{buildroot}

%check
make test

%clean
rm -rf %{buildroot}

%files
%doc COPYRIGHT changes
%{perl_vendorarch}/Crypt/
%{perl_vendorarch}/auto/Crypt/
%{_mandir}/man3/Crypt::IDEA.3pm*

%changelog
* Wed May  2 2012 Paul Howarth <paul@city-fan.org> - 1.08-9
- Spec clean-up:
  - Don't need to remove empty directories from buildroot
  - Drop %%defattr, redundant since rpm 4.4

* Thu Feb 16 2012 Paul Howarth <paul@city-fan.org> - 1.08-8
- Spec clean-up:
  - Don't use macros for commands
  - Use DESTDIR rather than PERL_INSTALL_ROOT
  - Use %%{_fixperms} macro rather than our own chmod incantation
  - One buildreq per line
  - Add buildreqs for Perl core modules that might be dual-lived

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep 28 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.08-6
- Rebuilt for perl

* Tue Aug 24 2010 Paul Howarth <paul@city-fan.org> 1.08-5
- Rebuild for Perl 5.12.1

* Wed Feb  3 2010 Paul Howarth <paul@city-fan.org> 1.08-4
- Rebuild for Perl 5.10.1
- Filter bogus provides for shared objects

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 1.08-3
- Rebuild for new F11 features

* Wed Jan 21 2009 Paul Howarth <paul@city-fan.org> 1.08-2
- Include "changes" file in documentation
- Use a different delimiter for sed command in %%prep to improve readability

* Thu Nov 27 2008 Paul Howarth <paul@city-fan.org> 1.08-1
- Update to 1.08
- Clean up for submission to RPM Fusion
  (http://bugzilla.rpmfusion.org/show_bug.cgi?id=195)

* Fri Dec  2 2005 Paul Howarth <paul@city-fan.org> 1.02-1
- Initial build
