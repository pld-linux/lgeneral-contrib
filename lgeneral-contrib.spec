# NOTE: all scenarios from v0.1 are contained in current lgeneral-addon-scenpack package
Summary:	LGeneral game - contributed scenarios
Summary(pl.UTF-8):	Gra Linux General - dodatkowe scenariusze
Name:		lgeneral-contrib
Version:	0.1
Release:	1.1
License:	Freeware
Group:		Applications/Games
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	e08a8baf0dd3bc301ae4f061fff5011b
URL:		http://lgames.sourceforge.net/LGeneral/
Requires:	lgeneral
Requires:	lgeneral-data-pg
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
%dir %{_datadir}/lgeneral/scenarios/contrib
%{_datadir}/lgeneral/scenarios/contrib/Avalanche
%{_datadir}/lgeneral/scenarios/contrib/Bastogne
%{_datadir}/lgeneral/scenarios/contrib/Bismarck
%{_datadir}/lgeneral/scenarios/contrib/Dunkirk
%{_datadir}/lgeneral/scenarios/contrib/Korea
%{_datadir}/lgeneral/scenarios/contrib/Malta
%{_datadir}/lgeneral/scenarios/contrib/Motti
%{_datadir}/lgeneral/scenarios/contrib/Poland45
