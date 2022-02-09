# Напишите программу Python, которая принимает слово от пользователя и переворачивает его
# Пример: input - Hello Worlds output - sdlroW olleH

word_to_invert = str(input("Input some word to invert: "))
inverted_string = ""
temp_variable = len(word_to_invert)
while temp_variable > 0:
    inverted_string += word_to_invert[temp_variable - 1]
    temp_variable = temp_variable - 1
print(inverted_string)
