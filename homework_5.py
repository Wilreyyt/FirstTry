"""Homework 5"""

STRING= 'www.my_site.com#about'
STRING=STRING.replace("#", "/")
print(STRING)

word=input("Введите слово: ")
newword=word+"ing"
print(newword)

IVAN= "Ivanou Ivan"
arr=IVAN.split()
arr.reverse()
IVAN= " ".join(arr)
print(IVAN)

string1=input("Введите строку с пробелами в начале и конце:")
string1=string1.strip()
print(string1)

BAGET= "pARiS"
print(BAGET.title())
