## ======================================================================================================
## [abnf000u00s00003.py] - Arquivo de funções comuns que serão utilizadas por todos os módulos do sistema
## ======================================================================================================

from flask_socketio import emit                         # Biblioteca do Flask-SocketIO (Websockets)
from flask import request                               # Biblioteca que captura IPs das maquinas clientes
from datetime import date, datetime, time, timedelta    # Biblioteca de data e hora

import time                                             # Biblioteca do sleep
import os                                               # Biblioteca de funções que interagem com o SO
# import re                                             # Usado em "abnf_valida_email" ==> Travando o sistema todo na análise (não vale a pena)
import base64                                           # Biblioteca que decodifica um arquivo de imagem em arquivo texto
import uuid                                             # Biblioteca para geração de token
import decimal                                          # Biblioteca usada para definiar a quantidade de casas decimais em um variável tipo "decimal"

dglobdws = {}                                           # Inicia o dicionário global

# Jamais fazer a importação 'import datetime' e a função 'timedelta' também - ex: datetime.timedelta(days = iqtddias)
# Elas dão conflito com as funções vinda de: 'from datetime import...'
# Buscar no sistema e remover todas elas:
# clear ; find . -name "abnf000u*.py" -exec grep -iH "timedelta" {} \;
# clear ; find . -name "abnf000u*.py" -exec grep -iH "import datetime" {} \;
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_valida_projeto_token ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que valida os projetos e os tokens capturados da pagina HTML/CSS/JS.                                                                         // #
# // Todo modulo tem que validar essa função antes de executar seu objetivo.                                                                             // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #  
    
def abnf_valida_projeto_token(dabnfopg):
    bvalidad = False
    sabnproj = dabnfopg['abnproje'][2] if dabnfopg.get('abnproje', None) != None else None
    sabntoke = dabnfopg['abntoken'][2] if dabnfopg.get('abntoken', None) != None else None
    print('sabnproj: ' + str(sabnproj))
    print('sabntoke: ' + str(sabntoke))
    print('dabnfopg: ' + str(dabnfopg))
    print('----------------------------------------------------------------------------------------------------------------------------------')
    if   sabnproj == None: abnf_alert('Falha de sistema: projeto inválido!', 4)
    elif sabntoke == None: abnf_alert('Falha de sistema: token inválido!', 4)
    else:    
        if not sabnproj in [
            '10000000000010000',    # Tupi Transporte
            '12792863164510001',    # Tupi Transporte
            '17646826035010002',    # Rápido Sumaré Piracicaba
            '15047354061710003',    # Trans Acreana
            ]:
            abnf_alert('Falha de sistema: projeto não encontrado!', 4)
        else:
            bvalidad = True
    return bvalidad, sabnproj, sabntoke
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_socket_004 ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função para enviar informações para a página principal HTML/CSS/JS via JS através da função 'emit' do flask_socketio.                               // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_socket_004(lskio004):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_socket_004 (AbnfReceivedForm)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    print(lskio004)
    emit('AbnfReceivedForm', lskio004)
    print('----------------------------------------------------------------------------------------------------------------------------------')
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_websocket_control_globdws ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que controla o dicionário global "dglobdws" (Método em memória).                                                                             // #
# // A chave desse dicionário é o projeto (sabnproj) e o token da página (sabntoke).                                                                     // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #    
    
def abnf_websocket_control_globdws(sabnproj, sabntoke, lparamet):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_websocket_control_globdws (Controla o dicionário global "dglobdws")')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    imaximin = 20                                                               # Tempo máximo de validade do registro em inatividade (em minutos)
    scaptuip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)       # IP de quem está usando o sistema
    ddttmnow = datetime.now()                                                   # Data/hora atual
    # ////////////////////////////////////////
    # Removendo registros com chaves expiradas
    # ////////////////////////////////////////
    lexcdreg = []
    for lglobdws in dglobdws:
        dultiuso = dglobdws[lglobdws]['dultiuso']                               # Data/hora do ultimo uso do registro
        idifminu = int((ddttmnow - dultiuso).total_seconds() / 60)              # Diferença em minutos entre a data/hora atual e a data/hora do último uso do registro
        if idifminu > imaximin:
            lexcdreg.append(lglobdws)
    if lexcdreg != []:
        for lglobdws in lexcdreg:
            print('Removendo registro com chave expirada .: ' + str(lglobdws) + ' - último uso: ' + str(dglobdws[lglobdws]['dultiuso']))
            dglobdws.pop(lglobdws)
        print('----------------------------------------------------------------------------------------------------------------------------------')
    # ///////////////////////////////
    # 01: Requisição de novo registro
    # ///////////////////////////////
    if lparamet[0] == 1:
        print('[ Parâmetro 01 ]')
        dglobdws[(sabnproj, sabntoke)] = {}
        dglobdws[(sabnproj, sabntoke)]['dultiuso'] = ddttmnow
        dglobdws[(sabnproj, sabntoke)]['sabnfsys'] = '00S00201A'                # abnf000u00s00200_login_sistema (página de login do sistema) - primeiro modulo para entrar no sistema
        dglobdws[(sabnproj, sabntoke)]['iidusuar'] = 0                          # ID do usuário - inicialmente zero, mas assume valor após passar pelo módulo de login
        dglobdws[(sabnproj, sabntoke)]['iidempre'] = 0                          # ID da empresa - inicialmente zero, mas assume valor após passar pelo módulo de definição da filial
        dglobdws[(sabnproj, sabntoke)]['iidfilia'] = 0                          # ID da filial - inicialmente zero, mas assume valor após passar pelo módulo de definição da filial
        dglobdws[(sabnproj, sabntoke)]['slogosys'] = lparamet[1]                # Logo do sistema
        print('Requisição de novo registro ...............: ' + str(dglobdws[(sabnproj, sabntoke)]))
        print('Requisição de novo registro ...............: ' + str(lparamet[1]))
    # //////////////////////////////////////////////
    # 02: Leitura de um regstro do dicionário global
    # //////////////////////////////////////////////
    elif lparamet[0] == 2:
        dglobaux = dglobdws.get((sabnproj, sabntoke), None)                     # De todas as informações do dicionário global (dglobdws), separa somente a que foi solicitada (dglobaux)
        if dglobaux == None:                                                    # Token não encontrado
            abnf_socket_004([4, '', ''])                                        # Então reinicia o sistema (refresh)
        else:
            print('[ Parâmetro 02 ]')
            print('Buscando registro (projeto) ...............: ' + str(sabnproj))
            print('Buscando registro (token) .................: ' + str(sabntoke))
            print('Registro encontrado .......................: ' + str(dglobaux))
            dglobaux['dultiuso'] = ddttmnow                                     # Antes de retornar o ítem solicitado, é atualizado a data do ultimo uso do registro                          
            print('Registro encontrado com data atualizada ...: ' + str(dglobaux))
            if lparamet[1] != None:                                             # Se o segundo ítem do parâmetro 2 não for nulo então será usado para abastecer "sabnfsys"
                dglobaux['sabnfsys'] = lparamet[1]                              # "sabnfsys" vai receber o próximo módulo que o sistema deverá buscar
            return dglobaux                                                     # Retorna o dicionário dglobaux
    # ///////////////////////////////////////////////////////////////
    # 03: Atualiza uma informação em um registro do dicionário global
    # ///////////////////////////////////////////////////////////////
    elif lparamet[0] == 3:
        dglobaux = dglobdws.get((sabnproj, sabntoke), None)                     # De todas as informações do dicionário global (dglobdws), separa somente a que foi solicitada (dglobaux)
        if dglobaux == None:                                                    # Token não encontrado
            abnf_socket_004([4, '', ''])                                        # Então reinicia o sistema (refresh)
        else:
            print('[ Parâmetro 03 ]')
            print('Atualizando registro (projeto) ............: ' + str(sabnproj))
            print('Atualizando registro (token) ..............: ' + str(sabntoke))
            for lauxi001 in lparamet[1]:
                sitchave = lauxi001[0]                                          # Parâmetro 01 - Chave do ítem que deseja que seja feita a atualização
                xvalorit = lauxi001[1]                                          # Parâmetro 02 - Valor que deseja que seja inserida no ítem
                print('Chave do campo a ser alterado .............: ' + str(sitchave))
                print('Valor a ser inserido no campo .............: ' + str(xvalorit))
                dglobaux[ sitchave ] = xvalorit                                 # Atualiza o ítem com o valor desejado
                dglobaux['dultiuso'] = ddttmnow                                 # Atualiza a data do ultimo uso do registro
            print('Registro após a atualização ...............: ' + str(dglobaux))
            return dglobaux                                                     # Retorna o dicionário dglobaux
    # //////////////////////////////////
    # Mostra os registros atuais válidos
    # //////////////////////////////////
    print('----------------------------------------------------------------------------------------------------------------------------------')
    for lglobdws in dglobdws:
        print('Registro atual válido .....................: ' + str(dglobdws[lglobdws]))
    print('----------------------------------------------------------------------------------------------------------------------------------')
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_alert ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que emite uma mensagem na tela no mesmo formato da função Flash do Flask.                                                                    // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #    
    
def abnf_alert(smessage, iparaler):
    if   iparaler in (1,11): sauxi001 = 'primary'
    elif iparaler in (2,12): sauxi001 = 'secondary'
    elif iparaler in (3,13): sauxi001 = 'success'
    elif iparaler in (4,14): sauxi001 = 'danger'
    elif iparaler in (5,15): sauxi001 = 'warning'
    elif iparaler in (6,16): sauxi001 = 'info'
    elif iparaler in (7,17): sauxi001 = 'light'
    elif iparaler in (8,18): sauxi001 = 'dark'
    if iparaler > 0:         smessage = '<div class="alert alert-' + sauxi001 + '" role="alert">&#128073; ' + smessage
    else:                    smessage = '<div class="alert alert-success" role="alert">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
    if iparaler > 10:
        smessage = smessage + '&nbsp;&nbsp;<div class="spinner-border" style="width: 1rem; height: 1rem;" role="status">'
        smessage = smessage + '<span class="sr-only"></span>'
        smessage = smessage + '</div><div class="spinner-grow" style="width: 1rem; height: 1rem;" role="status">'
        smessage = smessage + '<span class="sr-only"></span>'
        smessage = smessage + '</div>'
    abnf_socket_004([1, 'abnfdv02', smessage])
    # Nota: 14/07/2024
    # O procedimento abaixo não funcionou como esperado.
    # Ele faz o scroll incompleto, não chegando ao topo da pagina.
    # Provavelmente seja resolvido apenas com pequenos ajustes no JS como a quantide de linhas a subir.
    # Mas ao invés disso vamos fazer um teste com a abnfdv01 e abnfdv02 fixas na tela.
    # Se não der certo, voltamos a explorar a solução abaixo.
    # if smessage == '':  abnf_socket_004([1, 'abnfdv02', smessage])  # Envio de mensagem sem scroll de tela do navegador
    # else:               abnf_socket_004([8, 'abnfdv02', smessage])  # Envio de mensagem com scroll de tela do navegador
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_show ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que emite uma mensagem em uma div do sistema para auxiliar na programação (não usado no sistema em produção).                                // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    
def abnf_show(sdivsist, xmessage, itipshow):
    if itipshow == 0:    # linear
        smessage = '<div class="alert alert-info" role="alert"><font color="black" face="Courier New" size="3"><b>&#128681; ' + str(xmessage) + '</b></font></div>'
    elif itipshow == 1:  # listas/tuplas
        smessage = '<div class="alert alert-info" role="alert">'
        for lauxi001 in xmessage:
            smessage = smessage + '<font color="black" face="Courier New" size="3"><b>&#128681; ' + str(lauxi001) + '</b></font><br>'
        smessage = smessage + '</div>'
    elif itipshow == 2:  # dicionários
        smessage = '<div class="alert alert-info" role="alert">'
        for lauxi001 in xmessage:
            smessage = smessage + '<font color="black" face="Courier New" size="3"><b>&#128681; ' + str(lauxi001) + ' - ' + str(xmessage[lauxi001]) + '</b></font><br>'
        smessage = smessage + '</div>'
    abnf_socket_004([1, 'abnfdv' + sdivsist, smessage])
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_create_page ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função para criar os campos que serão disponibilizados para o usuário na pagina HTML/CSS/JS.                                                        // #
# // Esta função lê a lista ldatpage, monta a estrutura conforme as regras e devolve para ser inserido na página via websocket.                          // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #    
    
