def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
    

l = ["Datta", "Raj", "aj", "Krushna", "Ram"]

print(rem(l,"aj"))