# NOTE: for KDE4 version see kde4-kcachegrind.spec, for last KDE3 version see kcachegrind.spec
# TODO: crashes Xorg server (1.17.2 + nouveau 1.0.11)???
#
# Conditional build:
%bcond_with	qt5	# Qt5 GUI
#
Summary:	The most beautiful way to optimize your applications
Summary(pl.UTF-8):	Najładniejszy sposób optymalizowania aplikacji
Name:		qcachegrind
Version:	0.7.4
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://kcachegrind.sourceforge.net/kcachegrind-%{version}.tar.gz
# Source0-md5:	a0be465c0f4acfa08bedafb3963a3193
URL:		http://kcachegrind.sourceforge.net/html/Home.html
%if %{with qt5}
BuildRequires:	Qt5DBus-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	qt5-build >= 5
BuildRequires:	qt5-qmake >= 5
%else
BuildRequires:	QtDBus-devel >= 4.4
BuildRequires:	QtGui-devel >= 4.4
BuildRequires:	qt4-build >= 4.4
BuildRequires:	qt4-qmake >= 4.4
%endif
# "dot" can be used to generate graphs
Suggests:	graphviz
Suggests:	valgrind
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QCachegrind is a Qt GUI to visualize profiling data. It's mainly used
as visualization frontend for data measured by Cachegrind/Callgrind
tools from the Valgrind package, but there are converters for other
measurement tools available.

%description -l pl.UTF-8
QCachegrind to oparty na Qt graficzny interfejs użytkownika do
wizualizacji danych profilujących. Jest używany głównie jako interfejs
do wizualizacji dla danych zebranych przez narzędzia
Cachegrind/Callgrind z pakietu Valgrind, ale istnieją konwertery z
innych dostępnych narzędzi pomiarowych.

%prep
%setup -q -n kcachegrind-%{version}

%build
qmake-%{?with_qt5:qt5}%{!?with_qt5:qt4} \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}

install qcachegrind/qcachegrind $RPM_BUILD_ROOT%{_bindir}
cp -p qcachegrind/qcachegrind.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog.sfrelease KnownBugs README TODO
%attr(755,root,root) %{_bindir}/qcachegrind
%{_desktopdir}/qcachegrind.desktop
