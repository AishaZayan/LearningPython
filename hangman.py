import random
#اشكال هانجمان
hangman_stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#الكلمة العشوائيةو الخطوط
words = ["bad" , "smile" , "dog" , "cute" , "king" , "cat" , "love" , "good" , "fish" , "goat" , "meat" , "cake"]
random_word = random.choice(words)
display = ["_"] * len(random_word)
#التزيين و قائمة المحاولات
print(" ".join(display))
lives = 6
#عمل قائمة بالحروف المخمنة
guessed_letters = []
# هل الحرف تم تخمينه قبل ذلك
while "_" in display and lives > 0:
  guessed = input("Please guess a letter: ").lower()
  if guessed in guessed_letters:
    print("You have already guessed that. Try again.")
    print(f"You have {lives} more tries")

    continue
#في حالة لم يسبق تخمينه. ضيفه للقائمة
  guessed_letters.append(guessed)
 #التخمين غلط
  if guessed not in random_word:
    lives -= 1
    print(hangman_stages[6 - lives])
      
# التخمين صح
  else:
    for position in range(len(random_word)):
      if random_word[position] == guessed:
        display[position] = guessed

  print(" ".join(display))
  print(f"You have {lives} more tries ")

#إذا انتهت المحاولات
if lives == 0:
  print("""
        You lose!
        """)
  print(hangman_stages[-1])

#اذا عرف الكلمة
else:
  print("""
      ***********
        YOU WIN!
      ***********
       """)