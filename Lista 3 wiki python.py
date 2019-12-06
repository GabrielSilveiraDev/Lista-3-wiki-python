#Lista 3 wiki python

#Exercício 1:


""
while True:

    nota = float(input('Digite uma nota entre 0 a 10: '))
    if 0 <= nota <= 10:
        print(f'A nota digitada foi {nota}.')
        break

""

#Exercício 2:


while True:

    user = str(input('Digite seu nome de usuário: '))
    senha = str(input('Digite sua senha (diferente do nome do usuário): '))

    if user.upper() != senha.upper():
        break

""


#Exercício 3:


while True:

    nome = str(input('Digite seu nome: '))

    if len(nome) >= 3:

        break

while True:

    idade = int(input('Digite sua idade (0 até 150) '))

    if 0 <= idade <= 150:

        break

while True:

    salario = float(input('Digite seu salário: '))

    if salario > 0:

        break

while True:

    sexo = str(input('Digite seu sexo (f para feminino, m para masculino): '))

    if sexo.upper() == 'F':

        sexo = 'Feminino'

        break

    elif sexo.upper() == 'M':

        sexo = 'Masculino'

        break

while True:

    estado = str(input('Digite seu estado civil (s para solteiro, c para casado, v para viúvo, d para divorciado): '))

    if estado.upper() == 'V':

        estado = 'Viuvo'

        break

    elif estado.upper() == 'S':

        estado = 'Solteiro'

        break

    elif estado.upper() == 'C':

        estado = 'Casado'

        break

    elif estado.upper() == 'D':

        estado = 'Divorciado'

        break


print(f'Nome: {nome}\nIdade: {idade}\nSalário: R$ {salario}\nSexo: {sexo}\nEstado civil: {estado}')

""


#Exercício 4 e 5:


anos = 0

while True:

    popA = int(input('Digite a população do país A (precisa ser menor do que a do país B): '))
    popB = int(input('Digite a população do país B (precisa ser maior do que a do país A: '))

    if popA < popB:

        break

while True:

    txA = float(input('Digite a taxa de crescimento do país A (precisa ser maior do que a do país B): '))
    txB = float(input('Digite a taxa de crescimento do país B (precisa ser menor do que a do país A): '))

    if txA > txB:

        break

while True:

    popA += (txA/100)*popA
    popB += (txB/100)*popB
    anos += 1

    if popA >= popB:

        break

print(f'A população final do país A foi de {popA}\nA população final do país B foi de {popB}\nLevaram {anos} anos para isso acontecer.')

""


#Exercício 6:

for num in range(20):
    print(f'{num}', end=" ")
print()

""


#Exercício 7 e 8:

quantidade = int(input('Digite quantos números você quer digitar: '))
maiornum = 0
soma = 0

for i in range(quantidade):

    num = float(input(f'Digite o {i+1}º número: '))

    if i == 0:

        maiornum = num
        soma += num

    else:

        soma += num
        if num > maiornum:
            maiornum = num

print(f'O maior número foi: {maiornum}\nA soma foi: {soma}\nA média foi: {soma/quantidade}')


""


#Exercício 9:



while True:

    tamanho = int(input('Digite até que número você quer? ( o programa ira escrever os números impares ou pares de 0 até o o numero digitado ): '))

    if tamanho > 0:
        break

while True:

    paridade = str(input('Digite ''p'' para par ou ''i'' para impar: '))

    if paridade.upper() == 'I':

        for num in range(tamanho+1):

            if num % 2 != 0:

                print(f'{num}',end=" ")

        break

    elif paridade.upper() == 'P':

        for num in range(tamanho + 1):

            if num % 2 == 0:
                print(f'{num}', end=" ")

        break
print()

""


#Exercício 10 e 11:


num1 = int(input('Digite o primeiro número do intervalo: '))
num2 = int(input('Digite o segundo número do intervalo: '))
soma = 0

for i in range(num1,num2+1):

    soma += i

    print(f'{i}',end=" ")
print(f'\n{soma}')


