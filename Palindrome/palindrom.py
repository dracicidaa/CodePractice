#Palindromes!
#Your task is to write a program which:
#-asks the user for some text;
#-checks whether the entered text is a palindrome, and prints result.

#take all characters in a provided text
#determine where the halfway point of a sentance is, check one half of the sentance against the other

sentlist = []
sentlistBogaloo = []
sentance = input('Please enter a potential palindrom here> ')

for char in sentance:
    sentlist += char
#This got everything into a list
halfid = ((len(sentlist) + 1) // 2) - 1 #This will check for what the half way point is, to the nearest whole number, accounting for the fact that my mental math starts from one, any python starts at 0

sentlistBogaloo = sentlist[halfid::-1]
del sentlist[(halfid + 1):]

if sentlistBogaloo == sentlist:
    print('This is a palindrome')
else:
    print('This is not a palindrome.')