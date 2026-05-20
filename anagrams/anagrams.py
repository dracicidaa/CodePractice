#A Sneaky Snakey anagram finder. Compares 2 inputed strings to determine if there is an anagram
inpgram1 = input('Please input the first word in the anagram to check> ')
inpgram2 = input('Please input the second word in the anagram to check> ')
counter = 0
gramlist1 = []
gramlist2 = []
for i in inpgram1:
    if i.isalnum():
        gramlist1 += i.upper()

for i in inpgram2:
    if i.isalnum():
        gramlist2 += i.upper()

for i in gramlist1:
    for j in gramlist2:
        if i == j:
            counter += 1
            break
print(gramlist1)
print(gramlist2)

if counter == len(gramlist1):
    print('This is an anagram')
else:
    print('this is not an anagram.')
