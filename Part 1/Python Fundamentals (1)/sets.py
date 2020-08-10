numbers = {1, 2, 3, 3, 3, 3}
letters = {"a", "b", "c", "a", "a", "a", "a"}
words = set(["the", "cheese", "is", "good", "good", "good", "good"])

print(numbers)
print(letters)
print(words)

# Operations

# result = letters - {"a"}
# print(result)

# Get an Element or Slice

words_len = len(words)
print(words_len)

# Membership

word_list = dict.fromkeys(words, 1)
print(word_list)
has_the = "the" in word_list
print(has_the)
