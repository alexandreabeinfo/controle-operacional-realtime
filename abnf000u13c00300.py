## ========================================================
## [abnf000u13c00300.py] - Operacional - Cadastro de Linhas
## ========================================================

from abnfsrc.abnf000u00s00003 import *              # Arquivo de funções comuns que serão utilizadas por todos os módulos do sistema
from abnfsrc.abnf000u00s00004 import *              # Arquivo de banco de dados

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00300_operacional_cadastro_linhas ] ///////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Linhas.                                                                                                                   // #
# // Form inicial.                                                                                                                                       // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00300_operacional_cadastro_linhas(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00300_operacional_cadastro_linhas(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, '13C00301A'])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        lidolinh = abnf_database_menu(icodbase, iidfilia, 'L', '1303', 1, 1, 1)
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
            ('div-0', 'w-50 p-3', 'background-color: #eee;', None),
            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
            ('legend-0', 'Operacional - Cadastro de Linhas'),
            ('hr-0', None),
            ('label-0',  'Linha', 'form-control-label'),
            ('select-0', 'iidolinh', 'form-control', '16px', 'btbusreg', lidolinh, 1, None, False),
            ('hr-0', None),
            ('button-0', 'btbusreg', 'btn btn-primary mt-2', 'Buscar'),
            ('alt255-0', 2),
            ('button-0', 'btnovreg', 'btn btn-primary mt-2', 'Novo registro'),
            ('alt255-0', 2),
            ('button-0', 'btrelcad', 'btn btn-primary mt-2', 'Relação de linhas'),
            ('alt255-0', 2),
            ('button-0', 'btrelvei', 'btn btn-primary mt-2', 'Relação de veículos'),
            ('form-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
        ]
        snewpage = abnf_create_page(lnewpage)
        abnf_socket_004([1, 'abnfdv03', snewpage])
        
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00301_operacional_cadastro_linhas ] ///////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Linhas.                                                                                                                   // #
# // Form de cadastro/alteração da linha.                                                                                                                // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00301_operacional_cadastro_linhas(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00301_operacional_cadastro_linhas(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        if dabnfopg['abnfobj0'] == ['btbusreg', 'btbusreg']:        # Buscar registro existente
            lmfields = [
                ['iidolinh', 'input', 'F', 'linha', ['Notnull', 'D'], None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btbusreg')
            # Debug: (inicio)
            # abnf_show('08', lmfields, 1)
            # abnf_show('09', dabnfopg, 2)
            # abnf_show('10', dglobaux, 2)
            # Debug: (fim)
            if bvalidad:
                iidolinh = int(dabnfopg['iidolinh'][2])
                # ////////////////////////////////////////////////
                # Buscando a linha caso seja um registro existente
                # ////////////////////////////////////////////////
                lcamposb = ('codolin', 'desolin', 'idogrli', 'qtporve', 'perqtpd', 'perveca', 'pervesa', 'situreg')
                lfilbusc = (('idolinh', '=', iidolinh), ('situreg', '!=', 'C'))
                lorderby = None
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_linhas', lcamposb, lfilbusc, lorderby)
                if lsqlre01 == [] or iqtdre01 == 0:
                    abnf_alert('A linha não foi encontrada!', 4)
                else:
                    scodolin = lsqlre01[0][0]
                    sdesolin = lsqlre01[0][1]
                    iidogrli = lsqlre01[0][2]
                    iqtporve = lsqlre01[0][3]
                    bperqtpd = lsqlre01[0][4]
                    bperveca = lsqlre01[0][5]
                    bpervesa = lsqlre01[0][6]
                    ssitureg = lsqlre01[0][7]
                    # Debug: (inicio)
                    # abnf_show('10', lsqlre01, 1)
                    # Debug: (fim)
                    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidolinh', iidolinh),)])      # ==> Guardando o ID do registro. Obs: tem que ter essa vírgula: "),)])"
                    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '13C00302A'),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
                    lidogrli = abnf_database_menu(icodbase, iidfilia, 'L', '1302', 1, 1, 2)
                    lnewpage = [
                        ('div-0', 'container', None, None),
                        ('hr-0', None),
                        ('div-0', 'row', None, None),
                        ('div-0', 'col d-flex justify-content-center', None, None),
                        ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                        ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                        ('legend-0', 'Operacional - Cadastro de Linhas - [ Registro existente ]'),
                        ('hr-0', None),
                        ('label-0',  'Código da linha', 'form-control-label'),
                        ('input-0',  'scodolin', 'form-control', 0, 20, '16px', scodolin, 'sdesolin', True, 0),
                        ('label-0',  'Descrição da linha', 'form-control-label'),
                        ('input-0',  'sdesolin', 'form-control', 0, 50, '16px', sdesolin, 'iidogrli', True, 0),
                        ('label-0',  'Grupo de linha', 'form-control-label'),
                        ('select-0', 'iidogrli', 'form-control', '16px', 'iqtporve', lidogrli, 1, iidogrli, False),
                        ('label-0',  'Quantidade padrão de portas dos veículos da linha', 'form-control-label'),
                        ('number-0', 'iqtporve', 'form-control', 0, 10, '16px', iqtporve, 'ssitureg', True, None),
                        ('hr-0', None),
                        ('checkbox-0', 'bperqtpd', 1, (1 if bperqtpd else 0), 'Courier New', '16px', 'b', 'P', 'Permite veículos com quantidade de portas divergente do padrão'),
                        ('checkbox-0', 'bperveca', 1, (1 if bperveca else 0), 'Courier New', '16px', 'b', 'P', 'Permite veículos com ar-condicionado'),
                        ('checkbox-0', 'bpervesa', 1, (1 if bpervesa else 0), 'Courier New', '16px', 'b', 'P', 'Permite veículos sem ar-condicionado'),
                        ('hr-0', None),
                        ('label-0',  'Situação do registro', 'form-control-label'),
                        ('select-0', 'ssitureg', 'form-control', '16px', 'btmodsav', abnf_personal_retorna_lista(10001), 0, ssitureg, False),
                        ('hr-0', None),
                        ('alt255-0', 1),
                        ('button-1', 'btmodsav', 'btn btn-primary mt-2', 'Salvar', 'Salvar Registro', 'btsalreg', 'btn btn-primary mt-2', 'Salvar', 'Confirma a gravação das alterações?'),
                        ('alt255-0', 2),
                        ('button-1', 'btexclui', 'btn btn-primary mt-2', 'Excluir', 'Excluir Registro', 'btexcreg', 'btn btn-danger mt-2', 'Excluir', 'Confirma a exclusão deste registro?'),
                        ('alt255-0', 2),
                        ('button-0', 'btcancel', 'btn btn-primary mt-2', 'Cancelar'),
                        ('alt255-0', 1),
                        ('form-9', None),
                        ('div-9', None),
                        ('div-9', None),
                        ('div-9', None),
                        ('div-9', None),
                    ]
                    snewpage = abnf_create_page(lnewpage)
                    abnf_socket_004([1, 'abnfdv03', snewpage])
                    # Debug: (inicio)
                    # abnf_show('08', lsqlre01[0][5], 0)
                    # abnf_show('09', lnewpage, 1)
                    # Debug: (fim)                    
        elif dabnfopg['abnfobj0'] == ['btnovreg', 'btnovreg']:      # Novo registro
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidolinh', 0),)])             # ==> Indicativo para dizer que é novo registro. Obs: tem que ter essa vírgula: "),)])"
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '13C00302A'),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
            lidogrli = abnf_database_menu(icodbase, iidfilia, 'L', '1302', 1, 1, 2)
            lnewpage = [
                ('div-0', 'container', None, None),
                ('hr-0', None),
                ('div-0', 'row', None, None),
                ('div-0', 'col d-flex justify-content-center', None, None),
                ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                ('legend-0', 'Operacional - Cadastro de Linhas - [ Novo registro ]'),
                ('hr-0', None),
                ('label-0',  'Código da linha', 'form-control-label'),
                ('input-0',  'scodolin', 'form-control', 0, 20, '16px', None, 'sdesolin', True, 0),
                ('label-0',  'Descrição da linha', 'form-control-label'),
                ('input-0',  'sdesolin', 'form-control', 0, 50, '16px', None, 'iidogrli', True, 0),
                ('label-0',  'Grupo de linha', 'form-control-label'),
                ('select-0', 'iidogrli', 'form-control', '16px', 'iqtporve', lidogrli, 1, None, False),
                ('label-0',  'Quantidade padrão de portas dos veículos da linha', 'form-control-label'),
                ('number-0', 'iqtporve', 'form-control', 0, 10, '16px', None, 'btmodsav', True, None),
                ('hr-0', None),
                ('checkbox-0', 'bperqtpd', 1, (1 if bperqtpd else 0), 'Courier New', '16px', 'b', 'P', 'Permite veículos com quantidade de portas divergente do padrão'),
                ('checkbox-0', 'bperveca', 1, (1 if bperveca else 0), 'Courier New', '16px', 'b', 'P', 'Permite veículos com ar-condicionado'),
                ('checkbox-0', 'bpervesa', 1, (1 if bpervesa else 0), 'Courier New', '16px', 'b', 'P', 'Permite veículos sem ar-condicionado'),
                ('hr-0', None),
                ('alt255-0', 1),
                ('button-1', 'btmodsav', 'btn btn-primary mt-2', 'Salvar', 'Salvar Registro', 'btsalreg', 'btn btn-primary mt-2', 'Salvar', 'Confirma a gravação do novo registro?'),
                ('alt255-0', 2),
                ('button-0', 'btcancel', 'btn btn-primary mt-2', 'Cancelar'),
                ('alt255-0', 1),
                ('form-9', None),
                ('div-9', None),
                ('div-9', None),
                ('div-9', None),
                ('div-9', None),
            ]
            snewpage = abnf_create_page(lnewpage)
            abnf_socket_004([1, 'abnfdv03', snewpage])
            # Debug: (inicio)
            # abnf_socket_004([3, 'scodolin', '150'])
            # abnf_socket_004([3, 'sdesolin', 'TESTE'])
            # Debug: (fim)
        elif dabnfopg['abnfobj0'] == ['btrelcad', 'btrelcad']:      # Relação das linhas
            abnf000u13c00303_operacional_cadastro_linhas(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btrelvei', 'btrelvei']:      # Relação das veículos
            abnf000u13c00304_operacional_cadastro_linhas(dabnfopg)
            
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00302_operacional_cadastro_linhas ] ///////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Linhas.                                                                                                                   // #
# // Gravação dos registros e geração de log.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00302_operacional_cadastro_linhas(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00302_operacional_cadastro_linhas(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        if dabnfopg['abnfobj0'] == ['btcancel', 'btcancel']:        # Voltar para tela anterior
            abnf000u13c00300_operacional_cadastro_linhas(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btsalreg', 'btsalreg']:      # Salvar o registro
            iidolinh = dglobaux['iidolinh']
            lmfields = [
                ['scodolin', 'input',    'M', 'código da linha',                                   ['Notnull', 'D'],            None],
                ['sdesolin', 'input',    'F', 'descrição da linha',                                ['Notnull', 'D'],            None],
                ['iidogrli', 'select',   'M', 'grupo de linha',                                    ['Notnull', 'D'],            None],
                ['iqtporve', 'number',   'F', 'quantidade padrão de portas dos veículos da linha', ['Notnull', 'D', 'Notzero'], None],
                ['bperqtpd', 'checkbox', 'M', 'permite...',                                        [],                          None],
                ['bperveca', 'checkbox', 'M', 'permite...',                                        [],                          None],
                ['bpervesa', 'checkbox', 'M', 'permite...',                                        [],                          None],
            ]
            if iidolinh > 0: lmfields = lmfields + [
                ['ssitureg', 'select',   'F', 'situação do registro', ['Notnull', 'D'], None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btsalreg')
            # Debug: (inicio)
            # abnf_show('10', lmfields, 1)
            # abnf_show('09', dabnfopg, 2)
            # abnf_show('10', dglobaux, 0)
            # Debug: (fim)
            if bvalidad:
                icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
                iidfilia = dglobaux['iidfilia']
                if iidolinh == 0:   # Novo registro
                    lcamposb = ('codolin', 'idolinh')
                    lfilbusc = (('codolin', '=', lmfields[0][5]), ('situreg', '!=', 'C'))
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_linhas', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 != [] or iqtdre01 != 0:
                        abnf_alert('Não foi possível salvar! O código ' + str(lmfields[0][5]) + ' já está sendo utilizado em outro registro!', 4)
                    else:
                        bvalidad, iproxiid = abnf_database_insere_dados_v02(icodbase, sabnproj, 'abnf_operacional_cadastro_linhas', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                        [
                            ('codolin', lmfields[0][5]),
                            ('desolin', lmfields[1][5]),
                            ('idogrli', lmfields[2][5]),
                            ('qtporve', lmfields[3][5]),
                            ('perqtpd', lmfields[4][5]),
                            ('perveca', lmfields[5][5]),
                            ('pervesa', lmfields[6][5]),
                            ('idfilia', iidfilia),
                            ('situreg', 'A'),
                        ])
                        if bvalidad:
                            abnf_alert('Nova linha gravada com sucesso!', 3)
                            abnf000u13c00300_operacional_cadastro_linhas(dabnfopg)
                elif iidolinh > 0:  # Registro existente
                    lcamposb = ('codolin', 'idolinh')
                    lfilbusc = (('codolin', '=', lmfields[0][5]), ('situreg', '!=', 'C'), ('idolinh', '!=', iidolinh))
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_linhas', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 != [] or iqtdre01 != 0:
                        abnf_alert('Não foi possível salvar! O código ' + str(lmfields[0][5]) + ' já está sendo utilizado em outro registro!', 4)
                    else:
                        bvalidad = abnf_database_altera_dados_v02(icodbase, sabnproj, 'abnf_operacional_cadastro_linhas', iidolinh, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                        [
                            ('codolin', lmfields[0][5]),
                            ('desolin', lmfields[1][5]),
                            ('idogrli', lmfields[2][5]),
                            ('qtporve', lmfields[3][5]),
                            ('perqtpd', lmfields[4][5]),
                            ('perveca', lmfields[5][5]),
                            ('pervesa', lmfields[6][5]),
                            ('situreg', lmfields[7][5]),
                        ])
                        if bvalidad:
                            abnf_alert('Registro alterado com sucesso!', 3)
                            abnf000u13c00300_operacional_cadastro_linhas(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btexcreg', 'btexcreg']:      # Excluir registro
            iidolinh = dglobaux['iidolinh']        
            icodbase = int(dabnfopg['abnproje'][2][14:]) * 100      # Código do banco de dados a ser utilizado
            bvalidad = abnf_database_exclui_registro(icodbase, sabnproj, 'abnf_operacional_cadastro_linhas', iidolinh, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'])
            if bvalidad:
                abnf_alert('Registro excluído com sucesso!', 3)
                abnf000u13c00300_operacional_cadastro_linhas(dabnfopg)
                
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00303_operacional_cadastro_linhas ] ///////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Linhas.                                                                                                                   // #
# // Relatório de linhas.                                                                                                                                // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
                
def abnf000u13c00303_operacional_cadastro_linhas(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00303_operacional_cadastro_linhas(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        # abnf_show('10', dglobaux, 2)
        iidfilia = dglobaux['iidfilia']
        # /////////////////////
        # Variaveis de ambiente
        # /////////////////////
        icolspan = 7
        ifontlen = 2
        icontreg = 0
        # ////////////////////
        # Listas e dicionários
        # ////////////////////
        drelgrli = abnf_database_menu(icodbase, iidfilia, 'D', '1302', 1, 1, 2)
        # ///////////////////
        # Gerando o relatório
        # ///////////////////
        sarqurel = abnf_imprime_file(0, sabntoke)
        with open('abnftmp/' + sarqurel, 'w') as sarquwri:
            snomeemp, snomefil = abnf_database_retorna_empresa_filial(icodbase, iidfilia)
            abnf_imprime_doctype_head_fhead_body_form_table_thead(sarquwri, 3)
            abnf_imprime_thead_001_abeinfo_sistemas(sarquwri, icolspan)
            abnf_imprime_thead_002_titulo_relatorio(sarquwri, icolspan, 'RELAÇÃO DE LINHAS')
            abnf_imprime_thead_003_empresa_filial(sarquwri, icolspan, snomeemp, snomefil)
            # smensage = 'Per&iacute;odo: ' + abnf_converte_data(ddataini) + ' &agrave;s ' + abnf_converte_hora(thoraini) + ' at&eacute; ' + abnf_converte_data(ddatafim) + ' &agrave;s ' + abnf_converte_hora(thorafim)
            # abnf_imprime_thead_004_parametros(sarquwri, icolspan, smensage)
            abnf_imprime_thead_005_datetime(sarquwri, icolspan)
            abnf_imprime_line(sarquwri, icolspan, 'darkcyan')
            abnf_imprime_info_001(sarquwri, '#D1C5C5', 'center', 1,
                [
                    ('Código',             1, 2, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Descrição',          1, 2, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Grupo de linha',     1, 2, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Permite',            3, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Situação',           1, 2, None, None, 'black', 'Courier New', ifontlen, True, False),
                ]
            )
            abnf_imprime_info_001(sarquwri, '#D1C5C5', 'center', 1,
                [
                    ('Portas divergentes', 1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Veículos com ar',    1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Veículos sem ar',    1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                ]
            )
            abnf_imprime_fthead_tbody(sarquwri)
            lcamposb = ('codolin', 'desolin', 'idogrli', 'perqtpd', 'perveca', 'pervesa', 'situreg')
            lfilbusc = (('situreg', '!=', 'C'), ('idfilia', '=', iidfilia), None)
            lorderby = ('codolin', 'idolinh')
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_linhas', lcamposb, lfilbusc, lorderby)
            for lauxi001 in lsqlre01:
                
                sdesgrli = drelgrli.get(lauxi001[2], '')
                sperqtpd = 'Sim' if lauxi001[3] else 'Não'
                sperveca = 'Sim' if lauxi001[4] else 'Não'
                spervesa = 'Sim' if lauxi001[5] else 'Não'
                ssitureg = abnf_personal_retorna_string(10001, lauxi001[6])
                icontreg += 1
                abnf_imprime_info_001(sarquwri, None, None, 1,
                    [
                        (lauxi001[0], 1, 0, None, 'Center'  , 'black', 'Courier New', ifontlen, True, False),
                        (lauxi001[1], 1, 0, None, 'Left'    , 'black', 'Courier New', ifontlen, True, False),
                        (sdesgrli,    1, 0, None, 'Left'    , 'black', 'Courier New', ifontlen, True, False),
                        (sperqtpd,    1, 0, None, 'Center'  , 'black', 'Courier New', ifontlen, True, False),
                        (sperveca,    1, 0, None, 'Center'  , 'black', 'Courier New', ifontlen, True, False),
                        (spervesa,    1, 0, None, 'Center'  , 'black', 'Courier New', ifontlen, True, False),
                        (ssitureg,    1, 0, None, 'Center'  , 'black', 'Courier New', ifontlen, True, False),
                    ]
                )
            abnf_imprime_line(sarquwri, icolspan, 'darkcyan')
            abnf_imprime_info_001(sarquwri, None, None, 1,
                [
                    ('Total de registros impressos:', icolspan - 1, 0, None, 'Left'  , 'black', 'Courier New', ifontlen, True, False),
                    (icontreg,                                   1, 0, None, 'Right' , 'black', 'Courier New', ifontlen, True, False),
                ]
            )
            abnf_imprime_ftbody_ftable_fform_fbody(sarquwri)
        abnf_socket_004([7, sarqurel])
        abnf_socket_004([5, 'btrelcad'])
        abnf_alert('Relatório gerado com sucesso!', 3)
        time.sleep(5)
        abnf_alert('', 0)
        
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00304_operacional_cadastro_linhas ] ///////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Linhas.                                                                                                                   // #
# // Relatório de veículos.                                                                                                                              // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
                
def abnf000u13c00304_operacional_cadastro_linhas(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00304_operacional_cadastro_linhas(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        # abnf_show('10', dglobaux, 2)
        iidfilia = dglobaux['iidfilia']
        # /////////////////////
        # Variaveis de ambiente
        # /////////////////////
        icolspan = 5
        ifontlen = 2
        icontreg = 0
        # ////////////////////
        # Listas e dicionários
        # ////////////////////
        # ///////////////////
        # Gerando o relatório
        # ///////////////////
        sarqurel = abnf_imprime_file(0, sabntoke)
        with open('abnftmp/' + sarqurel, 'w') as sarquwri:
            snomeemp, snomefil = abnf_database_retorna_empresa_filial(icodbase, iidfilia)
            abnf_imprime_doctype_head_fhead_body_form_table_thead(sarquwri, 3)
            abnf_imprime_thead_001_abeinfo_sistemas(sarquwri, icolspan)
            abnf_imprime_thead_002_titulo_relatorio(sarquwri, icolspan, 'RELAÇÃO DE VEÍCULOS')
            abnf_imprime_thead_003_empresa_filial(sarquwri, icolspan, snomeemp, snomefil)
            # smensage = 'Per&iacute;odo: ' + abnf_converte_data(ddataini) + ' &agrave;s ' + abnf_converte_hora(thoraini) + ' at&eacute; ' + abnf_converte_data(ddatafim) + ' &agrave;s ' + abnf_converte_hora(thorafim)
            # abnf_imprime_thead_004_parametros(sarquwri, icolspan, smensage)
            abnf_imprime_thead_005_datetime(sarquwri, icolspan)
            abnf_imprime_line(sarquwri, icolspan, 'darkcyan')
            abnf_imprime_info_001(sarquwri, '#D1C5C5', 'center', 1,
                [
                    ('Prefixo',         1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Placa',           1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Nº de portas',    1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Ar condicionado', 1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Situação',        1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                ]
            )
            abnf_imprime_fthead_tbody(sarquwri)
            lcamposb = ('prefvei', 'placave', 'numport', 'arcondi', 'situreg')
            lfilbusc = (('situreg', '!=', 'C'), ('idfilia', '=', iidfilia), None)
            lorderby = ('prefvei', None)
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_veiculos', lcamposb, lfilbusc, lorderby)
            for lauxi001 in lsqlre01:
                sarcondi = 'Sim' if lauxi001[3] else 'Não'
                ssitureg = abnf_personal_retorna_string(10001, lauxi001[4])
                icontreg += 1
                abnf_imprime_info_001(sarquwri, None, None, 1,
                    [
                        (lauxi001[0], 1, 0, None, 'Center', 'black', 'Courier New', ifontlen, True, False),
                        (lauxi001[1], 1, 0, None, 'Center', 'black', 'Courier New', ifontlen, True, False),
                        (lauxi001[2], 1, 0, None, 'Center', 'black', 'Courier New', ifontlen, True, False),
                        (sarcondi,    1, 0, None, 'Center', 'black', 'Courier New', ifontlen, True, False),
                        (ssitureg,    1, 0, None, 'Center', 'black', 'Courier New', ifontlen, True, False),
                    ]
                )
            abnf_imprime_line(sarquwri, icolspan, 'darkcyan')
            abnf_imprime_info_001(sarquwri, None, None, 1,
                [
                    ('Total de registros impressos:', icolspan - 1, 0, None, 'Left'  , 'black', 'Courier New', ifontlen, True, False),
                    (icontreg,                                   1, 0, None, 'Right' , 'black', 'Courier New', ifontlen, True, False),
                ]
            )
            abnf_imprime_ftbody_ftable_fform_fbody(sarquwri)
        abnf_socket_004([7, sarqurel])
        abnf_socket_004([5, 'btrelvei'])
        abnf_alert('Relatório gerado com sucesso!', 3)
        time.sleep(5)
        abnf_alert('', 0)
                    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #