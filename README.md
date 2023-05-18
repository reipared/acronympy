# Create an acronym from user input

## Code

```python
user_input = input("Enter a phrase: ")
words = user_input.split()
acronym = ""

for word in words:
    acronym += word[0].upper()

print("Acronym:", acronym)
```

## Explanation

The first line of code, `user_input = input("Enter a phrase: ")`,
prompts the user to enter a phrase. The next line of code, `words = user_input.split()`, splits the phrase into a list of words. The third line of code, `acronym = ""`, creates an empty string to store the acronym. The fourth line of code, `for word in words:`, iterates through the list of words. For each word, the fifth line of code, `acronym += word[0].upper()`, adds the first letter of the word to the acronym string. The sixth line of code, `print("Acronym:", acronym)`, prints the acronym to the console.
