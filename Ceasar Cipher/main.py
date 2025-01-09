
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position] 
    else: 
      end_text += char # Will keep the additional number/symbol/space in the encoded message 
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
     
  print(f"Here's the {cipher_direction}d result: {end_text}")

#Imports the logo from art.py when the program starts.
from art import logo
print(logo)
#Will allow the user to continue to encode if they wish or close the program when they enter "No" 
should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
 
  shift = shift % 26  #Program continues to work even if the user enters a shift number greater than 26. 
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if result == 'no': 
    should_continue = False
    print("Thank you for using the Caesar Cipher Encoder!")
