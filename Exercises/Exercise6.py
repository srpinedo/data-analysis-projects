def contar_pares_impares(num):
  pares = sum(1 for n in num if n % 2 == 0)
  impares = len(num) - pares
  return pares, impares

  lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  pares, impares = contar_pares_impares(lista_num)

  print(f"Números pares: {pares}")
  print(f"Números impares: {impares}")