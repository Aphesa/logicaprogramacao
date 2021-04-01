def calcula_soma(lista):
    lista=[]
    return lista

lista = calcula_soma([])
soma = 0
for i in range(len(lista)):
    soma += lista[i]
print(soma)

def converte_entrada(texto):
  texto= " "
  lista_formatada=(texto.split(" "))
  for num in lista_formatada:
    num=int(num)
    lista_formatada.append(num)
  return lista_formatada
  
def processa_numeros(lista):
  lista = []
  soma = 0
  elementos = len(lista)
  for num in lista:
    soma += num 
  return (soma, elementos)
  
retorno = processa_numeros([])
print(retorno)

def main():
  i=soma_index[1]
  soma=soma_index[0]
  media=soma/i
  return media
lista=converte_entrada (input())
soma_index=processar_numeros(lista)
media=main(lista)
print(media)
