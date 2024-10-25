hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}



# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None


def hexToDec(hexNum):
   
    for i in hexNum:

        if  i not in hexNumbers:
            print("There is an error in your HEX")
            return None
    
    else:        
        totalhex = 0
        #print(len(hexNum))
        place  = 1 * (16**(len(hexNum)-1))
        #print(place)

        for i in range(len(hexNum)):
            hexvalue = hexNumbers[hexNum[i]] * place
            #print(hexvalue)
            totalhex = totalhex + hexvalue
            place = round (place / 16)
            #print(place)
        
        return totalhex


hexToDec("AAA")
