# revision 29193
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-piedmontese
Version:	20131011
Release:	9
Summary:	Piedmontese hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-piedmontese.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Piedmontese in ASCII encoding.
Compliant with 'Gramatica dla lengua piemonteisa' by Camillo
Brero.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-piedmontese
%_texmf_language_def_d/hyphen-piedmontese
%_texmf_language_lua_d/hyphen-piedmontese

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-piedmontese <<EOF
\%% from hyphen-piedmontese:
piedmontese loadhyph-pms.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-piedmontese
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-piedmontese <<EOF
\%% from hyphen-piedmontese:
\addlanguage{piedmontese}{loadhyph-pms.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-piedmontese
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-piedmontese <<EOF
-- from hyphen-piedmontese:
	['piedmontese'] = {
		loader = 'loadhyph-pms.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-pms.pat.txt',
		hyphenation = '',
	},
EOF
