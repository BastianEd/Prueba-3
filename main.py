#Librerias 
import os,time

#Importar funciones del archivo
import funciones as fun
# funciones.buscar_categoria
# funciones.eliminar_categoria
# funciones.editar_categoria

while True:
    print("********************************")
    print("*        MUNDO LIBRO           *")
    print("********************************")
    print("[1]-Mantenedores de Categorias")
    print("[2]-Reportes")
    print("[3]-Salir")
    opc = int(input("ingrese la opcion: "))
    os.system("CLS")
    time.sleep(0.5)
    if opc == 1:
        print("********************************")
        print("*   MANTENEDORES CATEGORIAS    *")
        print("********************************")
        print("[1] - Agregar Categoria")
        print("[2] - Editar Categoria")
        print("[3] - Eliminar Categoria")
        print("[4] - Buscar Categoria")
        print("[5] - Volver")
        opc_mantenedor = int(input("ingrese la opcion: "))
        if opc_mantenedor == 1:
            nombre = input('Ingresa nueva Categoria: ')
            fun.agregar_categoria(nombre)
        if opc_mantenedor == 2:
            id_categoria = int(input("ingrese la id de la categoria que desea modificar: "))
            nombre = str(input("Ingresa el nuevo nombre: "))
            fun.editar_categoria(nombre,id_categoria)
        if opc_mantenedor == 3:
            id_input = int(input("Ingresa el id de la categoria a eliminar:"))
            fun.eliminar_categoria(id_input)
        if opc_mantenedor == 4:
            print("EN MANTEMIENTO EL DE BUSCAR")
            fun.buscar_categoria(id_categoria)


    if opc == 3:
        break
            
            



            