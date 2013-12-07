%define major	1
%define libname	%mklibname cue %major
%define devname	%mklibname -d cue 

Summary:	Cuesheet parser library
Name:		libcue
Version:	1.4.0
Release:	7
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

%package -n %{devname}
Group:		Development/C
Summary:	Cuesheet parser library
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
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

%files -n %{devname}
%doc AUTHORS NEWS ChangeLog
%{_libdir}/libcue.so
%{_libdir}/pkgconfig/libcue.pc
%{_includedir}/libcue-1.4

