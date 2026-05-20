#I have to iterate through a string of characters and see if there are based on two inputs

count = 0
haystack = input('Please enter in the random characters to search through> ')
needle = [char for char in input('Please input needle to search for> ')]

for i in needle:
    if haystack.find(i) != -1:
        count += 1

if count == len(needle):
    print('Characters have been found.')
else:
    print('Characters have not been found.')