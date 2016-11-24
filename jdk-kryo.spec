Name     : jdk-kryo
Version  : 3.0.3
Release  : 3
URL      : https://repo1.maven.org/maven2/com/esotericsoftware/kryo-shaded/3.0.3/kryo-shaded-3.0.3.jar
Source0  : https://repo1.maven.org/maven2/com/esotericsoftware/kryo-shaded/3.0.3/kryo-shaded-3.0.3.jar
Source1  : https://repo1.maven.org/maven2/com/esotericsoftware/kryo-shaded/3.0.3/kryo-shaded-3.0.3.pom
Source2  : https://repo1.maven.org/maven2/com/esotericsoftware/kryo/3.0.3/kryo-3.0.3.jar
Source3  : https://repo1.maven.org/maven2/com/esotericsoftware/kryo/3.0.3/kryo-3.0.3.pom
Source4  : https://repo1.maven.org/maven2/com/esotericsoftware/kryo-parent/3.0.3/kryo-parent-3.0.3.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: jdk-kryo-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-kryo package.
Group: Data

%description data
data components for the jdk-kryo package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/kryo-shaded.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/kryo-shaded.pom
mv %{SOURCE2} %{buildroot}/usr/share/java/kryo.jar
mv %{SOURCE3} %{buildroot}/usr/share/maven-poms/kryo.pom
mv %{SOURCE4} %{buildroot}/usr/share/maven-poms/kryo-parent.pom

# Creates metadata
for n in kryo-shaded \
         kryo \
         kryo-parent;do
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/$n.xml \
%{buildroot}/usr/share/maven-poms/$n.pom \
%{buildroot}/usr/share/java/$n.jar
done

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/kryo.jar
/usr/share/maven-metadata/kryo.xml
/usr/share/maven-poms/kryo.pom
/usr/share/java/kryo-shaded.jar
/usr/share/maven-metadata/kryo-parent.xml
/usr/share/maven-metadata/kryo-shaded.xml
/usr/share/maven-poms/kryo-parent.pom
/usr/share/maven-poms/kryo-shaded.pom
