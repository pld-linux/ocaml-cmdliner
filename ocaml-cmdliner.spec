# TODO: apidocs
#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Declarative definition of command line interfaces for OCaml
Summary(pl.UTF-8):	Deklaratywne definiowanie interfejsów linii poleceń dla OCamla
Name:		ocaml-cmdliner
Version:	1.0.4
Release:	1
License:	ISC
Group:		Libraries
Source0:	https://erratique.ch/software/cmdliner/releases/cmdliner-%{version}.tbz
# Source0-md5:	fe2213d0bc63b1e10a2d0aa66d2fc8d9
URL:		https://erratique.ch/software/cmdliner
BuildRequires:	ocaml >= 1:4.03.0
BuildRequires:	ocaml-dune
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Cmdliner allows the declarative definition of command line interfaces
for OCaml.

%description -l pl.UTF-8
Cmdliner pozwala na deklaratywne definiowanie interfejsów linii
poleceń dla OCamla.

%package devel
Summary:	Declarative definition of command line interfaces for OCaml - development part
Summary(pl.UTF-8):	Deklaratywne definiowanie interfejsów linii poleceń dla OCamla - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
This package contains files needed to develop OCaml programs using
cmdliner library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki cmdliner.

%prep
%setup -q -n cmdliner-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/cmdliner/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/cmdliner

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/cmdliner
%{_libdir}/ocaml/cmdliner/META
%{_libdir}/ocaml/cmdliner/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/cmdliner/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/cmdliner/*.a
%{_libdir}/ocaml/cmdliner/*.cmi
%{_libdir}/ocaml/cmdliner/*.cmt
%{_libdir}/ocaml/cmdliner/*.cmti
%{_libdir}/ocaml/cmdliner/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/cmdliner/*.cmx
%{_libdir}/ocaml/cmdliner/*.cmxa
%endif
%{_libdir}/ocaml/cmdliner/dune-package
%{_libdir}/ocaml/cmdliner/opam
