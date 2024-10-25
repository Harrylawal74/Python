def encodeString(stringVal):
    encodedList = []
    prevChar = stringVal[0]
    count = 0
    for char in stringVal:
        if prevChar != char:
            encodedList.append((prevChar, count))
            count = 0

        count = count + 1
        prevChar = char

    encodedList.append((prevChar, count))
    return encodedList  


def decodeString(encodedList):
    decodedWord = ''

    for values in encodedList:
        decodedWord = decodedWord + (values[0] * values[1])
    return decodedWord
            

encoded = encodeString("ABCDEFT")
print(encoded)

decodeString(encoded)
