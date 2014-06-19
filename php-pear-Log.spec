%define		_status		stable
%define		pearname	Log
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - PHP PEAR logging utilities
Summary(pl.UTF-8):	%{pearname} - klasa z narzędziami logującymi
Name:		php-pear-%{pearname}
Version:	1.12.7
Release:	2
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	8594a3d89eac997f072fa088b1eddc42
URL:		http://pear.php.net/package/Log/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php(core) >= 4.3.0
Requires:	php-pear
Suggests:	php(sqlite)
Suggests:	php-pear-DB
Suggests:	php-pear-MDB2
Suggests:	php-pear-Mail
Obsoletes:	php-pear-Log-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq_pear DB.* MDB2.* Mail.*

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
%doc docs/%{pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{pearname}
%{php_pear_dir}/*.php
%{php_pear_dir}/Log/*.php
%{php_pear_dir}/data/%{pearname}
