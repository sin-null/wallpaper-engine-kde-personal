Name: wallpaper-engine-kde-plugin

%global shortcommit %(c=%{commit}; echo ${c:0:7})

Version: %{shortcommit}
Release: 1%{?dist}
Summary: A kde wallpaper plugin integrating wallpaper engine

Group: Development/System 
License: GPLv2
URL: https://github.com/catsout/wallpaper-engine-kde-plugin

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: mpv-libs-devel vulkan-headers plasma-workspace-devel libplasma-devel lz4-devel qt6-qtbase-private-devel qt6-qtdeclarative-devel git
Requires: plasma-workspace gstreamer1-libav mpv-libs lz4 python3-websockets qt6-qtwebchannel-devel qt6-qtwebsockets-devel

%description

%prep
git clone --single-branch --branch qt6 https://github.com/catsout/wallpaper-engine-kde-plugin.git
cd wallpaper-engine-kde-plugin && git submodule update --init --recursive  && cd ..
mv -v  wallpaper-engine-kde-plugin/* ./ && rm -rf wallpaper-engine-kde-plugin

%global _enable_debug_package 0
%global debug_package %{nil}

%build
mkdir -p build && cd build
cmake .. -DQT_MAJOR_VERSION=6 -DUSE_PLASMAPKG=ON
%make_build

%install
rm -rf $RPM_BUILD_ROOT
cd build
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/*

%changelog 

