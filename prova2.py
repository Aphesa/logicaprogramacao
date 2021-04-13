def exercicio1(media):
  list = []
  soma = 0
  while len(list) < 3:
    entrada = int(input("Nota: "))
    list.append(entrada)
  for nota in list:
    soma += nota
  media = soma / len(list)
  return f"Média do aluno é: {media}"

def exercicio2(N):
  list = []
  while len(list) != N:
    entrada = input("Digite qualquer caractere: ")
    list.append(entrada)
  return list

def exercicio3(abzZ):
  entrada = input("Insira a, b, z ou Z: ")
  if (entrada == 'z' or entrada == 'Z'):
    return
  elif (entrada == 'a'):
    print("Globo")
  elif (entrada == 'b'):
    print('SBT')
  else:
    print('Inválido')

def exercicio4(list):
  quantidade_de_medias_inferiores_a_sete = 0
  for media in list:
    if (media < 7):
      quantidade_de_medias_inferiores_a_sete += 1
  if (quantidade_de_medias_inferiores_a_sete < (len(list) * 0.25)):
    return "Professor Coxa"
  else:
    return "Professor Padrão"
