Summary:	Sun Open Look bitmap fonts
Summary(pl.UTF-8):	Fonty bitmapowe Sun Open Look
Name:		xorg-font-font-sun-misc
Version:	1.0.0
Release:	1
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-sun-misc-%{version}.tar.bz2
# Source0-md5:	e17d43a7c6c0d862cfba0908ff132ffa
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
# contains useful aliases for these fonts
Requires:	xorg-font-font-alias >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sun Open Look Cursor and Open Look Glyph bitmap fonts.

%description -l pl.UTF-8
Fonty bitmapowe Sun Open Look Cursor i Open Look Glyph.

%prep
%setup -q -n font-sun-misc-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-fontdir=%{_fontsdir}/misc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc

%postun
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_fontsdir}/misc/olcursor.pcf.gz
%{_fontsdir}/misc/olgl*.pcf.gz
