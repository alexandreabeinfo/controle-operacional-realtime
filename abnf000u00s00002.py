## ================================================
## [abnf000u00s00002.py] - Arquivo motor do sistema
## ================================================

from flask import Flask, render_template, redirect, url_for, request, abort, send_file, send_from_directory, session
from flask import Response                          # Biblioteca usada quando quiser retornar uma variável como página (return Response) no lugar do render_template (return render_template)
from flask_socketio import SocketIO                 # Biblioteca do Flask-SocketIO (Websockets)
from flask_bcrypt import Bcrypt                     # Biblioteca de criptografia
from abnfcfg import abnfcfg                         # Arquivo de configuração de ambiente

import os                                           # Para trabalhar com arquivos e diretorios do servidor
import shutil                                       # Biblioteca para manipular arquivos no servidor
import secrets                                      # Para gerar token de senha
import uuid                                         # Geração de token
import time                                         # Biblioteca do sleep

from abnfsrc.abnf000u00s00003 import *              # Arquivo de funções comuns que serão utilizadas por todos os módulos do sistema
from abnfsrc.abnf000u00s00004 import *              # Arquivo de banco de dados
from abnfsrc.abnf000u00s00005 import *              # Arquivo de elaboração de dashboards
from abnfsrc.abnf000u01c00100 import *              # Prontuário - Cadastro de Cidades                                                      (Padronização 001)
from abnfsrc.abnf000u01c00200 import *              # Prontuário - Cadastro de Bairros                                                      (Padronização 001)
from abnfsrc.abnf000u01c00300 import *              # Prontuário - Cadastro de Logradouros                                                  (Padronização 001)
from abnfsrc.abnf000u01c00400 import *              # Prontuário - Cadastro de CPF
from abnfsrc.abnf000u01c00500 import *              # Prontuário - Cadastro de CNPJ
from abnfsrc.abnf000u01c00600 import *              # Prontuário - Cadastro de Clientes e Fornecedores
from abnfsrc.abnf000u01c00700 import *              # Prontuário - Cadastro de Espécies de Documentos
from abnfsrc.abnf000u02c00100 import *              # Prontuário - Cadastro de Marcas de Veículos                                           (Padronização 003)
from abnfsrc.abnf000u02c00200 import *              # Prontuário - Cadastro de Modelos de Veículos                                          (Padronização 003)
from abnfsrc.abnf000u02c00300 import *              # Prontuário - Cadastro de Veículos                                                     (Padronização 003)
from abnfsrc.abnf000u03c00100 import *              # Prontuário - Cadastro de Cargos de Funcionários                                       (Padronização 003)
from abnfsrc.abnf000u03c00200 import *              # Prontuário - Cadastro de Funcionários                                                 (Padronização 002)
from abnfsrc.abnf000u04c00100 import *              # Almoxarifado - Cadastro de Grupos de Produtos e Serviços
from abnfsrc.abnf000u04c00200 import *              # Almoxarifado - Cadastro de Subgrupos de Produtos e Serviços
from abnfsrc.abnf000u04c00300 import *              # Almoxarifado - Cadastro de Marcas de Produtos e Serviços
from abnfsrc.abnf000u04c00400 import *              # Almoxarifado - Cadastro de Produtos e Serviços
from abnfsrc.abnf000u04c00500 import *              # Almoxarifado - Cadastro de Medidores de Produtos
from abnfsrc.abnf000u04m00100 import *              # Almoxarifado - Notas Fiscais
from abnfsrc.abnf000u04m00200 import *              # Almoxarifado - Requisições
from abnfsrc.abnf000u04m00300 import *              # Almoxarifado - Consumo em lote
from abnfsrc.abnf000u04m00500 import *              # Almoxarifado - Medidores de Produtos
from abnfsrc.abnf000u04m00600 import *              # Almoxarifado - Reabertura de Documentos
from abnfsrc.abnf000u04m00700 import *              # Almoxarifado - Alteração de Odômetros de Veículos
# from abnfsrc.abnf000u04m01000 import *            # Almoxarifado - Reabertura de Notas Fiscais
from abnfsrc.abnf000u04r00100 import *              # Almoxarifado - Relatório de Notas Fiscais
from abnfsrc.abnf000u04r00200 import *              # Almoxarifado - Relatório de Requisições
from abnfsrc.abnf000u04r00600 import *              # Almoxarifado - Relatório de Movimentação de Produtos e Serviços
from abnfsrc.abnf000u04r00700 import *              # Almoxarifado - Relatório de Consumo de Produtos e Serviços por Veículo
from abnfsrc.abnf000u04r00800 import *              # Almoxarifado - Medidores de Produtos
# from abnfsrc.abnf000u04r00900 import *              # Almoxarifado - Relatório Contábil de Estoque
from abnfsrc.abnf000u05c00100 import *              # Preventiva - Cadastro de Grupos
from abnfsrc.abnf000u05c00200 import *              # Preventiva - Cadastro de Ítens
from abnfsrc.abnf000u05c00300 import *              # Preventiva - Cadastro de Associação: Ítens x Grupos
from abnfsrc.abnf000u05c00400 import *              # Preventiva - Cadastro de Associação: Veículos x Grupos
from abnfsrc.abnf000u05m00100 import *              # Preventiva - Ação de Preventiva
from abnfsrc.abnf000u05r00100 import *              # Preventiva - Relatório de Preventivas
from abnfsrc.abnf000u08c00100 import *              # Financeiro - Cadastro de Contas Financeiras
from abnfsrc.abnf000u08c00200 import *              # Financeiro - Cadastro de Grupos
from abnfsrc.abnf000u08c00300 import *              # Financeiro - Cadastro de Subgrupos
from abnfsrc.abnf000u08c00400 import *              # Financeiro - Cadastro de Complementos
from abnfsrc.abnf000u08c00500 import *              # Financeiro - Cadastro de Centros de Custo
from abnfsrc.abnf000u08c00600 import *              # Financeiro - Cadastro de Departamentos
from abnfsrc.abnf000u08m00100 import *              # Financeiro - Registros Financeiros
from abnfsrc.abnf000u08m00400 import *              # Financeiro - Lançamento direto em conta
from abnfsrc.abnf000u08m00500 import *              # Financeiro - Alteração de filiais em registros financeiros
from abnfsrc.abnf000u08m00200 import *              # Financeiro - Conciliação Financeira
from abnfsrc.abnf000u08m00300 import *              # Financeiro - Transferência entre Contas
from abnfsrc.abnf000u08r00100 import *              # Financeiro - Relatório de Extrato de Contas
from abnfsrc.abnf000u08r00200 import *              # Financeiro - Relatório de Conta a Pagar e Receber
from abnfsrc.abnf000u10r00200 import *              # Elevar - Resumo de Km e Passageiros por Veículo
from abnfsrc.abnf000u11c00300 import *              # SAC - Cadastro de grupos de atendimentos
from abnfsrc.abnf000u11c00400 import *              # SAC - Cadastro de subgrupos de atendimentos
from abnfsrc.abnf000u11c00500 import *              # SAC - Cadastro de grupos de usuários
from abnfsrc.abnf000u11r00100 import *              # SAC - Visualização geral de atendimentos
from abnfsrc.abnf000u11r00200 import *              # SAC - Atendimentos aos Usuários
from abnfsrc.abnf000u12r00100 import *              # SIGOM - Visualização geral de ocorrências
from abnfsrc.abnf000u13c00100 import *              # Operacional - Cadastro de Locais                                                      (Padronização 001)
from abnfsrc.abnf000u13c00200 import *              # Operacional - Cadastro de Grupos de Linhas                                            (Padronização 001)
from abnfsrc.abnf000u13c00300 import *              # Operacional - Cadastro de Linhas                                                      (Padronização 001)
from abnfsrc.abnf000u13c00400 import *              # Operacional - Cadastro de Projetos                                                    (Padronização 001)
from abnfsrc.abnf000u13c00500 import *              # Operacional - Cadastro de Trajetos                                                    (Padronização 001)
from abnfsrc.abnf000u13c00600 import *              # Operacional - Cadastro de Itinerários                                                 (Padronização 001)
from abnfsrc.abnf000u13c00700 import *              # Operacional - Cadastro de Grupos de Veículos                                          (Padronização 001)
from abnfsrc.abnf000u13c00800 import *              # Operacional - Cadastro de Prioridades de Linhas                                       (Padronização 001)
from abnfsrc.abnf000u13c00900 import *              # Operacional - Cadastro de Operações Especiais                                         (Padronização 001)
from abnfsrc.abnf000u13m00100 import *              # Operacional - Propostas de OSO                                                        (Padronização 001)
from abnfsrc.abnf000u13m02100 import *              # Operacional - Controle Diário                                                         (Padronização 001)
from abnfsrc.abnf000u13m03000 import *              # Operacional - Entrada e Saída de Veículos                                             (Padronização 002)
from abnfsrc.abnf000u13r03000 import *              # Operacional - Relatório de Entrada e Saída de Veículos
from abnfsrc.abnf000u14m00100 import *              # Transdata - ITS Importação de dados                                                   (Padronização 001)
from abnfsrc.abnf000u14r00100 import *              # Transdata - ITS Análise                                                               (Padronização 001)
from abnfsrc.abnf000u14r00200 import *              # Transdata - ITS Horas trabalhadas de motoristas                                       (Padronização 001)

abnfxapp = Flask(__name__)                          # Declarando a aplicação
socketio = SocketIO(abnfxapp)                       # Iniciando o app em modo SocketIO
abnfbcry = Bcrypt(abnfxapp)                         # Criptografia do sistema usada na senha do usuário

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Padronização ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
'''
-----------------------------
Padronização 003 (2025-10-31)
1) Sem traço na observação
2) Traço antes da situação
3) Situação do registro no final
4) Utilização da função "abnf_database_registro_nao_ativo" para validar registros
5) Utilização da função "abnf_database_sqlx" para gerar listas ao invés de usar a função "abnf_database_menu"
6) Utilização da função "abnf_database_sqlx" para gerar relatórios ao invés de usar as funções "abnf_database_menu" e "abnf_database_busca_dados_v02"
-----------------------------
Padronização 002 (2025-10-22)
1) Sem traço na observação
2) Traço antes da situação
3) Situação do registro no final
4) Utilização da função "abnf_database_registro_nao_ativo" para validar registros
-----------------------------
Padronização 001 (2025-02-18)
1) Sem traço na observação
2) Traço antes da situação
3) Situação do registro no final
-----------------------------
'''
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

# clear ; find . -name "abnf000u*.py" -exec grep -iH "today" {} \; | grep -i "10"
# clear ; find . -name "abnf*.py" -exec grep -iH "'in'" {} \;  | grep -i "?????"
# clear ; find . -name "abnf*.py" -exec grep -iH "Null]" {} \;
# clear ; find . -name "abnf*.html" -exec grep -iH "A partir de agora" {} \;

# clear ; find . -name "abnf*.py" -exec grep -iH "'abnf_cadastro_veiculos'" {} \; | grep -i v02
# clear ; find . -name "abnf*.py" -exec grep -iH "], False)" {} \;

# =========> abnf_database_registro_nao_ativo
# clear ; find . -name "abnf*.py" -exec grep -iH "'descrição da cidade'" {} \; | grep -i '0201'

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_socket_001 ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que inicia o processo do Socket-IO para a empresa cliente.                                                                                   // #
# // Carrega a página principal HTML/CSS/JS com as bibliotecas necessárias para todo o sistema.                                                          // #
# // Não precisa do método GET/POST ==> , methods=['GET', 'POST']).                                                                                      // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

@abnfxapp.route('/treinamento_sistema')
def abnf_socket_001_treinamento_sistema():
    # exit()
    os.system('clear') or None
    slogosys = '''<a class="nav-link disabled" href="#" style="font-family: Segoe Script; font-size: 18px; font-weight: bold; font-style: italic; color:Red;">Flex Abeinfo<font style="font-family: Courier New; font-size: 18px; font-weight: bold; color: black"><b></i>&nbsp;2.0</b></font></a>'''
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_socket_001 (/treinamento_sistema)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    print('Iniciando o Socket-IO!')
    print('Gerando a página inicial!')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    sabnproj = '10000000000010000' # --- Treinamento Sistema
    print('Projeto .: ' + sabnproj + ' - Treinamento Sistema')
    spagehtm, sabntoke = abnf_gera_page_htm_websocket_project(sabnproj, slogosys)
    print('Token ...: ' + sabntoke)
    print('----------------------------------------------------------------------------------------------------------------------------------')
    # Registra o log:
    abnf_websocket_log(sabnproj[14:], 1, None, None, None, None, None, None, None)
    # Gera novo registro em dglobdws:
    abnf_websocket_control_globdws(sabnproj, sabntoke, [1, slogosys])
    return Response(spagehtm, mimetype="text/html")

@abnfxapp.route('/tupitransporte')
def abnf_socket_001_tupitransporte():
    # exit()
    os.system('clear') or None
    slogosys = '''<a class="nav-link disabled" href="#" style="font-family: Segoe Script; font-size: 18px; font-weight: bold; font-style: italic; color:Red;">Flex Abeinfo<font style="font-family: Courier New; font-size: 18px; font-weight: bold; color: black"><b></i>&nbsp;2.0</b></font></a>'''
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_socket_001 (/tupitransporte)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    print('Iniciando o Socket-IO!')
    print('Gerando a página inicial!')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    sabnproj = '12792863164510001' # --- Tupi Transporte
    print('Projeto .: ' + sabnproj + ' - Tupi Transporte')
    spagehtm, sabntoke = abnf_gera_page_htm_websocket_project(sabnproj, slogosys)
    print('Token ...: ' + sabntoke)
    print('----------------------------------------------------------------------------------------------------------------------------------')
    # Registra o log:
    abnf_websocket_log(sabnproj[14:], 1, None, None, None, None, None, None, None)
    # Gera novo registro em dglobdws:
    abnf_websocket_control_globdws(sabnproj, sabntoke, [1, slogosys])
    return Response(spagehtm, mimetype="text/html")
    
@abnfxapp.route('/rapidosumarepiracicaba')
def abnf_socket_001_rapidosumarepiracicaba():
    # exit()
    slogosys = '''<a class="nav-link disabled" href="#"><img src="data:image/jpeg;base64,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" class="rounded mx-auto d-block" width="150" height="35"></a>'''
    os.system('clear') or None
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_socket_001 (/rapidosumarepiracicaba)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    print('Iniciando o Socket-IO!')
    print('Gerando a página inicial!')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    sabnproj = '17646826035010002' # --- Rápido Sumaré Piracicaba
    print('Projeto .: ' + sabnproj + ' - Rápido Sumaré Piracicaba')
    spagehtm, sabntoke = abnf_gera_page_htm_websocket_project(sabnproj, slogosys)
    print('Token ...: ' + sabntoke)
    print('----------------------------------------------------------------------------------------------------------------------------------')
    # Registra o log:
    abnf_websocket_log(sabnproj[14:], 1, None, None, None, None, None, None, None)
    # Gera novo registro em dglobdws:
    abnf_websocket_control_globdws(sabnproj, sabntoke, [1, slogosys])
    return Response(spagehtm, mimetype="text/html")
    
@abnfxapp.route('/transacreana')
def abnf_socket_001_transacreana():
    # exit()
    slogosys = '''<a class="nav-link disabled" href="#" style="font-family: Segoe Script; font-size: 18px; font-weight: bold; font-style: italic; color:Red;">Flex Abeinfo<font style="font-family: Courier New; font-size: 18px; font-weight: bold; color: black"><b></i>&nbsp;2.0</b></font></a>'''
    os.system('clear') or None
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_socket_001 (/transacreana)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    print('Iniciando o Socket-IO!')
    print('Gerando a página inicial!')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    sabnproj = '15047354061710003' # --- Trans Acreana
    print('Projeto .: ' + sabnproj + ' - Trans Acreana')
    spagehtm, sabntoke = abnf_gera_page_htm_websocket_project(sabnproj, slogosys)
    print('Token ...: ' + sabntoke)
    print('----------------------------------------------------------------------------------------------------------------------------------')
    # Registra o log:
    abnf_websocket_log(sabnproj[14:], 1, None, None, None, None, None, None, None)
    # Gera novo registro em dglobdws:
    abnf_websocket_control_globdws(sabnproj, sabntoke, [1, slogosys])
    return Response(spagehtm, mimetype="text/html")

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ dashboard ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Essa função gera a página em formato de painel de Dashboard a qual fica se atualizando a cada X tempo.                                              // #
# // Programação RS: http://10.0.0.10:8005/dashboard?abnfempr=3&abnffili=1&abnfdash=C&abnfpara=X&abnfchav=JF8P6R2L&abnfulti=X                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #    

@abnfxapp.route('/dashboard', methods=['GET', 'POST'])
def abnf_dashboard():
    from flask import Response  # ==> Biblioteca usada quando quiser retornar uma variável como página (return Response) no lugar do render_template (return render_template)
    # http://10.0.0.10:8005/dashboard?d=e200p000s000
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('Dashboard')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad = False
    spage800 = ''
    if 'd' in request.args:
        sabnfdas = request.args['d']
        print('d: ', sabnfdas)
        if (len(sabnfdas) in (12, 13)
            and sabnfdas[0]  in 'Ee' # Empresa
            and sabnfdas[1]  in '0123456789'
            and sabnfdas[2]  in '0123456789'
            and sabnfdas[3]  in '0123456789'
            and sabnfdas[4]  in 'Pp' # Programação
            and sabnfdas[5]  in '0123456789'
            and sabnfdas[6]  in '0123456789'
            and sabnfdas[7]  in '0123456789'
            and sabnfdas[8]  in 'Ss' # Sequência
            and sabnfdas[9]  in '0123456789'
            and sabnfdas[10] in '0123456789'
            and sabnfdas[11] in '0123456789'):
            # # E000P000S000
            iempresa = int(sabnfdas[1:4])
            iprogram = int(sabnfdas[5:8])
            isequenc = int(sabnfdas[9:12])
            sretorno = '%' if len(sabnfdas) == 12 else sabnfdas[12]
            if iempresa > 0 and iprogram > 0 and isequenc > 0:
                bvalidad, irefresh, sdashtit, sabnfdas, spagbody = abnf000u00s00005_dashboards01(iempresa, iprogram, isequenc, sretorno)
            # Debug (início)
            # print('====================================')
            # print('bvalidad ...: ', bvalidad)
            # print('iempresa ...: ', iempresa)
            # print('iprogram ...: ', iprogram)
            # print('isequenc ...: ', isequenc)
            # print('irefresh ...: ', irefresh)
            # print('sdashtit ...: ', sdashtit)
            # print('sabnfdas ...: ', sabnfdas)
            # print('====================================')               
            # time.sleep(3)
            # Debug (fim)
    if bvalidad:
        # Metodos 01 de refresh
        # == (Método 01) ==> <script>
        # == (Método 01) ==>     const params = new URLSearchParams({
        # == (Método 01) ==>         d: "'''  + sabnfdas + '''",
        # == (Método 01) ==>     });        
        # == (Método 01) ==>     window.onload = function() {
        # == (Método 01) ==>         const interval = setInterval(() => {
        # == (Método 01) ==>             const url = new URL(window.location.href);
        # == (Método 01) ==>             url.search = params.toString();
        # == (Método 01) ==>             window.location.href = url.toString();
        # == (Método 01) ==>         }, ''' + str(irefresh) + '''000);
        # == (Método 01) ==>     };
        # == (Método 01) ==> </script>
        # Metodos 02 de refresh (com análise se o servidor esta ativo)
        # == (Método 02) ==> <script>
        # == (Método 02) ==>     const params = new URLSearchParams({
        # == (Método 02) ==>         d: "'''  + sabnfdas + '''",
        # == (Método 02) ==>     });
        # == (Método 02) ==>     const serverStatusCheckUrl = window.location.origin + '/dashboard'; // Altere conforme seu endpoint
        # == (Método 02) ==>     async function checkServerStatus() {
        # == (Método 02) ==>         try {
        # == (Método 02) ==>             const response = await fetch(serverStatusCheckUrl, { method: 'HEAD' }); // HEAD é mais leve
        # == (Método 02) ==>             if (response.ok) {
        # == (Método 02) ==>                 return true;
        # == (Método 02) ==>             } else {
        # == (Método 02) ==>                 console.warn(`Servidor respondeu com status ${response.status}.`);
        # == (Método 02) ==>                 return false;
        # == (Método 02) ==>             }
        # == (Método 02) ==>         } catch (error) {
        # == (Método 02) ==>             console.error('Erro ao verificar o status do servidor:', error);
        # == (Método 02) ==>             return false;
        # == (Método 02) ==>         }
        # == (Método 02) ==>     }
        # == (Método 02) ==>     window.onload = function() {
        # == (Método 02) ==>         const interval = setInterval(async () => {
        # == (Método 02) ==>             const serverIsActive = await checkServerStatus();
        # == (Método 02) ==>             if (serverIsActive) {
        # == (Método 02) ==>                 console.log('Servidor ativo, recarregando a página...');
        # == (Método 02) ==>                 const url = new URL(window.location.href);
        # == (Método 02) ==>                 url.search = params.toString();
        # == (Método 02) ==>                 window.location.href = url.toString();
        # == (Método 02) ==>             } else {
        # == (Método 02) ==>                 console.error('Servidor inativo ou inacessível. Recarregamento adiado.');
        # == (Método 02) ==>             }
        # == (Método 02) ==>         }, ''' + str(irefresh) + '''000);
        # == (Método 02) ==>     };
        # == (Método 02) ==> </script>
        # Metodos 03 de refresh (botão para pausar/reiniciar/retroceder/abançar e barra de progressão do tempo do dashboard)
        spagdash = '''
        <!DOCTYPE html>
        <html lang="pt">
        <head>
            <title>''' + sdashtit + '''</title>
            <meta http-equiv="Content-Type" content = "text/html; charset=ISO-8859-1" >
            <script src="https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js"></script>
            <style type="text/css">
                table
                {
                    font-size:0.0em;
                    width:100%;
                    border-collapse:collapse;
                }
                td
                {
                    padding-left: 5px;
                    padding-right: 5px;
                }
                .blinking-text {
                    animation: blinker 0.75s linear infinite;
                    color: brown;
                    font-weight: bold;
                }
                @keyframes blinker {
                    50% { opacity: 0; }
                }
                .error-text {
                    animation: blinker 0.75s linear infinite;
                    color: red; 
                    font-weight: bold;
                }                
            </style>
            <script>
                const REFRESH_TIME = ''' + str(irefresh) + '''000;
                const SERVER_CHECK_INTERVAL = 5000;
                const SERVER_URL_TO_CHECK = window.location.href.split('?')[0];
                const params = new URLSearchParams({
                    d: "'''  + sabnfdas + '''",
                });
                let reloadTimeout; 
                let isReloading = false; 
                let startTime;     
                let elapsedTime = 0; 
                let progressBarElement; 
                let statusMessageElement;
                function navigateToReload() {
                    const url = new URL(window.location.href);
                    url.search = params.toString();
                    window.location.href = url.toString(); 
                }
                async function checkServerAndReload() {
                    const checkUrl = SERVER_URL_TO_CHECK + "?check=true";
                    try {
                        const response = await fetch(checkUrl, { method: 'HEAD', cache: 'no-store' }); 
                        if (response.ok) {
                            elapsedTime = 0;
                            navigateToReload();
                        } else {
                            serverInactive(REFRESH_TIME); // Inicia nova tentativa após REFRESH_TIME
                        }
                    } catch (error) {
                        serverInactive(SERVER_CHECK_INTERVAL);
                    }
                }
                function serverInactive(timeToWait) {
                    clearTimeout(reloadTimeout); 
                    isReloading = true; 
                    const button = document.getElementById('playPauseButton');
                    if (statusMessageElement) {
                        statusMessageElement.classList.add('error-text');
                        statusMessageElement.innerText = "SERVIDOR INATIVO";
                    }
                    if (button) button.innerHTML = '&#9205;'; // Ícone de Pause
                    stopProgressBarAnimation();
                    reloadTimeout = setTimeout(() => {
                        checkServerAndReload(); 
                    }, timeToWait); 
                }
                function startCountdown(timeToWait) {
                    if (!isReloading) {
                        isReloading = true;
                        startTime = Date.now(); 
                        const button = document.getElementById('playPauseButton');
                        if (statusMessageElement) {
                            statusMessageElement.classList.remove('blinking-text'); 
                            statusMessageElement.classList.remove('error-text');
                        }
                        if (button) button.innerHTML = '&#9208;'; 
                        if (statusMessageElement) statusMessageElement.innerText = "ATIVO";
                        animateProgressBar(REFRESH_TIME, elapsedTime); 
                        reloadTimeout = setTimeout(() => {
                            checkServerAndReload();
                        }, timeToWait);
                    }
                }
                function pauseCountdown() {
                    if (isReloading) {
                        clearTimeout(reloadTimeout); 
                        isReloading = false;
                        elapsedTime += Date.now() - startTime; 
                        const button = document.getElementById('playPauseButton');
                        if (statusMessageElement) {
                            statusMessageElement.classList.add('blinking-text'); 
                            statusMessageElement.classList.remove('error-text');
                        }
                        if (button) button.innerHTML = '&#9205;'; 
                        if (statusMessageElement) statusMessageElement.innerText = "PAUSADO";
                        stopProgressBarAnimation(); 
                    }
                }
                function startReloading() {
                    elapsedTime = 0;
                    startCountdown(REFRESH_TIME); 
                }
                function stopReloading() {
                    pauseCountdown(); 
                }
                function animateProgressBar(totalTime, elapsed) {
                    if (!progressBarElement) {
                        progressBarElement = document.getElementById('progressBar');
                    }
                    if (!progressBarElement) return;
                    const timePassedInSeconds = elapsed / 1000;
                    progressBarElement.style.transition = `width ${totalTime / 1000}s linear`;
                    progressBarElement.style.transitionDelay = `-${timePassedInSeconds}s`; 
                    progressBarElement.style.width = '100%';
                }
                function stopProgressBarAnimation() {
                    if (!progressBarElement) {
                        progressBarElement = document.getElementById('progressBar');
                    }
                    if (!progressBarElement) return;
                    const currentWidthAtPause = (elapsedTime / REFRESH_TIME) * 100;
                    progressBarElement.style.transition = 'none';
                    progressBarElement.style.transitionDelay = '0s';
                    progressBarElement.style.width = `${currentWidthAtPause}%`; 
                }
                function handleRewindClick() {
                    let currentD = params.get('d');
                    let newD;
                    if (currentD && currentD.endsWith('*')) { 
                        newD = currentD.slice(0, -1);
                    } else {
                        newD = (currentD || "e200p099s001") + '*'; 
                    }
                    params.set('d', newD); 
                    navigateToReload(); 
                }
                function handleForwardClick() {
                    if (!isReloading) {
                        startReloading();
                    }
                    clearTimeout(reloadTimeout);
                    checkServerAndReload();
                }
                window.onload = function() {
                    const playPauseButton = document.getElementById('playPauseButton');
                    const forwardButton = document.getElementById('forwardButton');
                    const rewindButton = document.getElementById('rewindButton'); 
                    progressBarElement = document.getElementById('progressBar');
                    statusMessageElement = document.getElementById('statusMessage'); 
                    startReloading();
                    if (playPauseButton) {
                        playPauseButton.addEventListener('click', () => {
                            if (isReloading) {
                                pauseCountdown(); 
                            } else {
                                const timeRemaining = REFRESH_TIME - elapsedTime;
                                if (timeRemaining > 0) {
                                    startCountdown(timeRemaining); 
                                } else {
                                    checkServerAndReload();
                                }
                            }
                        });
                    }
                    if (forwardButton) {
                        forwardButton.addEventListener('click', handleForwardClick);
                    }
                    if (rewindButton) {
                        rewindButton.addEventListener('click', handleRewindClick);
                    }
                    slideshowContainer = document.getElementById('slideshow-container');
                    slides = document.querySelectorAll('.slide-content');
                    if (slides.length > 1 && slideshowTimeout === undefined) {
                        slideshowTimeout = setTimeout(showSlides, SLIDE_DURATION);
                    }
                    const slideshowWrapper = document.getElementById('slideshow-wrapper'); 
                    if (slideshowWrapper) {
                        slideshowWrapper.addEventListener('mouseenter', () => {
                            pauseSlideshow();
                        });
                        slideshowWrapper.addEventListener('mouseleave', () => {
                            resumeSlideshow();
                        });
                    }
                };
            </script>
        </head>
        <body>'''
        spagdash = spagdash + spagbody + '\n' +'        </body>'
    else:
        spagdash = ''
    return Response(spagdash, mimetype="text/html")

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ handle_404 ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // A função abaixo foi me fornecida pelo Gemini em 14/07/2024 para dar o entendimento quando o endereço do aplicativo for digitado incorretamente.     // #
# // Isso para enganar os robôs hackers que ficam tentando vários endereços diferentes para ver se o servidor responde.                                  // #
# // Essa função retorna uma resposta personalizada sem renderizar um modelo ou mensagem de erro.                                                        // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

