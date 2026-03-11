heroes = [
    {"nombre": "Spider-Man", "universo": "Marvel", "nivel": 85},
    {"nombre": "Iron Man", "universo": "Marvel", "nivel": 90},
    {"nombre": "Batman", "universo": "DC", "nivel": 88},
    {"nombre": "Superman", "universo": "DC", "nivel": 98},
    {"nombre": "Wonder Woman", "universo": "DC", "nivel": 95},
    {"nombre": "Thor", "universo": "Marvel", "nivel": 96},
    {"nombre": "Flash", "universo": "DC", "nivel": 92},
    {"nombre": "Doctor Strange", "universo": "Marvel", "nivel": 94},
    {"nombre": "Black Panther", "universo": "Marvel", "nivel": 89}
]

equipo_seleccionado = []
poder_total = 0
opcion = 0
equimarvel = 0
equipdc = 0

print("--- RECLUTAMIENTO ---")

while opcion != 2:
    print("\n--- MENÚ DE RECLUTAMIENTO ---")
    print("1. Agregar héroe a mi equipo")
    print("2. Salir y mostrar equipo")
    
    try:
        opcion = int(input("\nSelecciona una opción (1 o 2): "))
        
        if opcion == 1:
            print("¿A quién quieres reclutar?")
            
            for i, heroe in enumerate(heroes, start=1):
                print(f"{i}. {heroe['nombre']} ({heroe['universo']})")
            
            indice_heroe = int(input(f"Selecciona el número del héroe (1-{len(heroes)}): "))
            
            if indice_heroe <= len(heroes):
                heroe_elegido = heroes[indice_heroe - 1]
                
                if heroe_elegido["nombre"] in equipo_seleccionado:
                    print(f" {heroe_elegido['nombre']} ya está en tu equipo.")
                else:
                    equipo_seleccionado.append(heroe_elegido["nombre"])
                    poder_total += heroe_elegido["nivel"]
                    
                    if heroe_elegido["universo"] == "Marvel":
                        equimarvel += 1
                    else:
                        equipdc += 1
                    
                    print(f"{heroe_elegido['nombre']} reclutado con éxito.")
            else:
                print(" Número de héroe no válido.")

        elif opcion == 2:
            print("\nFinalizando reclutamiento...")
            
        else:
            print(" Por favor, elige 1 o 2")
            
    except ValueError:
        print("Error: Introduce un número válido.")
        opcion = 0 


print("\n" + "="*30)
print("REPORTE")
print("="*30)

if not equipo_seleccionado:
    print("No reclutaste a ningún héroe.")
else:
    print(f"Has reclutado a {len(equipo_seleccionado)} héroes:")
    
    for i, nombre in enumerate(equipo_seleccionado, start=1):
        print(f"{i}. {nombre}")
    
    print("-" * 30)
    print(f" PODER TOTAL DEL EQUIPO: {poder_total}")
    
    if poder_total >= 400:
        print("¡Aja papi bajale los mejores heroes pa ti!")
    else:
        print("Elegiste los más sonsos")

print("="*30)
print("Número de héroes de Marvel en tu equipo:", equimarvel)
print("Número de héroes de DC en tu equipo:", equipdc)