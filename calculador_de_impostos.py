
from impostos import ICMS, ISS
# -*- coding: UTF-8 -*-

class Calculador_de_impostos(object):

        def realiza_calculo(self, orcamento, imposto):    
            imposto_calculado =imposto.calcula(orcamento)
            print(imposto_calculado)


if __name__ == '__main__':

    print()
    print('--CALCULADOR DE IMPOSTOS--')
    from orcamento import Orcamento

    calculador = Calculador_de_impostos()
    #orcamento = Orcamento(500)

    #calculador.realiza_calculo(orcamento, ISS())
    #calculador.realiza_calculo(orcamento, ICMS())


    print('--         -*-          --')
