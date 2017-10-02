libspecinfra-python
=======

# Description

Python bindings for libspecinfra.

# Requirements

- Python 3
- [libspecinfra](https://github.com/libspecinfra/specinfra) (with rust-lang compiler)

# Installation

```sh
git clone git@github.com:libspecinfra/specinfra.git
git clone git@github.com:libspecinfra/libspecinfra-python.git
cd specinfra
cargo build
cp target/debug/libspecinfra.dylib ../libpecinfra-python/
cd ../libpecinfra-python
python setup.py install
```

**※ Installation from [PyPI](https://pypi.python.org/pypi) will be supported in the future.**

# Sample code

```python
import libspecinfra
import libspecinfra.backend

direct = libspecinfra.backend.Direct()
specinfra = libspecinfra.Specinfra(direct)
f = specinfra.file('/etc/passwd')

print(oct(f.mode())) # => 0o644
```

Development
-----------

-   Source hosted at [GitHub](https://github.com/libspecinfra/libspecinfra-python)
-   Report issues/questions/feature requests on [GitHub
    Issues](https://github.com/libspecinfra/libspecinfra-python/issues)

Pull requests are very welcome! Make sure your patches are well tested.
Ideally create a topic branch for every separate change you make. For
example:

1.  Fork the repo
2.  Create your feature branch (`git checkout -b my-new-feature`)
3.  Commit your changes (`git commit -am 'Added some feature'`)
4.  Push to the branch (`git push origin my-new-feature`)
5.  Create new Pull Request

License
-------

MIT License (see [LICENSE](https://github.com/libspecinfra/libspecinfra-python/blob/master/LICENSE))
