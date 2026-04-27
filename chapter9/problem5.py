words = ["Donkey", "bad", "ganda"]

with open("4.txt", "r") as f:
    content = f.read()

for word in words:
    contentNew = content.replace(word, "#" * len(word))

with open("4.txt", "w") as f:
    f.write(contentNew)

print("datta")