import sqlite3

#  Inicializamos la base de datos
conn = sqlite3.connect('diccionario.db')
cur = conn.cursor()

try:
    cur.execute("""CREATE TABLE diccionario (
            palabra text,
            significado text
            )""")
    conn.commit()
except:
    None


def inicio():
    menu()

def menu():
    print("Elija una opcion: "
          "\n1- Agregar palabra"
          "\n2- Editar palabra"
          "\n3- Eliminar palabra"
          "\n4- Ver listado de palabras"
          "\n5- Buscar significado de palabras"
          "\n6- Salir")

    opcion = int(input("Opcion: "))

    if opcion == 1:
        Agregar_Palabra()
    elif opcion == 2:
        Editar_Palabra()
    elif opcion == 3:
        Eliminar_Palabra()
    elif opcion == 4:
        Ver_Palabras()
    elif opcion == 5:
        Buscar_Palabra()
    elif opcion == 6:
        conn.close()
        exit()
    else:
        print("Ingrese valores enteros del 1 al 5.")
        inicio()


def Agregar_Palabra():
    palabra = input("Ingrese palabra: ")
    significado = input("Ingrese significado: ")
    cur.execute("INSERT INTO diccionario VALUES(?,?)", (palabra, significado))
    conn.commit()
    menu()

def Editar_Palabra():
    palabra = input("Ingrese palabra: ")
    print("Que desea editar?\n1-Palabra\n2-Significado")
    opc = int(input("Opcion: "))
    if opc == 1:
        palabra1 = input("Ingrese nueva palabra: ")
        cur.execute("UPDATE diccionario SET palabra = ? WHERE palabra = ?", (palabra1, palabra))
        conn.commit()
        menu()
    elif opc == 2:
        significado1 = input("Ingrese nuevo significado: ")
        cur.execute("UPDATE diccionario SET significado = ? WHERE palabra = ?", (significado1, palabra))
        conn.commit()
        menu()
    else:
        print("Ingrese solo valores numericos del 1 al 2.")
        Editar_Palabra()
    menu()

def Eliminar_Palabra():
    palabra = input("Ingrese palabra a eliminar: ")
    cur.execute("DELETE FROM diccionario WHERE palabra = ?", [palabra])
    conn.commit()
    menu()

def Ver_Palabras():
    cur.execute("SELECT * FROM diccionario")
    print(cur.fetchall())
    menu()

def Buscar_Palabra():
    palabra = input("Ingrese palabra a buscar: ")
    cur.execute("SELECT palabra, significado FROM diccionario WHERE palabra = ?", [palabra])
    print(cur.fetchone())
    menu()

inicio()