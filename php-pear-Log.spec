%define		_pearname	Log
Summary:	Log php pear logging utilities
Summary(pl):	Klasa Log dla php pear z narzêdziami loguj±cymi
Name:		php-pear-%{_pearname}
Version:	1.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
PreReq:		php-pear >= 4.2.0
PreReq:		php-zlib >= 4.2.0
URL:		http://pear.php.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		peardir		%{_datadir}/pear

%description
The Log framework provides an abstracted logging system. It supports
logging to console, file, syslog, SQL, and mcal targets. It also
provides a subject - observer mechanism.

%description -l pl
Klasa Log:: dostarcza abstrakcyjnej klasy loguj±cej systemu. Wspiera
logowanie do pliku, na konsolê, sysloga, SQLa oraz celów mcal.
Dostarcza tak¿e mechanizm subject - observer.

%prep
%setup -q -n %{_pearname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{peardir}/%{_pearname}

install *.php			$RPM_BUILD_ROOT%{peardir}
install %{_pearname}/*.php	$RPM_BUILD_ROOT%{peardir}/%{_pearname}
install %{SOURCE0}		$RPM_BUILD_ROOT%{peardir}

%post
pear install %{peardir}/%{_pearname}-%{version}.tgz

%postun
pear uninstall %{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{peardir}/%{_pearname}
%{peardir}/%{_pearname}-%{version}.tgz
%ghost %{peardir}/*.php
%ghost %{peardir}/%{_pearname}/*.php
