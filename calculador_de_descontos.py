# -*- coding: UTF-8 -*-

from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais,Sem_desconto

class Calculador_de_descontos(object):

    def calcula(self, orcamento):

        desconto = Desconto_por_cinco_itens(
            Desconto_por_mais_de_quinhentos_reais(Sem_desconto())
            ).calcula(orcamento)        
        
        return desconto





if __name__ == '__main__':

    print()
    print('--CALCULADOR DE DESCONTO--')
    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 10))
    orcamento.adiciona_item(Item('ITEM - 2', 10))
    orcamento.adiciona_item(Item('ITEM - 3', 10))
    orcamento.adiciona_item(Item('ITEM - 4', 10))    
    orcamento.adiciona_item(Item('ITEM - 5', 10))    
    orcamento.adiciona_item(Item('ITEM - 6', 50))

    calculador = Calculador_de_descontos()
    desconto = calculador.calcula(orcamento)

    print('Desconto calculado %s' %(desconto))



    print('--         -*-          --')