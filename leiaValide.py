loopControl = "continuar"
valNome = ""
valIdade = 0
valSalario = 0.0
valSexo = ""
valEstadoCivilC = ""
valValidEstadoCivil = "SCVD"

# loop com validacao do NOME

while len(valNome) < 4:  
    valNome  = input('Por favor, digite seu NOME ==> ')
    if (len(valNome) < 4):  
        print("O NOME deve ter mais que três caracteres!")


# loop com validacao da IDADE 
while loopControl == "continuar":
    valIdade = input('Por favor, digite sua IDADE ==> ')
    
    if valIdade.isdigit()== False:
       print("Por favor, digite um número Inteiro VÁLIDO! ")
    else:
        if (int(valIdade) > 150):  
            print("Por favor, digite uma IDADE menor que 150! ")
        else:
            loopControl = "Sair"    



# loop com validacao do SALARIO

def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False   

loopControl = "continuar"
while loopControl == "continuar":
    valSalario = input('Por favor, digite seu SALÁRIO ==> ')

    if not(check_float(valSalario)):
           print("Por favor, digite um número VÁLIDO! ")
    else:
        if (float(valSalario) < 0.0):  
            print("Por favor, digite um SALÁRIO maior que 0! ")
        else:
            loopControl = "Sair" 



# loop com validacao do SEXO

loopControl = "continuar"
while loopControl == "continuar":
    valSexo = input('Por favor, digite seu SEXO M/F ==> ')

    if (valSexo != "M" and valSexo != "F"):
           print('Por favor, digite APENAS UMA LETRA! "M" ou "F" ')
    else:
        loopControl = "Sair" 



# loop com validacao do ESTADO CIVIL

loopControl = "continuar"
while loopControl == "continuar":
    valEstadoCivil = input('Por favor, digite seu ESTADO CIVIL S/C/V/D ==> ')

    if (len(valEstadoCivil) > 1 or (valEstadoCivil not in valValidEstadoCivil)):
           print('Por favor, digite APENAS UMA LETRA! "S" ou "C" ou "V" ou "D" ')
    else:
        loopControl = "Sair" 