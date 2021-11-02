loopControl = "continuar"
valNome = ""
valSenha = ""

while loopControl == "continuar":
    valNome  = input('Por favor, digite seu NOME ==> ')
    valSenha = input('Por favor, digite sua SENHA ==> ')
    
    if (valNome == valSenha):  
        print("NOME e SENHA não podem ser iguais!")
    else:
        print(valNome,"foi o NOME digitado e", valSenha, "foi a SENHA escolhida." )
        loopControl = "Sair"