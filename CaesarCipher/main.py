alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1
  for letter in start_text:
    current_index = alphabet.index(letter)
    new_index = current_index + shift_amount
    if new_index > len(alphabet)-1:
        new_index = new_index - len(alphabet)
    if new_index < 0:
            new_index = len(alphabet) + new_index
    end_text += alphabet[new_index]
  print(f"Here's the {direction}d result: {end_text}")


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)