#I am practicing classes by making a ceaser cipher method!!

class cipher:
    def encode(self, text, shift):
        #Takes input of text, a shift value, and outputs a string
        if not isinstance(text, str):
            raise TypeError("Inputed text must be a string!")
        if shift < 1 or shift > 25:
            raise ValueError("Shift must be between 1 and 25 to correctly work!")
        self.text = text
        self.shift = shift
        intext = ''
        temp = 0
        for char in text:
            if char.isalnum():
                if char.islower():
                    temp = ord(char) + shift
                    if temp > ord('z'):
                        temp = ord('a')
                    intext += chr(temp)
                    temp = 0
                    continue
                elif char.isupper():
                    temp = ord(char) + shift
                    if temp > ord('Z'):
                        temp = ord('A')
                    intext += chr(temp)
                    temp = 0
                    continue
                else:
                    intext += str(char)
                    continue
            else:
                intext += str(char)
                continue
        return intext

    def decode(self, text, shift):
        if not isinstance(text, str):
            raise TypeError("Inputed text must be a string!")
        if shift < 1 or shift > 25:
            raise ValueError("Shift must be between 1 and 25 to correctly work!")
        self.text = text
        self.shift = shift

        intext = ''
        temp = 0

        for char in text:
            if char.isalnum():
                if char.islower():
                    temp = ord(char) - shift
                    if temp < ord('a'):
                        temp = ord('z')
                    intext += chr(temp)
                    temp = 0
                    continue
                elif char.isupper():
                    temp = ord(char) - shift
                    if temp < ord('A'):
                        temp = ord('Z')
                    intext += chr(temp)
                    temp = 0
                    continue
                else:
                    intext += str(char)
                    continue
            else:
                intext += str(char)
                continue
            
        return intext





#Program declarations
ceaser = cipher()
running = True
inptext = ''
inpcipher = ''
inpshift = 0
status = 0

while running:
    status = int(input('Please make as selection: 1 for encode, 2 for decode, -1 to exit: '))
    if status == 1:
        try:
            inptext = input('Please enter a string of text to encode: ')
        except Exception:
            print("Error, please enter in a string of characters. Restarting program")
            continue
        try:
            inpshift = int(input('Please enter a number (1 - 25) that you would like as a shift: '))
        except Exception:
            print("Error, please enter an integer between 1 and 25. Restarting program")
            continue
        print('Here is your output: ', ceaser.encode(inptext, inpshift))
    if status == 2:
        try:
            inptext = input('Please enter a string of text to dencode: ')
        except Exception:
            print("Error, please enter in a string of characters. Restarting program")
            continue
        try:
            inpshift = int(input('Please enter a number (1 - 25) that you would like as a shift: '))
        except Exception:
            print("Error, please enter an integer between 1 and 25. Restarting program")
            continue
        print('Here is your output: ', ceaser.decode(inptext, inpshift))
    if status == -1:
        print('Thanks for running the program, have a nice day!')
        running = False