@abnfxapp.errorhandler(404)
def handle_404(error):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('handle_404(error)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    print('Endereço digitado incorretamente!')
    print('Retornando erro 404!')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    # exit()
    return '', 404
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_socket_001_index ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // A função abaixo retorna o texto "Index" quando não tiver nenhuma complementação no endereço do aplicativo ("/").                                    // #
# // Até que o endereço raiz ("/") seja utilizado, foi deixado a função exit() para não dar nenhuma resposta a quem solicitar dessa forma.               // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #    
    
@abnfxapp.route('/')
def abnf_socket_001_index():
    exit()
    spagehtm = 'Index'
    return Response(spagehtm, mimetype="text/html")
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_user_files ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que cria link para arquivos de usuário baseado no código do projeto.                                                                         // #
# // Exemplos de uso:                                                                                                                                    // #
# // http://10.0.0.10:8005/arquivos/15047354061710003/abnfuser000000001.jpg                                                                              // #
# // http://10.0.0.10:8005/arquivos/15047354061710003/abnfuser000000041-07dc0fa5-fe60-406a-b269-8d983c.pdf                                               // #
# // Instruções de links dentro do sistema:                                                                                                              // #
# // <a href="imagem.jpg" download="minha_imagem.jpg">Download da Imagem</a>                                                                             // #
# // href="imagem.jpg": Indica o caminho para o arquivo JPG a ser baixado.                                                                               // #
# // download="minha_imagem.jpg": Define o nome do arquivo que será salvo no dispositivo do usuário. Pode usar um nome diferente do original se quiser.  // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #      
    
@abnfxapp.route('/arquivos/<sabnproj>/<sarquivo>')
def abnf_user_files(sabnproj, sarquivo):
    sldocpro = abnf_websocket_local_docs(sabnproj)
    if sldocpro == None:
        return '', 404
    else:
        return send_from_directory(abnfcfg.sdirsyst + sldocpro, sarquivo)
        # ==> idefflex = 0
        # ==> if   idefflex == 0: return send_from_directory('/flexabeinfo/' + sldocpro, sarquivo)
        # ==> elif idefflex == 1: return send_from_directory('/flexgb/' + sldocpro, sarquivo)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_socket_002 ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que será executada quando um cliente se conectar ao servidor.                                                                                // #
# // Apesar de poder dar qualquer nome o def (ex: abnf_socket_002), o que esta em @socketio.on tem que ser 'connect'.                                    // #
# // Tentei alterar 'connect' na função abaixo e no código JS dentro do HTML mas ele não funciona.                                                       // #
# // O gemini confirma que esse conteúdo pode ser alterado, mas fiz vários testes e não funcionou, então tive que manter 'connect' mesmo.                // #
# // A existência dessa função não é obrigatória.                                                                                                        // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

# @socketio.on('connect')
# def abnf_socket_002():
#     print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
#     print('==================================================================================================================================')
#     print('abnf_socket_002 (connect)')
#     print('----------------------------------------------------------------------------------------------------------------------------------')
#     print('Cliente conectado!')
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_socket_003 ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que recebe informações via JS através da função 'AbnfSubmitForm' da página principal HTML/CSS/JS.                                            // #
# // Esta função recebe informações de todos os campos da página e também seus respetivos valores atuais.                                                // #
# // Estas informações vem através de um dicionário chamado 'dabnfopg'.                                                                                  // #
# // Os valores são tratados e, logo após, enviado ações em JS de volta para a pagina através da função abnf_socket_004.                                 // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    
@socketio.on('abnf_socket_003')
def abnf_socket_003(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_socket_003 (AbnfSubmitForm)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    print(dabnfopg)
    print('----------------------------------------------------------------------------------------------------------------------------------')
    for lauxi001 in dabnfopg:
        print(lauxi001, ' - ', dabnfopg[lauxi001])
    print('----------------------------------------------------------------------------------------------------------------------------------')
    # time.sleep(10)
    # Enviar as informações recebidas para tratamento
    abnf_tratamento_websockets_recebidos(dabnfopg)
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_tratamento_websockets_recebidos ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que trata as informações recebidas via websocket pela função 'abnf_socket_003'.                                                              // #
# // Essa função que vai chamar as demais conforme websocket pela função 'abnf_socket_003'.                                                              // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #    
    
def abnf_tratamento_websockets_recebidos(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_tratamento_websockets_recebidos(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Vamos procurar "sabnfsys" em dois dicionários distintos de forma sequencial.
        # O primeiro é no dicionário "dabnfopg".
        # Caso ele for encontrado nesse dicionário é porque um ítem de menu foi selecionado.
        # Então vamos atualizar o nome do módulo selecionado dentro do dicionário global "dglobdws" no campo "sabnfsys".
        sabnfsys = dabnfopg.get('sabnfsys', None)
        if sabnfsys != None:
            # ****************
            # Nota: 05/07/2024
            # Apesar de "abnf_websocket_control_globdws(sabnproj, sabntoke, [3" servir para inserir um dado dentro do dicionário "dglobdws",
            # ele também vai retornar o dicionário caso necesssário, assim evita ter que usar "abnf_websocket_control_globdws(sabnproj, sabntoke, [2"
            # para recuperar o dicionário logo após sua atualização.
            # ****************
            dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (
                ('sabnfsys', sabnfsys),      # Módulo selecionado no menu
            )])
            print('dabnfopg: ', dabnfopg)
            print('----------------------------------------------------------------------------------------------------------------------------------')
            # dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        else:
            # Se entrou aqui é porque chegou nesse ponto através de um botão de uma tela do sistema e não por um menu.
            # Então "sabnfsys" será buscado dentro do dicionário "dglobdws" através do dicionário auxiliar "dglobaux".
            dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
            sabnfsys = dglobaux.get('sabnfsys', None)
            print('dglobaux: ', dglobaux)
            print('----------------------------------------------------------------------------------------------------------------------------------')
        print('sabnfsys: ', sabnfsys)
        print('----------------------------------------------------------------------------------------------------------------------------------')
        abnf_alert(0, 0)
        # Quanto tiver tupla: Ação 01: Atualiza dados em dglobdws para direcionar para a próxima etapa / Ação 02: Chama o módulo sequêncial (Obs: não remover a virgula)
        labnfmod = ([
            ['00S00201A' , 'Login'       , 'abnf000u00s00201_login_sistema(dabnfopg)'                                                   , None],
            ['00S00300A' , 'Free'        , 'abnf000u00s00300_definicao_empresa_filial(dabnfopg)'                                        , 'a definicao de empresa/filial'],
            ['00S00301A' , 'Filial'      , 'abnf000u00s00301_definicao_empresa_filial(dabnfopg)'                                        , None],
            ['00S00400A' , 'Free'        , 'abnf000u00s00400_perfil(dabnfopg)'                                                          , 'o perfil'],
            ['00S00401A' , 'Free'        , 'abnf000u00s00401_perfil(dabnfopg)'                                                          , None],
            ['00S00402A' , 'Free'        , 'abnf000u00s00402_perfil(dabnfopg)'                                                          , None],
            ['01C00100A' , '01C00100A'   , 'abnf000u01c00100_cadastro_cidades(dabnfopg)'                                                , 'o modulo de cadastro de cidades'],
            ['01C00101A' , '01C00100A'   , 'abnf000u01c00101_cadastro_cidades(dabnfopg)'                                                , None],
            ['01C00102A' , '01C00100A'   , 'abnf000u01c00102_cadastro_cidades(dabnfopg)'                                                , None],
            ['01C00200A' , '01C00200A'   , 'abnf000u01c00200_cadastro_bairros(dabnfopg)'                                                , 'o modulo de cadastro de bairros'],
            ['01C00201A' , '01C00200A'   , 'abnf000u01c00201_cadastro_bairros(dabnfopg)'                                                , None],
            ['01C00202A' , '01C00200A'   , 'abnf000u01c00202_cadastro_bairros(dabnfopg)'                                                , None],
            ['01C00300A' , '01C00300A'   , 'abnf000u01c00300_cadastro_logradouros(dabnfopg)'                                            , 'o modulo de cadastro de logradouros'],
            ['01C00301A' , '01C00300A'   , 'abnf000u01c00301_cadastro_logradouros(dabnfopg)'                                            , None],
            ['01C00302A' , '01C00300A'   , 'abnf000u01c00302_cadastro_logradouros(dabnfopg)'                                            , None],
            ['01C00400A' , '01C00400A'   , 'abnf000u01c00400_cadastro_cpf(dabnfopg)'                                                    , 'o modulo de cadastro de CPF'],
            ['01C00401A' , '01C00400A'   , 'abnf000u01c00401_cadastro_cpf(dabnfopg)'                                                    , None],
            ['01C00402A' , '01C00400A'   , 'abnf000u01c00402_cadastro_cpf(dabnfopg)'                                                    , None],
            ['01C00500A' , '01C00500A'   , 'abnf000u01c00500_cadastro_cnpj(dabnfopg)'                                                   , 'o modulo de cadastro de CNPJ'],
            ['01C00501A' , '01C00500A'   , 'abnf000u01c00501_cadastro_cnpj(dabnfopg)'                                                   , None],
            ['01C00502A' , '01C00500A'   , 'abnf000u01c00502_cadastro_cnpj(dabnfopg)'                                                   , None],
            ['01C00600A' , '01C00600A'   , 'abnf000u01c00600_cadastro_clientes_fornecedores(dabnfopg)'                                  , 'o modulo de cadastro de clientes'],
            ['01C00601A' , '01C00600A'   , 'abnf000u01c00601_cadastro_clientes_fornecedores(dabnfopg)'                                  , None],
            ['01C00602A' , '01C00600A'   , 'abnf000u01c00602_cadastro_clientes_fornecedores(dabnfopg)'                                  , None],
            ['01C00600B' , '01C00600B'   , 'abnf000u01c00600_cadastro_clientes_fornecedores(dabnfopg)'                                  , 'o modulo de cadastro de fornecedores'],
            ['01C00601B' , '01C00600B'   , 'abnf000u01c00601_cadastro_clientes_fornecedores(dabnfopg)'                                  , None],
            ['01C00602B' , '01C00600B'   , 'abnf000u01c00602_cadastro_clientes_fornecedores(dabnfopg)'                                  , None],
            ['01C00700A' , '01C00700A'   , 'abnf000u01c00700_cadastro_especies_documentos(dabnfopg)'                                    , 'o modulo de cadastro de especies de documentos'],
            ['01C00701A' , '01C00700A'   , 'abnf000u01c00701_cadastro_especies_documentos(dabnfopg)'                                    , None],
            ['01C00702A' , '01C00700A'   , 'abnf000u01c00702_cadastro_especies_documentos(dabnfopg)'                                    , None],
            ['02C00100A' , '02C00100A'   , 'abnf000u02c00100_cadastro_veiculos_marcas(dabnfopg)'                                        , 'o modulo de cadastro de marcas de veiculos'],
            ['02C00101A' , '02C00100A'   , 'abnf000u02c00101_cadastro_veiculos_marcas(dabnfopg)'                                        , None],
            ['02C00102A' , '02C00100A'   , 'abnf000u02c00102_cadastro_veiculos_marcas(dabnfopg)'                                        , None],
            ['02C00200A' , '02C00200A'   , 'abnf000u02c00200_cadastro_veiculos_modelos(dabnfopg)'                                       , 'o modulo de cadastro de modelos de veiculos'],
            ['02C00201A' , '02C00200A'   , 'abnf000u02c00201_cadastro_veiculos_modelos(dabnfopg)'                                       , None],
            ['02C00202A' , '02C00200A'   , 'abnf000u02c00202_cadastro_veiculos_modelos(dabnfopg)'                                       , None],
            ['02C00300A' , '02C00300A'   , 'abnf000u02c00300_cadastro_veiculos(dabnfopg)'                                               , 'o modulo de cadastro de veiculos'],
            ['02C00301A' , '02C00300A'   , 'abnf000u02c00301_cadastro_veiculos(dabnfopg)'                                               , None],
            ['02C00302A' , '02C00300A'   , 'abnf000u02c00302_cadastro_veiculos(dabnfopg)'                                               , None],
            ['03C00100A' , '03C00100A'   , 'abnf000u03c00100_cadastro_funcionarios_cargos(dabnfopg)'                                    , 'o modulo de cadastro de cargos de funcionarios'],
            ['03C00101A' , '03C00100A'   , 'abnf000u03c00101_cadastro_funcionarios_cargos(dabnfopg)'                                    , None],
            ['03C00102A' , '03C00100A'   , 'abnf000u03c00102_cadastro_funcionarios_cargos(dabnfopg)'                                    , None],
            ['03C00200A' , '03C00200A'   , 'abnf000u03c00200_cadastro_funcionarios(dabnfopg)'                                           , 'o modulo de cadastro de cargos de funcionarios'],
            ['03C00201A' , '03C00200A'   , 'abnf000u03c00201_cadastro_funcionarios(dabnfopg)'                                           , None],
            ['03C00202A' , '03C00200A'   , 'abnf000u03c00202_cadastro_funcionarios(dabnfopg)'                                           , None],
            ['04C00100A' , '04C00100A'   , 'abnf000u04c00100_almoxarifado_cadastro_produtos_servicos_grupos(dabnfopg)'                  , 'o modulo de cadastro de grupos de produtos e servicos'],
            ['04C00101A' , '04C00100A'   , 'abnf000u04c00101_almoxarifado_cadastro_produtos_servicos_grupos(dabnfopg)'                  , None],
            ['04C00102A' , '04C00100A'   , 'abnf000u04c00102_almoxarifado_cadastro_produtos_servicos_grupos(dabnfopg)'                  , None],
            ['04C00200A' , '04C00200A'   , 'abnf000u04c00200_almoxarifado_cadastro_produtos_servicos_subgrupos(dabnfopg)'               , 'o modulo de cadastro de subgrupos de produtos e servicos'],
            ['04C00201A' , '04C00200A'   , 'abnf000u04c00201_almoxarifado_cadastro_produtos_servicos_subgrupos(dabnfopg)'               , None],
            ['04C00202A' , '04C00200A'   , 'abnf000u04c00202_almoxarifado_cadastro_produtos_servicos_subgrupos(dabnfopg)'               , None],
            ['04C00300A' , '04C00300A'   , 'abnf000u04c00300_almoxarifado_cadastro_produtos_servicos_marcas(dabnfopg)'                  , 'o modulo de cadastro de marcas de produtos e servicos'],
            ['04C00301A' , '04C00300A'   , 'abnf000u04c00301_almoxarifado_cadastro_produtos_servicos_marcas(dabnfopg)'                  , None],
            ['04C00302A' , '04C00300A'   , 'abnf000u04c00302_almoxarifado_cadastro_produtos_servicos_marcas(dabnfopg)'                  , None],
            ['04C00400A' , '04C00400A'   , 'abnf000u04c00400_almoxarifado_cadastro_produtos_servicos(dabnfopg)'                         , 'o modulo de cadastro de produtos e servicos'],
            ['04C00401A' , '04C00400A'   , 'abnf000u04c00401_almoxarifado_cadastro_produtos_servicos(dabnfopg)'                         , None],
            ['04C00402A' , '04C00400A'   , 'abnf000u04c00402_almoxarifado_cadastro_produtos_servicos(dabnfopg)'                         , None],
            ['04C00500A' , '04C00500A'   , 'abnf000u04c00500_almoxarifado_cadastro_medidores_produtos(dabnfopg)'                        , 'o modulo de cadastro de medidores de produtos'],
            ['04C00501A' , '04C00500A'   , 'abnf000u04c00501_almoxarifado_cadastro_medidores_produtos(dabnfopg)'                        , None],
            ['04C00502A' , '04C00500A'   , 'abnf000u04c00502_almoxarifado_cadastro_medidores_produtos(dabnfopg)'                        , None],
            ['04M00100A' , '04M00100A'   , 'abnf000u04m00100_almoxarifado_movimentacao_notas_fiscais(dabnfopg)'                         , 'o modulo de lancamento de notas fiscais de clientes'],
            ['04M00101A' , '04M00100A'   , 'abnf000u04m00101_almoxarifado_movimentacao_notas_fiscais(dabnfopg)'                         , None],
            ['04M00102A' , '04M00100A'   , 'abnf000u04m00102_almoxarifado_movimentacao_notas_fiscais(dabnfopg)'                         , None],
            ['04M00100B' , '04M00100B'   , 'abnf000u04m00100_almoxarifado_movimentacao_notas_fiscais(dabnfopg)'                         , 'o modulo de lancamento de notas fiscais de fornecedores'],
            ['04M00101B' , '04M00100B'   , 'abnf000u04m00101_almoxarifado_movimentacao_notas_fiscais(dabnfopg)'                         , None],
            ['04M00102B' , '04M00100B'   , 'abnf000u04m00102_almoxarifado_movimentacao_notas_fiscais(dabnfopg)'                         , None],
            ['04M00200A' , '04M00200A'   , 'abnf000u04m00200_almoxarifado_movimentacao_requisicoes(dabnfopg)'                           , 'o modulo de lancamento de requisicoes'],
            ['04M00201A' , '04M00200A'   , 'abnf000u04m00201_almoxarifado_movimentacao_requisicoes(dabnfopg)'                           , None],
            ['04M00202A' , '04M00200A'   , 'abnf000u04m00202_almoxarifado_movimentacao_requisicoes(dabnfopg)'                           , None],
            ['04M00300A' , '04M00300A'   , 'abnf000u04m00300_almoxarifado_movimentacao_consumo_lote(dabnfopg)'                          , 'o modulo de lancamento de consumo em lote'],
            ['04M00301A' , '04M00300A'   , 'abnf000u04m00301_almoxarifado_movimentacao_consumo_lote(dabnfopg)'                          , None],
            ['04M00302A' , '04M00300A'   , 'abnf000u04m00302_almoxarifado_movimentacao_consumo_lote(dabnfopg)'                          , None],            
            ['04M00500A' , '04M00500A'   , 'abnf000u04m00500_almoxarifado_movimentacao_medidores_produtos(dabnfopg)'                    , 'o modulo de lancamento de medidores de produtos'],
            ['04M00501A' , '04M00500A'   , 'abnf000u04m00501_almoxarifado_movimentacao_medidores_produtos(dabnfopg)'                    , None],
            ['04M00600A' , '04M00600A'   , 'abnf000u04m00600_almoxarifado_movimentacao_reabertura_documentos(dabnfopg)'                 , 'o modulo de reabertura de documentos'],
            ['04M00601A' , '04M00600A'   , 'abnf000u04m00601_almoxarifado_movimentacao_reabertura_documentos(dabnfopg)'                 , None],
            ['04M00700A' , '04M00700A'   , 'abnf000u04m00700_almoxarifado_movimentacao_alteracao_odometros_veiculos(dabnfopg)'          , 'o modulo de alteracao de odometros de veiculos'],
            ['04M00701A' , '04M00700A'   , 'abnf000u04m00701_almoxarifado_movimentacao_alteracao_odometros_veiculos(dabnfopg)'          , None],
            # ['04M01000A' , '04M01000A'   , 'abnf000u04m01000_almoxarifado_movimentacao_notas_fiscais_reabertura(dabnfopg)'            , 'o modulo de reabertura de notas fiscais'],
            # ['04M01001A' , '04M01000A'   , 'abnf000u04m01001_almoxarifado_movimentacao_notas_fiscais_reabertura(dabnfopg)'            , None],
            # ['04M01002A' , '04M01000A'   , 'abnf000u04m01002_almoxarifado_movimentacao_notas_fiscais_reabertura(dabnfopg)'            , None],
            ['04R00100A' , '04R00100A'   , 'abnf000u04r00100_almoxarifado_relatorio_notas_fiscais(dabnfopg)'                            , 'o modulo do relatorio de notas fiscais de clientes'],
            ['04R00101A' , '04R00100A'   , 'abnf000u04r00101_almoxarifado_relatorio_notas_fiscais(dabnfopg)'                            , None],
            ['04R00100B' , '04R00100B'   , 'abnf000u04r00100_almoxarifado_relatorio_notas_fiscais(dabnfopg)'                            , 'o modulo do relatorio de notas fiscais de fornecedores'],
            ['04R00101B' , '04R00100B'   , 'abnf000u04r00101_almoxarifado_relatorio_notas_fiscais(dabnfopg)'                            , None],
            ['04R00200A' , '04R00200A'   , 'abnf000u04r00200_almoxarifado_relatorio_requisicoes(dabnfopg)'                              , 'o modulo do relatorio de requisicoes'],
            ['04R00201A' , '04R00200A'   , 'abnf000u04r00201_almoxarifado_relatorio_requisicoes(dabnfopg)'                              , None],
            ['04R00600A' , '04R00600A'   , 'abnf000u04r00600_almoxarifado_relatorio_movimentacao_produtos_servicos(dabnfopg)'           , 'o modulo do relatorio de movimentacao de produtos e servicos'],
            ['04R00601A' , '04R00600A'   , 'abnf000u04r00601_almoxarifado_relatorio_movimentacao_produtos_servicos(dabnfopg)'           , None],
            ['04R00700A' , '04R00700A'   , 'abnf000u04r00700_almoxarifado_relatorio_consumo_produtos_servicos_veiculo(dabnfopg)'        , 'o modulo do relatorio de movimentacao de produtos e servicos'],
            ['04R00701A' , '04R00700A'   , 'abnf000u04r00701_almoxarifado_relatorio_consumo_produtos_servicos_veiculo(dabnfopg)'        , None],
            ['04R00800A' , '04R00800A'   , 'abnf000u04r00800_almoxarifado_relatorio_medidores_produtos_consumo(dabnfopg)'               , 'o modulo do relatorio de medidores de produtos e consumo'],
            ['04R00801A' , '04R00800A'   , 'abnf000u04r00801_almoxarifado_relatorio_medidores_produtos_consumo(dabnfopg)'               , None],
            # ['04R00900A' , '04R00900A'   , 'abnf000u04r00900_almoxarifado_relatorio_contabil_estoque(dabnfopg)'                         , 'o modulo do relatorio contabil de estoque'],
            # ['04R00901A' , '04R00900A'   , 'abnf000u04r00901_almoxarifado_relatorio_contabil_estoque(dabnfopg)'                         , None],
            ['05C00100A' , '05C00100A'   , 'abnf000u05c00100_preventiva_cadastro_grupos(dabnfopg)'                                      , 'o modulo de cadastro de grupos de preventiva'],
            ['05C00101A' , '05C00100A'   , 'abnf000u05c00101_preventiva_cadastro_grupos(dabnfopg)'                                      , None],
            ['05C00102A' , '05C00100A'   , 'abnf000u05c00102_preventiva_cadastro_grupos(dabnfopg)'                                      , None],
            ['05C00200A' , '05C00200A'   , 'abnf000u05c00200_preventiva_cadastro_itens(dabnfopg)'                                       , 'o modulo de cadastro de itens de preventiva'],
            ['05C00201A' , '05C00200A'   , 'abnf000u05c00201_preventiva_cadastro_itens(dabnfopg)'                                       , None],
            ['05C00202A' , '05C00200A'   , 'abnf000u05c00202_preventiva_cadastro_itens(dabnfopg)'                                       , None],
            ['05C00300A' , '05C00300A'   , 'abnf000u05c00300_preventiva_cadastro_associacao_itens_grupos(dabnfopg)'                     , 'o modulo de cadastro de associacao: itens x grupos'],
            ['05C00301A' , '05C00300A'   , 'abnf000u05c00301_preventiva_cadastro_associacao_itens_grupos(dabnfopg)'                     , None],
            ['05C00302A' , '05C00300A'   , 'abnf000u05c00302_preventiva_cadastro_associacao_itens_grupos(dabnfopg)'                     , None],
            ['05C00400A' , '05C00400A'   , 'abnf000u05c00400_preventiva_cadastro_associacao_veiculos_grupos(dabnfopg)'                  , 'o modulo de cadastro de associacao: veiculos x grupos'],
            ['05C00401A' , '05C00400A'   , 'abnf000u05c00401_preventiva_cadastro_associacao_veiculos_grupos(dabnfopg)'                  , None],
            ['05C00402A' , '05C00400A'   , 'abnf000u05c00402_preventiva_cadastro_associacao_veiculos_grupos(dabnfopg)'                  , None],
            ['05M00100A' , '05M00100A'   , 'abnf000u05m00100_preventiva_acao_preventiva(dabnfopg)'                                      , 'o modulo de acao de preventiva'],
            ['05M00101A' , '05M00100A'   , 'abnf000u05m00101_preventiva_acao_preventiva(dabnfopg)'                                      , None],
            ['05M00102A' , '05M00100A'   , 'abnf000u05m00102_preventiva_acao_preventiva(dabnfopg)'                                      , None],
            ['05R00100A' , '05R00100A'   , 'abnf000u05r00100_preventiva_relatorio_preventivas(dabnfopg)'                                , 'o modulo do relatorio de preventivas'],
            ['05R00101A' , '05R00100A'   , 'abnf000u05r00101_preventiva_relatorio_preventivas(dabnfopg)'                                , None],
            ['08C00100A' , '08C00100A'   , 'abnf000u08c00100_financeiro_cadastro_contas_financeiras(dabnfopg)'                          , 'o modulo de cadastro de contas financeiras'],
            ['08C00101A' , '08C00100A'   , 'abnf000u08c00101_financeiro_cadastro_contas_financeiras(dabnfopg)'                          , None],
            ['08C00102A' , '08C00100A'   , 'abnf000u08c00102_financeiro_cadastro_contas_financeiras(dabnfopg)'                          , None],
            ['08C00200A' , '08C00200A'   , 'abnf000u08c00200_financeiro_cadastro_grupos(dabnfopg)'                                      , 'o modulo de cadastro de grupos financeiros'],
            ['08C00201A' , '08C00200A'   , 'abnf000u08c00201_financeiro_cadastro_grupos(dabnfopg)'                                      , None],
            ['08C00202A' , '08C00200A'   , 'abnf000u08c00202_financeiro_cadastro_grupos(dabnfopg)'                                      , None],
            ['08C00300A' , '08C00300A'   , 'abnf000u08c00300_financeiro_cadastro_subgrupos(dabnfopg)'                                   , 'o modulo de cadastro de subgrupos financeiros'],
            ['08C00301A' , '08C00300A'   , 'abnf000u08c00301_financeiro_cadastro_subgrupos(dabnfopg)'                                   , None],
            ['08C00302A' , '08C00300A'   , 'abnf000u08c00302_financeiro_cadastro_subgrupos(dabnfopg)'                                   , None],
            ['08C00400A' , '08C00400A'   , 'abnf000u08c00400_financeiro_cadastro_complementos(dabnfopg)'                                , 'o modulo de cadastro de complementos'],
            ['08C00401A' , '08C00400A'   , 'abnf000u08c00401_financeiro_cadastro_complementos(dabnfopg)'                                , None],
            ['08C00402A' , '08C00400A'   , 'abnf000u08c00402_financeiro_cadastro_complementos(dabnfopg)'                                , None],
            ['08C00500A' , '08C00500A'   , 'abnf000u08c00500_financeiro_cadastro_centros_custo(dabnfopg)'                               , 'o modulo de cadastro de centros de custo'],
            ['08C00501A' , '08C00500A'   , 'abnf000u08c00501_financeiro_cadastro_centros_custo(dabnfopg)'                               , None],
            ['08C00502A' , '08C00500A'   , 'abnf000u08c00502_financeiro_cadastro_centros_custo(dabnfopg)'                               , None],
            ['08C00600A' , '08C00600A'   , 'abnf000u08c00600_financeiro_cadastro_departamentos(dabnfopg)'                               , 'o modulo de cadastro de departamentos'],
            ['08C00601A' , '08C00600A'   , 'abnf000u08c00601_financeiro_cadastro_departamentos(dabnfopg)'                               , None],
            ['08C00602A' , '08C00600A'   , 'abnf000u08c00602_financeiro_cadastro_departamentos(dabnfopg)'                               , None],
            ['08M00100A' , '08M00100A'   , 'abnf000u08m00100_financeiro_movimentacao_registros_financeiros(dabnfopg)'                   , 'o modulo de registros financeiros'],
            ['08M00101A' , '08M00100A'   , 'abnf000u08m00101_financeiro_movimentacao_registros_financeiros(dabnfopg)'                   , None],
            ['08M00102A' , '08M00100A'   , 'abnf000u08m00102_financeiro_movimentacao_registros_financeiros(dabnfopg)'                   , None],
            ['08M00103A' , '08M00100A'   , 'abnf000u08m00103_financeiro_movimentacao_registros_financeiros(dabnfopg)'                   , None],
            ['08M00200A' , '08M00200A'   , 'abnf000u08m00200_financeiro_movimentacao_conciliacao_financeira(dabnfopg)'                  , 'o modulo de conciliacao financeira'],
            ['08M00201A' , '08M00200A'   , 'abnf000u08m00201_financeiro_movimentacao_conciliacao_financeira(dabnfopg)'                  , None],
            ['08M00202A' , '08M00200A'   , 'abnf000u08m00202_financeiro_movimentacao_conciliacao_financeira(dabnfopg)'                  , None],
            ['08M00300A' , '08M00300A'   , 'abnf000u08m00300_financeiro_movimentacao_transferencia_entre_contas(dabnfopg)'              , 'o modulo de conciliacao financeira'],
            ['08M00301A' , '08M00300A'   , 'abnf000u08m00301_financeiro_movimentacao_transferencia_entre_contas(dabnfopg)'              , None],
            ['08M00302A' , '08M00300A'   , 'abnf000u08m00302_financeiro_movimentacao_transferencia_entre_contas(dabnfopg)'              , None],
            ['08M00400A' , '08M00400A'   , 'abnf000u08m00400_financeiro_movimentacao_lancamento_direto_conta(dabnfopg)'                 , 'o modulo de lancamento direto em conta'],
            ['08M00401A' , '08M00400A'   , 'abnf000u08m00401_financeiro_movimentacao_lancamento_direto_conta(dabnfopg)'                 , None],
            ['08M00402A' , '08M00400A'   , 'abnf000u08m00402_financeiro_movimentacao_lancamento_direto_conta(dabnfopg)'                 , None],
            ['08M00500A' , '08M00500A'   , 'abnf000u08m00500_financeiro_movimentacao_alterar_filiais_registros_financeiros(dabnfopg)'   , 'o modulo de alteracao de filiais em registros financeiros'],
            ['08M00501A' , '08M00500A'   , 'abnf000u08m00501_financeiro_movimentacao_alterar_filiais_registros_financeiros(dabnfopg)'   , None],
            ['08M00501A' , '08M00500A'   , 'abnf000u08m00501_financeiro_movimentacao_alterar_filiais_registros_financeiros(dabnfopg)'   , None],
            ['08R00100A' , '08R00100A'   , 'abnf000u08r00100_financeiro_relatorio_extrato_contas(dabnfopg)'                             , 'o modulo do relatorio de extrato de contas'],
            ['08R00101A' , '08R00100A'   , 'abnf000u08r00101_financeiro_relatorio_extrato_contas(dabnfopg)'                             , None],
            ['08R00200A' , '08R00200A'   , 'abnf000u08r00200_financeiro_relatorio_contas_pagar_receber(dabnfopg)'                       , 'o modulo do relatorio de contas a pagar'],
            ['08R00201A' , '08R00200A'   , 'abnf000u08r00201_financeiro_relatorio_contas_pagar_receber(dabnfopg)'                       , None],
            ['08R00200B' , '08R00200B'   , 'abnf000u08r00200_financeiro_relatorio_contas_pagar_receber(dabnfopg)'                       , 'o modulo do relatorio de contas a receber'],
            ['08R00201B' , '08R00200B'   , 'abnf000u08r00201_financeiro_relatorio_contas_pagar_receber(dabnfopg)'                       , None],
            ['08R00200C' , '08R00200C'   , 'abnf000u08r00200_financeiro_relatorio_contas_pagar_receber(dabnfopg)'                       , 'o modulo do relatorio de contas pagas'],
            ['08R00201C' , '08R00200C'   , 'abnf000u08r00201_financeiro_relatorio_contas_pagar_receber(dabnfopg)'                       , None],
            ['08R00200D' , '08R00200D'   , 'abnf000u08r00200_financeiro_relatorio_contas_pagar_receber(dabnfopg)'                       , 'o modulo do relatorio de contas recebidas'],
            ['08R00201D' , '08R00200D'   , 'abnf000u08r00201_financeiro_relatorio_contas_pagar_receber(dabnfopg)'                       , None],
            ['10R00200A' , '10R00200A'   , 'abnf000u10r00200_elevar_resumo_km_passageiros_por_veiculo(dabnfopg)'                        , 'o modulo do relatorio de resumo de km e passageiros por veiculo do Elevar'],
            ['10R00201A' , '10R00200A'   , 'abnf000u10r00201_elevar_resumo_km_passageiros_por_veiculo(dabnfopg)'                        , None],
            ['11C00300A' , '11C00300A'   , 'abnf000u11c00300_sac_cadastro_atendimentos_grupos(dabnfopg)'                                , 'o modulo de cadastro de grupos de atendimentos do SAC'],
            ['11C00301A' , '11C00300A'   , 'abnf000u11c00301_sac_cadastro_atendimentos_grupos(dabnfopg)'                                , None],
            ['11C00302A' , '11C00300A'   , 'abnf000u11c00302_sac_cadastro_atendimentos_grupos(dabnfopg)'                                , None],
            ['11C00400A' , '11C00400A'   , 'abnf000u11c00400_sac_cadastro_atendimentos_subgrupos(dabnfopg)'                             , 'o modulo de cadastro de subgrupos de atendimentos do SAC'],
            ['11C00401A' , '11C00400A'   , 'abnf000u11c00401_sac_cadastro_atendimentos_subgrupos(dabnfopg)'                             , None],
            ['11C00402A' , '11C00400A'   , 'abnf000u11c00402_sac_cadastro_atendimentos_subgrupos(dabnfopg)'                             , None],
            ['11C00500A' , '11C00500A'   , 'abnf000u11c00500_sac_cadastro_usuarios_grupos(dabnfopg)'                                    , 'o modulo de cadastro de grupos de usuários do SAC'],
            ['11C00501A' , '11C00500A'   , 'abnf000u11c00501_sac_cadastro_usuarios_grupos(dabnfopg)'                                    , None],
            ['11C00502A' , '11C00500A'   , 'abnf000u11c00502_sac_cadastro_usuarios_grupos(dabnfopg)'                                    , None],
            ['11R00100A' , '11R00100A'   , 'abnf000u11r00100_sac_relatorio_visualizacao_geral_atendimentos(dabnfopg)'                   , 'o modulo do relatorio de visualizacao geral de atendimentos do SAC'],
            ['11R00101A' , '11R00100A'   , 'abnf000u11r00101_sac_relatorio_visualizacao_geral_atendimentos(dabnfopg)'                   , None],
            ['11R00200A' , '11R00200A'   , 'abnf000u11r00200_sac_relatorio_atendimentos_usuarios(dabnfopg)'                             , 'o modulo do relatorio de atendimentos ao usuarios do SAC'],
            ['11R00201A' , '11R00200A'   , 'abnf000u11r00201_sac_relatorio_atendimentos_usuarios(dabnfopg)'                             , None],
            ['12R00100A' , '12R00100A'   , 'abnf000u12r00100_sigom_visualizacao_geral_ocorrencias(dabnfopg)'                            , 'o modulo do relatorio de visualizacao geral de ocorrencias do SIGOM'],
            ['12R00101A' , '12R00100A'   , 'abnf000u12r00101_sigom_visualizacao_geral_ocorrencias(dabnfopg)'                            , None],
            ['13C00100A' , '13C00100A'   , 'abnf000u13c00100_operacional_cadastro_locais(dabnfopg)'                                     , 'o modulo de cadastro de locais'],
            ['13C00101A' , '13C00100A'   , 'abnf000u13c00101_operacional_cadastro_locais(dabnfopg)'                                     , None],
            ['13C00102A' , '13C00100A'   , 'abnf000u13c00102_operacional_cadastro_locais(dabnfopg)'                                     , None],
            ['13C00200A' , '13C00200A'   , 'abnf000u13c00200_operacional_cadastro_grupos_linhas(dabnfopg)'                              , 'o modulo de cadastro de grupos de linhas'],
            ['13C00201A' , '13C00200A'   , 'abnf000u13c00201_operacional_cadastro_grupos_linhas(dabnfopg)'                              , None],
            ['13C00202A' , '13C00200A'   , 'abnf000u13c00202_operacional_cadastro_grupos_linhas(dabnfopg)'                              , None],
            ['13C00300A' , '13C00300A'   , 'abnf000u13c00300_operacional_cadastro_linhas(dabnfopg)'                                     , 'o modulo de cadastro de linhas'],
            ['13C00301A' , '13C00300A'   , 'abnf000u13c00301_operacional_cadastro_linhas(dabnfopg)'                                     , None],
            ['13C00302A' , '13C00300A'   , 'abnf000u13c00302_operacional_cadastro_linhas(dabnfopg)'                                     , None],
            ['13C00400A' , '13C00400A'   , 'abnf000u13c00400_operacional_cadastro_projetos(dabnfopg)'                                   , 'o modulo de cadastro de projetos'],
            ['13C00401A' , '13C00400A'   , 'abnf000u13c00401_operacional_cadastro_projetos(dabnfopg)'                                   , None],
            ['13C00402A' , '13C00400A'   , 'abnf000u13c00402_operacional_cadastro_projetos(dabnfopg)'                                   , None],
            ['13C00500A' , '13C00500A'   , 'abnf000u13c00500_operacional_cadastro_trajetos(dabnfopg)'                                   , 'o modulo de cadastro de trajetos'],
            ['13C00501A' , '13C00500A'   , 'abnf000u13c00501_operacional_cadastro_trajetos(dabnfopg)'                                   , None],
            ['13C00502A' , '13C00500A'   , 'abnf000u13c00502_operacional_cadastro_trajetos(dabnfopg)'                                   , None],
            ['13C00600A' , '13C00600A'   , 'abnf000u13c00600_operacional_cadastro_itinerarios(dabnfopg)'                                , 'o modulo de cadastro de itinerarios'],
            ['13C00601A' , '13C00600A'   , 'abnf000u13c00601_operacional_cadastro_itinerarios(dabnfopg)'                                , None],
            ['13C00602A' , '13C00600A'   , 'abnf000u13c00602_operacional_cadastro_itinerarios(dabnfopg)'                                , None],
            ['13C00700A' , '13C00700A'   , 'abnf000u13c00700_operacional_cadastro_grupos_veiculos(dabnfopg)'                            , 'o modulo de cadastro de grupos de veiculos'],
            ['13C00701A' , '13C00700A'   , 'abnf000u13c00701_operacional_cadastro_grupos_veiculos(dabnfopg)'                            , None],
            ['13C00702A' , '13C00700A'   , 'abnf000u13c00702_operacional_cadastro_grupos_veiculos(dabnfopg)'                            , None],
            ['13C00800A' , '13C00800A'   , 'abnf000u13c00800_operacional_cadastro_prioridades_linhas(dabnfopg)'                         , 'o modulo de cadastro de prioridades de linhas'],
            ['13C00801A' , '13C00800A'   , 'abnf000u13c00801_operacional_cadastro_prioridades_linhas(dabnfopg)'                         , None],
            ['13C00802A' , '13C00800A'   , 'abnf000u13c00802_operacional_cadastro_prioridades_linhas(dabnfopg)'                         , None],
            ['13C00805A' , '13C00800A'   , 'abnf000u13c00805_operacional_cadastro_prioridades_linhas(dabnfopg)'                         , None],
            ['13C00900A' , '13C00900A'   , 'abnf000u13c00900_operacional_cadastro_operacoes_especiais(dabnfopg)'                        , 'o modulo de cadastro de operacoes especiais'],
            ['13C00901A' , '13C00900A'   , 'abnf000u13c00901_operacional_cadastro_operacoes_especiais(dabnfopg)'                        , None],
            ['13C00902A' , '13C00900A'   , 'abnf000u13c00902_operacional_cadastro_operacoes_especiais(dabnfopg)'                        , None],
            ['13M00100A' , '13M00100A'   , 'abnf000u13m00100_operacional_movimentacao_propostas_oso(dabnfopg)'                          , 'o modulo de lancamento de propostas de OSO'],
            ['13M00101A' , '13M00100A'   , 'abnf000u13m00101_operacional_movimentacao_propostas_oso(dabnfopg)'                          , None],
            ['13M00102A' , '13M00100A'   , 'abnf000u13m00102_operacional_movimentacao_propostas_oso(dabnfopg)'                          , None],
            ['13M00100B' , '13M00100B'   , 'abnf000u13m00100_operacional_movimentacao_propostas_oso(dabnfopg)'                          , 'o modulo de aprovacao de propostas de OSO'],
            ['13M00101B' , '13M00100B'   , 'abnf000u13m00101_operacional_movimentacao_propostas_oso(dabnfopg)'                          , None],
            ['13M00102B' , '13M00100B'   , 'abnf000u13m00102_operacional_movimentacao_propostas_oso(dabnfopg)'                          , None],
            ['13M02100A' , '13M02100A'   , 'abnf000u13m02100_operacional_programacao_movimentacao_controle_diario(dabnfopg)'            , 'o modulo de controle de programacao diaria'],
            ['13M02101A' , '13M02100A'   , 'abnf000u13m02101_operacional_programacao_movimentacao_controle_diario(dabnfopg)'            , None],
            ['13M02102A' , '13M02100A'   , 'abnf000u13m02102_operacional_programacao_movimentacao_controle_diario(dabnfopg)'            , None],
            ['13M03000A' , '13M03000A'   , 'abnf000u13m03000_operacional_entrada_saida_veiculos(dabnfopg)'                              , 'o modulo de entrada e saida de veiculos'],
            ['13M03001A' , '13M03000A'   , 'abnf000u13m03001_operacional_entrada_saida_veiculos(dabnfopg)'                              , None],
            ['13M03002A' , '13M03000A'   , 'abnf000u13m03002_operacional_entrada_saida_veiculos(dabnfopg)'                              , None],
            ['13R03000A' , '13R03000A'   , 'abnf000u13r03000_operacional_entrada_saida_veiculos(dabnfopg)'                              , 'o modulo do relatorio de entrada e saida de veiculos'],
            ['13R03001A' , '13R03000A'   , 'abnf000u13r03001_operacional_entrada_saida_veiculos(dabnfopg)'                              , None],
            ['14M00100A' , '14M00100A'   , 'abnf000u14m00100_transdata_its_importacao(dabnfopg)'                                        , 'o modulo de importacao de dados do Transdata ITS'],
            ['14M00101A' , '14M00100A'   , 'abnf000u14m00101_transdata_its_importacao(dabnfopg)'                                        , None],
            ['14R00100A' , '14R00100A'   , 'abnf000u14r00100_transdata_its_analise(dabnfopg)'                                           , 'o modulo do relatorio de analise do Transdata ITS'],
            ['14R00101A' , '14R00100A'   , 'abnf000u14r00101_transdata_its_analise(dabnfopg)'                                           , None],
            ['14R00200A' , '14R00200A'   , 'abnf000u14r00200_transdata_its_horarios_trabalho_motoristas(dabnfopg)'                      , 'o modulo do relatorio de horas trabalhadas de motoristas pelo Transdata ITS'],
            ['14R00201A' , '14R00200A'   , 'abnf000u14r00201_transdata_its_horarios_trabalho_motoristas(dabnfopg)'                      , None],
            ['00S00999A' , 'Free'        , 'abnf_socket_004([4, "", ""])'                                                               , None], # Reinicia o sistema (refresh)
        ])
        bencmodu = False
        for lauxi001 in labnfmod:
            if lauxi001[0] == sabnfsys:                 # Módulo solicitado foi encontrado
                bencmodu = True
                if lauxi001[1] == 'Free':               # Módulo não precisa de permissão de acesso
                    if lauxi001[3] != None:             # Módulo tem seu acesso registrado no log
                        abnf_websocket_log(
                            sabnproj[14:],
                            200,
                            'abnf_sistema_usuarios',
                            'idusuar',
                            dglobaux['iidusuar'],   # ID do usuário
                            dglobaux['slogiusu'],   # Login do usuário
                            dglobaux['snomeusu'],   # Nome completo do usuário
                            'Usuario acessou ' + lauxi001[3],
                            None
                    )
                    eval(lauxi001[2])
                    break
                else:
                    icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
                    if abnf_websocket_autoriza_modulo(icodbase, dglobaux['iidusuar'], dglobaux['iidfilia'], lauxi001[1]):
                        eval(lauxi001[2])
                        bvalidad = True
                    break
        if not bencmodu:
            abnf_alert('O módulo ' + sabnfsys + ' ainda não está disponível nesse sistema!', 4)
            abnf_socket_004([1, 'abnfdv03', ''])

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função para criar a página principal html/css/js com os parâmetros de projeto e usuário ////////////////////////////////////////////////////////////// #
# // Fonte do socket.io usado atualmente: https://cdn.jsdelivr.net/npm/socket.io-client/dist/socket.io.js                                                // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_gera_page_htm_websocket_project(sabnproj, slogosys):
    sabntoke = str(uuid.uuid4())
    # llegumes = (
    #     ('', ''), (100, 'CENOURA'), (231, 'BATATA')  # , (323, 'COUVE')
    # )
    snewpage = abnf_create_page([
        ('div-0', 'container', None, None),
        ('hr-0', None),
        ('div-0', 'row', None, None),
        ('div-0', 'col d-flex justify-content-center', None, None),
        ('div-0', 'w-50 p-3', 'background-color: #eee;', None),
        ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
        ('legend-0', 'Login do Sistema'),
        ('hr-0', None),
        ('label-0',    'Usuário' , 'form-control-label'),
        ('input-0',    'susuario', 'form-control', 0, 30, '16px', None, 'ssenhdig', True, 0),
        ('label-0',    'Senha'   , 'form-control-label',),
        ('password-0', 'ssenhdig', 'form-control', 6, 30, '16px', None, 'btacesso', True, 0),
        ('hr-0', None),
        ('button-0',   'btacesso', 'btn btn-primary mt-2', 'Fazer Login'),
        # Acesso direto a um módulo (início)
        ('hr-0', None),
        ('button-0',   'btdireto', 'btn btn-primary mt-2', 'Acesso direto'),
        # Acesso direto a um módulo (fim)
        # Área de testes (início)
        # ('hr-0', None),
        # ('button-4',   'btautocl', 'btn btn-primary mt-2', 'Autoclick', 5),
        # ('hr-0', None),
        # ('file-0', 'fteste01', 'btn btn-primary mt-2', '.jpg,.png,.bmp', False),
        # ('hr-0', None),
        # ('select-0', 'llegumes', 'form-control', '16px', 'btacesso', llegumes, 1, None, True),
        # ('select-1', 'llegumes', 'form-control', '16px', 'btacesso', llegumes, 1, None, True, 'TESTE'),
        # ('hr-0', None),
        # ('radio-0', 'iidcomid', '15', None, '16px', 'b', 'P', 'F', 'CENOURA'),
        # ('radio-0', 'iidcomid', '25', None, '16px', 'b', 'P', 'F', 'BATATA'),
        # ('radio-0', 'iidcomid', '32', None, '16px', 'b', 'P', 'F', 'COUVE'),
        # ('hr-0', None),
        # ('radio-1', 'iidcomid', '15', None, '16px', 'b', 'P', 'P', 'CENOURA', 'TESTE RADIO'),
        # ('radio-1', 'iidcomid', '25', None, '16px', 'b', 'P', 'P', 'BATATA' , 'TESTE RADIO'),
        # ('radio-1', 'iidcomid', '32', None, '16px', 'b', 'P', 'P', 'COUVE'  , 'TESTE RADIO'),
        # ('hr-0', None),
        # ('radio-0', 'iidveicu', '1', '2', '16px', 'P', 'ONIX'),
        # ('radio-0', 'iidveicu', '2', '2', '16px', 'P', 'VECTRA'),
        # ('radio-0', 'iidveicu', '3', '2', '16px', 'P', 'CIVIC'),
        # ('hr-0', None),
        # ('checkbox-0', 'iidcen01', 'y' , None, '16px', 'F', 'CENOURA'),
        # ('checkbox-0', 'iidbat01', 'y' , 'y' , '16px', 'F', 'BATATA'),
        # ('checkbox-0', 'iidcou01', 'y' , 'x' , '16px', 'F', 'COUVE'),
        # ('hr-0', None),
        # ('checkbox-0', 'iidcen01', 'y' , None, '16px', 'P', 'CENOURA'),
        # ('checkbox-0', 'iidbat01', 'y' , 'y' , '16px', 'P', None),
        # ('checkbox-0', 'iidcou01', 'y' , 'y' , '16px', 'P', 'COUVE'),
        # ('hr-0', None),
        # ('button-2', 'sdiv0001', 'btn btn-success mt-2', 'Opções adicionais'),
        # ('div-2', 'sdiv0001'),
        # ('br-0', None),
        # ('checkbox-0', 'bperod1k', 'y', None, '16px', 'P', 'Teste 001'),
        # ('checkbox-0', 'bperro1k', 'y', None, '16px', 'P', 'Teste 002'),
        # ('div-9', None),
        # ('hr-0', None),
        # ('time-0',   'hteste01', 'form-control', '16px', '00:00', 'thoraxxx', True, 0, None),
        # ('hr-0', None),
        # ('time-1',   'hteste02', 'form-control', '16px', '00:00', 'thoraxxx', True, 0, None),
        # Área de testes (fim)
        ('form-9', None),
        ('div-9', None),
        ('div-9', None),
        ('div-9', None),
        ('div-9', None),
    ])
    sauxht01 = ' class="fixed-top"'
    sauxht02 = ' style="position: fixed; top: 95px; width: 100%;"'
    sauxht03 = ' style="margin-top: 170px;"'
    # sauxht01 = ''
    # sauxht02 = ''
    # sauxht03 = ''
    # <link href="/static/abeinfo/abeinfo.css" rel="stylesheet" type="text/css" >
    # <script src="/static/abeinfo/abeinfo.js"></script>
    spagehtm = '''
    <!DOCTYPE html>
    <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <title>Abeinfo Sistemas</title>
            <link href="/static/bootstrap-5.2.1-dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
            <script src="/static/bootstrap-5.2.1-dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
            <script src="/static/socketio-4.7.5/socket.io.js"></script>
        </head>
        <body>
            <div id="abnfdv01"''' + sauxht01 + '''>
                <nav class="navbar navbar-expand-lg bg-light">
                    <div class="container-fluid container">
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                            <span class="navbar-toggler-icon"></span>
                        </button>
                        <ul class="navbar-nav me-auto mb-2 mb-lg-5">
                        </ul>
                        <ul class="d-flex navbar-nav">
                            <li class="nav-item">''' + slogosys + '''</li>
                        </ul>
                    </div>
                </nav>
            </div>
            <div id="abnfdv02"''' + sauxht02 + '''></div>
            <div id="abnfdv03"''' + sauxht03 + '''>''' + snewpage + '''</div>
            <div id="abnfdv04"></div>
            <div id="abnfdv05"></div>
            <div id="abnfdv06"></div>
            <div id="abnfdv07"></div>
            <div id="abnfdv08"></div>
            <div id="abnfdv09"></div>
            <div id="abnfdv10"></div>
            <input type="hidden" id="abnproje" name="abnproje" value="''' + sabnproj + '''">
            <input type="hidden" id="abntoken" name="abntoken" value="''' + sabntoke + '''">
            </div>
        </body>
    </html>'''
    spagehtm = spagehtm  + abnf_websocket_js_socketio(sabntoke)
    spagehtm = spagehtm  + abnf_websocket_js_abeinfo()
    spagehtm = spagehtm  + abnf_websocket_css_menu_dropdown()
    return spagehtm, sabntoke

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_files_upload ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de upload de arquivos.                                                                                                                       // #
# // Essa função recebe informação da função JS: AbnfUploadFiles.                                                                                        // #
# // Essa infterpretação é feita através do elemeto 'ffile001' criado pelo JS e recuperado aqui pelo 'request.files.getlist'.                            // #
# // Através das informações recebidas a função cria diretórios dentro do /abnftmp com o nome 'upload-<abntoken>' onde salva os arquivos de upload.      // #
# // Caso o dirtório exista, ele será destruído e recriado para que não corra riscos de existir arquivos antigos dentro dele.                            // #
# // Para ter certeza que o processo de upload foi finalizado, após o térnimo ele cria o arquivo 'abeinfo.upload.completed' com 0 bytes.                 // #
# // Para sucesso do upload essa função tem que ser método POST mas não cria nenhum problema para a página por estar terminado com 'Respose()'.          // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    
@abnfxapp.route('/upload/<abntoken>', methods=['POST'])
def abnf_files_upload(abntoken):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_files_upload(abntoken)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    abnfiles = request.files.getlist('ffile001') # Use getlist() for multiple files
    abntoken = 'upload-' + abntoken
    sdirecto = os.path.join('abnftmp/', abntoken)
    print(sdirecto)
    if os.path.exists(sdirecto):
        shutil.rmtree(sdirecto)
    os.makedirs(sdirecto, exist_ok = True)
    icontarq = 0
    for abnffile in abnfiles:
        suploarq = abnffile.filename
        ssavearq = os.path.join(sdirecto, suploarq)
        print(ssavearq)
        abnffile.save(ssavearq)
        icontarq += 1
    if icontarq > 0:
        ssavearq = os.path.join(sdirecto, 'abeinfo.upload.completed')
        abnffile.save(ssavearq)
    return Response()
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_files_download ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de download de arquivos.                                                                                                                     // #
# // Essa função recebe informação da função JS: AbnfDownloadFiles.                                                                                      // #
# // A informação recebida através de um GET será o nome do arquivo: <filename>.                                                                         // #
# // Caso o arquvo não exista vai ocasionar erro na página, então todo o processo de certificação da existência do arquivo tem que ser feita antes.      // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #    

@abnfxapp.route('/download/<filename>', methods=['GET'])
def abnf_files_download(filename):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_files_download(filename)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    sdirecto = abnfcfg.sdirsyst + 'abnftmp/' + filename
    # ==> idefflex = 0
    # ==> if   idefflex == 0: sdirecto = '/flexabeinfo/abnftmp/' + filename
    # ==> elif idefflex == 1: sdirecto = '/flexgb/abnftmp/' + filename
    print(sdirecto)
    if not os.path.exists(sdirecto):
        print('Arquivo não encontrado!')
        return Response()
    else:
        return send_file(sdirecto, as_attachment=True)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u00s00201_login_sistema ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função de login do sistema.                                                                                                                         // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u00s00201_login_sistema(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u00s00201_login_sistema(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Debug (início)
        # abnf_show('10', dabnfopg, 2)
        # Debug (fim)
        # Teste do botão automático (início)
        # if dabnfopg['abnfobj0'] == ['btautocl', 'btautocl']:
        #     agora = datetime.now()
        #     abnf_alert('Clique automático em ' + str(agora), 4)
        # Teste do botão automático (fim)
        if dabnfopg['abnfobj0'] == ['btacesso', 'btacesso']: # [ Foi pressionado o botão 'btacesso' ]
            lmfields = [
                ['susuario', 'input',   'M', 'usuário',        ['Notnull', 'P'], None],
                ['ssenhdig', 'input',   'F', 'senha',          ['Notnull', 'P'], None],
                #['fteste01', 'file',   'F', 'foto de perfil', ['Notnull', 'D'], None],
                #['hteste02', 'time-1', 'F', 'hora teste',     ['Notnull', 'D'], None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btacesso')
            if bvalidad:
                abnf_alert('Aguarde...', 6)
                # abnf_socket_004([6, 'fteste01'])
                # abnf_socket_004([7, 'abnfdebug000001.txt'])
                # abnf_socket_004([7, 'teste-download.txt'])
                # abnf_socket_004([7, 'teste-download.txt'])
                # abnf_socket_004([7, 'Fluxo 2023-01-02.xls'])
                susuario = lmfields[0][5]
                ssenhdig = lmfields[1][5]
                if not abnf_websocket_valida_estrutura_usuario(susuario):
                    time.sleep(10)
                    abnf_alert('Sistema em manutenção! Tente novamente mais tarde!', 4)
                    abnf_websocket_limpa_campos(lmfields)
                else:
                    icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
                    scamposb = 'idusuar, logiusu, senhusu, tipousu, emaiusu, idfotop, nomeusu, idgrams'
                    sfilbusc = 'logiusu = "' + susuario + '" AND situreg = "A"'
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v01(icodbase, 'abnf_sistema_usuarios', scamposb, sfilbusc, None)
                    if lsqlre01 == '[]' or iqtdre01 == 0:
                        abnf_alert('Falha no login: usuário ou senha incorretos!', 4)
                        abnf_websocket_limpa_campos(lmfields)
                        abnf_socket_004([5, 'btacesso'])
                    else:
                        # ////////////////////////////////////////////
                        # Teste de chamada usando toque e vóz (ínício)
                        # ////////////////////////////////////////////
                        # abnf_socket_004([12, 2])
                        # time.sleep(2)
                        # abnf_socket_004([13, 'ADALBERTO DOS SANTOS MATHIAS FERREIRA BARBOSA SANTOS: Guichê 003'])
                        # abnf_socket_004([13, 'VEICULO 12307: LIBERADO PELA OFICINA'])
                        # time.sleep(7)
                        # abnf_socket_004([12, 2])
                        # time.sleep(2)
                        # abnf_socket_004([13, 'JOSÉ DA SILVA: Guichê 002'])
                        # time.sleep(7)
                        # abnf_socket_004([12, 2])
                        # time.sleep(2)
                        # abnf_socket_004([13, 'JOSEFINA DE JESUS GUERREIRO PAIVA FERREIRA SILVA: Guichê 003'])
                        # /////////////////////////////////////////
                        # Teste de chamada usando toque e víz (fim)
                        # /////////////////////////////////////////
                        baltsenh = True if lsqlre01[0][2] == 'MUDAR@123'    else False
                        baltemai = True if lsqlre01[0][4] == None           else False
                        baltfoto = True if lsqlre01[0][5] == None           else False
                        print(baltsenh)
                        print(baltemai)
                        print(baltfoto)
                        print('----------------------------------------------------------------------------------------------------------------------------------')
                        if baltsenh and ssenhdig != 'MUDAR@123':
                            abnf_alert('Falha no login: usuário ou senha incorretos!', 4)
                            abnf_websocket_limpa_campos(lmfields)
                            abnf_socket_004([5, 'btacesso'])
                        elif not baltsenh and not abnfbcry.check_password_hash(lsqlre01[0][2], ssenhdig):
                            abnf_alert('Falha no login: usuário ou senha incorretos!', 4)
                            abnf_websocket_limpa_campos(lmfields)
                            abnf_socket_004([5, 'btacesso'])
                        else:
                            dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
                            abnf_alert('Login feito com sucesso!', 3)
                            # Registra o log:
                            abnf_websocket_log(
                                sabnproj[14:],
                                100,
                                'abnf_sistema_usuarios',
                                'idusuar',
                                lsqlre01[0][0],                 # ID do usuário
                                lsqlre01[0][1],                 # Login do usuário
                                lsqlre01[0][6],                 # Nome completo do usuário
                                'Usuario acessou o sistema',
                                None
                            )
                            # Atualiza dados em dglobdws para direcionar para a próxima etapa:
                            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (
                                ('iidusuar', lsqlre01[0][0]),   # ID do usuário
                                ('slogiusu', lsqlre01[0][1]),   # Login do usuário
                                ('ssenhusu', lsqlre01[0][2]),   # Senha do usuário
                                ('stipousu', lsqlre01[0][3]),   # Tipo de usuário: [A]dministrativo/[O]peracional
                                ('semaiusu', lsqlre01[0][4]),   # Email do usuário
                                ('iidfotop', lsqlre01[0][5]),   # ID da foto do perfil
                                ('snomeusu', lsqlre01[0][6]),   # Nome completo do usuário
                                ('iidgrams', lsqlre01[0][7]),   # ID do grupo de acessos dos modulos do sistema
                            )])
                            # Insere o nome do usuário e o botão de sair na página
                            snewpage = '''
                            <nav class="navbar navbar-expand-lg bg-light">
                                <div class="container-fluid container">
                                    <div class="border p-1 rounded border-secondary border-1">
                                        <font color="brown" face="Verdana, Geneva, sans-serif" size="2">''' + lsqlre01[0][6][:30] + '''</font>
                                    </div>
                                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                                        <span class="navbar-toggler-icon"></span>
                                    </button>
                                    <ul class="navbar-nav me-auto mb-2 mb-lg-5">
                                    </ul>
                                    <ul class="d-flex navbar-nav">
                                        <li class="nav-item border p-1 rounded border-secondary border-1">
                                            <a class="nav-link active" href="#" id="00S00999A" onclick="AbnfSubmitModule(this);">Sair</a>
                                        </li>
                                        <li class="nav-item">''' + dglobaux['slogosys'] + '''</li>
                                    </ul>
                                </div>
                            </div>'''
                            abnf_socket_004([1, 'abnfdv01', snewpage])
                            # Define o módulo sequêncial e encaminha:
                            if   baltsenh: abnf000u00s00400_perfil(dabnfopg)
                            elif baltemai: abnf000u00s00400_perfil(dabnfopg)
                            elif baltfoto: abnf000u00s00400_perfil(dabnfopg)
                            else: abnf000u00s00300_definicao_empresa_filial(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btdireto', 'btdireto']:
            # /////////////////////////
            # Área de testes sistêmicos
            # /////////////////////////
            if False:
                sauxi001 = abnf_websocket_date_time(6)
                abnf_show('05', sauxi001, 0)
                sauxi002 = 'UPDATE abnf_operacional_movimentacao_programacao_retencao_veiculos SET dtliber = "' + sauxi001 + '", idcusli = 0, idusual = 2, dtregal = CURRENT_TIMESTAMP() WHERE dataage < "2025-09-11" and dtliber IS NULL and situreg != "C" and statret IN (2, 3, 4);'
                abnf_show('06', sauxi002, 0)
                sauxi002 = 'SELECT * FROM abnf_operacional_movimentacao_programacao_retencao_veiculos WHERE dtliber = "' + sauxi001 + '";'
                abnf_show('07', sauxi002, 0)
                # SELECT * FROM abnf_operacional_movimentacao_programacao_retencao_veiculos WHERE codctrl = 368;
                # +---------+---------+---------+---------------------+---------------------+---------+---------+---------+------------+---------+---------------------------------+---------+---------+---------+---------+---------+---------+---------------------+---------------------+---------+
                # | idoprrv | codctrl | idveicu | dtreten             | dtliber             | idcusgr | idcusre | idcusli | dataage    | seghage | descrre                         | descrli | statret | idsdede | situreg | idusucr | idusual | dtregcr             | dtregal             | idfilia |
                # +---------+---------+---------+---------------------+---------------------+---------+---------+---------+------------+---------+---------------------------------+---------+---------+---------+---------+---------+---------+---------------------+---------------------+---------+
                # |     368 |     368 |     750 | 2025-09-08 12:54:34 | 2025-09-10 00:01:52 |       2 |      40 |       0 | 2025-09-09 |       0 | RAIO X/ SETA NAO FUNCIONA/ PNEU | NULL    |       2 |    1230 | A       |      40 |      17 | 2025-09-08 12:54:34 | 2025-09-10 00:01:52 |       3 |
                # +---------+---------+---------+---------------------+---------------------+---------+---------+---------+------------+---------+---------------------------------+---------+---------+---------+---------+---------+---------+---------------------+---------------------+---------+
                # UPDATE abnf_operacional_movimentacao_programacao_retencao_veiculos SET dtliber = "2025-09-09 23:59:59" WHERE codctrl = 368;
                # 31353
            # //////////////////////////////////////////
            # Área de teste para busca no banco de dados
            # //////////////////////////////////////////
            if False:
                icodbase = 200
                iidfilia = 3
                ddatahoj = date.today()
                ddatahoj = date(2025, 9, 5)
                # /////////////////////////#
                lcamposb = ('dtmetod', None)
                lfilbusc = (('idfilia', '=', iidfilia), ('situreg', '!=', 'C')) # , ('dtmetod', '>=', ddatahoj))
                lorderby = ('dtmetod', None)
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_movimentacao_programacao_automacao', lcamposb, lfilbusc, lorderby)
                abnf_show('05', lsqlre01, 1)
                # /////////////////////////#
                lcamposb = ('dtmetod', None)
                lfilbusc = (('idfilia', '=', iidfilia), ('situreg', '!=', 'C'), ('dtmetod', '>=', ddatahoj))
                lorderby = ('dtmetod', None)
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_movimentacao_programacao_automacao', lcamposb, lfilbusc, lorderby)
                abnf_show('06', lsqlre01, 1)
            # //////////////////////////////////////////
            # Área de teste com acesso direito ao módulo
            # //////////////////////////////////////////
            if True:
                lmodulos = [
                    # Cadastro de veículos
                    (1, 3, 'abnf000u12r00100_sigom_visualizacao_geral_ocorrencias'                                  , ([3, 'ddataini', '2025-11-01'], [3, 'ddatafim', '2025-11-01'], [3, 'itiporel', '2'])),
                    # Sem definição do produto
                    (0, 1, 'abnf000u04r00600_almoxarifado_relatorio_movimentacao_produtos_servicos'                 , ()), # ([3, 'iidprser', '1119'], [11, 'btgerrel'], None)), # ([3, 'ddataini', '2025-01-01'], [3, 'ddatafim', '2025-01-31'], [11, 'btgerrel'])),
                    (0, 1, 'abnf000u04r00600_almoxarifado_relatorio_movimentacao_produtos_servicos'                 , ([11, 'btgerrel'], None)), # ([3, 'iidprser', '1119'], [11, 'btgerrel'], None)), # ([3, 'ddataini', '2025-01-01'], [3, 'ddatafim', '2025-01-31'], [11, 'btgerrel'])),
                    # Oleo diesel
                    (0, 1, 'abnf000u04r00600_almoxarifado_relatorio_movimentacao_produtos_servicos'                 , ([3, 'irelator', '2'], [3, 'ddataini', '2025-02-01'], [3, 'ddatafim', '2025-02-28'], [3, 'iidprser', '1119'], [11, 'btgerrel'], None)), # ([3, 'ddataini', '2025-01-01'], [3, 'ddatafim', '2025-01-31'], [11, 'btgerrel'])),
                    # Catalisador
                    (0, 1, 'abnf000u04r00600_almoxarifado_relatorio_movimentacao_produtos_servicos'                 , ([3, 'iidprser', '683'], [11, 'btgerrel'], None)), # ([3, 'ddataini', '2025-01-01'], [3, 'ddatafim', '2025-01-31'], [11, 'btgerrel'])),
                    # Mola mestre taseira volvo
                    (0, 1, 'abnf000u04r00600_almoxarifado_relatorio_movimentacao_produtos_servicos'                 , ([3, 'iidprser', '1708'], [11, 'btgerrel'], None)), # ([3, 'ddataini', '2025-01-01'], [3, 'ddatafim', '2025-01-31'], [11, 'btgerrel'])),
                    # Teste acerto de registros
                    (0, 1, 'abnf000u04r00600_almoxarifado_relatorio_movimentacao_produtos_servicos'                 , ([3, 'iidprser', '1492'], [11, 'btgerrel'], None)), # ([3, 'ddataini', '2025-01-01'], [3, 'ddatafim', '2025-01-31'], [11, 'btgerrel'])),
                    (0, 1, 'abnf000u04r00700_almoxarifado_relatorio_consumo_produtos_servicos_veiculo'              , ([3, 'ddataini', '2000-01-01'], [3, 'iidveicu', '40'], [3, 'ddatafim', '2050-12-31'], [11, 'btgerrel'])),
                    (0, 1, 'abnf000u05c00300_preventiva_cadastro_associacao_itens_grupos'                           , ([3, 'iidgrpre', '1'], [11, 'btbusreg'])),
                    (0, 1, 'abnf000u05c00400_preventiva_cadastro_associacao_veiculos_grupos'                        , ([3, 'iidgrpre', '1'], [11, 'btbusreg'])),
                    (0, 1, 'abnf000u05m00100_preventiva_acao_preventiva'                                            , ([3, 'iidveicu', '40'], [11, 'btbusreg'], [99, 2], [3, 'ddatarea', '2025-05-15'], [3, 'iodomvei', '465600'], [3, 'iidfunci', '2'], [3, 'sobserva', 'TESTE OBSERVACAO'], [11, 'iiditpre[26]'], [11, 'iiditpre[8]'])),
                    (0, 1, 'abnf000u05m00100_preventiva_acao_preventiva'                                            , ([3, 'iidveicu', '40'], [11, 'btbusreg'], [99, 2], [3, 'ddatarea', '2025-02-09'], [3, 'iodomvei', '461000'], [3, 'iidfunci', '2'], [3, 'sobserva', 'TESTE OBSERVACAO'], [11, 'iiditpre[26]'], [11, 'iiditpre[8]'])),
                    (0, 1, 'abnf000u05r00100_preventiva_relatorio_preventivas'                                      , ()), # ([3, 'iidveicu', '40'], [11, 'btbusreg'], [99, 2], [3, 'ddatarea', '2025-02-09'], [3, 'iodomvei', '461000'], [3, 'iidfunci', '2'], [3, 'sobserva', 'TESTE OBSERVACAO'], [11, 'iiditpre[26]'], [11, 'iiditpre[8]'])),
                    (0, 1, 'abnf000u08m00400_financeiro_movimentacao_lancamento_direto_conta'                       , ([3, 'iidsubgr', '3'], [11, 'btnovreg'], [3, 'ddataini', '2024-01-01'], [3, 'ddatafim', '2025-12-31'])),
                    (0, 3, 'abnf000u13c00800_operacional_cadastro_prioridades_linhas'                               , ([3, 'iidolinh', '153'], [3, 'iidotraj', '1'], [3, 'ssentido', 'I'], [11, 'btbusreg'])),
                    (0, 3, 'abnf000u13c00900_operacional_cadastro_operacoes_especiais'                              , ([11, 'btnovope'], None)),
                    (0, 3, 'abnf000u13c00300_operacional_cadastro_linhas'                                           , ([3, 'iidolinh', '93'], [11, 'btbusreg'])),
                    (0, 3, 'abnf000u13m00100_operacional_movimentacao_propostas_oso'                                , ([11, 'btnovpro'], [99, 1], [3, 'iidoproj', '1'], [3, 'iidoproj', '1'], [3, 'iidolinh', '115'], [3, 'sdescpre', 'TESTE NOVO REGISTRO'], [11, 'btpdiaut'])),
                    (0, 3, 'abnf000u13m00100_operacional_movimentacao_propostas_oso'                                , ([3, 'inumepro', '222'], [11, 'btbusreg'], [99, 3])), #    , [3, 'irelator', '3'], [11, 'btgerrel'])), # 6a.003 - 220 - Produtivo - Correto
                    (0, 3, 'abnf000u13m00100_operacional_movimentacao_propostas_oso'                                , ([3, 'inumepro', '168'], [11, 'btbusreg'], [99, 3], [3, 'irelator', '6'], [11, 'btgerrel'])), # 6a.003 - 240 - Ocioso - Errado - Tem que ficar em baixo de 19.27 e ambos entre parenteses
                    (0, 3, 'abnf000u13m00100_operacional_movimentacao_propostas_oso'                                , ([3, 'inumepro', '202'], [11, 'btbusreg'])), # [99, 3], [3, 'irelator', '6'], [11, 'btgerrel'])), # 444-U
                    (0, 3, 'abnf000u13m00100_operacional_movimentacao_propostas_oso'                                , ([11, 'iidoprop'], [11, 'btselreg'])), # , [99, 2], [3, 'ddatavig', '2025-05-15'], [11, 'btaprovx'], [99, 2], [11, 'btaprova'])),
                    # Programação diária
                    (0, 3, 'abnf000u13m02100_operacional_programacao_movimentacao_controle_diario'                  , ()),
                    (0, 3, 'abnf000u13m02100_operacional_programacao_movimentacao_controle_diario'                  , ([11, 'btrelatx'], None)),
                    (0, 3, 'abnf000u13m02100_operacional_programacao_movimentacao_controle_diario'                  , ([11, 'btretvei'], [99, 2], [3, 'iidveicu', '775'], [3, 'ddataage', '2025-08-29'], [3, 'hseghage', '15:00'], [3, 'sdescrre', 'TESTE SISTEMA'], [3, 'istatret', '1'])),
                    (0, 3, 'abnf000u13m02100_operacional_programacao_movimentacao_controle_diario'                  , ([11, 'btalthoj'], [99, 2], [3, 'iidoprdi', '27934'], [3, 'iidveicu', '629'], [3, 'sobserva', 'TESTE 123'])),
                    (0, 3, 'abnf000u13m02100_operacional_programacao_movimentacao_controle_diario'                  , ([11, 'btrelatx'], [99, 1], [3, 'irelator', '11'], [3, 'ddataini', '2025-11-03'], [3, 'ddatafim', '2025-11-03'], [11, 'btgerrel'])),
                    (0, 3, 'abnf000u13m02100_operacional_programacao_movimentacao_controle_diario'                  , ([11, 'btrelatx'], [99, 1], [3, 'irelator', '5'], [3, 'ddataini', '2025-10-29'], [3, 'ddatafim', '2025-10-29'], [11, 'btgerrel'])),
                    (0, 3, 'abnf000u13m02100_operacional_programacao_movimentacao_controle_diario'                  , ([3, 'ddataesp', '2025-09-15'], [11, 'btaltesp'])),
                    # Entrada e saída de veículos
                    (0, 3, 'abnf000u13m03000_operacional_entrada_saida_veiculos'                                    , ([3, 'iidveicu', '608'], [3, 'ddataini', '2025-01-01'], [3, 'ddatafim', '2025-01-05'], [11, 'btbusreg'], [99, 2], [3, 'thoraesv', '04:02'], [3, 'stipomov', 'S'], [3, 'iodomvei', '192328'], [3, 'iidolinh', '96'], [3, 'iidmot01', '1360'], [11, 'btsalreg'])),
                    # Entrada e saída de veículos (testes de entradas e saída do veículo 12268 (ID 608)
                    (0, 3, 'abnf000u13m03000_operacional_entrada_saida_veiculos', (
                    [3, 'iidveicu', '608'],
                    # [11, 'btbusreg'], [99, 2],
                    # [3, 'thoraesv', '04:06'],
                    # [3, 'stipomov', 'S'],
                    # [3, 'iodomvei', '192330'],
                    # [3, 'irolevei', '100'],   
                    # [3, 'iidolinh', '96'],
                    # [3, 'iidmot01', '1360'], 
                    # [11, 'btsalreg']
                    # [11, 'btaltodo'], [99, 1],    # => Odômetro
                    # [11, 'btaltrol'], [99, 2],    # => Roleta
                    # [3, 'iodroatu', '89166'],
                    # [3, 'iodronov', '89140'],
                    # [3, 'iregis01', '17178'],
                    # [3, 'iregis02', '17125'],
                    # [11, 'btmodsav'], [99, 1],
                    # [11, 'btaltreg'],
                    # [3, 'iodroatu', '100'],
                    # [3, 'iodronov', '105'],
                    # [3, 'iregis01', '182682'],
                    # [3, 'iregis02', '182681'],
                    # [3, 'iregis01', '182680'],
                    # [3, 'iregis02', '182679'],
                    # [11, 'btmodsav'], [99, 1],
                    # [11, 'btaltreg'],
                    [3, 'ddataini', '2025-09-02'],
                    [3, 'ddatafim', '2025-10-31'], 
                    [11, 'btlisreg'], [99, 2],
                    )),
                    # Relatório de entrada e saída de veículos
                    (0, 3, 'abnf000u13r03000_operacional_entrada_saida_veiculos', (
                    [3, 'ddataini', '2025-10-01'],
                    [3, 'thoraini', '00:00'],
                    [3, 'ddatafim', '2025-10-05'],
                    [3, 'thorafim', '23:59'],
                    [3, 'itiporel', '2'],
                    [3, 'iformrel', '2'],
                    [11, 'bimpdcli'],
                    [11, 'bimprobs'],
                    [11, 'bimprusu'],
                    [11, 'btgerrel'],
                    )),
                    # API ITS-Transdata - Importação
                    (0, 3, 'abnf000u14m00100_transdata_its_importacao'                                              , ([3, 'ddataini', '2025-08-07'], [3, 'ddatafim', '2025-08-07'], [11, 'btimpdat'])),
                    # API ITS-Transdata - Relatório
                    (0, 3, 'abnf000u14r00100_transdata_its_analise'                                                 , ()),
                    (0, 3, 'abnf000u14r00100_transdata_its_analise'                                                 , ([3, 'ddataini', '2025-08-01'], [3, 'ddatafim', '2025-08-03'], [3, 'irelator', '18'])),
                ]
                for lauxi001 in lmodulos:
                    if lauxi001[0] == 1:
                        abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (
                            # =================================================
                            # ('iidusuar', 2),                                # ID do usuário
                            # ('slogiusu', 'ALEXANDRE.ABE'),                  # Login do usuário
                            # ('iidgrams', 1),                                # ID do grupo de acessos dos modulos do sistema (Administrador)
                            # =================================================
                            ('iidusuar', 61),                             # ID do usuário
                            ('slogiusu', 'JL.SOUZA'),                     # Login do usuário (Jean)
                            ('iidgrams', 8),                              # ID do grupo de acessos dos modulos do sistema (Operação)
                            # =================================================
                            ('ssenhusu', '123456'),                         # Senha do usuário
                            ('stipousu', 'O'),                              # Tipo de usuário: [A]dministrativo/[O]peracional
                            ('semaiusu', 'ALEXANDREABEINFO@GMAIL.COM'),     # Email do usuário
                            ('iidfotop', 3),                                # ID da foto do perfil
                            ('snomeusu', 'ALEXANDRE HIKARI ABE'),           # Nome completo do usuário
                            ('iidfilia', lauxi001[1]),                      # ID do filial
                            ('snomeemp', 'EMPRESA TESTE - ACESSO DIRETO'),  # Descricao da empresa
                            ('snomefil', 'FILIAL TESTE - ACESSO DIRETO'),   # Descricao da filial
                            ('sabnfsys', '13M00100B'),                      # sabnfsys (necessário somente quando o programa tiver mais de uma função)
                        )])
                        sauxi001 = lauxi001[2] + '(dabnfopg)'
                        # Debug: (inicio)
                        # abnf_show('05', sauxi001, 0)
                        # Debug: (fim)
                        eval(sauxi001)
                        for lauxi002 in lauxi001[3]:
                            if   lauxi002 == None: pass
                            elif lauxi002[0] <= 0: pass
                            elif lauxi002[0] == 99: time.sleep(lauxi002[1])
                            else: abnf_socket_004(lauxi002)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u00s00300_definicao_empresa_filial ] //////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Definição de empresa/filial.                                                                                                                        // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u00s00300_definicao_empresa_filial(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u00s00300_definicao_empresa_filial(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, '00S00301A'])
        # Criando lista de filiais:
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        lselectx = [(0, '')]
        scamposb = 'idempre, nomeemp, codiemp'
        sfilbusc = 'situreg != "C"'
        lsqlre01, iqtdre01 = abnf_database_busca_dados_v01(icodbase, 'abnf_sistema_empresas_matrizes', scamposb, sfilbusc, None)
        for lauxi001 in lsqlre01:
            scamposb = 'idfilia, nomefil, codifil'
            sfilbusc = 'situreg != "C" and idempre = ' + str(lauxi001[0])
            lsqlre02, iqtdre02 = abnf_database_busca_dados_v01(icodbase, 'abnf_sistema_empresas_filiais', scamposb, sfilbusc, None)
            for lauxi002 in lsqlre02:
                lselectx.append((
                    lauxi002[0],
                    lauxi001[1] + ' (' + str(lauxi001[2]) + ') - ' +
                    lauxi002[1] + ' (' + str(lauxi002[2]) + ')'
                ))
        # Atualização da página:
        snewpage = abnf_create_page([
            ('div-0', 'container', None, None),
            ('hr-0', None),
            ('div-0', 'row', None, None),
            ('div-0', 'col d-flex justify-content-center', None, None),
            ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
            ('legend-0', 'Definição de Empresa/Filial'),
            ('hr-0', None),
            ('label-0',  'Empresa/filial', 'form-control-label'),
            ('select-0', 'iidfilia', 'form-control', '16px', 'btbusreg', lselectx, 0, None, False),
            ('hr-0', None),
            ('button-0', 'btbusreg', 'btn btn-primary mt-2', 'Selecionar'),
            ('form-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
        ])
        abnf_socket_004([1, 'abnfdv03', snewpage])
        
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u00s00301_definicao_empresa_filial ] //////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Definição de empresa/filial.                                                                                                                        // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u00s00301_definicao_empresa_filial(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u00s00301_definicao_empresa_filial(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        lmfields = [
            ['iidfilia', 'select', 'F', 'empresa/filial', ['Notnull', 'D'], None],
        ]
        bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btbusreg')
        if bvalidad:
            abnf_alert('Aguarde...', 6)
            iidfilia = lmfields[0][5]
            # abnf_show('10', iidfilia, 0)
            icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
            # Análise da filial selecionada:
            scamposb = 'idfilia, nomefil, codifil, idempre, situreg'
            sfilbusc = 'situreg != "C" and idfilia = ' + str(iidfilia)
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v01(icodbase, 'abnf_sistema_empresas_filiais', scamposb, sfilbusc, None)
            if lsqlre01 == '[]' or iqtdre01 == 0:
                abnf_alert('O registro ID da filial não foi encontrado! Entre em contato com o departamento de sistemas!', 4)
                abnf_socket_004([5, 'btbusreg'])
            elif lsqlre01[0][4] == 'C':
                abnf_alert('Esta filial foi excluída por outro operador!', 5)
                abnf_socket_004([5, 'btbusreg'])
            elif lsqlre01[0][4] == 'I':
                abnf_alert('Esta filial esta inativa!', 5)
                abnf_socket_004([5, 'btbusreg'])
            else:
                # Análise da matriz selecionada:
                iidempre = lsqlre01[0][3]
                scamposb = 'idempre, nomeemp, codiemp, situreg'
                sfilbusc = 'situreg != "C" and idempre = ' + str(iidempre)
                lsqlre02, iqtdre02 = abnf_database_busca_dados_v01(icodbase, 'abnf_sistema_empresas_matrizes', scamposb, sfilbusc, None)
                if lsqlre02 == '[]' or iqtdre02 == 0:
                    abnf_alert('O registro ID da matriz não foi encontrado! Entre em contato com o departamento de sistemas!', 4)
                    abnf_socket_004([5, 'btbusreg'])
                elif lsqlre02[0][3] == 'C':
                    abnf_alert('Esta matriz foi excluída por outro operador!', 5)
                    abnf_socket_004([5, 'btbusreg'])
                elif lsqlre02[0][3] == 'I':
                    abnf_alert('Esta matriz esta inativa!', 5)
                    abnf_socket_004([5, 'btbusreg'])
                else:
                    abnf_alert('Empresa/filial definida com sucesso!', 3)
                    # Busca registro em dglobdws:
                    dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
                    # Registra o log:
                    abnf_websocket_log(
                        sabnproj[14:],
                        200,
                        'abnf_sistema_usuarios',
                        'idusuar',
                        dglobaux['iidusuar'],   # ID do usuário
                        dglobaux['slogiusu'],   # Login do usuário
                        dglobaux['snomeusu'],   # Nome completo do usuário
                        'Usuario selecionou uma empresa/filial',
                        [
                            ('abnf_sistema_empresas_matrizes', 'idempre', lsqlre02[0][0], 'ID da empresa',        None, None, None),
                            ('abnf_sistema_empresas_matrizes', 'codiemp', lsqlre02[0][2], 'Codigo da empresa',    None, None, None),
                            ('abnf_sistema_empresas_matrizes', 'nomeemp', lsqlre02[0][1], 'Descricao da empresa', None, None, None),
                            ('abnf_sistema_empresas_filiais',  'idfilia', lsqlre01[0][0], 'ID do filial',         None, None, None),
                            ('abnf_sistema_empresas_filiais',  'codifil', lsqlre01[0][2], 'Codigo da filial',     None, None, None),
                            ('abnf_sistema_empresas_filiais',  'nomefil', lsqlre01[0][1], 'Descricao da filial',  None, None, None),
                        ]
                    )
                    # Atualiza dados em dglobdws:
                    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (
                        ('iidfilia', lsqlre01[0][0]),   # ID do filial
                        ('snomeemp', lsqlre02[0][1]),   # Descricao da empresa
                        ('snomefil', lsqlre01[0][1]),   # Descricao da filial
                    )])
                    # Apaga todos o conteúdo da DIV usada para a seleção da empresa:
                    abnf_socket_004([1, 'abnfdv03', ''])
                    # Chama o módulo sequêncial:
                    abnf_websocket_define_menu_usuario(dabnfopg)
                    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u00s00400_perfil ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Perfil - Tela principal.                                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u00s00400_perfil(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u00s00400_perfil(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, '00S00401A'])
        if   dglobaux['ssenhusu'] == 'MUDAR@123':   abnf_alert('Altere sua senha!', 5)
        elif dglobaux['semaiusu'] == None:          abnf_alert('Defina seu e-mail!', 5)
        elif dglobaux['iidfotop'] == None:          abnf_alert('Defina sua foto de perfil!', 5)
        elif dglobaux['iidfilia'] == 0:             # Ainda não foi definido nenhuma empresa/filial
            # ****************
            # Nota: 04/07/2024
            # O método abaixo funcionou perfeitamente para redirecionar o sistema para a tela de seleção de empresa/filia.
            # Foi o mesmo que chamar a função direto só que dessa forma abaixo passamos por "abnf_tratamento_websockets_recebidos(dabnfopg)"
            # a qual é a função que tem poder de chamar todas as demais. Se este método funcionar, podemos deixa-lo como padrão para todos e
            # criar em "abnf_tratamento_websockets_recebidos(dabnfopg)" um método de log que vai servir para acesso a todos os módulos.
            # Lembrando que nesse sistema somente vamos registrar no log o acesso aos módulos e não mais a cada processo interno feito dentro deles.
            # Além dos acessos, pretendemos registrar log de inclusão e alteração de registros. Com isso vai gerar menos "poluição" nos arquivos de log.
            # ****************
            dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, '00S00300A'])
            abnf_tratamento_websockets_recebidos(dabnfopg)
            return
        # Analisar os dados recebidos (debug):
        # abnf_websocket_mostra_dicionario(dabnfopg, 0)
        # abnf_websocket_mostra_dicionario(dglobaux, 10)
        # ****************
        # Nota: 04/04/2024
        # Aqui estamos tendo um problema pela demora da conversão do arquivo pela função "abnf_websocket_converte_arquivo_imagem_base64".
        # Temos que testar leitura com link direto do arquivo para analisar se vai ficar mais rapido.
        # ****************
        # Define o local de documentos do projeto
        sldocpro = abnf_websocket_local_docs(sabnproj)
        # Buscar a foto do usuário:
        # simage01 = '<img src="/static/abnfarc/abnfsyst000000001.jpg" class="rounded mx-auto d-block" width="200">'
        simage01 = ''
        if dglobaux['iidfotop'] == None:
            simage01 = abnf_websocket_converte_arquivo_imagem_base64('abnfsrc/static/abnftmp/abnfsyst000000001.jpg', 'rounded mx-auto d-block', '35%', '35%')
        else:
            icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
            scamposb = 'nomearq'
            sfilbusc = 'idarqui = ' + str(dglobaux['iidfotop'])
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v01(icodbase, 'abnf_sistema_arquivos', scamposb, sfilbusc, None)
            if lsqlre01 == '[]' or iqtdre01 == 0:
                simage01 = abnf_websocket_converte_arquivo_imagem_base64('abnfsrc/static/abnftmp/abnfsyst000000001.jpg', 'rounded mx-auto d-block', '35%', '35%')
            else:
                sarqimag = sldocpro + lsqlre01[0][0]
                # abnf_alert(sarqimag, 8)
                # ****************
                # Nota: 08/07/2024
                # Abaixo as duas formas de visualização de arquivo de imagem:
                # 1) Visualização normal com hiperlink o que possibilita conhecer o caminho do arquivo no servidor.
                # 2) Codificando o arquivo em base64 o que torna mais lento mas o local do arquivo fica totalmente oculto.
                # O problema de usar o método "1)" é que o arquivo tem que ficar dentro da pasta "static".
                # A unica forma de deixar fora é crindo um "apontador" para a pasta desejada conforme instruções abaixo:
                # 1) Dentro da pasta "static" criar a pasta "/abnfdoc" .: mkdir "/flexabeinfo/abnfsrc/static/abnfdoc/"
                # 2) Criar o apontamento para a pasta criada ...........: ln -s "/flexabeinfo/abnfdoc/003/" "abnfdoc/"
                # ****************
                simage01 = abnf_websocket_converte_arquivo_imagem_base64(sarqimag, 'rounded mx-auto d-block', '35%', '35%')
                # simage01 = abnf_websocket_arquivo_imagem(sarqimag, 'rounded mx-auto d-block', '35%', '35%')
        # Atualização da página:
        lnewpage = [
            ('div-0', 'container', None, None),
            ('hr-0', None),
            ('div-0', 'row', None, None),
            ('div-0', 'col d-flex justify-content-center', None, None),
            ('div-0', 'w-50 p-3', 'background-color: #eee;', None),
            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
            ('legend-0', 'Perfil'),
            ('hr-0', None),
            ('div-0', 'img-responsive mt-2 d-flex flex-row align-items-center w-100', None, simage01),
            ('div-9', None),
            ('hr-0', None),
            ('hx-0', 4, 'mb-0 mt-0 text-center', '30px', 'blue', dglobaux['snomeusu']),
            ('hx-0', 6, 'mb-0 mt-0 text-center', '25px', 'brown', dglobaux['slogiusu']),
        ]
        if dglobaux['semaiusu'] != None: lnewpage = lnewpage + [
            ('hx-0', 6, 'mb-0 mt-0 text-center', '18px', '#8B008B', dglobaux['semaiusu']),
        ]
        lnewpage = lnewpage + [
            ('hr-0', None),
            ('div-0', 'mb-0 mt-0 text-center', None, None),
        ]
        lnewpage = lnewpage + [
            ('alt255-0', 1),
            ('button-0', 'btbaltse', 'btn btn-primary mt-2', 'Alterar senha'),
            ('alt255-0', 1),
        ]
        if dglobaux['ssenhusu'] != 'MUDAR@123': lnewpage = lnewpage + [
            ('alt255-0', 1),
            ('button-0', 'btbaltem', 'btn btn-primary mt-2', 'Alterar email'),
            ('alt255-0', 1),
        ]
        if dglobaux['ssenhusu'] != 'MUDAR@123' and dglobaux['semaiusu'] != None: lnewpage = lnewpage + [
            ('alt255-0', 1),
            ('button-0', 'btbaltfp', 'btn btn-primary mt-2', 'Alterar foto do perfil'),
            ('alt255-0', 1),
        ]    
        lnewpage = lnewpage + [
            ('div-9', None),
            ('form-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
        ]
        snewpage = abnf_create_page(lnewpage)
        abnf_socket_004([1, 'abnfdv03', snewpage])
        
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u00s00401_perfil ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Perfil - Tela de alteração.                                                                                                                         // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u00s00401_perfil(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u00s00401_perfil(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, '00S00402A'])
        # Analisar os dados recebidos (debug):
        # abnf_websocket_mostra_dicionario(dabnfopg, 0)
        # abnf_websocket_mostra_dicionario(dglobaux, 10)
        lnewpage = [
            ('div-0', 'container', None, None),
            ('hr-0', None),
            ('div-0', 'row', None, None),
            ('div-0', 'col d-flex justify-content-center', None, None),
            ('div-0', 'w-50 p-3', 'background-color: #eee;', None),
            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
        ]
        if dabnfopg['abnfobj0'] == ['btbaltse', 'btbaltse']: # Alterar senha
            lnewpage = lnewpage + [
                ('legend-0', 'Perfil - [ Alterar senha ]'),
                ('hr-0', None),
                ('label-0',    'Senha atual', 'form-control-label'),
                ('password-0', 'ssenhdig', 'form-control', 6, 30, '16px', None, 'ssenhnov', True, 0),
                ('label-0',    'Nova senha', 'form-control-label'),
                ('password-0', 'ssenhnov', 'form-control', 6, 30, '16px', None, 'ssenhcon', True, 0),
                ('label-0',    'Confirmação da nova senha', 'form-control-label'),
                ('password-0', 'ssenhcon', 'form-control', 6, 30, '16px', None, 'btmodsav', True, 0),
            ]
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (
                ('saltperf', 'S'),  # Alteração de senha
            )])
        elif dabnfopg['abnfobj0'] == ['btbaltem', 'btbaltem']: # Alterar e-mail
            lnewpage = lnewpage + [
                ('legend-0', 'Perfil - [ Alterar e-mail ]'),
                ('hr-0', None),
                ('label-0',    'E-mail' , 'form-control-label'),
                ('input-0',    'semainov', 'form-control', 0, 60, '16px', None, 'semaicon', True, 0),
                ('label-0',    'Confirmação do e-mail' , 'form-control-label'),
                ('input-0',    'semaicon', 'form-control', 0, 60, '16px', None, 'ssenhdig', True, 0),
                ('label-0',    'Senha no sistema', 'form-control-label'),
                ('password-0', 'ssenhdig', 'form-control', 6, 30, '16px', None, 'btmodsav', True, 0),
            ]
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (
                ('saltperf', 'E'),  # Alteração de e-mail
            )])
        elif dabnfopg['abnfobj0'] == ['btbaltfp', 'btbaltfp']: # Alterar foto do perfil
            # Define o local de documentos do projeto
            sldocpro = abnf_websocket_local_docs(sabnproj)
            # Buscar a foto do usuário:
            if dglobaux['iidfotop'] == None:
                simage01 = abnf_websocket_converte_arquivo_imagem_base64('abnfsrc/static/abnftmp/abnfsyst000000001.jpg', 'rounded mx-auto d-block', '35%', '35%')
            else:
                icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
                scamposb = 'nomearq'
                sfilbusc = 'idarqui = ' + str(dglobaux['iidfotop'])
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v01(icodbase, 'abnf_sistema_arquivos', scamposb, sfilbusc, None)
                if lsqlre01 == '[]' or iqtdre01 == 0:
                    simage01 = abnf_websocket_converte_arquivo_imagem_base64('abnfsrc/static/abnftmp/abnfsyst000000001.jpg', 'rounded mx-auto d-block', '35%', '35%')
                else:
                    sarqimag = sldocpro + lsqlre01[0][0]
                    # abnf_alert(sarqimag, 8)
                    simage01 = abnf_websocket_converte_arquivo_imagem_base64(sarqimag, 'rounded mx-auto d-block', '35%', '35%')
            lnewpage = lnewpage + [
                ('legend-0', 'Perfil - [ Alterar foto do perfil ]'),
                ('hr-0', None),
                ('div-0', 'img-responsive mt-2 d-flex flex-row align-items-center w-100', None, simage01),
                ('div-9', None),
                ('hr-0', None),
                ('div-0', 'form-group', None, None),
                ('label-0', 'Atualizar foto de perfil', None),
                # ('br-0', None),
                ('file-0', 'ffotousu', 'btn btn-primary mt-2', '.jpg,.png,.bmp', False, True),
                ('div-9', None),
                ('hr-0', None),
                ('label-0', 'Senha no sistema', 'form-control-label'),
                ('password-0', 'ssenhdig', 'form-control', 6, 30, '16px', None, 'btmodsav', True, 0),
            ]
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (
                ('saltperf', 'F'),  # Alteração de foto
            )])
        # Botães de salvar ou cancelar as alterações
        lnewpage = lnewpage + [
            ('hr-0', None),
            ('div-0', 'mb-0 mt-0 text-center', None, None),
            ('alt255-0', 1),
            ('button-1', 'btmodsav', 'btn btn-primary mt-2', 'Salvar', 'Salvar Registro', 'btsalreg', 'btn btn-primary mt-2', 'Salvar', 'Confirma a gravação das alterações?'),
            ('alt255-0', 2),
            ('button-0', 'btcancel', 'btn btn-primary mt-2', 'Cancelar'),
            ('alt255-0', 1),
            ('div-9', None),
            ('form-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
        ]
        snewpage = abnf_create_page(lnewpage)
        abnf_socket_004([1, 'abnfdv03', snewpage])
        # Debug: (inicio)
        # abnf_socket_004([3, 'ssenhnov', 'SEGUNDA000'])
        # abnf_socket_004([3, 'ssenhcon', 'SEGUNDA000'])
        # abnf_socket_004([3, 'semainov', 'ALEXANDRE@TESTE.COM'])
        # abnf_socket_004([3, 'semaicon', 'ALEXANDRE@TESTE.COM'])
        # abnf_socket_004([3, 'ssenhdig', 'TESTE123'])
        # Debug: (fim)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u00s00402_perfil ] ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Perfil - Tela de confirmação de ação.                                                                                                               // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u00s00402_perfil(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u00s00402_perfil(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, '00S00402A'])
        # Analisar os dados recebidos (debug):
        # abnf_websocket_mostra_dicionario(dabnfopg, 0)
        # abnf_websocket_mostra_dicionario(dglobaux, 10)
        if dabnfopg['abnfobj0'] == ['btcancel', 'btcancel']:
            abnf000u00s00400_perfil(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btsalreg', 'btsalreg']:
            if dglobaux['saltperf'] == 'S':     # Alteração de senha
                lmfields = [
                    ['ssenhdig', 'input', 'F', 'senha atual',               ['Notnull', 'P'], None],
                    ['ssenhnov', 'input', 'F', 'nova senha',                ['Notnull', 'P'], None],
                    ['ssenhcon', 'input', 'F', 'confirmação da nova senha', ['Notnull', 'P'], None],
                ]
                bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btacesso')
                if bvalidad:
                    abnf_alert('Aguarde...', 6)
                    ssenhdig = lmfields[0][5]
                    ssenhnov = lmfields[1][5]
                    ssenhcon = lmfields[2][5]
                    lmrulesx = [
                        ['nps', ssenhnov, 'F', 'nova senha', 'MUDAR@123' ],
                        ['equ', ssenhnov, 'F', 'nova senha', ssenhcon, 'F', 'confirmação da nova senha' ],
                    ]
                    bvalidad = abnf_check_rules_fields(lmrulesx, 'btacesso')
                    if bvalidad:
                        iidusuar = dglobaux['iidusuar']
                        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
                        scamposb = 'senhusu'
                        sfilbusc = 'idusuar = ' + str(iidusuar) + ' and situreg = "A";'
                        lsqlre01, iqtdre01 = abnf_database_busca_dados_v01(icodbase, 'abnf_sistema_usuarios', scamposb, sfilbusc, None)
                        if lsqlre01 == '[]' or iqtdre01 == 0:
                            abnf_alert('O registro ID ' + str(iidusuar) + ' não foi encontrado! Entre em contato com o departamento de sistemas!', 4)
                        else:
                            if len(ssenhnov) < 6:
                                abnf_alert('A nova senha tem que ter de 6 a 30 caracteres!', 5)
                            else:
                                ssenhusu = lsqlre01[0][0]
                                bvalidad = False
                                if ssenhusu == 'MUDAR@123':
                                    if ssenhdig != 'MUDAR@123':
                                        abnf_alert('A senha atual está incorreta!', 5)
                                    else:
                                        bvalidad = True
                                else:        
                                    if not abnfbcry.check_password_hash(ssenhusu, ssenhdig):
                                        abnf_alert('A senha atual está incorreta!', 5)
                                    else:
                                        bvalidad = True
                                if bvalidad:
                                    ssecript = abnfbcry.generate_password_hash(ssenhnov).decode("utf-8")
                                    bvalidad = abnf_database_altera_dados_v01(icodbase, sabnproj, 'abnf_sistema_usuarios', 'M', 'cadastro de usuarios do sistema', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                                        [
                                            ('idusuar', 'I', iidusuar,  'ID do registro'),
                                            ('situreg', 'S', 'A',       'Situacao do registro'),
                                        ],
                                        [   
                                            ('senhusu', 'S', ssecript,  'Senha do usuario'),
                                        ]
                                    )
                                    if bvalidad:
                                        abnf_alert('Nova senha gravada com sucesso!', 3)
                                        # Atualiza dados em dglobdws:
                                        abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (
                                            ('ssenhusu', ssecript),   # Senha (necessário quando a senha anterior era 'MUDAR@123')
                                        )])
                                        abnf000u00s00400_perfil(dabnfopg)
            elif dglobaux['saltperf'] == 'E':   # Alteração de e-mail
                lmfields = [
                    ['semainov', 'input', 'M', 'e-mail',                ['Notnull', 'P'], None],
                    ['semaicon', 'input', 'F', 'confirmação do e-mail', ['Notnull', 'P'], None],
                    ['ssenhdig', 'input', 'F', 'senha do sistema',      ['Notnull', 'P'], None],
                ]
                bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btacesso')
                if bvalidad:
                    abnf_alert('Aguarde...', 6)
                    semainov = lmfields[0][5]
                    semaicon = lmfields[1][5]
                    ssenhdig = lmfields[2][5]
                    lmrulesx = [
                        ['eml', semainov, 'M', 'e-mail' ],
                        ['eml', semaicon, 'F', 'confirmação do e-mail' ],
                        ['equ', semainov, 'M', 'e-mail', semaicon, 'F', 'confirmação do e-mail' ],
                    ]
                    bvalidad = abnf_check_rules_fields(lmrulesx, 'btacesso')
                    if bvalidad:
                        iidusuar = dglobaux['iidusuar']
                        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
                        scamposb = 'senhusu'
                        sfilbusc = 'idusuar = ' + str(iidusuar) + ' and situreg = "A";'
                        lsqlre01, iqtdre01 = abnf_database_busca_dados_v01(icodbase, 'abnf_sistema_usuarios', scamposb, sfilbusc, None)
                        if lsqlre01 == '[]' or iqtdre01 == 0:
                            abnf_alert('O registro ID ' + str(iidusuar) + ' não foi encontrado! Entre em contato com o departamento de sistemas!', 4)
                        else:
                            ssenhusu = lsqlre01[0][0]
                            if ssenhusu == 'MUDAR@123':
                                abnf_alert('A senha provisória ainda não foi alterada!', 5)
                            else:
                                if not abnfbcry.check_password_hash(ssenhusu, ssenhdig):
                                    abnf_alert('A senha no sistema está incorreta!', 5)
                                else:
                                    bvalidad = abnf_database_altera_dados_v01(icodbase, sabnproj, 'abnf_sistema_usuarios', 'M', 'cadastro de usuarios do sistema', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                                        [
                                            ('idusuar', 'I', iidusuar,  'ID do registro'),
                                            ('situreg', 'S', 'A',       'Situacao do registro'),
                                        ],
                                        [   
                                            ('emaiusu', 'S', semainov,  'E-mail do usuario'),
                                        ]
                                    )
                                    if bvalidad:
                                        abnf_alert('Novo e-mail gravado com sucesso!', 3)
                                        # Atualiza dados em dglobdws:
                                        abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (
                                            ('semaiusu', semainov),   # Email do usuário
                                        )])
                                        abnf000u00s00400_perfil(dabnfopg)
            elif dglobaux['saltperf'] == 'F':   # Alteração de foto
                lmfields = [
                    ['ffotousu', 'file',  'F', 'foto de perfil',   ['Notnull', 'D'], None],
                    ['ssenhdig', 'input', 'F', 'senha do sistema', ['Notnull', 'P'], None],
                ]
                bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btacesso')
                if bvalidad:
                    abnf_alert('Aguarde...', 6)
                    ssenhdig = lmfields[1][5]
                    iidusuar = dglobaux['iidusuar']
                    icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
                    scamposb = 'senhusu'
                    sfilbusc = 'idusuar = ' + str(dglobaux['iidusuar']) + ' and situreg = "A";'
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v01(icodbase, 'abnf_sistema_usuarios', scamposb, sfilbusc, None)
                    if lsqlre01 == '[]' or iqtdre01 == 0:
                        abnf_alert('O registro ID ' + str(dglobaux['iidusuar']) + ' não foi encontrado! Entre em contato com o departamento de sistemas!', 4)
                    else:
                        ssenhusu = lsqlre01[0][0]
                        if ssenhusu == 'MUDAR@123':
                            abnf_alert('A senha provisória ainda não foi alterada!', 5)
                        else:
                            if not abnfbcry.check_password_hash(ssenhusu, ssenhdig):
                                abnf_alert('A senha no sistema está incorreta!', 5)
                            else:
                                abnf_socket_004([6, 'ffotousu'])
                                bvalidad, larqsupl = abnf_database_salva_arquivos_upload(
                                    icodbase,               # Codigo banco
                                    sabnproj,               # Projeto
                                    sabntoke,               # Token
                                    dglobaux['iidusuar'],   # id do usuário
                                    dglobaux['slogiusu'],   # login do usuário
                                    dglobaux['snomeusu'],   # Nome completo do usuário
                                    600,                    # itimesle (tempo em segundos da espera pelo fim do(s) upload(s)
                                    False                   # Multiplos arquivos
                                )
                                if bvalidad:
                                    iidfotop = larqsupl[0][3]  # ID do arquivo que foi inserido no sistema
                                    bvalidad = abnf_database_altera_dados_v01(icodbase, sabnproj, 'abnf_sistema_usuarios', 'M', 'cadastro de usuarios do sistema', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                                        [
                                            ('idusuar', 'I', iidusuar,  'ID do registro'),
                                            ('situreg', 'S', 'A',       'Situacao do registro'),
                                        ],
                                        [   
                                            ('idfotop', 'S', iidfotop,  'ID da foto do perfil'),
                                        ]
                                    )
                                    if bvalidad:
                                        abnf_alert('Foto de perfil gravada com sucesso!', 3)
                                        # Atualiza dados em dglobdws:
                                        abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (
                                            ('iidfotop', iidfotop),   # Foto de perfil
                                        )])
                                        abnf000u00s00400_perfil(dabnfopg)
        
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_websocket_define_menu_usuario ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que monta o menu personalizado para cada usuário.                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// # 

