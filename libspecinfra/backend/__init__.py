import ctypes
import libspecinfra
from libspecinfra.structures import BackendWrapperS, BackendWrapperS ,SSHBuilderS


class Direct(object):

    def __init__(self):
        lib = libspecinfra.load()
        lib.backend_direct_new.restype = ctypes.POINTER(BackendWrapperS)
        lib.backend_direct_free.argtypes = (ctypes.POINTER(BackendWrapperS),)
        self.obj = lib.backend_direct_new()

    def __exit__(self, exc_type, exc_value, traceback):
        self.lib.backend_direct_free(self.obj)

class SSH(object):

    def __init__(self, host, user=None, password=None, key_file=None, port=None):
        lib = libspecinfra.load()
        ssh_builder_p = ctypes.POINTER(SSHBuilderS)
        lib.backend_ssh_builder_new.argtypes = (ctypes.c_char_p,)
        lib.backend_ssh_builder_new.restype = ssh_builder_p
        ssh_builder = lib.backend_ssh_builder_new(host.encode('utf-8'))

        if user is not None:
            user = user.encode('utf-8')
            lib.backend_ssh_builder_user.argtypes = (ssh_builder_p, ctypes.c_char_p,)
            lib.backend_ssh_builder_user.restype = ssh_builder_p
            ssh_builder = lib.backend_ssh_builder_user(ssh_builder, user)

        if password is not None:
            password = password.encode('utf-8')
            lib.backend_ssh_builder_password.argtypes = (ssh_builder_p, ctypes.c_char_p,)
            lib.backend_ssh_builder_password.restype = ssh_builder_p
            ssh_builder = lib.backend_ssh_builder_password(ssh_builder, password)

        if key_file is not None:
            key_file = key_file.encode('utf-8')
            lib.backend_ssh_builder_key_file.argtypes = (ssh_builder_p, ctypes.c_char_p,)
            lib.backend_ssh_builder_key_file.restype = ssh_builder_p
            ssh_builder = lib.backend_ssh_builder_key_file(ssh_builder, key_file)

        if port is not None:
            lib.backend_ssh_builder_port.argtypes = (ssh_builder_p, ctypes.c_uint32,)
            lib.backend_ssh_builder_port.restype = ssh_builder_p
            ssh_builder = lib.backend_ssh_builder_port(ssh_builder, port)

        lib.backend_ssh_builder_finalize.argtypes = (ssh_builder_p,)
        lib.backend_ssh_builder_finalize.restype = ctypes.POINTER(BackendWrapperS)
        self.obj = lib.backend_ssh_builder_finalize(ssh_builder)

    def __exit__(self, exc_type, exc_value, traceback):
        libspecinfra.load().backend_ssh_builder_free.argtypes = (ctypes.POINTER(SSHBuilderS),)
        self.lib.backend_ssh_free(self.obj)
