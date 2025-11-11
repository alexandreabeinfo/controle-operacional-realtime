## =============================================================
## [abnf000u13c00600.py] - Operacional - Cadastro de Itinerários
## =============================================================

from abnfsrc.abnf000u00s00003 import *              # Arquivo de funções comuns que serão utilizadas por todos os módulos do sistema
from abnfsrc.abnf000u00s00004 import *              # Arquivo de banco de dados

from abnfsrc.abnf000u13c00500 import abnf000u13c00503_operacional_cadastro_trajetos     # Arquivo de funções comuns que serã utilizadas por todos os módulos do sistema

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00600_operacional_cadastro_itinerarios ] //////////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Itinerários.                                                                                                              // #
# // Form inicial.                                                                                                                                       // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00600_operacional_cadastro_itinerarios(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00600_operacional_cadastro_itinerarios(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, '13C00601A'])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        lidotraj = abnf_database_menu(icodbase, (iidfilia, None, None), 'L', '1305A', 1, None, None)
        lsentido = abnf_personal_retorna_lista(10131)
        # Debug: (inicio)
        # abnf_show('08', iidolinh, 1)
        # abnf_show('09', dabnfopg, 2)
        # abnf_show('10', dglobaux, 2)
        # Debug: (fim)        
        lnewpage = [                                                                         
            ('div-0', 'container', None, None),
            ('hr-0', None),
            ('div-0', 'row', None, None),
            ('div-0', 'col d-flex justify-content-center', None, None),
            ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
            ('legend-0', 'Operacional - Cadastro de Itinerários'),
            ('hr-0', None),
            ('label-0',  'Projeto - Linha - Trajeto', 'form-control-label'),
            ('select-0', 'iidotraj', 'form-control', '16px', 'ssentido', lidotraj, 1, None, False),
            ('label-0',  'Sentido', 'form-control-label'),
            ('select-0', 'ssentido', 'form-control', '16px', 'btbusreg', lsentido, 0, None, False),
            ('hr-0', None),
            ('button-0', 'btbusreg', 'btn btn-primary mt-2', 'Buscar'),
            ('alt255-0', 2),
            ('button-0', 'btrelcad', 'btn btn-primary mt-2', 'Relação de trajetos cadastrados'),
            ('form-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
        ]
        snewpage = abnf_create_page(lnewpage)
        abnf_socket_004([1, 'abnfdv03', snewpage])
        
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00601_operacional_cadastro_itinerarios ] //////////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Itinerários.                                                                                                              // #
# // Form de cadastro/alteração do trajeto.                                                                                                              // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00601_operacional_cadastro_itinerarios(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00601_operacional_cadastro_itinerarios(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        if dabnfopg['abnfobj0'] == ['btbusreg', 'btbusreg']:        # Buscar registro existente
            lmfields = [
                ['iidotraj', 'input',  'M', 'trajeto', ['Notnull', 'D', 'Return_integer'], None],
                ['ssentido', 'select', 'M', 'sentido', ['Notnull', 'D'],                   None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btbusreg')
            # Debug: (inicio)
            # abnf_show('08', lmfields, 1)
            # abnf_show('09', dabnfopg, 2)
            # abnf_show('10', dglobaux, 2)
            # Debug: (fim)
            if bvalidad:
                iidotraj = lmfields[0][5]
                ssentido = lmfields[1][5]
                # //////////////////
                # Buscando o trajeto
                # //////////////////
                lcamposb = ('idoproj', 'idolinh', 'codotra', 'desotra')
                lfilbusc = (('idotraj', '=', iidotraj), ('situreg', '!=', 'C'))
                lorderby = None
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_trajetos', lcamposb, lfilbusc, lorderby)
                if lsqlre01 == [] or iqtdre01 == 0:
                    abnf_alert('O trajeto não foi encontrado!', 4)
                    abnf_socket_004([5, 'btbusreg'])
                else:
                    iidoproj = lsqlre01[0][0]
                    iidolinh = lsqlre01[0][1]
                    sdesotra = '[' + lsqlre01[0][2] + '] - ' + lsqlre01[0][3]
                    sdessent = abnf_personal_retorna_string(10131, ssentido)
                    # //////////////////
                    # Buscando o projeto
                    # //////////////////
                    lcamposb = ('codopro', 'desopro')
                    lfilbusc = (('idoproj', '=', iidoproj), ('situreg', '!=', 'C'))
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_projetos', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 == [] or iqtdre01 == 0:
                        abnf_alert('O projeto não foi encontrado!', 4)
                        abnf_socket_004([5, 'btbusreg'])
                    else:
                        sdesopro = lsqlre01[0][1] + ' (' + str(lsqlre01[0][0]) + ')'
                        # ////////////////
                        # Buscando a linha
                        # ////////////////
                        lcamposb = ('codolin', 'desolin')
                        lfilbusc = (('idolinh', '=', iidolinh), ('situreg', '!=', 'C'))
                        lorderby = None
                        lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_linhas', lcamposb, lfilbusc, lorderby)
                        if lsqlre01 == [] or iqtdre01 == 0:
                            abnf_alert('A linha não foi encontrada!', 4)
                            abnf_socket_004([5, 'btbusreg'])
                        else:
                            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '13C00602A'),)]) # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
                            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidotraj', iidotraj),)])    # ==> Guardado dados do trajeto para a próxima função. Obs: tem que ter essa vírgula: "),)])"
                            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('ssentido', ssentido),)])    # ==> Guardado dados do trajeto para a próxima função. Obs: tem que ter essa vírgula: "),)])"
                            sdesolin = lsqlre01[0][0] + ' - ' + str(lsqlre01[0][1])
                            lidlogra = abnf_database_menu(icodbase, None, 'L', '0103', 1, 1, 2)
                            lidotraj = abnf_database_menu(icodbase, (iidfilia, None, None), 'L', '1305A', 1, None, None)
                            lsentido = abnf_personal_retorna_lista(10131)
                            lnewpage = [
                                ('div-0', 'container', None, None),
                                ('hr-0', None),
                                ('div-0', 'row', None, None),
                                ('div-0', 'col d-flex justify-content-center', None, None),
                                ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                                ('table-0', 'table table-bordered table-sm table-responsive'),
                                    ('tr-0', 'text-white bg-secondary', False),
                                        ('td-0', None, 2, None, 1, None, None),
                                            ('legend-0', 'Cadastro de Itinerários'),
                                        ('td-9', None),
                                    ('tr-9', None),
                                    ('tr-0', None, False),
                                        ('td-0', None, None, None, None, None, None),
                                            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                                            ('table-0', 'table table-bordered table-sm table-responsive'),
                                                ('tr-0', None, False),
                                                    ('td-0', 'table-active', 1, None, 0, None, None),   ('label-0', 'Projeto', 'form-control-label'),                 ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),             ('font-0', 'Courier New;', '20px', 'darkcyan', sdesopro),     ('td-9', None),
                                                    ('td-0', None, 1,    4, 1,    1, None),             ('button-0', 'btcancel', 'btn btn-primary mt-2', 'Cancelar'), ('td-9', None),
                                                ('tr-9', None),
                                                ('tr-0', None, False),
                                                    ('td-0', 'table-active', 1, None, 0, None, None),   ('label-0', 'Linha', 'form-control-label'),                   ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),             ('font-0', 'Courier New;', '20px', 'darkcyan', sdesolin),     ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                                                                           ('td-9', None),
                                                ('tr-9', None),
                                                ('tr-0', None, False),
                                                    ('td-0', 'table-active', 1, None, 0, None, None),   ('label-0', 'Trajeto', 'form-control-label'),                 ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),             ('font-0', 'Courier New;', '20px', 'darkcyan', sdesotra),     ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                                                                           ('td-9', None),
                                                ('tr-9', None),
                                                ('tr-0', None, False),
                                                    ('td-0', 'table-active', 1, None, 0, None, None),   ('label-0', 'Sentido', 'form-control-label'),                 ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),             ('font-0', 'Courier New;', '20px', 'darkcyan', sdessent),     ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),                                                                           ('td-9', None),
                                                ('tr-9', None),
                                            ('table-9', None),
                                            ('form-9', None),
                                            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                                            ('table-0', None),
                                                ('tr-0', None, False),
                                                    ('div-1', 'sdivofic'),
                                                    ('div-9', None),
                                                    ('div-1', 'sdivitin'),
                                                    ('div-9', None),
                                                ('tr-9', None),
                                                ('tr-0', None, False),
                                                    ('td-0', None, 1, None, 1, None, None),
                                                        ('button-1', 'btexclox', 'btn btn-danger mt-2', 'Remover logradouros selecionados', 'Excluir Registro', 'btexclog', 'btn btn-danger mt-2', 'Excluir', 'Confirma a remoção dos logradouros selecionados?'),
                                                    ('td-9', None),
                                                    ('td-0', None, 1, None, 1, None, None), ('alt255-0', 2), ('td-9', None),
                                                    ('td-0', 'table-active', 1, None, 1, None, None), 
                                                        ('button-1', 'btsalrax', 'btn btn-primary mt-2', 'Salvar rascunho', 'Salvar', 'btsalras', 'btn btn-primary mt-2', 'Salvar', 'Confirma a gravação do itinerário através deste rascunho?'),
                                                    ('td-9', None),
                                                    ('td-0', None, 1, None, 1, None, None), ('alt255-0', 2), ('td-9', None),
                                                    ('td-0', None, 1, None, 1, None, None),    
                                                        ('button-0', 'btgerrel', 'btn btn-primary mt-2', 'Gerar relatório', None),
                                                    ('td-9', None),
                                                ('tr-9', None),
                                            ('table-9', None),
                                            ('form-9', None),
                                            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                                            ('table-0', 'table table-bordered table-sm table-responsive'),
                                                ('tr-0', None, False),
                                                    ('td-0', 'table-active', 1, None, 0, None, None), ('label-0', 'Ordem&nbsp;do&nbsp;itinerário&nbsp;(vazio&nbsp;para&nbsp;por&nbsp;no&nbsp;final)&nbsp;&nbsp;', 'form-control-label'), ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),           ('label-0', '&nbsp;', 'form-control-label'),                                                      ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),           ('number-0', 'iordemit', 'form-control', 0, 4, '16px', None, 'iidlogra', True, None),             ('td-9', None),
                                                ('tr-9', None),
                                                ('tr-0', None, False),
                                                    ('td-0', 'table-active', 1, None, 0, None, None), ('label-0', 'Logradouro', 'form-control-label'),                                                  ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),           ('label-0', '&nbsp;', 'form-control-label'),                                                      ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),           ('select-0', 'iidlogra', 'form-control', '16px', 'scomplem', lidlogra, 1, None, False),           ('td-9', None),
                                                ('tr-9', None),
                                                ('tr-0', None, False),
                                                    ('td-0', 'table-active', 1, None, 0, None, None), ('label-0', 'Complemento (opcional)', 'form-control-label'),                                      ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),           ('label-0', '&nbsp;', 'form-control-label'),                                                      ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),           ('input-0', 'scomplem', 'form-control', 0, 100, '16px', None, 'btinsiti', True, 0),               ('td-9', None),
                                                ('tr-9', None),
                                                ('tr-0', None, False),
                                                    ('td-0', 'table-active', 1, None, 0, None, None), ('label-0', 'Destaque', 'form-control-label'),                                                    ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),           ('label-0', '&nbsp;', 'form-control-label'),                                                      ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),           ('checkbox-0', 'bdestaqu', 1, 0, 'Courier New', '16px', 'b', 'P', None),                          ('td-9', None),
                                                ('tr-9', None),
                                                ('tr-0', None, False),
                                                    ('td-0', 'table-active', 1, None, 1, None, None), ('td-9', None),
                                                    ('td-0', 'table-active', 2, None, 1, None, None), 
                                                    ('button-0', 'btinsiti', 'btn btn-primary mt-2', 'Inserir novo itinerário', None),
                                                    ('td-9', None),
                                                ('tr-9', None),
                                            ('table-9', None),
                                            ('form-9', None),
                                            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                                            ('table-0', 'table table-bordered table-sm table-responsive'),
                                                ('tr-0', None, False),
                                                    ('td-0', 'table-active', 1, None, 0, None, None), ('label-0', 'Projeto-Linha-Trajeto', 'form-control-label'),                                       ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),           ('label-0', '&nbsp;', 'form-control-label'),                                                      ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),           ('select-0', 'iidotimp', 'form-control', '16px', 'ssentimp', lidotraj, 1, None, False),           ('td-9', None),
                                                ('tr-9', None),
                                                ('tr-0', None, False),
                                                    ('td-0', 'table-active', 1, None, 0, None, None), ('label-0', 'Sentido', 'form-control-label'),                                                     ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),           ('label-0', '&nbsp;', 'form-control-label'),                                                      ('td-9', None),
                                                    ('td-0', None, 1, None, 0, None, None),           ('select-0', 'ssentimp', 'form-control', '16px', 'btimporx', lsentido, 1, None, False),           ('td-9', None),
                                                ('tr-9', None),
                                                ('tr-0', None, False),
                                                    ('td-0', 'table-active', 1, None, 1, None, None), ('td-9', None),
                                                    ('td-0', 'table-active', 2, None, 1, None, None),
                                                    ('button-1', 'btimporx', 'btn btn-primary mt-2', 'Importar logradouros do [Projeto-Linha-Trajeto-Sentido] informado', 'Importar logradouros', 'btimport', 'btn btn-primary mt-2', 'Importar', 'Confirma a importação dos dados?'),
                                                    ('td-9', None),
                                                ('tr-9', None),
                                            ('table-9', None),
                                            ('form-9', None),
                                        ('td-9', None),
                                    ('tr-9', None),
                                ('table-9', None),
                                ('div-9', None),
                                ('div-9', None),
                                ('div-9', None),
                                ('div-9', None),
                            ]
                            snewpage = abnf_create_page(lnewpage)
                            abnf_socket_004([1, 'abnfdv03', snewpage])
                            # ////////////////////////////////////////
                            # Buscando os itinerários da linha/trajeto
                            # ////////////////////////////////////////
                            litinera = []
                            lcamposb = ('ordemit', 'idlogra', 'complem', 'destaqu')
                            lfilbusc = (('idotraj', '=', iidotraj), ('sentido', '=', ssentido), ('situreg', '!=', 'C'))
                            lorderby = (('idotraj', 'sentido', 'ordemit', 'idoitin'))
                            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_itinerarios', lcamposb, lfilbusc, lorderby)
                            if lsqlre01 != [] and iqtdre01 > 0:
                                for lauxi001 in lsqlre01:
                                    litinera.append([
                                        lauxi001[0],
                                        lauxi001[1],
                                        lauxi001[2],
                                        lauxi001[3],
                                    ])
                            abnf000u13c00603_operacional_cadastro_itinerarios(sabnproj, sabntoke, icodbase, litinera, True)
        elif dabnfopg['abnfobj0'] == ['btrelcad', 'btrelcad']:      # Relação dos trajetos cadastrados
            abnf000u13c00503_operacional_cadastro_trajetos(dabnfopg)
            
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00602_operacional_cadastro_itinerarios ] //////////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Itinerários.                                                                                                              // #
# // Gravação/exclusão dos logradouros do itinerário.                                                                                                    // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00602_operacional_cadastro_itinerarios(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00602_operacional_cadastro_itinerarios(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        iidotraj = dglobaux['iidotraj']
        if dabnfopg['abnfobj0'] == ['btcancel', 'btcancel']:        # Voltar para tela anterior
            abnf000u13c00600_operacional_cadastro_itinerarios(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btinsiti', 'btinsiti']:
            # ////////////////////////////////
            # Inserir logradouro no itinerário
            # ////////////////////////////////
            lmfields = [
                ['iordemit', 'number',   'F', 'ordem do itinerário', ['Empty_to_zero'],                  None],
                ['iidlogra', 'select',   'M', 'logradouro',          ['Notnull', 'D', 'Return_integer'], None],
                ['scomplem', 'input',    'M', 'complemento',         [],                                 None],
                ['bdestaqu', 'checkbox', 'M', 'destaque',            [],                                 None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btinsiti')
            if bvalidad:
                iordemit = lmfields[0][5]
                iidlogra = lmfields[1][5]
                scomplem = lmfields[2][5]
                bdestaqu = lmfields[3][5]
                if iordemit == 0: iordemit = 99999  # ==> Para ficar na ultima posição da lista
                # //////////////////////////////
                # Buscando o registro do trajeto
                # //////////////////////////////
                lcamposb = ('idotraj', None)
                lfilbusc = (('idotraj', '=', iidotraj), ('situreg', '!=', 'C'), None)
                lorderby = None
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_trajetos', lcamposb, lfilbusc, lorderby)
                if lsqlre01 == [] or iqtdre01 == 0:
                    abnf_alert('Erro interno! Não foi encontrado o registro ID ' + str(iidotraj) + '! Entre em contato com o depto. de sistemas!', 4)
                    abnf_socket_004([5, 'btinsiti'])
                else:
                    # //////////////////////////////
                    # Busca na memória a lista atual
                    # //////////////////////////////
                    litinera = dglobaux['litinera']
                    # /////////////////////////////////////////////////////////////////////////////////
                    # Acrescenta 1 na numeração de ordem igual ao acima da nova ordem que será incluída
                    # /////////////////////////////////////////////////////////////////////////////////
                    if litinera != []:
                        for lauxi001 in litinera:
                            if lauxi001[0] >= iordemit:
                               lauxi001[0] = lauxi001[0] + 1
                    # ///////////////////
                    # Inserer o novo ítem
                    # ///////////////////
                    litinera.append([
                        iordemit,
                        iidlogra,
                        scomplem,
                        bdestaqu,
                    ])
                    # /////////////////////////
                    # Organiza a ordem da lista
                    # /////////////////////////
                    litinera.sort()
                    # ///////////////////////////////////////////////////
                    # Atualiza toda a numeração da lista conforme a ordem
                    # ///////////////////////////////////////////////////
                    iauxi001 = 0
                    for lauxi001 in litinera:
                        iauxi001 += 1
                        lauxi001[0] = iauxi001
                    # ///////////
                    # Finalização
                    # ///////////
                    abnf_alert('Logradouro inserido com sucesso!', 3)
                    abnf000u13c00603_operacional_cadastro_itinerarios(sabnproj, sabntoke, icodbase, litinera, False)
                    abnf_socket_004([5, 'btinsiti'])
                    abnf_socket_004([3, 'iordemit', ''])     # Limpa o campo
                    abnf_socket_004([3, 'iidlogra', ''])     # Limpa o campo
                    abnf_socket_004([3, 'scomplem', ''])     # Limpa o campo
                    abnf_socket_004([15, 'bdestaqu'])        # Limpa o checkbox
        elif dabnfopg['abnfobj0'] == ['btexclog', 'btexclog']:
            # /////////////////////////////////
            # Remover logradouros do itinerário
            # /////////////////////////////////
            lmfields = [
                ['iordemix', 'checkbox', 'Nenhum logradouro foi marcado para ser removido', ['Notnull', 'Return_integer'], []],
            ]
            bvalidad, lmfields = abnf_find_checkbox_radio(dabnfopg, lmfields, 'btexclog')
            if bvalidad:
                lordemix = lmfields[0][4]
                # //////////////////////////////
                # Busca na memória a lista atual
                # //////////////////////////////
                litinera = dglobaux['litinera']
                # /////////////////////////////////////////////////////////
                # Refaz a lista somente com os ítens que não foram marcados
                # /////////////////////////////////////////////////////////
                lititemp = []
                for lauxi001 in litinera:
                    if not lauxi001[0] in lordemix:
                        lititemp.append(lauxi001)
                litinera = lititemp
                # /////////////////////////////////////////////////////////////////////////
                # Atualiza toda a numeração da lista conforme a ordem dos ítens que sobrarm
                # /////////////////////////////////////////////////////////////////////////
                if litinera != []:
                    iauxi001 = 0
                    for lauxi001 in litinera:
                        iauxi001 += 1
                        lauxi001[0] = iauxi001
                # ///////////
                # Finalização
                # ///////////
                iauxi001 = len(lordemix)
                if iauxi001 == 1: abnf_alert('1 logradouro removido com sucesso!', 3)
                else:             abnf_alert(str(iauxi001) + ' logradouros removidos com sucesso!', 3)
                abnf000u13c00603_operacional_cadastro_itinerarios(sabnproj, sabntoke, icodbase, litinera, False)
        elif dabnfopg['abnfobj0'] == ['btsalras', 'btsalras']:
            # ///////////////
            # Salvar rascunho
            # ///////////////
            iidotraj = dglobaux['iidotraj']
            ssentido = dglobaux['ssentido']
            litinera = dglobaux['litinera']
            # //////////////////
            # Buscando o trajeto
            # //////////////////
            lcamposb = ('idoproj', 'idolinh', 'situreg')
            lfilbusc = (('idotraj', '=', iidotraj), ('situreg', '!=', 'C'))
            lorderby = None
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_trajetos', lcamposb, lfilbusc, lorderby)
            if lsqlre01 == [] or iqtdre01 == 0:
                abnf_alert('O trajeto não foi encontrado!', 4)
                abnf_socket_004([5, 'btsalras'])
            elif lsqlre01[0][2] != 'A':
                abnf_alert('O trajeto não está ativo!', 5)
                abnf_socket_004([5, 'btsalras'])
            else:
                iidoproj = lsqlre01[0][0]
                iidolinh = lsqlre01[0][1]
                # //////////////////
                # Buscando o projeto
                # //////////////////
                lcamposb = ('situreg', 'idfilia')
                lfilbusc = (('idoproj', '=', iidoproj), ('situreg', '!=', 'C'))
                lorderby = None
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_projetos', lcamposb, lfilbusc, lorderby)
                if lsqlre01 == [] or iqtdre01 == 0:
                    abnf_alert('O projeto não foi encontrado!', 4)
                    abnf_socket_004([5, 'btsalras'])
                elif lsqlre01[0][0] != 'A':
                    abnf_alert('O projeto não está ativo!', 5)
                    abnf_socket_004([5, 'btsalras'])
                elif lsqlre01[0][1] != iidfilia:
                    abnf_alert('Alterações não permitidas devido a esta linha não pertencer a esta filial!', 5)
                    abnf_socket_004([5, 'btsalras'])  
                else:
                    # ////////////////
                    # Buscando a linha
                    # ////////////////
                    lcamposb = ('situreg', 'idfilia')
                    lfilbusc = (('idolinh', '=', iidolinh), ('situreg', '!=', 'C'))
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_linhas', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 == [] or iqtdre01 == 0:
                        abnf_alert('A linha não foi encontrada!', 4)
                        abnf_socket_004([5, 'btsalras'])
                    elif lsqlre01[0][0] != 'A':
                        abnf_alert('A linha não esta ativa!', 5)
                        abnf_socket_004([5, 'btsalras'])
                    elif lsqlre01[0][1] != iidfilia:
                        abnf_alert('Alterações não permitidas devido a esta linha não pertencer a esta filial!', 5)
                        abnf_socket_004([5, 'btsalras'])
                    else:
                        abnf_alert('Aguarde! Gravando registros...', 15)
                        bvalidad = True
                        # ///////////////////////////////////////////////////////////////
                        # Cancelando todos os registros atuais relacionados ao itinerário
                        # ///////////////////////////////////////////////////////////////
                        if bvalidad:
                            lcamposb = ('idoitin', None)
                            lfilbusc = (('idotraj', '=', iidotraj), ('sentido', '=', ssentido), ('situreg', '!=', 'C'), None)
                            lorderby = None
                            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_itinerarios', lcamposb, lfilbusc, lorderby)
                            if lsqlre01 != [] or iqtdre01 != 0:
                                lidoitin = []
                                for lauxi001 in lsqlre01:
                                    lidoitin.append(lauxi001[0])
                                for iidoitin in lidoitin:
                                    bvalidad = abnf_database_exclui_registro(icodbase, sabnproj, 'abnf_operacional_cadastro_itinerarios', iidoitin, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'])
                                    if not bvalidad:
                                        abnf_alert('Erro ao excluir registros de itinerários! Entre em contato com o depto. de sistemas!', 4)
                                        break
                        # //////////////////////////////////////////////////////////////////////////////////
                        # Guardando os IDs de todos os registros que estão excluídos para serem reutilizados
                        # //////////////////////////////////////////////////////////////////////////////////
                        if bvalidad:
                            lidexclu = []
                            lcamposb = ('idoitin', None)
                            lfilbusc = (('situreg', '=', 'C'), None)
                            lorderby = None
                            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_itinerarios', lcamposb, lfilbusc, lorderby)
                            if lsqlre01 != [] or iqtdre01 != 0:
                                for lauxi001 in lsqlre01:
                                    lidexclu.append(lauxi001[0])
                            # Debug (início)
                            # abnf_show('09', lidexclu, 0)
                            # abnf_show('10', len(lidexclu), 0)
                            # Debug (fim)
                        # /////////////////////////////////////////////////////////////////////////////////////////
                        # Inserindo os itinerários em registros excluídos ou criando novos registros de itinerários
                        # /////////////////////////////////////////////////////////////////////////////////////////
                        if bvalidad:
                            for lauxi001 in litinera:
                                iordemit = lauxi001[0]
                                iidlogra = lauxi001[1]
                                scomplem = lauxi001[2]
                                bdestaqu = lauxi001[3]
                                # /////////////////////////////////////////////////////
                                # Insere os dados em um registro de itinerário excluído
                                # /////////////////////////////////////////////////////
                                if lidexclu != []:
                                    iidoitin = lidexclu[0]
                                    del lidexclu[0]
                                    bvalidad = abnf_database_altera_dados_v02(icodbase, sabnproj, 'abnf_operacional_cadastro_itinerarios', iidoitin, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                                    [
                                        ('idotraj', iidotraj),
                                        ('sentido', ssentido),
                                        ('ordemit', iordemit),
                                        ('idlogra', iidlogra),
                                        ('complem', scomplem),
                                        ('destaqu', bdestaqu),
                                        ('situreg', 'A'),
                                    ])
                                    if not bvalidad:
                                        break
                                # ///////////////////////////////////
                                # Cria um registro novo de itinerário
                                # ///////////////////////////////////
                                else:
                                    bvalidad, iproxiid = abnf_database_insere_dados_v02(icodbase, sabnproj, 'abnf_operacional_cadastro_itinerarios', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                                    [
                                        ('idotraj', iidotraj),
                                        ('sentido', ssentido),
                                        ('ordemit', iordemit),
                                        ('idlogra', iidlogra),
                                        ('complem', scomplem),
                                        ('destaqu', bdestaqu),
                                        ('situreg', 'A'),
                                    ])
                                    if not bvalidad:
                                        break
                            if not bvalidad:
                                abnf_alert('Erro ao criar novos registros de itinerários! Entre em contato com o depto. de sistemas!', 4)
                            else:
                                abnf_alert('Registros gravados com sucesso!', 3)
                                abnf000u13c00603_operacional_cadastro_itinerarios(sabnproj, sabntoke, icodbase, litinera, True)
                                abnf_socket_004([5, 'btsalras'])
        elif dabnfopg['abnfobj0'] == ['btimport', 'btimport']:
            # /////////////////////////
            # Importação de logradouros
            # /////////////////////////
            lmfields = [
                ['iidotimp', 'input',  'M', 'trajeto a ser importado', ['Notnull', 'D', 'Return_integer'], None],
                ['ssentimp', 'select', 'M', 'sentido a ser importado', ['Notnull', 'D'],                   None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btbusreg')
            # Debug: (inicio)
            # abnf_show('08', lmfields, 1)
            # abnf_show('09', dabnfopg, 2)
            # abnf_show('10', dglobaux, 2)
            # Debug: (fim)
            if bvalidad:
                iidotimp = lmfields[0][5]
                ssentimp = lmfields[1][5]
                litinera = dglobaux['litinera']
                iauxi001 = len(litinera)
                # ////////////////////////////////////////
                # Buscando os itinerários da linha/trajeto
                # ////////////////////////////////////////
                lcamposb = ('idlogra', 'complem', 'destaqu')
                lfilbusc = (('idotraj', '=', iidotimp), ('sentido', '=', ssentimp), ('situreg', '!=', 'C'))
                lorderby = (('idotraj', 'sentido', 'ordemit', 'idoitin'))
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_itinerarios', lcamposb, lfilbusc, lorderby)
                if lsqlre01 != [] and iqtdre01 > 0:
                    for lauxi001 in lsqlre01:
                        iauxi001 += 1
                        litinera.append([
                            iauxi001,
                            lauxi001[0],
                            lauxi001[1],
                            lauxi001[2],
                        ])
                    abnf_alert('Importação realizada com sucesso com sucesso!', 3)   
                    abnf_socket_004([3, 'iidotimp', ''])     # Limpa o campo
                    abnf_socket_004([3, 'ssentimp', ''])     # Limpa o campo
                    abnf000u13c00603_operacional_cadastro_itinerarios(sabnproj, sabntoke, icodbase, litinera, False)
                else:
                    abnf_alert('Não haviam dados para serem importados!', 4)
        elif dabnfopg['abnfobj0'] == ['btgerrel', 'btgerrel']:
            # /////////
            # Relatório
            # /////////
            iidotraj = dglobaux['iidotraj']
            ssentido = dglobaux['ssentido']
            litinera = dglobaux['litinera']
            abnf000u13c00604_operacional_cadastro_itinerarios(dabnfopg, iidotraj, ssentido, litinera)
                
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00603_operacional_cadastro_itinerarios ] //////////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Itinerários.                                                                                                              // #
# // Reorganiza a lista de itinerários que está em memória, atualiza e posta a DIV.                                                                      // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00603_operacional_cadastro_itinerarios(sabnproj, sabntoke, icodbase, litinera, boficial):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00603_operacional_cadastro_itinerarios(...)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    # ==> dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
    # ********  litinera  ********
    # iordemit  => [0]  - Ordem no itinerário
    # iidlogra  => [1]  - ID do logradouro
    # scomplem  => [2]  - Complemento
    # bdestaqu  => [3]  - Destaque
    # ==> if boficial in (True, False):
    if boficial:
        lauxi001 = ('bg-success', 'white', 'Oficial')
        abnf_socket_004([10, 'btsalrax'])   # Desabilita o botão "Salvar rascunho"
    else:
        lauxi001 = ('bg-warning', None, 'Rascunho')
        abnf_socket_004([5, 'btsalrax'])    # Habilita o botão "Salvar rascunho"
    # ==> else:
    # ==>    lauxi001 = ('bg-secondary', 'white', 'Itinerário')
    lnewpage = [
        ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
        ('table-0', 'table table-bordered table-sm table-responsive border-secondary'),
            ('tr-0', None, False),
                ('td-0', lauxi001[0], 1, None, 1, None, None),
                ('font-0', 'Courier New;', '20px', lauxi001[1], lauxi001[2]),
                ('td-9', None),
            ('tr-9', None),
        ('table-9', None),
        ('form-9', None),
    ]
    snewpage = abnf_create_page(lnewpage)
    abnf_socket_004([1, 'sdivofic', snewpage])
    lnewpage = [
        ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
        ('table-2', 'table table-bordered table-sm table-responsive border-secondary', 1, 1211, 500, None, None),
            ('tr-0', None, False),
                ('td-0', 'table-active', 1, None, 1, None, None), ('font-0', 'Courier New;', '12px', None, 'Ordem'      ), ('td-9', None),
                ('td-0', 'table-active', 1, None, 1, None, None), ('font-0', 'Courier New;', '12px', None, 'Tipo'       ), ('td-9', None),
                ('td-0', 'table-active', 1, None, 1, None, None), ('font-0', 'Courier New;', '12px', None, 'Logradouro' ), ('td-9', None),
                ('td-0', 'table-active', 1, None, 1, None, None), ('font-0', 'Courier New;', '12px', None, 'Complemento'), ('td-9', None),
                ('td-0', 'table-active', 1, None, 1, None, None), ('font-0', 'Courier New;', '12px', None, 'Bairro'     ), ('td-9', None),
                ('td-0', 'table-active', 1, None, 1, None, None), ('font-0', 'Courier New;', '12px', None, 'Cidade'     ), ('td-9', None),
                ('td-0', 'table-active', 1, None, 1, None, None), ('font-0', 'Courier New;', '12px', None, 'Estado'     ), ('td-9', None),
                ('td-0', 'table-active', 1, None, 1, None, None), ('font-0', 'Courier New;', '12px', None, 'Destaque'   ), ('td-9', None),
                ('td-0', 'table-active', 1, None, 1, None, None), ('td-9', None),
            ('tr-9', None)
    ]
    if litinera == []:
        abnf_socket_004([10, 'btexclox'])   # Desabilita o botão "Remover logradouros selecionados"
    else:
        # ///////////////
        # Habilita botões
        # ///////////////
        abnf_socket_004([5, 'btexclox'])    # Habilita o botão "Remover logradouros selecionados"
        # ////////////////////
        # Monta os dicionários
        # ////////////////////
        didlogra = abnf_database_menu(icodbase, None, 'D', '0103', 1, 1, 2)
        # /////////////////////////////
        # Monta a tela com o itinerário
        # /////////////////////////////
        icontlog = 0
        for lauxi001 in litinera:
            icontlog += 1
            iordemit = lauxi001[0]
            iidlogra = lauxi001[1]
            scomplem = lauxi001[2]
            bdestaqu = lauxi001[3]
            # /// #
            sordemit = str(1000 + iordemit)[1:]
            lidlogra = didlogra.get(iidlogra, ('', '', '', '', '', '')) if iidlogra != None and iidlogra > 0 else ('', '', '', '', '', '')
            stiplogr = lidlogra[1]
            sdeslogr = lidlogra[2]
            sdesbair = lidlogra[3]
            sdescida = lidlogra[4]
            sdesesta = lidlogra[5]
            sdestaqu = '&#128307;' if bdestaqu else ''
            lauxi002 = ('checkbox-0', 'iordemix[' + str(iordemit) + ']', iordemit, None, 'Courier New', '12px', 'b', 'P', None)
            # /// #
            lnewpage = lnewpage + [
                ('tr-0', None, True),
                    ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '15px', 'darkcyan', sordemit), ('td-9', None),
                    ('td-0', None, 1, None, 0, None, None), ('font-0', 'Courier New;', '15px', None, stiplogr),       ('td-9', None),
                    ('td-0', None, 1, None, 0, None, None), ('font-0', 'Courier New;', '15px', None, sdeslogr),       ('td-9', None),
                    ('td-0', None, 1, None, 0, None, None), ('font-0', 'Courier New;', '15px', None, scomplem),       ('td-9', None),
                    ('td-0', None, 1, None, 0, None, None), ('font-0', 'Courier New;', '15px', None, sdesbair),       ('td-9', None),
                    ('td-0', None, 1, None, 0, None, None), ('font-0', 'Courier New;', '15px', None, sdescida),       ('td-9', None),
                    ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '15px', None, sdesesta),       ('td-9', None),
                    ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '15px', None, sdestaqu),       ('td-9', None),
                    ('td-0', None, 1, None, 1, None, None), lauxi002, ('td-9', None),
                ('tr-9', None)
            ]
        lnewpage = lnewpage + [
                ('tr-0', None, False),
                    ('td-0', 'table-active', 8, None, 2, None, None), ('font-0', 'Courier New;', '12px', None, 'Quantidade de logradouros:'), ('td-9', None),
                    ('td-0', 'table-active', 1, None, 1, None, None), ('font-0', 'Courier New;', '12px', None, abnf_formata_numero_milhar_decimal(icontlog, True, 0)), ('td-9', None),
                ('tr-9', None),
        ]
    lnewpage = lnewpage + [
        ('table-9', None),
        ('div-9', None),    # <== Esse 'div-9' é uma necessidade pelo uso de 'table-2'.
        ('form-9', None),
    ]
    # //////////////////////////////
    # Armazena 'litinera' em memória
    # //////////////////////////////
    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('litinera', litinera),)]) # ==> Guardado lista de itinerário para a próxima função. Obs: tem que ter essa vírgula: "),)])"
    # //////////////
    # Atualiza a DIV
    # //////////////
    snewpage = abnf_create_page(lnewpage)
    abnf_socket_004([1, 'sdivitin', snewpage])
    # Debug (início)
    # abnf_show('10', litinera, 0)
    # Debug (fim)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00604_operacional_cadastro_itinerarios ] //////////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Itinerários.                                                                                                              // #