""

#Exercício 12


num1 = int(input('Digite de qual número você quer a tabuada: '))
num2 = int(input('Digite até qual número você quer que a tabuada chegue: '))

print(f'Tabuada de {num1}:')

for i in range(1,num2+1):

    print(f'{num1} X {i} = {num1*i}')



""


#Exercício 13:

base = float(input('Digite a base da sua potência: '))
expoente = float(input('Digite o expoente da sua potência: '))

print(base**expoente)


""


#Exercício 14:

par = 0
impar = 0

for i in range (10):

    num = int(input(f'Digite o {i+1}º número: '))

    if int(num)%2 == 0:

        par += 1

    else:

        impar += 1

print(f'Sua lista de 10 números possui {par} valores pares e {impar} valores impares.')


""


#Exercício 15:

n = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1


if (n == 1) or (n == 2):

    print("1")

else:
    count = 3

    while count <= n:

        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1

    print( termo )


""


#Exercício 17:

num = int(input('Digite um número para saber seu fatorial: '))
fatorial = 1

for i in range(num  ,1 ,-1):

        fatorial *= i

print(fatorial)


""


#Exercício 18 e 19:

menornum = 1000
maiornum = 0

quantidade = int(input('Digite quantos números você vai digitar: '))

for i in range (quantidade):

    num = int(input(f'Digite o {i+1} número: '))

    if num < 1000:

        soma += num
        if num < menornum:

            menornum = num

        if num > maiornum:

            maiornum = num

print(f'A soma é: {soma}\nMenor valor: {menornum}\nMaior valor: {maiornum}')


""

#Exercício 21 e 22:

primo = int(input('Digite um número para saber se ele é primo: '))
cont = 0

for i in range(1, primo+1):

    if primo % i == 0 and i != primo and i != 1:

        if cont == 0:

            print('O número não é primo pois é divisível por: ')

        print(f'{i}',end=' ')
        cont += 1

if cont == 0:

    print(f'O número {primo} é primo.')




""

#Exercício 23:

num = int(input('Digite um número para ver os primos no intervalo entre 1 até ele: '))

cont = 0
conttotal = 0
contprimo = 0
primo = False

for i in range(1, num + 1):

    cont = 0
    contprimo = 0

    for j in range(1, num + 1):

        if j > i / 2:
            break

        cont += 1

        if i % j == 0:
            contprimo += 1

    if contprimo == 1:

        primo = True


    else:

        primo = False

    conttotal += cont

    if primo:

        print(f'\nO número {i} é primo, e foram feitas {cont} divisões para descobrir isso.')

    else:

        print(f'\nO número {i} não é primo, e foram feitas {cont} divisões para descobrir isso.')

print(f'\nNo total foram feitas {conttotal} divisões. ')



""

#Exercicio 24:

n = int(input('Digite quantas notas serão digitas: '))

media = 0

for i in range(n):

    nota = float(input(f'Digite a {i+1}º nota: '))
    media += nota/n

print(media)


""


#Exercício 25:

n = int(input('Quantas idades serão digitadas? '))

media = 0

for i in range(n):

    idade = int(input(f'Digite a {i+1} idade '))
    media += idade/n

if media >= 60:
    print(f'Turma idosa, média de idade {media}')

if 26 <= media < 60:
    print(f'Turma adulta, média de idade {media}')

if media < 26:
    print(f'Turma jovem, média de idade {media}')



""


#Exercício 26:


eleitores = int(input('Digite o número de eleitores: '))
candidatoA = 0
candidatoB = 0
candidatoC = 0

for i in range (eleitores):

    while True:

        votos = str(input(f'Digite o voto do {i+1}º eleitor: '))

        if votos.upper() == 'A':

            candidatoA += 1
            break

        elif votos.upper() == 'B':

            candidatoB += 1
            break

        elif votos.upper() == 'C':

            candidatoC += 1
            break

print(f'Votos do candidato A: {candidatoA}\nVotos do candidato B: {candidatoB}\nVotos do candidato C: {candidatoC}')


