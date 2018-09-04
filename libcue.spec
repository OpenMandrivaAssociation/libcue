%define major	2
%define libname	%mklibname cue %major
%define devname	%mklibname -d cue 

Summary:	Cuesheet parser library
Name:		libcue
Version:	2.2.1
Release:	1
License:	GPLv2
Group:		System/Libraries
Url:		https://github.com/lipnitsk/libcue
Source0:	https://github.com/lipnitsk/libcue/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake

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
%cmake
%make_build

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libcue.so.%{major}*

%files -n %{devname}
%doc AUTHORS NEWS ChangeLog
%{_libdir}/libcue.so
%{_libdir}/pkgconfig/libcue.pc
%{_includedir}/libcue-1.4

