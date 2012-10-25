%define name gummi
%define version 0.6.5
%define release 1

Summary: LaTeX editor for Linux
Name:	 %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: MIT
Group:	 Publishing
Url:	 http://dev.midnightcoding.org/projects/gummi/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtk2-devel
BuildRequires: gtkspell-devel
BuildRequires: libpoppler-devel

%description
Gummi is a LaTeX editor for the Linux platform written in C/GTK+. It
was designed with simplicity in mind, but aims to appeal to both
novices and advanced LaTeX writers.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%_bindir/gummi
%_libdir/gummi/latex_dvi.sh
%_datadir/gummi/*
%_datadir/applications/gummi.desktop
%_datadir/locale/*
%_datadir/pixmaps/gummi.png
%_mandir/man1/gummi.*