def abnf_create_page(ldatpage):
    sremospa = '' # '\n'
    shtmpage = ''
    inumsele = 1
    # método antigo => inumbutt = 1
    # sdeffogr = 'form-group'               # Não ultrapassa os limites das bordas, porém os textos não ficam alinhados com as legendas
    sdeffogr = 'form-group row'             # Ultrapassa os limites das bordas, porém os textos ficam alinhados com as legendas
    dhalignx = {0: 'left', 1: 'center', 2: 'right'}
    dvalignx = {0: 'top', 1: 'middle', 2: 'bottom'}
    for laxui001 in ldatpage:
        if laxui001 != None:                # Possibilita usar "None" nas tuplas que formam a page
            if   laxui001[0] == 'fg-0':
                sdeffogr = 'form-group'     # Não ultrapassa os limites das bordas, porém os textos não ficam alinhados com as legendas
            elif laxui001[0] == 'fg-1':
                sdeffogr = 'form-group row' # Ultrapassa os limites das bordas, porém os textos ficam alinhados com as legendas
            elif laxui001[0] == 'hr-0':
                shtmpage = shtmpage + '<hr>'
            elif laxui001[0] == 'br-0':
                shtmpage = shtmpage + '<br>'
            elif laxui001[0] == 'div-0':
                shtmpage = shtmpage + '<div'
                if laxui001[1] != None: shtmpage = shtmpage + ' class="' + laxui001[1] + '"'
                if laxui001[2] != None: shtmpage = shtmpage + ' style="' + laxui001[2] + '"'
                shtmpage = shtmpage + '>' + (laxui001[3] if laxui001[3] != None else '')
            elif laxui001[0] == 'div-1':
                shtmpage = shtmpage + '<div id="' + laxui001[1] + '">'
            elif laxui001[0] == 'div-2':
                shtmpage = shtmpage + '<div id="' + laxui001[1] + '" class="form-group collapse">'
            elif laxui001[0] == 'div-9':
                shtmpage = shtmpage + '</div>'
            elif laxui001[0] == 'form-0':
                shtmpage = shtmpage + '<form action=""'
                if laxui001[1] != None: shtmpage = shtmpage + ' class="' + laxui001[1] + '"'
                shtmpage = shtmpage + '>'
            elif laxui001[0] == 'form-9':
                shtmpage = shtmpage + '</form>' 
            elif laxui001[0] == 'legend-0':
                shtmpage = shtmpage + '<legend>' + laxui001[1] + '</legend>'
            elif laxui001[0] == 'label-0':
                shtmpage = shtmpage + '<label'
                if laxui001[2] != None: shtmpage = shtmpage + ' class="' + laxui001[2] + '"'
                if len(laxui001) >= 4 and laxui001[3] != None:  # Dessa forma consigo saber se o usuário utilizou esse parâmetro nessa função sem ter que criar um novo 'label-?'
                     shtmpage = shtmpage + '><a title="' + laxui001[3] + '"'
                shtmpage = shtmpage + '>' + laxui001[1] + '</label>'
            elif laxui001[0] == 'label-1':
                shtmpage = shtmpage + '<font style="font-family: ' + laxui001[1] + '; '
                shtmpage = shtmpage + 'font-size: ' + laxui001[2] + '; '
                shtmpage = shtmpage + 'font-weight: bold; '
                if laxui001[3] != None: shtmpage = shtmpage + 'color: ' + laxui001[3]
                shtmpage = shtmpage + '"><b><label'
                if laxui001[4] != None: shtmpage = shtmpage + ' class="' + laxui001[4] + '" '
                shtmpage = shtmpage + 'id="' + laxui001[5] + '" '
                shtmpage = shtmpage + 'name="' + laxui001[5] + '"'
                shtmpage = shtmpage + '>'
                if laxui001[6] != None: shtmpage = shtmpage + laxui001[6]
                shtmpage = shtmpage + '</label></b></font>'
            elif laxui001[0] in ('font-0'):
                shtmpage = shtmpage + '<font style="font-family: ' + laxui001[1] + '; '
                shtmpage = shtmpage + 'font-size: ' + laxui001[2] + '; '
                shtmpage = shtmpage + 'font-weight: bold; '
                if laxui001[3] != None: shtmpage = shtmpage + 'color: ' + laxui001[3]
                if len(laxui001) >= 6 and laxui001[5] != None:  # Dessa forma consigo saber se o usuário utilizou esse parâmetro nessa função sem ter que criar um novo 'font-?'
                    shtmpage = shtmpage + ';animation: abnfblink ' + str(laxui001[5]) +'s infinite;'
                if len(laxui001) >= 7 and laxui001[6] != None:  # Dessa forma consigo saber se o usuário utilizou esse parâmetro nessa função sem ter que criar um novo 'font-?'
                    shtmpage = shtmpage + '"><a title="' + laxui001[6]
                shtmpage = shtmpage + '"><b>' + str(laxui001[4]) + '</b></font>'
            elif laxui001[0] in ['input-0', 'password-0', 'cpf-0', 'cnpj-0', 'cep-0', 'phone-0']:
                shtmpage = shtmpage + '<fieldset><div class="' + sdeffogr + '">'
                shtmpage = shtmpage + '<input autocomplete="off" '
                if laxui001[2] != None: shtmpage = shtmpage + 'class="' + laxui001[2] + '" '
                shtmpage = shtmpage + 'id="' + laxui001[1] + '" '
                shtmpage = shtmpage + 'name="' + laxui001[1] + '" '
                shtmpage = shtmpage + 'minlength="' + str(laxui001[3]) + '" '
                shtmpage = shtmpage + 'maxlength="' + str(laxui001[4]) + '" '
                shtmpage = shtmpage + 'onKeyUp="'
                if   laxui001[0] == 'cpf-0':    shtmpage = shtmpage + 'AbnfMaskCPF(event),'
                elif laxui001[0] == 'cnpj-0':   shtmpage = shtmpage + 'AbnfMaskCNPJ(event),'
                elif laxui001[0] == 'cep-0':    shtmpage = shtmpage + 'AbnfMaskCEP(event),'
                elif laxui001[0] == 'phone-0':  shtmpage = shtmpage + 'AbnfMaskPhone(event),'
                shtmpage = shtmpage + 'AbnfTabEnter(event,getElementById(&#39;' + laxui001[7] + '&#39;));" '
                shtmpage = shtmpage + 'onfocus="this.select()" '
                shtmpage = shtmpage + 'onkeypress="return AbnfScriptKey(event)" '
                # shtmpage = shtmpage + '''onblur="AbnfSubmitForm(event, '45');" '''
                shtmpage = shtmpage + 'spellcheck="true" '
                if   laxui001[9] == 0: saligntx = 'left'
                elif laxui001[9] == 1: saligntx = 'center'
                elif laxui001[9] == 2: saligntx = 'right'
                shtmpage = shtmpage + 'style="text-transform:uppercase; font-family: Courier New; font-size: ' + laxui001[5] + '; font-weight: bold; text-align: ' + saligntx + ';'
                if not laxui001[8]: shtmpage = shtmpage + ' color: brown'
                shtmpage = shtmpage + '" '
                if   laxui001[0] in ['input-0', 'cpf-0', 'cnpj-0', 'cep-0', 'phone-0']:   sauxityp = 'text'
                elif laxui001[0] == 'password-0':                                         sauxityp = 'password'
                shtmpage = shtmpage + 'type="' + sauxityp + '" '
                sauxival = '' if laxui001[6] == None else str(laxui001[6])
                shtmpage = shtmpage + 'value="' + sauxival + '"'
                if not laxui001[8]: shtmpage = shtmpage + ' readonly'
                shtmpage = shtmpage + '>'
                shtmpage = shtmpage + '</div></fieldset>'
            elif laxui001[0] == 'number-0':
                shtmpage = shtmpage + '<fieldset><div class="' + sdeffogr + '">'
                shtmpage = shtmpage + '<input autocomplete="off" '
                if laxui001[2] != None: shtmpage = shtmpage + 'class="' + laxui001[2] + '" '
                shtmpage = shtmpage + 'id="' + laxui001[1] + '" '
                shtmpage = shtmpage + 'name="' + laxui001[1] + '" '
                shtmpage = shtmpage + 'minlength="' + str(laxui001[3]) + '" '
                shtmpage = shtmpage + 'maxlength="' + str(laxui001[4]) + '" '
                shtmpage = shtmpage + 'onKeyUp="AbnfMaxLength(this,' + str(laxui001[4]) + ');AbnfTabEnter(event,getElementById(&#39;' + laxui001[7] + '&#39;));" '
                shtmpage = shtmpage + 'onfocus="this.select()" '
                shtmpage = shtmpage + 'onkeypress="return AbnfScriptIntegerOnly(event)" '
                if laxui001[9] != None: shtmpage = shtmpage + 'onblur="AbnfSubmitForm(event,' + "'" + laxui001[9] + "'" + ');" '
                shtmpage = shtmpage + 'spellcheck="false" '
                shtmpage = shtmpage + 'style="text-transform:uppercase; font-family: Courier New; font-size: ' + laxui001[5] + '; font-weight: bold;'
                if not laxui001[8]: shtmpage = shtmpage + ' color: brown'
                shtmpage = shtmpage + '" '
                shtmpage = shtmpage + 'type="number" '
                sauxival = '' if laxui001[6] == None else str(laxui001[6])
                shtmpage = shtmpage + 'value="' + sauxival + '"'
                if not laxui001[8]: shtmpage = shtmpage + ' readonly'
                shtmpage = shtmpage + '>'
                shtmpage = shtmpage + '</div></fieldset>'
            elif laxui001[0] == 'thscom-0': # thousands separator & comma':
                shtmpage = shtmpage + '<fieldset><div class="' + sdeffogr + '">'
                shtmpage = shtmpage + '<input autocomplete="off" '
                if laxui001[2] != None: shtmpage = shtmpage + 'class="' + laxui001[2] + '" '
                shtmpage = shtmpage + 'id="' + laxui001[1] + '" '
                shtmpage = shtmpage + 'name="' + laxui001[1] + '" '
                shtmpage = shtmpage + 'minlength="' + str(laxui001[3]) + '" '
                shtmpage = shtmpage + 'maxlength="' + str(laxui001[4]) + '" '
                shtmpage = shtmpage + 'onKeyUp="AbnfTabEnter(event,getElementById(&#39;' + laxui001[7] + '&#39;));AbnfNumMaskDecimal(this,' + str(laxui001[8]) + ');" '
                shtmpage = shtmpage + 'onfocus="this.select()" '
                shtmpage = shtmpage + 'onkeypress="return AbnfScriptKey(event)" '
                if laxui001[11] != None: shtmpage = shtmpage + 'onblur="AbnfSubmitForm(event,' + "'" + laxui001[11] + "'" + ');" '
                shtmpage = shtmpage + 'spellcheck="true" '
                if   laxui001[10] == 0: saligntx = 'left'
                elif laxui001[10] == 1: saligntx = 'center'
                elif laxui001[10] == 2: saligntx = 'right'
                shtmpage = shtmpage + 'style="text-transform:uppercase; font-family: Courier New; font-size: ' + laxui001[5] + '; font-weight: bold; text-align: ' + saligntx + ';'
                if not laxui001[9]: shtmpage = shtmpage + ' color: brown'
                shtmpage = shtmpage + '" '
                shtmpage = shtmpage + 'type="text" '
                sauxival = '' if laxui001[6] == None else str(laxui001[6])
                shtmpage = shtmpage + 'value="' + sauxival + '"'
                if not laxui001[9]: shtmpage = shtmpage + ' readonly'
                shtmpage = shtmpage + '>'
                shtmpage = shtmpage + '</div></fieldset>'
            elif laxui001[0] in ['date-0', 'time-0', 'time-1']:
                # date-0 -> Padrão normal de data fornecido pelo html
                # time-0 -> Padrão normal de hora fornecido pelo html
                # time-1 -> Não assume o padrão de hora do html -> utilizado para poder digitar a hora fora do padrão (Ex: 26:35)
                shtmpage = shtmpage + '<fieldset><div class="' + sdeffogr + '">'
                shtmpage = shtmpage + '<input autocomplete="off" '
                if laxui001[2] != None: shtmpage = shtmpage + 'class="' + laxui001[2] + '" '
                shtmpage = shtmpage + 'id="' + laxui001[1] + '" size=5 maxlength="5" '
                shtmpage = shtmpage + 'name="' + laxui001[1] + '" '
                shtmpage = shtmpage + 'onKeyUp="AbnfTabEnter(event,getElementById(&#39;' + laxui001[5] + '&#39;));" '
                shtmpage = shtmpage + 'onfocus="this.select()" '
                shtmpage = shtmpage + 'onkeypress="return AbnfTimeMask(event)" '
                if laxui001[8] != None: shtmpage = shtmpage + 'onblur="AbnfSubmitForm(event,' + "'" + laxui001[8] + "'" + ');" '
                shtmpage = shtmpage + 'spellcheck="false" '
                if   laxui001[7] == 0: saligntx = 'left'
                elif laxui001[7] == 1: saligntx = 'center'
                elif laxui001[7] == 2: saligntx = 'right'
                shtmpage = shtmpage + 'style="text-transform:uppercase; font-family: Courier New; font-size: ' + laxui001[3] + '; font-weight: bold; text-align: ' + saligntx + ';'
                if not laxui001[6]: shtmpage = shtmpage + ' color: brown'
                shtmpage = shtmpage + '" '
                if   laxui001[0] == 'date-0': sauxityp = 'date'
                elif laxui001[0] == 'time-0': sauxityp = 'time'
                else: sauxityp = 'text'        
                shtmpage = shtmpage + 'type="' + sauxityp + '" '
                sauxival = '' if laxui001[4] == None else str(laxui001[4])
                shtmpage = shtmpage + 'value="' + sauxival + '"'
                if not laxui001[6]: shtmpage = shtmpage + ' readonly'
                shtmpage = shtmpage + '>'
                shtmpage = shtmpage + '</div></fieldset>'
            elif laxui001[0] in ('select-0', 'select-1'):
                #   0           1           2               3       4             5-0-0  5-0-1   5-1-0   5-1-1     6   7   8
                # ('select-0', 'ssitureg', 'form-control', '16px', 'sobserva', [('A', 'ATIVO'), ('I', 'INATIVO')], 0, 'I', False)
                icontreg = 0
                for lauxi002 in laxui001[5]:
                    if lauxi002[0] != '' and lauxi002[0] != '0' and lauxi002[0] != 0:
                        icontreg += 1
                shtmpage = shtmpage + '<fieldset><div class="' + sdeffogr + '">'
                shtmpage = shtmpage + '<select autocomplete="off" '
                if laxui001[2] != None: shtmpage = shtmpage + 'class="' + laxui001[2] + '" '
                shtmpage = shtmpage + 'id="' + laxui001[1] + '" '
                shtmpage = shtmpage + 'name="' + laxui001[1] + '" '
                shtmpage = shtmpage + 'onKeyUp="AbnfTabEnter(event,getElementById(&#39;' + laxui001[4] + '&#39;));" '
                shtmpage = shtmpage + 'onfocus="this.select()" '
                shtmpage = shtmpage + 'onkeypress="return AbnfScriptKey(event)" '
                if laxui001[0] == 'select-1':   # Obs => No 'select-0 não tem "laxui001[9]"
                    if laxui001[9] != None: shtmpage = shtmpage + 'onchange="AbnfSubmitForm(event,' + "'" + laxui001[9] + "'" + ');" '
                shtmpage = shtmpage + 'spellcheck="true" '
                shtmpage = shtmpage + 'style="text-transform:uppercase; font-family: Courier New; font-size: ' + laxui001[3] + '; font-weight: bold;">'
                for lauxi002 in laxui001[5]:
                    shtmpage = shtmpage + '<option value="' + str(lauxi002[0]) + '"'
                    if   laxui001[7] != None and lauxi002[0] == laxui001[7]:                shtmpage = shtmpage + ' selected'
                    elif laxui001[7] == None and laxui001[8] == True and icontreg == 1:     shtmpage = shtmpage + ' selected'
                    shtmpage = shtmpage + '>' + str(lauxi002[1]) + '</option>'
                shtmpage = shtmpage + '</select>'
                shtmpage = shtmpage + '</div></fieldset>'
                if laxui001[6] == 1: # Filtro para select
                    snumsele = 'ssele' + str(1000 + inumsele)[1:]
                    inumsele += 1
                    shtmpage = shtmpage + '<fieldset><div class="' + sdeffogr + '">'
                    shtmpage = shtmpage + '<input type="text" name="' + snumsele + '" id="' + snumsele + '" '
                    shtmpage = shtmpage + 'maxlength="100" class="form-control" autocomplete="off" onfocus="this.select()" spellcheck="false" '
                    shtmpage = shtmpage + 'style="text-transform:uppercase; font-family: Courier New; font-size: ' + laxui001[3] + '; font-weight: bold; color: brown" '
                    shtmpage = shtmpage + 'onkeypress="return AbnfScriptKey(event)" '
                    shtmpage = shtmpage + 'onKeyUp="'
                    shtmpage = shtmpage + 'AbnfFilterSelect(this, ' + laxui001[1] + ');'
                    shtmpage = shtmpage + 'AbnfTabEnter(event,getElementById(&#39;' + laxui001[1] + '&#39;));'
                    shtmpage = shtmpage + '">'
                    shtmpage = shtmpage + '</div></fieldset>'
            elif laxui001[0] in ['radio-0', 'radio-1', 'checkbox-0']:
                shtmpage = shtmpage + '<fieldset><div class="' + sdeffogr + '">'
                shtmpage = shtmpage + '<font style="font-family: ' + laxui001[4] + '; font-size: ' + laxui001[5] + ';">' + ('<b>' if 'b' in laxui001[6] else '')
                if laxui001[8] != None and laxui001[7] == 'F':  # F = Frontal
                    shtmpage = shtmpage + laxui001[8] + ' '
                shtmpage = shtmpage + '<input class="form-check-input" '
                shtmpage = shtmpage + 'id="' + laxui001[1] + '" '
                shtmpage = shtmpage + 'name="' + laxui001[1] + '" '
                if   laxui001[0] in ['radio-0', 'radio-1']: shtmpage = shtmpage + 'type="radio" '
                elif laxui001[0] == 'checkbox-0':           shtmpage = shtmpage + 'type="checkbox" '
                shtmpage = shtmpage + 'value="' + str(laxui001[2]) + '"'
                if laxui001[0] == 'radio-1':   # Obs => No 'radio-0 não tem "laxui001[9]"
                    if laxui001[9] != None: shtmpage = shtmpage + ' onchange="AbnfSubmitForm(event,' + "'" + laxui001[9] + "'" + ');"'                
                if laxui001[3] != None:
                    if laxui001[3] == laxui001[2]:
                        shtmpage = shtmpage + ' checked'
                shtmpage = shtmpage + '>'
                if laxui001[8] != None and laxui001[7] == 'P':  # P = Posterior
                    shtmpage = shtmpage + ' ' + laxui001[8]
                shtmpage = shtmpage + ('</b>' if 'b' in laxui001[6] else '') + '</font>'
                shtmpage = shtmpage + '</div></fieldset>'
            elif laxui001[0] == 'textarea-0':
                shtmpage = shtmpage + '<fieldset><div class="' + sdeffogr + '">'
                shtmpage = shtmpage + '<textarea autocomplete="off" '
                if laxui001[2] != None: shtmpage = shtmpage + 'class="' + laxui001[2] + '" '
                shtmpage = shtmpage + 'id="' + laxui001[1] + '" '
                shtmpage = shtmpage + 'name="' + laxui001[1] + '" '
                shtmpage = shtmpage + 'minlength="' + str(laxui001[3]) + '" '
                shtmpage = shtmpage + 'maxlength="' + str(laxui001[4]) + '" '
                shtmpage = shtmpage + 'onKeyUp="AbnfTabEnter(event,getElementById(&#39;' + laxui001[7] + '&#39;));" '
                shtmpage = shtmpage + 'onfocus="this.select()" '
                shtmpage = shtmpage + 'onkeypress="return AbnfScriptKey(event)" '
                shtmpage = shtmpage + 'spellcheck="false" '
                shtmpage = shtmpage + 'style="text-transform:uppercase; font-family: Courier New; font-size: ' + laxui001[5] + '; font-weight: bold;">'
                sauxival = '' if laxui001[6] == None else str(laxui001[6])
                shtmpage = shtmpage + sauxival
                shtmpage = shtmpage + '</textarea>'
                shtmpage = shtmpage + '</div></fieldset>'
            elif laxui001[0] == 'button-0':
                shtmpage = shtmpage + '<input type="button" '
                if laxui001[2] != None: shtmpage = shtmpage + 'class="' + laxui001[2] + '" '
                shtmpage = shtmpage + 'id="' + laxui001[1] + '" name="' + laxui001[1] + '" value="' + laxui001[3] + '" '
                shtmpage = shtmpage + 'onclick="AbnfSubmitForm(event);AbnfButtonDisable(this);">'
            elif laxui001[0] == 'button-1':
                # laxui001[1]   => Nome do botão modal
                # laxui001[2]   => Classe do botão modal
                # laxui001[3]   => Mensagem no botão modal
                # laxui001[4]   => Título da janela modal
                # laxui001[5]   => Nome do botão oficial
                # laxui001[6]   => Classe do botão oficial
                # laxui001[7]   => Mensagem no botão oficial
                # laxui001[8]   => Mensagem de confirmação
                # método antigo => snumbutt = 'sbutt' + str(1000 + inumbutt)[1:]
                # método antigo => inumbutt += 1
                ddttmnow = datetime.now()
                sauxi001 = str(100 + ddttmnow.hour) + str(100 + ddttmnow.minute) + str(100 + ddttmnow.second) + str(ddttmnow.microsecond)
                snumbutt = 'sbutt' + sauxi001
                shtmpage = shtmpage + '<input type="button" class="' + laxui001[2] + '" id="' + laxui001[1] + '" name="' + laxui001[1] + '" value="' + laxui001[3] + '" data-bs-toggle="modal" data-bs-target="#' + snumbutt + '" href="#">'
                shtmpage = shtmpage + '<div class="modal fade" id="' + snumbutt + '" tabindex="-1" aria-labelledby="' + snumbutt + '-label" aria-hidden="true">'
                shtmpage = shtmpage +     '<div class="modal-dialog">'
                shtmpage = shtmpage +         '<div class="modal-content">'
                shtmpage = shtmpage +             '<div class="modal-header">'
                shtmpage = shtmpage +                 '<h1 class="modal-title fs-5" id="' + snumbutt + '-label">' + laxui001[4] + '</h1>'
                shtmpage = shtmpage +             '</div>'
                shtmpage = shtmpage +             '<div class="modal-body">' + laxui001[8] + '</div>'
                shtmpage = shtmpage +             '<div class="modal-footer">'
                shtmpage = shtmpage +                 '<input type="button" class="btn btn-secondary mt-2" data-bs-dismiss="modal" value="Cancelar">'
                shtmpage = shtmpage +                 '<input type="button" class="' + laxui001[6] + '" data-bs-dismiss="modal" '
                shtmpage = shtmpage +                 'id="' + laxui001[5] + '" name="' + laxui001[5] + '" value="' + laxui001[7] + '" '
                shtmpage = shtmpage +                 '" onclick="AbnfSubmitForm(event);AbnfTimeButtonDisable(this,3);">'
                shtmpage = shtmpage +             '</div>'
                shtmpage = shtmpage +         '</div>'
                shtmpage = shtmpage +     '</div>'
                shtmpage = shtmpage + '</div>'
                # btn btn-primary   => azul
                # btn btn-secondary => cinza
                # btn btn-success   => verde
                # btn btn-danger    => vermelho
                # btn btn-warning   => amarelo
                # btn btn-info      => ciano
                # btn btn-light     => branco
                # btn btn-dark      => preto
                # btn btn-link      => hiperlink
            elif laxui001[0] == 'button-2':     # Botão para div retrátil
                shtmpage = shtmpage + '<button type="button" '
                shtmpage = shtmpage + 'class="' + laxui001[2] + '" '
                shtmpage = shtmpage + 'data-bs-toggle="collapse" '
                shtmpage = shtmpage + 'data-bs-target="#' + laxui001[1] + '">' + laxui001[3]
                shtmpage = shtmpage + '</button>'
            elif laxui001[0] == 'button-3':     # Botão para marcar/desmarcar vários checkbox juntos
                shtmpage = shtmpage + '<input type="button" '
                if laxui001[2] != None: shtmpage = shtmpage + 'class="' + laxui001[2] + '" '
                shtmpage = shtmpage + 'id="' + laxui001[1] + '" name="' + laxui001[1] + '" value="' + laxui001[3] + '" '
                if laxui001[5] == True: shtmpage = shtmpage + 'onclick="AbnfCheckboxCheckAll(['
                else:                   shtmpage = shtmpage + 'onclick="AbnfCheckboxUncheckAll(['
                sauxi001 = ''
                for lauxi002 in laxui001[4]:
                    if sauxi001 != '': sauxi001 = sauxi001 + ','
                    sauxi001 = sauxi001 + "'" + lauxi002 + "'"
                shtmpage = shtmpage + sauxi001 + '])">'
            elif laxui001[0] == 'button-4':
                shtmpage = shtmpage + '<input type="button" '
                if laxui001[2] != None: shtmpage = shtmpage + 'class="' + laxui001[2] + '" '
                shtmpage = shtmpage + 'id="' + laxui001[1] + '" name="' + laxui001[1] + '" value="' + laxui001[3] + '" '
                shtmpage = shtmpage + 'onclick="AbnfSubmitForm(event);AbnfAutomaticPressButtonInterval(this, ' + str(laxui001[4]) + ');">'
            elif laxui001[0] == 'table-0':
                shtmpage = shtmpage + '<table'
                if laxui001[1] != None: shtmpage = shtmpage + ' class="' + laxui001[1] + '"'
                shtmpage = shtmpage + '>'
            elif laxui001[0] == 'table-1':  # Table exclusivo para radiobutton => ao clicar na linha, o radiobutton da linha é selecionado e o bgcolor da linha é pintado pela cor definida.
                shtmpage = shtmpage + '<table'
                if laxui001[1] != None: shtmpage = shtmpage + ' class="' + laxui001[1] + '"'
                shtmpage = shtmpage + ' id="' + laxui001[2] + '" '
                shtmpage = shtmpage + ' onclick="AbnfRadioBgColor(' + "'" + laxui001[2] + "','" + laxui001[3] + "'" + ')">'
            elif laxui001[0] == 'table-2':  # Table com scroll e redimensionamento de tela.
                # Obs: essa função abre uma div no meio do processo, então tem que fechar com um "table-9" seguido de um "div-9".
                # Nota: 30/08/2025 - O parâmetro "laxui001[2]" era usado para ".abnf_table_scroll" onde eu tinha que determinar um número para cada "table-2".
                # Para evitar ter quer ficar inserindo esse valor individual para cada "table-2" eu substitui o "laxui001[2]" por "laxui001[5]".
                # Com isso resolver o problema de esquecer essa parametrização, mas deixo aqui registrado que laxui001[2] esta livre para futuramente ser utilizado para outra finalidade.
                shtmpage = shtmpage + '<style>'
                shtmpage = shtmpage + '    .abnf_table_scroll' + str(laxui001[5]) + ' {'
                shtmpage = shtmpage + '    width: ' + str(laxui001[3]) + 'px;'
                shtmpage = shtmpage + '    height: ' + str(laxui001[4]) + 'px;'
                shtmpage = shtmpage + '    overflow: auto;'
                shtmpage = shtmpage + '    resize: both;'
                shtmpage = shtmpage + '    border: 1px solid #ccc;'
                shtmpage = shtmpage + '    }'
                shtmpage = shtmpage + '    .abnf_table_scroll' + str(laxui001[5]) + ' table {'
                shtmpage = shtmpage + '    border-collapse: collapse;'
                shtmpage = shtmpage + '    width: 100%;'
                shtmpage = shtmpage + '    }'
                # ==> shtmpage = shtmpage + '    .abnf_table_scroll' + str(laxui001[5]) + ' th,'
                # ==> shtmpage = shtmpage + '    .abnf_table_scroll' + str(laxui001[5]) + ' td {'
                # ==> shtmpage = shtmpage + '    border: 1px solid black;'
                # ==> shtmpage = shtmpage + '    padding: 8px;'
                # ==> shtmpage = shtmpage + '    text-align: left;'
                # ==> shtmpage = shtmpage + '    }'
                shtmpage = shtmpage + '</style>'
                shtmpage = shtmpage + '<div class="abnf_table_scroll' + str(laxui001[5]) + '">'
                shtmpage = shtmpage + '    <table'
                if laxui001[1] != None: shtmpage = shtmpage + ' class="' + laxui001[1] + '"'
                if laxui001[5] != None and laxui001[6] != None: # Uso de radiobutton na table
                    shtmpage = shtmpage + ' id="' + laxui001[5] + '" '
                    shtmpage = shtmpage + ' onclick="AbnfRadioBgColor(' + "'" + laxui001[5] + "','" + laxui001[6] + "'" + ')"'
                shtmpage = shtmpage + '>'
            elif laxui001[0] == 'table-3':
                shtmpage = shtmpage + '<table border="' + str(laxui001[1]) + '">'
            elif laxui001[0] == 'table-9':
                shtmpage = shtmpage + '</table>'
            elif laxui001[0] == 'tr-0':
                if laxui001[2] == True:
                    shtmpage = shtmpage + '<style type="text/css">'
                    shtmpage = shtmpage +   '.abnf-check-clicked {'
                    shtmpage = shtmpage +       'background-color: lightgreen;'
                    shtmpage = shtmpage +   '}'
                    shtmpage = shtmpage + '</style>'
                shtmpage = shtmpage + '<tr'
                if laxui001[1] != None: shtmpage = shtmpage + ' class="' + laxui001[1] + '"'
                if laxui001[2] == True: shtmpage = shtmpage + ' onclick="AbnfCheckboxBgColor(this);"'
                shtmpage = shtmpage + '>'
            elif laxui001[0] == 'tr-9':
                shtmpage = shtmpage + '</tr>'
            elif laxui001[0] in ('td-0','td-1'):
                shtmpage = shtmpage + '<td scope="row"'
                if laxui001[1] != None: shtmpage = shtmpage + ' class="'   + laxui001[1] + '"'
                if laxui001[2] != None: shtmpage = shtmpage + ' colspan="' + str(laxui001[2]) + '"'
                if laxui001[3] != None: shtmpage = shtmpage + ' rowspan="' + str(laxui001[3]) + '"'
                if laxui001[4] != None: shtmpage = shtmpage + ' align="'   + dhalignx[laxui001[4]] + '"'
                if laxui001[5] != None: shtmpage = shtmpage + ' valign="'  + dvalignx[laxui001[5]] + '"'
                if laxui001[6] != None: shtmpage = shtmpage + ' bgcolor="' + laxui001[6] + '"'
                if laxui001[0] == 'td-1':
                    if laxui001[7] != None: shtmpage = shtmpage + ' style="width: ' + str(laxui001[7]) + 'px;"'
                    # <td style="width: 150px;">Conteúdo da Coluna 1</td>
                    # <td style="width: 200px;">Conteúdo da Coluna 2</td>
                shtmpage = shtmpage + '>'
            elif laxui001[0] == 'td-9':
                shtmpage = shtmpage + '</td>'
            elif laxui001[0] == 'hx-0':
                shtmpage = shtmpage + '<h' + str(laxui001[1]) + ' class="' + laxui001[2] + '">'
                shtmpage = shtmpage + '<font style="text-transform:uppercase; font-family: Courier New; font-size: ' + laxui001[3] + '; font-weight: bold; color: ' + laxui001[4] + '"><b>'
                shtmpage = shtmpage + str(laxui001[5]) + '</b></font>'
                shtmpage = shtmpage + '</h' + str(laxui001[1]) + '>'
            elif laxui001[0] == 'file-0':
                if laxui001[5]: shtmpage = shtmpage + '<fieldset><div class="' + sdeffogr + '">'
                shtmpage = shtmpage + '<input type="file" class="' + laxui001[2] + '" id="' + laxui001[1] + '" name="' + laxui001[1] + '" accept="' + laxui001[3] + '"'
                shtmpage = shtmpage + (' multiple' if laxui001[4] else '') + '>'
                if laxui001[5]: shtmpage = shtmpage + '</div></fieldset>'
            elif laxui001[0] == 'alt255-0':
                for icontd01 in range(laxui001[1]):
                    shtmpage = shtmpage + '&nbsp;'
            elif laxui001[0] == 'html-0':   # O parâmetro é o código html inteiro que deseja que seja acrescido
                shtmpage = shtmpage + laxui001[1]
            shtmpage = shtmpage + sremospa
    shtmpage = shtmpage.strip()
    return shtmpage
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_check_structure_fields ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que analisa os campos digitados/selecionados/flagados pelo usuário na pagina HTML/CSS/JS.                                                    // #
# // Esta função lê o dicionário dabnfopg e a lista lmfields, verifica as integridades conforme as regras, e mostra os erros ao usuário caso existam.    // #
# // Também abastece 'lmfields' com o conteúdos das variáveis que estão definidas no dicionários 'dabnfopg'.                                             // #
# // Por fim devolve 'lmfields' preenchido com as informações inseridas pelo usuário.                                                                    // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Nota: 18/07/2024                                                                                                                                    // #
# // No esse dia ocorreu o seguinte erro ao passar por essa função: 'TypeError: string indices must be integers'.                                        // #
# // Esse ja tinha ocorrido outras vezes e não é muito sugestivo do problema que realmente está ocorrendo.                                               // #
# // Depois de muito quebrar a cabeça, descobri que este problema ocorre quando falta vírgula (",") entre elementos de uma "lista dentro de lista".      // #
# // Exemplo:                                                                                                                                            // #
# // Lista correta ...............: ['stipogru', 'select', 'F', 'tipo de grupo', ['Notnull', 'D' ], None],                                               // #                                                                                                                                                // #
# // Lista com o erro mencionado .: ['stipogru', 'select', 'F', 'tipo de grupo'  ['Notnull', 'D' ], None],                                               // #
# // Razão do problema ...........: faltou vírgula entre: (...) 'tipo de grupo'  ['Notnull', 'D' ] (...)                                                 // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_check_structure_fields(dabnfopg, lmfields, btenable):
    bvalidad = True
    for lauxi001 in lmfields:
        # print('[A]', lauxi001)
        icontreg = 0
        for lauxi002 in dabnfopg:
            # print('[B]', lauxi002, ' - ', dabnfopg[lauxi002])
            if lauxi001[0] == lauxi002:
                icontreg += 1
                stypefil = lauxi001[1]
                sgenerof = lauxi001[2]
                snomecam = lauxi001[3]
                lregrcam = lauxi001[4]
                sconteud = dabnfopg[lauxi002][2].upper()
                sconteud = abnf_converte_string(sconteud)
                # print('[C]', sgenerof, ' - ', snomecam, ' - ', lregrcam, ' - ', sconteud)
                if (stypefil == 'input' or stypefil == 'textarea') and not abnf_valida_string(sconteud):
                    if   sgenerof == 'M': smenserr = 'Caracteres inválidos no ' + snomecam + '!'
                    elif sgenerof == 'F': smenserr = 'Caracteres inválidos na ' + snomecam + '!'
                    abnf_alert(smenserr, 5)
                    bvalidad = False
                    abnf_socket_004([5, btenable])
                    break
                elif stypefil == 'number' and not abnf_valida_integer(sconteud):
                    if   sgenerof == 'M': smenserr = 'Somente devem conter números no ' + snomecam + '!'
                    elif sgenerof == 'F': smenserr = 'Somente devem conter números na ' + snomecam + '!'
                    abnf_alert(smenserr, 5)
                    bvalidad = False
                    abnf_socket_004([5, btenable])
                    break
                elif (stypefil == 'thscom' or stypefil == 'thscd2') and not abnf_verifica_numero_milhares_decimais(sconteud):    
                    if   sgenerof == 'M': smenserr = 'O ' + snomecam + ' está inválido!'
                    elif sgenerof == 'F': smenserr = 'A ' + snomecam + ' está inválida!'
                    abnf_alert(smenserr, 5)
                    bvalidad = False
                    abnf_socket_004([5, btenable])
                    break
                elif stypefil == 'date' and not abnf_valida_data(sconteud):
                    if   sgenerof == 'M': smenserr = 'O ' + snomecam + ' está inválido!'
                    elif sgenerof == 'F': smenserr = 'A ' + snomecam + ' está inválida!'
                    abnf_alert(smenserr, 5)
                    bvalidad = False
                    abnf_socket_004([5, btenable])
                    break
                elif (stypefil == 'time-0' and sconteud != '' and not abnf_valida_hora(sconteud, 1)) or (stypefil == 'time-1' and sconteud != '' and not abnf_valida_hora(sconteud, 2)):
                    if   sgenerof == 'M': smenserr = 'O ' + snomecam + ' está inválido!'
                    elif sgenerof == 'F': smenserr = 'A ' + snomecam + ' está inválida!'
                    abnf_alert(smenserr, 5)
                    bvalidad = False
                    abnf_socket_004([5, btenable])
                    break
                # ///////////////////////////////////////////////////////////////////////////////////////////////////////
                # Não aceita vazio e nem texto númerico que seu conteúdo indique vazio como por ex: '0', '00', '000', etc
                # ///////////////////////////////////////////////////////////////////////////////////////////////////////
                elif 'Notnull' in lregrcam and (sconteud == '' or sconteud in '0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'):
                    if   'P' in lregrcam: sauxi001 = 'preenchid'
                    elif 'D' in lregrcam: sauxi001 = 'definid'
                    if   sgenerof == 'M': smenserr = 'O ' + snomecam + ' tem que ser ' + sauxi001 + 'o!'
                    elif sgenerof == 'F': smenserr = 'A ' + snomecam + ' tem que ser ' + sauxi001 + 'a!'
                    abnf_alert(smenserr, 5)
                    bvalidad = False
                    abnf_socket_004([5, btenable])
                    break
                # ////////////////////////////////////////////////////////////////////
                # Não aceita vazio mas aceita qualquer texto sem analisar seu conteúdo
                # ////////////////////////////////////////////////////////////////////
                elif 'Notempty' in lregrcam and sconteud == '':
                    if   'P' in lregrcam: sauxi001 = 'preenchid'
                    elif 'D' in lregrcam: sauxi001 = 'definid'
                    if   sgenerof == 'M': smenserr = 'O ' + snomecam + ' tem que ser ' + sauxi001 + 'o!'
                    elif sgenerof == 'F': smenserr = 'A ' + snomecam + ' tem que ser ' + sauxi001 + 'a!'
                    abnf_alert(smenserr, 5)
                    bvalidad = False
                    abnf_socket_004([5, btenable])
                    break
                # ///////////////////////////
                # Não aceita valor int zerado
                # ///////////////////////////
                elif 'Notzero' in lregrcam and int(sconteud) == 0:
                    if   sgenerof == 'M': smenserr = 'O ' + snomecam + ' não pode ser zero!'
                    elif sgenerof == 'F': smenserr = 'A ' + snomecam + ' não pode ser zero!'
                    abnf_alert(smenserr, 5)
                    bvalidad = False
                    abnf_socket_004([5, btenable])
                    break
                elif 'CPF' in lregrcam and sconteud != '' and not abnf_valida_cpf(sconteud):
                    if   sgenerof == 'M': smenserr = 'O ' + snomecam + ' está inválido!'
                    elif sgenerof == 'F': smenserr = 'A ' + snomecam + ' está inválida!'
                    abnf_alert(smenserr, 5)
                    bvalidad = False
                    abnf_socket_004([5, btenable])
                    break
                elif 'CNPJ' in lregrcam and sconteud != '' and not abnf_valida_cnpj(sconteud):
                    if   sgenerof == 'M': smenserr = 'O ' + snomecam + ' está inválido!'
                    elif sgenerof == 'F': smenserr = 'A ' + snomecam + ' está inválida!'
                    abnf_alert(smenserr, 5)
                    bvalidad = False
                    abnf_socket_004([5, btenable])
                    break
                elif 'e-mail' in lregrcam and not abnf_valida_email(sconteud):
                    if   sgenerof == 'M': smenserr = 'O ' + snomecam + ' está inválido!'
                    elif sgenerof == 'F': smenserr = 'A ' + snomecam + ' está inválida!'
                    abnf_alert(smenserr, 5)
                    bvalidad = False
                    abnf_socket_004([5, btenable])
                    break
                else:
                    if stypefil == 'thscom' or 'thscd' in stypefil:
                        if   stypefil == 'thscom': nconteud = abnf_converte_string_value_to_float(sconteud)
                        elif 'thscd' in stypefil:  nconteud = abnf_converte_string_value_to_decimal(sconteud, int(stypefil[-1:]))
                        smesserr = ''
                        if   '>0'  in lregrcam and nconteud <= 0: smesserr = ' tem que ser maior que zero!'
                        elif '>=0' in lregrcam and nconteud  < 0: smesserr = ' não pode ser negativo!'
                        elif '<>0' in lregrcam and nconteud == 0: smesserr = ' não pode ser zero!'
                        if smesserr != '':
                            if   sgenerof == 'M': smenserr = 'O ' + snomecam + smesserr
                            elif sgenerof == 'F': smenserr = 'A ' + snomecam + smesserr
                            abnf_alert(smenserr, 5)
                            bvalidad = False
                            abnf_socket_004([5, btenable])
                        else:
                            lauxi001[5] = nconteud
                    elif 'Empty_to_zero' in lregrcam and sconteud == '':
                        lauxi001[5] = 0
                    elif 'Empty_to_string' in lregrcam and sconteud == '':
                        lauxi001[5] = ''
                    elif 'Empty_to_null' in lregrcam and sconteud == '':
                        lauxi001[5] = None
                    elif stypefil == 'number':
                        if sconteud == '':
                            if   sgenerof == 'M': smenserr = 'Não foi possível ler os números do ' + snomecam + '!'
                            elif sgenerof == 'F': smenserr = 'Não foi possível ler os números da ' + snomecam + '!'
                            abnf_alert(smenserr, 5)
                            bvalidad = False
                            abnf_socket_004([5, btenable])
                            break
                        else:
                            # print('==============>>>> ', str(sconteud), ' === ', type(sconteud) )
                            lauxi001[5] = int(sconteud)
                    elif 'Return_date' in lregrcam:
                        if sconteud != None and sconteud != '':
                            try:
                                ddataret = datetime.strptime(sconteud, "%Y-%m-%d").date()   # Converte o conteúdo em data para poder fazer a comparação
                            except Exception as objerror:
                                # abnf_alert(str(objerror), 5)
                                abnf_alert('A ' +  snomecam + ' esta inválida!', 5)
                                abnf_socket_004([5, btenable])
                                bvalidad = False
                                break
                            ddatahoj = date.today()                                         # Guarda a data de hoje
                            if '<today' in lregrcam and ddataret >= ddatahoj:
                                smenserr = 'A ' +  snomecam + ' tem que ser menor que a data de hoje!'
                                bvalidad = False
                            elif '>today' in lregrcam and ddataret <= ddatahoj:
                                smenserr = 'A ' +  snomecam + ' tem que ser maior que a data de hoje!'
                                bvalidad = False
                            elif '<=today' in lregrcam and ddataret > ddatahoj:
                                smenserr = 'A ' +  snomecam + ' tem que ser menor ou igual a data de hoje!'
                                bvalidad = False
                            elif '>=today' in lregrcam and ddataret < ddatahoj:
                                smenserr = 'A ' +  snomecam + ' tem que ser maior ou igual a data de hoje!'
                                bvalidad = False
                            if not bvalidad:
                                abnf_alert(smenserr, 5)
                                abnf_socket_004([5, btenable])
                                break
                            else:
                                lauxi001[5] = ddataret
                    elif 'Return_time' in lregrcam:
                        if sconteud != None and sconteud != '':
                            try:
                                hhoraret = datetime.strptime(sconteud, "%H:%M").time()  #   # Converte o conteúdo em data para poder fazer a comparação
                            except Exception as objerror:
                                # abnf_alert(str(objerror), 5)
                                abnf_alert('A ' +  snomecam + ' esta inválida!', 5)
                                abnf_socket_004([5, btenable])
                                bvalidad = False
                                break
                            else:
                                lauxi001[5] = hhoraret
                    elif 'Return_integer' in lregrcam:
                        lauxi001[5] = int(sconteud)
                    elif 'Return_eval' in lregrcam:
                        lauxi001[5] = eval(sconteud)
                    elif stypefil == 'checkbox':
                        # abnf_show('08', lauxi002, 0)                      # <== Usar para visualizar eventos de checkbox e radio - Obs: radio não foi tratado ainda
                        # abnf_show('09', lauxi001, 1)                      # <== Usar para visualizar eventos de checkbox e radio - Obs: radio não foi tratado ainda
                        # abnf_show('10', dabnfopg[lauxi002], 1)            # <== Usar para visualizar eventos de checkbox e radio - Obs: radio não foi tratado ainda
                        # abnf_show('10', dabnfopg[lauxi002][3], 0)         # <== Usar para visualizar eventos de checkbox e radio - Obs: radio não foi tratado ainda
                        lauxi001[5] = dabnfopg[lauxi002][3]
                    else:
                        lauxi001[5] = sconteud
        if icontreg != 1:
            abnf_alert('Erro estrutural! Entre em contato com o departamento de sistemas!', 4)
            # abnf_show('09', lmfields, 1)
            # abnf_show('10', dabnfopg, 2)
            bvalidad = False
        if not bvalidad:
            break
    return bvalidad, lmfields
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_find_checkbox_radio ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função para buscar 'checkbox' e 'radio' dentro do form.                                                                                             // #
# // Esta função busca dentro de do dicionário dabnfopg.                                                                                                 // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #   
    