""

#Exercício 27:

turmas = int(input('Digite quantas turmas possui a escola: '))
media = 0

for i in range (turmas):

    alunos = int(input(f'Digite quantos alunos possui a {i+1}º turma: '))
    media += alunos/turmas

print(media)


""


#Exercício 28:

cds = int(input('Digite quantos CDs o usuário possui: '))
soma = 0

for i in range(cds):

    soma += float(input(f'Digite o preço do {i+1}º CD: '))

print(soma, soma/cds)



""


#Exercício 29:

soma = 0

for i in range(50):

    soma += 1.99
    print(f'{i+1} - R$ {round(soma,2)}')



#Exercício 30:

soma = 0

for i in range(50):
    soma += 0.18
    print(f'{i+1} - R$ {round(soma,2)}')


""



#Exercício 31:

soma = 0
o = 1
print('Quando quiser sair do programa, digite ''S''')

while True:

    produto = str(input(f'Digite o valor do {o}º produto: '))

    if produto.upper() == 'S':
        break

    soma += int(produto)
    print(f'Produto {o}: R$ {produto} ')

    o += 1

dinheiro = float(input('Digite quanto dinheiro o cliente deu: '))

print(f'Total: R$ {soma}\nDinheiro: R$ {dinheiro}\nTroco: R$ {dinheiro - soma}')


""

#Exercício 32:

num = int(input('Digite um número para saber seu fatorial: '))
fatorial = 1

for i in range (num,1,-1):

    fatorial *= i

    print(f'{i}', end=' . ')

print('1 = 'f'{fatorial}')



""


#Exercício 33:

menortemp = 5000
maiortemp = -273
contmedia = 0
soma = 0

while True:

    temp = float(input('Digite o valor da temperatura, ou 0 para sair: '))

    if temp == 0:

        break

    soma += temp
    contmedia += 1

    if temp <= menortemp:

        menortemp = temp

    if temp >= maiortemp:

        maiortemp = temp

print(f'A média é: {soma/contmedia} Cº\nMenor valor: {menortemp} Cº\nMaior valor: {maiortemp} Cº')


""


#Exercício 37:


maisLeve = 1000
maisPesado = 0
maisAlto = 0
maisBaixo = 200
maisLeveCod = 0
maisPesadoCod = 0
maisAltoCod = 0
maisBaixoCod = 0
mediaPeso = 0
mediaAltura = 0
cont = 0

while True:

    codigo = int(input('Digite o código do cliente, ou 0 para sair: '))

    if codigo == 0:
        break

    altura = int(input('Digite a altura do cliente, em cm: '))
    peso = float(input('Digite o peso do cliente, em kg: '))

    cont += 1

    mediaPeso += peso
    mediaAltura += altura

    if altura >= maisAlto:

        maisAlto = altura
        maisAltoCod = codigo

    if altura <= maisBaixo:

        maisBaixo = altura
        maisBaixoCod = codigo

    if peso >= maisPesado:

        maisPesado = peso
        maisPesadoCod = codigo

    if peso <= maisLeve:

        maisLeve = peso
        maisLeveCod = codigo

print(f'A pessoa mais leve foi: {maisLeveCod}, com {maisLeve} Kg\nA pessoa mais pesada foi: {maisPesadoCod}, com {maisPesado} Kg\nA pessoa mais alta foi: {maisAltoCod}, com {maisAlto}Cm'
      f'\nA pessoa mais baixa foi: {maisBaixoCod}, com {maisBaixo}Cm\nA média de altura é de {mediaAltura/cont}Cm\nA media de peso é de {mediaPeso/cont}Kg')


""


#Exercício 38:

salario = float(input('Digite o salário do funcionário: '))
anos = int(input('Digite quantos anos o funcionário continuou trabalhando na empresa: '))

for i in range (0,anos):

    salario += ((2**i)*0.015)*salario

print(f'O salário do funcionário após {anos} anos é de: {salario}')



""


#Exercício 39:

