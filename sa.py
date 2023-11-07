print('Welcome to my computer quiz ')

playng = input("Do you want to play? ")

if playng == "sim":
    quit()

print("okay! Lets play :)")
score = 0
answer = input("Qual é a tradução para a palavra since para o inglÊs? ")
if answer == "desde":
    print('correto!')
    score += 1
else:
    print('incorreto!')

answer = input("Qual é a tradução para a palavra once para o inglÊs ")
if answer == "uma vez":
    print('correto!')
    score += 1
else:
    print('incorreto!')

answer = input("Qual é a tradução para a palavra almost para o ingles? ")
if answer == "quase":
    print('correto!')
    score += 1
else:
    print('incorreto!')

answer = input("Qual é a tradução para a palavra however para o ingles? ")
if answer == "no entanto":
    print('correto!')
    score += 1
else:
    print('incorreto!')


answer = input("Qual é a tradução para a palavra mean para o ingles? ")
if answer == "média" or "significado":
    print('correto!')
    score += 1
else:
    print('incorreto!')

answer = input("Qual é a tradução para a palavra between para o ingles? ")
if answer == "entre":
    print('correto!')
    score += 1
else:
    print('incorreto!')

answer = input("Qual é a tradução para a palavra show  para o ingles? ")
if answer == "mostrar":
    print('correto!')
    score += 1
else:
    print('incorreto!')

print("you got " + str(score) + " questions correct")