def abnf_find_checkbox_radio(dabnfopg, lmfields, btenable):
    bvalidad = True
    for lauxi001 in lmfields:
        snamefil = lauxi001[0]
        stypefil = lauxi001[1]
        smenserr = lauxi001[2]
        lregrcam = lauxi001[3]
        # Busca o nome do campo dentro da chave de 'dabnfopg'
        # Se encontra, atualiza na lista.
        for lauxi002 in dabnfopg:
            if snamefil in lauxi002:
                if 'Return_integer' in lregrcam:
                    if   stypefil == 'checkbox' and dabnfopg[lauxi002][3] == True:      lauxi001[4].append(int(dabnfopg[lauxi002][2]))
                    elif stypefil == 'radio':                                           lauxi001[4] = int(dabnfopg[lauxi002][2])
                else:
                    if   stypefil == 'checkbox' and dabnfopg[lauxi002][3] == True:      lauxi001[4].append(dabnfopg[lauxi002][2])
                    elif stypefil == 'radio':                                           lauxi001[4] = dabnfopg[lauxi002][2]
        # Analisando as regras:
        if 'Notnull' in lregrcam and lauxi001[4] in (None, []):
            abnf_alert(smenserr + '!', 5)
            bvalidad = False
            abnf_socket_004([5, btenable])
    # Debug: (inicio)
    # abnf_show('09', lmfields, 1)
    # abnf_show('10', dabnfopg, 2)
    # Debug: (fim)
    abnf_socket_004([5, btenable])
    return bvalidad, lmfields
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_create_spinner ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função para criar spinners de página para com avisos personalizados.                                                                                // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #      
    
