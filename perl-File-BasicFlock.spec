%include	/usr/lib/rpm/macros.perl
Summary:	File-BasicFlock perl module
Summary(pl):	Modu³ perla File-BasicFlock
Name:		perl-File-BasicFlock
Version:	98.1202
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/File/File-BasicFlock-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File-BasicFlock - file locking with flock.

%description -l pl
File-BasicFlock umo¿liwia blokowanie pliku przy u¿yciu funkcji
flock().

%prep
%setup -q -n File-BasicFlock-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README CHANGELOG

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/File/BasicFlock.pm
%{_mandir}/man3/*
