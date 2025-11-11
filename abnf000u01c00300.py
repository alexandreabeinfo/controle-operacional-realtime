## ===============================================
## [abnf000u01c00300.py] - Cadastro de Logradouros
## ===============================================

from abnfsrc.abnf000u00s00003 import *              # Arquivo de funções comuns que serão utilizadas por todos os módulos do sistema
from abnfsrc.abnf000u00s00004 import *              # Arquivo de banco de dados

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u01c00300_cadastro_logradouros ] //////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de Logradouros.                                                                                                                            // #
# // Form inicial.                                                                                                                                       // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u01c00300_cadastro_logradouros(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u01c00300_cadastro_logradouros(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, '01C00301A'])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        lidlogra = abnf_database_menu(icodbase, None, 'L', '0103', 1, 1, 2)
        # Debug: (inicio)
        # abnf_show('08', iidlogra, 1)
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
            ('legend-0', 'Cadastro de Logradouros'),
            ('hr-0', None),
            ('label-0',  'Logradouro', 'form-control-label'),
            ('select-0', 'iidlogra', 'form-control', '16px', 'btbusreg', lidlogra, 1, None, False),
            ('hr-0', None),
            ('button-0', 'btbusreg', 'btn btn-primary mt-2', 'Buscar'),
            ('alt255-0', 2),
            ('button-0', 'btnovreg', 'btn btn-primary mt-2', 'Novo registro'),
            ('alt255-0', 2),
            ('button-0', 'btrelcad', 'btn btn-primary mt-2', 'Relação de logradouros cadastrados'),
            ('form-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
        ]
        snewpage = abnf_create_page(lnewpage)
        abnf_socket_004([1, 'abnfdv03', snewpage])
        
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u01c00301_cadastro_logradouros ] //////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de Logradouros.                                                                                                                            // #
# // Form de cadastro/alteração do logradouro.                                                                                                           // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u01c00301_cadastro_logradouros(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u01c00301_cadastro_logradouros(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        if dabnfopg['abnfobj0'] == ['btbusreg', 'btbusreg']:        # Buscar registro existente
            lmfields = [
                ['iidlogra', 'input', 'M', 'logradouro', ['Notnull', 'D', 'Return_integer'], None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btbusreg')
            # Debug: (inicio)
            # abnf_show('08', lmfields, 1)
            # abnf_show('09', dabnfopg, 2)
            # abnf_show('10', dglobaux, 2)
            # Debug: (fim)
            if bvalidad:
                icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
                iidlogra = lmfields[0][5]
                # /////////////////////////////////////////////////////
                # Buscando o logradouro caso seja um registro existente
                # /////////////////////////////////////////////////////
                lcamposb = ('codlogr', 'tiplogr', 'deslogr', 'idbairr', 'situreg')
                lfilbusc = (('idlogra', '=', iidlogra), ('situreg', '!=', 'C'))
                lorderby = None
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_logradouros', lcamposb, lfilbusc, lorderby)
                if lsqlre01 == [] or iqtdre01 == 0:
                    abnf_alert('O logradouro não foi encontrado!', 4)
                else:
                    # Debug: (inicio)
                    # abnf_show('10', lsqlre01, 1)
                    # Debug: (fim)
                    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidlogra', iidlogra),)])      # ==> Guardando o ID do registro. Obs: tem que ter essa vírgula: "),)])"
                    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '01C00302A'),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
                    lidbairr = abnf_database_menu(icodbase, None, 'L', '0102', 1, 1, 2)
                    lnewpage = [
                        ('div-0', 'container', None, None),
                        ('hr-0', None),
                        ('div-0', 'row', None, None),
                        ('div-0', 'col d-flex justify-content-center', None, None),
                        ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                        ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                        ('legend-0', 'Cadastro de Logradouros - [ Registro existente ]'),
                        ('hr-0', None),
                        ('label-0',  'Código do logradouro', 'form-control-label'),
                        ('number-0', 'icodlogr', 'form-control', 0, 6, '16px', lsqlre01[0][0], 'stiplogr', True, None),
                        ('label-0',  'Tipo de logradouro', 'form-control-label'),
                        ('select-0', 'stiplogr', 'form-control', '16px', 'sdeslogr', abnf_personal_retorna_lista(10103), 0, lsqlre01[0][1], False),
                        ('label-0',  'Descrição', 'form-control-label'),
                        ('input-0',  'sdeslogr', 'form-control', 0, 200, '16px', lsqlre01[0][2], 'iidbairr', True, 0),
                        ('label-0',  'Bairro/Cidade/Estado', 'form-control-label'),
                        ('select-0', 'iidbairr', 'form-control', '16px', 'ssitureg', lidbairr, 0, lsqlre01[0][3], False),
                        ('hr-0', None),
                        ('label-0',  'Situação do registro', 'form-control-label'),
                        ('select-0', 'ssitureg', 'form-control', '16px', 'btmodsav', abnf_personal_retorna_lista(10001), 0, lsqlre01[0][4], False),
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
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidlogra', 0),)])             # ==> Indicativo para dizer que é novo registro. Obs: tem que ter essa vírgula: "),)])"
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '01C00302A'),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
            icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
            iproxcod = abnf_database_valor_maximo_campo(icodbase, 'abnf_cadastro_logradouros', 'codlogr', None) + 1
            lidbairr = abnf_database_menu(icodbase, None, 'L', '0102', 1, 1, 2)
            lnewpage = [
                ('div-0', 'container', None, None),
                ('hr-0', None),
                ('div-0', 'row', None, None),
                ('div-0', 'col d-flex justify-content-center', None, None),
                ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                ('legend-0', 'Cadastro de Logradouros - [ Novo registro ]'),
                ('hr-0', None),
                ('label-0',  'Código do logradouro', 'form-control-label'),
                ('number-0', 'icodlogr', 'form-control', 0, 6, '16px', iproxcod, 'stiplogr', True, None),
                ('label-0',  'Tipo de logradouro', 'form-control-label'),
                ('select-0', 'stiplogr', 'form-control', '16px', 'sdeslogr', abnf_personal_retorna_lista(10103), 0, None, False),
                ('label-0',  'Descrição', 'form-control-label'),
                ('input-0',  'sdeslogr', 'form-control', 0, 200, '16px', None, 'iidbairr', True, 0),
                ('label-0',  'Bairro/Cidade/Estado', 'form-control-label'),
                ('select-0', 'iidbairr', 'form-control', '16px', 'btmodsav', lidbairr, 0, None, False),
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
        elif dabnfopg['abnfobj0'] == ['btrelcad', 'btrelcad']:      # Relação de bairros cadastrados
            abnf000u01c00303_cadastro_logradouros(dabnfopg)
            
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u01c00302_cadastro_logradouros ] //////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de Logradouros.                                                                                                                            // #
# // Gravação dos registros e geração de log.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u01c00302_cadastro_logradouros(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u01c00302_cadastro_logradouros(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        if dabnfopg['abnfobj0'] == ['btcancel', 'btcancel']:        # Voltar para tela anterior
            abnf000u01c00300_cadastro_logradouros(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btsalreg', 'btsalreg']:      # Salvar o registro
            iidlogra = dglobaux['iidlogra']
            lmfields = [
                ['icodlogr', 'number', 'M', 'código do logradouro',    ['Notnull', 'D'], None],
                ['stiplogr', 'select', 'M', 'tipo de logradouro',      ['Notnull', 'D'], None],
                ['sdeslogr', 'input',  'F', 'descrição do logradouro', ['Notnull', 'D'], None],
                ['iidbairr', 'select', 'M', 'bairro/cidade/estado',    ['Notnull', 'D'], None],
            ]
            if iidlogra > 0: lmfields = lmfields + [
                ['ssitureg', 'select', 'F', 'situação do registro',    ['Notnull', 'D'], None],
            ]            
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btsalreg')
            # Debug: (inicio)
            # abnf_show('10', lmfields, 1)
            # abnf_show('09', dabnfopg, 2)
            # abnf_show('10', dglobaux, 0)
            # Debug: (fim)            
            if bvalidad:
                icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
                if iidlogra == 0:   # Novo registro
                    lcamposb = ('codlogr', 'idlogra')
                    lfilbusc = (('codlogr', '=', lmfields[0][5]), ('situreg', '!=', 'C'))
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_logradouros', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 != [] or iqtdre01 != 0:
                        abnf_alert('Não foi possível salvar! O código ' + str(lmfields[0][5]) + ' já está sendo utilizado em outro registro!', 4)
                    else:
                        bvalidad, iproxiid = abnf_database_insere_dados_v02(icodbase, sabnproj, 'abnf_cadastro_logradouros', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                        [
                            ('codlogr', lmfields[0][5] ),
                            ('tiplogr', lmfields[1][5] ),
                            ('deslogr', lmfields[2][5] ),
                            ('idbairr', lmfields[3][5] ),
                            ('situreg', 'A'            ),
                        ])
                        if bvalidad:
                            abnf_alert('Novo bairro gravada com sucesso!', 3)
                            abnf000u01c00300_cadastro_logradouros(dabnfopg)
                elif iidlogra > 0:  # Registro existente
                    lcamposb = ('codlogr', 'idlogra')
                    lfilbusc = (('codlogr', '=', lmfields[0][5]), ('situreg', '!=', 'C'), ('idlogra', '!=', iidlogra))
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_logradouros', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 != [] or iqtdre01 != 0:
                        abnf_alert('Não foi possível salvar! O código ' + str(lmfields[0][5]) + ' já está sendo utilizado em outro registro!', 4)
                    else:
                        bvalidad = abnf_database_altera_dados_v02(icodbase, sabnproj, 'abnf_cadastro_logradouros', iidlogra, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                        [
                            ('codlogr', lmfields[0][5] ),
                            ('tiplogr', lmfields[1][5] ),
                            ('deslogr', lmfields[2][5] ),
                            ('idbairr', lmfields[3][5] ),
                            ('situreg', lmfields[4][5] ),
                        ])
                        if bvalidad:
                            abnf_alert('Registro alterado com sucesso!', 3)
                            abnf000u01c00300_cadastro_logradouros(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btexcreg', 'btexcreg']:      # Excluir registro
            iidlogra = dglobaux['iidlogra']        
            icodbase = int(dabnfopg['abnproje'][2][14:]) * 100      # Código do banco de dados a ser utilizado
            bvalidad = abnf_database_exclui_registro(icodbase, sabnproj, 'abnf_cadastro_logradouros', iidlogra, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'])
            if bvalidad:
                abnf_alert('Registro excluído com sucesso!', 3)
                abnf000u01c00300_cadastro_logradouros(dabnfopg)
                
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u01c00303_cadastro_logradouros ] //////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de Logradouros.                                                                                                                            // #
# // Relatório de bairros.                                                                                                                               // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
                
def abnf000u01c00303_cadastro_logradouros(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u01c00303_cadastro_logradouros(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        # /////////////////////
        # Variaveis de ambiente
        # /////////////////////
        icolspan = 6
        ifontlen = 2
        icontreg = 0
        # ////////////////////
        # Listas e dicionários
        # ////////////////////
        drelbair = abnf_database_menu(icodbase, None, 'D', '0102', 1, 1, 2)
        # ///////////////////
        # Gerando o relatório
        # ///////////////////
        sarqurel = abnf_imprime_file(0, sabntoke)
        with open('abnftmp/' + sarqurel, 'w') as sarquwri:
            snomeemp, snomefil = abnf_database_retorna_empresa_filial(icodbase, iidfilia)
            abnf_imprime_doctype_head_fhead_body_form_table_thead(sarquwri, 3)
            abnf_imprime_thead_001_abeinfo_sistemas(sarquwri, icolspan)
            abnf_imprime_thead_002_titulo_relatorio(sarquwri, icolspan, 'RELAÇÃO DE LOGRADOUROS')
            abnf_imprime_thead_003_empresa_filial(sarquwri, icolspan, snomeemp, snomefil)
            # smensage = 'Per&iacute;odo: ' + abnf_converte_data(ddataini) + ' &agrave;s ' + abnf_converte_hora(thoraini) + ' at&eacute; ' + abnf_converte_data(ddatafim) + ' &agrave;s ' + abnf_converte_hora(thorafim)
            # abnf_imprime_thead_004_parametros(sarquwri, icolspan, smensage)
            abnf_imprime_thead_005_datetime(sarquwri, icolspan)
            abnf_imprime_line(sarquwri, icolspan, 'darkcyan')
            abnf_imprime_info_001(sarquwri, '#D1C5C5', 'center', 1,
                [
                    ('Logradouro', 1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Bairro',     1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Cidade',     1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Estado',     1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Código',     1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Situação',   1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                ]
            )
            abnf_imprime_fthead_tbody(sarquwri)
            lcamposb = ('tiplogr', 'deslogr', 'idbairr', 'codlogr', 'situreg')
            lfilbusc = (('situreg', '!=', 'C'), None)
            lorderby = ('tiplogr', 'deslogr', 'idbairr', 'idlogra')
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_logradouros', lcamposb, lfilbusc, lorderby)
            for lauxi001 in lsqlre01:
                sauxi001 = lauxi001[0] + ' ' + lauxi001[1]
                sauxi002, sdesbair, sdescida, sdesesta, icodbair = drelbair.get(lauxi001[2], ('', '', '', '', ''))
                ssitureg = abnf_personal_retorna_string(10001, lauxi001[4])
                icontreg += 1
                abnf_imprime_info_001(sarquwri, None, None, 1,
                    [
                        (sauxi001,    1, 0, None, 'Left',   'black', 'Courier New', ifontlen, True, False),
                        (sdesbair,    1, 0, None, 'Left',   'black', 'Courier New', ifontlen, True, False),
                        (sdescida,    1, 0, None, 'Left',   'black', 'Courier New', ifontlen, True, False),
                        (sdesesta,    1, 0, None, 'Center', 'black', 'Courier New', ifontlen, True, False),
                        (lauxi001[3], 1, 0, None, 'Center', 'black', 'Courier New', ifontlen, True, False),
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
        abnf_socket_004([5, 'btrelcad'])
        abnf_alert('Relatório gerado com sucesso!', 3)
        time.sleep(5)
        abnf_alert('', 0)
                    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #