Name: hello_world
Version: 1.0
Release: 1%{?dist}
Summary: Simple Hello World script

License: MIT
URL: https://github.com/AndriiVyshnevskyi/WorksDevOps01-.git
Source0: hello_world.py
Source1: hello_world.spec

%description
This is a simple Hello World script in Python.

%prep
# Ніяких підготовчих дій для цього додатка

%build
# Ніяких підготовчих дій для цього додатка

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}%{_specdir}
install -p -m 755 %{SOURCE0} %{buildroot}/usr/bin/hello_world
install -p -m 644 %{SOURCE1} %{buildroot}%{_specdir}/hello_world.spec

%files
/usr/bin/hello_world.spec
%{_bindir}/hello_world
%{_specdir}/hello_world.spec

%changelog
* Wen 16 Aug 2023 Your Name <vishnia>
- Initial build of hello_world RPM package




