import time
def backwordsL():
    # Opens word list to sort through
    file = open("words.txt", 'r')
    # Clears compare.txt word list
    open('compare.txt', 'w').close()
    # Opens reversed word list
    backwords = open('backwords_words.txt', 'r')
    # Opens compare.txt
    comp = open('compare.txt', 'a')
    # Turns words.txt into a list
    line = file.readlines()
    b = backwords.readlines()


    # Selects each word in the list. Can handel files up to 888,888,888 words/lines long
    for i in range(888888888):
        # time.sleep(1)
        # Ends loop if the "password" is detected
        if line[i].strip() == 'zz239klp4t77t4plk932zz':
            break

        print(b[i].strip())
        # Checks if there is a comparison
        if b[i].strip() == line[i].strip():
            print('True')

            # Checks if selected word is a palindrome then returns the palindrome
            print(f'{b[i].strip()} is a a word')
        
            # Assigns the palindrome to a variable
            word = b[i].strip()
            # Adds the palindrome to the palindrome list
            comp.write(f'{word}\n')

backwordsL()