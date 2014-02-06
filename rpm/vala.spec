Name:       vala

Summary:    A modern programming language for GNOME
Version:    0.23.1
Release:    1
Group:      Development/Languages
License:    LGPLv2+ and BSD
URL:        http://live.gnome.org/Vala
Source0:    http://download.gnome.org/sources/vala/0.16/vala-%{version}.tar.xz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  flex
BuildRequires:  bison

%description
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

valac, the Vala compiler, is a self-hosting compiler that translates
Vala source code into C source and header files. It uses the GObject
type system to create classes and interfaces declared in the Vala source
code. It's also planned to generate GIDL files when gobject-
introspection is ready.

The syntax of Vala is similar to C#, modified to better fit the GObject
type system.


%package doc
Summary:    Documentation for %{name}
License:    LGPLv2+
Group:      Documentation
Requires:   %{name} = %{version}-%{release}
Requires:   devhelp

%description doc
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

This package contains documentation in a devhelp HTML book.


%package tools
Summary:    Tools for creating projects and bindings for %{name}
License:    LGPLv2+
Group:      Development/Languages
Requires:   %{name} = %{version}-%{release}
Requires:   gnome-common
Requires:   intltool
Requires:   libtool

%description tools
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

This package contains tools to generate Vala projects, as well as API bindings
from existing C libraries, allowing access from Vala programs.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

This package contains development files for %{name}. This is not necessary for
using the %{name} compiler.


%prep
%setup -q -n %{name}-%{version}/%{name}

%build

cd ../vala-bootstrap
export PREFIX=$PWD/../bootstrap
./autogen.sh --prefix=$PREFIX --enable-build-from-vala=no --disable-vapigen
./configure --prefix=$PREFIX --enable-build-from-vala=no --disable-vapigen

make V=1 %{?jobs:-j%jobs}
make install

cd ../vala
export VALAC=$PREFIX/bin/valac
%autogen --disable-static --enable-vapigen
echo %{version} > .version
echo %{version} > .tarball-version
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
# >> files
%doc COPYING
%{_bindir}/valac
%{_bindir}/valac-*
%{_bindir}/vala
%{_bindir}/vala-*
%{_datadir}/vala*
%{_libdir}/libvala*.so.*
%{_mandir}/*/valac*
# << files

%files doc
%defattr(-,root,root,-)
# >> files doc
%doc AUTHORS ChangeLog COPYING MAINTAINERS NEWS README THANKS
# << files doc

%files tools
%defattr(-,root,root,-)
# >> files tools
%{_bindir}/*gen*
%{_bindir}/vapicheck*
%{_libdir}/vala*
%{_mandir}/*/*gen*
# << files tools

%files devel
%defattr(-,root,root,-)
# >> files devel
%{_includedir}/vala*
%{_libdir}/libvala*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/pkgconfig/*.pc
%{_datadir}/aclocal/*
# << files devel
