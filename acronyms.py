user_input = input("Enter a phrase: ")
words = user_input.split()
acronym = ""

for word in words:
    acronym += word[0].upper()

print("Acronym:", acronym)
