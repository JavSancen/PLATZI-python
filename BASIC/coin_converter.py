pesos = input("¿Cuántos pesos mexicanos tienes?")
pesos = float(pesos)
valor_dolar = 20.04
valor_yuan = 2.85
valor_pesos_colombianos = 0.0045
dolares = pesos / valor_dolar
yuanes = pesos / valor_yuan
pesos_colombianos = pesos / valor_pesos_colombianos
# lo redondeo a 2 y lo grardo denuevo en la variable dolares con "round"
dolares = round(dolares, 2)
yuanes = round(yuanes, 2)
pesos_colombianos = round(pesos_colombianos, 2)

# "str" convierte el valor numero a texto
dolares = str(dolares)
yuanes = str(yuanes)
pesos_colombianos = str(pesos_colombianos)
print("Tienes $" + dolares + " dólares")
print("Tienes $" + yuanes + " yuanes chinos")
print("Tienes $" + pesos_colombianos + " pesos colombianos")
