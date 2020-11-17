"""Criando uma locadora e verificando se o filme que o usuário procura está disponível!"""

from time import sleep

Locadora = [{

        'Título': 'O jogo da imitação',
        'Ano': '2014',
        'Diretor': 'Mordem Tyldum'

    }, {

        'Título': 'Pulp Fiction',
        'Ano': '1994',
        'Diretor': 'Quentin Tarantino'

    }, {

        'Título': 'Baby Driver',
        'Ano': '2017',
        'Diretor': 'Edgar Wright'

    }, {

        'Título': 'Forrest Gump-O Contador de Histórias',
        'Ano': '1994',
        'Diretor': 'Robert Zemeckis'

    }, {

        'Título': 'Era uma Vez em... Hollywood',
        'Ano': '2019',
        'Diretor': 'Quentin Tarantino'

    }, {

        'Título': 'O Que Fazemos nas Sombras',
        'Ano': '2014',
        'Diretor': 'Taika Waititi, Jamaine Clement'

    }]


print('Os filmes da locadora são')


for i in Locadora:
    T = i['Título']
    print(f'[ {Locadora.index(i)} ] ==>  {T} ')


info = str(input('Deseja saber um pouco mais sobre algum filme?'))


if info in ' S s Sim SIm SIM siM sIM Sim sIm ':

    FilmeEscolhido = int(input('Número do Filme: '))
    print(f'''      O diretor do filme escolhido é : {Locadora[FilmeEscolhido]['Diretor']}
    O ano de lançamento é : {Locadora[FilmeEscolhido]['Ano']}''')

else:
    print('Tudo bem, Adeus! :D')
    sleep(2)
    exit()
