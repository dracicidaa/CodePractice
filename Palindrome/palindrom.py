#Palindromes!
#Your task is to write a program which:
#-asks the user for some text;
#-checks whether the entered text is a palindrome, and prints result.

#take all characters in a provided text
#determine where the halfway point of a sentance is, check one half of the sentance against the other

sentnumb = 0
senttotal = 0
sentance = input('Please enter a potential palindrom here> ')
sentlett = [char for char in sentance if char.isalpha()]
senlen = len(sentlett) - 1

for i in range(len(sentlett)):
    if i == senlen:
        break
    if sentlett[i] == sentlett[senlen]:
        senttotal += 1
    senlen -= 1

if senttotal == (len(sentlett) // 2):
    print('This is a palindrome.')
else:
    print('this is not a palindrome.')