maisAlto = 0
maisBaixo = 300
maisAltoCod = 0
maisBaixoCod = 0

for i in range (10):

    codigo = int(input('Digite o código do aluno: '))
    altura = int(input('Digite a altura do aluno: '))

    if altura >= maisAlto:

        maisAlto = altura
        maisAltoCod = codigo

    if altura <= maisBaixo:

        maisBaixo = altura
        maisBaixoCod = codigo

print(f'O aluno mais baixo é: {maisBaixoCod}, com {maisBaixo}Cm.\nO aluno mais alto é: {maisAltoCod}, com {maisAlto}Cm.')



""


#Exercício 40:


menor = 1000000
maior = -1
codigoMenor = 0
codigoMaior = 0
media = 0
mediaveiculos = 0
cont = 0

for i in range (5):

    cidade = int(input('Digite o código da cidade: '))
    veiculos = int(input('Digite a quantidade de veiculos de passeio:'))
    acidentes = int(input('Digite o número de acidentes de transito com vitmas: '))

    mediaveiculos += veiculos/5

    if acidentes <= menor:

        menor = acidentes
        codigoMenor = cidade

    if acidentes >= maior:

        maior = acidentes
        codigoMaior = cidade

    if veiculos < 2000:

        cont += 1
        media += acidentes

print(f'A média de veículos é de: {mediaveiculos}.\nO maior índice de acidente de trânsito é {maior}, na cidade {codigoMaior}.'
    f'\nO menor índice de acidente de trânsito é {menor}, na cidade {codigoMenor}.'
      f'\nA média de acidentes de trânsito nas cidades com menos de 2000 carros de passeio é de: {media/cont}.')

""

#Exercício 41:


divida = float(input('Digite o valor da dívida: '))
parcelas  = 0
juros = 1.05
print('Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor da Parcela')

while parcelas < 12:

    parcelas += 1

    if parcelas == 1:

        print(f'R$ {divida}     0      1          R$ {divida}')

    elif parcelas % 3 == 0:

        juros += 0.05

        print(f'R$ {round(divida*juros)}   {(round(divida*juros) - divida)}      {parcelas}          R$ {round((divida*juros)/parcelas)}')



""

#Exercício 42:

cont25 = 0
cont50 = 0
cont75 = 0
cont100 = 0

while True:

    num = float(input('Digite um número, um numero negativo  para sair: '))

    if num < 0:

        break

    if 0 <= num <= 25:

        cont25 += 1

    elif 26 <= num <= 50:

        cont50 += 1

    elif 51 <= num <= 75:

        cont75 += 1

    elif 76 <= num <= 100:

        cont100 += 1

print(f'Foram digitados:\n{cont25} números entre 0 e 25\n{cont50} números entre 26 e 50\n{cont75} entre 51 e 75\n{cont100} entre 76 e 100')



""


#Exercício 43:

preco = 0

while True:

    codigo = int(input('Digite o código do item: '))

    if codigo == 100:

        preco += 1.20

    elif codigo == 101:

        preco += 1.30

    elif codigo == 102:

        preco += 1.50

    elif codigo == 103:

        preco += 1.20

    elif codigo == 104:

        preco += 1.30

    elif codigo == 105:

        preco += 1.00

    elif codigo == 0:

        break

print(f'O preço total foi: R$ {preco}')


""

#Exercício 44:

contA = 0
contB = 0
contC = 0
contD = 0
contNulos = 0
contBrancos = 0

while True:

    voto = str(input('Digite o seu voto, ou 0 para sair: '))

    if voto == '0':

        break

    if voto == '1':

        contA += 1

    elif voto == '2':

        contB +=1

    elif voto == '3':

        contC += 1

    elif voto == '4':

        contD += 1

    elif voto == '5':

        contNulos += 1

    elif voto == '6':

        contBrancos += 1

