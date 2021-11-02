loopControl = "continuar"
valNota = 0

while loopControl == "continuar":
    valNota = input('Por favor, digite um numero entre 0 e 10 ==> ')
    
    if valNota.isdigit()== False:
       print("Por favor, digite um número Inteiro VÁLIDO! ")
    else:
        if (int(valNota) <0 or int(valNota) >10):  
            print("Por favor, digite uma NOTA entre 0 e 10! ")
        else:
            print("A sua Nota registrada foi ==> " , valNota)
            loopControl = "Sair"    
