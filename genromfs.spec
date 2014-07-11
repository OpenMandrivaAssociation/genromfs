Summary:	Tool for creating romfs filesystems
Name:		genromfs
Version:	0.5.2
Release:	15
License:	GPLv2
Group:		System/Kernel and hardware
Url:		http://romfs.sourceforge.net
Source0:	http://unc.dl.sourceforge.net/sourceforge/romfs/%{name}-%{version}.tar.gz

%description
Genromfs is a tool for creating romfs filesystems, which are
lightweight, read-only filesystems supported by the Linux
kernel.

%prep
%setup -q

%build
make CFLAGS="%{optflags} -DVERSION=\\\"%{version}\\\"" LDFLAGS="%{ldflags}"

%install
install -m0755 %{name} -D %{buildroot}%{_bindir}/%{name}
install -m0644 %{name}.8 -D %{buildroot}%{_mandir}/man8/%{name}.8

%files
%doc romfs.txt COPYING NEWS
%{_bindir}/*
%{_mandir}/man8/*

