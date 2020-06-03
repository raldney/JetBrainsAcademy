
text = input()
words = text.split()
words_lower = text.lower().split()
prefix = ["https://", "http://", "www."]
for x, z in enumerate(words):
    for y in prefix:
        if y in words_lower[x]:
            print(z)
            break
