#I am practicing classes by making a ceaser cipher method!!

class cipher:
    def encode(self, text, shift):
        #Takes input of text, a shift value, and outputs a string
        if not isinstance(text, str):
            raise TypeError("Inputed text must be a string!")
        if shift < 1 or shift > 25:
            raise ValueError("Shift must be between 1 and 25 to correctly work!")
        intext = ''
        temp = 0
        for char in self.text:
            if char.isalnum():
                if char.isupper():
                    temp = ord(char) + self.shift
                    if temp > ord('Z'):
                        temp = ord('A')
                    intext += chr(temp)
                    temp = 0
                    continue
                elif char.islower():
                    temp = ord(char) + self.shift
                    if temp > ord('z'):
                        temp = ord('a')
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
        
        intext = ''
        temp = 0

        for char in text:
            if char.isalnum():
                if char.isupper():
                    temp = ord(char) - self.shift
                    if temp < ord('A'):
                        temp = ord('Z')
                    intext += chr(temp)
                    temp = 0
                    continue
                elif char.islower():
                    temp = ord(char) - self.shift
                    if temp < ord('a'):
                        temp = ord('z')
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

