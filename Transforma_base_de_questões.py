def transforma_base(lista_questoes):

    if lista_questoes == []:
        return {}

    dic_proc_quest = {}

    # dic_proc_quest['facil'] = [] --> vou conseguir isso usando:
    # [queste['nivel']] pq a key devolverá o valor que me interessa
    # o novo dict.
    #dic_proc_quest['medio'] = []
    #dic_proc_quest['dificil'] = []

    for queste in lista_questoes:
        #print(queste)
        if queste['nivel'] not in dic_proc_quest.keys():
          dic_proc_quest[queste['nivel']] = []
          # dos 6 teste iniciais que eu fiz volta a última questão apresentada
        dic_proc_quest[queste['nivel']].append(queste) 
        # Resolve o problema de alguma questões desaparecerem
        # do banco de dados sendo processado
    
    return dic_proc_quest


print(transforma_base([
  {
    'titulo': 'Qual o resultado da operação 57 + 32?',
    'nivel': 'facil',
    'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
    'correta': 'C'
  },
  {
    'titulo': 'Qual a capital do Brasil?',
    'nivel': 'facil',
    'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
    'correta': 'A'
  },
  {
    'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
    'nivel': 'medio',
    'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
    'correta': 'C'
  },
  {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
          'nivel': 'medio',
          'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
          'correta': 'B'},

    {'titulo': 'Quem é Oxóssi?!',
          'nivel': 'dificil',
          'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Dissílabo', 'C': 'Divindade das religiões africanas', 'D': 'Trapper brasileiro'},
          'correta': 'C'},

    {'titulo': 'Qual a altura do Cristo Redentor?',
          'nivel': 'dificil',
          'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
          'correta': 'B'}
]))

print(transforma_base([]))