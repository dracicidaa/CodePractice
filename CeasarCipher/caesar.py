#Program requirements:
#-asks the user for one line of text to encrypt;
#-asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
#-prints out the encoded text.

#Define what needs to be defined
#Write funcitons
#main loop
#-get user input
#-determine validity
#-encodes text according to user supplied requirements

#Definitions
cipher = ''
text = ''
cipherShift = 0
running = True

#Functions
def encoding(text, cipherShift):
    entext = text
    enshift = cipherShift
    cipher = ''
    for char in entext:
        if char.isalpha():
            code = ord(char) + enshift
            if code > ord('Z'):
                code = ord('A')
            elif code > ord('z'):
                code = ord('a')
            cipher += chr(code)
        else:
            cipher += char
    return cipher

def decoding(cipher, cipherShift):
    encipher = cipher
    enshift = cipherShift
    text = ''
    for char in encipher:
        if char.isalpha():
            code = ord(char) - enshift
            if code < ord('A'):
                code = ord('Z')
            elif code < ord('a'):
                code = ord('z')
            text += chr(code)
        else:
            text += char
    return text


def usrMenu():
    global cipher, text, cipherShift
    try:
        selection = int(input('Are you encoding (1), decoding(2), or quitting(-1)? (1,2,-1 only)> '))
    except Exception:
        print('Error in menu input. Program exiting, goodbye.')
        running = False
    if selection == 1:
        #Encoding
        text = input('Please provide a line of text to encode. > ')
        try:
            cipherShift = int(input('Please provide a shift you would like for the cipher (1 - 25). > '))
        except Exception:
            print('Enter a valid cipher shift. Quitting program.')
            return 4
        if cipherShift <= 25 and cipherShift >= 1:
            print(encoding(text, cipherShift))
        else:
            print('Enter a valid cipher shift. Restarting program.')
            return 1
        return 3

    elif selection == 2:
        #Decoding
        cipher = input('Please input a line of encrypted text. > ')
        try:
            cipherShift = int(input('Please provide the shift used to encrypt this message (1 - 25). > '))
        except Exception:
            print('Enter valid cipher shift. Quitting program.')
            return 4
        if cipherShift <= 25 and cipherShift >=1:
            print(decoding(cipher, cipherShift))
        else:
            print('Enter a valid cipher shift. Restarting program.')
            return 1
        return 3

    elif selection < 0:
        print('Program exiting. Thank you for stopping by!')
        return 2
    
    else:
        print('Menu choice out of bound. Quitting program.')
        return 1


#main body of program
while running:
    status = usrMenu()
    if status == 1:
        print('Input error, restarting.')
        continue
    elif status == 2:
        print('Progam exited gracefully.')
        running = False
    elif status == 3:
        print('Job complete. Restarting')
        continue
    elif status == 4:
        print('Major error. Program exiting.')
        running = False