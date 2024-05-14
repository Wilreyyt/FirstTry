string= 'www.my_site.com#about'
string=string.replace("#","/")
print(string)

word=input("Введите слово: ")
newword=word+"ing"
print(newword)

ivan="Ivanou Ivan"
arr=ivan.split()
arr.reverse()
ivan=" ".join(arr)
print(ivan)

string1=input("Введите строку с пробелами в начале и конце:")
string1=string1.strip()
print(string1)

baget="pARiS"
print(baget.title())