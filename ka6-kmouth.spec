#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.04.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kmouth
Summary:	kmouth
Name:		ka6-%{kaname}
Version:	25.04.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	4087dcf92e0cbca504c1807889fb9e7a
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6PrintSupport-devel
BuildRequires:	Qt6TextToSpeech-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	Qt6Xml-devel
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kcompletion-devel >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kcrash-devel >= %{kframever}
BuildRequires:	kf6-kdoctools-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMouth is a program which enables persons that cannot speak to let
their computer speak, e.g. mutal people or people who have lost their
voice. It has a text input field and speaks the sentences that you
enter. It also has support for user defined phrasebooks.

%description -l pl.UTF-8
KMouth jest programem, który pozwala osobom, które nie mogą mówić, by
komputer mówił za nich, np, niemowom, lub osobom, które straciły głos.
Program ma pole tekstowe i wymawia zdania wprowadzane z klawiatury.
Wspiera też listę wyrażeń definiowanych przez użytkownika.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kmouthrc
%attr(755,root,root) %{_bindir}/kmouth
%{_desktopdir}/org.kde.kmouth.desktop
%{_iconsdir}/hicolor/*x*/actions/*.png
%{_iconsdir}/hicolor/*x*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/kmouth.svg
%{_datadir}/kmouth
%{_datadir}/metainfo/org.kde.kmouth.appdata.xml
%lang(ca) %{_mandir}/ca/man1/kmouth.1*
%lang(da) %{_mandir}/da/man1/kmouth.1*
%lang(de) %{_mandir}/de/man1/kmouth.1*
%lang(es) %{_mandir}/es/man1/kmouth.1*
%lang(et) %{_mandir}/et/man1/kmouth.1*
%lang(fr) %{_mandir}/fr/man1/kmouth.1*
%lang(it) %{_mandir}/it/man1/kmouth.1*
%lang(C) %{_mandir}/man1/kmouth.1*
%lang(nl) %{_mandir}/nl/man1/kmouth.1*
%lang(pt) %{_mandir}/pt/man1/kmouth.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/kmouth.1*
%lang(ru) %{_mandir}/ru/man1/kmouth.1.*
%lang(sl) %{_mandir}/sl/man1/kmouth.1*
%lang(sv) %{_mandir}/sv/man1/kmouth.1*
%lang(uk) %{_mandir}/uk/man1/kmouth.1*
