Summary:	Tool for creating romfs filesystems
Name:		genromfs
Version:	0.5.2
Release:	9
License:	GPL
Group:		System/Kernel and hardware
Source0:	http://unc.dl.sourceforge.net/sourceforge/romfs/%{name}-%{version}.tar.gz
URL:		http://romfs.sourceforge.net

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

%changelog
* Thu Feb 14 2013 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.5.2-9
- pass ldflags
- cleanups

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.2-8mdv2011.0
+ Revision: 664821
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.2-7mdv2011.0
+ Revision: 605445
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.2-6mdv2010.1
+ Revision: 522713
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.5.2-5mdv2010.0
+ Revision: 424580
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.5.2-4mdv2009.1
+ Revision: 351197
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.5.2-3mdv2009.0
+ Revision: 221054
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.5.2-2mdv2008.1
+ Revision: 150103
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Jul 06 2007 Adam Williamson <awilliamson@mandriva.org> 0.5.2-1mdv2008.0
+ Revision: 49210
- no need to bzip manpage manually
- drop patch (merged upstream)
- new release 0.5.2

* Sat Apr 28 2007 Adam Williamson <awilliamson@mandriva.org> 0.5.1-4mdv2008.0
+ Revision: 18902
- rebuild for new era
- clean spec
- add patch with couple of fixes from CVS


* Sat Oct 08 2005 Michael Scherer <misc@mandriva.org> 0.5.1-3mdk
- Rebuild
- mkrel, rpmlint error ( summary-end-with-dot )

* Tue Jul 22 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.5.1-2mdk
- rebuild
- cosmetics

* Fri Aug 02 2002 Jeff Garzik <jgarzik@mandrakesoft.com> 0.5.1-1mdk
- Version 0.5.1

* Mon Jan 21 2002 François Pons <fpons@mandrakesoft.com> 0.5-1mdk
- added url tag.
- added documentation files.
- removed patch.
- 0.5.

* Sat Jul 07 2001 Etienne Faure <etienne@mandrakesoft.com> 0.3-11mdk
- rebuild on cluster

* Thu Jul 20 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.3-10mdk
- BM, macros

* Sat Jun 10 2000 Etienne Faure <etienne@mandrakesoft.com> 0.3-9mdk
-rebuild on kenobi

* Wed Apr 05 2000 John Buswell <johnb@mandrakesoft.com> 0.3-8mdk
- fixed vendor tag

* Thu Mar 30 2000 John Buswell <johnb@mandrakesoft.com> 0.3-7mdk
- fixed groups
- spec helper

* Wed Dec 01 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add a defattr.

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Thu Nov 05 1998 Jeff Johnson <jbj@redhat.com>
- import from ultrapenguin 1.1.

* Fri Oct 30 1998 Jakub Jelinek <jj@ultra.linux.cz>
- new package

