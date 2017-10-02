import ctypes
import libspecinfra

from libspecinfra.structures import SpecinfraS, FileS


class File(object):

    def __init__(self, specinfra, path):
        lib = libspecinfra.load()
        lib.specinfra_file.argtypes = (ctypes.POINTER(SpecinfraS), ctypes.c_char_p,)
        lib.specinfra_file.restype = ctypes.POINTER(FileS)
        lib.resource_file_mode.argtypes = (ctypes.POINTER(FileS),)
        lib.resource_file_mode.restype = ctypes.c_uint
        self.lib = lib
        self.obj = lib.specinfra_file(specinfra, path.encode('utf-8'))

    def mode(self):
        return self.lib.resource_file_mode(self.obj)
