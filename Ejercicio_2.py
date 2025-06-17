import unicodedata # Importar unicodedata para normalizar caracteres

# La Funcion unicodedata sirve para limpiar tildes y poner en minúsculas
def normalizar(texto):
    texto = texto.lower()
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

print("**** Sistema de Gestión de Calificaciones ****")


asignaturas_validas = [
    "matematicas", "lenguaje", "biologia", "quimica",
    "artes", "filosofia", "historia", "fisica"
]

# Normalizar asignaturas válidas
asignaturas_validas_norm = [normalizar(a) for a in asignaturas_validas]

# Entradas principales
while True:
    try:
        cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
        if cantidad_estudiantes > 0:
            break
        else:
            print("Debe ser mayor que 0.")
    except ValueError:
        print("Debe ingresar un número válido.")

# Listas
nombres = []
promedios = []
estados = []
motivos = []

# Procesar cada estudiante
for i in range(cantidad_estudiantes):
    print(f"\n*** Estudiante {i+1} ***")

    # Validar nombre
    while True:
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        if nombre.replace(" ", "").isalpha():
            break
        else:
            print("Nombre inválido. Solo se permiten letras.")
    nombres.append(nombre)

    # Cantidad de asignaturas
    while True:
        try:
            cantidad_asignaturas = int(input("Ingrese la cantidad de asignaturas: "))
            if cantidad_asignaturas > 0:
                break
            else:
                print("Debe ser mayor que 0.")
        except ValueError:
            print("Entrada inválida.")

    suma_notas = 0
    contador_notas = 0
    asignaturas_ingresadas = []

    for j in range(cantidad_asignaturas):
        while True:
            asignatura = input(f"Ingrese el nombre de la asignatura {j+1}: ").strip()
            asignatura_normalizada = normalizar(asignatura)

            # Validar asignatura
            if asignatura_normalizada not in asignaturas_validas_norm:
                print(f"Asignatura no valida. Opciones: {', '.join(asignaturas_validas)}")
            elif asignatura_normalizada in asignaturas_ingresadas:
                print("Esa asignatura ya fue ingresada. Reintente con otra.")
            else:
                asignaturas_ingresadas.append(asignatura_normalizada)
                break

        # Validar nota
        while True:
            try:
                nota = float(input(f"Ingrese la calificación para {asignatura.title()}: "))
                if 0 <= nota <= 10:
                    suma_notas += nota
                    contador_notas += 1
                    break
                else:
                    print("La calificacion debe estar entre 0 y 10.") #valida la calificacion de 0 a 10
            except ValueError:
                print("Entrada no valida. Debe ser un número.")

    promedio = suma_notas / contador_notas
    promedios.append(promedio)

    # Evaluar estado
    if promedio >= 6.0:
        estados.append("Aprobado")
        motivos.append("Promedio mayor o igual a 6.0")
    else:
        estados.append("Reprobado")
        motivos.append("Promedio menor a 6.0")

# Mostrar resumen
print("\n ****** RESUMEN FINAL ******")
for i in range(cantidad_estudiantes):
    print(f"Estudiante: {nombres[i]}")
    print(f"  Promedio: {round(promedios[i], 2)}")
    print(f"  Estado: {estados[i]}")
    print(f"  Motivo: {motivos[i]}")
    print("-" * 30)
