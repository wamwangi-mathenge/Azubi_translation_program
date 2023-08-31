colors = {
    "red": "rot",
    "green": "grun",
    "blue": "blau",
    "yellow": "geib"
}

print(colors)

english1 = input("Input a color: ")
german1 = input("Input its German translation: ")
english2 = input("Input a second color: ")
german2 = input("Input its German translation: ")

colors[english1] = german1
colors[english2] = german2
print(colors)

## Exercise 2
eng_color = input("Which color should be translated? ")

print(f"The German word for {eng_color} is {colors[eng_color]}")