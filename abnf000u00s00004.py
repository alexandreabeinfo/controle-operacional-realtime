## ================================================================
## [abnf000u00s00004.py] - Arquivo de manipulação de banco de dados
## ================================================================

'''
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░          ░░        ░░░░          ░░        ░░░░          ░░          ░░          ░░  ░░░░░░  ░░  ░░░░░░░░░░  ░░  ░░░░░   ░░  ░░░░░░░░░░   ░░░░   ░░   ░░░░░  ░░          ░░          ░░          ░░          ░░          ░░          ░  ░░░░░░  ░░  ░░░░░░  ░░  ░░░░░░  ░░   ░░░░   ░░  ░░░░░░  ░░          ░░
░░  ░░░░░░  ░░  ░░░░░░  ░░  ░░░░░░░░░░  ░░░░░░  ░░  ░░░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░░░  ░░░░░░  ░░  ░░░░░░░░░░  ░░  ░░░   ░░░░  ░░░░░░░░░░    ░░    ░░    ░░░░  ░░  ░░░░░░  ░░  ░░░░░░  ░░  ░░░░░░  ░░  ░░░░░░  ░░  ░░░░░░░░░░░░░░  ░░░░░  ░░░░░░  ░░  ░░░░░░  ░░  ░░░░░░  ░░░░  ░░  ░░░░░  ░░░░  ░░░░░░░░░   ░░░
▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒  ▒   ▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒    ▒  ▒▒  ▒  ▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒    ▒▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒
▒▒          ▒▒  ▒▒    ▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒          ▒▒          ▒▒  ▒▒▒     ▒▒          ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒    ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒  ▒▒  ▒▒  ▒▒  ▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒          ▒▒  ▒▒▒▒▒▒  ▒▒          ▒▒          ▒▒▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒
▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒  ▒   ▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒  ▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒    ▒  ▒▒     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒  ▒▒▒▒  ▒▒▒  ▒    ▒  ▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒
██  ██████  ██  ██████  ██  ██████████  ██████  ██  ██████████  ██████████  ██████  ██  ██████  ██  ██  ██████  ██  ███   ████  ██████████  ██████  ██  ████    ██  ██████  ██  ██████████  ███     ██  ██    ████████████  ██████  █████  ██████  ████  ██  ████    ██    ████  ██  ████████  ███████   ████████
██  ██████  ██        ████          ██        ████          ██  ██████████          ██  ██████  ██  ██          ██  █████   ██          ██  ██████  ██  █████   ██          ██  ██████████          ██  ████    ██          ██████  █████          ██████  ██████  ██████  ██   ████   ██████  ██████          ██
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
'''

from flask_socketio import emit                         # Biblioteca do Flask-SocketIO (Websockets)
from datetime import date, datetime, time, timedelta    # Biblioteca de data e hora
from decimal import Decimal                             # Biblioteca para declarar variávels do tipo "decimal"

import mysql.connector                                  # Biblioteca para se comunicar com o MariaDB (pip install mysql-connector-python)
import shutil                                           # Biblioteca para manipular arquivos
import uuid                                             # Biblioteca do uuid.uuid4
import time                                             # Biblioteca do sleep

from abnfsrc.abnf000u00s00003 import *                  # Arquivo de funções comuns que serão utilizadas por todos os módulos do sistema
from abnfcfg import abnfcfg                             # Arquivo de configuração de ambiente

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_database_conexao_base_dados ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de conecção com a base de dados baseado no projeto.                                                                                          // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_database_conexao_base_dados(icodbase):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_database_conexao_base_dados (Acesso ao banco de dados do projeto)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bacesdba = False
    connecdb = None
    bvalidad = False
    print('Projeto .: ' + str(icodbase))
    # ///////////////////////////////////////////////////////////
    # Teste Sistema - Código de base: 000 - ab000 - MariaDB local
    # ///////////////////////////////////////////////////////////
    if icodbase == 0:
        sempresa = 'Teste Sistema'
        sdbuserx = abnfcfg.sdbus000
        sdbpassw = abnfcfg.sdbpw000
        sdblocal = abnfcfg.sdblc000
        sdbdatab = abnfcfg.sdbdb000
        bvalidad = True
    # /////////////////////////////////////////////////////////////
    # Tupi Transporte - Código de base: 100 - ab001 - MariaDB local
    # /////////////////////////////////////////////////////////////
    elif icodbase == 100:
        sempresa = 'Tupi Transporte'
        sdbuserx = abnfcfg.sdbus100
        sdbpassw = abnfcfg.sdbpw100
        sdblocal = abnfcfg.sdblc100
        sdbdatab = abnfcfg.sdbdb100
        bvalidad = True
    # //////////////////////////////////////////////////////////////////////
    # Rápido Sumaré Piracicaba - Código de base: 200 - gb001 - MariaDB local
    # //////////////////////////////////////////////////////////////////////
    elif icodbase == 200:
        sempresa = 'Rápido Sumaré Piracicaba'
        sdbuserx = abnfcfg.sdbus200
        sdbpassw = abnfcfg.sdbpw200
        sdblocal = abnfcfg.sdblc200
        sdbdatab = abnfcfg.sdbdb200
        bvalidad = True
    # ///////////////////////////////////////////////////////////
    # Trans Acreana - Código de base: 300 - ab003 - MariaDB local
    # ///////////////////////////////////////////////////////////
    elif icodbase == 300:
        sempresa = 'Trans Acreana'
        sdbuserx = abnfcfg.sdbus300
        sdbpassw = abnfcfg.sdbpw300
        sdblocal = abnfcfg.sdblc300
        sdbdatab = abnfcfg.sdbdb300
        bvalidad = True
    # //////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////
    if bvalidad:
        print('Empresa .: ' + sempresa)
        try:
            connecdb = mysql.connector.connect(
                user        = sdbuserx,
                password    = sdbpassw,
                host        = sdblocal,
                # port      = 1901,   Padrão: 3306
                database    = sdbdatab
            )
        except Exception as serrcone:
            print('Conexão .: Não foi possivel conectar com a base de dados!')
            abnf_socket_004([4, '', ''])
            abnf_socket_004([2, 'Não foi possivel conectar com a base de dados!', ''])
        else:
            print('Conexão .: Conectado a base de dados com sucesso!')
            bacesdba = True
    # //////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////
    return bacesdba, connecdb

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_database_busca_dados_v01 ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de busca de informações dentro de uma tabela do banco de dados.                                                                              // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_database_busca_dados_v01(icodbase, stabelax, scamposb, sfilbusc, sorderby):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_database_busca_dados_v01 (Buscando informações na base de dados)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    lsqlreto = []
    iqtdregs = 0
    bacesdba, connecdb = abnf_database_conexao_base_dados(icodbase)
    if bacesdba:
        cursordb = connecdb.cursor()
        scommsql = 'SELECT ' + scamposb + ' FROM ' + stabelax
        if sfilbusc != None:
            scommsql = scommsql + ' WHERE ' + sfilbusc
        if sorderby != None:
            scommsql = scommsql + ' ORDER BY ' + sorderby
        scommsql = scommsql + ';'
        print(scommsql)
        print('----------------------------------------------------------------------------------------------------------------------------------')
        cursordb.execute(scommsql)
        for lresusql in cursordb:
            lsqlreto.append(lresusql)
            iqtdregs += 1
            # print(lresusql)
    return lsqlreto, iqtdregs

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_database_busca_dados_v02 ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de busca de informações dentro de uma tabela do banco de dados.                                                                              // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_database_busca_dados_v02(icodbase, stabelax, lcamposb, lfilbusc, lorderby):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_database_busca_dados_v02 (Buscando informações na base de dados)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    # Nota: 05/08/2024
    # A lista "lcamposb" sempre tem que ser composta de, pelo menos, dois registros.
    # Caso necessite apenas de uma campo no retorno do SQL, então adicionar o elemento "None" no segundo registro.
    # Exemplo: lcamposb = ('idgrupo', None)
    # Isso porque se tivesse apenas um campo, o retorno seria o fracionamento de todas as letras deste campo ocasionando um erro no comando SQL.
    # Exemplo: lcamposb = ('idgrupo')  => Retorno: i,d,g,r,u,p,o.
    # Tomar cuidado que esse erro é comum de acontece e difícil de compreender o erro.
    # Exemplo abaixo de um erro ocasionado por esse problema:
    # mysql.connector.errors.ProgrammingError: 1054 (42S22): Unknown column 'i' in 'field list'
    lsqlreto = []
    iqtdregs = 0
    bacesdba, connecdb = abnf_database_conexao_base_dados(icodbase)
    if bacesdba:
        cursordb = connecdb.cursor()
        scommsql = 'SELECT '
        icontd01 = 0
        # abnf_show('05', lfilbusc, 0)
        for lauxi001 in lcamposb:
            if lauxi001 != None:
                if icontd01 > 0:
                    scommsql = scommsql + ', '
                scommsql = scommsql + lauxi001
                icontd01 += 1
        scommsql = scommsql + ' FROM ' + stabelax
        if lfilbusc != None:
            scommsql = scommsql + ' WHERE '
            sauxi001 = ' AND '
            icontd01 = 0
            for lauxi001 in lfilbusc:
                if lauxi001 == None:
                    pass
                elif lauxi001 == '[ChangeToOr]':
                    sauxi001 = ' OR '
                elif lauxi001 == '[ChangeToAnd]':
                    sauxi001 = ' AND '
                elif lauxi001 == '(':
                    scommsql = scommsql + lauxi001
                    icontd01 = 0
                elif lauxi001 == ')':
                    scommsql = scommsql + lauxi001
                else:
                    if icontd01 > 0:
                        scommsql = scommsql + sauxi001
                    scommsql = scommsql + lauxi001[0] + ' '
                    if lauxi001[1] in ('[InList]', '[NotInList]'):
                        icontd02 = 0
                        if   lauxi001[1] == '[InList]':    scommsql = scommsql + 'IN ('
                        elif lauxi001[1] == '[NotInList]': scommsql = scommsql + 'NOT IN ('
                        for lauxi002 in lauxi001[2]:
                            svalcamp = abnf_database_estrutura_converte_campos(stabelax, lauxi001[0], lauxi002)
                            if icontd02 > 0:
                                scommsql = scommsql + ','
                            scommsql = scommsql + svalcamp
                            icontd02 += 1
                        scommsql = scommsql + ')'
                    elif lauxi001[1] == '[Null]':
                        scommsql = scommsql + 'IS NULL'
                    elif lauxi001[1] == '[NotNull]':
                        scommsql = scommsql + 'IS NOT NULL'
                    else:
                        scommsql = scommsql + lauxi001[1] + ' '
                        svalcamp = abnf_database_estrutura_converte_campos(stabelax, lauxi001[0], lauxi001[2])
                        scommsql = scommsql + svalcamp
                    icontd01 += 1
        if lorderby != None:
            scommsql = scommsql + ' ORDER BY '
            icontd01 = 0
            for lauxi001 in lorderby:
                if lauxi001 != None:
                    if lauxi001 == '[Desc]':
                        scommsql = scommsql + ' DESC'
                        break
                    else:
                        if icontd01 > 0:
                            scommsql = scommsql + ', '
                        scommsql = scommsql + lauxi001
                        icontd01 += 1
        scommsql = scommsql + ';'
        print(scommsql)
        print('----------------------------------------------------------------------------------------------------------------------------------')
        # Debug: (inicio)
        # abnf_show('10', scommsql, 0)
        # Debug: (fim)
        cursordb.execute(scommsql)
        for lresusql in cursordb:
            lsqlreto.append(lresusql)
            iqtdregs += 1
            # print(lresusql)
    return lsqlreto, iqtdregs

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_database_executa_sql ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que executa um comando SQL no banco de dados.                                                                                                // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_database_executa_sql(icodbase, scommsql):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_database_executa_sql (Executa um comando SQL)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    lsqlreto = []
    iqtdregs = 0
    bacesdba, connecdb = abnf_database_conexao_base_dados(icodbase)
    if bacesdba:
        cursordb = connecdb.cursor()
        print(scommsql)
        print('----------------------------------------------------------------------------------------------------------------------------------')
        # Debug: (inicio)
        # abnf_show('10', scommsql, 0)
        # Debug: (fim)
        cursordb.execute(scommsql)
        for lresusql in cursordb:
            lsqlreto.append(lresusql)
            iqtdregs += 1
            # print(lresusql)
    return lsqlreto, iqtdregs
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_database_executa_sql_commit ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que executa um comando SQL com commit no banco de dados.                                                                                     // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_database_executa_sql_commit(icodbase, sabnproj, scommsql, iidusuar, slogiusu, snomeusu):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_database_executa_sql_commit (Executa um comando SQL com commit)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    lsqlreto = []
    bvalidad = False
    bacesdba, connecdb = abnf_database_conexao_base_dados(icodbase)
    if bacesdba:
        cursordb = connecdb.cursor()
        print(scommsql)
        print('----------------------------------------------------------------------------------------------------------------------------------')
        # Debug: (inicio)
        # abnf_show('10', scommsql, 0)
        # Debug: (fim)
        cursordb.execute(scommsql)
        try:
            connecdb.commit()
        except Exception as objerror:
            connecdb.rollback()
            abnf_alert('Erro durante a gravação do registro: ' + str(objerror), 4)
        else:
            bvalidad = True
            # Criando a frase para o log
            sfraslog = 'Foi executado um comando SQL com commit no banco de dados'
            # Gerando a lista dinâmica para o log
            abnf_websocket_log(
                sabnproj[14:],
                600,
                'idusuar',
                iidusuar,
                slogiusu,
                snomeusu,
                sfraslog,
                scommsql,
                None,
            )
    return bvalidad

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_database_valor_maximo_campo ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que traz o valor máximo de um campo de uma tabela do banco de dados.                                                                         // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_database_valor_maximo_campo(icodbase, stabelax, scamposb, iidfilia):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_database_valor_maximo_campo (Buscando o valor máximo de um campo em uma determinada tabela)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    ivalmaxi = 0
    bacesdba, connecdb = abnf_database_conexao_base_dados(icodbase)
    if bacesdba:
        cursordb = connecdb.cursor()
        scommsql = 'SELECT MAX(' + scamposb + ') FROM ' + stabelax
        if iidfilia != None: scommsql = scommsql + ' WHERE idfilia = ' + str(iidfilia)
        scommsql = scommsql + ';'
        print(scommsql)
        print('----------------------------------------------------------------------------------------------------------------------------------')
        cursordb.execute(scommsql)
        for lresusql in cursordb:
            if lresusql[0] != None:
                ivalmaxi = lresusql[0]
    return ivalmaxi

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_database_valor_maximo_campo_condicoes ] /////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que traz o valor máximo de um campo de uma tabela do banco de dados através de uma lista de condições.                                       // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_database_valor_maximo_campo_condicoes(icodbase, stabelax, scamposb, lcondico):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_database_valor_maximo_campo_condicoes (...)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    ivalmaxi = 0
    bacesdba, connecdb = abnf_database_conexao_base_dados(icodbase)
    if bacesdba:
        cursordb = connecdb.cursor()
        scommsql = 'SELECT MAX(' + scamposb + ') FROM ' + stabelax + ' WHERE '
        sauxi001 = ''
        for lauxi001 in lcondico:
            if lauxi001 != None:
                if sauxi001 != '': sauxi001 = sauxi001 + ' AND '
                sauxi001 = sauxi001 + lauxi001[0] + lauxi001[1] + str(lauxi001[2])
        scommsql = scommsql + sauxi001 + ';'
        print(scommsql)
        print('----------------------------------------------------------------------------------------------------------------------------------')
        cursordb.execute(scommsql)
        for lresusql in cursordb:
            if lresusql[0] != None:
                ivalmaxi = lresusql[0]
    return ivalmaxi

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_database_insere_dados_v01 ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função para salvar novos registros dentro de uma tabela do banco de dados.                                                                          // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_database_insere_dados_v01(icodbase, sabnproj, stabelax, sgenerot, sdesctab, iidusucr, slogiusu, snomeusu, linsregs):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_database_insere_dados_v01 (Salvando novas informações na base de dados)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad = False
    bacesdba, connecdb = abnf_database_conexao_base_dados(icodbase)
    if bacesdba:
        cursordb = connecdb.cursor()
        scommsql = 'INSERT INTO ' + stabelax + ' (' # + sprimkey
        icontd01 = 0
        for lauxi001 in linsregs:
            svirgula = '' if icontd01 == 0 else ', '
            scommsql = scommsql + svirgula + lauxi001[0]
            icontd01 += 1
        scommsql = scommsql + ', idusucr, dtregcr) VALUES ('    # + str(iproxiid)
        icontd01 = 0
        for lauxi001 in linsregs:
            svirgula = '' if icontd01 == 0 else ', '
            if lauxi001[1] == 'K':
                iproxiid = abnf_database_valor_maximo_campo(icodbase, stabelax, lauxi001[0], None) + 1
                scommsql = scommsql + svirgula + str(iproxiid)
                lauxi001[2] = iproxiid
            elif lauxi001[1] == 'N':
                scommsql = scommsql + svirgula + str(lauxi001[2])               # Number
            elif lauxi001[1] == 'S':
                scommsql = scommsql + svirgula + '"' + str(lauxi001[2]) + '"'   # String
            icontd01 += 1
        scommsql = scommsql +  ', ' + str(iidusucr) + ', CURRENT_TIMESTAMP());'
        # Executando o comando SQL
        print(scommsql)
        print('----------------------------------------------------------------------------------------------------------------------------------')
        # Debug: abnf_divisor(2, 2, 10)
        bvalidad = False
        cursordb.execute(scommsql)
        try:
            connecdb.commit()
        except Exception as objerror:
            connecdb.rollback()
            abnf_alert('Erro durante a gravação do registro: ' + str(objerror), 4)
        else:
            if cursordb.rowcount == 0:
                abnf_alert('Erro durante a gravação do registro! Entre em contato com o departamento de sistemas!', 4)
            else:
                bvalidad = True
                # Criando a frase para o log
                sfraslog = None
                if   sgenerot == 'M': sfraslog = 'Foi inserido um novo registro no ' + sdesctab
                elif sgenerot == 'F': sfraslog = 'Foi inserido um novo registro na ' + sdesctab
                # Gerando a lista dinâmica para o log
                ldinalog = []
                for lauxi001 in linsregs:
                    ldinalog.append([
                        stabelax,
                        lauxi001[0],
                        lauxi001[2],
                        lauxi001[3],
                        None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                        None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                        None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                    ])
                if sfraslog != None and ldinalog != []:
                    bvalidad = True
                    abnf_websocket_log(
                        sabnproj[14:],
                        300,
                        stabelax,
                        'idusuar',
                        iidusucr,
                        slogiusu,
                        snomeusu,
                        sfraslog,
                        ldinalog,
                    )
    return bvalidad, iproxiid

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_database_insere_dados_v02 ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função para salvar novos registros dentro de uma tabela do banco de dados.                                                                          // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_database_insere_dados_v02(icodbase, sabnproj, stabelax, iidusucr, slogiusu, snomeusu, linsregs):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_database_insere_dados_v02 (Salvando novas informações na base de dados)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad = False
    sgenerot = None
    sdesctab = None
    schavpri = None
    iproxiid = None
    bacesdba, connecdb = abnf_database_conexao_base_dados(icodbase)
    if bacesdba:
        ldbtabel, ldbstruc = abnf_database_estrutura()
        # Definindo o nome e o gênero da tabela:
        for lauxi001 in ldbtabel:
            if lauxi001[0] == stabelax:
                sgenerot = lauxi001[1]
                sdesctab = lauxi001[2]
                break
        # Definindo o campo de chave primária e valor a ser inserido neste campo:
        for lauxi001 in ldbstruc:
            if lauxi001[0] == stabelax:
                if lauxi001[2] == 'key':
                   schavpri = lauxi001[1]
                   iproxiid = abnf_database_valor_maximo_campo(icodbase, stabelax, schavpri, None) + 1
                   break
        if sgenerot != None and sdesctab != None and schavpri != None and iproxiid != None:
            # Gerando o comando SQL:
            cursordb = connecdb.cursor()
            scommsql = 'INSERT INTO ' + stabelax + ' (' + schavpri
            for lauxi001 in linsregs:
                scommsql = scommsql + ', ' + lauxi001[0]
            scommsql = scommsql + ', idusucr, dtregcr) VALUES (' + str(iproxiid)
            for lauxi001 in linsregs:
                svalcamp = abnf_database_estrutura_converte_campos(stabelax, lauxi001[0], lauxi001[1])
                scommsql = scommsql + ', ' + svalcamp
            scommsql = scommsql +  ', ' + str(iidusucr) + ', CURRENT_TIMESTAMP());'
            # abnf_show('09', scommsql, 0)
            # Executando o comando SQL
            print(scommsql)
            print('----------------------------------------------------------------------------------------------------------------------------------')
            # Debug: abnf_divisor(2, 2, 10)
            # abnf_show('07', scommsql, 0)
            cursordb.execute(scommsql)
            try:
                connecdb.commit()
            except Exception as objerror:
                connecdb.rollback()
                abnf_alert('Erro durante a gravação do registro: ' + str(objerror), 4)
            else:
                if cursordb.rowcount == 0:
                    abnf_alert('Erro durante a gravação do registro! Entre em contato com o departamento de sistemas!', 4)
                else:
                    bvalidad = True
                    # Criando a frase para o log
                    sfraslog = None
                    if   sgenerot == 'M': sfraslog = 'Foi inserido um novo registro no ' + sdesctab
                    elif sgenerot == 'F': sfraslog = 'Foi inserido um novo registro na ' + sdesctab
                    # Gerando a lista dinâmica para o log
                    ldinalog = []
                    # Inserindo o campo chave no log
                    ldinalog.append([
                        stabelax,
                        schavpri,
                        iproxiid,
                        'ID do registro',
                        None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                        None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                        None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                    ])
                    # Inserindo os demais campos
                    for lauxi001 in linsregs:
                        # Buscando a descrição do campo
                        sdefcamp = ''
                        for lauxi002 in ldbstruc:
                            if lauxi002[0] == stabelax and lauxi002[1] == lauxi001[0]:
                                sdefcamp = lauxi002[5]
                                break
                        # Inserindo dados do campo no log
                        ldinalog.append([
                            stabelax,
                            lauxi001[0],
                            lauxi001[1],
                            sdefcamp,
                            None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                            None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                            None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                        ])
                    if sfraslog != None and ldinalog != []:
                        abnf_websocket_log(
                            sabnproj[14:],
                            300,
                            stabelax,
                            'idusuar',
                            iidusucr,
                            slogiusu,
                            snomeusu,
                            sfraslog,
                            ldinalog,
                        )
        else:
            smessage = 'Parametros incorretos para gravação do registro!'
            smessage = smessage + '<br>stabelax: ' + str(stabelax)
            smessage = smessage + '<br>sgenerot: ' + str(sgenerot)
            smessage = smessage + '<br>sdesctab: ' + str(sdesctab)
            smessage = smessage + '<br>schavpri: ' + str(schavpri)
            smessage = smessage + '<br>iproxiid: ' + str(iproxiid)
            abnf_alert(smessage, 4)
    return bvalidad, iproxiid

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_database_insere_dados_v02_importacao ] //////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função para salvar novos registros dentro de uma tabela do banco de dados (usado somente para importacao de dados).                                 // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_database_insere_dados_v02_importacao(icodbase, sabnproj, stabelax, iidusucr, slogiusu, snomeusu, linsregs):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_database_insere_dados_v02_importacao (Salvando novas informações na base de dados)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad = False
    sgenerot = None
    sdesctab = None
    schavpri = None
    iproxiid = None
    bacesdba, connecdb = abnf_database_conexao_base_dados(icodbase)
    if bacesdba:
        ldbtabel, ldbstruc = abnf_database_estrutura()
        # Definindo o nome e o gênero da tabela:
        for lauxi001 in ldbtabel:
            if lauxi001[0] == stabelax:
                sgenerot = lauxi001[1]
                sdesctab = lauxi001[2]
                break
        # Definindo o campo de chave primária e valor a ser inserido neste campo:
        for lauxi001 in ldbstruc:
            if lauxi001[0] == stabelax:
                if lauxi001[2] == 'key':
                   schavpri = lauxi001[1]
                   iproxiid = abnf_database_valor_maximo_campo(icodbase, stabelax, schavpri, None) + 1
                   break
        if sgenerot != None and sdesctab != None and schavpri != None and iproxiid != None:
            # Gerando o comando SQL:
            cursordb = connecdb.cursor()
            scommsql = 'INSERT INTO ' + stabelax + ' (' + schavpri
            for lauxi001 in linsregs:
                scommsql = scommsql + ', ' + lauxi001[0]
            scommsql = scommsql + ', idusucr, dtregcr) VALUES (' + str(iproxiid)
            for lauxi001 in linsregs:
                svalcamp = abnf_database_estrutura_converte_campos(stabelax, lauxi001[0], lauxi001[1])
                scommsql = scommsql + ', ' + svalcamp
            scommsql = scommsql +  ', ' + str(iidusucr) + ', CURRENT_TIMESTAMP());'
            # abnf_show('09', scommsql, 0)
            # Executando o comando SQL
            print(scommsql)
            print('----------------------------------------------------------------------------------------------------------------------------------')
            # Debug: abnf_divisor(2, 2, 10)
            # abnf_show('07', scommsql, 0)
            cursordb.execute(scommsql)
            try:
                connecdb.commit()
            except Exception as objerror:
                connecdb.rollback()
                print('Erro durante a gravação do registro: ' + str(objerror))
                exit()
            else:
                if cursordb.rowcount == 0:
                    print('Erro durante a gravação do registro! Entre em contato com o departamento de sistemas!')
                    exit()
                else:
                    bvalidad = True
                    # Criando a frase para o log
                    sfraslog = None
                    if   sgenerot == 'M': sfraslog = 'Foi inserido um novo registro no ' + sdesctab
                    elif sgenerot == 'F': sfraslog = 'Foi inserido um novo registro na ' + sdesctab
                    # Inserindo os demais campos
                    for lauxi001 in linsregs:
                        # Buscando a descrição do campo
                        sdefcamp = ''
                        for lauxi002 in ldbstruc:
                            if lauxi002[0] == stabelax and lauxi002[1] == lauxi001[0]:
                                sdefcamp = lauxi002[5]
                                break
        else:
            print('Parametros incorretos para gravação do registro!')
            exit()
    return bvalidad, iproxiid

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_database_altera_dados_v01 ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função para alterar registros existentes dentro de uma tabela do banco de dados.                                                                    // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_database_altera_dados_v01(icodbase, sabnproj, stabelax, sgenerot, sdesctab, iidusual, slogiusu, snomeusu, lfilbusc, laltregs):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_database_altera_dados_v01 (Alterando informações na base de dados)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad = False
    bacesdba, connecdb = abnf_database_conexao_base_dados(icodbase)
    if bacesdba:
        cursordb = connecdb.cursor()
        scommsql = 'UPDATE ' + stabelax + ' SET '
        icontd01 = 0
        for lauxi001 in laltregs:
            if icontd01 > 0:
                scommsql = scommsql + ', '
            if   lauxi001[1] == 'I': scommsql = scommsql + lauxi001[0] + ' = '  + str(lauxi001[2])          # Integer
            elif lauxi001[1] == 'S': scommsql = scommsql + lauxi001[0] + ' = "' + str(lauxi001[2]) + '"'    # String
            icontd01 += 1
        scommsql = scommsql + ', idusual = ' + str(iidusual)
        scommsql = scommsql + ', dtregal = CURRENT_TIMESTAMP()'
        scommsql = scommsql + ' WHERE '
        icontd01 = 0
        for lauxi001 in lfilbusc:
            if icontd01 > 0:
                scommsql = scommsql + ' AND '
            if   lauxi001[1] == 'I': scommsql = scommsql + lauxi001[0] + ' = '  + str(lauxi001[2])          # Integer
            elif lauxi001[1] == 'S': scommsql = scommsql + lauxi001[0] + ' = "' + str(lauxi001[2]) + '"'    # String
            icontd01 += 1
        scommsql = scommsql + ';'
        # Executando o comando SQL
        print(scommsql)
        print('----------------------------------------------------------------------------------------------------------------------------------')
        # Debug: abnf_divisor(2, 2, 10)
        bvalidad = False
        cursordb.execute(scommsql)
        try:
            connecdb.commit()
        except Exception as objerror:
            connecdb.rollback()
            abnf_alert('Erro durante a gravação do registro: ' + str(objerror), 4)
        else:
            if cursordb.rowcount == 0:
                abnf_alert('Erro durante a gravação do registro! Entre em contato com o departamento de sistemas!', 4)
            else:
                bvalidad = True
                # Criando a frase para o log
                sfraslog = None
                if   sgenerot == 'M': sfraslog = 'Foi alterado um registro no ' + sdesctab
                elif sgenerot == 'F': sfraslog = 'Foi alterado um registro na ' + sdesctab
                # Gerando a lista dinâmica para o log
                ldinalog = []
                for lauxi001 in lfilbusc:
                    ldinalog.append([
                        stabelax,
                        lauxi001[0],
                        lauxi001[2],
                        lauxi001[3],
                        None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                        None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                        None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                    ])
                for lauxi001 in laltregs:
                    ldinalog.append([
                        stabelax,
                        lauxi001[0],
                        lauxi001[2],
                        lauxi001[3],
                        None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                        None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                        None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                    ])
                if sfraslog != None and ldinalog != []:
                    bvalidad = True
                    abnf_websocket_log(
                        sabnproj[14:],
                        400,
                        stabelax,
                        'idusuar',
                        iidusual,
                        slogiusu,
                        snomeusu,
                        sfraslog,
                        ldinalog,
                    )
    return bvalidad

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_database_altera_dados_v02 ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função para alterar registros existentes dentro de uma tabela do banco de dados.                                                                    // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_database_altera_dados_v02(icodbase, sabnproj, stabelax, iidregis, iidusual, slogiusu, snomeusu, laltregs, bignsalt = True):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_database_altera_dados_v02 (Alterando informações na base de dados)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    # Debug: (inicio)
    # abnf_show('10', laltregs, 1)
    # Debug: (fim)
    bvalidad = False
    sgenerot = None
    sdesctab = None
    schavpri = None
    bacesdba, connecdb = abnf_database_conexao_base_dados(icodbase)
    if bacesdba:
        ldbtabel, ldbstruc = abnf_database_estrutura()
        # Definindo o nome e o gênero da tabela:
        for lauxi001 in ldbtabel:
            if lauxi001[0] == stabelax:
                sgenerot = lauxi001[1]
                sdesctab = lauxi001[2]
                break
        # Definindo o campo de chave primário:
        for lauxi001 in ldbstruc:
            if lauxi001[0] == stabelax:
                if lauxi001[2] == 'key':
                   schavpri = lauxi001[1]
                   break
        if sgenerot != None and sdesctab != None and schavpri != None:
            # Buscando o registro e criando a lista ("lcompara") que irá conferir se houve alteração no registro:
            lcamposb = []
            lcompara = []
            for lauxi001 in laltregs:
                lcamposb.append(lauxi001[0])
                stipocam = ''
                for lauxi002 in ldbstruc:
                    if lauxi002[0] == stabelax:
                        if lauxi002[1] == lauxi001[0]:
                            stipocam = lauxi002[2]
                lcompara.append([lauxi001[0], lauxi001[1], stipocam, None, False])
            lfilbusc = ((schavpri, '=', iidregis), None)
            lorderby = None
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, stabelax, lcamposb, lfilbusc, lorderby)
            if lsqlre01 == [] or iqtdre01 == 0:
                abnf_alert('Não foi possível encontrar o registro! Entre em contato com o departamento de sistemas!', 4)
            else:
                icontd01 = 0
                for lauxi001 in lcompara:
                    lcompara[icontd01][3] = lsqlre01[0][icontd01]
                    icontd01 += 1
            # Analisando "lcompara" para saber se houve alteração em algum campo do registro:
            bfezalte = False
            for lauxi001 in lcompara:
                # Conversão de varíaveis do tipo "varchar" para poder realizar a comparação:
                if lauxi001[2] == 'varchar':
                    if lauxi001[1] != None:
                        lauxi001[1] = str(lauxi001[1])
                # Conversão de varíaveis do tipo "integer" para poder realizar a comparação:
                if lauxi001[2] == 'int':
                    if lauxi001[1] != None:
                        lauxi001[1] = int(lauxi001[1])
                # Conversão de varíaveis do tipo "decimal" para poder realizar a comparação:
                if lauxi001[2] == 'decimal':
                    if lauxi001[1] != None:
                        lauxi001[1] = Decimal(str(lauxi001[1]))
                # Conversão de varíaveis do tipo "date" para poder realizar a comparação:
                elif lauxi001[2] == 'date':
                    if lauxi001[3] != None:
                        lauxi001[3] = lauxi001[3].strftime("%Y-%m-%d")
                    else:
                        lauxi001[3] = ''
                    # Debug: (inicio)
                    # abnf_alert(str(lauxi001[1]) + ' - ' + str(lauxi001[3]), 4)
                    # time.sleep(3)
                    # Debug: (fim)
                # Comparando dados do registro
                if lauxi001[2] != 'date':
                    if lauxi001[1] != lauxi001[3]:
                        lauxi001[4] = True  # Salva apenas para análise de debug
                        bfezalte = True
                        # Debug: (inicio)
                        # print('===========================================')
                        # print(lauxi001)
                        # print('===========================================')
                        # time.sleep(5)
                        # Debug: (fim)
                else:
                    sauxdate = str(lauxi001[1].year) + '-' + str(100 + lauxi001[1].month)[1:] + '-' + str(100 + lauxi001[1].day)[1:] if lauxi001[1] != None else ''
                    if sauxdate != lauxi001[3]:
                        lauxi001[4] = True  # Salva apenas para análise de debug
                        bfezalte = True
                        # Debug: (inicio)
                        # print('===========================================')
                        # print(lauxi001)
                        # print(sauxdate, ' - ', lauxi001[3])
                        # print('===========================================')
                        # time.sleep(5)
                        # Debug: (fim)
            # Debug: (inicio)
            # abnf_show('09', lcompara, 1)
            # bfezalte = False
            # Debug: (fim)
            if not bfezalte and bignsalt:
                # Alexandre - 21/05/2025
                # 'bignsalt' foi criado para evitar a comparação se algum dado foi alterado.
                # Ele não é um parâmetro obrigatório na função devido a ter uma declaração inicial logo na chamada da função.
                # Ele foi usado a primeira vez no programa 'abnfu13c00700.py' por ser necessário nesse programa passar dessa etapa para gravar outras tabelas secundárias.
                abnf_alert('Nenhuma informação foi alterada para que possa ser salva!', 5)
            else:
                cursordb = connecdb.cursor()
                scommsql = 'UPDATE ' + stabelax + ' SET '
                icontd01 = 0
                for lauxi001 in laltregs:
                    if icontd01 > 0:
                        scommsql = scommsql + ', '
                    svalcamp = abnf_database_estrutura_converte_campos(stabelax, lauxi001[0], lauxi001[1])
                    scommsql = scommsql + lauxi001[0] + ' = ' + svalcamp
                    icontd01 += 1
                scommsql = scommsql + ', idusual = ' + str(iidusual)
                scommsql = scommsql + ', dtregal = CURRENT_TIMESTAMP()'
                scommsql = scommsql + ' WHERE ' + schavpri + ' = ' + str(iidregis) + ';'
                # abnf_show('09', scommsql, 0)
                # Executando o comando SQL
                print(scommsql)
                print('----------------------------------------------------------------------------------------------------------------------------------')
                # Debug: abnf_divisor(2, 2, 10)
                cursordb.execute(scommsql)
                try:
                    connecdb.commit()
                except Exception as objerror:
                    connecdb.rollback()
                    abnf_alert('Erro durante a gravação do registro: ' + str(objerror), 4)
                else:
                    if cursordb.rowcount == 0:
                        abnf_alert('Erro durante a gravação do registro! Entre em contato com o departamento de sistemas!', 4)
                    else:
                        bvalidad = True
                        # Criando a frase para o log
                        sfraslog = None
                        if   sgenerot == 'M': sfraslog = 'Foi alterado um registro no ' + sdesctab
                        elif sgenerot == 'F': sfraslog = 'Foi alterado um registro na ' + sdesctab
                        # Gerando a lista dinâmica para o log
                        ldinalog = []
                        # Inserindo o campo chave no log
                        ldinalog.append([
                            stabelax,
                            schavpri,
                            iidregis,
                            'ID do registro',
                            None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                            None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                            None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                        ])
                        # Inserindo os demais campos
                        for lauxi001 in laltregs:
                            # Buscando a descrição do campo
                            sdefcamp = ''
                            for lauxi002 in ldbstruc:
                                if lauxi002[0] == stabelax and lauxi002[1] == lauxi001[0]:
                                    sdefcamp = lauxi002[5]
                                    break
                            # Inserindo dados do campo no log
                            ldinalog.append([
                                stabelax,
                                lauxi001[0],
                                lauxi001[1],
                                sdefcamp,
                                None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                                None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                                None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                            ])
                        if sfraslog != None and ldinalog != []:
                            abnf_websocket_log(
                                sabnproj[14:],
                                400,
                                stabelax,
                                'idusuar',
                                iidusual,
                                slogiusu,
                                snomeusu,
                                sfraslog,
                                ldinalog,
                            )
        else:
            smessage = 'Parametros incorretos para gravação do registro!'
            smessage = smessage + '<br>stabelax: ' + str(stabelax)
            smessage = smessage + '<br>sgenerot: ' + str(sgenerot)
            smessage = smessage + '<br>sdesctab: ' + str(sdesctab)
            smessage = smessage + '<br>schavpri: ' + str(schavpri)
            abnf_alert(smessage, 4)
    return bvalidad

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_database_registro_nao_ativo ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de verifica se um registro não esta ativo.                                                                                                   // #
# // Ele busca a chave do registro dentro de abnf_database_estrutura e utiliza a chave para chegar no registro.                                          // #
# // Encontrando o registro, retorna inválido se o campo 'situreg' não estiver com valor 'A'.                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_database_registro_nao_ativo(icodbase, stabelax, iidregis, sgenerot, sdesctab, lcamptab):
    bacesdba, connecdb = abnf_database_conexao_base_dados(icodbase)
    if bacesdba:
        bvalidad = True
        ldbtabel, ldbstruc = abnf_database_estrutura()
        schavpri = None
        for lauxi001 in ldbstruc:
            if lauxi001[0] == stabelax:
                if lauxi001[2] == 'key':
                   schavpri = lauxi001[1]
                   break
        if schavpri == None:
            abnf_alert('Não foi possível encontrar a chave primária do registro d' + ('o' if sgenerot == 'M' else 'a') + ' ' + sdesctab + '!', 4)
        else:
            lcamposb = ['situreg', lcamptab[0]]
            if lcamptab[1] != None: lcamposb.append(lcamptab[1])
            lfilbusc = ((schavpri, '=', iidregis), None)
            lorderby = None
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, stabelax, lcamposb, lfilbusc, lorderby)
            if lsqlre01 == [] or iqtdre01 == 0:
                sauxi001 = 'Não foi possível encontrar o registro d' + ('o' if sgenerot == 'M' else 'a') + ' ' + sdesctab + '! '
                sauxi001 = sauxi001 + 'Entre em contato com o departamento de sistemas!'
                abnf_alert(sauxi001, 4)
            else:
                # if lsqlre01[0][0] == 'A':   # <= Para teste! (resultado negativo)
                if lsqlre01[0][0] != 'A':
                    sauxi001 = ('O' if sgenerot == 'M' else 'A') + ' ' + sdesctab + ' '
                    sauxi001 = sauxi001 + str(lsqlre01[0][1])
                    if len(lcamposb) == 3: sauxi001 = sauxi001 + ' (' + str(lsqlre01[0][2]) + ')'
                    sauxi001 = sauxi001 + ' não esta ativ' + ('o' if sgenerot == 'M' else 'a') + '!'
                    abnf_alert(sauxi001, 4)
                else:
                    bvalidad = False
    return bvalidad

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_database_exclui_registro] ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função para excluir registros existentes dentro de uma tabela do banco de dados.                                                                    // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_database_exclui_registro(icodbase, sabnproj, stabelax, iidregis, iidusual, slogiusu, snomeusu):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_database_exclui_registro (Excluindo registros da base de dados)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad = False
    sgenerot = None
    sdesctab = None
    schavpri = None
    bacesdba, connecdb = abnf_database_conexao_base_dados(icodbase)
    if bacesdba:
        # Desabilita os botões comuns do form
        abnf_socket_004([10, 'btmodsav'])
        abnf_socket_004([10, 'btexclui'])
        abnf_socket_004([10, 'btcancel'])
        abnf_alert('Aguarde...', 15)
        ldbtabel, ldbstruc = abnf_database_estrutura()
        # Definindo o nome e o gênero da tabela:
        for lauxi001 in ldbtabel:
            if lauxi001[0] == stabelax:
                sgenerot = lauxi001[1]
                sdesctab = lauxi001[2]
                break
        # Definindo o campo de chave primária:
        for lauxi001 in ldbstruc:
            if lauxi001[0] == stabelax:
                if lauxi001[2] == 'key':
                   schavpri = lauxi001[1]
                   break
        if sgenerot != None and sdesctab != None and schavpri != None:
            # Buscando o registro e comparando para saber se houve alteração nos campos:
            lcamposb = [schavpri, None]
            lfilbusc = ((schavpri, '=', iidregis), None)
            lorderby = None
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, stabelax, lcamposb, lfilbusc, lorderby)
            if lsqlre01 == [] or iqtdre01 == 0:
                abnf_alert('Não foi possível encontrar o registro! Entre em contato com o departamento de sistemas!', 4)
            else:
                iqtdvinc, ltabvinc = abnf_database_registro_vinculos(icodbase, stabelax, schavpri, iidregis)
                if iqtdvinc > 0:
                    abnf_alert('Não é possível excluir este registro! Existem ' + str(iqtdvinc) + ' registro(s) vinculado(s) a ele!', 4)
                else:
                    cursordb = connecdb.cursor()
                    scommsql = 'UPDATE ' + stabelax + ' SET situreg = "C" '
                    scommsql = scommsql + ', idusual = ' + str(iidusual)
                    scommsql = scommsql + ', dtregal = CURRENT_TIMESTAMP()'
                    scommsql = scommsql + ' WHERE ' + schavpri + ' = ' + str(iidregis) + ';'
                    # abnf_show('09', scommsql, 0)
                    # Executando o comando SQL
                    print(scommsql)
                    print('----------------------------------------------------------------------------------------------------------------------------------')
                    # Debug: abnf_divisor(2, 2, 10)
                    cursordb.execute(scommsql)
                    try:
                        connecdb.commit()
                    except Exception as objerror:
                        connecdb.rollback()
                        abnf_alert('Erro durante a exclusão do registro: ' + str(objerror), 4)
                    else:
                        if cursordb.rowcount == 0:
                            abnf_alert('Erro durante a exclusão do registro! Entre em contato com o departamento de sistemas!', 4)
                        else:
                            bvalidad = True
                            # Criando a frase para o log
                            sfraslog = None
                            if   sgenerot == 'M': sfraslog = 'Foi excluido um registro no ' + sdesctab
                            elif sgenerot == 'F': sfraslog = 'Foi excluido um registro na ' + sdesctab
                            # Gerando a lista dinâmica para o log
                            ldinalog = []
                            # Inserindo o campo chave no log
                            ldinalog.append([
                                stabelax,
                                schavpri,
                                iidregis,
                                'ID do registro',
                                None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                                None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                                None,   # Analisar no futuro se da pra trabalhar nesses campos da lista dinâmica para o log
                            ])
                            if sfraslog != None and ldinalog != []:
                                abnf_websocket_log(
                                    sabnproj[14:],
                                    500,
                                    stabelax,
                                    'idusuar',
                                    iidusual,
                                    slogiusu,
                                    snomeusu,
                                    sfraslog,
                                    ldinalog,
                                )
        else:
            smessage = 'Parametros incorretos para gravação do registro!'
            smessage = smessage + '<br>stabelax: ' + str(stabelax)
            smessage = smessage + '<br>sgenerot: ' + str(sgenerot)
            smessage = smessage + '<br>sdesctab: ' + str(sdesctab)
            smessage = smessage + '<br>schavpri: ' + str(schavpri)
            abnf_alert(smessage, 4)
        # Habilita os botões comuns do form
        abnf_socket_004([5, 'btmodsav'])
        abnf_socket_004([5, 'btexclui'])
        abnf_socket_004([5, 'btcancel'])
    return bvalidad

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_database_registro_vinculos ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que cria uma lista mostrando os vinculos de um determinado registro com outras tabelas.                                                      // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_database_registro_vinculos(icodbase, stabelax, sregvinc, xregvalo):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_database_registro_vinculos (Busca vinculos de um determinado registro com outras tabelas)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    ldbtabel, ldbstruc = abnf_database_estrutura()
    sarqvinc = "abnftmp/abnf000u00s00004a.log"
    # Criando lista de registros vinculados conforme a lista 'ldbstruc':
    iqtdvinc = 0
    ltabvinc = []
    for lauxi001 in ldbstruc:
        if lauxi001[6] == stabelax and lauxi001[7] == sregvinc:
            ltabvinc.append([lauxi001[0], lauxi001[1], lauxi001[2], None])
    # Buscando registros vinculados (e não cancelados) conforme a lista 'ldbstruc':
    if ltabvinc != []:
        with open(sarqvinc, 'w') as sarquwri:
            for lauxi001 in ltabvinc:
                # ////////////////////////////////////////////////////////////////////////
                # O select abaixo verifica a existência da tabela dentro do banco de dados
                # Isso evita erros caso a tabela não exista mesmo constando na estrutura
                # ////////////////////////////////////////////////////////////////////////
                sauxi001 = 'SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = "' + lauxi001[0] + '"'
                lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
                if lsqlre01 != [] and iqtdre01 > 0:
                    lcamposb = [lauxi001[1], None]
                    lfilbusc = ((lauxi001[1], '=', xregvalo), ('situreg', '!=', 'C'))
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, lauxi001[0], lcamposb, lfilbusc, lorderby)
                    lauxi001[3] = iqtdre01
                    iqtdvinc += iqtdre01
                    if iqtdre01 > 0:
                        sarquwri.write(str(lauxi001) + '\n')
    return iqtdvinc, ltabvinc

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_database_menu ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função para criar menus de select ou dicionário de dados.                                                                                           // #
# // SOMENTE USAR ESTE FUNÇÂO QUANDO ENVOLTER SOMENTE UMA TABELA                                                                                         // #
# // QUANDO ENVOLVER MAIS DE UMA TABELA CRIAR A ROTINA EM "abnf_database_sqlx" DEVIDO A USAR JOIN                                                        // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_database_menu(icodbase, iidfilia, stiporet, sdefmenu, iparlini, iparfilt, iparorde):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_database_menu (Gerando dados para a criação de menus de select ou dicionário de dados)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    if   iparlini == 0: lmselect = []
    elif iparlini == 1: lmselect = [('','')]
    # ===> elif iparlini == 2: lmselect = [(0,'[ Manter o atual] ')]
    elif iparlini == 3: lmselect = [(0,'Todos')]
    if False: pass
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '0001':
        stabela1 = 'abnf_sistema_empresas_matrizes'
        scampos1 = 'idempre, codiemp'
        sfilbus1 = 'situreg = "A"'
        sorderb1 = 'codiemp, idempre'
        stabela2 = 'abnf_sistema_empresas_filiais'
        scampos2 = 'idfilia, idempre, codifil'
        sfilbus2 = 'situreg = "A"'
        sorderb2 = 'codifil, idfilia'
        lkeyjoin = (0, 1)                                                                           # Posição das chave que unem as duas tabelas
        sstruret = "str(1000 + lauxi001[1])[1:] + '/' + str(1000 + lauxi002[2])[1:]"                # Estrutura de retorno
        icodmont = 2
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '0001B':
        stabela1 = 'abnf_sistema_empresas_matrizes'
        scampos1 = 'idempre, nomeemp, codiemp'              					                    # Ordenar por ordem da descrição da matriz
        sfilbus1 = 'situreg = "A"'                                                                  # Registros ativos e inativos
        sorderb1 = 'codiemp, nomeemp, idempre'                                                      # Ordenar por ordem de código da matriz
        stabela2 = 'abnf_sistema_empresas_filiais'
        scampos2 = 'idfilia, idempre, nomefil, codifil'                                             # Ordenar por ordem da descrição da filial
        sfilbus2 = 'situreg = "A"'                                                                  # Registros ativos e inativos
        sorderb2 = 'codifil, nomefil, idfilia'                                                      # Ordenar por ordem de código da filial
        lkeyjoin = (0, 1)                                                                           # Posição das chave que unem as duas tabelas
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ') - ' + str(lauxi002[2]) + ' (' + str(lauxi002[3]) + ')'" # Estrutura de retorno
        icodmont = 2
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '0002':
        stabelax = 'abnf_sistema_usuarios'
        if   iparorde == 1: scamposb = 'idusuar, logiusu, nomeusu,'                                 # Ordenar por ordem de login do usuário
        elif iparorde == 2: scamposb = 'idusuar, nomeusu, logiusu'                                  # Ordenar por ordem do nome do usuário
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iparorde == 1: sorderby = 'logiusu, nomeusu, idusuar'                                  # Ordenar por ordem de login do usuário
        elif iparorde == 2: sorderby = 'nomeusu, logiusu, idusuar'                                  # Ordenar por ordem do nome do usuário
        sstruret = "str(lauxi001[1])"                                                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu in ('0101A', '0101B'):
        stabelax = 'abnf_cadastro_logradouros_cidades'
        if   iparorde == 1: scamposb = 'idcidad, codcida, descida, desesta'                         # Ordenar por ordem de código da cidade
        elif iparorde == 2: scamposb = 'idcidad, descida, desesta, codcida'                         # Ordenar por ordem de descrição
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iidfilia != None: sfilbusc = sfilbusc + ' AND idfilia = ' + str(iidfilia)
        if   iparorde == 1: sorderby = 'codcida, descida, desesta, idcidad'                         # Ordenar por ordem de código da cidade
        elif iparorde == 2: sorderby = 'descida, desesta, codcida, idcidad'                         # Ordenar por ordem de descrição
        if   sdefmenu == '0101A': sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"     # Estrutura de retorno
        elif sdefmenu == '0101B': sstruret = "(lauxi001[1], lauxi001[2], lauxi001[3])"              # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '0102':
        stabela1 = 'abnf_cadastro_logradouros_bairros'
        scampos1 = 'idbairr, desbair, codbair, idcidad'                                             # Ordenar por ordem da descrição do bairro
        sfilbus1 = 'situreg != "C"'                                                                 # Registros ativos e inativos
        sorderb1 = 'desbair, idbairr'                                                               # Ordenar por ordem da descrição do bairro
        stabela2 = 'abnf_cadastro_logradouros_cidades'
        scampos2 = 'idcidad, descida, desesta'                                                      # Ordenar por ordem da descrição da cidade
        sfilbus2 = 'situreg != "C"'                                                                 # Registros ativos e inativos
        sorderb2 = 'descida, idcidad'                                                               # Ordenar por ordem da descrição da cidade
        icodmont = 402
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '0103':
        stabela1 = 'abnf_cadastro_logradouros'
        scampos1 = 'idlogra, tiplogr, deslogr, codlogr, idbairr'    			                    # Ordenar por ordem de descrição do logradouro
        sfilbus1 = 'situreg != "C"'                                                                 # Registros ativos e inativos
        sorderb1 = 'tiplogr, deslogr, idlogra'                                                      # Ordenar por ordem de descrição do logradouro
        stabela2 = 'abnf_cadastro_logradouros_bairros'
        scampos2 = 'idbairr, desbair, idcidad'                                                      # Ordenar por ordem da descrição do bairro
        sfilbus2 = 'situreg != "C"'                                                                 # Registros ativos e inativos
        sorderb2 = 'desbair, idbairr'                                                               # Ordenar por ordem da descrição do bairro
        stabela3 = 'abnf_cadastro_logradouros_cidades'
        scampos3 = 'idcidad, descida, desesta'                                                      # Ordenar por ordem da descrição da cidade
        sfilbus3 = 'situreg != "C"'                                                                 # Registros ativos e inativos
        sorderb3 = 'descida, idcidad'                                                               # Ordenar por ordem da descrição da cidade
        icodmont = 403
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '0104':
        stabelax = 'abnf_cadastro_cpfcnpj'
        if   iparorde == 1: scamposb = 'idcpfpj, codpfpj, nomraso'                					# Ordenar por ordem de cpf
        elif iparorde == 2: scamposb = 'idcpfpj, nomraso, codpfpj'                					# Ordenar por ordem do nome
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        sfilbusc = sfilbusc + ' AND tippfpj = "F"'                                                  # Somente registros de pessoa física
        if   iparorde == 1: sorderby = 'codpfpj, nomraso, idcpfpj'                					# Ordenar por ordem de cpf
        elif iparorde == 2: sorderby = 'nomraso, codpfpj, idcpfpj'                					# Ordenar por ordem do nome
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '0105':
        stabelax = 'abnf_cadastro_cpfcnpj'
        if   iparorde == 1: scamposb = 'idcpfpj, codpfpj, nomraso'                					# Ordenar por ordem de cnpj
        elif iparorde == 2: scamposb = 'idcpfpj, nomraso, codpfpj'                					# Ordenar por ordem do nome/razão social
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        sfilbusc = sfilbusc + ' AND tippfpj = "J"'                                                  # Somente registros de pessoa jurídica
        if   iparorde == 1: sorderby = 'codpfpj, nomraso, idcpfpj'                					# Ordenar por ordem de cnpj
        elif iparorde == 2: sorderby = 'nomraso, codpfpj, idcpfpj'                					# Ordenar por ordem do nome/razão social
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '010A':                                                                        # Pessoa física e jurídica
        stabelax = 'abnf_cadastro_cpfcnpj'
        if   iparorde == 1: scamposb = 'idcpfpj, codpfpj, nomraso'                					# Ordenar por ordem de cnpj
        elif iparorde == 2: scamposb = 'idcpfpj, nomraso, codpfpj'                					# Ordenar por ordem do nome/razão social
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iparorde == 1: sorderby = 'codpfpj, nomraso, idcpfpj'                					# Ordenar por ordem de cnpj
        elif iparorde == 2: sorderby = 'nomraso, codpfpj, idcpfpj'                					# Ordenar por ordem do nome/razão social
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu in ['010B', '010C', '010D', '010E']:
        if   sdefmenu == '010B': stipclfo = 'C'
        elif sdefmenu == '010C': stipclfo = 'F'
        stabela1 = 'abnf_cadastro_cpfcnpj'
        scampos1 = 'idcpfpj, nomraso, codpfpj'
        sfilbus1 = 'situreg != "C"'
        sorderb1 = 'nomraso, idcpfpj'
        stabela2 = 'abnf_cadastro_clientes_fornecedores'
        scampos2 = 'idclfor, codclfo, idcpfpj, tipclfo'
        if sdefmenu in ['010D', '010E']: sfilbus2 = 'situreg != "C"'                                                                 # Registros ativos e inativos
        else:                            sfilbus2 = 'tipclfo = "' + stipclfo + ' " AND situreg != "C"'                               # Tipo de registro = clientes ou fornecedores / registros ativos e inativos
        sorderb2 = 'idclfor'
        lkeyjoin = (0, 2)                                                                                                            # Posição das chave que unem as duas tabelas
        if sdefmenu != '010E': sstruret = "str(lauxi001[1]) + ' (' + str(lauxi002[1]) + ')' + ' (' + str(lauxi001[2]) + ')'"         # Estrutura de retorno
        else:                  sstruret = "(lauxi001[1], lauxi002[1], lauxi001[2], lauxi002[3])"                                     # Estrutura de retorno
        icodmont = 2
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '0107':
        stabelax = 'abnf_cadastro_especies_documentos'
        if   iparorde == 1: scamposb = 'idespdo, sigespd, desespd'                                  # Ordenar por ordem de sigla da espécie de documento
        elif iparorde == 2: scamposb = 'idespdo, desespd, sigespd'                                  # Ordenar por ordem de descrição da espécie de documento
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iidfilia != None: sfilbusc = sfilbusc + ' AND idfilia = ' + str(iidfilia)
        if   iparorde == 1: sorderby = 'sigespd, desespd, idespdo'                                  # Ordenar por ordem de sigla da espécie de documento
        elif iparorde == 2: sorderby = 'desespd, sigespd, idespdo'                                  # Ordenar por ordem de descrição da espécie de documento
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu in ['0201', '0202', '0203']:
        stabelax = 'abnf_cadastro_veiculos'
        scamposb = 'idveicu, prefvei, placave'
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        elif iparfilt == 3: sfilbusc = 'situreg = "A" AND veielev = True'                           # Somente registros ativos do Elevar
        if iidfilia != None: sfilbusc = sfilbusc + ' AND idfilia = ' + str(iidfilia)
        sorderby = 'prefvei, idveicu'
        if   sdefmenu == '0201': sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"      # Estrutura de retorno para 0201
        elif sdefmenu == '0202': sstruret = "str(lauxi001[1])"                                      # Estrutura de retorno para 0202
        elif sdefmenu == '0203': sstruret = "lauxi001[1], lauxi001[2]"                              # Estrutura de retorno para 0203
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu in ['0301', '0301B']:
        stabela1 = 'abnf_cadastro_cpfcnpj'
        scampos1 = 'idcpfpj, nomraso, codpfpj'
        sfilbus1 = 'situreg != "C"'                                                                 # Registros ativos e inativos
        sorderb1 = 'nomraso, idcpfpj'
        stabela2 = 'abnf_cadastro_funcionarios'
        scampos2 = 'idfunci, codfunc, idcpfpj'
        if   sdefmenu == '0301':  sfilbus2 = 'situreg != "C"'                                       # Registros ativos e inativos
        elif sdefmenu == '0301B': sfilbus2 = 'situreg = "A"'                                        # Registros ativos
        # Nota: 13/07/2024
        # Nesse novo sistema vamos testar tirar o filtro de funcionários
        # por empresa quando 'iparfilt = 0'.
        # Vamos usar assim no lançamento de entrada/saída de veículos e analisar os resultados.
        if iparfilt == 1: sfilbus2 = sfilbus2 + ' AND idfilia = ' + str(iidfilia)
        sorderb2 = 'idfunci'
        lkeyjoin = (0, 2)                                                                           # Posição das chave que unem as duas tabelas
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi002[1]) + ')'"                               # Estrutura de retorno
        icodmont = 2
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '0401':
        stabelax = 'abnf_almoxarifado_cadastro_produtos_servicos_grupos'
        if   iparorde == 1: scamposb = 'idgrupo, codgrup, descgru'                					# Ordenar por ordem de código do grupo
        elif iparorde == 2: scamposb = 'idgrupo, descgru, codgrup'                					# Ordenar por ordem da descrição do grupo
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iparorde == 1: sorderby = 'codgrup, descgru, idgrupo'                					# Ordenar por ordem de código do grupo
        elif iparorde == 2: sorderby = 'descgru, codgrup, idgrupo'                					# Ordenar por ordem de descrição do grupo
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '0402':
        stabela1 = 'abnf_almoxarifado_cadastro_produtos_servicos_grupos'
        scampos1 = 'idgrupo, descgru, codgrup'              					                    # Ordenar por ordem da descrição do subgrupo
        sfilbus1 = 'situreg != "C"'                                                                 # Registros ativos e inativos
        if   iparorde == 1: sorderb1 = 'codgrup, descgru, idgrupo'                                  # Ordenar por ordem de código do grupo
        elif iparorde == 2: sorderb1 = 'descgru, codgrup, idgrupo'                                  # Ordenar por ordem de descrição do grupo
        stabela2 = 'abnf_almoxarifado_cadastro_produtos_servicos_subgrupos'
        scampos2 = 'idsubgr, idgrupo, descsub, codsubg'                                             # Ordenar por ordem da descrição do subgrupo
        sfilbus2 = 'situreg != "C"'                                                                 # Registros ativos e inativos
        if   iparorde == 1: sorderb2 = 'codsubg, descsub, idsubgr'                                  # Ordenar por ordem de código do subgrupo
        elif iparorde == 2: sorderb2 = 'descsub, codsubg, idsubgr'                                  # Ordenar por ordem de descrição do subgrupo
        lkeyjoin = (0, 1)                                                                           # Posição das chave que unem as duas tabelas
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ') - ' + str(lauxi002[2]) + ' (' + str(lauxi002[3]) + ')'" # Estrutura de retorno
        icodmont = 2
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '0403':
        stabelax = 'abnf_almoxarifado_cadastro_produtos_servicos_marcas'
        if   iparorde == 1: scamposb = 'idmarca, codmarc, descmar'                                  # Ordenar por ordem de código da marca
        elif iparorde == 2: scamposb = 'idmarca, descmar, codmarc'                                  # Ordenar por ordem de descrição da marca
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iparorde == 1: sorderby = 'codmarc, descmar, idmarca'                                  # Ordenar por ordem de código da marca
        elif iparorde == 2: sorderby = 'descmar, codmarc, idmarca'                                  # Ordenar por ordem de descrição da marca
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu in ['0404', '0405', '0406', '0407']:
        stabelax = 'abnf_almoxarifado_cadastro_produtos_servicos'
        if   iparorde == 1: scamposb = 'idprser, codprse, descprs, tiporeg, uniesto, ncmsbxx, cstxxxx'                          # Ordenar por ordem de código do produto/serviço
        elif iparorde == 2: scamposb = 'idprser, descprs, codprse, tiporeg, uniesto, ncmsbxx, cstxxxx'                          # Ordenar por ordem de descrição do produto/serviço
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                                                         # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                                                          # Somente registros ativos
        if   iparorde == 1: sorderby = 'codprse, descprs, idprser'                                                              # Ordenar por ordem de código do produto/serviço
        elif iparorde == 2: sorderby = 'descprs, codprse, idprser'                                                              # Ordenar por ordem de descrição do produto/serviço
        if   sdefmenu == '0404': sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                                  # Estrutura de retorno para 0404
        elif sdefmenu == '0405': sstruret = "(lauxi001[1], lauxi001[2], lauxi001[3], lauxi001[4], lauxi001[5], lauxi001[6])"    # Estrutura de retorno para 0405
        elif sdefmenu == '0406':
            sfilbusc = sfilbusc + ' and tiporeg = "P"'                                                                          # Filtra somente o que for produto
            sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                                                       # Estrutura de retorno para 0406
        elif sdefmenu == '0407':
            sfilbusc = sfilbusc + ' and tiporeg = "P" and perldve = "S"'                                                        # Filtra somente o que for produto com permissão de saída em lote por veículo
            sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                                                       # Estrutura de retorno para 0406
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '0410':
        stabelax = 'abnf_almoxarifado_cadastro_medidores_produtos'
        if   iparorde == 1: scamposb = 'idmedid, codmedi, descmed'                                  # Ordenar por ordem de código da marca
        elif iparorde == 2: scamposb = 'idmedid, descmed, codmedi'                                  # Ordenar por ordem de descrição da marca
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iidfilia != None: sfilbusc = sfilbusc + ' AND idfilia = ' + str(iidfilia)
        if   iparorde == 1: sorderby = 'codmedi, descmed, idmedid'                                  # Ordenar por ordem de código da marca
        elif iparorde == 2: sorderby = 'descmed, codmedi, idmedid'                                  # Ordenar por ordem de descrição da marca
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '0501':
        stabelax = 'abnf_preventiva_cadastro_grupos'
        if   iparorde == 1: scamposb = 'idgrpre, codgrpr, descgrp'                					# Ordenar por ordem de código do grupo
        elif iparorde == 2: scamposb = 'idgrpre, descgrp, codgrpr'                					# Ordenar por ordem da descrição do grupo
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iparorde == 1: sorderby = 'codgrpr, descgrp, idgrpre'                					# Ordenar por ordem de código do grupo
        elif iparorde == 2: sorderby = 'descgrp, codgrpr, idgrpre'                					# Ordenar por ordem de descrição do grupo
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '0502':
        stabelax = 'abnf_preventiva_cadastro_itens'
        if   iparorde == 1: scamposb = 'iditpre, coditpr, descitp'                					# Ordenar por ordem de código do ítem
        elif iparorde == 2: scamposb = 'iditpre, descitp, coditpr'                					# Ordenar por ordem da descrição do ítem
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iparorde == 1: sorderby = 'coditpr, descitp, iditpre'                					# Ordenar por ordem de código do ítem
        elif iparorde == 2: sorderby = 'descitp, coditpr, iditpre'                					# Ordenar por ordem de descrição do ítem
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '0801':
        stabelax = 'abnf_financeiro_cadastro_contas'
        if   iparorde == 1: scamposb = 'idconta, codcont, descban, descage, desccon'                # Ordenar por ordem de código da conta
        elif iparorde == 2: scamposb = 'idconta, descban, descage, desccon, codcont'                # Ordenar por ordem de banco, agencia e conta
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iidfilia != None: sfilbusc = sfilbusc + ' AND idfilia = ' + str(iidfilia)
        if   iparorde == 1: sorderby = 'codcont, descban, descage, desccon, idconta'                # Ordenar por ordem de código da conta
        elif iparorde == 2: sorderby = 'descban, descage, desccon, codcont, idconta'                # Ordenar por ordem de banco, agencia e conta
        sstruret = "str(lauxi001[1]) + ' - ' + str(lauxi001[2]) + ' - ' + str(lauxi001[3]) + ' (' + str(lauxi001[4]) + ')'" # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '0802':
        stabelax = 'abnf_financeiro_cadastro_grupos'
        if   iparorde == 1: scamposb = 'idgrupo, codgrup, descgru'                					# Ordenar por ordem de código do grupo
        elif iparorde == 2: scamposb = 'idgrupo, descgru, codgrup'                					# Ordenar por ordem da descrição do grupo
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iparorde == 1: sorderby = 'codgrup, descgru, idgrupo'                					# Ordenar por ordem de código do grupo
        elif iparorde == 2: sorderby = 'descgru, codgrup, idgrupo'                					# Ordenar por ordem de descrição do grupo
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '0803':
        stabela1 = 'abnf_financeiro_cadastro_grupos'
        scampos1 = 'idgrupo, descgru, codgrup, tipogru'       					                    # Ordenar por ordem da descrição do subgrupo
        if   iparfilt == None: sfilbus1 = 'situreg != "C"'                                          # Registros ativos e inativos
        elif iparfilt == 'R':  sfilbus1 = 'situreg != "C" and tipogru = "R"'                        # Registros ativos e inativos e de receita
        elif iparfilt == 'D':  sfilbus1 = 'situreg != "C" and tipogru = "D"'                        # Registros ativos e inativos e de despesa
        if   iparorde == 1: sorderb1 = 'codgrup, descgru, idgrupo'                                  # Ordenar por ordem de código do grupo
        elif iparorde == 2: sorderb1 = 'descgru, codgrup, idgrupo'                                  # Ordenar por ordem de descrição do grupo
        stabela2 = 'abnf_financeiro_cadastro_subgrupos'
        scampos2 = 'idsubgr, idgrupo, descsub, codsubg'                                             # Ordenar por ordem da descrição do subgrupo
        sfilbus2 = 'situreg != "C"'                                                                 # Registros ativos e inativos
        if   iparorde == 1: sorderb2 = 'codsubg, descsub, idsubgr'                                  # Ordenar por ordem de código do subgrupo
        elif iparorde == 2: sorderb2 = 'descsub, codsubg, idsubgr'                                  # Ordenar por ordem de descrição do subgrupo
        lkeyjoin = (0, 1)                                                                           # Posição das chave que unem as duas tabelas
        icodmont = 3
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '0804':
        stabelax = 'abnf_financeiro_cadastro_complementos'
        if   iparorde == 1: scamposb = 'idcompl, codcomp, desccom'                					# Ordenar por ordem de código do grupo
        elif iparorde == 2: scamposb = 'idcompl, desccom, codcomp'                					# Ordenar por ordem da descrição do grupo
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iparorde == 1: sorderby = 'codcomp, desccom, idcompl'                					# Ordenar por ordem de código do grupo
        elif iparorde == 2: sorderby = 'desccom, codcomp, idcompl'                					# Ordenar por ordem de descrição do grupo
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '0805':
        stabelax = 'abnf_financeiro_cadastro_centros_custo'
        if   iparorde == 1: scamposb = 'idcecus, codcecu, desccec'                					# Ordenar por ordem de código do centro de custo
        elif iparorde == 2: scamposb = 'idcecus, desccec, codcecu'                					# Ordenar por ordem da descrição do centro de custo
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iparorde == 1: sorderby = 'codcecu, desccec, idcecus'                					# Ordenar por ordem de código do grupo
        elif iparorde == 2: sorderby = 'desccec, codcecu, idcecus'                					# Ordenar por ordem de descrição do grupo
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '0806':
        stabelax = 'abnf_financeiro_cadastro_departamentos'
        if   iparorde == 1: scamposb = 'iddepto, coddept, descdep'                					# Ordenar por ordem de código do departamento
        elif iparorde == 2: scamposb = 'iddepto, descdep, coddept'                					# Ordenar por ordem da descrição do departamento
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iparorde == 1: sorderby = 'coddept, descdep, iddepto'                					# Ordenar por ordem de código do departamento
        elif iparorde == 2: sorderby = 'descdep, coddept, iddepto'                					# Ordenar por ordem de descrição do departamento
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '1001':
        stabela1 = 'abnf_cadastro_cpfcnpj'
        scampos1 = 'idcpfpj, nomraso, codpfpj'
        sfilbus1 = 'situreg != "C"'                                                                 # Registros ativos e inativos
        sorderb1 = 'nomraso, idcpfpj'
        stabela2 = 'abnf_elevar_cadastro_passageiros'
        scampos2 = 'idepass, codepas, idcpfpj, cadeira, acompan'
        sfilbus2 = 'situreg != "C"'                                                                 # Registros ativos e inativos
        sorderb2 = 'idepass'
        lkeyjoin = (0, 2)                                                                           # Posição das chave que unem as duas tabelas
        sstruret = "(lauxi001[1], lauxi001[1] + ' (' + str( lauxi002[1]) + ')' , lauxi002[1], lauxi002[3], lauxi002[4])" # Estrutura de retorno
        icodmont = 2
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '1002':
        stabelax = 'abnf_elevar_cadastro_locais'
        if   iparorde == 1: scamposb = 'ideloca, codeloc, deseloc'                					# Ordenar por ordem de código do local do Elevar
        elif iparorde == 2: scamposb = 'ideloca, deseloc, codeloc'                					# Ordenar por ordem da descrição do local do Elevar
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iparorde == 1: sorderby = 'codeloc, deseloc, ideloca'                					# Ordenar por ordem de código do local do Elevar
        elif iparorde == 2: sorderby = 'deseloc, codeloc, ideloca'                					# Ordenar por ordem de descrição do local do Elevar
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '1003':
        stabelax = 'abnf_elevar_cadastro_finalidades'
        if   iparorde == 1: scamposb = 'idefina, codefin, desefin'                					# Ordenar por ordem de código de finalidade do Elevar
        elif iparorde == 2: scamposb = 'idefina, desefin, codefin'                					# Ordenar por ordem da descrição de finalidade do Elevar
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iparorde == 1: sorderby = 'codefin, desefin, idefina'                					# Ordenar por ordem de código de finalidade do Elevar
        elif iparorde == 2: sorderby = 'desefin, codefin, idefina'                					# Ordenar por ordem de descrição de finalidade do Elevar
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '1004':
        drelepas = abnf_database_menu(icodbase, None, 'D', '1001', 0, 0, None)
        drelefin = abnf_database_menu(icodbase, None, 'D', '1003', 0, 1, 2)
        stabelax = 'abnf_elevar_cadastro_servicos'
        scamposb = 'ideserv, codeser, idepass, idefina'                     	                    # Ordenar por ordem de código de serviço do Elevar
        sfilbusc = 'situreg != "C"'                                                                 # Registros ativos e inativos
        sorderby = 'codeser'                                                                        # Ordenar por ordem de código de serviço do Elevar
        sstruret = "(lauxi001[1], lauxi001[2], drelepas.get(lauxi001[2], ('','','','','')), lauxi001[3], drelefin.get(lauxi001[3],''))" # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu in ['1106', '1107']:
        stabelax = 'abnf_sac_cadastro_usuarios_grupos'
        if   iparorde == 1: scamposb = 'idsusgr, codsusg, dessusg, envpref'                         # Ordenar por ordem de código do grupo de usuários do SAC
        elif iparorde == 2: scamposb = 'idsusgr, dessusg, codsusg, envpref'                         # Ordenar por ordem da descrição do grupo de usuários do SAC
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iidfilia != None: sfilbusc = sfilbusc + ' AND idfilia = ' + str(iidfilia)
        if   iparorde == 1: sorderby = 'codsusg, dessusg, idsusgr'                					# Ordenar por ordem de código do grupo de usuários do SAC
        elif iparorde == 2: sorderby = 'dessusg, codsusg, idsusgr'                					# Ordenar por ordem de descrição do grupo de usuários do SAC
        if   sdefmenu == '1106': sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"      # Estrutura de retorno
        elif sdefmenu == '1107': sstruret = "lauxi001[3]"                                           # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '1101':
        stabelax = 'abnf_sac_cadastro_atendimentos_canais'
        if   iparorde == 1: scamposb = 'idsatca, codsatc, dessatc'                					# Ordenar por ordem de código de canal de atendimento do SAC
        elif iparorde == 2: scamposb = 'idsatca, dessatc, codsatc'                					# Ordenar por ordem da descrição de canal de atendimento do SAC
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iidfilia != None: sfilbusc = sfilbusc + ' AND idfilia = ' + str(iidfilia)
        if   iparorde == 1: sorderby = 'codsatc, dessatc, idsatca'                					# Ordenar por ordem de código de canal de atendimento do SAC
        elif iparorde == 2: sorderby = 'dessatc, codsatc, idsatca'                					# Ordenar por ordem de descrição de canal de atendimento do SAC
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '1102':
        stabelax = 'abnf_sac_cadastro_atendimentos_tipos'
        if   iparorde == 1: scamposb = 'idsatti, codsatt, dessatt'                					# Ordenar por ordem de código de tipo de atendimento do SAC
        elif iparorde == 2: scamposb = 'idsatti, dessatt, codsatt'                					# Ordenar por ordem da descrição de tipo de atendimento do SAC
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iidfilia != None: sfilbusc = sfilbusc + ' AND idfilia = ' + str(iidfilia)
        if   iparorde == 1: sorderby = 'codsatt, dessatt, idsatti'                					# Ordenar por ordem de código de tipo de atendimento do SAC
        elif iparorde == 2: sorderby = 'dessatt, codsatt, idsatti'                					# Ordenar por ordem de descrição de tipo de atendimento do SAC
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '1103':
        stabelax = 'abnf_sac_cadastro_atendimentos_grupos'
        if   iparorde == 1: scamposb = 'idsatgr, codsatg, dessatg'                					# Ordenar por ordem de código do grupo
        elif iparorde == 2: scamposb = 'idsatgr, dessatg, codsatg'                					# Ordenar por ordem da descrição do grupo
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iidfilia != None: sfilbusc = sfilbusc + ' AND idfilia = ' + str(iidfilia)
        if   iparorde == 1: sorderby = 'codsatg, dessatg, idsatgr'                					# Ordenar por ordem de código do grupo
        elif iparorde == 2: sorderby = 'dessatg, codsatg, idsatgr'                					# Ordenar por ordem de descrição do grupo
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu in ['1104', '1105']:
        stabela1 = 'abnf_sac_cadastro_atendimentos_grupos'
        scampos1 = 'idsatgr, dessatg, codsatg'              					                    # Ordenar por ordem da descrição do subgrupo
        sfilbus1 = 'situreg != "C"'                                                                 # Registros ativos e inativos
        if   iidfilia != None: sfilbus1 = sfilbus1 + ' AND idfilia = ' + str(iidfilia)
        if   iparorde == 1: sorderb1 = 'codsatg, dessatg, idsatgr'                                  # Ordenar por ordem de código do grupo
        elif iparorde == 2: sorderb1 = 'dessatg, codsatg, idsatgr'                                  # Ordenar por ordem de descrição do grupo
        stabela2 = 'abnf_sac_cadastro_atendimentos_subgrupos'
        scampos2 = 'idsatsg, idsatgr, dessats, codsats, envpref'                                    # Ordenar por ordem da descrição do subgrupo
        sfilbus2 = 'situreg != "C"'                                                                 # Registros ativos e inativos
        if   iparorde == 1: sorderb2 = 'codsats, dessats, idsatsg'                                  # Ordenar por ordem de código do subgrupo
        elif iparorde == 2: sorderb2 = 'dessats, codsats, idsatsg'                                  # Ordenar por ordem de descrição do subgrupo
        lkeyjoin = (0, 1)                                                                           # Posição das chave que unem as duas tabelas
        if   sdefmenu == '1104': sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ') - ' + str(lauxi002[2]) + ' (' + str(lauxi002[3]) + ')'"            # Estrutura de retorno
        elif sdefmenu == '1105': sstruret = "(str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')', str(lauxi002[2]) + ' (' + str(lauxi002[3]) + ')', lauxi002[4])" # Estrutura de retorno
        icodmont = 2
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '1201':
        stabelax = 'abnf_sigom_cadastro_ocorrencias_tipos'
        if   iparorde == 1: scamposb = 'idsocti, codsoct, dessoct'                					# Ordenar por ordem de código do tipo de ocorrência
        elif iparorde == 2: scamposb = 'idsocti, dessoct, codsoct'                					# Ordenar por ordem de descrição do tipo de ocorrência
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iidfilia != None: sfilbusc = sfilbusc + ' AND idfilia = ' + str(iidfilia)
        if   iparorde == 1: sorderby = 'codsoct, dessoct, idsocti'                					# Ordenar por ordem de código do tipo de ocorrência
        elif iparorde == 2: sorderby = 'dessoct, codsoct, idsocti'                					# Ordenar por ordem de descrição do tipo de ocorrência
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '1202':
        stabelax = 'abnf_sigom_cadastro_veiculos_situacao'
        if   iparorde == 1: scamposb = 'idsvesi, codsves, dessves'                					# Ordenar por ordem de código da situação
        elif iparorde == 2: scamposb = 'idsvesi, dessves, codsves'                					# Ordenar por ordem de descrição da situação
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iidfilia != None: sfilbusc = sfilbusc + ' AND idfilia = ' + str(iidfilia)
        if   iparorde == 1: sorderby = 'codsves, dessves, idsvesi'                					# Ordenar por ordem de código da situação
        elif iparorde == 2: sorderby = 'dessves, codsves, idsvesi'                					# Ordenar por ordem de descrição da situação
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '1203':
        stabelax = 'abnf_sigom_cadastro_classificacao'
        if   iparorde == 1: scamposb = 'idsclas, codscla, desscla'                					# Ordenar por ordem de código da classificação
        elif iparorde == 2: scamposb = 'idsclas, desscla, codscla'                					# Ordenar por ordem de descrição da sclassificação
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iidfilia != None: sfilbusc = sfilbusc + ' AND idfilia = ' + str(iidfilia)
        if   iparorde == 1: sorderby = 'codscla, desscla, idsclas'                					# Ordenar por ordem de código da classificação
        elif iparorde == 2: sorderby = 'desscla, codscla, idsclas'                					# Ordenar por ordem de descrição da classificação
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '1204':
        stabelax = 'abnf_sigom_cadastro_usuarios_grupos'
        if   iparorde == 1: scamposb = 'idsusgr, codsusg, dessusg'                                  # Ordenar por ordem de código do grupo de usuários do SIGOM
        elif iparorde == 2: scamposb = 'idsusgr, dessusg, codsusg'                                  # Ordenar por ordem da descrição do grupo de usuários do SIGOM
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iidfilia != None: sfilbusc = sfilbusc + ' AND idfilia = ' + str(iidfilia)
        if   iparorde == 1: sorderby = 'codsusg, dessusg, idsusgr'                					# Ordenar por ordem de código do grupo de usuários do SIGOM
        elif iparorde == 2: sorderby = 'dessusg, codsusg, idsusgr'                					# Ordenar por ordem de descrição do grupo de usuários do SIGOM
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu in ['1301A', '1301B']:
        stabelax = 'abnf_operacional_cadastro_locais'
        if   iparorde == 1: scamposb = 'idoloca, codoloc, desoloc'                					# Ordenar por ordem de código do local
        elif iparorde == 2: scamposb = 'idoloca, desoloc, codoloc'                					# Ordenar por ordem da descrição do local
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iidfilia != None: sfilbusc = sfilbusc + ' AND idfilia = ' + str(iidfilia)
        if   iparorde == 1: sorderby = 'codoloc, desoloc, idoloca'                					# Ordenar por ordem de código do local
        elif iparorde == 2: sorderby = 'desoloc, codoloc, idoloca'                					# Ordenar por ordem de descrição do local
        if   sdefmenu == '1301A': sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"     # Estrutura de retorno para 1301A
        elif sdefmenu == '1301B': sstruret = "str(lauxi001[1])"                                     # Estrutura de retorno para 1301B
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '1302':
        stabelax = 'abnf_operacional_cadastro_grupos_linhas'
        if   iparorde == 1: scamposb = 'idogrli, codogrl, desogrl'                					# Ordenar por ordem de código do grupo
        elif iparorde == 2: scamposb = 'idogrli, desogrl, codogrl'                					# Ordenar por ordem da descrição do grupo
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iidfilia != None: sfilbusc = sfilbusc + ' AND idfilia = ' + str(iidfilia)
        if   iparorde == 1: sorderby = 'codogrl, desogrl, idogrli'                					# Ordenar por ordem de código do grupo
        elif iparorde == 2: sorderby = 'desogrl, codogrl, idogrli'                					# Ordenar por ordem de descrição do grupo
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu in ['1303', '1303B', '1303C' ]:
        stabelax = 'abnf_operacional_cadastro_linhas'
        if   iparorde == 1: scamposb = 'idolinh, codolin, desolin'                					# Ordenar por ordem de código da linha
        elif iparorde == 2: scamposb = 'idolinh, desolin, codolin'                					# Ordenar por ordem da descrição da linha
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iidfilia != None: sfilbusc = sfilbusc + ' AND idfilia = ' + str(iidfilia)
        if   iparorde == 1: sorderby = 'codolin, desolin, idolinh'                					# Ordenar por ordem de código da linha
        elif iparorde == 2: sorderby = 'desolin, codolin, idolinh'                					# Ordenar por ordem de descrição da linha
        if   sdefmenu == '1303'  and iparorde == 1: sstruret = "lauxi001[1] + ' - ' + lauxi001[2]"                  # Estrutura de retorno
        elif sdefmenu == '1303'  and iparorde == 2: sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"   # Estrutura de retorno
        elif sdefmenu == '1303B' and iparorde == 1: sstruret = "lauxi001[1]"                                        # Estrutura de retorno
        elif sdefmenu == '1303C' and iparorde == 1: sstruret = "(lauxi001[1], lauxi001[2])"                         # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '1304':
        stabelax = 'abnf_operacional_cadastro_projetos'
        if   iparorde == 1: scamposb = 'idoproj, codopro, desopro'                					# Ordenar por ordem de código do projeto
        elif iparorde == 2: scamposb = 'idoproj, desopro, codopro'                					# Ordenar por ordem da descrição do projeto
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iidfilia != None: sfilbusc = sfilbusc + ' AND idfilia = ' + str(iidfilia)
        if   iparorde == 1: sorderby = 'codopro, desopro, idoproj'                					# Ordenar por ordem de código do projeto
        elif iparorde == 2: sorderby = 'desopro, codopro, idoproj'                					# Ordenar por ordem de descrição do projeto
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '1305A':
        # /// #
        iidfilia, iidoproj, iidolinh = iidfilia                                                     # No parâmetro onde é informado o ID da filial, é uma lista onde é informado os IDs da filial, projeto e linha!
        stabela1 = 'abnf_operacional_cadastro_projetos'
        scampos1 = 'idoproj, desopro, codopro'        					                            # Campos do projeto
        sfilbus1 = 'situreg != "C"'                                                                 # Registros ativos e inativos
        if iidfilia != None: sfilbus1 = sfilbus1 + ' AND idfilia = ' + str(iidfilia)                # Filtro por filial
        if iidoproj != None: sfilbus1 = sfilbus1 + ' AND idoproj = ' + str(iidoproj)                # Filtro por projeto
        sorderb1 = 'codopro, idoproj'                                                               # Ordenar por ordem de código do projeto
        # /// #
        stabela2 = 'abnf_operacional_cadastro_linhas'
        scampos2 = 'idolinh, codolin'                  					                            # Campos da linha
        sfilbus2 = 'situreg != "C"'                                                                 # Registros ativos e inativos
        if iidfilia != None: sfilbus2 = sfilbus2 + ' AND idfilia = ' + str(iidfilia)                # Filtro por filial
        if iidolinh != None: sfilbus2 = sfilbus2 + ' AND idolinh = ' + str(iidolinh)                # Filtro por linha
        sorderb2 = 'codolin, idolinh'                                                               # Ordenar por ordem de código da linha
        # /// #
        stabela3 = 'abnf_operacional_cadastro_trajetos'
        scampos3 = 'idotraj, idoproj, idolinh, codotra, desotra, kmidaxx, kmvolta'                  # Campos do trajeto
        sfilbus3 = 'situreg != "C"'                                                                 # Registros ativos e inativos
        sorderb3 = 'idoproj, idolinh, codotra'                                                      # Ordenar por ordem de projeto/linha/código do trajeto
        # /// #
        icodmont = 0
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '1306':
        stabelax = 'abnf_operacional_cadastro_motivo_substituicao'
        if   iparorde == 1: scamposb = 'idomsub, codomsu, descmsu'                					# Ordenar por ordem de código do motivo de substituição
        elif iparorde == 2: scamposb = 'idomsub, descmsu, codomsu'                					# Ordenar por ordem da descrição do motivo de substituição
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iidfilia != None: sfilbusc = sfilbusc + ' AND idfilia = ' + str(iidfilia)
        if   iparorde == 1: sorderby = 'codomsu, descmsu, idomsub'                					# Ordenar por ordem de código do motivo de substituição
        elif iparorde == 2: sorderby = 'descmsu, codomsu, idomsub'                					# Ordenar por ordem de descrição do motivo de substituição
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '1321A':
        stabelax = 'abnf_operacional_cadastro_grupos_veiculos'
        if   iparorde == 1: scamposb = 'idogrve, codogrf, descgrf'                					# Ordenar por ordem de código do grupo de veículo
        elif iparorde == 2: scamposb = 'idogrve, descgrf, codogrf'                					# Ordenar por ordem da descrição do grupo de veículos
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        if   iidfilia != None: sfilbusc = sfilbusc + ' AND idfilia = ' + str(iidfilia)
        if   iparorde == 1: sorderby = 'codogrf, descgrf, idogrve'                					# Ordenar por ordem de código do grupo de veículos
        elif iparorde == 2: sorderby = 'descgrf, codogrf, idogrve'                					# Ordenar por ordem de descrição do grupo de veículos
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '1330':
        stabelax = 'abnf_operacional_entrada_saida_veiculos_locais'
        scamposb = 'idoesvl, desoesl, codoesl'
        if   iparfilt == 1: sfilbusc = 'situreg != "C"'                                             # Registros ativos e inativos
        elif iparfilt == 2: sfilbusc = 'situreg = "A"'                                              # Somente registros ativos
        sfilbusc = sfilbusc + ' AND idfilia = ' + str(iidfilia)
        sorderby = 'desoesl, codoesl, idoesvl'
        sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ')'"                               # Estrutura de retorno
        icodmont = 1
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    # ◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    if icodmont == 1:
        lsqlre01, iqtdre01 = abnf_database_busca_dados_v01(icodbase, stabelax, scamposb, sfilbusc, sorderby)
        for lauxi001 in lsqlre01:
            lmselect.append((
                lauxi001[0],
                eval(sstruret)
            ))
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif icodmont == 2:
        lsqlre01, iqtdre01 = abnf_database_busca_dados_v01(icodbase, stabela1, scampos1, sfilbus1, sorderb1)
        lsqlre02, iqtdre02 = abnf_database_busca_dados_v01(icodbase, stabela2, scampos2, sfilbus2, sorderb2)
        for lauxi001 in lsqlre01:
            for lauxi002 in lsqlre02:
                if lauxi002[lkeyjoin[1]] == lauxi001[lkeyjoin[0]]:
                    lmselect.append((
                        lauxi002[0],
                        eval(sstruret)
                    ))
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif icodmont == 3:
        lsqlre01, iqtdre01 = abnf_database_busca_dados_v01(icodbase, stabela1, scampos1, sfilbus1, sorderb1)
        lsqlre02, iqtdre02 = abnf_database_busca_dados_v01(icodbase, stabela2, scampos2, sfilbus2, sorderb2)
        for stipogru in ('R','D'):
            sdesctip = ' - [Receita]' if stipogru == 'R' else ' - [Despesa]' if stipogru == 'D' else ''
            for lauxi001 in lsqlre01:
                if lauxi001[3] == stipogru:
                    for lauxi002 in lsqlre02:
                        if lauxi002[lkeyjoin[1]] == lauxi001[lkeyjoin[0]]:
                            lmselect.append((
                                lauxi002[0],
                                str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ') - ' + str(lauxi002[2]) + ' (' + str(lauxi002[3]) + ')' + sdesctip
                            ))
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif icodmont == 402:
        lsqlre01, iqtdre01 = abnf_database_busca_dados_v01(icodbase, stabela1, scampos1, sfilbus1, sorderb1)
        lsqlre02, iqtdre02 = abnf_database_busca_dados_v01(icodbase, stabela2, scampos2, sfilbus2, sorderb2)
        for lauxi001 in lsqlre01:
            for lauxi002 in lsqlre02:
                if lauxi001[3] == lauxi002[0]:
                    sauxi001 = lauxi001[1] + ' / ' + lauxi002[1] + ' / ' + lauxi002[2] + ' (' + str(lauxi001[2]) + ')'
                    if   stiporet == 'L': lauxi003 = sauxi001
                    elif stiporet == 'D': lauxi003 = (sauxi001, lauxi001[1], lauxi002[1], lauxi002[2], lauxi001[2])
                    lmselect.append((
                        lauxi001[0],
                        lauxi003
                    ))
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif icodmont == 403:
        lsqlre01, iqtdre01 = abnf_database_busca_dados_v01(icodbase, stabela1, scampos1, sfilbus1, sorderb1)
        lsqlre02, iqtdre02 = abnf_database_busca_dados_v01(icodbase, stabela2, scampos2, sfilbus2, sorderb2)
        lsqlre03, iqtdre03 = abnf_database_busca_dados_v01(icodbase, stabela3, scampos3, sfilbus3, sorderb3)
        for lauxi001 in lsqlre01:
            for lauxi002 in lsqlre02:
                for lauxi003 in lsqlre03:
                    if lauxi001[4] == lauxi002[0] and lauxi002[2] == lauxi003[0]:
                        sauxi001 = lauxi001[1] + ' ' + lauxi001[2] + ' / ' + lauxi002[1] + ' / ' + lauxi003[1] + ' / ' + lauxi003[2] + ' (' + str(lauxi001[3]) + ')'
                        if   stiporet == 'L': lauxi004 = sauxi001
                        elif stiporet == 'D': lauxi004 = (sauxi001, lauxi001[1], lauxi001[2], lauxi002[1], lauxi003[1], lauxi003[2])
                        lmselect.append((
                            lauxi001[0],
                            lauxi004
                        ))
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu in ('1305A'):
        lsqlre01, iqtdre01 = abnf_database_busca_dados_v01(icodbase, stabela1, scampos1, sfilbus1, sorderb1)
        lsqlre02, iqtdre02 = abnf_database_busca_dados_v01(icodbase, stabela2, scampos2, sfilbus2, sorderb2)
        lsqlre03, iqtdre03 = abnf_database_busca_dados_v01(icodbase, stabela3, scampos3, sfilbus3, sorderb3)
        for lauxi001 in lsqlre01:
            for lauxi002 in lsqlre02:
                for lauxi003 in lsqlre03:
                    if lauxi003[1] == lauxi001[0] and lauxi003[2] == lauxi002[0]:
                        if   stiporet == 'L': sauxi001 = 'Projeto: ' + lauxi001[1] + ' (' + str(lauxi001[2]) + ') - Linha: ' + lauxi002[1] + ' - Trajeto: [' + lauxi003[3] + '] - ' + lauxi003[4]   # Lista
                        elif stiporet == 'D': sauxi001 = (lauxi003[3], lauxi003[4], lauxi003[5], lauxi003[6])
                        lmselect.append((
                            lauxi003[0],
                            sauxi001
                        ))
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    # ◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    if stiporet == 'L':
        return lmselect
    elif stiporet == 'D':
        ddiciona = {}
        for lauxi001 in lmselect:
            ddiciona[lauxi001[0]] = lauxi001[1]
        return ddiciona
    elif stiporet == 'A':
        ddiciona = {}
        for lauxi001 in lmselect:
            ddiciona[lauxi001[0]] = lauxi001[1]
        return lmselect, ddiciona

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_database_sqlx ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função para criar menus de select ou dicionário de dados usado comandos SQL específicos.                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_database_sqlx(icodbase, stiporet, sdefmenu, iparlini, lparamet):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_database_sqlx (Gerando dados para a criação de menus de select ou dicionário de dados)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    # ◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    if False: pass
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '02001A':
        sauxi001 = 'SELECT '
        # Campos das tabelas
        sauxi001 = sauxi001 + 'abnf01.idmarca, '    # [00] ID da marca
        sauxi001 = sauxi001 + 'abnf01.desmarc, '    # [01] Descrição da marca
        sauxi001 = sauxi001 + 'abnf01.codmarc  '    # [02] Código da marca
        # Tabelas SQL
        sauxi001 = sauxi001 + 'FROM abnf_cadastro_veiculos_marcas AS abnf01 '
        # Condições
        sauxi001 = sauxi001 + 'WHERE '
        if   lparamet[0] == 0: sauxi001 = sauxi001 + 'abnf01.situreg != "C" '     # ==> Somente registros não cancelados
        elif lparamet[0] == 1: sauxi001 = sauxi001 + 'abnf01.situreg = "A" '      # ==> Somente registros ativo
        # Ordenação
        sauxi001 = sauxi001 + 'ORDER BY abnf01.desmarc, abnf01.idmarca;'
        # Estrutura de retorno
        sstruret = "lauxi001[1] + ' (' + str(lauxi001[2]) + ')'"
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu in ('02002A', '02002B'):
        sauxi001 = 'SELECT '
        # Campos das tabelas
        if sdefmenu == '02002A':    # Usado para select
            sauxi001 = sauxi001 + 'abnf01.idmodel, '    # [00] ID do modelo
            sauxi001 = sauxi001 + 'abnf02.desmarc, '    # [01] Descrição da marca
            sauxi001 = sauxi001 + 'abnf01.desmode, '    # [02] Descrição do modelo
            sauxi001 = sauxi001 + 'abnf01.codmode  '    # [03] Código do modelo
        elif sdefmenu == '02002B':  # Usado para relatório
            sauxi001 = sauxi001 + 'abnf02.desmarc, '    # [00] Descrição da marca
            sauxi001 = sauxi001 + 'abnf01.desmode, '    # [01] Descrição do modelo
            sauxi001 = sauxi001 + 'abnf01.codmode, '    # [02] Código do modelo
            sauxi001 = sauxi001 + 'abnf01.situreg  '    # [03] Situação do registro
        # Tabelas SQL
        sauxi001 = sauxi001 + 'FROM       abnf_cadastro_veiculos_modelos AS abnf01 '
        sauxi001 = sauxi001 + 'INNER JOIN abnf_cadastro_veiculos_marcas  AS abnf02 '
        sauxi001 = sauxi001 + 'ON         abnf01.idmarca = abnf02.idmarca '
        # Condições
        sauxi001 = sauxi001 + 'WHERE '
        if   lparamet[0] == 0: sauxi001 = sauxi001 + 'abnf01.situreg != "C" '     # ==> Somente registros não cancelados
        elif lparamet[0] == 1: sauxi001 = sauxi001 + 'abnf01.situreg = "A" '      # ==> Somente registros ativo
        # Ordenação
        sauxi001 = sauxi001 + 'ORDER BY abnf02.desmarc, abnf01.desmode, abnf01.idmodel;'
        # Estrutura de retorno
        if   sdefmenu == '02002A': sstruret = "lauxi001[1] + ' - ' + lauxi001[2] + ' (' + str(lauxi001[3]) + ')'"
        elif sdefmenu == '02002B': sstruret = "(lauxi001[0], lauxi001[1], lauxi001[2], lauxi001[3])"
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu in ('02003A', '02003B'):
        sauxi001 = 'SELECT '
        # Campos das tabelas
        if sdefmenu == '02003A':    # Usado para select
            sauxi001 = sauxi001 + 'abnf01.idveicu, '    # [00] ID do modelo
            sauxi001 = sauxi001 + 'abnf01.prefvei, '    # [01] Prefixo do veículo
            sauxi001 = sauxi001 + 'abnf01.placave  '    # [02] Placa do veículo
        elif sdefmenu == '02003B':  # Usado para relatório
            sauxi001 = sauxi001 + 'abnf01.prefvei, '    # [00] Prefixo do veículo
            sauxi001 = sauxi001 + 'abnf01.placave, '    # [01] Placa do veículo
            sauxi001 = sauxi001 + 'abnf03.desmarc, '    # [02] Descrição da marca
            sauxi001 = sauxi001 + 'abnf03.codmarc, '    # [03] Código da marca
            sauxi001 = sauxi001 + 'abnf02.desmode, '    # [04] Descrição do modelo
            sauxi001 = sauxi001 + 'abnf02.codmode, '    # [05] Código do modelo
            sauxi001 = sauxi001 + 'abnf01.dataini, '    # [06] Data de aquisição (ou início de atividade)
            sauxi001 = sauxi001 + 'abnf01.datafim, '    # [07] Data de venda (ou fim de atividade)
            sauxi001 = sauxi001 + 'abnf01.situreg  '    # [08] Situação do registro
        # Tabelas SQL
        sauxi001 = sauxi001 + 'FROM       abnf_cadastro_veiculos         AS abnf01 '
        if sdefmenu == '02003B':
            sauxi001 = sauxi001 + 'INNER JOIN abnf_cadastro_veiculos_modelos AS abnf02 '
            sauxi001 = sauxi001 + 'ON         abnf01.idmodel = abnf02.idmodel '
            sauxi001 = sauxi001 + 'INNER JOIN abnf_cadastro_veiculos_marcas  AS abnf03 '
            sauxi001 = sauxi001 + 'ON         abnf02.idmarca = abnf03.idmarca '
        # Condições
        sauxi001 = sauxi001 + 'WHERE '
        if   lparamet[0] == 0: sauxi001 = sauxi001 + 'abnf01.situreg != "C" '     # ==> Somente registros não cancelados
        elif lparamet[0] == 1: sauxi001 = sauxi001 + 'abnf01.situreg = "A" '      # ==> Somente registros ativo
        sauxi001 = sauxi001 + 'AND abnf01.idfilia = ' + str(lparamet[1])  + ' '   # ==> Somente registros da filial
        # Ordenação
        sauxi001 = sauxi001 + 'ORDER BY abnf01.prefvei, abnf01.idveicu;'
        # Estrutura de retorno
        if   sdefmenu == '02003A': sstruret = "lauxi001[1] + ' (' + str(lauxi001[2]) + ')'"
        elif sdefmenu == '02003B': sstruret = "(lauxi001[0], lauxi001[1], lauxi001[2], lauxi001[3], lauxi001[4], lauxi001[5], lauxi001[6], lauxi001[7], lauxi001[8])"
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '03001A':
        sauxi001 = 'SELECT '
        # Campos das tabelas
        sauxi001 = sauxi001 + 'abnf01.idcargo, '    # [00] ID do cargo
        sauxi001 = sauxi001 + 'abnf01.descarg, '    # [01] Descrição do cargo
        sauxi001 = sauxi001 + 'abnf01.codcarg  '    # [02] Código do cargo
        # Tabelas SQL
        sauxi001 = sauxi001 + 'FROM abnf_cadastro_funcionarios_cargos AS abnf01 '
        # Condições
        sauxi001 = sauxi001 + 'WHERE '
        if   lparamet[0] == 0: sauxi001 = sauxi001 + 'abnf01.situreg != "C" '     # ==> Somente registros não cancelados
        elif lparamet[0] == 1: sauxi001 = sauxi001 + 'abnf01.situreg = "A" '      # ==> Somente registros ativo
        # Ordenação
        sauxi001 = sauxi001 + 'ORDER BY abnf01.descarg, abnf01.idcargo;'
        # Estrutura de retorno
        sstruret = "lauxi001[1] + ' (' + str(lauxi001[2]) + ')'"
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu in ('03002A', '03002B'):
        sauxi001 = 'SELECT '
        # Campos das tabelas
        if sdefmenu == '03002A':    # Usado para select
            sauxi001 = sauxi001 + 'abnf01.idfunci, '    # [00] ID do funcionário
            sauxi001 = sauxi001 + 'abnf02.nomraso, '    # [01] Nome do funcionário
            sauxi001 = sauxi001 + 'abnf01.codfunc  '    # [02] Código do funcionário
        elif sdefmenu == '03002B':  # Usado para relatório
            sauxi001 = sauxi001 + 'abnf02.nomraso, '    # [00] Nome do funcionário
            sauxi001 = sauxi001 + 'abnf01.codfunc, '    # [01] Código do funcionário
            sauxi001 = sauxi001 + 'abnf02.codpfpj, '    # [02] CPF
            sauxi001 = sauxi001 + 'abnf03.descarg, '    # [03] Descrição do cargo
            sauxi001 = sauxi001 + 'abnf03.codcarg, '    # [04] Código do cargo
            sauxi001 = sauxi001 + 'abnf01.dataadm, '    # [05] Data de admissão
            sauxi001 = sauxi001 + 'abnf01.datades, '    # [06] Data de desligamento
            sauxi001 = sauxi001 + 'abnf01.situreg  '    # [07] Situação do registro
        # Tabelas SQL
        sauxi001 = sauxi001 + 'FROM       abnf_cadastro_funcionarios AS abnf01 '
        sauxi001 = sauxi001 + 'INNER JOIN abnf_cadastro_cpfcnpj      AS abnf02 '
        sauxi001 = sauxi001 + 'ON         abnf01.idcpfpj = abnf02.idcpfpj '
        if sdefmenu == '03002B':
            sauxi001 = sauxi001 + 'INNER JOIN abnf_cadastro_funcionarios_cargos AS abnf03 '
            sauxi001 = sauxi001 + 'ON         abnf01.idcargo = abnf03.idcargo '
        # Condições
        sauxi001 = sauxi001 + 'WHERE '
        if   lparamet[0] == 0: sauxi001 = sauxi001 + 'abnf01.situreg != "C" '     # ==> Somente registros não cancelados
        elif lparamet[0] == 1: sauxi001 = sauxi001 + 'abnf01.situreg = "A" '      # ==> Somente registros ativo
        sauxi001 = sauxi001 + 'AND abnf01.idfilia = ' + str(lparamet[1])  + ' '   # ==> Somente registros da filial
        # Ordenação
        sauxi001 = sauxi001 + 'ORDER BY abnf02.nomraso, abnf01.idfunci;'
        # Estrutura de retorno
        if   sdefmenu == '03002A': sstruret = "lauxi001[1] + ' (' + str(lauxi001[2]) + ')'"
        elif sdefmenu == '03002B': sstruret = "(lauxi001[0], lauxi001[1], lauxi001[2], lauxi001[3], lauxi001[4], lauxi001[5], lauxi001[6], lauxi001[7])"
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu in ('12008A', '12008B', '12008C'):
        sauxi001 = 'SELECT '
        # Campos das tabelas
        sauxi001 = sauxi001 + 'abnf03.idsdede, '        # ID da definição de defeito
        if sdefmenu in ('12008A', '12008C'):
            sauxi001 = sauxi001 + 'abnf01.dessdeg, '    # Descrição do grupo
            sauxi001 = sauxi001 + 'abnf01.codsdeg, '    # Código do grupo
            sauxi001 = sauxi001 + 'abnf02.dessdes, '    # Descrição do subgrupo
            sauxi001 = sauxi001 + 'abnf02.codsdes, '    # Código do subgrupo
            sauxi001 = sauxi001 + 'abnf03.dessded, '    # Descrição do defeito
            sauxi001 = sauxi001 + 'abnf03.codsded  '    # Código do defeito
        elif sdefmenu == '12008B':
            sauxi001 = sauxi001 + 'abnf01.idfilia, '    # ID da filial
            sauxi001 = sauxi001 + 'abnf01.situreg, '    # Situação do registro de grupo
            sauxi001 = sauxi001 + 'abnf02.situreg, '    # Situação do registro de subgrupo
            sauxi001 = sauxi001 + 'abnf03.situreg  '    # Situação do registro de definição do defeito
        # Tabelas SQL
        sauxi001 = sauxi001 + 'FROM       abnf_sigom_cadastro_defeitos_grupos     AS abnf01 '
        sauxi001 = sauxi001 + 'INNER JOIN abnf_sigom_cadastro_defeitos_subgrupos  AS abnf02 '
        sauxi001 = sauxi001 + 'ON         abnf01.idsdegr = abnf02.idsdegr '
        sauxi001 = sauxi001 + 'INNER JOIN abnf_sigom_cadastro_defeitos_definicoes AS abnf03 '
        sauxi001 = sauxi001 + 'ON         abnf02.idsdesg = abnf03.idsdesg '
        # Condições
        sauxi001 = sauxi001 + 'WHERE '
        if sdefmenu == '12008A':
            sauxi001 = sauxi001 + '    abnf01.situreg = "' + str(lparamet[1]) + '" '    # ==> Situações de registros de grupos
            sauxi001 = sauxi001 + 'AND abnf02.situreg = "' + str(lparamet[2]) + '" '    # ==> Situações de registros de subgrupos
            sauxi001 = sauxi001 + 'AND abnf03.situreg = "' + str(lparamet[3]) + '" '    # ==> Situações de registros de definicoes
            sauxi001 = sauxi001 + 'AND abnf01.idfilia = ' + str(lparamet[0])  + ' '     # ==> Somente registros da filial
        elif sdefmenu in ('12008B', '12008C'):
            sauxi001 = sauxi001 + '    abnf03.idsdede = ' + str(lparamet[0])  + ' '     # ==> ID do registro de definição do defeito
        # Ordenação
        sauxi001 = sauxi001 + 'ORDER BY abnf01.dessdeg, abnf02.dessdes, abnf03.dessded;'
        # Estrutura de retorno
        if   sdefmenu == '12008A': sstruret = "str(lauxi001[1]) + ' (' + str(lauxi001[2]) + ') - ' + str(lauxi001[3]) + ' (' + str(lauxi001[4]) + ') - ' + str(lauxi001[5]) + ' (' + str(lauxi001[6]) + ')'"
        elif sdefmenu == '12008B': sstruret = "(lauxi001[1], lauxi001[2], lauxi001[3], lauxi001[4])"
        elif sdefmenu == '12008C': sstruret = "(lauxi001[1], lauxi001[2], lauxi001[3], lauxi001[4], lauxi001[5], lauxi001[6])"
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdefmenu == '13021A':
        sauxi001 = 'SELECT '
        # Campos das tabelas
        sauxi001 = sauxi001 + 'abnf01.idcusgr, ' # [00] ID do grupo
        sauxi001 = sauxi001 + 'abnf01.descusg, ' # [01] Descrição do grupo de usuários
        sauxi001 = sauxi001 + 'abnf01.codcusg, ' # [02] Código do grupo do usuário
        sauxi001 = sauxi001 + 'abnf01.situreg, ' # [03] Situação do grupo
        sauxi001 = sauxi001 + 'abnf02.situreg, ' # [04] Situação do vínculo do grupo
        sauxi001 = sauxi001 + 'abnf01.permaut, ' # [05] Permite definir o método automático-manual
        sauxi001 = sauxi001 + 'abnf01.perrefd, ' # [06] Permite refazer os registros de diário
        sauxi001 = sauxi001 + 'abnf01.percaal  ' # [07] Permite cancelar alterações
        # Tabelas SQL
        sauxi001 = sauxi001 + 'FROM       abnf_operacional_cadastro_grupos_usuarios          AS abnf01 '
        sauxi001 = sauxi001 + 'INNER JOIN abnf_operacional_cadastro_grupos_usuarios_vinculos AS abnf02 '
        sauxi001 = sauxi001 + 'ON         abnf01.idcusgr = abnf02.idcusgr '
        # Condições
        sauxi001 = sauxi001 + 'WHERE abnf01.situreg != "C" '                        # ==> Somente registros não cancelados (grupos de usuários)
        sauxi001 = sauxi001 + 'AND   abnf02.situreg != "C" '                        # ==> Somente registros não cancelados (vínculos de grupos de usuários)
        sauxi001 = sauxi001 + 'AND   abnf01.idfilia = ' + str(lparamet[0]) + ' '    # ==> Somente registros da filial
        sauxi001 = sauxi001 + 'AND   abnf02.idusuar = ' + str(lparamet[1]) + ';'    # ==> Somente registros do usuário
        # Estrutura de retorno
        sstruret = "[lauxi001[0], lauxi001[1], lauxi001[2], lauxi001[3], lauxi001[4], lauxi001[5], lauxi001[6], lauxi001[7]]"
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    # ◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    lsqlre01, iqtdre01 = abnf_database_executa_sql(icodbase, sauxi001)
    if stiporet == 'X':
        xmselect = []
    elif stiporet == 'L':
        if   iparlini == 0: xmselect = []
        elif iparlini == 1: xmselect = [('','')]
        elif iparlini == 2: xmselect = [(0,'Todos')]
    elif stiporet == 'D':
        if   iparlini == 0: xmselect = {}
        elif iparlini == 1: xmselect = {'':''}
        elif iparlini == 2: xmselect = {0 :'Todos'}
    for lauxi001 in lsqlre01:
        if stiporet == 'X':
            xmselect.append((
                eval(sstruret)
            ))
        elif stiporet == 'L':
            xmselect.append((
                lauxi001[0],
                eval(sstruret)
            ))
        elif stiporet == 'D':
            xmselect[lauxi001[0]] = eval(sstruret)
    return xmselect

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_database_find ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função para buscar dados personalizados em tabelas.                                                                                                 // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_database_find(icodbase, iidfilia, sdeffind, xvalfind, lparamet):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_database_find (Parâmetros para buscar dados personalizados em tabelas)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    sretmess = ''
    if False: pass
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdeffind == '000A':
        if xvalfind != '':
            lcamposb = ('idempre', 'nomefil', 'codifil')
            lfilbusc = (('idsubgr', '=', xvalfind), ('situreg', '!=', 'C'))
            lorderby = None
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_sistema_empresas_filiais', lcamposb, lfilbusc, lorderby)
            if lsqlre01 != [] and iqtdre01 > 0:
                lcamposb = ('nomeemp', 'codiemp')
                lfilbusc = (('idempre', '=', lsqlre01[0][0]), ('situreg', '!=', 'C'))
                lorderby = None
                lsqlre02, iqtdre02 = abnf_database_busca_dados_v02(icodbase, 'abnf_sistema_empresas_matrizes', lcamposb, lfilbusc, lorderby)
                if lsqlre01 != [] and iqtdre01 > 0:
                    sretmess = lsqlre02[0][0] + ' (' + str(lsqlre02[0][1]) + ') - ' + lsqlre01[0][1] + ' (' + str(lsqlre01[0][2]) + ')'
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdeffind == '001H':
        if xvalfind != '':
            lcamposb = ('sigespd', None)
            lfilbusc = (('idespdo', '=', xvalfind), ('situreg', '!=', 'C'))
            lorderby = None
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_especies_documentos', lcamposb, lfilbusc, lorderby)
            if lsqlre01 != [] and iqtdre01 > 0:
                sretmess = lsqlre01[0][0]
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdeffind == '008A':
        if xvalfind != '':
            lcamposb = ('idgrupo', 'descsub', 'codsubg')
            lfilbusc = (('idsubgr', '=', xvalfind), ('situreg', '!=', 'C'))
            lorderby = None
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_financeiro_cadastro_subgrupos', lcamposb, lfilbusc, lorderby)
            if lsqlre01 != [] and iqtdre01 > 0:
                lcamposb = ('descgru', 'codgrup')
                lfilbusc = (('idgrupo', '=', lsqlre01[0][0]), ('situreg', '!=', 'C'))
                lorderby = None
                lsqlre02, iqtdre02 = abnf_database_busca_dados_v02(icodbase, 'abnf_financeiro_cadastro_grupos', lcamposb, lfilbusc, lorderby)
                if lsqlre01 != [] and iqtdre01 > 0:
                    sretmess = lsqlre02[0][0] + ' (' + str(lsqlre02[0][1]) + ') - ' + lsqlre01[0][1] + ' (' + str(lsqlre01[0][2]) + ')'
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdeffind == '008B':
        if xvalfind != '':
            lcamposb = ('desccom', 'codcomp')
            lfilbusc = (('idcompl', '=', xvalfind), ('situreg', '!=', 'C'))
            lorderby = None
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_financeiro_cadastro_complementos', lcamposb, lfilbusc, lorderby)
            if lsqlre01 != [] and iqtdre01 > 0:
                sretmess = lsqlre01[0][0] + ' (' + str(lsqlre01[0][1]) + ')'
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdeffind == '008C':
        if xvalfind != '':
            lcamposb = ('desccec', 'codcecu')
            lfilbusc = (('idcecus', '=', xvalfind), ('situreg', '!=', 'C'))
            lorderby = None
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_financeiro_cadastro_centros_custo', lcamposb, lfilbusc, lorderby)
            if lsqlre01 != [] and iqtdre01 > 0:
                sretmess = lsqlre01[0][0] + ' (' + str(lsqlre01[0][1]) + ')'
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdeffind == '008D':
        if xvalfind != '':
            lcamposb = ('descdep', 'coddept')
            lfilbusc = (('iddepto', '=', xvalfind), ('situreg', '!=', 'C'))
            lorderby = None
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_financeiro_cadastro_departamentos', lcamposb, lfilbusc, lorderby)
            if lsqlre01 != [] and iqtdre01 > 0:
                sretmess = lsqlre01[0][0] + ' (' + str(lsqlre01[0][1]) + ')'
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdeffind == '008E':
        if xvalfind != '':
            lcamposb = ('desccon', 'codcont', 'idclfor')
            lfilbusc = (('idcontr', '=', xvalfind), ('situreg', '!=', 'C'))
            lorderby = None
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_financeiro_cadastro_contratos', lcamposb, lfilbusc, lorderby)
            if lsqlre01 != [] and iqtdre01 > 0:
                sretmess = lsqlre01[0][0] + ' (' + str(lsqlre01[0][1]) + ')'
                iidclfor = lsqlre01[0][2]
                if iidclfor > 0:
                    lcamposb = ('codclfo', 'idcpfpj')
                    lfilbusc = (('idclfor', '=', iidclfor), ('situreg', '!=', 'C'))
                    lorderby = None
                    lsqlre02, iqtdre02 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_clientes_fornecedores', lcamposb, lfilbusc, lorderby)
                    if lsqlre02 != [] and iqtdre02 > 0:
                        icodclfo = lsqlre02[0][0]
                        iidcpfpj = lsqlre02[0][1]
                        lcamposb = ('nomraso', 'codpfpj')
                        lfilbusc = (('idcpfpj', '=', iidcpfpj), ('situreg', '!=', 'C'))
                        lorderby = None
                        lsqlre03, iqtdre03 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_cpfcnpj', lcamposb, lfilbusc, lorderby)
                        if lsqlre03 != [] or iqtdre03 != 0:
                            snomraso = lsqlre03[0][0]
                            scodpfpj = lsqlre03[0][1]
                            sretmess = sretmess + ' - ' + snomraso + ' (' + str(icodclfo) + ') (' + scodpfpj + ')'
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdeffind == '008F':
        if xvalfind != '':
            lcamposb = ('descban', 'descage', 'desccon', 'codcont')
            lfilbusc = (('idconta', '=', xvalfind), ('situreg', '!=', 'C'))
            lorderby = None
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_financeiro_cadastro_contas', lcamposb, lfilbusc, lorderby)
            if lsqlre01 != [] and iqtdre01 > 0:
                sretmess = lsqlre01[0][0] + ' - ' + lsqlre01[0][1] + ' - ' + lsqlre01[0][2] + ' (' + str(lsqlre01[0][3]) + ')'
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdeffind in ['008G']:  # Complemento
        if xvalfind != '':
            sretmess = '<font style="font-family: Courier New; font-size: 16px; font-weight: bold; color: red"><b>Complemento não encontrado!</b></font>'
            lcamposb = ('desccom', 'codcomp', 'idcompl')
            lfilbusc = (('codcomp', '=', xvalfind), ('situreg', '!=', 'C'))
            lorderby = None
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_financeiro_cadastro_complementos', lcamposb, lfilbusc, lorderby)
            if lsqlre01 != [] and iqtdre01 > 0:
               return lsqlre01[0][2] # <== idcompl
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdeffind in ['010A', '010B', '010C', '010D']:  # Cliente / Fornecedor
        if xvalfind != '':
            if   lparamet[0] == 'C': sretmess = '<font style="font-family: Courier New; font-size: 16px; font-weight: bold; color: red"><b>Cliente não encontrado!</b></font>'
            elif lparamet[0] == 'F': sretmess = '<font style="font-family: Courier New; font-size: 16px; font-weight: bold; color: red"><b>Fornecedor não encontrado!</b></font>'
            lcamposb = ('idcpfpj', 'codclfo', 'idclfor')
            if   sdeffind in ['010A', '010B']: lfilbusc = (('tipclfo', '=', lparamet[0]), ('codclfo', '=', xvalfind), ('situreg', '!=', 'C'))   # Busca pelo código do cliente/fornecedor
            elif sdeffind in ['010C', '010D']: lfilbusc = (('tipclfo', '=', lparamet[0]), ('idclfor', '=', xvalfind), ('situreg', '!=', 'C'))   # Busca pelo ID do cliente/fornecedor
            lorderby = None
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_clientes_fornecedores', lcamposb, lfilbusc, lorderby)
            if lsqlre01 != [] and iqtdre01 > 0:
                if sdeffind == '010B':
                    return lsqlre01[0][2] # <== idclfor
                else:
                    lcamposb = ('nomraso', 'codpfpj')
                    lfilbusc = (('idcpfpj', '=', lsqlre01[0][0]), ('situreg', '!=', 'C'))
                    lorderby = None
                    lsqlre02, iqtdre02 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_cpfcnpj', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 != [] or iqtdre01 != 0:
                        if   sdeffind in ['010A', '010C']: sretmess = lsqlre02[0][0] + ' (' + str(lsqlre01[0][1]) + ')'                         # => Retorno sem CPF/CNPJ
                        elif sdeffind in ['010D']:         sretmess = ((lsqlre02[0][0], lsqlre01[0][1], lsqlre02[0][1]))                        # => Retorno com CPF/CNPJ (em lista)
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdeffind == '013A':
        if xvalfind != '':
            lcamposb = ('desolin', 'codolin')
            lfilbusc = (('idolinh', '=', xvalfind), ('situreg', '!=', 'C'))
            lorderby = None
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_linhas', lcamposb, lfilbusc, lorderby)
            if lsqlre01 != [] and iqtdre01 > 0:
                # sretmess = lsqlre01[0][0] + ' (' + lsqlre01[0][1] + ')'
                sretmess = lsqlre01[0][1] + ' - ' + lsqlre01[0][0]
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    elif sdeffind == '013B':
        if xvalfind != '':
            lcamposb = ('desopro', 'codopro')
            lfilbusc = (('idoproj', '=', xvalfind), ('situreg', '!=', 'C'))
            lorderby = None
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_projetos', lcamposb, lfilbusc, lorderby)
            if lsqlre01 != [] and iqtdre01 > 0:
                sretmess = lsqlre01[0][0] + ' (' + str(lsqlre01[0][1]) + ')'
    # ▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨
    return sretmess

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_database_salva_arquivos_upload ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função para salvar arquivos de upload dentro da pasta de doc do projeto e também catalogar no banco de dados cada um dos arquivos.                  // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_database_salva_arquivos_upload(icodbase, sabnproj, sabntoke, iidusucr, slogiusu, snomeusu, itimesle, bmultarq):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_database_salva_arquivos_upload (Salvando arquivos de upload)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    sdirecto = 'abnftmp/upload-' + sabntoke
    suploend = sdirecto + '/abeinfo.upload.completed'
    bvalidad = False
    larqsupl = []
    for icontd01 in range(itimesle):
        if os.path.exists(suploend):
            bvalidad = True
            break
        time.sleep(1)
    if not bvalidad:
        abnf_alert('O diretório do upload não foi encontrado! Entre em contato com o departamento de sistemas!', 4)
    else:
        bvalidad = False
        for sarquivo in os.listdir(sdirecto):
            if os.path.isfile(os.path.join(sdirecto, sarquivo)):
                if sarquivo != 'abeinfo.upload.completed':
                    scomparq = (str(uuid.uuid4()) + 'xxxxxxxxxxxxxxxxxxx xxxxxxxxxxx')[:30]                  # Complementação para o nome do arquivo (feito dessa forma para evitar que qualquer um pudesse ficar vendo os arquivos simplesmente digitando as sequencias dos nomes no navegador)
                    larqsupl.append([sarquivo, sarquivo.split(".")[-1], scomparq, None])
        itamlist = len(larqsupl)
        if itamlist == 0:
            abnf_alert('Os arquivos de upload não foram encontrados! Entre em contato com o departamento de sistemas!', 4)
        elif itamlist != 1 and not bmultarq:
            abnf_alert('Excesso de arquivos de upload foram encontrados! Entre em contato com o departamento de sistemas!', 4)
        else:
            sldocpro = abnf_websocket_local_docs(sabnproj)
            # Debug: sdbug001 = sdirecto + '<br>'
            # Debug: sdbug001 = sdbug001 + sldocpro + '<br>'
            for lauxi001 in larqsupl:
                # ****************
                # Nota: 04/07/2024
                # Apesar da função "abnf_database_insere_dados_v01" executar internamente a função "abnf_database_valor_maximo_campo" para
                # determinar o próximo ID de campos chave ("K"), essa função também vai ser executada logo abaixo porque o retorno dela
                # é essencial para determinar o novo nome do arquivo que esta sendo feito upload ("abnfuser000000001...").
                # Então é esperando que tanto abaixo quanto dentro da função "abnf_database_insere_dados_v01" seja trazido o mesmo número
                # sequencial de ID da tabela "abnf_sistema_arquivos".
                # Obviamente existe o risco de duas pessoas fazerem upload ao mesmo tempo e acabar dando divergências nos IDs gerados
                # ocasionando um nome de arquivo com ID não esperado para o registro criado em "abnf_sistema_arquivos".
                # Mas mesmo que isso aconteça, não será um problema pois o sistema não exige que o novo nome do arquivo tenha nele o número
                # de ID do registro de "abnf_sistema_arquivos", pois isto é apenas uma convenção que eu crie.
                # Todos os dados do arquivo estão gravados dentro do registro da tabela "abnf_sistema_arquivos" e é isso que identifica
                # qual é o arquivo que esta ligado a aquele registro, mesmo que não tenha o ID no nome do arquivo.
                # ****************
                iproxiid = abnf_database_valor_maximo_campo(icodbase, 'abnf_sistema_arquivos', 'idarqui', None) + 1
                snovoarq = 'abnfuser' + str(1000000000 + iproxiid)[1:] + '-' + str(lauxi001[2]) + '.' + str(lauxi001[1])
                bvalidad, iproxiid = abnf_database_insere_dados_v01(icodbase, sabnproj, 'abnf_sistema_arquivos', 'M', 'cadastro de arquivos', iidusucr, slogiusu, snomeusu,
                [
                    ['idarqui', 'K', None             , 'ID do registro'           , None, None, None],
                    ['nomearq', 'S', snovoarq         , 'Nome do arquivo'          , None, None, None],
                    ['extearq', 'S', str(lauxi001[1]) , 'Extensao do arquivo'      , None, None, None],
                    ['pastarq', 'S', sldocpro         , 'Pasta do arquivo'         , None, None, None],
                    ['nomeori', 'S', str(lauxi001[0]) , 'Nome original do arquivo' , None, None, None],
                    ['situreg', 'S', 'A'              , 'Situacao do registro'     , None, None, None],
                ])
                lauxi001[3] = iproxiid  # Guarda na lista o ID de cada registro gerado na tabela 'abnf_sistema_arquivos' para depois associar esses IDs com outras tabelas
                shutil.move(sdirecto + '/' + str(lauxi001[0]), sldocpro + str(snovoarq))    # Move o arquivo para a pasta de documentos do projeto
                shutil.rmtree(sdirecto)                                                     # Apaga o diretório criado para upload dos arquivos
                # Debug: sdbug001 = sdbug001 + str(lauxi001) + '<br>'
            # Debug: abnf_alert(sdbug001, 4)
    return bvalidad, larqsupl

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_database_retorna_empresa_filial /////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que retorna a empresa e a filial através do id da filial.                                                                                    // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_database_retorna_empresa_filial(icodbase, iidfilia):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_database_retorna_empresa_filial(icodbase, iidfilia)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    snomeemp = 'ERRO DE SISTEMA - ENTRE EM CONTATO COM DEPARTAMENTO DE SISTEMAS'
    snomefil = 'ERRO DE SISTEMA - ENTRE EM CONTATO COM DEPARTAMENTO DE SISTEMAS'
    lcamposb = ('nomefil', 'idempre')
    lfilbusc = (('idfilia', '=', iidfilia), None)
    lorderby = None
    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_sistema_empresas_filiais', lcamposb, lfilbusc, lorderby)
    if lsqlre01 != [] and iqtdre01 != 0:
        snomefil = lsqlre01[0][0]
        lcamposb = ('nomeemp', None)
        lfilbusc = (('idempre', '=', lsqlre01[0][1]), None)
        lorderby = None
        lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_sistema_empresas_matrizes', lcamposb, lfilbusc, lorderby)
        if lsqlre01 != [] and iqtdre01 != 0:
            snomeemp = lsqlre01[0][0]
    return snomeemp, snomefil

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_database_estrutura ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que retorna a estrutura de tabelas do sistema para serem usadas em vários locais como geração de logs e criação de tabelas.                  // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_database_estrutura():
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_database_estrutura()')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    ldbtabel = [
        # /// #
        ('abnf_sistema_empresas_matrizes'                                           , 'M', 'cadastro de empresas do sistema'),
        ('abnf_sistema_empresas_filiais'                                            , 'M', 'cadastro de filiais do sistema'),
        ('abnf_sistema_usuarios'                                                    , 'M', 'cadastro de usuarios do sistema'),
        ('abnf_sistema_arquivos'                                                    , 'M', 'cadastro de arquivos do sistema'),
        ('abnf_sistema_modulos_grupos'                                              , 'M', 'cadastro de grupos de modulos do sistema'),
        ('abnf_sistema_modulos_acessos'                                             , 'M', 'controle de permissao aos modulos do sistema'),
        # /// #
        ('abnf_cadastro_logradouros_cidades'                                        , 'M', 'cadastro de cidades'),
        ('abnf_cadastro_logradouros_bairros'                                        , 'M', 'cadastro de bairros'),
        ('abnf_cadastro_logradouros'                                                , 'M', 'cadastro de logradouros'),
        ('abnf_cadastro_cpfcnpj'                                                    , 'M', 'cadastro de CPF/CNPJ'),
        ('abnf_cadastro_funcionarios_cargos'                                        , 'M', 'cadastro de cargos de funcionarios'),
        ('abnf_cadastro_funcionarios'                                               , 'M', 'cadastro de funcionarios'),        
        ('abnf_cadastro_veiculos_marcas'                                            , 'M', 'cadastro de marcas de veiculos'),
        ('abnf_cadastro_veiculos_modelos'                                           , 'M', 'cadastro de modelos de veiculos'),
        ('abnf_cadastro_veiculos'                                                   , 'M', 'cadastro de veiculos'),
        ('abnf_cadastro_veiculos_km'                                                , 'M', 'cadastro de km de veiculos'),
        ('abnf_cadastro_cid_capitulos'                                              , 'M', 'cadastro de capitulos de CID'),
        ('abnf_cadastro_cid_grupos'                                                 , 'M', 'cadastro de grupos de CID'),
        ('abnf_cadastro_cid_categorias'                                             , 'M', 'cadastro de categorias de CID'),
        ('abnf_cadastro_clientes_fornecedores'                                      , 'M', 'cadastro de clientes/fornecedores'),
        ('abnf_cadastro_especies_documentos'                                        , 'M', 'cadastro de especie de documentos'),
        # /// #
        ('abnf_almoxarifado_cadastro_produtos_servicos_grupos'                      , 'M', 'cadastro de grupos de produtos e servicos'),
        ('abnf_almoxarifado_cadastro_produtos_servicos_subgrupos'                   , 'M', 'cadastro de subgrupos de produtos e servicos'),
        ('abnf_almoxarifado_cadastro_produtos_servicos_marcas'                      , 'M', 'cadastro de marcas de produtos e servicos'),
        ('abnf_almoxarifado_cadastro_produtos_servicos'                             , 'M', 'cadastro de produtos e servicos'),
        ('abnf_almoxarifado_cadastro_medidores_produtos'                            , 'M', 'cadastro de medidores de produtos'),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'M', 'movimentacao de produtos e servicos'),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'M', 'itens de movimentacao de produtos e servicos'),
        ('abnf_almoxarifado_movimentacao_medidores_produtos'                        , 'M', 'medicao de medidores de produtos'),
        # /// #
        ('abnf_preventiva_cadastro_grupos'                                          , 'M', 'cadastro de grupos de preventiva'),
        ('abnf_preventiva_cadastro_itens'                                           , 'M', 'cadastro de itens de preventiva'),
        ('abnf_preventiva_cadastro_associacao_itens_grupos'                         , 'M', 'cadastro de associacao de itens com grupos de preventiva'),
        ('abnf_preventiva_cadastro_associacao_veiculos_grupos'                      , 'M', 'cadastro de associacao de veiculos com grupos de preventiva'),
        ('abnf_preventiva_movimentacao_acao_preventiva'                             , 'M', 'movimentacao de acao de preventiva'),
        # ///
        ('abnf_financeiro_cadastro_contas'                                          , 'M', 'cadastro de contas financeiras'),
        ('abnf_financeiro_cadastro_grupos'                                          , 'M', 'cadastro de grupos financeiros'),
        ('abnf_financeiro_cadastro_subgrupos'                                       , 'M', 'cadastro de subgrupos financeiros'),
        ('abnf_financeiro_cadastro_complementos'                                    , 'M', 'cadastro de complementos'),
        ('abnf_financeiro_cadastro_centros_custo'                                   , 'M', 'cadastro de centros de custo'),
        ('abnf_financeiro_cadastro_departamentos'                                   , 'M', 'cadastro de departamentos'),
        ('abnf_financeiro_cadastro_contratos'                                       , 'M', 'cadastro de contratos'),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'F', 'movimentacao de lancamentos financeiros'),
        # /// #
        ('abnf_elevar_cadastro_passageiros'                                         , 'M', 'cadastro de passageiros do Elevar'),
        ('abnf_elevar_cadastro_locais'                                              , 'M', 'cadastro de locais do Elevar'),
        ('abnf_elevar_cadastro_finalidades'                                         , 'M', 'cadastro de finalidades do Elevar'),
        ('abnf_elevar_cadastro_servicos'                                            , 'M', 'cadastro de servicos do Elevar'),
        ('abnf_elevar_cadastro_frota_patrimonial'                                   , 'M', 'cadastro de frota patrimonial do Elevar'),
        ('abnf_elevar_cadastro_ordens_servico_padrao_grupos'                        , 'M', 'cadastro de grupos de ordens de servico padrao do Elevar'),
        ('abnf_elevar_cadastro_ordens_servico_padrao'                               , 'M', 'cadastro de de ordens de servico padrao do Elevar'),
        ('abnf_elevar_cadastro_ordens_servico_padrao_itens'                         , 'M', 'cadastro de itens de ordens de servico padrao do Elevar'),
        ('abnf_elevar_movimentacao_ordens_servico_diaria'                           , 'F', 'movimentacao de ordens de servico diaria do Elevar'),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'F', 'movimentacao de itens do programado de ordens de servico diaria do Elevar'),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'F', 'movimentacao de itens do realizado de ordens de servico diaria do Elevar'),
        # /// #
        ('abnf_sac_cadastro_usuarios_grupos'                                        , 'M', 'cadastro de grupos de usuarios do SAC'),
        ('abnf_sac_cadastro_usuarios_grupos_vinculos'                               , 'M', 'cadastro de vinculos de grupos de usuarios do SAC'),
        ('abnf_sac_cadastro_atendimentos_canais'                                    , 'M', 'cadastro de canais de atendimento do SAC'),
        ('abnf_sac_cadastro_atendimentos_tipos'                                     , 'M', 'cadastro de tipos de atendimento do SAC'),
        ('abnf_sac_cadastro_atendimentos_grupos'                                    , 'M', 'cadastro de grupos de atendimento do SAC'),
        ('abnf_sac_cadastro_atendimentos_subgrupos'                                 , 'M', 'cadastro de subgrupos de atendimento do SAC'),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'F', 'movimentacao de atendimento do SAC'),
        ('abnf_sac_movimentacao_atendimentos_complementos'                          , 'M', 'complementos de movimentacao de atendimentos do SAC'),
        ('abnf_sac_movimentacao_atendimentos_arquivos'                              , 'M', 'arquivos de movimentacao de atendimentos do SAC'),
        # /// #
        ('abnf_operacional_cadastro_locais'                                         , 'M', 'cadastro de locais operacionais'),
        ('abnf_operacional_cadastro_grupos_linhas'                                  , 'M', 'cadastro de grupo de linhas operacionais'),
        ('abnf_operacional_cadastro_linhas'                                         , 'M', 'cadastro de linhas operacionais'),
        ('abnf_operacional_cadastro_projetos'                                       , 'M', 'cadastro de projetos operacionais'),
        ('abnf_operacional_cadastro_trajetos'                                       , 'M', 'cadastro de trajetos'),
        ('abnf_operacional_cadastro_itinerarios'                                    , 'M', 'cadastro de itinerarios'),
        ('abnf_operacional_cadastro_grupos_veiculos'                                , 'M', 'cadastro de grupo de veiculos'),
        ('abnf_operacional_cadastro_grupos_veiculos_vinculos'                       , 'M', 'cadastro de vinculos de grupos de veiculos'),
        ('abnf_operacional_cadastro_prioridades_linhas'                             , 'M', 'cadastro de prioridade de linhas'),
        ('abnf_operacional_cadastro_prioridades_linhas_gv'                          , 'M', 'cadastro de vinculos de prioridade de linhas com grupos de veiculos'),
        ('abnf_operacional_cadastro_operacoes_especiais'                            , 'M', 'cadastro de operacoes especiais'),
        ('abnf_operacional_cadastro_setor_veiculos'                                 , 'M', 'cadastro de setores de veiculos'),
        ('abnf_operacional_cadastro_motivo_substituicao'                            , 'M', 'cadastro de motivos de substituicao'),
        ('abnf_operacional_cadastro_grupos_usuarios'                                , 'M', 'cadastro de grupos de usuarios do controle diario'),
        ('abnf_operacional_cadastro_grupos_usuarios_vinculos'                       , 'M', 'cadastro de vinculos de grupos de usuarios do controle diario'),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'M', 'movimentacao de propostas de OSO'),
        ('abnf_operacional_movimentacao_propostas_oso_viagens'                      , 'M', 'movimentacao de viagens de propostas de OSO'),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'M', 'movimentacao oficial de OSO'),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'M', 'movimentacao oficial de viagens de OSO'),
        ('abnf_operacional_movimentacao_oficial_oso_trajetos'                       , 'M', 'movimentacao oficial de trajetos de OSO'),
        ('abnf_operacional_movimentacao_oficial_oso_itinerarios'                    , 'M', 'movimentacao oficial de itinerarios de OSO'),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'F', 'movimentacao de programacao diaria'),
        ('abnf_operacional_movimentacao_programacao_substituicao'                   , 'F', 'movimentacao de substituicao de dados da programacao diaria'),
        ('abnf_operacional_movimentacao_programacao_automacao'                      , 'F', 'movimentacao de automacao da programacao diaria'),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'F', 'movimentacao de retencao de veiculos da programacao diaria'),
        ('abnf_operacional_entrada_saida_veiculos_locais'                           , 'M', 'locais de entrada e saide veiculos'),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'M', 'entrada e saida de veiculos'),
        ('abnf_operacional_entrada_saida_veiculos_check_list_padrao'                , 'M', 'check list padrao de veiculos'),
        ('abnf_operacional_entrada_saida_veiculos_check_list'                       , 'M', 'check list de veiculos'),
        # /// #
        ('abnf_sigom_cadastro_usuarios_grupos'                                      , 'M', 'cadastro de grupos de usuarios do SIGOM'),
        ('abnf_sigom_cadastro_usuarios_grupos_vinculos'                             , 'M', 'cadastro de vinculos de grupos de usuarios do SIGOM'),
        ('abnf_sigom_cadastro_ocorrencias_tipos'                                    , 'M', 'cadastro de tipos de ocorrencias do SIGOM'),
        ('abnf_sigom_cadastro_veiculos_situacao'                                    , 'M', 'cadastro de situacao de veiculos do SIGOM'),
        ('abnf_sigom_cadastro_classificacao'                                        , 'M', 'cadastro de classificacao do SIGOM'),
        ('abnf_sigom_cadastro_defeitos_grupos'                                      , 'M', 'cadastro de grupos de GSD do SIGOM'),
        ('abnf_sigom_cadastro_defeitos_subgrupos'                                   , 'M', 'cadastro de subgrupos de GSD do SIGOM'),
        ('abnf_sigom_cadastro_defeitos_definicoes'                                  , 'M', 'cadastro de definicoes de GSD do SIGOM'),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'M', 'movimentacao de ocorrencias do SIGOM'),
        ('abnf_sigom_movimentacao_ocorrencias_complementos'                         , 'M', 'complementos de movimentacao de ocorrencias do SIGOM'),
        ('abnf_sigom_movimentacao_ocorrencias_arquivos'                             , 'M', 'arquivos de movimentacao de ocorrencias do SIGOM'),
        # /// #
        # (Mudança de planos: usar informações fixas no lugar de tabela) ==> ('abnf_operacional_cadastro_tipos_viagem'                           , 'M', 'cadastro de tipos de viagem'),
    ]
    ldbstruc = [
        # /// #
        ('abnf_sistema_empresas_matrizes'                                           , 'idempre' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sistema_empresas_matrizes'                                           , 'codiemp' , 'int'      , None , None , 'Codigo da empresa'                                                , None, None),
        ('abnf_sistema_empresas_matrizes'                                           , 'nomeemp' , 'varchar'  , 100  , None , 'Nome da empresa'                                                  , None, None),
        ('abnf_sistema_empresas_matrizes'                                           , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sistema_empresas_matrizes'                                           , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sistema_empresas_matrizes'                                           , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sistema_empresas_matrizes'                                           , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sistema_empresas_matrizes'                                           , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_sistema_empresas_filiais'                                            , 'idfilia' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sistema_empresas_filiais'                                            , 'idempre' , 'int'      , None , None , 'ID da empresa'                                                    , 'abnf_sistema_empresas_matrizes', 'idempre'),
        ('abnf_sistema_empresas_filiais'                                            , 'codifil' , 'int'      , None , None , 'Codigo da filial'                                                 , None, None),
        ('abnf_sistema_empresas_filiais'                                            , 'nomefil' , 'varchar'  , 100  , None , 'Nome da filial'                                                   , None, None),
        ('abnf_sistema_empresas_filiais'                                            , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sistema_empresas_filiais'                                            , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sistema_empresas_filiais'                                            , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sistema_empresas_filiais'                                            , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sistema_empresas_filiais'                                            , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_sistema_usuarios'                                                    , 'idusuar' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sistema_usuarios'                                                    , 'logiusu' , 'varchar'  , 30   , None , 'Login do usuario'                                                 , None, None),
        ('abnf_sistema_usuarios'                                                    , 'senhusu' , 'varchar'  , 200  , None , 'Senha do usuario'                                                 , None, None),
        ('abnf_sistema_usuarios'                                                    , 'tipousu' , 'varchar'  , 1    , None , 'Tipo de usuario'                                                  , None, None),
        ('abnf_sistema_usuarios'                                                    , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sistema_usuarios'                                                    , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sistema_usuarios'                                                    , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sistema_usuarios'                                                    , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sistema_usuarios'                                                    , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_sistema_usuarios'                                                    , 'dthrini' , 'datetime' , None , None , 'Data/hora inicial de permissao de uso do sistema'                 , None, None),
        ('abnf_sistema_usuarios'                                                    , 'dtrhfim' , 'datetime' , None , None , 'Data/hora final de permissao de uso do sistema'                   , None, None),
        ('abnf_sistema_usuarios'                                                    , 'nomeusu' , 'varchar'  , 100  , None , 'Nome completo do usuario'                                         , None, None),
        ('abnf_sistema_usuarios'                                                    , 'emaiusu' , 'varchar'  , 100  , None , 'E-mail do usuario'                                                , None, None),
        ('abnf_sistema_usuarios'                                                    , 'idfotop' , 'int'      , None , None , 'ID da foto do perfil'                                             , 'abnf_sistema_arquivos', 'idarqui'),
        ('abnf_sistema_usuarios'                                                    , 'idgrams' , 'int'      , None , None , 'ID do grupo de acessos dos modulos do sistema'                    , 'abnf_sistema_modulos_grupos', 'idgrams'),
        # /// #
        ('abnf_sistema_arquivos'                                                    , 'idarqui' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sistema_arquivos'                                                    , 'nomearq' , 'varchar'  , 200  , None , 'Nome do arquivo'                                                  , None, None),
        ('abnf_sistema_arquivos'                                                    , 'extearq' , 'varchar'  , 20   , None , 'Extensao do arquivo'                                              , None, None),
        ('abnf_sistema_arquivos'                                                    , 'pastarq' , 'varchar'  , 200  , None , 'Pasta do arquivo'                                                 , None, None),
        ('abnf_sistema_arquivos'                                                    , 'nomeori' , 'varchar'  , 200  , None , 'Nome original do arquivo'                                         , None, None),
        ('abnf_sistema_arquivos'                                                    , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sistema_arquivos'                                                    , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sistema_arquivos'                                                    , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sistema_arquivos'                                                    , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sistema_arquivos'                                                    , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_sistema_modulos_grupos'                                              , 'idgrams' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sistema_modulos_grupos'                                              , 'codgrup' , 'int'      , None , None , 'Codigo do grupo'                                                  , None, None),
        ('abnf_sistema_modulos_grupos'                                              , 'descgru' , 'varchar'  , 100  , None , 'Descricao do grupo'                                               , None, None),
        ('abnf_sistema_modulos_grupos'                                              , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sistema_modulos_grupos'                                              , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sistema_modulos_grupos'                                              , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sistema_modulos_grupos'                                              , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sistema_modulos_grupos'                                              , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_sistema_modulos_acessos'                                             , 'idmodac' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sistema_modulos_acessos'                                             , 'idgrams' , 'int'      , None , None , 'ID do grupo de acessos dos modulos do sistema'                    , 'abnf_sistema_modulos_grupos', 'idgrams'),
        ('abnf_sistema_modulos_acessos'                                             , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        ('abnf_sistema_modulos_acessos'                                             , 'codmodu' , 'varchar'  , 9    , None , 'Codigo do modulo'                                                 , None, None),
        ('abnf_sistema_modulos_acessos'                                             , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sistema_modulos_acessos'                                             , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sistema_modulos_acessos'                                             , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sistema_modulos_acessos'                                             , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sistema_modulos_acessos'                                             , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_cadastro_logradouros_cidades'                                        , 'idcidad' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_cadastro_logradouros_cidades'                                        , 'codcida' , 'int'      , None , None , 'Codigo da cidade'                                                 , None, None),
        ('abnf_cadastro_logradouros_cidades'                                        , 'descida' , 'varchar'  , 100  , None , 'Descricao da cidade'                                              , None, None),
        ('abnf_cadastro_logradouros_cidades'                                        , 'desesta' , 'varchar'  , 2    , None , 'Descricao do estado'                                              , None, None),
        ('abnf_cadastro_logradouros_cidades'                                        , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_cadastro_logradouros_cidades'                                        , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_logradouros_cidades'                                        , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_logradouros_cidades'                                        , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_cadastro_logradouros_cidades'                                        , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_cadastro_logradouros_bairros'                                        , 'idbairr' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_cadastro_logradouros_bairros'                                        , 'codbair' , 'int'      , None , None , 'Codigo do bairro'                                                 , None, None),
        ('abnf_cadastro_logradouros_bairros'                                        , 'desbair' , 'varchar'  , 100  , None , 'Descricao do bairro'                                              , None, None),
        ('abnf_cadastro_logradouros_bairros'                                        , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_cadastro_logradouros_bairros'                                        , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_logradouros_bairros'                                        , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_logradouros_bairros'                                        , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_cadastro_logradouros_bairros'                                        , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_cadastro_logradouros_bairros'                                        , 'idcidad' , 'int'      , None , None , 'ID da cidade'                                                     , 'abnf_cadastro_logradouros_cidades', 'idcidad'),
        # /// #
        ('abnf_cadastro_logradouros'                                                , 'idlogra' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_cadastro_logradouros'                                                , 'codlogr' , 'int'      , None , None , 'Codigo do logradouro'                                             , None, None),
        ('abnf_cadastro_logradouros'                                                , 'tiplogr' , 'varchar'  , 50   , None , 'Tipo de logradouro'                                               , None, None),
        ('abnf_cadastro_logradouros'                                                , 'deslogr' , 'varchar'  , 200  , None , 'Descricao do logradouro'                                          , None, None),
        ('abnf_cadastro_logradouros'                                                , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_cadastro_logradouros'                                                , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_logradouros'                                                , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_logradouros'                                                , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_cadastro_logradouros'                                                , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_cadastro_logradouros'                                                , 'idbairr' , 'int'      , None , None , 'ID do bairro'                                                     , 'abnf_cadastro_logradouros_bairros', 'idbairr'),
        # /// #
        ('abnf_cadastro_cpfcnpj'                                                    , 'idcpfpj' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'codpfpj' , 'varchar'  , 20   , None , 'Codigo do CPF/CNPJ'                                               , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'tippfpj' , 'varchar'  , 1    , None , 'Tipo de pessoa'                                                   , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'nomraso' , 'varchar'  , 100  , None , 'Nome/razao social'                                                , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'nomfant' , 'varchar'  , 100  , None , 'Nome fantasia'                                                    , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_cpfcnpj'                                                    , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_cpfcnpj'                                                    , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'idfotof' , 'int'      , None , None , 'ID da foto'                                                       , 'abnf_sistema_arquivos', 'idarqui'),
        ('abnf_cadastro_cpfcnpj'                                                    , 'idlogra' , 'int'      , None , None , 'ID do logradouro'                                                 , 'abnf_cadastro_logradouros', 'idlogra'),
        ('abnf_cadastro_cpfcnpj'                                                    , 'logrnum' , 'varchar'  , 20   , None , 'Logradouro (numero)'                                              , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'logrcom' , 'varchar'  , 100  , None , 'Logradouro (complemento)'                                         , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'logrcep' , 'varchar'  , 10   , None , 'Logradouro (CEP)'                                                 , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'sexoxxx' , 'varchar'  , 1    , None , 'Sexo'                                                             , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'rgiexxx' , 'varchar'  , 20   , None , 'RG/IE'                                                            , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'cnhxxxx' , 'varchar'  , 20   , None , 'CNH'                                                              , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'inscmun' , 'varchar'  , 20   , None , 'Inscricao municipal'                                              , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'titenum' , 'varchar'  , 20   , None , 'Titulo de eleitor - Numero'                                       , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'titezon' , 'varchar'  , 10   , None , 'Titulo de eleitor - Zona'                                         , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'titesec' , 'varchar'  , 10   , None , 'Titulo de eleitor - Secao'                                        , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'certres' , 'varchar'  , 20   , None , 'Certificado de reservista'                                        , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'datanas' , 'date'     , None , None , 'Data de nascimento'                                               , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'datacas' , 'date'     , None , None , 'Data de casamento'                                                , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'datafal' , 'date'     , None , None , 'Data de falecimento'                                              , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'nomepai' , 'varchar'  , 100  , None , 'Nome pai'                                                         , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'nomemae' , 'varchar'  , 100  , None , 'Nome mae'                                                         , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'nomecon' , 'varchar'  , 100  , None , 'Nome conjuge'                                                     , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'telef01' , 'varchar'  , 20   , None , 'Telefone 01'                                                      , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'telef02' , 'varchar'  , 20   , None , 'Telefone 02'                                                      , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'telef03' , 'varchar'  , 20   , None , 'Telefone 03'                                                      , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'telef04' , 'varchar'  , 20   , None , 'Telefone 04'                                                      , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'telef05' , 'varchar'  , 20   , None , 'Telefone 05'                                                      , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'email01' , 'varchar'  , 100  , None , 'E-mail 01'                                                        , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'email02' , 'varchar'  , 100  , None , 'E-mail 02'                                                        , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'email03' , 'varchar'  , 100  , None , 'E-mail 03'                                                        , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'email04' , 'varchar'  , 100  , None , 'E-mail 04'                                                        , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'email05' , 'varchar'  , 100  , None , 'E-mail 05'                                                        , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'hpage01' , 'varchar'  , 100  , None , 'Home page 01'                                                     , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'hpage02' , 'varchar'  , 100  , None , 'Home page 02'                                                     , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'hpage03' , 'varchar'  , 100  , None , 'Home page 03'                                                     , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'hpage04' , 'varchar'  , 100  , None , 'Home page 04'                                                     , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'hpage05' , 'varchar'  , 100  , None , 'Home page 05'                                                     , None, None),
        ('abnf_cadastro_cpfcnpj'                                                    , 'observa' , 'text'     , None , None , 'Observacao'                                                       , None, None),
        # /// #
        ('abnf_cadastro_funcionarios_cargos'                                        , 'idcargo' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_cadastro_funcionarios_cargos'                                        , 'codcarg' , 'int'      , None , None , 'Codigo do cargo'                                                  , None, None),
        ('abnf_cadastro_funcionarios_cargos'                                        , 'descarg' , 'varchar'  , 100  , None , 'Nome do cargo'                                                    , None, None),
        ('abnf_cadastro_funcionarios_cargos'                                        , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_cadastro_funcionarios_cargos'                                        , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_funcionarios_cargos'                                        , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_funcionarios_cargos'                                        , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_cadastro_funcionarios_cargos'                                        , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_cadastro_funcionarios_cargos'                                        , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #
        ('abnf_cadastro_funcionarios'                                               , 'idfunci' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_cadastro_funcionarios'                                               , 'codfunc' , 'int'      , None , None , 'Codigo do funcionario'                                            , None, None),
        ('abnf_cadastro_funcionarios'                                               , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_cadastro_funcionarios'                                               , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_funcionarios'                                               , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_funcionarios'                                               , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_cadastro_funcionarios'                                               , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_cadastro_funcionarios'                                               , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        ('abnf_cadastro_funcionarios'                                               , 'idcpfpj' , 'datetime' , None , None , 'ID cadastro CPF/CNPJ'                                             , 'abnf_cadastro_cpfcnpj', 'idcpfpj'),
        ('abnf_cadastro_funcionarios'                                               , 'idcargo' , 'datetime' , None , None , 'ID do cargo'                                                      , 'abnf_cadastro_funcionarios_cargos', 'idcargo'),
        ('abnf_cadastro_funcionarios'                                               , 'dataadm' , 'date'     , None , None , 'Data de admissao'                                                 , None, None),
        ('abnf_cadastro_funcionarios'                                               , 'dataafa' , 'date'     , None , None , 'Data de afastamento'                                              , None, None),
        ('abnf_cadastro_funcionarios'                                               , 'datades' , 'date'     , None , None , 'Data de desligamento'                                             , None, None),
        ('abnf_cadastro_funcionarios'                                               , 'dataitr' , 'date'     , None , None , 'Data inicio de treinamento'                                       , None, None),
        ('abnf_cadastro_funcionarios'                                               , 'dataftr' , 'date'     , None , None , 'Data fim de treinamento'                                          , None, None),
        ('abnf_cadastro_funcionarios'                                               , 'motelev' , 'boolean'  , None , None , 'Motorista do Elevar'                                              , None, None),
        ('abnf_cadastro_funcionarios'                                               , 'observa' , 'text'     , None , None , 'Observacao'                                                       , None, None),
        # /// #
        ('abnf_cadastro_veiculos_marcas'                                            , 'idmarca' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_cadastro_veiculos_marcas'                                            , 'codmarc' , 'int'      , None , None , 'Codigo da marca de veiculo'                                       , None, None),
        ('abnf_cadastro_veiculos_marcas'                                            , 'desmarc' , 'varchar'  , 100  , None , 'Descricao da marca de veiculo'                                    , None, None),
        ('abnf_cadastro_veiculos_marcas'                                            , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_cadastro_veiculos_marcas'                                            , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_veiculos_marcas'                                            , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_veiculos_marcas'                                            , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_cadastro_veiculos_marcas'                                            , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_cadastro_veiculos_modelos'                                           , 'idmodel' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_cadastro_veiculos_modelos'                                           , 'codmode' , 'int'      , None , None , 'Codigo do modelo de veiculo'                                      , None, None),
        ('abnf_cadastro_veiculos_modelos'                                           , 'desmode' , 'varchar'  , 100  , None , 'Descricao do modelo de veiculo'                                   , None, None),
        ('abnf_cadastro_veiculos_modelos'                                           , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_cadastro_veiculos_modelos'                                           , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_veiculos_modelos'                                           , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_veiculos_modelos'                                           , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_cadastro_veiculos_modelos'                                           , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_cadastro_veiculos_modelos'                                           , 'idmarca' , 'int'      , None , None , 'ID da marca de veiculo'                                           , 'abnf_cadastro_veiculos_marcas', 'idmarca'),
        # /// #
        ('abnf_cadastro_veiculos'                                                   , 'idveicu' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'prefvei' , 'varchar'  , 20   , None , 'Prefixo do veiculo'                                               , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'placave' , 'varchar'  , 10   , None , 'Placa do veiculo'                                                 , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_veiculos'                                                   , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_veiculos'                                                   , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        ('abnf_cadastro_veiculos'                                                   , 'idmodel' , 'int'      , None , None , 'ID do modelo de veiculo'                                          , 'abnf_cadastro_veiculos_modelos', 'idmodel'),
        ('abnf_cadastro_veiculos'                                                   , 'renavam' , 'varchar'  , 20   , None , 'Renavam do veiculo'                                               , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'chassiv' , 'varchar'  , 20   , None , 'Chassi do veiculo'                                                , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'corveic' , 'varchar'  , 20   , None , 'Cor do veiculo'                                                   , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'anofabr' , 'int'      , None , None , 'Ano de fabricacao'                                                , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'anomode' , 'int'      , None , None , 'Ano do modelo'                                                    , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'tipmoto' , 'int'      , None , None , 'Tipo de motor'                                                    , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'tipcomb' , 'int'      , None , None , 'Tipo de combustivel'                                              , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'captanq' , 'int'      , None , None , 'Capacidade em litros do tanque de combustivel'                    , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'lugsent' , 'int'      , None , None , 'Numero de lugares sentados'                                       , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'lugempe' , 'int'      , None , None , 'Numero de lugares em pe'                                          , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'lugroda' , 'int'      , None , None , 'Numero de lugares para cadeirantes'                               , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'lugacom' , 'int'      , None , None , 'Numero de lugares para acompanhantes'                             , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'numport' , 'int'      , None , None , 'Numero de portas'                                                 , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'dataini' , 'date'     , None , None , 'Data de compra do veiculo ou do seu inicio de atividades'         , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'datafim' , 'date'     , None , None , 'Data de venda do veiculo ou do seu termino de atividades'         , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'arcondi' , 'boolean'  , None , None , 'Veiculo tem ar-condicionado'                                      , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'veielev' , 'boolean'  , None , None , 'Veiculo do Elevar'                                                , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'observa' , 'text'     , None , None , 'Observacao'                                                       , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'libpsod' , 'boolean'  , None , None , 'Libera o odometro para ser lancado como novo'                     , None, None),
        ('abnf_cadastro_veiculos'                                                   , 'libpsro' , 'boolean'  , None , None , 'Libera a roleta para ser lancada como nova'                       , None, None),
        # /// #
        ('abnf_cadastro_veiculos_km'                                                , 'idkmvei' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_cadastro_veiculos_km'                                                , 'idveicu' , 'int'      , None , None , 'ID do veiculo'                                                    , 'abnf_cadastro_veiculos', 'idveicu'),
        ('abnf_cadastro_veiculos_km'                                                , 'dtregkm' , 'datetime' , None , None , 'Data do registro do km'                                           , None, None),
        ('abnf_cadastro_veiculos_km'                                                , 'kmveicu' , 'int'      , None , None , 'Km registrado'                                                    , None, None),
        ('abnf_cadastro_veiculos_km'                                                , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_cadastro_veiculos_km'                                                , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_veiculos_km'                                                , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_veiculos_km'                                                , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_cadastro_veiculos_km'                                                , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_cadastro_veiculos_km'                                                , 'tabgrup' , 'int'      , None , None , 'Grupo do modulo vinculado ao registro'                            , None, None),
        ('abnf_cadastro_veiculos_km'                                                , 'tabsubg' , 'int'      , None , None , 'Subgrupo do modulo vinculado ao registro'                         , None, None),
        ('abnf_cadastro_veiculos_km'                                                , 'tiporeg' , 'varchar'  , 1    , None , 'Tipo de registro'                                                 , None, None),
        # /// #
        ('abnf_cadastro_clientes_fornecedores'                                      , 'idclfor' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_cadastro_clientes_fornecedores'                                      , 'tipclfo' , 'varchar'  , 1    , None , 'Tipo de registro'                                                 , None, None),
        ('abnf_cadastro_clientes_fornecedores'                                      , 'codclfo' , 'varchar'  , 20   , None , 'Codigo do cliente/fornecedor'                                     , None, None),
        ('abnf_cadastro_clientes_fornecedores'                                      , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_cadastro_clientes_fornecedores'                                      , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_clientes_fornecedores'                                      , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_clientes_fornecedores'                                      , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_cadastro_clientes_fornecedores'                                      , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_cadastro_clientes_fornecedores'                                      , 'idcpfpj' , 'int'      , None , None , 'ID do CPF/CNPJ'                                                   , 'abnf_cadastro_cpfcnpj', 'idcpfpj'),
        ('abnf_cadastro_clientes_fornecedores'                                      , 'ccontab' , 'int'      , None , None , 'Conta contabil'                                                   , None, None),
        ('abnf_cadastro_clientes_fornecedores'                                      , 'observa' , 'text'     , None , None , 'Observacao'                                                       , None, None),
        # /// #
        ('abnf_cadastro_especies_documentos'                                        , 'idespdo' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_cadastro_especies_documentos'                                        , 'sigespd' , 'varchar'  , 3    , None , 'Sigla da especie de documento'                                    , None, None),
        ('abnf_cadastro_especies_documentos'                                        , 'desespd' , 'varchar'  , 100  , None , 'Descricao da especie de documento'                                , None, None),
        ('abnf_cadastro_especies_documentos'                                        , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_cadastro_especies_documentos'                                        , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_especies_documentos'                                        , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_cadastro_especies_documentos'                                        , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_cadastro_especies_documentos'                                        , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_almoxarifado_cadastro_produtos_servicos_grupos'                      , 'idgrupo' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos_grupos'                      , 'codgrup' , 'int'      , None , None , 'Codigo do grupo'                                                  , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos_grupos'                      , 'descgru' , 'varchar'  , 100  , None , 'Descricao do grupo'                                               , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos_grupos'                      , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos_grupos'                      , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_almoxarifado_cadastro_produtos_servicos_grupos'                      , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_almoxarifado_cadastro_produtos_servicos_grupos'                      , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos_grupos'                      , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_almoxarifado_cadastro_produtos_servicos_subgrupos'                   , 'idsubgr' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos_subgrupos'                   , 'codsubg' , 'int'      , None , None , 'Codigo do subgrupo'                                               , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos_subgrupos'                   , 'descsub' , 'varchar'  , 100  , None , 'Descricao do subgrupo'                                            , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos_subgrupos'                   , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos_subgrupos'                   , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_almoxarifado_cadastro_produtos_servicos_subgrupos'                   , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_almoxarifado_cadastro_produtos_servicos_subgrupos'                   , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos_subgrupos'                   , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos_subgrupos'                   , 'idgrupo' , 'int'      , None , None , 'ID do grupo financeiro'                                           , 'abnf_almoxarifado_cadastro_produtos_servicos_grupos', 'idgrupo'),
        # /// #
        ('abnf_almoxarifado_cadastro_produtos_servicos_marcas'                      , 'idmarca' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos_marcas'                      , 'codmarc' , 'int'      , None , None , 'Codigo da marca'                                                  , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos_marcas'                      , 'descmar' , 'varchar'  , 100  , None , 'Descricao da marca'                                               , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos_marcas'                      , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos_marcas'                      , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_almoxarifado_cadastro_produtos_servicos_marcas'                      , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_almoxarifado_cadastro_produtos_servicos_marcas'                      , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos_marcas'                      , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_almoxarifado_cadastro_produtos_servicos'                             , 'idprser' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos'                             , 'codprse' , 'int'      , None , None , 'Codigo do produto/servico'                                        , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos'                             , 'descprs' , 'varchar'  , 200  , None , 'Descricao do produto/servico'                                     , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos'                             , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos'                             , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_almoxarifado_cadastro_produtos_servicos'                             , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_almoxarifado_cadastro_produtos_servicos'                             , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos'                             , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos'                             , 'tiporeg' , 'varchar'  , 1    , None , 'Tipo de registro'                                                 , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos'                             , 'idsubgr' , 'int'      , None , None , 'ID do subgrupo do produto/servico'                                , 'abnf_almoxarifado_cadastro_produtos_servicos_subgrupos', 'idsubgr'),
        ('abnf_almoxarifado_cadastro_produtos_servicos'                             , 'idmarca' , 'int'      , None , None , 'ID da marca do produto/servico'                                   , 'abnf_almoxarifado_cadastro_produtos_servicos_marcas', 'idsubgr'),
        ('abnf_almoxarifado_cadastro_produtos_servicos'                             , 'uniesto' , 'int'      , None , None , 'Unidade de estoque'                                               , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos'                             , 'codloca' , 'varchar'  , 10   , None , 'Codigo de localizacao'                                            , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos'                             , 'ncmsbxx' , 'int'      , None , None , 'NCM/SB'                                                           , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos'                             , 'cstxxxx' , 'int'      , None , None , 'CST'                                                              , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos'                             , 'perldve' , 'varchar'  , 1    , None , 'Permite saida em lote por veiculo'                                , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos'                             , 'perdire' , 'varchar'  , 1    , None , 'Permite consumo direto por veiculo'                               , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos'                             , 'tipopne' , 'varchar'  , 1    , None , 'Tipo de pneu'                                                     , None, None),
        ('abnf_almoxarifado_cadastro_produtos_servicos'                             , 'qtdesto' , 'decimal'  , 16   , 6    , 'Quantidade em estoque'                                            , None, None),
        # /// #
        ('abnf_almoxarifado_cadastro_medidores_produtos'                            , 'idmedid' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_almoxarifado_cadastro_medidores_produtos'                            , 'codmedi' , 'int'      , None , None , 'Codigo do medidor de produto'                                     , None, None),
        ('abnf_almoxarifado_cadastro_medidores_produtos'                            , 'descmed' , 'varchar'  , 200  , None , 'Descricao do medidor de produto'                                  , None, None),
        ('abnf_almoxarifado_cadastro_medidores_produtos'                            , 'idprser' , 'int'      , None , None , 'ID do produto'                                                    , 'abnf_almoxarifado_cadastro_produtos_servicos', 'idprser'),
        ('abnf_almoxarifado_cadastro_medidores_produtos'                            , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        ('abnf_almoxarifado_cadastro_medidores_produtos'                            , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_almoxarifado_cadastro_medidores_produtos'                            , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_almoxarifado_cadastro_medidores_produtos'                            , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_almoxarifado_cadastro_medidores_produtos'                            , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_almoxarifado_cadastro_medidores_produtos'                            , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'idcmprs' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'nrdocnf' , 'bigint'   , None , None , 'Numero do documento/nota fiscal'                                  , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'serienf' , 'varchar'  , 5    , None , 'serie da nota fiscal'                                             , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'idespdo' , 'int'      , None , None , 'especie do documento'                                             , 'abnf_cadastro_especies_documentos', 'idespdo'),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'tiporeg' , 'int'      , None , None , 'Tipo de registro'                                                 , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'regfech' , 'boolean'  , None , None , 'Registro fechado'                                                 , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'idclfor' , 'int'      , None , None , 'ID do cliente/fornecedor'                                         , 'abnf_cadastro_clientes_fornecedores', 'idclfor'),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'idsubgr' , 'int'      , None , None , 'ID do subgrupo financeiro'                                        , 'abnf_financeiro_cadastro_subgrupos', 'idsubgr'),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'idfabos' , 'int'      , None , None , 'ID do funcionario que solicitou a ordem de servico'               , 'abnf_cadastro_funcionarios', 'idfunci'),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'vatoprs' , 'decimal'  , 10   , 2    , 'Valor total de produtos e servicos'                               , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'valabat' , 'decimal'  , 10   , 2    , 'Valor abatimento/desconto/devolucao'                              , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'vatonot' , 'decimal'  , 10   , 2    , 'Valor total do documento'                                         , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'bcaicst' , 'decimal'  , 10   , 2    , 'Base de calculo do ICMS/ST'                                       , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'vrticst' , 'decimal'  , 10   , 2    , 'Valor de retencao do ICMS/ST'                                     , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'datalan' , 'datetime' , None , None , 'Data/hora do lancamento do registro'                              , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'datacan' , 'datetime' , None , None , 'Data/hora do cancelamento do registro'                            , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'datafin' , 'datetime' , None , None , 'Data/hora da finalizacao'                                         , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'datadoc' , 'date'     , None , None , 'Data do documento'                                                , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'dataent' , 'date'     , None , None , 'Data da entrada'                                                  , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'observa' , 'text'     , None , None , 'Observacao'                                                       , None, None),
        # /// #
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'iditmps' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'idcmprs' , 'int'      , None , None , 'ID do subgrupo do produto/servico'                                , 'abnf_almoxarifado_movimentacao_produtos_servicos', 'idcmprs'),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'idprser' , 'int'      , None , None , 'ID do produto/servico'                                            , 'abnf_almoxarifado_cadastro_produtos_servicos', 'idprser'),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'tipomov' , 'varchar'  , 1    , None , 'Tipo de movimentacao'                                             , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'qtdmovi' , 'decimal'  , 16   , 6    , 'Quantidade movimentada do produto/servico'                        , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'valunit' , 'decimal'  , 13   , 6    , 'Valor unitario do produto/servico'                                , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'valdesc' , 'decimal'  , 10   , 2    , 'Valor desconto'                                                   , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'valriss' , 'decimal'  , 10   , 2    , 'Valor retencao ISSQN'                                             , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'valrpis' , 'decimal'  , 10   , 2    , 'Valor retencao PIS/COFINS/CSLL'                                   , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'valrins' , 'decimal'  , 10   , 2    , 'Valor retencao INSS'                                              , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'valrirr' , 'decimal'  , 10   , 2    , 'Valor retencao IRRF'                                              , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'valoutr' , 'decimal'  , 10   , 2    , 'Valor outros (Frete/IPI/Desp.Acess)'                              , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'valtota' , 'decimal'  , 10   , 2    , 'Valor total do produto/servico'                                   , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'cfopxxx' , 'int'      , None , None , 'CFOP'                                                             , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'bcaicms' , 'decimal'  , 10   , 2    , 'Base de calculo do ICMS'                                          , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'vrticms' , 'decimal'  , 10   , 2    , 'Valor de retencao do ICMS'                                        , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'valipix' , 'decimal'  , 10   , 2    , 'Valor IPI'                                                        , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'datalan' , 'datetime' , None , None , 'Data/hora do lancamento do registro'                              , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'datacan' , 'datetime' , None , None , 'Data/hora do cancelamento do registro'                            , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'idveicu' , 'int'      , None , None , 'ID do veiculo'                                                    , 'abnf_cadastro_veiculos', 'idveicu'),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'odomvei' , 'int'      , None , None , 'Odometro do veiculo'                                              , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'idmedid' , 'int'      , None , None , 'ID do medidor de produto'                                         , 'abnf_almoxarifado_movimentacao_medidores_produtos', 'idcmmed'),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'qtdesat' , 'decimal'  , 16   , 6    , 'Quantidade encontrada em estoque quando registro ativo'           , None, None),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'qtdesca' , 'decimal'  , 16   , 6    , 'Quantidade encontrada em estoque quando registro cancelado'       , None, None),
        # /// #
        ('abnf_almoxarifado_movimentacao_medidores_produtos'                        , 'idcmmed' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_almoxarifado_movimentacao_medidores_produtos'                        , 'idmedid' , 'int'      , None , None , 'ID do medidor'                                                    , 'abnf_almoxarifado_cadastro_medidores_produtos', 'idmedid'),
        ('abnf_almoxarifado_movimentacao_medidores_produtos'                        , 'datamed' , 'date'     , None , None , 'Data da medicao'                                                  , None, None),
        ('abnf_almoxarifado_movimentacao_medidores_produtos'                        , 'valmedi' , 'decimal'  , 16   , 6    , 'Valor da medicao'                                                 , None, None),
        ('abnf_almoxarifado_movimentacao_medidores_produtos'                        , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_almoxarifado_movimentacao_medidores_produtos'                        , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_almoxarifado_movimentacao_medidores_produtos'                        , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_almoxarifado_movimentacao_medidores_produtos'                        , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_almoxarifado_movimentacao_medidores_produtos'                        , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_preventiva_cadastro_grupos'                                          , 'idgrpre' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_preventiva_cadastro_grupos'                                          , 'codgrpr' , 'int'      , None , None , 'Codigo do grupo de preventiva'                                    , None, None),
        ('abnf_preventiva_cadastro_grupos'                                          , 'descgrp' , 'varchar'  , 100  , None , 'Descricao do grupo de preventiva'                                 , None, None),
        ('abnf_preventiva_cadastro_grupos'                                          , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_preventiva_cadastro_grupos'                                          , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_preventiva_cadastro_grupos'                                          , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_preventiva_cadastro_grupos'                                          , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_preventiva_cadastro_grupos'                                          , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_preventiva_cadastro_itens'                                           , 'iditpre' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_preventiva_cadastro_itens'                                           , 'coditpr' , 'int'      , None , None , 'Codigo do item de preventiva'                                     , None, None),
        ('abnf_preventiva_cadastro_itens'                                           , 'descitp' , 'varchar'  , 100  , None , 'Descricao do item de preventiva'                                  , None, None),
        ('abnf_preventiva_cadastro_itens'                                           , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_preventiva_cadastro_itens'                                           , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_preventiva_cadastro_itens'                                           , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_preventiva_cadastro_itens'                                           , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_preventiva_cadastro_itens'                                           , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_preventiva_cadastro_associacao_itens_grupos'                         , 'idassig' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_preventiva_cadastro_associacao_itens_grupos'                         , 'idgrpre' , 'int'      , None , None , 'ID do grupo de preventiva'                                        , 'abnf_preventiva_cadastro_grupos', 'idgrpre'),
        ('abnf_preventiva_cadastro_associacao_itens_grupos'                         , 'iditpre' , 'int'      , None , None , 'ID do item de preventiva'                                         , 'abnf_preventiva_cadastro_itens', 'iditpre'),
        ('abnf_preventiva_cadastro_associacao_itens_grupos'                         , 'kmpreve' , 'int'      , None , None , 'Km de preventiva'                                                 , None, None),
        ('abnf_preventiva_cadastro_associacao_itens_grupos'                         , 'kmaviso' , 'int'      , None , None , 'Km de aviso anticipado'                                           , None, None),
        ('abnf_preventiva_cadastro_associacao_itens_grupos'                         , 'kmtoler' , 'int'      , None , None , 'Km de tolerancia'                                                 , None, None),
        ('abnf_preventiva_cadastro_associacao_itens_grupos'                         , 'diaspre' , 'int'      , None , None , 'Dias de preventiva'                                               , None, None),
        ('abnf_preventiva_cadastro_associacao_itens_grupos'                         , 'diasavi' , 'int'      , None , None , 'Dias de aviso anticipado'                                         , None, None),
        ('abnf_preventiva_cadastro_associacao_itens_grupos'                         , 'diastol' , 'int'      , None , None , 'Dias de tolerancia'                                               , None, None),
        ('abnf_preventiva_cadastro_associacao_itens_grupos'                         , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_preventiva_cadastro_associacao_itens_grupos'                         , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_preventiva_cadastro_associacao_itens_grupos'                         , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_preventiva_cadastro_associacao_itens_grupos'                         , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_preventiva_cadastro_associacao_itens_grupos'                         , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_preventiva_cadastro_associacao_veiculos_grupos'                      , 'idassvg' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_preventiva_cadastro_associacao_veiculos_grupos'                      , 'idgrpre' , 'int'      , None , None , 'ID do grupo de preventiva'                                        , 'abnf_preventiva_cadastro_grupos', 'idgrpre'),
        ('abnf_preventiva_cadastro_associacao_veiculos_grupos'                      , 'idveicu' , 'int'      , None , None , 'ID do veiculo'                                                    , 'abnf_cadastro_veiculos', 'idveicu'),
        ('abnf_preventiva_cadastro_associacao_veiculos_grupos'                      , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_preventiva_cadastro_associacao_veiculos_grupos'                      , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_preventiva_cadastro_associacao_veiculos_grupos'                      , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_preventiva_cadastro_associacao_veiculos_grupos'                      , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_preventiva_cadastro_associacao_veiculos_grupos'                      , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_preventiva_movimentacao_acao_preventiva'                             , 'idacpre' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_preventiva_movimentacao_acao_preventiva'                             , 'datarea' , 'date'     , None , None , 'Data da realizacao da preventiva'                                 , None, None),
        ('abnf_preventiva_movimentacao_acao_preventiva'                             , 'idveicu' , 'int'      , None , None , 'ID do veiculo'                                                    , 'abnf_cadastro_veiculos', 'idveicu'),
        ('abnf_preventiva_movimentacao_acao_preventiva'                             , 'iditpre' , 'int'      , None , None , 'ID do item de preventiva'                                         , 'abnf_preventiva_cadastro_itens', 'iditpre'),
        ('abnf_preventiva_movimentacao_acao_preventiva'                             , 'idgrpre' , 'int'      , None , None , 'ID do grupo de preventiva'                                        , 'abnf_preventiva_cadastro_grupos', 'idgrpre'),
        ('abnf_preventiva_movimentacao_acao_preventiva'                             , 'odomvei' , 'int'      , None , None , 'Odometro do veiculo'                                              , None, None),
        ('abnf_preventiva_movimentacao_acao_preventiva'                             , 'idfunci' , 'int'      , None , None , 'ID do funcionario que realizou a preventiva'                      , 'abnf_cadastro_funcionarios', 'idfunci'),
        ('abnf_preventiva_movimentacao_acao_preventiva'                             , 'observa' , 'text'     , None , None , 'Observacao'                                                       , None, None),
        ('abnf_preventiva_movimentacao_acao_preventiva'                             , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_preventiva_movimentacao_acao_preventiva'                             , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_preventiva_movimentacao_acao_preventiva'                             , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_preventiva_movimentacao_acao_preventiva'                             , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_preventiva_movimentacao_acao_preventiva'                             , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_financeiro_cadastro_contas'                                          , 'idconta' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_financeiro_cadastro_contas'                                          , 'codcont' , 'int'      , None , None , 'Codigo da conta'                                                  , None, None),
        ('abnf_financeiro_cadastro_contas'                                          , 'descban' , 'varchar'  , 100  , None , 'Banco'                                                            , None, None),
        ('abnf_financeiro_cadastro_contas'                                          , 'descage' , 'varchar'  , 100  , None , 'Agencia'                                                          , None, None),
        ('abnf_financeiro_cadastro_contas'                                          , 'desccon' , 'varchar'  , 100  , None , 'Conta'                                                            , None, None),
        ('abnf_financeiro_cadastro_contas'                                          , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_financeiro_cadastro_contas'                                          , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_financeiro_cadastro_contas'                                          , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_financeiro_cadastro_contas'                                          , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_financeiro_cadastro_contas'                                          , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_financeiro_cadastro_contas'                                          , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        ('abnf_financeiro_cadastro_contas'                                          , 'saldoin' , 'decimal'  , 30   , 2    , 'Saldo inicial'                                                    , None, None),
        ('abnf_financeiro_cadastro_contas'                                          , 'totalre' , 'decimal'  , 30   , 2    , 'Total de receitas'                                                , None, None),
        ('abnf_financeiro_cadastro_contas'                                          , 'totalde' , 'decimal'  , 30   , 2    , 'Total de despesas'                                                , None, None),
        ('abnf_financeiro_cadastro_contas'                                          , 'observa' , 'text'     , None , None , 'Observacao'                                                       , None, None),
        ('abnf_financeiro_cadastro_contas'                                          , 'ccontab' , 'int'      , None , None , 'Conta contabil'                                                   , None, None),
        # /// #
        ('abnf_financeiro_cadastro_grupos'                                          , 'idgrupo' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_financeiro_cadastro_grupos'                                          , 'codgrup' , 'int'      , None , None , 'Codigo do grupo'                                                  , None, None),
        ('abnf_financeiro_cadastro_grupos'                                          , 'descgru' , 'varchar'  , 100  , None , 'Descricao do grupo'                                               , None, None),
        ('abnf_financeiro_cadastro_grupos'                                          , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_financeiro_cadastro_grupos'                                          , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_financeiro_cadastro_grupos'                                          , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_financeiro_cadastro_grupos'                                          , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_financeiro_cadastro_grupos'                                          , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_financeiro_cadastro_grupos'                                          , 'tipogru' , 'varchar'  , 1    , None , 'Tipo de grupo'                                                    , None, None),
        # /// #
        ('abnf_financeiro_cadastro_subgrupos'                                       , 'idsubgr' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_financeiro_cadastro_subgrupos'                                       , 'codsubg' , 'int'      , None , None , 'Codigo do subgrupo'                                               , None, None),
        ('abnf_financeiro_cadastro_subgrupos'                                       , 'descsub' , 'varchar'  , 100  , None , 'Descricao do subgrupo'                                            , None, None),
        ('abnf_financeiro_cadastro_subgrupos'                                       , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_financeiro_cadastro_subgrupos'                                       , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_financeiro_cadastro_subgrupos'                                       , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_financeiro_cadastro_subgrupos'                                       , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_financeiro_cadastro_subgrupos'                                       , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_financeiro_cadastro_subgrupos'                                       , 'idgrupo' , 'int'      , None , None , 'ID do grupo financeiro'                                           , 'abnf_financeiro_cadastro_grupos', 'idgrupo'),
        # /// #
        ('abnf_financeiro_cadastro_complementos'                                    , 'idcompl' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_financeiro_cadastro_complementos'                                    , 'codcomp' , 'int'      , None , None , 'Codigo do complemento'                                            , None, None),
        ('abnf_financeiro_cadastro_complementos'                                    , 'desccom' , 'varchar'  , 100  , None , 'Descricao do complemento'                                         , None, None),
        ('abnf_financeiro_cadastro_complementos'                                    , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_financeiro_cadastro_complementos'                                    , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_financeiro_cadastro_complementos'                                    , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_financeiro_cadastro_complementos'                                    , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_financeiro_cadastro_complementos'                                    , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_financeiro_cadastro_complementos'                                    , 'ccontab' , 'int'      , None , None , 'Conta contabil'                                                   , None, None),
        # /// #
        ('abnf_financeiro_cadastro_centros_custo'                                   , 'idcecus' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_financeiro_cadastro_centros_custo'                                   , 'codcecu' , 'int'      , None , None , 'Codigo do centro de custo'                                        , None, None),
        ('abnf_financeiro_cadastro_centros_custo'                                   , 'desccec' , 'varchar'  , 100  , None , 'Descricao do centro de custo'                                     , None, None),
        ('abnf_financeiro_cadastro_centros_custo'                                   , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_financeiro_cadastro_centros_custo'                                   , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_financeiro_cadastro_centros_custo'                                   , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_financeiro_cadastro_centros_custo'                                   , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_financeiro_cadastro_centros_custo'                                   , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_financeiro_cadastro_departamentos'                                   , 'iddepto' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_financeiro_cadastro_departamentos'                                   , 'coddept' , 'int'      , None , None , 'Codigo do departamento'                                           , None, None),
        ('abnf_financeiro_cadastro_departamentos'                                   , 'descdep' , 'varchar'  , 100  , None , 'Descricao do departamento'                                        , None, None),
        ('abnf_financeiro_cadastro_departamentos'                                   , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_financeiro_cadastro_departamentos'                                   , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_financeiro_cadastro_departamentos'                                   , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_financeiro_cadastro_departamentos'                                   , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_financeiro_cadastro_departamentos'                                   , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_financeiro_cadastro_contratos'                                       , 'idcontr' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_financeiro_cadastro_contratos'                                       , 'codcont' , 'int'      , None , None , 'Codigo do contrato'                                               , None, None),
        ('abnf_financeiro_cadastro_contratos'                                       , 'desccon' , 'varchar'  , 100  , None , 'Descricao do contrato'                                            , None, None),
        ('abnf_financeiro_cadastro_contratos'                                       , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_financeiro_cadastro_contratos'                                       , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_financeiro_cadastro_contratos'                                       , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_financeiro_cadastro_contratos'                                       , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_financeiro_cadastro_contratos'                                       , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_financeiro_cadastro_contratos'                                       , 'idclfor' , 'int'      , None , None , 'ID do cliente/fornecedor'                                         , 'abnf_cadastro_clientes_fornecedores', 'idclfor'),
        ('abnf_financeiro_cadastro_contratos'                                       , 'tipocon' , 'varchar'  , 1    , None , 'Tipo de contrato'                                                 , None, None),
        ('abnf_financeiro_cadastro_contratos'                                       , 'dataini' , 'date'     , None , None , 'Data de inicio do contrato'                                       , None, None),
        ('abnf_financeiro_cadastro_contratos'                                       , 'datafim' , 'date'     , None , None , 'Data de termino do contrato'                                      , None, None),
        ('abnf_financeiro_cadastro_contratos'                                       , 'qtdparc' , 'int'      , None , None , 'Quantidade de parcelas'                                           , None, None),
        ('abnf_financeiro_cadastro_contratos'                                       , 'valtotc' , 'decimal'  , 10   , 2    , 'Valor total do contrato'                                          , None, None),
        ('abnf_financeiro_cadastro_contratos'                                       , 'observa' , 'text'     , 100  , None , 'Observacao'                                                       , None, None),
        # /// #
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'idregfi' , 'key'      , None , None , 'ID do lancamento financeiro'                                      , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'ctrlfin' , 'int'      , None , None , 'Controle do registro financeiro'                                  , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'ctrlpgt' , 'int'      , None , None , 'Controle de pagamento'                                            , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou/excluiu o registro'                     , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'idsubgr' , 'int'      , None , None , 'ID do subgrupo financeiro'                                        , 'abnf_financeiro_cadastro_subgrupos', 'idsubgr'),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'idclfor' , 'int'      , None , None , 'ID do cliente/fornecedor'                                         , 'abnf_cadastro_clientes_fornecedores', 'idclfor'),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'idcompl' , 'int'      , None , None , 'ID do complemento'                                                , 'abnf_financeiro_cadastro_complementos', 'idcompl'),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'idcecus' , 'int'      , None , None , 'ID do centro de custo'                                            , 'abnf_financeiro_cadastro_centros_custo', 'idcecus'),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'iddepto' , 'int'      , None , None , 'ID do departamento'                                               , 'abnf_financeiro_cadastro_departamentos', 'iddepto'),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'idcontr' , 'int'      , None , None , 'ID do contrato'                                                   , 'abnf_financeiro_cadastro_contratos', 'idcontr'),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'idconta' , 'int'      , None , None , 'ID da conta financeira'                                           , 'abnf_financeiro_cadastro_contas', 'idconta'),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'tiporeg' , 'varchar'  , 1    , None , 'Tipo de registro'                                                 , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'modoreg' , 'varchar'  , 1    , None , 'Modo do registro'                                                 , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'regiadi' , 'boolean'  , None , None , 'Registro de adiantamento'                                         , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'valptdc' , 'decimal'  , 10   , 2    , 'Valor previsto total do documento'                                , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'valppar' , 'decimal'  , 10   , 2    , 'Valor previsto da parcela'                                        , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'valrtdc' , 'decimal'  , 10   , 2    , 'Valor realizado total do documento'                               , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'valrpar' , 'decimal'  , 10   , 2    , 'Valor realizado da parcela'                                       , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'valjuro' , 'decimal'  , 10   , 2    , 'Valor do juros'                                                   , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'valcemo' , 'decimal'  , 10   , 2    , 'Valor de custas e emolumentos'                                    , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'valdesc' , 'decimal'  , 10   , 2    , 'Valor do desconto'                                                , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'valabat' , 'decimal'  , 10   , 2    , 'Valor do abatimento'                                              , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'valpago' , 'decimal'  , 10   , 2    , 'Valor real pago'                                                  , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'nrdocnf' , 'bigint'   , None , None , 'Numero do documento/nota fiscal'                                  , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'serienf' , 'varchar'  , 5    , None , 'serie da nota fiscal'                                             , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'idespdo' , 'int'      , None , None , 'especie do documento'                                             , 'abnf_cadastro_especies_documentos', 'idespdo'),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'totparc' , 'int'      , None , None , 'Total de parcelas'                                                , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'numparc' , 'int'      , None , None , 'Numero da parcela corrente'                                       , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'datadoc' , 'date'     , None , None , 'Data do documento'                                                , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'dataven' , 'date'     , None , None , 'Data do vencimento'                                               , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'datavor' , 'date'     , None , None , 'Data do vencimento original'                                      , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'datapgt' , 'date'     , None , None , 'Data do pagamento'                                                , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'observa' , 'text'     , 100  , None , 'Observacao'                                                       , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'cglob01' , 'int'      , None , None , 'Codigo 01 do registro financeiro do Globus'                       , None, None),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'cglob02' , 'int'      , None , None , 'Codigo 02 do registro financeiro do Globus'                       , None, None),
        # /// #
        ('abnf_elevar_cadastro_passageiros'                                         , 'idepass' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_elevar_cadastro_passageiros'                                         , 'codepas' , 'int'      , None , None , 'Codigo do passageiro do Elevar'                                   , None, None),
        ('abnf_elevar_cadastro_passageiros'                                         , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_elevar_cadastro_passageiros'                                         , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_elevar_cadastro_passageiros'                                         , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_elevar_cadastro_passageiros'                                         , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_elevar_cadastro_passageiros'                                         , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_elevar_cadastro_passageiros'                                         , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        ('abnf_elevar_cadastro_passageiros'                                         , 'idcpfpj' , 'int'      , None , None , 'ID do CPF/CNPJ'                                                   , 'abnf_cadastro_cpfcnpj', 'idcpfpj'),
        ('abnf_elevar_cadastro_passageiros'                                         , 'idcidct' , 'int'      , None , None , 'ID da categoria do CID'                                           , 'abnf_cadastro_cid_categorias', 'idcidct'),
        ('abnf_elevar_cadastro_passageiros'                                         , 'cadeira' , 'boolean'  , None , None , 'Cadeirante'                                                       , None, None),
        ('abnf_elevar_cadastro_passageiros'                                         , 'acompan' , 'boolean'  , None , None , 'Necessita de acompanhante'                                        , None, None),
        ('abnf_elevar_cadastro_passageiros'                                         , 'observa' , 'text'     , None , None , 'Observacao'                                                       , None, None),
        # /// #
        ('abnf_elevar_cadastro_locais'                                              , 'ideloca' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_elevar_cadastro_locais'                                              , 'codeloc' , 'int'      , None , None , 'Codigo do local do Elevar'                                        , None, None),
        ('abnf_elevar_cadastro_locais'                                              , 'deseloc' , 'varchar'  , 100  , None , 'Descricao do local do Elevar'                                     , None, None),
        ('abnf_elevar_cadastro_locais'                                              , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_elevar_cadastro_locais'                                              , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_elevar_cadastro_locais'                                              , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_elevar_cadastro_locais'                                              , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_elevar_cadastro_locais'                                              , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_elevar_cadastro_locais'                                              , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        ('abnf_elevar_cadastro_locais'                                              , 'idlogra' , 'int'      , None , None , 'ID do logradouro'                                                 , 'abnf_cadastro_logradouros', 'idlogra'),
        ('abnf_elevar_cadastro_locais'                                              , 'logrnum' , 'varchar'  , 20   , None , 'Logradouro - Numero'                                              , None, None),
        ('abnf_elevar_cadastro_locais'                                              , 'logrcom' , 'varchar'  , 100  , None , 'Logradouro - Complemento'                                         , None, None),
        ('abnf_elevar_cadastro_locais'                                              , 'logrcep' , 'varchar'  , 10   , None , 'Logradouro - CEP'                                                 , None, None),
        ('abnf_elevar_cadastro_locais'                                              , 'pontope' , 'boolean'  , None , None , 'Ponto operacional'                                                , None, None),
        ('abnf_elevar_cadastro_locais'                                              , 'chortra' , 'boolean'  , None , None , 'Conta horarios trabalhados'                                       , None, None),
        ('abnf_elevar_cadastro_locais'                                              , 'observa' , 'text'     , None , None , 'Observacao'                                                       , None, None),
        # /// #
        ('abnf_elevar_cadastro_finalidades'                                         , 'idefina' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_elevar_cadastro_finalidades'                                         , 'codefin' , 'int'      , None , None , 'Codigo da finalidade do Elevar'                                   , None, None),
        ('abnf_elevar_cadastro_finalidades'                                         , 'desefin' , 'varchar'  , 100  , None , 'Descricao da finalidade do Elevar'                                , None, None),
        ('abnf_elevar_cadastro_finalidades'                                         , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_elevar_cadastro_finalidades'                                         , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_elevar_cadastro_finalidades'                                         , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_elevar_cadastro_finalidades'                                         , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_elevar_cadastro_finalidades'                                         , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_elevar_cadastro_finalidades'                                         , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #
        ('abnf_elevar_cadastro_servicos'                                            , 'ideserv' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_elevar_cadastro_servicos'                                            , 'codeser' , 'int'      , None , None , 'Codigo do servico do Elevar'                                      , None, None),
        ('abnf_elevar_cadastro_servicos'                                            , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_elevar_cadastro_servicos'                                            , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_elevar_cadastro_servicos'                                            , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_elevar_cadastro_servicos'                                            , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_elevar_cadastro_servicos'                                            , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_elevar_cadastro_servicos'                                            , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        ('abnf_elevar_cadastro_servicos'                                            , 'idepass' , 'int'      , None , None , 'ID do passageiro do Elevar'                                       , 'abnf_elevar_cadastro_passageiros', 'idepass'),
        ('abnf_elevar_cadastro_servicos'                                            , 'idefina' , 'int'      , None , None , 'ID da finalidade do Elevar'                                       , 'abnf_elevar_cadastro_finalidades', 'idefina'),
        ('abnf_elevar_cadastro_servicos'                                            , 'datasol' , 'date'     , None , None , 'Data da solicitacao'                                              , None, None),
        ('abnf_elevar_cadastro_servicos'                                            , 'dataini' , 'date'     , None , None , 'Data de inicio'                                                   , None, None),
        ('abnf_elevar_cadastro_servicos'                                            , 'datafim' , 'date'     , None , None , 'Data de termino'                                                  , None, None),
        ('abnf_elevar_cadastro_servicos'                                            , 'observa' , 'text'     , None , None , 'Observacao'                                                       , None, None),
        # /// #
        ('abnf_elevar_cadastro_frota_patrimonial'                                   , 'idefrpa' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_elevar_cadastro_frota_patrimonial'                                   , 'dataini' , 'date'     , None , None , 'Data de inicio do periodo'                                        , None, None),
        ('abnf_elevar_cadastro_frota_patrimonial'                                   , 'qtdfrpa' , 'int'      , None , None , 'Quantidade de frota patrimonial no periodo'                       , None, None),
        ('abnf_elevar_cadastro_frota_patrimonial'                                   , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_elevar_cadastro_frota_patrimonial'                                   , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_elevar_cadastro_frota_patrimonial'                                   , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_elevar_cadastro_frota_patrimonial'                                   , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_elevar_cadastro_frota_patrimonial'                                   , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_elevar_cadastro_frota_patrimonial'                                   , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #
        ('abnf_elevar_cadastro_ordens_servico_padrao_grupos'                        , 'idegopa' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_elevar_cadastro_ordens_servico_padrao_grupos'                        , 'codegop' , 'int'      , None , None , 'Codigo do grupo de ordens de servico padrao do Elevar'            , None, None),
        ('abnf_elevar_cadastro_ordens_servico_padrao_grupos'                        , 'desegru' , 'varchar'  , 100  , None , 'Descricao do grupo de ordens de servico padrao do Elevar'         , None, None),
        ('abnf_elevar_cadastro_ordens_servico_padrao_grupos'                        , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_elevar_cadastro_ordens_servico_padrao_grupos'                        , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_elevar_cadastro_ordens_servico_padrao_grupos'                        , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_elevar_cadastro_ordens_servico_padrao_grupos'                        , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_elevar_cadastro_ordens_servico_padrao_grupos'                        , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_elevar_cadastro_ordens_servico_padrao_grupos'                        , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #
        ('abnf_elevar_cadastro_ordens_servico_padrao'                               , 'ideospa' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_elevar_cadastro_ordens_servico_padrao'                               , 'codeosp' , 'int'      , None , None , 'Codigo da ordem de servico padrao do Elevar'                      , None, None),
        ('abnf_elevar_cadastro_ordens_servico_padrao'                               , 'desemos' , 'varchar'  , 100  , None , 'Descricao da ordem de servico padrao do Elevar'                   , None, None),
        ('abnf_elevar_cadastro_ordens_servico_padrao'                               , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_elevar_cadastro_ordens_servico_padrao'                               , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_elevar_cadastro_ordens_servico_padrao'                               , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_elevar_cadastro_ordens_servico_padrao'                               , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_elevar_cadastro_ordens_servico_padrao'                               , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_elevar_cadastro_ordens_servico_padrao'                               , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        ('abnf_elevar_cadastro_ordens_servico_padrao'                               , 'idegopa' , 'int'      , None , None , 'ID do grupo de ordens de servico padrao'                          , 'abnf_elevar_cadastro_ordens_servico_padrao_grupos', 'idegopa'),
        ('abnf_elevar_cadastro_ordens_servico_padrao'                               , 'idveicu' , 'int'      , None , None , 'ID do veiculo'                                                    , 'abnf_cadastro_veiculos', 'idveicu'),
        # /// #
        ('abnf_elevar_cadastro_ordens_servico_padrao_itens'                         , 'ideitop' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_elevar_cadastro_ordens_servico_padrao_itens'                         , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_elevar_cadastro_ordens_servico_padrao_itens'                         , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_elevar_cadastro_ordens_servico_padrao_itens'                         , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_elevar_cadastro_ordens_servico_padrao_itens'                         , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_elevar_cadastro_ordens_servico_padrao_itens'                         , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_elevar_cadastro_ordens_servico_padrao_itens'                         , 'ideospa' , 'int'      , None , None , 'ID da ordem de servico padrao'                                    , 'abnf_elevar_cadastro_ordens_servico_padrao', 'ideospa'),
        ('abnf_elevar_cadastro_ordens_servico_padrao_itens'                         , 'idfunci' , 'int'      , None , None , 'ID do motorista'                                                  , 'abnf_cadastro_funcionarios', 'idfunci'),
        ('abnf_elevar_cadastro_ordens_servico_padrao_itens'                         , 'ideloca' , 'int'      , None , None , 'ID do local do Elevar'                                            , 'abnf_elevar_cadastro_locais', 'ideloca'),
        ('abnf_elevar_cadastro_ordens_servico_padrao_itens'                         , 'horario' , 'time'     , None , None , 'Horario'                                                          , None, None),
        ('abnf_elevar_cadastro_ordens_servico_padrao_itens'                         , 'ideserv' , 'int'      , None , None , 'ID do cadastro de servico do Elevar'                              , 'abnf_elevar_cadastro_servicos', 'ideserv'),
        ('abnf_elevar_cadastro_ordens_servico_padrao_itens'                         , 'motivox' , 'varchar'  , 1    , None , 'Motivo'                                                           , None, None),
        ('abnf_elevar_cadastro_ordens_servico_padrao_itens'                         , 'pontope' , 'boolean'  , None , None , 'Ponto operacional'                                                , None, None),
        ('abnf_elevar_cadastro_ordens_servico_padrao_itens'                         , 'viagimp' , 'boolean'  , None , None , 'Viagem improdutiva'                                               , None, None),
        ('abnf_elevar_cadastro_ordens_servico_padrao_itens'                         , 'horamot' , 'boolean'  , None , None , 'Computa hora do motorista'                                        , None, None),
        # /// #
        ('abnf_elevar_movimentacao_ordens_servico_diaria'                           , 'ideosdi' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria'                           , 'numeosd' , 'int'      , None , None , 'Numero da ordem de servico diaria do Elevar'                      , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria'                           , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria'                           , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_elevar_movimentacao_ordens_servico_diaria'                           , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_elevar_movimentacao_ordens_servico_diaria'                           , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria'                           , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria'                           , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        ('abnf_elevar_movimentacao_ordens_servico_diaria'                           , 'dataord' , 'date'     , None , None , 'Data da ordem de servico'                                         , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria'                           , 'tiporeg' , 'varchar'  , 1    , None , 'Tipo de registro'                                                 , None, None),
        # /// #
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'ideitod' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'tiporeg' , 'varchar'  , 1    , None , 'Tipo de registro: [S]istema/[M]anual'                             , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'ideosdi' , 'int'      , None , None , 'ID da ordem de servico diaria'                                    , 'abnf_elevar_movimentacao_ordens_servico_diaria', 'ideosdi'),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'idveicu' , 'int'      , None , None , 'ID do veiculo'                                                    , 'abnf_cadastro_veiculos', 'idveicu'),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'idfunci' , 'int'      , None , None , 'ID do motorista'                                                  , 'abnf_cadastro_funcionarios', 'idfunci'),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'ideloca' , 'int'      , None , None , 'ID do local do Elevar'                                            , 'abnf_elevar_cadastro_locais', 'ideloca'),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'idlogra' , 'int'      , None , None , 'ID do logradouro'                                                 , 'abnf_cadastro_logradouros', 'idlogra'),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'logrnum' , 'varchar'  , 20   , None , 'Logradouro - Numero'                                              , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'logrcom' , 'varchar'  , 100  , None , 'Logradouro - Complemento'                                         , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'logrcep' , 'varchar'  , 10   , None , 'Logradouro - CEP'                                                 , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'horario' , 'time'     , None , None , 'Horario'                                                          , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'horamin' , 'int'      , None , None , 'Horario (em minutos)'                                             , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'ideserv' , 'int'      , None , None , 'ID do cadastro de servico do Elevar'                              , 'abnf_elevar_cadastro_servicos', 'ideserv'),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'motivox' , 'varchar'  , 1    , None , 'Motivo'                                                           , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'pontope' , 'boolean'  , None , None , 'Ponto operacional'                                                , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'viagimp' , 'boolean'  , None , None , 'Viagem improdutiva'                                               , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'horamot' , 'boolean'  , None , None , 'Computa hora do motorista'                                        , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'observa' , 'text'     , None , None , 'Observacao'                                                       , None, None),
        # /// #
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'ideitod' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'tiporeg' , 'varchar'  , 1    , None , 'Tipo de registro'                                                 , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'ideosdi' , 'int'      , None , None , 'ID da ordem de servico diaria'                                    , 'abnf_elevar_movimentacao_ordens_servico_diaria', 'ideosdi'),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'idveicu' , 'int'      , None , None , 'ID do veiculo'                                                    , 'abnf_cadastro_veiculos', 'idveicu'),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'idfunci' , 'int'      , None , None , 'ID do motorista'                                                  , 'abnf_cadastro_funcionarios', 'idfunci'),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'ideloca' , 'int'      , None , None , 'ID do local do Elevar'                                            , 'abnf_elevar_cadastro_locais', 'ideloca'),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'idlogra' , 'int'      , None , None , 'ID do logradouro'                                                 , 'abnf_cadastro_logradouros', 'idlogra'),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'logrnum' , 'varchar'  , 20   , None , 'Logradouro - Numero'                                              , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'logrcom' , 'varchar'  , 100  , None , 'Logradouro - Complemento'                                         , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'logrcep' , 'varchar'  , 10   , None , 'Logradouro - CEP'                                                 , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'horario' , 'time'     , None , None , 'Horario'                                                          , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'horamin' , 'int'      , None , None , 'Horario (em minutos)'                                             , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'ideserv' , 'int'      , None , None , 'ID do cadastro de servico do Elevar'                              , 'abnf_elevar_cadastro_servicos', 'ideserv'),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'motivox' , 'varchar'  , 1    , None , 'Motivo'                                                           , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'pontope' , 'boolean'  , None , None , 'Ponto operacional'                                                , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'viagimp' , 'boolean'  , None , None , 'Viagem improdutiva'                                               , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'horamot' , 'boolean'  , None , None , 'Computa hora do motorista'                                        , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'observa' , 'text'     , None , None , 'Observacao'                                                       , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'horcheg' , 'time'     , None , None , 'Horario de chegada'                                               , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'horcmin' , 'int'      , None , None , 'Horario de chegada (em minutos)'                                  , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'horsaid' , 'time'     , None , None , 'Horario de saida'                                                 , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'horsmin' , 'int'      , None , None , 'Horario de saida (em minutos)'                                    , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'idkmvei' , 'int'      , None , None , 'Km anotado pelo motorista'                                        , None, None),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'statreg' , 'int'      , None , None , 'Status do registro'                                               , None, None),
        # /// #
        ('abnf_sac_cadastro_usuarios_grupos'                                        , 'idsusgr' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sac_cadastro_usuarios_grupos'                                        , 'codsusg' , 'int'      , None , None , 'Codigo do grupo de usuarios do SAC'                               , None, None),
        ('abnf_sac_cadastro_usuarios_grupos'                                        , 'dessusg' , 'varchar'  , 100  , None , 'Descricao do grupo de usuarios do SAC'                            , None, None),
        ('abnf_sac_cadastro_usuarios_grupos'                                        , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sac_cadastro_usuarios_grupos'                                        , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sac_cadastro_usuarios_grupos'                                        , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sac_cadastro_usuarios_grupos'                                        , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sac_cadastro_usuarios_grupos'                                        , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_sac_cadastro_usuarios_grupos'                                        , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        ('abnf_sac_cadastro_usuarios_grupos'                                        , 'emailgr' , 'varchar'  , 100  , None , 'E-mail do grupo'                                                  , None, None),
        ('abnf_sac_cadastro_usuarios_grupos'                                        , 'envpref' , 'varchar'  , 1    , None , 'Envia dados para prefeitura'                                      , None, None),
        # /// #
        ('abnf_sac_cadastro_usuarios_grupos_vinculos'                               , 'idsugvi' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sac_cadastro_usuarios_grupos_vinculos'                               , 'idsusgr' , 'int'      , None , None , 'ID do grupo de usuarios do SAC'                                   , 'abnf_sac_cadastro_usuarios_grupos', 'idsusgr'),
        ('abnf_sac_cadastro_usuarios_grupos_vinculos'                               , 'idusuar' , 'int'      , None , None , 'ID do usuario'                                                    , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sac_cadastro_usuarios_grupos_vinculos'                               , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sac_cadastro_usuarios_grupos_vinculos'                               , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sac_cadastro_usuarios_grupos_vinculos'                               , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sac_cadastro_usuarios_grupos_vinculos'                               , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sac_cadastro_usuarios_grupos_vinculos'                               , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_sac_cadastro_atendimentos_canais'                                    , 'idsatca' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sac_cadastro_atendimentos_canais'                                    , 'codsatc' , 'int'      , None , None , 'Codigo do canal de atendimento do SAC'                            , None, None),
        ('abnf_sac_cadastro_atendimentos_canais'                                    , 'dessatc' , 'varchar'  , 100  , None , 'Descricao do canal de atendimento do SAC'                         , None, None),
        ('abnf_sac_cadastro_atendimentos_canais'                                    , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sac_cadastro_atendimentos_canais'                                    , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sac_cadastro_atendimentos_canais'                                    , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sac_cadastro_atendimentos_canais'                                    , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sac_cadastro_atendimentos_canais'                                    , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_sac_cadastro_atendimentos_canais'                                    , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #
        ('abnf_sac_cadastro_atendimentos_tipos'                                     , 'idsatti' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sac_cadastro_atendimentos_tipos'                                     , 'codsatt' , 'int'      , None , None , 'Codigo do tipo de atendimento do SAC'                             , None, None),
        ('abnf_sac_cadastro_atendimentos_tipos'                                     , 'dessatt' , 'varchar'  , 100  , None , 'Descricao do tipo de atendimento do SAC'                          , None, None),
        ('abnf_sac_cadastro_atendimentos_tipos'                                     , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sac_cadastro_atendimentos_tipos'                                     , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sac_cadastro_atendimentos_tipos'                                     , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sac_cadastro_atendimentos_tipos'                                     , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sac_cadastro_atendimentos_tipos'                                     , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_sac_cadastro_atendimentos_tipos'                                     , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #
        ('abnf_sac_cadastro_atendimentos_grupos'                                    , 'idsatgr' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sac_cadastro_atendimentos_grupos'                                    , 'codsatg' , 'int'      , None , None , 'Codigo do grupo de atendimento do SAC'                            , None, None),
        ('abnf_sac_cadastro_atendimentos_grupos'                                    , 'dessatg' , 'varchar'  , 100  , None , 'Descricao do grupo de atendimento do SAC'                         , None, None),
        ('abnf_sac_cadastro_atendimentos_grupos'                                    , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sac_cadastro_atendimentos_grupos'                                    , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sac_cadastro_atendimentos_grupos'                                    , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sac_cadastro_atendimentos_grupos'                                    , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sac_cadastro_atendimentos_grupos'                                    , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_sac_cadastro_atendimentos_grupos'                                    , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #
        ('abnf_sac_cadastro_atendimentos_subgrupos'                                 , 'idsatsg' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sac_cadastro_atendimentos_subgrupos'                                 , 'codsats' , 'int'      , None , None , 'Codigo do subgrupo de atendimento do SAC'                         , None, None),
        ('abnf_sac_cadastro_atendimentos_subgrupos'                                 , 'dessats' , 'varchar'  , 100  , None , 'Descricao do subgrupo de atendimento do SAC'                      , None, None),
        ('abnf_sac_cadastro_atendimentos_subgrupos'                                 , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sac_cadastro_atendimentos_subgrupos'                                 , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sac_cadastro_atendimentos_subgrupos'                                 , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sac_cadastro_atendimentos_subgrupos'                                 , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sac_cadastro_atendimentos_subgrupos'                                 , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_sac_cadastro_atendimentos_subgrupos'                                 , 'idsatgr' , 'int'      , None , None , 'ID do grupo de atendimento do SAC'                                , 'abnf_sac_cadastro_atendimentos_grupos', 'idsatgr'),
        ('abnf_sac_cadastro_atendimentos_subgrupos'                                 , 'envpref' , 'varchar'  , 1    , None , 'Envia dados para prefeitura'                                      , None, None),
        # /// #
        ('abnf_sac_movimentacao_atendimentos'                                       , 'idsaten' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'codsate' , 'int'      , None , None , 'Codigo do atendimento do SAC'                                     , None, None),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'situate' , 'varchar'  , 1    , None , 'Situacao do atendimento'                                          , None, None),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'dataabe' , 'date'     , None , None , 'Data de abertura'                                                 , None, None),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'horaabe' , 'time'     , None , None , 'Horario de abertura'                                              , None, None),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'datafec' , 'date'     , None , None , 'Data de fechamento'                                               , None, None),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'horafec' , 'time'     , None , None , 'Horario de fechamento'                                            , None, None),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'dataoco' , 'date'     , None , None , 'Data da ocorrencia'                                               , None, None),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'horaoco' , 'time'     , None , None , 'Horario da ocorrencia'                                            , None, None),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'idsatca' , 'int'      , None , None , 'ID do canal de atendimento do SAC'                                , 'abnf_sac_cadastro_atendimentos_canais', 'idsatca'),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'idsatti' , 'int'      , None , None , 'ID do tipo de atendimento do SAC'                                 , 'abnf_sac_cadastro_atendimentos_tipos', 'idsatti'),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'idsatsg' , 'int'      , None , None , 'ID do subgrupo de atendimento do SAC'                             , 'abnf_sac_cadastro_atendimentos_subgrupos', 'idsatsg'),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'idfunci' , 'int'      , None , None , 'ID do funcionario envolvido'                                      , 'abnf_cadastro_funcionarios', 'idfunci'),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'idveicu' , 'int'      , None , None , 'ID do veiculo envolvido'                                          , 'abnf_cadastro_veiculos', 'idveicu'),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'idolinh' , 'int'      , None , None , 'ID da linha da operacao envolvida'                                , 'abnf_operacional_cadastro_linhas', 'idolinh'),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'descroc' , 'text'     , None , None , 'Descricao da ocorrencia'                                          , None, None),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'idcpfcl' , 'int'      , None , None , 'ID do cliente (cadastrado)'                                       , 'abnf_cadastro_cpfcnpj', 'idcpfpj'),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'nomecli' , 'varchar'  , 100  , None , 'Nome do cliente (nao cadastrado)'                                 , None, None),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'contato' , 'varchar'  , 100  , None , 'Contato do cliente (nao cadastrado)'                              , None, None),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'idsusab' , 'int'      , None , None , 'ID do grupo de usuarios do SAC que abriu o atendimento'           , 'abnf_sac_cadastro_usuarios_grupos', 'idsusgr'),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'idsusde' , 'int'      , None , None , 'ID do grupo de usuarios do SAC que foi destinado o atendimento'   , 'abnf_sac_cadastro_usuarios_grupos', 'idsusgr'),
        # /// #
        ('abnf_sac_movimentacao_atendimentos_complementos'                          , 'idsatco' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sac_movimentacao_atendimentos_complementos'                          , 'idsaten' , 'int'      , None , None , 'ID do atendimento do SAC'                                         , 'abnf_sac_movimentacao_atendimentos', 'idsaten'),
        ('abnf_sac_movimentacao_atendimentos_complementos'                          , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sac_movimentacao_atendimentos_complementos'                          , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sac_movimentacao_atendimentos_complementos'                          , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sac_movimentacao_atendimentos_complementos'                          , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sac_movimentacao_atendimentos_complementos'                          , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_sac_movimentacao_atendimentos_complementos'                          , 'datacom' , 'date'     , None , None , 'Data do complemento'                                              , None, None),
        ('abnf_sac_movimentacao_atendimentos_complementos'                          , 'horacom' , 'time'     , None , None , 'Horario do complemento'                                           , None, None),
        ('abnf_sac_movimentacao_atendimentos_complementos'                          , 'descrco' , 'text'     , None , None , 'Descricao do complemento'                                         , None, None),
        ('abnf_sac_movimentacao_atendimentos_complementos'                          , 'idsusab' , 'int'      , None , None , 'ID do grupo de usuarios do SAC que abriu o complemento'           , 'abnf_sac_cadastro_usuarios_grupos', 'idsusgr'),
        ('abnf_sac_movimentacao_atendimentos_complementos'                          , 'idsusde' , 'int'      , None , None , 'ID do grupo de usuarios do SAC que foi destinado o complemento'   , 'abnf_sac_cadastro_usuarios_grupos', 'idsusgr'),
        # /// #
        ('abnf_sac_movimentacao_atendimentos_arquivos'                              , 'idsatar' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sac_movimentacao_atendimentos_arquivos'                              , 'idsaten' , 'int'      , None , None , 'ID do atendimento do SAC'                                         , 'abnf_sac_movimentacao_atendimentos', 'idsaten'),
        ('abnf_sac_movimentacao_atendimentos_arquivos'                              , 'idsatco' , 'int'      , None , None , 'ID do complemento de atendimento do SAC'                          , 'abnf_sac_movimentacao_atendimentos_complementos', 'idsatco'),
        ('abnf_sac_movimentacao_atendimentos_arquivos'                              , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sac_movimentacao_atendimentos_arquivos'                              , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sac_movimentacao_atendimentos_arquivos'                              , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sac_movimentacao_atendimentos_arquivos'                              , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sac_movimentacao_atendimentos_arquivos'                              , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_sac_movimentacao_atendimentos_arquivos'                              , 'idarqui' , 'int'      , None , None , 'ID do arquivo'                                                    , 'abnf_sistema_arquivos', 'idarqui'),
        # /// #
        ('abnf_operacional_cadastro_locais'                                         , 'idoloca' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_cadastro_locais'                                         , 'codoloc' , 'int'      , None , None , 'Codigo do local'                                                  , None, None),
        ('abnf_operacional_cadastro_locais'                                         , 'desoloc' , 'varchar'  , 100  , None , 'Descricao do local'                                               , None, None),
        ('abnf_operacional_cadastro_locais'                                         , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_cadastro_locais'                                         , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_locais'                                         , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_locais'                                         , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_cadastro_locais'                                         , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_cadastro_locais'                                         , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        ('abnf_operacional_cadastro_locais'                                         , 'idlogra' , 'int'      , None , None , 'ID do logradouro'                                                 , 'abnf_cadastro_logradouros', 'idlogra'),
        ('abnf_operacional_cadastro_locais'                                         , 'logrnum' , 'varchar'  , 20   , None , 'Logradouro - Numero'                                              , None, None),
        ('abnf_operacional_cadastro_locais'                                         , 'logrcom' , 'varchar'  , 100  , None , 'Logradouro - Complemento'                                         , None, None),
        ('abnf_operacional_cadastro_locais'                                         , 'logrcep' , 'varchar'  , 10   , None , 'Logradouro - CEP'                                                 , None, None),
        ('abnf_operacional_cadastro_locais'                                         , 'observa' , 'text'     , None , None , 'Observacao'                                                       , None, None),
        ('abnf_operacional_cadastro_locais'                                         , 'saidgar' , 'boolean'  , None , None , 'Saida da garagem'                                                 , None, None),
        # /// #
        ('abnf_operacional_cadastro_grupos_linhas'                                  , 'idogrli' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_cadastro_grupos_linhas'                                  , 'codogrl' , 'int'      , None , None , 'Codigo do grupo de linha'                                         , None, None),
        ('abnf_operacional_cadastro_grupos_linhas'                                  , 'desogrl' , 'varchar'  , 100  , None , 'Descricao do grupo de linha'                                      , None, None),
        ('abnf_operacional_cadastro_grupos_linhas'                                  , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_cadastro_grupos_linhas'                                  , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_grupos_linhas'                                  , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_grupos_linhas'                                  , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_cadastro_grupos_linhas'                                  , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_cadastro_grupos_linhas'                                  , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #
        ('abnf_operacional_cadastro_linhas'                                         , 'idolinh' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_cadastro_linhas'                                         , 'codolin' , 'varchar'  , 20   , None , 'Codigo da linha'                                                  , None, None),
        ('abnf_operacional_cadastro_linhas'                                         , 'desolin' , 'varchar'  , 100  , None , 'Descricao da linha'                                               , None, None),
        ('abnf_operacional_cadastro_linhas'                                         , 'idogrli' , 'int'      , None , None , 'ID do grupo da linha'                                             , 'abnf_operacional_cadastro_grupos_linhas', 'idogrli'),
        ('abnf_operacional_cadastro_linhas'                                         , 'qtporve' , 'int'      , None , None , 'Quantidade padrao de portas dos veiculos da linha'                , None, None),
        ('abnf_operacional_cadastro_linhas'                                         , 'perqtpd' , 'boolean'  , None , None , 'Permite veiculos com quantidade de portas divergente do padrao'   , None, None),
        ('abnf_operacional_cadastro_linhas'                                         , 'perveca' , 'boolean'  , None , None , 'Permite veiculos com ar-condicionado'                             , None, None),
        ('abnf_operacional_cadastro_linhas'                                         , 'pervesa' , 'boolean'  , None , None , 'Permite veiculos sem ar-condicionado'                             , None, None),
        ('abnf_operacional_cadastro_linhas'                                         , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_cadastro_linhas'                                         , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_linhas'                                         , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_linhas'                                         , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_cadastro_linhas'                                         , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_cadastro_linhas'                                         , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #
        ('abnf_operacional_cadastro_projetos'                                       , 'idoproj' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_cadastro_projetos'                                       , 'codopro' , 'int'      , None , None , 'Codigo do projeto'                                                , None, None),
        ('abnf_operacional_cadastro_projetos'                                       , 'desopro' , 'varchar'  , 100  , None , 'Descricao do projeto'                                             , None, None),
        ('abnf_operacional_cadastro_projetos'                                       , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_cadastro_projetos'                                       , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_projetos'                                       , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_projetos'                                       , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_cadastro_projetos'                                       , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_cadastro_projetos'                                       , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #
        ('abnf_operacional_cadastro_trajetos'                                       , 'idotraj' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_cadastro_trajetos'                                       , 'idoproj' , 'int'      , None , None , 'ID do projeto'                                                    , 'abnf_operacional_cadastro_projetos', 'idoproj'),
        ('abnf_operacional_cadastro_trajetos'                                       , 'idolinh' , 'int'      , None , None , 'ID da linha'                                                      , 'abnf_operacional_cadastro_linhas', 'idolinh'),
        ('abnf_operacional_cadastro_trajetos'                                       , 'codotra' , 'varchar'  , 4    , None , 'Codigo do trajeto'                                                , None, None),
        ('abnf_operacional_cadastro_trajetos'                                       , 'desotra' , 'varchar'  , 200  , None , 'Descricao do trajeto'                                             , None, None),
        ('abnf_operacional_cadastro_trajetos'                                       , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_cadastro_trajetos'                                       , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_trajetos'                                       , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_trajetos'                                       , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_cadastro_trajetos'                                       , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_cadastro_trajetos'                                       , 'kmidaxx' , 'decimal'  , 8    , 1    , 'km ida'                                                           , None, None),
        ('abnf_operacional_cadastro_trajetos'                                       , 'kmvolta' , 'decimal'  , 8    , 1    , 'km volta'                                                         , None, None),
        # /// #
        ('abnf_operacional_cadastro_itinerarios'                                    , 'idoitin' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_cadastro_itinerarios'                                    , 'idotraj' , 'int'      , None , None , 'ID do trajeto'                                                    , 'abnf_operacional_cadastro_trajetos', 'idotraj'),
        ('abnf_operacional_cadastro_itinerarios'                                    , 'sentido' , 'varchar'  , 1    , None , 'Sentido'                                                          , None, None),
        ('abnf_operacional_cadastro_itinerarios'                                    , 'ordemit' , 'int'      , None , None , 'Ordem no itinerario'                                              , None, None),
        ('abnf_operacional_cadastro_itinerarios'                                    , 'idlogra' , 'int'      , None , None , 'ID do logradouro'                                                 , 'abnf_cadastro_logradouros', 'idlogra'),
        ('abnf_operacional_cadastro_itinerarios'                                    , 'complem' , 'varchar'  , 100  , None , 'Complemento'                                                      , None, None),
        ('abnf_operacional_cadastro_itinerarios'                                    , 'destaqu' , 'boolean'  , None , None , 'Destaque'                                                         , None, None),
        ('abnf_operacional_cadastro_itinerarios'                                    , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_cadastro_itinerarios'                                    , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_itinerarios'                                    , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_itinerarios'                                    , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_cadastro_itinerarios'                                    , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_operacional_cadastro_grupos_veiculos'                                , 'idogrve' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_cadastro_grupos_veiculos'                                , 'codogrf' , 'int'      , None , None , 'Codigo do grupo de veiculo'                                       , None, None),
        ('abnf_operacional_cadastro_grupos_veiculos'                                , 'descgrf' , 'varchar'  , 200  , None , 'Descricao do grupo de veiculo'                                    , None, None),
        ('abnf_operacional_cadastro_grupos_veiculos'                                , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_cadastro_grupos_veiculos'                                , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_grupos_veiculos'                                , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_grupos_veiculos'                                , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_cadastro_grupos_veiculos'                                , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_cadastro_grupos_veiculos'                                , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #
        ('abnf_operacional_cadastro_grupos_veiculos_vinculos'                       , 'idogrvv' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_cadastro_grupos_veiculos_vinculos'                       , 'idogrve' , 'int'      , None , None , 'ID do grupo de veiculo'                                           , 'abnf_operacional_cadastro_grupos_veiculos', 'idogrve'),
        ('abnf_operacional_cadastro_grupos_veiculos_vinculos'                       , 'idveicu' , 'int'      , None , None , 'ID do veiculo'                                                    , 'abnf_cadastro_veiculos', 'idveicu'),
        ('abnf_operacional_cadastro_grupos_veiculos_vinculos'                       , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_cadastro_grupos_veiculos_vinculos'                       , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_grupos_veiculos_vinculos'                       , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_grupos_veiculos_vinculos'                       , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_cadastro_grupos_veiculos_vinculos'                       , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_operacional_cadastro_prioridades_linhas'                             , 'idoplin' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_cadastro_prioridades_linhas'                             , 'ordprio' , 'int'      , None , None , 'Ordem de prioridade'                                              , None, None),
        ('abnf_operacional_cadastro_prioridades_linhas'                             , 'idolinh' , 'int'      , None , None , 'ID da linha'                                                      , 'abnf_operacional_cadastro_linhas', 'idolinh'),
        ('abnf_operacional_cadastro_prioridades_linhas'                             , 'veicser' , 'int'      , None , None , 'Veiculo/servico'                                                  , None, None),
        ('abnf_operacional_cadastro_prioridades_linhas'                             , 'idveicu' , 'int'      , None , None , 'ID do veiculo oficial'                                            , 'abnf_cadastro_veiculos', 'idveicu'),
        ('abnf_operacional_cadastro_prioridades_linhas'                             , 'tpdiaut' , 'boolean'  , None , None , 'Tipo de dia: util'                                                , None, None),
        ('abnf_operacional_cadastro_prioridades_linhas'                             , 'tpdiasa' , 'boolean'  , None , None , 'Tipo de dia: sabado'                                              , None, None),
        ('abnf_operacional_cadastro_prioridades_linhas'                             , 'tpdiado' , 'boolean'  , None , None , 'Tipo de dia: domingo'                                             , None, None),
        ('abnf_operacional_cadastro_prioridades_linhas'                             , 'tpdiafe' , 'boolean'  , None , None , 'Tipo de dia: feriado'                                             , None, None),
        ('abnf_operacional_cadastro_prioridades_linhas'                             , 'tpdia2a' , 'boolean'  , None , None , 'Tipo de dia: segunda-feira'                                       , None, None),
        ('abnf_operacional_cadastro_prioridades_linhas'                             , 'tpdia3a' , 'boolean'  , None , None , 'Tipo de dia: terca-feira'                                         , None, None),
        ('abnf_operacional_cadastro_prioridades_linhas'                             , 'tpdia4a' , 'boolean'  , None , None , 'Tipo de dia: quarta-feira'                                        , None, None),
        ('abnf_operacional_cadastro_prioridades_linhas'                             , 'tpdia5a' , 'boolean'  , None , None , 'Tipo de dia: quinta-feira'                                        , None, None),
        ('abnf_operacional_cadastro_prioridades_linhas'                             , 'tpdia6a' , 'boolean'  , None , None , 'Tipo de dia: sexta-feira'                                         , None, None),
        ('abnf_operacional_cadastro_prioridades_linhas'                             , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_cadastro_prioridades_linhas'                             , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_prioridades_linhas'                             , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_prioridades_linhas'                             , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_cadastro_prioridades_linhas'                             , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_cadastro_prioridades_linhas'                             , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #
        ('abnf_operacional_cadastro_prioridades_linhas_gv'                          , 'idoplgv' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_cadastro_prioridades_linhas_gv'                          , 'idoplin' , 'int'      , None , None , 'Prioridade de linha'                                              , 'abnf_operacional_cadastro_prioridades_linhas', 'idoplin'),
        ('abnf_operacional_cadastro_prioridades_linhas_gv'                          , 'ordprio' , 'int'      , None , None , 'Ordem de prioridade'                                              , None, None),
        ('abnf_operacional_cadastro_prioridades_linhas_gv'                          , 'idogrve' , 'int'      , None , None , 'ID do grupo de veiculo'                                           , 'abnf_operacional_cadastro_grupos_veiculos', 'idogrve'),
        ('abnf_operacional_cadastro_prioridades_linhas_gv'                          , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_cadastro_prioridades_linhas_gv'                          , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_prioridades_linhas_gv'                          , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_prioridades_linhas_gv'                          , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_cadastro_prioridades_linhas_gv'                          , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #        
        ('abnf_operacional_cadastro_operacoes_especiais'                            , 'idooesp' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_cadastro_operacoes_especiais'                            , 'dataope' , 'date'     , None , None , 'Data da operacao'                                                 , None, None),
        ('abnf_operacional_cadastro_operacoes_especiais'                            , 'idolinh' , 'int'      , None , None , 'Veiculo/servico'                                                  , 'abnf_operacional_cadastro_linhas', 'idolinh'),
        ('abnf_operacional_cadastro_operacoes_especiais'                            , 'veicser' , 'int'      , None , None , 'ID do veiculo oficial'                                            , None, None),
        ('abnf_operacional_cadastro_operacoes_especiais'                            , 'tipodia' , 'varchar'  , 1    , None , 'Tipo de dia'                                                      , None, None),
        ('abnf_operacional_cadastro_operacoes_especiais'                            , 'descmot' , 'varchar'  , 100  , None , 'Descricao do motivo'                                              , None, None),
        ('abnf_operacional_cadastro_operacoes_especiais'                            , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_cadastro_operacoes_especiais'                            , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_operacoes_especiais'                            , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_operacoes_especiais'                            , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_cadastro_operacoes_especiais'                            , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_cadastro_operacoes_especiais'                            , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #
        ('abnf_operacional_cadastro_setor_veiculos'                                 , 'idosetv' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_cadastro_setor_veiculos'                                 , 'codoset' , 'int'      , None , None , 'Codigo do setor de veiculos'                                      , None, None),
        ('abnf_operacional_cadastro_setor_veiculos'                                 , 'descset' , 'varchar'  , 100  , None , 'Descricao do setor de veiculos'                                   , None, None),
        ('abnf_operacional_cadastro_setor_veiculos'                                 , 'qtdveic' , 'int'      , None , None , 'Quantidade de veiculos'                                           , None, None),
        ('abnf_operacional_cadastro_setor_veiculos'                                 , 'ordprio' , 'int'      , None , None , 'Ordem de prioridade'                                              , None, None),
        ('abnf_operacional_cadastro_setor_veiculos'                                 , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_cadastro_setor_veiculos'                                 , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_setor_veiculos'                                 , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_setor_veiculos'                                 , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_cadastro_setor_veiculos'                                 , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_cadastro_setor_veiculos'                                 , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #
        ('abnf_operacional_cadastro_motivo_substituicao'                            , 'idomsub' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_cadastro_motivo_substituicao'                            , 'codomsu' , 'int'      , None , None , 'Codigo do motivo de substituicao'                                 , None, None),
        ('abnf_operacional_cadastro_motivo_substituicao'                            , 'descmsu' , 'varchar'  , 100  , None , 'Descricao do motivo de substituicao'                              , None, None),
        ('abnf_operacional_cadastro_motivo_substituicao'                            , 'tiposub' , 'varchar'  , 1    , None , 'Tipo de substituicao'                                             , None, None),
        ('abnf_operacional_cadastro_motivo_substituicao'                            , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_cadastro_motivo_substituicao'                            , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_motivo_substituicao'                            , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_motivo_substituicao'                            , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_cadastro_motivo_substituicao'                            , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_cadastro_motivo_substituicao'                            , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #
        ('abnf_operacional_cadastro_grupos_usuarios'                                , 'idcusgr' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_cadastro_grupos_usuarios'                                , 'codcusg' , 'int'      , None , None , 'Codigo do grupo de usuarios do controle diario'                   , None, None),
        ('abnf_operacional_cadastro_grupos_usuarios'                                , 'descusg' , 'varchar'  , 100  , None , 'Descricao do grupo de usuarios do controle diario'                , None, None),
        ('abnf_operacional_cadastro_grupos_usuarios'                                , 'permaut' , 'boolean'  , None , None , 'Permite definir o metodo automatico-manual no controle diario'    , None, None),
        ('abnf_operacional_cadastro_grupos_usuarios'                                , 'perrefd' , 'boolean'  , None , None , 'Permite refazer os registros de diario'                           , None, None),
        ('abnf_operacional_cadastro_grupos_usuarios'                                , 'percaal' , 'boolean'  , None , None , 'Permite cancelar alteracao de informacoes'                        , None, None),
        ('abnf_operacional_cadastro_grupos_usuarios'                                , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_cadastro_grupos_usuarios'                                , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_grupos_usuarios'                                , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_grupos_usuarios'                                , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_cadastro_grupos_usuarios'                                , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_cadastro_grupos_usuarios'                                , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #
        ('abnf_operacional_cadastro_grupos_usuarios_vinculos'                       , 'idcugvi' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_cadastro_grupos_usuarios_vinculos'                       , 'idcusgr' , 'int'      , None , None , 'ID do grupo de usuarios do controle diario'                       , 'abnf_operacional_cadastro_grupos_usuarios', 'idcusgr'),
        ('abnf_operacional_cadastro_grupos_usuarios_vinculos'                       , 'idusuar' , 'int'      , None , None , 'ID do usuario'                                                    , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_grupos_usuarios_vinculos'                       , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_cadastro_grupos_usuarios_vinculos'                       , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_grupos_usuarios_vinculos'                       , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_cadastro_grupos_usuarios_vinculos'                       , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_cadastro_grupos_usuarios_vinculos'                       , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'idoprop' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'numepro' , 'int'      , None , None , 'Numero da proposta'                                               , None, None),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'idoproj' , 'int'      , None , None , 'ID do projeto'                                                    , 'abnf_operacional_cadastro_projetos', 'idoproj'),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'idolinh' , 'int'      , None , None , 'ID da linha'                                                      , 'abnf_operacional_cadastro_linhas', 'idolinh'),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'observa' , 'text'     , None , None , 'Observacao'                                                       , None, None),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'descpre' , 'varchar'  , 200  , None , 'Descricao da prefeitura'                                          , None, None),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'tpdiaut' , 'boolean'  , None , None , 'Tipo de dia: util'                                                , None, None),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'tpdiasa' , 'boolean'  , None , None , 'Tipo de dia: sabado'                                              , None, None),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'tpdiado' , 'boolean'  , None , None , 'Tipo de dia: domingo'                                             , None, None),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'tpdiafe' , 'boolean'  , None , None , 'Tipo de dia: feriado'                                             , None, None),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'tpdia2a' , 'boolean'  , None , None , 'Tipo de dia: segunda-feira'                                       , None, None),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'tpdia3a' , 'boolean'  , None , None , 'Tipo de dia: terca-feira'                                         , None, None),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'tpdia4a' , 'boolean'  , None , None , 'Tipo de dia: quarta-feira'                                        , None, None),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'tpdia5a' , 'boolean'  , None , None , 'Tipo de dia: quinta-feira'                                        , None, None),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'tpdia6a' , 'boolean'  , None , None , 'Tipo de dia: sexta-feira'                                         , None, None),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'numrele' , 'int'      , None , None , 'Numero de release'                                                , None, None),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'situpro' , 'varchar'  , 1    , None , 'Situacao da proposta'                                             , None, None),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'dataapr' , 'datetime' , None , None , 'Ultima data/hora de aprovacao/reprovacao da proposta'             , None, None),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'datavig' , 'date'     , None , None , 'Ultima data de vigoracao da OSO'                                  , None, None),
        # /// #
        ('abnf_operacional_movimentacao_propostas_oso_viagens'                      , 'idopvia' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_movimentacao_propostas_oso_viagens'                      , 'idoprop' , 'int'      , None , None , 'ID da proposta'                                                   , 'abnf_operacional_movimentacao_propostas_oso', 'idoprop'),
        ('abnf_operacional_movimentacao_propostas_oso_viagens'                      , 'numrele' , 'int'      , None , None , 'Numero de release'                                                , None, None),
        ('abnf_operacional_movimentacao_propostas_oso_viagens'                      , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_movimentacao_propostas_oso_viagens'                      , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_propostas_oso_viagens'                      , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_propostas_oso_viagens'                      , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_movimentacao_propostas_oso_viagens'                      , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_movimentacao_propostas_oso_viagens'                      , 'sentido' , 'varchar'  , 1    , None , 'Sentido'                                                          , None, None),
        ('abnf_operacional_movimentacao_propostas_oso_viagens'                      , 'tipopon' , 'varchar'  , 1    , None , 'Tipo de ponto'                                                    , None, None),
        ('abnf_operacional_movimentacao_propostas_oso_viagens'                      , 'veicpro' , 'int'      , None , None , 'Veiculo da proposta'                                              , None, None),
        ('abnf_operacional_movimentacao_propostas_oso_viagens'                      , 'veicger' , 'int'      , None , None , 'Veiculo geral'                                                    , None, None),
        ('abnf_operacional_movimentacao_propostas_oso_viagens'                      , 'seghini' , 'int'      , None , None , 'Horario de inicio (em segundos)'                                  , None, None),
        ('abnf_operacional_movimentacao_propostas_oso_viagens'                      , 'seghfim' , 'int'      , None , None , 'Horario de termino (em segundos)'                                 , None, None),
        ('abnf_operacional_movimentacao_propostas_oso_viagens'                      , 'idotraj' , 'int'      , None , None , 'ID do trajeto'                                                    , 'abnf_operacional_cadastro_trajetos', 'idotraj'),
        ('abnf_operacional_movimentacao_propostas_oso_viagens'                      , 'idolori' , 'boolean'  , None , None , 'ID do local de origem'                                            , 'abnf_operacional_cadastro_locais', 'idoloca'),
        ('abnf_operacional_movimentacao_propostas_oso_viagens'                      , 'idoldes' , 'boolean'  , None , None , 'ID do local de destino'                                           , 'abnf_operacional_cadastro_locais', 'idoloca'),
        ('abnf_operacional_movimentacao_propostas_oso_viagens'                      , 'idotivi' , 'int'      , None , None , 'Tipo de viagem'                                                   , None, None),
        ('abnf_operacional_movimentacao_propostas_oso_viagens'                      , 'encerra' , 'varchar'  , 1    , None , 'Encerramento da viagem'                                           , None, None),
        ('abnf_operacional_movimentacao_propostas_oso_viagens'                      , 'enctext' , 'varchar'  , 100  , None , 'Encerramento da viagem: texto opcional'                           , None, None),
        ('abnf_operacional_movimentacao_propostas_oso_viagens'                      , 'seghgar' , 'int'      , None , None , 'Horario de saida extra da garagem (em segundos) '                 , None, None),
        # /// #
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'idoosoo' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'numeoso' , 'int'      , None , None , 'Numero da OSO'                                                    , None, None),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'idoprop' , 'key'      , None , None , 'ID da proposta'                                                   , 'abnf_operacional_movimentacao_propostas_oso', 'idoprop'),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'numepro' , 'int'      , None , None , 'Numero da proposta (historico)'                                   , None, None),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'numrele' , 'int'      , None , None , 'Numero de release (historico)'                                    , None, None),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'idoproj' , 'int'      , None , None , 'ID do projeto'                                                    , 'abnf_operacional_cadastro_projetos', 'idoproj'),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'codopro' , 'int'      , None , None , 'Codigo do projeto (historico)'                                    , None, None),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'desopro' , 'varchar'  , 100  , None , 'Descricao do projeto (historico)'                                 , None, None),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'idolinh' , 'int'      , None , None , 'ID da linha'                                                      , 'abnf_operacional_cadastro_linhas', 'idolinh'),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'codolin' , 'varchar'  , 20   , None , 'Codigo da linha (historico)'                                      , None, None),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'desolin' , 'varchar'  , 100  , None , 'Descricao da linha (historico)'                                   , None, None),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'observa' , 'text'     , None , None , 'Observacao'                                                       , None, None),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'descpre' , 'varchar'  , 200  , None , 'Descricao da prefeitura'                                          , None, None),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'tpdiaut' , 'boolean'  , None , None , 'Tipo de dia: util'                                                , None, None),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'tpdiasa' , 'boolean'  , None , None , 'Tipo de dia: sabado'                                              , None, None),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'tpdiado' , 'boolean'  , None , None , 'Tipo de dia: domingo'                                             , None, None),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'tpdiafe' , 'boolean'  , None , None , 'Tipo de dia: feriado'                                             , None, None),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'tpdia2a' , 'boolean'  , None , None , 'Tipo de dia: segunda-feira'                                       , None, None),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'tpdia3a' , 'boolean'  , None , None , 'Tipo de dia: terca-feira'                                         , None, None),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'tpdia4a' , 'boolean'  , None , None , 'Tipo de dia: quarta-feira'                                        , None, None),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'tpdia5a' , 'boolean'  , None , None , 'Tipo de dia: quinta-feira'                                        , None, None),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'tpdia6a' , 'boolean'  , None , None , 'Tipo de dia: sexta-feira'                                         , None, None),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'idusuap' , 'int'      , None , None , 'ID do usuario que aprovou/reprovou a OSO'                         , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'dtaprov' , 'datetime' , None , None , 'Data/hora da aprovacao da OSO'                                    , None, None),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'datavig' , 'date'     , None , None , 'Data de vigoracao da OSO'                                         , None, None),
        # /// #
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'idoovia' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'idoosoo' , 'int'      , None , None , 'ID da OSO oficial'                                                , 'abnf_operacional_movimentacao_oficial_oso', 'idoosoo'),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'sentido' , 'varchar'  , 1    , None , 'Sentido'                                                          , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'tipopon' , 'varchar'  , 1    , None , 'Tipo de ponto'                                                    , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'veicpro' , 'int'      , None , None , 'Veiculo da proposta'                                              , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'veicger' , 'int'      , None , None , 'Veiculo geral'                                                    , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'seghini' , 'int'      , None , None , 'Horario de inicio (em segundos)'                                  , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'seghfim' , 'int'      , None , None , 'Horario de termino (em segundos)'                                 , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'idootra' , 'int'      , None , None , 'ID do trajeto'                                                    , 'abnf_operacional_movimentacao_oficial_oso_trajetos', 'idootra'),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'idolori' , 'boolean'  , None , None , 'ID do local de origem'                                            , 'abnf_operacional_cadastro_locais', 'idoloca'),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'codolor' , 'int'      , None , None , 'Codigo do local de origem (historico)'                            , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'desolor' , 'varchar'  , 100  , None , 'Descricao do local de origem (historico)'                         , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'idlogor' , 'int'      , None , None , 'ID do logradouro do local de origem (historico)'                  , 'abnf_cadastro_logradouros', 'idlogra'),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'tiploor' , 'varchar'  , 50   , None , 'Tipo de logradouro do local de origem (historico)'                , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'desloor' , 'varchar'  , 200  , None , 'Descricao do logradouro do local de origem (historico)'           , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'logrnor' , 'varchar'  , 20   , None , 'Numero do logradouro do local de origem (historico)'              , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'logrcor' , 'varchar'  , 100  , None , 'Complemento do logradouro do local de origem (historico)'         , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'desbaor' , 'varchar'  , 100  , None , 'Bairro do logradouro do local de origem (historico)'              , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'descior' , 'varchar'  , 100  , None , 'Cidade do logradouro do local de origem (historico)'              , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'estador' , 'varchar'  , 2    , None , 'Estado do logradouro do local de origem (historico)'              , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'logceor' , 'varchar'  , 10   , None , 'CEP do logradouro do local de origem (historico)'                 , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'obseror' , 'text'     , None , None , 'Observacao do logradouro do local de origem (historico)'          , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'idoldes' , 'boolean'  , None , None , 'ID do local de destino'                                           , 'abnf_operacional_cadastro_locais', 'idoloca'),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'codolde' , 'int'      , None , None , 'Codigo do local de destino (historico)'                           , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'desolde' , 'varchar'  , 100  , None , 'Descricao do local de destino (historico)'                        , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'idlogde' , 'int'      , None , None , 'ID do logradouro do local de destino (historico)'                 , 'abnf_cadastro_logradouros', 'idlogra'),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'tiplode' , 'varchar'  , 50   , None , 'Tipo de logradouro do local de destino (historico)'               , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'deslode' , 'varchar'  , 200  , None , 'Descricao do logradouro do local de destino (historico)'          , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'logrnde' , 'varchar'  , 20   , None , 'Numero do logradouro do local de destino (historico)'             , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'logrcde' , 'varchar'  , 100  , None , 'Complemento do logradouro do local de destino (historico)'        , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'desbade' , 'varchar'  , 100  , None , 'Bairro do logradouro do local de destino (historico)'             , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'descide' , 'varchar'  , 100  , None , 'Cidade do logradouro do local de destino (historico)'             , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'desesde' , 'varchar'  , 2    , None , 'Estado do logradouro do local de destino (historico)'             , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'logcede' , 'varchar'  , 10   , None , 'CEP do logradouro do local de destino (historico)'                , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'obserde' , 'text'     , None , None , 'Observacao do logradouro do local de destino (historico)'         , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'idotivi' , 'int'      , None , None , 'Tipo de viagem'                                                   , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'encerra' , 'varchar'  , 1    , None , 'Encerramento da viagem'                                           , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'enctext' , 'varchar'  , 100  , None , 'Encerramento da viagem: texto opcional'                           , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'seghgar' , 'int'      , None , None , 'Horario de saida extra da garagem (em segundos) '                 , None, None),
        # /// #
        ('abnf_operacional_movimentacao_oficial_oso_trajetos'                       , 'idootra' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_trajetos'                       , 'idoosoo' , 'int'      , None , None , 'ID da OSO oficial'                                                , 'abnf_operacional_movimentacao_oficial_oso', 'idoosoo'),
        ('abnf_operacional_movimentacao_oficial_oso_trajetos'                       , 'codotra' , 'varchar'  , 4    , None , 'Codigo do trajeto'                                                , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_trajetos'                       , 'desotra' , 'varchar'  , 200  , None , 'Descricao do trajeto'                                             , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_trajetos'                       , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_trajetos'                       , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_oficial_oso_trajetos'                       , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_oficial_oso_trajetos'                       , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_trajetos'                       , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_trajetos'                       , 'kmidaxx' , 'decimal'  , 8    , 1    , 'km ida'                                                           , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_trajetos'                       , 'kmvolta' , 'decimal'  , 8    , 1    , 'km volta'                                                         , None, None),
        # /// #        
        ('abnf_operacional_movimentacao_oficial_oso_itinerarios'                    , 'idooiti' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_itinerarios'                    , 'idootra' , 'int'      , None , None , 'ID do trajeto'                                                    , 'abnf_operacional_movimentacao_oficial_oso_trajetos', 'idotraj'),
        ('abnf_operacional_movimentacao_oficial_oso_itinerarios'                    , 'sentido' , 'varchar'  , 1    , None , 'Sentido'                                                          , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_itinerarios'                    , 'ordemit' , 'int'      , None , None , 'Ordem no itinerario'                                              , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_itinerarios'                    , 'idlogra' , 'int'      , None , None , 'ID do logradouro'                                                 , 'abnf_cadastro_logradouros', 'idlogra'),
        ('abnf_operacional_movimentacao_oficial_oso_itinerarios'                    , 'tiplogr' , 'varchar'  , 50   , None , 'Tipo de logradouro (historico)'                                   , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_itinerarios'                    , 'deslogr' , 'varchar'  , 200  , None , 'Descricao do logradouro (historico)'                              , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_itinerarios'                    , 'complem' , 'varchar'  , 100  , None , 'Complemento (historico)'                                          , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_itinerarios'                    , 'desbair' , 'varchar'  , 100  , None , 'Descricao do bairro (historico)'                                  , None, None),        
        ('abnf_operacional_movimentacao_oficial_oso_itinerarios'                    , 'descida' , 'varchar'  , 100  , None , 'Descricao da cidade (historico)'                                  , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_itinerarios'                    , 'desesta' , 'varchar'  , 2    , None , 'Descricao do estado (historico)'                                  , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_itinerarios'                    , 'destaqu' , 'boolean'  , None , None , 'Destaque'                                                         , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_itinerarios'                    , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_itinerarios'                    , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_oficial_oso_itinerarios'                    , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_oficial_oso_itinerarios'                    , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_movimentacao_oficial_oso_itinerarios'                    , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'idoprdi' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'dataope' , 'date'     , None , None , 'Data da operacao'                                                 , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'tiporeg' , 'varchar'  , 1    , None , 'Tipo de registro'                                                 , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'idcusde' , 'int'      , None , None , 'ID do usuario que definiu o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'idolinh' , 'int'      , None , None , 'ID da linha'                                                      , 'abnf_operacional_cadastro_linhas', 'idolinh'),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'codolin' , 'varchar'  , 20   , None , 'Codigo da linha (historico)'                                      , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'desolin' , 'varchar'  , 100  , None , 'Descricao da linha (historico)'                                   , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'veicpro' , 'int'      , None , None , 'Veiculo da proposta'                                              , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'veicger' , 'int'      , None , None , 'Veiculo geral'                                                    , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'tipodia' , 'varchar'  , 1    , None , 'Tipo de dia'                                                      , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'descmot' , 'varchar'  , 100  , None , 'Descricao do motivo'                                              , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'sentido' , 'varchar'  , 1    , None , 'Sentido'                                                          , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'tipopon' , 'varchar'  , 1    , None , 'Tipo de ponto'                                                    , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'idotivi' , 'int'      , None , None , 'Tipo de viagem'                                                   , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'seghini' , 'int'      , None , None , 'Horario de inicio (em segundos)'                                  , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'seghfim' , 'int'      , None , None , 'Horario de termino (em segundos)'                                 , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'saidgar' , 'boolean'  , None , None , 'Saida da garagem'                                                 , None, None),        
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'seghgar' , 'int'      , None , None , 'Horario de saida da garagem (em segundos) '                       , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'idolori' , 'boolean'  , None , None , 'ID do local de origem'                                            , 'abnf_operacional_cadastro_locais', 'idoloca'),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'codolor' , 'int'      , None , None , 'Codigo do local de origem (historico)'                            , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'desolor' , 'varchar'  , 100  , None , 'Descricao do local de origem (historico)'                         , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'idoldes' , 'boolean'  , None , None , 'ID do local de destino'                                           , 'abnf_operacional_cadastro_locais', 'idoloca'),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'codolde' , 'int'      , None , None , 'Codigo do local de destino (historico)'                           , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'desolde' , 'varchar'  , 100  , None , 'Descricao do local de destino (historico)'                        , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'idveicu' , 'int'      , None , None , 'ID do veiculo'                                                    , 'abnf_cadastro_veiculos', 'idveicu'),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'prefvei' , 'varchar'  , 20   , None , 'Prefixo do veiculo (historico)'                                   , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'idveofi' , 'int'      , None , None , 'ID do veiculo oficial'                                            , 'abnf_cadastro_veiculos', 'idveicu'),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'prefvof' , 'varchar'  , 20   , None , 'Prefixo do veiculo oficial (historico)'                           , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'idosetv' , 'int'      , None , None , 'ID do setor de veiculo'                                           , 'abnf_operacional_cadastro_setor_veiculos', 'idosetv'),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'codoset' , 'int'      , None , None , 'Codigo do setor de veiculos (historico)'                          , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'descset' , 'varchar'  , 100  , None , 'Descricao do setor de veiculos (historico)'                       , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'observa' , 'text'     , None , None , 'Observacao'                                                       , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #        
        ('abnf_operacional_movimentacao_programacao_substituicao'                   , 'idoprsu' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_movimentacao_programacao_substituicao'                   , 'idoprdi' , 'key'      , None , None , 'ID do registro de diario de programacao'                          , 'abnf_operacional_movimentacao_programacao_diario', 'idoprdi'),
        ('abnf_operacional_movimentacao_programacao_substituicao'                   , 'tiposub' , 'varchar'  , 1    , None , 'Tipo de substituicao'                                             , None, None),
        ('abnf_operacional_movimentacao_programacao_substituicao'                   , 'idveisa' , 'int'      , None , None , 'ID do veiculo que sai'                                            , 'abnf_cadastro_veiculos', 'idveicu'),
        ('abnf_operacional_movimentacao_programacao_substituicao'                   , 'idveien' , 'int'      , None , None , 'ID do veiculo que entra'                                          , 'abnf_cadastro_veiculos', 'idveicu'),
        ('abnf_operacional_movimentacao_programacao_substituicao'                   , 'idomsub' , 'int'      , None , None , 'ID do motivo da substituicao'                                     , 'abnf_operacional_cadastro_motivo_substituicao', 'idomsub'),
        ('abnf_operacional_movimentacao_programacao_substituicao'                   , 'motisub' , 'text'     , None , None , 'Complemento'                                                      , None, None),
        ('abnf_operacional_movimentacao_programacao_substituicao'                   , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_movimentacao_programacao_substituicao'                   , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_programacao_substituicao'                   , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_programacao_substituicao'                   , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_movimentacao_programacao_substituicao'                   , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_movimentacao_programacao_substituicao'                   , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #
        ('abnf_operacional_movimentacao_programacao_automacao'                      , 'idoprau' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_movimentacao_programacao_automacao'                      , 'dtmetod' , 'datetime' , None , None , 'Data/hora da definicao do metodo'                                 , None, None),
        ('abnf_operacional_movimentacao_programacao_automacao'                      , 'defmeto' , 'varchar'  , 1    , None , 'Definicao do metodo'                                              , None, None),
        ('abnf_operacional_movimentacao_programacao_automacao'                      , 'idusuar' , 'int'      , None , None , 'ID do usuario que definiu o metodo'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_programacao_automacao'                      , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_movimentacao_programacao_automacao'                      , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_programacao_automacao'                      , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_programacao_automacao'                      , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_movimentacao_programacao_automacao'                      , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_movimentacao_programacao_automacao'                      , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'idoprrv' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'codctrl' , 'int'      , None , None , 'Codigo de controle'                                               , None, None),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'idveicu' , 'int'      , None , None , 'ID do veiculo'                                                    , 'abnf_cadastro_veiculos', 'idveicu'),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'dtreten' , 'datetime' , None , None , 'Data/hora da ordem de retencao'                                   , None, None),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'dtliber' , 'datetime' , None , None , 'Data/hora da ordem de liberacao'                                  , None, None),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'idcusgr' , 'int'      , None , None , 'ID do grupo de usuarios do controle diario'                       , 'abnf_operacional_cadastro_grupos_usuarios', 'idcusgr'),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'idcusre' , 'int'      , None , None , 'ID do usuario que reteve'                                         , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'idcusli' , 'int'      , None , None , 'ID do usuario que liberou'                                        , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'dataage' , 'date'     , None , None , 'Data do agendamento da retencao'                                  , None, None),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'seghage' , 'int'      , None , None , 'Horario do agendamento da retencao (em segundos)'                 , None, None),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'descrre' , 'text'     , None , None , 'Descricao na retencao do veiculo'                                 , None, None),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'descrli' , 'text'     , None , None , 'Descricao na liberacao do veiculo'                                , None, None),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'statret' , 'int'      , None , None , 'Status da retencao'                                               , None, None),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'idsdede' , 'int'      , None , None , 'ID da definicao de defeito do SIGOM'                              , 'abnf_sigom_cadastro_defeitos_definicoes', 'idsdede'),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #
        ('abnf_operacional_entrada_saida_veiculos_locais'                           , 'idoesvl' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_entrada_saida_veiculos_locais'                           , 'codoesl' , 'int'      , None , None , 'Codigo do local'                                                  , None, None),
        ('abnf_operacional_entrada_saida_veiculos_locais'                           , 'desoesl' , 'varchar'  , 100  , None , 'Descricao do local'                                               , None, None),
        ('abnf_operacional_entrada_saida_veiculos_locais'                           , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_entrada_saida_veiculos_locais'                           , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_entrada_saida_veiculos_locais'                           , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_entrada_saida_veiculos_locais'                           , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_entrada_saida_veiculos_locais'                           , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_entrada_saida_veiculos_locais'                           , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        ('abnf_operacional_entrada_saida_veiculos_locais'                           , 'tipoloc' , 'varchar'  , 1    , None , 'Tipo de local'                                                    , None, None),
        # /// #
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'idoesve' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'idveicu' , 'int'      , None , None , 'ID do veiculo'                                                    , 'abnf_cadastro_veiculos', 'idveicu'),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'idoesvl' , 'int'      , None , None , 'ID do local'                                                      , 'abnf_operacional_entrada_saida_veiculos_locais', 'idoesvl'),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'dataesv' , 'date'     , None , None , 'Data da entrada/saida do veiculo'                                 , None, None),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'horaesv' , 'time'     , None , None , 'Hora da entrada/saida do veiculo'                                 , None, None),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'tipomov' , 'varchar'  , 1    , None , 'Tipo de movimentacao'                                             , None, None),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'odomvei' , 'int'      , None , None , 'Odometro do veiculo'                                              , None, None),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'rolevei' , 'int'      , None , None , 'Roleta do veiculo'                                                , None, None),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'idolinh' , 'int'      , None , None , 'ID da linha'                                                      , 'abnf_operacional_cadastro_linhas', 'idolinh'),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'idmot01' , 'int'      , None , None , 'ID do motorista 01'                                               , 'abnf_cadastro_funcionarios', 'idfunci'),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'idmot02' , 'int'      , None , None , 'ID do motorista 02'                                               , 'abnf_cadastro_funcionarios', 'idfunci'),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'idmot03' , 'int'      , None , None , 'ID do motorista 03'                                               , 'abnf_cadastro_funcionarios', 'idfunci'),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'idcob01' , 'int'      , None , None , 'ID do cobrador 01'                                                , 'abnf_cadastro_funcionarios', 'idfunci'),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'idcob02' , 'int'      , None , None , 'ID do cobrador 02'                                                , 'abnf_cadastro_funcionarios', 'idfunci'),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'idcob03' , 'int'      , None , None , 'ID do cobrador 03'                                                , 'abnf_cadastro_funcionarios', 'idfunci'),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'observa' , 'text'     , None , None , 'Observacao'                                                       , None, None),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #
        ('abnf_operacional_entrada_saida_veiculos_check_list_padrao'                , 'idoclpa' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_entrada_saida_veiculos_check_list_padrao'                , 'codoclp' , 'int'      , None , None , 'Codigo do item de check list'                                     , None, None),
        ('abnf_operacional_entrada_saida_veiculos_check_list_padrao'                , 'desoclp' , 'varchar'  , 100  , None , 'Descricao do item de check list'                                  , None, None),
        ('abnf_operacional_entrada_saida_veiculos_check_list_padrao'                , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_entrada_saida_veiculos_check_list_padrao'                , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_entrada_saida_veiculos_check_list_padrao'                , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_entrada_saida_veiculos_check_list_padrao'                , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_entrada_saida_veiculos_check_list_padrao'                , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_entrada_saida_veiculos_check_list_padrao'                , 'tipomov' , 'varchar'  , 1    , None , 'Tipo de movimentacao'                                             , None, None),
        # /// #
        ('abnf_operacional_entrada_saida_veiculos_check_list'                       , 'idochli' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_operacional_entrada_saida_veiculos_check_list'                       , 'idoclpa' , 'int'      , None , None , 'ID de item de check list padrao'                                  , 'abnf_operacional_entrada_saida_veiculos_check_list_padrao', 'idoclpa'),
        ('abnf_operacional_entrada_saida_veiculos_check_list'                       , 'idoesve' , 'int'      , None , None , 'ID do registro de movimentacao do veiculo'                        , 'abnf_operacional_entrada_saida_veiculos', 'idoesve'),
        ('abnf_operacional_entrada_saida_veiculos_check_list'                       , 'idveicu' , 'int'      , None , None , 'ID do veiculo'                                                    , 'abnf_cadastro_veiculos', 'idveicu'),
        ('abnf_operacional_entrada_saida_veiculos_check_list'                       , 'marcado' , 'varchar'  , 1    , None , 'Marcado'                                                          , None, None),
        ('abnf_operacional_entrada_saida_veiculos_check_list'                       , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_operacional_entrada_saida_veiculos_check_list'                       , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_entrada_saida_veiculos_check_list'                       , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_operacional_entrada_saida_veiculos_check_list'                       , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_operacional_entrada_saida_veiculos_check_list'                       , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_operacional_entrada_saida_veiculos_check_list'                       , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #
        ('abnf_sigom_cadastro_usuarios_grupos'                                      , 'idsusgr' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sigom_cadastro_usuarios_grupos'                                      , 'codsusg' , 'int'      , None , None , 'Codigo do grupo de usuarios do SIGOM'                             , None, None),
        ('abnf_sigom_cadastro_usuarios_grupos'                                      , 'dessusg' , 'varchar'  , 100  , None , 'Descricao do grupo de usuarios do SIGOM'                          , None, None),
        ('abnf_sigom_cadastro_usuarios_grupos'                                      , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sigom_cadastro_usuarios_grupos'                                      , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_cadastro_usuarios_grupos'                                      , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_cadastro_usuarios_grupos'                                      , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sigom_cadastro_usuarios_grupos'                                      , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_sigom_cadastro_usuarios_grupos'                                      , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        ('abnf_sigom_cadastro_usuarios_grupos'                                      , 'emailgr' , 'varchar'  , 100  , None , 'E-mail do grupo'                                                  , None, None),
        # /// #                                                              
        ('abnf_sigom_cadastro_usuarios_grupos_vinculos'                             , 'idsugvi' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sigom_cadastro_usuarios_grupos_vinculos'                             , 'idsusgr' , 'int'      , None , None , 'ID do grupo de usuarios do SIGOM'                                 , 'abnf_sigom_cadastro_usuarios_grupos', 'idsusgr'),
        ('abnf_sigom_cadastro_usuarios_grupos_vinculos'                             , 'idusuar' , 'int'      , None , None , 'ID do usuario'                                                    , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_cadastro_usuarios_grupos_vinculos'                             , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sigom_cadastro_usuarios_grupos_vinculos'                             , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_cadastro_usuarios_grupos_vinculos'                             , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_cadastro_usuarios_grupos_vinculos'                             , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sigom_cadastro_usuarios_grupos_vinculos'                             , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # /// #
        ('abnf_sigom_cadastro_ocorrencias_tipos'                                    , 'idsocti' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sigom_cadastro_ocorrencias_tipos'                                    , 'codsoct' , 'int'      , None , None , 'Codigo do tipo de ocorrencia do SIGOM'                            , None, None),
        ('abnf_sigom_cadastro_ocorrencias_tipos'                                    , 'dessoct' , 'varchar'  , 100  , None , 'Descricao do tipo de ocorrencia do SIGOM'                         , None, None),
        ('abnf_sigom_cadastro_ocorrencias_tipos'                                    , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sigom_cadastro_ocorrencias_tipos'                                    , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_cadastro_ocorrencias_tipos'                                    , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_cadastro_ocorrencias_tipos'                                    , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sigom_cadastro_ocorrencias_tipos'                                    , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_sigom_cadastro_ocorrencias_tipos'                                    , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        ('abnf_sigom_cadastro_ocorrencias_tipos'                                    , 'obrdulp' , 'boolean'  , None , None , 'Obrigatorio inserir a data da ultima preventiva no fechamento'    , None, None),
        ('abnf_sigom_cadastro_ocorrencias_tipos'                                    , 'obrnerp' , 'boolean'  , None , None , 'Obrigatorio inserir o numero do documento do ERP no fechamento'   , None, None),
        ('abnf_sigom_cadastro_ocorrencias_tipos'                                    , 'obracto' , 'boolean'  , None , None , 'Obrigatorio inserir a acao tomada no fechamento'                  , None, None),
        # /// #
        ('abnf_sigom_cadastro_veiculos_situacao'                                    , 'idsvesi' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sigom_cadastro_veiculos_situacao'                                    , 'codsves' , 'int'      , None , None , 'Codigo da situacao de veiculo do SIGOM'                           , None, None),
        ('abnf_sigom_cadastro_veiculos_situacao'                                    , 'dessves' , 'varchar'  , 100  , None , 'Descricao da situacao de veiculo do SIGOM'                        , None, None),
        ('abnf_sigom_cadastro_veiculos_situacao'                                    , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sigom_cadastro_veiculos_situacao'                                    , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_cadastro_veiculos_situacao'                                    , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_cadastro_veiculos_situacao'                                    , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sigom_cadastro_veiculos_situacao'                                    , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_sigom_cadastro_veiculos_situacao'                                    , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #
        ('abnf_sigom_cadastro_classificacao'                                        , 'idsclas' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sigom_cadastro_classificacao'                                        , 'codscla' , 'int'      , None , None , 'Codigo da classificacao do SIGOM'                                 , None, None),
        ('abnf_sigom_cadastro_classificacao'                                        , 'desscla' , 'varchar'  , 100  , None , 'Descricao da classificacao do SIGOM'                              , None, None),
        ('abnf_sigom_cadastro_classificacao'                                        , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sigom_cadastro_classificacao'                                        , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_cadastro_classificacao'                                        , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_cadastro_classificacao'                                        , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sigom_cadastro_classificacao'                                        , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_sigom_cadastro_classificacao'                                        , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # /// #
        ('abnf_sigom_cadastro_defeitos_grupos'                                      , 'idsdegr' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sigom_cadastro_defeitos_grupos'                                      , 'codsdeg' , 'int'      , None , None , 'Codigo do grupo de GSD do SIGOM'                                  , None, None),
        ('abnf_sigom_cadastro_defeitos_grupos'                                      , 'dessdeg' , 'varchar'  , 100  , None , 'Descricao do grupo de GSD do SIGOM'                               , None, None),
        ('abnf_sigom_cadastro_defeitos_grupos'                                      , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sigom_cadastro_defeitos_grupos'                                      , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_cadastro_defeitos_grupos'                                      , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_cadastro_defeitos_grupos'                                      , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sigom_cadastro_defeitos_grupos'                                      , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_sigom_cadastro_defeitos_grupos'                                      , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        ('abnf_sigom_cadastro_defeitos_grupos'                                      , 'impiifo' , 'boolean'  , None , None , 'Impacta no indicador IFO (Indice de falha operacional)'           , None, None),
        ('abnf_sigom_cadastro_defeitos_grupos'                                      , 'dashboa' , 'boolean'  , None , None , 'Ativo nos dashboards'                                             , None, None),
        # /// #
        ('abnf_sigom_cadastro_defeitos_subgrupos'                                   , 'idsdesg' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sigom_cadastro_defeitos_subgrupos'                                   , 'codsdes' , 'int'      , None , None , 'Codigo do subgrupo de GSD do SIGOM'                               , None, None),
        ('abnf_sigom_cadastro_defeitos_subgrupos'                                   , 'dessdes' , 'varchar'  , 100  , None , 'Descricao do subgrupo de GSD do SIGOM'                            , None, None),
        ('abnf_sigom_cadastro_defeitos_subgrupos'                                   , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sigom_cadastro_defeitos_subgrupos'                                   , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_cadastro_defeitos_subgrupos'                                   , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_cadastro_defeitos_subgrupos'                                   , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sigom_cadastro_defeitos_subgrupos'                                   , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_sigom_cadastro_defeitos_subgrupos'                                   , 'idsdegr' , 'int'      , None , None , 'ID do grupo de GSD do SIGOM'                                      , 'abnf_sigom_cadastro_defeitos_grupos', 'idsdegr'),
        # /// #
        ('abnf_sigom_cadastro_defeitos_definicoes'                                  , 'idsdede' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sigom_cadastro_defeitos_definicoes'                                  , 'codsded' , 'int'      , None , None , 'Codigo da definicao de GSD do SIGOM'                              , None, None),
        ('abnf_sigom_cadastro_defeitos_definicoes'                                  , 'dessded' , 'varchar'  , 100  , None , 'Descricao da definicao de GSD do SIGOM'                           , None, None),
        ('abnf_sigom_cadastro_defeitos_definicoes'                                  , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sigom_cadastro_defeitos_definicoes'                                  , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_cadastro_defeitos_definicoes'                                  , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_cadastro_defeitos_definicoes'                                  , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sigom_cadastro_defeitos_definicoes'                                  , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_sigom_cadastro_defeitos_definicoes'                                  , 'idsdesg' , 'int'      , None , None , 'ID do subgrupo de GSD do SIGOM'                                   , 'abnf_sigom_cadastro_defeitos_definicoes', 'idsdegr'),
        # /// #
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'idsocor' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'codsate' , 'int'      , None , None , 'Codigo da ocorrencia do SIGOM'                                    , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'situoco' , 'varchar'  , 1    , None , 'Situacao da ocorrencia'                                           , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'dataabe' , 'date'     , None , None , 'Data de abertura'                                                 , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'horaabe' , 'time'     , None , None , 'Horario de abertura'                                              , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'datafec' , 'date'     , None , None , 'Data de fechamento'                                               , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'horafec' , 'time'     , None , None , 'Horario de fechamento'                                            , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'dataoco' , 'date'     , None , None , 'Data da ocorrencia'                                               , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'horaoco' , 'time'     , None , None , 'Horario da ocorrencia'                                            , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'horalib' , 'time'     , None , None , 'Horario da liberacao'                                             , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'idfunci' , 'int'      , None , None , 'ID do funcionario envolvido'                                      , 'abnf_cadastro_funcionarios', 'idfunci'),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'idolinh' , 'int'      , None , None , 'ID da linha da operacao envolvida'                                , 'abnf_operacional_cadastro_linhas', 'idolinh'),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'tabolin' , 'int'      , None , None , 'Numero da tabela da linha da operacao envolvida'                  , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'situoco' , 'varchar'  , 1    , None , 'Entrada/Saida'                                                    , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'idclfor' , 'int'      , None , None , 'Cliente'                                                          , 'abnf_cadastro_clientes_fornecedores', 'idclfor'),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'tempatr' , 'time'     , None , None , 'Tempo de atraso do cliente'                                       , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'idvedef' , 'int'      , None , None , 'ID do veiculo com defeito'                                        , 'abnf_cadastro_veiculos', 'idveicu'),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'idvesub' , 'int'      , None , None , 'ID do veiculo substituto'                                         , 'abnf_cadastro_veiculos', 'idveicu'),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'localoc' , 'varchar'  , 100  , None , 'Local da ocorrencia'                                              , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'descroc' , 'text'     , None , None , 'Descricao da ocorrencia'                                          , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'idsocti' , 'int'      , None , None , 'ID do tipo de ocorrencia do SIGOM'                                , 'abnf_sigom_cadastro_ocorrencias_tipos', 'idsocti'),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'idsvesi' , 'int'      , None , None , 'ID da situacao de veiculo do SIGOM'                               , 'abnf_sigom_movimentacao_ocorrencias', 'idsvesi'),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'dultprv' , 'date'     , None , None , 'Data da ultima preventiva do veiculo'                             , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'kmmorto' , 'decimal'  , 10   , 1    , 'Km morto'                                                         , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'erpdocu' , 'int'      , None , None , 'Numero do documento gerado pelo ERP da empresa'                   , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'idsclas' , 'int'      , None , None , 'ID da classificacao do SIGOM'                                     , 'abnf_sigom_cadastro_classificacao', 'idsclas'),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'idsdede' , 'int'      , None , None , 'ID da definicao de GSD do SIGOM'                                  , 'abnf_sigom_cadastro_defeitos_definicoes', 'idsdede'),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'impiifo' , 'boolean'  , None , None , 'Impacta no indicador IFO'                                         , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'kmprogr' , 'decimal'  , 10   , 1    , 'Km programado'                                                    , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'kmreali' , 'decimal'  , 10   , 1    , 'Km realizado'                                                     , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'acaotom' , 'text'     , None , None , 'Acao tomada'                                                      , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'idfuate' , 'int'      , None , None , 'ID do usuario atendente'                                          , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'idfures' , 'int'      , None , None , 'ID do usuario responsavel'                                        , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'ococanc' , 'boolean'  , None , None , 'Ocorrencia cancelada'                                             , None, None),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'idsusab' , 'int'      , None , None , 'ID do grupo de usuarios do SIGOM que abriu o ocorrencia'          , 'abnf_sigom_cadastro_usuarios_grupos', 'idsusgr'),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'idsusde' , 'int'      , None , None , 'ID do grupo de usuarios do SIGOM que foi destinado o ocorrencia'  , 'abnf_sigom_cadastro_usuarios_grupos', 'idsusgr'),
        # /// #
        ('abnf_sigom_movimentacao_ocorrencias_complementos'                         , 'idsocco' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sigom_movimentacao_ocorrencias_complementos'                         , 'idsocor' , 'int'      , None , None , 'ID da ocorrencia do SIGOM'                                        , 'abnf_sigom_movimentacao_ocorrencias', 'idsocor'),
        ('abnf_sigom_movimentacao_ocorrencias_complementos'                         , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sigom_movimentacao_ocorrencias_complementos'                         , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_movimentacao_ocorrencias_complementos'                         , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_movimentacao_ocorrencias_complementos'                         , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sigom_movimentacao_ocorrencias_complementos'                         , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_sigom_movimentacao_ocorrencias_complementos'                         , 'datacom' , 'date'     , None , None , 'Data do complemento'                                              , None, None),
        ('abnf_sigom_movimentacao_ocorrencias_complementos'                         , 'horacom' , 'time'     , None , None , 'Horario do complemento'                                           , None, None),
        ('abnf_sigom_movimentacao_ocorrencias_complementos'                         , 'descrco' , 'text'     , None , None , 'Descricao do complemento'                                         , None, None),
        ('abnf_sigom_movimentacao_ocorrencias_complementos'                         , 'idsusab' , 'int'      , None , None , 'ID do grupo de usuarios do SIGOM que abriu a ocorrencia'          , 'abnf_sigom_cadastro_usuarios_grupos', 'idsusgr'),
        ('abnf_sigom_movimentacao_ocorrencias_complementos'                         , 'idsusde' , 'int'      , None , None , 'ID do grupo de usuarios do SIGOM que foi destinado a ocorrencia'  , 'abnf_sigom_cadastro_usuarios_grupos', 'idsusgr'),
        # /// #
        ('abnf_sigom_movimentacao_ocorrencias_arquivos'                             , 'idsocar' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        ('abnf_sigom_movimentacao_ocorrencias_arquivos'                             , 'idsocor' , 'int'      , None , None , 'ID da ocorrencia do SIGOM'                                        , 'abnf_sigom_movimentacao_ocorrencias', 'idsocor'),
        ('abnf_sigom_movimentacao_ocorrencias_arquivos'                             , 'idsocco' , 'int'      , None , None , 'ID do complemento de ocorrencia do SIGOM'                         , 'abnf_sigom_movimentacao_ocorrencias_complementos', 'idsocco'),
        ('abnf_sigom_movimentacao_ocorrencias_arquivos'                             , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        ('abnf_sigom_movimentacao_ocorrencias_arquivos'                             , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_movimentacao_ocorrencias_arquivos'                             , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        ('abnf_sigom_movimentacao_ocorrencias_arquivos'                             , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        ('abnf_sigom_movimentacao_ocorrencias_arquivos'                             , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        ('abnf_sigom_movimentacao_ocorrencias_arquivos'                             , 'idarqui' , 'int'      , None , None , 'ID do arquivo'                                                    , 'abnf_sistema_arquivos', 'idarqui'),
        # /// #
        # (Mudança de planos: usar informações fixas no lugar de tabela) ==> ('abnf_operacional_movimentacao_propostas_oso_viagens'              , 'idotivi' , 'int'      , None , None , 'ID do tipo de viagem'                                             , 'abnf_operacional_cadastro_tipos_viagem', 'idotivi'),
        # (Mudança de planos: usar informações fixas no lugar de tabela) ==> ('abnf_operacional_cadastro_tipos_viagem'                           , 'idotivi' , 'key'      , None , None , 'ID do registro'                                                   , None, None),
        # (Mudança de planos: usar informações fixas no lugar de tabela) ==> ('abnf_operacional_cadastro_tipos_viagem'                           , 'codotiv' , 'int'      , None , None , 'Codigo do tipo de viagem'                                         , None, None),
        # (Mudança de planos: usar informações fixas no lugar de tabela) ==> ('abnf_operacional_cadastro_tipos_viagem'                           , 'desotiv' , 'varchar'  , 100  , None , 'Descricao do tipo de viagem'                                      , None, None),
        # (Mudança de planos: usar informações fixas no lugar de tabela) ==> ('abnf_operacional_cadastro_tipos_viagem'                           , 'situreg' , 'varchar'  , 1    , None , 'Situacao do registro'                                             , None, None),
        # (Mudança de planos: usar informações fixas no lugar de tabela) ==> ('abnf_operacional_cadastro_tipos_viagem'                           , 'idusucr' , 'int'      , None , None , 'ID do usuario que criou o registro'                               , 'abnf_sistema_usuarios', 'idusuar'),
        # (Mudança de planos: usar informações fixas no lugar de tabela) ==> ('abnf_operacional_cadastro_tipos_viagem'                           , 'idusual' , 'int'      , None , None , 'ID do usuario que alterou o registro'                             , 'abnf_sistema_usuarios', 'idusuar'),
        # (Mudança de planos: usar informações fixas no lugar de tabela) ==> ('abnf_operacional_cadastro_tipos_viagem'                           , 'dtregcr' , 'datetime' , None , None , 'Data/hora da criacao do registro'                                 , None, None),
        # (Mudança de planos: usar informações fixas no lugar de tabela) ==> ('abnf_operacional_cadastro_tipos_viagem'                           , 'dtregal' , 'datetime' , None , None , 'Data/hora da ultima alteracao do registro'                        , None, None),
        # (Mudança de planos: usar informações fixas no lugar de tabela) ==> ('abnf_operacional_cadastro_tipos_viagem'                           , 'idfilia' , 'int'      , None , None , 'ID da filial'                                                     , 'abnf_sistema_empresas_filiais', 'idfilia'),
        # (Mudança de planos: usar informações fixas no lugar de tabela) ==> ('abnf_operacional_cadastro_tipos_viagem'                           , 'tranpas' , 'boolean'  , None , None , 'Transporta passageiros'                                           , None, None),
        # (Mudança de planos: usar informações fixas no lugar de tabela) ==> ('abnf_operacional_cadastro_tipos_viagem'                           , 'observa' , 'text'     , None , None , 'Observacao'                                                       , None, None),
        # /// #
    ]
    ldbindic = [
        # /// #
        ('abnf_sistema_empresas_matrizes'                                           , 'abnfdx01' , ('codiemp', 'idempre')),
        ('abnf_sistema_empresas_matrizes'                                           , 'abnfdx02' , ('nomeemp', 'idempre')),
        ('abnf_sistema_empresas_filiais'                                            , 'abnfdx01' , ('codifil', 'idfilia')),
        ('abnf_sistema_empresas_filiais'                                            , 'abnfdx02' , ('nomefil', 'idfilia')),
        ('abnf_sistema_usuarios'                                                    , 'abnfdx01' , ('logiusu', 'idusuar')),
        ('abnf_sistema_usuarios'                                                    , 'abnfdx02' , ('nomeusu', 'idusuar')),
        ('abnf_sistema_usuarios'                                                    , 'abnfdx03' , ('emaiusu', 'idusuar')),
        ('abnf_sistema_modulos_grupos'                                              , 'abnfdx01' , ('codgrup', 'idgrams')),
        ('abnf_sistema_modulos_grupos'                                              , 'abnfdx02' , ('desgrup', 'idgrams')),
        ('abnf_sistema_modulos_acessos'                                             , 'abnfdx01' , ('idgrams', 'idfilia', 'codmodu', 'idmodac')),
        # /// #
        ('abnf_cadastro_logradouros_cidades'                                        , 'abnfdx01' , ('codcida', 'idcidad')),
        ('abnf_cadastro_logradouros_cidades'                                        , 'abnfdx02' , ('descida', 'desesta', 'idcidad')),
        ('abnf_cadastro_logradouros_bairros'                                        , 'abnfdx01' , ('codbair', 'idbairr')),
        ('abnf_cadastro_logradouros_bairros'                                        , 'abnfdx02' , ('desbair', 'idcidad', 'idbairr')),
        ('abnf_cadastro_logradouros'                                                , 'abnfdx01' , ('codlogr', 'idlogra')),
        ('abnf_cadastro_logradouros'                                                , 'abnfdx02' , ('deslogr', 'idbairr', 'idlogra')),
        ('abnf_cadastro_logradouros'                                                , 'abnfdx03' , ('tiplogr', 'deslogr', 'idbairr', 'idlogra')),
        ('abnf_cadastro_cpfcnpj'                                                    , 'abnfdx01' , ('codpfpj', 'idcpfpj')),
        ('abnf_cadastro_cpfcnpj'                                                    , 'abnfdx02' , ('nomraso', 'idcpfpj')),
        # /// #
        ('abnf_cadastro_funcionarios_cargos'                                        , 'abnfdx01' , ('codcarg', 'idcargo')),
        ('abnf_cadastro_funcionarios_cargos'                                        , 'abnfdx01' , ('descarg', 'idcargo')),
        ('abnf_cadastro_funcionarios'                                               , 'abnfdx02' , ('codfunc', 'idfunci')),
        # /// #
        ('abnf_cadastro_veiculos_marcas'                                            , 'abnfdx01' , ('codmarc', 'idmarca')),
        ('abnf_cadastro_veiculos_marcas'                                            , 'abnfdx01' , ('desmarc', 'idmarca')),
        ('abnf_cadastro_veiculos_modelos'                                           , 'abnfdx01' , ('codmode', 'idmodel')),
        ('abnf_cadastro_veiculos_modelos'                                           , 'abnfdx01' , ('desmode', 'idmarca', 'idmodel')),
        ('abnf_cadastro_veiculos'                                                   , 'abnfdx01' , ('prefvei', 'idveicu')),
        ('abnf_cadastro_veiculos'                                                   , 'abnfdx01' , ('placave', 'idveicu')),
        ('abnf_cadastro_veiculos_km'                                                , 'abnfdx01' , ('idveicu', 'dtregkm', 'kmveicu')),
        ('abnf_cadastro_veiculos_km'                                                , 'abnfdx02' , ('idveicu', 'kmveicu', 'dtregkm')),
        # /// #
        ('abnf_cadastro_clientes_fornecedores'                                      , 'abnfdx01' , ('tipclfo', 'codclfo', 'idclfor')),
        ('abnf_cadastro_especies_documentos'                                        , 'abnfdx01' , ('sigespd', 'desespd')),
        ('abnf_cadastro_especies_documentos'                                        , 'abnfdx02' , ('desespd', 'sigespd')),
        # /// #
        ('abnf_almoxarifado_cadastro_produtos_servicos_grupos'                      , 'abnfdx01' , ('codgrup', 'descgru', 'idgrupo')),
        ('abnf_almoxarifado_cadastro_produtos_servicos_grupos'                      , 'abnfdx02' , ('descgru', 'codgrup', 'idgrupo')),
        ('abnf_almoxarifado_cadastro_produtos_servicos_subgrupos'                   , 'abnfdx01' , ('codsubg', 'descsub', 'idsubgr')),
        ('abnf_almoxarifado_cadastro_produtos_servicos_subgrupos'                   , 'abnfdx02' , ('descsub', 'codsubg', 'idsubgr')),
        ('abnf_almoxarifado_cadastro_produtos_servicos_marcas'                      , 'abnfdx01' , ('codmarc', 'descmar', 'idmarca')),
        ('abnf_almoxarifado_cadastro_produtos_servicos_marcas'                      , 'abnfdx02' , ('descmar', 'codmarc', 'idmarca')),
        ('abnf_almoxarifado_cadastro_produtos_servicos'                             , 'abnfdx01' , ('codprse', 'descprs', 'idprser')),
        ('abnf_almoxarifado_cadastro_produtos_servicos'                             , 'abnfdx02' , ('descprs', 'codprse', 'idprser')),
        ('abnf_almoxarifado_cadastro_medidores_produtos'                            , 'abnfdx01' , ('codmedi', 'descmed', 'idmedid')),
        ('abnf_almoxarifado_cadastro_medidores_produtos'                            , 'abnfdx02' , ('descmed', 'codmedi', 'idmedid')),
        ('abnf_almoxarifado_movimentacao_produtos_servicos'                         , 'abnfdx01' , ('idclfor', 'nrdocnf', 'serienf', 'idespdo', 'tiporeg')),
        ('abnf_almoxarifado_movimentacao_produtos_servicos_itens'                   , 'abnfdx02' , ('idcmprs', 'datalan')),
        ('abnf_almoxarifado_movimentacao_medidores_produtos'                        , 'abnfdx01' , ('datamed', 'idmedid', 'idcmmed')),
        # /// #
        ('abnf_preventiva_cadastro_grupos'                                          , 'abnfdx01' , ('codgrpr', 'descgrp', 'idgrpre')),
        ('abnf_preventiva_cadastro_grupos'                                          , 'abnfdx02' , ('descgrp', 'codgrpr', 'idgrpre')),
        ('abnf_preventiva_cadastro_itens'                                           , 'abnfdx01' , ('coditpr', 'descitp', 'iditpre')),
        ('abnf_preventiva_cadastro_itens'                                           , 'abnfdx02' , ('descitp', 'coditpr', 'iditpre')),
        ('abnf_preventiva_cadastro_associacao_itens_grupos'                         , 'abnfdx01' , ('idgrpre', 'iditpre', 'idassig')),
        ('abnf_preventiva_cadastro_associacao_veiculos_grupos'                      , 'abnfdx01' , ('idgrpre', 'idveicu', 'idassvg')),
        ('abnf_preventiva_movimentacao_acao_preventiva'                             , 'abnfdx01' , ('datarea', 'idveicu', 'idacpre')),
        ('abnf_preventiva_movimentacao_acao_preventiva'                             , 'abnfdx02' , ('datarea', 'iditpre', 'idacpre')),
        # /// #
        ('abnf_financeiro_cadastro_contas'                                          , 'abnfdx01' , ('codcont', 'idconta')),
        ('abnf_financeiro_cadastro_contas'                                          , 'abnfdx02' , ('descban', 'descage', 'desccon', 'idconta')),
        ('abnf_financeiro_cadastro_grupos'                                          , 'abnfdx01' , ('codgrup', 'descgru', 'idgrupo')),
        ('abnf_financeiro_cadastro_grupos'                                          , 'abnfdx02' , ('descgru', 'codgrup', 'idgrupo')),
        ('abnf_financeiro_cadastro_subgrupos'                                       , 'abnfdx01' , ('codsubg', 'descsub', 'idsubgr')),
        ('abnf_financeiro_cadastro_subgrupos'                                       , 'abnfdx02' , ('descsub', 'codsubg', 'idsubgr')),
        ('abnf_financeiro_cadastro_complementos'                                    , 'abnfdx01' , ('codcomp', 'desccom', 'idcompl')),
        ('abnf_financeiro_cadastro_complementos'                                    , 'abnfdx02' , ('desccom', 'codcomp', 'idcompl')),
        ('abnf_financeiro_cadastro_centros_custo'                                   , 'abnfdx01' , ('codcecu', 'desccec', 'idcecus')),
        ('abnf_financeiro_cadastro_centros_custo'                                   , 'abnfdx02' , ('desccec', 'codcecu', 'idcecus')),
        ('abnf_financeiro_cadastro_departamentos'                                   , 'abnfdx01' , ('coddept', 'descdep', 'iddepto')),
        ('abnf_financeiro_cadastro_departamentos'                                   , 'abnfdx02' , ('descdep', 'coddept', 'iddepto')),
        ('abnf_financeiro_cadastro_contratos'                                       , 'abnfdx01' , ('codcont', 'desccon', 'idcontr')),
        ('abnf_financeiro_cadastro_contratos'                                       , 'abnfdx02' , ('desccon', 'codcont', 'idcontr')),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'abnfdx01' , ('ctrlfin', 'idregfi')),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'abnfdx02' , ('ctrlpgt', 'idregfi')),
        ('abnf_financeiro_movimentacao_registros_financeiros'                       , 'abnfdx03' , ('dataven', 'idregfi')),
        # /// #
        ('abnf_elevar_cadastro_passageiros'                                         , 'abnfdx01' , ('codepas', 'idepass')),
        ('abnf_elevar_cadastro_locais'                                              , 'abnfdx01' , ('codeloc', 'ideloca')),
        ('abnf_elevar_cadastro_locais'                                              , 'abnfdx02' , ('deseloc', 'ideloca')),
        ('abnf_elevar_cadastro_finalidades'                                         , 'abnfdx01' , ('codefin', 'idefina')),
        ('abnf_elevar_cadastro_finalidades'                                         , 'abnfdx02' , ('desefin', 'idefina')),
        ('abnf_elevar_cadastro_servicos'                                            , 'abnfdx01' , ('codeser', 'ideserv')),
        ('abnf_elevar_cadastro_frota_patrimonial'                                   , 'abnfdx01' , ('dataini', 'idefrpa')),
        ('abnf_elevar_cadastro_ordens_servico_padrao_grupos'                        , 'abnfdx01' , ('codegop', 'idegopa')),
        ('abnf_elevar_cadastro_ordens_servico_padrao_grupos'                        , 'abnfdx02' , ('desegru', 'idegopa')),
        ('abnf_elevar_cadastro_ordens_servico_padrao'                               , 'abnfdx01' , ('codeosp', 'ideospa')),
        ('abnf_elevar_cadastro_ordens_servico_padrao'                               , 'abnfdx02' , ('desemos', 'ideospa')),
        ('abnf_elevar_cadastro_ordens_servico_padrao_itens'                         , 'abnfdx01' , ('horario', 'ideitop')),
        ('abnf_elevar_movimentacao_ordens_servico_diaria'                           , 'abnfdx01' , ('numeosd', 'ideosdi')),
        ('abnf_elevar_movimentacao_ordens_servico_diaria'                           , 'abnfdx02' , ('dataord', 'numeosd', 'ideosdi')),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog'                , 'abnfdx01' , ('ideosdi', 'horario', 'ideitod')),
        ('abnf_elevar_movimentacao_ordens_servico_diaria_itens_real'                , 'abnfdx01' , ('ideosdi', 'horario', 'ideitod')),
        # /// #
        ('abnf_sac_cadastro_usuarios_grupos'                                        , 'abnfdx01' , ('codsusg', 'idsusgr')),
        ('abnf_sac_cadastro_usuarios_grupos'                                        , 'abnfdx02' , ('dessusg', 'idsusgr')),
        ('abnf_sac_cadastro_usuarios_grupos_vinculos'                               , 'abnfdx01' , ('idsusgr', 'idusuar', 'idsugvi')),
        ('abnf_sac_cadastro_atendimentos_canais'                                    , 'abnfdx01' , ('codsatc', 'idsatca')),
        ('abnf_sac_cadastro_atendimentos_canais'                                    , 'abnfdx02' , ('dessatc', 'idsatca')),
        ('abnf_sac_cadastro_atendimentos_tipos'                                     , 'abnfdx01' , ('codsatt', 'idsatti')),
        ('abnf_sac_cadastro_atendimentos_tipos'                                     , 'abnfdx02' , ('dessatt', 'idsatti')),
        ('abnf_sac_cadastro_atendimentos_grupos'                                    , 'abnfdx01' , ('codsatg', 'idsatgr')),
        ('abnf_sac_cadastro_atendimentos_grupos'                                    , 'abnfdx02' , ('dessatg', 'idsatgr')),
        ('abnf_sac_cadastro_atendimentos_subgrupos'                                 , 'abnfdx01' , ('codsats', 'idsatsg')),
        ('abnf_sac_cadastro_atendimentos_subgrupos'                                 , 'abnfdx02' , ('dessats', 'idsatsg')),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'abnfdx01' , ('codsate', 'idsaten')),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'abnfdx02' , ('dataabe', 'horaabe', 'idsaten')),
        ('abnf_sac_movimentacao_atendimentos'                                       , 'abnfdx03' , ('dataoco', 'horaoco', 'idsaten')),
        ('abnf_sac_movimentacao_atendimentos_complementos'                          , 'abnfdx01' , ('datacom', 'horacom', 'idsatco')),
        ('abnf_sac_movimentacao_atendimentos_arquivos'                              , 'abnfdx01' , ('idsaten', 'idsatco', 'idsatar')),
        # /// #
        ('abnf_operacional_cadastro_locais'                                         , 'abnfdx01' , ('codoloc', 'idoloca')),
        ('abnf_operacional_cadastro_locais'                                         , 'abnfdx02' , ('desoloc', 'idoloca')),
        ('abnf_operacional_cadastro_grupos_linhas'                                  , 'abnfdx01' , ('codogrl', 'idogrli')),
        ('abnf_operacional_cadastro_grupos_linhas'                                  , 'abnfdx02' , ('desogrl', 'idogrli')),
        ('abnf_operacional_cadastro_linhas'                                         , 'abnfdx01' , ('codolin', 'idolinh')),
        ('abnf_operacional_cadastro_linhas'                                         , 'abnfdx02' , ('desolin', 'idolinh')),
        ('abnf_operacional_cadastro_projetos'                                       , 'abnfdx01' , ('codopro', 'idoproj')),
        ('abnf_operacional_cadastro_projetos'                                       , 'abnfdx02' , ('desopro', 'idoproj')),
        ('abnf_operacional_cadastro_trajetos'                                       , 'abnfdx01' , ('idoproj', 'idolinh', 'codotra')),
        ('abnf_operacional_cadastro_itinerarios'                                    , 'abnfdx01' , ('idotraj', 'sentido', 'ordemit', 'idoitin')),
        ('abnf_operacional_cadastro_grupos_veiculos'                                , 'abnfdx01' , ('codogrf', 'descgrf', 'idogrve')),
        ('abnf_operacional_cadastro_grupos_veiculos'                                , 'abnfdx01' , ('descgrf', 'codogrf', 'idogrve')),
        ('abnf_operacional_cadastro_grupos_veiculos_vinculos'                       , 'abnfdx01' , ('idogrve', 'idveicu', 'idogrvv')),
        ('abnf_operacional_cadastro_prioridades_linhas'                             , 'abnfdx01',  ('ordprio', 'idoplin')),
        ('abnf_operacional_cadastro_prioridades_linhas_gv'                          , 'abnfdx01',  ('idoplin', 'ordprio', 'idoplgv')),
        ('abnf_operacional_cadastro_operacoes_especiais'                            , 'abnfdx01',  ('dataope', 'idolinh', 'veicser', 'idooesp')),
        ('abnf_operacional_cadastro_setor_veiculos'                                 , 'abnfdx01' , ('codoset', 'idosetv')),
        ('abnf_operacional_cadastro_setor_veiculos'                                 , 'abnfdx02' , ('descset', 'idosetv')),
        ('abnf_operacional_cadastro_motivo_substituicao'                            , 'abnfdx01' , ('codomsu', 'idomsub')),
        ('abnf_operacional_cadastro_motivo_substituicao'                            , 'abnfdx02' , ('descmsu', 'idomsub')),
        ('abnf_operacional_cadastro_grupos_usuarios'                                , 'abnfdx01' , ('codcusg', 'idcusgr')),
        ('abnf_operacional_cadastro_grupos_usuarios'                                , 'abnfdx02' , ('descusg', 'idcusgr')),
        ('abnf_operacional_cadastro_grupos_usuarios_vinculos'                       , 'abnfdx01' , ('idsusgr', 'idusuar', 'idcugvi')),
        ('abnf_operacional_movimentacao_propostas_oso'                              , 'abnfdx01' , ('codopos', 'idoprop')),
        ('abnf_operacional_movimentacao_propostas_oso_viagens'                      , 'abnfdx01' , ('idoprop', 'numrele', 'seghini', 'veicpro', 'idopvia')),
        ('abnf_operacional_movimentacao_oficial_oso'                                , 'abnfdx01' , ('numeoso', 'idoosoo')),
        ('abnf_operacional_movimentacao_oficial_oso_viagens'                        , 'abnfdx01' , ('idoosoo', 'seghini', 'veicpro', 'idoovia')),
        ('abnf_operacional_movimentacao_oficial_oso_trajetos'                       , 'abnfdx01' , ('idoosoo', 'codotra')),
        ('abnf_operacional_movimentacao_oficial_oso_itinerarios'                    , 'abnfdx01' , ('idootra', 'sentido', 'ordemit', 'idooiti')),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'abnfdx01',  ('dataope', 'idolinh', 'veicpro', 'dtregcr')),
        ('abnf_operacional_movimentacao_programacao_diario'                         , 'abnfdx02',  ('dataope', 'idveicu', 'dtregcr')),
        ('abnf_operacional_movimentacao_programacao_automacao'                      , 'abnfdx01',  ('dtmetod')),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'abnfdx01',  ('codctrl', 'idoprrv')),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'abnfdx02',  ('idveicu', 'idoprrv')),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'abnfdx03',  ('dtreten', 'idoprrv')),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'abnfdx04',  ('dtliber', 'idoprrv')),
        ('abnf_operacional_movimentacao_programacao_retencao_veiculos'              , 'abnfdx05',  ('dataage', 'seghage', 'idoprrv')),
        ('abnf_operacional_entrada_saida_veiculos_locais'                           , 'abnfdx01',  ('codoesl', 'idoesvl')),
        ('abnf_operacional_entrada_saida_veiculos_locais'                           , 'abnfdx02',  ('desoesl', 'idoesvl')),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'abnfdx01',  ('idveicu', 'dataesv', 'horaesv')),
        ('abnf_operacional_entrada_saida_veiculos'                                  , 'abnfdx02',  ('dataesv', 'horaesv', 'idveicu')),
        ('abnf_operacional_entrada_saida_veiculos_check_list_padrao'                , 'abnfdx01',  ('codoclp', 'idoclpa')),
        ('abnf_operacional_entrada_saida_veiculos_check_list_padrao'                , 'abnfdx02',  ('desoclp', 'idoclpa')),
        ('abnf_operacional_entrada_saida_veiculos_check_list'                       , 'abnfdx01',  ('idoclpa', 'idochli')),
        ('abnf_operacional_entrada_saida_veiculos_check_list'                       , 'abnfdx02',  ('idoesve', 'idochli')),
        # /// #        
        ('abnf_sigom_cadastro_usuarios_grupos'                                      , 'abnfdx01' , ('codsusg', 'idsusgr')),
        ('abnf_sigom_cadastro_usuarios_grupos'                                      , 'abnfdx02' , ('dessusg', 'idsusgr')),
        ('abnf_sigom_cadastro_usuarios_grupos_vinculos'                             , 'abnfdx01' , ('idsusgr', 'idusuar', 'idsugvi')),
        ('abnf_sigom_cadastro_ocorrencias_tipos'                                    , 'abnfdx01' , ('codsoct', 'idsocti')),
        ('abnf_sigom_cadastro_ocorrencias_tipos'                                    , 'abnfdx02' , ('dessoct', 'idsocti')),
        ('abnf_sigom_cadastro_veiculos_situacao'                                    , 'abnfdx01' , ('codsves', 'idsvesi')),
        ('abnf_sigom_cadastro_veiculos_situacao'                                    , 'abnfdx02' , ('dessves', 'idsvesi')),
        ('abnf_sigom_cadastro_classificacao'                                        , 'abnfdx01' , ('codscla', 'idsclas')),
        ('abnf_sigom_cadastro_classificacao'                                        , 'abnfdx02' , ('desscla', 'idsclas')),
        ('abnf_sigom_cadastro_defeitos_grupos'                                      , 'abnfdx01',  ('codsdeg', 'idsdegr')),
        ('abnf_sigom_cadastro_defeitos_grupos'                                      , 'abnfdx02',  ('dessdeg', 'idsdegr')),
        ('abnf_sigom_cadastro_defeitos_subgrupos'                                   , 'abnfdx01',  ('codsdes', 'idsdesg')),
        ('abnf_sigom_cadastro_defeitos_subgrupos'                                   , 'abnfdx02',  ('dessdes', 'idsdesg')),
        ('abnf_sigom_cadastro_defeitos_definicoes'                                  , 'abnfdx01',  ('codsded', 'idsdede')),
        ('abnf_sigom_cadastro_defeitos_definicoes'                                  , 'abnfdx02',  ('dessded', 'idsdede')),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'abnfdx01' , ('codsoco', 'idsocor')),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'abnfdx02' , ('dataabe', 'horaabe', 'idsocor')),
        ('abnf_sigom_movimentacao_ocorrencias'                                      , 'abnfdx03' , ('dataoco', 'horaoco', 'idsocor')),
        ('abnf_sigom_movimentacao_ocorrencias_complementos'                         , 'abnfdx01' , ('datacom', 'horacom', 'idsocco')),
        ('abnf_sigom_movimentacao_ocorrencias_arquivos'                             , 'abnfdx01' , ('idsocor', 'idsocco', 'idsocar')),        
        # (Mudança de planos: usar informações fixas no lugar de tabela) ==> ('abnf_operacional_cadastro_tipos_viagem'                           , 'abnfdx01' , ('codotiv', 'idotivi')),
        # (Mudança de planos: usar informações fixas no lugar de tabela) ==> ('abnf_operacional_cadastro_tipos_viagem'                           , 'abnfdx02' , ('desotiv', 'idotivi')),
        # /// #
    ]
    return ldbtabel, ldbstruc
    # áàäâã-éèëê-íìïî-óòöôõ-úùüû-çñ

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_database_estrutura_converte_campos ] ////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que converte o valor do campo (se necessário) para poder ser inserido dentro da tabela.                                                      // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_database_estrutura_converte_campos(stabelax, scamposb, sauxvalc):
    svalcamp = ''
    if sauxvalc == None:
        svalcamp = 'NULL'
    else:
        ldbtabel, ldbstruc = abnf_database_estrutura()
        for lauxi001 in ldbstruc:
            # abnf_show('09', lauxi001, 1)
            if lauxi001[0] == stabelax and lauxi001[1] == scamposb:
                if lauxi001[2] in ['varchar', 'text']:
                    svalcamp = '"' + str(sauxvalc) + '"'
                elif lauxi001[2] in ['date', 'time', 'datetime']:
                    if sauxvalc == '':
                        svalcamp = 'NULL'
                    elif sauxvalc == 'CURRENT_TIMESTAMP':
                        svalcamp = 'CURRENT_TIMESTAMP()'
                    else:
                        svalcamp = '"' + str(sauxvalc) + '"'
                else:
                    svalcamp = str(sauxvalc)
                break
    return svalcamp

'''
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░          ░░  ░░          ░░          ░░          ░░   ░░░░   ░░          ░░
░░  ░░░░░░░░░░  ░░  ░░░░░░░░░░░░░░  ░░░░░░  ░░░░░░░░░░    ░░    ░░  ░░░░░░  ░░
▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒    ▒  ▒▒  ▒▒▒▒▒▒  ▒▒
▒▒          ▒▒  ▒▒          ▒▒▒▒▒▒  ▒▒▒▒▒▒          ▒▒  ▒▒  ▒▒  ▒▒          ▒▒
▒▒▒▒▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒
██████████  ██  ██████████  ██████  ██████  ██████████  ██████  ██  ██████  ██
██          ██  ██          ██████  ██████          ██  ██████  ██  ██████  ██
██████████████████████████████████████████████████████████████████████████████
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ TABLE abnf_sistema_empresas_matrizes ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sistema_empresas_matrizes (
    idempre     INT                     PRIMARY KEY         NOT NULL                            ,   # ID da empresa
    codiemp     INT                                         NOT NULL                            ,   # Código da empresa
    nomeemp     VARCHAR(100)                                NOT NULL                            ,   # Nome da empresa
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (codiemp, idempre),
    INDEX abnfdx02 (nomeemp, idempre)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sistema_empresas_matrizes (codiemp, idempre);
CREATE INDEX abnfdx02 ON abnf_sistema_empresas_matrizes (nomeemp, idempre);
---------------------------------------------
SHOW COLUMNS FROM abnf_sistema_empresas_matrizes;
SHOW INDEX FROM abnf_sistema_empresas_matrizes;
SELECT * FROM abnf_sistema_empresas_matrizes;
DROP *** TABLE abnf_sistema_empresas_matrizes;
---------------------------------------------
INSERT *** INTO abnf_sistema_empresas_matrizes (idempre, codiemp, nomeemp, situreg, idusucr, dtregcr) VALUES
(?, ?, ???, "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
UPDATE *** abnf_sistema_empresas_matrizes SET nomeemp = 'RAPIDO SUMARE LTDA.', situreg = 'A' where idempre = 2;
---------------------------------------------
UPDATE *** abnf_sistema_empresas_matrizes SET situreg = "A" where idempre = 2;
---------------------------------------------
DELETE *** FROM abnf_sistema_empresas_matrizes WHERE idempre = 2;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ TABLE abnf_sistema_empresas_filiais ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sistema_empresas_filiais (
    idfilia     INT                     PRIMARY KEY         NOT NULL                            ,   # ID da filial
    idempre     INT                                         NOT NULL                            ,   # ID da empresa (FK)
    codifil     INT                                         NOT NULL                            ,   # Código da filial
    nomefil     VARCHAR(100)                                NOT NULL                            ,   # Nome da filial
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (codifil, idfilia),
    INDEX abnfdx02 (nomefil, idfilia)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sistema_empresas_filiais (codifil, idfilia);
CREATE INDEX abnfdx02 ON abnf_sistema_empresas_filiais (nomefil, idfilia);
---------------------------------------------
SHOW COLUMNS FROM abnf_sistema_empresas_filiais;
SHOW INDEX FROM abnf_sistema_empresas_filiais;
SELECT * FROM abnf_sistema_empresas_filiais;
DROP *** TABLE abnf_sistema_empresas_filiais;
---------------------------------------------
INSERT *** INTO abnf_sistema_empresas_filiais (idfilia, idempre, codifil, nomefil, situreg, idusucr, dtregcr) VALUES
(?, ?, ??, "???", "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
DELETE *** FROM abnf_sistema_empresas_filiais WHERE idfilia = 3;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ TABLE abnf_sistema_usuarios ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
--------------------------------------------
CREATE TABLE abnf_sistema_usuarios (
    idusuar     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do usuário
    logiusu     VARCHAR(30)                                 NOT NULL                            ,   # Login do usuário
    senhusu     VARCHAR(200)                                NOT NULL                            ,   # Senha do usuário
    tipousu     VARCHAR(1)                                  NOT NULL                            ,   # Tipo de usuário: [A]dministrativo/[O]peracional
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    dthrini     DATETIME                                    NOT NULL                            ,   # Data hora inicial (a partir de quando o usuário pode usar o sistema)
    dtrhfim     DATETIME                                                                        ,   # Data hora final (até quando o usuário pode usar o sistema)
    nomeusu     VARCHAR(100)                                NOT NULL                            ,   # Nome completo do usuário
    emaiusu     VARCHAR(100)                                                                    ,   # E-mail do usuário
    idfotop     INT                                                                             ,   # ID da foto do perfil (FK)
    idgrams     INT                                                                             ,   # ID do grupo de acessos dos modulos do sistema (FK)
    INDEX abnfdx01 (logiusu, idusuar),
    INDEX abnfdx02 (nomeusu, idusuar),
    INDEX abnfdx03 (emaiusu, idusuar)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sistema_usuarios (logiusu, idusuar);
CREATE INDEX abnfdx02 ON abnf_sistema_usuarios (nomeusu, idusuar);
CREATE INDEX abnfdx03 ON abnf_sistema_usuarios (emaiusu, idusuar);
---------------------------------------------
SHOW COLUMNS FROM abnf_sistema_usuarios;
SHOW INDEX FROM abnf_sistema_usuarios;
DROP *** TABLE abnf_sistema_usuarios;
---------------------------------------------
SELECT * FROM abnf_sistema_usuarios;
---------------------------------------------
SELECT
abnf01.nomeusu,
abnf01.logiusu,
abnf01.senhusu,
abnf01.idusuar,
abnf01.situreg,
abnf01.idgrams,
abnf02.desgrup
FROM       abnf_sistema_usuarios       as abnf01
INNER JOIN abnf_sistema_modulos_grupos as abnf02
ON         abnf01.idgrams = abnf02.idgrams
WHERE
-- abnf01.logiusu = "EA.MOREIRA"
abnf01.nomeusu LIKE '%MARIA%'
-- OR abnf01.nomeusu LIKE '%ESTEFA%'
-- idusuar = 23
-- idusuar IN (16, 57, 83)
-- idusuar >= 85
-- abnf01.idgrams = 5
-- abnf01.situreg = 'A'
-- abnf01.situreg = 'I'
-- abnf01.situreg = 'C'
-- AND abnf01.senhusu = 'MUDAR@123'
ORDER BY
-- abnf01.idusuar;
abnf01.logiusu;
--------------------------------------------
Inserir usuário (*** principal ***)
INSERT INTO abnf_sistema_usuarios (idusuar, logiusu, senhusu, tipousu, situreg, idusucr, dtregcr, dthrini, nomeusu, idgrams) VALUES
(96, "LRF.MARQUES" , "MUDAR@123", "O", "A", 1, CURRENT_TIMESTAMP(), "2025-01-01 00:00:00", "LAURA RODRIGUES FISCHER MARQUES", 1);
---------------------------------------------
UPDATE abnf_sistema_usuarios SET senhusu = "MUDAR@123" WHERE idusuar = 92;
UPDATE *** abnf_sistema_usuarios SET situreg = "A" WHERE idusuar IN (83);
UPDATE *** abnf_sistema_usuarios SET idgrams = 4 WHERE idusuar = 96;
---------------------------------------------
http://189.44.98.122:8900/abnf000t00h00100
http://190.89.248.19:8005/transacreana
---------------------------------------------
Segue dados para acesso dos novos usuarios:

LAURA RODRIGUES FISCHER MARQUES

Link:

http://189.44.98.122:8900/abnf000t00h00100

Usuario
LRF.MARQUES

Senha provisória:
MUDAR@123

Assim que ela entrar, tem que fazer os 3 processos de personalização
---------------------------------------------
Segue dados para acesso do novo usuario:
MARIA CHIRLE ROCHA DAS CHAGAS

Link:
http://189.44.98.122:8900/abnf000t00h00100

Usuario
MCR.CHAGAS

Senha provisória:
MUDAR@123

Assim que ela entrar, tem que fazer os 3 processos de personalização
---------------------------------------------
Segue dados para acesso do novo usuario:
ALINE MARIA DA SILVA MARQUES VIAMONTE

Link:
http://189.44.98.122:8901/abnf000t00h00200

Usuario
AMSM.VIAMONTE

Senha provisória:
MUDAR@123

Assim que ela entrar, tem que fazer os 3 processos de personalização
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_sistema_arquivos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sistema_arquivos (
    idarqui     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do arquivo
    nomearq     VARCHAR(200)                                NOT NULL                            ,   # Nome do arquivo
    extearq     VARCHAR(20)                                 NOT NULL                            ,   # Extensão do arquivo
    pastarq     VARCHAR(200)                                NOT NULL                            ,   # Pasta do arquivo
    nomeori     VARCHAR(200)                                                                    ,   # Nome original do arquivo (upload)
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                            # Data/hora de alteração/exclusão do registro
);
---------------------------------------------
SHOW COLUMNS FROM abnf_sistema_arquivos;
SHOW INDEX FROM abnf_sistema_arquivos;
SELECT * FROM abnf_sistema_arquivos;
DROP *** TABLE abnf_sistema_arquivos;
---------------------------------------------
DELETE *** FROM abnf_sistema_arquivos WHERE idarqui > 0;
---------------------------------------------
ALTER *** TABLE abnf_sistema_arquivos ADD COLUMN nomeori VARCHAR(200) AFTER pastarq;
---------------------------------------------
UPDATE *** abnf_sistema_arquivos SET nomeori = 'TESTANDO O ARQUIVO DE IMAGEM FEITO UPLOAD.JPG' WHERE idarqui = 26;
UPDATE *** abnf_sistema_arquivos SET nomeori = 'PRIMEIRO ARQUIVO PDF QUE FOI IMPORTANDO.PDF' WHERE idarqui = 27;
UPDATE *** abnf_sistema_arquivos SET nomeori = 'TESTANDO A PLANILHA 123.XLS' WHERE idarqui = 28;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_sistema_modulos_grupos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sistema_modulos_grupos (
    idgrams     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do grupo de acessos dos modulos do sistema
    codgrup     INT                                         NOT NULL                            ,   # Código do grupo
    desgrup     VARCHAR(100)                                NOT NULL                            ,   # Descrição do grupo
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (codgrup, idgrams),
    INDEX abnfdx02 (desgrup, idgrams)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sistema_modulos_grupos (codgrup, idgrams);
CREATE INDEX abnfdx02 ON abnf_sistema_modulos_grupos (desgrup, idgrams);
---------------------------------------------
SHOW COLUMNS FROM abnf_sistema_modulos_grupos;
SHOW INDEX FROM abnf_sistema_modulos_grupos;
DROP *** TABLE abnf_sistema_modulos_grupos;
SELECT * FROM abnf_sistema_modulos_grupos;
---------------------------------------------
INSERT *** INTO abnf_sistema_modulos_grupos (idgrams, codgrup, desgrup, situreg, idusucr, dtregcr) VALUES
(15, 24, 'CONTROLE DIARIO', "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
UPDATE *** abnf_sistema_modulos_grupos SET desgrup = 'CCO' WHERE idgrams = 3;
UPDATE *** abnf_sistema_modulos_grupos SET desgrup = 'SAC & SIGOM' WHERE idgrams = 5;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_sistema_modulos_acessos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sistema_modulos_acessos (
    idmodac     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do registro de acesso ao módulo
    idgrams     INT                                         NOT NULL                            ,   # ID do grupo de acessos dos modulos do sistema (FK)
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    codmodu     VARCHAR(9)                                  NOT NULL                            ,   # Código do módulo
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (idgrams, idfilia, codmodu, idmodac)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sistema_modulos_acessos (idgrams, idfilia, codmodu, idmodac);
---------------------------------------------
SHOW COLUMNS FROM abnf_sistema_modulos_acessos;
SHOW INDEX FROM abnf_sistema_modulos_acessos;
DROP *** TABLE abnf_sistema_modulos_acessos;
---------------------------------------------
Relação de acessos (*** principal ***)
SELECT * FROM abnf_sistema_modulos_acessos;
SELECT * FROM abnf_sistema_modulos_grupos;
SELECT * INTO OUTFILE '/tmp/resultado_sql.txt' FROM abnf_sistema_modulos_acessos;
SELECT * FROM abnf_sistema_modulos_acessos WHERE codmodu LIKE '%13M001%'; and idfilia = 1 and idgrams = 1 order by codmodu;
SELECT * FROM abnf_sistema_modulos_acessos WHERE codmodu = '04R00104A'; or codmodu = '13M00104A';
SELECT * FROM abnf_sistema_modulos_acessos WHERE idmodac = 677 or idmodac = 678 ORDER by codmodu;
SELECT * FROM abnf_sistema_modulos_acessos WHERE idgrams = 5 order by codmodu;
SELECT * from abnf_sistema_modulos_grupos;
SELECT idusuar, logiusu, nomeusu, situreg, idgrams FROM abnf_sistema_usuarios WHERE idgrams = 5;
SELECT * FROM abnf_sistema_modulos_acessos WHERE idgrams = 5 ORDER by codmodu;
SELECT * FROM abnf_sistema_modulos_acessos as tb01 INNER JOIN abnf_sistema_modulos_grupos as tb02 WHERE tb01.codmodu in ('14M00100A', '14R00100A', '14R00200A') and tb01.idgrams = tb02.idgrams;
---------------------------------------------
DELETE *** FROM abnf_sistema_modulos_acessos WHERE codmodu = '04M00600A';
SELECT * FROM abnf_sistema_modulos_acessos WHERE codmodu in ('01C00600A', '01C00600B', '01C00100A', '01C00400A', '01C00500A');
UPDATE *** abnf_sistema_modulos_acessos SET codmodu = '04M00600A' WHERE codmodu = '04M01000A';
SELECT * FROM abnf_sistema_modulos_acessos WHERE codmodu = '04M00600A';
UPDATE *** abnf_sistema_modulos_acessos SET situreg = 'C' where codmodu = '04M00600A' and idgrams != 1;
---------------------------------------------
INSERT *** INTO abnf_sistema_modulos_acessos (idmodac, idgrams, idfilia, codmodu, situreg, idusucr, dtregcr) VALUES
(1645, 15, 3, "13M02100A", "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
*** alexandre ***
SELECT

abnf01.idusuar,
abnf01.nomeusu,
abnf01.logiusu,
abnf02.idgrams,
abnf02.desgrup,
abnf03.codmodu,
abnf03.idmodac,
abnf01.situreg,
abnf02.situreg,
abnf03.situreg

FROM       abnf_sistema_usuarios              AS abnf01
INNER JOIN abnf_sistema_modulos_grupos        AS abnf02
ON         abnf01.idgrams = abnf02.idgrams
INNER JOIN abnf_sistema_modulos_acessos       AS abnf03
ON         abnf02.idgrams = abnf03.idgrams

WHERE abnf01.situreg != "C"
-- AND abnf01.nomeusu LIKE '%ALEX%'
AND abnf03.codmodu LIKE '%13M00100A%'
-- AND abnf02.desgrup LIKE '%PORTA%'
-- AND abnf03.idmodac IN (1580, 1581)

ORDER BY abnf01.nomeusu, abnf03.codmodu;
---------------------------------------------
*** descarte ***
SELECT

abnf02.idgrams,
abnf02.desgrup,
abnf03.codmodu,
abnf03.idmodac,
abnf02.situreg,
abnf03.situreg

FROM       abnf_sistema_modulos_grupos        AS abnf02
INNER JOIN abnf_sistema_modulos_acessos       AS abnf03
ON         abnf02.idgrams = abnf03.idgrams

WHERE abnf03.codmodu LIKE '%13M00100A%' or abnf03.codmodu LIKE '%13M03000A%'

ORDER BY abnf02.desgrup, abnf03.codmodu;
---------------------------------------------
*** descarte ***
UPDATE *** abnf_sistema_modulos_acessos SET codmodu = '13M03000A' WHERE idmodac IN (1580, 1581, 1404);
---------------------------------------------
*** descarte ***
SELECT

abnf02.idgrams,
abnf02.desgrup,
abnf03.codmodu,
abnf03.idmodac,
abnf02.situreg,
abnf03.situreg

FROM       abnf_sistema_modulos_grupos        AS abnf02
INNER JOIN abnf_sistema_modulos_acessos       AS abnf03
ON         abnf02.idgrams = abnf03.idgrams

WHERE abnf03.codmodu LIKE '%13R00100A%' or abnf03.codmodu LIKE '%13R03000A%'

ORDER BY abnf02.desgrup, abnf03.codmodu;
---------------------------------------------
*** descarte ***
UPDATE *** abnf_sistema_modulos_acessos SET codmodu = '13R03000A' WHERE codmodu = '13R00100A';
---------------------------------------------
*** descarte ***
SELECT

abnf02.idgrams,
abnf02.desgrup,
abnf03.codmodu,
abnf03.idmodac,
abnf02.situreg,
abnf03.situreg

FROM       abnf_sistema_modulos_grupos        AS abnf02
INNER JOIN abnf_sistema_modulos_acessos       AS abnf03
ON         abnf02.idgrams = abnf03.idgrams

WHERE abnf03.codmodu LIKE '%13R03000A%' 
-- AND abnf02.desgrup LIKE '%PORTA%'

ORDER BY abnf02.desgrup, abnf03.codmodu;
---------------------------------------------

# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░          ░░          ░░        ░░░░          ░░          ░░          ░░          ░░          ░░          ░░
░░  ░░░░░░░░░░  ░░░░░░  ░░  ░░░░░░  ░░  ░░░░░░  ░░  ░░░░░░░░░░░░░░  ░░░░░░  ░░░░░░  ░░  ░░░░░░  ░░  ░░░░░░░░░░
▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒
▒▒  ▒▒▒▒▒▒▒▒▒▒          ▒▒  ▒▒▒▒▒▒  ▒▒          ▒▒          ▒▒▒▒▒▒  ▒▒▒▒▒▒          ▒▒  ▒▒▒▒▒▒  ▒▒          ▒▒
▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒▒     ▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒
██  ██████████  ██████  ██  ██████  ██  ██████  ██████████  ██████  ██████  ██    ████  ██████  ██████████  ██
██          ██  ██████  ██        ████  ██████  ██          ██████  ██████  ████    ██          ██          ██
██████████████████████████████████████████████████████████████████████████████████████████████████████████████
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_cadastro_logradouros_cidades ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_cadastro_logradouros_cidades (
    idcidad     INT                     PRIMARY KEY         NOT NULL                            ,   # ID da cidade
    codcida     INT                                         NOT NULL                            ,   # Código da cidade
    descida     VARCHAR(100)                                NOT NULL                            ,   # Descrição da cidade
    desesta     VARCHAR(2)                                  NOT NULL                            ,   # Descrição do estado
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (codcida, idcidad),
    INDEX abnfdx02 (descida, desesta, idcidad)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_cadastro_logradouros_cidades (codcida, idcidad);
CREATE INDEX abnfdx02 ON abnf_cadastro_logradouros_cidades (descida, desesta, idcidad);
---------------------------------------------
DROP *** TABLE abnf_cadastro_logradouros_cidades;
DROP *** INDEX abnfdx?? ON abnf_cadastro_logradouros_cidades;
---------------------------------------------
SHOW COLUMNS FROM abnf_cadastro_logradouros_cidades;
SHOW INDEX FROM abnf_cadastro_logradouros_cidades;
---------------------------------------------
SELECT * FROM abnf_cadastro_logradouros_cidades;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_cadastro_logradouros_bairros ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_cadastro_logradouros_bairros (
    idbairr     INT                     PRIMARY KEY         NOT NULL                            ,   # ID cadastro bairros
    codbair     INT                                         NOT NULL                            ,   # Código do bairro
    desbair     VARCHAR(100)                                NOT NULL                            ,   # Descrição do bairro
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idcidad     INT                                         NOT NULL                            ,   # ID cadastro cidade (FK)
    INDEX abnfdx01 (codbair, idbairr),
    INDEX abnfdx02 (desbair, idcidad, idbairr)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_cadastro_logradouros_bairros (codbair, idbairr);
CREATE INDEX abnfdx02 ON abnf_cadastro_logradouros_bairros (desbair, idcidad, idbairr);
---------------------------------------------
DROP *** TABLE abnf_cadastro_logradouros_bairros;
DROP *** INDEX abnfdx?? ON abnf_cadastro_logradouros_bairros;
---------------------------------------------
SHOW COLUMNS FROM abnf_cadastro_logradouros_bairros;
SHOW INDEX FROM abnf_cadastro_logradouros_bairros;
---------------------------------------------
SELECT * FROM abnf_cadastro_logradouros_bairros;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_cadastro_logradouros ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_cadastro_logradouros (
    idlogra     INT                     PRIMARY KEY         NOT NULL                            ,   # ID cadastro logradouros
    codlogr     INT                                         NOT NULL                            ,   # Código do logradouro
    tiplogr     VARCHAR(50)                                 NOT NULL                            ,   # Tipo de logradouro
    deslogr     VARCHAR(200)                                NOT NULL                            ,   # Descrição do logradouro
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idbairr     INT                                         NOT NULL                            ,   # ID do bairro (FK)
    INDEX abnfdx01 (codlogr, idlogra),
    INDEX abnfdx02 (deslogr, idbairr, idlogra),
    INDEX abnfdx03 (tiplogr, deslogr, idbairr, idlogra)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_cadastro_logradouros (codlogr, idlogra);
CREATE INDEX abnfdx02 ON abnf_cadastro_logradouros (deslogr, idbairr, idlogra);
CREATE INDEX abnfdx03 ON abnf_cadastro_logradouros (tiplogr, deslogr, idbairr, idlogra);
---------------------------------------------
DROP *** TABLE abnf_cadastro_logradouros;
DROP *** INDEX abnfdx?? ON abnf_cadastro_logradouros;
---------------------------------------------
SHOW COLUMNS FROM abnf_cadastro_logradouros;
SHOW INDEX FROM abnf_cadastro_logradouros;
---------------------------------------------
SELECT * FROM abnf_cadastro_logradouros WHERE idlogra = 4;
UPDATE abnf_cadastro_logradouros SET situreg = 'A' WHERE idlogra = 41;
---------------------------------------------
ALTER *** TABLE abnf_cadastro_logradouros CHANGE deslogr deslogr VARCHAR(200) NOT NULL;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_cadastro_cpfcnpj ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_cadastro_cpfcnpj (
    idcpfpj     INT                     PRIMARY KEY         NOT NULL                            ,   # ID cadastro CPF/CNPJ
    codpfpj     VARCHAR(20)                                 NOT NULL                            ,   # Código do PF/PJ
    tippfpj     VARCHAR(1)                                  NOT NULL                            ,   # Tipo: F = Física / J = Jurídica
    nomraso     VARCHAR(100)                                NOT NULL                            ,   # Nome / Razão social
    nomfant     VARCHAR(100)                                                                    ,   # Nome fantasia
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfotof     INT                                                                             ,   # ID da foto (Pessoa física) (FK)
    idlogra     INT                                         NOT NULL                            ,   # ID do logradouro (FK)
    logrnum     VARCHAR(20)                                 NOT NULL                            ,   # Logradouro - Número
    logrcom     VARCHAR(100)                                                                    ,   # Logradouro - Complemento
    logrcep     VARCHAR(10)                                                                     ,   # Logradouro - CEP
    sexoxxx     VARCHAR(1)                                                                      ,   # Sexo (M/F)
    rgiexxx     VARCHAR(20)                                                                     ,   # RG/IE
    cnhxxxx     VARCHAR(20)                                                                     ,   # CNH
    inscmun     VARCHAR(20)                                                                     ,   # Inscrição municipal
    titenum     VARCHAR(20)                                                                     ,   # Titulo de eleitor - Número
    titezon     VARCHAR(10)                                                                     ,   # Titulo de eleitor - Zona
    titesec     VARCHAR(10)                                                                     ,   # Titulo de eleitor - Seção
    certres     VARCHAR(20)                                                                     ,   # Certificado de reservista
    datanas     DATE                                                                            ,   # Data de nascimento
    datacas     DATE                                                                            ,   # Data de casamento
    datafal     DATE                                                                            ,   # Data de falecimento
    nomepai     VARCHAR(100)                                                                    ,   # Nome pai
    nomemae     VARCHAR(100)                                                                    ,   # Nome mãe
    nomecon     VARCHAR(100)                                                                    ,   # Nome conjuge
    telef01     VARCHAR(20)                                                                     ,   # Telefone 01
    telef02     VARCHAR(20)                                                                     ,   # Telefone 02
    telef03     VARCHAR(20)                                                                     ,   # Telefone 03
    telef04     VARCHAR(20)                                                                     ,   # Telefone 04
    telef05     VARCHAR(20)                                                                     ,   # Telefone 05
    email01     VARCHAR(100)                                                                    ,   # E-mail 01
    email02     VARCHAR(100)                                                                    ,   # E-mail 02
    email03     VARCHAR(100)                                                                    ,   # E-mail 03
    email04     VARCHAR(100)                                                                    ,   # E-mail 04
    email05     VARCHAR(100)                                                                    ,   # E-mail 05
    hpage01     VARCHAR(100)                                                                    ,   # Home page 01
    hpage02     VARCHAR(100)                                                                    ,   # Home page 02
    hpage03     VARCHAR(100)                                                                    ,   # Home page 03
    hpage04     VARCHAR(100)                                                                    ,   # Home page 04
    hpage05     VARCHAR(100)                                                                    ,   # Home page 05
    observa     TEXT                                                                            ,   # Observação
    INDEX abnfdx01 (codpfpj, idcpfpj),
    INDEX abnfdx02 (nomraso, idcpfpj)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_cadastro_cpfcnpj (codpfpj, idcpfpj);
CREATE INDEX abnfdx02 ON abnf_cadastro_cpfcnpj (nomraso, idcpfpj);
---------------------------------------------
DROP *** TABLE abnf_cadastro_cpfcnpj;
DROP *** INDEX abnfdx?? ON abnf_cadastro_cpfcnpj;
---------------------------------------------
SHOW COLUMNS FROM abnf_cadastro_cpfcnpj;
SHOW INDEX FROM abnf_cadastro_cpfcnpj;
---------------------------------------------
SELECT * FROM abnf_cadastro_cpfcnpj;
SELECT idcpfpj, nomraso, tippfpj FROM abnf_cadastro_cpfcnpj ORDER by idcpfpj;
SELECT datanas, datacas, datafal FROM abnf_cadastro_cpfcnpj;
SELECT idcpfpj, codpfpj, nomraso, situreg FROM abnf_cadastro_cpfcnpj where codpfpj = '090.616.218-10';      '11.137.434/0002-35';
---------------------------------------------
SELECT idcpfpj, codpfpj, nomraso, situreg FROM abnf_cadastro_cpfcnpj WHERE situreg = 'C';
UPDATE *** abnf_cadastro_cpfcnpj SET situreg = 'A' WHERE idcpfpj = 310;
SELECT idcpfpj, codpfpj, nomraso, situreg FROM abnf_cadastro_cpfcnpj WHERE idcpfpj = 126;
SELECT idcpfpj, codpfpj, nomraso, situreg FROM abnf_cadastro_cpfcnpj WHERE idcpfpj = 836;
SELECT idcpfpj, codpfpj, nomraso, situreg FROM abnf_cadastro_cpfcnpj WHERE nomraso LIKE '%JOSI%';
SELECT idcpfpj, codpfpj, nomraso, situreg FROM abnf_cadastro_cpfcnpj WHERE nomraso LIKE '%BRUNO SILVA DA LUZ%';
---------------------------------------------
DELETE *** FROM abnf_cadastro_cpfcnpj WHERE idcpfpj = 5;
---------------------------------------------
\! clear; SELECT idfotof FROM abnf_cadastro_cpfcnpj; UPDATE *** abnf_cadastro_cpfcnpj SET idfotof = 6 WHERE idcpfpj = 1; SELECT idfotof FROM abnf_cadastro_cpfcnpj;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_cadastro_funcionarios_cargos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_cadastro_funcionarios_cargos (
    idcargo     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do cargo de funcionário
    codcarg     INT                                         NOT NULL                            ,   # Código do cargo de funcionário
    descarg     VARCHAR(100)                                NOT NULL                            ,   # Descrição do cargo de funcionário
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data de criação do registro
    dtregal     DATETIME                                                                        ,   # Data de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    INDEX abnfdx01 (codcarg, idcargo),
    INDEX abnfdx02 (descarg, idcargo)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_cadastro_funcionarios_cargos (codcarg, idcargo);
CREATE INDEX abnfdx02 ON abnf_cadastro_funcionarios_cargos (descarg, idcargo);
---------------------------------------------
DROP *** TABLE abnf_cadastro_funcionarios_cargos;
DROP *** INDEX abnfdx?? ON abnf_cadastro_funcionarios_cargos;
---------------------------------------------
SHOW COLUMNS FROM abnf_cadastro_funcionarios_cargos;
SHOW INDEX FROM abnf_cadastro_funcionarios_cargos;
---------------------------------------------
SELECT * FROM abnf_cadastro_funcionarios_cargos;
---------------------------------------------
INSERT *** INTO abnf_cadastro_funcionarios_cargos (idcargo, codcarg, descarg, situreg, idusucr, dtregcr, idfilia) VALUES
(?, ?, '???', "A", 2, CURRENT_TIMESTAMP(), ?);
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_cadastro_funcionarios ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_cadastro_funcionarios (
    idfunci     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do funcionário
    codfunc     INT                                         NOT NULL                            ,   # Código do funcionário
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data de criação do registro
    dtregal     DATETIME                                                                        ,   # Data de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    idcpfpj     INT                                         NOT NULL                            ,   # ID do cargo (FK)
    idcargo     INT                                         NOT NULL                            ,   # ID cadastro CPF/CNPJ (FK)
    dataadm     DATE                                        NOT NULL                            ,   # Data de admissão
    dataafa     DATE                                                                            ,   # Data de afastamento
    datades     DATE                                                                            ,   # Data de desligamento
    dataitr     DATE                                                                            ,   # Data inicio de treinamento
    dataftr     DATE                                                                            ,   # Data fim de treinamento
    motelev     BOOLEAN                                                                         ,   # Motorista do Elevar?
    observa     TEXT                                                                            ,   # Observação
    INDEX abnfdx01 (codfunc, idfunci)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_cadastro_funcionarios (codfunc, idfunci);
---------------------------------------------
DROP *** TABLE abnf_cadastro_funcionarios;
DROP *** INDEX abnfdx?? ON abnf_cadastro_funcionarios;
---------------------------------------------
SHOW COLUMNS FROM abnf_cadastro_funcionarios;
SHOW INDEX FROM abnf_cadastro_funcionarios;
---------------------------------------------
SELECT * FROM abnf_cadastro_funcionarios;
SELECT * FROM abnf_cadastro_funcionarios WHERE idcpfpj = 1;
SELECT * FROM abnf_cadastro_funcionarios WHERE idfunci = 192;
SELECT * FROM abnf_cadastro_funcionarios WHERE codfunc = 60641;
SELECT * FROM abnf_cadastro_funcionarios WHERE situreg = 'C';
---------------------------------------------
SELECT * FROM abnf_cadastro_funcionarios WHERE situreg = 'C';
UPDATE *** abnf_cadastro_funcionarios SET situreg = 'A' WHERE idfunci = 192;
SELECT * FROM abnf_cadastro_funcionarios WHERE idfunci = 13;
SELECT * FROM abnf_cadastro_funcionarios WHERE codfunc = 8;
---------------------------------------------
DELETE *** FROM abnf_cadastro_funcionarios WHERE idfunci = 1;
---------------------------------------------
ALTER *** TABLE abnf_cadastro_funcionarios ADD COLUMN motelev BOOLEAN AFTER dataftr;
---------------------------------------------
INSERT *** INTO abnf_cadastro_funcionarios (idfunci, codfunc, situreg, idusucr, dtregcr, idfilia, idcpfpj, idcargo, dataadm, datades) VALUES
(708 , 373 , "A", 1, CURRENT_TIMESTAMP(), 1, 826, 51 , '2020-06-01', NULL);
---------------------------------------------
SELECT * FROM abnf_elevar_cadastro_ordens_servico_padrao_itens WHERE idfunci = 479;
SELECT * FROM abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog WHERE idfunci = 479;
SELECT * FROM abnf_elevar_movimentacao_ordens_servico_diaria_itens_real WHERE idfunci = 479;
SELECT * FROM abnf_sac_movimentacao_atendimentos WHERE idfunci = 479;
SELECT * FROM abnf_sigom_movimentacao_ocorrencias WHERE idfunci = 479;
SELECT * FROM abnf_sigom_movimentacao_ocorrencias WHERE idfuate = 479;
SELECT * FROM abnf_sigom_movimentacao_ocorrencias WHERE idfures = 479;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_cadastro_veiculos_marcas ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_cadastro_veiculos_marcas (
    idmarca     INT                     PRIMARY KEY         NOT NULL                            ,   # ID da marca de veículo
    codmarc     INT                                         NOT NULL                            ,   # Código da marca de veículo
    desmarc     VARCHAR(100)                                NOT NULL                            ,   # Descrição da marca de veículo
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (codmarc, idmarca),
    INDEX abnfdx02 (desmarc, idmarca)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_cadastro_veiculos_marcas (codmarc, idmarca);
CREATE INDEX abnfdx02 ON abnf_cadastro_veiculos_marcas (desmarc, idmarca);
---------------------------------------------
DROP *** TABLE abnf_cadastro_veiculos_marcas;
DROP *** INDEX abnfdx?? ON abnf_cadastro_veiculos_marcas;
---------------------------------------------
SHOW COLUMNS FROM abnf_cadastro_veiculos_marcas;
SHOW INDEX FROM abnf_cadastro_veiculos_marcas;
---------------------------------------------
SELECT * FROM abnf_cadastro_veiculos_marcas;
---------------------------------------------
INSERT *** INTO abnf_cadastro_veiculos_marcas (idmarca, codmarc, desmarc, situreg, idusucr, dtregcr) VALUES
(?, ?, '???', "A", 1, CURRENT_TIMESTAMP()),
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_cadastro_veiculos_modelos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_cadastro_veiculos_modelos (
    idmodel     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do modelo de veículo
    codmode     INT                                         NOT NULL                            ,   # Código do modelo de veículo
    desmode     VARCHAR(100)                                NOT NULL                            ,   # Descrição do modelo de veículo
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idmarca     INT                                         NOT NULL                            ,   # ID da marca de veículo (FK)
    INDEX abnfdx01 (codmode, idmodel),
    INDEX abnfdx02 (desmode, idmarca, idmodel)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_cadastro_veiculos_modelos (codmode, idmodel);
CREATE INDEX abnfdx02 ON abnf_cadastro_veiculos_modelos (desmode, idmarca, idmodel);
---------------------------------------------
DROP *** TABLE abnf_cadastro_veiculos_modelos;
DROP *** INDEX abnfdx?? ON abnf_cadastro_veiculos_modelos;
---------------------------------------------
SHOW COLUMNS FROM abnf_cadastro_veiculos_modelos;
SHOW INDEX FROM abnf_cadastro_veiculos_modelos;
---------------------------------------------
SELECT * FROM abnf_cadastro_veiculos_modelos;
---------------------------------------------
INSERT *** INTO abnf_cadastro_veiculos_modelos (idmodel, codmode, idmarca, desmode, situreg, idusucr, dtregcr) VALUES
(?, ?, ?, '???', "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_cadastro_veiculos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_cadastro_veiculos (
    idveicu     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do veículo
    prefvei     VARCHAR(20)                                 NOT NULL                            ,   # Prefixo do veículo
    placave     VARCHAR(10)                                 NOT NULL                            ,   # Placa do veículo
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    idmodel     INT                                         NOT NULL                            ,   # ID do modelo de veículo (FK)
    renavam     VARCHAR(30)                                                                     ,   # Renavam do veículo
    chassiv     VARCHAR(30)                                                                     ,   # Chassi do veículo
    corveic     VARCHAR(30)                                                                     ,   # Cor do veículo
    anofabr     INT                                                                             ,   # Ano de fabricação
    anomode     INT                                                                             ,   # Ano do modelo
    tipmoto     INT                                                                             ,   # Tipo de motor: [1]=Dianteiro/[2]=Traseiro
    tipcomb     INT                                                                             ,   # Tipo de combustível: [1]=Diesel/[2]=Gasolina/[3]=Alcool/[4]=Flex/[5]=GNV
    captanq     INT                                                                             ,   # Capacidade em litros do tanque de combustível
    lugsent     INT                                                                             ,   # Número de lugares sentados
    lugempe     INT                                                                             ,   # Número de lugares em pé
    lugroda     INT                                                                             ,   # Número de lugares para cadeirantes
    lugacom     INT                                                                             ,   # Número de lugares para acompanhantes
    numport     INT                                                                             ,   # Número de portas
    dataini     DATE                                        NOT NULL                            ,   # Data de compra do veículo ou do seu início de atividades
    datafim     DATE                                                                            ,   # Data de venda do veículo ou do seu término de atividades
    arcondi     BOOLEAN                                                                         ,   # Veículo tem ar-condicionado?
    veielev     BOOLEAN                                                                         ,   # Veículo do Elevar?
    observa     TEXT                                                                            ,   # Observação
    libpsod     BOOLEAN                                                                         ,   # Libera o odômetro para ser lançado como novo na próxima saída do veículo?
    libpsro     BOOLEAN                                                                         ,   # Libera a roleta para ser lançada como nova na próxima saída do veículo?
    INDEX abnfdx01 (prefvei, idveicu),
    INDEX abnfdx02 (placave, idveicu)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_cadastro_veiculos (prefvei, idveicu);
CREATE INDEX abnfdx02 ON abnf_cadastro_veiculos (placave, idveicu);
---------------------------------------------
DROP *** TABLE abnf_cadastro_veiculos;
DROP *** INDEX abnfdx?? ON abnf_cadastro_veiculos;
---------------------------------------------
SHOW COLUMNS FROM abnf_cadastro_veiculos;
SHOW INDEX FROM abnf_cadastro_veiculos;
---------------------------------------------
DELETE *** FROM abnf_cadastro_veiculos WHERE idveicu = 1;
---------------------------------------------
ALTER *** TABLE abnf_cadastro_veiculos ADD COLUMN numport INT AFTER lugacom;
ALTER *** TABLE abnf_cadastro_veiculos ADD COLUMN arcondi BOOLEAN AFTER datafim;
---------------------------------------------
Relação de veículos (*** principal ***)
SELECT * FROM abnf_cadastro_veiculos;
SELECT idveicu, prefvei, placave, situreg FROM abnf_cadastro_veiculos WHERE prefvei = '32531';
SELECT idveicu, prefvei, placave, situreg FROM abnf_cadastro_veiculos WHERE situreg = 'A';
SELECT idveicu, prefvei, placave, situreg FROM abnf_cadastro_veiculos WHERE idveicu = 16;
---------------------------------------------
INSERT *** INTO abnf_cadastro_veiculos (idveicu, prefvei, placave, situreg, idusucr, dtregcr, idfilia, idmodel, renavam, chassiv, anofabr, anomode, dataini) VALUES
(278, 'VAN 03', '???????', "A", ?, CURRENT_TIMESTAMP(), ?, ?, '?' , '?' , 20?? , 20??, '20??-??-??', NULL, 1, '???', ?, ?);
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_cadastro_clientes_fornecedores ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_cadastro_clientes_fornecedores (
    idclfor     INT                     PRIMARY KEY         NOT NULL                            ,   # ID cadastro de clientes e fornecedores
    tipclfo     VARCHAR(1)                                  NOT NULL                            ,   # Tipo: C = Cliente / F = Fornecedor
    codclfo     VARCHAR(20)                                 NOT NULL                            ,   # Código do cliente/fornecedor
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idcpfpj     INT                                         NOT NULL                            ,   # ID cadastro CPF/CNPJ (FK)
    ccontab     INT                                                                             ,   # Conta contábil
    observa     TEXT                                                                            ,   # Observação
    INDEX abnfdx01 (tipclfo, codclfo, idclfor)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_cadastro_clientes_fornecedores (tipclfo, codclfo, idclfor);
---------------------------------------------
DROP *** TABLE abnf_cadastro_clientes_fornecedores;
DROP *** INDEX abnfdx?? ON abnf_cadastro_clientes_fornecedores;
---------------------------------------------
SHOW COLUMNS FROM abnf_cadastro_clientes_fornecedores;
SHOW INDEX FROM abnf_cadastro_clientes_fornecedores;
---------------------------------------------
SELECT * FROM abnf_cadastro_clientes_fornecedores;
---------------------------------------------
ALTER *** TABLE abnf_cadastro_clientes_fornecedores ADD COLUMN ccontab INT AFTER idcpfpj;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_cadastro_especies_documentos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_cadastro_especies_documentos (
    idespdo     INT                     PRIMARY KEY         NOT NULL                            ,   # ID cadastro de espécie de documento
    sigespd     VARCHAR(3)                                  NOT NULL                            ,   # Sigla da espécie de documento
    desespd     VARCHAR(100)                                NOT NULL                            ,   # Descrição da espécie de documento
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (sigespd, desespd),
    INDEX abnfdx02 (desespd, sigespd)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_cadastro_especies_documentos (sigespd, desespd);
CREATE INDEX abnfdx02 ON abnf_cadastro_especies_documentos (desespd, sigespd);
---------------------------------------------
DROP *** TABLE abnf_cadastro_especies_documentos;
DROP *** INDEX abnfdx?? ON abnf_cadastro_especies_documentos;
---------------------------------------------
SHOW COLUMNS FROM abnf_cadastro_especies_documentos;
SHOW INDEX FROM abnf_cadastro_especies_documentos;
---------------------------------------------
SELECT * FROM abnf_cadastro_especies_documentos;
---------------------------------------------
INSERT *** INTO abnf_cadastro_especies_documentos (idespdo, sigespd, desespd, situreg, idusucr, dtregcr) VALUES
(?, '', '???', "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░          ░░  ░░░░░░░░░░   ░░░░   ░░          ░░   ░░░░   ░░          ░░          ░░  ░░          ░░          ░░        ░░░░          ░░
░░  ░░░░░░  ░░  ░░░░░░░░░░    ░░    ░░  ░░░░░░  ░░░░  ░░  ░░░░  ░░░░░░  ░░  ░░░░░░  ░░  ░░  ░░░░░░░░░░  ░░░░░░  ░░  ░░░░░░  ░░  ░░░░░░  ░░
▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒    ▒  ▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒    ▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒
▒▒          ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒  ▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒▒          ▒▒          ▒▒  ▒▒          ▒▒          ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒
▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒    ▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒     ▒▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒
██  ██████  ██  ██████████  ██████  ██  ██████  ████  ██  ████  ██████  ██  ██    ████  ██  ██████████  ██████  ██  ██████  ██  ██████  ██
██  ██████  ██          ██  ██████  ██          ██   ████   ██  ██████  ██  ████    ██  ██  ██████████  ██████  ██        ████          ██
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_almoxarifado_cadastro_produtos_servicos_grupos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_almoxarifado_cadastro_produtos_servicos_grupos (
    idgrupo     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do grupo
    codgrup     INT                                         NOT NULL                            ,   # Código do grupo
    descgru     VARCHAR(100)                                NOT NULL                            ,   # Descrição do grupo
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (codgrup, descgru, idgrupo),
    INDEX abnfdx02 (descgru, codgrup, idgrupo)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_almoxarifado_cadastro_produtos_servicos_grupos (codgrup, descgru, idgrupo);
CREATE INDEX abnfdx02 ON abnf_almoxarifado_cadastro_produtos_servicos_grupos (descgru, codgrup, idgrupo);
---------------------------------------------
DROP *** TABLE abnf_almoxarifado_cadastro_produtos_servicos_grupos;
DROP *** INDEX abnfdx?? ON abnf_almoxarifado_cadastro_produtos_servicos_grupos;
---------------------------------------------
SHOW COLUMNS FROM abnf_almoxarifado_cadastro_produtos_servicos_grupos;
SHOW INDEX FROM abnf_almoxarifado_cadastro_produtos_servicos_grupos;
---------------------------------------------
SELECT * FROM abnf_almoxarifado_cadastro_produtos_servicos_grupos;
---------------------------------------------
INSERT *** INTO abnf_almoxarifado_cadastro_produtos_servicos_grupos (idgrupo, codgrup, descgru, situreg, idusucr, dtregcr) VALUES
(??, ??, ??, "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_almoxarifado_cadastro_produtos_servicos_subgrupos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_almoxarifado_cadastro_produtos_servicos_subgrupos (
    idsubgr     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do subgrupo
    codsubg     INT                                         NOT NULL                            ,   # Código do subgrupo
    descsub     VARCHAR(100)                                NOT NULL                            ,   # Descrição do subgrupo
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idgrupo     INT                                         NOT NULL                            ,   # ID do grupo (FK)
    INDEX abnfdx01 (codsubg, descsub, idsubgr),
    INDEX abnfdx02 (descsub, codsubg, idsubgr)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_almoxarifado_cadastro_produtos_servicos_subgrupos (codsubg, descsub, idsubgr);
CREATE INDEX abnfdx02 ON abnf_almoxarifado_cadastro_produtos_servicos_subgrupos (descsub, codsubg, idsubgr);
---------------------------------------------
DROP *** TABLE abnf_almoxarifado_cadastro_produtos_servicos_subgrupos;
DROP *** INDEX abnfdx?? ON abnf_almoxarifado_cadastro_produtos_servicos_subgrupos;
---------------------------------------------
SHOW COLUMNS FROM abnf_almoxarifado_cadastro_produtos_servicos_subgrupos;
SHOW INDEX FROM abnf_almoxarifado_cadastro_produtos_servicos_subgrupos;
---------------------------------------------
SELECT * FROM abnf_almoxarifado_cadastro_produtos_servicos_subgrupos;
---------------------------------------------
INSERT *** INTO abnf_almoxarifado_cadastro_produtos_servicos_subgrupos (idsubgr, codsubg, idgrupo, descsub, situreg, idusucr, dtregcr) VALUES
(??, ??, ??, ??, "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_almoxarifado_cadastro_produtos_servicos_marcas ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_almoxarifado_cadastro_produtos_servicos_marcas (
    idmarca     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do centro de custo
    codmarc     INT                                         NOT NULL                            ,   # Código do centro de custo
    descmar     VARCHAR(100)                                NOT NULL                            ,   # Descrição do centro de custo
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (codmarc, descmar, idmarca),
    INDEX abnfdx02 (descmar, codmarc, idmarca)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_almoxarifado_cadastro_produtos_servicos_marcas (codmarc, descmar, idmarca);
CREATE INDEX abnfdx02 ON abnf_almoxarifado_cadastro_produtos_servicos_marcas (descmar, codmarc, idmarca);
---------------------------------------------
DROP *** TABLE abnf_almoxarifado_cadastro_produtos_servicos_marcas;
DROP *** INDEX abnfdx?? ON abnf_almoxarifado_cadastro_produtos_servicos_marcas;
---------------------------------------------
SHOW COLUMNS FROM abnf_almoxarifado_cadastro_produtos_servicos_marcas;
SHOW INDEX FROM abnf_almoxarifado_cadastro_produtos_servicos_marcas;
---------------------------------------------
SELECT * FROM abnf_almoxarifado_cadastro_produtos_servicos_marcas;
---------------------------------------------
INSERT *** INTO abnf_almoxarifado_cadastro_produtos_servicos_marcas (idmarca, codmarc, descmar, situreg, idusucr, dtregcr) VALUES
(1, 1, 'GERAL', "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_almoxarifado_cadastro_produtos_servicos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_almoxarifado_cadastro_produtos_servicos (
    idprser     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do produto/serviço
    codprse     INT                                         NOT NULL                            ,   # Código do produto/serviço
    descprs     VARCHAR(200)                                NOT NULL                            ,   # Descrição do produto/serviço
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    tiporeg     VARCHAR(1)                                  NOT NULL                            ,   # Tipo de registro: [P]roduto/[S]erviço
    idsubgr     INT                                         NOT NULL                            ,   # ID do subgrupo do produto/serviço (FK)
    idmarca     INT                                         NOT NULL                            ,   # ID da marca do produto/serviço (FK)
    uniesto     INT                                         NOT NULL                            ,   # Unidade de estoque
    codloca     VARCHAR(10)                                                                     ,   # Código de localização
    ncmsbxx     INT                                                                             ,   # NCM/SB
    cstxxxx     INT                                                                             ,   # CST
    perldve     VARCHAR(1)                                  NOT NULL    DEFAULT 'N'             ,   # Permite saída em lote por veículo
    perdire     VARCHAR(1)                                  NOT NULL    DEFAULT 'N'             ,   # Permite consumo direto por veículo
    tipopne     VARCHAR(1)                                                                      ,   # Tipo de pneu
    qtdesto     DECIMAL(16,6)                               NOT NULL    DEFAULT 0.00            ,   # Quantidade em estoque
    INDEX abnfdx01 (codprse, descprs, idprser),
    INDEX abnfdx02 (descprs, codprse, idprser)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_almoxarifado_cadastro_produtos_servicos (codprse, descprs, idprser);
CREATE INDEX abnfdx02 ON abnf_almoxarifado_cadastro_produtos_servicos (descprs, codprse, idprser);
---------------------------------------------
DROP *** TABLE abnf_almoxarifado_cadastro_produtos_servicos;
DROP *** INDEX abnfdx?? ON abnf_almoxarifado_cadastro_produtos_servicos;
---------------------------------------------
SHOW COLUMNS FROM abnf_almoxarifado_cadastro_produtos_servicos;
SHOW INDEX FROM abnf_almoxarifado_cadastro_produtos_servicos;
---------------------------------------------
SELECT * FROM abnf_almoxarifado_cadastro_produtos_servicos WHERE idprser = 1119;
SELECT * FROM abnf_almoxarifado_cadastro_produtos_servicos WHERE codprse = 80;
SELECT * FROM abnf_almoxarifado_cadastro_produtos_servicos WHERE qtdesto != 0;
---------------------------------------------
INSERT *** INTO abnf_almoxarifado_cadastro_produtos_servicos (idprser, codprse, descprs, situreg, idusucr, dtregcr, tiporeg, idsubgr, idmarca, uniesto, perldve, qtdesto) VALUES
(?, ?, '???', '???', '???', "A", 1, CURRENT_TIMESTAMP(), ...);
---------------------------------------------
ALTER *** TABLE abnf_almoxarifado_cadastro_produtos_servicos ADD COLUMN ncmsbxx INT AFTER codloca;
ALTER *** TABLE abnf_almoxarifado_cadastro_produtos_servicos ADD COLUMN cstxxxx INT AFTER ncmsbxx;
UPDATE *** abnf_almoxarifado_cadastro_produtos_servicos SET qtdesto = 0;
ALTER *** TABLE abnf_almoxarifado_cadastro_produtos_servicos CHANGE descprs descprs VARCHAR(200) NOT NULL;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_almoxarifado_cadastro_medidores_produtos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_almoxarifado_cadastro_medidores_produtos (
    idmedid     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do medidor
    codmedi     INT                                         NOT NULL                            ,   # Código do medidor
    descmed     VARCHAR(200)                                NOT NULL                            ,   # Descrição do medidor
    idprser     INT                                         NOT NULL                            ,   # ID do produto (FK)
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (codmedi, descmed, idmedid),
    INDEX abnfdx02 (descmed, codmedi, idmedid)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_almoxarifado_cadastro_medidores_produtos (codmedi, descmed, idmedid);
CREATE INDEX abnfdx02 ON abnf_almoxarifado_cadastro_medidores_produtos (descmed, codmedi, idmedid);
---------------------------------------------
DROP *** TABLE abnf_almoxarifado_cadastro_medidores_produtos;
DROP *** INDEX abnfdx?? ON abnf_almoxarifado_cadastro_medidores_produtos;
---------------------------------------------
SHOW COLUMNS FROM abnf_almoxarifado_cadastro_medidores_produtos;
SHOW INDEX FROM abnf_almoxarifado_cadastro_medidores_produtos;
---------------------------------------------
SELECT * FROM abnf_almoxarifado_cadastro_medidores_produtos;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_almoxarifado_movimentacao_produtos_servicos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_almoxarifado_movimentacao_produtos_servicos (
    idcmprs     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do registro de movimentação de produtos/serviços
    nrdocnf     BIGINT                                      NOT NULL                            ,   # Número do documento/nota fiscal
    serienf     VARCHAR(5)                                                                      ,   # Série da nota fiscal (opcional)
    idespdo     INT                                         NOT NULL                            ,   # ID da espécie do documento (FK)
    tiporeg     INT                                         NOT NULL                            ,   # Tipo de registro: [1]=Nota Fiscal/[2]=RQ/[3]=Consumo em lote/[4]=OS//[5]=Inventário
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[C]ancelado
    regfech     BOOLEAN                                                DEFAULT False            ,   # Registro fechado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    idclfor     INT                                                                             ,   # ID do cliente/fornecedor
    idsubgr     INT                                                                             ,   # ID do subgrupo financeiro (FK)
    idfabos     INT                                                                             ,   # ID do funcionário que solicitou a ordem de serviço
    vatoprs     DECIMAL(10,2)                               NOT NULL    DEFAULT 0.00            ,   # Valor total de produtos e serviços            (+)
    valabat     DECIMAL(10,2)                               NOT NULL    DEFAULT 0.00            ,   # Valor abatimento/desconto/devolução           (-)
    vatonot     DECIMAL(10,2)                               NOT NULL    DEFAULT 0.00            ,   # Valor total do documento                      (=)
    bcaicst     DECIMAL(10,2)                                                                   ,   # Base de cálculo do ICMS/ST
    vrticst     DECIMAL(10,2)                                                                   ,   # Valor de retenção do ICMS/ST
    datalan     DATETIME                                    NOT NULL                            ,   # Data/hora do lançamento do registro (data exata extraída do sistema)
    datacan     DATETIME                                                                        ,   # Data/hora do cancelamento do registro (data exata extraída do sistema)
    datafin     DATETIME                                                                        ,   # Data/hora da finalização (data exata extraída do sistema)
    datadoc     DATE                                                                            ,   # Data do documento
    dataent     DATE                                                                            ,   # Data de entrada
    observa     TEXT                                                                            ,   # Observação
    INDEX abnfdx01 (idclfor, nrdocnf, serienf, idespdo, tiporeg)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_almoxarifado_movimentacao_produtos_servicos (idclfor, nrdocnf, serienf, idespdo, datadoc, tiporeg);
---------------------------------------------
DROP *** TABLE abnf_almoxarifado_movimentacao_produtos_servicos;
DROP *** INDEX abnfdx?? ON abnf_almoxarifado_movimentacao_produtos_servicos;
---------------------------------------------
SHOW COLUMNS FROM abnf_almoxarifado_movimentacao_produtos_servicos;
SHOW INDEX FROM abnf_almoxarifado_movimentacao_produtos_servicos;
---------------------------------------------
SELECT * FROM abnf_almoxarifado_movimentacao_produtos_servicos;
SELECT * FROM abnf_almoxarifado_movimentacao_produtos_servicos WHERE nrdocnf = 16816;
---------------------------------------------
ALTER *** TABLE abnf_almoxarifado_movimentacao_produtos_servicos ADD COLUMN regfech BOOLEAN DEFAULT False AFTER situreg;
ALTER *** TABLE abnf_almoxarifado_movimentacao_produtos_servicos CHANGE idespdo idespdo INT;
ALTER *** TABLE abnf_almoxarifado_movimentacao_produtos_servicos CHANGE vatoprs vatoprs DECIMAL(10,2);
ALTER *** TABLE abnf_almoxarifado_movimentacao_produtos_servicos CHANGE valabat valabat DECIMAL(10,2);
ALTER *** TABLE abnf_almoxarifado_movimentacao_produtos_servicos CHANGE vatonot vatonot DECIMAL(10,2);
ALTER *** TABLE abnf_almoxarifado_movimentacao_produtos_servicos DROP COLUMN idveicu;
---------------------------------------------
*** rafael - arrumar - reabrir nf/requisição***
SELECT idcmprs, regfech FROM abnf_almoxarifado_movimentacao_produtos_servicos WHERE nrdocnf = 70;
UPDATE *** abnf_almoxarifado_movimentacao_produtos_servicos SET regfech = False WHERE nrdocnf = 70;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_almoxarifado_movimentacao_produtos_servicos_itens ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_almoxarifado_movimentacao_produtos_servicos_itens (
    iditmps     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do ítem de registro de movimentação de produtos/serviços
    idcmprs     INT                                         NOT NULL                            ,   # ID do registro de movimentação de produtos/serviços (FK)
    idprser     INT                                         NOT NULL                            ,   # ID do produto/serviço (FK)
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    tipomov     VARCHAR(1)                                  NOT NULL                            ,   # Tipo de movimentação: [E]ntrada/[S]aída/[D]ireto
    qtdmovi     DECIMAL(16,6)                               NOT NULL                            ,   # Quantidade movimentada do produto/servico
    valunit     DECIMAL(13,6)                                                                   ,   # Valor unitário do produto/servico
    valdesc     DECIMAL(10,2)                                                                   ,   # Valor desconto                                (-)
    valriss     DECIMAL(10,2)                                                                   ,   # Valor retenção ISSQN                          (-)
    valrpis     DECIMAL(10,2)                                                                   ,   # Valor retenção PIS/COFINS/CSLL                (-)
    valrins     DECIMAL(10,2)                                                                   ,   # Valor retenção INSS                           (-)
    valrirr     DECIMAL(10,2)                                                                   ,   # Valor retenção IRRF                           (-)
    valoutr     DECIMAL(10,2)                                                                   ,   # Valor outros (Frete/IPI/Desp.Acess)           (+)
    valtota     DECIMAL(10,2)                                                                   ,   # Valor total do produto/servico
    cfopxxx     INT                                                                             ,   # CFOP
    bcaicms     DECIMAL(10,2)                                                                   ,   # Base de cálculo do ICMS
    vrticms     DECIMAL(10,2)                                                                   ,   # Valor de retenção do ICMS
    valipix     DECIMAL(10,2)                                                                   ,   # Valor IPI
    datalan     DATETIME                                    NOT NULL                            ,   # Data/hora do lançamento do registro (data exata extraída do sistema)
    datacan     DATETIME                                                                        ,   # Data/hora do cancelamento do registro (data exata extraída do sistema)
    idveicu     INT                                                                             ,   # ID do veículo (FK)
    odomvei     INT                                                                             ,   # Odômetro do veículo
    idmedid     INT                                                                             ,   # ID do medidor de produto (FK)
    qtdesat     DECIMAL(16,6)                                                                   ,   # Quantidade encontrada em estoque quando registro ativo
    qtdesca     DECIMAL(16,6)                                                                   ,   # Quantidade encontrada em estoque quando registro cancelado
    INDEX abnfdx01 (idcmprs, datalan)
);
---------------------------------------------
CREATE INDEX abnf_almoxarifado_movimentacao_produtos_servicos_itens (idcmprs, datalan);
---------------------------------------------
DROP *** TABLE abnf_almoxarifado_movimentacao_produtos_servicos_itens;
DROP *** INDEX abnfdx?? ON abnf_almoxarifado_movimentacao_produtos_servicos_itens;
---------------------------------------------
SHOW COLUMNS FROM abnf_almoxarifado_movimentacao_produtos_servicos_itens;
SHOW INDEX FROM abnf_almoxarifado_movimentacao_produtos_servicos_itens;
---------------------------------------------
SELECT * FROM abnf_almoxarifado_movimentacao_produtos_servicos_itens;
SELECT * FROM abnf_almoxarifado_movimentacao_produtos_servicos_itens WHERE idprser = 1666;
---------------------------------------------
UPDATE *** abnf_almoxarifado_movimentacao_produtos_servicos_itens SET situreg = 'A' where iditmps = 1;
---------------------------------------------
ALTER *** TABLE abnf_almoxarifado_movimentacao_produtos_servicos_itens DROP COLUMN datamov;
ALTER *** TABLE abnf_almoxarifado_movimentacao_produtos_servicos_itens ADD COLUMN idmedid INT AFTER odomvei;
---------------------------------------------
SELECT idprser, codprse, descprs, qtdesto FROM abnf_almoxarifado_cadastro_produtos_servicos WHERE codprse = 1010014;
SELECT iditmps, idprser, qtdmovi, datalan, datacan, qtdesat, qtdesca FROM abnf_almoxarifado_movimentacao_produtos_servicos_itens WHERE idprser = 153 ORDER BY datalan;
update *** abnf_almoxarifado_movimentacao_produtos_servicos_itens set qtdesat = 4 where iditmps = 3;
update *** abnf_almoxarifado_movimentacao_produtos_servicos_itens set qtdesat = 6 where iditmps = 4;
update *** abnf_almoxarifado_movimentacao_produtos_servicos_itens set qtdesat = 8 where iditmps = 5;
update *** abnf_almoxarifado_movimentacao_produtos_servicos_itens set qtdesca = 6 where iditmps = 3;
update *** abnf_almoxarifado_movimentacao_produtos_servicos_itens set qtdesca = 4 where iditmps = 4;
update *** abnf_almoxarifado_cadastro_produtos_servicos set qtdesto = 4 where idprser = 153;
---------------------------------------------
SELECT a.iditmps, a.idprser, a. qtdmovi, a.datalan, a.datacan, a.qtdesat, a.qtdesca, b.idcmprs, a.situreg, b.situreg, a.idveicu, b.datadoc, a.odomvei
FROM abnf_almoxarifado_movimentacao_produtos_servicos_itens as a
INNER JOIN abnf_almoxarifado_movimentacao_produtos_servicos as b
WHERE a.idcmprs = b.idcmprs and
idveicu IS NOT NULL
ORDER BY a.idveicu, b.datadoc, a.odomvei;
---------------------------------------------
*** Rafael ***
*** Adicionar 1.000.000 a todos os kms de um determinado veiculo ***
SELECT idveicu, prefvei, placave, situreg FROM abnf_cadastro_veiculos WHERE prefvei IN ('824');   ('836','838');
***
SELECT idveicu, odomvei, situreg FROM abnf_almoxarifado_movimentacao_produtos_servicos_itens WHERE idveicu IN (18);  (24,25);
SELECT idveicu, odomvei, situreg FROM abnf_almoxarifado_movimentacao_produtos_servicos_itens WHERE idveicu IN (24,25) AND situreg != 'C';
SELECT idveicu, odomvei, situreg FROM abnf_almoxarifado_movimentacao_produtos_servicos_itens WHERE idveicu IN (24,25) AND situreg = 'C';
***
UPDATE abnf_almoxarifado_movimentacao_produtos_servicos_itens SET odomvei = odomvei + 1000000 WHERE idveicu IN (18) and odomvei < 1000000;
---------------------------------------------
*** alexandre ***
Acabar com os campos e com os cálculo envolvendo os campos:
qtdesat
qtdesca
Procurar todos os programas que envolvem esses campos e alterar
---------------------------------------------
*** alexandre *** Acerto de registros de movimentação de produtos ***
# Produto 1684
SELECT * FROM abnf_almoxarifado_movimentacao_produtos_servicos_itens WHERE iditmps = 833;
UPDATE *** abnf_almoxarifado_movimentacao_produtos_servicos_itens SET situreg = 'C', datacan = '2025-03-21 11:35:13', idusual = 2 WHERE iditmps = 833;
# Produto 1565
SELECT * FROM abnf_almoxarifado_movimentacao_produtos_servicos_itens WHERE iditmps = 1178;
UPDATE *** abnf_almoxarifado_movimentacao_produtos_servicos_itens SET situreg = 'C', datacan = '2025-04-01 12:21:56', idusual = 2 WHERE iditmps = 1178;
# Produto 1708
SELECT * FROM abnf_almoxarifado_movimentacao_produtos_servicos_itens WHERE iditmps = 1176;
UPDATE *** abnf_almoxarifado_movimentacao_produtos_servicos_itens SET situreg = 'C', datacan = '2025-04-01 12:20:57', idusual = 2 WHERE iditmps = 1176;
# Produto 1496
SELECT * FROM abnf_almoxarifado_movimentacao_produtos_servicos_itens WHERE iditmps = 3771;
UPDATE *** abnf_almoxarifado_movimentacao_produtos_servicos_itens SET qtdmovi = 39 WHERE iditmps = 3771;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_almoxarifado_movimentacao_medidores_produtos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_almoxarifado_movimentacao_medidores_produtos (
    idcmmed     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do registro de movimentação do medidor
    idmedid     INT                                         NOT NULL                            ,   # ID do medidor (FK)
    datamed     DATE                                        NOT NULL                            ,   # Data da medição
    valmedi     DECIMAL(16,6)                               NOT NULL                            ,   # Valor encontrado no medidor
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (datamed, idmedid, idcmmed)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_almoxarifado_movimentacao_medidores_produtos (datamed, idmedid, idcmmed);
---------------------------------------------
DROP *** TABLE abnf_almoxarifado_movimentacao_medidores_produtos;
DROP *** INDEX abnfdx?? ON abnf_almoxarifado_movimentacao_medidores_produtos;
---------------------------------------------
SHOW COLUMNS FROM abnf_almoxarifado_movimentacao_medidores_produtos;
SHOW INDEX FROM abnf_almoxarifado_movimentacao_medidores_produtos;
---------------------------------------------
SELECT * FROM abnf_almoxarifado_movimentacao_medidores_produtos;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░          ░░          ░░          ░░  ░░░░░░  ░░          ░░   ░░░░░  ░░          ░░  ░░  ░░░░░░  ░░          ░░
░░  ░░░░░░  ░░  ░░░░░░  ░░  ░░░░░░░░░░  ░░░░░░  ░░  ░░░░░░░░░░    ░░░░  ░░░░░░  ░░░░░░  ░░  ░░░░░░  ░░  ░░░░░░  ░░
▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒  ▒▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒
▒▒          ▒▒          ▒▒          ▒▒  ▒▒▒▒▒▒  ▒▒          ▒▒  ▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒          ▒▒
▒▒  ▒▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒  ▒  ▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒▒  ▒▒▒▒  ▒▒▒  ▒▒▒▒▒▒  ▒▒
██  ██████████  ██    ████  ████████████  ██  ████  ██████████  ████    ██████  ██████  ████  ██  ████  ██████  ██
██  ██████████  ████    ██          ██████  ██████          ██  █████   ██████  ██████  ██████  ██████  ██████  ██
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_preventiva_cadastro_grupos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_preventiva_cadastro_grupos (
    idgrpre     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do grupo de preventiva
    codgrpr     INT                                         NOT NULL                            ,   # Código do grupo de preventiva
    descgrp     VARCHAR(100)                                NOT NULL                            ,   # Descrição do grupo de preventiva
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (codgrpr, descgrp, idgrpre),
    INDEX abnfdx02 (descgrp, codgrpr, idgrpre)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_preventiva_cadastro_grupos (codgrpr, descgrp, idgrpre);
CREATE INDEX abnfdx02 ON abnf_preventiva_cadastro_grupos (descgrp, codgrpr, idgrpre);
---------------------------------------------
DROP *** TABLE abnf_preventiva_cadastro_grupos;
DROP *** INDEX abnfdx?? ON abnf_preventiva_cadastro_grupos;
---------------------------------------------
SHOW COLUMNS FROM abnf_preventiva_cadastro_grupos;
SHOW INDEX FROM abnf_preventiva_cadastro_grupos;
---------------------------------------------
SELECT * FROM abnf_preventiva_cadastro_grupos;
---------------------------------------------
INSERT *** INTO abnf_preventiva_cadastro_grupos (idgrpre, codgrpr, descgrp, situreg, idusucr, dtregcr) VALUES
(??, ??, ??, "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_preventiva_cadastro_itens ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_preventiva_cadastro_itens (
    iditpre     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do ítem de preventiva
    coditpr     INT                                         NOT NULL                            ,   # Código do ítem de preventiva
    descitp     VARCHAR(100)                                NOT NULL                            ,   # Descrição do ítem de preventiva
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (coditpr, descitp, iditpre),
    INDEX abnfdx02 (descitp, coditpr, iditpre)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_preventiva_cadastro_itens (coditpr, descitp, iditpre);
CREATE INDEX abnfdx02 ON abnf_preventiva_cadastro_itens (descitp, coditpr, iditpre);
---------------------------------------------
DROP *** TABLE abnf_preventiva_cadastro_itens;
DROP *** INDEX abnfdx?? ON abnf_preventiva_cadastro_itens;
---------------------------------------------
SHOW COLUMNS FROM abnf_preventiva_cadastro_itens;
SHOW INDEX FROM abnf_preventiva_cadastro_itens;
---------------------------------------------
SELECT * FROM abnf_preventiva_cadastro_itens;
---------------------------------------------
INSERT *** INTO abnf_preventiva_cadastro_itens (iditpre, coditpr, descitp, situreg, idusucr, dtregcr) VALUES
(??, ??, ??, "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_preventiva_cadastro_associacao_itens_grupos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_preventiva_cadastro_associacao_itens_grupos (
    idassig     INT                     PRIMARY KEY         NOT NULL                            ,   # ID da associação ítem x grupo
    idgrpre     INT                                         NOT NULL                            ,   # ID do grupo de preventiva (FK)
    iditpre     INT                                         NOT NULL                            ,   # ID do ítem de preventiva (FK)
    kmpreve     INT                                                                             ,   # Km de preventiva
    kmaviso     INT                                                                             ,   # Km de aviso anticipado
    kmtoler     INT                                                                             ,   # Km de tolerância
    diaspre     INT                                                                             ,   # Dias de preventiva
    diasavi     INT                                                                             ,   # Dias de aviso anticipado
    diastol     INT                                                                             ,   # Dias de tolerância
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (idgrpre, iditpre, idassig)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_preventiva_cadastro_associacao_itens_grupos (idgrpre, iditpre, idassig);
---------------------------------------------
DROP *** TABLE abnf_preventiva_cadastro_associacao_itens_grupos;
DROP *** INDEX abnfdx?? ON abnf_preventiva_cadastro_associacao_itens_grupos;
---------------------------------------------
SHOW COLUMNS FROM abnf_preventiva_cadastro_associacao_itens_grupos;
SHOW INDEX FROM abnf_preventiva_cadastro_associacao_itens_grupos;
---------------------------------------------
SELECT * FROM abnf_preventiva_cadastro_associacao_itens_grupos;
---------------------------------------------
INSERT *** INTO abnf_preventiva_cadastro_associacao_itens_grupos (...) VALUES
(..., "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_preventiva_cadastro_associacao_veiculos_grupos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_preventiva_cadastro_associacao_veiculos_grupos (
    idassvg     INT                     PRIMARY KEY         NOT NULL                            ,   # ID da associação
    idgrpre     INT                                         NOT NULL                            ,   # ID do grupo de preventiva (FK)
    idveicu     INT                                         NOT NULL                            ,   # ID do veículo (FK)
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (idgrpre, idveicu, idassvg)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_preventiva_cadastro_associacao_veiculos_grupos (idgrpre, idveicu, idassvg);
---------------------------------------------
DROP *** TABLE abnf_preventiva_cadastro_associacao_veiculos_grupos;
DROP *** INDEX abnfdx?? ON abnf_preventiva_cadastro_associacao_veiculos_grupos;
---------------------------------------------
SHOW COLUMNS FROM abnf_preventiva_cadastro_associacao_veiculos_grupos;
SHOW INDEX FROM abnf_preventiva_cadastro_associacao_veiculos_grupos;
---------------------------------------------
SELECT * FROM abnf_preventiva_cadastro_associacao_veiculos_grupos;
---------------------------------------------
INSERT *** INTO abnf_preventiva_cadastro_associacao_veiculos_grupos (...) VALUES
(..., "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_preventiva_movimentacao_acao_preventiva ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_preventiva_movimentacao_acao_preventiva (
    idacpre     INT                     PRIMARY KEY         NOT NULL                            ,   # ID da ação de preventiva
    datarea     DATE                                        NOT NULL                            ,   # Data da realização da preventiva
    idveicu     INT                                         NOT NULL                            ,   # ID do veículo (FK)
    iditpre     INT                                         NOT NULL                            ,   # ID do ítem de preventiva (FK)
    idgrpre     INT                                         NOT NULL                            ,   # ID do grupo de preventiva (FK)
    odomvei     INT                                         NOT NULL                            ,   # Odômetro do veículo
    idfunci     INT                                         NOT NULL                            ,   # ID do funcionário que realizou a preventiva (FK)
    observa     TEXT                                                                            ,   # Observação
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (datarea, idveicu, idacpre),
    INDEX abnfdx02 (datarea, iditpre, idacpre)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_preventiva_movimentacao_acao_preventiva (datarea, idveicu, idacpre);
CREATE INDEX abnfdx01 ON abnf_preventiva_movimentacao_acao_preventiva (datarea, iditpre, idacpre);
---------------------------------------------
DROP *** TABLE abnf_preventiva_movimentacao_acao_preventiva;
DROP *** INDEX abnfdx?? ON abnf_preventiva_movimentacao_acao_preventiva;
---------------------------------------------
SHOW COLUMNS FROM abnf_preventiva_movimentacao_acao_preventiva;
SHOW INDEX FROM abnf_preventiva_movimentacao_acao_preventiva;
---------------------------------------------
SELECT * FROM abnf_preventiva_movimentacao_acao_preventiva;
---------------------------------------------
INSERT *** INTO abnf_preventiva_movimentacao_acao_preventiva (...) VALUES
(..., "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░          ░░  ░░   ░░░░░  ░░          ░░   ░░░░░  ░░          ░░          ░░  ░░          ░░          ░░
░░  ░░░░░░░░░░  ░░    ░░░░  ░░  ░░░░░░  ░░    ░░░░  ░░  ░░░░░░░░░░  ░░░░░░░░░░  ░░  ░░░░░░  ░░  ░░░░░░  ░░
▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒  ▒  ▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒  ▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒
▒▒          ▒▒  ▒▒  ▒▒  ▒▒  ▒▒          ▒▒  ▒▒  ▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒          ▒▒  ▒▒          ▒▒  ▒▒▒▒▒▒  ▒▒
▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒  ▒▒▒  ▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒  ▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒     ▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒
██  ██████████  ██  ████    ██  ██████  ██  ████    ██  ██████████  ██████████  ██  ██    ████  ██████  ██
██  ██████████  ██  █████   ██  ██████  ██  █████   ██          ██          ██  ██  ████    ██          ██
██████████████████████████████████████████████████████████████████████████████████████████████████████████
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_financeiro_cadastro_contas ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_financeiro_cadastro_contas (
    idconta     INT                     PRIMARY KEY         NOT NULL                            ,   # ID da conta financeira
    codcont     INT                                         NOT NULL                            ,   # Código da conta financeira
    descban     VARCHAR(100)                                NOT NULL                            ,   # Descrição do banco
    descage     VARCHAR(100)                                NOT NULL                            ,   # Descrição da agência
    desccon     VARCHAR(100)                                NOT NULL                            ,   # Descrição da conta
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    saldoin     DECIMAL(30,2)                               NOT NULL    DEFAULT 0.00            ,   # Saldo da conta
    totalre     DECIMAL(30,2)                               NOT NULL    DEFAULT 0.00            ,   # Total de receitas
    totalde     DECIMAL(30,2)                               NOT NULL    DEFAULT 0.00            ,   # Total de despesas
    ccontab     INT                                                                             ,   # Conta contábil
    observa     TEXT                                                                            ,   # Observação
    INDEX abnfdx01 (codcont, idconta),
    INDEX abnfdx02 (descban, descage, desccon, idconta)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_financeiro_cadastro_contas (codcont, idconta);
CREATE INDEX abnfdx02 ON abnf_financeiro_cadastro_contas (descban, descage, desccon, idconta);
---------------------------------------------
DROP *** TABLE abnf_financeiro_cadastro_contas;
DROP *** INDEX abnfdx?? ON abnf_financeiro_cadastro_contas;
---------------------------------------------
SHOW COLUMNS FROM abnf_financeiro_cadastro_contas;
SHOW INDEX FROM abnf_financeiro_cadastro_contas;
---------------------------------------------
SELECT idconta, codcont, descban, descage, desccon, situreg, idfilia, saldoin, totalre, totalde, ccontab FROM abnf_financeiro_cadastro_contas;
SELECT * FROM abnf_financeiro_cadastro_contas;
SELECT idconta, saldoin, totalre, totalde FROM abnf_financeiro_cadastro_contas WHERE idconta = 28;
UPDATE *** abnf_financeiro_cadastro_contas SET totalde = 8608389.76 WHERE idconta = 28;
---------------------------------------------
INSERT *** INTO abnf_financeiro_cadastro_contas (idconta, codcont, descban, descage, desccon, idfilia, saldoin, situreg, idusucr, dtregcr) VALUES
(?, ?, '???', '???', '???', ?, ?, "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
ALTER *** TABLE abnf_financeiro_cadastro_contas MODIFY saldoin DECIMAL(10,2) DEFAULT 0.00;
ALTER *** TABLE abnf_financeiro_cadastro_contas MODIFY totalre DECIMAL(10,2) DEFAULT 0.00;
ALTER *** TABLE abnf_financeiro_cadastro_contas MODIFY totalde DECIMAL(10,2) DEFAULT 0.00;
ALTER *** TABLE abnf_financeiro_cadastro_contas MODIFY saldoin DECIMAL(30,2) NOT NULL DEFAULT 0.00;
ALTER *** TABLE abnf_financeiro_cadastro_contas MODIFY totalre DECIMAL(30,2) NOT NULL DEFAULT 0.00;
ALTER *** TABLE abnf_financeiro_cadastro_contas MODIFY totalde DECIMAL(30,2) NOT NULL DEFAULT 0.00;
ALTER *** TABLE abnf_financeiro_cadastro_contas ADD COLUMN ccontab INT AFTER totalde;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_financeiro_cadastro_grupos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_financeiro_cadastro_grupos (
    idgrupo     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do grupo financeiro
    codgrup     INT                                         NOT NULL                            ,   # Código do grupo financeiro
    descgru     VARCHAR(100)                                NOT NULL                            ,   # Descrição do grupo financeiro
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    tipogru     VARCHAR(1)                                  NOT NULL                            ,   # Tipo de grupo: [R]eceitas/[D]espesas
    INDEX abnfdx01 (codgrup, descgru, idgrupo),
    INDEX abnfdx02 (descgru, codgrup, idgrupo)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_financeiro_cadastro_grupos (codgrup, descgru, idgrupo);
CREATE INDEX abnfdx02 ON abnf_financeiro_cadastro_grupos (descgru, codgrup, idgrupo);
---------------------------------------------
DROP *** TABLE abnf_financeiro_cadastro_grupos;
DROP *** INDEX abnfdx?? ON abnf_financeiro_cadastro_grupos;
---------------------------------------------
SHOW COLUMNS FROM abnf_financeiro_cadastro_grupos;
SHOW INDEX FROM abnf_financeiro_cadastro_grupos;
---------------------------------------------
SELECT * FROM abnf_financeiro_cadastro_grupos;
---------------------------------------------
INSERT *** INTO abnf_financeiro_cadastro_grupos (idgrupo, codgrup, descgru, situreg, idusucr, dtregcr) VALUES
(?, ?, '???', '???', '???', "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_financeiro_cadastro_subgrupos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_financeiro_cadastro_subgrupos (
    idsubgr     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do subgrupo financeiro
    codsubg     INT                                         NOT NULL                            ,   # Código do subgrupo financeiro
    descsub     VARCHAR(100)                                NOT NULL                            ,   # Descrição do subgrupo financeiro
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idgrupo     INT                                         NOT NULL                            ,   # ID do grupo financeiro (FK)
    INDEX abnfdx01 (codsubg, descsub, idsubgr),
    INDEX abnfdx02 (descsub, codsubg, idsubgr)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_financeiro_cadastro_subgrupos (codsubg, descsub, idsubgr);
CREATE INDEX abnfdx02 ON abnf_financeiro_cadastro_subgrupos (descsub, codsubg, idsubgr);
---------------------------------------------
DROP *** TABLE abnf_financeiro_cadastro_subgrupos;
DROP *** INDEX abnfdx?? ON abnf_financeiro_cadastro_subgrupos;
---------------------------------------------
SHOW COLUMNS FROM abnf_financeiro_cadastro_subgrupos;
SHOW INDEX FROM abnf_financeiro_cadastro_subgrupos;
---------------------------------------------
SELECT * FROM abnf_financeiro_cadastro_subgrupos;
---------------------------------------------
INSERT *** INTO abnf_financeiro_cadastro_subgrupos (idsubgr, codsubg, descsub, situreg, idusucr, dtregcr) VALUES
(?, ?, '???', '???', '???', "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_financeiro_cadastro_complementos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_financeiro_cadastro_complementos (
    idcompl     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do complemento
    codcomp     INT                                         NOT NULL                            ,   # Código do complemento
    desccom     VARCHAR(100)                                NOT NULL                            ,   # Descrição do complemento
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    ccontab     INT                                                                             ,   # Conta contábil
    INDEX abnfdx01 (codcomp, desccom, idcompl),
    INDEX abnfdx02 (desccom, codcomp, idcompl)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_financeiro_cadastro_complementos (codcomp, desccom, idcompl);
CREATE INDEX abnfdx02 ON abnf_financeiro_cadastro_complementos (desccom, codcomp, idcompl);
---------------------------------------------
DROP *** TABLE abnf_financeiro_cadastro_complementos;
DROP *** INDEX abnfdx?? ON abnf_financeiro_cadastro_complementos;
---------------------------------------------
SHOW COLUMNS FROM abnf_financeiro_cadastro_complementos;
SHOW INDEX FROM abnf_financeiro_cadastro_complementos;
---------------------------------------------
SELECT * FROM abnf_financeiro_cadastro_complementos;
---------------------------------------------
INSERT *** INTO abnf_financeiro_cadastro_complementos (idcompl, codcomp, desccom, situreg, idusucr, dtregcr) VALUES
(?, ?, '???', '???', '???', "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
ALTER *** TABLE abnf_financeiro_cadastro_complementos ADD COLUMN ccontab INT AFTER dtregal;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_financeiro_cadastro_centros_custo ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_financeiro_cadastro_centros_custo (
    idcecus     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do centro de custo
    codcecu     INT                                         NOT NULL                            ,   # Código do centro de custo
    desccec     VARCHAR(100)                                NOT NULL                            ,   # Descrição do centro de custo
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (codcecu, desccec, idcecus),
    INDEX abnfdx02 (desccec, codcecu, idcecus)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_financeiro_cadastro_centros_custo (codcecu, desccec, idcecus);
CREATE INDEX abnfdx02 ON abnf_financeiro_cadastro_centros_custo (desccec, codcecu, idcecus);
---------------------------------------------
DROP *** TABLE abnf_financeiro_cadastro_centros_custo;
DROP *** INDEX abnfdx?? ON abnf_financeiro_cadastro_centros_custo;
---------------------------------------------
SHOW COLUMNS FROM abnf_financeiro_cadastro_centros_custo;
SHOW INDEX FROM abnf_financeiro_cadastro_centros_custo;
---------------------------------------------
SELECT * FROM abnf_financeiro_cadastro_centros_custo;
---------------------------------------------
INSERT *** INTO abnf_financeiro_cadastro_centros_custo (idcecus, codcecu, desccec, situreg, idusucr, dtregcr) VALUES
(?, ?, '???', '???', '???', "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_financeiro_cadastro_departamentos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_financeiro_cadastro_departamentos (
    iddepto     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do departamento
    coddept     INT                                         NOT NULL                            ,   # Código do departamento
    descdep     VARCHAR(100)                                NOT NULL                            ,   # Descrição do departamento
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (coddept, descdep, iddepto),
    INDEX abnfdx02 (descdep, coddept, iddepto)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_financeiro_cadastro_departamentos (coddept, descdep, iddepto);
CREATE INDEX abnfdx02 ON abnf_financeiro_cadastro_departamentos (descdep, coddept, iddepto);
---------------------------------------------
DROP *** TABLE abnf_financeiro_cadastro_departamentos;
DROP *** INDEX abnfdx?? ON abnf_financeiro_cadastro_departamentos;
---------------------------------------------
SHOW COLUMNS FROM abnf_financeiro_cadastro_departamentos;
SHOW INDEX FROM abnf_financeiro_cadastro_departamentos;
---------------------------------------------
SELECT * FROM abnf_financeiro_cadastro_departamentos;
---------------------------------------------
INSERT *** INTO abnf_financeiro_cadastro_departamentos (iddepto, coddept, descdep, situreg, idusucr, dtregcr) VALUES
(?, ?, '???', '???', '???', "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_financeiro_cadastro_contratos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_financeiro_cadastro_contratos (
    idcontr     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do contrato
    codcont     INT                                         NOT NULL                            ,   # Código do contrato
    desccon     VARCHAR(100)                                NOT NULL                            ,   # Descrição do contrato
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
	idclfor     INT                                         NOT NULL                            ,   # ID do cliente/fornecedor
	tipocon     VARCHAR(1)                                  NOT NULL                            ,   # Tipo de contrato: [R]eceitas/[D]espesas
    dataini     DATE                                        NOT NULL                            ,   # Data de início do contrato
    datafim     DATE                                                                            ,   # Data de término do contrato
    qtdparc     INT                                                                             ,   # Quantidade de parcelas
    valtotc     DECIMAL(10,2) DEFAULT 0.00                  NOT NULL    DEFAULT 0.00            ,   # Valor total do contrato
    observa     TEXT                                                                            ,   # Observação
    INDEX abnfdx01 (codcont, desccon, idcontr),
    INDEX abnfdx02 (desccon, codcont, idcontr)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_financeiro_cadastro_contratos (codcont, desccon, idcontr);
CREATE INDEX abnfdx02 ON abnf_financeiro_cadastro_contratos (desccon, codcont, idcontr);
---------------------------------------------
DROP *** TABLE abnf_financeiro_cadastro_contratos;
DROP *** INDEX abnfdx?? ON abnf_financeiro_cadastro_contratos;
---------------------------------------------
SHOW COLUMNS FROM abnf_financeiro_cadastro_contratos;
SHOW INDEX FROM abnf_financeiro_cadastro_contratos;
---------------------------------------------
SELECT * FROM abnf_financeiro_cadastro_contratos;
---------------------------------------------
INSERT *** INTO abnf_financeiro_cadastro_contratos (idcontr, codcont, desccon, situreg, idusucr, dtregcr) VALUES
(?, ?, '???', '???', '???', "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
ALTER *** TABLE abnf_financeiro_cadastro_contratos MODIFY valtotc DECIMAL(10,2) DEFAULT 0.00;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_financeiro_movimentacao_registros_financeiros ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_financeiro_movimentacao_registros_financeiros (
    idregfi     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do movimento financeiro
    ctrlfin     INT                                         NOT NULL                            ,   # Controle do registro financeiro
    ctrlpgt     INT                                                                             ,   # Controle de pagamento
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    idsubgr     INT                                                                             ,   # ID do subgrupo financeiro (FK)
    idclfor     INT                                                                             ,   # ID do cliente/fornecedor (FK)
    idcompl     INT                                                                             ,   # ID do complemento (FK)
    idcecus     INT                                                                             ,   # ID do centro de custo (FK)
    iddepto     INT                                                                             ,   # ID do departamento (FK)
    idcontr     INT                                                                             ,   # ID do contrato (FK)
    idconta     INT                                                                             ,   # ID da conta financeira (FK)
    tiporeg     VARCHAR(1)                                  NOT NULL                            ,   # Tipo de registro: [R]eceitas/[D]espesas
    modoreg     VARCHAR(1)                                  NOT NULL                            ,   # Modo do registro: [P]previsto/[R]realizado/[T]ransferência
    regiadi     BOOLEAN                                                DEFAULT False            ,   # Registro de adiantamento
    nrdocnf     BIGINT                                                                          ,   # Número do documento/nota fiscal
    serienf     VARCHAR(5)                                                                      ,   # Série da nota fiscal (opcional)
    idespdo     INT                                                                             ,   # ID da espécie do documento (FK)
    totparc     INT                                         NOT NULL                            ,   # Total de parcelas
    numparc     INT                                         NOT NULL                            ,   # Número da parcela corrente
    datadoc     DATE                                        NOT NULL                            ,   # Data do documento
    dataven     DATE                                        NOT NULL                            ,   # Data do vencimento
    datavor     DATE                                        NOT NULL                            ,   # Data do vencimento original
    datapgt     DATE                                                                            ,   # Data do pagamento
    valptdc     DECIMAL(10,2)                               NOT NULL    DEFAULT 0.00            ,   # Valor previsto total do documento
    valppar     DECIMAL(10,2)                               NOT NULL    DEFAULT 0.00            ,   # Valor previsto da parcela
    valrtdc     DECIMAL(10,2)                               NOT NULL    DEFAULT 0.00            ,   # Valor realizado total do documento
    valrpar     DECIMAL(10,2)                               NOT NULL    DEFAULT 0.00            ,   # Valor realizado da parcela
    valjuro     DECIMAL(10,2)                               NOT NULL    DEFAULT 0.00            ,   # Valor do juros
    valcemo     DECIMAL(10,2)                               NOT NULL    DEFAULT 0.00            ,   # Valor de custas e emolumentos
    valdesc     DECIMAL(10,2)                               NOT NULL    DEFAULT 0.00            ,   # Valor do desconto
    valabat     DECIMAL(10,2)                               NOT NULL    DEFAULT 0.00            ,   # Valor do abatimento
    valpago     DECIMAL(10,2)                               NOT NULL    DEFAULT 0.00            ,   # Valor real pago
    observa     TEXT                                                                            ,   # Observação
    cglob01     INT                                                                             ,   # Codigo 01 do registro financeiro do Globus
    cglob02     INT                                                                             ,   # Codigo 02 do registro financeiro do Globus
    INDEX abnfdx01 (ctrlfin, idregfi),
    INDEX abnfdx02 (ctrlpgt, idregfi),
    INDEX abnfdx03 (dataven, idregfi),
    INDEX abnfdx04 (datapgt, valpago, idregfi)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_financeiro_movimentacao_registros_financeiros (ctrlfin, idregfi);
CREATE INDEX abnfdx02 ON abnf_financeiro_movimentacao_registros_financeiros (ctrlpgt, idregfi);
CREATE INDEX abnfdx03 ON abnf_financeiro_movimentacao_registros_financeiros (dataven, idregfi);
CREATE INDEX abnfdx04 ON abnf_financeiro_movimentacao_registros_financeiros (datapgt, valpago, idregfi);
---------------------------------------------
DROP *** TABLE abnf_financeiro_movimentacao_registros_financeiros;
DROP *** INDEX abnfdx?? ON abnf_financeiro_movimentacao_registros_financeiros;
---------------------------------------------
SHOW COLUMNS FROM abnf_financeiro_movimentacao_registros_financeiros;
SHOW INDEX FROM abnf_financeiro_movimentacao_registros_financeiros;
---------------------------------------------
SELECT * FROM abnf_financeiro_movimentacao_registros_financeiros WHERE ctrlfin in (267543, 267544);
SELECT ctrlpgt, datapgt, valpago, idconta FROM abnf_financeiro_movimentacao_registros_financeiros;
SELECT * FROM abnf_financeiro_cadastro_contas WHERE idconta = 1;
SELECT ctrlfin, ctrlpgt, datapgt, valpago, idconta, regiadi, tiporeg FROM abnf_financeiro_movimentacao_registros_financeiros WHERE regiadi = True;
UPDATE *** abnf_financeiro_cadastro_contas SET totalde = 50328.84 WHERE idconta = 1;
DROP *** TABLE abnf_financeiro_movimentacao_registros_financeiros;
--------------------------------------------
SELECT COUNT(*) FROM abnf_financeiro_movimentacao_registros_financeiros;
SHOW FULL PROCESSLIST;
SELECT MAX(cglob01) FROM abnf_financeiro_movimentacao_registros_financeiros;
--------------------------------------------
INSERT *** INTO abnf_financeiro_movimentacao_registros_financeiros (idcontr, codcont, desccon, situreg, idusucr, dtregcr) VALUES
(?, ?, '???', '???', '???', "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
SELECT idclfor, nrdocnf, serienf, idespdo FROM abnf_financeiro_movimentacao_registros_financeiros WHERE idclfor = 7486 and nrdocnf = 47944;
---------------------------------------------
UPDATE *** abnf_financeiro_movimentacao_registros_financeiros SET idcompl = NULL WHERE modoreg = 'T';
SELECT idclfor FROM abnf_financeiro_movimentacao_registros_financeiros WHERE modoreg = 'T';
*** rayeli - arrumar filial ***
SELECT ctrlfin, idfilia, datapgt FROM abnf_financeiro_movimentacao_registros_financeiros WHERE ctrlfin in (
262824
);
UPDATE *** abnf_financeiro_movimentacao_registros_financeiros SET idfilia = 2 WHERE ctrlfin in (
262814
);
UPDATE abnf_financeiro_movimentacao_registros_financeiros SET idfilia = 1 WHERE ctrlfin in (
262824
);
SELECT idregfi, ctrlpgt FROM abnf_financeiro_movimentacao_registros_financeiros WHERE serienf IS NULL;
UPDATE abnf_financeiro_movimentacao_registros_financeiros SET serienf = '' WHERE serienf IS NULL;

+---------+---------+---------+---------+---------+---------+---------------------+---------------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+------------+------------+------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
| idregfi | ctrlfin | ctrlpgt | situreg | idusucr | idusual | dtregcr             | dtregal             | idfilia | idsubgr | idclfor | idcompl | idcecus | iddepto | idcontr | idconta | tiporeg | modoreg | regiadi | nrdocnf | serienf | idespdo | totparc | numparc | datadoc    | dataven    | datavor    | datapgt | valptdc | valppar | valrtdc | valrpar | valjuro | valcemo | valdesc | valabat | valpago | observa | cglob01 | cglob02 |
+---------+---------+---------+---------+---------+---------+---------------------+---------------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+------------+------------+------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
|  263021 |  263021 |    NULL | A       |       2 |    NULL | 2024-12-04 10:23:31 | NULL                |       2 |    NULL |    8942 |       0 |    NULL |    NULL |    NULL |    NULL | D       | R       |       0 |   73351 | NULL    |      40 |       1 |       1 | 2024-11-19 | 2024-11-19 | 2024-11-19 | NULL    |  690.03 |  690.03 |  690.03 |  690.03 |    0.00 |    0.00 |    0.00 |    0.00 |    0.00 |         |    NULL |    NULL |
|  264170 |  264167 |    NULL | A       |       2 |       2 | 2025-01-24 00:00:24 | 2025-01-24 00:08:06 |       2 |     166 |       0 |      15 |       1 |       1 |       0 |       0 | D       | R       |       0 |       1 |         |      14 |       2 |       1 | 2025-01-01 | 2025-01-01 | 2025-01-01 | NULL    | 1000.00 |  500.00 | 1000.00 |  500.00 |    0.00 |    0.00 |    0.00 |    0.00 |    0.00 |         |    NULL |    NULL |
|  264171 |  264168 |    NULL | A       |       2 |    NULL | 2025-01-24 00:00:24 | NULL                |       2 |      25 |    6778 |       0 |       1 |       1 |       0 |       0 | D       | R       |       0 |       1 |         |      14 |       2 |       2 | 2025-01-01 | 2025-02-01 | 2025-02-01 | NULL    | 1000.00 |  500.00 | 1000.00 |  500.00 |    0.00 |    0.00 |    0.00 |    0.00 |    0.00 |         |    NULL |    NULL |
+---------+---------+---------+---------+---------+---------+---------------------+---------------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+------------+------------+------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+

SELECT idsubgr, idcecus, iddepto, idcontr, idconta, serienf FROM abnf_financeiro_movimentacao_registros_financeiros WHERE
idsubgr Is Null or
idcecus Is Null or
iddepto Is Null or
idcontr Is Null or
idconta Is Null or
serienf Is Null;

SELECT idsubgr FROM abnf_financeiro_movimentacao_registros_financeiros WHERE idsubgr IS NULL;
UPDATE *** abnf_financeiro_movimentacao_registros_financeiros SET idsubgr = 166 WHERE idsubgr IS NULL;


SELECT idclfor, idcompl FROM abnf_financeiro_movimentacao_registros_financeiros WHERE idclfor > 0 and idcompl IS NULL;
UPDATE *** abnf_financeiro_movimentacao_registros_financeiros SET idcompl = 0 WHERE idclfor > 0 and idcompl IS NULL;

SELECT idclfor, idcompl FROM abnf_financeiro_movimentacao_registros_financeiros WHERE idclfor IS NULL and idcompl > 0;

SELECT * FROM abnf_financeiro_movimentacao_registros_financeiros WHERE idclfor = 0 and idcompl = 15;
SELECT idclfor, idcompl FROM abnf_financeiro_movimentacao_registros_financeiros WHERE idclfor IS NULL and idcompl IS NULL;
UPDATE *** abnf_financeiro_movimentacao_registros_financeiros SET idclfor = 0, idcompl = 15  WHERE idclfor IS NULL and idcompl IS NULL;

SELECT idsubgr, idclfor, idcompl FROM abnf_financeiro_movimentacao_registros_financeiros WHERE idsubgr IS NULL or idsubgr <= 0 or idclfor IS NULL or idcompl IS NULL or (idclfor <= 0 and idcompl <= 0);

SELECT * FROM abnf_financeiro_movimentacao_registros_financeiros WHERE idcecus IS NULL or idcecus <= 0;
UPDATE *** abnf_financeiro_movimentacao_registros_financeiros SET idcecus = 1 WHERE idcecus IS NULL or idcecus <= 0;

SELECT * FROM abnf_financeiro_movimentacao_registros_financeiros WHERE iddepto IS NULL or iddepto <= 0;
UPDATE *** abnf_financeiro_movimentacao_registros_financeiros SET iddepto = 1 WHERE iddepto IS NULL or iddepto <= 0;

SELECT * FROM abnf_financeiro_movimentacao_registros_financeiros WHERE idcontr IS NULL;
UPDATE *** abnf_financeiro_movimentacao_registros_financeiros SET idcontr = 0 WHERE idcontr IS NULL;

SELECT * FROM abnf_financeiro_movimentacao_registros_financeiros WHERE idconta IS NULL;
UPDATE *** abnf_financeiro_movimentacao_registros_financeiros SET idconta = 0 WHERE idconta IS NULL;

+---------+---------+---------+---------+---------+---------+---------------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+------------+------------+------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
| idregfi | ctrlfin | ctrlpgt | situreg | idusucr | idusual | dtregcr             | dtregal | idfilia | idsubgr | idclfor | idcompl | idcecus | iddepto | idcontr | idconta | tiporeg | modoreg | regiadi | nrdocnf | serienf | idespdo | totparc | numparc | datadoc    | dataven    | datavor    | datapgt | valptdc | valppar | valrtdc | valrpar | valjuro | valcemo | valdesc | valabat | valpago | observa | cglob01 | cglob02 |
+---------+---------+---------+---------+---------+---------+---------------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+------------+------------+------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
|  263021 |  263021 |    NULL | A       |       2 |    NULL | 2024-12-04 10:23:31 | NULL    |       2 |     166 |    8942 |       0 |       1 |       1 |       0 |       0 | D       | R       |       0 |   73351 | NULL    |      40 |       1 |       1 | 2024-11-19 | 2024-11-19 | 2024-11-19 | NULL    |  690.03 |  690.03 |  690.03 |  690.03 |    0.00 |    0.00 |    0.00 |    0.00 |    0.00 |         |    NULL |    NULL |
+---------+---------+---------+---------+---------+---------+---------------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+------------+------------+------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+

SELECT idregfi, datadoc, dataven, datapgt FROM abnf_financeiro_movimentacao_registros_financeiros order by datapgt;
SELECT idregfi, datadoc, dataven, datapgt, idusucr, idusual FROM abnf_financeiro_movimentacao_registros_financeiros where idusucr = 5 or idusual = 5;
UPDATE *** abnf_financeiro_movimentacao_registros_financeiros set idfilia = 3 where idfilia = 1;  60802
UPDATE *** abnf_financeiro_movimentacao_registros_financeiros set idfilia = 1 where idfilia = 2; 201646
UPDATE *** abnf_financeiro_movimentacao_registros_financeiros set idfilia = 2 where idfilia = 3;  60802
SELECT COUNT(*) FROM abnf_financeiro_movimentacao_registros_financeiros; 262448

*** rafael ***

select * from abnf_financeiro_movimentacao_registros_financeiros where idregfi in (265224, 265225);
+---------+---------+---------+---------+---------+---------+---------------------+---------------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+------------+------------+------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
| idregfi | ctrlfin | ctrlpgt | situreg | idusucr | idusual | dtregcr             | dtregal             | idfilia | idsubgr | idclfor | idcompl | idcecus | iddepto | idcontr | idconta | tiporeg | modoreg | regiadi | nrdocnf | serienf | idespdo | totparc | numparc | datadoc    | dataven    | datavor    | datapgt | valptdc | valppar | valrtdc | valrpar | valjuro | valcemo | valdesc | valabat | valpago | observa | cglob01 | cglob02 |
+---------+---------+---------+---------+---------+---------+---------------------+---------------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+------------+------------+------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
|  265229 |  265224 |    NULL | A       |      10 |      10 | 2025-02-06 12:17:18 | 2025-02-06 16:10:19 |       1 |      17 |    7073 |       0 |       1 |       1 |       0 |       0 | D       | R       |       0 |    4487 | U       |      41 |       3 |       1 | 2025-01-13 | 2025-02-05 | 2025-02-05 | NULL    | 3441.00 | 1720.50 | 3441.00 | 1720.50 |    0.00 |    0.00 |    0.00 |    0.00 |    0.00 |         |    NULL |    NULL |
|  265230 |  265225 |    NULL | A       |      10 |      10 | 2025-02-06 12:17:18 | 2025-02-06 16:11:43 |       1 |      17 |    7073 |       0 |       1 |       1 |       0 |       0 | D       | R       |       0 |    4487 | U       |      41 |       1 |       1 | 2025-01-13 | 2025-02-05 | 2025-02-28 | NULL    | 3441.00 | 1720.50 | 3441.00 | 1720.50 |    0.00 |    0.00 |    0.00 |    0.00 |    0.00 |         |    NULL |    NULL |
+---------+---------+---------+---------+---------+---------+---------------------+---------------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+------------+------------+------------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+

select idusuar, logiusu, nomeusu FROM abnf_sistema_usuarios where idusuar = 10;
+---------+---------+--------------------------+
| idusuar | logiusu | nomeusu                  |
+---------+---------+--------------------------+
|      10 | AA.LIMA | AURILENE DE ALMEIDA LIMA |
+---------+---------+--------------------------+

---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░          ░░  ░░░░░░░░░░          ░░  ░░░░░░  ░░          ░░          ░░
░░  ░░░░░░░░░░  ░░░░░░░░░░  ░░░░░░░░░░  ░░░░░░  ░░  ░░░░░░  ░░  ░░░░░░  ░░
▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒
▒▒          ▒▒  ▒▒▒▒▒▒▒▒▒▒          ▒▒  ▒▒▒▒▒▒  ▒▒          ▒▒          ▒▒
▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒▒  ▒▒▒▒▒▒  ▒▒     ▒▒▒▒▒▒▒
██  ██████████  ██████████  ████████████  ██  ████  ██████  ██  ██    ████
██          ██          ██          ██████  ██████  ██████  ██  ████    ██
██████████████████████████████████████████████████████████████████████████
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_elevar_cadastro_passageiros ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_elevar_cadastro_passageiros (
    idepass     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do passageiro do Elevar
    codepas     INT                                         NOT NULL                            ,   # Código do passageiro do Elevar
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    idcpfpj     INT                                         NOT NULL                            ,   # ID cadastro CPF/CNPJ (FK)
    idcidct     INT                                         NOT NULL                            ,   # ID da categoria do CID (FK)
    cadeira     BOOLEAN                                                                         ,   # Cadeirante?
    acompan     BOOLEAN                                                                         ,   # Necessita de acompanhante?
    observa     TEXT                                                                            ,   # Observação
    INDEX abnfdx01 (codepas, idepass)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_elevar_cadastro_passageiros (codepas, idepass);
---------------------------------------------
DROP *** TABLE abnf_elevar_cadastro_passageiros;
DROP *** INDEX abnfdx?? ON abnf_elevar_cadastro_passageiros;
---------------------------------------------
SHOW COLUMNS FROM abnf_elevar_cadastro_passageiros;
SHOW INDEX FROM abnf_elevar_cadastro_passageiros;
---------------------------------------------
SELECT * FROM abnf_elevar_cadastro_passageiros;
DELETE *** FROM abnf_elevar_cadastro_passageiros WHERE idepass = 1;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_elevar_cadastro_locais ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_elevar_cadastro_locais (
    ideloca     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do local do Elevar
    codeloc     INT                                         NOT NULL                            ,   # Código do local do Elevar
    deseloc     VARCHAR(100)                                NOT NULL                            ,   # Descrição do local do Elevar
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    idlogra     INT                                                                             ,   # ID do logradouro (FK)
    logrnum     VARCHAR(20)                                                                     ,   # Logradouro - Número
    logrcom     VARCHAR(100)                                                                    ,   # Logradouro - Complemento
    logrcep     VARCHAR(10)                                                                     ,   # Logradouro - CEP
    pontope     BOOLEAN                                                                         ,   # É um ponto operacional
    chortra     BOOLEAN                                                                         ,   # Conta horários trabalhados
    observa     TEXT                                                                            ,   # Observação
    INDEX abnfdx01 (codeloc, ideloca),
    INDEX abnfdx02 (deseloc, ideloca)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_elevar_cadastro_locais (codeloc, ideloca);
CREATE INDEX abnfdx02 ON abnf_elevar_cadastro_locais (deseloc, ideloca);
---------------------------------------------
DROP *** TABLE abnf_elevar_cadastro_locais;
DROP *** INDEX abnfdx?? ON abnf_elevar_cadastro_locais;
---------------------------------------------
SHOW COLUMNS FROM abnf_elevar_cadastro_locais;
SHOW INDEX FROM abnf_elevar_cadastro_locais;
---------------------------------------------
SELECT * FROM abnf_elevar_cadastro_locais WHERE deseloc LIKE '%STE%';
DELETE *** FROM abnf_elevar_cadastro_locais WHERE ideloca = 1;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_elevar_cadastro_finalidades ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_elevar_cadastro_finalidades (
    idefina     INT                     PRIMARY KEY         NOT NULL                            ,   # ID da finalidade do Elevar
    codefin     INT                                         NOT NULL                            ,   # Código da finalidade do Elevar
    desefin     VARCHAR(100)                                NOT NULL                            ,   # Descrição da finalidade do Elevar
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    INDEX abnfdx01 (codefin, idefina),
    INDEX abnfdx02 (desefin, idefina)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_elevar_cadastro_finalidades (codefin, idefina);
CREATE INDEX abnfdx02 ON abnf_elevar_cadastro_finalidades (desefin, idefina);
---------------------------------------------
DROP *** TABLE abnf_elevar_cadastro_finalidades;
DROP *** INDEX abnfdx?? ON abnf_elevar_cadastro_finalidades;
---------------------------------------------
SHOW COLUMNS FROM abnf_elevar_cadastro_finalidades;
SHOW INDEX FROM abnf_elevar_cadastro_finalidades;
---------------------------------------------
SELECT * FROM abnf_elevar_cadastro_finalidades;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_elevar_cadastro_servicos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_elevar_cadastro_servicos (
    ideserv     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do cadastro de serviço do Elevar
    codeser     INT                                         NOT NULL                            ,   # Código do serviço do Elevar
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    idepass     INT                                         NOT NULL                            ,   # ID do passageiro do Elevar (FK)
    idefina     INT                                         NOT NULL                            ,   # ID da finalidade do Elevar (FK)
    datasol     DATE                                        NOT NULL                            ,   # Data da solicitação
    dataini     DATE                                                                            ,   # Data de início
    datafim     DATE                                                                            ,   # Data de término
    observa     TEXT                                                                            ,   # Observação
    INDEX abnfdx01 (codeser, ideserv)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_elevar_cadastro_servicos (codeser, ideserv);
---------------------------------------------
DROP *** TABLE abnf_elevar_cadastro_servicos;
DROP *** INDEX abnfdx?? ON abnf_elevar_cadastro_servicos;
---------------------------------------------
SHOW COLUMNS FROM abnf_elevar_cadastro_servicos;
SHOW INDEX FROM abnf_elevar_cadastro_servicos;
---------------------------------------------
SELECT * FROM abnf_elevar_cadastro_servicos;
DELETE *** FROM abnf_elevar_cadastro_servicos WHERE ideserv = 1;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_elevar_cadastro_frota_patrimonial ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_elevar_cadastro_frota_patrimonial (
    idefrpa     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do cadastro de frota patrimonial do Elevar
    dataini     DATE                                        NOT NULL                            ,   # Data de início do período
    qtdfrpa     INT                                         NOT NULL                            ,   # Quantidade de frota patrimonial no período
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    INDEX abnfdx01 (dataini, idefrpa)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_elevar_cadastro_frota_patrimonial (dataini, idefrpa);
---------------------------------------------
DROP *** TABLE abnf_elevar_cadastro_frota_patrimonial;
DROP *** INDEX abnfdx?? ON abnf_elevar_cadastro_frota_patrimonial;
---------------------------------------------
SHOW COLUMNS FROM abnf_elevar_cadastro_frota_patrimonial;
SHOW INDEX FROM abnf_elevar_cadastro_frota_patrimonial;
---------------------------------------------
SELECT * FROM abnf_elevar_cadastro_frota_patrimonial;
---------------------------------------------
INSERT *** INTO abnf_elevar_cadastro_frota_patrimonial (idefrpa, dataini, qtdfrpa, situreg, idusucr, dtregcr, idfilia)
VALUES (1, "2023-01-01", 8, "A", 1, CURRENT_TIMESTAMP(), 1);
---------------------------------------------
INSERT *** INTO abnf_elevar_cadastro_frota_patrimonial (idefrpa, dataini, qtdfrpa, situreg, idusucr, dtregcr, idfilia)
VALUES (2, "2023-08-22", 9, "A", 1, CURRENT_TIMESTAMP(), 1);
---------------------------------------------
INSERT *** INTO abnf_elevar_cadastro_frota_patrimonial (idefrpa, dataini, qtdfrpa, situreg, idusucr, dtregcr, idfilia)
VALUES (3, "2023-09-14", 10, "A", 1, CURRENT_TIMESTAMP(), 1);
---------------------------------------------
INSERT *** INTO abnf_elevar_cadastro_frota_patrimonial (idefrpa, dataini, qtdfrpa, situreg, idusucr, dtregcr, idfilia)
VALUES (4, "2023-09-15", 12, "A", 1, CURRENT_TIMESTAMP(), 1);
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_elevar_cadastro_ordens_servico_padrao_grupos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_elevar_cadastro_ordens_servico_padrao_grupos (
    idegopa     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do grupo de ordens de serviço padrão do Elevar
    codegop     INT                                         NOT NULL                            ,   # Código do grupo de ordens de serviço padrão do Elevar
    desegru     VARCHAR(100)                                NOT NULL                            ,   # Descrição do grupo de ordens de serviço padrão do Elevar
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    INDEX abnfdx01 (codegop, idegopa),
    INDEX abnfdx02 (desegru, idegopa)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_elevar_cadastro_ordens_servico_padrao_grupos (codegop, idegopa);
CREATE INDEX abnfdx02 ON abnf_elevar_cadastro_ordens_servico_padrao_grupos (desegru, idegopa);
---------------------------------------------
DROP *** TABLE abnf_elevar_cadastro_ordens_servico_padrao_grupos;
DROP *** INDEX abnfdx?? ON abnf_elevar_cadastro_ordens_servico_padrao_grupos;
---------------------------------------------
SHOW COLUMNS FROM abnf_elevar_cadastro_ordens_servico_padrao_grupos;
SHOW INDEX FROM abnf_elevar_cadastro_ordens_servico_padrao_grupos;
---------------------------------------------
SELECT * FROM abnf_elevar_cadastro_ordens_servico_padrao_grupos;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_elevar_cadastro_ordens_servico_padrao ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_elevar_cadastro_ordens_servico_padrao (
    ideospa     INT                     PRIMARY KEY         NOT NULL                            ,   # ID da ordem de serviço padrão do Elevar
    codeosp     INT                                         NOT NULL                            ,   # Código da ordem de serviço padrão do Elevar
    desemos     VARCHAR(100)                                NOT NULL                            ,   # Descrição da ordem de serviço padrão do Elevar
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    idegopa     INT                                         NOT NULL                            ,   # ID do grupo de ordens de serviço padrão (FK)
    idveicu     INT                                         NOT NULL                            ,   # ID do veículo (FK)
    INDEX abnfdx01 (codeosp, ideospa),
    INDEX abnfdx02 (desemos, ideospa)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_elevar_cadastro_ordens_servico_padrao (codeosp, ideospa);
CREATE INDEX abnfdx02 ON abnf_elevar_cadastro_ordens_servico_padrao (desemos, ideospa);
---------------------------------------------
DROP *** TABLE abnf_elevar_cadastro_ordens_servico_padrao;
DROP *** INDEX abnfdx?? ON abnf_elevar_cadastro_ordens_servico_padrao;
---------------------------------------------
SHOW COLUMNS FROM abnf_elevar_cadastro_ordens_servico_padrao;
SHOW INDEX FROM abnf_elevar_cadastro_ordens_servico_padrao;
---------------------------------------------
SELECT * FROM abnf_elevar_cadastro_ordens_servico_padrao;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_elevar_cadastro_ordens_servico_padrao_itens ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_elevar_cadastro_ordens_servico_padrao_itens (
    ideitop     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do item de ordem de serviço padrão do Elevar
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    ideospa     INT                                         NOT NULL                            ,   # ID da ordem de serviço padrão (FK)
    idfunci     INT                                         NOT NULL                            ,   # ID do funcionário (motorista) (FK)
    ideloca     INT                                         NOT NULL                            ,   # ID do local do Elevar (FK)
    horario     TIME                                        NOT NULL                            ,   # Horário
    ideserv     INT                                                                             ,   # ID do cadastro de serviço do Elevar (FK)
    motivox     VARCHAR(1)                                                                      ,   # Motivo: [E]mbarque/[D]esembarque
    pontope     BOOLEAN                                                                         ,   # Ponto operacional?
    viagimp     BOOLEAN                                                                         ,   # Viagem improdutiva?
    horamot     BOOLEAN                                                                         ,   # Computa hora do motorista?
    INDEX abnfdx01 (horario, ideitop)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_elevar_cadastro_ordens_servico_padrao_itens (horario, ideitop);
---------------------------------------------
DROP *** TABLE abnf_elevar_cadastro_ordens_servico_padrao_itens;
DROP *** INDEX abnfdx?? ON abnf_elevar_cadastro_ordens_servico_padrao_itens;
---------------------------------------------
SHOW COLUMNS FROM abnf_elevar_cadastro_ordens_servico_padrao_itens;
SHOW INDEX FROM abnf_elevar_cadastro_ordens_servico_padrao_itens;
---------------------------------------------
SELECT * FROM abnf_elevar_cadastro_ordens_servico_padrao_itens;
---------------------------------------------
ALTER *** TABLE abnf_elevar_cadastro_ordens_servico_padrao_itens CHANGE horprog horario TIME NOT NULL;
Alterar nos logs: horprog -> horario
---------------------------------------------
ALTER *** TABLE abnf_elevar_cadastro_ordens_servico_padrao_itens ADD COLUMN viagimp BOOLEAN AFTER pontope;
ALTER *** TABLE abnf_elevar_cadastro_ordens_servico_padrao_itens CHANGE improdu viagimp BOOLEAN;
---------------------------------------------
*** Julinha - Verificação de registros excluídos dos ítens do padrão ***

SELECT 

abnf01.ideitop,
abnf05.codeosp,
abnf05.desemos,
abnf02.codeser,
abnf03.codepas,
abnf04.nomraso,
abnf01.dtregal

FROM       abnf_elevar_cadastro_ordens_servico_padrao_itens     AS abnf01
INNER JOIN abnf_elevar_cadastro_servicos                        AS abnf02
INNER JOIN abnf_elevar_cadastro_passageiros                     AS abnf03
INNER JOIN abnf_cadastro_cpfcnpj                                AS abnf04
INNER JOIN abnf_elevar_cadastro_ordens_servico_padrao           AS abnf05

WHERE abnf01.ideserv = abnf02.ideserv
AND   abnf02.idepass = abnf03.idepass
AND   abnf03.idcpfpj = abnf04.idcpfpj
AND   abnf01.ideospa = abnf05.ideospa

AND   abnf01.situreg = "C"

ORDER BY abnf04.nomraso;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_elevar_movimentacao_ordens_servico_diaria ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_elevar_movimentacao_ordens_servico_diaria (
    ideosdi     INT                     PRIMARY KEY         NOT NULL                            ,   # ID da ordem de serviço diária do Elevar
    numeosd     INT                                         NOT NULL                            ,   # Número da ordem de serviço diária do Elevar
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
	dataord     DATE                                        NOT NULL                            ,   # Data da ordem de serviço
    tiporeg     VARCHAR(1)                                  NOT NULL                            ,   # Tipo de registro: [S]istema/[M]anual
    INDEX abnfdx01 (numeosd, ideosdi),
	INDEX abnfdx02 (dataord, numeosd, ideosdi)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_elevar_movimentacao_ordens_servico_diaria (numeosd, ideosdi);
CREATE INDEX abnfdx02 ON abnf_elevar_movimentacao_ordens_servico_diaria (dataord, numeosd, ideosdi);
---------------------------------------------
DROP *** TABLE abnf_elevar_movimentacao_ordens_servico_diaria;
DROP *** INDEX abnfdx?? ON abnf_elevar_movimentacao_ordens_servico_diaria;
---------------------------------------------
SHOW COLUMNS FROM abnf_elevar_movimentacao_ordens_servico_diaria;
SHOW INDEX FROM abnf_elevar_movimentacao_ordens_servico_diaria;
---------------------------------------------
SELECT * FROM abnf_elevar_movimentacao_ordens_servico_diaria;
SELECT * FROM abnf_elevar_movimentacao_ordens_servico_diaria WHERE numeosd = 2880;
---------------------------------------------
(*** Julinha/Bia ***)
SELECT * FROM abnf_elevar_movimentacao_ordens_servico_diaria WHERE numeosd >= 3283 AND numeosd <= 3296;
UPDATE *** abnf_elevar_movimentacao_ordens_servico_diaria SET dataord = '2025-07-01' WHERE numeosd = 2491;
SELECT * FROM abnf_elevar_movimentacao_ordens_servico_diaria WHERE dataord = '2025-09-30';
UPDATE *** abnf_elevar_movimentacao_ordens_servico_diaria SET dataord = '2025-09-23' WHERE dataord = '2025-09-30';
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog (
    ideitod     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do item de ordem de serviço diária do Elevar
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    tiporeg     VARCHAR(1)                                  NOT NULL                            ,   # Tipo de registro: [S]istema/[M]anual
    ideosdi     INT                                         NOT NULL                            ,   # ID da ordem de serviço diária (FK)
    idveicu     INT                                         NOT NULL                            ,   # ID do veículo (FK)
    idfunci     INT                                         NOT NULL                            ,   # ID do funcionário (motorista) (FK)
    ideloca     INT                                         NOT NULL                            ,   # ID do local do Elevar (FK)
    idlogra     INT                                         NOT NULL                            ,   # ID do logradouro (FK)
    logrnum     VARCHAR(20)                                 NOT NULL                            ,   # Logradouro - Número
    logrcom     VARCHAR(100)                                NOT NULL                            ,   # Logradouro - Complemento
    logrcep     VARCHAR(10)                                 NOT NULL                            ,   # Logradouro - CEP
    horario     TIME                                        NOT NULL                            ,   # Horário
    horamin     INT                                                                             ,   # Horário (em minutos)
    ideserv     INT                                                                             ,   # ID do cadastro de serviço do Elevar (FK)
    motivox     VARCHAR(1)                                                                      ,   # Motivo: [E]mbarque/[D]esembarque
    pontope     BOOLEAN                                                                         ,   # Ponto operacional?
    viagimp     BOOLEAN                                                                         ,   # Viagem improdutiva?
    horamot     BOOLEAN                                                                         ,   # Computa hora do motorista?
    observa     TEXT                                                                            ,   # Observação
    INDEX abnfdx01 (ideosdi, horario, ideitod)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog (ideosdi, horario, ideitod);
---------------------------------------------
DROP *** TABLE abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog;
DROP *** INDEX abnfdx?? ON abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog;
---------------------------------------------
SHOW COLUMNS FROM abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog;
SHOW INDEX FROM abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog;
---------------------------------------------
SELECT * FROM abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog;
---------------------------------------------
ALTER *** TABLE abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog DROP COLUMN kmveicu;
---------------------------------------------
ALTER *** TABLE abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog ADD COLUMN viagimp BOOLEAN AFTER pontope;
ALTER *** TABLE abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog CHANGE improdu viagimp BOOLEAN;
---------------------------------------------
ALTER *** TABLE abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog DROP COLUMN horamin;
---------------------------------------------
ALTER *** TABLE abnf_elevar_movimentacao_ordens_servico_diaria_itens_prog ADD COLUMN horamin INT DEFAULT NULL AFTER horario;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_elevar_movimentacao_ordens_servico_diaria_itens_real ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_elevar_movimentacao_ordens_servico_diaria_itens_real (
    ideitod     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do item de ordem de serviço diária do Elevar
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    tiporeg     VARCHAR(1)                                  NOT NULL                            ,   # Tipo de registro: [S]istema/[M]anual
    ideosdi     INT                                         NOT NULL                            ,   # ID da ordem de serviço diária (FK)
    idveicu     INT                                         NOT NULL                            ,   # ID do veículo (FK)
    idfunci     INT                                         NOT NULL                            ,   # ID do funcionário (motorista) (FK)
    ideloca     INT                                         NOT NULL                            ,   # ID do local do Elevar (FK)
    idlogra     INT                                         NOT NULL                            ,   # ID do logradouro (FK)
    logrnum     VARCHAR(20)                                 NOT NULL                            ,   # Logradouro - Número
    logrcom     VARCHAR(100)                                NOT NULL                            ,   # Logradouro - Complemento
    logrcep     VARCHAR(10)                                 NOT NULL                            ,   # Logradouro - CEP
    horario     TIME                                        NOT NULL                            ,   # Horário
    horamin     INT                                                                             ,   # Horário (em minutos)
    ideserv     INT                                                                             ,   # ID do cadastro de serviço do Elevar (FK)
    motivox     VARCHAR(1)                                                                      ,   # Motivo: [E]mbarque/[D]esembarque
    pontope     BOOLEAN                                                                         ,   # Ponto operacional?
    viagimp     BOOLEAN                                                                         ,   # Viagem improdutiva?
    horamot     BOOLEAN                                                                         ,   # Computa hora do motorista?
    observa     TEXT                                                                            ,   # Observação
    horcheg     TIME                                                                            ,   # Horário de chegada
    horcmin     INT                                                                             ,   # Horário de chegada (em minutos)
    horsaid     TIME                                                                            ,   # Horário de saída
    horsmin     INT                                                                             ,   # Horário de saída (em minutos)
    idkmvei     INT                                                                             ,   # Km anotado pelo motorista (FK)
    statreg     INT                                         NOT NULL                            ,   # Status do registro: (1 a 9)
    INDEX abnfdx01 (ideosdi, horario, ideitod)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_elevar_movimentacao_ordens_servico_diaria_itens_real (ideosdi, horario, ideitod);
---------------------------------------------
DROP *** TABLE abnf_elevar_movimentacao_ordens_servico_diaria_itens_real;
DROP *** INDEX abnfdx?? ON abnf_elevar_movimentacao_ordens_servico_diaria_itens_real;
---------------------------------------------
SHOW COLUMNS FROM abnf_elevar_movimentacao_ordens_servico_diaria_itens_real;
SHOW INDEX FROM abnf_elevar_movimentacao_ordens_servico_diaria_itens_real;
---------------------------------------------
SELECT * FROM abnf_elevar_movimentacao_ordens_servico_diaria_itens_real;
---------------------------------------------
Exemplo: ALTER *** TABLE aluno ADD idade INT AFTER nome
---------------------------------------------
ALTER *** TABLE abnf_elevar_movimentacao_ordens_servico_diaria_itens_real DROP COLUMN kmveicu;
ALTER *** TABLE abnf_elevar_movimentacao_ordens_servico_diaria_itens_real ADD horcheg TIME;
ALTER *** TABLE abnf_elevar_movimentacao_ordens_servico_diaria_itens_real ADD horsaid TIME;
ALTER *** TABLE abnf_elevar_movimentacao_ordens_servico_diaria_itens_real ADD idkmvei INT;
---------------------------------------------
ALTER *** TABLE abnf_elevar_movimentacao_ordens_servico_diaria_itens_real ADD statreg INT;
UPDATE *** abnf_elevar_movimentacao_ordens_servico_diaria_itens_real SET statreg = 1;
ALTER *** TABLE abnf_elevar_movimentacao_ordens_servico_diaria_itens_real CHANGE statreg statreg INT NOT NULL;
SELECT statreg FROM abnf_elevar_movimentacao_ordens_servico_diaria_itens_real;
---------------------------------------------
ALTER *** TABLE abnf_elevar_movimentacao_ordens_servico_diaria_itens_real ADD COLUMN viagimp BOOLEAN AFTER pontope;
ALTER *** TABLE abnf_elevar_movimentacao_ordens_servico_diaria_itens_real CHANGE improdu viagimp BOOLEAN;
---------------------------------------------
ALTER *** TABLE abnf_elevar_movimentacao_ordens_servico_diaria_itens_real DROP COLUMN horamin;
ALTER *** TABLE abnf_elevar_movimentacao_ordens_servico_diaria_itens_real DROP COLUMN horcmin;
ALTER *** TABLE abnf_elevar_movimentacao_ordens_servico_diaria_itens_real DROP COLUMN horsmin;
---------------------------------------------
ALTER *** TABLE abnf_elevar_movimentacao_ordens_servico_diaria_itens_real ADD COLUMN horamin INT DEFAULT NULL AFTER horario;
ALTER *** TABLE abnf_elevar_movimentacao_ordens_servico_diaria_itens_real ADD COLUMN horcmin INT DEFAULT NULL AFTER horcheg;
ALTER *** TABLE abnf_elevar_movimentacao_ordens_servico_diaria_itens_real ADD COLUMN horsmin INT DEFAULT NULL AFTER horsaid;
---------------------------------------------
SELECT ideosdi, statreg FROM abnf_elevar_movimentacao_ordens_servico_diaria_itens_real WHERE statreg = 5;

SELECT * FROM abnf_elevar_movimentacao_ordens_servico_diaria WHERE ideosdi = 214;

8273 -> 6994 + 2 + 1191 + 84 + 2 = 8273

statreg 01 -> NORMAL
statreg 02 -> CANCELADO PELA EMPRESA
statreg 03 -> CANCELADO PELO USUARIO
statreg 04 -> CANCELADO NA PORTA
statreg 05 -> TRANSFERIDO
statreg 06 -> NAO CONCLUIDO -> FALHA MECANICA E/OU ELETRICA
statreg 07 -> NAO CONCLUIDO -> MOTIVOS DIVERSOS
statreg 08 -> ADIANTO
statreg 09 -> ATRASO

Tabela Alpha:

-> Viagens programada 01 ................... [A][01]: Tudo o que for statreg 01, 02, 03, 04, 06, 07, 08 e 09
-> Viagens canceladas pelo usuário ......... [B][02]: Tudo o que for statreg 03 e 04
-> Viagens programada 02 ................... [C][03]: Cálculo: A-B
-> Partida não realizada ................... [D][04]: Tudo o que for statreg 02
-> Viagem não concluída .................... [E][05]: Tudo o que for statreg 06 e 07
-> Viagem realizada ........................ [F][06]: Cálculo: C-D-E
-> Partida em adianto ...................... [G][07]: Tudo o que for statreg 08
-> Partida em atraso ....................... [H][08]: Tudo o que for statreg 09
-> Partida no horário ...................... [I][09]: Cálculo: F-G-H
-> Viagens iniciadas ....................... [J][10]: Cálculo: C-D
-> Viagens não concluídas (falhas) ......... [K][11]: Tudo o que for statreg 06
---------------------------------------------
Levantamento para Vanderlei sobre finalidade de viagens do Elevar mês a mês:

SELECT abnf04.desefin, TO_CHAR(abnf02.dataord, "YYYY-MM") AS ano_mes, COUNT(*) AS total

FROM       abnf_elevar_movimentacao_ordens_servico_diaria_itens_real as abnf01

INNER JOIN abnf_elevar_movimentacao_ordens_servico_diaria            as abnf02
ON         abnf01.ideosdi = abnf02.ideosdi

INNER JOIN abnf_elevar_cadastro_servicos                             as abnf03
ON         abnf01.ideserv = abnf03.ideserv

INNER JOIN abnf_elevar_cadastro_finalidades                          as abnf04
ON         abnf03.idefina = abnf04.idefina

WHERE

abnf01.statreg = 1 AND
abnf01.motivox = "E"

GROUP BY -- Agrupa pelas 3 colunas que definem a unicidade
    TO_CHAR(abnf02.dataord, "YYYY-MM"),
    abnf04.desefin
ORDER BY -- Opcional: Para deixar a visualização mais organizada
    abnf04.desefin, TO_CHAR(abnf02.dataord, "YYYY-MM");
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░          ░░          ░░          ░░
░░  ░░░░░░░░░░  ░░░░░░  ░░  ░░░░░░░░░░
▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒
▒▒          ▒▒          ▒▒  ▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒
██████████  ██  ██████  ██  ██████████
██          ██  ██████  ██          ██
██████████████████████████████████████
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_sac_cadastro_usuarios_grupos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sac_cadastro_usuarios_grupos (
    idsusgr     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do grupo de usuarios do SAC
    codsusg     INT                                         NOT NULL                            ,   # Código do grupo de usuarios do SAC
    dessusg     VARCHAR(100)                                NOT NULL                            ,   # Descrição do grupo de usuarios do SAC
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    emailgr     VARCHAR(100)                                                                    ,   # E-mail do grupo
    envpref     VARCHAR(1)                                  NOT NULL                            ,   # Envia dados para prefeitura? (S/N)
    INDEX abnfdx01 (codsusg, idsusgr),
    INDEX abnfdx02 (dessusg, idsusgr)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sac_cadastro_usuarios_grupos (codsusg, idsusgr);
CREATE INDEX abnfdx02 ON abnf_sac_cadastro_usuarios_grupos (dessusg, idsusgr);
---------------------------------------------
SHOW COLUMNS FROM abnf_sac_cadastro_usuarios_grupos;
SHOW INDEX FROM abnf_sac_cadastro_usuarios_grupos;
SELECT * FROM abnf_sac_cadastro_usuarios_grupos;
DROP *** TABLE abnf_sac_cadastro_usuarios_grupos;
---------------------------------------------
INSERT INTO abnf_sac_cadastro_usuarios_grupos (idsusgr, codsusg, dessusg, situreg, idusucr, dtregcr, idfilia, emailgr) VALUES
(??, ??, ??, "A", 1, CURRENT_TIMESTAMP(), ??, ??);
---------------------------------------------
UPDATE *** abnf_sac_cadastro_usuarios_grupos SET emailgr = 'SAC@TUPITRANSPORTE.COM.BR' WHERE idsusgr = 1;MONITORAMENTOS & TREINAMENTOS
---------------------------------------------
ALTER *** TABLE abnf_sac_cadastro_usuarios_grupos ADD COLUMN envpref VARCHAR(1) NOT NULL DEFAULT 'N';
UPDATE *** abnf_sac_cadastro_usuarios_grupos SET dessusg = "MONITORAMENTOS & TREINAMENTOS" WHERE idsusgr = 17;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_sac_cadastro_usuarios_grupos_vinculos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sac_cadastro_usuarios_grupos_vinculos (
    idsugvi     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do vinculo de grupos de usuarios do SAC
	idsusgr     INT                                         NOT NULL                            ,   # ID do grupo de usuarios do SAC (FK)
	idusuar     INT                                         NOT NULL                            ,   # ID do usuário (FK)
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (idsusgr, idusuar, idsugvi)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sac_cadastro_usuarios_grupos_vinculos (idsusgr, idusuar, idsugvi);
---------------------------------------------
SHOW COLUMNS FROM abnf_sac_cadastro_usuarios_grupos_vinculos;
SHOW INDEX FROM abnf_sac_cadastro_usuarios_grupos_vinculos;
SELECT * FROM abnf_sac_cadastro_usuarios_grupos_vinculos;
SELECT * FROM abnf_sac_cadastro_usuarios_grupos_vinculos WHERE idusuar in (40);
SELECT * FROM abnf_sac_cadastro_usuarios_grupos_vinculos WHERE idsusgr = 1;
DROP *** TABLE abnf_sac_cadastro_usuarios_grupos_vinculos;
---------------------------------------------
SELECT idusuar, logiusu, nomeusu, situreg, idgrams FROM abnf_sistema_usuarios WHERE
nomeusu LIKE '%VANUSS%';
---------------------------------------------
SELECT 
abnf01.idsusgr, abnf01.codsusg, abnf01.dessusg, abnf02.idusuar, abnf03.nomeusu, abnf03.situreg
FROM       abnf_sac_cadastro_usuarios_grupos          AS abnf01
INNER JOIN abnf_sac_cadastro_usuarios_grupos_vinculos AS abnf02
INNER JOIN abnf_sistema_usuarios                      AS abnf03
WHERE abnf01.idsusgr = abnf02.idsusgr
AND   abnf02.idusuar = abnf03.idusuar
AND   abnf01.situreg = "A"
AND   abnf02.situreg = "A"
AND   abnf03.situreg = "A"
ORDER BY abnf01.dessusg, abnf03.nomeusu;
---------------------------------------------
INSERT *** INTO abnf_sac_cadastro_usuarios_grupos_vinculos (idsugvi, idsusgr, idusuar, situreg, idusucr, dtregcr) VALUES
(100, 15, 40, "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
UPDATE *** abnf_sac_cadastro_usuarios_grupos_vinculos SET situreg = "C", idusual = 1, dtregal = CURRENT_TIMESTAMP() WHERE idsugvi = ??;
UPDATE *** abnf_sac_cadastro_usuarios_grupos_vinculos SET idsusgr = 15 WHERE idsugvi = ??;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_sac_cadastro_atendimentos_canais ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sac_cadastro_atendimentos_canais (
    idsatca     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do canal de atendimento do SAC
    codsatc     INT                                         NOT NULL                            ,   # Código do canal de atendimento do SAC
    dessatc     VARCHAR(100)                                NOT NULL                            ,   # Descrição do canal de atendimento do SAC
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    INDEX abnfdx01 (codsatc, idsatca),
    INDEX abnfdx02 (dessatc, idsatca)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sac_cadastro_atendimentos_canais (codsatc, idsatca);
CREATE INDEX abnfdx02 ON abnf_sac_cadastro_atendimentos_canais (dessatc, idsatca);
---------------------------------------------
SHOW COLUMNS FROM abnf_sac_cadastro_atendimentos_canais;
SHOW INDEX FROM abnf_sac_cadastro_atendimentos_canais;
SELECT * FROM abnf_sac_cadastro_atendimentos_canais;
DROP *** TABLE abnf_sac_cadastro_atendimentos_canais;
---------------------------------------------
INSERT *** INTO abnf_sac_cadastro_atendimentos_canais (idsatca, codsatc, dessatc, situreg, idusucr, dtregcr, idfilia) VALUES
(12, 12, '156', "A", 1, CURRENT_TIMESTAMP(), 3);
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_sac_cadastro_atendimentos_tipos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sac_cadastro_atendimentos_tipos (
    idsatti     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do tipo de atendimento do SAC
    codsatt     INT                                         NOT NULL                            ,   # Código do tipo de atendimento do SAC
    dessatt     VARCHAR(100)                                NOT NULL                            ,   # Descrição do tipo de atendimento do SAC
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    INDEX abnfdx01 (codsatt, idsatti),
    INDEX abnfdx02 (dessatt, idsatti)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sac_cadastro_atendimentos_tipos (codsatt, idsatti);
CREATE INDEX abnfdx02 ON abnf_sac_cadastro_atendimentos_tipos (dessatt, idsatti);
---------------------------------------------
SHOW COLUMNS FROM abnf_sac_cadastro_atendimentos_tipos;
SHOW INDEX FROM abnf_sac_cadastro_atendimentos_tipos;
SELECT * FROM abnf_sac_cadastro_atendimentos_tipos;
DROP *** TABLE abnf_sac_cadastro_atendimentos_tipos;
---------------------------------------------
INSERT *** INTO abnf_sac_cadastro_atendimentos_tipos (idsatti, codsatt, dessatt, situreg, idusucr, dtregcr, idfilia) VALUES
(??, ??, '???', "A", 1, CURRENT_TIMESTAMP(), 3);
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_sac_cadastro_atendimentos_grupos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sac_cadastro_atendimentos_grupos (
    idsatgr     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do grupo de atendimento do SAC
    codsatg     INT                                         NOT NULL                            ,   # Código do grupo de atendimento do SAC
    dessatg     VARCHAR(100)                                NOT NULL                            ,   # Descrição do grupo de atendimento do SAC
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    INDEX abnfdx01 (codsatg, idsatgr),
    INDEX abnfdx02 (dessatg, idsatgr)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sac_cadastro_atendimentos_grupos (codsatg, idsatgr);
CREATE INDEX abnfdx02 ON abnf_sac_cadastro_atendimentos_grupos (dessatg, idsatgr);
---------------------------------------------
SHOW COLUMNS FROM abnf_sac_cadastro_atendimentos_grupos;
SHOW INDEX FROM abnf_sac_cadastro_atendimentos_grupos;
SELECT * FROM abnf_sac_cadastro_atendimentos_grupos;
DROP *** TABLE abnf_sac_cadastro_atendimentos_grupos;
---------------------------------------------
INSERT *** INTO abnf_sac_cadastro_atendimentos_grupos (idsatgr, codsatg, dessatg, situreg, idusucr, dtregcr, idfilia) VALUES
(29, 29, 'TT - ROTINA INSTRUTOR', "A", 1, CURRENT_TIMESTAMP(), 3);
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_sac_cadastro_atendimentos_subgrupos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sac_cadastro_atendimentos_subgrupos (
    idsatsg     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do subgrupo de atendimento do SAC
    codsats     INT                                         NOT NULL                            ,   # Código do subgrupo de atendimento do SAC
    dessats     VARCHAR(100)                                NOT NULL                            ,   # Descrição do subgrupo de atendimento do SAC
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idsatgr     INT                                         NOT NULL                            ,   # ID do grupo de atendimento do SAC (FK)
    envpref     VARCHAR(1)                                  NOT NULL                            ,   # Envia dados para prefeitura? (S/N)
    INDEX abnfdx01 (codsats, idsatsg),
    INDEX abnfdx02 (dessats, idsatsg)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sac_cadastro_atendimentos_subgrupos (codsats, idsatsg);
CREATE INDEX abnfdx02 ON abnf_sac_cadastro_atendimentos_subgrupos (dessats, idsatsg);
---------------------------------------------
SHOW COLUMNS FROM abnf_sac_cadastro_atendimentos_subgrupos;
SHOW INDEX FROM abnf_sac_cadastro_atendimentos_subgrupos;
SELECT * FROM abnf_sac_cadastro_atendimentos_subgrupos; WHERE idsatgr = 9 order by dessats;
DROP *** TABLE abnf_sac_cadastro_atendimentos_subgrupos;
---------------------------------------------
SELECT
abnf01.idsatgr,
abnf01.codsatg,
abnf01.dessatg,
abnf02.idsatsg,
abnf02.codsats,
abnf02.idsatsg,
abnf02.dessats,
abnf02.envpref
envpref
FROM       abnf_sac_cadastro_atendimentos_grupos    as abnf01
INNER JOIN abnf_sac_cadastro_atendimentos_subgrupos as abnf02
ON         abnf01.idsatgr = abnf02.idsatgr
WHERE
-- abnf01.dessatg LIKE '%M%'
abnf02.dessats LIKE '%MUL%'
ORDER BY
abnf01.codsatg, abnf02.codsats;
-- abnf02.idsatsg;
---------------------------------------------
INSERT INTO abnf_sac_cadastro_atendimentos_subgrupos (idsatsg, codsats, dessats, situreg, idusucr, dtregcr, idsatgr) VALUES
(126, 31, '', "A", 1, CURRENT_TIMESTAMP(), 9);
UPDATE abnf_sac_cadastro_atendimentos_subgrupos SET dessats = 'MULTA' where idsatsg = 126;    
---------------------------------------------
ALTER *** TABLE abnf_sac_cadastro_atendimentos_subgrupos ADD COLUMN envpref VARCHAR(1) NOT NULL DEFAULT 'N';
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_sac_movimentacao_atendimentos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sac_movimentacao_atendimentos(
    idsaten     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do atendimento do SAC
    codsate     INT                                         NOT NULL                            ,   # Código do atendimento do SAC
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    situate     INT                                         NOT NULL                            ,   # Situação do atendimento: [1]=Aberto/[2]=Em tratativa/[3]=Encerrado
    dataabe     DATE                                        NOT NULL                            ,   # Data de abertura
    horaabe     TIME                                        NOT NULL                            ,   # Horário de abertura
    datafec     DATE                                                                            ,   # Data de fechamento
    horafec     TIME                                                                            ,   # Horário de fechamento
    dataoco     DATE                                        NOT NULL                            ,   # Data da ocorrência
    horaoco     TIME                                        NOT NULL                            ,   # Horário da ocorrência
    idsatca     INT                                         NOT NULL                            ,   # ID do canal de atendimento do SAC (FK)
    idsatti     INT                                         NOT NULL                            ,   # ID do tipo de atendimento do SAC (FK)
    idsatsg     INT                                         NOT NULL                            ,   # ID do subgrupo de atendimento do SAC (FK)
    idfunci     INT                                                                             ,   # ID do funcionário envolvido (FK)
    idveicu     INT                                                                             ,   # ID do veículo envolvido (FK)
    idolinh     INT                                                                             ,   # ID da linha da operação envolvida (FK)
    descroc     TEXT                                                                            ,   # Descrição da ocorrência
    idcpfcl     INT                                                                             ,   # ID do cliente (cadastrado) (FK)
    nomecli     VARCHAR(100)                                                                    ,   # Nome do cliente (não cadastrado)
    contato     VARCHAR(100)                                                                    ,   # Contato do cliente (não cadastrado)
    idsusab     INT                                         NOT NULL                            ,   # ID do grupo de usuarios do SAC que abriu o atendimento (FK)
    idsusde     INT                                                                             ,   # ID do grupo de usuarios do SAC que foi destinado o atendimento (FK)
    INDEX abnfdx01 (codsate, idsaten),
    INDEX abnfdx02 (dataabe, horaabe, idsaten),
    INDEX abnfdx03 (dataoco, horaoco, idsaten)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sac_movimentacao_atendimentos (codsate, idsaten);
CREATE INDEX abnfdx02 ON abnf_sac_movimentacao_atendimentos (dataabe, horaabe, idsaten);
CREATE INDEX abnfdx03 ON abnf_sac_movimentacao_atendimentos (dataoco, horaoco, idsaten);
---------------------------------------------
SHOW COLUMNS FROM abnf_sac_movimentacao_atendimentos;
SHOW INDEX FROM abnf_sac_movimentacao_atendimentos;
SELECT * FROM abnf_sac_movimentacao_atendimentos;
DROP *** TABLE abnf_sac_movimentacao_atendimentos;
---------------------------------------------
ALTER *** TABLE abnf_sac_movimentacao_atendimentos ADD COLUMN idcpfcl INT AFTER descroc;
ALTER *** TABLE abnf_sac_movimentacao_atendimentos ADD COLUMN idsatca INT NOT NULL AFTER horaoco;
---------------------------------------------
SELECT idsaten, dtregal, datafec, horafec FROM abnf_sac_movimentacao_atendimentos WHERE idsaten = 127;
SELECT idsaten, dtregal, datafec, horafec FROM abnf_sac_movimentacao_atendimentos WHERE idsaten = 489;
SELECT idsaten, dtregal, datafec, horafec, situreg FROM abnf_sac_movimentacao_atendimentos WHERE codsate = 33719;
UPDATE *** abnf_sac_movimentacao_atendimentos SET datafec = dtregal, horafec = dtregal WHERE idsaten = 127;
UPDATE *** abnf_sac_movimentacao_atendimentos SET datafec = dtregal, horafec = dtregal WHERE idsaten = 489;
UPDATE *** abnf_sac_movimentacao_atendimentos SET datafec = dtregal, horafec = dtregal WHERE idsaten = 588;
---------------------------------------------
*** Correção em palavras erradas nos descritivos do SAC ***
UPDATE *** abnf_sac_movimentacao_atendimentos SET descroc = REPLACE(descroc, 'ATROPLEOU', 'ATROPELOU') WHERE codsate = 33190;
---------------------------------------------
*** patrícia *** reabertura de atendimento do SAC - arrumar - abrir atendimento ***
SELECT codsate, datafec, horafec, situate FROM abnf_sac_movimentacao_atendimentos WHERE codsate in (50235);
UPDATE abnf_sac_movimentacao_atendimentos SET situate = 1, datafec = Null, horafec = Null WHERE codsate in (50235);
---------------------------------------------
No MariaDB eu tenho uma tabela chamada abnf_sac_movimentacao_atendimentos a qual tem um campo text chamado descroc.
Esse campo tem varios textos cadastrados pelos usuários os quais inseriram ';' dentro do texto.
Tem como usar um comando SQL para que varre todos os registros dessa tabela e nesse campo substitua todos os ';' por ','?
SELECT descroc FROM abnf_sac_movimentacao_atendimentos WHERE codsate = 38994;
UPDATE *** abnf_sac_movimentacao_atendimentos SET descroc = REPLACE(descroc, ';', ',');
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_sac_movimentacao_atendimentos_complementos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sac_movimentacao_atendimentos_complementos(
    idsatco     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do complemento de atendimento do SAC
	idsaten     INT                                         NOT NULL                            ,   # ID do atendimento do SAC (FK)
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    datacom     DATE                                        NOT NULL                            ,   # Data do complemento
    horacom     TIME                                        NOT NULL                            ,   # Horário do complemento
    descrco     TEXT                                        NOT NULL                            ,   # Descrição do complemento
    idsusab     INT                                         NOT NULL                            ,   # ID do grupo de usuarios do SAC que abriu o complemento (FK)
    idsusde     INT                                         NOT NULL                            ,   # ID do grupo de usuarios do SAC que foi destinado o complemento (FK)
    INDEX abnfdx01 (datacom, horacom, idsatco)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sac_movimentacao_atendimentos_complementos (datacom, horacom, idsatco);
---------------------------------------------
SHOW COLUMNS FROM abnf_sac_movimentacao_atendimentos_complementos;
SHOW INDEX FROM abnf_sac_movimentacao_atendimentos_complementos;
SELECT * FROM abnf_sac_movimentacao_atendimentos_complementos;
DROP *** TABLE abnf_sac_movimentacao_atendimentos_complementos;
---------------------------------------------
UPDATE *** abnf_sac_movimentacao_atendimentos_complementos SET situreg = 'A' WHERE idsatco = 78;
---------------------------------------------
*** Correção de textos nos descritivos dos complementos do SAC ***
SELECT * from abnf_sac_movimentacao_atendimentos_complementos WHERE idsaten = 40750;
UPDATE *** abnf_sac_movimentacao_atendimentos_complementos SET descrco = 'CONDUTOR ORIENTADO EM 14/05/25 A FICAR ATENTO AO TRAJETO A SER REALIZADO.' WHERE idsatco = 2846;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_sac_movimentacao_atendimentos_arquivos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sac_movimentacao_atendimentos_arquivos(
	idsatar     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do arquivo de atendimento do SAC
	idsaten     INT                                         NOT NULL                            ,   # ID do atendimento do SAC (FK)
    idsatco     INT                                         NOT NULL                            ,   # ID do complemento de atendimento do SAC
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idarqui     INT                                                                             ,   # ID do arquivo (FK)
    INDEX abnfdx01 (idsaten, idsatco, idsatar)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sac_movimentacao_atendimentos_arquivos (idsaten, idsatco, idsatar);
---------------------------------------------
SHOW COLUMNS FROM abnf_sac_movimentacao_atendimentos_arquivos;
SHOW INDEX FROM abnf_sac_movimentacao_atendimentos_arquivos;
SELECT * FROM abnf_sac_movimentacao_atendimentos_arquivos;
DROP *** TABLE abnf_sac_movimentacao_atendimentos_arquivos;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░          ░░          ░░          ░░          ░░          ░░          ░░  ░░          ░░   ░░░░░  ░░          ░░  ░░░░░░░░░░
░░  ░░░░░░  ░░  ░░░░░░  ░░  ░░░░░░░░░░  ░░░░░░  ░░  ░░░░░░  ░░  ░░░░░░░░░░  ░░  ░░░░░░  ░░    ░░░░  ░░  ░░░░░░  ░░  ░░░░░░░░░░
▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒  ▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒
▒▒  ▒▒▒▒▒▒  ▒▒          ▒▒          ▒▒          ▒▒          ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒  ▒▒  ▒▒          ▒▒  ▒▒▒▒▒▒▒▒▒▒
▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒  ▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒
██  ██████  ██  ██████████  ██████████  ██    ████  ██████  ██  ██████████  ██  ██████  ██  ████    ██  ██████  ██  ██████████
██          ██  ██████████          ██  ████    ██  ██████  ██          ██  ██          ██  █████   ██  ██████  ██          ██
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_cadastro_locais ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_cadastro_locais (
    idoloca     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do local
    codoloc     INT                                         NOT NULL                            ,   # Código do local
    desoloc     VARCHAR(100)                                NOT NULL                            ,   # Descrição do local
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    idlogra     INT                                                                             ,   # ID do logradouro (FK)
    logrnum     VARCHAR(20)                                                                     ,   # Logradouro - Número
    logrcom     VARCHAR(100)                                                                    ,   # Logradouro - Complemento
    logrcep     VARCHAR(10)                                                                     ,   # Logradouro - CEP
    observa     TEXT                                                                            ,   # Observação
    saidgar     BOOLEAN                                     NOT NULL    DEFAULT FALSE           ,   # Saída da garagem?
    INDEX abnfdx01 (codoloc, idoloca),
    INDEX abnfdx02 (desoloc, idoloca)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_cadastro_locais (codoloc, idoloca);
CREATE INDEX abnfdx02 ON abnf_operacional_cadastro_locais (desoloc, idoloca);
---------------------------------------------
DROP *** TABLE abnf_operacional_cadastro_locais;
DROP *** INDEX abnfdx?? ON abnf_operacional_cadastro_locais;
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_cadastro_locais;
SHOW INDEX FROM abnf_operacional_cadastro_locais;
---------------------------------------------
SELECT * FROM abnf_operacional_cadastro_locais WHERE codoloc = 47;
DELETE *** FROM abnf_operacional_cadastro_locais WHERE codoloc = 1;
SELECT * FROM abnf_operacional_cadastro_locais WHERE desoloc LIKE '%STENI%';
---------------------------------------------
ALTER *** TABLE abnf_operacional_cadastro_locais ADD COLUMN saidgar BOOLEAN NOT NULL DEFAULT FALSE AFTER observa;
UPDATE *** abnf_operacional_cadastro_locais SET saidgar = TRUE WHERE codoloc = 47;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_cadastro_grupos_linhas ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_cadastro_grupos_linhas (
    idogrli     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do grupo da linha
	codogrl     INT                                         NOT NULL                            ,   # Código do grupo da linha
    desogrl     VARCHAR(100)                                NOT NULL                            ,   # Descrição do grupo da linha
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    INDEX abnfdx01 (codogrl, idogrli),
    INDEX abnfdx02 (desogrl, idogrli)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_cadastro_grupos_linhas (codogrl, idogrli);
CREATE INDEX abnfdx02 ON abnf_operacional_cadastro_grupos_linhas (desogrl, idogrli);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_cadastro_grupos_linhas;
SHOW INDEX FROM abnf_operacional_cadastro_grupos_linhas;
SELECT * FROM abnf_operacional_cadastro_grupos_linhas;
DROP *** TABLE abnf_operacional_cadastro_grupos_linhas;
---------------------------------------------
INSERT *** INTO abnf_operacional_cadastro_grupos_linhas (idogrli, codogrl, desogrl, situreg, idusucr, dtregcr, idfilia) VALUES
(?, ?, '???', "A", 1, CURRENT_TIMESTAMP(), 2);
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_cadastro_linhas ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_cadastro_linhas (
    idolinh     INT                     PRIMARY KEY         NOT NULL                            ,   # ID da linha
	codolin     VARCHAR(20)                                 NOT NULL                            ,   # Código da linha
    desolin     VARCHAR(100)                                NOT NULL                            ,   # Descrição da linha
    idogrli     INT                                         NOT NULL                            ,   # ID do grupo da linha (FK)
    qtporve     INT                                                                             ,   # Quantidade padrão de portas dos veículos da linha
    perqtpd     BOOLEAN                                                                         ,   # Permite veículos com quantidade de portas divergente do padrão
    perveca     BOOLEAN                                                                         ,   # Permite veículos com ar-condicionado
    pervesa     BOOLEAN                                                                         ,   # Permite veículos sem ar-condicionado
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    INDEX abnfdx01 (codolin, idolinh),
    INDEX abnfdx02 (desolin, idolinh)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_cadastro_linhas (codolin, idolinh);
CREATE INDEX abnfdx02 ON abnf_operacional_cadastro_linhas (desolin, idolinh);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_cadastro_linhas;
SHOW INDEX FROM abnf_operacional_cadastro_linhas;
SELECT * FROM abnf_operacional_cadastro_linhas;
SELECT * FROM abnf_operacional_cadastro_linhas WHERE desolin LIKE '%TAQUA%';
SELECT * FROM abnf_operacional_cadastro_linhas WHERE codolin = 504;
SELECT * FROM abnf_operacional_cadastro_linhas WHERE idogrli = 3;
DROP *** TABLE abnf_operacional_cadastro_linhas;
---------------------------------------------
ALTER *** TABLE abnf_operacional_cadastro_linhas MODIFY COLUMN idogrli INT AFTER desolin;
ALTER *** TABLE abnf_operacional_cadastro_linhas RENAME COLUMN limitkm TO qtporve;
ALTER *** TABLE abnf_operacional_cadastro_linhas MODIFY COLUMN qtporve INT AFTER idogrli;
ALTER *** TABLE abnf_operacional_cadastro_linhas ADD COLUMN perqtpd BOOLEAN AFTER qtporve;
ALTER *** TABLE abnf_operacional_cadastro_linhas ADD COLUMN perveca BOOLEAN AFTER perqtpd;
ALTER *** TABLE abnf_operacional_cadastro_linhas ADD COLUMN pervesa BOOLEAN AFTER perveca;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_cadastro_projetos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_cadastro_projetos (
    idoproj     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do projeto
	codopro     INT                                         NOT NULL                            ,   # Código do projeto
    desopro     VARCHAR(100)                                NOT NULL                            ,   # Descrição do projeto
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    INDEX abnfdx01 (codopro, idoproj),
    INDEX abnfdx02 (desopro, idoproj)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_cadastro_projetos (codopro, idoproj);
CREATE INDEX abnfdx02 ON abnf_operacional_cadastro_projetos (desopro, idoproj);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_cadastro_projetos;
SHOW INDEX FROM abnf_operacional_cadastro_projetos;
SELECT * FROM abnf_operacional_cadastro_projetos;
DROP *** TABLE abnf_operacional_cadastro_projetos;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_cadastro_trajetos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_cadastro_trajetos (
    idotraj     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do trajeto
    idoproj     INT                                         NOT NULL                            ,   # ID do projeto (FK)
    idolinh     INT                                         NOT NULL                            ,   # ID da linha (FK)
    codotra     VARCHAR(4)                                  NOT NULL                            ,   # Código do trajeto
    desotra     VARCHAR(200)                                NOT NULL                            ,   # Descrição do trajeto
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    kmidaxx     DECIMAL(8,1)                                NOT NULL    DEFAULT 0.0             ,   # Km ida
    kmvolta     DECIMAL(8,1)                                NOT NULL    DEFAULT 0.0             ,   # Km volta
    INDEX abnfdx01 (idoproj, idolinh, codotra)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_cadastro_trajetos (idolinh, codotra);
---------------------------------------------
DROP *** TABLE abnf_operacional_cadastro_trajetos;
DROP *** INDEX abnfdx?? ON abnf_operacional_cadastro_trajetos;
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_cadastro_trajetos;
SHOW INDEX FROM abnf_operacional_cadastro_trajetos;
SELECT * FROM abnf_operacional_cadastro_trajetos;
DROP *** TABLE abnf_operacional_cadastro_trajetos;
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_cadastro_trajetos;
ALTER *** TABLE abnf_operacional_cadastro_trajetos ADD COLUMN idoproj INT NOT NULL AFTER idotraj;
SHOW COLUMNS FROM abnf_operacional_cadastro_trajetos;
SHOW INDEX FROM abnf_operacional_cadastro_trajetos;
ALTER *** TABLE abnf_operacional_cadastro_trajetos DROP INDEX abnfdx01;
ALTER *** TABLE abnf_operacional_cadastro_trajetos ADD INDEX abnfdx01 (idoproj, idolinh, codotra);
SHOW INDEX FROM abnf_operacional_cadastro_trajetos;
SELECT * FROM abnf_operacional_cadastro_trajetos;
UPDATE *** abnf_operacional_cadastro_trajetos SET idoproj = 1;
SELECT * FROM abnf_operacional_cadastro_trajetos;
SELECT * FROM abnf_sistema_modulos_acessos WHERE codmodu LIKE '%13C00%' ORDER BY codmodu, idgrams;
UPDATE *** abnf_sistema_modulos_acessos SET situreg = 'C' WHERE codmodu = '13C00700A';
ls /flexgb/abnfsrc/abnf000u13c00700.py
r***m /flexgb/abnfsrc/abnf000u13c00700.py
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_cadastro_itinerarios ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_cadastro_itinerarios (
    idoitin     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do itinerario
    idotraj     INT                                         NOT NULL                            ,   # ID do trajeto (FK)
    sentido     VARCHAR(1)                                  NOT NULL                            ,   # Sentido: [I]da/[V]olta
    ordemit     INT                                         NOT NULL                            ,   # Ordem no itinerário
    idlogra     INT                                         NOT NULL                            ,   # ID do logradouro (FK)
    complem     VARCHAR(100)                                                                    ,   # Complemento
    destaqu     BOOLEAN                                                                         ,   # Destaque?
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (idotraj, sentido, ordemit, idoitin)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_cadastro_itinerarios (idotraj, sentido, ordemit, idoitin);
---------------------------------------------
DROP *** TABLE abnf_operacional_cadastro_itinerarios;
DROP *** INDEX abnfdx?? ON abnf_operacional_cadastro_itinerarios;
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_cadastro_itinerarios;
SHOW INDEX FROM abnf_operacional_cadastro_itinerarios;
SELECT * FROM abnf_operacional_cadastro_itinerarios;
DROP *** TABLE abnf_operacional_cadastro_itinerarios;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_cadastro_grupos_veiculos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_cadastro_grupos_veiculos (
    idogrve     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do registro do grupo de veículo
	codogrf     INT                                         NOT NULL                            ,   # Código do grupo de veículo
	descgrf     VARCHAR(100)                                NOT NULL                            ,   # Descrição do grupo de veículo
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    INDEX abnfdx01 (codogrf, descgrf, idogrve),
    INDEX abnfdx02 (descgrf, codogrf, idogrve)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_cadastro_grupos_veiculos (codogrf, descgrf, idogrve);
CREATE INDEX abnfdx02 ON abnf_operacional_cadastro_grupos_veiculos (descgrf, codogrf, idogrve);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_cadastro_grupos_veiculos;
SHOW INDEX FROM abnf_operacional_cadastro_grupos_veiculos;
SELECT * FROM abnf_operacional_cadastro_grupos_veiculos;
DROP *** TABLE abnf_operacional_cadastro_grupos_veiculos;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_cadastro_grupos_veiculos_vinculos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_cadastro_grupos_veiculos_vinculos (
    idogrvv     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do registro de vínculo do grupo ao veículos
	idogrve     INT                                         NOT NULL                            ,   # ID do registro do grupo de veículo (FK)
    idveicu     INT                                                                             ,   # ID do veículo (FK)
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (idogrve, idveicu, idogrvv)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_cadastro_grupos_veiculos_vinculos (idogrve, idveicu, idogrvv);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_cadastro_grupos_veiculos_vinculos;
SHOW INDEX FROM abnf_operacional_cadastro_grupos_veiculos_vinculos;
SELECT * FROM abnf_operacional_cadastro_grupos_veiculos_vinculos;
DROP *** TABLE abnf_operacional_cadastro_grupos_veiculos_vinculos;
---------------------------------------------
*** jean *** acerto de registros que foram gerados sem pai (orfãos) ***
SELECT * FROM abnf_operacional_cadastro_grupos_veiculos_vinculos WHERE situreg = 'A' and idogrve = 0;
UPDATE abnf_operacional_cadastro_grupos_veiculos_vinculos SET situreg = 'C' WHERE situreg = 'A' and idogrve = 0;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_cadastro_prioridades_linhas ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_cadastro_prioridades_linhas (
    idoplin     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do registro de prioridade de linha
    ordprio     INT                                         NOT NULL                            ,   # Ordem de prioridade    
    idolinh     INT                                         NOT NULL                            ,   # ID da linha (FK)
    veicser     INT                                         NOT NULL                            ,   # Veículo/serviço
    idveicu     INT                                                                             ,   # ID do veículo oficial (FK)
    tpdiaut     BOOLEAN                                                                         ,   # Tipo de dia: útil
    tpdiasa     BOOLEAN                                                                         ,   # Tipo de dia: sábado
    tpdiado     BOOLEAN                                                                         ,   # Tipo de dia: domingo
    tpdiafe     BOOLEAN                                                                         ,   # Tipo de dia: feriado
    tpdia2a     BOOLEAN                                                                         ,   # Tipo de dia: segunda-feira
    tpdia3a     BOOLEAN                                                                         ,   # Tipo de dia: terça-feira
    tpdia4a     BOOLEAN                                                                         ,   # Tipo de dia: quarta-feira
    tpdia5a     BOOLEAN                                                                         ,   # Tipo de dia: quinta-feira
    tpdia6a     BOOLEAN                                                                         ,   # Tipo de dia: sexta-feira
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    INDEX abnfdx01 (ordprio, idoplin)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_cadastro_prioridades_linhas (ordprio, idoplin);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_cadastro_prioridades_linhas;
SHOW INDEX FROM abnf_operacional_cadastro_prioridades_linhas;
SELECT * FROM abnf_operacional_cadastro_prioridades_linhas;
DROP *** TABLE abnf_operacional_cadastro_prioridades_linhas;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_cadastro_prioridades_linhas_gv ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_cadastro_prioridades_linhas_gv (
    idoplgv     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do registro de vínculo da prioridade de linha com grupo de veículos
    idoplin     INT                                         NOT NULL                            ,   # ID do registro de prioridade de linha (FK)
    ordprio     INT                                         NOT NULL                            ,   # Ordem de prioridade
    idogrve     INT                                         NOT NULL                            ,   # ID do registro do grupo de veículo (FK)
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (idoplin, ordprio, idoplgv)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_cadastro_prioridades_linhas_gv (idoplin, ordprio, idoplgv);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_cadastro_prioridades_linhas_gv;
SHOW INDEX FROM abnf_operacional_cadastro_prioridades_linhas_gv;
SELECT * FROM abnf_operacional_cadastro_prioridades_linhas_gv;
DROP *** TABLE abnf_operacional_cadastro_prioridades_linhas_gv;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_cadastro_operacoes_especiais ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_cadastro_operacoes_especiais (
    idooesp     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do registro de vínculo da personalização da data
    dataope     DATE                                        NOT NULL                            ,   # Data da operação
    idolinh     INT                                         NOT NULL                            ,   # ID da linha (FK)
    veicser     INT                                         NOT NULL                            ,   # Veículo/serviço
    tipodia     VARCHAR(1)                                  NOT NULL                            ,   # Tipo de dia
    descmot     VARCHAR(100)                                NOT NULL                            ,   # Descrição do motivo
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    INDEX abnfdx01 (dataope, idolinh, veicser, idooesp)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_cadastro_operacoes_especiais (dataope, idolinh, veicser, idooesp);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_cadastro_operacoes_especiais;
SHOW INDEX FROM abnf_operacional_cadastro_operacoes_especiais;
SELECT * FROM abnf_operacional_cadastro_operacoes_especiais;
DROP *** TABLE abnf_operacional_cadastro_operacoes_especiais;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_cadastro_setor_veiculos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_cadastro_setor_veiculos (
    idosetv     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do registro de setor de veículos
	codoset     INT                                         NOT NULL                            ,   # Código do setor de veículos
	descset     VARCHAR(100)                                NOT NULL                            ,   # Descrição do setor de veículos
    qtdveic     INT                                         NOT NULL                            ,   # Quantidade de veículos
    ordprio     INT                                         NOT NULL                            ,   # Ordem de prioridade
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    INDEX abnfdx01 (codoset, idosetv),
    INDEX abnfdx02 (descset, idosetv)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_cadastro_setor_veiculos (codoset, idosetv);
CREATE INDEX abnfdx02 ON abnf_operacional_cadastro_setor_veiculos (descset, idosetv);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_cadastro_setor_veiculos;
SHOW INDEX FROM abnf_operacional_cadastro_setor_veiculos;
SELECT * FROM abnf_operacional_cadastro_setor_veiculos;
DROP *** TABLE abnf_operacional_cadastro_setor_veiculos;
---------------------------------------------
INSERT *** INTO abnf_operacional_cadastro_setor_veiculos (idosetv, codoset, descset, qtdveic, ordprio, situreg, idusucr, idfilia, dtregcr) VALUES
(?, ?, ???, 10, 6, "A", 1, 3, CURRENT_TIMESTAMP());
---------------------------------------------
*** Mudar a quantidade de veículos por setor ***
UPDATE *** abnf_operacional_cadastro_setor_veiculos SET qtdveic = 31 WHERE idosetv = 3;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_cadastro_motivo_substituicao ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_cadastro_motivo_substituicao (
    idomsub     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do registro de motivo de substituição
	codomsu     INT                                         NOT NULL                            ,   # Código do motivo de substituição
	descmsu     VARCHAR(100)                                NOT NULL                            ,   # Descrição do motivo de substuição
    tiposub     VARCHAR(1)                                  NOT NULL                            ,   # Tipo de substituição: [V]eículo
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    INDEX abnfdx01 (codomsu, idomsub),
    INDEX abnfdx02 (descmsu, idomsub)
);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_cadastro_motivo_substituicao;
SHOW INDEX FROM abnf_operacional_cadastro_motivo_substituicao;
SELECT * FROM abnf_operacional_cadastro_motivo_substituicao;
DROP *** TABLE abnf_operacional_cadastro_motivo_substituicao;
---------------------------------------------
INSERT *** INTO abnf_operacional_cadastro_motivo_substituicao (idomsub, codomsu, descmsu, tiposub, situreg, idusucr, dtregcr, idfilia) VALUES
(11, 10, '10 - RETORNO PARA LINHA TITULAR'                    , 'V', "A", 1, CURRENT_TIMESTAMP(), 3),
(12, 11, '11 - TROCA NA SOLTURA'                              , 'V', "A", 1, CURRENT_TIMESTAMP(), 3),
(13, 12, '12 - TROCA DE CARRO NA OPERACAO'                    , 'V', "A", 1, CURRENT_TIMESTAMP(), 3),
(14, 13, '13 - VEICULO ENCERROU PRIMEIRO TURNO NA GARAGEM'    , 'V', "A", 1, CURRENT_TIMESTAMP(), 3),
(15, 14, '14 - VEICULO DISPONIVEL PARA SOLTURA'               , 'V', "A", 1, CURRENT_TIMESTAMP(), 3);
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_cadastro_grupos_usuarios ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_cadastro_grupos_usuarios (
    idcusgr     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do grupo de usuários do controle diário
    codcusg     INT                                         NOT NULL                            ,   # Código do grupo de usuários do controle diário
    descusg     VARCHAR(100)                                NOT NULL                            ,   # Descrição do grupo de usuários do controle diário
    permaut     BOOLEAN                                     NOT NULL                            ,   # Permite definir o método automático-manual no controle diário
    perrefd     BOOLEAN                                     NOT NULL                            ,   # Permite refazer os registros de diário
    percaal     BOOLEAN                                     NOT NULL                            ,   # Permite cancelar alteração de informações
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    INDEX abnfdx01 (codcusg, idcusgr),
    INDEX abnfdx02 (descusg, idcusgr)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_cadastro_grupos_usuarios (codcusg, idcusgr);
CREATE INDEX abnfdx02 ON abnf_operacional_cadastro_grupos_usuarios (descusg, idcusgr);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_cadastro_grupos_usuarios;
SHOW INDEX FROM abnf_operacional_cadastro_grupos_usuarios;
SELECT * FROM abnf_operacional_cadastro_grupos_usuarios;
DROP *** TABLE abnf_operacional_cadastro_grupos_usuarios;
---------------------------------------------
INSERT *** INTO abnf_operacional_cadastro_grupos_usuarios (idcusgr, codcusg, descusg, permaut, situreg, idusucr, dtregcr, idfilia) VALUES
(1, 1, 'OPERACAO',             True,  "A", 1, CURRENT_TIMESTAMP(), 3),
(2, 2, 'CONTROLE MANUTENCAO',  False, "A", 1, CURRENT_TIMESTAMP(), 3);
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_cadastro_grupos_usuarios_vinculos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_cadastro_grupos_usuarios_vinculos (
    idcugvi     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do vinculo de grupos de usuarios do controle diário
	idcusgr     INT                                         NOT NULL                            ,   # ID do grupo de usuários do controle diário (FK)
	idusuar     INT                                         NOT NULL                            ,   # ID do usuário (FK)
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (idcusgr, idusuar, idcugvi)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_cadastro_grupos_usuarios_vinculos (idcusgr, idusuar, idcugvi);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_cadastro_grupos_usuarios_vinculos;
SHOW INDEX FROM abnf_operacional_cadastro_grupos_usuarios_vinculos;
SELECT * FROM abnf_operacional_cadastro_grupos_usuarios_vinculos;
DROP *** TABLE abnf_operacional_cadastro_grupos_usuarios_vinculos;
---------------------------------------------
SELECT
abnf01.idcugvi,
abnf02.idusuar,
abnf02.logiusu,
abnf02.nomeusu,
abnf03.idcusgr,
abnf03.descusg
FROM abnf_operacional_cadastro_grupos_usuarios_vinculos AS abnf01
INNER JOIN abnf_sistema_usuarios AS abnf02
ON abnf01.idusuar = abnf02.idusuar
INNER JOIN abnf_operacional_cadastro_grupos_usuarios AS abnf03
ON abnf01.idcusgr = abnf03.idcusgr
ORDER BY abnf02.nomeusu;
---------------------------------------------
INSERT *** INTO abnf_operacional_cadastro_grupos_usuarios_vinculos (idcugvi, idcusgr, idusuar, situreg, idusucr, dtregcr) VALUES
(23, 2, 90, "A", 2, CURRENT_TIMESTAMP());
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_movimentacao_propostas_oso ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_movimentacao_propostas_oso (
    idoprop     INT                     PRIMARY KEY         NOT NULL                            ,   # ID da proposta
    numepro     INT                                         NOT NULL                            ,   # Número da proposta
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    idoproj     INT                                         NOT NULL                            ,   # ID do projeto (FK)
    idolinh     INT                                         NOT NULL                            ,   # ID da linha (FK)
    observa     TEXT                                                                            ,   # Observação
    descpre     VARCHAR(200)                                                                    ,   # Descrição da prefeitura
    tpdiaut     BOOLEAN                                                                         ,   # Tipo de dia: útil
    tpdiasa     BOOLEAN                                                                         ,   # Tipo de dia: sábado
    tpdiado     BOOLEAN                                                                         ,   # Tipo de dia: domingo
    tpdiafe     BOOLEAN                                                                         ,   # Tipo de dia: feriado
    tpdia2a     BOOLEAN                                                                         ,   # Tipo de dia: segunda-feira
    tpdia3a     BOOLEAN                                                                         ,   # Tipo de dia: terça-feira
    tpdia4a     BOOLEAN                                                                         ,   # Tipo de dia: quarta-feira
    tpdia5a     BOOLEAN                                                                         ,   # Tipo de dia: quinta-feira
    tpdia6a     BOOLEAN                                                                         ,   # Tipo de dia: sexta-feira
    numrele     INT                                         NOT NULL                            ,   # Número de release
    situpro     VARCHAR(1)                                  NOT NULL                            ,   # Situação da proposta: [D]esenvolvimento/[E]nviado/[A]provado/[R]eprovado
    dataapr     DATETIME                                                                        ,   # Última data/hora de aprovação/reprovação da proposta
    datavig     DATE                                                                            ,   # Ultima data de vigoração da OSO
    INDEX abnfdx01 (numepro, idoprop)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_movimentacao_propostas_oso (numepro, idoprop);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_movimentacao_propostas_oso;
SHOW INDEX FROM abnf_operacional_movimentacao_propostas_oso;
SELECT * FROM abnf_operacional_movimentacao_propostas_oso;
DROP *** TABLE abnf_operacional_movimentacao_propostas_oso;
---------------------------------------------
ALTER *** TABLE abnf_operacional_movimentacao_propostas_oso ADD COLUMN dataapr DATETIME AFTER numrele;
ALTER *** TABLE abnf_operacional_movimentacao_propostas_oso ADD COLUMN datavig DATE AFTER dataapr;
ALTER *** TABLE abnf_operacional_movimentacao_propostas_oso ADD COLUMN situpro VARCHAR(1) NOT NULL AFTER numrele;
SELECT situpro FROM abnf_operacional_movimentacao_propostas_oso;
UPDATE *** abnf_operacional_movimentacao_propostas_oso SET situpro = "D";
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_movimentacao_propostas_oso_viagens ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_movimentacao_propostas_oso_viagens (
    idopvia     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do horário de viagem da proposta
    idoprop     INT                                         NOT NULL                            ,   # ID da proposta (FK)
    numrele     INT                                         NOT NULL                            ,   # Número de release
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    sentido     VARCHAR(1)                                  NOT NULL                            ,   # Sentido: [I]da/[V]olta
    tipopon     VARCHAR(1)                                  NOT NULL                            ,   # Tipo de ponto: [O]ficial/[P]assagem/[I]ntermediário
    veicpro     INT                                         NOT NULL                            ,   # Veículo da proposta
    veicger     INT                                         NOT NULL                            ,   # Veículo geral
    seghini     INT                                         NOT NULL                            ,   # Horário de início (em segundos)
    seghfim     INT                                         NOT NULL                            ,   # Horário de término (em segundos)
    idotraj     INT                                         NOT NULL                            ,   # ID do trajeto (FK)
    idolori     INT                                         NOT NULL                            ,   # ID do local de origem (FK)
    idoldes     INT                                         NOT NULL                            ,   # ID do local de destino (FK)
    idotivi     INT                                         NOT NULL                            ,   # Tipo de viagem: 1=Ocioso/2=Produtivo/3=Reservado/4=Deslocamento
    encerra     VARCHAR(1)                                  NOT NULL                            ,   # Encerramento da viagem: [N]ormal/[I]ntervalo/[D]upla pegada/[M]ultilinha/I[N]tervalo + Multilinha/[A]certo de Horário + Multilinha
    enctext     VARCHAR(100)                                                                    ,   # Encerramento da viagem: Texto opcional
    seghgar     INT                                                                             ,   # Horário de saída extra da garagem (em segundos)
    INDEX abnfdx01 (idoprop, numrele, seghini, veicpro, idopvia)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_movimentacao_propostas_oso_viagens (idoprop, numrele, seghini, veicpro, idopvia);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_movimentacao_propostas_oso_viagens;
SHOW INDEX FROM abnf_operacional_movimentacao_propostas_oso_viagens;
SELECT * FROM abnf_operacional_movimentacao_propostas_oso_viagens;
DROP *** TABLE abnf_operacional_movimentacao_propostas_oso_viagens;
---------------------------------------------
ALTER *** TABLE abnf_operacional_movimentacao_propostas_oso_viagens RENAME COLUMN veiculo TO veicpro;
ALTER *** TABLE abnf_operacional_movimentacao_propostas_oso_viagens ADD COLUMN veicger INT NOT NULL AFTER veicpro;
ALTER *** TABLE abnf_operacional_movimentacao_propostas_oso_viagens ADD COLUMN enctext VARCHAR(100) AFTER encerra;
ALTER *** TABLE abnf_operacional_movimentacao_propostas_oso_viagens
ALTER *** TABLE abnf_operacional_movimentacao_propostas_oso_viagens ADD COLUMN seghgar INT AFTER enctext;
DROP COLUMN hista01,
DROP COLUMN hista02,
DROP COLUMN histb01,
DROP COLUMN histb02,
DROP COLUMN histc01,
DROP COLUMN histc02,
DROP COLUMN histd01,
DROP COLUMN histd02;
---------------------------------------------
*** alexandre ***
SELECT idopvia, idolinh
FROM abnf_operacional_movimentacao_propostas_oso_viagens AS tb2 INNER JOIN abnf_operacional_movimentacao_propostas_oso AS tb1
WHERE tb2.idoprop = tb1.idoprop AND tpdiaut = True ORDER by idopvia INTO OUTFILE '/flexabeinfo/resu-U.txt'
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
*** alexandre ***
SELECT idopvia, idolinh
FROM abnf_operacional_movimentacao_propostas_oso_viagens AS tb2 INNER JOIN abnf_operacional_movimentacao_propostas_oso AS tb1
WHERE tb2.idoprop = tb1.idoprop AND tpdiasa = True ORDER by idopvia INTO OUTFILE '/flexabeinfo/resu-S.txt'
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
*** alexandre ***
SELECT idopvia, idolinh
FROM abnf_operacional_movimentacao_propostas_oso_viagens AS tb2 INNER JOIN abnf_operacional_movimentacao_propostas_oso AS tb1
WHERE tb2.idoprop = tb1.idoprop AND tpdiado = True ORDER by idopvia INTO OUTFILE '/flexabeinfo/resu-D.txt'
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_movimentacao_oficial_oso ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_movimentacao_oficial_oso (
    idoosoo     INT                     PRIMARY KEY         NOT NULL                            ,   # ID da OSO oficial
    numeoso     INT                                         NOT NULL                            ,   # Número da OSO
    idoprop     INT                                         NOT NULL                            ,   # ID da proposta (FK)
    numepro     INT                                         NOT NULL                            ,   # Número da proposta (histórico)
    numrele     INT                                         NOT NULL                            ,   # Número de release (histórico)
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    idoproj     INT                                         NOT NULL                            ,   # ID do projeto (FK)
	codopro     INT                                         NOT NULL                            ,   # Código do projeto (histórico)
    desopro     VARCHAR(100)                                NOT NULL                            ,   # Descrição do projeto (histórico)
    idolinh     INT                                         NOT NULL                            ,   # ID da linha (FK)
	codolin     VARCHAR(20)                                 NOT NULL                            ,   # Código da linha (histórico)
    desolin     VARCHAR(100)                                NOT NULL                            ,   # Descrição da linha (histórico)
    observa     TEXT                                                                            ,   # Observação
    descpre     VARCHAR(200)                                                                    ,   # Descrição da prefeitura
    tpdiaut     BOOLEAN                                                                         ,   # Tipo de dia: útil
    tpdiasa     BOOLEAN                                                                         ,   # Tipo de dia: sábado
    tpdiado     BOOLEAN                                                                         ,   # Tipo de dia: domingo
    tpdiafe     BOOLEAN                                                                         ,   # Tipo de dia: feriado
    tpdia2a     BOOLEAN                                                                         ,   # Tipo de dia: segunda-feira
    tpdia3a     BOOLEAN                                                                         ,   # Tipo de dia: terça-feira
    tpdia4a     BOOLEAN                                                                         ,   # Tipo de dia: quarta-feira
    tpdia5a     BOOLEAN                                                                         ,   # Tipo de dia: quinta-feira
    tpdia6a     BOOLEAN                                                                         ,   # Tipo de dia: sexta-feira
    idusuap     INT                                         NOT NULL                            ,   # ID do usuário que aprovou/reprovou a OSO (FK)
    dtaprov     DATETIME                                    NOT NULL                            ,   # Data/hora da aprovação da OSO
    datavig     DATE                                        NOT NULL                            ,   # Data de vigoração da OSO
    INDEX abnfdx01 (numeoso, idoosoo)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_movimentacao_oficial_oso (numeoso, idoosoo);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_movimentacao_oficial_oso;
SHOW INDEX FROM abnf_operacional_movimentacao_oficial_oso;
SELECT * FROM abnf_operacional_movimentacao_oficial_oso;
DROP *** TABLE abnf_operacional_movimentacao_oficial_oso;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_movimentacao_oficial_oso_viagens ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_movimentacao_oficial_oso_viagens (
    idoovia     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do horário de viagem da OSO oficial
    idoosoo     INT                                         NOT NULL                            ,   # ID da OSO oficial (FK)
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    sentido     VARCHAR(1)                                  NOT NULL                            ,   # Sentido: [I]da/[V]olta
    tipopon     VARCHAR(1)                                  NOT NULL                            ,   # Tipo de ponto: [O]ficial/[P]assagem/[I]ntermediário
    veicpro     INT                                         NOT NULL                            ,   # Veículo da proposta
    veicger     INT                                         NOT NULL                            ,   # Veículo geral
    seghini     INT                                         NOT NULL                            ,   # Horário de início (em segundos)
    seghfim     INT                                         NOT NULL                            ,   # Horário de término (em segundos)
    idootra     INT                                         NOT NULL                            ,   # ID do trajeto (FK)
    idolori     INT                                         NOT NULL                            ,   # ID do local de origem (FK)
    codolor     INT                                         NOT NULL                            ,   # Código do local de origem (histórico)
    desolor     VARCHAR(100)                                NOT NULL                            ,   # Descrição do local de origem (histórico)
    idlogor     INT                                                                             ,   # ID do logradouro do local de origem (FK) (histórico)
    tiploor     VARCHAR(50)                                                                     ,   # Tipo de logradouro do local de origem (histórico)
    desloor     VARCHAR(200)                                                                    ,   # Descrição do logradouro do local de origem (histórico)
    logrnor     VARCHAR(20)                                                                     ,   # Número do logradouro do local de origem (histórico)
    logrcor     VARCHAR(100)                                                                    ,   # Complemento do logradouro do local de origem (histórico)
    desbaor     VARCHAR(100)                                                                    ,   # Bairro do logradouro do local de origem (histórico)
	descior     VARCHAR(100)                                                                    ,   # Cidade do logradouro do local de origem (histórico)
    estador     VARCHAR(2)                                                                      ,   # Estado do logradouro do local de origem (histórico)
    logceor     VARCHAR(10)                                                                     ,   # CEP do logradouro do local de origem (histórico)
    obseror     TEXT                                                                            ,   # Observação do logradouro do local de origem (histórico)
    idoldes     INT                                         NOT NULL                            ,   # ID do local de destino (FK)
    codolde     INT                                         NOT NULL                            ,   # Código do local de destino (histórico)
    desolde     VARCHAR(100)                                NOT NULL                            ,   # Descrição do local de destino (histórico)
    idlogde     INT                                                                             ,   # ID do logradouro do local de destino (FK) (histórico)
    tiplode     VARCHAR(50)                                                                     ,   # Tipo de logradouro do local de destino (histórico)
    deslode     VARCHAR(200)                                                                    ,   # Descrição do logradouro do local de destino (histórico)
    logrnde     VARCHAR(20)                                                                     ,   # Número do logradouro do local de destino (histórico)
    logrcde     VARCHAR(100)                                                                    ,   # Complemento do logradouro do local de destino (histórico)
    desbade     VARCHAR(100)                                                                    ,   # Bairro do logradouro do local de destino (histórico)
	descide     VARCHAR(100)                                                                    ,   # Cidade do logradouro do local de destino (histórico)
    desesde     VARCHAR(2)                                                                      ,   # Estado do logradouro do local de destino (histórico)
    logcede     VARCHAR(10)                                                                     ,   # CEP do logradouro do local de destino (histórico)
    obserde     TEXT                                                                            ,   # Observação do logradouro do local de destino (histórico)    
    idotivi     INT                                         NOT NULL                            ,   # Tipo de viagem: 1=Ocioso/2=Produtivo/3=Reservado/4=Deslocamento
    encerra     VARCHAR(1)                                  NOT NULL                            ,   # Encerramento da viagem: [N]ormal/[I]ntervalo/[D]upla pegada/[M]ultilinha/I[N]tervalo + Multilinha/[A]certo de Horário + Multilinha
    enctext     VARCHAR(100)                                                                    ,   # Encerramento da viagem: Texto opcional
    seghgar     INT                                                                             ,   # Horário de saída extra da garagem (em segundos)
    INDEX abnfdx01 (idoosoo, seghini, veicpro, idoovia)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_movimentacao_oficial_oso_viagens (idoosoo, seghini, veicpro, idoovia);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_movimentacao_oficial_oso_viagens;
SHOW INDEX FROM abnf_operacional_movimentacao_oficial_oso_viagens;
SELECT * FROM abnf_operacional_movimentacao_oficial_oso_viagens;
DROP *** TABLE abnf_operacional_movimentacao_oficial_oso_viagens;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_movimentacao_oficial_oso_trajetos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_movimentacao_oficial_oso_trajetos (
    idootra     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do trajeto da OSO oficial
    idoosoo     INT                                         NOT NULL                            ,   # ID da OSO oficial (FK)
    codotra     VARCHAR(4)                                  NOT NULL                            ,   # Código do trajeto
    desotra     VARCHAR(200)                                NOT NULL                            ,   # Descrição do trajeto
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    kmidaxx     DECIMAL(8,1)                                NOT NULL    DEFAULT 0.0             ,   # Km ida
    kmvolta     DECIMAL(8,1)                                NOT NULL    DEFAULT 0.0             ,   # Km volta
    INDEX abnfdx01 (idoosoo, codotra)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_movimentacao_oficial_oso_trajetos (idoosoo, codotra);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_movimentacao_oficial_oso_trajetos;
SHOW INDEX FROM abnf_operacional_movimentacao_oficial_oso_trajetos;
SELECT * FROM abnf_operacional_movimentacao_oficial_oso_trajetos;
DROP *** TABLE abnf_operacional_movimentacao_oficial_oso_trajetos;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_movimentacao_oficial_oso_itinerarios ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_movimentacao_oficial_oso_itinerarios (
    idooiti     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do itinerario
    idootra     INT                                         NOT NULL                            ,   # ID do trajeto da OSO oficial (FK)
    sentido     VARCHAR(1)                                  NOT NULL                            ,   # Sentido: [I]da/[V]olta
    ordemit     INT                                         NOT NULL                            ,   # Ordem no itinerário
    idlogra     INT                                         NOT NULL                            ,   # ID do logradouro (FK)
    tiplogr     VARCHAR(50)                                                                     ,   # Tipo de logradouro (histórico)
    deslogr     VARCHAR(200)                                                                    ,   # Descrição do logradouro (histórico)
    complem     VARCHAR(100)                                                                    ,   # Complemento (histórico)
    desbair     VARCHAR(100)                                                                    ,   # Descrição do bairro (histórico)
	descida     VARCHAR(100)                                                                    ,   # Descrição da cidade (histórico)
    desesta     VARCHAR(2)                                                                      ,   # Descrição do estado (histórico)
    destaqu     BOOLEAN                                                                         ,   # Destaque?
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (idootra, sentido, ordemit, idooiti)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_movimentacao_oficial_oso_itinerarios (idootra, sentido, ordemit, idooiti);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_movimentacao_oficial_oso_itinerarios;
SHOW INDEX FROM abnf_operacional_movimentacao_oficial_oso_itinerarios;
SELECT * FROM abnf_operacional_movimentacao_oficial_oso_itinerarios;
DROP *** TABLE abnf_operacional_movimentacao_oficial_oso_itinerarios;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_movimentacao_programacao_diario ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_movimentacao_programacao_diario (
    idoprdi     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do registro de diário de programação
    dataope     DATE                                        NOT NULL                            ,   # Data da operação
    tiporeg     VARCHAR(1)                                  NOT NULL                            ,   # Tipo de registro: [A]utomático/[M]anual
    idcusde     INT                                                                             ,   # ID do usuario que definiu o registro (FK)
    idolinh     INT                                         NOT NULL                            ,   # ID da linha (FK)
	codolin     VARCHAR(20)                                 NOT NULL                            ,   # Código da linha (histórico)
    desolin     VARCHAR(100)                                NOT NULL                            ,   # Descrição da linha (histórico)
    veicpro     INT                                         NOT NULL                            ,   # Veículo da proposta
    veicger     INT                                         NOT NULL                            ,   # Veículo geral
    tipodia     VARCHAR(1)                                  NOT NULL                            ,   # Tipo de dia
    descmot     VARCHAR(100)                                                                    ,   # Descrição do motivo    
    sentido     VARCHAR(1)                                  NOT NULL                            ,   # Sentido: [I]da/[V]olta
    tipopon     VARCHAR(1)                                  NOT NULL                            ,   # Tipo de ponto: [O]ficial/[P]assagem/[I]ntermediário
    idotivi     INT                                         NOT NULL                            ,   # Tipo de viagem: 1=Ocioso/2=Produtivo/3=Reservado/4=Deslocamento    
    seghini     INT                                         NOT NULL                            ,   # Horário de início (em segundos)
    seghfim     INT                                         NOT NULL                            ,   # Horário de término (em segundos)
    saidgar     BOOLEAN                                                                         ,   # Saída da garagem?
    seghgar     INT                                                                             ,   # Horário de saída da garagem (em segundos)
    idolori     INT                                         NOT NULL                            ,   # ID do local de origem (FK)
    codolor     INT                                         NOT NULL                            ,   # Código do local de origem (histórico)
    desolor     VARCHAR(100)                                NOT NULL                            ,   # Descrição do local de origem (histórico)
    idoldes     INT                                         NOT NULL                            ,   # ID do local de destino (FK)
    codolde     INT                                         NOT NULL                            ,   # Código do local de destino (histórico)
    desolde     VARCHAR(100)                                NOT NULL                            ,   # Descrição do local de destino (histórico)
    idveicu     INT                                                                             ,   # ID do veículo (FK)
    prefvei     VARCHAR(20)                                                                     ,   # Prefixo do veículo (histórico)
    idveofi     INT                                                                             ,   # ID do veículo oficial (FK)
    prefvof     VARCHAR(20)                                                                     ,   # Prefixo do veículo oficial (histórico)
    idosetv     INT                                                                             ,   # ID do setor de veículos
	codoset     INT                                                                             ,   # Código do setor de veículos (histórico)
	descset     VARCHAR(100)                                                                    ,   # Descrição do setor de veículos (histórico)
    observa     TEXT                                                                            ,   # Observação
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    INDEX abnfdx01 (dataope, idolinh, veicpro, dtregcr),
    INDEX abnfdx02 (dataope, idveicu, dtregcr)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_movimentacao_programacao_diario (dataope, idolinh, veicpro, dtregcr);
CREATE INDEX abnfdx02 ON abnf_operacional_movimentacao_programacao_diario (dataope, idveicu, dtregcr);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_movimentacao_programacao_diario;
SHOW INDEX FROM abnf_operacional_movimentacao_programacao_diario;
SELECT * FROM abnf_operacional_movimentacao_programacao_diario WHERE dataope = '2025-09-05' and situreg = 'A';
DROP *** TABLE abnf_operacional_movimentacao_programacao_diario;
---------------------------------------------
ALTER *** TABLE abnf_operacional_movimentacao_programacao_diario ADD COLUMN idosetv INT AFTER idveicu;
---------------------------------------------
SELECT idosetv FROM abnf_operacional_movimentacao_programacao_diario WHERE idoprdi = 798;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_movimentacao_programacao_substituicao ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_movimentacao_programacao_substituicao (
    idoprsu     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do registro de controle de substituição
    idoprdi     INT                                         NOT NULL                            ,   # ID do registro de diário de programação (FK)
    tiposub     VARCHAR(1)                                  NOT NULL                            ,   # Tipo de substituição: [V]eículo
    idveisa     INT                                                                             ,   # ID do veículo que sai (FK)
    idveien     INT                                                                             ,   # ID do veículo que entra (FK)
    idomsub     INT                                         NOT NULL                            ,   # ID do registro de motivo de substituição
    motisub     TEXT                                                                            ,   # Motivo da substituição
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                            # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_movimentacao_programacao_substituicao;
SHOW INDEX FROM abnf_operacional_movimentacao_programacao_substituicao;
SELECT * FROM abnf_operacional_movimentacao_programacao_substituicao;
DROP *** TABLE abnf_operacional_movimentacao_programacao_substituicao;
---------------------------------------------
*** Alexandre/Jean - Procedimento para cancelar uma substituição errada feita pelo CCO ***   
SELECT * FROM abnf_operacional_movimentacao_programacao_substituicao WHERE idoprsu IN (
1131,
1132
);
UPDATE abnf_operacional_movimentacao_programacao_substituicao SET situreg = 'C', idusual = 2, dtregal = CURRENT_TIMESTAMP() WHERE idoprsu IN (
1131,
1132
);
SELECT * FROM abnf_operacional_movimentacao_programacao_substituicao WHERE idoprsu IN (
1131,
1132
);
Feitos!
Lembrando que o cancelamento não faz os veículos voltarem para suas posições originais
Então as correções precisam serem feitas de forma manual, ok?
---------------------------------------------
SELECT * FROM abnf_operacional_movimentacao_programacao_substituicao WHERE idoprsu = 26;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_movimentacao_programacao_automacao ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_movimentacao_programacao_automacao (
    idoprau     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do registro de controle de automação
    dtmetod     DATETIME                                    NOT NULL                            ,   # Data/hora da definição do método
    defmeto     VARCHAR(1)                                  NOT NULL                            ,   # Definição do método: [A]utomático/[M]anual
    idusuar     INT                                                                             ,   # ID do usuários que definiu o método
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    INDEX abnfdx01 (dtmetod)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_movimentacao_programacao_automacao (dtmetod);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_movimentacao_programacao_automacao;
SHOW INDEX FROM abnf_operacional_movimentacao_programacao_automacao;
SELECT * FROM abnf_operacional_movimentacao_programacao_automacao;
DROP *** TABLE abnf_operacional_movimentacao_programacao_automacao;
---------------------------------------------
*** Pegar o último registro do select ***
SELECT idoprau, defmeto FROM abnf_operacional_movimentacao_programacao_automacao ORDER BY dtmetod DESC LIMIT 1;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_movimentacao_programacao_retencao_veiculos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_movimentacao_programacao_retencao_veiculos (
    idoprrv     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do registro de controle de retenção do veículos
    codctrl     INT                                         NOT NULL                            ,   # Código de controle
    idveicu     INT                                         NOT NULL                            ,   # ID do veículo oficial (FK)
    dtreten     DATETIME                                    NOT NULL                            ,   # Data/hora da ordem de retenção
    dtliber     DATETIME                                                                        ,   # Data/hora da ordem de liberação
    idcusgr     INT                                         NOT NULL                            ,   # ID do grupo de usuarios do controle diário (FK)
    idcusre     INT                                         NOT NULL                            ,   # ID do usuários que reteve (FK)
    idcusli     INT                                                                             ,   # ID do usuários que liberou (FK)
    dataage     DATE                                        NOT NULL                            ,   # Data do agendamento da retenção
    seghage     INT                                         NOT NULL                            ,   # Horário do agendamento da retenção (em segundos)
    descrre     TEXT                                        NOT NULL                            ,   # Descrição na retenção do veículo
    descrli     TEXT                                                                            ,   # Descrição na liberação do veículo
    statret     INT                                         NOT NULL                            ,   # Status da retenção
    idsdede     INT                                                                             ,   # ID da definição de defeito do SIGOM (FK)
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    INDEX abnfdx01 (codctrl, idoprrv),
    INDEX abnfdx02 (idveicu, idoprrv),
    INDEX abnfdx03 (dtreten, idoprrv),
    INDEX abnfdx04 (dtliber, idoprrv),
    INDEX abnfdx05 (dataage, seghage, idoprrv)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_movimentacao_programacao_retencao_veiculos (codctrl, idoprrv);
CREATE INDEX abnfdx02 ON abnf_operacional_movimentacao_programacao_retencao_veiculos (idveicu, idoprrv);
CREATE INDEX abnfdx03 ON abnf_operacional_movimentacao_programacao_retencao_veiculos (dtreten, idoprrv);
CREATE INDEX abnfdx04 ON abnf_operacional_movimentacao_programacao_retencao_veiculos (dtliber, idoprrv);
CREATE INDEX abnfdx05 ON abnf_operacional_movimentacao_programacao_retencao_veiculos (dataage, seghage, idoprrv);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_movimentacao_programacao_retencao_veiculos;
SHOW INDEX FROM abnf_operacional_movimentacao_programacao_retencao_veiculos;
SELECT * FROM abnf_operacional_movimentacao_programacao_retencao_veiculos;
DROP *** TABLE abnf_operacional_movimentacao_programacao_retencao_veiculos;
---------------------------------------------
ALTER *** TABLE abnf_operacional_movimentacao_programacao_retencao_veiculos RENAME COLUMN codmovi TO codctrl;
---------------------------------------------
\! clear
SELECT statret FROM abnf_operacional_movimentacao_programacao_retencao_veiculos WHERE statret = 4;
SELECT statret FROM abnf_operacional_movimentacao_programacao_retencao_veiculos WHERE statret = 3;
UPDATE *** abnf_operacional_movimentacao_programacao_retencao_veiculos SET statret = 4 WHERE statret = 3;
\! clear
SELECT statret FROM abnf_operacional_movimentacao_programacao_retencao_veiculos WHERE statret = 3;
SELECT statret FROM abnf_operacional_movimentacao_programacao_retencao_veiculos WHERE statret = 2;
UPDATE *** abnf_operacional_movimentacao_programacao_retencao_veiculos SET statret = 3 WHERE statret = 2;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_entrada_saida_veiculos_locais ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_entrada_saida_veiculos_locais (
    idoesvl     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do local
	codoesl     INT                                         NOT NULL                            ,   # Código do local
    desoesl     VARCHAR(100)                                NOT NULL                            ,   # Descrição do local
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    tipoloc     VARCHAR(1)                                  NOT NULL                            ,   # Tipo de local: [G]aragem/[P]onto de passagem
    INDEX abnfdx01 (codoesl, idoesvl),
    INDEX abnfdx02 (desoesl, idoesvl)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_entrada_saida_veiculos_locais (codoesl, idoesvl);
CREATE INDEX abnfdx02 ON abnf_operacional_entrada_saida_veiculos_locais (desoesl, idoesvl);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_entrada_saida_veiculos_locais;
SHOW INDEX FROM abnf_operacional_entrada_saida_veiculos_locais;
SELECT * FROM abnf_operacional_entrada_saida_veiculos_locais;
DROP *** TABLE abnf_operacional_entrada_saida_veiculos_locais;
---------------------------------------------
INSERT *** INTO abnf_operacional_entrada_saida_veiculos_locais (idoesvl, codoesl, desoesl, situreg, idusucr, dtregcr, idfilia, tipoloc) VALUES
(?, ?, '???', "A", 1, CURRENT_TIMESTAMP(), 1, "?");
---------------------------------------------
=> Obrigatorio fazer o movimento oposto a entrada/saida
=> Se ultimo movimento for entrada obrigatorio fazer saida do mesmo local
=> Ponto de passagem somente após saida ou ponto de passagem
=> Entrada somente após uma saida ou ponto de passagem
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_entrada_saida_veiculos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_entrada_saida_veiculos(
    idoesve     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do registro de entrada/saída do veiculo
    idveicu     INT                                         NOT NULL                            ,   # ID do veículo (FK)
    idoesvl     INT                                         NOT NULL                            ,   # ID do local (FK)
    dataesv     DATE                                        NOT NULL                            ,   # Data da entrada/saída do veículo
    horaesv     TIME                                        NOT NULL                            ,   # Hora da entrada/saída do veículo
    tipomov     VARCHAR(1)                                  NOT NULL                            ,   # Tipo de movimentação: [E]ntrada/[S]aída/[P]onto de passagem
    odomvei     INT                                         NOT NULL                            ,   # Odômetro do veículo
    rolevei     INT                                                                             ,   # Roleta do veículo
    idolinh     INT                                         NOT NULL                            ,   # ID da linha da operação envolvida (FK)
    idmot01     INT                                         NOT NULL                            ,   # ID do motorista 01 (FK)
    idmot02     INT                                                                             ,   # ID do motorista 02 (FK)
    idmot03     INT                                                                             ,   # ID do motorista 03 (FK)
    idcob01     INT                                                                             ,   # ID do cobrador 01 (FK)
    idcob02     INT                                                                             ,   # ID do cobrador 02 (FK)
    idcob03     INT                                                                             ,   # ID do cobrador 03 (FK)
    observa     TEXT                                                                            ,   # Observação
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    INDEX abnfdx01 (idveicu, dataesv, horaesv),
    INDEX abnfdx02 (dataesv, horaesv, idveicu)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_entrada_saida_veiculos (idveicu, dataesv, horaesv);
CREATE INDEX abnfdx02 ON abnf_operacional_entrada_saida_veiculos (dataesv, horaesv, idveicu);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_entrada_saida_veiculos;
SHOW INDEX FROM abnf_operacional_entrada_saida_veiculos;
SELECT * FROM abnf_operacional_entrada_saida_veiculos; WHERE idveicu = 6;
SELECT idveicu, prefvei, placave, situreg FROM abnf_cadastro_veiculos WHERE idveicu = 766;
DROP *** TABLE abnf_operacional_entrada_saida_veiculos;
---------------------------------------------
*** portaria ***
SELECT idveicu, prefvei FROM abnf_cadastro_veiculos WHERE prefvei = '811';
SELECT * FROM abnf_operacional_entrada_saida_veiculos WHERE idveicu = 66;
UPDATE abnf_operacional_entrada_saida_veiculos SET odomvei = 755501 WHERE odomvei = 75555011 and idveicu = 6;
---------------------------------------------
SELECT * FROM abnf_operacional_entrada_saida_veiculos WHERE odomvei = 929976;
UPDATE *** abnf_operacional_entrada_saida_veiculos SET odomvei = 929568 WHERE odomvei = 929976;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_entrada_saida_veiculos_check_list_padrao ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_entrada_saida_veiculos_check_list_padrao(
    idoclpa     INT                     PRIMARY KEY         NOT NULL                            ,   # ID de ítem de check list padrão
    codoclp     INT                                         NOT NULL                            ,   # Código do ítem de check list
    desoclp     VARCHAR(100)                                NOT NULL                            ,   # Descrição do ítem de check list
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
	tipomov     VARCHAR(1)                                  NOT NULL                            ,   # Tipo de movimentação: [E]ntrada/[S]aída/[P]onto de passagem
    INDEX abnfdx01 (codoclp, idoclpa),
    INDEX abnfdx02 (desoclp, idoclpa)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_entrada_saida_veiculos_check_list_padrao (codoclp, idoclpa);
CREATE INDEX abnfdx02 ON abnf_operacional_entrada_saida_veiculos_check_list_padrao (desoclp, idoclpa);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_entrada_saida_veiculos_check_list_padrao;
SHOW INDEX FROM abnf_operacional_entrada_saida_veiculos_check_list_padrao;
SELECT * FROM abnf_operacional_entrada_saida_veiculos_check_list_padrao;
DROP *** TABLE abnf_operacional_entrada_saida_veiculos_check_list_padrao;
---------------------------------------------
INSERT *** INTO abnf_operacional_entrada_saida_veiculos_check_list_padrao (idoclpa, codoclp, desoclp, situreg, idusucr, dtregcr, tipomov) VALUES
(?, ?, '???', "A", 1, CURRENT_TIMESTAMP(), "?");
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_entrada_saida_veiculos_check_list ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_operacional_entrada_saida_veiculos_check_list(
    idochli     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do registro de check list do veículo
	idoclpa     INT                                         NOT NULL                            ,   # ID de ítem de check list padrão (FK)
	idoesve     INT                                         NOT NULL                            ,   # ID do registro de movimentacao do veiculo (FK)
    idveicu     INT                                         NOT NULL                            ,   # ID do veículo (FK)
	marcado     VARCHAR(1)                                  NOT NULL                            ,   # Marcado: [S]im/[N]ão
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    INDEX abnfdx01 (idoclpa, idochli),
    INDEX abnfdx02 (idoesve, idochli)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_operacional_entrada_saida_veiculos_check_list (idoclpa, idochli);
CREATE INDEX abnfdx02 ON abnf_operacional_entrada_saida_veiculos_check_list (idoesve, idochli);
---------------------------------------------
SHOW COLUMNS FROM abnf_operacional_entrada_saida_veiculos_check_list;
SHOW INDEX FROM abnf_operacional_entrada_saida_veiculos_check_list;
SELECT * FROM abnf_operacional_entrada_saida_veiculos_check_list;
DROP *** TABLE abnf_operacional_entrada_saida_veiculos_check_list;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░          ░░  ░░          ░░          ░░   ░░░░   ░░
░░  ░░░░░░░░░░  ░░  ░░░░░░░░░░  ░░░░░░  ░░    ░░    ░░
▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒  ▒▒  ▒    ▒  ▒▒
▒▒          ▒▒  ▒▒  ▒▒▒     ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒  ▒▒  ▒▒
▒▒▒▒▒▒▒▒▒▒  ▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒  ▒▒▒▒▒▒  ▒▒
██████████  ██  ██  ██████  ██  ██████  ██  ██████  ██
██          ██  ██          ██          ██  ██████  ██
██████████████████████████████████████████████████████
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_sigom_cadastro_usuarios_grupos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sigom_cadastro_usuarios_grupos (
    idsusgr     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do grupo de usuarios do SIGOM
    codsusg     INT                                         NOT NULL                            ,   # Código do grupo de usuarios do SIGOM
    dessusg     VARCHAR(100)                                NOT NULL                            ,   # Descrição do grupo de usuarios do SIGOM
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    emailgr     VARCHAR(100)                                                                    ,   # E-mail do grupo
    INDEX abnfdx01 (codsusg, idsusgr),
    INDEX abnfdx02 (dessusg, idsusgr)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sigom_cadastro_usuarios_grupos (codsusg, idsusgr);
CREATE INDEX abnfdx02 ON abnf_sigom_cadastro_usuarios_grupos (dessusg, idsusgr);
---------------------------------------------
SHOW COLUMNS FROM abnf_sigom_cadastro_usuarios_grupos;
SHOW INDEX FROM abnf_sigom_cadastro_usuarios_grupos;
SELECT * FROM abnf_sigom_cadastro_usuarios_grupos WHERE idsusgr = 8;
DROP *** TABLE abnf_sigom_cadastro_usuarios_grupos;
---------------------------------------------
INSERT *** INTO abnf_sigom_cadastro_usuarios_grupos (idsusgr, codsusg, dessusg, situreg, idusucr, dtregcr, idfilia, emailgr) VALUES
(??, ??, ??, 'A', 1, CURRENT_TIMESTAMP(), ??, ??);
---------------------------------------------
UPDATE *** abnf_sigom_cadastro_usuarios_grupos SET dessusg = "TELEMETRIA & TREINAMENTOS" WHERE idsusgr = 4;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_sigom_cadastro_usuarios_grupos_vinculos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sigom_cadastro_usuarios_grupos_vinculos (
    idsugvi     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do vinculo de grupos de usuarios do SIGOM
	idsusgr     INT                                         NOT NULL                            ,   # ID do grupo de usuarios do SIGOM (FK)
	idusuar     INT                                         NOT NULL                            ,   # ID do usuário (FK)
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    INDEX abnfdx01 (idsusgr, idusuar, idsugvi)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sigom_cadastro_usuarios_grupos_vinculos (idsusgr, idusuar, idsugvi);
---------------------------------------------
SHOW COLUMNS FROM abnf_sigom_cadastro_usuarios_grupos_vinculos;
SHOW INDEX FROM abnf_sigom_cadastro_usuarios_grupos_vinculos;
SELECT * FROM abnf_sigom_cadastro_usuarios_grupos_vinculos;
SELECT * FROM abnf_sigom_cadastro_usuarios_grupos_vinculos WHERE idusuar in (13);
SELECT * FROM abnf_sigom_cadastro_usuarios_grupos_vinculos WHERE idsusgr = 13;
DROP *** TABLE abnf_sigom_cadastro_usuarios_grupos_vinculos;
---------------------------------------------
INSERT *** INTO abnf_sigom_cadastro_usuarios_grupos_vinculos (idsugvi, idsusgr, idusuar, situreg, idusucr, dtregcr) VALUES
(79, 8, 81, "A", 1, CURRENT_TIMESTAMP()),
(80, 8, 82, "A", 1, CURRENT_TIMESTAMP());
---------------------------------------------
UPDATE *** abnf_sigom_cadastro_usuarios_grupos_vinculos SET situreg = "C", idusual = 1, dtregal = CURRENT_TIMESTAMP() WHERE idsugvi = 27;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_sigom_cadastro_ocorrencias_tipos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sigom_cadastro_ocorrencias_tipos (
    idsocti     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do tipo de ocorrência do SIGOM
    codsoct     INT                                         NOT NULL                            ,   # Código do tipo de ocorrência do SIGOM
    dessoct     VARCHAR(100)                                NOT NULL                            ,   # Descrição do tipo de ocorrência do SIGOM
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    obrdulp     BOOLEAN                                                                         ,   # Obrigatório inserir a data da ultima preventiva no fechamento?
    obrnerp     BOOLEAN                                                                         ,   # Obrigatório inserir o número do documento do ERP no fechamento?
    obracto     BOOLEAN                                                                         ,   # Obrigatório inserir a ação tomada no fechamento?
    INDEX abnfdx01 (codsoct, idsocti),
    INDEX abnfdx02 (dessoct, idsocti)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sigom_cadastro_ocorrencias_tipos (codsoct, idsocti);
CREATE INDEX abnfdx02 ON abnf_sigom_cadastro_ocorrencias_tipos (dessoct, idsocti);
---------------------------------------------
SHOW COLUMNS FROM abnf_sigom_cadastro_ocorrencias_tipos;
SHOW INDEX FROM abnf_sigom_cadastro_ocorrencias_tipos;
SELECT * FROM abnf_sigom_cadastro_ocorrencias_tipos;
DROP *** TABLE abnf_sigom_cadastro_ocorrencias_tipos;
---------------------------------------------
INSERT *** INTO abnf_sigom_cadastro_ocorrencias_tipos (idsocti, codsoct, dessoct, situreg, idusucr, dtregcr, idfilia) VALUES
(??, ??, ??, "A", 1, CURRENT_TIMESTAMP(), ??);
---------------------------------------------
ALTER *** TABLE abnf_sigom_cadastro_ocorrencias_tipos ADD COLUMN obrdulp BOOLEAN AFTER idfilia;
ALTER *** TABLE abnf_sigom_cadastro_ocorrencias_tipos ADD COLUMN obrnerp BOOLEAN AFTER obrdulp;
ALTER *** TABLE abnf_sigom_cadastro_ocorrencias_tipos ADD COLUMN obracto BOOLEAN AFTER obrnerp;
UPDATE ***abnf_sigom_cadastro_ocorrencias_tipos SET obrdulp = True WHERE idsocti > 0;
UPDATE ***abnf_sigom_cadastro_ocorrencias_tipos SET obrnerp = True WHERE idsocti > 0;
UPDATE ***abnf_sigom_cadastro_ocorrencias_tipos SET obracto = True WHERE idsocti > 0;
UPDATE ***abnf_sigom_cadastro_ocorrencias_tipos SET obrdulp = False WHERE dessoct = 'OC';
UPDATE ***abnf_sigom_cadastro_ocorrencias_tipos SET obrnerp = False WHERE dessoct = 'OC';
UPDATE ***abnf_sigom_cadastro_ocorrencias_tipos SET obracto = False WHERE dessoct = 'OC';
UPDATE ***abnf_sigom_cadastro_ocorrencias_tipos SET obrdulp = False WHERE dessoct = 'TROCA';
UPDATE ***abnf_sigom_cadastro_ocorrencias_tipos SET obrnerp = False WHERE dessoct = 'TROCA';
UPDATE ***abnf_sigom_cadastro_ocorrencias_tipos SET obracto = False WHERE dessoct = 'TROCA';
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_sigom_cadastro_veiculos_situacao ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sigom_cadastro_veiculos_situacao (
    idsvesi     INT                     PRIMARY KEY         NOT NULL                            ,   # ID da situação de veículo do SIGOM
    codsves     INT                                         NOT NULL                            ,   # Código da situação de veículo do SIGOM
    dessves     VARCHAR(100)                                NOT NULL                            ,   # Descrição da situação de veículo do SIGOM
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    INDEX abnfdx01 (codsves, idsvesi),
    INDEX abnfdx02 (dessves, idsvesi)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sigom_cadastro_veiculos_situacao (codsves, idsvesi);
CREATE INDEX abnfdx02 ON abnf_sigom_cadastro_veiculos_situacao (dessves, idsvesi);
---------------------------------------------
SHOW COLUMNS FROM abnf_sigom_cadastro_veiculos_situacao;
SHOW INDEX FROM abnf_sigom_cadastro_veiculos_situacao;
SELECT * FROM abnf_sigom_cadastro_veiculos_situacao;
DROP *** TABLE abnf_sigom_cadastro_veiculos_situacao;
---------------------------------------------
INSERT *** INTO abnf_sigom_cadastro_veiculos_situacao (idsvesi, codsves, dessves, situreg, idusucr, dtregcr, idfilia) VALUES
(??, ??, ??, "A", 1, CURRENT_TIMESTAMP(), ??);
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_sigom_cadastro_classificacao ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sigom_cadastro_classificacao (
    idsclas     INT                     PRIMARY KEY         NOT NULL                            ,   # ID da classificação do SIGOM
    codscla     INT                                         NOT NULL                            ,   # Código da classificação do SIGOM
    desscla     VARCHAR(100)                                NOT NULL                            ,   # Descrição da classificação do SIGOM
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    INDEX abnfdx01 (codscla, idsclas),
    INDEX abnfdx02 (desscla, idsclas)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sigom_cadastro_classificacao (codscla, idsclas);
CREATE INDEX abnfdx02 ON abnf_sigom_cadastro_classificacao (desscla, idsclas);
---------------------------------------------
SHOW COLUMNS FROM abnf_sigom_cadastro_classificacao;
SHOW INDEX FROM abnf_sigom_cadastro_classificacao;
SELECT * FROM abnf_sigom_cadastro_classificacao;
DROP *** TABLE abnf_sigom_cadastro_classificacao;
---------------------------------------------
INSERT *** INTO abnf_sigom_cadastro_classificacao (idsclas, codscla, desscla, situreg, idusucr, dtregcr, idfilia) VALUES
(??, ??, ??, "A", 1, CURRENT_TIMESTAMP(), ??);
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_sigom_cadastro_defeitos_grupos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sigom_cadastro_defeitos_grupos (
    idsdegr     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do grupo de GSD do SIGOM
    codsdeg     INT                                         NOT NULL                            ,   # Código do grupo de GSD do SIGOM
    dessdeg     VARCHAR(100)                                NOT NULL                            ,   # Descrição do grupo de GSD do SIGOM
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    impiifo     BOOLEAN                                     NOT NULL    DEFAULT FALSE           ,   # Impacta no indicador IFO (Índice de falha operacional)
    dashboa     BOOLEAN                                     NOT NULL    DEFAULT FALSE           ,   # Ativo nos dashboards
    INDEX abnfdx01 (codsdeg, idsdegr),
    INDEX abnfdx02 (dessdeg, idsdegr)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sigom_cadastro_defeitos_grupos (codsdeg, idsdegr);
CREATE INDEX abnfdx02 ON abnf_sigom_cadastro_defeitos_grupos (dessdeg, idsdegr);
---------------------------------------------
SHOW COLUMNS FROM abnf_sigom_cadastro_defeitos_grupos;
SHOW INDEX FROM abnf_sigom_cadastro_defeitos_grupos;
SELECT * FROM abnf_sigom_cadastro_defeitos_grupos;
DROP *** TABLE abnf_sigom_cadastro_defeitos_grupos;
---------------------------------------------
ALTER *** TABLE abnf_sigom_cadastro_defeitos_grupos ADD COLUMN dashboa BOOLEAN NOT NULL AFTER impiifo;
UPDATE *** abnf_sigom_cadastro_defeitos_grupos SET dashboa = True;
UPDATE *** abnf_sigom_cadastro_defeitos_grupos SET dashboa = False WHERE idsdegr in (13, 14, 17);
---------------------------------------------
INSERT *** INTO abnf_sigom_cadastro_defeitos_grupos (idsdegr, codsdeg, dessdeg, situreg, idusucr, dtregcr, idfilia) VALUES
(17, 26, 'REVISAO PROGRAMADA (KM)', "A", 1, CURRENT_TIMESTAMP(), 3);
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_sigom_cadastro_defeitos_subgrupos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sigom_cadastro_defeitos_subgrupos (
    idsdesg     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do subgrupo de GSD do SIGOM
    codsdes     INT                                         NOT NULL                            ,   # Código do subgrupo de GSD do SIGOM
    dessdes     VARCHAR(100)                                NOT NULL                            ,   # Descrição do subgrupo de GSD do SIGOM
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idsdegr     INT                                         NOT NULL                            ,   # ID do grupo de GSD do SIGOM (FK)
    INDEX abnfdx01 (codsdes, idsdesg),
    INDEX abnfdx02 (dessdes, idsdesg)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sigom_cadastro_defeitos_subgrupos (codsdes, idsdesg);
CREATE INDEX abnfdx02 ON abnf_sigom_cadastro_defeitos_subgrupos (dessdes, idsdesg);
---------------------------------------------
SHOW COLUMNS FROM abnf_sigom_cadastro_defeitos_subgrupos;
SHOW INDEX FROM abnf_sigom_cadastro_defeitos_subgrupos;
SELECT * FROM abnf_sigom_cadastro_defeitos_subgrupos;
DROP *** TABLE abnf_sigom_cadastro_defeitos_subgrupos;
---------------------------------------------
INSERT INTO abnf_sigom_cadastro_defeitos_subgrupos (idsdesg, codsdes, dessdes, situreg, idusucr, dtregcr, idsdegr) VALUES
(55, 1, 'PREVENTIVA', "A", 1, CURRENT_TIMESTAMP(), 17);
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_sigom_cadastro_defeitos_definicoes ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sigom_cadastro_defeitos_definicoes (
    idsdede     INT                     PRIMARY KEY         NOT NULL                            ,   # ID da definição de GSD do SIGOM
    codsded     INT                                         NOT NULL                            ,   # Código da definição de GSD do SIGOM
    dessded     VARCHAR(100)                                NOT NULL                            ,   # Descrição da definição de GSD do SIGOM
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idsdesg     INT                                         NOT NULL                            ,   # ID do subgrupo de GSD do SIGOM (FK)
    INDEX abnfdx01 (codsded, idsdede),
    INDEX abnfdx02 (dessded, idsdede)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sigom_cadastro_defeitos_definicoes (codsded, idsdede);
CREATE INDEX abnfdx02 ON abnf_sigom_cadastro_defeitos_definicoes (dessded, idsdede);
---------------------------------------------
SHOW COLUMNS FROM abnf_sigom_cadastro_defeitos_definicoes;
SHOW INDEX FROM abnf_sigom_cadastro_defeitos_definicoes;
SELECT * FROM abnf_sigom_cadastro_defeitos_definicoes;
DROP *** TABLE abnf_sigom_cadastro_defeitos_definicoes;
---------------------------------------------
INSERT *** INTO abnf_sigom_cadastro_defeitos_definicoes (idsdede, codsded, dessded, situreg, idusucr, dtregcr, idsdesg) VALUES
(1277, ???, ???, "A", 1, CURRENT_TIMESTAMP(), 55);
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_sigom_movimentacao_ocorrencias ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sigom_movimentacao_ocorrencias(
    idsocor     INT                     PRIMARY KEY         NOT NULL                            ,   # ID da ocorrência do SIGOM
    codsoco     INT                                         NOT NULL                            ,   # Código da ocorrência do SIGOM
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
    situoco     INT                                         NOT NULL                            ,   # Situação da ocorrência: [1]=Aberto/[2]=Em tratativa/[3]=Encerrado
    dataabe     DATE                                        NOT NULL                            ,   # Data de abertura
    horaabe     TIME                                        NOT NULL                            ,   # Horário de abertura
    datafec     DATE                                                                            ,   # Data de fechamento
    horafec     TIME                                                                            ,   # Horário de fechamento
    dataoco     DATE                                        NOT NULL                            ,   # Data da ocorrência
    horaoco     TIME                                        NOT NULL                            ,   # Horário da ocorrência
    horalib     TIME                                                                            ,   # Horário da liberação (obrigatório no encerramento)
    idfunci     INT                                                                             ,   # ID do funcionário envolvido (FK)
    idolinh     INT                                                                             ,   # ID da linha da operação envolvida (FK)
    tabolin     INT                                                                             ,   # Número da tabela da linha da operação envolvida
    linensa     VARCHAR(1)                                                                      ,   # [E]ntrada/[S]aída
    idclfor		INT                                         		                            ,   # ID do cliente (FK)
    tempatr     TIME                                          		                            ,   # Tempo de atraso do cliente (obrigatório no encerramento se selecionado cliente)
    idvedef     INT                                         NOT NULL                            ,   # ID do veículo com defeito (FK)
    idvesub     INT                                                                             ,   # ID do veículo substituto (FK) (obrigatório no encerramento)
    localoc     VARCHAR(100)                                NOT NULL                            ,   # Local da ocorrência
    descroc     TEXT                                        NOT NULL                            ,   # Descrição da ocorrência
    idsocti     INT                                                                             ,   # ID do tipo de ocorrência do SIGOM (FK) (obrigatório no encerramento)
    idsvesi     INT                                                                             ,   # ID da situação de veículo do SIGOM (FK) (obrigatório no encerramento)
    dultprv     DATE                                                                            ,   # Data da última preventiva do veículo
    kmmorto     NUMERIC(10,1)                                                                   ,   # Km morto
    erpdocu     INT                                                                             ,   # Número do documento gerado pelo ERP da empresa (obrigatório no encerramento) (não duplicar)
    idsclas     INT                                                                             ,   # ID da classificação do SIGOM (FK) (obrigatório no encerramento)
    idsdede     INT                                                                             ,   # ID da definição de GSD do SIGOM (FK) (obrigatório no encerramento)
    impiifo     BOOLEAN                                     NOT NULL    DEFAULT FALSE           ,   # Impacta no indicador IFO (Índice de falha operacional)
    kmprogr     NUMERIC(10,1)                                                                   ,   # Km programado
    kmreali     NUMERIC(10,1)                                                                   ,   # Km realizado
    acaotom     TEXT                                                                            ,   # Ação tomada (1000 caracteres)
    idfuate     INT                                                                             ,   # ID do funcionário atendente (FK)
    idfures     INT                                                                             ,   # ID do funcionário responsável (FK)
    ococanc     BOOLEAN                                                                         ,   # Ocorrência cancelada? (Quando o problema foi resolvido somente com instruções)
    idsusab     INT                                         NOT NULL                            ,   # ID do grupo de usuarios do SIGOM que abriu a ocorrência (FK)
    idsusde     INT                                                                             ,   # ID do grupo de usuarios do SIGOM que foi destinado a ocorrência (FK)
    INDEX abnfdx01 (codsoco, idsocor),
    INDEX abnfdx02 (dataabe, horaabe, idsocor),
    INDEX abnfdx03 (dataoco, horaoco, idsocor)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sigom_movimentacao_ocorrencias (codsoco, idsocor);
CREATE INDEX abnfdx02 ON abnf_sigom_movimentacao_ocorrencias (dataabe, horaabe, idsocor);
CREATE INDEX abnfdx03 ON abnf_sigom_movimentacao_ocorrencias (dataoco, horaoco, idsocor);
---------------------------------------------
SHOW COLUMNS FROM abnf_sigom_movimentacao_ocorrencias;
SHOW INDEX FROM abnf_sigom_movimentacao_ocorrencias;
SELECT * FROM abnf_sigom_movimentacao_ocorrencias;
DROP *** TABLE abnf_sigom_movimentacao_ocorrencias;
---------------------------------------------
ALTER *** TABLE abnf_sigom_movimentacao_ocorrencias ADD COLUMN idfuate INT AFTER acaotom;
ALTER *** TABLE abnf_sigom_movimentacao_ocorrencias ADD COLUMN idfures INT AFTER idfuate;
ALTER *** TABLE abnf_sigom_movimentacao_ocorrencias ADD COLUMN ococanc BOOLEAN AFTER idfures;
ALTER *** TABLE abnf_sigom_movimentacao_ocorrencias ADD COLUMN dultprv DATE AFTER idsvesi;
ALTER *** TABLE abnf_sigom_movimentacao_ocorrencias MODIFY dultprv DATE;
---------------------------------------------
ALTER *** TABLE abnf_sigom_movimentacao_ocorrencias MODIFY COLUMN idfunci INT NULL;
ALTER *** TABLE abnf_sigom_movimentacao_ocorrencias MODIFY COLUMN idolinh INT NULL;
---------------------------------------------
SELECT codsoco, ococanc FROM abnf_sigom_movimentacao_ocorrencias;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET ococanc = True WHERE codsoco = 2;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET ococanc = True WHERE codsoco = 4;
---------------------------------------------
*** Karolin, Duda  - Quando ocorrencia estiver bloqueada por estar cancelada ***
SELECT codsoco, ococanc, situoco FROM abnf_sigom_movimentacao_ocorrencias WHERE codsoco = 5597;
UPDATE abnf_sigom_movimentacao_ocorrencias SET ococanc = False WHERE codsoco = 5597;
---------------------------------------------
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET situoco = 1 WHERE codsoco = 1;
SELECT codsoco, situoco FROM abnf_sigom_movimentacao_ocorrencias;
---------------------------------------------
ALTER *** TABLE abnf_sigom_movimentacao_ocorrencias ADD COLUMN impiifo BOOLEAN NOT NULL DEFAULT False AFTER idsdede;
ALTER *** TABLE abnf_sigom_movimentacao_ocorrencias ADD COLUMN kmprogr NUMERIC(10,1) AFTER impiifo;
ALTER *** TABLE abnf_sigom_movimentacao_ocorrencias ADD COLUMN kmreali NUMERIC(10,1) AFTER kmprogr;
---------------------------------------------
SELECT codsoco, situreg, situoco FROM abnf_sigom_movimentacao_ocorrencias WHERE codsoco = 5597;
UPDATE abnf_sigom_movimentacao_ocorrencias SET situoco = 1 WHERE codsoco = 3470;
IFO - Indice de falha operacional
SELECT * FROM abnf_sigom_movimentacao_ocorrencias WHERE codsoco IN (3157, 3151, 3207, 3218, 3263, 3265, 3289, 3292, 3313, 3320, 3319, 3323, 3331, 3369, 3386, 3400, 3406, 3399, 3422);
SELECT * FROM abnf_sigom_movimentacao_ocorrencias WHERE codsoco IN (3481, 3482, 3473, 3491, 3502, 3509, 3511, 3533, 3566, 3583, 3591);
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 11.1 , kmreali = 2.4  WHERE codsoco = 3157;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 11.2 , kmreali = 3    WHERE codsoco = 3151;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 7.7  , kmreali = 4.3  WHERE codsoco = 3207;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 34.4 , kmreali = 21.5 WHERE codsoco = 3218;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 6    , kmreali = 0.1  WHERE codsoco = 3263;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 11.2 , kmreali = 5.6  WHERE codsoco = 3265;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 6.1  , kmreali = 2.3  WHERE codsoco = 3289;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 21.1 , kmreali = 2.2  WHERE codsoco = 3292;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 8.9  , kmreali = 3.1  WHERE codsoco = 3313;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 4.4  , kmreali = 1.6  WHERE codsoco = 3320;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 7.7  , kmreali = 0    WHERE codsoco = 3319;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 10.8 , kmreali = 6.2  WHERE codsoco = 3323;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 7.7  , kmreali = 0.5  WHERE codsoco = 3331;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 22.4 , kmreali = 3.9  WHERE codsoco = 3369;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 8.2  , kmreali = 5.2  WHERE codsoco = 3386;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 10.2 , kmreali = 2.8  WHERE codsoco = 3400;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 14.9 , kmreali = 4.4  WHERE codsoco = 3406;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 5.6  , kmreali = 1.8  WHERE codsoco = 3399;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 8.3  , kmreali = 1.7  WHERE codsoco = 3422;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 19.5 , kmreali = 5.8  WHERE codsoco = 3481;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 19.2 , kmreali = 2.9  WHERE codsoco = 3482;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 8.3  , kmreali = 3.6  WHERE codsoco = 3473;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 9.5  , kmreali = 4.9  WHERE codsoco = 3491;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 17.6 , kmreali = 6.1  WHERE codsoco = 3502;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 10.5 , kmreali = 4.5  WHERE codsoco = 3509;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 8.7  , kmreali = 1.7  WHERE codsoco = 3511;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 11.2 , kmreali = 4    WHERE codsoco = 3533;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 3.6  , kmreali = 0.5  WHERE codsoco = 3566;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 21.7 , kmreali = 10.8 WHERE codsoco = 3583;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 14.5 , kmreali = 4.5  WHERE codsoco = 3591;
SELECT codsoco, impiifo, kmprogr, kmreali FROM abnf_sigom_movimentacao_ocorrencias WHERE codsoco IN (3473, 3482, 3511, 3533, 3566, 3583, 3591, 3621, 3626, 3628, 3637, 3657, 3667, 3691, 3694);
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 7.3  , kmreali = 3.7  WHERE codsoco = 3621;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 8.6  , kmreali = 1.5  WHERE codsoco = 3626;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 12.2 , kmreali = 1.3  WHERE codsoco = 3628;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 5.2  , kmreali = 3.3  WHERE codsoco = 3637;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 12   , kmreali = 7.9  WHERE codsoco = 3657;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 5.6  , kmreali = 2.7  WHERE codsoco = 3667;
UPDATE *** abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 19.2 , kmreali = 1.3  WHERE codsoco = 3691;
UPDATE abnf_sigom_movimentacao_ocorrencias SET impiifo = True, kmprogr = 11.2 , kmreali = 6.7 WHERE codsoco = 3470;
UPDATE abnf_sigom_movimentacao_ocorrencias SET idvedef = 638 WHERE codsoco = 3470;
select descroc from abnf_sigom_movimentacao_ocorrencias where codsoco = 3470;
UPDATE abnf_sigom_movimentacao_ocorrencias SET descroc = 'AR CONDICIONADO NAO FUNCIONA' WHERE codsoco = 3470;
SELECT codsoco, impiifo FROM abnf_sigom_movimentacao_ocorrencias WHERE codsoco IN (3481, 3491, 3502, 3509);
UPDATE abnf_sigom_movimentacao_ocorrencias SET impiifo = False WHERE codsoco IN (3481, 3491, 3502, 3509);
UPDATE abnf_sigom_movimentacao_ocorrencias SET descroc = 'FALHA NO SENSOR DO ELEVADOR' WHERE codsoco = 3626;
3621	7.3	    3.7
3626	8.6	    1.5
3628	12.2	1.3
3637	5.2	    3.3
3657	12	    7.9
3667	5.6	    2.7
3691	19.2	1.3
MariaDB [gb001]> SELECT codsoco, impiifo, kmprogr, kmreali FROM abnf_sigom_movimentacao_ocorrencias WHERE codsoco IN (3473, 3482, 3511, 3533, 3566, 3583, 3591, 3621, 3626, 3628, 3637, 3657, 3667, 3691, 3694);
+---------+---------+---------+---------+
| codsoco | impiifo | kmprogr | kmreali |
+---------+---------+---------+---------+
|    3473 |       1 |     8.3 |     3.6 |
|    3482 |       1 |    19.2 |     2.9 |
|    3511 |       1 |     8.7 |     1.7 |
|    3533 |       1 |    11.2 |     4.0 |
|    3566 |       1 |     3.6 |     0.5 |
|    3583 |       1 |    21.7 |    10.8 |
|    3591 |       1 |    14.5 |     4.5 |
|    3621 |       1 |     7.3 |     3.7 |
|    3626 |       1 |     8.6 |     1.5 |
|    3628 |       1 |    12.2 |     1.3 |
|    3637 |       1 |     5.2 |     3.3 |
|    3657 |       1 |    12.0 |     7.9 |
|    3667 |       1 |     5.6 |     2.7 |
|    3691 |       1 |    19.2 |     1.3 |
|    3694 |       1 |    18.8 |     4.0 |
+---------+---------+---------+---------+
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_sigom_movimentacao_ocorrencias_complementos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sigom_movimentacao_ocorrencias_complementos(
    idsocco     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do complemento de ocorrência do SIGOM
	idsocor     INT                                         NOT NULL                            ,   # ID da ocorrência do SIGOM (FK)
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    datacom     DATE                                        NOT NULL                            ,   # Data do complemento
    horacom     TIME                                        NOT NULL                            ,   # Horário do complemento
    descrco     TEXT                                        NOT NULL                            ,   # Descrição do complemento
    idsusab     INT                                         NOT NULL                            ,   # ID do grupo de usuarios do SIGOM que abriu o complemento (FK)
    idsusde     INT                                         NOT NULL                            ,   # ID do grupo de usuarios do SIGOM que foi destinado o complemento (FK)
    INDEX abnfdx01 (datacom, horacom, idsocco)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sigom_movimentacao_ocorrencias_complementos (datacom, horacom, idsocco);
---------------------------------------------
SHOW COLUMNS FROM abnf_sigom_movimentacao_ocorrencias_complementos;
SHOW INDEX FROM abnf_sigom_movimentacao_ocorrencias_complementos;
SELECT * FROM abnf_sigom_movimentacao_ocorrencias_complementos;
DROP *** TABLE abnf_sigom_movimentacao_ocorrencias_complementos;
---------------------------------------------
ALTER *** TABLE abnf_sigom_movimentacao_ocorrencias_complementos MODIFY COLUMN descrco TEXT;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_sigom_movimentacao_ocorrencias_arquivos ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
CREATE TABLE abnf_sigom_movimentacao_ocorrencias_arquivos(
	idsocar     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do arquivo de ocorrência do SIGOM
	idsocor     INT                                         NOT NULL                            ,   # ID da ocorrência do SIGOM (FK)
    idsocco     INT                                         NOT NULL                            ,   # ID do complemento de ocorrência do SIGOM
    situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
    idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
    idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
    dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
    dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
    idarqui     INT                                                                             ,   # ID do arquivo (FK)
    INDEX abnfdx01 (idsocor, idsocco, idsocar)
);
---------------------------------------------
CREATE INDEX abnfdx01 ON abnf_sigom_movimentacao_ocorrencias_arquivos (idsocor, idsocco, idsocar);
---------------------------------------------
SHOW COLUMNS FROM abnf_sigom_movimentacao_ocorrencias_arquivos;
SHOW INDEX FROM abnf_sigom_movimentacao_ocorrencias_arquivos;
SELECT * FROM abnf_sigom_movimentacao_ocorrencias_arquivos;
DROP *** TABLE abnf_sigom_movimentacao_ocorrencias_arquivos;
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠ abnf_operacional_cadastro_tipos_viagem ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
(Mudança de planos: usar informações fixas no lugar de tabela) ==> CREATE TABLE abnf_operacional_cadastro_tipos_viagem (
(Mudança de planos: usar informações fixas no lugar de tabela) ==>     idotivi     INT                     PRIMARY KEY         NOT NULL                            ,   # ID do tipo de viagem
(Mudança de planos: usar informações fixas no lugar de tabela) ==>     codotiv     INT                                         NOT NULL                            ,   # Código do tipo de viagem
(Mudança de planos: usar informações fixas no lugar de tabela) ==>     desotiv     VARCHAR(100)                                NOT NULL                            ,   # Descrição do tipo de viagem
(Mudança de planos: usar informações fixas no lugar de tabela) ==>     situreg     VARCHAR(1)                                  NOT NULL                            ,   # Situação do registro: [A]tivo/[I]nativo/[C]ancelado
(Mudança de planos: usar informações fixas no lugar de tabela) ==>     idusucr     INT                                         NOT NULL                            ,   # ID do usuário que criou o registro (FK)
(Mudança de planos: usar informações fixas no lugar de tabela) ==>     idusual     INT                                                                             ,   # ID do usuário que alterou/excluiu o registro (FK)
(Mudança de planos: usar informações fixas no lugar de tabela) ==>     dtregcr     DATETIME                                    NOT NULL                            ,   # Data/hora de criação do registro
(Mudança de planos: usar informações fixas no lugar de tabela) ==>     dtregal     DATETIME                                                                        ,   # Data/hora de alteração/exclusão do registro
(Mudança de planos: usar informações fixas no lugar de tabela) ==>     idfilia     INT                                         NOT NULL                            ,   # ID da filial (FK)
(Mudança de planos: usar informações fixas no lugar de tabela) ==>     tranpas     BOOLEAN                                     NOT NULL    DEFAULT FALSE           ,   # Transporta passageiros?
(Mudança de planos: usar informações fixas no lugar de tabela) ==>     observa     TEXT                                                                            ,   # Observação
(Mudança de planos: usar informações fixas no lugar de tabela) ==>     INDEX abnfdx01 (codotiv, idotivi),
(Mudança de planos: usar informações fixas no lugar de tabela) ==>     INDEX abnfdx02 (desotiv, idotivi)
(Mudança de planos: usar informações fixas no lugar de tabela) ==> );
---------------------------------------------
(Mudança de planos: usar informações fixas no lugar de tabela) ==> CREATE INDEX abnfdx01 ON abnf_operacional_cadastro_tipos_viagem (codotiv, idotivi);
(Mudança de planos: usar informações fixas no lugar de tabela) ==> CREATE INDEX abnfdx02 ON abnf_operacional_cadastro_tipos_viagem (desotiv, idotivi);
---------------------------------------------
(Mudança de planos: usar informações fixas no lugar de tabela) ==> DROP *** TABLE abnf_operacional_cadastro_tipos_viagem;
(Mudança de planos: usar informações fixas no lugar de tabela) ==> DROP *** INDEX abnfdx?? ON abnf_operacional_cadastro_tipos_viagem;
---------------------------------------------
(Mudança de planos: usar informações fixas no lugar de tabela) ==> SHOW COLUMNS FROM abnf_operacional_cadastro_tipos_viagem;
(Mudança de planos: usar informações fixas no lugar de tabela) ==> SHOW INDEX FROM abnf_operacional_cadastro_tipos_viagem;
---------------------------------------------
(Mudança de planos: usar informações fixas no lugar de tabela) ==> SELECT * FROM abnf_operacional_cadastro_tipos_viagem;
(Mudança de planos: usar informações fixas no lugar de tabela) ==> DELETE *** FROM abnf_operacional_cadastro_tipos_viagem WHERE idotivi = 1;
---------------------------------------------
OCIOSO: SAIDA E RETORNO DA GARAGEM
PRODUTIVO: LEVA PASSAGEIROS
RESERVADO: NAO LEVA PASSAGEIRO, UTILIZADO NOS PICOS ONDE A DEMANDA ESTA CONCENTRADA EM UMA DAS PONTAS DA LINHA.
DESLOCAMENTO: UM ONIBUS QUE FAZ MAIS DE UMA LINHA. ENCERRA NO PONTO X E DESLOCA PARA O Y PARA REALIZAR A OUTRA LINHA.
---------------------------------------------
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
# ⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠ #
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ #
---------------------------------------------
'''