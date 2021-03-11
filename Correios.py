"""
    Autor: George Ikeda   Programa: CorreiosV2.py  Data: 16/02/2021
            renomeado para Correios.py versão 1.0.0 (GitFlow GitHub)

    Linguagem: Python versão:3.9.2 64bits
    Descrição: Programa cria um cadastro simples com codigo de rastreio
             : Rastreia os produtos de compras imprimindo num terminal 
             : 
    recurso  : Correios : Banco de dados Mysql.
               compras  : Tabela MySQL: cadastra os produtos adquiridos
                        : guarda a última informação recebido do rastreio
               rastreio : Tabela MySQL: armazena os rastreios do correios

    objetivo : Treinamento em Python utilizando MYSQL e API 
             : Aprender e treinar Python  em app útil para sociedade
             : Add  em 09/03/21 - Workflow GitFlow para gerenciar o desenvolvimento de software (gitflow / github)

"""
from colorama import init
init(convert=True)
import mysql.connector as mysql
from  mod_util import agora, hoje, strdate, convfdate, convfdata, convfdatastr
from mysql.connector import Error
from pyrastreio import correios
from datetime import datetime, date
from time import sleep


default_ =  '\33[m'  ## cor padrão
underlin_ = '\33[4m'  ## cor padrão, sublinhado
bold_ = '\33[1m'  ## cor padrão, bold
green_ = '\33[0;32m' ## letra verde
red_ = '\33[0;31m' ##  letra vermelha
redbold_ = '\33[1;31m' ##  letra vermelha e bold
yellow_ =  '\33[0;33m' ##  letra amarela
blue_ = '\33[0;34m' ##  letra amarela
inversion_ ='\33[7;37;40m' ## padrão reverso -  fundo branco, letra preta
title_ = '\33[1;33m' ## padrão reverso -  fundo branco, letra preta


def print_end():
    """  Mensagem de final de Programa.
        :Imprime no modo typewriter: delay entre letras.
    """ 
    print()
    typewriter('  .... ', pulalinha=False)
    typewriter(f'Mais uma conquista, siga em frente !! - {agora()}'    , cor=green_ , pulalinha=False)
    typewriter('  .... ', pulalinha=False)
    print()


def typewriter(palavra, tempo = 0.1, cor = default_, pulalinha=True):
    ''' Escreve a palavra letra por letra com delay.
        palavra    : imprime no comando print.
        tempo      : delay entre letras da palavra. 
        cor        : cor da palavra default_ = letra branca, fundo preto.
        pulalinha  : True ->pula linha e False -> não pula linha
    '''
    linha = '\n' if pulalinha else ''


    print(cor, end='')
    for letra in palavra:
        print(letra, end='')
        sleep(tempo)
        if letra in ',:"=!.':
            sleep(0.1)
    print(default_, end=linha)


def DB_ativo():
    ''' Verifica se Bd Correios está ativo '''
    try:
        conn = mysql.connect(host='localhost', database = 'correios', user ='root', password='')
        conn.close()
        return True, 'Pronto'
    except Error as erro:
        # print(f' Banco de dados com falha: {erro.msg}')
        return False, erro.msg

def Executa_SQL(pSQL, isList=False):
    ''' Executa comandos SQL se islist = True , pSQL contém uma lista de comandos SQL'''
    try:
        conn = mysql.connect(host='localhost', database = 'correios', user ='root', password='')
        cursor = conn.cursor()
        if not isList:
            cursor.execute(pSQL)     
        else:
            for sql in pSQL:
                cursor.execute(sql)

        conn.commit()
        cursor.close()
        conn.close()
        # print('\nConexão ao MySQL encerrada - Executa SQL.........', agora())   

    except Error as e:
        print('Erro ao acessar tabela compras: ', e)

def Busca_SQL(pSQL):
    ''' Faz Query do banco de dados correios - entra com SQL'''
    try:
        conn = mysql.connect(host='localhost', database = 'correios', user ='root', password='')
        cursor = conn.cursor()
        cursor.execute(pSQL)
        linhas = list()
        linhas = cursor.fetchall()
        cursor.close()
        conn.close()
        # print('\nConexão ao MySQL encerrada - Busca SQL.........', agora()) 

        return linhas

    except Error as e:
        print('Erro ao acessar tabela compras: ', e)


def Existe(campo , valor):
    ''' Verifica se o dado está cadastrado na tabela compras
        campo: campo da tabela compras
        valor: dado a ser verificadose já está cadastrado
    '''
    pSQL = f"Select count({campo}) from compras where {campo} = '{valor}' "
    linha = Busca_SQL(pSQL)
    if linha[0][0] > 0:
        return True
    else:
        return False


