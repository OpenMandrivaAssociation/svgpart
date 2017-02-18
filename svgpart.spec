Name:		svgpart
Summary:	A SVG KPart
Version:	16.12.2
Release:	1
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://www.kde.org
%define is_beta %(if test `echo %version |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
Conflicts:	kdegraphics4-core < 2:4.6.90

%description
A SVG KPart Service.

%files                                                                                                 
%{_libdir}/kde4/svgpart.so                                                                             
%{_datadir}/apps/svgpart/svgpart.rc                                                                    
%{_datadir}/kde4/services/svgpart.desktop 

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build

