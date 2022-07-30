from random import randint, sample

def gera_ajuda(questoes):

    alt_correta = questoes['correta']

    l_alt_inc = []

    for questao in questoes:
        if questao == 'opcoes':
            for k,v in questoes[questao].items():
                if k != alt_correta:
                    l_alt_inc.append(v)
    
    random_number = randint(1,2)

    random_alternative = sample(l_alt_inc, k = random_number)

    txt_d = 'DICA:\n'
    txt_d += 'Opções certamente erradas: ' + ' | '  .join(random_alternative)



    return txt_d



print(gera_ajuda({
  "titulo": "Qual destes parques não se localiza em São Paulo?!",
  "nivel": "facil",
  "opcoes": {
    "A": "Ibirapuera",
    "B": "Parque do Carmo",
    "C": "Parque Villa Lobos",
    "D": "Morro da Urca"
  },
  "correta": "D"
}))
print(gera_ajuda({
  "titulo": "Qual destes parques não se localiza em São Paulo?!",
  "nivel": "facil",
  "opcoes": {
    "A": "Ibirapuera",
    "B": "Parque do Carmo",
    "C": "Parque Villa Lobos",
    "D": "Morro da Urca"
  },
  "correta": "D"
}))