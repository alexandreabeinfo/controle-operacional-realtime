## ========================================================
## [abnf000u13c00100.py] - Operacional - Cadastro de Locais
## ========================================================

from abnfsrc.abnf000u00s00003 import *              # Arquivo de funções comuns que serão utilizadas por todos os módulos do sistema
from abnfsrc.abnf000u00s00004 import *              # Arquivo de banco de dados

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00100_operacional_cadastro_locais ] ///////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Locais.                                                                                                                   // #
# // Form inicial.                                                                                                                                       // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00100_operacional_cadastro_locais(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00100_operacional_cadastro_locais(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, '13C00101A'])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        lidoloca = abnf_database_menu(icodbase, iidfilia, 'L', '1301A', 1, 1, 2)
        # Debug: (inicio)
        # abnf_show('08', iidoloca, 1)
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
            ('legend-0', 'Operacional - Cadastro de Locais'),
            ('hr-0', None),
            ('label-0',  'Local', 'form-control-label'),
            ('select-0', 'iidoloca', 'form-control', '16px', 'btbusreg', lidoloca, 1, None, False),
            ('hr-0', None),
            ('button-0', 'btbusreg', 'btn btn-primary mt-2', 'Buscar'),
            ('alt255-0', 2),
            ('button-0', 'btnovreg', 'btn btn-primary mt-2', 'Novo registro'),
            ('alt255-0', 2),
            ('button-0', 'btrelcad', 'btn btn-primary mt-2', 'Relação de locais cadastrados'),
            ('form-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
        ]
        snewpage = abnf_create_page(lnewpage)
        abnf_socket_004([1, 'abnfdv03', snewpage])
        
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00101_operacional_cadastro_locais ] ///////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Locais.                                                                                                                   // #
# // Form de cadastro/alteração do local.                                                                                                                // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00101_operacional_cadastro_locais(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00101_operacional_cadastro_locais(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        if dabnfopg['abnfobj0'] == ['btbusreg', 'btbusreg']:        # Buscar registro existente
            lmfields = [
                ['iidoloca', 'select', 'M', 'local', ['Notnull', 'D'], None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btbusreg')
            # Debug: (inicio)
            # abnf_show('08', lmfields, 1)
            # abnf_show('09', dabnfopg, 2)
            # abnf_show('10', dglobaux, 2)
            # Debug: (fim)
            if bvalidad:
                iidoloca = int(dabnfopg['iidoloca'][2])
                # ////////////////////////////////////////////////
                # Buscando o local caso seja um registro existente
                # ////////////////////////////////////////////////
                lcamposb = ('codoloc', 'desoloc', 'idlogra', 'logrnum', 'logrcom', 'logrcep', 'observa', 'situreg')
                lfilbusc = (('idoloca', '=', iidoloca), ('situreg', '!=', 'C'))
                lorderby = None
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_locais', lcamposb, lfilbusc, lorderby)
                if lsqlre01 == [] or iqtdre01 == 0:
                    abnf_alert('O local não foi encontrado!', 4)
                else:
                    # Debug: (inicio)
                    # abnf_show('10', lsqlre01, 1)
                    # Debug: (fim)
                    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidoloca', iidoloca),)])      # ==> Guardando o ID do registro. Obs: tem que ter essa vírgula: "),)])"
                    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '13C00102A'),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
                    lidlogra = abnf_database_menu(icodbase, None, 'L', '0103', 1, 1, 2)
                    lnewpage = [
                        ('div-0', 'container', None, None),
                        ('hr-0', None),
                        ('div-0', 'row', None, None),
                        ('div-0', 'col d-flex justify-content-center', None, None),
                        ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                        ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                        ('legend-0', 'Operacional - Cadastro de Locais - [ Registro existente ]'),
                        ('hr-0', None),
                        ('label-0',  'Código do local', 'form-control-label'),
                        ('number-0', 'icodoloc', 'form-control', 0, 6, '16px', lsqlre01[0][0], 'sdesoloc', True, None),
                        ('label-0',  'Descrição do local', 'form-control-label'),
                        ('input-0',  'sdesoloc', 'form-control', 0, 50, '16px', lsqlre01[0][1], 'iidlogra', True, 0),
                        ('label-0',  'Logradouro: Rua/Bairro/Cidade/Estado (opcional)', 'form-control-label'),
                        ('select-0', 'iidlogra', 'form-control', '16px', 'slogrnum', lidlogra, 1, lsqlre01[0][2], False),
                        ('label-0',  'Logradouro: Número (opcional)', 'form-control-label'),
                        ('input-0',  'slogrnum', 'form-control', 0, 20, '16px', lsqlre01[0][3], 'slogrcom', True, 0),
                        ('label-0',  'Logradouro: Complemento (Opcional)', 'form-control-label'),
                        ('input-0',  'slogrcom', 'form-control', 0, 100, '16px', lsqlre01[0][4], 'slogrcep', True, 0),
                        ('label-0',  'Logradouro: CEP (Opcional)', 'form-control-label'),
                        ('cep-0',    'slogrcep', 'form-control', 0, 9, '16px', lsqlre01[0][5], 'sobserva', True, 0),
                        ('label-0',  'Observação (Opcional) (1000 caracteres)', 'form-control-label'),
                        ('textarea-0', 'sobserva', 'form-control', 2, 1000, '16px', lsqlre01[0][6], 'ssitureg'),
                        ('hr-0', None),
                        ('label-0',  'Situação do registro', 'form-control-label'),
                        ('select-0', 'ssitureg', 'form-control', '16px', 'btmodsav', abnf_personal_retorna_lista(10001), 0, lsqlre01[0][7], False),
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
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidoloca', 0),)])             # ==> Indicativo para dizer que é novo registro. Obs: tem que ter essa vírgula: "),)])"
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '13C00102A'),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
            icodoloc = abnf_database_valor_maximo_campo(icodbase, 'abnf_operacional_cadastro_locais', 'codoloc', iidfilia) + 1
            lidlogra = abnf_database_menu(icodbase, None, 'L', '0103', 1, 1, 2)
            lnewpage = [
                ('div-0', 'container', None, None),
                ('hr-0', None),
                ('div-0', 'row', None, None),
                ('div-0', 'col d-flex justify-content-center', None, None),
                ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                ('legend-0', 'Operacional - Cadastro de Locais - [ Novo registro ]'),
                ('hr-0', None),
                ('label-0',  'Código do local', 'form-control-label'),
                ('number-0', 'icodoloc', 'form-control', 0, 6, '16px', icodoloc, 'sdesoloc', True, None),
                ('label-0',  'Descrição do local', 'form-control-label'),
                ('input-0',  'sdesoloc', 'form-control', 0, 50, '16px', None, 'iidlogra', True, 0),
                ('label-0',  'Logradouro: Rua/Bairro/Cidade/Estado (opcional)', 'form-control-label'),
                ('select-0', 'iidlogra', 'form-control', '16px', 'slogrnum', lidlogra, 1, None, False),
                ('label-0',  'Logradouro: Número (opcional)', 'form-control-label'),
                ('input-0',  'slogrnum', 'form-control', 0, 20, '16px', None, 'slogrcom', True, 0),
                ('label-0',  'Logradouro: Complemento (Opcional)', 'form-control-label'),
                ('input-0',  'slogrcom', 'form-control', 0, 100, '16px', None, 'slogrcep', True, 0),
                ('label-0',  'Logradouro: CEP (Opcional)', 'form-control-label'),
                ('cep-0',    'slogrcep', 'form-control', 0, 9, '16px', None, 'sobserva', True, 0),
                ('label-0',  'Observação (Opcional) (1000 caracteres)', 'form-control-label'),
                ('textarea-0', 'sobserva', 'form-control', 2, 1000, '16px', None, 'btmodsav'),
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
            # abnf_socket_004([3, 'icodoloc', '150'])
            # abnf_socket_004([3, 'sdesoloc', 'TESTE'])
            # Debug: (fim)
        elif dabnfopg['abnfobj0'] == ['btrelcad', 'btrelcad']:      # Relação de locais cadastrados
            abnf000u13c00103_operacional_cadastro_locais(dabnfopg)
            
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00102_operacional_cadastro_locais ] ///////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Locais.                                                                                                                   // #
# // Gravação dos registros e geração de log.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00102_operacional_cadastro_locais(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00102_operacional_cadastro_locais(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        if dabnfopg['abnfobj0'] == ['btcancel', 'btcancel']:        # Voltar para tela anterior
            abnf000u13c00100_operacional_cadastro_locais(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btsalreg', 'btsalreg']:      # Salvar o registro
            iidoloca = dglobaux['iidoloca']
            lmfields = [
                ['icodoloc', 'number',   'M', 'código do local',                       ['Notnull', 'D', 'Notzero'], None],
                ['sdesoloc', 'input',    'F', 'descrição do local',                    ['Notnull', 'D'],            None],
                ['iidlogra', 'number',   'M', 'logradouro (rua/bairro/cidade/estado)', ['Empty_to_null'],           None],
                ['slogrnum', 'input',    'M', 'logradouro (número)',                   [],                          None],
                ['slogrcom', 'input',    'M', 'logradouro (complemento)',              [],                          None],
                ['slogrcep', 'input',    'M', 'logradouro (CEP)',                      [],                          None],
                ['sobserva', 'textarea', 'F', 'observação',                            [],                          None],
            ]
            if iidoloca > 0: lmfields = lmfields + [
                ['ssitureg', 'select',   'F', 'situação do registro',                  ['Notnull', 'D'],            None],
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
                if iidoloca == 0:   # Novo registro
                    lcamposb = ('codoloc', 'idoloca')
                    lfilbusc = (('codoloc', '=', lmfields[0][5]), ('situreg', '!=', 'C'))
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_locais', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 != [] or iqtdre01 != 0:
                        abnf_alert('Não foi possível salvar! O código ' + str(lmfields[0][5]) + ' já está sendo utilizado em outro registro!', 4)
                    else:
                        bvalidad, iproxiid = abnf_database_insere_dados_v02(icodbase, sabnproj, 'abnf_operacional_cadastro_locais', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                        [
                            ('codoloc', lmfields[0][5]),
                            ('desoloc', lmfields[1][5]),
                            ('idlogra', lmfields[2][5]),
                            ('logrnum', lmfields[3][5]),
                            ('logrcom', lmfields[4][5]),
                            ('logrcep', lmfields[5][5]),
                            ('observa', lmfields[6][5]),
                            ('idfilia', iidfilia),
                            ('situreg', 'A'),
                        ])
                        if bvalidad:
                            abnf_alert('Novo local gravado com sucesso!', 3)
                            abnf000u13c00100_operacional_cadastro_locais(dabnfopg)
                elif iidoloca > 0:  # Registro existente
                    lcamposb = ('codoloc', 'idoloca')
                    lfilbusc = (('codoloc', '=', lmfields[0][5]), ('situreg', '!=', 'C'), ('idoloca', '!=', iidoloca))
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_locais', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 != [] or iqtdre01 != 0:
                        abnf_alert('Não foi possível salvar! O código ' + str(lmfields[0][5]) + ' já está sendo utilizado em outro registro!', 4)
                    else:
                        bvalidad = abnf_database_altera_dados_v02(icodbase, sabnproj, 'abnf_operacional_cadastro_locais', iidoloca, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                        [
                            ('codoloc', lmfields[0][5]),
                            ('desoloc', lmfields[1][5]),
                            ('idlogra', lmfields[2][5]),
                            ('logrnum', lmfields[3][5]),
                            ('logrcom', lmfields[4][5]),
                            ('logrcep', lmfields[5][5]),
                            ('observa', lmfields[6][5]),
                            ('situreg', lmfields[7][5]),
                        ])
                        if bvalidad:
                            abnf_alert('Registro alterado com sucesso!', 3)
                            abnf000u13c00100_operacional_cadastro_locais(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btexcreg', 'btexcreg']:      # Excluir registro
            iidoloca = dglobaux['iidoloca']        
            icodbase = int(dabnfopg['abnproje'][2][14:]) * 100      # Código do banco de dados a ser utilizado
            bvalidad = abnf_database_exclui_registro(icodbase, sabnproj, 'abnf_operacional_cadastro_locais', iidoloca, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'])
            if bvalidad:
                abnf_alert('Registro excluído com sucesso!', 3)
                abnf000u13c00100_operacional_cadastro_locais(dabnfopg)
                
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00103_operacional_cadastro_locais ] ///////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Locais.                                                                                                                   // #
# // Relatório de locais.                                                                                                                                // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
                
def abnf000u13c00103_operacional_cadastro_locais(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00103_operacional_cadastro_locais(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        # abnf_show('10', dglobaux, 2)
        iidfilia = dglobaux['iidfilia']
        didlogra = abnf_database_menu(icodbase, None, 'D', '0103', 1, 1, 2)
        # /////////////////////
        # Variaveis de ambiente
        # /////////////////////
        icolspan = 12
        ifontlen = 2
        icontreg = 0
        # ===> if bimprusu: icolspan = 16
        # ===> ddttmini = datetime.combine(ddataini, thoraini)
        # ===> ddttmfim = datetime.combine(ddatafim, thorafim)
        # ////////////////////
        # Listas e dicionários
        # ////////////////////
        # ===> desvveic = abnf_dict_veiculos(current_user.idfilia, True, 0)
        # ===> desvloca = abnf_dict_operacional_entrada_saida_veiculos_locais(current_user.idfilia, False)
        # ===> desvlinh = abnf_dict_operacional_linhas(current_user.idfilia, False, 1)
        # ===> desvfunc = abnf_dict_funcionarios(current_user.idfilia, True, 0)        
        # ///////////////////
        # Gerando o relatório
        # ///////////////////
        sarqurel = abnf_imprime_file(0, sabntoke)
        with open('abnftmp/' + sarqurel, 'w') as sarquwri:
            snomeemp, snomefil = abnf_database_retorna_empresa_filial(icodbase, iidfilia)
            abnf_imprime_doctype_head_fhead_body_form_table_thead(sarquwri, 3)
            abnf_imprime_thead_001_abeinfo_sistemas(sarquwri, icolspan)
            abnf_imprime_thead_002_titulo_relatorio(sarquwri, icolspan, 'RELAÇÃO DE LOCAIS')
            abnf_imprime_thead_003_empresa_filial(sarquwri, icolspan, snomeemp, snomefil)
            # smensage = 'Per&iacute;odo: ' + abnf_converte_data(ddataini) + ' &agrave;s ' + abnf_converte_hora(thoraini) + ' at&eacute; ' + abnf_converte_data(ddatafim) + ' &agrave;s ' + abnf_converte_hora(thorafim)
            # abnf_imprime_thead_004_parametros(sarquwri, icolspan, smensage)
            abnf_imprime_thead_005_datetime(sarquwri, icolspan)
            abnf_imprime_line(sarquwri, icolspan, 'darkcyan')
            abnf_imprime_info_001(sarquwri, '#D1C5C5', 'center', 1,
                [
                    ('Descrição do local', 1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Código',             1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Tipo',               1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Logradouro',         1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Número',             1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Complemento',        1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Bairro',             1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Cidade',             1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Estado',             1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('CEP',                1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Observação',         1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Situação',           1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                ]
            )
            abnf_imprime_fthead_tbody(sarquwri)
            lcamposb = ('desoloc', 'codoloc', 'situreg', 'idlogra', 'logrnum', 'logrcom', 'logrcep', 'observa')
            lfilbusc = (('situreg', '!=', 'C'), ('idfilia', '=', iidfilia), None)
            lorderby = ('desoloc', 'idoloca')
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_locais', lcamposb, lfilbusc, lorderby)
            for lauxi001 in lsqlre01:
                ssitureg = abnf_personal_retorna_string(10001, lauxi001[2])
                lidlogra = didlogra.get(lauxi001[3], ('', '', '', '', '', '')) if lauxi001[3] != None and lauxi001[3] > 0 else ('', '', '', '', '', '')
                icontreg += 1
                abnf_imprime_info_001(sarquwri, None, None, 1,
                    [
                        (lauxi001[0], 1, 0, None, 'Left'   , 'black', 'Courier New', ifontlen, True, False),
                        (lauxi001[1], 1, 0, None, 'Center' , 'black', 'Courier New', ifontlen, True, False),
                        (lidlogra[1], 1, 0, None, 'Left'   , 'black', 'Courier New', ifontlen, True, False),
                        (lidlogra[2], 1, 0, None, 'Left'   , 'black', 'Courier New', ifontlen, True, False),
                        (lauxi001[4], 1, 0, None, 'Right'  , 'black', 'Courier New', ifontlen, True, False),
                        (lauxi001[5], 1, 0, None, 'Left'   , 'black', 'Courier New', ifontlen, True, False),
                        (lidlogra[3], 1, 0, None, 'Left'   , 'black', 'Courier New', ifontlen, True, False),
                        (lidlogra[4], 1, 0, None, 'Left'   , 'black', 'Courier New', ifontlen, True, False),
                        (lidlogra[5], 1, 0, None, 'Center' , 'black', 'Courier New', ifontlen, True, False),
                        (lauxi001[6], 1, 0, None, 'Center' , 'black', 'Courier New', ifontlen, True, False),
                        (lauxi001[7], 1, 0, None, 'Left'   , 'black', 'Courier New', ifontlen, True, False),
                        (ssitureg,    1, 0, None, 'Center' , 'black', 'Courier New', ifontlen, True, False),
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
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
