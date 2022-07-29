def valida_questao(dict_quest):

    dict_saida = {}

    lista_nomes = ['titulo', 'nivel', 'opcoes', 'correta']

    ABCD = ['A', 'B', 'C', 'D']

    for nome in lista_nomes:
        
        if nome in dict_quest.keys():
            pass
        else:
            dict_saida['titulo'] = 'nao_encontrado'
        
    if len(dict_quest.keys()) == 4:
        pass
    else:
        dict_saida['outro'] = 'numero_chaves_invalido'
        
    if dict_quest.keys() == 'titulo' and dict_quest['titulo'] != ' ' or dict_quest['titulo'] != '':
        pass
    else:
        dict_saida['titulo'] = 'vazio'
        
    if 'nivel' in dict_quest.keys() and dict_quest['nivel'] == ('facil' or 'medio' or 'dificil'):
        pass
    else:
        dict_saida['nivel'] = 'valor_errado'
        
    if dict_quest.keys() == 'opcoes' and len(dict_quest['opcoes']) != 4:

        dict_saida['opcoes'] = 'tamanho_invalido'
    
    else:

        for abcd in ABCD:

            if abcd not in dict_quest['opcoes'].keys():
                pass
            else:
                dict_saida['opcoes'] = 'chave_invalida_ou_nao_encontrada'
## parte da resposta vazia
            ##if dict_quest['opcoes'[abcd]] == '' or dict_quest['opcoes'[abcd]] == ' ':
                ##dict_saida['opcoes'] = {dict_quest['opcoes'[abcd]]: 'vazia'}
        
    if 'correta' in dict_quest.keys() and dict_quest['correta'] in ABCD:
        pass
    else:
        dict_saida['correta'] = 'valor_errado'

    return dict_saida



print(valida_questao({
  'titulo': 'Qual o resultado da operação 57 + 32?',
  'nivel': 'facil',
  'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
  'correta': 'C'
})) 
# {}
print(valida_questao({
  'titulo': 'Qual o resultado da operação 57 + 32?',
  'nivel': 'moleza',
  'opcoes': {'A': '  ', 'B': '85', 'C': '89', 'D': '\t'}
}))

# {
#  'correta': 'nao_encontrado',
#  'outro': 'numero_chaves_invalido',
#  'nivel': 'valor_errado',
#  'opcoes': {'A': 'vazia', 'D': 'vazia'}
#}