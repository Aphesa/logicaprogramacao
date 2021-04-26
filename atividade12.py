#Dadas três variáveis, num1, num2, num3, imprima a maior delas

def maior(*num):
    print('Analisando 3 variáveis passadas...')
    for c in range(0, len(num)):
        print(num[c], end=' ')
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor encontrado foi {max(num)}.')

maior(1, 3, 6,)
#
#Mas como essa aí não está limitada apenas a 3 variáveis, tem essa também:
#
def maior():
  primeiro = int(input('Primeiro numero: '))
  segundo  = int(input('Segundo numero: '))
  terceiro = int(input('Terceiro numero: '))


  maior = primeiro

  if (segundo > maior):
        maior = segundo
  if (terceiro > maior):
        maior = terceiro

  print('Maior: ',maior)
  
#Converta o texto: "Eu sou um aluno feliz" em uma lista de palavras.

texto='Eu sou um aluno feliz'
lista=texto.split(' ')
print(lista)

#Calcule a soma da lista [3,6,3,2,1]

def somando(lista):
    lista=[3,6,3,2,1]
    return lista

lista = calcula_soma([])
soma = 0
for i in range(len(lista)):
    soma += lista[i]
print(soma)

#Converta a lista ["seu", "joao", "esta", "aqui"] em uma frase (separada por espaço)

list = ["seu", "joao", "esta", "aqui"]
boa = ' '.join(map(str, list))
print(boa)

#Utilize a lista lista_numeros = [3,8,9,1,0,2]

#Imprima a lista dos elementos pares dessa lista

lista_numeros = [3,8,9,1,0,2]
print ([numb for numb in lista_numeros if numb % 2 == 0])

#Imprima a soma dos números de no mínimo 4.

lista_numeros = [3,8,9,1,0,2]
print (sum(list(filter(lambda numb: numb >= 4, lista_numeros))))

#Imprima a média dessa lista


print (sum(lista_numeros)/len(lista_numeros))

#Imprima essa lista como números separados por barra vertical. Exemplo: 3|8|9|1|0|2

lista_numeros = [3,8,9,1,0,2]
print ("|".join(list(map(lambda numb: str(numb), lista_numeros))))

#Ordene a lista acima

lista_numeros = [3,8,9,1,0,2]
print (sorted(lista_numeros))

#Ordene a lista acima na ordem decrescente

lista_numeros = [3,8,9,1,0,2
print (sorted(lista_numeros, reverse = True))
                 
#Use a lista lista_numeros = [ 4, 5, 2, 0, 9 ]
                 
#Imprima uma copia da lista
                 
lista_numeros = [ 4, 5, 2, 0, 9 ]
print(lista_numeros[:])
                 
#Imprime a lista dos 3 primeiros elementos dessa lista

lista_numeros = [ 4, 5, 2, 0, 9 ]
print(lista_numero([:3])
  
#Imprima os dois menores valores dessa lista

lista_numeros = [ 4, 5, 2, 0, 9 ]
print(sorted(lista_numeros)[:2])
      
#Imprima os três maiores valores dessa lista

lista_numeros = [ 4, 5, 2, 0, 9 ]
print(sorted(lista_numeros, reverse = true)[:3])
      
#Imprima uma lista de números de 1 a 10

print (list(x+1 for x in range(10)))
      
#Imprima uma lista de números pares de 0 a 20

print(list(x for x in range(21) if x % 2 == 0))    
      
#Imprima uma lista de 20 números aleatórios

print ([randint(1, 100) for x in range(20)])
      
#Converta a lista = ["alo", "Alo", "aLO", alO"] em uma lista de elementos com apenas letras maísculas

print (list(numb.upper() for numb in ["alo", "Alo", "aLO", "alO"]))
      
#Converta a lista = ["alo ", " Alo ", " aLO , " alO"] em uma lista de elementos com apenas letras minúsculas, e sem espaços.

print (list(numb.lower() for numb in ["alo" "Alo" "aLO" "alO"]))
