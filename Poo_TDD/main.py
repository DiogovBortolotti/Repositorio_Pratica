from banco.bancotest import BancoConta

conta1 = BancoConta('123', 20)
conta2 = BancoConta('223', 30, 900)

print(conta1)
conta1.depositar(1000)
print(conta1)


conta1.sacar(1)
print(conta1)

print(conta2)
conta1.transferir(1520, conta2)

print(conta1,conta2)