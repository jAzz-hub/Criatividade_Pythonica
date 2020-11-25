# ☾✿ Criando uma classe que representa tudo que pode se apresentar como coxinha:


class Coxinha():
    """
    A classe Coxinha define uma coxinha sugestiva
    """

    # ☾✿ Criação de um construtor e atribuição de atributos:
    def __init__(self):
        """
        O construtor __init__ recebe um objeto e constroi aquele como uma instância da classe coxinha!
        self => objeto que recebe atribuições de aspecto e composição
        """

        # ☾✿ Fique a vontade pra discordar mas se custar mais de 20 reais não é uma coxinha!
        self.preço_em_reais = [valor for valor in range(0,20)]
        self.aspecto = 'fast food delicioso'
        self.composição = 'massa frita e recheio'
        self.origem = 'Brasil'
        print('Uma nova coxinha foi criada')

    # ☾✿ Criação de método de classe:
    def info(self):
        """
        O método info recebe um objeto de sua classe e informa seus atributos base!
        self => Tem de ser objeto da classe Coxinha que utiliza do método info
        """
        print(f'Toda coxinha tem um aspecto de {self.aspecto} e é feita de {self.composição}')

# ☾✿ Atribui-se o bolinho_de_chuva_recheado como uma instância da classe Coxinha()
bolinho_de_chuva_recheado = Coxinha()

# ☾✿ É chamado o método info() para um objeto da classe Coxinha()
bolinho_de_chuva_recheado.info()
