from DaxQuery import execute_dax_query
from Formatar import f
from Formatar import dh
from Formatar import dt

def corpo():

    valor = execute_dax_query()

    texto = (
        f'⌚️ Hora da atualização: {dh(valor[7])}\n'
        f'🚀 Total Validado: {f(valor[0])}\n'
        f'🎯 Necessários: {f(valor[1])}\n'
        f'📅 Expectativa de conclusão: {dt(valor[6])}\n'
        f'📈 Média diária (sete dias): {f(valor[9])}\n'
        f'🇧🇷 Estados que atingiram o mínimo: {valor[5]} de {valor[4]}\n\n'
        f'🌐 Relatório completo: https://bit.ly/4fjX8Zy\n\n'
        f'@PartidoMissao\n'
    )

    return texto