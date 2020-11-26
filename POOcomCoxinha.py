
# ☾✿ Criando uma classe que representa tudo que pode se apresentar como coxinha:

from random import randint

class almost_Coxinha():
    """
    A classe almost Coxinha define comidas brasileiras que são quase coxinhas
    """

    # ☾✿ Criação de um construtor e atribuição de atributos:
    def __init__(self,custo_em_reais,nome,aspecto,composição,origem):
        """
        O construtor __init__ recebe um objeto e constroi aquele como uma instância da classe almost_Coxinha!
        self => objeto que recebe atribuições de:
                    custo_em_reais
                    aspecto
                    composição
                    origem
        """

        # ☾✿ Fique a vontade pra discordar mas se custar mais de 20 reais não é uma coxinha!
        self.custo_em_reais = custo_em_reais
        self.nome = nome
        self.aspecto = aspecto
        self.composição = composição
        self.origem = origem
        print(f'Uma nova quase coxinha foi criada com aspecto {self.aspecto}')

    # ☾✿ Criação de método de classe:
    def info(self):
        """
        O método info recebe um objeto de sua classe e informa seus atributos base!
        self => Tem de ser objeto da classe Coxinha que utiliza do método info
        """
        print(f' {self.nome} é quase uma coxinha só que tem um aspecto {self.aspecto} e é feita(o) de {self.composição}')



# ☾✿ Atribui-se o bolinho_de_chuva_recheado como uma instância da classe Coxinha():
bolinho_de_chuva_recheado =  almost_Coxinha(custo_em_reais = randint(0, 5), nome = 'Bolinho de chuva', aspecto = 'Fofinho e esferico', composição = 'massa de bolo', origem = 'Brasileira' )
acarajé = almost_Coxinha(custo_em_reais = randint(0, 20), nome = 'Acarajé', aspecto = 'Crocante poroso e macio', composição = 'massa de acarajé', origem = 'Brasileira')

# ☾✿ São chamados atributos do objeto para que se analise os mesmos detalhadamente:
print(f'O {bolinho_de_chuva_recheado.nome} é de origem: {bolinho_de_chuva_recheado.origem}')
print(f'O {acarajé.nome} é de origem: {bolinho_de_chuva_recheado.origem}')

# ☾✿ É chamado o método info() para um objeto da classe Coxinha()
bolinho_de_chuva_recheado.info()
