# Transposition Cipher Encryption

import pyperclip

def main():
    myMessage = input('Message:')
    myKey = int(input('Key:'))

    ciphertext = encryptMessage(myKey, myMessage)

    print(ciphertext)

    # Copy the encrypted string in ciphertext to the clipboard.
    pyperclip.copy(ciphertext)
    input('')


def encryptMessage(key, message):
    # Each string in ciphertext represents a column in the grid.
    ciphertext = [''] * key

    # Loop through each column in ciphertext.
    for col in range(key):
        pointer = col

        # Keep looping until pointer goes past the length of the message.
        while pointer < len(message):
            # Place the character at pointer in message at the end of the
            # current column in the ciphertext list.
            ciphertext[col] += message[pointer]

            # move pointer over
            pointer += key

    # Convert the ciphertext list into a single string value and return it.
    return ''.join(ciphertext)


# If transpositionEncrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()
