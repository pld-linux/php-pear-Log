%include        /usr/lib/rpm/macros.php
%define		_class		Log
%define		_pearname	%{_class}
Summary:	%{_pearname} - php pear logging utilities
Summary(pl):	%{_pearname} - klasa z narzêdziami loguj±cymi
Name:		php-pear-%{_pearname}
Version:	1.4
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Log framework provides an abstracted logging system. It supports
logging to console, file, syslog, SQL, mail and mcal targets. It also
provides a subject - observer mechanism.

%description -l pl
Klasa Log daje abstrakcyjny system logowania. Obs³uguje logowanie do
pliku, na konsolê, do sysloga, bazy SQL, poczt± oraz celów mcal. Dostarcza
tak¿e mechanizm subject - observer.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_pearname}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}
install %{_pearname}-%{version}/%{_pearname}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_pearname}
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_pearname}/*.php
