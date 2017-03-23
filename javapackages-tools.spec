%global pkg_name javapackages-tools
%{?scl:%scl_package javapackages-tools}
%{?java_common_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        4.3.2
Release:        1.14%{?dist}

Summary:        Macros and scripts for Java packaging support

License:        BSD
URL:            https://git.fedorahosted.org/git/javapackages.git
Source0:        https://fedorahosted.org/released/javapackages/javapackages-%{version}.tar.xz
Source1:        xmvn-configuration.xml
Source2:        javapackages-config.json

Patch0:         0001-Do-not-try-to-produce-pretty-XML-with-Python-2.7.patch
Patch1:         0002-mvn_artifact-Fix-TypeError-process_raw_request-got-a.patch
Patch2:         0003-Fix-invalid-XML.patch
Patch3:         0004-maven.req-Force-namespace-for-R-on-subpackage.patch
Patch4:         0005-Replace-all-dashes-with-dots-in-versioned-provides-a.patch
Patch5:         0006-java-functions-Fix-incorrect-quotation.patch

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-lxml
BuildRequires:  python-setuptools
BuildRequires:  python-nose
BuildRequires:  %{?scl_prefix}PyXB = 1.2.4
BuildRequires:  asciidoc
BuildRequires:  xmlto
BuildRequires:  scl-utils-build
#BuildRequires:  %{?scl_prefix}javapackages-tools >= 4.0.0
#BuildRequires:  %{?scl_prefix}xmvn-resolve >= 2

Requires:       coreutils
Requires:       findutils
Requires:       which
Requires:       lua
Requires:       %{?scl_prefix}python-javapackages = %{version}-%{release}
Requires:       python

Provides:       %{?scl_prefix}jpackage-utils = %{version}-%{release}

Provides:       %{?scl_prefix}mvn(com.sun:tools)
Provides:       %{?scl_prefix}mvn(sun.jdk:jconsole)

%description
This package provides macros and scripts to support Java packaging.

%package -n %{?scl_prefix}maven-local
Summary:        Support for Maven packaging
Requires:       %{?scl_prefix}maven-local-support = %{version}-%{release}
Requires:       %{?scl_prefix}javapackages-local = %{version}-%{release}
Requires:       %{?scl_prefix_maven}maven
Requires:       %{?scl_prefix_maven}xmvn >= 2
Requires:       %{?scl_prefix_maven}xmvn-mojo >= 2
Requires:       %{?scl_prefix_maven}xmvn-connector-aether >= 2
# POM files needed by maven itself
Requires:       %{?scl_prefix_maven}apache-commons-parent
Requires:       %{?scl_prefix_maven}apache-parent
Requires:       %{?scl_prefix_maven}geronimo-parent-poms
Requires:       %{?scl_prefix_maven}httpcomponents-project
Requires:       %{?scl_prefix_maven}jboss-parent
Requires:       %{?scl_prefix_maven}jvnet-parent
Requires:       %{?scl_prefix_maven}maven-parent
Requires:       %{?scl_prefix_maven}maven-plugins-pom
Requires:       %{?scl_prefix_maven}mojo-parent
#Requires:       %{?scl_prefix_maven}objectweb-pom
Requires:       %{?scl_prefix_maven}plexus-components-pom
Requires:       %{?scl_prefix_maven}plexus-pom
Requires:       %{?scl_prefix_maven}plexus-tools-pom
Requires:       %{?scl_prefix_maven}sonatype-oss-parent
Requires:       %{?scl_prefix_maven}weld-parent
# Common Maven plugins required by almost every build. It wouldn't make
# sense to explicitly require them in every package built with Maven.
Requires:       %{?scl_prefix_maven}maven-assembly-plugin
Requires:       %{?scl_prefix_maven}maven-compiler-plugin
Requires:       %{?scl_prefix_maven}maven-enforcer-plugin
Requires:       %{?scl_prefix_maven}maven-jar-plugin
Requires:       %{?scl_prefix_maven}maven-javadoc-plugin
Requires:       %{?scl_prefix_maven}maven-resources-plugin
Requires:       %{?scl_prefix_maven}maven-surefire-plugin
# Tests based on JUnit are very common and JUnit itself is small.
# Include JUnit provider for Surefire just for convenience.
Requires:       %{?scl_prefix_maven}maven-surefire-provider-junit
# testng is quite common as well
Requires:       %{?scl_prefix_maven}maven-surefire-provider-testng

%description -n %{?scl_prefix}maven-local
This package provides tools to support packaging Maven artifacts.

%package -n %{?scl_prefix}maven-local-support
Summary:        Macros and scripts for Maven packaging support
Requires:       %{name} = %{version}-%{release}
Requires:       %{?scl_prefix}javapackages-local-support = %{version}-%{release}

%description -n %{?scl_prefix}maven-local-support
This package provides macros and scripts to support packaging Maven
artifacts. To enable all features, it's necessary to install also
rh-java-common-maven-local package, or <scl-prefix>maven-local package
from other compatible Software Collection.

%package -n %{?scl_prefix}ivy-local
Summary:        Support for Apache Ivy packaging
Requires:       %{?scl_prefix}ivy-local-support = %{version}-%{release}
Requires:       %{?scl_prefix}javapackages-local = %{version}-%{release}
Requires:       %{?scl_prefix_maven}apache-ivy
Requires:       %{?scl_prefix_maven}xmvn-connector-ivy >= 2

%description -n %{?scl_prefix}ivy-local
This package provides tools to support Apache Ivy packaging.

%package -n %{?scl_prefix}ivy-local-support
Summary:        Local mode for Apache Ivy
Requires:       %{name} = %{version}-%{release}
Requires:       %{?scl_prefix}javapackages-local-support = %{version}-%{release}

%description -n %{?scl_prefix}ivy-local-support
This package implements local mode fow Apache Ivy, which allows artifact
resolution using XMvn resolver. To enable all features, it's necessary
to install also rh-java-common-ivy-local package, or <scl-prefix>ivy-local
package from other compatible Software Collection.

%package -n %{?scl_prefix}python-javapackages
Summary:        Module for handling various files for Java packaging
Requires:       %{?scl_prefix}PyXB = 1.2.4
Requires:       python-lxml
%{?scl:Requires: %scl_runtime}

%description -n %{?scl_prefix}python-javapackages
Module for handling, querying and manipulating of various files for Java
packaging in Linux distributions

%package -n %{?scl_prefix}javapackages-local
Summary:        Non-essential tools for Java packaging
Requires:       %{?scl_prefix}javapackages-local-support = %{version}-%{release}
Requires:       %{?scl_prefix_maven}xmvn-install >= 2
Requires:       %{?scl_prefix_maven}xmvn-subst >= 2
Requires:       %{?scl_prefix_maven}xmvn-resolve >= 2

%description -n %{?scl_prefix}javapackages-local
This package provides non-essential tools for Java packaging.

%package -n %{?scl_prefix}javapackages-local-support
Summary:        Non-essential macros and scripts for Java packaging support
Requires:       %{name} = %{version}-%{release}

%description -n %{?scl_prefix}javapackages-local-support
This package provides non-essential macros and scripts to support Java
packaging. To enable all features, it's necessary to install also
rh-java-common-javapackages-local package, or <scl-prefix>javapackages-local
package from other compatible Software Collection.

%prep
%setup -q -n javapackages-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

cp %{SOURCE1} configs/configuration.xml
cp etc/javapackages-config.json etc/javapackages-config.json.1
cp %{SOURCE2} etc/javapackages-config.json

sed -i '/fedora-review/d' install
sed -i 's:\(inst_exec target/mvn-local\).*:\1 ${javadir}-utils:' install
sed -i '/make -C doc/d' build
sed -i '/^inst_doc /d' install

sed -i 's:${rpmconfigdir}/macros.d:%{_root_sysconfdir}/rpm:' install

# Add SCL namespace to generated provides
%{?scl:sed -i '/<groupId>/{h;s|<.*|<namespace>%{scl}</namespace>|;p;g}' etc/javapackages-metadata.xml}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%configure
./build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
./install
sed -e 's/.[17]$/&.gz/' -e 's/.py$/&*/' -i files-*

mv ${RPM_BUILD_ROOT}/%{_root_sysconfdir}/rpm/macros.fjava{,.%{?scl}}
mv ${RPM_BUILD_ROOT}/%{_root_sysconfdir}/rpm/macros.jpackage{,.%{?scl}}
mv ${RPM_BUILD_ROOT}/%{_root_sysconfdir}/rpm/macros.xmvn{,.%{?scl}}
sed -i 's:macros.\(fjava\|jpackage\|xmvn\):&.%{?scl}:' files-*

# no fedora-review in RHEL 7
rm -rf %{buildroot}/%{_datadir}/fedora-review/
%{?scl:EOF}

%check
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
cp etc/javapackages-config.json.1 etc/javapackages-config.json
./check
%{?scl:EOF}

%files -f files-common
%doc LICENSE

%files -n %{?scl_prefix}javapackages-local
%files -n %{?scl_prefix}javapackages-local-support -f files-local

%files -n %{?scl_prefix}maven-local
%files -n %{?scl_prefix}maven-local-support -f files-maven

%files -n %{?scl_prefix}ivy-local
%files -n %{?scl_prefix}ivy-local-support -f files-ivy

%files -n %{?scl_prefix}python-javapackages
%doc LICENSE
%{?_scl_root}%{python_sitelib}/javapackages*

%changelog
* Tue Jan 17 2017 Michael Simacek <msimacek@redhat.com> - 4.3.2-1.14
- Add requires on which and findutils
- Resolves: rhbz#1413880

* Mon Jan 16 2017 Michael Simacek <msimacek@redhat.com> - 4.3.2-1.13
- Rebuild to regenerate autorequires

* Mon Jan 16 2017 Michael Simacek <msimacek@redhat.com> - 4.3.2-1.12
- Generate autorequires on java-headless instead of java
- Resolves: rhbz#1413543

* Mon Jan 25 2016 Michal Srb <msrb@redhat.com> - 4.3.2-1.11
- Move all macros and scripts to the "support" subpackages (Resolves: rhbz#1298464)

* Wed Jul 22 2015 Michal Srb <msrb@redhat.com> - 4.3.2-1.10
- Fix incorrect quotation in java-functions
- Resolves: rhbz#1245266

* Mon Apr 27 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.3.2-1.9
- Rebuild for final RHSCL 2.0 release

* Wed Jan 14 2015 Michal Srb <msrb@redhat.com> - 4.3.2-1.8
- Replace all dashes with dots in versioned provides and requires

* Wed Jan 14 2015 Michal Srb <msrb@redhat.com> - 4.3.2-1.7
- Add namespace for OSGi Requires on subpackage

* Wed Jan 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.3.2-1.6
- Fix invalid XML

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 4.3.2-1.5
- Mass rebuild 2015-01-13

* Fri Jan 09 2015 Michal Srb <msrb@redhat.com> - 4.3.2-1.4
- Mass rebuild 2015-01-09

* Wed Jan  7 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.3.2-1.3
- Fix XMvn configuration

* Tue Jan 06 2015 Michal Srb <msrb@redhat.com> - 4.3.2-1.2
- Fix TypeError in mvn_artifact

* Tue Jan 06 2015 Michal Srb <msrb@redhat.com> - 4.3.2-1.1
- Fix release tag

* Tue Jan 06 2015 Michal Srb <msrb@redhat.com> - 4.3.2-2
- Backport "pretty" XML fix for python 2.6

* Mon Jan 05 2015 Michal Srb <msrb@redhat.com> - 4.3.2-1
- Update to upstream release 4.3.2

* Mon Jan 05 2015 Michael Simacek <msimacek@redhat.com> - 4.3.2-0.4.20150105git4fb1f4b
- Update to latest snapshot

* Fri Jan  2 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.3.2-0.3.20150201git98d04f9
- Spec file fixes

* Fri Jan 02 2015 Michal Srb <msrb@redhat.com> - 4.3.2-0.2.20150201git98d04f9
- Update to upstream 4.3.2 snapshot

* Fri Jan  2 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.3.1-1.3
- Update xmvn-configuration.xml

* Wed Dec 24 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.3.1-1.2
- Don't generate requires on java-headless

* Wed Dec 24 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.3.1-1.1
- Update to upstream version 4.3.1

* Mon Dec 22 2014 Michael Simacek <msimacek@redhat.com> - 4.3.0-1.8
- Autoenable scl for getting config

* Mon Dec 22 2014 Michael Simacek <msimacek@redhat.com> - 4.3.0-1.7
- Fix getting Python version on 2.6

* Fri Dec 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.3.0-1.6
- Update patch removing dependency on python-six

* Thu Dec 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.3.0-1.5
- Install custom javapackages-config.json

* Wed Dec 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.3.0-1.4
- Rebuild to regenerate requires

* Wed Dec 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.3.0-1.3
- Fix resolver prefixes in XMvn config

* Wed Dec 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.3.0-1.2
- Remove dependency on python-six

* Wed Dec 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.3.0-1.1
- Update to upstream version 4.3.0
- Add up-to-date SCL-ized XMvn configuration

* Mon Dec 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.4.1-5.18
- Fix mavendepmapfragdir location

* Mon Dec 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.4.1-5.17
- Rebuid to regenerate requires

* Mon Dec 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.4.1-5.16
- Rebuild for rh-java-common collection

* Tue May 27 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.4.1-5.15
- Rebuild

* Thu Feb 20 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.4.1-5.14
- Add scl requires in python subpackage

* Tue Feb 18 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.4.1-5.13
- Skip requires on java and java-devel

* Tue Feb 18 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.4.1-5.12
- Skip requires on tools/jconsole jars

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.4.1-5.11
- Don't resolve artifacts from base RHEL

* Mon Feb 17 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.4.1-5.10
- Fix autorequires for javadoc packages

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.4.1-5.9
- SCL-ize requires for maven-local

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.4.1-5.8
- Install macros.jpackage

* Wed Feb 12 2014 Michal Srb <msrb@redhat.com> - 3.4.1-5.7
- Backport upstream patch for add_maven_depmap

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.4.1-5.6
- Use custom XMvn config

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.4.1-5.5
- Add SCL namespace to generated provides

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.4.1-5.4
- Backport two upstream fixes related to SCL

* Fri Feb 07 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.4.1-5.3
- Move macros to not conflict with normal packages

* Thu Feb 06 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.4.1-5.2
- Fix requires on subpackage

* Thu Feb 06 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.4.1-5.1
- SCLize javapackages-tools

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.4.1-5
- Mass rebuild 2013-12-27

* Mon Dec 16 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.4.1-4
- Support absolute symlinks in SCLs in mvn_file
- Resolves: rhbz#1038553

* Thu Dec 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.4.1-3
- Move mvn-local out of bindir
- Resolves: rhbz#1015422

* Thu Nov 14 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.4.1-2
- Add versioned requires on python-javapackages

* Wed Nov 06 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.4.1-1
- Rebase to bugfix release 3.4.1
- Related: rhbz#1015158

* Tue Oct 08 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.3.1-2
- Remove workaround for guice-no_aop
- Remove fedora-review subpackage
- Resolves: rhbz#1016667
- Related: rhbz#1015158

* Wed Oct  2 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.1-1
- Update to upstream version 3.3.1
- Remove workaround for sisu-guice no_aop

* Tue Oct 01 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.3.0-1
- Update to upstream version 3.3.0

* Wed Sep 25 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.2.4-2
- Fix installation of artifacts with classifier

* Tue Sep 24 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.2.4-1
- Update to upstream version 3.2.4

* Tue Sep 24 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.2.3-1
- Update to upstream version 3.2.3

* Fri Sep 20 2013 Michal Srb <msrb@redhat.com> - 3.2.2-1
- Update to upstream version 3.2.2

* Fri Sep 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.1-1
- Update to upstream version 3.2.1

* Fri Sep 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.0-1
- Update to upstream version 3.2.0

* Fri Sep 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.2-1
- Update to upstream version 3.1.2

* Thu Sep 19 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.1.1-1
- Update to upstream version 3.1.1

* Thu Sep 19 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.1.0-1
- Update to upstream version 3.1.0

* Mon Sep 16 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.4-2
- Add depmap for sun.jdk:jconsole

* Fri Sep 13 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.0.4-1
- Update to upstream version 3.0.4

* Wed Sep 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.0.3-1
- Update to upstream version 3.0.3

* Tue Sep 10 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.0.2-3
- Fix a typo in temporary depmap

* Tue Sep 10 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.0.2-2
- Make sure we do not provide google guice mapping

* Tue Sep 10 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> 3.0.2-1
- Update to upstream version 3.0.2
- Add separate python-javapackages subpackage
- Add separate fedora-review-plugin-java subpackage
- Enable part of unit tests

* Tue Sep  3 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> 3.0.0-0.2
- Fix javadoc directory override

* Tue Sep  3 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> 3.0.0-0.1
- Update to upstream pre-release version 3.0.0

* Fri Jul 26 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0.1-1
- Update to upstream version 2.0.1
- Fix creation of artifact aliases, resolves: rhbz#988462

* Thu Jul 25 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0.0-2
- Require maven-resources-plugin by maven-local

* Thu Jul 11 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0.0-1
- Update to upstream version 2.0.0
- Merge functionality of jpackage-utils
- Provide and obsolete jpackage-utils
- %%add_maven_depmap macro now injects pom.properties to every JAR
- %%add_to_maven_depmap and %%update_maven_depmap macros were removed
- maven2jpp-mapdeps.xsl template has been removed
- Macros related to installation of icons and desktop files were removed
- 14 new manual pages were added
- Documentation specific to JPackage was removed
- Add BuildRequires: asciidoc, xmlto

* Mon Jul  1 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.15.0-2
- Add R: jvnet-parent

* Wed Jun  5 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.15.0-1
- Update to upstream version 0.15.0
- Added depmap for tools.jar
- Added support for versioned autorequires
- New plugin metadata from Maven Central

* Tue Jun  4 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.14.1-2
- Add several maven plugins to maven-local requires

* Wed May 29 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.14.1-1
- Update to upstream version 0.14.1 with disabled debugging

* Tue Apr 09 2013 Michal Srb <msrb@redhat.com> - 0.14.0-1
- Update to upstream version 0.14.0

* Mon Apr  8 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.13.7-2
- Add R: maven-surefire-provider-junit4 to maven-local

* Fri Mar 22 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.13.7-1
- Update to upstream version 0.13.7

* Wed Mar 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.13.6-4
- Add geronimo-parent-poms to common POMs

* Wed Mar 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.13.6-3
- Add weld-parent to common POMs

* Wed Mar 20 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.13.6-2
- Fix conditional macro to evaluate properly when fedora is not defined

* Mon Mar 18 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.13.6-1
- Update to upstream version 0.13.6

* Wed Mar 13 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.13.5-1
- Update to upstream version 0.13.5

* Wed Mar 13 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.13.4-1
- Update to upstream version 0.13.4

* Tue Mar 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.13.3-1
- Update to upstream version 0.13.3

* Thu Mar  7 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.13.2-1
- Update to upstream version 0.13.2

* Thu Mar  7 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.13.1-1
- Update to upstream version 0.13.1

* Wed Mar  6 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.13.0-1
- Update to upstream version 0.13.0

* Wed Mar  6 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.13.0-0.1.git2f13366
- Upate to upstream pre-release snapshot 2f13366

* Mon Mar  4 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.12.6-1
- Update to upstream version 0.12.6
- Resolves: rhbz#917618 (remove jetty orbit provides)
- Resolves: rhbz#917647 (system.bundle into autogenerated deps)

* Fri Mar  1 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.12.5-1
- Update to upstream version 0.12.5
- Resolves problems with compat package provides and automatic requires

* Wed Feb 27 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.12.4-2
- Don't mark RPM macro files as configuration

* Mon Feb 25 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.12.4-1
- Update to upstream version 0.12.4
- Resolves: rhbz#913630 (versioned requires between subpackages)

* Fri Feb 22 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.12.3-1
- Update to upstream version 0.12.3
- Resolves: rhbz#913694 (No plugin found for prefix 'X')

* Wed Feb 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.12.2-1
- Update to upstream version 0.12.2
- Resolves: rhbz#913120 (MAVEN_OPTS are not passed to Maven)

* Mon Feb 18 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.12.1-1
- Update to upstream version 0.12.1
- Resolves: rhbz#912333 (M2_HOME is not exported)

* Fri Feb 15 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.12.0-1
- Update to upstream version 0.12.0
- Implement new pom macros: xpath_replace and xpath_set
- Remove Support-local-depmaps.patch (accepted upstream)

* Fri Feb 15 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.11.2-6
- Support local depmaps

* Thu Feb 14 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.11.2-5
- Add some maven-local Requires for convenience

* Thu Feb  7 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.11.2-4
- Add missing R: httpcomponents-project

* Thu Feb  7 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.11.2-3
- Add missing R: jboss-patent

* Wed Feb  6 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.11.2-2
- Don't install mvn-local and mvn-rpmbuild on F18

* Wed Jan 30 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.11.2-1
- Update to upstream version 0.11.2

* Wed Jan 30 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.11.1-1
- Update to upstream version 0.11.1

* Wed Jan 23 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.11.0-1
- Update to upstream version 0.11.0
- Add mvn-local and mvn-rpmbuild scripts

* Mon Jan 21 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.10.1-1
- Update to upstream version 0.10.1

* Mon Jan  7 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.10.0-1
- Update to upstream version 0.10.0
- Implement %%xmvn_alias, %%xmvn_file and %%xmvn_package macros
- Fix regex in osgi.attr
- Add support for pre- and post-goals in mvn-build script

* Mon Dec 10 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.9.1-1
- Update to upstream version 0.9.1
- Resolves: rhbz#885636

* Thu Dec  6 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.9.0-1
- Update to latest upstream version
- Enable maven requires generator for xmvn packages
- Enable requires generator for javadoc packages

* Wed Dec  5 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.8.3-1
- Update to upstream version 0.8.3
- Fix maven provides generator for new XML valid fragments

* Fri Nov 30 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.8.2-1
- Update to upstream version 0.8.2

* Fri Nov 30 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.8.1-1
- Update to upstream version 0.8.1

* Wed Nov 28 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.8.0-1
- Update to upstream version 0.8.0
- Add xmvn macros

* Tue Nov 27 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7.5-3
- Add BR: jpackage-utils

* Tue Nov 27 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7.5-2
- Add maven-local subpackage

* Thu Nov 08 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.7.5-1
- Fix versioned pom installation by quoting _jpath

* Wed Oct 31 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.7.4-1
- Shorten maven filelist filenames

* Wed Oct 31 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7.3-1
- Update to upstream version 0.7.3

* Wed Oct 31 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.7.2-1
- Make sure add_maven_depmap fails when python tracebacks

* Wed Oct 31 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.7.1-1
- Fix problem with exception in default add_maven_depmap invocation

* Tue Oct 30 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.7.0-1
- Update to latest upstream
- Full support for compat depmap generation
- Generate maven-files-%%{name} with a list of files to package
- Add support for maven repo generation (alpha version)

* Mon Jul 30 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.6.0-1
- Update to upstream version 0.6.0
- Make maven provides versioned
- Add additional pom_ macros to simplify additional pom editing

* Wed Jul 25 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.5.0-1
- Update to upstream version 0.5.0 - add support for add_maven_depmap -v

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  9 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.4.1-1
- Update to upstream version 0.4.1
- Fixes #837203

* Wed Jun 27 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.4.0-1
- Update to upstream version 0.4.0

* Tue Mar  6 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.3.1-1
- Create maven provides from fragments instead of poms

* Thu Feb 16 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.3.0-3
- Fix maven_depmap installation

* Wed Feb 15 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.3.0-2
- Add conflicts with older jpackage-utils

* Wed Feb 15 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.3.0-1
- Initial version split from jpackage-utils
