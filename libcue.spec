%define name libcue
%define version 1.3.0
%define release %mkrel 1
%define major 1
%define libname %mklibname cue %major
%define develname %mklibname -d cue 

Summary: Cuesheet parser library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://sourceforge.net/projects/libcue/files/libcue/%version/%{name}-%{version}.tar.bz2
License: GPLv2
Group: System/Libraries
Url: http://libcue.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is a library for parsing cue sheets which describe audio CD images. They
are useful for gapless music playback.

%package -n %libname
Group: System/Libraries
Summary:Cuesheet parser library

%description -n %libname
This is a library for parsing cue sheets which describe audio CD images. They
are useful for gapless music playback.

%package -n %develname
Group: Development/C
Summary:Cuesheet parser library
Requires: %libname = %version-%release
Provides: libcue-devel = %version-%release

%description -n %develname
This is a library for parsing cue sheets which describe audio CD images. They
are useful for gapless music playback.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %libname
%defattr(-,root,root)
%_libdir/libcue.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%doc AUTHORS NEWS ChangeLog
%_libdir/libcue.so
%_libdir/libcue.la
%_libdir/libcue.a
%_libdir/pkgconfig/libcue.pc
%_includedir/libcue-1.3

