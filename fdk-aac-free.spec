%global commit 282947f73b01df9b6f7f75f7c7e9019186e4e1f1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           fdk-aac-free
Version:        0.1.6
Release:        3%{?dist}
Summary:        Third-Party Modified Version of the Fraunhofer FDK AAC Codec Library for Android

License:        FDK-AAC
URL:            https://cgit.freedesktop.org/~wtay/fdk-aac/log/?h=fedora
Source0:        https://github.com/UnitedRPMs/fdk-aac-free/releases/download/0.1.6/fdk-aac-free-%{shortcommit}.tar.gz

# Note you can download the current commit; why not maintain in gitlab or github?
# ./fdk-aac-free-snapshot -c $commit
Source1:	fdk-aac-free-snapshot

BuildRequires:  gcc gcc-c++
BuildRequires:  automake libtool

%description
The Third-Party Modified Version of the Fraunhofer FDK AAC Codec Library
for Android is software that implements part of the MPEG Advanced Audio Coding
("AAC") encoding and decoding scheme for digital audio.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.



%prep
%autosetup -n %{name}-%{shortcommit}
autoreconf -vif

%build
%configure \
  --disable-silent-rules \
  --disable-static

%make_build


%install
%make_install INSTALL="install -p"
find %{buildroot} -name '*.la' -print -delete

%ldconfig_scriptlets

%files
%doc ChangeLog README.fedora
%license NOTICE
%{_libdir}/*.so.*

%files devel
%doc documentation/*.pdf
%dir %{_includedir}/fdk-aac
%{_includedir}/fdk-aac/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/fdk-aac.pc


%changelog

* Wed Jun 12 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 0.1.6-3
- Updated to current commit

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 25 2018 Wim Taymans <wtaymans@redhat.com> - 0.1.6-1
- Update to 0.1.6
- Fix url

* Tue Sep 25 2018 Wim Taymans <wtaymans@redhat.com> - 0.1.5-5
- Use %ldconfig_scriptlets
- Remove Group

* Thu Nov 02 2017 Wim Taymans <wtaymans@redhat.com> - 0.1.5-4
- Fix BuildRequires, fix libtool cleanup

* Tue Oct 10 2017 Wim Taymans <wtaymans@redhat.com> - 0.1.5-3
- Build against stripped fdk-aac library

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.1.5-1
- Update to 1.5

* Wed Sep 07 2016 Nicolas Chauvet <kwizart@gmail.com> - 0.1.5-0.1.gita0bd8aa
- Update to github snapshot
- Spec file clean-up

* Fri Nov 06 2015 Nicolas Chauvet <kwizart@gmail.com> - 0.1.4-1
- Update to 1.4

* Sun Jan 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.1.3-1
- Update to 1.3.0

* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.1.2-1
- Update to 0.1.2

* Thu Mar 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.1.1-1
- Initial spec