print(f'Lulinha: {contA}\nBonoro: {contB}\nCiro: {contC}\nBoulos: {contB}\nVotos nulos: {contNulos}\nVotos brancos: {contBrancos}\n'
      f'Percentagem de votos nulos sobre o total de votos: {(contNulos/(contA+contB+contC+contD+contNulos+contBrancos))*100}%\nPercentagem de votos brancos sobre o total de votos: {(contBrancos/(contA+contB+contC+contD+contNulos+contBrancos))*100}%')

""


#Exercício 45:

media = 0
maiorNota = 0
menorNota = 10
cont = 0

q1 = 'A'
q2 = 'B'
q3 = 'C'
q4 = 'D'
q5 = 'E'
q6 = 'E'
q7 = 'D'
q8 = 'C'
q9 = 'B'
q10 = 'A'


while True:

    nota = 0

    menu = str(input('Digite 0 se quiser sair: '))

    if menu == '0':

        break

    cont += 1

    for i in range (10):

        respostas = str(input(f'Digite a {i+1}º resposta do aluno: '))

        if i == 0 and respostas.upper() == q1:

            nota += 1

        elif i == 1 and respostas.upper() == q2:

            nota += 1

        elif i == 2 and respostas.upper() == q3:

            nota += 1

        elif i == 3 and respostas.upper() == q4:

            nota += 1

        elif i == 4 and respostas.upper() == q5:

            nota += 1

        elif i == 5 and respostas.upper() == q6:

            nota += 1

        elif i == 6 and respostas.upper() == q7:

            nota += 1

        elif i == 7 and respostas.upper() == q8:

            nota += 1

        elif i == 8 and respostas.upper() == q9:

            nota += 1

        elif i == 9 and respostas.upper() == q10:

            nota += 1


        if i == 9:

            media += nota

        if nota >= maiorNota:

            maiorNota = nota

        if nota <= menorNota:

            menorNota = nota

print(f'A maior quantidade de acertos foi de: {maiorNota}\nA menor quantidade de acertos foi de: {menorNota}\n{cont} Alunos usaram o sistema\nA média de notas da turma foi de: {media/cont}')

""


#Exercício 46:

atleta = str(input('Digite o nome do atleta: '))
saltos = str(input(f'Digite a distância dos saltos do atleta: '))
listaSaltos = saltos.split()

print(f'Primeiro salto: {listaSaltos[0]}m\nSegundo salto: {listaSaltos[1]}m\nTerceiro salto: {listaSaltos[2]}m\nQuarto salto: {listaSaltos[3]}m\nQuinto salto: {listaSaltos[4]}m')

listaSaltos.sort()

print(f'\n{atleta}\nMelhor salto: {listaSaltos[4]}m\nPior salto: {listaSaltos[0]}m\nMédia dos demais saltos: {((float(listaSaltos[1]))+float(listaSaltos[2])+float(listaSaltos[3]))/3}')


""

#Exercício 47:


nome = str(input('Digite o nome do atleta: '))
notas = str(input(f'Digite as notas do atleta: '))
listaNotas = notas.split()

print(f'Nota: {listaNotas[0]}\nNota: {listaNotas[1]}\nNota: {listaNotas[2]}\nNota: {listaNotas[3]}\nNota: {listaNotas[4]}\nNota: {listaNotas[5]}\nNota: {listaNotas[6]}')

listaNotas.sort()

print(f'\nResultado final:\nAtleta: {nome}\nMelhor nota: {listaNotas[6]}\nPior Nota: {listaNotas[0]}'
      f'\nMédia das demais notas: {round((((float(listaNotas[1]))+float(listaNotas[2])+float(listaNotas[3])+float(listaNotas[4])+float(listaNotas[5]))/5), 2)}')



""


#Exercício 48:

numero = input("Digite um número: ")
print("Número invertido: ", numero[:: -1])


""


#Exercício 49:

limite = int(input('Digite o número limite para a série: '))
s = 0

for i in range (limite):

   s += (1+i)/(1+2*i)

print(s)



""

#Exercício 50:


h = 0

limite = int(input('Digite o maximo valor de n: '))

for i in range(1,limite):

    h += (1/i)

print(h)


""