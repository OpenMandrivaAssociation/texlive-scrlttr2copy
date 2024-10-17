Name:		texlive-scrlttr2copy
Version:	56733
Release:	2
Summary:	A letter class option file for the automatic creation of copies
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/scrlttr2copy
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scrlttr2copy.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scrlttr2copy.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The file copy.lco provides the new class option "copy" for the
KOMA-Script letter class scrlttr2. If the option "copy" is
given, all pages of a specific letter are duplicated with
background text marking as copies.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/scrlttr2copy
%doc %{_texmfdistdir}/doc/latex/scrlttr2copy

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