def abnf_websocket_define_menu_usuario(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf_websocket_define_menu_usuario(iidfilia, iidgrams, stipousu)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        dultiuso = dglobaux['dultiuso']
        sabnfsys = dglobaux['sabnfsys']
        iidusuar = dglobaux['iidusuar']
        iidfilia = dglobaux['iidfilia']
        snomeemp = dglobaux['snomeemp']
        snomefil = dglobaux['snomefil']
        slogiusu = dglobaux['slogiusu']
        snomeusu = dglobaux['snomeusu']
        iidgrams = dglobaux['iidgrams']
        stipousu = dglobaux['stipousu']
        # /// #
        lmenusis = [
            (None,1,"Prontuário",(
                (None,1,"Cadastros gerais",(
                    ('01C00600A',0,"Clientes",                                              None), # ==> abnf000u01c00600_cadastro_clientes_fornecedores
                    ('01C00600B',0,"Fornecedores",                                          None), # ==> abnf000u01c00600_cadastro_clientes_fornecedores
                    ('01C00400A',0,"CPF",                                                   None), # ==> abnf000u01c00400_cadastro_cpf
                    ('01C00500A',0,"CNPJ",                                                  None), # ==> abnf000u01c00500_cadastro_cnpj
                    ('01C00300A',0,"Logradouros",                                           None), # ==> abnf000u01c00300_cadastro_logradouros
                    ('01C00200A',0,"Bairros",                                               None), # ==> abnf000u01c00200_cadastro_bairros
                    ('01C00100A',0,"Cidades",                                               None), # ==> abnf000u01c00100_cadastro_cidades
                    ('01C00700A',0,"Espécies de documentos",                                None), # ==> abnf000u01c00700_cadastro_especies_documentos
                )),
                (None,1,"Veículos",(
                    ('02C00100A',0,"Marcas",                                                None), # ==> abnf000u02c00100_cadastro_veiculos_marcas
                    ('02C00200A',0,"Modelos",                                               None), # ==> abnf000u02c00200_cadastro_veiculos_modelos
                    ('02C00300A',0,"Veículos",                                              None), # ==> abnf000u02c00300_cadastro_veiculos
                )),
                (None,1,"Funcionários",(
                    ('03C00100A',0,"Cargos",                                                None), # ==> abnf000u03c00100_cadastro_funcionarios_cargos
                    ('03C00200A',0,"Funcionários",                                          None), # ==> abnf000u03c00200_cadastro_funcionarios
                )),
            )),
            (None,1,"Almoxarifado",(
                (None,1,"Cadastros",(
                    ('04C00500A',0,"Medidores de produtos",                                 None), # ==> abnf000u04c00500_almoxarifado_cadastro_medidores_produtos
                )),
                (None,1,"Lançamentos",(
                    ('04M00200A',0,"Requisições",                                           None), # ==> abnf000u04m00200_almoxarifado_movimentacao_requisicoes
                    ('04M00600A',0,"Reabertura de documentos",                              None), # ==> abnf000u04m00600_almoxarifado_movimentacao_reabertura_documentos
                    ('04M00700A',0,"Alteração de odômetros de veículos",                    None), # ==> abnf000u04m00700_almoxarifado_movimentacao_alteracao_odometros_veiculos(dabnfopg)
                )),
                (None,1,"Relatórios",(
                    ('04R00200A',0,"Requisições",                                           None), # ==> abnf000u04r00200_almoxarifado_relatorio_requisicoes
                    ('04R00600A',0,"Movimentação de produtos e serviços",                   None), # ==> abnf000u04r00600_almoxarifado_relatorio_movimentacao_produtos_servicos
                    ('04R00700A',0,"Consumo de produtos e serviços por veículo",            None), # ==> abnf000u04r00700_almoxarifado_relatorio_consumo_produtos_servicos_veiculo
                    # ('04R00900A',0,"Relatório Contábil de Estoque",                         None), # ==> abnf000u04r00900_almoxarifado_relatorio_contabil_estoque
                )),
            )),
            (None,1,"Manutenção",(
                (None,1,"Controle de manutenção",(
                    (None,1,"Lançamentos",(
                        ('04M00500A',0,"Medidores de produtos",                             None), # ==> abnf000u04m00500_almoxarifado_movimentacao_medidores_produtos
                        ('04M00300A',0,"Consumo em lote",                                   None), # ==> abnf000u04m00300_almoxarifado_movimentacao_consumo_lote
                    )),
                    (None,1,"Relatórios",(
                        ('04R00800A',0,"Medidores de produtos e consumo",                   None), # ==> abnf000u04r00800_almoxarifado_relatorio_medidores_produtos_consumo
                    )),
                    (None,1,"Preventiva",(
                        ('05C00100A',0,"Grupos de preventiva",                              None), # ==> abnf000u05c00100_preventiva_cadastro_grupos
                        ('05C00200A',0,"Ítens de preventiva",                               None), # ==> abnf000u05c00200_preventiva_cadastro_itens
                        ('05C00300A',0,"Associação: Ítens x Grupos",                        None), # ==> abnf000u05c00300_preventiva_cadastro_associacao_itens_grupos
                        ('05C00400A',0,"Associação: Veículos x Grupos",                     None), # ==> abnf000u05c00400_preventiva_cadastro_associacao_veiculos_grupos
                        ('05M00100A',0,"Ação de preventiva",                                None), # ==> abnf000u05m00100_preventiva_acao_preventiva
                        ('05R00100A',0,"Relatório de preventivas",                          None), # ==> abnf000u05r00100_preventiva_relatorios_preventivas
                    )),                    
                )),
            )),
            (None,1,"Notas Fiscais",(
                (None,1,"Cadastros",(
                    ('04C00100A',0,"Grupos de produtos e serviços",                         None), # ==> abnf000u04c00100_almoxarifado_cadastro_produtos_servicos_grupos
                    ('04C00200A',0,"Subgrupos de produtos e serviços",                      None), # ==> abnf000u04c00200_almoxarifado_cadastro_produtos_servicos_subgrupos
                    ('04C00300A',0,"Marcas de produtos e serviços",                         None), # ==> abnf000u04c00300_almoxarifado_cadastro_produtos_servicos_marcas
                    ('04C00400A',0,"Produtos e serviços",                                   None), # ==> abnf000u04c00400_almoxarifado_cadastro_produtos_servicos
                )),
                (None,1,"Lançamentos",(
                    ('04M00100B',0,"Notas fiscais - Contas a pagar",                        None), # ==> abnf000u04m00100_almoxarifado_movimentacao_notas_fiscais
                    ('04M00100A',0,"Notas fiscais - Contas a receber",                      None), # ==> abnf000u04m00100_almoxarifado_movimentacao_notas_fiscais
                    ('04M00600A',0,"Reabertura de documentos",                              None), # ==> abnf000u04m00600_almoxarifado_movimentacao_reabertura_documentos
                    # ('04M01000A',0,"Reabertura de notas fiscais",                         None), # ==> abnf000u04m01000_almoxarifado_movimentacao_notas_fiscais_reabertura
                )),
                (None,1,"Relatórios",(
                    ('04R00100B',0,"Notas fiscais - Contas a pagar",                        None), # ==> abnf000u04r00100_almoxarifado_relatorio_notas_fiscais
                    ('04R00100A',0,"Notas fiscais - Contas a receber",                      None), # ==> abnf000u04r00100_almoxarifado_relatorio_notas_fiscais
                )),
            )),
            (None,1,"Financeiro",(
                (None,1,"Cadastros",(
                    ('08C00100A',0,"Contas financeiras",                                    None), # ==> abnf000u08c00100_financeiro_cadastro_contas_financeiras
                    ('08C00200A',0,"Grupos financeiros",                                    None), # ==> abnf000u08c00200_financeiro_cadastro_grupos
                    ('08C00300A',0,"Subgrupos financeiros",                                 None), # ==> abnf000u08c00300_financeiro_cadastro_subgrupos
                    ('08C00400A',0,"Complementos",                                          None), # ==> abnf000u08c00500_financeiro_cadastro_complementos
                    ('08C00500A',0,"Centros de custo",                                      None), # ==> abnf000u08c00500_financeiro_cadastro_centros_custo
                    ('08C00600A',0,"Departamentos",                                         None), # ==> abnf000u08c00600_financeiro_cadastro_departamentos
                )),
                (None,1,"Lançamentos",(
                    ('08M00100A',0,"Registros financeiros",                                 None), # ==> abnf000u08m00100_financeiro_movimentacao_registros_financeiros
                    ('08M00200A',0,"Conciliação financeira",                                None), # ==> abnf000u08m00200_financeiro_movimentacao_conciliacao_financeira
                    ('08M00300A',0,"Tranferência entre contas",                             None), # ==> abnf000u08m00300_financeiro_movimentacao_transferencia_entre_contas
                    ('08M00400A',0,"Lançamento direto em conta",                            None), # ==> abnf000u08m00400_financeiro_movimentacao_lancamento_direto_conta
                    ('08M00500A',0,"Alterar filiais em registros financeiros",              None), # ==> abnf000u08m00500_financeiro_movimentacao_alterar_filiais_registros_financeiros
                )),
                (None,1,"Relatórios",(
                    ('08R00100A',0,"Extrato de contas",                                     None), # ==> abnf000u08r00100_financeiro_relatorio_extrato_contas
                    ('08R00200A',0,"Contas a pagar",                                        None), # ==> abnf000u08r00200_financeiro_relatorio_contas_pagar_receber
                    ('08R00200B',0,"Contas a receber",                                      None), # ==> abnf000u08r00200_financeiro_relatorio_contas_pagar_receber
                    ('08R00200C',0,"Contas pagas",                                          None), # ==> abnf000u08r00200_financeiro_relatorio_contas_pagar_receber
                    ('08R00200D',0,"Contas recebidas",                                      None), # ==> abnf000u08r00200_financeiro_relatorio_contas_pagar_receber
                )),
            )),
            (None,1,"SAC",(
                (None,1,"Cadastros",(
                    ('11C00300A',0,"Grupos de atendimentos",                                None), # ==> abnf000u11c00300_sac_cadastro_atendimentos_grupos
                    ('11C00400A',0,"Subgrupos de atendimentos",                             None), # ==> abnf000u11c00400_sac_cadastro_atendimentos_subgrupos
                    ('11C00500A',0,"Grupos de usuários",                                    None), # ==> abnf000u11c00500_sac_cadastro_usuarios_grupos
                )),
                (None,1,"Relatórios",(
                    ('11R00100A',0,"Visualização geral de atendimentos",                    None), # ==> abnf000u11r00100_sac_relatorio_visualizacao_geral_atendimentos
                    ('11R00200A',0,"Atendimentos aos usuários",                             None), # ==> abnf000u11r00200_sac_relatorio_atendimentos_usuarios
                )),
            )),
            (None,1,"SIGOM",(
                (None,1,"Relatórios",(
                    ('12R00100A',0,"Visualização geral de ocorrências",                     None), # ==> abnf000u12r00100_sigom_visualizacao_geral_ocorrencias
                )),
            )),
            (None,1,"Operacional",(
                (None,1,"Cadastros",(
                    ('13C00100A',0,"Locais",                                                None), # ==> abnf000u13c00100_operacional_cadastro_locais
                    ('13C00200A',0,"Grupos de linhas",                                      None), # ==> abnf000u13c00200_operacional_cadastro_grupos_linhas
                    ('13C00300A',0,"Linhas",                                                None), # ==> abnf000u13c00300_operacional_cadastro_linhas
                    ('13C00400A',0,"Projetos",                                              None), # ==> abnf000u13c00400_operacional_cadastro_projetos
                    ('13C00500A',0,"Trajetos",                                              None), # ==> abnf000u13c00500_operacional_cadastro_trajetos
                    ('13C00600A',0,"Itinerários",                                           None), # ==> abnf000u13c00600_operacional_cadastro_itinerarios
                    ('13C00700A',0,"Grupos de veículos",                                    None), # ==> abnf000u13c00700_operacional_cadastro_grupos_veiculos
                    ('13C00800A',0,"Prioridades de linhas",                                 None), # ==> abnf000u13c00800_operacional_cadastro_prioridades_linhas
                    ('13C00900A',0,"Operações especiais",                                   None), # ==> abnf000u13c00900_operacional_cadastro_operacoes_especiais
                )),
                (None,1,"Programação",(
                    ('13M02100A',0,"Controle Diário",                                       None), # ==> abnf000u13m02100_operacional_programacao_movimentacao_controle_diario
                    ('13M00100A',0,"Propostas de OSO",                                      None), # ==> abnf000u13m00100_operacional_movimentacao_propostas_oso
                    ('13M00100B',0,"Aprovacao de propostas de OSO",                         None), # ==> abnf000u13m00100_operacional_movimentacao_propostas_oso
                )),
                (None,1,"Portaria",(
                    ('13M03000A',0,"Entrada e saída de veículos",                           None), # ==> abnf000u13m03000_operacional_entrada_saida_veiculos
                    ('13R03000A',0,"Relatório",                                             None), # ==> abnf000u13r03000_operacional_entrada_saida_veiculos
                )),
            )),
            (None,1,"Transdata",(
                (None,1,"Importação",(
                    ('14M00100A',0,"Importação de dados do ITS",                            None), # ==> abnf000u14m00100_transdata_its_importacao
                )),
                (None,1,"Relatórios",(
                    ('14R00100A',0,"Análise do ITS",                                        None), # ==> abnf000u14r00100_transdata_its_analise
                    ('14R00200A',0,"Horários de trabalho de motoristas pelo ITS",           None), # ==> abnf000u14r00200_transdata_its_horarios_trabalho_motoristas
                )),
            )),
        ]
        laceslib = []
        lmenuusu = []
        # Para teste:
        # stipousu = 'A'
        if stipousu == 'A':
            lmenuusu = lmenusis
        elif iidgrams > 0:
            # Busca o grupo de acesso do usuário
            icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
            scamposb = 'idgrams'
            sfilbusc = 'idgrams = "' + str(iidgrams) + '" AND situreg = "A"'
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v01(icodbase, 'abnf_sistema_modulos_grupos', scamposb, sfilbusc, None)
            for lauxi001 in lsqlre01:
                scamposb = 'idgrams, codmodu'
                sfilbusc = 'idgrams = ' + str(lauxi001[0]) + ' and idfilia = ' + str(iidfilia) + ' and situreg = "A"'
                lsqlre02, iqtdre02 = abnf_database_busca_dados_v01(icodbase, 'abnf_sistema_modulos_acessos', scamposb, sfilbusc, None)
                for lauxi002 in lsqlre02:
                    laceslib.append(lauxi002[1])
            if laceslib != []:
                lmenuusu = abnf_websocket_define_menu_usuario_auxiliar_recursivo(lmenusis, laceslib)
        # /// #
        smenuhtm = '''
        <nav class="navbar navbar-expand-lg bg-light">
            <div class="container-fluid container">
                <div class="border p-1 rounded border-secondary border-1">
                    <font color="black" face="Verdana, Geneva, sans-serif" size="2"><b>''' + snomeemp[:30] + '''</b></font><br>
                    <font color="black" face="Verdana, Geneva, sans-serif" size="2">''' + snomefil[:30] + '''</font><br>
                    <font color="brown" face="Verdana, Geneva, sans-serif" size="2">''' + snomeusu[:30] + '''</font>
                </div>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-5">'''
        for lmitemxb in lmenuusu:
            if lmitemxb[1] == 0:
                smenuhtm = smenuhtm + '''
                <li class="nav-item border p-1 rounded border-secondary border-1">
                    <a class="nav-link" href="#" id="''' + lmitemxb[0] + '''"onclick="AbnfSubmitModule(this);">''' + lmitemxb[2] + '''</a>
                </li>'''
            elif lmitemxb[1] == 1:
                smenuhtm = smenuhtm + '''
                <li class="nav-item dropdown border p-1 rounded border-secondary border-1">
                <a class="dropdown-item" href="#" data-bs-toggle="dropdown" aria-expanded="false">''' + lmitemxb[2] + '''</a>
                <ul class="dropdown-menu border-secondary border-1" role="menu" aria-labelledby="dropdownMenu">'''
                for lmitemxc in lmitemxb[3]:
                    if lmitemxc[1] == 0:
                        smenuhtm = smenuhtm + '''
                        <li><a class="dropdown-item" href="#" id="''' + lmitemxc[0] + '''"onclick="AbnfSubmitModule(this);">''' + lmitemxc[2] + '''</a></li>'''
                    elif lmitemxc[1] == 1:
                        smenuhtm = smenuhtm + '''
                        <li><a class="dropdown-item" href="#">''' + lmitemxc[2] + ''' &raquo;</a>
                        <ul class="dropdown-menu submenu border-secondary border-1">'''
                        for lmitemxd in lmitemxc[3]:
                            if lmitemxd[1] == 0:
                                smenuhtm = smenuhtm + '''
                                <li><a class="dropdown-item" href="#" id="''' + lmitemxd[0] + '''"onclick="AbnfSubmitModule(this);">''' + lmitemxd[2] + '''</a></li>'''
                            elif lmitemxd[1] == 1:
                                smenuhtm = smenuhtm + '''
                                <li><a class="dropdown-item" href="#">''' + lmitemxd[2] + '''&raquo;</a>
                                <ul class="dropdown-menu submenu border-secondary border-1">'''
                                for lmitemxe in lmitemxd[3]:
                                    if lmitemxe[1] == 0:
                                        smenuhtm = smenuhtm + '''
                                        <li><a class="dropdown-item" href="#" id="''' + lmitemxe[0] + '''"onclick="AbnfSubmitModule(this);">''' + lmitemxe[2] + '''</a></li>'''
                                    elif lmitemxe[1] == 1:
                                        pass
                                smenuhtm = smenuhtm + '''
                                </ul>
                                </li>'''
                        smenuhtm = smenuhtm + '''
                        </ul>
                        </li>'''
                smenuhtm = smenuhtm + '''
                </ul>
                </li>'''
        smenuhtm = smenuhtm + '''
                    </ul>
                    <ul class="d-flex navbar-nav">'''
        if stipousu == 'A':
            smenuhtm = smenuhtm + '''
                        <li class="nav-item dropdown border p-1 rounded border-secondary border-2">
                            <a class="dropdown-item nav-link active" href="#" data-bs-toggle="dropdown" aria-expanded="false">Administrativo</a>
                            <ul class="dropdown-menu border-secondary border-1" role="menu" aria-labelledby="dropdownMenu">
                                <li><a class="nav-link active" href="#" id="00S00000A">Cadastro de empresas</a></li>
                                <li><a class="nav-link active" href="#" id="00S00000A">Cadastro de usuários</a></li>
                                <li><a class="nav-link active" href="#" id="00S00000A">Cadastro de grupos de acesso</a></li>
                                <li><a class="nav-link active" href="#" id="00S00000A">Vínculos de usuários com grupos de acesso</a></li>
                            </ul>
                        </li>'''
        smenuhtm = smenuhtm + '''
                        <li class="nav-item border p-1 rounded border-secondary border-1">
                            <a class="nav-link active" href="#" id="00S00300A" onclick="AbnfSubmitModule(this);">Alterar empresa</a>
                        </li>
                        <li class="nav-item border p-1 rounded border-secondary border-1">
                            <a class="nav-link active" href="#" id="00S00400A" onclick="AbnfSubmitModule(this);">Perfil</a>
                        </li>
                        <li class="nav-item border p-1 rounded border-secondary border-1">
                            <a class="nav-link active" href="#" id="00S00999A" onclick="AbnfSubmitModule(this);">Sair</a>
                        </li>
                        <li class="nav-item">''' + dglobaux['slogosys'] + '''</li>
                    </ul>
                </div>
            </div>
        </nav>
        '''
        abnf_socket_004([1, 'abnfdv01', smenuhtm])
        '''
        <li class="nav-item">
            <a class="nav-link disabled" href="#"><img src="data:image/jpeg;base64,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" class="rounded mx-auto d-block" width="150" height="35"></a>
        </li>
        '''
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_websocket_autoriza_modulo ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que autoriza um usuário a acessar um módulo do sistema.                                                                                      // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    
def abnf_websocket_autoriza_modulo(icodbase, iidusuar, iidfilia, scodmodu):
    bvalidad = False
    if scodmodu == 'Login':
        bvalidad = True
    else:
        scamposb = 'idusuar, tipousu, idgrams'
        sfilbusc = 'idusuar = "' + str(iidusuar) + '" AND situreg = "A"'
        lsqlre01, iqtdre01 = abnf_database_busca_dados_v01(icodbase, 'abnf_sistema_usuarios', scamposb, sfilbusc, None)
        if lsqlre01 == '[]' or iqtdre01 == 0:
            abnf_alert('O registro ID do usuário não foi encontrado! Entre em contato com o departamento de sistemas!', 4)
        else:
            if scodmodu in ['Filial', 'Free']:
                bvalidad = True
            else:
                scamposb = 'idfilia'
                sfilbusc = 'idfilia = "' + str(iidfilia) + '" AND situreg = "A"'
                lsqlre02, iqtdre01 = abnf_database_busca_dados_v01(icodbase, 'abnf_sistema_empresas_filiais', scamposb, sfilbusc, None)
                if lsqlre02 == '[]' or iqtdre01 == 0:
                    abnf_alert('O registro ID da filial não foi encontrado! Entre em contato com o departamento de sistemas!', 4)
                else:
                    if scodmodu == 'Free':
                        bvalidad = True
                    else:
                        if lsqlre01[0][1] == 'A':   # Usuário administrador (acesso total aos módulos)
                            bvalidad = True
                        else:
                            scamposb = 'idgrams'
                            sfilbusc = 'idgrams = "' + str(lsqlre01[0][2]) + '" AND situreg = "A"'
                            lsqlre03, iqtdre01 = abnf_database_busca_dados_v01(icodbase, 'abnf_sistema_modulos_grupos', scamposb, sfilbusc, None)
                            if lsqlre03 == '[]' or iqtdre01 == 0:
                                abnf_alert('O registro ID do módulo não foi encontrado! Entre em contato com o departamento de sistemas!', 4)
                            else:
                                scamposb = 'idmodac'
                                sfilbusc =            'idgrams = "' + str(lsqlre03[0][0]) + '" AND '
                                sfilbusc = sfilbusc + 'idfilia = "' + str(lsqlre02[0][0]) + '" AND '
                                sfilbusc = sfilbusc + 'codmodu = "' + scodmodu + '" AND '
                                sfilbusc = sfilbusc + 'situreg = "A"'
                                lsqlre04, iqtdre01 = abnf_database_busca_dados_v01(icodbase, 'abnf_sistema_modulos_acessos', scamposb, sfilbusc, None)
                                if lsqlre04 == '[]' and iqtdre01 > 0:
                                    abnf_alert('Seu usuário não tem autorização de acesso a este módulo!', 4)
                                else:
                                    bvalidad = True
    return bvalidad

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_websocket_define_menu_usuario_auxiliar_recursivo ] //////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que monta o menu personalizado para cada usuário (função auxiliar que monta o menu com recursividade).                                       // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf_websocket_define_menu_usuario_auxiliar_recursivo(lmenusis, laceslib):
    if lmenusis:
        lauxi001 = []
        for lauxi002 in lmenusis:
            # print('-------------------------')
            # print(lauxi002[0], ' - ', lauxi002[1], ' - ', lauxi002[2], ' - ', lauxi002[3])
            # print('-------------------------')
            if lauxi002[1] == 1:    # menu/submenu de item
                lauxi003 = abnf_websocket_define_menu_usuario_auxiliar_recursivo(lauxi002[3], laceslib)
                if lauxi003:
                    lauxi001.append((lauxi002[0], lauxi002[1], lauxi002[2], lauxi003))
            if lauxi002[1] == 0:    # item de menu/submenu
                if lauxi002[0] in laceslib:
                    lauxi001.append((lauxi002[0], lauxi002[1], lauxi002[2], lauxi002[3]))
        return lauxi001

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_websocket_js_socketio ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que traz para o codigo HTML funções específicas para a comunicação cliente/servidor via websocket.                                           // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #   

