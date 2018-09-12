"""
libspecinfra-python
----
Python bindings for libspecinfra
"""

__version__ = '0.0.1'

import sys
import ctypes
import os
import libspecinfra.resource

from libspecinfra.structures import SpecinfraS, BackendWrapperS

library = None

def load():
    global library

    if library is None:
        libdir = os.path.dirname(os.path.abspath(__file__))
        prefix = {'win32': ''}.get(sys.platform, 'lib')
        extension = {'darwin': '.dylib', 'win32': '.dll'}.get(sys.platform, '.so')
        libpath = os.path.join(libdir, '{}specinfra{}'.format(prefix, extension))
        library = ctypes.cdll.LoadLibrary(libpath)

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
