import pytest

from Poo_TDD.banco.bancotest import BancoConta

#Precisa colocar __INIT__ na pasta para reconhecer
#

class TestClass:
    
    def test_se_a_condicao_de_criar_conta_for_igual_a_numeracao_da_conta_for_198(self):
        resultado_esperado = 'Conta: 198            Saldo:0                       Limite:500'
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
        
    
    def test_se_o_valor_sacado_for_menor_que_limite_usado_retorna_ok(self):
        resultado_esperado = 200
        
    
    def test_se_o_valor_sacado_for_menor_que_saldo_retorna_ok(self):
        pass
    
    def test_se_valor_transferido_vao_estar_correto(sel):
        pass