''' Exercise 1: Creating a user-defined function
    Implementing a Caesar cipher in Python
'''
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
    
    
    
    # alphabet="ABC"


    # x=getDoubleAlphabet(alphabet)
    
    # print(x)

''' Encrypting a message
    Function that equest a message to encrypt from the user.
'''

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

''' Getting a cipher key
'''

def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount
    
''' Encrypting a message
    first lets write an algorithm for encryption as follows

'''
    
    # Take three arguments: the message, the cipherKey, and the alphabet.
    
    # Initialize variables.
    
    # Use a for loop to traverse each letter in the message.
    
    # For a specific letter, find the position.
    
    # For a specific letter, determine the new position given the cipher key.
    
    # If current letter is in the alphabet, append the new letter to the encrypted message.
    
    # If current letter is not in the alphabet, append the current letter.
    
    # Return the encrypted message after exhausting all the letters in the message.


def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage
    

''' Decrypting a message
    we also need to write an algorithm for this code
'''

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

'''
    Creating a main function
    algorithm for creating main func
'''
''' Before you look at the code, plan out your logic:
'''

    
    # Define a string variable to contain the English alphabet.
    
    # To be able to shift letters, double your alphabet string.
    
    # Get a message to encrypt from the user.
    
    # Get a cipher key from the user.
    
    # Encrypt the message.
    
    # Decrypt the message.
    
    
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')
    
runCaesarCipherProgram()