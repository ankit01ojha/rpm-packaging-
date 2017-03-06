Name:    howdy
Version: 1
Release: 1%{?dist}
Summary: Say hello, Texas style

License: Public Domain
Source0: howdy
BuildArch: noarch

%description
A simple program to greet the user, Texas style.

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE0} %{buildroot}/%{_bindir}

%files
%{_bindir}/howdy
%changelog* Sat Feb 4 2107 Ankit Raj Ojha <ankit123rudra@gmail.com> - 1.0-1
          - Initial packaging.
