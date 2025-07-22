#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		svgpart
Summary:	A SVG KPart
Version:	25.04.3
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/graphics/svgpart/-/archive/%{gitbranch}/svgpart-%{gitbranchd}.tar.bz2#/svgpart-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/svgpart-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6SvgWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Parts)

%rename plasma6-svgpart

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
A SVG KPart Service.

%files -f %{name}.lang
%{_libdir}/qt6/plugins/kf6/parts/svgpart.so
#{_datadir}/kservices6/svgpart.desktop
%{_datadir}/metainfo/org.kde.svgpart.metainfo.xml
