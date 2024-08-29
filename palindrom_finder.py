import time
import controle
from backwords import backwordsL

# Opens word list to sort through
file = open("words.txt", 'r')
# Clears palindrome list
open('palindromes.txt', 'w').close()
# Clears reversed word list
open('backwords_words.txt', 'w').close()
# Opens palindrome list
new_file = open('palindromes.txt', 'a')
# Opens reversed word list
b = open('backwords_words.txt', 'a')
# Turns words.txt into a list
line = file.readlines()

# Selects each word in the list. Can handel files up to 888,888,888 words/lines long
for i in range(888888888):
    # Ends loop if the "password" is detected
    if line[i].strip() == 'zz239klp4t77t4plk932zz':
       backwords = line[i].strip()[::-1]
       b.write(f'{backwords}\n')
       break
    backwords = line[i].strip()[::-1]
    b.write(f'{backwords}\n')
    # Prints each word in words.txt
    print(line[i].strip())

    # Checks if selected word is a palindrome
    if controle.bool_palindrome(line[i].strip()):
        print('True')

        # Checks if selected word is a palindrome then returns the palindrome
        print(f'{controle.is_palindrome(line[i].strip())} is a palindrome')
    
        # Assigns the palindrome to a variable
        palindrome = controle.is_palindrome(line[i].strip())
        # Adds the palindrome to the palindrome list
        new_file.write(f'{palindrome}\n')

new_file.close()
b.close()
file.close()

time.sleep(2)
backwordsL()