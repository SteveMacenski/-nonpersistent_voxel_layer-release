%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-nonpersistent-voxel-layer
Version:        1.3.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS nonpersistent_voxel_layer package

License:        BSD
URL:            http://wiki.ros.org/non-persisent-voxel-layer
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-costmap-2d
Requires:       ros-noetic-dynamic-reconfigure
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-laser-geometry
Requires:       ros-noetic-map-msgs
Requires:       ros-noetic-message-filters
Requires:       ros-noetic-message-runtime
Requires:       ros-noetic-nav-msgs
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-rosconsole
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-tf
Requires:       ros-noetic-visualization-msgs
Requires:       ros-noetic-voxel-grid
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-cmake-modules
BuildRequires:  ros-noetic-costmap-2d
BuildRequires:  ros-noetic-dynamic-reconfigure
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-laser-geometry
BuildRequires:  ros-noetic-map-msgs
BuildRequires:  ros-noetic-message-filters
BuildRequires:  ros-noetic-message-generation
BuildRequires:  ros-noetic-nav-msgs
BuildRequires:  ros-noetic-pluginlib
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-tf
BuildRequires:  ros-noetic-visualization-msgs
BuildRequires:  ros-noetic-voxel-grid
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
include This package provides an implementation of a 3D costmap that takes in
sensor data from the world, builds a 3D occupancy grid of the data for only one
iteration.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Thu Jan 28 2021 Steven Macenski <stevenmacenski@gmail.com> - 1.3.0-1
- Autogenerated by Bloom

* Wed Jul 08 2020 Steven Macenski <stevenmacenski@gmail.com> - 1.2.3-2
- Autogenerated by Bloom

* Mon Jun 01 2020 Steven Macenski <stevenmacenski@gmail.com> - 1.2.3-1
- Autogenerated by Bloom

