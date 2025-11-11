## ==========================================================
## [abnf000u13c00500.py] - Operacional - Cadastro de Trajetos
## ==========================================================

from abnfsrc.abnf000u00s00003 import *              # Arquivo de funções comuns que serão utilizadas por todos os módulos do sistema
from abnfsrc.abnf000u00s00004 import *              # Arquivo de banco de dados

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00500_operacional_cadastro_trajetos ] /////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Trajetos.                                                                                                                 // #
# // Form inicial.                                                                                                                                       // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00500_operacional_cadastro_trajetos(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00500_operacional_cadastro_trajetos(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, '13C00501A'])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        lidotraj = abnf_database_menu(icodbase, (iidfilia, None, None), 'L', '1305A', 1, None, None)
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
            ('legend-0', 'Operacional - Cadastro de Trajetos'),
            ('hr-0', None),
            ('label-0',  'Projeto - Linha - Trajeto', 'form-control-label'),
            ('select-0', 'iidotraj', 'form-control', '16px', 'btbusreg', lidotraj, 1, None, False),
            ('hr-0', None),
            ('button-0', 'btbusreg', 'btn btn-primary mt-2', 'Buscar'),
            ('alt255-0', 2),
            ('button-0', 'btnovreg', 'btn btn-primary mt-2', 'Novo registro'),
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
# // [ abnf000u13c00501_operacional_cadastro_trajetos ] /////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Trajetos.                                                                                                                 // #
# // Form de cadastro/alteração do trajeto.                                                                                                              // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00501_operacional_cadastro_trajetos(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00501_operacional_cadastro_trajetos(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        if dabnfopg['abnfobj0'] == ['btbusreg', 'btbusreg']:        # Buscar registro existente
            lmfields = [
                ['iidotraj', 'input', 'M', 'trajeto', ['Notnull', 'D', 'Return_integer'], None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btbusreg')
            # Debug: (inicio)
            # abnf_show('08', lmfields, 1)
            # abnf_show('09', dabnfopg, 2)
            # abnf_show('10', dglobaux, 2)
            # Debug: (fim)
            if bvalidad:
                iidotraj = lmfields[0][5]
                # //////////////////////////////////////////////////
                # Buscando o trajeto caso seja um registro existente
                # //////////////////////////////////////////////////
                lcamposb = ('idoproj', 'idolinh', 'codotra', 'desotra', 'kmidaxx', 'kmvolta', 'situreg')
                lfilbusc = (('idotraj', '=', iidotraj), ('situreg', '!=', 'C'))
                lorderby = None
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_trajetos', lcamposb, lfilbusc, lorderby)
                if lsqlre01 == [] or iqtdre01 == 0:
                    abnf_alert('O trajeto não foi encontrado!', 4)
                    abnf_socket_004([5, 'btbusreg'])
                else:
                    # Debug: (inicio)
                    # abnf_show('10', lsqlre01, 1)
                    # Debug: (fim)
                    iidoproj = lsqlre01[0][0]
                    iidolinh = lsqlre01[0][1]
                    scodotra = lsqlre01[0][2]
                    sdesotra = lsqlre01[0][3]
                    skmidaxx = abnf_formata_numero_milhar_decimal(lsqlre01[0][4], True, 1)
                    skmvolta = abnf_formata_numero_milhar_decimal(lsqlre01[0][5], True, 1)
                    ssitureg = lsqlre01[0][6]
                    sdesopro = abnf_database_find(icodbase, None, '013B', iidoproj, None)
                    sdesolin = abnf_database_find(icodbase, None, '013A', iidolinh, None)
                    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidotraj', iidotraj),)])      # ==> Guardando o ID do registro do trajeto. Obs: tem que ter essa vírgula: "),)])"
                    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidoproj', iidoproj),)])      # ==> Guardando o ID do registro do projeto. Obs: tem que ter essa vírgula: "),)])"
                    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidolinh', iidolinh),)])      # ==> Guardando o ID do registro da linha. Obs: tem que ter essa vírgula: "),)])"
                    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '13C00502A'),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
                    lnewpage = [
                        ('div-0', 'container', None, None),
                        ('hr-0', None),
                        ('div-0', 'row', None, None),
                        ('div-0', 'col d-flex justify-content-center', None, None),
                        ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                        ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                        ('legend-0', 'Operacional - Cadastro de Trajetos - [ Registro existente ]'),
                        ('hr-0', None),
                        ('label-0',  'Projeto', 'form-control-label'),
                        ('input-0',  'sdesopro', 'form-control', 0, 50, '16px', sdesopro, 'sdesolin', False, 0),
                        ('label-0',  'Linha', 'form-control-label'),
                        ('input-0',  'sdesolin', 'form-control', 0, 50, '16px', sdesolin, 'scodotra', False, 0),
                        ('label-0',  'Código do trajeto', 'form-control-label'),
                        ('input-0',  'scodotra', 'form-control', 0, 4, '16px', scodotra, 'sdesotra', True, 0),
                        ('label-0',  'Descrição do trajeto', 'form-control-label'),
                        ('input-0',  'sdesotra', 'form-control', 0, 200, '16px', sdesotra, 'nkmidaxx', True, 0),
                        ('label-0',  'Km ida', 'form-control-label'),
                        ('thscom-0', 'nkmidaxx', 'form-control', 0, 8, '16px', skmidaxx, 'nkmvolta', 1, True, 2, None), ('td-9', None),
                        ('label-0',  'Km volta', 'form-control-label'),
                        ('thscom-0', 'nkmvolta', 'form-control', 0, 8, '16px', skmvolta, 'ssitureg', 1, True, 2, None), ('td-9', None),
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
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidotraj', 0),)])             # ==> Indicativo para dizer que é novo registro. Obs: tem que ter essa vírgula: "),)])"
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '13C00502A'),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
            lidoproj = abnf_database_menu(icodbase, iidfilia, 'L', '1304', 1, 2, 2)
            lidolinh = abnf_database_menu(icodbase, iidfilia, 'L', '1303', 1, 2, 2)
            lnewpage = [
                ('div-0', 'container', None, None),
                ('hr-0', None),
                ('div-0', 'row', None, None),
                ('div-0', 'col d-flex justify-content-center', None, None),
                ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                ('legend-0', 'Operacional - Cadastro de Trajetos - [ Novo registro ]'),
                ('hr-0', None),
                ('label-0',  'Projeto', 'form-control-label'),
                ('select-0', 'iidoproj', 'form-control', '16px', 'iidolinh', lidoproj, 1, None, False),
                ('label-0',  'Linha', 'form-control-label'),
                ('select-0', 'iidolinh', 'form-control', '16px', 'scodotra', lidolinh, 1, None, False),
                ('label-0',  'Código do trajeto', 'form-control-label'),
                ('input-0',  'scodotra', 'form-control', 0, 4, '16px', None, 'sdesotra', True, 0),
                ('label-0',  'Descrição do trajeto', 'form-control-label'),
                ('input-0',  'sdesotra', 'form-control', 0, 200, '16px', None, 'nkmidaxx', True, 0),
                ('label-0',  'Km ida', 'form-control-label'),
                ('thscom-0', 'nkmidaxx', 'form-control', 0, 8, '16px', '0,0', 'nkmvolta', 1, True, 2, None), ('td-9', None),
                ('label-0',  'Km volta', 'form-control-label'),
                ('thscom-0', 'nkmvolta', 'form-control', 0, 8, '16px', '0,0', 'btmodsav', 1, True, 2, None), ('td-9', None),
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
            # abnf_socket_004([3, 'scodotra', '150'])
            # abnf_socket_004([3, 'sdesotra', 'TESTE'])
            # Debug: (fim)
        elif dabnfopg['abnfobj0'] == ['btrelcad', 'btrelcad']:      # Relação dos trajetos cadastrados
            abnf000u13c00503_operacional_cadastro_trajetos(dabnfopg)
            
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00502_operacional_cadastro_trajetos ] /////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Trajetos.                                                                                                                 // #
# // Gravação dos registros e geração de log.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00502_operacional_cadastro_trajetos(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00502_operacional_cadastro_trajetos(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        if dabnfopg['abnfobj0'] == ['btcancel', 'btcancel']:        # Voltar para tela anterior
            abnf000u13c00500_operacional_cadastro_trajetos(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btsalreg', 'btsalreg']:      # Salvar o registro
            iidotraj = dglobaux['iidotraj']
            lmfields = []
            if iidotraj == 0: lmfields = lmfields + [
                ['iidoproj', 'select', 'F', 'linha',                ['Notnull',  'D', 'Return_integer'], None],
                ['iidolinh', 'select', 'F', 'linha',                ['Notnull',  'D', 'Return_integer'], None],
            ]
            lmfields = lmfields + [
                ['scodotra', 'input',  'M', 'código do trajeto',    ['Notempty', 'D'                  ], None],
                ['sdesotra', 'input',  'F', 'descrição do trajeto', ['Notnull',  'D'                  ], None],
                ['nkmidaxx', 'thscom', 'M', 'km ida',               ['Notempty', 'D', '>=0'           ], None],
                ['nkmvolta', 'thscom', 'M', 'km volta',             ['Notempty', 'D', '>=0'           ], None],
            ]
            if iidotraj > 0: lmfields = lmfields + [
                ['ssitureg', 'select', 'F', 'situação do registro', ['Notnull', 'D'                   ], None],
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
                if iidotraj == 0:   # Novo registro
                    if abnf_database_registro_nao_ativo(icodbase, 'abnf_operacional_cadastro_linhas', lmfields[1][5], 'F', 'linha', ('desolin', 'codolin')): pass
                    else:
                        lcamposb = ('idoproj', 'idolinh', 'codotra')
                        lfilbusc = (('idoproj', '=', lmfields[0][5]), ('idolinh', '=', lmfields[1][5]), ('codotra', '=', lmfields[2][5]), ('situreg', '!=', 'C'))
                        lorderby = None
                        lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_trajetos', lcamposb, lfilbusc, lorderby)
                        if lsqlre01 != [] or iqtdre01 != 0:
                            abnf_alert('Não foi possível salvar! O código de trajeto "' + str(lmfields[1][5]) + '" já está sendo utilizado em outro registro deste projeto-linha!', 4)
                        else:
                            bvalidad, iproxiid = abnf_database_insere_dados_v02(icodbase, sabnproj, 'abnf_operacional_cadastro_trajetos', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                            [
                                ('idoproj', lmfields[0][5]),
                                ('idolinh', lmfields[1][5]),
                                ('codotra', lmfields[2][5]),
                                ('desotra', lmfields[3][5]),
                                ('kmidaxx', lmfields[4][5]),
                                ('kmvolta', lmfields[5][5]),
                                ('situreg', 'A'),
                            ])
                            if bvalidad:
                                abnf_alert('Novo trajeto gravado com sucesso!', 3)
                                abnf000u13c00500_operacional_cadastro_trajetos(dabnfopg)
                elif iidotraj > 0:  # Registro existente
                    iidoproj = dglobaux['iidoproj']
                    iidolinh = dglobaux['iidolinh']
                    lcamposb = ('idoproj', 'idolinh', 'codotra')
                    lfilbusc = (('idoproj', '=', iidoproj), ('idolinh', '=', iidolinh), ('codotra', '=', lmfields[0][5]), ('idotraj', '!=', iidotraj), ('situreg', '!=', 'C'))
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_trajetos', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 != [] or iqtdre01 != 0:
                        abnf_alert('Não foi possível salvar! O código de trajeto "' + str(lmfields[0][5]) + '" já está sendo utilizado em outro registro deste projeto-linha!', 4)
                    else:
                        bvalidad = abnf_database_altera_dados_v02(icodbase, sabnproj, 'abnf_operacional_cadastro_trajetos', iidotraj, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                        [
                            ('codotra', lmfields[0][5]),
                            ('desotra', lmfields[1][5]),
                            ('kmidaxx', lmfields[2][5]),
                            ('kmvolta', lmfields[3][5]),
                            ('situreg', lmfields[4][5]),
                        ])
                        if bvalidad:
                            abnf_alert('Registro alterado com sucesso!', 3)
                            abnf000u13c00500_operacional_cadastro_trajetos(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btexcreg', 'btexcreg']:      # Excluir registro
            iidotraj = dglobaux['iidotraj']        
            icodbase = int(dabnfopg['abnproje'][2][14:]) * 100      # Código do banco de dados a ser utilizado
            bvalidad = abnf_database_exclui_registro(icodbase, sabnproj, 'abnf_operacional_cadastro_trajetos', iidotraj, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'])
            if bvalidad:
                abnf_alert('Registro excluído com sucesso!', 3)
                abnf000u13c00500_operacional_cadastro_trajetos(dabnfopg)
                
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00503_operacional_cadastro_trajetos ] /////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Trajetos.                                                                                                                 // #
# // Relatório de trajetos.                                                                                                                              // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
                
def abnf000u13c00503_operacional_cadastro_trajetos(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00503_operacional_cadastro_trajetos(dabnfopg)')
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
        drelgrli = abnf_database_menu(icodbase, iidfilia, 'D', '1302', 1, 1, 2)
        # ///////////////////
        # Gerando o relatório
        # ///////////////////
        sarqurel = abnf_imprime_file(0, sabntoke)
        with open('abnftmp/' + sarqurel, 'w') as sarquwri:
            snomeemp, snomefil = abnf_database_retorna_empresa_filial(icodbase, iidfilia)
            abnf_imprime_doctype_head_fhead_body_form_table_thead(sarquwri, 3)
            abnf_imprime_thead_001_abeinfo_sistemas(sarquwri, icolspan)
            abnf_imprime_thead_002_titulo_relatorio(sarquwri, icolspan, 'RELAÇÃO DE TRAJETOS POR LINHA')
            abnf_imprime_thead_003_empresa_filial(sarquwri, icolspan, snomeemp, snomefil)
            # smensage = 'Per&iacute;odo: ' + abnf_converte_data(ddataini) + ' &agrave;s ' + abnf_converte_hora(thoraini) + ' at&eacute; ' + abnf_converte_data(ddatafim) + ' &agrave;s ' + abnf_converte_hora(thorafim)
            # abnf_imprime_thead_004_parametros(sarquwri, icolspan, smensage)
            abnf_imprime_thead_005_datetime(sarquwri, icolspan)
            abnf_imprime_fthead_tbody(sarquwri)
            # ////////
            # Projetos
            # ////////
            lcamposb = ('codopro', 'desopro', 'idoproj')
            lfilbusc = (('situreg', '=', 'A'), ('idfilia', '=', iidfilia), None)
            lorderby = ('codopro', 'idoproj')
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_projetos', lcamposb, lfilbusc, lorderby)
            for lauxi001 in lsqlre01:
                abnf_imprime_line(sarquwri, icolspan, 'black')
                sauxi001 = 'PROJETO: ' + lauxi001[1] + ' (' + str(lauxi001[1]) + ')'
                abnf_imprime_info_001(sarquwri, '#80E083', None, 1, [
                    (sauxi001, icolspan, 0, None, None, 'black', 'Courier New', ifontlen + 1, True, False),
                ])
                # ==> abnf_imprime_line(sarquwri, icolspan, 'green')
                # //////
                # Linhas
                # //////
                lcamposb = ('codolin', 'desolin', 'idolinh')
                lfilbusc = (('situreg', '=', 'A'), ('idfilia', '=', iidfilia), None)
                lorderby = ('codolin', 'idolinh')
                lsqlre02, iqtdre02 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_linhas', lcamposb, lfilbusc, lorderby)
                for lauxi002 in lsqlre02:
                    abnf_imprime_line(sarquwri, icolspan, 'black')
                    sauxi001 = 'LINHA: ' + lauxi002[0] + ' - ' + lauxi002[1]
                    abnf_imprime_info_001(sarquwri, '#E0AA80', None, 1, [
                        (sauxi001, icolspan, 0, None, None, 'black', 'Courier New', ifontlen + 1, True, False),
                    ])
                    abnf_imprime_line(sarquwri, icolspan, 'darkcyan')
                    abnf_imprime_info_001(sarquwri, '#D1C5C5', 'center', 1,
                        [
                            ('Código do trajeto', 1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                            ('Descrição',         1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                            ('Km ida',            1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                            ('Km volta',          1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                            ('Situação',          1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                        ]
                    )
                    # ////////
                    # Trajetos
                    # ////////
                    lcamposb = ('codotra', 'desotra', 'kmidaxx', 'kmvolta', 'situreg')
                    lfilbusc = (('situreg', '!=', 'C'), ('idolinh', '=', lauxi002[2]), None)
                    lorderby = ('codotra', 'idotraj')
                    lsqlre03, iqtdre03 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_trajetos', lcamposb, lfilbusc, lorderby)
                    for lauxi003 in lsqlre03:
                        scodotra = lauxi003[0]
                        sdesotra = lauxi003[1]
                        skmidaxx = abnf_formata_numero_milhar_decimal(lauxi003[2], True, 1)
                        skmvolta = abnf_formata_numero_milhar_decimal(lauxi003[3], True, 1)
                        ssitureg = abnf_personal_retorna_string(10001, lauxi003[4])
                        icontreg += 1
                        abnf_imprime_info_001(sarquwri, None, None, 1,
                            [
                                (scodotra, 1, 0, None, 'Center', 'black', 'Courier New', ifontlen, True, False),
                                (sdesotra, 1, 0, None, 'Left'  , 'black', 'Courier New', ifontlen, True, False),
                                (skmidaxx, 1, 0, None, 'Right' , 'black', 'Courier New', ifontlen, True, False),
                                (skmvolta, 1, 0, None, 'Right' , 'black', 'Courier New', ifontlen, True, False),
                                (ssitureg, 1, 0, None, 'Center', 'black', 'Courier New', ifontlen, True, False),
                            ]
                        )
            abnf_imprime_line(sarquwri, icolspan, 'black')
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
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #