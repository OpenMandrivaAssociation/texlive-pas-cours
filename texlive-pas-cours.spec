Name:		texlive-pas-cours
Version:	1.6
Release:	2
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
%{_texmfdistdir}/tex/latex/pas-cours
%doc %{_texmfdistdir}/doc/latex/pas-cours

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
