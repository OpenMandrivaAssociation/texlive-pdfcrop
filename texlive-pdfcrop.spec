# revision 29348
# category Package
# catalog-ctan /support/pdfcrop/pdfcrop.pl
# catalog-date 2012-10-25 10:45:27 +0200
# catalog-license lppl
# catalog-version 1.37
Name:		texlive-pdfcrop
Version:	1.37
Release:	6
Summary:	Crop PDF graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/pdfcrop/pdfcrop.pl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcrop.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcrop.doc.tar.xz
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
%{_texmfdistdir}/scripts/pdfcrop/pdfcrop.pl
%doc %{_texmfdistdir}/doc/support/pdfcrop/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/pdfcrop/pdfcrop.pl pdfcrop
    ln -sf pdfcrop rpdfcrop
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
