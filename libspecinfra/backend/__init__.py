import ctypes
import libspecinfra
from libspecinfra.structures import BackendWrapperS


class Direct(object):

    def __init__(self):
        lib = libspecinfra.load()
        lib.backend_direct_new.restype = ctypes.POINTER(BackendWrapperS)
        lib.backend_direct_free.argtypes = (ctypes.POINTER(BackendWrapperS),)
        self.obj = lib.backend_direct_new()

    def __exit__(self, exc_type, exc_value, traceback):
        self.lib.backend_direct_free(self.obj)

class SSH(object):

    def __init__(self, host):
        lib = libspecinfra.load()
        lib.backend_ssh_new.argtypes = (ctypes.c_char_p,)
        lib.backend_ssh_new.restype = ctypes.POINTER(BackendWrapperS)
        lib.backend_ssh_free.argtypes = (ctypes.POINTER(BackendWrapperS),)
        self.obj = lib.backend_ssh_new(host.encode('utf-8'))

    def __exit__(self, exc_type, exc_value, traceback):
        self.lib.backend_ssh_free(self.obj)
