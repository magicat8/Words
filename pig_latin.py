consonants = 'bcdfghjklmnpqrstvwxyz'

def igpa_atinlay(word):
    # Check if the first letter is a vowel
    if word[0] not in consonants:
        return word + 'way'
    
    # Initialize the position of the first vowel
    last = -1
    
    # Iterate over each character in the word
    for i, v in enumerate(word):
        # Check if the character is a vowel
        if v not in consonants:
            last = i
            break
    
    # Rearrange the word assuming there's always a vowel
    word = word[last:] + word[:last] + "ay"
    return word

# Test the function with different words
print(igpa_atinlay('life'))  # Output: apeshay
print(igpa_atinlay('apple'))  # Output: appleway
