%include	/usr/lib/rpm/macros.perl
Summary:	File-BasicFlock perl module
Summary(pl):	Modu� perla File-BasicFlock
Name:		perl-File-BasicFlock
Version:	98.1202
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/File/File-BasicFlock-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File-BasicFlock - file locking with flock.

%description -l pl
File-BasicFlock umo�liwia blokowanie pliku przy u�yciu funkcji
flock().

%prep
%setup -q -n File-BasicFlock-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/File/BasicFlock
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README CHANGELOG

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGELOG}.gz

%{perl_sitelib}/File/BasicFlock.pm
%{perl_sitearch}/auto/File/BasicFlock

%{_mandir}/man3/*