def abnf_create_spinner(icodspin, iparamew):
    sspipage = ''
    sspinner = ''
    if icodspin == 1:
        sspinner = sspinner + '<table class="table table-sm table-bordered table-responsive">'
        sspinner = sspinner + '<tr class="table-active">'
        sspinner = sspinner + '<td align="center"><font style="font-family: Courier New; font-size: 32px; font-weight: bold; color: black"><b>Por favor aguarde...</b></font></td>'
        sspinner = sspinner + '<td align="center">'
        sspinner = sspinner + '<div class="spinner-border" style="width: 3rem; height: 3rem;" role="status">'
        sspinner = sspinner + '<span class="sr-only"></span>'
        sspinner = sspinner + '</div><div class="spinner-grow" style="width: 3rem; height: 3rem;" role="status">'
        sspinner = sspinner + '<span class="sr-only"></span>'
        sspinner = sspinner + '</div>'
        sspinner = sspinner + '</td>'
        sspinner = sspinner + '</table>'
        lnewpage = [                                                                         
            ('div-0', 'container', None, None),
            ('hr-0', None),
            ('div-0', 'row', None, None),
            ('div-0', 'col d-flex justify-content-center', None, None),
            ('div-0', 'w-' + str(iparamew) + ' p-3', 'background-color: #eee;', None),
            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
            ('hr-0', None),
            ('legend-0', sspinner),
            ('hr-0', None),
            ('form-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
        ]
        sspipage = abnf_create_page(lnewpage)   
    return sspipage
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_converte_string ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que converte uma string para ser gravado nas tabelas do banco de dados.                                                                      // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_converte_string(stextchk):
    # /// #
    # stextchk = ' '.join(stextchk.split())                       # Remoção os espaços em branco duplicados
    # stextchk = stextchk.strip()                                 # Remoção dos espaços em branco no início e no fim
    # /// #
    stextchk = stextchk.upper()                                 # converter todos os caracteres da sring em maiúsculo
    # /// #
    stextchk = stextchk.strip()                                 # Remove os espaços em branco no início e no final de uma string,
    # /// #
    bvalidad = False                                            # Remoção os espaços em branco duplicados
    while bvalidad != True:                                     # Remoção os espaços em branco duplicados
        if stextchk.count('  ') > 0:                            # Remoção os espaços em branco duplicados
            stextchk = stextchk.replace('  ',' ')               # Remoção os espaços em branco duplicados
        else:                                                   # Remoção os espaços em branco duplicados
            bvalidad = True                                     # Remoção os espaços em branco duplicados
    # /// #
    stextchk = stextchk.replace('( ','(')                       # Remoção de parêntesis com espaços
    stextchk = stextchk.replace(' )',')')                       # Remoção de parêntesis com espaços
    # /// #
    stextchk = stextchk.replace('Á', 'A')                       # Substituição de caracteres em vogal
    stextchk = stextchk.replace('À', 'A')                       # Substituição de caracteres em vogal
    stextchk = stextchk.replace('Ã', 'A')                       # Substituição de caracteres em vogal
    stextchk = stextchk.replace('Ä', 'A')                       # Substituição de caracteres em vogal
    stextchk = stextchk.replace('Â', 'A')                       # Substituição de caracteres em vogal
    # /// #                                     
    stextchk = stextchk.replace('É', 'E')                       # Substituição de caracteres em vogal
    stextchk = stextchk.replace('È', 'E')                       # Substituição de caracteres em vogal
    stextchk = stextchk.replace('Ë', 'E')                       # Substituição de caracteres em vogal
    stextchk = stextchk.replace('Ê', 'E')                       # Substituição de caracteres em vogal
    # /// #                                     
    stextchk = stextchk.replace('Í', 'I')                       # Substituição de caracteres em vogal
    stextchk = stextchk.replace('Ì', 'I')                       # Substituição de caracteres em vogal
    stextchk = stextchk.replace('Ï', 'I')                       # Substituição de caracteres em vogal
    stextchk = stextchk.replace('Î', 'I')                       # Substituição de caracteres em vogal
    # /// #                                     
    stextchk = stextchk.replace('Ó', 'O')                       # Substituição de caracteres em vogal
    stextchk = stextchk.replace('Ò', 'O')                       # Substituição de caracteres em vogal
    stextchk = stextchk.replace('Õ', 'O')                       # Substituição de caracteres em vogal
    stextchk = stextchk.replace('Ö', 'O')                       # Substituição de caracteres em vogal
    stextchk = stextchk.replace('Ô', 'O')                       # Substituição de caracteres em vogal
    # /// #                                     
    stextchk = stextchk.replace('Ú', 'U')                       # Substituição de caracteres em vogal
    stextchk = stextchk.replace('Ù', 'U')                       # Substituição de caracteres em vogal
    stextchk = stextchk.replace('Ü', 'U')                       # Substituição de caracteres em vogal
    stextchk = stextchk.replace('Û', 'U')                       # Substituição de caracteres em vogal
    # /// #                                     
    stextchk = stextchk.replace('Ç', 'C')                       # Substituição de caracteres em consoantes
    stextchk = stextchk.replace('Ñ', 'N')                       # Substituição de caracteres em consoantes
    # /// #
    stextchk = stextchk.replace('Ñ', 'N')                       # Substituição de caracteres em consoantes
    # /// #
    stextchk = stextchk.replace('ª', '.')                       # Substituição de caracteres especiais
    stextchk = stextchk.replace('º', '.')                       # Substituição de caracteres especiais
    # /// #
    stextchk = stextchk.replace(';', ',')                       # Substituição de caracteres que são usado para transferência de dados
    # /// #
    return stextchk
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_converte_espaco ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que substitui espaços por caracter especial invisível html.                                                                                  // #
# // O intúito dessa função é evitar que ocorra no texto uma quebra de linha na formação de tela ou na impressão.                                        // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #   

def abnf_converte_espaco(stextchk):
    stextchk = stextchk.replace(' ', '&nbsp;')                  # Substituição de espaço por caracter especial invisível html
    return stextchk   
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_converte_string_value_to_float ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que converte uma string com separador de milhar e decimal para uma variável float.                                                           // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_converte_string_value_to_float(stextchk):
    sconteud = stextchk
    sconteud = sconteud.replace('.','')
    sconteud = sconteud.replace(',','.')
    nconteud = float(sconteud)
    if nconteud == None:
        nconteud = 0.0
    return nconteud

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_converte_string_value_to_decimal ] //////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que converte uma string com separador de milhar e decimal para uma variável decimal com o número de casas decimais definida em "iqtddeci".   // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_converte_string_value_to_decimal(stextchk, iqtddeci):
    sconteud = stextchk
    sconteud = sconteud.replace('.','')
    sconteud = sconteud.replace(',','.')
    nconteud = decimal.Decimal(sconteud)
    if nconteud == None:
        nconteud = 0.0
    # Define o formato da variavel auxiliar para arredondamento de casas
    if   iqtddeci == 1: nauxidec = decimal.Decimal('0.1')
    elif iqtddeci == 2: nauxidec = decimal.Decimal('0.01')
    elif iqtddeci == 3: nauxidec = decimal.Decimal('0.001')
    elif iqtddeci == 4: nauxidec = decimal.Decimal('0.0001')
    elif iqtddeci == 5: nauxidec = decimal.Decimal('0.00001')
    elif iqtddeci == 6: nauxidec = decimal.Decimal('0.000001')
    # Arredonda o número de casas decimais conforme a variavel auxiliar
    nconteud = nconteud.quantize(nauxidec, rounding=decimal.ROUND_HALF_UP)
    return nconteud

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_insere_alt255 ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que insere codificação de caractere invisível html para auxiliar na montagem de telas em html.                                               // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_insere_alt255(iqtda255, binsevaz):
    shtmpage = ''
    if binsevaz:
        shtmpage = shtmpage + ' '
    for icontd01 in range(iqtda255):
        shtmpage = shtmpage + '&nbsp;'
    return shtmpage
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_retorna_decimal ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que retorna em inteiro o valor decimal de um número.                                                                                         // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    
def abnf_retorna_decimal(nconteud):
    n = 3.14
    sconteud = str(nconteud)
    ipontdec = sconteud.find('.')
    svaldeci = sconteud[ipontdec+1:]
    nvaldeci = int(svaldeci)  # Convertendo para inteiro
    return nvaldeci

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_valida_string ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que valida os caracteres digitados em um campo string.                                                                                       // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_valida_string(stextchk):
    if not stextchk: return True
    stxtlist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*()_-+=:<>,.?/~^|ªº '
    ilentext = len(stextchk)
    btexterr = True
    for iauxi001 in range(ilentext):
        iauxi002 = stxtlist.find(stextchk[iauxi001])
        # print(str(iauxi001)+' - '+stextchk[iauxi001]+' - '+str(iauxi002))
        if iauxi002 < 0: btexterr = False
    # print(btexterr)
    return btexterr
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_valida_integer ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que valida os caracteres digitados em um campo integer.                                                                                      // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_valida_integer(stextchk):
    # abnf_show('10', stextchk, 0)
    if not stextchk: return True
    stxtlist = '0123456789'
    ilentext = len(stextchk)
    btexterr = True
    for iauxi001 in range(ilentext):
        iauxi002 = stxtlist.find(stextchk[iauxi001])
        #print(str(iauxi001)+' - '+stextchk[iauxi001]+' - '+str(iauxi002))
        if iauxi002 < 0: btexterr = False
    #print(btexterr)
    return btexterr    
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_valida_data ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que valida uma data.                                                                                                                         // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_valida_data(stextchk):
    # abnf_show('07', stextchk, 0)
    # Nota: 24/07/2024
    # Por enquanto não está sendo necessário criar uma rotina para validar um campo data.
    # Isso porque o proprio html já deixa como nula (ou vazia) o valor de qualquer data digitada de forma incompleta.
    # Ele também não permite que data inexistentes sejam digitadas.
    # Mas vamos deixar essa função em aberto apenas retornando True.
    # No futuro, se por algum motivo houver uma necessidade, tratamos aqui as datas digitadas.
    return True
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_valida_hora ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que valida uma hora.                                                                                                                         // #
# // Essa função será utilizado pelos campos "time-1" que não são campos time mas sim campos personalizados com JS para digitar horas acima de 23:59.    // #
# // Os campos time do html ja tem o padrão de corrigirem horas digitas incorretamente.                                                                  // #
# // Se iparamet = 1 => Permite hora até 23                                                                                                              // #
# // Se iparamet = 2 => Permite hora até 29                                                                                                              // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_valida_hora(stextchk, iparamet):
    bvalidad = True
    if len(stextchk) != 5:                                                  bvalidad = False    # Tamanho menor que 5
    elif stextchk[2] != ':':                                                bvalidad = False    # Não tiver ":" na posição correta
    elif not stextchk[0] in '012':                                          bvalidad = False    # Primeiro dígito da hora
    elif not stextchk[1] in '0123456789':                                   bvalidad = False    # Segundo dígito da hora
    elif not stextchk[3] in '012345':                                       bvalidad = False    # Primeiro dígito do minuto
    elif not stextchk[4] in '0123456789':                                   bvalidad = False    # Segundo dígito do minuto
    elif iparamet == 1 and int(stextchk[:2]) > 23:                          bvalidad = False    # Segundo dígito da hora (hora até 23)
    elif iparamet == 2 and int(stextchk[:2]) > 29:                          bvalidad = False    # Segundo dígito da hora (hora até 29)
    return bvalidad
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_valida_email ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que valida o formato do email.                                                                                                               // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_valida_email(stextchk):
    icontarr = 0
    icontpon = 0
    bcontpon = False
    bvalidad = True
    stextchk = stextchk.upper()
    if stextchk != '':
        if ('@@' in stextchk or
            '..' in stextchk or
            '@.' in stextchk or
            '.@' in stextchk or
            stextchk[0]  in '@.' or
            stextchk[-1] in '@.'):
            bvalidad = False
        else:
            for sauxi001 in stextchk:
                if sauxi001 == '@':
                    icontarr += 1
                    bcontpon = True
                else:
                    if not sauxi001 in '.0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_-':
                        bvalidad = False
                    else:
                        if bcontpon and sauxi001 == '.':
                            icontpon += 1
            if icontarr != 1 or icontpon == 0:
                bvalidad = False
            else:
                for sauxi001 in stextchk[::-1]: # Varre a string de tráz para frente
                    if sauxi001 == '.':
                        break
                    else:
                        if not sauxi001 in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                            bvalidad = False
    return bvalidad
    # == Não usar mais esse método! Ele trava todo o sistema quando e-mail é grande: ==> if not stextchk: return True
    # == Não usar mais esse método! Ele trava todo o sistema quando e-mail é grande: ==> xvalem01 = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    # == Não usar mais esse método! Ele trava todo o sistema quando e-mail é grande: ==> # xvalem01 = re.compile(r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')
    # == Não usar mais esse método! Ele trava todo o sistema quando e-mail é grande: ==> # xvalem02 = re.compile(r'^[a-zA-Z0-9][\w.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$')
    # == Não usar mais esse método! Ele trava todo o sistema quando e-mail é grande: ==> # if xvalem01.match(stextchk) and xvalem02.match(stextchk): return True
    # == Não usar mais esse método! Ele trava todo o sistema quando e-mail é grande: ==> if re.fullmatch(xvalem01, stextchk): return True
    # == Não usar mais esse método! Ele trava todo o sistema quando e-mail é grande: ==> else: return False    
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_valida_cpf ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que valida um CPF.                                                                                                                           // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_valida_cpf(stextchk):
    stxtlist = '0123456789'
    ilentext = len(stextchk)
    sauxstru = ''
    snumonly = ''
    bvalidad = False
    if ilentext == 14:
        if stextchk != '000.000.000-00':
            for iauxi001 in range(ilentext):
                if   stextchk[iauxi001] == '.': sauxstru = sauxstru + '.'
                elif stextchk[iauxi001] == '-': sauxstru = sauxstru + '-'
                else:
                    iauxi002 = stxtlist.find(stextchk[iauxi001])
                    if iauxi002 >= 0:
                        sauxstru = sauxstru + 'X'
                        if len(snumonly) < 9:
                            snumonly = snumonly + stextchk[iauxi001]
            if sauxstru == 'XXX.XXX.XXX-XX':
                # Cálculo do primeiro dígito
                iauxi003 = 0
                for iauxi001 in range(len(snumonly)):
                    iauxi002 = 10 - iauxi001
                    iauxi003 = iauxi003 + (int(snumonly[iauxi001]) * iauxi002)
                iauxi004 = iauxi003 % 11
                if iauxi004 < 2:    ipridigi = 0
                else:               ipridigi = 11 - iauxi004
                snumonly = str(snumonly) + str(ipridigi)
                # Cálculo do segundo dígito
                iauxi003 = 0
                for iauxi001 in range(len(snumonly)):
                    iauxi002 = 11 - iauxi001
                    iauxi003 = iauxi003 + (int(snumonly[iauxi001]) * iauxi002)
                iauxi004 = iauxi003 % 11
                if iauxi004 < 2:    isecdigi = 0
                else:               isecdigi = 11 - iauxi004
                # Comparando resultados
                idigveri = (int(stextchk[12]) * 10) + int(stextchk[13])
                idigconf = (ipridigi * 10) + isecdigi
                if idigveri == idigconf: bvalidad = True
    return bvalidad
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_valida_cnpj ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que valida um CNPJ.                                                                                                                          // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_valida_cnpj(stextchk):
    stxtlist = '0123456789'
    ilentext = len(stextchk)
    sauxstru = ''
    snumonly = ''
    bvalidad = False
    if ilentext == 18:
        if stextchk != '00.000.000/0000-00':
            for iauxi001 in range(ilentext):
                if stextchk[iauxi001] in './-':
                    sauxstru += stextchk[iauxi001]
                else:
                    iauxi002 = stxtlist.find(stextchk[iauxi001])
                    if iauxi002 >= 0:
                        sauxstru += 'X'
                        if len(snumonly) < 14:
                            snumonly += stextchk[iauxi001]
            # print('========================================')            
            # print('sauxstru: ', sauxstru)            
            # print('snumonly: ', snumonly)
            if sauxstru == 'XX.XXX.XXX/XXXX-XX':
                # Cálculo do primeiro dígito verificador
                lcalprid = [
                    [int(snumonly[0])  , 5    , None],
                    [int(snumonly[1])  , 4    , None],
                    [int(snumonly[2])  , 3    , None],
                    [int(snumonly[3])  , 2    , None],
                    [int(snumonly[4])  , 9    , None],
                    [int(snumonly[5])  , 8    , None],
                    [int(snumonly[6])  , 7    , None],
                    [int(snumonly[7])  , 6    , None],
                    [int(snumonly[8])  , 5    , None],
                    [int(snumonly[9])  , 4    , None],
                    [int(snumonly[10]) , 3    , None],
                    [int(snumonly[11]) , 2    , None],
                ]
                lpridigv = [int(snumonly[12]), 0, None, None, None]
                for lauxi001 in lcalprid:
                    lauxi001[2] = lauxi001[0] * lauxi001[1]
                    lpridigv[1] = lpridigv[1] + lauxi001[2]
                lpridigv[2] = round(lpridigv[1] / 11,2)
                lpridigv[3] = lpridigv[1] % 11
                if lpridigv[3] in [0, 1]:   lpridigv[4] = 0
                else:                       lpridigv[4] = 11 - lpridigv[3]
                # Cálculo do segundo dígito verificador
                lcalsegd = [
                    [int(snumonly[0])  , 6    , None],
                    [int(snumonly[1])  , 5    , None],
                    [int(snumonly[2])  , 4    , None],
                    [int(snumonly[3])  , 3    , None],
                    [int(snumonly[4])  , 2    , None],
                    [int(snumonly[5])  , 9    , None],
                    [int(snumonly[6])  , 8    , None],
                    [int(snumonly[7])  , 7    , None],
                    [int(snumonly[8])  , 6    , None],
                    [int(snumonly[9])  , 5    , None],
                    [int(snumonly[10]) , 4    , None],
                    [int(snumonly[11]) , 3    , None],
                    [int(snumonly[12]) , 2    , None],
                ]
                lsegdigv = [int(snumonly[13]), 0, None, None, None]
                for lauxi001 in lcalsegd:
                    lauxi001[2] = lauxi001[0] * lauxi001[1]
                    lsegdigv[1] = lsegdigv[1] + lauxi001[2]
                lsegdigv[2] = round(lsegdigv[1] / 11,2)
                lsegdigv[3] = lsegdigv[1] % 11
                if lsegdigv[3] in [0, 1]:   lsegdigv[4] = 0
                else:                       lsegdigv[4] = 11 - lsegdigv[3]
                # print('========================================')
                # for lauxi001 in lcalprid:
                #     print(lauxi001)
                # print('----------------------------------------')
                # print(lpridigv)
                # print('========================================')
                # for lauxi001 in lcalsegd:
                #     print(lauxi001)
                # print('----------------------------------------')
                # print(lsegdigv)
                # print('========================================')
                # print(lpridigv[0], ' - ', lpridigv[4], ' - ', lpridigv[0] == lpridigv[4])
                # print(lsegdigv[0], ' - ', lsegdigv[4], ' - ', lsegdigv[0] == lsegdigv[4])
                if lpridigv[0] == lpridigv[4] and lsegdigv[0] == lsegdigv[4]:
                    bvalidad = True
    return bvalidad
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_check_rules_fields ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que analisa as regras referentes ao campos digitados/selecionados/flagados pelo usuário na pagina HTML/CSS/JS.                               // #
# // Esta função lê o dicionário a lista lmrulesx, verifica as integridades conforme as regras, e mostra os erros ao usuário caso existam.               // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_check_rules_fields(lmrulesx, btenable):
    bvalidad = True
    # Debug: (inicio)
    # abnf_show('10', lmrulesx, 1)
    # Debug: (fim)
    for lauxi001 in lmrulesx:
        if lauxi001[0] == 'nps':    # "Não pode ser" => Não pode ser igual ao que foi definido
            if lauxi001[1] == lauxi001[4]:
                sgenerof = lauxi001[2]
                snomecam = lauxi001[3]
                if   sgenerof == 'M': smenserr = 'O ' + snomecam + ' está inválido!'
                elif sgenerof == 'F': smenserr = 'A ' + snomecam + ' está inválida!'
                abnf_alert(smenserr, 5)
                bvalidad = False
                abnf_socket_004([5, btenable])
                break
        elif lauxi001[0] == 'equ':    # "Equal" => Dois campos que tem que serem iguais
            if lauxi001[1] != lauxi001[4]:
                sgenerof = lauxi001[2]
                snomecam = lauxi001[3]
                if   sgenerof == 'M': smenserr = 'O ' + snomecam + ' está diferente d'
                elif sgenerof == 'F': smenserr = 'A ' + snomecam + ' está diferente d'
                sgenerof = lauxi001[5]
                snomecam = lauxi001[6]
                if   sgenerof == 'M': smenserr = smenserr + 'o ' + snomecam + '!'
                elif sgenerof == 'F': smenserr = smenserr + 'a ' + snomecam + '!'
                abnf_alert(smenserr, 5)
                bvalidad = False
                abnf_socket_004([5, btenable])
                break
        elif lauxi001[0] == 'eml':    # "E-mail" => Analisa se o e-mail foi digitado corretamente
            if not abnf_valida_email(lauxi001[1]):
                sgenerof = lauxi001[2]
                snomecam = lauxi001[3]
                if   sgenerof == 'M': smenserr = 'O ' + snomecam + ' está inválido!'
                elif sgenerof == 'F': smenserr = 'A ' + snomecam + ' está inválida!'
                abnf_alert(smenserr, 5)
                bvalidad = False
                abnf_socket_004([5, btenable])
                break
        elif lauxi001[0] == '@e1@e2':    # Se um dos elementos existir o outro também tem que existir
            if (lauxi001[1] != None and lauxi001[4] == None) or (lauxi001[1] == None and lauxi001[4] != None):
                if lauxi001[1] == None:
                    sgenerof = lauxi001[2]
                    snomecam = lauxi001[3]
                elif lauxi001[4] == None:
                    sgenerof = lauxi001[5]
                    snomecam = lauxi001[6]
                smenserr = ''
                if   sgenerof == 'M': smenserr = 'O ' + snomecam + ' está inválido!'
                elif sgenerof == 'F': smenserr = 'A ' + snomecam + ' está inválida!'
                abnf_alert(smenserr, 5)
                bvalidad = False
                abnf_socket_004([5, btenable])
                break
        elif lauxi001[0] == 'e2>e1':    # O segundo elemento tem que ser maior que o primeiro
            if lauxi001[4] != None and lauxi001[1] != None and not lauxi001[4] > lauxi001[1]:
                sgener01 = lauxi001[2]
                snomec01 = lauxi001[3]
                sgener02 = lauxi001[5]
                snomec02 = lauxi001[6]
                smenserr = ''
                if   sgener01 == 'M': smenserr = smenserr + 'O '
                elif sgener01 == 'F': smenserr = smenserr + 'A '
                smenserr = smenserr + snomec01 + ' tem que ser menor que '
                if   sgener02 == 'M': smenserr = smenserr + ' o '
                elif sgener02 == 'F': smenserr = smenserr + ' a '
                smenserr = smenserr + snomec02 + '!'
                abnf_alert(smenserr, 5)
                bvalidad = False
                abnf_socket_004([5, btenable])
                break
        elif lauxi001[0] == 'e2>=e1':   # O segundo elemento tem que ser maior ou igual ao primeiro
            if lauxi001[4] != None and lauxi001[1] != None and not lauxi001[4] >= lauxi001[1]:
                sgener01 = lauxi001[2]
                snomec01 = lauxi001[3]
                sgener02 = lauxi001[5]
                snomec02 = lauxi001[6]
                smenserr = ''
                if   sgener01 == 'M': smenserr = smenserr + 'O '
                elif sgener01 == 'F': smenserr = smenserr + 'A '
                smenserr = smenserr + snomec01 + ' tem que ser menor ou igual'
                if   sgener02 == 'M': smenserr = smenserr + ' o '
                elif sgener02 == 'F': smenserr = smenserr + ' a '
                smenserr = smenserr + snomec02 + '!'
                abnf_alert(smenserr, 5)
                bvalidad = False
                abnf_socket_004([5, btenable])
                break
        elif lauxi001[0] == 'e1<>e2':   # O dois elementos não podem ser iguais
            if lauxi001[1] != None and lauxi001[4] != None and lauxi001[1] == lauxi001[4]:
                sgener01 = lauxi001[2]
                snomec01 = lauxi001[3]
                sgener02 = lauxi001[5]
                snomec02 = lauxi001[6]
                smenserr = ''
                if   sgener01 == 'M': smenserr = smenserr + 'O '
                elif sgener01 == 'F': smenserr = smenserr + 'A '
                smenserr = smenserr + snomec01 + ' não pode ser igual'
                if   sgener02 == 'M': smenserr = smenserr + ' o '
                elif sgener02 == 'F': smenserr = smenserr + ' a '
                smenserr = smenserr + snomec02 + '!'
                abnf_alert(smenserr, 5)
                bvalidad = False
                abnf_socket_004([5, btenable])
                break
        elif lauxi001[0] == 'e1>zero':  # O primeiro elemento tem que ser maior que zero
            if lauxi001[1] != None and lauxi001[1] <= 0:
                sgener01 = lauxi001[2]
                snomec01 = lauxi001[3]
                smenserr = ''
                if   sgener01 == 'M': smenserr = smenserr + 'O '
                elif sgener01 == 'F': smenserr = smenserr + 'A '
                smenserr = smenserr + snomec01 + ' não pode ser menor ou igual a zero!'
                abnf_alert(smenserr, 5)
                bvalidad = False
                abnf_socket_004([5, btenable])
                break
        elif lauxi001[0] == 'e1<=limite':  # O primeiro elemento não pode ser maior que o limite
            if lauxi001[1] != None and lauxi001[1] > lauxi001[4]:
                sgener01 = lauxi001[2]
                snomec01 = lauxi001[3]
                smenserr = ''
                if   sgener01 == 'M': smenserr = smenserr + 'O '
                elif sgener01 == 'F': smenserr = smenserr + 'A '
                smenserr = smenserr + snomec01 + ' não pode ser maior que ' + str(lauxi001[4]) + '!'
                abnf_alert(smenserr, 5)
                bvalidad = False
                abnf_socket_004([5, btenable])
                break
        elif lauxi001[0] == 'e1>=limite':  # O primeiro elemento não pode ser menor que o limite
            if lauxi001[1] != None and lauxi001[1] < lauxi001[4]:
                sgener01 = lauxi001[2]
                snomec01 = lauxi001[3]
                smenserr = ''
                if   sgener01 == 'M': smenserr = smenserr + 'O '
                elif sgener01 == 'F': smenserr = smenserr + 'A '
                smenserr = smenserr + snomec01 + ' não pode ser menor que ' + str(lauxi001[4]) + '!'
                abnf_alert(smenserr, 5)
                bvalidad = False
                abnf_socket_004([5, btenable])
                break
    return bvalidad
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_websocket_valida_estrutura_usuario ] ////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que valida o formato do usuário.                                                                                                             // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_websocket_valida_estrutura_usuario(stextchk):
    if not stextchk: return True
    stxtlist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    ilentext = len(stextchk)
    sauxstru = ''
    bvalidad = True
    for iauxi001 in range(ilentext):
        if stextchk[iauxi001] == '.':
            sauxstru = sauxstru + '.'
            bvalidad = True
        else:
            iauxi002 = stxtlist.find(stextchk[iauxi001])
            if iauxi002 >= 0 and bvalidad:
                sauxstru = sauxstru + 'X'
                bvalidad = False
    if sauxstru == 'X.X': return True
    else: return False
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_websocket_limpa_campos ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Limpa campos do formulário HTML/CSS/JS utilizando recursos SockectIO e JS.                                                                          // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #    
    
