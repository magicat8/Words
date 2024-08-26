import time
import math_test

file = open("words.txt", 'r')
open('palindromes.txt', 'w').close()
new_file = open('palindromes.txt', 'a')
line = file.readlines()

for i in range(888888888):
    # time.sleep(1)
    if line[i].strip() == 'zz239klp4t7':
       break 
    print(line[i].strip())
    if math_test.bool_palindrome(line[i].strip()):
        print('true')
        print(f'{math_test.is_palindrome(line[i].strip())} is a palindrome')
        palindrome = math_test.is_palindrome(line[i].strip())
        new_file.write((f'{palindrome}\n'))