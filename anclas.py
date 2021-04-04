import re

lista = [
    "lina - python",
    "camilo - java",
    "cris - php",
    "jose - vue",
    "html - cris"
]

for i in lista:
    if re.findall("cris",i):
        print(i)
print("------------------------------")
for i in lista:
    if re.findall("^cris",i):
        print(i)
print("------------------------------")
for i in lista:
    if re.findall("cris$",i):
        print(i)

