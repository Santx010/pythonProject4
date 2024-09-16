def calcular_promedio_temperaturas(ciudades_temperaturas):
    """
    Calcula la temperatura promedio de varias ciudades durante un periodo de tiempo.

    Args:
        ciudades_temperaturas (dict): Diccionario donde las claves son las ciudades y los valores
                                      son listas de temperaturas semanales.

    Returns:
        dict: Diccionario con las ciudades y su temperatura promedio.
    """
    promedios = {}

    for ciudad, temperaturas in ciudades_temperaturas.items():
        # Calculamos el promedio de las temperaturas de cada ciudad
        promedio = sum(temperaturas) / len(temperaturas)
        promedios[ciudad] = promedio

    return promedios


# Ejemplo de uso con datos de 3 ciudades y 4 semanas
ciudades_temperaturas = {
    'QUITO': [30, 32, 29, 31],  # Semana 1, 2, 3 y 4
    'LOJA': [25, 27, 26, 28],
    'TENA': [20, 21, 19, 22]
}

promedios = calcular_promedio_temperaturas(ciudades_temperaturas)

for ciudad, promedio in promedios.items():
    print(f"El promedio de temperatura en {ciudad} es {promedio:.2f}°C")
