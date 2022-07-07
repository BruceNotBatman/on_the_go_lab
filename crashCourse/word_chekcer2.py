letters ='ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvwxyz'
allowed='ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvwxyz 1234567890'

word = input('Enter a word: ')
def checking(word):
    #this function checks if the word is a valid file name
    status = True
    if word[0] not in letters:
        return (False)
    else:    
        for ch in word:
            if ch not in allowed:
                status = False
        if status == True:
            return(True)
        else:
            return(False)

def renaming(word):
    #this funciton calls checking and if true is returned a new file name is made
    corrected = bool
    while True:
        corrected = checking(word)
        if corrected == True:
            print('No errors found: {text}'.format(text = word))
            break
        else:
            print('string is incorrect')
            word = input('Enter a new file name: ')    
renaming(word)        