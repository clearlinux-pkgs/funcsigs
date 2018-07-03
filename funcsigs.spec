#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x597240FE94E60165 (rbtcollins@hp.com)
#
Name     : funcsigs
Version  : 1.0.2
Release  : 35
URL      : http://pypi.debian.net/funcsigs/funcsigs-1.0.2.tar.gz
Source0  : http://pypi.debian.net/funcsigs/funcsigs-1.0.2.tar.gz
Source99 : http://pypi.debian.net/funcsigs/funcsigs-1.0.2.tar.gz.asc
Summary  : Python function signatures from PEP362 for Python 2.6, 2.7 and 3.2+
Group    : Development/Tools
License  : Apache-2.0
Requires: funcsigs-python3
Requires: funcsigs-license
Requires: funcsigs-python
Requires: ordereddict
BuildRequires : linecache2
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-core
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
BuildRequires : six
BuildRequires : traceback2
BuildRequires : unittest2

%description
.. funcsigs documentation master file, created by
sphinx-quickstart on Fri Apr 20 20:27:52 2012.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive.

%package legacypython
Summary: legacypython components for the funcsigs package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the funcsigs package.


%package license
Summary: license components for the funcsigs package.
Group: Default

%description license
license components for the funcsigs package.


%package python
Summary: python components for the funcsigs package.
Group: Default
Requires: funcsigs-python3

%description python
python components for the funcsigs package.


%package python3
Summary: python3 components for the funcsigs package.
Group: Default
Requires: python3-core

%description python3
python3 components for the funcsigs package.


%prep
%setup -q -n funcsigs-1.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530372003
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1530372003
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/funcsigs
cp LICENSE %{buildroot}/usr/share/doc/funcsigs/LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/funcsigs/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
