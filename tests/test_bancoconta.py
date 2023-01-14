import pytest

from Poo_TDD.banco.bancotest import BancoConta

#Precisa colocar __INIT__ na pasta para reconhecer
#pip install pytest-cov
#pytest --cov=Poo_TDD\banco tests/ --cov-report term-missing
#pytest --cov=Poo_TDD\banco tests/ --cov-report html

class TestClass:
    
    def test_se_a_condicao_de_criar_conta_for_igual_a_numeracao_da_conta_for_198(self):
        resultado_esperado = 'Conta:198, Atual Saldo:0.00, Atual Limite:500.00'
        conta_test =  BancoConta(198)
        conta_resultado = str(conta_test)
        assert conta_resultado == resultado_esperado
    
    def test_se_depositar_300_deve_retornar_300(self):
        resultado_esperado = 300
        conta_test = BancoConta(199)
        resultado = conta_test.depositar(300)
        assert resultado == resultado_esperado
        
    def test_se_o_valor_sacado_for_maior_que_limite_retorna_erro(self):
        with pytest.raises(ValueError):
            conta_test = BancoConta(199)
            resultado = conta_test.sacar(900)
            assert resultado
        
    def test_se_o_valor_sacado_for_menor_que_limite_max_usado_retorna_ok(self):
        resultado_esperado = 'Atual Saldo:0.00, Atual Limite:0.00, Saque:200.00'
                            #conta | saldo |limite
        conta_teste = BancoConta(10, 10, 190)
        resultado = conta_teste.sacar(200)
        assert resultado_esperado == resultado
        
    def test_se_o_valor_sacado_for_menor_que_saldo_max_retorna_ok(self):
        resultado_esperado = 'Atual Saldo:150.00, Atual Limite:500.00, Saque:50.00'
                            #conta | saldo |limite
        conta_teste = BancoConta(10, 200, 500)
        resultado = conta_teste.sacar(50)
        assert resultado_esperado == resultado
    
    def test_se_valor_transferido_vao_estar_correto(self):
        resultado_esperado_conta_transferencia = 'Atual Saldo:0.00, Atual Limite:150.00, Transferido:1000.00'
        resultado_esperado_saldo_conta_1 = 'Conta:53, Atual Saldo:0.00, Atual Limite:150.00'
        resultado_esperado_saldo_conta_2 = 'Conta:22, Atual Saldo:1350.00, Atual Limite:500.00'
        conta_teste1 = BancoConta(53, 650)
        conta_teste2 = BancoConta(22, 350)
        
        resultado_transferencia = conta_teste1.transferir(1000, conta_teste2)
        resultado_saldo_conta_1 = str(conta_teste1)
        resultado_saldo_conta_2 = str(conta_teste2)
        
        #validacao_transferencia = (resultado_transferencia == resultado_esperado_conta_transferencia) 
        #validacao_saldo_conta_1 = (resultado_esperado_saldo_conta_1 == resultado_saldo_conta_1) 
        #validacao_saldo_conta_2 =(resultado_esperado_saldo_conta_2 == resultado_saldo_conta_2)
        #assert validacao_transferencia == True & validacao_saldo_conta_1 == True & validacao_saldo_conta_2 == True
        
        assert (resultado_transferencia == resultado_esperado_conta_transferencia) & (resultado_esperado_saldo_conta_1 == resultado_saldo_conta_1) & (resultado_esperado_saldo_conta_2 == resultado_saldo_conta_2)
        
        
    def test_se_o_valor_sera_consumido_somente_do_saldo(self):
        resultado_esperado_conta_transferencia = 'Atual Saldo:50.00, Atual Limite:500.00, Transferido:50.00'
        resultado_esperado_saldo_conta_1 = 'Conta:12, Atual Saldo:50.00, Atual Limite:500.00'
        resultado_esperado_saldo_conta_2 = 'Conta:22, Atual Saldo:50.00, Atual Limite:500.00'
        conta_teste1 = BancoConta(12, 100)
        conta_teste2 = BancoConta(22, 0)
        
        resultado_transferencia = conta_teste1.transferir(50, conta_teste2)
        resultado_saldo_conta_1 = str(conta_teste1)
        resultado_saldo_conta_2 = str(conta_teste2)
        assert (resultado_transferencia == resultado_esperado_conta_transferencia) & (resultado_esperado_saldo_conta_1 == resultado_saldo_conta_1) & (resultado_esperado_saldo_conta_2 == resultado_saldo_conta_2)
    
    
    
    def test_se_o_valor_limite_passar_ira_apresentar_erro(self):
        conta_teste1 = BancoConta(12, 100)
        conta_teste2 = BancoConta(22, 0)
        with pytest.raises(ValueError):
            resultado_transferencia = conta_teste1.transferir(5000, conta_teste2)
            assert resultado_transferencia