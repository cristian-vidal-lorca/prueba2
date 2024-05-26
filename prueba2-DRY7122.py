import requests

def obtener_datos_viaje(origen, destino, token):
    url = f"https://graphhopper.com/api/1/route?point={origen}&point={destino}&vehicle=car&locale=es&key={token}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error al obtener los datos de la API:", response.status_code, response.text)
        return None

def calcular_combustible(distancia, rendimiento):
    return distancia / rendimiento

def main():
    token = "9d4da262-a2e0-4bd0-bb39-643fdf000136"  # Reemplaza esto con tu token real
    while True:
        try:
            print("Introduce la ciudad de origen:")
            print("Ejemplo: Santiago")
            ciudad_origen = input("Ciudad de Origen: ").strip().lower()
            
            if ciudad_origen == "santiago":
                origen = "-33.43311464688593,-70.76642861305926"
            else:
                origen = input("Introduce las coordenadas de la ciudad de origen (formato: lat,lon): ")

            print("Introduce la ciudad de destino:")
            print("Ejemplo: Valdivia")
            ciudad_destino = input("Ciudad de Destino: ").strip().lower()
            
            if ciudad_destino == "valdivia":
                destino = "-39.83148203214363,-73.22456872092175"
            else:
                destino = input("Introduce las coordenadas de la ciudad de destino (formato: lat,lon): ")

            rendimiento = float(input("Rendimiento del vehículo (km/l): "))

            datos_viaje = obtener_datos_viaje(origen, destino, token)
            if datos_viaje:
                distancia = datos_viaje['paths'][0]['distance'] / 1000  # Convertir metros a kilómetros
                duracion = datos_viaje['paths'][0]['time'] / 1000  # Convertir milisegundos a segundos
                horas, rem = divmod(duracion, 3600)
                minutos, segundos = divmod(rem, 60)
                combustible = calcular_combustible(distancia, rendimiento)

                print(f"\nNarrativa del viaje:")
                print(f"De {ciudad_origen.capitalize()} a {ciudad_destino.capitalize()}")
                print(f"Distancia: {distancia:.2f} km")
                print(f"Duración: {int(horas)} horas, {int(minutos)} minutos, {int(segundos)} segundos")
                print(f"Combustible requerido: {combustible:.2f} litros\n")

        except ValueError:
            print("Entrada inválida. Por favor, ingresa los datos correctamente.")
        except Exception as e:
            print("Ocurrió un error:", str(e))

        salir = input("Presiona 'q' para salir o cualquier otra tecla para realizar otro cálculo: ")
        if salir.lower() == 'q':
            break

if __name__ == "__main__":
    main()
