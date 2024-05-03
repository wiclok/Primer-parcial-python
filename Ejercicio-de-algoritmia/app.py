def capitalizar_palabra(palabra):
  
  if not isinstance(palabra , str):
    raise ValueError('El dato de entrada debe ser un dato tipo string')
  
  if len(palabra) < 1:
    raise ValueError('La palabra debe tener al menos 1 caracter')
  
  return palabra.capitalize()

print(capitalizar_palabra('Hola como estas'))