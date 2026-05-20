#Palindromes!
#Your task is to write a program which:
#-asks the user for some text;
#-checks whether the entered text is a palindrome, and prints result.

#take all characters in a provided text
#determine where the halfway point of a sentance is, check one half of the sentance against the other

sentnumb = 0
senttotal = 0
sentance = input('Please enter a potential palindrom here> ')
senlen = len(sentance)

for i in range(len(sentance)):
    if i == senlen:
        break
    if sentance(i) == sentance(senlen):
        senttotal += 1
    senlen -= senlen

if senttotal == (senlen // 2):
    print('This is a palindrom.')
else:
    print('This is not a palindrome.')

