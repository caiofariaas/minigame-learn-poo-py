class ContaBancaria:
    def __init__(self, saldo: float, carteira: float):
        self.carteira = carteira
        self.saldo = saldo

    def depositar(self):
        if self.carteira <= 0:
            print("\n\nSua carteira se encontra vazia! Trabalhe primeiro.\n")
            print(f"Total em carteira : R${self.carteira:.2f}\nTotal em conta bancaria: R${self.saldo}\n")

        else: 
            print(f"\nTotal em carteira : R${self.carteira:.2f}\nTotal em conta bancaria: R${self.saldo}\n")
            try:
                value = float(input("Quanto deseja depositar?: "))
                if value <= self.carteira:
                    self.saldo += value
                    self.carteira -= value
                    print(f"\nO depósito no valor de R${value:.2f} foi concluído!\nTotal em conta bancaria : R${self.saldo:.2f}\nSaldo em carteira : R${self.carteira:.2f}")
                else:
                    print("\n\nVocê não possui este valor em carteira!\n")
            except:
                print("\nValor inválido, Tente novamente!\n")

    def sacar(self):
        if self.saldo <= 0:
            print("\nSua conta se encontra vazia! Deposite primeiro.")
            print(f"\nTotal em conta banca1
            ria: R${self.saldo}\nTotal em carteira : R${self.carteira:.2f}\n")
        else:
            try:
                print(f"\nTotal em conta bancaria: R${self.saldo}\nTotal em carteira : R${self.carteira:.2f}\n")
                value = float(input("Quanto deseja sacar?: "))
                if value > self.saldo:
                    print("\n\nVocê não possui esse valor em sua conta!\n")
                else:
                    self.saldo -= value
                    self.carteira += value
                    print(f"\nO saque no valor de R${value:.2f} foi concluído!\n\nTotal em conta bancaria : R${self.saldo:.2f}\nTotal em carteira : R${self.carteira:.2f}")
            except:
                print("\nValor inválido, Tente novamente!\n")


    def trabalhar(self):
        import random
        
        print(f"\nTotal em carteira : R${self.carteira:.2f}\nTotal em conta bancaria: R${self.saldo}\n")
        if self.saldo <= 2000:
            while True:
                try:
                    opt = int(input("1 <- Uber\n0 <- Sair\n-> "))
                    match(opt):
                        case 1:
                            value = random.randrange(200, 1000)
                            self.carteira += value

                            print(f"\nVocê Trabalhou o dia todo como Uber e ganhou um total de R${value:.2f}\n"
                                + f"O total em sua carteira é de RS{self.carteira:.2f}\nO total em sua conta no banco é de R${self.saldo}\n")
                            
                        case 0:
                            print("\naté a proxima!\n")
                            break

                except ValueError:
                    print("\nValor inválido\n")

        elif self.saldo > 2000:
            while True:
                try:
                    opt = int(input("1 <- Uber\n2 <- Developer\n0 <- Sair\n-> "))
                    match(opt):
                        case 1:

                            value = random.randrange(200, 500)
                            self.carteira += value
                            print(f"\nVocê Trabalhou o dia todo como Uber e ganhou um total de R${value:.2f}\n"
                                + f"O total em sua carteira é de RS{self.carteira:.2f}\nO total em sua conta no banco é de R${self.saldo}\n")
                            
                        case 2:

                            value = random.randrange(500, 1000)
                            self.carteira += value
                            print(f"\nVocê Trabalhou o dia todo como Desenvolvedor e ganhou um total de R${value:.2f}\n"
                                + f"\nO total em sua carteira é de RS{self.carteira:.2f}\nO total em sua conta no banco é de R${self.saldo}\n")
                            
                        case 0:
                            print("\naté a proxima!\n")
                            break

                except ValueError:
                    print("\nValor inválido\n")
