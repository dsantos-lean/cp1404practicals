"""
Word Occurrences
Estimate: 25 minutes
Actual:   40 minutes
"""
text_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    word_count = text_to_count.get(word, 0)
    text_to_count[word] = word_count + 1
words = list(text_to_count.keys())
words.sort()
max_length = max(len(word) for word in words)
for word in words:
    print(f"{word:{max_length}} : {text_to_count[word]}")
