Name     : cinder-storage-services
Version  : 2015.1.0
Release  : 8
Source0  : cinder-volume.service
Summary  : Cinder Storage Services
Group    : Development/Tools
License  : Apache-2.0

%description
Cinder Storage Services files

%setup

%build

%install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE0} %{buildroot}/usr/lib/systemd/system/

%files
%defattr(-,root,root,-)
/usr/lib/systemd/system/cinder-volume.service
