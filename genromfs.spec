%define name genromfs
%define version 0.5.2
%define release %mkrel 2

Summary:	Tool for creating romfs filesystems
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Kernel and hardware
Source:		http://unc.dl.sourceforge.net/sourceforge/romfs/%{name}-%{version}.tar.gz
URL:		http://romfs.sourceforge.net
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Genromfs is a tool for creating romfs filesystems, which are
lightweight, read-only filesystems supported by the Linux
kernel.

%prep
%setup -q

%build
make CFLAGS="$RPM_OPT_FLAGS -DVERSION=\\\"%{version}\\\""

%install
rm -rf $RPM_BUILD_ROOT
install -m 0755 %{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m 0644 %{name}.8 -D $RPM_BUILD_ROOT%{_mandir}/man8/%{name}.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc romfs.txt COPYING ChangeLog NEWS
%{_bindir}/*
%{_mandir}/man8/*

