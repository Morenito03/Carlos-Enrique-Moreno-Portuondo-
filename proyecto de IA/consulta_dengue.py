from pyswip import Prolog


nombre = input('Por favor, ingresa tu nombre: ')
fiebre = input('¿Tienes fiebre? (s/n): ')
dolor_cabeza = input('¿Tienes dolor de cabeza? (s/n): ')
dolor_articulaciones = input('¿Tienes dolor en las articulaciones? (s/n): ')
nauseas = input('¿Tienes náuseas? (s/n): ')

prolog = Prolog()
prolog.consult("diagnostico_dengue.pl")

result = bool(list(prolog.query(f"diagnostico_dengue({nombre},{fiebre},{dolor_cabeza},{dolor_articulaciones},{nauseas})")))


print("Tienes dengue" if result else "No tienes dengue")