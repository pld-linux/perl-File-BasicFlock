#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	BasicFlock
Summary:	File::BasicFlock - file locking with flock
Summary(pl.UTF-8):	File::BasicFlock - blokowanie plików za pomocą flock
Name:		perl-File-BasicFlock
Version:	98.1202
Release:	11
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	760451bfea6b4f20a2e31d81b3f4f551
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::BasicFlock module is used to lock files using the flock() call. 
The file to be locked must already exist.

%description -l pl.UTF-8
Moduł File::BasicFlock służy do blokowania plików za pomocą wywołania
flock(). Blokowany plik musi istnieć. 

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG
%{perl_vendorlib}/File/BasicFlock.pm
%{_mandir}/man3/*
