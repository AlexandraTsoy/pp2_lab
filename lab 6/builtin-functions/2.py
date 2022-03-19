string = input()
print("The number of uppercase letters in string:", sum(1 for c in string if c.isupper()))
print("The number of lowercase letters in string:", sum(1 for c in string if c.islower()))