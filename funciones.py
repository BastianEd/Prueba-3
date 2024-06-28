#Librerias
import json


## FUNCIONES

def lectura_json():
    with open("biblioteca.json", mode="r") as archivoJson:
        lectura = json.load(archivoJson)
        for fila in lectura["Categoria"]:
             print(fila)
# lectura_json()

def buscar_categoria():#No me funciono ""I am Sorry Teacher"""
    with open('biblioteca.json', mode="r") as file:
        lectura = json.load(file)
        for fila in lectura["Categoria"]:
            # print(fila["CategoriaID"])
            id_categoria = int(input("Ingrese el id: "))
            if fila["CategoriaID"] == id_categoria:
                print(fila["CategoriaID"])

# buscar_categoria()

def editar_categoria(nombre,id_categoria):
    with open('biblioteca.json', mode="r") as file:
        lectura = json.load(file)
        # id_categoria = int(input("ingrese la id de la categoria que desea modificar: "))
        for categoria in lectura["Categoria"]: 
                if categoria["CategoriaID"] == id_categoria:
                    #Variables que almacenen el nuevo valor para el nombre
                    # nombre = str(input("Ingresa el nuevo nombre: "))
                    #indicar los nuevos parametros en el json
                    categoria["Nombre"]=nombre
        #Escribir de nuevo en el archivo JSON
    with open("biblioteca.json", mode="w") as file:
        json.dump(lectura, file, indent=4) 
# editar_categoria()

def agregar_categoria(nombre):
    with open('biblioteca.json', mode="r") as file:
        lectura = json.load(file)
        print("AGREGAR NUEVA CATEGORIA")
        nuevo_categoria = {
            "CategoriaID": len(lectura["Categoria"]) + 1,
            "Nombre": nombre
        }
    # Agregar el nuevo libro a la lista de libros
        lectura["Categoria"].append(nuevo_categoria)
        # Escribir de nuevo en el archivo JSON ------> SOBREESCRIBIR LOS NUEVOS CAMBIOS
    with open('biblioteca.json', mode="w") as file:
        json.dump(lectura, file, indent=4)
# agregar_categoria()
        
def eliminar_categoria():#FUNCIONANDO, PORFIN 😖
    with open('biblioteca.json', mode="r") as file:
        lector = json.load(file)
        id_input=int(input("Ingresa el id de la categoria a eliminar: "))
        categoria_a_eliminar = None
        for categoria in lector["Categoria"]:
                if categoria["CategoriaID"] == id_input:
                    categoria_a_eliminar = categoria
                    lector["Categoria"].remove(categoria_a_eliminar)
        #Escribir nuevos cambios en el archivo JSON
    with open("biblioteca.json", mode="w") as file:
        json.dump(lector, file, indent=4) 
# eliminar_categoria()













