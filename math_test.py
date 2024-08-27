def is_palindrome(s):
    if s == s[::-1]:
        return s
    
def bool_palindrome(s):
    return s == s[::-1]

def dev_controles():
    file = open("words.txt", 'a')
    file.write('\nzz239klp4t7')
    file.close()
