Sentence = input("Enter a sentence: ").split()
reverse_words = Sentence[::-1]
print(reverse_words)
reverse_sentence = " ".join(reverse_words)
print(f"The reverse sentence is: {reverse_sentence}")