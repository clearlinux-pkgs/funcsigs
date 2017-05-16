#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : funcsigs
Version  : 1.0.2
Release  : 16
URL      : http://pypi.debian.net/funcsigs/funcsigs-1.0.2.tar.gz
Source0  : http://pypi.debian.net/funcsigs/funcsigs-1.0.2.tar.gz
Summary  : Python function signatures from PEP362 for Python 2.6, 2.7 and 3.2+
Group    : Development/Tools
License  : Apache-2.0
Requires: funcsigs-python
BuildRequires : linecache2
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : traceback2
BuildRequires : unittest2

%description
.. funcsigs documentation master file, created by
sphinx-quickstart on Fri Apr 20 20:27:52 2012.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive.

%package python
Summary: python components for the funcsigs package.
Group: Default

%description python
python components for the funcsigs package.


%prep
%setup -q -n funcsigs-1.0.2

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484547018
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
export SOURCE_DATE_EPOCH=1484547018
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
