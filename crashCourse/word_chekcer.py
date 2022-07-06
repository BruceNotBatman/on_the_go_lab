letters ='ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvwxyz'
status = True
word = input('Enter a word: ')

for ch in word:
    if ch not in letters:
        status = False
if status == True:
    print('all characters are letters')
else:
    print('Error!')