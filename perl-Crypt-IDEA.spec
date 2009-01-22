Summary:	Perl interface to IDEA block cipher
Name:		perl-Crypt-IDEA
Version:	1.08
Release:	2%{?dist}
License:	BSD with advertising
Group:		Development/Libraries
Url:		http://search.cpan.org/dist/Crypt-IDEA/
Source0:	http://search.cpan.org/CPAN/authors/id/D/DP/DPARIS/Crypt-IDEA-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRequires:	perl(ExtUtils::MakeMaker), perl(Test::More)

%description
This perl extension is an implementation of the IDEA block cipher algorithm.
The module implements the Crypt::BlockCipher interface.

The IDEA algorithm is patented in Europe and the United States by Ascom-Tech
AG. This implementation is copyright Systemics Ltd (http://www.systemics.com/).

%prep
%setup -q -n Crypt-IDEA-%{version}

# Remove unnecessary shellbang that points to the wrong perl interpreter anyway
%{__sed} -i -e '\|^#! */usr/local/bin/perl |d' IDEA.pm

# Remove file we don't want packaged
%{__rm} -f ._test.pl

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install PERL_INSTALL_ROOT=%{buildroot}
/usr/bin/find %{buildroot} -type f -name .packlist -exec %{__rm} -f {} \;
/usr/bin/find %{buildroot} -type f -name '*.bs' -a -size 0 -exec %{__rm} -f {} \;
/usr/bin/find %{buildroot} -depth -type d -exec /bin/rmdir {} 2>/dev/null \;
%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYRIGHT changes
%{perl_vendorarch}/Crypt/
%{perl_vendorarch}/auto/Crypt/
%{_mandir}/man3/Crypt::IDEA.3pm*

%changelog
* Wed Jan 21 2009 Paul Howarth <paul@city-fan.org> 1.08-2
- Include "changes" file in documentation
- Use a different delimiter for sed command in %%prep to improve readability

* Thu Nov 27 2008 Paul Howarth <paul@city-fan.org> 1.08-1
- Update to 1.08
- Clean up for submission to RPM Fusion
  (http://bugzilla.rpmfusion.org/show_bug.cgi?id=195)

* Fri Dec  2 2005 Paul Howarth <paul@city-fan.org> 1.02-1
- Initial build
