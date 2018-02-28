#
# spec file for package 
#
# Copyright (c) 2017 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           hello_world
Version:        0.0.1
Release:        1.1
License:        MIT
Summary:        test package
Url:            https://github.com/bgeuken/hello_world
Group:          Development/Tools/Building
Source:         hello_world.tar.bz2
Requires:       ruby
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description

%prep

%build

%install

install -m 755 ${SOURCE1} %{_bindir}/%{name}

%post

%postun

%files
%defattr(-,root,root)
%{_bindir}/%{name}


