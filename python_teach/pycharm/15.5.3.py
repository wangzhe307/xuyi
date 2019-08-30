db = {}

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')
# -*- coding: utf-8 -*-
import hashlib, random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}
def login(username, password):
    # 数据库中对应用户名的 User类的实例
    user = db[username]
    # 数据库中对应密码加的 salt
    sql_digest_salt = user.salt
    # 数据库中 密码 + salt 生成的 dist
    sqp_digest_password = user.password
    # 待验证的 输入密码 + salt
    data = password + sql_digest_salt
    md5 = hashlib.md5()
    md5.update(data.encode('utf-8'))
    # 待验证的 digest
    enter_digest_password = md5.hexdigest()
    # 对比
    if enter_digest_password == sqp_digest_password:
        return True
    else:
        False
# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')