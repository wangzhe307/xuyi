import hashlib
def calc_md5(password):
    sha1=hashlib.sha1()
    sha1.update(password.encode('utf-8'))
    print(sha1.hexdigest())
calc_md5('xuyameng')