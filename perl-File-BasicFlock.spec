%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	BasicFlock
Summary:	File::BasicFlock perl module
Summary(pl):	Modu³ perla File::BasicFlock
Name:		perl-File-BasicFlock
Version:	98.1202
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::BasicFlock - file locking with flock.

%description -l pl
File::BasicFlock umo¿liwia blokowanie pliku przy u¿yciu funkcji
flock().

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG
%{perl_vendorlib}/File/BasicFlock.pm
%{_mandir}/man3/*
