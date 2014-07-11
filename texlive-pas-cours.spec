# revision 32444
# category Package
# catalog-ctan /macros/latex/contrib/pas-cours
# catalog-date 2013-12-05 10:50:59 +0100
# catalog-license lppl
# catalog-version 1.06
Name:		texlive-pas-cours
Version:	1.06
Release:	3
Summary:	Macros useful in preparing teaching material
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pas-cours
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pas-cours.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pas-cours.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Several groups of macros cover different branches of
mathematics.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pas-cours/pas-cours.sty
%doc %{_texmfdistdir}/doc/latex/pas-cours/README
%doc %{_texmfdistdir}/doc/latex/pas-cours/README.TEXLIVE
%doc %{_texmfdistdir}/doc/latex/pas-cours/attention.png
%doc %{_texmfdistdir}/doc/latex/pas-cours/coeur.png
%doc %{_texmfdistdir}/doc/latex/pas-cours/macro-patrons.tex
%doc %{_texmfdistdir}/doc/latex/pas-cours/macro-solides.tex
%doc %{_texmfdistdir}/doc/latex/pas-cours/macro-styles.tex
%doc %{_texmfdistdir}/doc/latex/pas-cours/prerequis.png

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
