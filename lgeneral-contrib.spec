Summary:	LGeneral game - contributed scenarios
Summary(pl):	Gra Linux General - dodatkowe scenariusze
Name:		lgeneral-contrib
Version:	0.1
Release:	0.9
License:	?
Group:		Applications/Games
BuildArch:	noarch
Source0:	%{name}-%{version}.tar.bz2
URL:		http://lgames.sourceforge.net/
Requires:	lgeneral
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer
General. This package contains contributed scenarios.

%description -l pl
LGeneral jest turow± gr± strategiczn± zainspirowan± o Panzer General.
Ten pakiet zawiera dodatkowe scenariusze, nades³ane przez graczy.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/lgeneral/scenarios/contrib
cp * $RPM_BUILD_ROOT/%{_datadir}/lgeneral/scenarios/contrib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/lgeneral/scenarios/contrib
