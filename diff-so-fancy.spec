Summary:	Good-lookin' diffs. Actually… nah… The best-lookin' diffs
Name:		diff-so-fancy
Version:	1.4.2
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/so-fancy/diff-so-fancy/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b98082c2c4aca5867c28178368f8475c
URL:		https://github.com/so-fancy/diff-so-fancy
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
diff-so-fancy strives to make your diffs human readable instead of
machine readable. This helps improve code quality and helps you spot
defects faster.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env perl,%{__perl},' diff-so-fancy

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{perl_vendorlib}}

cp -p diff-so-fancy $RPM_BUILD_ROOT%{_bindir}
cp -p lib/DiffHighlight.pm $RPM_BUILD_ROOT%{perl_vendorlib}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md {hacking-and-testing,history,pro-tips}.md
%attr(755,root,root) %{_bindir}/diff-so-fancy
%{perl_vendorlib}/DiffHighlight.pm
