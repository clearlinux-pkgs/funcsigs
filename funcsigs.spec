#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x597240FE94E60165 (rbtcollins@hp.com)
#
Name     : funcsigs
Version  : 1.0.2
Release  : 60
URL      : http://pypi.debian.net/funcsigs/funcsigs-1.0.2.tar.gz
Source0  : http://pypi.debian.net/funcsigs/funcsigs-1.0.2.tar.gz
Source1  : http://pypi.debian.net/funcsigs/funcsigs-1.0.2.tar.gz.asc
Summary  : Python function signatures from PEP362 for Python 2.6, 2.7 and 3.2+
Group    : Development/Tools
License  : Apache-2.0
Requires: funcsigs-license = %{version}-%{release}
Requires: funcsigs-python = %{version}-%{release}
Requires: funcsigs-python3 = %{version}-%{release}
Requires: ordereddict
BuildRequires : buildreq-distutils3
BuildRequires : linecache2
BuildRequires : ordereddict
BuildRequires : setuptools
BuildRequires : six
BuildRequires : traceback2
BuildRequires : unittest2

%description
.. funcsigs documentation master file, created by
sphinx-quickstart on Fri Apr 20 20:27:52 2012.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive.

%package license
Summary: license components for the funcsigs package.
Group: Default

%description license
license components for the funcsigs package.


%package python
Summary: python components for the funcsigs package.
Group: Default
Requires: funcsigs-python3 = %{version}-%{release}

%description python
python components for the funcsigs package.


%package python3
Summary: python3 components for the funcsigs package.
Group: Default
Requires: python3-core
Provides: pypi(funcsigs)

%description python3
python3 components for the funcsigs package.


%prep
%setup -q -n funcsigs-1.0.2
cd %{_builddir}/funcsigs-1.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603392261
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/funcsigs
cp %{_builddir}/funcsigs-1.0.2/LICENSE %{buildroot}/usr/share/package-licenses/funcsigs/ff5d728e7efdc9db8f36d54824ca9a57f497e1f6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/funcsigs/ff5d728e7efdc9db8f36d54824ca9a57f497e1f6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
