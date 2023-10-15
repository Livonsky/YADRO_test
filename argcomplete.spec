%{!?_version: %define _version 3.1.2}
%{!?_requires: %define _requires python3-devel python-setuptools}


Name: argcomplete
Version: %{_version}
Release: 1%{?dist}
Summary: Bash tab completion for argparse

License: GPLv2+
URL: https://pypi.org/project/argcomplete/
Source0: %{name}-%{version}.tar.gz

BuildRequires: python3-devel python3-setuptools tcsh
Requires: %{_requires}

%description
Argcomplete provides easy, extensible command line tab completion of arguments for your Python script.

%global debug_package %{nil}

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%license LICENSE.rst
%doc README.rst
%{python3_sitelib}/argcomplete*/
/usr/bin/activate-global-python-argcomplete
/usr/bin/python-argcomplete-check-easy-install-script
/usr/bin/register-python-argcomplete
/usr/lib/python3.6/site-packages/UNKNOWN-0.0.0-py3.6.egg-info/PKG-INFO
/usr/lib/python3.6/site-packages/UNKNOWN-0.0.0-py3.6.egg-info/SOURCES.txt
/usr/lib/python3.6/site-packages/UNKNOWN-0.0.0-py3.6.egg-info/dependency_links.txt
/usr/lib/python3.6/site-packages/UNKNOWN-0.0.0-py3.6.egg-info/not-zip-safe
/usr/lib/python3.6/site-packages/UNKNOWN-0.0.0-py3.6.egg-info/top_level.txt


