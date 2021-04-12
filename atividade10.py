def exercicio1():
  N = int(input("coloque os valores: "))

  for N in range (int(N)):
    if N %  5 == 0 and N % 2 != 0:
      print(N)
exercicio1()

\\\\\\\\\\\\\\\\\\\\\\\\

def exercicio2():
 num = int(input("Digite o valor de entradas separado por virgula: "))
 lista = []
 i = 0
 while  i < num:
    lista.append(  input() )
    i += 1 
exercicio2()

\\\\\\\\\\\\\\\\\\\\\\

def exercicio3(lista):
  num_superiores_a_5 = 0
  for elemento in lista:
    if elemento > 5:
      num_superiores_a_5 += 1
  return num_superiores_a_5

#insira na lista aqui:
lista = []
print (exercicio3(lista))

\\\\\\\\\\\\\\\\\\\\\\
def exercicio4():

  while opcao != 'd':
    if opcao == 'a':
      print("PSG")
    elif opcao == 'b':
      print("Bayern")
    else:
      print("Inválido")
    opcao = input()
