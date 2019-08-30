# -*- coding: utf-8 -*-

import hmac, random

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac.new(str.encode(self.key),str.encode(password),digestmod='MD5').hexdigest()

db = {

'michael': User('michael', '123456'),

'bob': User('bob', 'abc999'),

'alice': User('alice', 'alice2008')

}

def login(username, password):

    user = db[username]

    return user.password == hmac.new(str.encode(user.key), str.encode(password),digestmod='MD5').hexdigest()

assert login('michael', '123456')

assert login('bob', 'abc999')

assert login('alice', 'alice2008')

assert not login('michael', '1234567')

assert not login('bob', '123456')

assert not login('alice', 'Alice2008')

print('ok')
