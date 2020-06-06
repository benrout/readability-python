import re

# Get text from user
text = input("Text: ")

# Initialise counts
letters = 0
words = 1
sentences = 0

# Loop through each character in the text
for char in text:
    # Check for lowercase and uppercase letters
    if re.search("[a-z]|[A-Z]", char):
        letters += 1
    # Check for spaces
    if re.search(" ", char):
        words += 1
    # Check for end of sentences
    if re.search("\.|\!|\?", char):
        sentences += 1

# Calculate index
index = round(0.0588 * (letters / words) * 100 - 0.296 * (sentences / words) * 100 - 15.8)

# Print Grade level to user
if index < 1:
    print("Before Grade 1")
elif index < 16:
    print(f"Grade {index}")
else:
    print("Grade 16+")