def Le_Arquivo_compras(bln_print):
    ''' Acessa BD correios e lê tabela compras: registra as compras e códigos de rastreio '''
    pSQL = 'select id,nome,produto, codigocp, statuscp, local from compras'
    
    linhas = list()
    linhas = Busca_SQL(pSQL)
    rastreios = list()
    for item in linhas:
        rast = dict()
        rast['id'] = item[0]
        rast['nome'] = item[1]
        rast['produto'] = item[2]
        rast['codigo'] = item[3]
        rast['status'] = item[4]
        rast['local'] = item[5]
        rastreios.append(rast)

    if bln_print:    
        print('-'*50)
        print('** Rastreio de compras pelo Correios **')
        print('-'*70)
        print('')
        for item in rastreios:
            print('{0:3}: {1:10}: {2:25}: {3:12}'.format(item['id'], item['nome'], item['produto'], item['codigo']))
            print('-'*70)          
        print()

    return rastreios  ## retorna um uma lista contendo produto e codigo em formato de dicionário


def Limpa_mens(mens):
    ''' Limpa mensagem - sintetiza a mensagem para exibição '''
    msgs = ['Informar nº do documento para a fiscalização e entrega do seu objeto. Clique aqui Minhas' ,
            'por favor aguarde de ','por favor aguarde de ',
            'Acesse o ambiente Minhas Importações',
            'Acesse o ambiente Minhas Importações',
            'Unidade de Tratamento em',
            'Unidade de Distribuição em',
            'País em',
            'País em Unidade de Tratamento Internacional /',
            'Unidade de Tratamento Internacional',
            'Importações',
            'Consulte os prazos clicando aqui.'
            ]
    for msg in msgs:  ## limpa mens, deixando o essencial
        if msg in mens:
            mens = mens.replace(msg,'')   
    mens = mens.replace(' / ', '-').replace('  ', ' ').replace('-para -',' para ')
    mens = mens.replace('para','-->>')
    return mens


def Gera_status(mens):
    ''' Dá tratamento às mensagem postada pelo correio, 
       sintetiza para otimizar as mensagens '''
    ## Mensgens do correioclear
    msg_entregue = 'Objeto entregue ao destinatário'
    msg_entrega = 'Objeto saiu para entrega ao destinatário'
    msg_pagamento = 'Aguardando pagamento'
    msg_pago = 'Pagamento confirmado'
    msg_fiscalizada = 'Fiscalização aduaneira finalizada'
    msg_fiscalizando = 'Encaminhado para fiscalização aduaneira'
    msg_transito = 'Objeto em trânsito -'
    msg_recebido = 'Objeto recebido pelos'
    msg_postado = 'Objeto postado'

    status = local = ''
    if msg_postado in mens:         ## postado pelo vendedor
        status = msg_postado

    elif msg_recebido in mens:      ## recebido no correio - pais de origem
        status = mens.replace(msg_recebido,'')

    elif msg_transito in mens:      ## em trânsito
        status = msg_transito
        local = mens.replace( msg_transito,'')

    elif msg_fiscalizando in mens:  ## fiscalizando
        status = msg_fiscalizando

    elif msg_pagamento in mens:     ## aguardando pagamento
        status = msg_pagamento
    
    elif msg_pago in mens:          ## pago
        status = msg_pago
    
    elif msg_fiscalizada in mens:   ## fiscalizado
        status = msg_fiscalizada

    elif msg_entrega in mens:       ## Entregando
        status = 'Saiu para entrega'
        local = 'Cond. Japy'

    elif msg_entregue in mens:      ## Entregou
        status = '## Já Chegou!!! ##'.upper()
        local = 'Cond. Japy'

    local = local.replace('/','')
    msg_status = dict()
    msg_status['status'] = status.strip()
    msg_status['local'] = local.strip()
    return msg_status


