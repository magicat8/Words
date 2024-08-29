import time
import controle

# Opens word list to sort through
file = open("words.txt", 'r')
# Clears palindrome list
open('palindromes.txt', 'w').close()
# Clears reversed word list
open('backwords_words.txt', 'w').close()
# Clears compare list
open('compare.txt', 'w').close()
# Opens palindrome list
new_file = open('palindromes.txt', 'a')
# Opens reversed word list
b = open('backwords_words.txt', 'a')
# Opens compare list
c = open('compare.txt', 'a')
# Turns words.txt into a list
line = file.readlines()

# Selects each word in the list. Can handel files up to 888,888,888 words/lines long
for i in range(888888888):
    # Ends loop if the "password" is detected
    if line[i].strip() == 'zz239klp4t77t4plk932zz':
       backwords = line[i].strip()[::-1]
       b.write(f'{backwords}\n')
       break
    b.write(f'{backwords}\n')
       break
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
b.close()
b = open('backwords_words.txt', 'r')
b_line = b.readlines()
for z in range(888888888):
    if b_line[z].strip() == 'zz239klp4t77t4plk932zz':
       break

    print(b_line[z].strip())

    if b_line[z].strip() == line[z].strip():
        c.write(f'{b_line[z].strip()}\n')