nomeCliente = input("Por favor insira o nome do cliente:")
idadeCliente = int(input("por favor insria a idade do cliente:"))
renda = int(input("Informe a renda do cliente:"))

if renda >=2000 or idadeCliente >= 60:
    print(f'Parabéns {nomeCliente}, voce está qualificado para o empréstimo!')
else:
    print(f'Sinto muito {nomeCliente}, você não está qualificado para o empréstimo.')