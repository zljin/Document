import hashlib

m=hashlib.md5()

m.update('hello'.encode('utf8'))

print(m.hexdigest())