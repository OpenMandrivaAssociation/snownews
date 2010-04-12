# TODO man pages translation
# locales
%define name	snownews
%define version 1.5.12

Name:		%{name}
Version:	%{version}
Release:	%mkrel 2
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

