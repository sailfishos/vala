Name:       vala

Summary:    A modern programming language for GNOME
Version:    0.46.5
Release:    1
License:    LGPLv2+ and BSD
URL:        https://wiki.gnome.org/Projects/Vala
Source0:    %{name}-%{version}.tar.xz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  autoconf-archive
BuildRequires:  vala
BuildRequires:  vala-tools

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
Requires:   %{name} = %{version}-%{release}

%description devel
Vala is a new programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

This package contains development files for %{name}. This is not necessary for
using the %{name} compiler.


%prep
%autosetup -n %{name}-%{version}/%{name}

%build
echo %{version} | cut -d '+' -f 1 > .tarball-version
cp .tarball-version .version
%autogen --disable-static --disable-valadoc
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
# Drop the devhelp, as it's conditionally built depending on the presence of xsltproc
rm -rf %{buildroot}/%{_datadir}/devhelp/books/vala-*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/valac
%{_bindir}/valac-*
%{_bindir}/vala
%{_bindir}/vala-*
%{_datadir}/vala*
%{_libdir}/libvala*.so.*

%files doc
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS
%{_mandir}/*/valac*
%{_mandir}/*/*gen*

%files tools
%defattr(-,root,root,-)
%{_bindir}/*gen*
%{_libdir}/vala*

%files devel
%defattr(-,root,root,-)
%{_includedir}/vala*
%{_libdir}/libvala*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*
