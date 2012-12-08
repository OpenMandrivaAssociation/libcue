%define major 1
%define libname %mklibname cue %major
%define develname %mklibname -d cue 

Summary:	Cuesheet parser library
Name:		libcue
Version:	1.4.0
Release:	3
License:	GPLv2
Group:		System/Libraries
Url:		http://libcue.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.bz2

%description
This is a library for parsing cue sheets which describe audio CD images. They
are useful for gapless music playback.

%package -n %{libname}
Group:		System/Libraries
Summary:	Cuesheet parser library

%description -n %{libname}
This is a library for parsing cue sheets which describe audio CD images. They
are useful for gapless music playback.

%package -n %{develname}
Group:		Development/C
Summary:	Cuesheet parser library
Requires:	%{libname} = %{version}-%{release}
Provides:	libcue-devel = %{version}-%{release}

%description -n %{develname}
This is a library for parsing cue sheets which describe audio CD images. They
are useful for gapless music playback.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libcue.so.%{major}*

%files -n %{develname}
%doc AUTHORS NEWS ChangeLog
%{_libdir}/libcue.so
%{_libdir}/pkgconfig/libcue.pc
%{_includedir}/libcue-1.4



%changelog
* Tue Jul 12 2011 Götz Waschk <waschk@mandriva.org> 1.4.0-2
+ Revision: 689635
- rebuild

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 1.4.0-1mdv2011.0
+ Revision: 550983
- new version
- update file list

* Tue Nov 10 2009 Götz Waschk <waschk@mandriva.org> 1.3.0-1mdv2010.1
+ Revision: 463976
- import libcue