def Correios_Rastreio (rastreios):
    ''' Rastreia os produtos usando respectivo código
     de rastreio através do site dos Correios '''

    msg_entregue = 'Objeto entregue ao destinatário'
    msg_fim = '===>>>> E N T R E G U E <<<<==='
    # print()

    compras = list()
    relatorio = list()
    for item in rastreios:
        rast = dict()
        infos = correios(item['codigo'])  ## chamada da api correios, devolve 

        tag_fim = aviso = status = data = local = ''
        i = 0
        for info in infos:
            info['idprod'] = item['id']
            info['nome'] = item['nome']
            info['produto'] = item['produto']
            info['codigo'] = item['codigo']
            
            mens = Limpa_mens(info['mensagem'])
            info['mensagem'] = mens
            
            if msg_entregue in mens:  # produto chegou 
                tag_fim = msg_fim + " " + item['produto'].upper() + " ...>>> "

            mens_prt = "{0} {1} -> {2:15}:  {3} {4}".format(info['data'],  info['hora'],
                          info['local'].replace(' / ','-').replace(' /',''), mens, tag_fim) ## fim     
            tag_fim =''

            if i == 0:
                data = info['data'] + '|' + info['hora']
                msg_status = Gera_status(mens)
                status = msg_status['status']
                local = msg_status['local']
            i +=1
            tag_fim= ""

        rast['id'] = item['id']
        rast['nome'] = item['nome']
        rast['produto'] = item['produto']  ## dados para atualizar dados sobre status e local do produto
        rast['codigo'] = item['codigo']
        rast['status'] = status
        rast['data'] = data[0:10]
        rast['hora'] = data[11:]
        rast['local'] = local
        compras.append(rast)

        relatorio += infos
    return compras , relatorio ## dado atualizados da tabela compras - statuscp e 


def Update_Status(compras):
    ''' Atualiza tabela compras com informações de sobre o ultimo status do produto '''
    pSQL = list()
    for item in compras: # Atualiza compras com informações de status, local 


        sql = "update compras set statuscp='{0}', datast='{1}', hora='{2}', local='{3}' \
          where id='{4}'".format( item['status'], convfdate(item['data']) ,
           item['hora'], item['local'], item['id'])         
        pSQL.append(sql)
    Executa_SQL(pSQL, True)  ## Atualiza a tabela compras com status e local
    print('\nConexão ao MySQL encerrada - Update_Status SQL.........', agora()) 
    
def Upload_Rastreio(infos):
    ''' Executa comandos SQL se islist = True , pSQL contém uma lista de comandos SQL'''
    try:
        conn = mysql.connect(host='localhost', database = 'correios', user ='root', password='')
        cursor = conn.cursor()
        pSQL ='Truncate table rastreios'
        cursor.execute(pSQL)
        conn.commit()

        for info in infos:
            pSQL = "insert into rastreios \
(idprod, nome, produto, codigo, data, hora, local, mens) values\
('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(\
info['idprod'], info['nome'], info['produto'], info['codigo'],\
strdate(info['data']), info['hora'], info['local'], info['mensagem']) 

            cursor.execute(pSQL)    

    except Error as e:
        print('Erro ao acessar tabela rastreios: ', e)

    finally:
       if conn.is_connected():
            
            conn.commit()
            cursor.close()
            conn.close()
            print('\nConexão ao MySQL encerrada - Update_Rastreio SQL.........', agora())    


def Print_Rastreios(nlin=100):
    ''' Consulta tabela rastreios '''
    ''' campos : idprod, nome, produto, codigo, data, hora, local, mens'''
 
    pSQL ='Select * from rastreios order by idrst'
    rastreios = Busca_SQL(pSQL)
    id = 0
    print()
    print(f'{bold_}Rastreio dos Correios{default_}: {green_}{agora()}{default_} ')
    lin = 0
    for linha in rastreios:
        if id != linha[1]:
            print('-'*120)
            print()
            sleep(1)
            print(f" # {linha[1]} -->> {linha[2]}:{green_} {linha[3]}{default_} # {yellow_} {linha[4]}{default_} # ")
            print('='*120)
            id = linha[1]
            lin = 0

        if lin < nlin:
            lin += 1
            if lin==1:
                print(f" {yellow_} {convfdatastr(linha[5])} {linha[6]} -> {linha[7]:15}: {linha[8]:90}{default_}")
                sleep(1)
            else:
                print(f"  {convfdatastr(linha[5])} {linha[6]} -> {linha[7]:15}: {linha[8]:90}")
    print('-'*120)


def Print_Status():
    ''' Consulta tabela compras '''
    ''' campos : id, nome, produto, datacp, codigocp, statuscp, datast, hora, local, comentario'''
    '''           0   1      2        3        4          5       6       7     8       9  '''
    pSQL ='Select * from compras order by id'
    compras = Busca_SQL(pSQL)
    print()
    print()
    print(f' # Status de rastreio dos Correios # {green_}{agora()}{default_} ')
    for linha in compras:
        print('_'*130)
        print(f" {linha[0]:2}: ({linha[1]}):{green_} {linha[2]:22}{default_} : {linha[4]:13} : \
{green_}{convfdata(linha[6]):8}|{str(linha[7])[0:5]}{default_} -->>> {linha[5]:20} :{redbold_} {linha[8]:18}{default_}")
    print('_'*130)


