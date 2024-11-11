def lista_de_numeros_pares(lista:list):
    for numero in lista:
        if numero %2 == 0:
            print(numero)

lista_qualquer = []

lista_de_numeros_pares(lista_qualquer)
while  True:
    lista = int(input("digite sua lista de numeros: "))
    if lista == 000:
        break 
    lista_qualquer.append(lista)
