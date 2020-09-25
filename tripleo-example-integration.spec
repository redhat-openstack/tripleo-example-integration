%global shortname example
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           tripleo-example-integration
Version:        XXX
Release:        XXX
Summary:        Example TripleO 3rd party integration

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://github.com/redhat-openstack/tripleo-example-integration
Source0:        https://github.com/redhat-openstack/tripleo-example-integration/archive/%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git

Requires:       python3dist(ansible)
Requires:       openstack-tripleo-heat-templates

%description
Example TripleO 3rd party integration. The main package includes all the
files that need to be included on the Undercloud. This can included
scripts, ansible roles, and tripleo-heat-template related items.

%package -n puppet-%{shortname}
Summary:        Puppet modules for Example TripleO 3rd party integration
Requires:       puppet

%description -n puppet-%{shortname}
Puppet modules for the example TripleO 3rd party integration. This package
will need to be included on the remote systems where it is used. This is
usually handled as part of a virt-customize action on overcloud-full or
provided via a repository to the overcloud that is available at deployment
time.

%prep
%autosetup -n %{name}-%{upstream_version} -S git


%build


%install
install -d -m 0755 %{buildroot}/%{_datadir}/%{name}/scripts
cp -r scripts/* %{buildroot}%{_datadir}/%{name}/scripts/
# ansible roles
install -d -m 0755 %{buildroot}/%{_datadir}/ansible/roles/
cp -r ansible/roles/* %{buildroot}%{_datadir}/ansible/roles/
# puppet modules
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/
cp -r puppet/* %{buildroot}%{_datadir}/openstack-puppet/modules/
# tripleo-heat-template integration
install -d -m 0755 %{buildroot}%{_datadir}/openstack-tripleo-heat-templates/environments/%{shortname}
cp -r tripleo/environments/* %{buildroot}%{_datadir}/openstack-tripleo-heat-templates/environments/%{shortname}/
install -d -m 0755  %{buildroot}%{_datadir}/openstack-tripleo-heat-templates/deployment/%{shortname}
cp -r tripleo/deployment/* %{buildroot}%{_datadir}/openstack-tripleo-heat-templates/deployment/%{shortname}/
install -d -m 0755  %{buildroot}%{_datadir}/openstack-tripleo-heat-templates/network/%{shortname}
cp -r tripleo/network/* %{buildroot}%{_datadir}/openstack-tripleo-heat-templates/network/%{shortname}/

%files
%doc README*
%license LICENSE
%{_datadir}/%{name}
%{_datadir}/%{name}/scripts
# TODO: list role
%{_datadir}/ansible/roles/*
# TODO: list modules
%{_datadir}/openstack-tripleo-heat-templates/environments/%{shortname}
%{_datadir}/openstack-tripleo-heat-templates/deployment/%{shortname}
%{_datadir}/openstack-tripleo-heat-templates/network/%{shortname}

%files -n puppet-%{shortname}
%doc README*
%license LICENSE
%{_datadir}/openstack-puppet/modules/*

%changelog
