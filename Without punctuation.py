import string
sentence = input("Please type a sentence: ")
new = ""
for x in sentence:
  if x not in string.punctuation:
    new += x
print("\n\n *** Here is the same sentence withour punctuation ***\n\n" , new)