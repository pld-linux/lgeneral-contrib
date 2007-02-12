Summary:	LGeneral game - contributed scenarios
Summary(pl.UTF-8):   Gra Linux General - dodatkowe scenariusze
Name:		lgeneral-contrib
Version:	0.1
Release:	1
License:	Freeware
Group:		Applications/Games
Source0:	%{name}-%{version}.tar.bz2
URL:		http://lgames.sourceforge.net/
Requires:	lgeneral
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer
General. This package contains contributed scenarios.

%description -l pl.UTF-8
LGeneral jest turową grą strategiczną zainspirowaną o Panzer General.
Ten pakiet zawiera dodatkowe scenariusze, nadesłane przez graczy.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/lgeneral/scenarios/contrib

cp * $RPM_BUILD_ROOT%{_datadir}/lgeneral/scenarios/contrib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/lgeneral/scenarios/contrib
