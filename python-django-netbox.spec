%global oname netbox

%global python2_pkgversion 2
%{?!python3_pkgversion:%global python3_pkgversion 3}

%if %{with python3}
%global use_pyver %python3_pkgversion
%else
%global use_pyver %python2_pkgversion
%endif

Name:           python-django-%{oname}
Version:        1.5.2
Release:        1%{?dist}
Summary:        IP address management and data center infrastructure management tool

License:        ASL 2.0
URL:            https://github.com/digitalocean/%{oname}
Source0:        %{url}/archive/v%{version}/%{oname}-%{version}.tar.gz

# Technically, this isn't necessary since netbox doesn't use setuptools
# However, it's quite useful for knowing how it was softened
Patch0:         netbox-1.5.2-Soften-dependencies-in-requirements.txt.patch

# Requirements from softened requirements.txt
BuildRequires:  python%{use_pyver}-devel
BuildRequires:  python%{use_pyver}-cryptography >= 1.4
BuildRequires:  python%{use_pyver}-django >= 1.10
# Missing py3 build
BuildRequires:  python%{use_pyver}-django-debug-toolbar >= 1.4
BuildRequires:  python%{use_pyver}-django-filter >= 0.13.0
BuildRequires:  python%{use_pyver}-django-rest-swagger >= 0.3.10
BuildRequires:  python%{use_pyver}-django-tables2 >= 1.2.1
BuildRequires:  python%{use_pyver}-django-rest-framework >= 3.4.3
BuildRequires:  python%{use_pyver}-graphviz >= 0.4.10
BuildRequires:  python%{use_pyver}-markdown >= 2.6.6
BuildRequires:  python%{use_pyver}-natsort >= 5.0.0
BuildRequires:  python%{use_pyver}-ncclient >= 0.5.2
BuildRequires:  python%{use_pyver}-netaddr >= 0.7.18
BuildRequires:  python%{use_pyver}-paramiko >= 2.0.0
BuildRequires:  python%{use_pyver}-psycopg2 >= 2.6.1
# This is py-gfm
BuildRequires:  python%{use_pyver}-gfm >= 0.1.3
# This is pycrypto
BuildRequires:  python%{use_pyver}-crypto >= 2.6.1

BuildRequires:  python%{use_pyver}-sqlparse >= 0.1.19
BuildRequires:  python%{use_pyver}-xmltodict >= 0.10.2

%description
NetBox is an open source web application designed
to help manage and document computer networks.
Initially conceived by the network engineering team at DigitalOcean,
NetBox was developed specifically to address the needs of network
and infrastructure engineers.

%package -n python%{use_pyver}-django-netbox
Summary:   IP address management and data center infrastructure management tool
%{?python_provide:%python_provide python%{use_pyver}-django-netbox}
Requires:  python%{use_pyver}
Requires:  python%{use_pyver}-cryptography >= 1.4
Requires:  python%{use_pyver}-django >= 1.10
Requires:  python%{use_pyver}-django-debug-toolbar >= 1.4
Requires:  python%{use_pyver}-django-filter >= 0.13.0
Requires:  python%{use_pyver}-django-rest-swagger >= 0.3.10
Requires:  python%{use_pyver}-django-tables2 >= 1.2.1
Requires:  python%{use_pyver}-djangorestframework >= 3.4.3
Requires:  python%{use_pyver}-graphviz >= 0.4.10
Requires:  python%{use_pyver}-markdown >= 2.6.6
Requires:  python%{use_pyver}-natsort >= 5.0.0
Requires:  python%{use_pyver}-ncclient >= 0.5.2
Requires:  python%{use_pyver}-netaddr >= 0.7.18
Requires:  python%{use_pyver}-paramiko >= 2.0.0
Requires:  python%{use_pyver}-psycopg2 >= 2.6.1
Requires:  python%{use_pyver}-gfm >= 0.1.3
Requires:  python%{use_pyver}-crypto >= 2.6.1
Requires:  python%{use_pyver}-sqlparse >= 0.1.19
Requires:  python%{use_pyver}-xmltodict >= 0.10.2

# Also provide by original name
Provides:  %{oname} = %{version}-%{release}

%description -n python%{use_pyver}-django-netbox
NetBox is an open source web application designed
to help manage and document computer networks.
Initially conceived by the network engineering team at DigitalOcean,
NetBox was developed specifically to address the needs of network
and infrastructure engineers.

%prep
%autosetup -n %{oname}-%{version} -p1

%build
# TODO: Write build steps

%install
# TODO: Write install step

# TODO: Add scriptlets

%files -n python%{use_pyver}-django-netbox
%license LICENSE.txt
%doc README.md



%changelog
* Fri Aug 19 2016 Neal Gompa <ngompa13@gmail.com> - 1.5.2-1
- Upgrade to 1.5.2
- Rediff patches
- Rename to python-django-netbox
- Merge in spec changes from Germano Massullo

* Wed Aug 10 2016 Germano Massullo <germano.massullo@gmail.com> - 1.5.0-1
- Initial packaging (python-django-netbox)

* Fri Jul 15 2016 Neal Gompa <ngompa13@gmail.com> - 1.2.2-1
- Initial packaging (netbox)
