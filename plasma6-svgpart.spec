%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		plasma6-svgpart
Summary:	A SVG KPart
Version:	24.01.90
Release:	3
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/svgpart-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	ninja
Conflicts:	kdegraphics4-core < 2:4.6.90

%description
A SVG KPart Service.

%files -f svgpart.lang
%{_libdir}/qt6/plugins/kf6/parts/svgpart.so
#{_datadir}/kservices6/svgpart.desktop
%{_datadir}/metainfo/org.kde.svgpart.metainfo.xml

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n svgpart-%{?git:master}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang svgpart
