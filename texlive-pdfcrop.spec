# revision 26313
# category Package
# catalog-ctan /support/pdfcrop/pdfcrop.pl
# catalog-date 2012-04-18 16:26:37 +0200
# catalog-license lppl
# catalog-version 1.34
Name:		texlive-pdfcrop
Version:	1.34
Release:	2
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


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.34-2
+ Revision: 812728
- Update to latest release.

* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.34-1
+ Revision: 805016
- Update to latest release.

* Wed Feb 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.32-3
+ Revision: 772128
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.32-2
+ Revision: 754752
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.32-1
+ Revision: 719216
- texlive-pdfcrop
- texlive-pdfcrop
- texlive-pdfcrop
- texlive-pdfcrop

