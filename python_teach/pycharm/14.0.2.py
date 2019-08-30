import re
def name_of_email(addr):
    return re.match(r'.*?([\w\s]+)', addr).group(1)
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')