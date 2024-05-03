import pandas as pd
import matplotlib.pyplot as plt

productos = [
  {"nombre": "Camisa", "precio": 20, "cantidad_disponible":100},
  {"nombre": "Panta", "precio": 30, "cantidad_disponible": 80},
  {"nombre": "Zapatos", "precio": 50, "cantidad_disponible": 50},
  {"nombre": "Reloj", "precio": 100, "cantidad_disponible": 30},
  {"nombre": "Gorra", "precio": 15, "cantidad_disponible": 120},
  {"nombre": "Bufanda", "precio": 25, "cantidad_disponible": 60},
  {"nombre": "Sudade", "precio": 40, "cantidad_disponible": 70},
  {"nombre": "Bolsa", "precio": 35, "cantidad_disponible": 90},
  {"nombre": "Chaqueta", "precio": 80, "cantidad_disponible": 40},
  {"nombre": "Gafas", "precio": 45, "cantidad_disponible":25},
  {"nombre": "Calcetin", "precio": 10, "cantidad_disponible":150},
  {"nombre": "Sombre", "precio": 20, "cantidad_disponible": 55},
  {"nombre": "Pulsera", "precio": 5, "cantidad_disponible": 200},
  {"nombre": "Pendien", "precio": 15, "cantidad_disponible":180},
  {"nombre": "Cinto", "precio": 20, "cantidad_disponible":100},
  {"nombre": "Vestido", "precio": 60, "cantidad_disponible": 35},
  {"nombre": "Corbata", "precio": 25, "cantidad_disponible": 75},
  {"nombre": "Bolso", "precio": 70, "cantidad_disponible": 45},
  {"nombre": "Paraguas", "precio": 30, "cantidad_disponible": 65},
  {"nombre": "Collar", "precio": 40, "cantidad_disponible": 85},
]

def calcular_valor_de_inventario_por_producto(productos):
  for producto in productos:
    value_total = producto['precio'] * producto['cantidad_disponible']
    producto.update({"valor_total" : value_total})
  return productos

def simulacion_de_ventas(valor_total_por_productos):
  final = 0
  subtotal = []
  print('Un cliente decide comprar 5 Camis, 3 zapatos, 5 Pantes, 1 collar y 1 reloj: ')
  for producto in valor_total_por_productos:
    if producto['nombre'] == 'Cami':
      subtotal.append(producto['precio'] * 5)
      producto.update({"cantidad_disponible": producto["cantidad_disponible"] - 5})
      producto.update({"valor_total" : producto["precio"] * producto["cantidad_disponible"]})
      print(producto)
    if producto['nombre'] == 'Zapatos':
      subtotal.append(producto['precio'] * 3)
      producto.update({"cantidad_disponible": producto["cantidad_disponible"] - 3})
      producto.update({"valor_total" : producto["precio"] * producto["cantidad_disponible"]})
      print(producto)
    if producto['nombre'] == 'Pant':
      subtotal.append(producto['precio'] * 5)
      producto.update({"cantidad_disponible": producto["cantidad_disponible"] - 5})
      producto.update({"valor_total" : producto["precio"] * producto["cantidad_disponible"]})
      print(producto)
    if producto['nombre'] == 'Collar':
      subtotal.append(producto['precio'] * 1)
      producto.update({"cantidad_disponible": producto["cantidad_disponible"] - 1})
      producto.update({"valor_total" : producto["precio"] * producto["cantidad_disponible"]})
      print(producto)
    if producto['nombre'] == 'Reloj':
      subtotal.append(producto['precio'] * 1)
      producto.update({"cantidad_disponible": producto["cantidad_disponible"] - 1})
      producto.update({"valor_total" : producto["precio"] * producto["cantidad_disponible"]})
      print(producto)
  print('')
  print('El stock acutal es de: ')
  print(productos)
  for precio in subtotal:
    final += precio
  print('')
  print('El precio final de la compra fue de: $', final)
  return productos

def generar_DataFrame(stock_actualizado):
  cantidad_de_producto = []
  nombre_de_producto = []
  for cantidad in stock_actualizado:
    cantidad_de_producto.append(cantidad['cantidad_disponible'])
    nombre_de_producto.append(cantidad['nombre'])
  
  df = pd.DataFrame({'Nombre': nombre_de_producto, 'Cantidad disponible': cantidad_de_producto})
  return df

def generar_grafico(DataFrame):
  plt.bar(DataFrame['Nombre'], DataFrame['Cantidad disponible'])
  plt.xlabel('Nombre de producto')
  plt.ylabel('Cantidad disponible')
  plt.title('Analisis de cantidad de productos')
  plt.show()

def ejecutar_programa():
  
  valor_total_por_producto = calcular_valor_de_inventario_por_producto(productos)
  print('')
  print('Valor total por producto agregado:')
  print(valor_total_por_producto)
  print('')
  stock_actualizado = simulacion_de_ventas(valor_total_por_producto)
  print('')
  DataFrame = generar_DataFrame(stock_actualizado)
  print('Data Frame creado con exito:')
  print(DataFrame)
  print('')
  generar_grafico(DataFrame)


if __name__ == '__main__':
  ejecutar_programa()