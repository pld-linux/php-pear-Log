%include        /usr/lib/rpm/macros.php
%define		_pearname	Log
Summary:	Log - php pear logging utilities
Summary(pl):	Klasa Log dla php pear z narz�dziami loguj�cymi
Name:		php-pear-%{_pearname}
Version:	1.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Log framework provides an abstracted logging system. It supports
logging to console, file, syslog, SQL, and mcal targets. It also
provides a subject - observer mechanism.

%description -l pl
Klasa Log daje abstrakcyjny system logowania. Obs�uguje logowanie do
pliku, na konsol�, do sysloga, bazy SQL oraz cel�w mcal. Dostarcza
tak�e mechanizm subject - observer.

%prep
%setup -q -c

%install
cd %{_pearname}-%{version}
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_pearname}

install *.php			$RPM_BUILD_ROOT%{php_pear_dir}
install %{_pearname}/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_pearname}
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_pearname}/*.php