def atualiza_correios():
    compras = list()
    infos = list()
    rastreios = list()  ## dados sobre compras - produto codigo
    rastreios = Le_Arquivo_compras(False)  # false não imprime entrada - entrada no banco de dados correios
    compras, infos = Correios_Rastreio (rastreios)  ## rastreia produtos no correiso rastreio e imprime a pesquisa e gera saída para gravar tabela rastreio
    Update_Status(compras)
    print(f'{green_}... atualizando status (compras) ...{default_}')
    Upload_Rastreio(infos)
    print(f'{green_}... atualizando (rastreios) ...{default_}')
    sleep(3)

def Editar_Compras():
    ''' Inserir, alterar e deletar registros da tabela compras '''
    print()
    print(f'{green_} Programa de Manutenção de Compras{default_}')
    print('¨'*40)
    print(f' {yellow_}(1):{default_} Inserir dados ')
    print(f' {yellow_}(2):{default_} Alterar dados ')
    print(f' {yellow_}(3):{default_} Deletar compras ')
    print('¨'*40) 

    while True:   
        print(f'  Escolha uma opção? [{yellow_}99-sair{default_}]: ', end='') 
        escolha = str(input(''))
        if escolha.isnumeric():
            escolha = int(escolha)

        if escolha == 1: ## Inserir dados
            Insere_Compras() 
            break
        elif escolha == 2: ## Alterar dados 
            Altera_Compras()
            break
        elif escolha == 3: ## Deletar compras 
            Deleta_Compras()
            break
        elif escolha == 99:
            break
        else:
            print()
            print(' .... Opção inválida, escolher outra...')  
            sleep(3)


def Insere_Compras():
    ''' Insere compras   Insert into compras '''
    while True:
        print()
        print(' Inserindo Novas de Compras')
        print('¨'*40)  
        nome = str(input(' Quem comprou : '))
        produto = str(input(' Produto: ')).strip()
        data = str(input(' Data: '))

        if len(data) > 0:
            data = strdate(data)
        while True:
            codigo = str(input(' Código de Rastreio: '))
            if not Existe('codigocp', codigo):
                break
            else:
                print(" Código já cadastrado, outro!! ")
    
        if len(produto) > 0:
            pSQL = f"insert into compras \
(nome, produto, datacp, codigocp, statuscp, datast, hora, local, comentario) values \
('{nome}', '{produto}', '{data}', '{codigo}', '{''}', '{''}', '{''}', '{''}', '{''}')"            
            Executa_SQL(pSQL)
            print( '     ... Inserido uma nova compra ...')
            print()
            sleep(3)
            Print_Status()
        else:
            print('  ... Produto em branco, não será cadastrado. ...')  
            print()  
        if str(input(' ... Quer inserir mais compras? [S/N]: ')) in 'nN':
            break

def Altera_Compras():
    '''Altera compras    Update compras'''
    while True:
        Print_Status()
        print()
        print(f' {green_}Alterando dados de Compras{default_}')
        print('¨'*40) 
        lista_id = Load_id_Compras()
        print(f' Quer modificar qual item: {green_}{lista_id}{default_} ou [{green_}99-Sair] ', end='')
        num = str(input())
        print(default_)

        if num.isnumeric():
            num = int(num)

        if num == 99:
            break
        elif num in lista_id :
            Print_id_Compras(num)
            sleep(1)
            print()
            campos = ['nome', 'produto', 'datacp', 'codigocp']
            valores = ["", "", "", ""]
            print(f' Quer mesmo modificar esta compra?{green_} [S/N]: ',end='')
            if str(input('')) in 'sS':
                print(default_)
                print(f'  Digite {green_}<enter>{default_} se não quiser modificar')
                str_set ='set'
                valores[0] = str(input(' Quem....: ')).strip()
                valores[1] = str(input(' Produto.: ')).strip()
                valores[2] = str(input(' Data....: ')).strip()
                while True:
                    valores[3] = str(input(' Código..: ')).strip()  
                    if not Existe('codigocp', valores[3] ):
                        break 
                    else:
                        print(f" {green_}Código já existe, digite outro ou deixe em branco.{default_} \n")
           
                for i in range(4):
                    if len(str(valores[i])) > 0:
                        str_set += f" {campos[i]} = '{valores[i]}'"

                    if i in [1,2]:
                        if len(str_set) > 5 and len(str(valores[i+1])):
                            str_set += ','     ## coloca virgula
                    if i+1 == 2:
                        if len(valores[2]) > 0:
                            valores[2] = strdate(valores[2]) 
                        
                if len(str_set) > 5:
                    pSQL = f"Update compras {str_set} where id = '{num}' "
                    print(pSQL)
                    Executa_SQL(pSQL)
                    sleep(3) 
                    Print_Status()
                    print(f' ... Quer Alterar mais algum?{green_} [S/N]: ', end='')
                    print(default_, end='')
                    if str(input()) in 'nN':
                        break 
                else:
                    print()
                    print(f' {green_} ---->>> {redbold_}Alteração cancelada em id={num}{default_}....')
        else:
            print()
            print(f'{redbold_} ... Escolher uma válida: {green_}{lista_id}{default_} ...')
 

