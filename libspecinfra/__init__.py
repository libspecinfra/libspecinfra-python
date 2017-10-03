"""
libspecinfra-python
----
Python bindings for libspecinfra
"""

__version__ = '0.0.1'

import sys
import ctypes
import libspecinfra.resource

from libspecinfra.structures import SpecinfraS, BackendWrapperS

library = None

def load():
    global library

    if library is None:
        prefix = {'win32': ''}.get(sys.platform, 'lib')
        extension = {'darwin': '.dylib', 'win32': '.dll'}.get(sys.platform, '.so')
        library = ctypes.cdll.LoadLibrary(
            '{}specinfra{}'.format(prefix, extension))

    return library


class Specinfra(object):

    def __init__(self, direct):
        lib = load()
        lib.specinfra_new.argtypes = (ctypes.POINTER(BackendWrapperS),)
        lib.specinfra_new.restype = ctypes.POINTER(SpecinfraS)
        lib.specinfra_free.argtypes = (ctypes.POINTER(SpecinfraS),)
        self.lib = lib
        self.obj = lib.specinfra_new(direct.obj)

    def __exit__(self, exc_type, exc_value, traceback):
        self.lib.specinfra_free(self.obj)

    def file(self, path):
        return libspecinfra.resource.File(self.obj, path)
