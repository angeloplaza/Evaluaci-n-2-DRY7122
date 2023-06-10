import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "OQVbEHaDIPapGFMW0HUoRH0jKcJVx5Kt"

while True:
    orig = input("Ingrese ciudad de origen (o 'q' para salir): ")
    if orig.lower() == "q":
        break

    dest = input("Ingrese ciudad de destino (o 'q' para salir): ")
    if dest.lower() == "q":
        break

    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    json_data = requests.get(url).json()

    print("URL: " + url)

    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Dirección desde " + orig + " to " + dest)
        print("Duración del viaje:   " + json_data["route"]["formattedTime"])
        print("Kilómetros:           {:.2f}".format(json_data["route"]["distance"] * 1.61))
        
        km_por_litro = 10  # Rendimiento de combustible del vehículo en kilómetros por litro
        litros_combustible = json_data["route"]["distance"] * 1.61 / km_por_litro
        print("Combustible requerido: {:.2f} litros".format(litros_combustible))
        
        print("=============================================")

        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print(each["narrative"] + " ({:.2f} km)".format(each["distance"] * 1.61))

        print("=============================================\n")
