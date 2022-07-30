def questao_para_texto(questao, id):

    txt = '''----------------------------------------\n\n'''

    txt += 'QUESTÃO ' + str(id) + '\n\n'

    txt += questao['titulo'] + '\n'

    txt += '\nRESPOSTAS:\n'

    for chave, valor in questao['opcoes'].items():

        txt += chave + ': ' + valor + '\n'


    return txt



print(questao_para_texto({
  "titulo": "Qual destes parques não se localiza em São Paulo?!",
  "nivel": "facil",
  "opcoes": {
    "A": "Ibirapuera",
    "B": "Parque do Carmo",
    "C": "Parque Villa Lobos",
    "D": "Morro da Urca"
  },
  "correta": "D"
}, 5))