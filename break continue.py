for i in range(10):
    if i == 4:
        break
    print(i)

print("----------")

for i in range(10):
    print(i)
    if i == 4:
        break
    
print("----------")

for i in range(10):
    if i == 4:
        continue
    print(i)
    

print("----------")

dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]
for i in dias:
    if i == "martes":
        continue
    print(i)
    
print("----------")

for i in dias:
    if i == "martes":
        break
    print(i)
    