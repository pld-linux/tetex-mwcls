%define		_short_name 	mwcls

Summary:	LaTeX Article, Report and Book classes by Marcin Wolinski
Summary(pl):	Klasy Article, Report i Book Marcina Woliñskiego
Name:		tetex-mwcls
Version:	20011004
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
Source0:	http://duch.mimuw.edu.pl/~wolinski/mwcls.zip
Url:		http://duch.mimuw.edu.pl/~wolinski/mwcls.html
%requires_eq	tetex
%requires_eq	tetex-latex
BuildRequires:	tetex-latex
BuildRequires:	unzip
Prereq:		tetex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes for Aricle, Report and Book by Marcin Wolinski. These classes follow
Polish (and European) typography tradition.

%description -l pl
Klasy Aricle, Report i Book autorstwa Marcina Woliñskiego. Klasy te s± zgodne 
z polskimi (i europejskimi) zwyczajami typograficznymi.

%prep
%setup  -c

%build
latex mwcls.ins

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/{tex,doc}/latex/%{_short_name} 

install {*.clo,*.cls} \
	$RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{_short_name} 

gzip -9nf mwclsdoc.ps

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p %{_bindir}/mktexlsr
%postun	-p %{_bindir}/mktexlsr

%files 
%defattr(644,root,root,755)
%doc *.gz
%{_datadir}/texmf/tex/latex/%{_short_name}/*
