# Desafio #
 ## 1- Para a primeira versão do sistema bancário simples devemos implementar apenas 3 operações:
 ## 1.1- Depósito: deve ser possível depositar somente valores positivos para a conta bancária. Ademais, todos os depósitos devem ser exibidos na operação de "Extrato".

 ## 2- Saque: O sistema deve permitir realizar apenas 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não possua saldo suficiente em conta, deve ser exibido uma mensagem informando que não será possível realizar a operação por saldo insuficiente. Todos os saques devem ser exibidos na operação de "Extrato".

## 3- Extrato: Essa operação deve listar todos depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Os valores devem ser exibidos utilizando o formato "R$ xxx.xx".

menu_inicial = f"""

    |------SISTEMA-BANCÁRIO------|
    |                            |
    | [1] Deposito               |
    | [2] Saque                  |
    | [3] Extrato                |
    | [0] Sair                   |
    |                            |
    |----------------------------|

Informe a operação desejada => """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu_inicial)

    if opcao == "1":
        valor = float(input("Qual valor será depositado? "))
    
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: + R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso.")

        else:
            print("Erro na operação! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Qual o valor do saque? "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Erro na operação! Você não possui saldo suficiente.")

        elif excedeu_limite:
            print("Erro na operação! O valor informado é maior que o seu limite por saque.")
        
        elif excedeu_saques:
            print("Erro na operação! Limite de saques diários atingido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: - R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso.")

        else:
            print("Erro na operação! O valor informado é inválido.")

    elif opcao == "3":
        print("----------EXTRATO----------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("---------------------------")

    elif opcao == "0":
        print("Encerrando o sistema",
            end="..." "\nObrigado por utilizar nosso sistema bancário!",)
        break

    else:
        print("Operação inválida! Selecione a operação desejada novamente.")
