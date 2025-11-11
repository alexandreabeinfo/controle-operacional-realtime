## ==================================================================
## [abnf000u13c00200.py] - Operacional - Cadastro de Grupos de Linhas
## ==================================================================

from abnfsrc.abnf000u00s00003 import *              # Arquivo de funções comuns que serão utilizadas por todos os módulos do sistema
from abnfsrc.abnf000u00s00004 import *              # Arquivo de banco de dados

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00200_operacional_cadastro_grupos_linhas ] ////////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Grupos de Linhas.                                                                                                         // #
# // Form inicial.                                                                                                                                       // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00200_operacional_cadastro_grupos_linhas(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00200_operacional_cadastro_grupos_linhas(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, '13C00201A'])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        lidogrli = abnf_database_menu(icodbase, iidfilia, 'L', '1302', 1, 1, 2)
        # Debug: (inicio)
        # abnf_show('08', iidogrli, 1)
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
            ('legend-0', 'Operacional - Cadastro de Grupos de Linhas'),
            ('hr-0', None),
            ('label-0',  'Grupo de linha', 'form-control-label'),
            ('select-0', 'iidogrli', 'form-control', '16px', 'btbusreg', lidogrli, 1, None, False),
            ('hr-0', None),
            ('button-0', 'btbusreg', 'btn btn-primary mt-2', 'Buscar'),
            ('alt255-0', 2),
            ('button-0', 'btnovreg', 'btn btn-primary mt-2', 'Novo registro'),
            ('alt255-0', 2),
            ('button-0', 'btrelcad', 'btn btn-primary mt-2', 'Relação de grupos cadastrados'),
            ('form-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
        ]
        snewpage = abnf_create_page(lnewpage)
        abnf_socket_004([1, 'abnfdv03', snewpage])
        
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00201_operacional_cadastro_grupos_linhas ] ////////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Grupos de Linhas.                                                                                                         // #
# // Form de cadastro/alteração do grupo de linha.                                                                                                       // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00201_operacional_cadastro_grupos_linhas(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00201_operacional_cadastro_grupos_linhas(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        if dabnfopg['abnfobj0'] == ['btbusreg', 'btbusreg']:        # Buscar registro existente
            lmfields = [
                ['iidogrli', 'input', 'M', 'grupo de linha', ['Notnull', 'D'], None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btbusreg')
            # Debug: (inicio)
            # abnf_show('08', lmfields, 1)
            # abnf_show('09', dabnfopg, 2)
            # abnf_show('10', dglobaux, 2)
            # Debug: (fim)
            if bvalidad:
                icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
                iidogrli = int(dabnfopg['iidogrli'][2])
                # /////////////////////////////////////////////////////////
                # Buscando o grupo de linha caso seja um registro existente
                # /////////////////////////////////////////////////////////
                lcamposb = ('codogrl', 'desogrl', 'situreg')
                lfilbusc = (('idogrli', '=', iidogrli), ('situreg', '!=', 'C'))
                lorderby = None
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_grupos_linhas', lcamposb, lfilbusc, lorderby)
                if lsqlre01 == [] or iqtdre01 == 0:
                    abnf_alert('O grupo de linha não foi encontrado!', 4)
                else:
                    # Debug: (inicio)
                    # abnf_show('10', lsqlre01, 1)
                    # Debug: (fim)
                    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidogrli', iidogrli),)])      # ==> Guardando o ID do registro. Obs: tem que ter essa vírgula: "),)])"
                    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '13C00202A'),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
                    lnewpage = [
                        ('div-0', 'container', None, None),
                        ('hr-0', None),
                        ('div-0', 'row', None, None),
                        ('div-0', 'col d-flex justify-content-center', None, None),
                        ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                        ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                        ('legend-0', 'Operacional - Cadastro de Grupos de Linhas - [ Registro existente ]'),
                        ('hr-0', None),
                        ('label-0',  'Código do grupo', 'form-control-label'),
                        ('number-0', 'icodogrl', 'form-control', 0, 6, '16px', lsqlre01[0][0], 'sdesogrl', True, None),
                        ('label-0',  'Descrição do grupo', 'form-control-label'),
                        ('input-0',  'sdesogrl', 'form-control', 0, 50, '16px', lsqlre01[0][1], 'ssitureg', True, 0),
                        ('hr-0', None),
                        ('label-0',  'Situação do registro', 'form-control-label'),
                        ('select-0', 'ssitureg', 'form-control', '16px', 'btmodsav', abnf_personal_retorna_lista(10001), 0, lsqlre01[0][2], False),
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
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidogrli', 0),)])             # ==> Indicativo para dizer que é novo registro. Obs: tem que ter essa vírgula: "),)])"
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '13C00202A'),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
            lnewpage = [
                ('div-0', 'container', None, None),
                ('hr-0', None),
                ('div-0', 'row', None, None),
                ('div-0', 'col d-flex justify-content-center', None, None),
                ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                ('legend-0', 'Operacional - Cadastro de Grupos de Linhas - [ Novo registro ]'),
                ('hr-0', None),
                ('label-0',  'Código do grupo', 'form-control-label'),
                ('number-0', 'icodogrl', 'form-control', 0, 6, '16px', None, 'sdesogrl', True, None),
                ('label-0',  'Descrição do grupo', 'form-control-label'),
                ('input-0',  'sdesogrl', 'form-control', 0, 50, '16px', None, 'btmodsav', True, 0),
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
            # abnf_socket_004([3, 'icodogrl', '150'])
            # abnf_socket_004([3, 'sdesogrl', 'TESTE'])
            # Debug: (fim)
        elif dabnfopg['abnfobj0'] == ['btrelcad', 'btrelcad']:      # Relação de grupos cadastrados
            abnf000u13c00203_operacional_cadastro_grupos_linhas(dabnfopg)
            
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00202_operacional_cadastro_grupos_linhas ] ////////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Grupos de Linhas.                                                                                                         // #
# // Gravação dos registros e geração de log.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00202_operacional_cadastro_grupos_linhas(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00202_operacional_cadastro_grupos_linhas(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        if dabnfopg['abnfobj0'] == ['btcancel', 'btcancel']:        # Voltar para tela anterior
            abnf000u13c00200_operacional_cadastro_grupos_linhas(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btsalreg', 'btsalreg']:      # Salvar o registro
            iidogrli = dglobaux['iidogrli']
            lmfields = [
                ['icodogrl', 'number',   'M', 'código do grupo',        ['Notnull', 'D', 'Notzero'], None],
                ['sdesogrl', 'input',    'F', 'descrição do grupo',     ['Notnull', 'D'],            None],
            ]
            if iidogrli > 0: lmfields = lmfields + [
                ['ssitureg', 'select',   'F', 'situação do registro',   ['Notnull', 'D'],            None],
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
                if iidogrli == 0:   # Novo registro
                    lcamposb = ('codogrl', 'idogrli')
                    lfilbusc = (('codogrl', '=', lmfields[0][5]), ('situreg', '!=', 'C'))
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_grupos_linhas', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 != [] or iqtdre01 != 0:
                        abnf_alert('Não foi possível salvar! O código ' + str(lmfields[0][5]) + ' já está sendo utilizado em outro registro!', 4)
                    else:
                        bvalidad, iproxiid = abnf_database_insere_dados_v02(icodbase, sabnproj, 'abnf_operacional_cadastro_grupos_linhas', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                        [
                            ('codogrl', lmfields[0][5]),
                            ('desogrl', lmfields[1][5]),
                            ('idfilia', iidfilia),
                            ('situreg', 'A'),
                        ])
                        if bvalidad:
                            abnf_alert('Novo grupo de linha gravado com sucesso!', 3)
                            abnf000u13c00200_operacional_cadastro_grupos_linhas(dabnfopg)
                elif iidogrli > 0:  # Registro existente
                    lcamposb = ('codogrl', 'idogrli')
                    lfilbusc = (('codogrl', '=', lmfields[0][5]), ('situreg', '!=', 'C'), ('idogrli', '!=', iidogrli))
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_grupos_linhas', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 != [] or iqtdre01 != 0:
                        abnf_alert('Não foi possível salvar! O código ' + str(lmfields[0][5]) + ' já está sendo utilizado em outro registro!', 4)
                    else:
                        bvalidad = abnf_database_altera_dados_v02(icodbase, sabnproj, 'abnf_operacional_cadastro_grupos_linhas', iidogrli, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                        [
                            ('codogrl', lmfields[0][5]),
                            ('desogrl', lmfields[1][5]),
                            ('situreg', lmfields[2][5]),
                        ])
                        if bvalidad:
                            abnf_alert('Registro alterado com sucesso!', 3)
                            abnf000u13c00200_operacional_cadastro_grupos_linhas(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btexcreg', 'btexcreg']:      # Excluir registro
            iidogrli = dglobaux['iidogrli']        
            icodbase = int(dabnfopg['abnproje'][2][14:]) * 100      # Código do banco de dados a ser utilizado
            bvalidad = abnf_database_exclui_registro(icodbase, sabnproj, 'abnf_operacional_cadastro_grupos_linhas', iidogrli, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'])
            if bvalidad:
                abnf_alert('Registro excluído com sucesso!', 3)
                abnf000u13c00200_operacional_cadastro_grupos_linhas(dabnfopg)
                
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00203_operacional_cadastro_grupos_linhas ] ////////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Grupos de Linhas.                                                                                                         // #
# // Relatório de grupos de linhas.                                                                                                                      // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
                
def abnf000u13c00203_operacional_cadastro_grupos_linhas(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00203_operacional_cadastro_grupos_linhas(dabnfopg)')
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
        icolspan = 3
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
            abnf_imprime_thead_002_titulo_relatorio(sarquwri, icolspan, 'RELAÇÃO DE GRUPOS DE LINHAS')
            abnf_imprime_thead_003_empresa_filial(sarquwri, icolspan, snomeemp, snomefil)
            # smensage = 'Per&iacute;odo: ' + abnf_converte_data(ddataini) + ' &agrave;s ' + abnf_converte_hora(thoraini) + ' at&eacute; ' + abnf_converte_data(ddatafim) + ' &agrave;s ' + abnf_converte_hora(thorafim)
            # abnf_imprime_thead_004_parametros(sarquwri, icolspan, smensage)
            abnf_imprime_thead_005_datetime(sarquwri, icolspan)
            abnf_imprime_line(sarquwri, icolspan, 'darkcyan')
            abnf_imprime_info_001(sarquwri, '#D1C5C5', 'center', 1,
                [
                    ('Descrição',   1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Código',      1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Situação',    1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                ]
            )
            abnf_imprime_fthead_tbody(sarquwri)
            lcamposb = ('desogrl', 'codogrl', 'situreg')
            lfilbusc = (('situreg', '!=', 'C'), ('idfilia', '=', iidfilia), None)
            lorderby = ('desogrl', 'idogrli')
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_grupos_linhas', lcamposb, lfilbusc, lorderby)
            for lauxi001 in lsqlre01:
                ssitureg = abnf_personal_retorna_string(10001, lauxi001[2])
                icontreg += 1
                abnf_imprime_info_001(sarquwri, None, None, 1,
                    [
                        (lauxi001[0], 1, 0, None, 'Left'    , 'black', 'Courier New', ifontlen, True, False),
                        (lauxi001[1], 1, 0, None, 'Center'  , 'black', 'Courier New', ifontlen, True, False),
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
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #