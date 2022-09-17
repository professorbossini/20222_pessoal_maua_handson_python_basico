#Exibe o texto Hello, World
#print ("Hello, World")
# nome = "Rodrigo"
# idade = 20
# print (nome)
# print ("Meu nome é: " + nome)
# print ("Tenho " + str(idade) + " anos.")
# nome = input("Digite seu nome")
# idade = input("Digite a sua idade")
# print("Olá, " + nome + ". Você tem " + idade + " anos.")

# a = int (input ("Digite o primeiro número"))
# b = int (input ("Digite o segundo número"))
# soma = a + b
# #exibe 2+3=5
# print (str(a) + "+" + str(b) + "=" + str(soma))

# nota1 = int (input ("Digite a primeira nota"))
# nota2 = int (input ("Digite a segunda nota"))
# lembre-se de alterar a precedência dos operadores
# media = (nota1 + nota2) / 2
# estrutura de seleção if
# if media >= 6:
#   print ("Parabéns, você está aprovado!")
# else:
#   print ("Você ainda não passou mas pode fazer a prova SUB :)")

# contador = 1
# print(contador)
# #incrementando..
# contador = contador + 1
# print(contador)
# #de novo...
# contador = contador + 1
# print(contador)
# #também pode ser assim
# contador += 1
# print(contador)

# contador = 1
# while contador <= 3:
#   print ("Hello, estruturas de repetição")
#   contador = contador + 1

# digamos que temos três alunos
# contador = 1
# while contador <= 3:
#   nota1 = int(input("Digite a primeira nota"))
#   nota2 = int(input("Digite a segunda nota"))
#   media = (nota1 + nota2) / 2
#   print ("Media desse aluno: " + str(media))
#   contador += 1


#para poder usar o gerador de números
import random
#gera um número aleatório entre 1 e 10
segredo = random.randint(1, 10)
#pega o primeiro palpite do usuário
palpite = int(input("Qual o seu palpite?"))
#ele acabou de tentar uma vez
tentativas = 1
# != diferente (enquanto palpite for diferente de segredo)
while palpite != segredo:

  ###################
  #encaixe o seu if/else aqui
  ###################
  
  # pega outro palpite
  palpite = int(input("Qual o seu palpite?"))
  # mais uma tentativa foi realizada
  tentativas += 1
# chega aqui quando o usuário acertou
print ("Acabou. O segredo era " + str(segredo) + ". Você tentou " + str(tentativas) + " vezes")