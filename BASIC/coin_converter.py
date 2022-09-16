pesos = input("¿Cuántos pesos mexicanos tienes?")
pesos = float(pesos)
valor_dolar = 20.04
dolares = pesos / valor_dolar
# lo redondeo a 2 y lo grardo denuevo en la variable dolares con "round"
dolares = round(dolares, 2)
# "str" convierte el valor numero a texto
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")

# Pendiente agregar más conversiones en lista con print()