%define		_short_name 	mwcls

Summary:	LaTeX Article, Report and Book classes by Marcin Wolinski
Summary(pl):	Klasy Article, Report i Book Marcina Woliñskiego
Name:		tetex-mwcls
Version:	20030509
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
Source0:	http://duch.mimuw.edu.pl/~wolinski/tex/mwcls.zip
# Source0-md5:	39526eacb03437aeebb04b1561e6dab2
URL:		http://duch.mimuw.edu.pl/~wolinski/mwcls.html
#BuildRequires:	tetex-format-latex  (for tetex-2.0 - but it's included there)
BuildRequires:	tetex-latex
BuildRequires:	unzip
PreReq:		tetex
%requires_eq	tetex
%requires_eq	tetex-latex
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes for Aricle, Report and Book by Marcin Wolinski. These classes
follow Polish (and European) typography tradition.

%description -l pl
Klasy Aricle, Report i Book autorstwa Marcina Woliñskiego. Klasy te s±
zgodne z polskimi (i europejskimi) zwyczajami typograficznymi.

%prep
%setup -q -c

%build
latex mwcls.ins

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/{tex,doc}/latex/%{_short_name}

install {*.clo,*.cls} \
	$RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{_short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p %{_bindir}/mktexlsr
%postun	-p %{_bindir}/mktexlsr

%files
%defattr(644,root,root,755)
%doc *.pdf
%{_datadir}/texmf/tex/latex/%{_short_name}