def Deleta_Compras():  ## escolha == 3
    ''' Deleta compras  Delete from compras'''
    Print_Status()
    print()
    print(' ...  Deletando itens de Compras ...')
    print('¨'*40) 
    while True:
        lista_id = Load_id_Compras()
        sleep(2)
        num = int(input(f' ... Qual quer deletar {lista_id} ou [999-sair] '))
        if num == 99:
            break  
        else:           
            if num in lista_id:
                Print_id_Compras(num)
                sleep(1)
                if str(input(' Vai mesmo apagar esta compra? [S/N]}: ')) in 'sS':
                    pSQL = f"Delete from compras where id='{num}'"
                    Executa_SQL(pSQL)
                    print(f'     ... Deletado id={num} ... ')        
                sleep(3) 
                Print_Status()
            else:
                print(f' ... Escolha uma compra válida: {lista_id}') 
        print()
                
        if str(input(' ... Quer deletar mais algum? [S/N]: ')) in 'nN':
            break    


def Load_id_Compras():
    ''' Carrega os id's das compras '''
    pSQL = 'select id from compras order by id'
    linhas = Busca_SQL(pSQL)
    lt_id = list()
    for linha in linhas:
        lt_id.append(linha[0])
    return lt_id


def Print_id_Compras(num):
    ''' Localiza através do id a compra correspondente em compras '''
    if num > 0 :
        pSQL = f"Select id, nome, produto, codigocp from compras where id ='{num}'"
        linhas = Busca_SQL(pSQL)
        linha = linhas[0]
        print(f" {yellow_}   ----->> id={linha[0]}: {linha[1]} : {linha[2]} {linha[3]}{default_}")
    else:
        print(f' {redbold_}  Erro em Find_id_compras: num <= 0 {default_}')
        return ''


def main():

    myDB_ativo, mens_erro = DB_ativo()   ## verifica-se o DB Mysql está acessível

    if myDB_ativo is True:
        while True:
            print()
            # print('_'*40)
            print()
            print(f'{green_} Programa de Rastreio - Correios / BR {default_}')
            print('¨'*40)
            print(f' {yellow_} (1):{default_} Atualizar agora o rastreamento ')
            print(f' {yellow_} (2):{default_} Mostrar informação detalhada ')
            print(f' {yellow_} (3):{default_} Mostrar informação resumida ')
            print(f' {yellow_} (4):{default_} Editar dados de compras ')
            print('¨'*40)
            print(f'  Escolha uma opção? [{yellow_}99-sair{default_}]: ', end='') 
            escolha = str(input(''))
            if escolha.isnumeric():
                escolha  = int(escolha)
            print()
            if escolha == 1:
                atualiza_correios()
            elif escolha == 2:
                Print_Rastreios()
                sleep(2)
            elif escolha == 3:
                Print_Status()
                sleep(2)
            elif escolha == 4:
                Editar_Compras()
            elif escolha == 99:
                break
            else:
                print()
                print(f' ....{green_} Escolha uma opção válida {default_}....')
                sleep(2)

        print('-'*40)
        print()
        print_end()
        print()
    else:
        print()
        print()
        print(f'{green_} Programa de Rastreio - Correios / BR {default_}')
        print('¨'*40)
        print()
        print(f' {redbold_}... Encerrado por falha de coneção ao BD MySQL.{default_}')
        print(f' {red_}... Erro: {yellow_}{mens_erro}{default_}.')
        print(f'\n {green_}... Comunique ao Administrador sobre esta falha, obrigado.{default_}')
        print('¨'*70)
        print()
        sleep(15)

main()



