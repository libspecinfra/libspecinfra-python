import libspecinfra
import libspecinfra.backend

#backend = libspecinfra.backend.Direct()

backend = libspecinfra.backend.SSH(
    host='ec2-52-25-30-143.us-west-2.compute.amazonaws.com',
    user='ubuntu',
    key_file='/Users/marcy/.ssh/orthros.pem',
    port=22)
specinfra = libspecinfra.Specinfra(backend)
f = specinfra.file('/etc/passwd')

#print(oct(f.mode())) # => 0o6441
print(oct(f.mode()))
