Name: svgpart
Summary: A SVG KPart
Version: 4.6.90
Release: 1
Epoch: 2
Group: Graphical desktop/KDE
License: GPLv2
URL: http://www.kde.org
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}
Conflicts: kdegraphics4-core < 2:4.6.90

%description
A SVG KPart Service.

%files
%_kde_libdir/kde4/svgpart.so
%_kde_appsdir/svgpart/svgpart.rc
%_kde_services/svgpart.desktop

#----------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

