import os
os.system("cls")

VIDRIAGON_POR_SOLDADO = 1
TEMPERATURA_CONGELACION = -15

soldados_inmaculados = int(input("Ingrese la cantidad de soldados inmaculados\n"))
soldados_dothrakis = int(input("Ingrese la cantidad de soldados dothrakis\n"))
dagas_Vidriagón = int(input("Ingrese la cantidad de dagas de Vidriagón\n"))
temperatura_invernalia = float(input("Ingrese la temperatura actual de Invernalia\n"))
Daenerys_dragon = (input("¿Daenerys trajo a sus dragones? (si/no)\n"))

ejercitoTotal = soldados_inmaculados + soldados_dothrakis

vidriagon_necesario = ejercitoTotal * VIDRIAGON_POR_SOLDADO
deficit_armas = vidriagon_necesario - dagas_Vidriagón

if ejercitoTotal >= 20000 and Daenerys_dragon == "si" and dagas_Vidriagón >= vidriagon_necesario:
    print("Victoria Absoluta")

elif ejercitoTotal >= 10000 and Daenerys_dragon == "si" and temperatura_invernalia <= TEMPERATURA_CONGELACION or deficit_armas < 0:
    print(f"Victoria Amarga: Sobrevivimos gracias al fuego de dragón, pero las bajas por el frío y la falta de armas fueron catastróficas. Faltaron {deficit_armas} dagas.")

elif ejercitoTotal < 10000 and Daenerys_dragon == "si" and temperatura_invernalia > TEMPERATURA_CONGELACION:
    print("Retirada Táctica: No somos suficientes, pero los dragones nos dieron tiempo para huir hacia el sur.")

else:
    print("Derrota Total: Invernalia ha caído. Comienza la Larga Noche...")