def abnf_websocket_js_socketio(sabntoke):
    spagehtm = ''
    # JS: ==================================================================================================================================
    # JS: Cria uma instância do objeto io
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    spagehtm = spagehtm  + '''
    <script type="text/javascript">
    const socket = io();'''
    # JS: ==================================================================================================================================
    # JS: Função que será executada quando o cliente se conectar ao servidor - abnf_socket_002 (connect).
    # JS: A existência dessa função não é obrigatória.
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    # JS: console.log('Cliente conectado no servidor !!!');         => Inserir essa linha na função quando quiser debugar pelo console.
    # JS: alert('Cliente conectado no servidor !!!');               => Inserir essa linha na função quando quiser debugar pelo JS.
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    # spagehtm = spagehtm  + '''
    # socket.on('connect', function(){
    # });'''
    # JS: ==================================================================================================================================
    # JS: Função que será executada quando o evento 'AbnfReceivedForm' for recebido do servidor - abnf_socket_004 (AbnfReceivedForm).
    # JS: Essa função recebe uma lista (lskio004) aos quais o JS a interpreta para executar ações na pagina HTML/CSS/JS.
    # JS: O primeiro ítem da lista (sparam00) é o parâmetro de ação a ser realizada.
    # JS: O segundo ítem em diante vai depender dos parâmetros necessários para a ação definida no primeiro ítem.
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    # JS: sparam00 ..: 01 - Envia um HTML para o conteúdo de um objeto pelo endereço ID desse objeto.
    # JS: sparam01 ..: Endereço ID do objeto que vai receber o HTML.
    # JS: sparam02 ..: Conteúdo HTML a ser inserido.
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    # JS: sparam00 ..: 02 - Dispara um alert JS na tela do navegador.
    # JS: sparam01 ..: Mensagem a ser disparada.
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    # JS: sparam00 ..: 03 - Preenche o conteúdo de campos editáveis do formulário (inclusive com valores vazios para apagar).
    # JS: sparam01 ..: Endereço ID do objeto que vai receber o coteúdo.
    # JS: sparam02 ..: Conteúdo a ser inserido.
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    # JS: sparam00 ..: 04 - Reinicia o sistema (refresh).
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    # JS: sparam00 ..: 05 - Habilita um botão que estava desabilitado após ser pressionado.
    # JS: sparam01 ..: Endereço ID do botão que vai ser habilitado.
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    # JS: sparam00 ..: 06 - Realiza upload de arquivos.
    # JS: sparam01 ..: Endereço ID do input type file de onde serão realizados os uploads.
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    # JS: sparam00 ..: 07 - Realiza dowload de arquivos.
    # JS: sparam01 ..: Nome do arquivo que deseja que seja feito o download.
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    # JS: sparam00 ..: 08 - Envia um HTML para o conteúdo de um objeto pelo endereço ID desse objeto (igual ao 01).
    # JS: sparam00 ..: 08 - Faz o scroll de tela para o topo do navegador. 
    # JS: sparam00 ..: 08 - Para uso exclusivo da função python "abnf_alert" (quando a mensagem não estiver vazia).
    # JS: sparam01 ..: Endereço ID do objeto que vai receber o HTML.
    # JS: sparam02 ..: Conteúdo HTML a ser inserido.
    # JS: iauxi001 ..: Duração em milissegundos por rolagem
    # JS: iauxi002 ..: Quantidade de linhas roladas por vez
    # JS: iauxi003 ..: Posição Y do topo da página
    # JS: iauxi004 ..: Posição de rolagem atual
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    # JS: sparam00 ..: 09 - Coloca o focu em um objeto pelo endereço ID desse objeto.
    # JS: sparam01 ..: Endereço ID do objeto que será dado o focu.
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    # JS: sparam00 ..: 10 - Desabilita um objeto do form.
    # JS: sparam01 ..: Endereço ID do objeto que vai ser desabilitado.
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    # JS: sparam00 ..: 11 - Pressiona um botão do form.
    # JS: sparam01 ..: Endereço ID do objeto que vai ser desabilitado.
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    # JS: sparam00 ..: 12 - Dispara alarmes sonoros no navegador.
    # JS: sparam01 ..: Número do alarme que será disparado.
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    # JS: sparam00 ..: 13 - Dispara um texto falado pelo navegador. Obs: navegador tem que ser compatível.
    # JS: sparam01 ..: Texto que será falado pelo navegador.
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    # JS: sparam00 ..: 14 - Habilita o check de um checkbox.
    # JS: sparam01 ..: Endereço ID do checkbox que vai habilitar o check.
    # JS: ----------------------------------------------------------------------------------------------------------------------------------    
    # JS: sparam00 ..: 15 - Desabilita o check de um checkbox.
    # JS: sparam01 ..: Endereço ID do checkbox que vai desabilitar o check.
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    # JS: console.log('Received AbnfReceivedForm: ' + lskio004);    => Inserir essa linha na função quando quiser debugar pelo console.
    # JS: alert('Received AbnfReceivedForm: ' + lskio004);          => Inserir essa linha na função quando quiser debugar pelo JS.
    # JS: var s004a001 = document.getElementById('abnfpa01');       => Obtém o elemento HTML pelo seu ID.
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    spagehtm = spagehtm  + '''
    socket.on('AbnfReceivedForm', function(lskio004){
        const sparam00 = lskio004[0];
        if (sparam00 == 1) {
            const sparam01 = lskio004[1];
            const sparam02 = lskio004[2];
            var s004a001 = document.getElementById(sparam01);
            s004a001.innerHTML = sparam02;
        }
        else if (sparam00 == 2) {
            const sparam01 = lskio004[1];
            alert(sparam01);
        }
        else if (sparam00 == 3) {
            const sparam01 = lskio004[1];
            const sparam02 = lskio004[2];
            var s004a001 = document.getElementById(sparam01);
            s004a001.value = sparam02;
        }
        else if (sparam00 == 4) {
            window.location.reload();
        }
        else if (sparam00 == 5) {
            const sparam01 = lskio004[1];
            AbnfButtonEnable(sparam01);
        }
        else if (sparam00 == 6) {
            const sparam01 = lskio004[1];
            var s004a001 = document.getElementById(sparam01);
            AbnfUploadFiles(s004a001);
        }
        else if (sparam00 == 7) {
            const sparam01 = lskio004[1];
            AbnfDownloadFiles(sparam01);
        }
        else if (sparam00 == 8) {
            const sparam01 = lskio004[1];
            const sparam02 = lskio004[2];
            var s004a001 = document.getElementById(sparam01);
            s004a001.innerHTML = sparam02;
            const iauxi001 = 50;
            const iauxi002 = 10;
            const iauxi003 = 0;
            let iauxi004 = window.scrollY;
            while (iauxi004 > iauxi003) {
                iauxi004 -= iauxi002;
                window.scrollTo(0, iauxi004);
                setTimeout(() => {
                    window.scrollTo(0, iauxi004);
                }, iauxi001);
            }
        }
        else if (sparam00 == 9) {
            const sparam01 = lskio004[1];
            var s004a001 = document.getElementById(sparam01);
            s004a001.focus();
        }
        else if (sparam00 == 10) {
            const sparam01 = lskio004[1];
            document.getElementById(sparam01).disabled = true;
        }
        else if (sparam00 == 11) {
            const sparam01 = lskio004[1];
            document.getElementById(sparam01).click();
        }
        else if (sparam00 == 12) {
            const sparam01 = lskio004[1];
            AbnfRingtone(sparam01);
        }
        else if (sparam00 == 13) {
            const sparam01 = lskio004[1];
            AbnfVoice(sparam01);
        }
        else if (sparam00 == 14) {
            const sparam01 = lskio004[1];
            var s004a001 = document.getElementById(sparam01);
            s004a001.checked = true;
        }
        else if (sparam00 == 15) {
            const sparam01 = lskio004[1];
            var s004a001 = document.getElementById(sparam01);
            s004a001.checked = false;
        }
    });'''
    # JS: ==================================================================================================================================
    # JS: Função que será executada quando um evento de botão for pressionado para enviar dados para o servidor - abnf_socket_003 (dabnfopg)
    # JS: Os objetos da página serão capturados e enviados para o servidor dentro do dicionário 'dabnfopg'.
    # JS: Em dabnfopg['abnfobj0'] fica uma lista contendo [ID, nome] do botão que foi pressionado.
    # JS: Dessa forma é possível tratar cada botão do formulário.
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    spagehtm = spagehtm  + '''
    function AbnfSubmitForm(event, sparam01) {
        let dabnfopg = new Object();
        dabnfopg['abnfobj0'] = [event.target.id, event.target.name];
        const objects = document.querySelectorAll('*');
        for (const object of objects) {
            const id = object.id;
            if (id != '') {
                const type = object.type;
                if (type == 'text' ||
                    type == 'password' || 
                    type == 'textarea' || 
                    type == 'select-one' || 
                    type == 'select-multiple' || 
                    type == 'radio' || 
                    type == 'checkbox' || 
                    type == 'hidden' || 
                    type == 'file' ||
                    type == 'date' ||
                    type == 'time' ||
                    type == 'number') {
                    const name = object.name;
                    const value = object.value;
                    // console.log(`ID: ${id}, Name: ${name}, Type: ${type}, Value: ${value}`);
                    if (type != 'radio') { dabnfopg[id] = [name, type, value]; }
                    else { 
                        if (object.checked) {
                            dabnfopg[id] = [name, type, value];
                        }
                    }
                    if (type == 'checkbox') {
                        if (object.checked) { dabnfopg[id].push(true) }
                        else { dabnfopg[id].push(false) }
                    }
                    if (type == 'select-multiple') {
                        const select = document.getElementById(id);
                        // const selectedValues = select.options.filter(option => option.selected).map(option => option.value);
                        var result = [];
                        var options = select && select.options;
                        var opt;
                        for (var i=0, iLen=options.length; i<iLen; i++) {
                            opt = options[i];
                            if (opt.selected) { result.push(opt.value); }
                        }
                        dabnfopg[id].splice(2, 1);
                        dabnfopg[id].push(result);
                    }
                }
            }
        }
        if (sparam01 !== undefined) {
            dabnfopg['sonblurx'] = sparam01;
        }
        else {
            dabnfopg['sonblurx'] = '';
        }
        socket.emit('abnf_socket_003', dabnfopg);
    }'''
    # JS: ==================================================================================================================================
    # JS: Função que será executada quando for clicado um ítem de menu.
    # JS: O ítem selecionado será capturado pelo ID e enviado para o servidor dentro do dicionário 'dabnfopg'.
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    # JS: alert(event.id);                              => Inserir essa linha na função quando quiser debugar pelo JS.
    # JS: alert(abnproje + ' - ' + abntoken)            => Inserir essa linha na função quando quiser debugar pelo JS.
    # JS: const sauxi001 = JSON.stringify(dabnfopg);    => Inserir essa linha na função quando quiser debugar pelo JS.
    # JS: alert(sauxi001);                              => Inserir essa linha na função quando quiser debugar pelo JS.
    spagehtm = spagehtm  + '''
    function AbnfSubmitModule(event) {
        let dabnfopg = new Object();
        const abnproje = document.getElementById('abnproje').value;
        const abntoken = document.getElementById('abntoken').value;
        dabnfopg['sabnfsys'] = event.id;
        dabnfopg['abnproje'] = ['abnproje', 'hidden', abnproje];
        dabnfopg['abntoken'] = ['abntoken', 'hidden', abntoken];
        socket.emit('abnf_socket_003', dabnfopg);
    }
    </script>'''
    # JS: ==================================================================================================================================
    # JS: Função para upload de arquivo via websocket.
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    # JS: Essa função será executada via comando no python: abnf_socket_004([6, '<id do input type="file">']).
    # JS: Ela trabalha em conjunto com a função do python: abnf_files_upload.
    spagehtm = spagehtm  + '''
    <script>
        function AbnfUploadFiles(fileInput) {
            const files = fileInput.files;
            const formData = new FormData();
            for (let i = 0; i < files.length; i++) {
                formData.append('ffile001', files[i]);
            }
            const xhr = new XMLHttpRequest();
            xhr.open('POST', "/upload/''' + sabntoke + '''");
            xhr.send(formData);
        }
    </script>'''
    # JS: ==================================================================================================================================
    # JS: Função para download de arquivo via websocket.
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    # JS: Essa função será executada via comando no python: abnf_socket_004([7, '<arquivo>']).
    # JS: Ela trabalha em conjunto com a função do python: abnf_files_download.
    # JS: Apesar de existir outros método mas complexos e com mais controles, essa função foi feita da forma mais simples possivel.
    # JS: Ela somente recebe o nome do arquivo e aciona a função python que faz o donwload do arquivo.
    # JS: Caso o arquivo não exista no repositório, será feito do download de um arquivo sem bites.
    # JS: Isso é bom porque não da erros na pagina caso o arquivo não venha a existir.
    # JS: O arquivo para download tem que estar na pasta /flexabeinfo/abnftmp.
    spagehtm = spagehtm  + '''
    <script>
        function AbnfDownloadFiles(filename) {
            const downloadLink = document.createElement('a');
            downloadLink.href = `/download/${filename}`;
            downloadLink.download = filename;
            downloadLink.click();
        }
    </script>'''
    # JS: ==================================================================================================================================
    # JS: Função para soar toques sonoros pelo navegador.
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    # JS: Essa função será executada via comando no python: abnf_socket_004([12, '<Número do toque>']).
    spagehtm = spagehtm  + '''
    <script>
        function AbnfRingtone(ringtone) {
			if (ringtone == 1) {
				const audioContext = new (window.AudioContext || window.webkitAudioContext)();
				const oscillator = audioContext.createOscillator();
				const gainNode = audioContext.createGain();
				oscillator.type = 'sine';
				oscillator.frequency.setValueAtTime(880, audioContext.currentTime); // Frequência inicial
				gainNode.gain.setValueAtTime(1, audioContext.currentTime);
				gainNode.gain.exponentialRampToValueAtTime(0.001, audioContext.currentTime + 1); // Fade out
				oscillator.connect(gainNode);
				gainNode.connect(audioContext.destination);
				oscillator.start();
				oscillator.stop(audioContext.currentTime + 1);
			} else if (ringtone == 2) {
				const audioContext = new (window.AudioContext || window.webkitAudioContext)();
				// Primeiro "Ding"
				const oscillator1 = audioContext.createOscillator();
				const gainNode1 = audioContext.createGain();
				oscillator1.type = 'sine';
				oscillator1.frequency.setValueAtTime(440, audioContext.currentTime); // Frequência inicial
				gainNode1.gain.setValueAtTime(1, audioContext.currentTime);
				gainNode1.gain.exponentialRampToValueAtTime(0.001, audioContext.currentTime + 0.5); // Fade out
				oscillator1.connect(gainNode1);
				gainNode1.connect(audioContext.destination);
				oscillator1.start();
				oscillator1.stop(audioContext.currentTime + 0.5);
				// Segundo "Dong"
				const oscillator2 = audioContext.createOscillator();
				const gainNode2 = audioContext.createGain();
				oscillator2.type = 'sine';
				oscillator2.frequency.setValueAtTime(330, audioContext.currentTime + 0.5); // Frequência mais baixa
				gainNode2.gain.setValueAtTime(1, audioContext.currentTime + 0.5);
				gainNode2.gain.exponentialRampToValueAtTime(0.001, audioContext.currentTime + 1.5); // Fade out
				oscillator2.connect(gainNode2);
				gainNode2.connect(audioContext.destination);
				oscillator2.start(audioContext.currentTime + 0.5); // Inicia após o primeiro "Ding"
				oscillator2.stop(audioContext.currentTime + 1.5);
			}
        }
    </script>'''
    # JS: ==================================================================================================================================
    # JS: Função para ler um texto com voz no navegador.
    # JS: ----------------------------------------------------------------------------------------------------------------------------------
    # JS: Essa função será executada via comando no python: abnf_socket_004([13, '<texto a ser falado>']).
    # JS: Até o momento somnente voz brasileira masculina foi encontrada nas funções suportadas pelos navegadores.
    spagehtm = spagehtm  + '''
    <script>
        function AbnfVoice(textvoice) {
            if ('speechSynthesis' in window) {
                const utterance = new SpeechSynthesisUtterance();
                utterance.text = textvoice;
                utterance.lang = 'pt-BR';
                utterance.rate = 0.7;
                speechSynthesis.speak(utterance);
            } else {
                alert('A API Web Speech não é suportada neste navegador.');
            }
        }
    </script>'''
    return spagehtm

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_websocket_js_abeinfo ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que traz para o codigo HTML funções personalizadas em JS para o sistema.                                                                     // #
# // Este código é o que também esta no arquivo: /flexabeinfo/abnfsrc/static/abeinfo/abeinfo.js                                                          // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #          
        
