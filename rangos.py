import re

cadena = "abceef ghi" \
         "0123456789-" \
         "los buenos dias de hola con hola que bien"

print(re.findall("[a-d]", cadena))
print("--------------------------------")
print(re.findall("[a-d2-5]", cadena))
print("--------------------------------")
print(re.findall("[^a-d2-5]", cadena))
print("--------------------------------")
print(re.findall("[\d]", cadena))
print("--------------------------------")
print(re.findall("[\w]", cadena))
print("--------------------------------")
print(re.findall("[\s]", cadena))
print("--------------------------------")
print(re.findall("[\W]", cadena))
print("--------------------------------")
print(re.findall("[\D]", cadena))
print("--------------------------------")
print(re.findall("[hola?]", cadena))
print("--------------------------------")
print(re.findall("[.*hola]", cadena))
print("--------------------------------")
print(re.findall("[hola.*]", cadena))
print("--------------------------------")
print(re.findall("[hola]", cadena))