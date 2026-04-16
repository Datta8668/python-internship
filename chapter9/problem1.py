f = open("poem.txt")
content = f.read()

if ("twinkle" in content):
    print("The word twinke is present in poem")

else:
    print("The woed is not in poem")

f.close()