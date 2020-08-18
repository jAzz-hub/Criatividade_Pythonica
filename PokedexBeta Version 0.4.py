#Uma versão super ultra mega simplificada de um pokedex

a=input('me diga o nome de um pokemon do tipo pedra: ')
b=input('agora me diga o nome de um pokemon do tipo água: ')
c=input('e pór último um pokemon do tipo fogo: ')

def pokemon(x):
    
    print('Pokedex :V =>  este pokemon é do tipo:')
    print(x)

print('Olha só quem apareceu direto da terra! é um {}!!!'.format(a))
pokemon('pedra')


print('O que é aquilo vindo do fundo do lago? Nossa é um {}!!'.format(b))
pokemon('água')

print('Que calor aqui... olha é um {}!!'.format(c))
pokemon('fogo')