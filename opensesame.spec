%global origname OpenSesame
%global __python python3

Name:           opensesame
Version:        3.0.2
Release:        1%{?dist}
Summary:        graphical experiment builder for the social sciences
License:        GPLv3+
URL:            http://osdoc.cogsci.nl/
Source0:        https://github.com/smathot/OpenSesame/archive/release/%{version}/%{name}-%{version}.tar.gz
#https://github.com/smathot/OpenSesame/pull/365
Patch0:         0001-setup.py-fix-print-statement-for-py3.patch
BuildRequires:  git-core
Requires: 	python3-%{name}
BuildArch:      noarch

%description
OpenSesame is a tool to create experiments for psychology,
neuroscience, and experimental economics.

%package -n python2-%{name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{name}}
BuildRequires:  python2-devel
BuildRequires:  pygame
BuildRequires:  numpy
BuildRequires:  PyQt4
Requires:       pygame
Requires:       numpy
Requires:       PyQt4

%description -n python2-%{name}
OpenSesame is a tool to create experiments for psychology,
neuroscience, and experimental economics.
 
Python 2 version.
 

%package -n python3-%{name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{name}}
BuildRequires:  python3-devel
BuildRequires:  python3-pygame
BuildRequires:  python3-PyQt4
BuildRequires:  python3-numpy
Requires:       python3-PyQt4
Requires:       python3-numpy
 
Requires:       python3-pygame

%description -n python3-%{name}
OpenSesame is a tool to create experiments for psychology,
neuroscience, and experimental economics.
 
Python 3 version.

%prep
%autosetup -n %{origname}-release-%{version} -S git

%build
%py2_build
%py3_build
 
%install
%py2_install
%py3_install

#%check

%files
%license COPYING
%doc readme.md
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/*.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files -n python2-%{name}
%license COPYING
%doc readme.md
%{python2_sitelib}/%{name}-*
%{python2_sitelib}/openexp/
%{python2_sitelib}/libopensesame/
%{python2_sitelib}/libqtopensesame/

%files -n python3-%{name}
%license COPYING
%doc readme.md
%{python3_sitelib}/%{name}-*
%{python3_sitelib}/openexp/
%{python3_sitelib}/libopensesame/
%{python3_sitelib}/libqtopensesame/



%changelog
* Sat Nov  7 2015 Adrian Alves <alvesadrian@fedoraproject.org> - 3.0.2-1
- Initial package