def abnf_websocket_js_abeinfo():  
    spagehtm = '''
    <script>'''
    # ===========================================
    # Nos inputs somente aceitar números inteiros
    # ===========================================
    spagehtm = spagehtm + '''
        function AbnfScriptIntegerOnly(e) {
            //var teste = e.value.length;
            //window.alert(teste);
            var tecla=(window.event)?event.keyCode:e.which;
            if ((tecla>47 && tecla<58)) return true;
            else {
                if (tecla==8 || tecla==0) return true;
                else return false;
            }
        }'''
    # =======================================
    # Limita o número de caracteres em inputs
    # =======================================
    spagehtm = spagehtm + '''
        function AbnfMaxLength(element,max_chars)
        {
            if(element.value.length > max_chars) {
                element.value = element.value.substr(0, max_chars);
            }
        }'''
    # =============================================================================
    # Nos inputs somente aceitar letras sem acentuação, números e alguns caracteres
    # =============================================================================
    spagehtm = spagehtm + '''
        function AbnfScriptKey(e) {
            var mKey = (window.event)?event.keyCode:e.which;
            var nKey = String.fromCharCode(mKey);
            var nKey = nKey.toUpperCase();
            var oKey = (e)? e: event;
            var mLib = "|8|9|32|";
            var nLib = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*()-_+={}[],:/?\|ªº';
            var oLib = "|9|37|39|46|116|";
            var m = mLib.search(mKey); 
            var n = nLib.search(nKey);
            var o = oLib.search(oKey.keyCode);
            var show = false;
            if (show) {
                window.alert('1:'+mKey);
                window.alert('2:'+nKey);
                window.alert('3:'+oKey.keyCode);
                window.alert('4:'+m);
                window.alert('5:'+n);
                window.alert('6:'+o);
            }
            if (m>-1) return true;
            if (n>-1) return true;
            if (o>-1) return true;
            return false;
        }'''
    # ==================================================================================================
    # Nos inputs tratar digitação de valores com decimal inserindo pontos e virgulas de forma automática
    # ==================================================================================================
    spagehtm = spagehtm + '''
        function AbnfNumMaskDecimal(obj,dec) {
            AbnfNumMaskValidaNum(obj)
            if (obj.value.match("-")) {
                mod = "-";
            } else {
                mod = "";
            }
            valor = obj.value.replace("-","");
            valor = valor.replace(",","");
            if (valor.length >= (dec+1)) {
                valor = AbnfNumMaskGetPoint(valor.substring(0,valor.length-dec))+","+valor.substring(valor.length-dec, valor.length);
            }
            obj.value = mod+valor;
            for (i=0;i<obj.value.length-1;i++) {
                result += obj.value.charAt(i)
                result += "-"
            }
        }
        function AbnfNumMaskGetPoint(valor) {
            valor = valor.replace(/\./g,"");
            if (valor.length > 3) {
                valores = "";
                while (valor.length > 3) {
                valores = "."+valor.substring(valor.length-3,valor.length)+""+valores;
                valor = valor.substring(0,valor.length-3);
            }
            return valor+""+valores;
            } else {
                return valor;
            }
        }
        function AbnfNumMaskValidaNum(obj) {
            numeros = new RegExp("[0-9]");
            while (!obj.value.charAt(obj.value.length-1).match(numeros)) {
                if (obj.value.length == 1 && obj.value == "-") {
                    return true;
                }
                if (obj.value.length >= 1) {
                    obj.value = obj.value.substring(0,obj.value.length-1)
                } else {
                    return false;
                }
            }
        }'''
    # =======================
    # Utilizar enter como tab
    # =======================
    spagehtm = spagehtm + '''
        function AbnfTabEnter(event,campo) {
            var tecla = event.keyCode ? event.keyCode : event.which ? event.which : event.charCode;
            if (tecla == 13) {
                campo.focus();
            }
        }'''
    # Esse comando abaixo faz a tela centralizar sobre o campo que esta recebendo o foco:
    # campo.scrollIntoView({ behavior: "smooth", block: "center" }); // Rolagem suave e centralizada    
    # Não vamos usálos por enquanto, mas vamos estudar no futuro.
    # ============================================
    # Desabilitar o botão por um determinado tempo
    # ============================================
    spagehtm = spagehtm + '''
        function AbnfTimeButtonDisable(e,time) {
            e.disabled=true;
            time=time*1000
            setTimeout(
                function(){
                    e.disabled=false;
                },time
            );
            return true;
        }'''
    # ====================
    # Desabilitar um botão
    # ====================
    # Alexandre - 11/04/2025
    # Antes esta função estava no formato abaixo, só que estava tendo problema de duplicidade
    # de registros gerados na TA provavelmente pela função "setTimeout" que estava atrasando
    # o processo de inatividade do botão. Tire então o "setTimeout" para ver se resolve.
    # --------------------
    # setTimeout(
    #     function(){
    #         e.disabled=true;
    #     },0
    # );
    # return true;
    spagehtm = spagehtm + '''
        function AbnfButtonDisable(e) {
            e.disabled=true;
            return true;
            // onclick="var e=this;setTimeout(function(){e.disabled=true;},0);return true;"
            // document.getElementById(e).disabled = true;
            // alert("Hello! I am an alert box!!");
            // e.disabled = true;
        }'''
    # ==================
    # Habilitar um botão
    # ==================
    spagehtm = spagehtm + '''
        function AbnfButtonEnable(e) {
            document.getElementById(e).disabled = false;
        }'''
    # =============================================================================================================================
    # Função que pressiona um botão automaticamente a cada X tempo
    # O problema dessa função é que ela acumula contadores a cada aperto no botão gerando uma enxurrada de solicitações ao servidor
    # Não consegui resolver esse problema até o momento mesmo pedindo ajuda ao Gêmini
    # Mas vamos na aposta que o usuário não vai ficar clicando varias vezes nesse botão uma vez que ele se atualiza
    # E também vamos fazer um método no servidor para que o programa busque, via arquivo texto, saber se ele esta atualizado
    # Dessa forma não vai ficar buscando toda hora no banco de dados informações que esteja repetidas
    # =============================================================================================================================
    spagehtm = spagehtm + '''
        const intervalButtons = {};
        function AbnfAutomaticPressButtonInterval(buttonElement, intervalSeconds) {
            const buttonId = buttonElement.id;
            const tempoIntervaloMs = intervalSeconds * 1000;
            if (!buttonElement.dataset.originalValue) {
                buttonElement.dataset.originalValue = buttonElement.value;
            }
            const originalButtonText = buttonElement.dataset.originalValue;
            if (intervalButtons[buttonId]) {
                clearInterval(intervalButtons[buttonId].mainInterval);
                clearInterval(intervalButtons[buttonId].countdownInterval);
                console.log(`Intervalos anteriores para ${buttonId} limpos.`);
            }
            intervalButtons[buttonId] = {
                secondsRemaining: intervalSeconds, // AGORA: secondsRemaining é parte do estado do botão
                mainInterval: null,
                countdownInterval: null
            };
            const currentButtonState = intervalButtons[buttonId];
            function simulateInternalClick() {
                buttonElement.click(); 
                buttonElement.value = originalButtonText; // Restaura o texto original ao clicar
            }
            function updateAccountant() {
                const minutes = Math.floor(currentButtonState.secondsRemaining / 60);
                const seconds = currentButtonState.secondsRemaining % 60;
                let displayText = originalButtonText;
                if (currentButtonState.secondsRemaining > 0) {
                    displayText += ` ${minutes > 0 ? minutes + 'm ' : ''}${seconds} seg`;
                } else {
                    displayText += ` Atualizando...`; // Mensagem quando o tempo é zero antes do clique
                }
                buttonElement.value = displayText;
            }
            simulateInternalClick(); // O primeiro clique é imediato (chama a ação e inicia a contagem)
            currentButtonState.mainInterval = setInterval(simulateInternalClick, tempoIntervaloMs);
            currentButtonState.countdownInterval = setInterval(() => {
                currentButtonState.secondsRemaining--;
                if (currentButtonState.secondsRemaining < 0) {
                    currentButtonState.secondsRemaining = 0; // Evita mostrar negativo antes do próximo clique
                }
                updateAccountant();
            }, 1000);
            console.log(`Automatização para botão "${buttonId}" configurada para cada ${intervalSeconds} segundos.`);
        }
        '''
    # ==============================
    # Alterar o valor de um checkbox
    # ==============================
    spagehtm = spagehtm + '''
        function AbnfCheckboxChangeValue(id) {
            const checkbox = document.getElementById(id);
            checkbox.checked = !checkbox.checked;
        }'''
    # ===============
    # Máscara de Hora
    # ===============
    spagehtm = spagehtm + '''
        function AbnfTimeMask(e) {
            var txtOrigem;
            var key;
            if (window.event)     {
                key = e.keyCode;
                if (key >= 48 && key <= 57)         {
                    origem = e.srcElement;
                    txtOrigem = origem.value;
                    if (txtOrigem.length == 2) {
                        txtOrigem += ":";
                        origem.value = txtOrigem ;
                    }
                } else {
                    event.returnValue = false;
                }  
            }
            else {
                key = e.which;
                if (key >= 48 && key <= 57) {
                    origem = e.target;
                    txtOrigem = origem.value;
                    if (txtOrigem.length == 2) {
                        txtOrigem += ":";
                        origem.value = txtOrigem ;
                    }
                } else {
                    if (key != 8 && key != 0) {
                        e.preventDefault();
                    }
                }
            }
        }'''
    # ==============
    # Máscara CPF
    # XXX.XXX.XXX-XX
    # ==============
    spagehtm = spagehtm + '''
        function AbnfMaskCPF(event) {
            let input = event.target
            input.value = AbnfReplaceMaskCPF(input.value)
        }
        function AbnfReplaceMaskCPF(value) {
            if (!value) return ""
            value = value.replace(/\D/g,"");
            value = value.replace(/(\d{3})(\d)/,"$1.$2");
            value = value.replace(/(\d{3})(\d)/,"$1.$2");
            value = value.replace(/(\d{3})(\d{1,2})$/,"$1-$2");
            return value
        }'''
    # ====================
    # Máscara CNPJ
    # XX. XXX. XXX/0001-XX
    # =====================
    spagehtm = spagehtm + '''
        function AbnfMaskCNPJ(event) {
            let input = event.target
            input.value = AbnfReplaceMaskCNPJ(input.value)
        }
        function AbnfReplaceMaskCNPJ(value) {
            if (!value) return ""
            value = value.replace(/\D/g,"");
            value = value.replace(/(\d{2})(\d)/, "$1.$2");
            value = value.replace(/(\d{3})(\d)/, "$1.$2");
            value = value.replace(/(\d{3})(\d)/, "$1/$2");
            value = value.replace(/(\d{4})(\d{1,2})$/, "$1-$2");
            return value
        }'''
    # ===========
    # Máscara CEP
    # ===========
    spagehtm = spagehtm + '''
        function AbnfMaskCEP(event) {
            let input = event.target
            input.value = AbnfReplaceMaskCEP(input.value)
        }
        function AbnfReplaceMaskCEP(value) {
            if (!value) return ""
            value = value.replace(/\D/g,'')
            value = value.replace(/(\d{5})(\d)/,'$1-$2')
            return value
        }'''
    # ================
    # Máscara telefone
    # ================
    spagehtm = spagehtm + '''
        function AbnfMaskPhone(event) {
            let input = event.target
            input.value = AbnfReplaceMaskPhone(input.value)
        }
        function AbnfReplaceMaskPhone(value) {
            if (!value) return ""
            value = value.replace(/\D/g,'')
            value = value.replace(/(\d{2})(\d)/,"($1) $2")
            value = value.replace(/(\d)(\d{4})$/,"$1-$2")
            return value
        }'''
    # ============================
    # Pede para o usuário aguardar
    # ============================
    spagehtm = spagehtm + '''
        function AbnfWaitProcedure() {
            document.getElementById("abnfdivwait").innerHTML = '<table class="table table-sm table-bordered table-responsive"><tr class="table-active"><td align="center"><font style="font-family: Courier New; font-size: 32px; font-weight: bold; color: black"><b>Por favor aguarde...</b></font></td><td align="center"><div class="spinner-border" style="width: 3rem; height: 3rem;" role="status"><span class="sr-only"></span></div><div class="spinner-grow" style="width: 3rem; height: 3rem;" role="status"><span class="sr-only"></span></div></td>';
        }'''
    # ================
    # Filtro de select
    # ================
    spagehtm = spagehtm + '''
        function AbnfFilterSelect(inputElement, selectElement) {
            var searchText = inputElement.value.toUpperCase();
            var words = searchText.split(" ");
            for (var i = 0; i < selectElement.options.length; i++) {
                var option = selectElement.options[i];
                var optionText = option.textContent.toUpperCase();
                var match = true;
                for (var j = 0; j < words.length; j++) {
                    if (!optionText.includes(words[j])) {
                        match = false;
                        break;
                    }
                }
                option.hidden = !match;
            }
        }'''
    # ========================================================================================
    # Altera a cor de fundo da linha do "tr" conforme a situação do checkbox que esta na linha
    # ========================================================================================
    spagehtm = spagehtm + '''
        function AbnfCheckboxBgColor(element) {
            const checkbox = element.querySelector('input[type="checkbox"]');
            if (element.className === 'abnf-check-clicked') {
                element.className = '';
                checkbox.checked = false
            } else {
                element.className = 'abnf-check-clicked';
                checkbox.checked = true
            }
        }'''
    # =========================================================================================================================
    # Altera a cor de fundo da linha do "tr" quando o radiobutton for selecionado e volta a cor das demais linhas para o padrão
    # Problema: Quando você altera a propriedade checked via JavaScript (radioButton.checked = true;), o navegador entende isso
    # como uma modificação programática, não uma interação do usuário, e, por isso, não dispara o evento change.
    # Solução:
    # 1)   const event = new Event('change', { bubbles: true });
    # 1.a) Cria uma nova instância do evento change.
    # 1.b) { bubbles: true }: É importante definir bubbles como true. Isso significa que o evento "borbulhará" (ou se propagará)
    #      para cima na árvore DOM, permitindo que manipuladores de eventos em elementos pai (como a própria linha da tabela)
    #      também o capturem, caso você tenha algum. Para radio buttons, bubbles geralmente deve ser true.
    # 2)   radioButton.dispatchEvent(event);:
    # 2.a) Este método é chamado no elemento HTML (radioButton neste caso) no qual você quer disparar o evento.
    # 2.b) Ele simula o comportamento de um evento que acabou de acontecer, fazendo com que qualquer listener (onchange
    #      embutido no HTML ou addEventListener('change', ...) em JS para aquele evento no elemento seja executado.
    # =========================================================================================================================
    spagehtm = spagehtm + '''
        function AbnfRadioBgColor(tableId, bgcolor) {
            const table = document.getElementById(tableId);
            const tableRows = table.querySelectorAll('tr');
            let selectedRow;
            tableRows.forEach(row => {
                row.addEventListener('click', () => {
                    if (selectedRow) {
                        selectedRow.style.backgroundColor = '';
                    }
                    selectedRow = row;
                    row.style.backgroundColor = bgcolor; 
                    const radioButton = AbnfFindRadioButton(row);
                    radioButton.checked = true;
                    const event = new Event('change', { bubbles: true });
                    radioButton.dispatchEvent(event);
                });
            });
        }
        function AbnfFindRadioButton(parent) {
            return parent.querySelector('input[type="radio"]');
        }'''
    # =================================
    # Marca todos os checkbox definidos
    # =================================
    spagehtm = spagehtm + '''
        function AbnfCheckboxCheckAll(checkboxesIds) {
            checkboxesIds.forEach(id => {
                const checkbox = document.getElementById(id);
                if (checkbox) {
                    checkbox.checked = true;
                } else {
                    console.error(`Checkbox com ID ${id} não encontrado.`);
                }
            });
        }'''
    # ====================================
    # Desmarca todos os checkbox definidos
    # ====================================
    spagehtm = spagehtm + '''
        function AbnfCheckboxUncheckAll(checkboxesIds) {
            checkboxesIds.forEach(id => {
                const checkbox = document.getElementById(id);
                if (checkbox) {
                    checkbox.checked = false;
                } else {
                    console.error(`Checkbox com ID ${id} não encontrado.`);
                }
            });
        }'''
    # ================
    # ????????????????
    # ================
    spagehtm = spagehtm + '''
        function AbnfCheckboxUnselectAll(event) {
            for (i=0;i<event.form.elements.length;i++)
                if (event.form.elements[i].type == "checkbox")
                    event.form.elements[i].checked=0
        }
    </script>'''
    # spagehtm = spagehtm.strip().replace('\n', '')  # .replace('        ', ' ').replace('     ', ' ').replace('    ', ' ')
    return spagehtm
        
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_websocket_css_menu_dropdown ] ///////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Função que traz para o codigo HTML o CSS responsável pelo menu dropdown do sistema.                                                                 // #
# // Este código é o que também esta no arquivo: /flexabeinfo/abnfsrc/static/abeinfo/abeinfo.css                                                         // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #        

