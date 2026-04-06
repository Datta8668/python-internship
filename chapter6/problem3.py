p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

msg = input("Enter your comment: ")

if((p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg)):
    print("This comment is spam")
else:
    print("This is not a spam")
