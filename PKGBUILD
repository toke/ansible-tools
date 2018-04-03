# Maintainer: Thomas Kerpe <thomas@kerpe.net>

pkgname=('python2-ansible-tools-pass-git')
_pkgname=ansible-tools
pkgver=v0.0.8.r1.gf1af41f
pkgrel=1
pkgdesc="pass integration for ansible"
arch=('any')
url='https://github.com/toke/ansible-tools'
license=('custom:MIT')
makedepends=('git' 'python2-setuptools')
options=()
source=('ansible-tools::git+https://github.com/toke/ansible-tools.git')
md5sums=('SKIP')

pkgver() {
  cd "$srcdir/$_pkgname"
  git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build_python2-ansible-tools-git() {
  cd "$srcdir/$_pkgname"
  python2 setup.py build
}

package_python2-ansible-tools-pass-git() {
  depends=('python2')
  cd "$srcdir/$_pkgname"
  make
  python2 setup.py install --root=${pkgdir} --optimize=1
  #install -D -m644 LICENSE ${pkgdir}/usr/share/licenses/python2-ansible-tools-pass-git
}