# // Relatórios.                                                                                                                                         // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00604_operacional_cadastro_itinerarios(dabnfopg, iidotraj, ssentido, litinera):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00604_operacional_cadastro_itinerarios(...)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        # ////////////////////
        # Listas e dicionários
        # ////////////////////
        didlogra = abnf_database_menu(icodbase, None, 'D', '0103', 1, 1, 2)
        # /////////////////////
        # Variaveis de ambiente
        # /////////////////////
        ifontlen = 2
        icolspan = 8
        sarqurel = abnf_imprime_file(0, sabntoke)
        with open('abnftmp/' + sarqurel, 'w') as sarquwri:
            snomeemp, snomefil = abnf_database_retorna_empresa_filial(icodbase, iidfilia)
            abnf_imprime_doctype_head_fhead_body_form_table_thead(sarquwri, 3)
            abnf_imprime_thead_001_abeinfo_sistemas(sarquwri, icolspan)
            abnf_imprime_thead_002_titulo_relatorio(sarquwri, icolspan, 'ITINERÁRIOS DE TRAJETOS')
            abnf_imprime_thead_003_empresa_filial(sarquwri, icolspan, snomeemp, snomefil)
            # smensage = 'Per&iacute;odo: ' + abnf_converte_data(ddataini) + ' &agrave;s ' + abnf_converte_hora(thoraini) + ' at&eacute; ' + abnf_converte_data(ddatafim) + ' &agrave;s ' + abnf_converte_hora(thorafim)
            # abnf_imprime_thead_004_parametros(sarquwri, icolspan, smensage)
            abnf_imprime_thead_005_datetime(sarquwri, icolspan)
            abnf_imprime_line(sarquwri, icolspan, 'darkcyan')
            # //////////////////
            # Buscando o trajeto
            # //////////////////
            lcamposb = ('idoproj', 'idolinh', 'codotra', 'desotra')
            lfilbusc = (('idotraj', '=', iidotraj), ('situreg', '!=', 'C'))
            lorderby = None
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_trajetos', lcamposb, lfilbusc, lorderby)
            if lsqlre01 == [] or iqtdre01 == 0:
                abnf_alert('O trajeto não foi encontrado!', 4)
                abnf_socket_004([5, 'btbusreg'])
            else:
                iidoproj = lsqlre01[0][0]
                iidolinh = lsqlre01[0][1]
                sdesotra = '[' + lsqlre01[0][2] + '] - ' + lsqlre01[0][3]
                sdessent = abnf_personal_retorna_string(10131, ssentido)
                # //////////////////
                # Buscando o projeto
                # //////////////////
                lcamposb = ('codopro', 'desopro')
                lfilbusc = (('idoproj', '=', iidoproj), ('situreg', '!=', 'C'))
                lorderby = None
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_projetos', lcamposb, lfilbusc, lorderby)
                if lsqlre01 == [] or iqtdre01 == 0:
                    abnf_alert('O projeto não foi encontrado!', 4)
                    abnf_socket_004([5, 'btbusreg'])
                else:
                    sdesopro = lsqlre01[0][1] + ' (' + str(lsqlre01[0][0]) + ')'
                    # ////////////////
                    # Buscando a linha
                    # ////////////////
                    lcamposb = ('codolin', 'desolin')
                    lfilbusc = (('idolinh', '=', iidolinh), ('situreg', '!=', 'C'))
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_linhas', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 == [] or iqtdre01 == 0:
                        abnf_alert('A linha não foi encontrada!', 4)
                        abnf_socket_004([5, 'btbusreg'])
                    else:
                        sdesolin = lsqlre01[0][0] + ' - ' + str(lsqlre01[0][1])
                        abnf_imprime_info_001(sarquwri, None, None, 1,
                            [
                                ('Projeto:',            1, 0, '#CEF1F5', 'left', 'black', 'Courier New', ifontlen, True, False),
                                (sdesopro,   icolspan - 1, 0, None,      'left', 'black', 'Courier New', ifontlen, True, False),
                            ]
                        )
                        abnf_imprime_info_001(sarquwri, None, None, 1,
                            [
                                ('Linha:',              1, 0, '#CEF1F5', 'left', 'black', 'Courier New', ifontlen, True, False),
                                (sdesolin,   icolspan - 1, 0, None,      'left', 'black', 'Courier New', ifontlen, True, False),
                            ]
                        )
                        abnf_imprime_info_001(sarquwri, None, None, 1,
                            [
                                ('Trajeto:',            1, 0, '#CEF1F5', 'left', 'black', 'Courier New', ifontlen, True, False),
                                (sdesotra,   icolspan - 1, 0, None,      'left', 'black', 'Courier New', ifontlen, True, False),
                            ]
                        )
                        abnf_imprime_info_001(sarquwri, None, None, 1,
                            [
                                ('Sentido:',            1, 0, '#CEF1F5', 'left', 'black', 'Courier New', ifontlen, True, False),
                                (sdessent,   icolspan - 1, 0, None,      'left', 'black', 'Courier New', ifontlen, True, False),
                            ]
                        )
                        abnf_imprime_line(sarquwri, icolspan, 'brown')
                        abnf_imprime_info_001(sarquwri, None, None, 1,
                            [
                                ('Ordem',       1, 0, '#F5DBCE', 'center', 'black', 'Courier New', ifontlen, True, False),
                                ('Tipo',        1, 0, '#F5DBCE', 'center', 'black', 'Courier New', ifontlen, True, False),
                                ('Logradouro',  1, 0, '#F5DBCE', 'center', 'black', 'Courier New', ifontlen, True, False),
                                ('Complemento', 1, 0, '#F5DBCE', 'center', 'black', 'Courier New', ifontlen, True, False),
                                ('Bairro',      1, 0, '#F5DBCE', 'center', 'black', 'Courier New', ifontlen, True, False),
                                ('Cidade',      1, 0, '#F5DBCE', 'center', 'black', 'Courier New', ifontlen, True, False),
                                ('Estado',      1, 0, '#F5DBCE', 'center', 'black', 'Courier New', ifontlen, True, False),
                                ('Destaque',    1, 0, '#F5DBCE', 'center', 'black', 'Courier New', ifontlen, True, False),
                            ]
                        )
                        # ///////////
                        # Logradouros
                        # ///////////
                        icontlog = 0
                        for lauxi001 in litinera:
                            icontlog += 1
                            iordemit = lauxi001[0]
                            iidlogra = lauxi001[1]
                            scomplem = lauxi001[2]
                            bdestaqu = lauxi001[3]
                            # /// #
                            sordemit = str(1000 + iordemit)[1:]
                            lidlogra = didlogra.get(iidlogra, ('', '', '', '', '', '')) if iidlogra != None and iidlogra > 0 else ('', '', '', '', '', '')
                            stiplogr = lidlogra[1]
                            sdeslogr = lidlogra[2]
                            sdesbair = lidlogra[3]
                            sdescida = lidlogra[4]
                            sdesesta = lidlogra[5]
                            sdestaqu = '&#128307;' if bdestaqu else ''
                            # /// #
                            abnf_imprime_info_001(sarquwri, None, None, 1,
                                [
                                    (sordemit, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                                    (stiplogr, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                                    (sdeslogr, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                                    (scomplem, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                                    (sdesbair, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                                    (sdescida, 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                                    (sdesesta, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                                    (sdestaqu, 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                                ]
                            )
                        abnf_imprime_line(sarquwri, icolspan, 'black')   
                        abnf_imprime_info_001(sarquwri, None, None, 1,
                            [
                                ('Quantidade de logradouros:',                icolspan - 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                                (abnf_formata_numero_milhar_decimal(icontlog, True, 0),  1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                            ]
                        )
            # //////////////////
            # Fim dos relatórios
            # //////////////////
            abnf_imprime_ftbody_ftable_fform_fbody(sarquwri)
        abnf_socket_004([7, sarqurel])
        abnf_socket_004([5, 'btgerrel'])
        abnf_alert('Relatório gerado com sucesso!', 3)
        time.sleep(5)
        abnf_alert('', 0)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #