n = int(input())
words = []
for x in range(n):
    words.append(str(input()))

for word in words:
    if len(word) <= 10:
        print(word)
    else:
        length = len(word)
        word = word[0] + str(len(word) - 2) + word[length - 1]
        print(word)