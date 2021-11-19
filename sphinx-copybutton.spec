#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sphinx-copybutton
Version  : 0.4.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/d0/79/d57ca42f4be2ac21f660300a5e1a285ce42b23c45b5a4b9a21ce973a3b2f/sphinx-copybutton-0.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d0/79/d57ca42f4be2ac21f660300a5e1a285ce42b23c45b5a4b9a21ce973a3b2f/sphinx-copybutton-0.4.0.tar.gz
Summary  : Add a copy button to each of your code cells.
Group    : Development/Tools
License  : MIT
Requires: sphinx-copybutton-license = %{version}-%{release}
Requires: sphinx-copybutton-python = %{version}-%{release}
Requires: sphinx-copybutton-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(ipython)
BuildRequires : pypi(pre_commit)
BuildRequires : pypi(sphinx)
BuildRequires : pypi(sphinx_book_theme)

%description
# sphinx-copybutton
[![PyPI](https://img.shields.io/pypi/v/sphinx-copybutton.svg)](https://pypi.org/project/sphinx_copybutton/) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/sphinx-copybutton.svg)](https://anaconda.org/conda-forge/sphinx-copybutton) | [![Documentation](https://readthedocs.org/projects/sphinx-copybutton/badge/?version=latest)](https://sphinx-copybutton.readthedocs.io/en/latest/?badge=latest)

%package license
Summary: license components for the sphinx-copybutton package.
Group: Default

%description license
license components for the sphinx-copybutton package.


%package python
Summary: python components for the sphinx-copybutton package.
Group: Default
Requires: sphinx-copybutton-python3 = %{version}-%{release}

%description python
python components for the sphinx-copybutton package.


%package python3
Summary: python3 components for the sphinx-copybutton package.
Group: Default
Requires: python3-core
Provides: pypi(sphinx_copybutton)
Requires: pypi(ipython)
Requires: pypi(pre_commit)
Requires: pypi(sphinx)
Requires: pypi(sphinx_book_theme)

%description python3
python3 components for the sphinx-copybutton package.


%prep
%setup -q -n sphinx-copybutton-0.4.0
cd %{_builddir}/sphinx-copybutton-0.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637341996
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sphinx-copybutton
cp %{_builddir}/sphinx-copybutton-0.4.0/LICENSE %{buildroot}/usr/share/package-licenses/sphinx-copybutton/04f302f55e177936c00dce6b36ca9cf0c4e007ff
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinx-copybutton/04f302f55e177936c00dce6b36ca9cf0c4e007ff

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
