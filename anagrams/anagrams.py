#A Sneaky Snakey anagram finder. Compares 2 inputed strings to determine if there is an anagram
inpgram1 = input('Please input the first word in the anagram to check> ')
inpgram2 = input('Please input the second word in the anagram to check> ')
counter = 0

for i in inpgram1:
    for j in inpgram2:
        if i == j:
            counter += 1
            break

if counter == len(inpgram1):
    print('This is an anagram')
else:
    print('this is not an anagram.')
