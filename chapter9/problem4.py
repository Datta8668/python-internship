word = "Donkey"

with open("4.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "#####")

with open("4.txt", "w") as f:
    f.write(contentNew)

print("datta")