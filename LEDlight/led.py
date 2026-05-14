#Pactice using lists, mulilines, etc to make an "LED" board
#I have no idea how to neatly print multilines rightnext to each other lol

#define stuff
led_states = ['''
###
# #
# #
# #
###''','''
#
#
#
#
#''','''
###
  #
###
#
###''','''
###
  #
###
  #
###''','''
# #
# #
###
  #
  #''','''
###
#
###
  #
###''','''
###
#
###
# #
###''','''
###
  #
  #
  #
  #''','''
###
# #
###
# #
###''','''
###
# #
###
  #
###'''  
]
num0 = led_states[0]
num1 = led_states[1]
num2 = led_states[2]
num3 = led_states[3]
num4 = led_states[4]
num5 = led_states[5]
num6 = led_states[6]
num7 = led_states[7]
num8 = led_states[8]
num9 = led_states[9]

running = True

#Main program body
while running:
    selection = input('\nPlease enter a number, or any negative number to exit program: ')
    try:
        if int(selection) >= 0:
            for i in selection:
                if int(i) == 0:
                    print(num0, end=' ')
                elif int(i) == 1:
                    print(num1, end=' ')
                elif int(i) == 2:
                    print(num2, end=' ')
                elif int(i) == 3:
                    print(num3, end=' ')
                elif int(i) == 4:
                    print(num4, end=' ')
                elif int(i) == 5:
                    print(num5, end=' ')
                elif int(i) == 6:
                    print(num6, end=' ')
                elif int(i) == 7:
                    print(num7, end=' ')
                elif int(i) == 8:
                    print(num8, end=' ')
                else:
                    print(num9, end=' ')
        else:
            print('Good bye!')
            running = False

    except Exception:
        print('Please enter a number!')
        continue
