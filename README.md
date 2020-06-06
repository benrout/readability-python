# readability-python
A program that computes the approximate grade level needed to comprehend written text using the Coleman-Liau index:
```
index = 0.0588 * L - 0.296 * S - 15.8
```
Where L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.

Example usage:
```
$ ./readability
Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
Grade 3
```
