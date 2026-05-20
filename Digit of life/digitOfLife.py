#The digit of life is a digit evaluated using somebodys birthday. Simply sum all digits. If result has more than one digit, continue summation.
#For the time being, I will only allow integer inputs for the dates
#I came up with this super slick single line input, generator. It takes a users input, filters out non numberical characters, and sums it all together

lifeDigits = sum(int(char) for char in input('Pleas input your birthday here using only numbers (04/28/2000 instead of april 28 2000)> ') if char.isalnum())

lifeDigits = sum(int(num) for num in str(lifeDigits))

print('Your life digit is: ', lifeDigits)
