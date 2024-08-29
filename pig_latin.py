constonance = 'bcdfghjklmnpqrstvwxz'

def igpa_atinlay(word):
    last = None
    for i, v in enumerate(word):
        if v not in constonance:
            last = i - 1 
    if i >= 0:
        word = word[last + 1:] + word[0:last + 1] + "ay"
    else:
        word = word + 'ay' 
    return word
print(igpa_atinlay('shape'))
