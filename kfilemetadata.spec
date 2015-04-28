Summary:	A KDE library for extracting file metadata
Name:		kfilemetadata
Version:	4.14.3
Release:	3
License:	GPLv2+
Group:		Graphical desktop/KDE
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%name-%{version}.tar.xz
Url:		https://www.kde.org/
BuildRequires:	ebook-tools-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	qmobipocket-devel
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(poppler-qt4)
BuildRequires:	pkgconfig(taglib)

%description
A KDE library for extracting file metadata.

%files
%{_kde_libdir}/kde4/*.so
%{_kde_services}/*.desktop
%{_kde_servicetypes}/kfilemetadataextractor.desktop

#----------------------------------------------------------------------------

%define kfilemetadata_major 4
%define libkfilemetadata %mklibname kfilemetadata %{kfilemetadata_major}

%package -n %{libkfilemetadata}
Summary:	A KDE library for extracting file metadata
Group:		System/Libraries

%description -n %{libkfilemetadata}
A KDE library for extracting file metadata.

%files -n %{libkfilemetadata}
%{_kde_libdir}/libkfilemetadata.so.%{kfilemetadata_major}*

#----------------------------------------------------------------------------

%define devkfilemetadata %mklibname kfilemetadata -d

%package -n %{devkfilemetadata}

Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libkfilemetadata} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devkfilemetadata}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{devkfilemetadata}
%{_kde_libdir}/libkfilemetadata.so
%{_kde_includedir}/kfilemetadata/
%{_kde_libdir}/cmake/KFileMetaData

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.14.3-1
- New version 4.14.3

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.14.1-1
- New version 4.14.1

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-1
- Initial Rosa package
