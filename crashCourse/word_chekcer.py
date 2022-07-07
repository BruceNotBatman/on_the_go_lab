letters ='ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvwxyz'
allowed='ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvwxyz 1234567890'

word = input('Enter a word: ')
def checking():
    status = True
    if word[0] not in letters:
        print('Error: first character is a special character')
    else:    
        for ch in word:
            if ch not in allowed:
                status = False
        if status == True:
            print('all characters are letters')
        else:
            print('Error!')

checking()