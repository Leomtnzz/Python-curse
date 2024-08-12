class balanceException(Exception):
    pass


class BankAccounts:
    def __init__(self,initialAmount,AcctName):
        self.balance= initialAmount
        self.name=AcctName
        print(f'\nLa cuenta \'{self.name}\' ha sido creada.\nBalance de {self.balance:.2f}$\n')

    def GetBalance(self):
        print(f'\nCuenta \'{self.name}\' tiene un balance de {self.balance:.2f}$')

    def deposito(self, amount):
        self.balance=self.balance+amount
        print('\nDeposito hecho.')
        self.GetBalance()

    def ViableTransaction(self,amount):
        if self.balance>=amount:
            return
        else:
            raise balanceException(f'\nLo siento, \'{self.name}\' solo tiene {self.balance:.2f}$\n')
        
    def retirada(self,amount):
        try:
            self.ViableTransaction(amount)
            self.balance=self.balance-amount
            print('\nTransferencia completada:')
            self.GetBalance()
        except balanceException as error:
            print(f'\nTransferencia denegada, {error}')

    def transferencia(self, amount,account):
        try:
            print('\n********\n\nEmpezando transferencia.. 🚀')
            self.ViableTransaction(amount)
            self.retirada(amount)
            account.deposit(amount)
            print('\nTransferencia completada.💵\n\n********')
        except balanceException as error:
            print(f'\ntransferencia denegada❌, {error}') 