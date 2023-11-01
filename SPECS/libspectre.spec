Name:           libspectre
Version:        0.2.8
Release:        5%{?dist}
Summary:        A library for rendering PostScript(TM) documents

License:        GPLv2+
URL:            http://libspectre.freedesktop.org
Source0:        http://libspectre.freedesktop.org/releases/%{name}-%{version}.tar.gz

%if 0%{?fedora} > 27
BuildRequires: libgs-devel
%else
BuildRequires: ghostscript-devel >= 8.61
%endif

%description
%{name} is a small library for rendering PostScript(TM) documents.
It provides a convenient easy to use API for handling and rendering
PostScript documents.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup


%build
%configure \
  --disable-silent-rules \
  --disable-static

make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

rm -fv %{buildroot}%{_libdir}/libspectre.la


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS README TODO
%{_libdir}/libspectre.so.1*

%files devel
%{_includedir}/libspectre/
%{_libdir}/libspectre.so
%{_libdir}/pkgconfig/libspectre.pc


%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.2.8-5
- BR: libgs-devel (f28+)
- .spec cleanup/cosmetics (drop deprecated tags, use %%autosetup/%%license, tighten subpkg dep)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 12 2016 Martin Hatina <mhatina@redhat.com> - 0.2.8-1
- Update to 0.2.8

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 31 2015 Marek Kasik <mkasik@redhat.com> - 0.2.7-7
- Rotate result of rendering in libspectre
- Resolves: #1172317

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 19 2012 Marek Kasik <mkasik@redhat.com> - 0.2.7-1
- Update to 0.2.7

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 0.2.6-3
- Rebuilt for gcc bug 634757

* Sat Sep 25 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.2.6-2
- rebuild (ghostscript)
- %%files: track sonames (and friends) closer

* Sat Jun 12 2010 Matthias Clasen <mclasen@redhat.com> - 0.2.6-1
- Update to 0.2.6

* Wed Mar  3 2010 Matthias Clasen <mclasen@redhat.com> - 0.2.4-1
- Update to 0.2.4
- See http://mail.gnome.org/archives/gnome-announce-list/2010-February/msg00059.html

* Fri Jan  8 2010  Marek Kasik <mkasik@redhat.com> - 0.2.3-4
- Correct release number

* Fri Jan  8 2010  Marek Kasik <mkasik@redhat.com> - 0.2.3-1
- Update to 0.2.3

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec  3 2008  Matthias Clasen <mclasen@redhat.com> - 0.2.2-1
- Update to 0.2.2

* Sun Aug 10 2008  Matthias Clasen <mclasen@redhat.com> - 0.2.1-1
- Update to 0.2.1

* Sat Feb  9 2008  Matthias Clasen <mclasen@redhat.com> - 0.2.0-2
- Rebuild for gcc 4.3

* Tue Jan 29 2008  Matthias Clasen <mclasen@redhat.com> - 0.2.0-1
- Initial packaging 
