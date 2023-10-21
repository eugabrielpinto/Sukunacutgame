
import random as rd

#o excesso de \n abaixo é pra deixar bonitinho

print(    "[SPOILER] Sukuna derrotou Kashimo no Capitulo 238\n")

print("**********************************************************")
print("Tente Advinhar em quantas partes o Sukuna cortou o Kashimo")
print("**********************************************************\n")

rodada = 1
cortes = rd.randint(5,250)
total_tentativas = 0
pontuacao = 100 


print("Qual classe vai escolher? \n \
      Não Feiticeiro (1) \n \
      Feiticeiro Comum (2)\n \
      Feiticeiro Especial (3) \n \
      Maldição (4) \n \
      God (5)\n")

nivel = int(input("Defina seu nivel: "))

while True:
    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 15
    elif (nivel == 3):
        total_tentativas = 10
    elif (nivel == 4):
        total_tentativas = 5
    elif (nivel == 5):
        total_tentativas = 3
    break
else:
    print("\ninválido, escreva novamente entre 1 e 5")

print ("\nVocê tem 100 pontos")
while rodada <= total_tentativas:  
    print("\nTentativa", rodada, "de", total_tentativas)
    print("Sabemos que foram entre 5 a 250 partes")
    nchute = input("Quantos cortes Sukuna realizou: ")
    print("\nVocê digitou", nchute)
    chute = int(nchute)

    if(chute<5 or chute >250):
        print("Sukuna irá te cortar se errar, escolha entre 5 e 250")
        continue
   
   #Esse código garante relação de 5 a 250 em 0 e 100 pontos e que não chegue a negativo
    diferenca = abs(chute - cortes)
    pontuacao -= int((diferenca - 5) * (100 - 0) / (250) + 1)
    pontuacao = max(0, min(100, pontuacao))

    print(f"Sua pontuação atual é {pontuacao}")

    if chute == cortes:
        print("Você acertou, ó Feiticeiro Jujutsu!")
        break
    elif chute < cortes:
        print("Sukuna realizou mais cortes que isso, tente novamente!")
    else:
        print("Sukuna não cortou tanto assim, tente de novo!")

    rodada = rodada + 1
    
if rodada > total_tentativas:
    print("\nVocê esgotou todas as tentativas. Sukuna cortou ", cortes," vezes" "\nFim do jogo!\n")

print("Gostaria de tentar novamente?\n (1)SIM \n (2)NÃO")
retorno = int(input("Digite sua resposta: "))

while True:
    if(retorno == 1):
        import Sukunacutgame
    elif (retorno == 2):
        print("Obrigado por jogar")
        break
    else:
        print("Digite novamente")
        break


