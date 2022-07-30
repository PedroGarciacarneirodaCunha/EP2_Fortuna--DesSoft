def valida_questao(dict_quest):

    dict_saida = {}

    lista_nomes = ['titulo', 'nivel', 'opcoes', 'correta']

    ABCD = ['A', 'B', 'C', 'D']

    l_nivel = ['facil', 'medio', 'dificil']

    for nome in lista_nomes:
        
        if nome in dict_quest.keys():
            pass
        else:
            dict_saida[nome] = 'nao_encontrado'
        
    if len(dict_quest.keys()) == 4:
        pass
    else:
        dict_saida['outro'] = 'numero_chaves_invalido'
        
    if 'titulo' in dict_quest.keys() and len(str(dict_quest['titulo']).strip()) != 0:
        pass
    else:
        dict_saida['titulo'] = 'vazio'
        
    if 'nivel' in dict_quest.keys() and dict_quest['nivel'] in l_nivel:
        pass
    else:
        dict_saida['nivel'] = 'valor_errado'
        
    if 'opcoes' in dict_quest.keys() and len(dict_quest['opcoes']) != 4:

        dict_saida['opcoes'] = 'tamanho_invalido'
    
    else:

        dict_vaz = {}

        for abcd in ABCD:

            if abcd in dict_quest['opcoes'].keys():
                pass
            else:
                dict_saida['opcoes'] = 'chave_invalida_ou_nao_encontrada'
## parte da resposta vazia

            if len(str(dict_quest['opcoes'][abcd]).strip()) == 0:
                dict_vaz[abcd] = 'vazia'
            
            if len(dict_vaz) > 0:
                dict_saida['opcoes'] = dict_vaz
        
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