def abnf_websocket_limpa_campos(lmfields):
    for lauxi001 in lmfields:
        snomecam = lauxi001[0]
        abnf_socket_004([3, snomecam, ''])
    return True

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_websocket_date_time ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que devolve data/hora do sistema.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_websocket_date_time(iparamet):
    if iparamet == 1:       # Devolve [dia/mês/ano hora:minuto:segundo] atual
        ddateaux = datetime.now()
        sdateaux = ddateaux.strftime('%d/%m/%Y %H:%M:%S')
        return sdateaux
    elif iparamet == 2:     # Devolve [dia/mês/ano] atual
        ddateaux = datetime.now()
        sdateaux = ddateaux.strftime('%d/%m/%Y')
        return sdateaux
    elif iparamet == 3:     # Devolve [hora:minuto:segundo] atual
        ddateaux = datetime.now()
        sdateaux = ddateaux.strftime('%H:%M:%S')
        return sdateaux
    elif iparamet == 4:     # Devolve [hora:minuto] atual
        ddateaux = datetime.now()
        sdateaux = ddateaux.strftime('%H:%M')
        return sdateaux
    elif iparamet == 5:     # Devolve [anomêsdiahora] atual
        ddateaux = datetime.now()
        sdateaux = ddateaux.strftime('%Y%m%d%H')
        return sdateaux
    elif iparamet == 6:     # Devolve a data e última hora/minuto/segundo do dia anterior no formato para abastecer campo datetime de um banco SQL
        ddateaux = (datetime.now() - timedelta(days=1)).replace(hour=23, minute=59, second=59, microsecond=0)
        sdateaux = ddateaux.strftime('%Y-%m-%d %H:%M:%S')
        return sdateaux
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_websocket_log ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que escreve no arquivo de log separado por projeto.                                                                                          // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_websocket_log(sabnproj, icodilog, slogtxt1, slogtxt2, slogtxt3, slogtxt4, slogtxt5, slogtxt6, xlistadb):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_websocket_log (Gravação no arquivo de log do projeto)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    scaptuip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    # Abaixo o local do Log separado por projeto (ele vai ser usado assim que tiver mais de uma empresa usando o sitema):
    # sarqulog = 'abnflog/' + sabnproj + '/abnflog' + datetime.now().strftime('%Y%m')
    # Por enquanto manter o log no mesmo local onde está sendo usado pelo sistema Flask (sem SocketIO):
    sarqulog = 'abnflog/abnflog' + datetime.now().strftime('%Y%m')
    print('Projeto ........: ' + sabnproj)
    print('IP do cliente ..: ' + scaptuip)
    print('Arquivo de log .: ' + sarqulog)
    print('----------------------------------------------------------------------------------------------------------------------------------')
    if icodilog == 1 or icodilog == 2 or icodilog == 3 or icodilog == 4:
        sarqulog = sarqulog + 'a.log'
        with open(sarqulog, 'a') as sarquwri:
            sarquwri.write('================\n')
            sarquwri.write('@abnflog#000000'+str(icodilog)+'\n')
            sarquwri.write(abnf_websocket_date_time(2) + '\n')
            sarquwri.write(abnf_websocket_date_time(3) + '\n')
            sarquwri.write(scaptuip + '\n')
            if icodilog != 1: sarquwri.write(str(slogtxt1) + '\n')
            sarquwri.write('@abnflog#9999999\n')
    elif icodilog == 100:   # =>> Acesso ao sistema
        sarqulog = sarqulog + 'b.log'
        with open(sarqulog, 'a') as sarquwri:
            sarquwri.write('================\n')
            sarquwri.write('@abnflog#0000100\n')
            sarquwri.write(abnf_websocket_date_time(2) + '\n')
            sarquwri.write(abnf_websocket_date_time(3) + '\n')
            sarquwri.write(scaptuip + '\n')
            sarquwri.write(str(slogtxt1) + '\n')
            sarquwri.write(str(slogtxt2) + '\n')
            sarquwri.write(str(slogtxt3) + '\n')
            sarquwri.write(str(slogtxt4) + '\n')
            sarquwri.write(str(slogtxt5) + '\n')
            sarquwri.write(str(slogtxt6) + '\n')
            sarquwri.write('@abnflog#9999999\n')
    elif icodilog == 200:   # =>> Acesso aos modulos do sistema / seleção registro de dados
        sarqulog = sarqulog + 'b.log'
        with open(sarqulog, 'a') as sarquwri:
            sarquwri.write('================\n')
            sarquwri.write('@abnflog#0000200\n')
            sarquwri.write(abnf_websocket_date_time(2) + '\n')
            sarquwri.write(abnf_websocket_date_time(3) + '\n')
            sarquwri.write(scaptuip + '\n')
            sarquwri.write(str(slogtxt1) + '\n')
            sarquwri.write(str(slogtxt2) + '\n')
            sarquwri.write(str(slogtxt3) + '\n')
            sarquwri.write(str(slogtxt4) + '\n')
            sarquwri.write(str(slogtxt5) + '\n')
            sarquwri.write(str(slogtxt6) + '\n')
            if xlistadb != None:
                for xauxilis in xlistadb:
                    if xauxilis[4] == None:
                        sarquwri.write('@abnflog#0000201\n')
                        sarquwri.write(str(xauxilis[0] if xauxilis[0] != None else '') + '\n')
                        sarquwri.write(str(xauxilis[1] if xauxilis[1] != None else '') + '\n')
                        sarquwri.write(str(xauxilis[2] if xauxilis[2] != None else '') + '\n')
                        sarquwri.write(str(xauxilis[3] if xauxilis[3] != None else '') + '\n')
                    else:
                        sarquwri.write('@abnflog#0000202\n')
                        sarquwri.write(str(xauxilis[0] if xauxilis[0] != None else '') + '\n')
                        sarquwri.write(str(xauxilis[1] if xauxilis[1] != None else '') + '\n')
                        sarquwri.write(str(xauxilis[2] if xauxilis[2] != None else '') + '\n')
                        sarquwri.write(str(xauxilis[3] if xauxilis[3] != None else '') + '\n')
                        sarquwri.write(str(xauxilis[4] if xauxilis[4] != None else '') + '\n')
                        sarquwri.write(str(xauxilis[5] if xauxilis[5] != None else '') + '\n')
                        sarquwri.write(str(xauxilis[6] if xauxilis[6] != None else '') + '\n')
            sarquwri.write('@abnflog#9999999\n')
    elif (
        icodilog == 300 or  # =>> Inclusão de registros
        icodilog == 400 or  # =>> Alteração de registros
        icodilog == 500     # =>> Exclusão de registros
        ):
        sarqulog = sarqulog + 'b.log'
        with open(sarqulog, 'a') as sarquwri:
            sarquwri.write('================\n')
            sarquwri.write('@abnflog#0000'+str(icodilog)+'\n')
            sarquwri.write(abnf_websocket_date_time(2) + '\n')
            sarquwri.write(abnf_websocket_date_time(3) + '\n')
            sarquwri.write(scaptuip + '\n')
            sarquwri.write(str(slogtxt1) + '\n')
            sarquwri.write(str(slogtxt2) + '\n')
            sarquwri.write(str(slogtxt3) + '\n')
            sarquwri.write(str(slogtxt4) + '\n')
            sarquwri.write(str(slogtxt5) + '\n')
            sarquwri.write(str(slogtxt6) + '\n')
            for xauxilis in xlistadb:
                if xauxilis[4] == None:
                    sarquwri.write('@abnflog#0000'+str(icodilog + 1)+'\n')
                    sarquwri.write(str(xauxilis[0] if xauxilis[0] != None else '') + '\n')
                    sarquwri.write(str(xauxilis[1] if xauxilis[1] != None else '') + '\n')
                    sarquwri.write(str(xauxilis[2] if xauxilis[2] != None else '') + '\n')
                    sarquwri.write(str(xauxilis[3] if xauxilis[3] != None else '') + '\n')
                else:
                    sarquwri.write('@abnflog#0000'+str(icodilog + 2)+'\n')
                    sarquwri.write(str(xauxilis[0] if xauxilis[0] != None else '') + '\n')
                    sarquwri.write(str(xauxilis[1] if xauxilis[1] != None else '') + '\n')
                    sarquwri.write(str(xauxilis[2] if xauxilis[2] != None else '') + '\n')
                    sarquwri.write(str(xauxilis[3] if xauxilis[3] != None else '') + '\n')
                    sarquwri.write(str(xauxilis[4] if xauxilis[4] != None else '') + '\n')
                    sarquwri.write(str(xauxilis[5] if xauxilis[5] != None else '') + '\n')
                    sarquwri.write(str(xauxilis[6] if xauxilis[6] != None else '') + '\n')
            sarquwri.write('@abnflog#9999999\n')
    elif icodilog == 600:   # =>> Executa comnando SQL com commit
        sarqulog = sarqulog + 'b.log'
        with open(sarqulog, 'a') as sarquwri:
            sarquwri.write('================\n')
            sarquwri.write('@abnflog#0000'+str(icodilog)+'\n')
            sarquwri.write(abnf_websocket_date_time(2) + '\n')
            sarquwri.write(abnf_websocket_date_time(3) + '\n')
            sarquwri.write(scaptuip + '\n')
            sarquwri.write(str(slogtxt1) + '\n')
            sarquwri.write(str(slogtxt2) + '\n')
            sarquwri.write(str(slogtxt3) + '\n')
            sarquwri.write(str(slogtxt4) + '\n')
            sarquwri.write(str(slogtxt5) + '\n')
            sarquwri.write(str(slogtxt6) + '\n')
            sarquwri.write('@abnflog#9999999\n')
    # elif (
    #     icodilog == 901 or  # =>> Negado ao usuario acesso a modulos
    #     icodilog == 902 or  # =>> Negado ao usuario criação de registros
    #     icodilog == 903 or  # =>> Negado ao usuario alteração de registros
    #     icodilog == 904     # =>> Negado ao usuario exclusão de registros
    #     ):
    #     sarqulog = sarqulog + 'b.log'
    #     with open(sarqulog, 'a') as sarquwri:
    #         sarquwri.write('================\n')
    #         sarquwri.write('@abnflog#0000'+str(icodilog)+'\n')
    #         sarquwri.write(abnf_websocket_date_time(2) + '\n')
    #         sarquwri.write(abnf_websocket_date_time(3) + '\n')
    #         sarquwri.write(scaptuip + '\n')
    #         sarquwri.write(str(slogtxt1) + '\n')
    #         sarquwri.write(str(slogtxt2) + '\n')
    #         sarquwri.write(str(slogtxt3) + '\n')
    #         sarquwri.write(str(slogtxt4) + '\n')
    #         sarquwri.write(str(slogtxt5) + '\n')
    #         sarquwri.write(str(slogtxt6) + '\n')
    #         sarquwri.write('@abnflog#9999999\n')
    # elif icodilog == 9999000:
    #     sarqulog = sarqulog + 'b.log'
    #     with open(sarqulog, 'a') as sarquwri:
    #         sarquwri.write('================\n')
    #         sarquwri.write('@abnflog#9999000\n')
    #         sarquwri.write(abnf_websocket_date_time(2) + '\n')
    #         sarquwri.write(abnf_websocket_date_time(3) + '\n')
    #         sarquwri.write(scaptuip + '\n')
    #         sarquwri.write(str(slogtxt1) + '\n')
    #         sarquwri.write(str(slogtxt2) + '\n')
    #         sarquwri.write(str(slogtxt3) + '\n')
    #         sarquwri.write(str(slogtxt4) + '\n')
    #         sarquwri.write(str(slogtxt5) + '\n')
    #         sarquwri.write(str(slogtxt6) + '\n')
    #         sarquwri.write('@abnflog#9999999\n')
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_websocket_local_docs ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que define o local onde ficam os arquivos de upload dos usuários conforme o projeto.                                                         // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_websocket_local_docs(sabnproj):
    sldocpro = None
    if   sabnproj == '10000000000010000': sldocpro = 'abnfsrc/static/abnfarc/'          # Teste Sistema
    elif sabnproj == '12792863164510001': sldocpro = 'abnfsrc/static/abnfarc/'          # Tupi Transporte
    elif sabnproj == '17646826035010002': sldocpro = 'abnfsrc/static/abnfarc/'          # Rapido Sumaré
    # Nota: 24/07/2024
    # elif sabnproj == '15047354061710003': sldocpro = 'abnfdoc/003/'                   # Trans Acreana    
    # O local definido acima ('abnfdoc/003/') vai passar a ser o oficial a partir do momento
    # que não precisar mais do sistema velho o qual não consegue enxergar essa pasta.
    # Então para alinhar os sistemas, é necessário no momento apontar para o local onde os dois consigam enxergar: 'abnfsrc/static/abnfarc/'
    elif sabnproj == '15047354061710003': sldocpro = 'abnfsrc/static/abnfarc/'          # Trans Acreana
    return sldocpro
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_divisor ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função provisório de auxilío de programação - separa dados no prompt através de barras divisoras.                                                   // #
# // Usado apenas para auxiliar na programação.                                                                                                          // #
# // Dica de uso: abnf_divisor(2, 2, 5)                                                                                                                  // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    
def abnf_divisor(icodbarr, iqtdbarr, iqtdpara):
    if   icodbarr == 1: sbarrtxt = '⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠⊠'
    elif icodbarr == 2: sbarrtxt = '█▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀█'
    else:               sbarrtxt = '----------------------------------------------------------------------------------------------------------------------------------'
    for icontd01 in range(iqtdbarr):
        print(sbarrtxt)
    time.sleep(iqtdpara)
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_mostra_variável ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função provisória de auxilío de programação - mostra variávies e para pelo tempo definido em segundos para análise.                                 // #
# // Usado apenas para auxiliar na programação.                                                                                                          // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    
def abnf_mostra_variáveis(lauxi001, itempopa):
    abnf_divisor(2, 2, 0)
    for lauxi002 in lauxi001:
        if lauxi002 != None:
            print(lauxi002)
    abnf_divisor(2, 2, itempopa)    
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_websocket_mostra_dicionario ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função provisória de auxilío de programação - mostra um dicionário em formato de lista e para pelo tempo definido em segundos para análise.         // #
# // Usado apenas para auxiliar na programação.                                                                                                          // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    
def abnf_websocket_mostra_dicionario(dauxi001, itempopa):
    abnf_divisor(2, 2, 0)
    for lauxi001 in dauxi001:
        print(lauxi001, ' - ', dauxi001[lauxi001])
    abnf_divisor(2, 2, itempopa)
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_websocket_arquivo_imagem ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que complementa arquivo de imagem para ser mostrado no codigo HTML.                                                                          // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_websocket_arquivo_imagem(sarqimag, sclassbo, simgwidt, simgheig):
    scodeimg = '<img src="' + sarqimag + '" width="' + simgwidt + '" height="' + simgheig + '"'
    if sclassbo != None: scodeimg = scodeimg + ' class="' + sclassbo + '"'
    scodeimg = scodeimg + '>'
    return scodeimg    
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_websocket_converte_arquivo_imagem_base64 ] //////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que converte arquivos de imagem em codificação binária 64.                                                                                   // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_websocket_converte_arquivo_imagem_base64(sarqimag, sclassbo, simgwidt, simgheig):
    scodeimg = ''
    if os.path.exists(sarqimag):
        with open(sarqimag, "rb") as ofileimg:
            scodeimg = base64.b64encode(ofileimg.read()).decode('utf-8')
    scodeimg = '<img src="data:image/jpeg;base64,' + scodeimg + '" width="' + simgwidt + '" height="' + simgheig + '"'
    if sclassbo != None: scodeimg = scodeimg + ' class="' + sclassbo + '"'
    scodeimg = scodeimg + '>'
    return scodeimg

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_lista_outlers ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que identifica outlers em uma lista de dados numérica.                                                                                       // #
# // Ao observar uma lista de números, percebemos que a maioria dos valores está concentrada em uma faixa relativamente pequena,                         // #
# // com exceção de um valor muito maior que os demais.                                                                                                  // #
# // Esse número maior é chamado de "outlier".                                                                                                           // #
# // Porque indentificar um outler?                                                                                                                      // #
# // Distância dos demais valores: É significativamente maior que os outros valores da lista.                                                            // #
# // Possibilidade de erro: Pode ser um erro de digitação ou um valor inserido incorretamente.                                                           // #
# // Natureza dos dados: Dependendo do contexto dos dados, um valor tão alto pode não fazer sentido.                                                     // #
# // Parâmetros:                                                                                                                                         // #
# // llisnume: Uma lista de números.                                                                                                                     // #
# // ilimitez: O limite do z-score para considerar um valor como outlier.                                                                                // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_lista_outlers(llisnume, ilimitez):
    # Calcula a média
    nmediaxx = sum(llisnume) / len(llisnume)
    # Calcula o desvio padrão
    ndesvpad = (sum((nauxi001 - nmediaxx) ** 2 for nauxi001 in llisnume) / len(llisnume)) ** 0.5
    # Calcula os z-scores e identifica os outliers
    loutlier = []
    if ndesvpad != 0:
        for iauxi001 in llisnume:
            nzscorex = (iauxi001 - nmediaxx) / ndesvpad
            if abs(nzscorex) > ilimitez:
                loutlier.append(iauxi001)
    return loutlier
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_converte_data ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que converte data em string.                                                                                                                 // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_converte_data(ddatachk):
    if ddatachk:    sdatachk = ddatachk.strftime('%d/%m/%Y')
    else:           sdatachk = ''
    return sdatachk
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_converte_datahora ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que converte datahota em string.                                                                                                             // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_converte_datahora(ddatachk, iparamet):
    if ddatachk:
        if iparamet == 0:
            sdatachk = ddatachk.strftime('%d/%m/%Y %H:%M:%S')
        elif iparamet == 1:
            sdatachk = ddatachk.strftime('%d/%m/%Y %H:%M')
    else:
        sdatachk = ''
    return sdatachk

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_converte_string_datahora ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que converte uma string em um campo data/hora.                                                                                               // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_converte_string_datahora(sdatachk):
    if sdatachk: ddatachk = datetime.strptime(sdatachk, '%d/%m/%Y %H:%M:%S')
    else:        ddatachk = ''
    return ddatachk

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_converte_data_semana ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que tras informações do dia semana de uma data.                                                                                              // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_converte_data_semana(ddatachk):
    lsemanax = ('', '')
    if ddatachk:
        iauxi001 = ddatachk.weekday()
        if   iauxi001 == 0: lsemanax = ('SEGUNDA-FEIRA', 'SEG', ('2', 'U'))
        elif iauxi001 == 1: lsemanax = ('TERÇA-FEIRA',   'TER', ('3', 'U'))
        elif iauxi001 == 2: lsemanax = ('QUARTA-FEIRA',  'QUA', ('4', 'U'))
        elif iauxi001 == 3: lsemanax = ('QUINTA-FEIRA',  'QUI', ('5', 'U'))
        elif iauxi001 == 4: lsemanax = ('SEXTA-FEIRA',   'SEX', ('6', 'U'))
        elif iauxi001 == 5: lsemanax = ('SÁBADO',        'SAB', ('S'))
        elif iauxi001 == 6: lsemanax = ('DOMINGO',       'DOM', ('D'))
    return lsemanax

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_converte_hora ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que converte hora em string.                                                                                                                 // #
# // Eu ainda não sei ainda o motivo mas os registros tipo "time" ao ser buscados dentro do MariaDB estão vindo como "timedelta".                        // #
# // Devido a essa falha, estou tendo que converter em texto primeiramente antes de trabalhar sobre o conteúdo dos registros.                            // #
# // E vamos ter que usar recursos de string para separar os dados entre hora, minuto e segundo.                                                         // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_converte_hora(dhorachk, bseconds):
    lhorachk = str(dhorachk).split(':')
    shoraret = ''
    if len(lhorachk) == 3:  # tem hora, minuto e segundo
        shoraaxu = str(int(lhorachk[0]) + 100)[1:]
        sminuaux = str(int(lhorachk[1]) + 100)[1:]
        sseguaux = str(int(lhorachk[2]) + 100)[1:]
        shoraret = shoraaxu + ':' + sminuaux
        if bseconds:
            shoraret = shoraret + ':' + sseguaux
    return shoraret

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_converte_hseg ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que converte hora em string incluindo os segundos.                                                                                           // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_converte_hseg(dhorachk):
    if dhorachk:    shorachk = dhorachk.strftime('%H:%M:%S')
    else:           shorachk = ''
    return shorachk

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_converte_data_hora ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que converte data/hora em string.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_converte_data_hora(ddthrchk, bseconds):
    if ddthrchk:    
        if bseconds:    sdthrchk = ddthrchk.strftime('%d/%m/%Y %H:%M:%S')
        else:           sdthrchk = ddthrchk.strftime('%d/%m/%Y %H:%M')
    else:               sdthrchk = ''
    return sdthrchk

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_converte_hora_especial ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função especial que converte hora em string.                                                                                                        // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_converte_hora_especial(tauxtime, bseconds):
    sauxtime = str(tauxtime)
    lauxtime = sauxtime.split(':')
    shoratmp = str(int(lauxtime[0]) + 100)[1:]
    sminutmp = str(int(lauxtime[1]) + 100)[1:]
    ssegutmp = str(int(lauxtime[2]) + 100)[1:]
    srettime = shoratmp + ':' + sminutmp
    if bseconds: srettime = srettime + ':' + ssegutmp
    return str(srettime)
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_converte_hora_string_em_segundos ] //////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função especial para traballhar com hora em formato texto.                                                                                          // #
# // Essa função foi criada para tratar conteúdos de input texto 'time-1' as quais foram criadas para trabalhar com horários fora do padrão html.        // #
# // Lembrando que os inputs 'time-1' são usados para digitação de horários acima de 23:59, portanto são considerados pelo html como textos e não horas. // #
# // Essa função então analisa a string, transforma esses textos em segundos no formato integer e devolve o resultado obtido.                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_converte_hora_string_em_segundos(shoratxt):
    ihoratmp = int(shoratxt[0:2]) * 60 * 60
    iminutmp = int(shoratxt[3:5]) * 60
    ihoraseg = ihoratmp + iminutmp
    return ihoraseg

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_converte_segundos_em_hora_string ] //////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função especial para traballhar com hora em formato texto.                                                                                          // #
# // Essa função foi criada para tratar conteúdos de input texto 'time-1' as quais foram criadas para trabalhar com horários fora do padrão html.        // #
# // Lembrando que os inputs 'time-1' são usados para digitação de horários acima de 23:59, portanto são considerados pelo html como textos e não horas. // #
# // Essa função então transforma os segundos no formato integer em textos padrão 'hh:min' e devolve o resultado obtido.                                 // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #    
    
def abnf_converte_segundos_em_hora_string(ihoraseg, bconv24h):
    ihoratmp = ihoraseg // 3600
    if bconv24h and ihoratmp > 23: ihoratmp = ihoratmp - 24
    iminutmp = (ihoraseg % 3600) // 60
    shoratxt = str(100 + ihoratmp)[1:] + ':' + str(100 + iminutmp)[1:]
    return shoratxt
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_converte_mes_ano_lista ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que lê uma lista contendendo mes ano. (Ex: [(2025, 1), (2025, 2) (2025,3), ...])                                                             // #
# // E converte em uma nova lista convertendo para Mês/Ano. (Ex: [('Jan/2025', 'Fev/2025', 'Mar/2025', ...])                                             // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #    

def abnf_converte_mes_ano_lista(lauxi001):
    lauxiret = []
    dauxi001 = {1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun', 7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'}
    for lauxi002 in lauxi001:
        lauxiret.append(dauxi001[lauxi002[1]] + '/' + str(lauxi002[0]))
    return lauxiret
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_formata_lista_hora ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que formata uma lista em hora.                                                                                                               // #
# // O primeiro parâmetro define a lista: 1 = (h, m, s) / 2 = (h, m) / 3 = (m, s)                                                                        // #
# // O segundo parâmetro define como a lista deve ser impressa:  1 = "00:00:00" / 2 = "00:00"                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_formata_lista_hora(lauxtime, itipolis, iretolis):
    if itipolis == 1:
        shoratmp = str(int(lauxtime[0]) + 100)[1:]
        sminutmp = str(int(lauxtime[1]) + 100)[1:]
        ssegutmp = str(int(lauxtime[2]) + 100)[1:]
    elif itipolis == 2:
        shoratmp = str(int(lauxtime[0]) + 100)[1:]
        sminutmp = str(int(lauxtime[1]) + 100)[1:]
        ssegutmp = '00'
    elif itipolis == 3:
        shoratmp = '00'
        sminutmp = str(int(lauxtime[0]) + 100)[1:]
        ssegutmp = str(int(lauxtime[1]) + 100)[1:]
    if   iretolis == 1: srettime = shoratmp + ':' + sminutmp + ':' + ssegutmp
    elif iretolis == 2: srettime = shoratmp + ':' + sminutmp
    elif iretolis == 3: srettime = sminutmp + ':' + ssegutmp
    return str(srettime)    

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_soma_subtrai_lista_hora_datetime ] //////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que soma ou substrai uma lista_hora e uma campo datetime e retorna em formato datetime.                                                      // #
# // ddtaux01 => recebe datetime.                                                                                                                        // #
# // lhauxi01 => recebe a lista.                                                                                                                         // #
# // itipolis => define o formato da lista: 1 = (h, m, s) / 2 = (h, m) / 3 = (m, s)                                                                      // #
# // stipoope => define o tipo de operação: 'A' = adição (soma o tempo) / 'S' = subtração (subtraí o tempo)                                              // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_soma_subtrai_lista_hora_datetime(ddtaux01, lhauxi01, itipolis, stipoope):
    idtaux01 = int(ddtaux01.timestamp())                                                        # Converte o campo datahora no momento exato do tempo em segundos e transforma em inteiro
    if   itipolis == 1: idtaux02 = (lhauxi01[0] * 60 * 60) + (lhauxi01[1] * 60) + lhauxi01[2]   # Converte a lista_hora em segundos
    elif itipolis == 2: idtaux02 = (lhauxi01[0] * 60 * 60) + (lhauxi01[1] * 60)                 # Converte a lista_hora em segundos
    elif itipolis == 3: idtaux02 = (lhauxi01[1] * 60) + lhauxi01[2]                             # Converte a lista_hora em segundos
    if   stipoope == 'A': idhretor = idtaux01 + idtaux02
    elif stipoope == 'S': idhretor = idtaux01 - idtaux02
    ddhretor = datetime.fromtimestamp(idhretor)
    return ddhretor
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_converte_timestamp_para_hora ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que converte a função timestamp para hora e retorna em formato string (HHHH:MM:SS).                                                          // #
# // A função timestamp, após passar de 23:59:59, retorna desta forma: 1 day, 14:04:00                                                                   // #
# // Essa função faz com que esses valores sejam convertidos para voltar no formato string que precisamos.                                               // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_converte_timestamp_para_hora(ddtaux01):
    # Para converter um objeto timedelta para o formato desejado, você pode utilizar o método total_seconds() para obter o número total
    # de segundos e, em seguida, tranformar em inteiro esse resultado e depois realizar cálculos para obter as horas, minutos e segundos.
    idtaux01 = int(ddtaux01.total_seconds())
    srettime = abnf_converte_segundos_em_horas(idtaux01, 0)
    return srettime
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_converte_segundos_em_minutos ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que converte segundos (int) em minutos no formato "00:00"                                                                                    // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_converte_segundos_em_minutos(iseconds, iparamet):
    icalcmin = iseconds // 60
    icalcseg = iseconds % 60
    if   iparamet == 0 and icalcmin >  99: srettime = str(icalcmin)           + ':' + str(100 + icalcseg)[1:]
    elif iparamet == 0 and icalcmin <= 99: srettime = str(100 + icalcmin)[1:] + ':' + str(100 + icalcseg)[1:]
    elif iparamet == 1 and icalcmin >  99: srettime = str(icalcmin)           + 'm' + str(100 + icalcseg)[1:] + 's'
    elif iparamet == 1 and icalcmin <= 99: srettime = str(100 + icalcmin)[1:] + 'm' + str(100 + icalcseg)[1:] + 's'
    return str(srettime)
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_converte_segundos_em_horas ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que converte segundos (int) em horas no formato "x00:00:00"                                                                                  // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_converte_segundos_em_horas(iseconds, iparamet):
    icalchor = iseconds // 3600
    icalcmin = (iseconds % 3600) // 60
    icalcseg = iseconds % 60
    if   iparamet == 0 and icalchor >  99: srettime = str(icalchor)           + ':' + str(100 + icalcmin)[1:] + ':' + str(100 + icalcseg)[1:]
    elif iparamet == 0 and icalchor <= 99: srettime = str(100 + icalchor)[1:] + ':' + str(100 + icalcmin)[1:] + ':' + str(100 + icalcseg)[1:]
    elif iparamet == 1 and icalchor >  99: srettime = str(icalchor)           + 'h' + str(100 + icalcmin)[1:] + 'm' + str(100 + icalcseg)[1:] + 's'
    elif iparamet == 1 and icalchor <= 99: srettime = str(100 + icalchor)[1:] + 'h' + str(100 + icalcmin)[1:] + 'm' + str(100 + icalcseg)[1:] + 's'
    return str(srettime)
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_soma_dias_data ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que soma dias a uma data usando timestamp.                                                                                                   // #
# // Essa função transforma o campo data em data-hora e depois em um número inteiro equivalente a data com zero horas.                                   // #
# // Depois multiplica a quantidade de segundos do dia pelos dias desejado, soma ao inteiro da data e transforma o resultado de volta para data.         // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #   
    
