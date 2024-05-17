"""Homework 6"""

STRING = "Robin Singh"
arr = STRING.split()
print(arr)

LOVE = "I love arrays they are my favorite"
arr1 = LOVE.split()
print(arr1)

LIST = ["Ivan", "Ivanou"]
STRING1, STRING2 = "Minsk", "Belarus"
LIST1 = " ".join(LIST)
print("Привет,", LIST1 + "!", "Добро пожаловать в", STRING1, STRING2)

LIST3 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
STRING3 = " ".join(LIST3)
print(STRING3)

LIST4 = [1, 2, 3, 4, 5, "Hello", "Медоед", "Волк", 10.5, "Степан"]
LIST4[2]= "Скунс"
del LIST4[6]
print(LIST4)

