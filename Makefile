PKG_NAME := jdk-kryo
URL := https://repo1.maven.org/maven2/com/esotericsoftware/kryo-shaded/3.0.3/kryo-shaded-3.0.3.jar
ARCHIVES := https://repo1.maven.org/maven2/com/esotericsoftware/kryo-shaded/3.0.3/kryo-shaded-3.0.3.pom %{buildroot} \
	https://repo1.maven.org/maven2/com/esotericsoftware/kryo/3.0.3/kryo-3.0.3.jar %{buildroot} \
	https://repo1.maven.org/maven2/com/esotericsoftware/kryo/3.0.3/kryo-3.0.3.pom %{buildroot} \
	https://repo1.maven.org/maven2/com/esotericsoftware/kryo-parent/3.0.3/kryo-parent-3.0.3.pom %{buildroot}

include ../common/Makefile.common
