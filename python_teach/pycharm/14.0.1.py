import re
def is_valid_email(addr):


    if re.match(r'.*?@.*?\.com',addr):
        return True
    else:
        return False
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mrbob@example.com')
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')


print('ok')
