while True:
    nomeCliente = input ("Digite o nome do cliente " )
    idadeClinete= int(input ("Digite a idade do cliente " ))
    rendaCliente = float(input ("Digite a renda mensal do cliente " ))
    continuar = input("Deseja cadastrar mais um cliente ? (*s/n) : " )
    if continuar == "n":
        break
    print ( f"cliente : {nomeCliente} - idade : {idadeClinete} - renda mensal : {rendaCliente}" )