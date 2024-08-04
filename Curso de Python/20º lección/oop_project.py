from bank_accounts import *

Leo=BankAccounts(2353.46, 'Leo')
# Leo.GetBalance()
# Leo.deposit(852.61)
Leo.retirada(3650)
Leo.transferencia(845,'Nora')

Nora=BankAccounts(3501.91, 'Nora')
# Nora.GetBalance()
# Nora.deposit(673.43)
# Nora.retirada(4500)
Nora.transferencia(845,'Leo')