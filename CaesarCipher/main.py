from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1

  if shift_amount > len(alphabet) or shift_amount < len(alphabet)*-1:
      shift_amount = shift_amount%len(alphabet)
      print(shift_amount)

  for char in start_text:
      if char in alphabet:
          current_index = alphabet.index(char)
          new_index = current_index + shift_amount
          if new_index > len(alphabet)-1:
              new_index = new_index - len(alphabet)
          if new_index < 0:
              new_index = len(alphabet) + new_index
          end_text += alphabet[new_index]
      else:
          end_text += char
          
    
  print(f"Here's the {direction}d result: {end_text}")

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % len(alphabet)
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")