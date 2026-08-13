%global tl_name hyphen-piedmontese
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Piedmontese hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-piedmontese
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-piedmontese.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Piedmontese in ASCII encoding. Compliant with
'Gramatica dla lengua piemonteisa' by Camillo Brero.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-piedmontese:
piedmontese loadhyph-pms.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-piedmontese:
\addlanguage{piedmontese}{loadhyph-pms.tex}{}{2}{2}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-piedmontese:
['piedmontese'] = {
	loader = 'loadhyph-pms.tex',
	lefthyphenmin = 2,
	righthyphenmin = 2,
	synonyms = {  },
	patterns = 'hyph-pms.pat.txt',
},
TL_HYPHEN_EOF
