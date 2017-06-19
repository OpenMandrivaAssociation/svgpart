%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		svgpart
Summary:	A SVG KPart
Version:	17.04.2
Release:	1
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	ninja
Conflicts:	kdegraphics4-core < 2:4.6.90

%description
A SVG KPart Service.

%files -f svgpart.lang
%{_libdir}/qt5/plugins/svgpart.so
%{_datadir}/kxmlgui5/svgpart
%{_datadir}/kservices5/svgpart.desktop

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang svgpart
