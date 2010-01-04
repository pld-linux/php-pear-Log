%include	/usr/lib/rpm/macros.php
%define		_class		Log
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - PHP PEAR logging utilities
Summary(pl.UTF-8):	%{_pearname} - klasa z narzędziami logującymi
Name:		php-pear-%{_pearname}
Version:	1.11.6
Release:	1
Epoch:		0
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a390fd9940e3c1785fd19341b543f135
URL:		http://pear.php.net/package/Log/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.3.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(DB.*)' 'pear(MDB2.*)'

%description
The Log framework provides an abstracted logging system. It supports
logging to console, file, syslog, SQL, mail and mcal targets. It also
provides a subject - observer mechanism.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa Log daje abstrakcyjny system logowania. Obsługuje logowanie do
pliku, na konsolę, do sysloga, bazy SQL, pocztą oraz celów mcal.
Dostarcza także mechanizm subject - observer.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_pearname}
%{php_pear_dir}/*.php
%{php_pear_dir}/Log/*.php
%{php_pear_dir}/data/%{_pearname}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
