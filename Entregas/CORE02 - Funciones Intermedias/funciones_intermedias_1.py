matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# 1. Actualizar valores en diccionarios y listas

matriz[1][0] = 6
print(matriz)
cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes)
ciudades["México"][2] = "Monterrey"
print(ciudades)
coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)

# 2. Iterar a través de una lista de diccionarios

def iterarDiccionario(lista):
    for i in range(len(lista)):
        print("nombre -", lista[i]["nombre"], ", pais -", lista[i]["pais"])

# 3. Obtener valores de una lista de diccionarios

def iterarDiccionario2(llave, lista):
    for i in range(len(lista)):
        print(lista[i][llave])

# 4. Iterar a través de un diccionario con valores de lista

def imprimirInformacion(diccionario):
    for clave in diccionario:
        print(len(diccionario[clave]), clave.upper())
        
        for i in range(len(diccionario[clave])):
            print(diccionario[clave][i])
        print("")
