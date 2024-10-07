import string



def play(message, shift):
  alphabet = string.ascii_lowercase

  encrypted_message = ""

  for letter in message:
    if letter.lower() in alphabet:
      original_position = alphabet.index(letter.lower())
      new_position = (original_position + shift) % 26
      encrypted_letter = alphabet[new_position]
      if letter.isupper():
        encrypted_letter = encrypted_letter.upper()

      encrypted_message += encrypted_letter
    else:
      encrypted_message += letter

  print(encrypted_message)


user_massage = input("Enter a messsage: ")
shift_number = int(input("Enter a shift number:"))

play(message=user_massage, shift=shift_number)