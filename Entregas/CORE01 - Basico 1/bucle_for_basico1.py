#Codifica el ejercicio 1. Básico
print("Ejercicio 1. Básico")
for i in range(1,101):
    print(i)

#Codifica el ejercicio 2. Múltiples de 2
print("Ejercicio 2. Múltiples de 2")
for i in range(2,501,2):
    print(i)

#Codifica el ejercicio 3. Contando Vanilla Ice
print("Ejercicio 3. Contando Vanilla Ice")
for i in range(1,101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)

#Codifica el ejercicio 4. Wow. Número gigante a la vista
print("Ejercicio 4. Wow. Número gigante a la vista")
suma = 0
for i in range(0, 500001, 2):
    suma += i
print(suma)

#Codifica el ejercicio 5. Regrésame al 3
print("Ejercicio 5. Regrésame al 3")
for i in range(2024, 0, -3):
    print(i)

#Codifica el ejercicio 6. Contador dinámico
print("Ejercicio 6. Contador dinámico")
numInicial = 3
numFinal = 10
multiplo = 2

for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)