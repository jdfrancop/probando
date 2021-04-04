for i in "Cadena":
    print(i)
    
dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]

for i in dias:
    print(i)

for i in range(0, 5):
    print(i)

for i in range(len(dias)):
    print(dias[i])
    
print(len(dias))


for i in range(10):
    if i == 4:
        print("Ganaste el sorteo")
    else:
        print("No eres un ganador")
        
for i in range(10):
    for i2 in range(5):
        for i3 in range(3):
            print(i, i2, i3)
            
for i in range(5):
    for i2 in range(3):
        print(i, i2)
        
for i in range(2, 100, 4):
    print(i)