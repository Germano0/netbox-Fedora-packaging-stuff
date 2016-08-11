%global name django-netbox
# Python 3 only for Fedora for now.
%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with python3
%else
%bcond_without python3
%endif

Name:           python-%{name}
Version:        1.5.0
Release:        1%{?dist}
Summary:        IP address management (IPAM) and data center infrastructure management (DCIM) tool

License:        BSD
URL:            https://github.com/digitalocean/netbox
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{name}; echo ${n:0:1})/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-django
BuildRequires:  python2-setuptools
# not complete
%if %{with python3}
BuildRequires:  python3-devel
BuildRequires:  python3-django
BuildRequires:  python3-setuptools
# not complete
%endif # if with_python3

%description
NetBox is an IP address management (IPAM) and data center infrastructure management (DCIM) tool.
Initially conceived by the network engineering team at DigitalOcean, NetBox was developed specifically
to address the needs of network and infrastructure engineers.

%package -n python2-%{name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{name}}
Requires:  python2-django
# not complete
%description -n python2-%{name}
NetBox is an IP address management (IPAM) and data center infrastructure management (DCIM) tool.
Initially conceived by the network engineering team at DigitalOcean, NetBox was developed specifically
to address the needs of network and infrastructure engineers.

%if %{with python3}
%package -n python3-%{name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{name}}
Requires:  python3-django
# not complete
%description -n python3-%{name}
NetBox is an IP address management (IPAM) and data center infrastructure management (DCIM) tool.
Initially conceived by the network engineering team at DigitalOcean, NetBox was developed specifically
to address the needs of network and infrastructure engineers.
%endif # if with_python3

%prep
%setup -q -n %{name}-%{version}

%build
%py2_build
%if %{with python3}
%py3_build
%endif # if with_python3

%install
%py2_install
%if %{with python3}
%py3_install
%endif # if with_python3

%check
%{__python2} setup.py test
%if %{with python3}
%{__python3} setup.py test
%endif # if with_python3

%files -n python2-%{name}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/*

%if %{with python3}
%files -n python3-%{name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/*
%endif # if with_python3

%changelog
* Wed Aug 10 2016 Germano Massullo <germano.massullo@gmail.com> - 1.5.0-1
- First commit on Fedora's Git
