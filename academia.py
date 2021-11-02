
# Criando a class onde guardaremos as informações 
class alunos: 
    def __init__(self, codigo, nome, altura, peso): 
        self.codigo = codigo 
        self.nome = nome 
        self.altura = altura
        self.peso = peso

# criando uma lista       
list = [] 

# criando as variaves que serão usadas no processo  
loopPrincipal = "continuar"
loopControl = "continuar"
codigoAluno = 0
nomeAluno = ""
pesoAluno = 0.0
alturaAluno = 0.0

# funcao para validar campo float

def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False   


# loop do CODIGO ==> digitar 0(zero) para encerrar o loop e sair

while loopPrincipal == "continuar":  

# loop do CODIGO 

    while loopControl == "continuar":
        codigoAluno = input('\nPor favor, digite seu CÓDIGO ==> ')
        
        if codigoAluno.isdigit()== False:
            print("Por favor, digite um número Inteiro VÁLIDO! ")
        else:
            loopControl = "Sair"    

    # Executa saida do programa em caso do código digitado ser 0(zero)
    if (int(codigoAluno) == 0):
        loopPrincipal = "Sair"
        break

# loop do NOME 

    while len(nomeAluno) < 4:  
        nomeAluno = input('Por favor, digite seu NOME ==> ')
        if (len(nomeAluno) < 4):  
            print("O NOME deve ter mais que três caracteres!")



# loop da  ALTURA 

    loopControl = "continuar"
    while loopControl == "continuar":
        alturaAluno = input('Por favor, digite sua ALTURA ==> ')

        if not(check_float(alturaAluno)):
            print('Por favor, digite uma ALTURA VÁLIDA! (usar "." ao invés de "," ) ')
        else:
            if (float(alturaAluno) < 0.0 or float(alturaAluno) > 2.70):  
                print("Por favor, digite uma ALTURA entre 0 e 2.70M ! ")
            else:
                loopControl = "Sair" 


# loop do peso  

    loopControl = "continuar"
    while loopControl == "continuar":
        pesoAluno = input('Por favor, digite seu PESO ==> ')

        if not(check_float(pesoAluno)):
            print('Por favor, digite uma PESO VÁLIDO! (usar "." ao invés de "," ) ')
        else:
            if (float(pesoAluno) < 20.0 or float(pesoAluno) > 350.00):  
                print("Por favor, digite uma ALTURA entre 20 e 350.0 kg  ! ")
            else:
                loopControl = "Sair" 


    # appending to list - Guarda/Adiciona os elementos digitados na LISTA 

    list.append( alunos(codigoAluno, nomeAluno, alturaAluno, pesoAluno) )
    loopControl = "continuar"
    nomeAluno = "" 


# imprime a LISTA com todos os alunos e calcula os valores

posicaoAlunoMaisAlto = 0
posicaoAlunoMaisBaixo = 0 
posicaoAlunoMaisMagro = 0
posicaoAlunoMaisGordo = 0 
valMaisAlto = 0.0
valMaisBaixo = 2.70 
valMaisMagro = 350.0
valMaisGordo = 0.0
somaTotalPesos = 0.00
somaTotalAlturas = 0.00
posicao = 0 

print('\n\n')
for obj in list:
    
    print('Código:', obj.codigo, ' Nome:', obj.nome, ' Altura', obj.altura, ' Peso:', obj.peso, sep =' ')

    # seleciona o mais alto
    if (float(obj.altura) > float(valMaisAlto)):
        valMaisAlto = obj.altura
        posicaoAlunoMaisAlto = posicao

    # seleciona o mais baixo
    if (float(obj.altura) < float(valMaisBaixo)):
        valMaisBaixo = obj.altura
        posicaoAlunoMaisBaixo = posicao

    # seleciona o mais gordo
    if (float(obj.peso) > float(valMaisGordo)):
        valMaisGordo = obj.peso
        posicaoAlunoMaisGordo = posicao

    # seleciona o mais magro
    if (float(obj.peso) < float(valMaisMagro)):
        valMaisMagro = obj.peso
        posicaoAlunoMaisMagro = posicao

    posicao = posicao + 1
    somaTotalPesos = somaTotalPesos + float(obj.peso)
    somaTotalAlturas = somaTotalAlturas + float(obj.altura)


# Acabou o loop Principal Inicio das impressões 


contador = list.count

if  len(list) > 0:

    print('\nSoma total dos Pesos ==> ', somaTotalPesos)
    print('Média dos Pesos ==> ', (float(somaTotalPesos)/posicao))

    print('\nSoma total das Alturas ==> ', somaTotalAlturas)
    print('Média de Altura ==> ', (float(somaTotalAlturas)/posicao))

    print("\nO aluno mais PESADO é : " , list[posicaoAlunoMaisGordo].nome, 'com',  list[posicaoAlunoMaisGordo].peso, 'Quilos')
    print("\nO aluno mais LEVE é : " , list[posicaoAlunoMaisMagro].nome, 'com',  list[posicaoAlunoMaisMagro].peso, 'Quilos')
    print("\nO aluno mais ALTO é : " , list[posicaoAlunoMaisAlto].nome, 'com',  list[posicaoAlunoMaisAlto].altura, 'Metros')
    print("\nO aluno mais BAIXO é : " , list[posicaoAlunoMaisBaixo].nome, 'com',  list[posicaoAlunoMaisBaixo].altura, 'Metros')
    