def abnf_websocket_css_menu_dropdown():
    spagehtm = '''
    <style>
        .card {
            width: 400px;
            border: none;
            border-radius: 10px;
            background-color: #fff;
        }
        .stats {
            background: #f2f5f8 !important;
            color: #000 !important;
        }
        .articles {
            font-size:10px;
            color: #a1aab9;
        }
        .number1 {
            font-weight:500;
        }
        .followers {
            font-size:10px;
            color: #a1aab9;
        }
        .number2 {
            font-weight:500;
        }
        .rating {
            font-size:10px;
            color: #a1aab9;
        }
        .number3 {
            font-weight:500;
        }
        .meupost {
            background: #f2f5f8 !important;
        }
    '''
    # =====================
    # Dropdowns de submenus
    # =====================
    spagehtm = spagehtm + '''
        .dropdown-menu li {
            position: relative;
        }
        .dropdown-menu .submenu{
            display: none;
            position: absolute;
            left: 100%;
            top: -7px;
        }
        .dropdown-menu>li:hover>.submenu {
            display: block;
        }
        .dropdown-menu .submenu-left {
            right: 100%;
            left: auto;
        }
    '''
    # ======================
    # Funções personalizadas
    # ======================
    # Script para piscar o texto em tela
    spagehtm = spagehtm + '''
        @keyframes abnfblink {
            50% { opacity: 0; }
        }
    '''
    # ======================
    # Funções personalizadas
    # ======================
    # Script para criar cores personalizadas no bootstrap.
    # https://www.youtube.com/watch?v=1S3asK3f7us&ab_channel=B%C3%B3sonTreinamentos
    # Essa cor abaixo esta sendo usado no arquivo "abnf000u13m2100.py" no cabeçalho de veículos retidos
    # Ela somente funciona em "tr", não funciona em "td"
    spagehtm = spagehtm + '''
        .bg-abnf001 {
            background-color: #ED7632;
        }
    '''
    # ================================
    # Fechando nosso CSS personalizado
    # ================================
    spagehtm = spagehtm + '''
    </style>
    '''
    spagehtm = spagehtm.strip().replace('\n', '').replace('        ', ' ').replace('     ', ' ').replace('    ', ' ')
    return spagehtm

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_convert_image ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Conversor de imagem para texto no padrão base64 o qual será usado como código dentro do html.                                                       // #
# // Colocar o arquivo na raiz do sistema ("/flexabeinfo") para fazer a conversão.                                                                       // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #    
    
@abnfxapp.route('/abnf_convert_image')
def abnf_convert_image():
    exit()
    simage01 = abnf_websocket_converte_arquivo_imagem_base64('imagem.jpg', 'rounded mx-auto d-block', '35%', '35%')
    spagehtm = '''
    <!DOCTYPE html>
    <html lang="pt-br">
        <table>
        <tr>
            <td scope="row">
                <font style="font-family: Courier New; font-size: 20px;"><b>Imagem =></b></font>
            </td>
            <td scope="row">
                <div>''' + simage01 + '''</div>
            </td>
        </tr>
    </html>'''
    sabntoke = 'teste'
    spagehtm = spagehtm  + abnf_websocket_js_socketio(sabntoke)
    spagehtm = spagehtm  + abnf_websocket_js_abeinfo()
    spagehtm = spagehtm  + abnf_websocket_css_menu_dropdown()
    return Response(spagehtm, mimetype="text/html")

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_teste_000 ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Área de teste do sistema.                                                                                                                           // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

