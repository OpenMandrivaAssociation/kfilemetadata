%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
%define libname %{mklibname KF5FileMetaData}
%define devname %{mklibname KF5FileMetaData -d}

Summary:	File metadata parsing library
Name:		kfilemetadata
Version:	5.112.0
Release:	1
License:	LGPL
Group:		Graphical desktop/KDE
Url:		http://kde.org/
Source0:	http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/kfilemetadata-%{version}.tar.xz
Source1000:	%{name}.rpmlintrc
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(QMobipocket)
BuildRequires:	ebook-tools-devel
BuildRequires:	pkgconfig(poppler-qt5)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libssh)
BuildRequires:	cmake(Gettext)
BuildRequires:	ffmpeg-devel
BuildRequires:	attr-devel
BuildRequires:	lld
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
Requires: %{libname} = %{EVRD}
%rename %{name}5
Obsoletes: %{mklibname KF5FileMetaData 5}

%dependinglibpackage KF5FileMetaData 5
%{_libdir}/libKF5FileMetaData.so.3

%description
File metadata parsing library.

%files -f kfilemetadata5.lang
# FIXME may want to split some not so commonly used plugins into subpackages
%dir %{_libdir}/qt5/plugins/kf5/kfilemetadata
%dir %{_libdir}/qt5/plugins/kf5/kfilemetadata/writers
%{_libdir}/qt5/plugins/kf5/kfilemetadata/kfilemetadata_*.so
%{_libdir}/qt5/plugins/kf5/kfilemetadata/writers/kfilemetadata_*.so
%{_datadir}/qlogging-categories5/kfilemetadata.*categories

%package -n %{devname}
Summary:	Development files for KFileMetaData
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Conflicts:	%{name} < 5.13.0-2

%description -n %{devname}
Development files for KFileMetaData.

%files -n %{devname}
%{_libdir}/cmake/KF5FileMetaData
%{_includedir}/KF5/KFileMetaData
%{_libdir}/*.so
%{_libdir}/qt5/mkspecs/modules/qt_KFileMetaData.pri

#----------------------------------------------------------------------------
%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
#----------------------------------------------------------------------------

%prep
%autosetup -n kfilemetadata-%{version} -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kfilemetadata5
