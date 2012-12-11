# TODO man pages translation
# locales
%define name	snownews
%define version 1.5.12

Name:		%{name}
Version:	%{version}
Release:	%mkrel 3
Summary: 	Text mode RSS/RDF newsreader
License:	GPLv2
Url:		http://kiza.kcore.de/software/snownews/
Group:     	Networking/News
Source0:    	http://kiza.kcore.de/software/snownews/download/%{name}-%{version}.tar.bz2
Source1:    	%{name}.bash-completion.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	ncurses-devel
BuildRequires:	libxml2-devel
BuildRequires:  libncursesw-devel
BuildRequires:  openssl-devel

%description
Snownews is a text mode RSS/RDF newsreader.
It allow you to read the headlines of your favorite news site if
they propose a RSS newsfeed.

%prep
%setup -q
bzcat %{SOURCE1} > %{name}.bash-completion

%build
./configure --prefix=%_prefix
%make

%install

rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std
#mv %buildroot%_prefix/man %buildroot%_datadir
#mv %buildroot%_mandir/ru* %buildroot%_mandir/ru
ln -sf opml2snow %buildroot%_bindir/snow2opml
# bash completion
install -d -m 755 %{buildroot}%{_sysconfdir}/bash_completion.d
install -m 644 %{name}.bash-completion %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-, root, root, 0755)
%doc AUTHOR COPYING CREDITS Changelog INSTALL* README*
%{_bindir}/*
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(ru) %{_mandir}/ru_RU.KOI8-R/man1/*
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}



%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5.12-3mdv2011.0
+ Revision: 614934
- the mass rebuild of 2010.1 packages

* Mon Apr 12 2010 Funda Wang <fwang@mandriva.org> 1.5.12-2mdv2010.1
+ Revision: 533647
- rebuild for openssl 1.0

* Tue Sep 29 2009 Michael Scherer <misc@mandriva.org> 1.5.12-1mdv2010.0
+ Revision: 450825
- fix BuildRequires
- use a contruct suitable for mdvsys update for Release tag
- fix the License tag
- update to new version 1.5.12

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Mar 21 2009 Michael Scherer <misc@mandriva.org> 1.5.11-1mdv2009.1
+ Revision: 359743
- update to new version 1.5.11

* Sun Aug 10 2008 Jérôme Soyer <saispo@mandriva.org> 1.5.10-1mdv2009.0
+ Revision: 270602
- New release 1.5.10

* Sat Mar 01 2008 Michael Scherer <misc@mandriva.org> 1.5.9-1mdv2008.1
+ Revision: 177201
- fix missing tar.gz
- use gz as upstream use it
- new version 1.5.9

  + Thierry Vignaud <tv@mandriva.org>
    - fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Mon Jan 14 2008 Jérôme Soyer <saispo@mandriva.org> 1.5.8-2mdv2008.1
+ Revision: 151158
- Add UTF8 per default

* Sat Jan 12 2008 Jérôme Soyer <saispo@mandriva.org> 1.5.8-1mdv2008.1
+ Revision: 149642
- New release

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu May 03 2007 Michael Scherer <misc@mandriva.org> 1.5.7-3mdv2008.0
+ Revision: 20961
- use %%mkrel, yearly rebuild


* Mon Sep 19 2005 Götz Waschk <waschk@mandriva.org> 1.5.7-2mdk
- add missing files

* Sun Jun 05 2005 Michael Scherer <misc@mandriva.org> 1.5.7-1mdk
- New release 1.5.7
- fix prefix

* Thu Dec 09 2004 Michael Scherer <misc@mandrake.org> 1.5.6.1-1mdk
- New release 1.5.6.1

* Wed Dec 08 2004 Michael Scherer <misc@mandrake.org> 1.5.6-1mdk
- New release 1.5.6

* Tue Nov 02 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.5.5.1-1mdk
- New release 1.5.5.1
- Add configure to %%build 
[           1      -eq 1 ] || exit 0 
[           1      -eq 1 ] || exit 0 
 phase (although that's not an autoconf configure)
- Update URLs

* Mon Oct 25 2004 Michael Scherer <misc@mandrake.org> 1.5.4-1mdk
- New release 1.5.4

* Mon Oct 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.5.3-2mdk 
- bash-completion in a distinct file
- spec cleanup

* Fri Jun 04 2004 Michael Scherer <misc@mandrake.org> 1.5.3-1mdk
- New release 1.5.3

* Wed Apr 14 2004 Michael Scherer <misc@mandrake.org> 1.5.2-1mdk
- New release 1.5.2
- rpmbuildupdate compliant

* Fri Apr 09 2004 Michael Scherer <misc@mandrake.org> 1.5.1-1mdk
- 1.5.1

* Fri Mar 05 2004 Michael Scherer <misc@mandrake.org> 1.5.0-1mdk
- 1.5

* Tue Jan 27 2004 Michael Scherer <misc@mandrake.org> 1.4.4-1mdk
- 1.4.4

* Thu Jan 01 2004 Michael Scherer <misc@mandrake.org> 1.4.2-2mdk 
- added bash_completion file

* Tue Dec 23 2003 Michael Scherer <misc@mandrake.org> 1.4.2-1mdk 
- 1.4.2

* Sun Dec 07 2003 Michael Scherer <misc@mandrake.org> 1.4.1-1mdk
- first mandrake spec

