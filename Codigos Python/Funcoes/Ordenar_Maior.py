def maior_lista(lista):
  lista_maior = max(lista)
  return lista_maior


def ordenar_lista(lista):
  lista.sort()
  return lista


lista = [5, 2, 4, 1, 3]

lista_ordenada = ordenar_lista(lista)
lista_maior = maior_lista(lista)
print(f"Lista ordenada: {lista_ordenada}")
print(f"Maior elemento da lista: {lista_maior}")

