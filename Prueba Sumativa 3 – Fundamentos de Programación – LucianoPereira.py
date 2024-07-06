import json
def cargar_usuarios_desde_json(ruta_archivo_json):
    with open(ruta_archivo_json, 'r') as archivo_json:
        datos = json.load(archivo_json)
    return datos


def buscar_usuario_por_nombre(datos, nombre):
    try:
        for usuario in datos:
            print(usuario['nombre'] )
            print(nombre)
            if usuario['nombre'] == nombre:
                return usuario
            else:
                print("Usuario no encontrado. Terminando Programa")
    except: 
        print("Error inesperado. Intente nuevamente.")


def guardar_usuario_en_txt(usuario, ruta_archivo_txt):
    
    try:
        with open(ruta_archivo_txt+usuario['nombre']+'.txt', 'w') as archivo_txt:
            archivo_txt.write(f"Nombre: {usuario['nombre']}\n")
            archivo_txt.write(f"Edad: {usuario['edad']}\n")
            archivo_txt.write(f"Email: {usuario['email']}\n")
            print("Guardado exitoso en formato txt.")
    except:
        print("Error al escribir archivo. Intente nuevamente.")


def main(ruta_archivo_json):
    #Lee un archivo JSON y devuelve los datos.
    with open(ruta_archivo_json, 'r') as archivo:
        datos = json.load(archivo)          
    return datos


def main():
    ruta_json = 'C:\\Users\\ssdd\\Downloads\\usuarios.json'
    ruta_txt = 'C:\\Users\\ssdd\\Downloads\\'
    
    datos_estudiantes = cargar_usuarios_desde_json(ruta_json)

    nombre = input("Escriba el nombre del usuario que desea buscar: ")
    usuarioEncontrado =buscar_usuario_por_nombre(datos_estudiantes,nombre)
    guardar_usuario_en_txt(usuarioEncontrado,ruta_txt)

if __name__ == "__main__":
    main()