def abnf_soma_dias_data(ddatasom, iqtddias):
    tqtddias = timedelta(days = iqtddias)
    ddataret = ddatasom + tqtddias
    return ddataret
    
'''
# método antigo (início)
ddataaux = datetime(ddatasom.year, ddatasom.month, ddatasom.day)
ioldtmst = int(ddataaux.timestamp())
inewtmst = ioldtmst + (86400 * iqtddias)    # => 86400 segundos = 24 horas
ddataaux = datetime.fromtimestamp(inewtmst).date()
return ddataaux
# método antigo (fim)

TESTE:

from datetime import date, datetime, time, timedelta
ddataini = date(2000,1,1)
ddatafim = date(2050,12,31)
ddataaux = datetime(ddatafim.year, ddatafim.month, ddatafim.day)
print(ddataini, ' - ', ddatafim, ' - ', ddataaux)
print(ddataaux.timestamp())

ddatafim = date(2038,1,20)
ddataaux = datetime(ddatafim.year, ddatafim.month, ddatafim.day)
print(ddataaux.timestamp())

ddatafim = date(2038,1,19)
ddataaux = datetime(ddatafim.year, ddatafim.month, ddatafim.day)
print(ddataaux.timestamp())

No meu python esta ocorrendo o seguinte fato:

O codigo abaixo:

ddatafim = date(2038,1,19)
ddataaux = datetime(ddatafim.year, ddatafim.month, ddatafim.day)
print(ddataaux.timestamp())

retorna:

2147482800.0

Mas o codigo abaixo:

ddatafim = date(2038,1,20)
ddataaux = datetime(ddatafim.year, ddatafim.month, ddatafim.day)
print(ddataaux.timestamp())

retorna:

OverflowError: timestamp out of range for platform time_t

Ou seja, aparentemente tem um limite de timestamp até 19/01/2038.

Sabe dizer porque isso ocorre?

dteste = date(2050, 11, 23)
um_dia = timedelta(days=1)
print(um_dia)
dteste = dteste - um_dia
print(dteste)
menos_um_dia = timedelta(days=-1)
dteste = dteste + menos_um_dia
'''
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_personal_retorna_lista ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que retorna uma lista de opções personalizadas para serem inseridas em select.                                                               // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #    
    
