%global oname netbox

# Use Python 3 by default
%bcond_without python3

%global python2_pkgversion 2
%{?!python3_pkgversion:%global python3_pkgversion 3}

%if %{with python3}
%global use_pyver %python3_pkgversion
%else
%global use_pyver %python2_pkgversion
%endif

# Minimum versions for deps
%global min_cryptography_ver 1.4
%global min_django_ver 1.10
%global min_django_debug_toolbar_ver 1.4
%global min_django_filter_ver 0.13.0
%global min_django_rest_swagger_ver 0.3.10
%global min_django_tables2_ver 1.2.1
%global min_django_rest_framework_ver 3.4.3
%global min_graphviz_ver 0.4.10
%global min_markdown_ver 2.6.6
%global min_natsort_ver 5.0.0
%global min_ncclient_ver 0.5.2
%global min_netaddr_ver 0.7.18
%global min_paramiko_ver 2.0.0
%global min_psycopg2_ver 2.6.1
%global min_py_gfm_ver 0.1.3
%global min_pycrypto_ver 2.6.1
%global min_sqlparse_ver 0.1.19
%global min_xmltodict_ver 0.10.2

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
BuildRequires:  python%{use_pyver}-cryptography >= %{min_cryptography_ver}
BuildRequires:  python%{use_pyver}-django >= %{min_django_ver}
# Missing py3 build
BuildRequires:  python%{use_pyver}-django-debug-toolbar >= %{min_django_debug_toolbar_ver}
BuildRequires:  python%{use_pyver}-django-filter >= %{min_django_filter_ver}
BuildRequires:  python%{use_pyver}-django-rest-swagger >= %{min_django_rest_swagger_ver}
BuildRequires:  python%{use_pyver}-django-tables2 >= %{min_django_tables2_ver}
BuildRequires:  python%{use_pyver}-django-rest-framework >= %{min_django_rest_framework_ver}
BuildRequires:  python%{use_pyver}-graphviz >= %{min_graphviz_ver}
BuildRequires:  python%{use_pyver}-markdown >= %{min_markdown_ver}
BuildRequires:  python%{use_pyver}-natsort >= %{min_natsort_ver}
BuildRequires:  python%{use_pyver}-ncclient >= %{min_ncclient_ver}
BuildRequires:  python%{use_pyver}-netaddr >= %{min_netaddr_ver}
BuildRequires:  python%{use_pyver}-paramiko >= %{min_paramiko_ver}
BuildRequires:  python%{use_pyver}-psycopg2 >= %{min_psycopg2_ver}
# This is py-gfm
BuildRequires:  python%{use_pyver}-gfm >= %{min_py_gfm_ver}
# This is pycrypto
BuildRequires:  python%{use_pyver}-crypto >= %{min_pycrypto_ver}

BuildRequires:  python%{use_pyver}-sqlparse >= %{min_sqlparse_ver}
BuildRequires:  python%{use_pyver}-xmltodict >= %{min_xmltodict_ver}

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
Requires:  python%{use_pyver}-cryptography >= %{min_cryptography_ver}
Requires:  python%{use_pyver}-django >= %{min_django_ver}
Requires:  python%{use_pyver}-django-debug-toolbar >= %{min_django_debug_toolbar_ver}
Requires:  python%{use_pyver}-django-filter >= %{min_django_filter_ver}
Requires:  python%{use_pyver}-django-rest-swagger >= %{min_django_rest_swagger_ver}
Requires:  python%{use_pyver}-django-tables2 >= %{min_django_tables2_ver}
Requires:  python%{use_pyver}-django-rest-framework >= %{min_django_rest_framework_ver}
Requires:  python%{use_pyver}-graphviz >= %{min_graphviz_ver}
Requires:  python%{use_pyver}-markdown >= %{min_markdown_ver}
Requires:  python%{use_pyver}-natsort >= %{min_natsort_ver}
Requires:  python%{use_pyver}-ncclient >= %{min_ncclient_ver}
Requires:  python%{use_pyver}-netaddr >= %{min_netaddr_ver}
Requires:  python%{use_pyver}-paramiko >= %{min_paramiko_ver}
Requires:  python%{use_pyver}-psycopg2 >= %{min_psycopg2_ver}
Requires:  python%{use_pyver}-gfm >= %{min_py_gfm_ver}
Requires:  python%{use_pyver}-crypto >= %{min_pycrypto_ver}
Requires:  python%{use_pyver}-sqlparse >= %{min_sqlparse_ver}
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
# nothing to do here

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_bindir}

cp -a netbox/* %{buildroot}%{_datadir}/%{name}
ln -sf %{_sysconfdir}/%{name}/%{oname}/configuration.py %{buildroot}%{_datadir}/%{name}/configuration.py

# FIXME: This doesn't actually work
#ln -sf %{_datadir}/%{name}/manage.py %{buildroot}%{_bindir}/%{oname}-manage
#ln -sf %{_datadir}/%{name}/generate_secret_key.py %{buildroot}%{_bindir}/%{oname}-genseckey


# We'll docify this later
rm %{buildroot}%{_datadir}/%{name}/%{oname}/configuration.{docker,example}.py

# TODO: Add scriptlets

%files -n python%{use_pyver}-django-netbox
%license LICENSE.txt
%doc README.md docs/* netbox/netbox/configuration.{docker,example}.py



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
