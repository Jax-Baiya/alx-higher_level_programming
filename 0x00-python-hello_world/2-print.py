#!/usr/bin/python3
print("Programming is like building a multilingual puzzle")


#!/usr/bin/python3
number = 98
print(f"{number} Battery street")

#!/usr/bin/python3
number = 3.14159
print(f"{number:.3}")

#!/usr/bin/python3
str = "Holberton School"
print(len(str))
print(str*4)
print(str[:9])

#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"

print(f"Welcome to {str1} {str2}!")

#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
str3 = str1 + " " + str2
print(f"Welcome to {str3}!")

#!/usr/bin/python3
word = "Holberton"
# Code goes here
word_first_3 = "wor"
word_last_2 = "rd"
middle_word = "or"
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")

    #The above code is wrong as it did not follow the instructions.
    #'word' is a variable for the value "Holberton"

#!/usr/bin/python3
word = "Holberton"
# Code goes here
word_first_3 = word[:-6]
word_last_2 = word[7:]
middle_word = word[-8:8]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
print(len(word))

#!/usr/bin/python
var ="Holberton"

first_3_words = var[3:]
last_2_word = var[-7:]
mid_word = var[1:-1]

print(f"First 3 letters; {first_3_words}")
print(f"Last 2 letters; {last_2_word}")
print(f"Middle word; {mid_word}")
