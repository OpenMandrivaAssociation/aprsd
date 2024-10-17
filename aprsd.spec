Name:         aprsd
Summary:      APRS Internet server program
Version:      2.2.5
Release:      %mkrel 1
License:      GPL, Other License(s), see package
Group:        Networking/Other
Url:          https://www.wa4dsy.net/aprs/
Source:       aprsd-2.2.5.tar.bz2
Patch:        aprsd-2.2.5.diff
Patch1:       aprsd-mic-e-pass.patch
Patch2:       aprsd-linuxh.diff
Patch3:       aprsd-2.2.5_for_11.0.diff
Patch4:       validate_fix_iterator.diff


%description
This is an APRS Internet server program.  It acts as a gateway between
the Internet and a local ham VHF APRS packet network. It is interfaced
directly to a TNC via one of the PC serial ports and does not use the
Linux ax25 sockets interface.



Authors:
--------
Dale A. Heatherington <wa4dsy@wa4dsy.radio.org>

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1


%build
./configure --prefix=/usr
make prefix=$RPM_BUILD_ROOT install

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
mv $RPM_BUILD_ROOT/bin/aprsd $RPM_BUILD_ROOT/usr/bin/aprsd
mv $RPM_BUILD_ROOT/bin/aprspass $RPM_BUILD_ROOT/usr/bin/aprspass
rmdir $RPM_BUILD_ROOT/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/aprsd
cp doc/aprsddoc.html $RPM_BUILD_ROOT/usr/share/doc/aprsd/aprsddoc.html
cp doc/ports.html $RPM_BUILD_ROOT/usr/share/doc/aprsd/ports.html
cp doc/q.html $RPM_BUILD_ROOT/usr/share/doc/aprsd/q.html
cp doc/qalgorithm.html $RPM_BUILD_ROOT/usr/share/doc/aprsd/qalgorithm.html
mkdir -p $RPM_BUILD_ROOT/usr/share/aprsd
cp admin/* $RPM_BUILD_ROOT/usr/share/aprsd/

%post

%postun

%files
%defattr(-,root,root)
/usr/bin/aprsd
/usr/bin/aprspass
/usr/share/aprsd/*
%doc doc/aprsddoc.html doc/ports.html doc/q.html doc/qalgorithm.html



