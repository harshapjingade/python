sentence=input("Enter a sentence:").lower()
word_to_find = input("Enter a word from th sentence:").lower()
words = sentence.split()

for i in range(len(words)):
    if word_to_find == words[i]:
        print(i)
