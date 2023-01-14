
# conta > saldo, limite
class BancoConta():
    
    def __init__(self, conta, saldo=0, limite=500):
        self.conta = conta
        self.saldo = saldo
        self.limite = limite
        
    def __str__(self):
        return f'Conta:{self.conta}, Atual Saldo:{self.saldo:.2f}, Atual Limite:{self.limite:.2f}'
    
    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return f'Atual Saldo:{self.saldo:.2f}, Atual Limite:{self.limite:.2f}, Saque:{valor:.2f}'
        elif (self.limite+self.saldo) >= valor:
            self.saldo -= valor
            self.limite = (self.saldo+self.limite)
            self.saldo =0
            return f'Atual Saldo:{self.saldo:.2f}, Atual Limite:{self.limite:.2f}, Saque:{valor:.2f}'
        else:
            raise ValueError(f'Não Possui Saldo suficiente {self.saldo} e Limite: {self.limite}')
    
    
    def transferir(self, valor, conta_destino):
        if self.saldo >= valor:
            self.saldo -= valor
            conta_destino.depositar(valor)
            return f'Atual Saldo:{self.saldo:.2f}, Atual Limite:{self.limite:.2f}, Transferido:{valor:.2f}'
        elif (self.limite+self.saldo) >= valor:
            self.saldo -= valor
            self.limite = (self.saldo+self.limite)
            self.saldo = 0
            conta_destino.depositar(valor)
            return f'Atual Saldo:{self.saldo:.2f}, Atual Limite:{self.limite:.2f}, Transferido:{valor:.2f}'
        else:
            raise ValueError(f'Não Possui Saldo suficiente {self.saldo} e Limite: {self.limite}')