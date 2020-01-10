Name: hunspell-ak
Summary: Akan hunspell dictionaries
Version: 0.6
Release: 6%{?dist}
Group: Applications/Text
Source: http://releases.mozilla.org/pub/mozilla.org/addons/9978/akan_ns__mfuaasekyer__-%{version}-fx.xpi
URL: http://kasahorow.org/content/akan-nsɛmfuaasekyerɛ
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#https://addons.mozilla.org/en-US/firefox/versions/license/73122
License: LGPLv3
BuildArch: noarch
BuildRequires: redland

Requires: hunspell

%description
Akan hunspell dictionaries.

%prep
%setup -q -c

%build
rdfproc hunspell-oc parse install.rdf
rdfproc hunspell-oc print | grep install-manifest | grep -v targetApplication | sed -e 's/.*#//' | sed -e 's/], "/: /'| sed -e 's/"}//' > CREDITS
chmod -x dictionaries/ak-GH.*

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/ak-GH.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/ak_GH.aff
cp -p dictionaries/ak-GH.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/ak_GH.dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CREDITS
%{_datadir}/myspell/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 30 2011 Caolan McNamara <caolanm@redhat.com> - 0.6-3
- Resolves: rhbz#734218 remove executable flags

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 25 2010 Caolan McNamara <caolanm@redhat.com> - 0.6-1
- latest version

* Fri Aug 21 2009 Caolan McNamara <caolanm@redhat.com> - 0.3-1
- initial version
