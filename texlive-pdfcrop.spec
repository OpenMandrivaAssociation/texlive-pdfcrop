Name:		texlive-pdfcrop
Version:	1.32
Release:	1
Summary:	Crop PDF graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/pdfcrop/pdfcrop.pl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcrop.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdfcrop.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-pdfcrop.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3

%description
A Perl script that can either trim pages of any whitespace
border, or trim them of a fixed border.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
