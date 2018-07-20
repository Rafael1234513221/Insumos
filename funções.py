"""
Todas as funções necessárias para trabalhar com o banco de dados.
"""

from tkinter import messagebox
from time import strftime


def arquivo_mensal():
    """
    Descobre a data que será o nome do arquivo.txt (mes-ano).
    """
    data = strftime('%m-%y')
    local_arquivo = f"historico/{data}.txt"
    return str(local_arquivo)


def cadastrar_dados(produto, valor, parcelas):
    """
    Escreve no arquivo dados.txt alguma coisa.
    """
    data_info = strftime('%D')
    produto = produto.strip()
    produto = produto.replace(' ', '_')
    valor = valor.strip()
    parcelas = parcelas.strip()
    
    if len(produto) and len(valor) == 0:
        messagebox.showinfo(message='Ainda existem campos em branco, por favor preencha-os!')
    
    elif len(parcelas) == 0 or int(parcelas) == 0:
        parcelas = 1

    elif len(produto) and len(valor) > 0 and valor.isnumeric() == True:
        with open(f'{arquivo_mensal()}', 'a', encoding='Utf-8') as dados:
            dados.write(f'{data_info} {produto} {valor} {parcelas}\n')


def limpar_dados():
    """
    Apaga todos os dados do arquivo externo do mês em andamento.
    """
    with open(f'{arquivo_mensal()}', 'w') as dados:
        dados.write('')


def filtrar_dados(tipo: str):
    """
    Pega todos os valores que estão no arquivo externo e depois separa de acordo com a entrada.
    """
    linhas = []
    valores = ''
    with open(f'{arquivo_mensal()}', 'r') as arquivo:
        for linha in arquivo:
            linhas.append(linha.strip().split('\n'))
    for conteúdo in linhas:
        valores += f'{conteúdo}\n'
    valores = valores.replace('[', '').replace(']', '').replace("'", '').split()
    # Filtra por tipo de arquivo.
    cont_geral = 0
    lista_datas = []
    lista_produtos = []
    lista_preços = []
    lista_parcelas = []
    while cont_geral < len(valores)-1:
        lista_datas.append    (str(valores[cont_geral]))
        lista_produtos.append (str(valores[(cont_geral)+1]))
        lista_preços.append   (float(valores[(cont_geral)+2]))
        lista_parcelas.append (int(valores[(cont_geral)+3]))
        cont_geral += 4
    if tipo == 'data':
        return lista_datas 
    elif tipo == 'produtos':
        return lista_produtos
    elif tipo == 'preços':
        return lista_preços
    elif tipo == 'todos':
        return [lista_datas, lista_produtos, lista_preços]


def atualiza_salário():
    """
    É retornado o valor do seu salário menos as compras feitas.
    """
    salário = 1000
    compras = filtrar_dados('preços')
    for valor in compras:
        salário -= valor
    
    return f'{salário:.2f}'


def compras_mensais():
    """
    Localiza o arquivo que diz respeito ao mês de consulta e retorna em uma forma amigável.
    """
    extrato_mensal = filtrar_dados('todos')
    dados_de_saida = f'{"":-^55}\n'
    dados_de_saida += f'|{"DATA":^10} {"PRODUTO":^30} {"VALOR":^10} |\n'
    for cont in range(len(extrato_mensal[0])):
        dados_de_saida += f'|{extrato_mensal[0][cont]:<10} '  # Pega as datas
        dados_de_saida += f'{extrato_mensal[1][cont]:<40} '   # Pega o nome dos produtos
        dados_de_saida += f'{extrato_mensal[2][cont]:<10} |'  # Pega o valores dos produtos
        dados_de_saida += '\n'
    dados_de_saida += f'{"":-^55}\n'
    dados_de_saida = dados_de_saida.replace('_', ' ')
    return dados_de_saida


def cria_arquivos():
    """
    Cria todos arquivos necessários durante o ano que o usuário digitou as compras.
    """
    mes = 1
    ano = strftime('%y')
    print(ano)
    while mes != 12:
        if mes < 10:
            str_mes = f'0{mes}'
            mes += 1
        if mes >= 10:
            str_mes = mes
            mes += 1
        with open(f'historico/{str_mes}-{ano}.txt', 'w') as arquivo:
            arquivo.write('')


def lança_fatura(vezes):
    """ 
    Cadastra nos proximos meses os valores de uma fatura de acordo com o número
    de parcela que esta tem. Por exemplo se tiver um celular parcelado em 12x
    essa função lançará nos arquivos dos proxímos 12 meses o valor da parcela.
    """
    vezes = vezes.get()
    
