# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.s 
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

# Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

import sys

eng_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet = eng_alphabet * 2
print(alphabet)

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")

def caesar(text, shift, direction):
  new_text = ""
  for letter in text:
    position = alphabet.index(letter)

    if direction == "encode":
      new_position = position + shift
    elif direction == "decode":
      new_position = position - shift

    new_text += alphabet[new_position]
  print(f"The {direction} text is {new_text}")
  return new_text

if __name__ == "__main__":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if direction not in ("decode", "encode"):
    print("Wrong... <= 2048")
    sys.exit()
  # 1. "encode" or "decode" - VALID
  # 2. "anystring"

  text = input("Type your message:\n").lower()
  if len(text) <= 0 or len(text) > 2048:
    print("Wrong...0 > len(text) <= 2048")
    sys.exit()
  
  try:
    shift = int(input("Type the shift number:\n"))
  except:
    print("Wrong")
    sys.exit()
  
  if shift >= len(alphabet) - 1:
    print("Wrong")
    sys.exit()

  result = caesar(text, shift, direction)
