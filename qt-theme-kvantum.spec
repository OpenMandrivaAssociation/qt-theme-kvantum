Name: qt-theme-kvantum
Summary: Kvantum - an SVG renderer for drawing Qt widgets - theme engine
Version: 1.1.5
Release: 1
URL: https://github.com/tsujan/Kvantum
Source0: https://github.com/tsujan/Kvantum/archive/V%{version}/Kvantum-%{version}.tar.gz
Group: Graphical Desktop/KDE
License: GPLv3
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)

%description
Kvantum is an SVG-based theme engine for Qt, tuned to KDE and LXQt, with
an emphasis on elegance, usability and practicality.

Kvantum has a default dark theme, which is inspired by the default theme
of Enlightenment. Creation of realistic themes like that for KDE was my
first reason to make Kvantum but it goes far beyond its default theme:
you could make themes with very different looks and feels for it, whether
they be photorealistic or cartoonish, 3D or flat, embellished or
minimalistic, or something in between, and Kvantum will let you control
almost every aspect of Qt widgets.

Kvantum also comes with extra themes that are installed as root with Qt6
installation and can be selected and activated by using Kvantum Manager.

%prep
%autosetup -p1 -n Kvantum-%{version}/Kvantum

%build
%cmake
%make_build

%install
%make_install -C build

# We don't need obsolete stuff
rm -rf %{buildroot}%{_datadir}/kde4

%find_lang kvantum --all-name --with-qt

%files -f kvantum.lang
%license COPYING
%{_bindir}/kvantummanager
%{_bindir}/kvantumpreview
%{_libdir}/qt6/plugins/styles/libkvantum.so
%dir %{_datadir}/Kvantum
%{_datadir}/Kvantum/KvAdapta
%{_datadir}/color-schemes/KvAdapta.colors
%{_datadir}/Kvantum/KvAdaptaDark
%{_datadir}/color-schemes/KvAdaptaDark.colors
%{_datadir}/Kvantum/KvAmbiance
%{_datadir}/color-schemes/KvAmbiance.colors
%{_datadir}/Kvantum/KvAmbience
%{_datadir}/color-schemes/KvAmbience.colors
%{_datadir}/Kvantum/KvArc
%{_datadir}/color-schemes/KvArc.colors
%{_datadir}/Kvantum/KvArcDark
%{_datadir}/color-schemes/KvArcDark.colors
%{_datadir}/Kvantum/KvBeige
%{_datadir}/color-schemes/KvBeige.colors
%{_datadir}/Kvantum/KvBlender
%{_datadir}/color-schemes/KvBlender.colors
%{_datadir}/Kvantum/KvBrown
%{_datadir}/color-schemes/KvBrown.colors
%{_datadir}/Kvantum/KvCurves
%{_datadir}/color-schemes/KvCurves.colors
%{_datadir}/Kvantum/KvCurves3d
%{_datadir}/Kvantum/KvCurves3d1
%{_datadir}/color-schemes/KvCurves3d1.colors
%{_datadir}/Kvantum/KvCurvesLight
%{_datadir}/color-schemes/KvCurvesLight.colors
%{_datadir}/Kvantum/KvCurvesLight1
%{_datadir}/Kvantum/KvCyan
%{_datadir}/color-schemes/KvCyan.colors
%{_datadir}/Kvantum/KvDark
%{_datadir}/color-schemes/KvDark.colors
%{_datadir}/Kvantum/KvDarkRed
%{_datadir}/color-schemes/KvDarkRed.colors
%{_datadir}/Kvantum/KvFlat
%{_datadir}/color-schemes/KvFlat.colors
%{_datadir}/Kvantum/KvFlatLight
%{_datadir}/color-schemes/KvFlatLight.colors
%{_datadir}/Kvantum/KvFlatRed
%{_datadir}/color-schemes/KvFlatRed.colors
%{_datadir}/Kvantum/KvGnome
%{_datadir}/color-schemes/KvGnome.colors
%{_datadir}/Kvantum/KvGnomeAlt
%{_datadir}/color-schemes/KvGnomeAlt.colors
%{_datadir}/Kvantum/KvGnomeDark
%{_datadir}/color-schemes/KvGnomeDark.colors
%{_datadir}/Kvantum/KvGnomish
%{_datadir}/color-schemes/KvGnomish.colors
%{_datadir}/Kvantum/KvGray
%{_datadir}/color-schemes/KvGray.colors
%{_datadir}/Kvantum/KvMojave
%{_datadir}/color-schemes/KvMojave.colors
%{_datadir}/Kvantum/KvMojaveLight
%{_datadir}/color-schemes/KvMojaveLight.colors
%{_datadir}/Kvantum/KvOxygen
%{_datadir}/color-schemes/KvOxygen.colors
%{_datadir}/Kvantum/KvRoughGlass
%{_datadir}/color-schemes/KvRoughGlass.colors
%{_datadir}/Kvantum/KvSimplicity
%{_datadir}/color-schemes/KvSimplicity.colors
%{_datadir}/Kvantum/KvSimplicityDark
%{_datadir}/color-schemes/KvSimplicityDark.colors
%{_datadir}/Kvantum/KvSimplicityDarkLight
%{_datadir}/color-schemes/KvSimplicityDarkLight.colors
%{_datadir}/Kvantum/KvSimplicityTurquoise
%{_datadir}/color-schemes/KvSimplicityTurquoise.colors
%{_datadir}/Kvantum/KvYaru
%{_datadir}/color-schemes/KvYaru.colors
%{_datadir}/Kvantum/KvantumAlt
%{_datadir}/color-schemes/Kvantum.colors
%{_datadir}/color-schemes/KvantumAlt.colors
%{_datadir}/Kvantum/KvMojaveMixed/KvMojaveMixed.kvconfig
%{_datadir}/Kvantum/KvMojaveMixed/KvMojaveMixed.svg
%{_datadir}/color-schemes/KvMojaveMixed.colors
%{_datadir}/applications/kvantummanager.desktop
%{_datadir}/icons/hicolor/scalable/apps/kvantum.svg
%{_datadir}/Kvantum/KvMojaveMixed1/KvMojaveMixed1.kvconfig
%{_datadir}/Kvantum/KvMojaveMixed1/KvMojaveMixed1.svg
%{_datadir}/color-schemes/KvMojaveMixed1.colors
