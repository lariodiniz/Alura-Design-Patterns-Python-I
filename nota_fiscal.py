# -*- coding: UTF-8 -*-

from datetime import date
from observadores import imprime, salva_no_banco, envia_por_email
#from criador_de_nota_fiscal import Criador_de_nota_fiscal

class Item(object):

    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor

class Nota_fiscal(object):

    def __init__(self, razao_social, cnpj, itens, data_de_emissao = date.today(), detalhes = '', observadores = []):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception('Detalhes da nota não pode ter mais do que 20 caracteres')
        self.__detalhes = detalhes
        self.__itens = itens

        # chamando os métodos
        for observador in observadores:
            observador(self)

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes

if __name__ == '__main__':

    itens=[
        Item(
            'ITEM A',
            100
        ),
        Item(
            'ITEM B',
            200
        )
    ]

    nota_fiscal = Nota_fiscal(
        razao_social = 'FHSA Limitada',
        cnpj = '012345678901234',
        itens = itens,
        observadores=[imprime, envia_por_email, salva_no_banco]
        )


    print(nota_fiscal.razao_social)
    print(nota_fiscal.detalhes)
    print(nota_fiscal.cnpj)