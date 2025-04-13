import re
from collections import Counter
text = input("Enter a block of text for analysis:")

print("Text Analysis Results:")

print("Total Characters:", len(text))
print("Total Words:", len(text.split()))

spliting = re.split(r'[.!?]+', text)
print("Total Sentences:", len(spliting))

split_it = text.split()
counter_found = Counter(split_it)
most_occur = counter_found.most_common(4)
print("Most Frequent Word:", most_occur)

words = text.split()
average = sum(len(word) for word in words) / len(words)
print("Average Word Length:", average, 'character')

sentences = text.split('.')
average2 = sum(len(sentence) for sentence in sentences) / len(sentences)
print("Average Word Length:", average2, 'words')


