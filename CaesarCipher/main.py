alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    encoded_word = []
    for letter in text:
        current_index = alphabet.index(letter)
        new_index = current_index + shift
        if new_index > len(alphabet)-1:
            new_index = new_index - len(alphabet)
        encoded_letter = alphabet[new_index]
        encoded_word.append(encoded_letter)
    print(''.join(encoded_word))

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(text, shift)
