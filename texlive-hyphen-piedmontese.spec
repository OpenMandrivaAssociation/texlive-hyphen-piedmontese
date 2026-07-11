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
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Piedmontese in ASCII encoding. Compliant with
'Gramatica dla lengua piemonteisa' by Camillo Brero.

