%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-rcl-lifecycle
Version:        6.0.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rcl_lifecycle package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-iron-lifecycle-msgs
Requires:       ros-iron-rcl
Requires:       ros-iron-rcutils
Requires:       ros-iron-rmw
Requires:       ros-iron-rosidl-runtime-c
Requires:       ros-iron-tracetools
Requires:       ros-iron-ros-workspace
BuildRequires:  ros-iron-ament-cmake-ros
BuildRequires:  ros-iron-lifecycle-msgs
BuildRequires:  ros-iron-rcl
BuildRequires:  ros-iron-rcutils
BuildRequires:  ros-iron-rmw
BuildRequires:  ros-iron-rosidl-runtime-c
BuildRequires:  ros-iron-tracetools
BuildRequires:  ros-iron-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-iron-ament-cmake-gtest
BuildRequires:  ros-iron-ament-lint-auto
BuildRequires:  ros-iron-ament-lint-common
BuildRequires:  ros-iron-osrf-testing-tools-cpp
%endif

%description
Package containing a C-based lifecycle implementation

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/iron" \
    -DAMENT_PREFIX_PATH="/opt/ros/iron" \
    -DCMAKE_PREFIX_PATH="/opt/ros/iron" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Fri May 19 2023 Audrow Nash <audrow@openrobotics.org> - 6.0.2-1
- Autogenerated by Bloom

* Thu Apr 20 2023 Audrow Nash <audrow@openrobotics.org> - 6.0.1-2
- Autogenerated by Bloom

* Tue Apr 18 2023 Audrow Nash <audrow@openrobotics.org> - 6.0.1-1
- Autogenerated by Bloom

* Wed Apr 12 2023 Audrow Nash <audrow@openrobotics.org> - 6.0.0-1
- Autogenerated by Bloom

* Tue Mar 21 2023 Audrow Nash <audrow@openrobotics.org> - 5.9.0-2
- Autogenerated by Bloom

