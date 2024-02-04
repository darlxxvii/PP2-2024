"""Write a function that accepts string from user, return a sentence with the
 words reversed. We are ready -> ready are We
"""
def treversed(sentence):
    words = sentence.split()
    i = len(words)-1
    while i >= 0:
        print(words[i], end=' ')
        i -= 1

sentence = input('Enter your sentence: ')
treversed(sentence)