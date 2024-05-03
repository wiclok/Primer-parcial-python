productos = [
  {"nombre": "Camiseta", "precio": 20, "cantidad_disponible":100},
  {"nombre": "Pantalon", "precio": 30, "cantidad_disponible": 80},
  {"nombre": "Zapatos", "precio": 50, "cantidad_disponible": 50},
  {"nombre": "Reloj", "precio": 100, "cantidad_disponible": 30},
  {"nombre": "Gorra", "precio": 15, "cantidad_disponible": 120},
  {"nombre": "Bufanda", "precio": 25, "cantidad_disponible": 60},
  {"nombre": "Sudadera", "precio": 40, "cantidad_disponible": 70},
  {"nombre": "Bolsa", "precio": 35, "cantidad_disponible": 90},
  {"nombre": "Chaqueta", "precio": 80, "cantidad_disponible": 40},
  {"nombre": "Gafas de sol", "precio": 45, "cantidad_disponible":25},
  {"nombre": "Calcetines", "precio": 10, "cantidad_disponible":150},
  {"nombre": "Sombrero", "precio": 20, "cantidad_disponible": 55},
  {"nombre": "Pulsera", "precio": 5, "cantidad_disponible": 200},
  {"nombre": "Pendientes", "precio": 15, "cantidad_disponible":180},
  {"nombre": "Cinturón", "precio": 20, "cantidad_disponible":100},
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
  print('Un cliente decide comprar 5 camisetas, 3 zapatos, 5 pantalones, 1 collar y 1 reloj: ')
  for producto in valor_total_por_productos:
    if producto['nombre'] == 'Camiseta':
      subtotal.append(producto['precio'] * 5)
      producto.update({"cantidad_disponible": producto["cantidad_disponible"] - 5})
      producto.update({"valor_total" : producto["precio"] * producto["cantidad_disponible"]})
      print(producto)
    if producto['nombre'] == 'Zapatos':
      subtotal.append(producto['precio'] * 3)
      producto.update({"cantidad_disponible": producto["cantidad_disponible"] - 3})
      producto.update({"valor_total" : producto["precio"] * producto["cantidad_disponible"]})
      print(producto)
    if producto['nombre'] == 'Pantalon':
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
  

def ejecutar_programa():
  
  valor_total_por_producto = calcular_valor_de_inventario_por_producto(productos)
  print('')
  print('Valor total por producto agregado:')
  print(valor_total_por_producto)
  print('')
  simulacion_de_ventas(valor_total_por_producto)
  
if __name__ == '__main__':
    ejecutar_programa()