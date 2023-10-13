from poo import ContaBancaria

saldo = 0
carteira = 0

conta1 = ContaBancaria(saldo, carteira)

while True:
    try:
        op = int(input("\nSelecione uma opção\n1 <- Depositar\n2 <- Sacar\n3 <- Trabalhar\n0 <- Sair\n-> "))
        match(op):
            case 1:
                conta1.depositar()
            case 2:
                conta1.sacar()
            case 3:
                conta1.trabalhar()
            case 0:
                print("\nAté a proxima!\n")
                break
    except ValueError:
        print("Valor inválido, Tente novamente!")
