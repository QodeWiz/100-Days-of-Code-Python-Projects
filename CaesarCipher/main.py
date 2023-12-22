alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    for letter in text:
        current_index = alphabet.index(letter)
        new_index = current_index + shift
        if new_index > len(alphabet)-1:
            new_index = new_index - len(alphabet)
        encoded_letter = alphabet[new_index]
        encoded_word =+ encoded_letter
    print(f" The encoded text is {''.join(encoded_word)}")


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    encoded_word = []
    for letter in text:
        current_index = alphabet.index(letter)
        new_index = current_index + shift
        if new_index > len(alphabet)-1:
            new_index = new_index - len(alphabet)
        encoded_letter = alphabet[new_index]
        encoded_word.append(encoded_letter)
    print(f"The encoded text is {''.join(encoded_word)}")

#TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#e.g. 
#cipher_text = "mjqqt"
#shift = 5
#plain_text = "hello"
#print output: "The decoded text is hello"
def decrypt(cipher_text, shift_amount):
    decoded_word = []
    for letter in text:
        current_index = alphabet.index(letter)
        new_index = current_index - shift
        if new_index < 0:
            new_index = len(alphabet) + new_index
        decoded_letter = alphabet[new_index]
        decoded_word.append(decoded_letter)
    print(f"The decoded text is {''.join(decoded_word)}")

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
# Then call the correct function based on that 'drection' variable. You should be able to test the code to 
# encrypt *AND* decrypt a message. 
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
