
from impostos import ICMS, ISS, ICPP, IKCV
# -*- coding: UTF-8 -*-

class Calculador_de_impostos(object):

        def realiza_calculo(self, orcamento, imposto):    
            imposto_calculado =imposto.calcula(orcamento)
            print(imposto_calculado)


if __name__ == '__main__':

    print()
    print('--CALCULADOR DE IMPOSTOS--')
    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 10))
    orcamento.adiciona_item(Item('ITEM - 2', 10))
    orcamento.adiciona_item(Item('ITEM - 3', 10))
    orcamento.adiciona_item(Item('ITEM - 4', 10))    
    orcamento.adiciona_item(Item('ITEM - 5', 10))    
    orcamento.adiciona_item(Item('ITEM - 6', 50))

    calculador = Calculador_de_impostos()

    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())

    calculador.realiza_calculo(orcamento, ICPP())
    calculador.realiza_calculo(orcamento, IKCV())


    print('--         -*-          --')
