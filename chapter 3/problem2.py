letter = '''Dear <|Name|>,
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "Datta").replace("<|Date|>", "05-May-2026"))