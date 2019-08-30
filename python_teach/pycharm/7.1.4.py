def is_palindrome(n):
    t = ''.join(list(str(n))[::-1])
    if int(t) == n:
        return True
    else:
        return False

print(list(filter(is_palindrome,[12321])))