def abnf_personal_retorna_lista(icodopti):
    if   icodopti == 10001:         # Situação do registro
        lmselect = [('A','ATIVO'),  ('I','INATIVO')]
    elif icodopti == 10002:         # Situação do registro
        lmselect = [('',''), ('M','MASCULINO'),  ('F','FEMININO')]
    elif icodopti == 10003:         # Vazio / Sim / Não
        lmselect = [('',''), ('S','SIM'),  ('N','NÃO')]
    elif icodopti == 10004:         # Sim / Não
        lmselect = [('S','SIM'),  ('N','NÃO')]        
    elif icodopti == 10101:         # Estados do Brasil
        lmselect = [ 
            ('',''),
            ('AC','AC -> ACRE'),
            ('AL','AL -> ALAGOAS'),
            ('AP','AP -> AMAPA'),
            ('AM','AM -> AMAZONAS'),
            ('BA','BA -> BAHIA'),
            ('CE','CE -> CEARA'),
            ('DF','DF -> DISTRITO FEDERAL'),
            ('ES','ES -> ESPIRITO SANTO'),
            ('GO','GO -> GOIAS'),
            ('MA','MA -> MARANHAO'),
            ('MT','MT -> MATO GROSSO'),
            ('MS','MS -> MATO GROSSO DO SUL'),
            ('MG','MG -> MINAS GERAIS'),
            ('PA','PA -> PARA'),
            ('PB','PB -> PARAIBA'),
            ('PR','PR -> PARANA'),
            ('PE','PE -> PERNAMBUCO'),
            ('PI','PI -> PIAUI'),
            ('RJ','RJ -> RIO DE JANEIRO'),
            ('RN','RN -> RIO GRANDE DO NORTE'),
            ('RS','RS -> RIO GRANDE DO SUL'),
            ('RO','RO -> RANDONIA'),
            ('RR','RR -> RARAIMA'),
            ('SC','SC -> SANTA CATARINA'),
            ('SP','SP -> SAO PAULO'),
            ('SE','SE -> SERGIPE'),
            ('TO','TO -> TOCANTINS')
        ]
    elif icodopti == 10103:         # Tipo de logradouro
        lmselect = [ 
            ('',''),
            ('ACAMPAMENTO'                     , 'ACAMPAMENTO'),
            ('ACESSO'                          , 'ACESSO'),
            ('ACESSO LOCAL'                    , 'ACESSO LOCAL'),
            ('ADRO'                            , 'ADRO'),
            ('AEROPORTO'                       , 'AEROPORTO'),
            ('ALAMEDA'                         , 'ALAMEDA'),
            ('ALCA DE ACESSO'                  , 'ALCA DE ACESSO'),
            ('ALTO'                            , 'ALTO'),
            ('ANEL VIARIO'                     , 'ANEL VIARIO'),
            ('ANTIGA ESTRADA'                  , 'ANTIGA ESTRADA'),
            ('AREA'                            , 'AREA'),
            ('AREA ESPECIAL'                   , 'AREA ESPECIAL'),
            ('AREA VERDE'                      , 'AREA VERDE'),
            ('ARTERIA'                         , 'ARTERIA'),
            ('ATALHO'                          , 'ATALHO'),
            ('AVENIDA'                         , 'AVENIDA'),
            ('AVENIDA CONTORNO'                , 'AVENIDA CONTORNO'),
            ('AVENIDA MARGINAL'                , 'AVENIDA MARGINAL'),
            ('AVENIDA MARGINAL DIREITA'        , 'AVENIDA MARGINAL DIREITA'),
            ('AVENIDA MARGINAL ESQUERDA'       , 'AVENIDA MARGINAL ESQUERDA'),
            ('AVENIDA VELHA'                   , 'AVENIDA VELHA'),
            ('BAIXA'                           , 'BAIXA'),
            ('BALAO'                           , 'BALAO'),
            ('BALNEARIO'                       , 'BALNEARIO'),
            ('BECO'                            , 'BECO'),
            ('BELVEDERE'                       , 'BELVEDERE'),
            ('BLOCO'                           , 'BLOCO'),
            ('BLOCOS'                          , 'BLOCOS'),
            ('BOSQUE'                          , 'BOSQUE'),
            ('BOULEVARD'                       , 'BOULEVARD'),
            ('BULEVAR'                         , 'BULEVAR'),
            ('BURACO'                          , 'BURACO'),
            ('CAIS'                            , 'CAIS'),
            ('CALCADA'                         , 'CALCADA'),
            ('CAMINHO'                         , 'CAMINHO'),
            ('CAMPO'                           , 'CAMPO'),
            ('CANAL'                           , 'CANAL'),
            ('CHACARA'                         , 'CHACARA'),
            ('CHAPADAO'                        , 'CHAPADAO'),
            ('CICLOVIA'                        , 'CICLOVIA'),
            ('CIRCULAR'                        , 'CIRCULAR'),
            ('COLONIA'                         , 'COLONIA'),
            ('COMPLEXO VIARIO'                 , 'COMPLEXO VIARIO'),
            ('COMUNIDADE'                      , 'COMUNIDADE'),
            ('CONDOMINIO'                      , 'CONDOMINIO'),
            ('CONJUNTO'                        , 'CONJUNTO'),
            ('CONJUNTO MUTIRAO'                , 'CONJUNTO MUTIRAO'),
            ('CONTORNO'                        , 'CONTORNO'),
            ('CORREDOR'                        , 'CORREDOR'),
            ('CORREGO'                         , 'CORREGO'),
            ('DESCIDA'                         , 'DESCIDA'),
            ('DESVIO'                          , 'DESVIO'),
            ('DISTRITO'                        , 'DISTRITO'),
            ('EIXO INDUSTRIAL'                 , 'EIXO INDUSTRIAL'),
            ('ELEVADA'                         , 'ELEVADA'),
            ('ENSEADA'                         , 'ENSEADA'),
            ('ENTRADA PARTICULAR'              , 'ENTRADA PARTICULAR'),
            ('ENTRE BLOCO'                     , 'ENTRE BLOCO'),
            ('ENTRE QUADRA'                    , 'ENTRE QUADRA'),
            ('ESCADA'                          , 'ESCADA'),
            ('ESCADARIA'                       , 'ESCADARIA'),
            ('ESPLANADA'                       , 'ESPLANADA'),
            ('ESTACAO'                         , 'ESTACAO'),
            ('ESTACIONAMENTO'                  , 'ESTACIONAMENTO'),
            ('ESTADIO'                         , 'ESTADIO'),
            ('ESTANCIA'                        , 'ESTANCIA'),
            ('ESTRADA'                         , 'ESTRADA'),
            ('ESTRADA ANTIGA'                  , 'ESTRADA ANTIGA'),
            ('ESTRADA DE LIGACAO'              , 'ESTRADA DE LIGACAO'),
            ('ESTRADA DE SERVIDAO'             , 'ESTRADA DE SERVIDAO'),
            ('ESTRADA ESTADUAL'                , 'ESTRADA ESTADUAL'),
            ('ESTRADA INTERMUNICIPAL'          , 'ESTRADA INTERMUNICIPAL'),
            ('ESTRADA MUNICIPAL'               , 'ESTRADA MUNICIPAL'),
            ('ESTRADA PARTICULAR'              , 'ESTRADA PARTICULAR'),
            ('ESTRADA VELHA'                   , 'ESTRADA VELHA'),
            ('ESTRADA VICINAL'                 , 'ESTRADA VICINAL'),
            ('EVANGELICA'                      , 'EVANGELICA'),
            ('FAVELA'                          , 'FAVELA'),
            ('FAZENDA'                         , 'FAZENDA'),
            ('FEIRA'                           , 'FEIRA'),
            ('FERROVIA'                        , 'FERROVIA'),
            ('FONTE'                           , 'FONTE'),
            ('FORTE'                           , 'FORTE'),
            ('GALERIA'                         , 'GALERIA'),
            ('GRANJA'                          , 'GRANJA'),
            ('ILHA'                            , 'ILHA'),
            ('ILHOTA'                          , 'ILHOTA'),
            ('INDETERMINADO'                   , 'INDETERMINADO'),
            ('JARDIM'                          , 'JARDIM'),
            ('JARDINETE'                       , 'JARDINETE'),
            ('LADEIRA'                         , 'LADEIRA'),
            ('LAGO'                            , 'LAGO'),
            ('LAGOA'                           , 'LAGOA'),
            ('LARGO'                           , 'LARGO'),
            ('LOTE'                            , 'LOTE'),
            ('LOTEAMENTO'                      , 'LOTEAMENTO'),
            ('MARGEM'                          , 'MARGEM'),
            ('MARINA'                          , 'MARINA'),
            ('MERCADO'                         , 'MERCADO'),
            ('MODULO'                          , 'MODULO'),
            ('MONTE'                           , 'MONTE'),
            ('MORRO'                           , 'MORRO'),
            ('NUCLEO'                          , 'NUCLEO'),
            ('NUCLEO HABITACIONAL'             , 'NUCLEO HABITACIONAL'),
            ('NUCLEO RURAL'                    , 'NUCLEO RURAL'),
            ('OUTEIRO'                         , 'OUTEIRO'),
            ('PARADA'                          , 'PARADA'),
            ('PARADOURO'                       , 'PARADOURO'),
            ('PARALELA'                        , 'PARALELA'),
            ('PARQUE'                          , 'PARQUE'),
            ('PARQUE MUNICIPAL'                , 'PARQUE MUNICIPAL'),
            ('PARQUE RESIDENCIAL'              , 'PARQUE RESIDENCIAL'),
            ('PASSAGEM'                        , 'PASSAGEM'),
            ('PASSAGEM DE PEDESTRE'            , 'PASSAGEM DE PEDESTRE'),
            ('PASSAGEM SUBTERRANEA'            , 'PASSAGEM SUBTERRANEA'),
            ('PASSARELA'                       , 'PASSARELA'),
            ('PASSEIO'                         , 'PASSEIO'),
            ('PATIO'                           , 'PATIO'),
            ('PONTA'                           , 'PONTA'),
            ('PONTE'                           , 'PONTE'),
            ('PORTO'                           , 'PORTO'),
            ('PRACA'                           , 'PRACA'),
            ('PRACA DE ESPORTES'               , 'PRACA DE ESPORTES'),
            ('PRAIA'                           , 'PRAIA'),
            ('PROJECAO'                        , 'PROJECAO'),
            ('PROLONGAMENTO'                   , 'PROLONGAMENTO'),
            ('QUADRA'                          , 'QUADRA'),
            ('QUINTA'                          , 'QUINTA'),
            ('QUINTAS'                         , 'QUINTAS'),
            ('RAMAL'                           , 'RAMAL'),
            ('RAMPA'                           , 'RAMPA'),
            ('RECANTO'                         , 'RECANTO'),
            ('RECREIO'                         , 'RECREIO'),
            ('RESIDENCIAL'                     , 'RESIDENCIAL'),
            ('RETA'                            , 'RETA'),
            ('RETIRO'                          , 'RETIRO'),
            ('RETORNO'                         , 'RETORNO'),
            ('RODO ANEL'                       , 'RODO ANEL'),
            ('RODOVIA'                         , 'RODOVIA'),
            ('ROTATORIA'                       , 'ROTATORIA'),
            ('ROTULA'                          , 'ROTULA'),
            ('RUA'                             , 'RUA'),
            ('RUA DE LIGACAO'                  , 'RUA DE LIGACAO'),
            ('RUA DE PEDESTRE'                 , 'RUA DE PEDESTRE'),
            ('RUA INTEGRACAO'                  , 'RUA INTEGRACAO'),
            ('RUA PARTICULAR'                  , 'RUA PARTICULAR'),
            ('RUA VELHA'                       , 'RUA VELHA'),
            ('RUELA'                           , 'RUELA'),
            ('SEGUNDA AVENIDA'                 , 'SEGUNDA AVENIDA'),
            ('SERVIDAO'                        , 'SERVIDAO'),
            ('SETOR'                           , 'SETOR'),
            ('SITIO'                           , 'SITIO'),
            ('SUBIDA'                          , 'SUBIDA'),
            ('TERMINAL'                        , 'TERMINAL'),
            ('TRAVESSA'                        , 'TRAVESSA'),
            ('TRAVESSA PARTICULAR'             , 'TRAVESSA PARTICULAR'),
            ('TRAVESSA VELHA'                  , 'TRAVESSA VELHA'),
            ('TRECHO'                          , 'TRECHO'),
            ('TREVO'                           , 'TREVO'),
            ('TRINCHEIRA'                      , 'TRINCHEIRA'),
            ('TUNEL'                           , 'TUNEL'),
            ('UNIDADE'                         , 'UNIDADE'),
            ('VALA'                            , 'VALA'),
            ('VALE'                            , 'VALE'),
            ('VARIANTE'                        , 'VARIANTE'),
            ('VEREDA'                          , 'VEREDA'),
            ('VIA'                             , 'VIA'),
            ('VIA COLETORA'                    , 'VIA COLETORA'),
            ('VIA COSTEIRA'                    , 'VIA COSTEIRA'),
            ('VIA DE ACESSO'                   , 'VIA DE ACESSO'),
            ('VIA DE PEDESTRE'                 , 'VIA DE PEDESTRE'),
            ('VIA ELEVADO'                     , 'VIA ELEVADO'),
            ('VIA EXPRESSA'                    , 'VIA EXPRESSA'),
            ('VIA LITORANEA'                   , 'VIA LITORANEA'),
            ('VIA LOCAL'                       , 'VIA LOCAL'),
            ('VIADUTO'                         , 'VIADUTO'),
            ('VIELA'                           , 'VIELA'),
            ('VILA'                            , 'VILA'),
            ('ZIGUE-ZAGUE'                     , 'ZIGUE-ZAGUE'),
        ]
    elif icodopti == 10131:         # Sentido
        lmselect = [('',''), ('I','IDA'),  ('V','VOLTA')]
    elif icodopti == 10132:         # Tipo de ponto
        lmselect = [('',''), ('O','OFICIAL'),  ('P','PASSAGEM'), ('I', 'INTERMEDIARIO')]
    elif icodopti == 10133:         # Tipo de viagem
        lmselect = [
            ('',''),
            ('1', 'OCIOSO'),        # => SAIDA E RETORNO DA GARAGEM
            ('2', 'PRODUTIVO'),     # => LEVA PASSAGEIROS
            ('3', 'RESERVADO'),     # => NAO LEVA PASSAGEIRO, UTILIZADO NOS PICOS ONDE A DEMANDA ESTA CONCENTRADA EM UMA DAS PONTAS DA LINHA
            ('4', 'DESLOCAMENTO'),  # => UM ONIBUS QUE FAZ MAIS DE UMA LINHA. ENCERRA NO PONTO X E DESLOCA PARA O Y PARA REALIZAR A OUTRA LINHA
        ]        
    elif icodopti == 10134:         # Encerramento de viagem
        lmselect = [
            ('N', 'NORMAL'),
            ('I', 'INTERVALO'),
            ('D', 'DUPLA PEGADA'),
            ('M', 'MULTILINHA'),
            ('T', 'INTERVALO + MULTILINHA'),
            ('A', 'ACERTO DE HORARIO'),
            ('C', 'ACERTO DE HORARIO + MULTILINHA'),
            ('E', 'DUPLA PAGADA + MULTILINHA')
        ]
    elif icodopti == 10201:         # Tipo de motor
        lmselect = [
            (0,''),
            (1,'DIANTEIRO'),
            (2,'TRASEIRO'),
        ]
    elif icodopti == 10202:         # Tipo de combustível
        lmselect = [
            (0,''),
            (1,'DIESEL'),
            (2,'GASOLINA'),
            (3,'ETANOL'),
            (4,'FLEX'),
            (5,'GNV'),
            (6,'ELETRICO'),
            (7,'HIBRIDO'),
        ]
    elif icodopti == 10401:         # Tipo de grupo de produtos e serviços
        lmselect = [('',''), ('P','PRODUTO'),  ('S','SERVIÇO')]
    elif icodopti == 10402:         # Unidade de estoque
        lmselect = [
            (0,''),
            (1,'UNIDADE'),
            (2,'PECA'),
            (3,'LITROS (ACEITA CASAS DECIMAIS)'),
            (4,'KILO (ACEITA CASAS DECIMAIS)'),
            (5,'METROS (ACEITA CASAS DECIMAIS)'),
            (6,'GALAO'),
            (7,'TAMBOR'),
            (8,'ROLO'),
            (9,'SERVICO'),
        ]
    elif icodopti == 10403:         # Tipo de pneu
        lmselect = [
            ('', 'NÃO É PNEU'),
            ('N','NOVO'),
            ('R','RESSOLADO'),
        ]
    elif icodopti == 10404:         # Tipo de movimentação
        lmselect = [
            ('', ''),
            ('E','ENTRADA'),
            ('S','SAÍDA'),
        ]
    elif icodopti == 10801:         # Tipo de grupo financeiro
        lmselect = [('',''), ('R','RECEITA'),  ('D','DESPESA')]
    elif icodopti == 10802:         # Tipo de registro financeiro
        lmselect = [('',''), ('P','PREVISTO'),  ('R','REALIZADO')]
    elif icodopti == 10803:         # Tipo de registro financeiro
        lmselect = [('P','PREVISTO'),  ('R','REALIZADO')]
    elif icodopti == 10804:         # Tipo de parcelamento
        lmselect = [
            (1,'SEMPRE NO MESMO DIA'),
            (2,'NAS DATAS INFORMADAS'),
            (3,'INTERVALO FIXO'),
            (4,'O MESMO DA PRIMEIRA PARCELA'),
            (5,'MESMA DATA DO DOCUMENTO'),
            (6,'ULTIMO DIA DO MES'),
        ]
    elif icodopti == 13001:         # Tipo de dia
        lmselect = [
            ('',''),
            ('U', 'UTIL'),
            ('S', 'SABADO'),
            ('D', 'DOMINGO'),
            ('F', 'FERIADO'),
            ('2', 'SEGUNDA-FEIRA'),
            ('3', 'TERCA-FEIRA'),
            ('4', 'QUARTA-FEIRA'),
            ('5', 'QUINTA-FEIRA'),
            ('6', 'SEXTA-FEIRA')
        ]
    elif icodopti == 13002:         # Status de retenção
        lmselect = [
            ('',''),
            ('1', '01 - PRESO'),
            ('2', '02 - RETIDO'),
            ('3', '03 - RETORNO DIARIO'),
            ('4', '04 - RETORNO NOTURNO'),
        ]
    elif icodopti == 13030:         # Entrada e saída de veículos: tipo de movimentação
        lmselect = [
            ('',''),
            ('E', 'ENTRADA'),
            ('S', 'SAIDA'),
            ('P', 'PONTO DE PASSAGEM'),
        ]
    return lmselect
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_personal_retorna_string ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que retorna uma string de resultados personalizados.                                                                                         // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_personal_retorna_string(icodopti, sdesccam):
    sdesccam = str(sdesccam)
    if   icodopti == 10001:         # Situação do registro
        if   sdesccam == 'A': sdesccam = 'ATIVO'
        elif sdesccam == 'I': sdesccam = 'INATIVO'
        elif sdesccam == 'C': sdesccam = 'CANCELADO'
        else:                 sdesccam = 'INDEFINIDO'
    elif icodopti == 10003:         # Sim/Não
        if   sdesccam == 'S': sdesccam = 'SIM'
        elif sdesccam == 'N': sdesccam = 'NÃO'
        else:                 sdesccam = 'INDEFINIDO'
    elif icodopti == 10131:         # Sentido
        if   sdesccam == 'I': sdesccam = 'IDA'
        elif sdesccam == 'V': sdesccam = 'VOLTA'
    elif icodopti == 10132:         # Tipo de ponto
        if   sdesccam == 'O': sdesccam = 'OFICIAL'
        elif sdesccam == 'P': sdesccam = 'PASSAGEM'
        elif sdesccam == 'I': sdesccam = 'INTERMEDIARIO'
    elif icodopti == 10133:         # Tipo de viagem
        if   sdesccam == '1': sdesccam = 'OCIOSO'           # => SAIDA E RETORNO DA GARAGEM
        elif sdesccam == '2': sdesccam = 'PRODUTIVO'        # => LEVA PASSAGEIROS
        elif sdesccam == '3': sdesccam = 'RESERVADO'        # => NAO LEVA PASSAGEIRO, UTILIZADO NOS PICOS ONDE A DEMANDA ESTA CONCENTRADA EM UMA DAS PONTAS DA LINHA
        elif sdesccam == '4': sdesccam = 'DESLOCAMENTO'     # => UM ONIBUS QUE FAZ MAIS DE UMA LINHA. ENCERRA NO PONTO X E DESLOCA PARA O Y PARA REALIZAR A OUTRA LINHA
    elif icodopti == 10134:         # Encerrarramento
        if   sdesccam == 'N': sdesccam = 'NORMAL'
        elif sdesccam == 'I': sdesccam = 'INTERVALO'
        elif sdesccam == 'D': sdesccam = 'DUPLA PEGADA'
        elif sdesccam == 'M': sdesccam = 'MULTILINHA'
        elif sdesccam == 'T': sdesccam = 'INTERVALO + MULTILINHA'
        elif sdesccam == 'A': sdesccam = 'ACERTO DE HORARIO'   
        elif sdesccam == 'C': sdesccam = 'ACERTO DE HORARIO + MULTILINHA'
        elif sdesccam == 'E': sdesccam = 'DUPLA PAGADA + MULTILINHA'
    elif icodopti == 10201:         # Tipo de motor        
        if   sdesccam == '1': sdesccam = 'DIANTEIRO'
        elif sdesccam == '2': sdesccam = 'TRASEIRO'
    elif icodopti == 10202:         # Tipo de combustível        
        if   sdesccam == '1': sdesccam = 'DIESEL'
        elif sdesccam == '2': sdesccam = 'GASOLINA'
        elif sdesccam == '3': sdesccam = 'ETANOL'
        elif sdesccam == '4': sdesccam = 'FLEX'
        elif sdesccam == '5': sdesccam = 'GNV'
        elif sdesccam == '6': sdesccam = 'ELETRICO'
        elif sdesccam == '7': sdesccam = 'HIBRIDO'
    elif icodopti == 10401:         # Tipo de registro
        if   sdesccam == 'P': sdesccam = 'PRODUTO'
        elif sdesccam == 'S': sdesccam = 'SERVICO'
        else:                 sdesccam = 'INDEFINIDO'
    elif icodopti == 10402:         # Unidade de estoque
        if   sdesccam == '0': sdesccam = ''
        elif sdesccam == '1': sdesccam = 'UNIDADE'
        elif sdesccam == '2': sdesccam = 'PECA'
        elif sdesccam == '3': sdesccam = 'LITROS'
        elif sdesccam == '4': sdesccam = 'KILO'
        elif sdesccam == '5': sdesccam = 'METROS'
        elif sdesccam == '6': sdesccam = 'GALAO'
        elif sdesccam == '7': sdesccam = 'TAMBOR'
        elif sdesccam == '8': sdesccam = 'ROLO'
        elif sdesccam == '9': sdesccam = 'SERVICO'
        else:                 sdesccam = 'INDEFINIDO'
    elif icodopti == 10404:         # Unidade de estoque
        if   sdesccam == 'E': sdesccam = 'ENTRADA'
        elif sdesccam == 'S': sdesccam = 'SAIDA'
        else:                 sdesccam = 'INDEFINIDO'
    elif icodopti == 10405:         # Tipo de registro de movimentação
        if   sdesccam == '1': sdesccam = 'NOTA FISCAL'
        elif sdesccam == '2': sdesccam = 'REQUISIÇÃO'
        elif sdesccam == '3': sdesccam = 'CONSUMO EM LOTE'        
        elif sdesccam == '4': sdesccam = 'ORDEM DE SERVIÇO'
        elif sdesccam == '5': sdesccam = 'INVENTÁRIO'
        else:                 sdesccam = 'INDEFINIDO'
    elif icodopti == 10801:         # Tipo de registro financeiro
        if   sdesccam == 'R': sdesccam = 'RECEITA'
        elif sdesccam == 'D': sdesccam = 'DESPESA'
        else:                 sdesccam = 'INDEFINIDO'
    elif icodopti == 13001:         # Tipo de dia
        if   sdesccam == 'U': sdesccam = 'UTIL'
        elif sdesccam == 'S': sdesccam = 'SABADO'
        elif sdesccam == 'D': sdesccam = 'DOMINGO'
        elif sdesccam == 'F': sdesccam = 'FERIADO'
        elif sdesccam == '2': sdesccam = 'SEGUNDA-FEIRA'
        elif sdesccam == '3': sdesccam = 'TERCA-FEIRA'
        elif sdesccam == '4': sdesccam = 'QUARTA-FEIRA'
        elif sdesccam == '5': sdesccam = 'QUINTA-FEIRA'
        elif sdesccam == '6': sdesccam = 'SEXTA-FEIRA'
    elif icodopti == 13002:         # Status de retenção
        if   sdesccam == '1': sdesccam = '01 - PRESO'
        elif sdesccam == '2': sdesccam = '02 - RETIDO'
        elif sdesccam == '3': sdesccam = '03 - RETORNO DIARIO'
        elif sdesccam == '4': sdesccam = '04 - RETORNO NOTURNO'
    elif icodopti == 13030:         # Entrada e saída de veículos: tipo de movimentação
        if   sdesccam == 'E': sdesccam = 'ENTRADA'
        elif sdesccam == 'S': sdesccam = 'SAIDA'
        elif sdesccam == 'P': sdesccam = 'PONTO DE PASSAGEM'
    return sdesccam
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_regras_datas ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de análise de regras entre datas.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    
def abnf_regras_datas(ddate001, ddate002, sdate001, sdate002, ldatepar, idifdmax, btenable):
    bvalidad = False                            # Variável de retorno da função
    ddatahoj = date.today()                     # Guarda a data de hoje
    if ddate001 and ddate002:   idifdats = (ddate001 - ddate002).days       # Diferença de dias entre as duas datas
    if ddate001:                idifhdt1 = (ddate001 - ddatahoj).days       # Diferença de dias entre a primeira data e a data de hoje
    if ddate002:                idifhdt2 = (ddate002 - ddatahoj).days       # Diferença de dias entre a segunda data e a data de hoje
    idifdtmp = idifdmax if idifdats >= 0 else idifdmax * (-1)
    if   ddate001 and not ddate002 and abnf_busca_item_em_lista('d1@@d2', ldatepar):                                                smesserr = 'A ' + sdate002 + ' tem que ser definida devido a existir a ' + sdate001 + '!'
    elif ddate002 and not ddate001 and abnf_busca_item_em_lista('d2@@d1', ldatepar):                                                smesserr = 'A ' + sdate001 + ' tem que ser definida devido a existir a ' + sdate002 + '!'
    elif ddate001 and ddate002 and abnf_busca_item_em_lista('d1<<d2', ldatepar) and not idifdats <  0:                              smesserr = 'A ' + sdate001 + ' tem que ser menor que a ' + sdate002 + '!'
    elif ddate001 and ddate002 and abnf_busca_item_em_lista('d1<=d2', ldatepar) and not idifdats <= 0:                              smesserr = 'A ' + sdate001 + ' tem que ser menor ou igual a ' + sdate002 + '!'
    elif ddate001 and ddate002 and abnf_busca_item_em_lista('d1==d2', ldatepar) and not idifdats == 0:                              smesserr = 'A ' + sdate001 + ' tem que ser igual a ' + sdate002 + '!'
    elif ddate001 and ddate002 and abnf_busca_item_em_lista('d1=>d2', ldatepar) and not idifdats >= 0:                              smesserr = 'A ' + sdate001 + ' tem que ser maior ou igual a ' + sdate002 + '!'
    elif ddate001 and ddate002 and abnf_busca_item_em_lista('d1>>d2', ldatepar) and not idifdats >  0:                              smesserr = 'A ' + sdate001 + ' tem que ser maior que a ' + sdate002 + '!'
    elif ddate001 and abnf_busca_item_em_lista('d1<<dh', ldatepar) and not idifhdt1 <  0:                                           smesserr = 'A ' + sdate001 + ' tem que ser menor que a data de hoje!'
    elif ddate001 and abnf_busca_item_em_lista('d1<=dh', ldatepar) and not idifhdt1 <= 0:                                           smesserr = 'A ' + sdate001 + ' tem que ser menor ou igual a data de hoje!'
    elif ddate001 and abnf_busca_item_em_lista('d1==dh', ldatepar) and not idifhdt1 == 0:                                           smesserr = 'A ' + sdate001 + ' tem que ser igual a data de hoje!'
    elif ddate001 and abnf_busca_item_em_lista('d1=>dh', ldatepar) and not idifhdt1 >= 0:                                           smesserr = 'A ' + sdate001 + ' tem que ser maior ou igual a data de hoje!'
    elif ddate001 and abnf_busca_item_em_lista('d1>>dh', ldatepar) and not idifhdt1 >  0:                                           smesserr = 'A ' + sdate001 + ' tem que ser maior que a data de hoje!'
    elif ddate002 and abnf_busca_item_em_lista('d2<<dh', ldatepar) and not idifhdt2 <  0:                                           smesserr = 'A ' + sdate002 + ' tem que ser menor que a data de hoje!'
    elif ddate002 and abnf_busca_item_em_lista('d2<=dh', ldatepar) and not idifhdt2 <= 0:                                           smesserr = 'A ' + sdate002 + ' tem que ser menor ou igual a data de hoje!'
    elif ddate002 and abnf_busca_item_em_lista('d2==dh', ldatepar) and not idifhdt2 == 0:                                           smesserr = 'A ' + sdate002 + ' tem que ser igual a data de hoje!'
    elif ddate002 and abnf_busca_item_em_lista('d2=>dh', ldatepar) and not idifhdt2 >= 0:                                           smesserr = 'A ' + sdate002 + ' tem que ser maior ou igual a data de hoje!'
    elif ddate002 and abnf_busca_item_em_lista('d2>>dh', ldatepar) and not idifhdt2 >  0:                                           smesserr = 'A ' + sdate002 + ' tem que ser maior que a data de hoje!'
    elif ddate001 and ddate002 and ddate001 != ddate002 and abnf_busca_item_em_lista('d1xad2', ldatepar) and idifdats <= idifdtmp:  smesserr = 'O máximo permitido entre a ' + sdate001 + ' e a ' + sdate002 + ' é de ' + str(idifdmax) + ' dia' + ('s' if idifdmax > 1 else '') + '!'
    else: bvalidad = True
    if not bvalidad: 
        abnf_alert(smesserr, 5)
        abnf_socket_004([5, btenable])
    return bvalidad 
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_busca_item_em_lista ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que busca uma string dentro de uma lista                                                                                                     // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_busca_item_em_lista(svalbusc, lauxi001):
    bvalidad = False
    for lauxi002 in lauxi001:
        if svalbusc == lauxi002: bvalidad = True
    return bvalidad
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_verifica_string_somente_numeros ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que valida uma string se ela tiver em seu conteúdo somente números.                                                                          // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_verifica_string_somente_numeros(sstrnume):
    bvalidad = True
    for sauxi001 in sstrnume:
        if not sauxi001 in '0123456789':
            bvalidad = False
    return bvalidad

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_verifica_numero_milhares_decimais ] /////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que valida digitação de valores com separador de milhares e casas decimais.                                                                  // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_verifica_numero_milhares_decimais(svalofin):
    sstructu = '';
    bvalidad = False
    itamvari = len(svalofin)
    for icontd01 in range(itamvari):
        sdignume = svalofin[icontd01]
        if ((sdignume == '0') or
            (sdignume == '1') or
            (sdignume == '2') or
            (sdignume == '3') or
            (sdignume == '4') or
            (sdignume == '5') or
            (sdignume == '6') or
            (sdignume == '7') or
            (sdignume == '8') or
            (sdignume == '9')): sstructu = sstructu + 'x'
        elif (sdignume == '-'): sstructu = sstructu + '-'
        elif (sdignume == '.'): sstructu = sstructu + '.'
        elif (sdignume == ','): sstructu = sstructu + ','
        else:                   sstructu = sstructu + 'y'
    lsvalido = [
              'x,x' ,           'x,xx' ,           'x,xxx' ,           'x,xxxx' ,           'x,xxxxx' ,           'x,xxxxxx' , 
             '-x,x' ,          '-x,xx' ,          '-x,xxx' ,          '-x,xxxx' ,          '-x,xxxxx' ,          '-x,xxxxxx' , 
             'xx,x' ,          'xx,xx' ,          'xx,xxx' ,          'xx,xxxx' ,          'xx,xxxxx' ,          'xx,xxxxxx' , 
            '-xx,x' ,         '-xx,xx' ,         '-xx,xxx' ,         '-xx,xxxx' ,         '-xx,xxxxx' ,         '-xx,xxxxxx' , 
            'xxx,x' ,         'xxx,xx' ,         'xxx,xxx' ,         'xxx,xxxx' ,         'xxx,xxxxx' ,         'xxx,xxxxxx' , 
           '-xxx,x' ,        '-xxx,xx' ,        '-xxx,xxx' ,        '-xxx,xxxx' ,        '-xxx,xxxxx' ,        '-xxx,xxxxxx' , 
          'x.xxx,x' ,       'x.xxx,xx' ,       'x.xxx,xxx' ,       'x.xxx,xxxx' ,       'x.xxx,xxxxx' ,       'x.xxx,xxxxxx' , 
         '-x.xxx,x' ,      '-x.xxx,xx' ,      '-x.xxx,xxx' ,      '-x.xxx,xxxx' ,      '-x.xxx,xxxxx' ,      '-x.xxx,xxxxxx' , 
         'xx.xxx,x' ,      'xx.xxx,xx' ,      'xx.xxx,xxx' ,      'xx.xxx,xxxx' ,      'xx.xxx,xxxxx' ,      'xx.xxx,xxxxxx' , 
        '-xx.xxx,x' ,     '-xx.xxx,xx' ,     '-xx.xxx,xxx' ,     '-xx.xxx,xxxx' ,     '-xx.xxx,xxxxx' ,     '-xx.xxx,xxxxxx' , 
        'xxx.xxx,x' ,     'xxx.xxx,xx' ,     'xxx.xxx,xxx' ,     'xxx.xxx,xxxx' ,     'xxx.xxx,xxxxx' ,     'xxx.xxx,xxxxxx' , 
       '-xxx.xxx,x' ,    '-xxx.xxx,xx' ,    '-xxx.xxx,xxx' ,    '-xxx.xxx,xxxx' ,    '-xxx.xxx,xxxxx' ,    '-xxx.xxx,xxxxxx' , 
      'x.xxx.xxx,x' ,   'x.xxx.xxx,xx' ,   'x.xxx.xxx,xxx' ,   'x.xxx.xxx,xxxx' ,   'x.xxx.xxx,xxxxx' ,   'x.xxx.xxx,xxxxxx' , 
     '-x.xxx.xxx,x' ,  '-x.xxx.xxx,xx' ,  '-x.xxx.xxx,xxx' ,  '-x.xxx.xxx,xxxx' ,  '-x.xxx.xxx,xxxxx' ,  '-x.xxx.xxx,xxxxxx' , 
     'xx.xxx.xxx,x' ,  'xx.xxx.xxx,xx' ,  'xx.xxx.xxx,xxx' ,  'xx.xxx.xxx,xxxx' ,  'xx.xxx.xxx,xxxxx' ,  'xx.xxx.xxx,xxxxxx' , 
    '-xx.xxx.xxx,x' , '-xx.xxx.xxx,xx' , '-xx.xxx.xxx,xxx' , '-xx.xxx.xxx,xxxx' , '-xx.xxx.xxx,xxxxx' , '-xx.xxx.xxx,xxxxxx' , 
    'xxx.xxx.xxx,x' , 'xxx.xxx.xxx,xx' , 'xxx.xxx.xxx,xxx' , 'xxx.xxx.xxx,xxxx' , 'xxx.xxx.xxx,xxxxx' , 'xxx.xxx.xxx,xxxxxx' ] 
    if sstructu in lsvalido:
        bvalidad = True
	# if ((substr($nvalofin,0,2) == '-0') and (substr($nvalofin,0,3) <> '-0,')) $numret = false;
	# if ((substr($nvalofin,0,1) ==  '0') and (substr($nvalofin,0,2) <>  '0,')) $numret = false;	
	# if ($nvalofin == '-0,00') $numret = false;
    return bvalidad

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_formata_numero_milhar_decimal ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que converte um numero no formato brasileiro com pontos separando milhares e vírgula separando decimal.                                      // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_formata_numero_milhar_decimal(snumerox, bsmilhar, iqtdecim):
    if bsmilhar:
        if iqtdecim == 0:
            snumerox = format(snumerox, ',').replace(',', '.')
        else:
            snumerox = f'{snumerox:,.{iqtdecim}f}'
            snumerox = snumerox.replace(',', '_').replace('.', ',').replace('_', '.')
    return snumerox
  
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_imprime_file ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de impressão em arquivo html/csv.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_imprime_file(iparamet, sabntoke):
    if   iparamet == 0: sfileext = '.htm'
    elif iparamet == 1: sfileext = '.csv'
    elif iparamet == 2: sfileext = '.txt'
    elif iparamet == 3: sfileext = '.png'
    return 'abnfprn' + sabntoke[:10] + datetime.now().strftime('%Y%m%d%H%M%S') + str(uuid.uuid4())[:10] + sfileext

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_imprime_converte_caracteres ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de impressão em arquivo html/csv.                                                                                                            // #
# // Essa função converte caracteres especiais de uma string para codificações padrões compreendidos pelo HTML.                                          // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_imprime_converte_caracteres(stextstr):
    ltabconv = [
        (' ', '&nbsp;'), # Alt+255 (caracter invisível) 
        ('ã', '&atilde;'),
        ('Ã', '&Atilde;'),
        ('á', '&aacute;'),
        ('à', '&agrave;'),
        ('Á', '&Aacute;'),
        ('â', '&acirc;'),
        ('Â', '&Acirc;'),
        ('é', '&eacute;'),
        ('É', '&Eacute;'),
        ('ê', '&ecirc;'),
        ('Ê', '&Ecirc;'),
        ('í', '&iacute;'),
        ('Í', '&Iacute;'),
        ('õ', '&otilde;'),
        ('Õ', '&Otilde;'),
        ('ó', '&oacute;'),
        ('Ó', '&Oacute;'),
        ('ô', '&ocirc;'),
        ('Ô', '&Ocirc;'),
        ('ú', '&uacute;'),
        ('Ú', '&Uacute;'),
        ('ç', '&ccedil;'),
        ('Ç', '&Ccedil;'),
        ('ñ', '&ntilde;'),
        ('Ñ', '&Ntilde;'),
        ('ª', '&ordf;'),
        ('º', '&ordm;'),
    ]
    stextret = ''
    for sauxi001 in stextstr:
        bencontr = False
        for lauxi001 in ltabconv:
            if sauxi001 in lauxi001[0]:
                stextret = stextret + lauxi001[1]
                bencontr = True
        if not bencontr:
            stextret = stextret + sauxi001
    return stextret
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_imprime_doctype_head_fhead_body_form_table_thead ] //////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de impressão em arquivo html/csv.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_imprime_doctype_head_fhead_body_form_table_thead(sarquwri, itabbord):
    sarquwri.write('<!DOCTYPE html>' + '\n')
    sarquwri.write('<html lang="pt">' + '\n')
    sarquwri.write('<head>' + '\n')
    sarquwri.write('    <title>Abeinfo</title>' + '\n')
    sarquwri.write('    <meta http-equiv="Content-Type" content = "text/html; charset=ISO-8859-1" >' + '\n')
    sarquwri.write('    <style type="text/css">' + '\n')
    sarquwri.write('        table' + '\n')
    sarquwri.write('        {' + '\n')
    sarquwri.write('            font-size:0.0em;' + '\n')
    sarquwri.write('            width:100%;' + '\n')
    sarquwri.write('            border-collapse:collapse;' + '\n')
    sarquwri.write('        }' + '\n')
    sarquwri.write('        td' + '\n')
    sarquwri.write('        {' + '\n')
    sarquwri.write('            padding-left: 5px;' + '\n')
    sarquwri.write('            padding-right: 5px;' + '\n')
    sarquwri.write('        }' + '\n')
    sarquwri.write('    </style>' + '\n')
    sarquwri.write('</head>' + '\n')
    sarquwri.write('<body>' + '\n')
    sarquwri.write('    <form>' + '\n')
    sarquwri.write('        <table border="' + str(itabbord) + '">' + '\n')
    sarquwri.write('            <thead>' + '\n')
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_imprime_thead_001_abeinfo_sistemas ] ////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de impressão em arquivo html/csv.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_imprime_thead_001_abeinfo_sistemas(sarquwri, icolspan):
    sarquwri.write('                <tr>' + '\n')
    sarquwri.write('                    <td colspan="' + str(icolspan) + '" align=center><font color=black FACE="Courier New" size=4><b>Abeinfo Sistemas de Informa&ccedil;&atilde;o</b></font></td>' + '\n')
    sarquwri.write('                </tr>' + '\n')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_imprime_thead_002_titulo_relatorio ] ////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de impressão em arquivo html/csv.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_imprime_thead_002_titulo_relatorio(sarquwri, icolspan, sauxi001):
    sarquwri.write('                <tr>' + '\n')
    sarquwri.write('                    <td colspan="' + str(icolspan) + '" align=center bgcolor=#E6DEE8><font color=black FACE="Courier New" size=4><b>' + abnf_imprime_converte_caracteres(sauxi001) + '</b></font></td>' + '\n')
    sarquwri.write('                </tr>' + '\n')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_imprime_thead_003_empresa_filial ] //////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de impressão em arquivo html/csv.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_imprime_thead_003_empresa_filial(sarquwri, icolspan, snomeemp, snomefil):
    sarquwri.write('                <tr>' + '\n')
    sarquwri.write('                    <td colspan="' + str(icolspan) + '" align=center>' + '\n')
    sarquwri.write('                        <font color=black FACE="Courier New" size=3><b>' + snomeemp + '</b></font>' + '\n')
    sarquwri.write('                        <font color=black FACE="Courier New" size=3><b>&nbsp;(' + snomefil + ')</b></font>' + '\n')
    sarquwri.write('                    </td>' + '\n')
    sarquwri.write('                </tr>' + '\n')
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_imprime_thead_004_parametros ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de impressão em arquivo html/csv.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_imprime_thead_004_parametros(sarquwri, icolspan, sauxi001):
    sarquwri.write('                <tr>' + '\n')
    sarquwri.write('                    <td colspan="' + str(icolspan) + '" align=center><font color=black FACE="Courier New" size=4><b>' + abnf_imprime_converte_caracteres(sauxi001) + '</b></font></td>' + '\n')
    sarquwri.write('                </tr>' + '\n')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_imprime_thead_005_datetime ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de impressão em arquivo html/csv.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_imprime_thead_005_datetime(sarquwri, icolspan):
    sarquwri.write('                <tr>' + '\n')
    sarquwri.write('                    <td colspan="' + str(icolspan) + '" align=center>' + '\n')
    sarquwri.write('                        <font color=black FACE="Courier New" size=3><b>Emiss&atilde;o: </b></font>' + '\n')
    sarquwri.write('                        <font color=black FACE="Courier New" size=3><b>[' + abnf_websocket_date_time(1) + ']</b></font>' + '\n')
    sarquwri.write('                    </td>' + '\n')
    sarquwri.write('                </tr>' + '\n')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_imprime_open_table ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de impressão em arquivo html/csv.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_imprime_open_table(sarquwri, itabbord):
    sarquwri.write('                <table border="' + str(itabbord) + '">' + '\n')
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_imprime_close_table ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de impressão em arquivo html/csv.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_imprime_close_table(sarquwri):
    sarquwri.write('                </table>' + '\n')
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_imprime_table_open_tr ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de impressão em arquivo html/csv.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_imprime_table_open_tr(sarquwri, sbgcolor, salignxx):
    sarquwri.write('                <tr')
    if sbgcolor: sarquwri.write(' bgcolor="' + sbgcolor + '"')
    if salignxx: sarquwri.write(' align="' + salignxx + '"')
    sarquwri.write('>' + '\n')
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_imprime_table_close_tr ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de impressão em arquivo html/csv.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_imprime_table_close_tr(sarquwri):
    sarquwri.write('                </tr>' + '\n')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_imprime_tr_open_td ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de impressão em arquivo html/csv.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_imprime_tr_open_td(sarquwri, sclasstr, icolspan, irowspan, sbgcolor, salignxx, svalignx):
    sarquwri.write('                <td')
    if sclasstr: sarquwri.write(' class="'   + sclasstr + '"')
    if icolspan: sarquwri.write(' colspan="' + str(icolspan) + '"')
    if icolspan: sarquwri.write(' rowspan="' + str(irowspan) + '"' )   
    if sbgcolor: sarquwri.write(' bgcolor="' + sbgcolor + '"')
    if salignxx: sarquwri.write(' align="'   + salignxx + '"')
    if svalignx: sarquwri.write(' valign="'  + svalignx + '"')
    sarquwri.write('>' + '\n')
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_imprime_tr_close_td ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de impressão em arquivo html/csv.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_imprime_tr_close_td(sarquwri):
    sarquwri.write('                </td>' + '\n')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_imprime_info_001 ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de impressão em arquivo html/csv.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_imprime_info_001(sarquwri, sbgcolor, salignxx, itipoinf, linfowri):
    if linfowri != None:
        sarquwri.write('                <tr')
        if sbgcolor: sarquwri.write(' bgcolor="' + sbgcolor + '"')
        if salignxx: sarquwri.write(' align="' + salignxx + '"')
        sarquwri.write('>' + '\n')
        for xauxilis in linfowri:
            if itipoinf == 1:       # Impressão de informações textuais
                # print(xauxilis[0], ' - ', type(xauxilis[0]))
                # if type(xauxilis[0]) == str:               
                if type(xauxilis[0]) in (list, tuple):      # Impressão com informações ocultas ("<a>")
                    stextprn = abnf_imprime_converte_caracteres(str(xauxilis[0][0]))
                    ssimbprn = str(xauxilis[0][1])
                else:    
                    stextprn = abnf_imprime_converte_caracteres(str(xauxilis[0]))             # Impressão sem informações
                    ssimbprn = None
                icolspan = xauxilis[1]
                irowspan = xauxilis[2]
                sbgcolor = xauxilis[3]
                salignxx = xauxilis[4]
                sfontcol = xauxilis[5]
                sfontdes = xauxilis[6]
                ifontlen = xauxilis[7]
                bbolding = xauxilis[8]
                bitalicx = xauxilis[9]
                bprefcel = xauxilis[10] if len(xauxilis) >= 11 else False
                sprefcin = '<pre>'  if bprefcel == True else ''
                sprefcfi = '</pre>' if bprefcel == True else ''
                sarquwri.write('                    <td')
                if (icolspan > 0): sarquwri.write(' colspan="' + str(icolspan) + '"')
                if (irowspan > 0): sarquwri.write(' rowspan="' + str(irowspan) + '"')
                if sbgcolor: sarquwri.write(' bgcolor="' + sbgcolor + '"')
                if salignxx: sarquwri.write(' align="' + salignxx + '"')
                # sarquwri.write('><font color=' + sfontcol + ' FACE="' + sfontdes + '" size=' + str(ifontlen) + '>')
                sarquwri.write('>' + sprefcin + '<font color=' + sfontcol + ' FACE="' + sfontdes + '" size=' + str(ifontlen) + '>')
                if bbolding: sarquwri.write('<b>')
                if bitalicx: sarquwri.write('<i>')
                if ssimbprn == None: sarquwri.write(stextprn)
                elif stextprn != '': sarquwri.write('<a arget="blank" title="' + stextprn + '">' + ssimbprn + '</a>')
                if bitalicx: sarquwri.write('</i>')
                if bbolding: sarquwri.write('</b>')
                # sarquwri.write('</font></td>' + '\n')
                sarquwri.write('</font>' + sprefcfi + '</td>' + '\n')
            elif itipoinf == 2:     # Não usado por enquanto  
                pass
            elif itipoinf == 3:     # Impressão de gráficos (canvas)
                stextprn = abnf_imprime_converte_caracteres(str(xauxilis[0]))
                stipdado = str(xauxilis[1])
                icolspan = xauxilis[2]
                irowspan = xauxilis[3]
                sbgcolor = xauxilis[4]
                salignxx = xauxilis[5]
                sfontcol = xauxilis[6]
                sfontdes = xauxilis[7]
                ifontlen = xauxilis[8]
                bbolding = xauxilis[9]
                bitalicx = xauxilis[10]
                sdivwipx = str(xauxilis[11])
                sdivhepx = str(xauxilis[12])
                scanwipo = str(xauxilis[13])
                scanhepo = str(xauxilis[14])
                sarquwri.write('                    <td')
                if (icolspan > 0): sarquwri.write(' colspan="' + str(icolspan) + '"')
                if (irowspan > 0): sarquwri.write(' rowspan="' + str(irowspan) + '"')
                if sbgcolor: sarquwri.write(' bgcolor="' + sbgcolor + '"')
                if salignxx: sarquwri.write(' align="' + salignxx + '"')
                if stipdado == 'N':         # Neutro
                    sarquwri.write('>')
                    sarquwri.write(stextprn)
                    sarquwri.write('</td>' + '\n')
                elif stipdado == 'T':       # Texto
                    sarquwri.write('><font color=' + sfontcol + ' FACE="' + sfontdes + '" size=' + str(ifontlen) + '>')
                    if bbolding: sarquwri.write('<b>')
                    if bitalicx: sarquwri.write('<i>')
                    sarquwri.write(stextprn)
                    if bitalicx: sarquwri.write('</i>')
                    if bbolding: sarquwri.write('</b>')
                    sarquwri.write('</font></td>' + '\n')
                elif stipdado == 'C':       # Canvas
                    sarquwri.write('><div id="AbnfGraph' + stextprn + '" style="width: ' + sdivwipx + 'px; height: ' + sdivhepx + 'px;">')
                    sarquwri.write('<canvas id="AbnfCanvas' + stextprn + '" width="' + scanwipo + '%" height="' + scanhepo + '%"></canvas>')
                    sarquwri.write('</div>')
                    sarquwri.write('</td>' + '\n')
        sarquwri.write('                </tr>' + '\n')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_imprime_fthead_tbody ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de impressão em arquivo html/csv.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_imprime_fthead_tbody(sarquwri):
    sarquwri.write('            </thead>' + '\n')
    sarquwri.write('            <tbody>' + '\n')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_imprime_ftbody_ftable_fform_fbody ] /////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de impressão em arquivo html/csv.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_imprime_ftbody_ftable_fform_fbody(sarquwri):
    sarquwri.write('            </tbody>' + '\n')
    sarquwri.write('        </table>' + '\n')
    sarquwri.write('    </form>' + '\n')
    sarquwri.write('</body>' + '\n')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_imprime_line ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de impressão em arquivo html/csv.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_imprime_line(sarquwri, icolspan, sbgcolor):
    sarquwri.write('                <tr><td colspan="' + str(icolspan) + '" bgcolor="' + sbgcolor + '"></td></tr>' + '\n')
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_matplotlib_gerar_grafico_002 ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de geração de gráfico com o Matplotlib.                                                                                                      // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_matplotlib_gerar_grafico_002(dgrafdat):
    import matplotlib.pyplot as oabnfmpl        # pip install matplotlib
    import numpy as oabnfnmp
    # import base64
    ofigurex, oaxesfig = oabnfmpl.subplots(figsize = (dgrafdat['figusize'][0], dgrafdat['figusize'][1]))        # Ajuste o tamanho da figura conforme necessário
    oaxesfig.set_title(dgrafdat['titletex'], fontsize = dgrafdat['titlefsi'])                                   # Título e ajuste o tamanho da fonte do título
    # Variaveis auto valoráveis quando não tem definição (início)
    if not 'explodex' in dgrafdat: dgrafdat['explodex'] = 0
    if not 'nstarang' in dgrafdat: dgrafdat['nstarang'] = 0
    # Variaveis auto valoráveis quando não tem definição (fim)
    if dgrafdat['chartype'] == 'bar01':
        lfatmult = oabnfnmp.arange(len(dgrafdat['datlabel'])) * dgrafdat['ifatmult'] # * 1.5                    # Ajuste o fator multiplicativo conforme necessário
        oaxesfig.set_xlabel(dgrafdat['labelxte'], fontsize = dgrafdat['labelxfs'])                              # Label - Eixo "X"
        oaxesfig.set_ylabel(dgrafdat['labelyte'], fontsize = dgrafdat['labelyfs'])                              # Label - Eixo "Y"
        oaxesfig.set_xticks(lfatmult)
        oaxesfig.set_xticklabels(dgrafdat['datlabel'], fontsize = dgrafdat['tickxlfo'], rotation = dgrafdat['tickxlro'], ha = dgrafdat['tickxlha']) # Rotação dos rótulos para melhor legibilidade
        obarlabe = oaxesfig.bar(lfatmult, dgrafdat['datvalue'], dgrafdat['nbarlarg'])
        oaxesfig.bar_label(obarlabe, fontsize = dgrafdat['axbarlfs'])
        oaxesfig.tick_params(axis = dgrafdat['axtickax'], labelsize = dgrafdat['axtickfl'])
        oabnfmpl.tight_layout()
    elif dgrafdat['chartype'] == 'pie01':
        iauxi001 = 0
        lrecipex = []
        lexplode = []
        for lauxi001 in dgrafdat['datlabel']:
            lrecipex.append(lauxi001 + ' (Qtd: ' + str(dgrafdat['datvalue'][iauxi001]) + ')')
            lexplode.append(dgrafdat['explodex'])
            iauxi001 += 1
        # Criando o gráfico e colocando a função da legenda interna			
        owedgesx, ltextsxx, lautotxt = oaxesfig.pie(dgrafdat['datvalue'], autopct = lambda iautopct: abnf_matplotlib_auxi001(iautopct, dgrafdat['datvalue'], oabnfnmp), textprops = dict(color = "black"), startangle = dgrafdat['nstarang'], explode = lexplode)
        # Definindo a caixa de legenda externa, título, localização e onde vai 'ancorar o box'
        oaxesfig.legend(owedgesx, lrecipex, loc = "center left", bbox_to_anchor = (1, 0, 0.5, 1))
        # Tamanho do texto de dentro do gráfico e o peso da fonte como bold
        oabnfmpl.setp(lautotxt, size = 8, weight = "bold")
    elif dgrafdat['chartype'] == 'pie02':
        iauxi001 = 0
        lrecipex = []
        lexplode = []
        for lauxi001 in dgrafdat['datlabel']:
            lrecipex.append(lauxi001 + ' (Qtd: ' + str(dgrafdat['datvalue'][iauxi001]) + ')')
            lexplode.append(dgrafdat['explodex'])
            iauxi001 += 1
        # Criando o gráfico e colocando a função da legenda interna
        owedgesx, ltextsxx, lautotxt = oaxesfig.pie(dgrafdat['datvalue'], autopct = lambda iautopct: abnf_matplotlib_auxi001(iautopct, dgrafdat['datvalue'], oabnfnmp), wedgeprops = dict(width = 1), startangle = dgrafdat['nstarang'], shadow = False, explode = lexplode)
        # Inserindo legandas laterais apontadas para cada pedaço da pizza do gráfico
        dbboxpro = dict(boxstyle = "square,pad=0.3", fc = "w", ec = "k", lw = 0.72)
        dkeyargs = dict(arrowprops = dict(arrowstyle = "-"), bbox = dbboxpro, zorder = 0, va = "center")
        for iowedges, lowedges in enumerate(owedgesx):
            nanglegr = (lowedges.theta2 - lowedges.theta1) / 2. + lowedges.theta1
            nycoordi = oabnfnmp.sin(oabnfnmp.deg2rad(nanglegr))
            nxcoordi = oabnfnmp.cos(oabnfnmp.deg2rad(nanglegr))
            dhoralig = {-1: "right", 1: "left"}[int(oabnfnmp.sign(nxcoordi))]
            scostyle = f"angle,angleA=0,angleB={nanglegr}"
            dkeyargs["arrowprops"].update({"connectionstyle": scostyle})
            oaxesfig.annotate(lrecipex[iowedges], xy = (nxcoordi, nycoordi), xytext = (1.35 * oabnfnmp.sign(nxcoordi), 1.4 * nycoordi), horizontalalignment = dhoralig, **dkeyargs)
        # Tamanho do texto de dentro do gráfico e o peso da fonte como bold
        oabnfmpl.setp(lautotxt, size = 12, weight = "bold")
    elif dgrafdat['chartype'] == 'line01':
        pass
    # Salvando arquivo:
    oabnfmpl.savefig(dgrafdat['sarqimag'])
    oabnfmpl.cla()
    oabnfmpl.close()
    return

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_converte_arquivo_imagem_base64 ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função auxiliar 01 para geração de gráfico com o Matplotlib.                                                                                        // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_matplotlib_auxi001(iautopct, ldtvalue, oabnfnmp):
    iabsolut = int(iautopct/100. * oabnfnmp.sum(ldtvalue))
    return "{:.1f}%".format(iautopct, iabsolut)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_converte_arquivo_imagem_base64 ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que converte arquivos de imagem em codificação binária 64.                                                                                   // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_converte_arquivo_imagem_base64(sarqimag, simgwidt, simgheig):
    import base64
    scodeimg = ''
    if os.path.exists(sarqimag):
        with open(sarqimag, "rb") as ofileimg:
            scodeimg = base64.b64encode(ofileimg.read()).decode('utf-8')
    scodeimg = '<img src="data:image/jpeg;base64,' + scodeimg + '" width="' + simgwidt + '" height="' + simgheig + '">'
    return scodeimg

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_echarts_gerar_grafico ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de geração de gráfico com o Apache ECharts                                                                                                   // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_echarts_gerar_grafico(dgrafdat):
    # Alexandre - 25/09/2025
    # Quando usamos "r" na frente das 3 aspas simples é devido a exisitir "\n" dentro do conteúdo assumido por "spagbod".
    # O "r" faz o que é chamado de "força bruta" fazendo o Python não interpretar o "\n" como uma quebra de página"
    # /////////////
    # Inicialização
    # /////////////
    spagbody = '''
    <script type="text/javascript">
    var chartDom = document.currentScript.parentElement;
    var AbnfGraph = echarts.init(chartDom);
    option = {
        title: [
            {
                text: ''' + '"' + dgrafdat['titletex'] + '"' + ''',
                left: 'center',     // Centraliza o cabeçalho horizontalmente
                top: '2%',          // Posiciona o cabeçalho a 2% da borda superior
                textStyle: {
                    fontSize: ''' + str(dgrafdat['titlefsi']) + ''',
                    // color: '#666'   // Cor mais suave
                }
                
            },
            {
                text: ''' + '"' + dgrafdat['footetex'] + '"' + ''',
                left: 'center',     // Centraliza o rodapé horizontalmente
                bottom: '0%',       // Posiciona o rodapé a 2% da borda inferior
                textStyle: {
                    fontSize: ''' + str(dgrafdat['footefsi']) + ''',
                    color: '#666'   // Cor mais suave
                }
            }
        ],
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        grid: {
            left: '1%',
            right: '4%',
            bottom: '10%',
            containLabel: true
        },
    '''
    if dgrafdat['chartype'] == 'pie01':
        sauxi001 = ''
        sauxi002 = ''
        for lauxi001 in sorted(dgrafdat['datvalue']):
            sauxi001 = sauxi001 + "'" + lauxi001[0] + "', "
            sauxi002 = sauxi002 + "{ value: " + str(lauxi001[1]) + ", name: '" + lauxi001[0] + "'}, "  
        # Debug: (inicio)
        # print(dgrafdat)
        # print(sauxi001)
        # print(sauxi002)
        # print(sauxi003)
        # Debug: (fim)
        spagbody = spagbody + '''
            legend: {
                data: [''' + sauxi001 + '''],
                bottom: '5%',           // Define a distância do fundo (ajuste o valor se necessário)
                left: 'center',         // Centraliza horizontalmente
                textStyle: {
                    fontSize: 16,
                    fontWeight: 'bold',
                },
                selected: {'''
        for lauxi001 in dgrafdat['selected']:
            spagbody = spagbody + '"' + str(lauxi001) + '": ' + (' true, ' if dgrafdat['selected'][lauxi001] == 1 else ' false, ')
        spagbody = spagbody + '''
                }
            },
            tooltip: {
                trigger: 'item',
                formatter: '{a} <br/>{b}: {c} ({d}%)'
            },
            series: [
                {
                    name: 'Abeinfo',
                    type: 'pie',
                    center: ''' + str(dgrafdat['grcenter']) + ''',
                    radius: ''' + str(dgrafdat['grradius']) + ''',
                    animationDuration: ''' + str(dgrafdat['animdura']) + ''',
                    itemStyle: {
                        borderRadius: 5,
                        borderColor: '#fff',
                        borderWidth: 2
                    },
                    labelLine: {
                        length: 30
                    },
                    label: {
                        formatter: '{hr|}''' + r'\n' + '''{b|{b}：}{c}  {per|{d}%}',
                        backgroundColor: '#F6F8FC',
                        borderColor: '#8C8D8E',
                        borderWidth: 1,
                        borderRadius: 4,
                        padding: [0, 5],
                        rich: {
                            a: {
                                color: '#6E7079',
                                lineHeight: 22,
                                align: 'center'
                            },
                            hr: {
                                borderColor: '#8C8D8E',
                                width: '100%',
                                borderWidth: 1,
                                height: 0
                            },
                            b: {
                                color: '#4C5058',
                                fontSize: 14,
                                fontWeight: 'bold',
                                lineHeight: 33
                            },
                            per: {
                                color: '#fff',
                                backgroundColor: '#4C5058',
                                padding: [3, 4],
                                borderRadius: 4
                            }
                        }
                    },
                    data: [''' + sauxi002 + ''']
                }
            ]
        };
        AbnfGraph.setOption(option);'''
    elif dgrafdat['chartype'] == 'line01':
        spagbody = spagbody + '''
            legend: {
                bottom: '5%',           // Define a distância do fundo (ajuste o valor se necessário)
                left: 'center',         // Centraliza horizontalmente
                icon: 'roundRect',      // Ícones com cantos arredodandos
                textStyle: {
                    fontSize: 16,
                    fontWeight: 'bold',
                },
                selected: {'''
        for lauxi001 in dgrafdat['selected']:
            spagbody = spagbody + '"' + str(lauxi001) + '": ' + (' true, ' if dgrafdat['selected'][lauxi001] == 1 else ' false, ')
        spagbody = spagbody + '''
                }
            },
            tooltip: {
                trigger: 'axis'
            },
            label: {
                show: true,             // Garante que o rótulo seja visível
                position: 'right',      // Coloca o rótulo à direita (na frente) da barra
                valueAnimation: true,   // Opcional: Adiciona animação ao valor, se o gráfico for dinâmico
                formatter: '{c}',       // O {c} é o placeholder que exibe o valor da série
            },
            xAxis: {
                type: 'category',
                boundaryGap: false,
                data: ''' + str(dgrafdat['parxaxis']) + '''
            },
            yAxis: {
                type: 'value',
                name: "''' + str(dgrafdat['paryaxis']) + '''",
                nameTextStyle: {
                    fontWeight: 'bold',
                }
            },
            animationDuration: ''' + str(dgrafdat['animdura']) + ''',
            series: ['''
        for lauxi001 in sorted(dgrafdat['datvalue']):
            spagbody = spagbody + '{name: "' + lauxi001[0] + '", type: "line", lineStyle: {width: 6}, data: ' + str(lauxi001[1]) + '},'
        spagbody = spagbody + '''
            ]
        };
        AbnfGraph.setOption(option);'''
    elif dgrafdat['chartype'] == 'barh01':
        spagbody = spagbody + '''
            legend: {
                bottom: '5%', 
                left: 'center' 
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },
            label: {
                show: true,             // Garante que o rótulo seja visível
                position: 'right',      // Coloca o rótulo à direita (na frente) da barra
                valueAnimation: true,   // Opcional: Adiciona animação ao valor, se o gráfico for dinâmico
                formatter: '{c}'        // O {c} é o placeholder que exibe o valor da série
            },
            xAxis: {
                type: 'value',
                boundaryGap: [0, 0.01]
            },
            yAxis: {
                type: 'category',
                data: ''' + str(dgrafdat['paryaxis']) + '''
            },
            series: ['''
        for lauxi001 in dgrafdat['datvalue']:
            spagbody = spagbody + '{name: "' + lauxi001[0] + '", type: "bar", data: ' + str(lauxi001[1]) + '},'
        spagbody = spagbody + '''
            ]
        };
        AbnfGraph.setOption(option);'''
    elif dgrafdat['chartype'] == 'barv01':
        spagbody = spagbody + '''
            legend: {
                bottom: '5%', 
                left: 'center' 
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },
            label: {
                show: true,             // Garante que o rótulo seja visível
                position: 'top',        // Coloca o rótulo no topo da barra
                valueAnimation: true,   // Opcional: Adiciona animação ao valor, se o gráfico for dinâmico
                formatter: '{c}'        // O {c} é o placeholder que exibe o valor da série
            },
            xAxis: [
                {
                    type: 'category',
                    data: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul']
                }
            ],
            yAxis: [
                {
                    type: 'value',
                    name: "''' + str(dgrafdat['paryaxis']) + '''",
                    nameTextStyle: {
                        fontWeight: 'bold',
                    }
                }
            ],
            series: ['''
        for lauxi001 in dgrafdat['datvalue']:
            spagbody = spagbody + '{name: "' + lauxi001[0] + '", type: "bar", data: ' + str(lauxi001[1]) + ', emphasis: {focus: "series"},'
            if   lauxi001[2] == 1: spagbody = spagbody + 'markLine: {lineStyle: { type: "dashed" }, data: [[{ type: "min", label: { show: false }}, { type: "max" }]]}'
            elif lauxi001[2] == 2: spagbody = spagbody + 'markLine: {lineStyle: { type: "dashed" }, data: [[{ type: "max", label: { show: false }}, { type: "min" }]]}'
            spagbody = spagbody + '},'
        spagbody = spagbody + '''
            ]
        };
        AbnfGraph.setOption(option);'''
    spagbody = spagbody + '</script>'
    return spagbody

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #