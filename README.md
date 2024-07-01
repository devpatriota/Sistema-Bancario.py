# Sistema Bancário em Python - Versão 1

Este é um sistema bancário simples desenvolvido em Python, utilizando o terminal como interface.

## Funcionalidades

- Depósito: Permite ao usuário depositar dinheiro em sua conta bancária.
- Saque: Permite ao usuário sacar dinheiro de sua conta bancária, respeitando saldo disponível e limite de saque.
- Extrato Bancário: Permite ao usuário visualizar o extrato de sua conta bancária, incluindo todas as transações realizadas.
- Sair: Permite ao usuário encerrar o programa.

## Instruções de Uso

1. Execute o programa `main.py`.
2. Você será apresentado com um menu que oferece as seguintes opções:
   - [1] Depósito
   - [2] Saque
   - [3] Extrato Bancário
   - [0] Sair
3. Selecione a opção desejada digitando o número correspondente e pressionando Enter.
4. Siga as instruções apresentadas no terminal para realizar a operação desejada.
5. Após concluir uma operação, você retornará ao menu principal, onde poderá selecionar outra opção ou sair do programa.

## Limitações e Observações

- O sistema utiliza o terminal como interface, sem interface gráfica.
- O saldo inicial é zero e o limite de saque é de R$ 500,00.
- O número máximo de saques diários é limitado a 3.
- O sistema não possui persistência de dados entre execuções; todas as informações são perdidas quando o programa é encerrado.

## Contribuição

Contribuições são bem-vindas! Se você quiser melhorar este sistema bancário, sinta-se à vontade para fazer um fork do repositório, implementar suas melhorias e enviar um pull request.

## Autor

- Este sistema bancário em Python foi desenvolvido por [João Patriota](https://github.com/devpatriota).
