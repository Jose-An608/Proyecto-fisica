from modulos import CalculadoraMAS, GraficadorMAS  # Importar las clases desde el paquete

import math  # Importar la librería math para usar funciones matemáticas

def menu_principal():
    while True:
        print("\n--- Calculadora de Movimiento Armónico Simple ---")
        print("1. Calcular parámetros")
        print("2. Calcular variables en un tiempo específico")
        print("3. Graficar desplazamiento")
        print("4. Graficar velocidad")
        print("5. Graficar aceleración")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            calcular_parametros()
        elif opcion == '2':
            calcular_variables()
        elif opcion == '3':
            graficar_desplazamiento()
        elif opcion == '4':
            graficar_velocidad()
        elif opcion == '5':
            graficar_aceleracion()
        elif opcion == '6':
            break
        else:
            print("Opción inválida")

def calcular_parametros():
    print("\nIngrese los datos conocidos:")
    amplitud = float(input("Amplitud (m) [opcional]: ") or 0)
    frecuencia = float(input("Frecuencia (Hz) [opcional]: ") or 0)
    periodo = float(input("Periodo (s) [opcional]: ") or 0)
    
    calculadora = CalculadoraMAS(
        amplitud=amplitud if amplitud > 0 else None,
        frecuencia=frecuencia if frecuencia > 0 else None,
        periodo=periodo if periodo > 0 else None
    )
    
    parametros = calculadora.calcular_parametros()
    
    if parametros:
        print("\nParámetros calculados:")
        for param, valor in parametros.items():
            print(f"{param}: {valor}")
    else:
        print("No se pueden calcular los parámetros. Proporcione más información.")

def calcular_variables():
    amplitud = float(input("Amplitud (m): "))
    periodo = float(input("Periodo (s): "))
    tiempo = float(input("Tiempo (s): "))
    
    omega = 2 * math.pi / periodo
    calculadora = CalculadoraMAS(amplitud=amplitud, periodo=periodo)
    
    variables = calculadora.calcular_variables(tiempo)
    
    if variables:
        print("\nVariables en el tiempo especificado:")
        for var, valor in variables.items():
            print(f"{var}: {valor}")
    else:
        print("No se pueden calcular las variables.")

def graficar_desplazamiento():
    amplitud = float(input("Amplitud (m): "))
    periodo = float(input("Periodo (s): "))
    
    omega = 2 * math.pi / periodo
    GraficadorMAS.graficar_desplazamiento(amplitud, omega)

def graficar_velocidad():
    amplitud = float(input("Amplitud (m): "))
    periodo = float(input("Periodo (s): "))
    
    omega = 2 * math.pi / periodo
    GraficadorMAS.graficar_velocidad(amplitud, omega)

def graficar_aceleracion():
    amplitud = float(input("Amplitud (m): "))
    periodo = float(input("Periodo (s): "))
    
    omega = 2 * math.pi / periodo
    GraficadorMAS.graficar_aceleracion(amplitud, omega)

if __name__ == "__main__":
    menu_principal()