@abnfxapp.route('/t000')
def abnf_teste_000():
    exit()
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    if False:
        snewpage = abnf_create_page([
            ('div-0', 'container', None, None),
            ('hr-0', None),
            ('div-0', 'row', None, None),
            ('div-0', 'col d-flex justify-content-center', None, None),
            ('div-0', 'w-50 p-3', 'background-color: #eee;', None),
            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
            ('legend-0', 'Login do Sistema'),
            ('hr-0', None),
            ('label-0',    'Usuário' , 'form-control-label'),
            ('input-0',    'susuario', 'form-control', 0, 30, '16px', None, 'ssenhdig', True, 0),
            ('label-0',    'Senha'   , 'form-control-label',),
            ('password-0', 'ssenhdig', 'form-control', 6, 30, '16px', None, 'btacesso', True, 0),
            ('hr-0', None),
            ('button-0',   'btacesso', 'btn btn-primary mt-2', 'Fazer Login'),
            # Área de testes (início)
            # ('hr-0', None),
            # ('file-0', 'fteste01', 'btn btn-primary mt-2', '.jpg,.png,.bmp', False),
            # ('hr-0', None),
            # ('select-0', 'llegumes', 'form-control', '16px', 'btacesso', llegumes, 1, None, True),
            # ('hr-0', None),
            # ('radio-0', 'iidcomid', '1', '0', '16px', 'F', 'CENOURA'),
            # ('radio-0', 'iidcomid', '2', '0', '16px', 'F', 'BATATA'),
            # ('radio-0', 'iidcomid', '3', '0', '16px', 'F', 'COUVE'),
            # ('hr-0', None),
            # ('radio-0', 'iidveicu', '1', '2', '16px', 'P', 'ONIX'),
            # ('radio-0', 'iidveicu', '2', '2', '16px', 'P', 'VECTRA'),
            # ('radio-0', 'iidveicu', '3', '2', '16px', 'P', 'CIVIC'),
            # ('hr-0', None),
            # ('checkbox-0', 'iidcen01', 'y' , None, '16px', 'F', 'CENOURA'),
            # ('checkbox-0', 'iidbat01', 'y' , 'y' , '16px', 'F', 'BATATA'),
            # ('checkbox-0', 'iidcou01', 'y' , 'x' , '16px', 'F', 'COUVE'),
            # ('hr-0', None),
            # ('checkbox-0', 'iidcen01', 'y' , None, '16px', 'P', 'CENOURA'),
            # ('checkbox-0', 'iidbat01', 'y' , 'y' , '16px', 'P', None),
            # ('checkbox-0', 'iidcou01', 'y' , 'y' , '16px', 'P', 'COUVE'),
            # Área de testes (fim)
            ('form-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
        ])
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    if True:
        snewpage = '''
        <div class="container">
            <hr>
            <div class="row">
                <div class="col d-flex justify-content-center">
                    <div class="w-100 p-3" style="background-color: #eee;">
                        <table class="table table-bordered table-sm table-responsive">
                            <tr class="table-active">
                                <td scope="row" colspan="2" align="center">
                                    <legend>Operacional - Entrada e Saída de Veículos</legend>
                                </td>
                            </tr>
                            <tr>
                                <td scope="row">
                                    <form method="POST" action="" class="border p-4 mt-2 rounded border-secondary border-3">
                                        <input id="csrf_token" name="csrf_token" type="hidden" value="IjgxNmE3ODc3NGJmNmFiMWE0NGRlNGExYWI0ZDQ1MGQ0Y2E0ODk1NWIi.ZpGAfA.H6QTTo1jWxdlxwfPqHFPv2iJfJ4">
                                            <fieldset>
                                                <div class="form-group row">
                                                    <label class="form-control-label" for="iidoesvl">Local</label>
                                                    <select autocomplete="off" class="form-control" id="iidoesvl" name="iidoesvl" onKeyUp="AbnfTabEnter(event,getElementById(&#39;ddataesv&#39;));" onfocus="this.select()" onkeypress="return AbnfScriptKey(event)" spellcheck="false" style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold;"><option value=""></option><option value="3">CRUZEIRO DO SUL (3)</option><option value="2">LIMA (2)</option><option selected value="1">RIO BRANCO (1)</option><option value="4">SAO PAULO (4)</option></select>
                                                </div>
                                            </fieldset>
                                            <fieldset>
                                                <div class="form-group row">
                                                    <input type="text" name="sfilt001" id="sfilt001" 
                                                    maxlength="100"
                                                    class="form-control"
                                                    autocomplete="off"
                                                    onfocus="this.select()"
                                                    spellcheck="false"
                                                    style="text-transform:uppercase; font-family: Courier New; font-size: 14px; font-weight: bold; color: brown"
                                                    onKeyUp="AbnfTabEnter(event,getElementById(&#39;iidoesvl&#39;));"
                                                    onkeypress="return AbnfScriptKey(event)"
                                                    spellcheck="false">
                                                </div>
                                            </fieldset>
                                            <script>
                                                var srela001 = document.querySelector("#iidoesvl");
                                                var sfilt001 = document.querySelector("#sfilt001");
                                                // Executa o filtro sempre que o valor do campo sfilt001 é alterado
                                                sfilt001.addEventListener("input", function() {
                                                    var stxtbusc = sfilt001.value.toUpperCase();
                                                    var palavras = stxtbusc.split(" ");
                                                    // Filtra as opções do select
                                                    for (var i = 0; i < srela001.options.length; i++) {
                                                        var option = srela001.options[i];
                                                        // Verifica se todas as palavras estão contidas na opção
                                                        var boptvali = true;
                                                        for (var j = 0; j < palavras.length; j++) {
                                                            if (!option.textContent.toUpperCase().includes(palavras[j])) {
                                                                boptvali = false;
                                                                break;
                                                            }
                                                        }
                                                        if (boptvali) {
                                                            option.hidden = false;
                                                        } else {
                                                            option.hidden = true;
                                                        }
                                                    }
                                                });
                                            </script>
                                            
                                            <input type="text" name="nsaldoin" id="nsaldoin" size=12 maxlength="12" value=""
                                            style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold; text-align:right;"
                                            onkeyup="AbnfNumMaskDecimal(this,3);"
                                            onfocus="this.select()" autocomplete="off" spellcheck="false">
                                            <fieldset>
                                            <div class="form-group row">
                                            <label class="form-control-label" for="ddataesv">Data</label>
                                            <input autocomplete="off" class="form-control" id="ddataesv" maxlength="10" name="ddataesv" onKeyUp="AbnfTabEnter(event,getElementById(&#39;thoraesv&#39;));" onfocus="this.select()" onkeypress="return AbnfScriptKey(event)" spellcheck="false" style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold;" type="date" value="2024-07-12">
                                            </div>
                                            </fieldset>
                                            <fieldset>
                                            <div class="form-group row">
                                            <label class="form-control-label" for="thoraesv">Hora</label>
                                            <input autocomplete="off" class="form-control" id="thoraesv" maxlength="100" name="thoraesv" onKeyUp="AbnfTabEnter(event,getElementById(&#39;stipomov&#39;));" onfocus="this.select()" onkeypress="return AbnfScriptKey(event)" spellcheck="false" style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold;" type="time" value="">
                                            </div>
                                            </fieldset>
                                            <fieldset>
                                            <div class="form-group row">
                                            <label class="form-control-label" for="stipomov">Tipo de movimentação</label>
                                            <select autocomplete="off" class="form-control" id="stipomov" name="stipomov" onKeyUp="AbnfTabEnter(event,getElementById(&#39;iodomvei&#39;));" onfocus="this.select()" onkeypress="return AbnfScriptKey(event)" spellcheck="false" style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold;"><option value=""></option><option value="E">ENTRADA</option><option value="S">SAIDA</option><option value="P">PONTO DE PASSAGEM</option></select>
                                            </div>
                                            </fieldset>
                                            <fieldset>
                                            <div class="form-group row">
                                            <label class="form-control-label" for="iodomvei">Odômetro</label>
                                            <input autocomplete="off" class="form-control" id="iodomvei" max="99999999" maxlength="6" min="1" name="iodomvei" onKeyUp="AbnfMaxLength(this,8);AbnfTabEnter(event,getElementById(&#39;irolevei&#39;));" onfocus="this.select()" onkeypress="return AbnfScriptIntegerOnly(event)" spellcheck="false" style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold;" type="number" value="491325">
                                            </div>
                                            </fieldset>
                                            <fieldset>
                                            <div class="form-group row">
                                            <label class="form-control-label" for="irolevei">Roleta</label>
                                            <input autocomplete="off" class="form-control" id="irolevei" max="99999999" maxlength="6" min="1" name="irolevei" onKeyUp="AbnfMaxLength(this,8);AbnfTabEnter(event,getElementById(&#39;iidolinh&#39;));" onfocus="this.select()" onkeypress="return AbnfScriptIntegerOnly(event)" spellcheck="false" style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold;" type="number" value="1">
                                            </div>
                                            </fieldset>
                                            <fieldset>
                                            <div class="form-group row">
                                            <label class="form-control-label" for="iidolinh">Linha</label>
                                            <select autocomplete="off" class="form-control" id="iidolinh" name="iidolinh" onKeyUp="AbnfTabEnter(event,getElementById(&#39;iidmot01&#39;));" onfocus="this.select()" onkeypress="return AbnfScriptKey(event)" spellcheck="false" style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold;"><option value=""></option><option value="4">1000 - RIO BRANCO X CRUZEIRO DO SUL (07H00)</option><option value="5">1001 - RIO BRANCO X CRUZEIRO DO SUL 19H00</option><option value="13">1002 - CRUZEIRO DO SUL X RIO BRANCO (07H00)</option><option value="14">1003 - CRUZEIRO DO SUL X RIO BRANCO (19H00)</option><option value="3">1010 - RIO BRANCO X TARAUACA</option><option value="12">1011 - TARAUACA X RIO BRANCO</option><option value="1">1013 - RIO BRANCO X ASSIS BRASIL</option><option value="2">1013-1 - RIO BRANCO X BRASILEIA</option><option value="10">1017 - ASSIS BRASIL X RIO BRANCO</option><option value="11">1017-1 - BRASILEIA X RIO BRANCO</option><option value="7">1022 - RIO BRANCO X BOCA DO ACRE - AM (06H00)</option><option value="8">1100 - RIO BRANCO X BOCA DO ACRE - AM (13H00)</option><option value="17">1101 - BOCA DO ACRE - AM X RIO BRANCO (13H00)</option><option value="16">1102 - BOCA DO ACRE - AM X RIO BRANCO (07H00)</option><option value="9">1199 - RIO BRANCO X PUERTO MALDONADO</option><option value="18">1199-1 - PUERTO MALDONADO - PERU X RIO BRANCO</option><option value="24">1509 - RIO DE JANEIRO X LIMA - PERU</option><option value="25">1511 - LIMA - PERU X RIO DE JANEIRO</option><option value="6">8000 - RIO BRANCO X CRUZEIRO DO SUL (EXTRA 19HRS)</option><option value="15">8001 - CRUZEIRO DO SUL X RIO BRANCO (EXTRA 19H00)</option><option value="27">8002 - RIO BRANCO X CRUZEIRO DO SUL (EXTRA 19H00)</option><option value="32">8008 - RIO BRANCO X CRUZEIRO DO SUL (EXTRA 07HRS)</option><option value="26">F01 - FRETAMENTO RODOVIARIO</option><option value="19">I01 - RIO BRANCO X SENADOR GUIOMARD (SEMIURBANO)</option><option value="21">I01 - INTERMUNICIPAL RIO BRANCO X SENADOR GUIOMARD</option><option value="20">I02 - RIO BRANCO X BUJARI (SEMIURBANO)</option><option value="22">I02 - INTERMUNICIPAL RIO BRANCO X BUJARI</option><option value="28">R01 - RIO BRANCO X PORTO ALONSO</option><option value="29">R011 - PORTO ALONSO X RIO BRANCO</option><option value="30">R02 - RIO BRANCO X CAQUETA</option><option value="31">R022 - CAQUETA X RIO BRANCO</option><option value="23">SOS - SOCORRO</option></select>
                                            </div>
                                            </fieldset>
                                            <fieldset>
                                            <div class="form-group row">
                                            <input type="text" name="sfilt002" id="sfilt002"
                                            maxlength="100"
                                            class="form-control"
                                            autocomplete="off"
                                            onfocus="this.select()"
                                            spellcheck="false"
                                            style="text-transform:uppercase; font-family: Courier New; font-size: 14px; font-weight: bold; color: brown"
                                            onKeyUp="AbnfTabEnter(event,getElementById(&#39;iidolinh&#39;));"
                                            onkeypress="return AbnfScriptKey(event)"
                                            spellcheck="false">
                                            </div>
                                            </fieldset>
                                            <script>
                                            var srela002 = document.querySelector("#iidolinh");
                                            var sfilt002 = document.querySelector("#sfilt002");
                                            // Executa o filtro sempre que o valor do campo sfilt002 é alterado
                                            sfilt002.addEventListener("input", function() {
                                            var stxtbusc = sfilt002.value.toUpperCase();
                                            var palavras = stxtbusc.split(" ");
                                            // Filtra as opções do select
                                            for (var i = 0; i < srela002.options.length; i++) {
                                            var option = srela002.options[i];
                                            // Verifica se todas as palavras estão contidas na opção
                                            var boptvali = true;
                                            for (var j = 0; j < palavras.length; j++) {
                                            if (!option.textContent.toUpperCase().includes(palavras[j])) {
                                            boptvali = false;
                                            break;
                                            }
                                            }
                                            if (boptvali) {
                                            option.hidden = false;
                                            } else {
                                            option.hidden = true;
                                            }
                                            }
                                            });
                                            </script>
                                            <fieldset>
                                            <div class="form-group row">
                                            <label class="form-control-label" for="iidmot01">Motorista 01</label>
                                            <select autocomplete="off" class="form-control" id="iidmot01" name="iidmot01" onKeyUp="AbnfTabEnter(event,getElementById(&#39;iidmot02&#39;));" onfocus="this.select()" onkeypress="return AbnfScriptKey(event)" spellcheck="false" style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold;"><option value=""></option><option value="2">ADEMILTON MARTINS DE MENEZE (7)</option><option value="3">ALAN RODRIGUES SALDANHA (19)</option><option value="4">AMARAL LIMA DINIZ (38)</option><option value="5">ANGELICA DA SILVA BRANDAO (119)</option><option value="6">ANTONIEL SANTOS DE SOUZA (8)</option><option value="7">ANTONIO ALDENIR FERREIRA (6)</option><option value="8">ANTONIO JOSE DE SOUZA BARBO (121)</option><option value="11">AURILENE DE ALMEIDA LIMA (28)</option><option value="12">CARLITO DOS SANTOS (5)</option><option value="120">CARLOS ALBERTO TEIXEIRA SANTIAGO (8017)</option><option value="121">CARLOS ANDRE CAVALCANTE VIANA (8018)</option><option value="109">CARLOS CESAR RIBEIRO (131)</option><option value="13">CLAUDIO RIBEIRO DA SILVA (50)</option><option value="14">CLENILSON SILVA DO AMARAL (80)</option><option value="15">CLEONE LOPES DA SILVA (73)</option><option value="16">CLEUSON ALVES LEITE (40)</option><option value="17">CLOVIS ROQUE BANDEIRA (105)</option><option value="18">DANIEL DO NASCIMENTO ABREU (72)</option><option value="19">DANIELA ALMEIDA DE OLIVEIRA (64)</option><option value="20">DAVID DE ALMEIDA DA ROCHA (76)</option><option value="21">DJONATHAN COSTA DOS REIS (47)</option><option value="104">EDINALDO DA SILVA LOPES (8011)</option><option value="111">EDNALDO DE OLIVEIRA MORAES (8008)</option><option value="22">EDNILSON RIBEIRO DA SILVA (17)</option><option value="23">ELIESER GONCALVES PEIXOTO (112)</option><option value="24">ELITA PAULINO DE BARROS (44)</option><option value="25">EMERSON OLIVEIRA DA SILVA A (74)</option><option value="26">FABIANA DE OLIVEIRA RODRIGU (24)</option><option value="27">FALIK RANGEL MALTA DE MENEZ (12)</option><option value="28">FERNANDO QUEIROZ CANUTO DE (128)</option><option value="29">FRANC LANDY ALMEIDA DOS SAN (124)</option><option value="30">FRANCISCO ALCENIR DA SILVA (97)</option><option value="31">FRANCISCO OSIEL HOLANDA LOP (90)</option><option value="32">FRANCISCO PEREIRA DE QUEIRO (11)</option><option value="33">FRANCISCO UIDULO MOURA DE B (43)</option><option value="34">FRANCISCO XAVIER DA SILVA (45)</option><option value="35">FRANCIVALDO BARBOSA DE LIMA (79)</option><option value="36">GEOVANE ARAUJO DA SILVA (42)</option><option value="37">GIOVANE SIQUEIRA FERREIRA (84)</option><option value="38">HELIO DA SILVA LINS JUNIOR (63)</option><option value="110">HORLANDO RAFAEL DE OLIVEIRA RIBEIRO (130)</option><option value="41">ISMAEL DO VALE SILVA (107)</option><option value="108">IZACK DA SILVA (8004)</option><option value="42">IZAIAS ALVES DE LIMA (14)</option><option value="44">JAILSON CORDEIRO MACHADO SI (13)</option><option value="45">JEAN DE ARAUJO SILVA (69)</option><option value="117">JEREMIAS DA SILVA (8014)</option><option value="118">JERSIEL PINHEIRO MAGALHAES (8015)</option><option value="46">JESSE SILVA PESSOA (20)</option><option value="47">JOABE DA SILVA GARCIA (110)</option><option value="48">JOABE MENESES CRUZ (100)</option><option value="49">JOAO DA SILVA GOMES (106)</option><option value="50">JOAO PAULO MANUARIO (15)</option><option value="51">JOAO PAULO VASCONCELOS OLIV (103)</option><option value="122">JOAO SERAFIM MENESES (8019)</option><option value="52">JONATHAN SOUSA DA SILVA (37)</option><option value="53">JORGE CORREIA DE PAIVA JUNI (91)</option><option value="54">JOSE ALTEMIR DE QUEIROZ CAS (30)</option><option value="106">JOSE CARLOS DO ROSARIO (8005)</option><option value="116">JOSE CARLOS FELIX DE OLIVEIRA (8013)</option><option value="55">JOSE DA COSTA MACEDO (99)</option><option value="57">JOSE ELISSON OLIVEIRA SOUZA (21)</option><option value="58">JOSE JARDESON PAULA ROGERIO (104)</option><option value="107">JOSE LUIZ DA ROCHA RODRIGUES LIMA (8003)</option><option value="59">JOSE MARIA NASCIMENTO DOS S (53)</option><option value="60">JOSE MARIA SOLON DA PAZ (39)</option><option value="115">JOSUE RIBEIRO DA SILVA (8012)</option><option value="61">KENNEDY SILVA DE SOUZA (113)</option><option value="62">LEONARDO RODRIGUES DA COSTA (78)</option><option value="65">LUIZ RIBEIRO SILVA (33)</option><option value="66">MAICO DIONE BRAGA DE PAIVA (27)</option><option value="114">MANOEL ANGELO NOGUEIRA DA SILVA (8002)</option><option value="112">MARCIEL SOUZA DA SILVA (8009)</option><option value="68">MARIA MADALENA BRITO MATEUS (25)</option><option value="69">MARIA MAIRA DE SOUSA DA SIL (118)</option><option value="70">MAURICELIO FREIRE DA SILVA (68)</option><option value="71">MAURO ESCLEIDE DOS SANTOS A (41)</option><option value="72">MELQUISEDEQUE ARAUJO DE LIM (31)</option><option value="113">NATANAEL SOARES DA SILVA (8007)</option><option value="76">ORCLEILTON DE SOUZA MONTEIR (108)</option><option value="77">OSVALDO FERREIRA DA SILVA (89)</option><option value="78">PEDRO SALDANHA DA SILVA (51)</option><option value="105">RAIMUNDO ANTONIO DE MELO CUNHO (8001)</option><option value="81">RAIMUNDO NONATO FONTENELLE (125)</option><option value="82">RAIMUNDO NONATO SILVA DA (109)</option><option value="83">RAYELI FALCAO DE LIMA (4)</option><option value="84">REGINALDO DA COSTA FALCAO (81)</option><option value="85">RIAN LUCAS DE OLIVEIRA PINH (101)</option><option value="86">RICARDO RAMALHO DO NASCIMEN (115)</option><option value="87">ROBERTO MARINHO DE SOUZA (111)</option><option value="89">RONALDO GONCALVES PINTO (86)</option><option value="90">RONALDO RIBEIRO DOS SANTOS (116)</option><option value="91">ROSINEIDE CHAVES DA SILVA (3)</option><option value="92">SAMUEL PITER SANTOS DE SOUZ (127)</option><option value="93">SANDRO NASCIMENTO LEONE (67)</option><option value="94">SARA JANE BARBOSA DE QUEIRO (10)</option><option value="95">TALISSON DE OLIVEIRA FREITA (9)</option><option value="96">TAMIRES ALVES DA SILVA (56)</option><option value="98">TATIANA BARBOSA DE QUEIROZ (117)</option><option value="99">VALDOMIRO RIBEIRO OLIVEIRA (34)</option><option value="100">VANESSA MENDONCA UCHOA (35)</option><option value="101">WHENESON DIAS GOMES (122)</option><option value="102">WILLIAN MOTA DE SOUZA (62)</option><option value="119">WILMERSON SILVA DO AMARAL (8016)</option></select>
                                            </div>
                                            </fieldset>
                                            <fieldset>
                                            <div class="form-group row">
                                            <input type="text" name="sfilt003" id="sfilt003"
                                            maxlength="100"
                                            class="form-control"
                                            autocomplete="off"
                                            onfocus="this.select()"
                                            spellcheck="false"
                                            style="text-transform:uppercase; font-family: Courier New; font-size: 14px; font-weight: bold; color: brown"
                                            onKeyUp="AbnfTabEnter(event,getElementById(&#39;iidmot01&#39;));"
                                            onkeypress="return AbnfScriptKey(event)"
                                            spellcheck="false">
                                            </div>
                                            </fieldset>
                                            <script>
                                            var srela003 = document.querySelector("#iidmot01");
                                            var sfilt003 = document.querySelector("#sfilt003");
                                            // Executa o filtro sempre que o valor do campo sfilt003 é alterado
                                            sfilt003.addEventListener("input", function() {
                                            var stxtbusc = sfilt003.value.toUpperCase();
                                            var palavras = stxtbusc.split(" ");
                                            // Filtra as opções do select
                                            for (var i = 0; i < srela003.options.length; i++) {
                                            var option = srela003.options[i];
                                            // Verifica se todas as palavras estão contidas na opção
                                            var boptvali = true;
                                            for (var j = 0; j < palavras.length; j++) {
                                            if (!option.textContent.toUpperCase().includes(palavras[j])) {
                                            boptvali = false;
                                            break;
                                            }
                                            }
                                            if (boptvali) {
                                            option.hidden = false;
                                            } else {
                                            option.hidden = true;
                                            }
                                            }
                                            });
                                            </script>
                                            <fieldset>
                                            <div class="form-group row">
                                            <label class="form-control-label" for="iidmot02">Motorista 02</label>
                                            <select autocomplete="off" class="form-control" id="iidmot02" name="iidmot02" onKeyUp="AbnfTabEnter(event,getElementById(&#39;iidcob01&#39;));" onfocus="this.select()" onkeypress="return AbnfScriptKey(event)" spellcheck="false" style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold;"><option value=""></option><option value="2">ADEMILTON MARTINS DE MENEZE (7)</option><option value="3">ALAN RODRIGUES SALDANHA (19)</option><option value="4">AMARAL LIMA DINIZ (38)</option><option value="5">ANGELICA DA SILVA BRANDAO (119)</option><option value="6">ANTONIEL SANTOS DE SOUZA (8)</option><option value="7">ANTONIO ALDENIR FERREIRA (6)</option><option value="8">ANTONIO JOSE DE SOUZA BARBO (121)</option><option value="11">AURILENE DE ALMEIDA LIMA (28)</option><option value="12">CARLITO DOS SANTOS (5)</option><option value="120">CARLOS ALBERTO TEIXEIRA SANTIAGO (8017)</option><option value="121">CARLOS ANDRE CAVALCANTE VIANA (8018)</option><option value="109">CARLOS CESAR RIBEIRO (131)</option><option value="13">CLAUDIO RIBEIRO DA SILVA (50)</option><option value="14">CLENILSON SILVA DO AMARAL (80)</option><option value="15">CLEONE LOPES DA SILVA (73)</option><option value="16">CLEUSON ALVES LEITE (40)</option><option value="17">CLOVIS ROQUE BANDEIRA (105)</option><option value="18">DANIEL DO NASCIMENTO ABREU (72)</option><option value="19">DANIELA ALMEIDA DE OLIVEIRA (64)</option><option value="20">DAVID DE ALMEIDA DA ROCHA (76)</option><option value="21">DJONATHAN COSTA DOS REIS (47)</option><option value="104">EDINALDO DA SILVA LOPES (8011)</option><option value="111">EDNALDO DE OLIVEIRA MORAES (8008)</option><option value="22">EDNILSON RIBEIRO DA SILVA (17)</option><option value="23">ELIESER GONCALVES PEIXOTO (112)</option><option value="24">ELITA PAULINO DE BARROS (44)</option><option value="25">EMERSON OLIVEIRA DA SILVA A (74)</option><option value="26">FABIANA DE OLIVEIRA RODRIGU (24)</option><option value="27">FALIK RANGEL MALTA DE MENEZ (12)</option><option value="28">FERNANDO QUEIROZ CANUTO DE (128)</option><option value="29">FRANC LANDY ALMEIDA DOS SAN (124)</option><option value="30">FRANCISCO ALCENIR DA SILVA (97)</option><option value="31">FRANCISCO OSIEL HOLANDA LOP (90)</option><option value="32">FRANCISCO PEREIRA DE QUEIRO (11)</option><option value="33">FRANCISCO UIDULO MOURA DE B (43)</option><option value="34">FRANCISCO XAVIER DA SILVA (45)</option><option value="35">FRANCIVALDO BARBOSA DE LIMA (79)</option><option value="36">GEOVANE ARAUJO DA SILVA (42)</option><option value="37">GIOVANE SIQUEIRA FERREIRA (84)</option><option value="38">HELIO DA SILVA LINS JUNIOR (63)</option><option value="110">HORLANDO RAFAEL DE OLIVEIRA RIBEIRO (130)</option><option value="41">ISMAEL DO VALE SILVA (107)</option><option value="108">IZACK DA SILVA (8004)</option><option value="42">IZAIAS ALVES DE LIMA (14)</option><option value="44">JAILSON CORDEIRO MACHADO SI (13)</option><option value="45">JEAN DE ARAUJO SILVA (69)</option><option value="117">JEREMIAS DA SILVA (8014)</option><option value="118">JERSIEL PINHEIRO MAGALHAES (8015)</option><option value="46">JESSE SILVA PESSOA (20)</option><option value="47">JOABE DA SILVA GARCIA (110)</option><option value="48">JOABE MENESES CRUZ (100)</option><option value="49">JOAO DA SILVA GOMES (106)</option><option value="50">JOAO PAULO MANUARIO (15)</option><option value="51">JOAO PAULO VASCONCELOS OLIV (103)</option><option value="122">JOAO SERAFIM MENESES (8019)</option><option value="52">JONATHAN SOUSA DA SILVA (37)</option><option value="53">JORGE CORREIA DE PAIVA JUNI (91)</option><option value="54">JOSE ALTEMIR DE QUEIROZ CAS (30)</option><option value="106">JOSE CARLOS DO ROSARIO (8005)</option><option value="116">JOSE CARLOS FELIX DE OLIVEIRA (8013)</option><option value="55">JOSE DA COSTA MACEDO (99)</option><option value="57">JOSE ELISSON OLIVEIRA SOUZA (21)</option><option value="58">JOSE JARDESON PAULA ROGERIO (104)</option><option value="107">JOSE LUIZ DA ROCHA RODRIGUES LIMA (8003)</option><option value="59">JOSE MARIA NASCIMENTO DOS S (53)</option><option value="60">JOSE MARIA SOLON DA PAZ (39)</option><option value="115">JOSUE RIBEIRO DA SILVA (8012)</option><option value="61">KENNEDY SILVA DE SOUZA (113)</option><option value="62">LEONARDO RODRIGUES DA COSTA (78)</option><option value="65">LUIZ RIBEIRO SILVA (33)</option><option value="66">MAICO DIONE BRAGA DE PAIVA (27)</option><option value="114">MANOEL ANGELO NOGUEIRA DA SILVA (8002)</option><option value="112">MARCIEL SOUZA DA SILVA (8009)</option><option value="68">MARIA MADALENA BRITO MATEUS (25)</option><option value="69">MARIA MAIRA DE SOUSA DA SIL (118)</option><option value="70">MAURICELIO FREIRE DA SILVA (68)</option><option value="71">MAURO ESCLEIDE DOS SANTOS A (41)</option><option value="72">MELQUISEDEQUE ARAUJO DE LIM (31)</option><option value="113">NATANAEL SOARES DA SILVA (8007)</option><option value="76">ORCLEILTON DE SOUZA MONTEIR (108)</option><option value="77">OSVALDO FERREIRA DA SILVA (89)</option><option value="78">PEDRO SALDANHA DA SILVA (51)</option><option value="105">RAIMUNDO ANTONIO DE MELO CUNHO (8001)</option><option value="81">RAIMUNDO NONATO FONTENELLE (125)</option><option value="82">RAIMUNDO NONATO SILVA DA (109)</option><option value="83">RAYELI FALCAO DE LIMA (4)</option><option value="84">REGINALDO DA COSTA FALCAO (81)</option><option value="85">RIAN LUCAS DE OLIVEIRA PINH (101)</option><option value="86">RICARDO RAMALHO DO NASCIMEN (115)</option><option value="87">ROBERTO MARINHO DE SOUZA (111)</option><option value="89">RONALDO GONCALVES PINTO (86)</option><option value="90">RONALDO RIBEIRO DOS SANTOS (116)</option><option value="91">ROSINEIDE CHAVES DA SILVA (3)</option><option value="92">SAMUEL PITER SANTOS DE SOUZ (127)</option><option value="93">SANDRO NASCIMENTO LEONE (67)</option><option value="94">SARA JANE BARBOSA DE QUEIRO (10)</option><option value="95">TALISSON DE OLIVEIRA FREITA (9)</option><option value="96">TAMIRES ALVES DA SILVA (56)</option><option value="98">TATIANA BARBOSA DE QUEIROZ (117)</option><option value="99">VALDOMIRO RIBEIRO OLIVEIRA (34)</option><option value="100">VANESSA MENDONCA UCHOA (35)</option><option value="101">WHENESON DIAS GOMES (122)</option><option value="102">WILLIAN MOTA DE SOUZA (62)</option><option value="119">WILMERSON SILVA DO AMARAL (8016)</option></select>
                                            </div>
                                            </fieldset>
                                            <fieldset>
                                            <div class="form-group row">
                                            <input type="text" name="sfilt004" id="sfilt004"
                                            maxlength="100"
                                            class="form-control"
                                            autocomplete="off"
                                            onfocus="this.select()"
                                            spellcheck="false"
                                            style="text-transform:uppercase; font-family: Courier New; font-size: 14px; font-weight: bold; color: brown"
                                            onKeyUp="AbnfTabEnter(event,getElementById(&#39;iidmot02&#39;));"
                                            onkeypress="return AbnfScriptKey(event)"
                                            spellcheck="false">
                                            </div>
                                            </fieldset>
                                            <script>
                                            var srela004 = document.querySelector("#iidmot02");
                                            var sfilt004 = document.querySelector("#sfilt004");
                                            // Executa o filtro sempre que o valor do campo sfilt004 é alterado
                                            sfilt004.addEventListener("input", function() {
                                            var stxtbusc = sfilt004.value.toUpperCase();
                                            var palavras = stxtbusc.split(" ");
                                            // Filtra as opções do select
                                            for (var i = 0; i < srela004.options.length; i++) {
                                            var option = srela004.options[i];
                                            // Verifica se todas as palavras estão contidas na opção
                                            var boptvali = true;
                                            for (var j = 0; j < palavras.length; j++) {
                                            if (!option.textContent.toUpperCase().includes(palavras[j])) {
                                            boptvali = false;
                                            break;
                                            }
                                            }
                                            if (boptvali) {
                                            option.hidden = false;
                                            } else {
                                            option.hidden = true;
                                            }
                                            }
                                            });
                                            </script>
                                            <fieldset>
                                            <div class="form-group row">
                                            <label class="form-control-label" for="iidcob01">Cobrador 01</label>
                                            <select autocomplete="off" class="form-control" id="iidcob01" name="iidcob01" onKeyUp="AbnfTabEnter(event,getElementById(&#39;sobserva&#39;));" onfocus="this.select()" onkeypress="return AbnfScriptKey(event)" spellcheck="false" style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold;"><option value=""></option><option value="2">ADEMILTON MARTINS DE MENEZE (7)</option><option value="3">ALAN RODRIGUES SALDANHA (19)</option><option value="4">AMARAL LIMA DINIZ (38)</option><option value="5">ANGELICA DA SILVA BRANDAO (119)</option><option value="6">ANTONIEL SANTOS DE SOUZA (8)</option><option value="7">ANTONIO ALDENIR FERREIRA (6)</option><option value="8">ANTONIO JOSE DE SOUZA BARBO (121)</option><option value="11">AURILENE DE ALMEIDA LIMA (28)</option><option value="12">CARLITO DOS SANTOS (5)</option><option value="120">CARLOS ALBERTO TEIXEIRA SANTIAGO (8017)</option><option value="121">CARLOS ANDRE CAVALCANTE VIANA (8018)</option><option value="109">CARLOS CESAR RIBEIRO (131)</option><option value="13">CLAUDIO RIBEIRO DA SILVA (50)</option><option value="14">CLENILSON SILVA DO AMARAL (80)</option><option value="15">CLEONE LOPES DA SILVA (73)</option><option value="16">CLEUSON ALVES LEITE (40)</option><option value="17">CLOVIS ROQUE BANDEIRA (105)</option><option value="18">DANIEL DO NASCIMENTO ABREU (72)</option><option value="19">DANIELA ALMEIDA DE OLIVEIRA (64)</option><option value="20">DAVID DE ALMEIDA DA ROCHA (76)</option><option value="21">DJONATHAN COSTA DOS REIS (47)</option><option value="104">EDINALDO DA SILVA LOPES (8011)</option><option value="111">EDNALDO DE OLIVEIRA MORAES (8008)</option><option value="22">EDNILSON RIBEIRO DA SILVA (17)</option><option value="23">ELIESER GONCALVES PEIXOTO (112)</option><option value="24">ELITA PAULINO DE BARROS (44)</option><option value="25">EMERSON OLIVEIRA DA SILVA A (74)</option><option value="26">FABIANA DE OLIVEIRA RODRIGU (24)</option><option value="27">FALIK RANGEL MALTA DE MENEZ (12)</option><option value="28">FERNANDO QUEIROZ CANUTO DE (128)</option><option value="29">FRANC LANDY ALMEIDA DOS SAN (124)</option><option value="30">FRANCISCO ALCENIR DA SILVA (97)</option><option value="31">FRANCISCO OSIEL HOLANDA LOP (90)</option><option value="32">FRANCISCO PEREIRA DE QUEIRO (11)</option><option value="33">FRANCISCO UIDULO MOURA DE B (43)</option><option value="34">FRANCISCO XAVIER DA SILVA (45)</option><option value="35">FRANCIVALDO BARBOSA DE LIMA (79)</option><option value="36">GEOVANE ARAUJO DA SILVA (42)</option><option value="37">GIOVANE SIQUEIRA FERREIRA (84)</option><option value="38">HELIO DA SILVA LINS JUNIOR (63)</option><option value="110">HORLANDO RAFAEL DE OLIVEIRA RIBEIRO (130)</option><option value="41">ISMAEL DO VALE SILVA (107)</option><option value="108">IZACK DA SILVA (8004)</option><option value="42">IZAIAS ALVES DE LIMA (14)</option><option value="44">JAILSON CORDEIRO MACHADO SI (13)</option><option value="45">JEAN DE ARAUJO SILVA (69)</option><option value="117">JEREMIAS DA SILVA (8014)</option><option value="118">JERSIEL PINHEIRO MAGALHAES (8015)</option><option value="46">JESSE SILVA PESSOA (20)</option><option value="47">JOABE DA SILVA GARCIA (110)</option><option value="48">JOABE MENESES CRUZ (100)</option><option value="49">JOAO DA SILVA GOMES (106)</option><option value="50">JOAO PAULO MANUARIO (15)</option><option value="51">JOAO PAULO VASCONCELOS OLIV (103)</option><option value="122">JOAO SERAFIM MENESES (8019)</option><option value="52">JONATHAN SOUSA DA SILVA (37)</option><option value="53">JORGE CORREIA DE PAIVA JUNI (91)</option><option value="54">JOSE ALTEMIR DE QUEIROZ CAS (30)</option><option value="106">JOSE CARLOS DO ROSARIO (8005)</option><option value="116">JOSE CARLOS FELIX DE OLIVEIRA (8013)</option><option value="55">JOSE DA COSTA MACEDO (99)</option><option value="57">JOSE ELISSON OLIVEIRA SOUZA (21)</option><option value="58">JOSE JARDESON PAULA ROGERIO (104)</option><option value="107">JOSE LUIZ DA ROCHA RODRIGUES LIMA (8003)</option><option value="59">JOSE MARIA NASCIMENTO DOS S (53)</option><option value="60">JOSE MARIA SOLON DA PAZ (39)</option><option value="115">JOSUE RIBEIRO DA SILVA (8012)</option><option value="61">KENNEDY SILVA DE SOUZA (113)</option><option value="62">LEONARDO RODRIGUES DA COSTA (78)</option><option value="65">LUIZ RIBEIRO SILVA (33)</option><option value="66">MAICO DIONE BRAGA DE PAIVA (27)</option><option value="114">MANOEL ANGELO NOGUEIRA DA SILVA (8002)</option><option value="112">MARCIEL SOUZA DA SILVA (8009)</option><option value="68">MARIA MADALENA BRITO MATEUS (25)</option><option value="69">MARIA MAIRA DE SOUSA DA SIL (118)</option><option value="70">MAURICELIO FREIRE DA SILVA (68)</option><option value="71">MAURO ESCLEIDE DOS SANTOS A (41)</option><option value="72">MELQUISEDEQUE ARAUJO DE LIM (31)</option><option value="113">NATANAEL SOARES DA SILVA (8007)</option><option value="76">ORCLEILTON DE SOUZA MONTEIR (108)</option><option value="77">OSVALDO FERREIRA DA SILVA (89)</option><option value="78">PEDRO SALDANHA DA SILVA (51)</option><option value="105">RAIMUNDO ANTONIO DE MELO CUNHO (8001)</option><option value="81">RAIMUNDO NONATO FONTENELLE (125)</option><option value="82">RAIMUNDO NONATO SILVA DA (109)</option><option value="83">RAYELI FALCAO DE LIMA (4)</option><option value="84">REGINALDO DA COSTA FALCAO (81)</option><option value="85">RIAN LUCAS DE OLIVEIRA PINH (101)</option><option value="86">RICARDO RAMALHO DO NASCIMEN (115)</option><option value="87">ROBERTO MARINHO DE SOUZA (111)</option><option value="89">RONALDO GONCALVES PINTO (86)</option><option value="90">RONALDO RIBEIRO DOS SANTOS (116)</option><option value="91">ROSINEIDE CHAVES DA SILVA (3)</option><option value="92">SAMUEL PITER SANTOS DE SOUZ (127)</option><option value="93">SANDRO NASCIMENTO LEONE (67)</option><option value="94">SARA JANE BARBOSA DE QUEIRO (10)</option><option value="95">TALISSON DE OLIVEIRA FREITA (9)</option><option value="96">TAMIRES ALVES DA SILVA (56)</option><option value="98">TATIANA BARBOSA DE QUEIROZ (117)</option><option value="99">VALDOMIRO RIBEIRO OLIVEIRA (34)</option><option value="100">VANESSA MENDONCA UCHOA (35)</option><option value="101">WHENESON DIAS GOMES (122)</option><option value="102">WILLIAN MOTA DE SOUZA (62)</option><option value="119">WILMERSON SILVA DO AMARAL (8016)</option></select>
                                            </div>
                                            </fieldset>
                                            <fieldset>
                                            <div class="form-group row">
                                            <input type="text" name="sfilt006" id="sfilt006"
                                            maxlength="100"
                                            class="form-control"
                                            autocomplete="off"
                                            onfocus="this.select()"
                                            spellcheck="false"
                                            style="text-transform:uppercase; font-family: Courier New; font-size: 14px; font-weight: bold; color: brown"
                                            onKeyUp="AbnfTabEnter(event,getElementById(&#39;iidcob01&#39;));"
                                            onkeypress="return AbnfScriptKey(event)"
                                            spellcheck="false">
                                            </div>
                                            </fieldset>
                                            <script>
                                            var srela006 = document.querySelector("#iidcob01");
                                            var sfilt006 = document.querySelector("#sfilt006");
                                            // Executa o filtro sempre que o valor do campo sfilt006 é alterado
                                            sfilt006.addEventListener("input", function() {
                                            var stxtbusc = sfilt006.value.toUpperCase();
                                            var palavras = stxtbusc.split(" ");
                                            // Filtra as opções do select
                                            for (var i = 0; i < srela006.options.length; i++) {
                                            var option = srela006.options[i];
                                            // Verifica se todas as palavras estão contidas na opção
                                            var boptvali = true;
                                            for (var j = 0; j < palavras.length; j++) {
                                            if (!option.textContent.toUpperCase().includes(palavras[j])) {
                                            boptvali = false;
                                            break;
                                            }
                                            }
                                            if (boptvali) {
                                            option.hidden = false;
                                            } else {
                                            option.hidden = true;
                                            }
                                            }
                                            });
                                            </script>
                                            <hr>
                            <fieldset>
                            <div class="form-group row">
                            <label class="form-control-label" for="sobserva">Observação (Opcional) (1000 caracteres)</label>
                            <textarea autocomplete="off" class="form-control" id="sobserva" maxlength="1000" minlength="2" name="sobserva" onKeyUp="AbnfTabEnter(event,getElementById(&#39;btmodsav&#39;));" onfocus="this.select()" onkeypress="return AbnfScriptKey(event)" spellcheck="false" style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold;">
                            </textarea>
                            </div>
                            <div class="input-group mb-3">
                            <span class="input-group-text">$</span>
                            <input type="text" class="form-control" id="financialInput">
                            </div>
                            <hr>
                            <button type="button" id="btmodsav" class="btn btn-primary mt-2" data-bs-toggle="modal" data-bs-target="#abnfconfsav" href="#">Salvar</button>
                            <input class="btn btn-secondary mt-2" id="btcancel" name="btcancel" onclick="AbnfButtonDisable(this);" type="submit" value="Cancelar">
                            <hr>
                            <button type="button" class="btn btn-success" data-bs-toggle="collapse" data-bs-target="#sdiv0001">Opções adicionais</button>
                            <!-- Modal de gravação -->
                            <div class="modal fade" id="abnfconfsav" tabindex="-1" aria-labelledby="abnfconfsavLabel" aria-hidden="true">
                            <div class="modal-dialog">
                            <div class="modal-content">
                            <div class="modal-header">
                            <h1 class="modal-title fs-5" id="abnfconfsavLabel">Salvar Registro</h1>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                            Confirma a gravação?
                            </div>
                            <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                            <input class="btn btn-primary mt-1" id="btsalreg" name="btsalreg" onclick="AbnfTimeButtonDisable(this,3);" type="submit" value="Salvar">
                            </div>
                            </div>
                            </div>
                            </div>
                            <!-- Fim modais -->
                            <div id="sdiv0001" class="form-group collapse">
                            <br>
                            <input class="form-check-input" id="bperod1k" name="bperod1k" type="checkbox" value="y">
                            <font color="black" face="Courier New" size="3"><b> Permite total de quilometragem acima de 1000 km</b></font><br>
                            <input class="form-check-input" id="bperro1k" name="bperro1k" type="checkbox" value="y">
                            <font color="black" face="Courier New" size="3"><b> Permite total de passageiros acima de 1000 passageiros</b></font><br>
                            </div>
                            </form>
                            </td>
                            <td scope="row">
                            <form method="POST" action="" class="border p-4 mt-2 rounded border-secondary border-3">
                            <table class="table table-bordered table-sm table-responsive">
                            <tr class="table-active">
                            <td scope="row">
                            <font style="font-family: Courier New; font-size: 20px;"><b>Veículo:</b></font>
                            </td>
                            <td scope="row" align="left">
                            <font style="text-transform:uppercase; font-family: Courier New; font-size: 22px; font-weight: bold; color: blue"><b>
                            800 (CGH2E24)
                            </b></font>
                            </td>
                            </tr>
                            <tr class="table-secondary">
                            <td scope="row" colspan="2" bgcolor="cyan">
                            <font style="font-family: Courier New; font-size: 20px; font-weight: bold; color: darkcyan"><b>Última movimentação do veículo:</b></font>
                            </td>
                            </tr>
                            <tr>
                            <td scope="row">
                            <font style="font-family: Courier New; font-size: 15px;"><b>Local:</b></font>
                            </td>
                            <td scope="row">
                            <font style="text-transform:uppercase; font-family: Courier New; font-size: 15px; font-weight: bold; color: brown"><b>
                            RIO BRANCO (1)
                            </b></font>
                            </td>
                            </tr>
                            <tr>
                            <td scope="row">
                            <font style="font-family: Courier New; font-size: 15px;"><b>Data:</b></font>
                            </td>
                            <td scope="row">
                            <font style="text-transform:uppercase; font-family: Courier New; font-size: 15px; font-weight: bold; color: brown"><b>
                            07/07/2024
                            </b></font>
                            </td>
                            </tr>
                            <tr>
                            <td scope="row">
                            <font style="font-family: Courier New; font-size: 15px;"><b>Hora:</b></font>
                            </td>
                            <td scope="row">
                            <font style="text-transform:uppercase; font-family: Courier New; font-size: 15px; font-weight: bold; color: brown"><b>
                            08:20
                            </b></font>
                            </td>
                            </tr>
                            <tr>
                            <td scope="row">
                            <font style="font-family: Courier New; font-size: 15px;"><b>Tipo mov:</b></font>
                            </td>
                            <td scope="row">
                            <font style="text-transform:uppercase; font-family: Courier New; font-size: 15px; font-weight: bold; color: brown"><b>
                            ENTRADA
                            </b></font>
                            </td>
                            </tr>
                            <tr>
                            <td scope="row">
                            <font style="font-family: Courier New; font-size: 15px;"><b>Odômetro:</b></font>
                            </td>
                            <td scope="row">
                            <font style="text-transform:uppercase; font-family: Courier New; font-size: 15px; font-weight: bold; color: brown"><b>
                            491325
                            </b></font>
                            </td>
                            </tr>
                            <tr>
                            <td scope="row">
                            <font style="font-family: Courier New; font-size: 15px;"><b>Roleta:</b></font>
                            </td>
                            <td scope="row">
                            <font style="text-transform:uppercase; font-family: Courier New; font-size: 15px; font-weight: bold; color: brown"><b>
                            1
                            </b></font>
                            </td>
                            </tr>
                            <tr>
                            <td scope="row">
                            <font style="font-family: Courier New; font-size: 15px;"><b>Linha:</b></font>
                            </td>
                            <td scope="row">
                            <font style="text-transform:uppercase; font-family: Courier New; font-size: 15px; font-weight: bold; color: brown"><b>
                            RIO DE JANEIRO X LIMA - PERU (1509)
                            </b></font>
                            </td>
                            </tr>
                            <tr>
                            <td scope="row">
                            <font style="font-family: Courier New; font-size: 15px;"><b>Motorista:</b></font>
                            </td>
                            <td scope="row">
                            <font style="text-transform:uppercase; font-family: Courier New; font-size: 15px; font-weight: bold; color: brown"><b>
                            IZAIAS ALVES DE LIMA (14)
                            </b></font>
                            </td>
                            </tr>
                            <tr>
                            <td scope="row">
                            <font style="font-family: Courier New; font-size: 15px;"><b>Motorista:</b></font>
                            </td>
                            <td scope="row">
                            <font style="text-transform:uppercase; font-family: Courier New; font-size: 15px; font-weight: bold; color: brown"><b>
                            JOSE JARDESON PAULA ROGERIO (104)
                            </b></font>
                            </td>
                            </tr>
                            </table>
                            </form>
                            </td>
                            </tr>
                        </table>
                    </div>
                </div>
            </div>
        </div>             
        '''
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    sauxht01 = ' class="fixed-top"'
    sauxht02 = ' style="position: fixed; top: 95px; width: 100%;"'
    sauxht03 = ' style="margin-top: 170px;"'
    spagehtm = '''
    <!DOCTYPE html>
    <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <title>Abeinfo Sistemas</title>
            <link href="/static/bootstrap-5.2.1-dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
            <script src="/static/bootstrap-5.2.1-dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
            <script src="/static/socketio-4.7.5/socket.io.js"></script>
        </head>
        <body>
            <div id="abnfdv01"''' + sauxht01 + '''>
                <nav class="navbar navbar-expand-lg bg-light">
                    <div class="container-fluid container">
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                            <span class="navbar-toggler-icon"></span>
                        </button>
                        <ul class="navbar-nav me-auto mb-2 mb-lg-5">
                        </ul>
                        <ul class="d-flex navbar-nav">
                            <li class="nav-item">Teste Sistema</li>
                        </ul>
                    </div>
                </nav>
            </div>
            <div id="abnfdv02"''' + sauxht02 + '''></div>
            <div id="abnfdv03"''' + sauxht03 + '''>''' + snewpage + '''</div>
            <div id="abnfdv04"></div>
            <div id="abnfdv05"></div>
            <div id="abnfdv06"></div>
            <div id="abnfdv07"></div>
            <div id="abnfdv08"></div>
            <div id="abnfdv09"></div>
            <div id="abnfdv10"></div>
            </div>
        </body>
    </html>'''
    sabntoke = 'teste'
    spagehtm = spagehtm  + abnf_websocket_js_socketio(sabntoke)
    spagehtm = spagehtm  + abnf_websocket_js_abeinfo()
    spagehtm = spagehtm  + abnf_websocket_css_menu_dropdown()
    return Response(spagehtm, mimetype="text/html")
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_teste_001 ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Área de teste do sistema.                                                                                                                           // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

@abnfxapp.route('/t001')
def abnf_teste_001():
    exit()
    lmfields = [['sdescgrs', 'input', 'F', 'descrição do grupo/subgrupo', ['Notnull', 'P'], 'CUSTOS DA OPERACAO - PECAS, ACESSORIOS E INSUMOS - MECANICA'], ['stipogrs', 'input', 'M', 'tipo de registro', ['Notnull', 'D'], 'DESPESAS'], ['smodoreg', 'select', 'M', 'modo do registro', ['Notnull', 'D'], 'R'], ['icodclfo', 'number', 'M', 'código do fornecedor', ['Empty_to_zero'], 0], ['iidclfor', 'input', 'M', 'lista de fornecedores', ['Empty_to_zero', 'Return_integer'], 7739], ['iidcompl', 'input', 'M', 'complemento', ['Empty_to_zero', 'Return_integer'], 0], ['iidcecus', 'select', 'M', 'centro de custo', ['Notnull', 'D', 'Return_integer'], 1], ['iiddepto', 'select', 'M', 'departamento', ['Notnull', 'D', 'Return_integer'], 1], ['iidcontr', 'select', 'M', 'contrato', [], ''], ['iidconta', 'select', 'M', 'conta financeira prevista', [], ''], ['sobserva', 'textarea', 'F', 'observação', [], ''], ['inrdocnf', 'number', 'M', 'documento/nf', ['Notnull', 'D', 'Notzero'], 11223344], ['sserienf', 'input', 'M', 'série', [], 'ABCDE'], ['icodclfo', 'number', 'M', 'código do fornecedor', ['Empty_to_zero'], 0], ['ddatadoc', 'date', 'F', 'data do documento', ['Notnull', 'D', 'Return_date'], date(2024, 5, 1)], ['nvalxtdc', 'thscom', 'M', 'total do documento', ['Notnull', 'D', '>0'], 2345.67], ['itotparc', 'number', 'M', 'total de parcelas', ['Notnull', 'D'], 10], ['inumparc', 'number', 'M', 'número da 1ª parcela', ['Notnull', 'D'], 12]]
    dabnfopg = {'abnfobj0': ['btnovreg', 'btnovreg'], 'sdescgrs': ['sdescgrs', 'text', 'CUSTOS DA OPERACAO - PEDAGIO'], 'stipogrs': ['stipogrs', 'text', 'DESPESAS'], 'smodoreg': ['smodoreg', 'select-one', 'R'], 'icodclfo': ['icodclfo', 'number', ''], 'iidclfor': ['iidclfor', 'select-one', ''], 'ssele001': ['ssele001', 'text', ''], 'iidcompl': ['iidcompl', 'select-one', '13'], 'ssele002': ['ssele002', 'text', ''], 'iidcecus': ['iidcecus', 'select-one', '1'], 'ssele003': ['ssele003', 'text', ''], 'iiddepto': ['iiddepto', 'select-one', '1'], 'ssele004': ['ssele004', 'text', ''], 'iidcontr': ['iidcontr', 'select-one', ''], 'ssele005': ['ssele005', 'text', ''], 'iidconta': ['iidconta', 'select-one', ''], 'ssele006': ['ssele006', 'text', ''], 'sobserva': ['sobserva', 'textarea', ''], 'inrdocnf': ['inrdocnf', 'number', '11223344'], 'sserienf': ['sserienf', 'text', 'ABCDE'], 'ddatadoc': ['ddatadoc', 'date', '2024-05-01'], 'nvalxtdc': ['nvalxtdc', 'text', '2.345,67'], 'itotparc': ['itotparc', 'number', '10'], 'inumparc': ['inumparc', 'number', '12'], 'sauxiite': ['sauxiite', 'text', '010'], 'sauxipar': ['sauxipar', 'text', '021/010'], 'ddataven[0]': ['ddataven[0]', 'date', '2024-06-01'], 'nvalopar[0]': ['nvalopar[0]', 'text', '234,57'], 'ddataven[1]': ['ddataven[1]', 'date', '2024-07-01'], 'nvalopar[1]': ['nvalopar[1]', 'text', '234,57'], 'ddataven[2]': ['ddataven[2]', 'date', '2024-08-01'], 'nvalopar[2]': ['nvalopar[2]', 'text', '234,57'], 'ddataven[3]': ['ddataven[3]', 'date', '2024-09-01'], 'nvalopar[3]': ['nvalopar[3]', 'text', '234,57'], 'ddataven[4]': ['ddataven[4]', 'date', '2024-10-01'], 'nvalopar[4]': ['nvalopar[4]', 'text', '234,57'], 'ddataven[5]': ['ddataven[5]', 'date', '2024-11-01'], 'nvalopar[5]': ['nvalopar[5]', 'text', '234,57'], 'ddataven[6]': ['ddataven[6]', 'date', '2024-12-01'], 'nvalopar[6]': ['nvalopar[6]', 'text', '234,57'], 'ddataven[7]': ['ddataven[7]', 'date', '2025-01-01'], 'nvalopar[7]': ['nvalopar[7]', 'text', '234,57'], 'ddataven[8]': ['ddataven[8]', 'date', '2025-02-01'], 'nvalopar[8]': ['nvalopar[8]', 'text', '234,57'], 'ddataven[9]': ['ddataven[9]', 'date', '2025-03-01'], 'nvalopar[9]': ['nvalopar[9]', 'text', '234,54'], 'abnproje': ['abnproje', 'hidden', '15047354061710003'], 'abntoken': ['abntoken', 'hidden', '866d040a-ded7-4e0f-a9fa-547367e17ffb'], 'sonblurx': ''}

    lauxif01 = ['<font style="font-family: Courier New; font-size: 18px; font-weight: bold; color: black"><b></i>', '</b></font><br>']
    
    spagehtm = '<font style="font-family: Courier New; font-size: 18px; font-weight: bold; color: brown"><b>'
    
    iseconds = 138
    icalcmin = iseconds // 60
    icalcseg = iseconds % 60
    sretminu = str(100 + icalcmin)[1:] + 'm' + str(100 + icalcseg)[1:] + 's'
    
    spagehtm = spagehtm + '<hr>'
    spagehtm = spagehtm + str(iseconds) + '<br>'
    spagehtm = spagehtm + str(icalcmin) + '<br>'
    spagehtm = spagehtm + str(icalcseg) + '<br>'
    spagehtm = spagehtm + str(sretminu) + '<br>'
    spagehtm = spagehtm + '</b></font><hr>'
    
    for lauxi001 in lmfields:
        if lauxi001[0] == 'ddatadoc':
            ddatadoc = lauxi001[5]
        elif lauxi001[0] == 'nvalxtdc':
            nvalxtdc = lauxi001[5]
        elif lauxi001[0] == 'itotparc':
            itotparc = lauxi001[5]
    
    
    lparcela = []
    for icontd01 in range(10000):
        schavd01 = 'ddataven[' + str(icontd01) + ']'
        if dabnfopg.get(schavd01, None) == None:
            break
        else:
            schavd02 = 'nvalopar[' + str(icontd01) + ']'
            lauxi001 = [datetime.strptime(dabnfopg[schavd01][2], "%Y-%m-%d").date(), abnf_converte_string_value_to_float(dabnfopg[schavd02][2]), None]
            lparcela.append(lauxi001)
            
    if True:
        
        isomaqtp = len(lparcela)
        nsomavap = 0
        for lauxi001 in lparcela:
            spagehtm = spagehtm + lauxif01[0] + str(lauxi001) + lauxif01[1]
            nsomavap = round(nsomavap + lauxi001[1], 2)
            
        spagehtm = spagehtm + lauxif01[0] + '=========================' + lauxif01[1]
        
        spagehtm = spagehtm + lauxif01[0] + str(isomaqtp) + lauxif01[1]
        spagehtm = spagehtm + lauxif01[0] + str(nsomavap) + lauxif01[1]
            
        spagehtm = spagehtm + lauxif01[0] + '=========================' + lauxif01[1]
        
        spagehtm = spagehtm + lauxif01[0] + str(ddatadoc) + lauxif01[1]
        spagehtm = spagehtm + lauxif01[0] + str(nvalxtdc) + lauxif01[1]
        spagehtm = spagehtm + lauxif01[0] + str(itotparc) + lauxif01[1]
        
        spagehtm = spagehtm + lauxif01[0] + '=========================' + lauxif01[1]
    
    spagehtm = spagehtm + '<hr>'
    
    if True:
        for lauxi001 in lmfields:
            spagehtm = spagehtm + lauxif01[0] + str(lauxi001) + lauxif01[1]
    
    spagehtm = spagehtm + '<hr>'

    if True:
        for lauxi001 in dabnfopg:
            spagehtm = spagehtm + lauxif01[0] + str(lauxi001) + ' - ' + str(dabnfopg[lauxi001]) + lauxif01[1]

    spagehtm = spagehtm + '<hr>'

    return Response(spagehtm, mimetype="text/html")


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf_teste_002 ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Área de teste do sistema.                                                                                                                           // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

@abnfxapp.route('/t002')
def abnf_teste_002():
    exit()
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    if False:
        snewpage = abnf_create_page([
            ('div-0', 'container', None, None),
            ('hr-0', None),
            ('div-0', 'row', None, None),
            ('div-0', 'col d-flex justify-content-center', None, None),
            ('div-0', 'w-50 p-3', 'background-color: #eee;', None),
            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
            ('legend-0', 'Login do Sistema'),
            ('hr-0', None),
            ('label-0',    'Usuário' , 'form-control-label'),
            ('input-0',    'susuario', 'form-control', 0, 30, '16px', None, 'ssenhdig', True, 0),
            ('label-0',    'Senha'   , 'form-control-label',),
            ('password-0', 'ssenhdig', 'form-control', 6, 30, '16px', None, 'btacesso', True, 0),
            ('hr-0', None),
            ('button-0',   'btacesso', 'btn btn-primary mt-2', 'Fazer Login'),
            # Área de testes (início)
            # ('hr-0', None),
            # ('file-0', 'fteste01', 'btn btn-primary mt-2', '.jpg,.png,.bmp', False),
            # ('hr-0', None),
            # ('select-0', 'llegumes', 'form-control', '16px', 'btacesso', llegumes, 1, None, True),
            # ('hr-0', None),
            # ('radio-0', 'iidcomid', '1', '0', '16px', 'F', 'CENOURA'),
            # ('radio-0', 'iidcomid', '2', '0', '16px', 'F', 'BATATA'),
            # ('radio-0', 'iidcomid', '3', '0', '16px', 'F', 'COUVE'),
            # ('hr-0', None),
            # ('radio-0', 'iidveicu', '1', '2', '16px', 'P', 'ONIX'),
            # ('radio-0', 'iidveicu', '2', '2', '16px', 'P', 'VECTRA'),
            # ('radio-0', 'iidveicu', '3', '2', '16px', 'P', 'CIVIC'),
            # ('hr-0', None),
            # ('checkbox-0', 'iidcen01', 'y' , None, '16px', 'F', 'CENOURA'),
            # ('checkbox-0', 'iidbat01', 'y' , 'y' , '16px', 'F', 'BATATA'),
            # ('checkbox-0', 'iidcou01', 'y' , 'x' , '16px', 'F', 'COUVE'),
            # ('hr-0', None),
            # ('checkbox-0', 'iidcen01', 'y' , None, '16px', 'P', 'CENOURA'),
            # ('checkbox-0', 'iidbat01', 'y' , 'y' , '16px', 'P', None),
            # ('checkbox-0', 'iidcou01', 'y' , 'y' , '16px', 'P', 'COUVE'),
            # Área de testes (fim)
            ('form-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
        ])
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    if True:
        snewpage = '''
        <div class="container">
            <hr>
            <div class="row">
                <div class="col d-flex justify-content-center">
                    <div class="w-100 p-3" style="background-color: #eee;">
                        <table class="table table-bordered table-sm table-responsive">
                            <tr class="table-active">
                                <td scope="row" colspan="2" align="center">
                                    <legend>Operacional - Entrada e Saída de Veículos</legend>
                                </td>
                            </tr>
                            <tr>
                                <td scope="row">
                                    <form method="POST" action="" class="border p-4 mt-2 rounded border-secondary border-3">
                                        <input id="csrf_token" name="csrf_token" type="hidden" value="IjgxNmE3ODc3NGJmNmFiMWE0NGRlNGExYWI0ZDQ1MGQ0Y2E0ODk1NWIi.ZpGAfA.H6QTTo1jWxdlxwfPqHFPv2iJfJ4">
                                            <fieldset>
                                                <div class="form-group row">
                                                    <label class="form-control-label" for="iidoesvl">Local</label>
                                                    <select autocomplete="off" class="form-control" id="iidoesvl" name="iidoesvl" onKeyUp="AbnfTabEnter(event,getElementById(&#39;ddataesv&#39;));" onfocus="this.select()" onkeypress="return AbnfScriptKey(event)" spellcheck="false" style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold;"><option value=""></option><option value="3">CRUZEIRO DO SUL (3)</option><option value="2">LIMA (2)</option><option selected value="1">RIO BRANCO (1)</option><option value="4">SAO PAULO (4)</option></select>
                                                </div>
                                            </fieldset>
                                            <fieldset>
                                                <div class="form-group row">
                                                    <input type="text" name="sfilt001" id="sfilt001" 
                                                    maxlength="100"
                                                    class="form-control"
                                                    autocomplete="off"
                                                    onfocus="this.select()"
                                                    spellcheck="false"
                                                    style="text-transform:uppercase; font-family: Courier New; font-size: 14px; font-weight: bold; color: brown"
                                                    onKeyUp="AbnfTabEnter(event,getElementById(&#39;iidoesvl&#39;));"
                                                    onkeypress="return AbnfScriptKey(event)"
                                                    spellcheck="false">
                                                </div>
                                            </fieldset>
                                            <script>
                                                var srela001 = document.querySelector("#iidoesvl");
                                                var sfilt001 = document.querySelector("#sfilt001");
                                                // Executa o filtro sempre que o valor do campo sfilt001 é alterado
                                                sfilt001.addEventListener("input", function() {
                                                    var stxtbusc = sfilt001.value.toUpperCase();
                                                    var palavras = stxtbusc.split(" ");
                                                    // Filtra as opções do select
                                                    for (var i = 0; i < srela001.options.length; i++) {
                                                        var option = srela001.options[i];
                                                        // Verifica se todas as palavras estão contidas na opção
                                                        var boptvali = true;
                                                        for (var j = 0; j < palavras.length; j++) {
                                                            if (!option.textContent.toUpperCase().includes(palavras[j])) {
                                                                boptvali = false;
                                                                break;
                                                            }
                                                        }
                                                        if (boptvali) {
                                                            option.hidden = false;
                                                        } else {
                                                            option.hidden = true;
                                                        }
                                                    }
                                                });
                                            </script>
                                            
                                            <input type="text" name="nsaldoin" id="nsaldoin" size=12 maxlength="12" value=""
                                            style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold; text-align:right;"
                                            onkeyup="AbnfNumMaskDecimal(this,3);"
                                            onfocus="this.select()" autocomplete="off" spellcheck="false">
                                            <fieldset>
                                            <div class="form-group row">
                                            <label class="form-control-label" for="ddataesv">Data</label>
                                            <input autocomplete="off" class="form-control" id="ddataesv" maxlength="10" name="ddataesv" onKeyUp="AbnfTabEnter(event,getElementById(&#39;thoraesv&#39;));" onfocus="this.select()" onkeypress="return AbnfScriptKey(event)" spellcheck="false" style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold;" type="date" value="2024-07-12">
                                            </div>
                                            </fieldset>
                                            <fieldset>
                                            <div class="form-group row">
                                            <label class="form-control-label" for="thoraesv">Hora</label>
                                            <input autocomplete="off" class="form-control" id="thoraesv" maxlength="100" name="thoraesv" onKeyUp="AbnfTabEnter(event,getElementById(&#39;stipomov&#39;));" onfocus="this.select()" onkeypress="return AbnfScriptKey(event)" spellcheck="false" style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold;" type="time" value="">
                                            </div>
                                            </fieldset>
                                            <fieldset>
                                            <div class="form-group row">
                                            <label class="form-control-label" for="stipomov">Tipo de movimentação</label>
                                            <select autocomplete="off" class="form-control" id="stipomov" name="stipomov" onKeyUp="AbnfTabEnter(event,getElementById(&#39;iodomvei&#39;));" onfocus="this.select()" onkeypress="return AbnfScriptKey(event)" spellcheck="false" style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold;"><option value=""></option><option value="E">ENTRADA</option><option value="S">SAIDA</option><option value="P">PONTO DE PASSAGEM</option></select>
                                            </div>
                                            </fieldset>
                                            <fieldset>
                                            <div class="form-group row">
                                            <label class="form-control-label" for="iodomvei">Odômetro</label>
                                            <input autocomplete="off" class="form-control" id="iodomvei" max="99999999" maxlength="6" min="1" name="iodomvei" onKeyUp="AbnfMaxLength(this,8);AbnfTabEnter(event,getElementById(&#39;irolevei&#39;));" onfocus="this.select()" onkeypress="return AbnfScriptIntegerOnly(event)" spellcheck="false" style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold;" type="number" value="491325">
                                            </div>
                                            </fieldset>
                                            <fieldset>
                                            <div class="form-group row">
                                            <label class="form-control-label" for="irolevei">Roleta</label>
                                            <input autocomplete="off" class="form-control" id="irolevei" max="99999999" maxlength="6" min="1" name="irolevei" onKeyUp="AbnfMaxLength(this,8);AbnfTabEnter(event,getElementById(&#39;iidolinh&#39;));" onfocus="this.select()" onkeypress="return AbnfScriptIntegerOnly(event)" spellcheck="false" style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold;" type="number" value="1">
                                            </div>
                                            </fieldset>
                                            <fieldset>
                                            <div class="form-group row">
                                            <label class="form-control-label" for="iidolinh">Linha</label>
                                            <select autocomplete="off" class="form-control" id="iidolinh" name="iidolinh" onKeyUp="AbnfTabEnter(event,getElementById(&#39;iidmot01&#39;));" onfocus="this.select()" onkeypress="return AbnfScriptKey(event)" spellcheck="false" style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold;"><option value=""></option><option value="4">1000 - RIO BRANCO X CRUZEIRO DO SUL (07H00)</option><option value="5">1001 - RIO BRANCO X CRUZEIRO DO SUL 19H00</option><option value="13">1002 - CRUZEIRO DO SUL X RIO BRANCO (07H00)</option><option value="14">1003 - CRUZEIRO DO SUL X RIO BRANCO (19H00)</option><option value="3">1010 - RIO BRANCO X TARAUACA</option><option value="12">1011 - TARAUACA X RIO BRANCO</option><option value="1">1013 - RIO BRANCO X ASSIS BRASIL</option><option value="2">1013-1 - RIO BRANCO X BRASILEIA</option><option value="10">1017 - ASSIS BRASIL X RIO BRANCO</option><option value="11">1017-1 - BRASILEIA X RIO BRANCO</option><option value="7">1022 - RIO BRANCO X BOCA DO ACRE - AM (06H00)</option><option value="8">1100 - RIO BRANCO X BOCA DO ACRE - AM (13H00)</option><option value="17">1101 - BOCA DO ACRE - AM X RIO BRANCO (13H00)</option><option value="16">1102 - BOCA DO ACRE - AM X RIO BRANCO (07H00)</option><option value="9">1199 - RIO BRANCO X PUERTO MALDONADO</option><option value="18">1199-1 - PUERTO MALDONADO - PERU X RIO BRANCO</option><option value="24">1509 - RIO DE JANEIRO X LIMA - PERU</option><option value="25">1511 - LIMA - PERU X RIO DE JANEIRO</option><option value="6">8000 - RIO BRANCO X CRUZEIRO DO SUL (EXTRA 19HRS)</option><option value="15">8001 - CRUZEIRO DO SUL X RIO BRANCO (EXTRA 19H00)</option><option value="27">8002 - RIO BRANCO X CRUZEIRO DO SUL (EXTRA 19H00)</option><option value="32">8008 - RIO BRANCO X CRUZEIRO DO SUL (EXTRA 07HRS)</option><option value="26">F01 - FRETAMENTO RODOVIARIO</option><option value="19">I01 - RIO BRANCO X SENADOR GUIOMARD (SEMIURBANO)</option><option value="21">I01 - INTERMUNICIPAL RIO BRANCO X SENADOR GUIOMARD</option><option value="20">I02 - RIO BRANCO X BUJARI (SEMIURBANO)</option><option value="22">I02 - INTERMUNICIPAL RIO BRANCO X BUJARI</option><option value="28">R01 - RIO BRANCO X PORTO ALONSO</option><option value="29">R011 - PORTO ALONSO X RIO BRANCO</option><option value="30">R02 - RIO BRANCO X CAQUETA</option><option value="31">R022 - CAQUETA X RIO BRANCO</option><option value="23">SOS - SOCORRO</option></select>
                                            </div>
                                            </fieldset>
                                            <fieldset>
                                            <div class="form-group row">
                                            <input type="text" name="sfilt002" id="sfilt002"
                                            maxlength="100"
                                            class="form-control"
                                            autocomplete="off"
                                            onfocus="this.select()"
                                            spellcheck="false"
                                            style="text-transform:uppercase; font-family: Courier New; font-size: 14px; font-weight: bold; color: brown"
                                            onKeyUp="AbnfTabEnter(event,getElementById(&#39;iidolinh&#39;));"
                                            onkeypress="return AbnfScriptKey(event)"
                                            spellcheck="false">
                                            </div>
                                            </fieldset>
                                            <script>
                                            var srela002 = document.querySelector("#iidolinh");
                                            var sfilt002 = document.querySelector("#sfilt002");
                                            // Executa o filtro sempre que o valor do campo sfilt002 é alterado
                                            sfilt002.addEventListener("input", function() {
                                            var stxtbusc = sfilt002.value.toUpperCase();
                                            var palavras = stxtbusc.split(" ");
                                            // Filtra as opções do select
                                            for (var i = 0; i < srela002.options.length; i++) {
                                            var option = srela002.options[i];
                                            // Verifica se todas as palavras estão contidas na opção
                                            var boptvali = true;
                                            for (var j = 0; j < palavras.length; j++) {
                                            if (!option.textContent.toUpperCase().includes(palavras[j])) {
                                            boptvali = false;
                                            break;
                                            }
                                            }
                                            if (boptvali) {
                                            option.hidden = false;
                                            } else {
                                            option.hidden = true;
                                            }
                                            }
                                            });
                                            </script>
                                            <fieldset>
                                            <div class="form-group row">
                                            <label class="form-control-label" for="iidmot01">Motorista 01</label>
                                            <select autocomplete="off" class="form-control" id="iidmot01" name="iidmot01" onKeyUp="AbnfTabEnter(event,getElementById(&#39;iidmot02&#39;));" onfocus="this.select()" onkeypress="return AbnfScriptKey(event)" spellcheck="false" style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold;"><option value=""></option><option value="2">ADEMILTON MARTINS DE MENEZE (7)</option><option value="3">ALAN RODRIGUES SALDANHA (19)</option><option value="4">AMARAL LIMA DINIZ (38)</option><option value="5">ANGELICA DA SILVA BRANDAO (119)</option><option value="6">ANTONIEL SANTOS DE SOUZA (8)</option><option value="7">ANTONIO ALDENIR FERREIRA (6)</option><option value="8">ANTONIO JOSE DE SOUZA BARBO (121)</option><option value="11">AURILENE DE ALMEIDA LIMA (28)</option><option value="12">CARLITO DOS SANTOS (5)</option><option value="120">CARLOS ALBERTO TEIXEIRA SANTIAGO (8017)</option><option value="121">CARLOS ANDRE CAVALCANTE VIANA (8018)</option><option value="109">CARLOS CESAR RIBEIRO (131)</option><option value="13">CLAUDIO RIBEIRO DA SILVA (50)</option><option value="14">CLENILSON SILVA DO AMARAL (80)</option><option value="15">CLEONE LOPES DA SILVA (73)</option><option value="16">CLEUSON ALVES LEITE (40)</option><option value="17">CLOVIS ROQUE BANDEIRA (105)</option><option value="18">DANIEL DO NASCIMENTO ABREU (72)</option><option value="19">DANIELA ALMEIDA DE OLIVEIRA (64)</option><option value="20">DAVID DE ALMEIDA DA ROCHA (76)</option><option value="21">DJONATHAN COSTA DOS REIS (47)</option><option value="104">EDINALDO DA SILVA LOPES (8011)</option><option value="111">EDNALDO DE OLIVEIRA MORAES (8008)</option><option value="22">EDNILSON RIBEIRO DA SILVA (17)</option><option value="23">ELIESER GONCALVES PEIXOTO (112)</option><option value="24">ELITA PAULINO DE BARROS (44)</option><option value="25">EMERSON OLIVEIRA DA SILVA A (74)</option><option value="26">FABIANA DE OLIVEIRA RODRIGU (24)</option><option value="27">FALIK RANGEL MALTA DE MENEZ (12)</option><option value="28">FERNANDO QUEIROZ CANUTO DE (128)</option><option value="29">FRANC LANDY ALMEIDA DOS SAN (124)</option><option value="30">FRANCISCO ALCENIR DA SILVA (97)</option><option value="31">FRANCISCO OSIEL HOLANDA LOP (90)</option><option value="32">FRANCISCO PEREIRA DE QUEIRO (11)</option><option value="33">FRANCISCO UIDULO MOURA DE B (43)</option><option value="34">FRANCISCO XAVIER DA SILVA (45)</option><option value="35">FRANCIVALDO BARBOSA DE LIMA (79)</option><option value="36">GEOVANE ARAUJO DA SILVA (42)</option><option value="37">GIOVANE SIQUEIRA FERREIRA (84)</option><option value="38">HELIO DA SILVA LINS JUNIOR (63)</option><option value="110">HORLANDO RAFAEL DE OLIVEIRA RIBEIRO (130)</option><option value="41">ISMAEL DO VALE SILVA (107)</option><option value="108">IZACK DA SILVA (8004)</option><option value="42">IZAIAS ALVES DE LIMA (14)</option><option value="44">JAILSON CORDEIRO MACHADO SI (13)</option><option value="45">JEAN DE ARAUJO SILVA (69)</option><option value="117">JEREMIAS DA SILVA (8014)</option><option value="118">JERSIEL PINHEIRO MAGALHAES (8015)</option><option value="46">JESSE SILVA PESSOA (20)</option><option value="47">JOABE DA SILVA GARCIA (110)</option><option value="48">JOABE MENESES CRUZ (100)</option><option value="49">JOAO DA SILVA GOMES (106)</option><option value="50">JOAO PAULO MANUARIO (15)</option><option value="51">JOAO PAULO VASCONCELOS OLIV (103)</option><option value="122">JOAO SERAFIM MENESES (8019)</option><option value="52">JONATHAN SOUSA DA SILVA (37)</option><option value="53">JORGE CORREIA DE PAIVA JUNI (91)</option><option value="54">JOSE ALTEMIR DE QUEIROZ CAS (30)</option><option value="106">JOSE CARLOS DO ROSARIO (8005)</option><option value="116">JOSE CARLOS FELIX DE OLIVEIRA (8013)</option><option value="55">JOSE DA COSTA MACEDO (99)</option><option value="57">JOSE ELISSON OLIVEIRA SOUZA (21)</option><option value="58">JOSE JARDESON PAULA ROGERIO (104)</option><option value="107">JOSE LUIZ DA ROCHA RODRIGUES LIMA (8003)</option><option value="59">JOSE MARIA NASCIMENTO DOS S (53)</option><option value="60">JOSE MARIA SOLON DA PAZ (39)</option><option value="115">JOSUE RIBEIRO DA SILVA (8012)</option><option value="61">KENNEDY SILVA DE SOUZA (113)</option><option value="62">LEONARDO RODRIGUES DA COSTA (78)</option><option value="65">LUIZ RIBEIRO SILVA (33)</option><option value="66">MAICO DIONE BRAGA DE PAIVA (27)</option><option value="114">MANOEL ANGELO NOGUEIRA DA SILVA (8002)</option><option value="112">MARCIEL SOUZA DA SILVA (8009)</option><option value="68">MARIA MADALENA BRITO MATEUS (25)</option><option value="69">MARIA MAIRA DE SOUSA DA SIL (118)</option><option value="70">MAURICELIO FREIRE DA SILVA (68)</option><option value="71">MAURO ESCLEIDE DOS SANTOS A (41)</option><option value="72">MELQUISEDEQUE ARAUJO DE LIM (31)</option><option value="113">NATANAEL SOARES DA SILVA (8007)</option><option value="76">ORCLEILTON DE SOUZA MONTEIR (108)</option><option value="77">OSVALDO FERREIRA DA SILVA (89)</option><option value="78">PEDRO SALDANHA DA SILVA (51)</option><option value="105">RAIMUNDO ANTONIO DE MELO CUNHO (8001)</option><option value="81">RAIMUNDO NONATO FONTENELLE (125)</option><option value="82">RAIMUNDO NONATO SILVA DA (109)</option><option value="83">RAYELI FALCAO DE LIMA (4)</option><option value="84">REGINALDO DA COSTA FALCAO (81)</option><option value="85">RIAN LUCAS DE OLIVEIRA PINH (101)</option><option value="86">RICARDO RAMALHO DO NASCIMEN (115)</option><option value="87">ROBERTO MARINHO DE SOUZA (111)</option><option value="89">RONALDO GONCALVES PINTO (86)</option><option value="90">RONALDO RIBEIRO DOS SANTOS (116)</option><option value="91">ROSINEIDE CHAVES DA SILVA (3)</option><option value="92">SAMUEL PITER SANTOS DE SOUZ (127)</option><option value="93">SANDRO NASCIMENTO LEONE (67)</option><option value="94">SARA JANE BARBOSA DE QUEIRO (10)</option><option value="95">TALISSON DE OLIVEIRA FREITA (9)</option><option value="96">TAMIRES ALVES DA SILVA (56)</option><option value="98">TATIANA BARBOSA DE QUEIROZ (117)</option><option value="99">VALDOMIRO RIBEIRO OLIVEIRA (34)</option><option value="100">VANESSA MENDONCA UCHOA (35)</option><option value="101">WHENESON DIAS GOMES (122)</option><option value="102">WILLIAN MOTA DE SOUZA (62)</option><option value="119">WILMERSON SILVA DO AMARAL (8016)</option></select>
                                            </div>
                                            </fieldset>
                                            <fieldset>
                                            <div class="form-group row">
                                            <input type="text" name="sfilt003" id="sfilt003"
                                            maxlength="100"
                                            class="form-control"
                                            autocomplete="off"
                                            onfocus="this.select()"
                                            spellcheck="false"
                                            style="text-transform:uppercase; font-family: Courier New; font-size: 14px; font-weight: bold; color: brown"
                                            onKeyUp="AbnfTabEnter(event,getElementById(&#39;iidmot01&#39;));"
                                            onkeypress="return AbnfScriptKey(event)"
                                            spellcheck="false">
                                            </div>
                                            </fieldset>
                                            <script>
                                            var srela003 = document.querySelector("#iidmot01");
                                            var sfilt003 = document.querySelector("#sfilt003");
                                            // Executa o filtro sempre que o valor do campo sfilt003 é alterado
                                            sfilt003.addEventListener("input", function() {
                                            var stxtbusc = sfilt003.value.toUpperCase();
                                            var palavras = stxtbusc.split(" ");
                                            // Filtra as opções do select
                                            for (var i = 0; i < srela003.options.length; i++) {
                                            var option = srela003.options[i];
                                            // Verifica se todas as palavras estão contidas na opção
                                            var boptvali = true;
                                            for (var j = 0; j < palavras.length; j++) {
                                            if (!option.textContent.toUpperCase().includes(palavras[j])) {
                                            boptvali = false;
                                            break;
                                            }
                                            }
                                            if (boptvali) {
                                            option.hidden = false;
                                            } else {
                                            option.hidden = true;
                                            }
                                            }
                                            });
                                            </script>
                                            <fieldset>
                                            <div class="form-group row">
                                            <label class="form-control-label" for="iidmot02">Motorista 02</label>
                                            <select autocomplete="off" class="form-control" id="iidmot02" name="iidmot02" onKeyUp="AbnfTabEnter(event,getElementById(&#39;iidcob01&#39;));" onfocus="this.select()" onkeypress="return AbnfScriptKey(event)" spellcheck="false" style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold;"><option value=""></option><option value="2">ADEMILTON MARTINS DE MENEZE (7)</option><option value="3">ALAN RODRIGUES SALDANHA (19)</option><option value="4">AMARAL LIMA DINIZ (38)</option><option value="5">ANGELICA DA SILVA BRANDAO (119)</option><option value="6">ANTONIEL SANTOS DE SOUZA (8)</option><option value="7">ANTONIO ALDENIR FERREIRA (6)</option><option value="8">ANTONIO JOSE DE SOUZA BARBO (121)</option><option value="11">AURILENE DE ALMEIDA LIMA (28)</option><option value="12">CARLITO DOS SANTOS (5)</option><option value="120">CARLOS ALBERTO TEIXEIRA SANTIAGO (8017)</option><option value="121">CARLOS ANDRE CAVALCANTE VIANA (8018)</option><option value="109">CARLOS CESAR RIBEIRO (131)</option><option value="13">CLAUDIO RIBEIRO DA SILVA (50)</option><option value="14">CLENILSON SILVA DO AMARAL (80)</option><option value="15">CLEONE LOPES DA SILVA (73)</option><option value="16">CLEUSON ALVES LEITE (40)</option><option value="17">CLOVIS ROQUE BANDEIRA (105)</option><option value="18">DANIEL DO NASCIMENTO ABREU (72)</option><option value="19">DANIELA ALMEIDA DE OLIVEIRA (64)</option><option value="20">DAVID DE ALMEIDA DA ROCHA (76)</option><option value="21">DJONATHAN COSTA DOS REIS (47)</option><option value="104">EDINALDO DA SILVA LOPES (8011)</option><option value="111">EDNALDO DE OLIVEIRA MORAES (8008)</option><option value="22">EDNILSON RIBEIRO DA SILVA (17)</option><option value="23">ELIESER GONCALVES PEIXOTO (112)</option><option value="24">ELITA PAULINO DE BARROS (44)</option><option value="25">EMERSON OLIVEIRA DA SILVA A (74)</option><option value="26">FABIANA DE OLIVEIRA RODRIGU (24)</option><option value="27">FALIK RANGEL MALTA DE MENEZ (12)</option><option value="28">FERNANDO QUEIROZ CANUTO DE (128)</option><option value="29">FRANC LANDY ALMEIDA DOS SAN (124)</option><option value="30">FRANCISCO ALCENIR DA SILVA (97)</option><option value="31">FRANCISCO OSIEL HOLANDA LOP (90)</option><option value="32">FRANCISCO PEREIRA DE QUEIRO (11)</option><option value="33">FRANCISCO UIDULO MOURA DE B (43)</option><option value="34">FRANCISCO XAVIER DA SILVA (45)</option><option value="35">FRANCIVALDO BARBOSA DE LIMA (79)</option><option value="36">GEOVANE ARAUJO DA SILVA (42)</option><option value="37">GIOVANE SIQUEIRA FERREIRA (84)</option><option value="38">HELIO DA SILVA LINS JUNIOR (63)</option><option value="110">HORLANDO RAFAEL DE OLIVEIRA RIBEIRO (130)</option><option value="41">ISMAEL DO VALE SILVA (107)</option><option value="108">IZACK DA SILVA (8004)</option><option value="42">IZAIAS ALVES DE LIMA (14)</option><option value="44">JAILSON CORDEIRO MACHADO SI (13)</option><option value="45">JEAN DE ARAUJO SILVA (69)</option><option value="117">JEREMIAS DA SILVA (8014)</option><option value="118">JERSIEL PINHEIRO MAGALHAES (8015)</option><option value="46">JESSE SILVA PESSOA (20)</option><option value="47">JOABE DA SILVA GARCIA (110)</option><option value="48">JOABE MENESES CRUZ (100)</option><option value="49">JOAO DA SILVA GOMES (106)</option><option value="50">JOAO PAULO MANUARIO (15)</option><option value="51">JOAO PAULO VASCONCELOS OLIV (103)</option><option value="122">JOAO SERAFIM MENESES (8019)</option><option value="52">JONATHAN SOUSA DA SILVA (37)</option><option value="53">JORGE CORREIA DE PAIVA JUNI (91)</option><option value="54">JOSE ALTEMIR DE QUEIROZ CAS (30)</option><option value="106">JOSE CARLOS DO ROSARIO (8005)</option><option value="116">JOSE CARLOS FELIX DE OLIVEIRA (8013)</option><option value="55">JOSE DA COSTA MACEDO (99)</option><option value="57">JOSE ELISSON OLIVEIRA SOUZA (21)</option><option value="58">JOSE JARDESON PAULA ROGERIO (104)</option><option value="107">JOSE LUIZ DA ROCHA RODRIGUES LIMA (8003)</option><option value="59">JOSE MARIA NASCIMENTO DOS S (53)</option><option value="60">JOSE MARIA SOLON DA PAZ (39)</option><option value="115">JOSUE RIBEIRO DA SILVA (8012)</option><option value="61">KENNEDY SILVA DE SOUZA (113)</option><option value="62">LEONARDO RODRIGUES DA COSTA (78)</option><option value="65">LUIZ RIBEIRO SILVA (33)</option><option value="66">MAICO DIONE BRAGA DE PAIVA (27)</option><option value="114">MANOEL ANGELO NOGUEIRA DA SILVA (8002)</option><option value="112">MARCIEL SOUZA DA SILVA (8009)</option><option value="68">MARIA MADALENA BRITO MATEUS (25)</option><option value="69">MARIA MAIRA DE SOUSA DA SIL (118)</option><option value="70">MAURICELIO FREIRE DA SILVA (68)</option><option value="71">MAURO ESCLEIDE DOS SANTOS A (41)</option><option value="72">MELQUISEDEQUE ARAUJO DE LIM (31)</option><option value="113">NATANAEL SOARES DA SILVA (8007)</option><option value="76">ORCLEILTON DE SOUZA MONTEIR (108)</option><option value="77">OSVALDO FERREIRA DA SILVA (89)</option><option value="78">PEDRO SALDANHA DA SILVA (51)</option><option value="105">RAIMUNDO ANTONIO DE MELO CUNHO (8001)</option><option value="81">RAIMUNDO NONATO FONTENELLE (125)</option><option value="82">RAIMUNDO NONATO SILVA DA (109)</option><option value="83">RAYELI FALCAO DE LIMA (4)</option><option value="84">REGINALDO DA COSTA FALCAO (81)</option><option value="85">RIAN LUCAS DE OLIVEIRA PINH (101)</option><option value="86">RICARDO RAMALHO DO NASCIMEN (115)</option><option value="87">ROBERTO MARINHO DE SOUZA (111)</option><option value="89">RONALDO GONCALVES PINTO (86)</option><option value="90">RONALDO RIBEIRO DOS SANTOS (116)</option><option value="91">ROSINEIDE CHAVES DA SILVA (3)</option><option value="92">SAMUEL PITER SANTOS DE SOUZ (127)</option><option value="93">SANDRO NASCIMENTO LEONE (67)</option><option value="94">SARA JANE BARBOSA DE QUEIRO (10)</option><option value="95">TALISSON DE OLIVEIRA FREITA (9)</option><option value="96">TAMIRES ALVES DA SILVA (56)</option><option value="98">TATIANA BARBOSA DE QUEIROZ (117)</option><option value="99">VALDOMIRO RIBEIRO OLIVEIRA (34)</option><option value="100">VANESSA MENDONCA UCHOA (35)</option><option value="101">WHENESON DIAS GOMES (122)</option><option value="102">WILLIAN MOTA DE SOUZA (62)</option><option value="119">WILMERSON SILVA DO AMARAL (8016)</option></select>
                                            </div>
                                            </fieldset>
                                            <fieldset>
                                            <div class="form-group row">
                                            <input type="text" name="sfilt004" id="sfilt004"
                                            maxlength="100"
                                            class="form-control"
                                            autocomplete="off"
                                            onfocus="this.select()"
                                            spellcheck="false"
                                            style="text-transform:uppercase; font-family: Courier New; font-size: 14px; font-weight: bold; color: brown"
                                            onKeyUp="AbnfTabEnter(event,getElementById(&#39;iidmot02&#39;));"
                                            onkeypress="return AbnfScriptKey(event)"
                                            spellcheck="false">
                                            </div>
                                            </fieldset>
                                            <script>
                                            var srela004 = document.querySelector("#iidmot02");
                                            var sfilt004 = document.querySelector("#sfilt004");
                                            // Executa o filtro sempre que o valor do campo sfilt004 é alterado
                                            sfilt004.addEventListener("input", function() {
                                            var stxtbusc = sfilt004.value.toUpperCase();
                                            var palavras = stxtbusc.split(" ");
                                            // Filtra as opções do select
                                            for (var i = 0; i < srela004.options.length; i++) {
                                            var option = srela004.options[i];
                                            // Verifica se todas as palavras estão contidas na opção
                                            var boptvali = true;
                                            for (var j = 0; j < palavras.length; j++) {
                                            if (!option.textContent.toUpperCase().includes(palavras[j])) {
                                            boptvali = false;
                                            break;
                                            }
                                            }
                                            if (boptvali) {
                                            option.hidden = false;
                                            } else {
                                            option.hidden = true;
                                            }
                                            }
                                            });
                                            </script>
                                            <fieldset>
                                            <div class="form-group row">
                                            <label class="form-control-label" for="iidcob01">Cobrador 01</label>
                                            <select autocomplete="off" class="form-control" id="iidcob01" name="iidcob01" onKeyUp="AbnfTabEnter(event,getElementById(&#39;sobserva&#39;));" onfocus="this.select()" onkeypress="return AbnfScriptKey(event)" spellcheck="false" style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold;"><option value=""></option><option value="2">ADEMILTON MARTINS DE MENEZE (7)</option><option value="3">ALAN RODRIGUES SALDANHA (19)</option><option value="4">AMARAL LIMA DINIZ (38)</option><option value="5">ANGELICA DA SILVA BRANDAO (119)</option><option value="6">ANTONIEL SANTOS DE SOUZA (8)</option><option value="7">ANTONIO ALDENIR FERREIRA (6)</option><option value="8">ANTONIO JOSE DE SOUZA BARBO (121)</option><option value="11">AURILENE DE ALMEIDA LIMA (28)</option><option value="12">CARLITO DOS SANTOS (5)</option><option value="120">CARLOS ALBERTO TEIXEIRA SANTIAGO (8017)</option><option value="121">CARLOS ANDRE CAVALCANTE VIANA (8018)</option><option value="109">CARLOS CESAR RIBEIRO (131)</option><option value="13">CLAUDIO RIBEIRO DA SILVA (50)</option><option value="14">CLENILSON SILVA DO AMARAL (80)</option><option value="15">CLEONE LOPES DA SILVA (73)</option><option value="16">CLEUSON ALVES LEITE (40)</option><option value="17">CLOVIS ROQUE BANDEIRA (105)</option><option value="18">DANIEL DO NASCIMENTO ABREU (72)</option><option value="19">DANIELA ALMEIDA DE OLIVEIRA (64)</option><option value="20">DAVID DE ALMEIDA DA ROCHA (76)</option><option value="21">DJONATHAN COSTA DOS REIS (47)</option><option value="104">EDINALDO DA SILVA LOPES (8011)</option><option value="111">EDNALDO DE OLIVEIRA MORAES (8008)</option><option value="22">EDNILSON RIBEIRO DA SILVA (17)</option><option value="23">ELIESER GONCALVES PEIXOTO (112)</option><option value="24">ELITA PAULINO DE BARROS (44)</option><option value="25">EMERSON OLIVEIRA DA SILVA A (74)</option><option value="26">FABIANA DE OLIVEIRA RODRIGU (24)</option><option value="27">FALIK RANGEL MALTA DE MENEZ (12)</option><option value="28">FERNANDO QUEIROZ CANUTO DE (128)</option><option value="29">FRANC LANDY ALMEIDA DOS SAN (124)</option><option value="30">FRANCISCO ALCENIR DA SILVA (97)</option><option value="31">FRANCISCO OSIEL HOLANDA LOP (90)</option><option value="32">FRANCISCO PEREIRA DE QUEIRO (11)</option><option value="33">FRANCISCO UIDULO MOURA DE B (43)</option><option value="34">FRANCISCO XAVIER DA SILVA (45)</option><option value="35">FRANCIVALDO BARBOSA DE LIMA (79)</option><option value="36">GEOVANE ARAUJO DA SILVA (42)</option><option value="37">GIOVANE SIQUEIRA FERREIRA (84)</option><option value="38">HELIO DA SILVA LINS JUNIOR (63)</option><option value="110">HORLANDO RAFAEL DE OLIVEIRA RIBEIRO (130)</option><option value="41">ISMAEL DO VALE SILVA (107)</option><option value="108">IZACK DA SILVA (8004)</option><option value="42">IZAIAS ALVES DE LIMA (14)</option><option value="44">JAILSON CORDEIRO MACHADO SI (13)</option><option value="45">JEAN DE ARAUJO SILVA (69)</option><option value="117">JEREMIAS DA SILVA (8014)</option><option value="118">JERSIEL PINHEIRO MAGALHAES (8015)</option><option value="46">JESSE SILVA PESSOA (20)</option><option value="47">JOABE DA SILVA GARCIA (110)</option><option value="48">JOABE MENESES CRUZ (100)</option><option value="49">JOAO DA SILVA GOMES (106)</option><option value="50">JOAO PAULO MANUARIO (15)</option><option value="51">JOAO PAULO VASCONCELOS OLIV (103)</option><option value="122">JOAO SERAFIM MENESES (8019)</option><option value="52">JONATHAN SOUSA DA SILVA (37)</option><option value="53">JORGE CORREIA DE PAIVA JUNI (91)</option><option value="54">JOSE ALTEMIR DE QUEIROZ CAS (30)</option><option value="106">JOSE CARLOS DO ROSARIO (8005)</option><option value="116">JOSE CARLOS FELIX DE OLIVEIRA (8013)</option><option value="55">JOSE DA COSTA MACEDO (99)</option><option value="57">JOSE ELISSON OLIVEIRA SOUZA (21)</option><option value="58">JOSE JARDESON PAULA ROGERIO (104)</option><option value="107">JOSE LUIZ DA ROCHA RODRIGUES LIMA (8003)</option><option value="59">JOSE MARIA NASCIMENTO DOS S (53)</option><option value="60">JOSE MARIA SOLON DA PAZ (39)</option><option value="115">JOSUE RIBEIRO DA SILVA (8012)</option><option value="61">KENNEDY SILVA DE SOUZA (113)</option><option value="62">LEONARDO RODRIGUES DA COSTA (78)</option><option value="65">LUIZ RIBEIRO SILVA (33)</option><option value="66">MAICO DIONE BRAGA DE PAIVA (27)</option><option value="114">MANOEL ANGELO NOGUEIRA DA SILVA (8002)</option><option value="112">MARCIEL SOUZA DA SILVA (8009)</option><option value="68">MARIA MADALENA BRITO MATEUS (25)</option><option value="69">MARIA MAIRA DE SOUSA DA SIL (118)</option><option value="70">MAURICELIO FREIRE DA SILVA (68)</option><option value="71">MAURO ESCLEIDE DOS SANTOS A (41)</option><option value="72">MELQUISEDEQUE ARAUJO DE LIM (31)</option><option value="113">NATANAEL SOARES DA SILVA (8007)</option><option value="76">ORCLEILTON DE SOUZA MONTEIR (108)</option><option value="77">OSVALDO FERREIRA DA SILVA (89)</option><option value="78">PEDRO SALDANHA DA SILVA (51)</option><option value="105">RAIMUNDO ANTONIO DE MELO CUNHO (8001)</option><option value="81">RAIMUNDO NONATO FONTENELLE (125)</option><option value="82">RAIMUNDO NONATO SILVA DA (109)</option><option value="83">RAYELI FALCAO DE LIMA (4)</option><option value="84">REGINALDO DA COSTA FALCAO (81)</option><option value="85">RIAN LUCAS DE OLIVEIRA PINH (101)</option><option value="86">RICARDO RAMALHO DO NASCIMEN (115)</option><option value="87">ROBERTO MARINHO DE SOUZA (111)</option><option value="89">RONALDO GONCALVES PINTO (86)</option><option value="90">RONALDO RIBEIRO DOS SANTOS (116)</option><option value="91">ROSINEIDE CHAVES DA SILVA (3)</option><option value="92">SAMUEL PITER SANTOS DE SOUZ (127)</option><option value="93">SANDRO NASCIMENTO LEONE (67)</option><option value="94">SARA JANE BARBOSA DE QUEIRO (10)</option><option value="95">TALISSON DE OLIVEIRA FREITA (9)</option><option value="96">TAMIRES ALVES DA SILVA (56)</option><option value="98">TATIANA BARBOSA DE QUEIROZ (117)</option><option value="99">VALDOMIRO RIBEIRO OLIVEIRA (34)</option><option value="100">VANESSA MENDONCA UCHOA (35)</option><option value="101">WHENESON DIAS GOMES (122)</option><option value="102">WILLIAN MOTA DE SOUZA (62)</option><option value="119">WILMERSON SILVA DO AMARAL (8016)</option></select>
                                            </div>
                                            </fieldset>
                                            <fieldset>
                                            <div class="form-group row">
                                            <input type="text" name="sfilt006" id="sfilt006"
                                            maxlength="100"
                                            class="form-control"
                                            autocomplete="off"
                                            onfocus="this.select()"
                                            spellcheck="false"
                                            style="text-transform:uppercase; font-family: Courier New; font-size: 14px; font-weight: bold; color: brown"
                                            onKeyUp="AbnfTabEnter(event,getElementById(&#39;iidcob01&#39;));"
                                            onkeypress="return AbnfScriptKey(event)"
                                            spellcheck="false">
                                            </div>
                                            </fieldset>
                                            <script>
                                            var srela006 = document.querySelector("#iidcob01");
                                            var sfilt006 = document.querySelector("#sfilt006");
                                            // Executa o filtro sempre que o valor do campo sfilt006 é alterado
                                            sfilt006.addEventListener("input", function() {
                                            var stxtbusc = sfilt006.value.toUpperCase();
                                            var palavras = stxtbusc.split(" ");
                                            // Filtra as opções do select
                                            for (var i = 0; i < srela006.options.length; i++) {
                                            var option = srela006.options[i];
                                            // Verifica se todas as palavras estão contidas na opção
                                            var boptvali = true;
                                            for (var j = 0; j < palavras.length; j++) {
                                            if (!option.textContent.toUpperCase().includes(palavras[j])) {
                                            boptvali = false;
                                            break;
                                            }
                                            }
                                            if (boptvali) {
                                            option.hidden = false;
                                            } else {
                                            option.hidden = true;
                                            }
                                            }
                                            });
                                            </script>
                                            <hr>
                            <fieldset>
                            <div class="form-group row">
                            <label class="form-control-label" for="sobserva">Observação (Opcional) (1000 caracteres)</label>
                            <textarea autocomplete="off" class="form-control" id="sobserva" maxlength="1000" minlength="2" name="sobserva" onKeyUp="AbnfTabEnter(event,getElementById(&#39;btmodsav&#39;));" onfocus="this.select()" onkeypress="return AbnfScriptKey(event)" spellcheck="false" style="text-transform:uppercase; font-family: Courier New; font-size: 16px; font-weight: bold;">
                            </textarea>
                            </div>
                            <div class="input-group mb-3">
                            <span class="input-group-text">$</span>
                            <input type="text" class="form-control" id="financialInput">
                            </div>
                            <hr>
                            <button type="button" id="btmodsav" class="btn btn-primary mt-2" data-bs-toggle="modal" data-bs-target="#abnfconfsav" href="#">Salvar</button>
                            <input class="btn btn-secondary mt-2" id="btcancel" name="btcancel" onclick="AbnfButtonDisable(this);" type="submit" value="Cancelar">
                            <hr>
                            <button type="button" class="btn btn-success" data-bs-toggle="collapse" data-bs-target="#sdiv0001">Opções adicionais</button>
                            <!-- Modal de gravação -->
                            <div class="modal fade" id="abnfconfsav" tabindex="-1" aria-labelledby="abnfconfsavLabel" aria-hidden="true">
                            <div class="modal-dialog">
                            <div class="modal-content">
                            <div class="modal-header">
                            <h1 class="modal-title fs-5" id="abnfconfsavLabel">Salvar Registro</h1>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                            Confirma a gravação?
                            </div>
                            <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                            <input class="btn btn-primary mt-1" id="btsalreg" name="btsalreg" onclick="AbnfTimeButtonDisable(this,3);" type="submit" value="Salvar">
                            </div>
                            </div>
                            </div>
                            </div>
                            <!-- Fim modais -->
                            <div id="sdiv0001" class="form-group collapse">
                            <br>
                            <input class="form-check-input" id="bperod1k" name="bperod1k" type="checkbox" value="y">
                            <font color="black" face="Courier New" size="3"><b> Permite total de quilometragem acima de 1000 km</b></font><br>
                            <input class="form-check-input" id="bperro1k" name="bperro1k" type="checkbox" value="y">
                            <font color="black" face="Courier New" size="3"><b> Permite total de passageiros acima de 1000 passageiros</b></font><br>
                            </div>
                            </form>
                            </td>
                            <td scope="row">
                            <form method="POST" action="" class="border p-0 mt-2 rounded border-secondary border-3">
                            <style>
                                .abnf_table_scroll {
                                width: 700px;
                                height: 500px;
                                overflow: auto;
                                resize: both;
                                border: 1px solid #ccc;
                                }
                                .abnf_table_scroll table {
                                border-collapse: collapse;
                                width: 100%;
                                }
                                .abnf_table_scroll th,
                                .abnf_table_scroll td {
                                border: 1px solid black;
                                padding: 8px;
                                text-align: left;
                                }
                            </style>
                            <div class="abnf_table_scroll">
                                <table>
                                    <tr>
                                    <th>Cabeçalho 1</th>
                                    <th>Cabeçalho 2</th>
                                    <th>Cabeçalho 3</th>
                                    <th>Cabeçalho 4</th>
                                    <th>Cabeçalho 5</th>
                                    <th>Cabeçalho 6</th>
                                    <th>Cabeçalho 7</th>
                                    <th>Cabeçalho 8</th>
                                    <th>Cabeçalho 9</th>
                                    <th>Cabeçalho 10</th>
                                    </tr>
                                    <tr>
                                    <td>Dado 1</td>
                                    <td>Dado 2</td>
                                    <td>Dado 3</td>
                                    <td>Dado 4</td>
                                    <td>Dado 5</td>
                                    <td>Dado 6</td>
                                    <td>Dado 7</td>
                                    <td>Dado 8</td>
                                    <td>Dado 9</td>
                                    <td>Dado 10</td>
                                    </tr>
                                        <tr>
                                    <td>Dado 1</td>
                                    <td>Dado 2</td>
                                    <td>Dado 3</td>
                                    <td>Dado 4</td>
                                    <td>Dado 5</td>
                                    <td>Dado 6</td>
                                    <td>Dado 7</td>
                                    <td>Dado 8</td>
                                    <td>Dado 9</td>
                                    <td>Dado 10</td>
                                    </tr>
                                    <tr>
                                    <td>Dado 1</td>
                                    <td>Dado 2</td>
                                    <td>Dado 3</td>
                                    <td>Dado 4</td>
                                    <td>Dado 5</td>
                                    <td>Dado 6</td>
                                    <td>Dado 7</td>
                                    <td>Dado 8</td>
                                    <td>Dado 9</td>
                                    <td>Dado 10</td>
                                    </tr>
                                    <tr>
                                    <td>Dado 1</td>
                                    <td>Dado 2</td>
                                    <td>Dado 3</td>
                                    <td>Dado 4</td>
                                    <td>Dado 5</td>
                                    <td>Dado 6</td>
                                    <td>Dado 7</td>
                                    <td>Dado 8</td>
                                    <td>Dado 9</td>
                                    <td>Dado 10</td>
                                    </tr>
                                    <tr>
                                    <td>Dado 1</td>
                                    <td>Dado 2</td>
                                    <td>Dado 3</td>
                                    <td>Dado 4</td>
                                    <td>Dado 5</td>
                                    <td>Dado 6</td>
                                    <td>Dado 7</td>
                                    <td>Dado 8</td>
                                    <td>Dado 9</td>
                                    <td>Dado 10</td>
                                    </tr>
                                    <tr>
                                    <td>Dado 1</td>
                                    <td>Dado 2</td>
                                    <td>Dado 3</td>
                                    <td>Dado 4</td>
                                    <td>Dado 5</td>
                                    <td>Dado 6</td>
                                    <td>Dado 7</td>
                                    <td>Dado 8</td>
                                    <td>Dado 9</td>
                                    <td>Dado 10</td>
                                    </tr>
                                    <tr>
                                    <td>Dado 1</td>
                                    <td>Dado 2</td>
                                    <td>Dado 3</td>
                                    <td>Dado 4</td>
                                    <td>Dado 5</td>
                                    <td>Dado 6</td>
                                    <td>Dado 7</td>
                                    <td>Dado 8</td>
                                    <td>Dado 9</td>
                                    <td>Dado 10</td>
                                    </tr>
                                    <tr>
                                    <td>Dado 1</td>
                                    <td>Dado 2</td>
                                    <td>Dado 3</td>
                                    <td>Dado 4</td>
                                    <td>Dado 5</td>
                                    <td>Dado 6</td>
                                    <td>Dado 7</td>
                                    <td>Dado 8</td>
                                    <td>Dado 9</td>
                                    <td>Dado 10</td>
                                    </tr>
                                    <tr>
                                    <td>Dado 1</td>
                                    <td>Dado 2</td>
                                    <td>Dado 3</td>
                                    <td>Dado 4</td>
                                    <td>Dado 5</td>
                                    <td>Dado 6</td>
                                    <td>Dado 7</td>
                                    <td>Dado 8</td>
                                    <td>Dado 9</td>
                                    <td>Dado 10</td>
                                    </tr>
                                    <tr>
                                    <td>Dado 1</td>
                                    <td>Dado 2</td>
                                    <td>Dado 3</td>
                                    <td>Dado 4</td>
                                    <td>Dado 5</td>
                                    <td>Dado 6</td>
                                    <td>Dado 7</td>
                                    <td>Dado 8</td>
                                    <td>Dado 9</td>
                                    <td>Dado 10</td>
                                    </tr>
                                </table>
                            </div>
                            </form>
                            </td>
                            </tr>
                        </table>
                    </div>
                </div>
            </div>
        </div>             
        '''
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
    sauxht01 = ' class="fixed-top"'
    sauxht02 = ' style="position: fixed; top: 95px; width: 100%;"'
    sauxht03 = ' style="margin-top: 170px;"'
    spagehtm = '''
    <!DOCTYPE html>
    <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <title>Abeinfo Sistemas</title>
            <link href="/static/bootstrap-5.2.1-dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
            <script src="/static/bootstrap-5.2.1-dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
            <script src="/static/socketio-4.7.5/socket.io.js"></script>
        </head>
        <body>
            <div id="abnfdv01"''' + sauxht01 + '''>
                <nav class="navbar navbar-expand-lg bg-light">
                    <div class="container-fluid container">
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                            <span class="navbar-toggler-icon"></span>
                        </button>
                        <ul class="navbar-nav me-auto mb-2 mb-lg-5">
                        </ul>
                        <ul class="d-flex navbar-nav">
                            <li class="nav-item">Teste Sistema</li>
                        </ul>
                    </div>
                </nav>
            </div>
            <div id="abnfdv02"''' + sauxht02 + '''></div>
            <div id="abnfdv03"''' + sauxht03 + '''>''' + snewpage + '''</div>
            <div id="abnfdv04"></div>
            <div id="abnfdv05"></div>
            <div id="abnfdv06"></div>
            <div id="abnfdv07"></div>
            <div id="abnfdv08"></div>
            <div id="abnfdv09"></div>
            <div id="abnfdv10"></div>
            </div>
        </body>
    </html>'''
    sabntoke = 'teste'
    spagehtm = spagehtm  + abnf_websocket_js_socketio(sabntoke)
    spagehtm = spagehtm  + abnf_websocket_js_abeinfo()
    spagehtm = spagehtm  + abnf_websocket_css_menu_dropdown()
    return Response(spagehtm, mimetype="text/html")

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #