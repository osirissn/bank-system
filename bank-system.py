saldo = 0.0

saldo_inicial = float(input("Digite o saldo inicial da conta: "))
saldo = saldo_inicial

while True:
    print("\nOpções:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Consultar Saldo")
    print("4. Sair")

    operacao = int(input("Digite o número da opção desejada: "))

    if operacao == 1:
        valor_deposito = float(input("Qual valor deseja depositar? "))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f"Depósito de {valor_deposito} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")
    elif operacao == 2:
        valor_saque = float(input("Qual valor deseja sacar? "))
        if valor_saque > 0:
            if valor_saque <= saldo:
                saldo -= valor_saque
                print(f"Saque de {valor_saque} realizado com sucesso.")
            else:
                print("Valor inválido para saque.")
        else:
            print("O valor do saque deve ser positivo.")
    elif operacao == 3:
        print(f"Saldo atual: {saldo}")
    elif operacao == 4:
        print("Você saiu do sistema.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
    
