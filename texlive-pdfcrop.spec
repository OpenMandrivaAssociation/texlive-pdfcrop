Name:		texlive-pdfcrop
Version:	55435
Release:	1
Summary:	Crop PDF graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/pdfcrop/pdfcrop.pl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcrop.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcrop.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-pdfcrop.bin = %{EVRD}

%description
A Perl script that can either trim pages of any whitespace
border, or trim them of a fixed border.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/pdfcrop
%{_bindir}/rpdfcrop
%{_texmfdistdir}/scripts/pdfcrop
%doc %{_texmfdistdir}/doc/support/pdfcrop

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/pdfcrop/pdfcrop.pl pdfcrop
ln -sf pdfcrop rpdfcrop
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
