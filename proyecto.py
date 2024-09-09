estado = "En tránsito"
if estado == "Entregado":
    print("El envío ha sido entregado.")
elif estado == "En tránsito":
    print("El envío está en tránsito.")
else:
    print("Estado del envío desconocido.")

envios = ["Envío 1", "Envío 2", "Envío 3"]
for envio in envios:
    print(f"Procesando {envio}")

for envio in envios:
    if envio == "Envío 2":
        continue  # Saltar "Envío 2"
    print(f"Procesando {envio}")

envios = {
    '123456789': {'Origen': 'Ciudad A', 'Destino': 'Ciudad B', 'Estado': 'En tránsito'},
    '987654321': {'Origen': 'Ciudad B', 'Destino': 'Ciudad C', 'Estado': 'Entregado'}
}

from collections import Counter

estados_envios = ['En tránsito', 'Entregado', 'En tránsito', 'Cancelado']
contador_estados = Counter(estados_envios)
print(contador_estados)  # Output: Counter({'En tránsito': 2, 'Entregado': 1, 'Cancelado': 1})

from datetime import datetime

fecha_entrega_prevista = datetime(2024, 8, 5)
hoy = datetime.now()
dias_restantes = (fecha_entrega_prevista - hoy).days
print(f"Días restantes para la entrega: {dias_restantes}")



import math

# Ejemplo: calcular el costo del envío basado en la distancia (hipotética)
distancia = 100  # distancia en km
costo_por_km = 2.5
costo_total = math.ceil(distancia * costo_por_km)
print(f"Costo total del envío: ${costo_total}")



import random
import string

def generar_numero_seguimiento():
    return ''.join(random.choices(string.digits, k=10))

numero_seguimiento = generar_numero_seguimiento()
print(f"Número de seguimiento generado: {numero_seguimiento}")


