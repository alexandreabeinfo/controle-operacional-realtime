## =====================================================================
## [abnf000u13c00900.py] - Operacional - Cadastro de Operações Especiais
## =====================================================================

from abnfsrc.abnf000u00s00003 import *              # Arquivo de funções comuns que serão utilizadas por todos os módulos do sistema
from abnfsrc.abnf000u00s00004 import *              # Arquivo de banco de dados

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00900_operacional_cadastro_operacoes_especiais ] //////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Operações Especiais.                                                                                                      // #
# // Form inicial.                                                                                                                                       // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00900_operacional_cadastro_operacoes_especiais(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00900_operacional_cadastro_operacoes_especiais(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, '13C00901A'])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        lnewpage = [
            ('div-0', 'container', None, None),
            ('hr-0', None),
            ('div-0', 'row', None, None),
            ('div-0', 'col d-flex justify-content-center', None, None),
            ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
            ('legend-0', 'Operacional - Cadastro de Operações Especiais'),
            ('hr-0', None),
            ('div-1', 'sdivprio'),
            ('div-9', None),
            ('hr-0', None),
            ('button-0', 'btnovope', 'btn btn-primary mt-2', 'Nova operação especial'),
            ('form-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
        ]
        snewpage = abnf_create_page(lnewpage)
        abnf_socket_004([1, 'abnfdv03', snewpage])
        abnf000u13c00903_operacional_cadastro_operacoes_especiais(icodbase, iidfilia, '')
        
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00901_operacional_cadastro_operacoes_especiais ] //////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Operações Especiais.                                                                                                      // #
# // Form de inclusão/alteração/exclusão do registro de operação especial.                                                                               // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00901_operacional_cadastro_operacoes_especiais(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00901_operacional_cadastro_operacoes_especiais(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        if dabnfopg['abnfobj0'] == ['btfilreg', 'btfilreg']:        # Filtrar registros
            lmfields = [
                ['sfilprio', 'input', 'M', 'filtro de registros', [], None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btfilreg')
            if bvalidad:
                sfilprio = lmfields[0][5]
                abnf000u13c00903_operacional_cadastro_operacoes_especiais(icodbase, iidfilia, sfilprio)
            bvalidad = False    # => Para não entrar na parte que monta a tela principal
        elif dabnfopg['abnfobj0'] == ['btrelcad', 'btrelcad']:      # Relação de operações especiais
            lmfields = [
                ['sfilprio', 'input', 'M', 'filtro de registros', [], None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btfilreg')
            if bvalidad:
                sfilprio = lmfields[0][5]
                abnf000u13c00904_operacional_cadastro_operacoes_especiais(dabnfopg, sfilprio)
            bvalidad = False    # => Para não entrar na parte que monta a tela principal
        elif dabnfopg['abnfobj0'] == ['btnovope', 'btnovope']:        # Novo registro
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidooesp', 0),)]) # ==> Guardado dados do registro para a próxima função. Obs: tem que ter essa vírgula: "),)])"
            iidooesp = 0
            ddataope = None
            iidolinh = None
            iveicser = None
            stipodia = None
            sdescmot = None
            bvalidad = True
        elif dabnfopg['abnfobj0'] == ['btselreg', 'btselreg']:
            # ////////////////////////////////
            # Buscando um registro selecionado
            # ////////////////////////////////
            lmfields = [
                ['iidooesp', 'radio', 'Nenhum registro foi selecionado', ['Notnull', 'Return_integer'], None],
            ]
            bvalidad, lmfields = abnf_find_checkbox_radio(dabnfopg, lmfields, 'btselreg')
            if bvalidad:
                iidooesp = lmfields[0][4]
                # ///////////////////
                # Buscando o registro
                # ///////////////////
                lcamposb = ('dataope', 'idolinh', 'veicser', 'tipodia', 'descmot')
                lfilbusc = (('idooesp', '=', iidooesp), ('situreg', '!=', 'C'))
                lorderby = None
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_operacoes_especiais', lcamposb, lfilbusc, lorderby)
                if lsqlre01 == [] or iqtdre01 == 0:
                    abnf_alert('Registro não encontrado! Entre em contato com o depto. de sistemas!', 4)
                    abnf_socket_004([5, 'btselreg'])
                    bvalidad = False
                else:
                    ddataope = lsqlre01[0][0]
                    iidolinh = lsqlre01[0][1]
                    iveicser = lsqlre01[0][2]
                    stipodia = lsqlre01[0][3]
                    sdescmot = lsqlre01[0][4]
                    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidooesp', iidooesp),)]) # ==> Guardado dados do registro para a próxima função. Obs: tem que ter essa vírgula: "),)])"
                abnf_socket_004([5, 'btselreg'])
        if bvalidad:
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '13C00902A'),)]) # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
            # //////////////////////////
            # Buscas em tabelas externas
            # //////////////////////////
            lidolinh = abnf_database_menu(icodbase, iidfilia, 'L', '1303', 3, 2, 1)
            ltipodia = abnf_personal_retorna_lista(13001)
            # /// #
            if iidooesp > 0:
                sauxi001 = '[ Registro existente ]'
            else:
                sauxi001 = '[ Novo registro ]'
            lnewpage = [
                ('div-0', 'container', None, None),
                ('hr-0', None),
                ('div-0', 'row', None, None),
                ('div-0', 'col d-flex justify-content-center', None, None),
                ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                ('table-0', 'table table-bordered table-sm table-responsive'),
                    ('tr-0', 'text-white bg-secondary', False),
                        ('td-0', None, 2, None, 1, None, None),
                            ('legend-0', 'Cadastro de Operações Especiais - ' + sauxi001),
                        ('td-9', None),
                    ('tr-9', None),
                    ('tr-0', None, False),
                        ('td-0', None, None, None, None, None, None),
                            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                            ('table-0', 'table table-bordered table-sm table-responsive'),
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None), ('label-0', 'Data da operação', 'form-control-label'),                                      ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),           ('label-0', '&nbsp;', 'form-control-label'),                                                ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),           ('date-0', 'ddataope', 'form-control', '16px', ddataope, 'iidolinh', True, 0, None),        ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None), ('label-0', 'Linha', 'form-control-label'),                                                 ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),           ('label-0', '&nbsp;', 'form-control-label'),                                                ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),           ('select-0', 'iidolinh', 'form-control', '16px', 'iveicser', lidolinh, 1, iidolinh, False), ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None), ('label-0', 'Veículo/serviço (digite 0 "zero" para todos)', 'form-control-label'),          ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),           ('label-0', '&nbsp;', 'form-control-label'),                                                ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),           ('number-0', 'iveicser', 'form-control', 0, 6, '16px', iveicser, 'stipodia', True, None),   ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None), ('label-0', 'Tipo de dia', 'form-control-label'),                                           ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),           ('label-0', '&nbsp;', 'form-control-label'),                                                ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),           ('select-0', 'stipodia', 'form-control', '16px', 'sdescmot', ltipodia, 1, stipodia, False), ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None), ('label-0', 'Motivo', 'form-control-label'),                                                ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),           ('label-0', '&nbsp;', 'form-control-label'),                                                ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),           ('input-0', 'sdescmot', 'form-control', 0, 50, '16px', sdescmot, 'btmodsav', True, 0),      ('td-9', None),
                                ('tr-9', None),
                                ('form-9', None),
                                ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                                ('table-0', None),
                                    ('tr-0', None, False),
                                        ('td-0', None, 1, None, 1, None, None),
                                            ('button-1', 'btmodsav', 'btn btn-primary mt-2', 'Salvar', 'Salvar Registro', 'btsalreg', 'btn btn-primary mt-2', 'Salvar', 'Confirma a gravação?'),
                                        ('td-9', None),
                                        ('td-0', None, 1, None, 1, None, None), ('alt255-0', 2), ('td-9', None),
                                        ('td-0', 'table-active', 1, None, 1, None, None), 
                                            ('button-0', 'btcancel', 'btn btn-primary mt-2', 'Cancelar'),
                                        ('td-9', None),
            ]
            if iidooesp > 0:
                lnewpage = lnewpage + [
                                        ('td-0', None, 1, None, 1, None, None), ('alt255-0', 2), ('td-9', None),
                                        ('td-0', None, 1, None, 1, None, None),    
                                            ('button-1', 'btexclui', 'btn btn-primary mt-2', 'Excluir', 'Excluir Registro', 'btexcreg', 'btn btn-danger mt-2', 'Excluir', 'Confirma a exclusão deste registro?'),
                                        ('td-9', None),
                ]
            lnewpage = lnewpage + [   
                                    ('tr-9', None),
                                ('table-9', None),
                                ('form-9', None),
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
            
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00902_operacional_cadastro_operacoes_eseciais ] ///////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Operações Especiais.                                                                                                      // #
# // Somatória/gravação/exclusão do registro de operação especial.                                                                                       // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00902_operacional_cadastro_operacoes_especiais(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00902_operacional_cadastro_operacoes_especiais(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        iidooesp = dglobaux['iidooesp']
        # Debug: (inicio)
        # abnf_show('09', iidooesp, 0)
        # Debug: (fim)
        if dabnfopg['abnfobj0'] == ['btcancel', 'btcancel']:        # Voltar para tela anterior
            abnf000u13c00900_operacional_cadastro_operacoes_especiais(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btsalreg', 'btsalreg']:
            # /////////////////
            # Gravar o registro
            # /////////////////
            lmfields = []
            lmfields = lmfields + [
                ['ddataope', 'date',     'F', 'data da operação', ['Notnull', 'D', 'Return_date'],    None],
                ['iidolinh', 'select',   'F', 'linha',            ['Return_integer'],                 None],
                ['iveicser', 'number',   'M', 'veículo/serviço',  ['Return_integer'],                 None],
                ['stipodia', 'select',   'M', 'tipo de dia',      ['Notnull', 'D'],                   None],
                ['sdescmot', 'input',    'M', 'motivo',           ['Notnull', 'D'],                   None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btsalreg')
            if bvalidad:
                # Debug: (inicio)
                # abnf_show('10', lmfields, 1)
                # Debug: (fim)
                ddataope = lmfields[0][5]
                iidolinh = lmfields[1][5]
                iveicser = lmfields[2][5]
                stipodia = lmfields[3][5]
                sdescmot = lmfields[4][5]
                # ////////////////////////////
                # Analisando os preenchimentos
                # ////////////////////////////
                if iidolinh == 0 and iveicser > 0:
                    abnf_alert('Não pode haver veículo/serviço definido sem que haja uma linha definida!', 5)
                    abnf_socket_004([5, 'btsalreg'])
                else:
                    # ///////////////////////////////////////////////////
                    # Buscando incompatibilidade com registros existentes
                    # ///////////////////////////////////////////////////
                    lcamposb = ('idooesp', 'dataope', 'idolinh', 'veicser', 'tipodia')
                    lfilbusc = (
                        ('idooesp', '!=', iidooesp),    # ID diferentes
                        ('idfilia', '=',  iidfilia),    # Mesma filial
                        ('dataope', '=',  ddataope),    # Mesma data
                        ('idolinh', '=',  iidolinh),    # Mesma linha
                        ('veicser', '=',  iveicser),    # Mesmo veiculo/serviço
                        ('situreg', '!=', 'C'),         # Registro não cancelado
                    )
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_operacoes_especiais', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 != [] or iqtdre01 > 0:
                        abnf_alert('Já existe um registro destinado a esta data-linha-serviço!', 5)
                        abnf_socket_004([5, 'btsalreg'])
                    else:
                        # /////////////////////////////////////////
                        # Grava a inclusão ou alteração do registro
                        # /////////////////////////////////////////
                        if bvalidad:
                            bvalidad = False
                            if iidooesp > 0:
                                # ////////////////////////////////////////
                                # Buscando o registro de operação especial
                                # ////////////////////////////////////////
                                lcamposb = ('idooesp', 'idfilia')
                                lfilbusc = (('idooesp', '=', iidooesp), ('situreg', '!=', 'C'), None)
                                lorderby = None
                                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_operacoes_especiais', lcamposb, lfilbusc, lorderby)
                                if lsqlre01 == [] or iqtdre01 == 0:
                                    abnf_alert('Erro interno! Não foi encontrado o registro ID ' + str(iidooesp) + '! Entre em contato com o depto. de sistemas!', 4)
                                    abnf_socket_004([5, 'btsalreg'])
                                else:
                                    if lsqlre01[0][1] != iidfilia:
                                        abnf_alert('Alterações não permitidas devido a este registro de operação especial não pertencer a esta filial!', 5)
                                        abnf_socket_004([5, 'btsalreg'])
                                    else:
                                        # //////////////////////
                                        # Atualizando o registro
                                        # //////////////////////
                                        bvalidad = abnf_database_altera_dados_v02(icodbase, sabnproj, 'abnf_operacional_cadastro_operacoes_especiais', iidooesp, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                                        [
                                            ('dataope', ddataope),
                                            ('idolinh', iidolinh),
                                            ('veicser', iveicser),
                                            ('tipodia', stipodia),
                                            ('descmot', sdescmot),
                                        ])
                                        if bvalidad:
                                            abnf_alert('Registro alterado com sucesso!', 3)
                            else:
                                # //////////////////////
                                # Salvando novo registro
                                # //////////////////////
                                bvalidad, iproxiid = abnf_database_insere_dados_v02(icodbase, sabnproj, 'abnf_operacional_cadastro_operacoes_especiais', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                                [
                                    ('dataope', ddataope),
                                    ('idolinh', iidolinh),
                                    ('veicser', iveicser),
                                    ('tipodia', stipodia),
                                    ('descmot', sdescmot),
                                    ('idfilia', iidfilia),
                                    ('situreg', 'A'),
                                ])
                                if bvalidad:
                                    abnf_alert('Registro gravado com sucesso!', 3)
                            if bvalidad:
                                abnf000u13c00900_operacional_cadastro_operacoes_especiais(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btexcreg', 'btexcreg']:
            # //////////////////
            # Excluir o registro
            # //////////////////
            lcamposb = ('idooesp', 'idfilia')
            lfilbusc = (('idooesp', '=', iidooesp), ('situreg', '!=', 'C'), None)
            lorderby = None
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_operacoes_especiais', lcamposb, lfilbusc, lorderby)
            if lsqlre01 == [] or iqtdre01 == 0:
                abnf_alert('Erro interno! Não foi encontrado o registro ID ' + str(iidooesp) + '! Entre em contato com o depto. de sistemas!', 4)
                abnf_socket_004([5, 'btexcreg'])
            elif lsqlre01[0][1] != iidfilia:
                abnf_alert('Alterações não permitidas devido a este registro não pertencer a esta filial!', 5)
                abnf_socket_004([5, 'btexcreg'])
            else:
                # /////////////////
                # Exclui o registro
                # /////////////////
                bvalidad = abnf_database_exclui_registro(icodbase, sabnproj, 'abnf_operacional_cadastro_operacoes_especiais', iidooesp, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'])
                if bvalidad:
                    abnf_alert('Registro excluído com sucesso!', 3)
                    abnf000u13c00900_operacional_cadastro_operacoes_especiais(dabnfopg)
                abnf_socket_004([5, 'btexcreg'])

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00903_operacional_cadastro_operacoes_especiais ] //////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Operações Especiais.                                                                                                      // #
# // Cria a lista de operações especiais da tela inicial.                                                                                                // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00903_operacional_cadastro_operacoes_especiais(icodbase, iidfilia, sfilprio):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00903_operacional_cadastro_operacoes_especiais(...)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    lcamposb = ('idooesp', 'dataope', 'idolinh', 'veicser', 'tipodia', 'descmot')
    lfilbusc = (('idfilia', '=', iidfilia), ('situreg', '!=', 'C'))
    lorderby = ('dataope', 'idolinh', 'veicser', 'idooesp')
    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_operacoes_especiais', lcamposb, lfilbusc, lorderby)
    if lsqlre01 != [] and iqtdre01 > 0:
        drelolin = abnf_database_menu(icodbase, iidfilia, 'D', '1303C', 0, 1, 1)
        lnewpage = [
        # ('table-1', 'table table-bordered table-sm table-responsive border-dark', 'abnftr01', 'lightgreen'),
        ('table-2', 'table table-bordered table-sm table-responsive border-secondary', 1, 1211, 300, 'abnftr01', 'lightgreen'),
            ('tr-0', 'text-white bg-secondary', False),
                ('td-0', None, 8, None, 1, None, None), ('label-0', 'Operações especiais', 'form-control-label'), ('td-9', None),
            ('tr-9', None),
            ('tr-0', None, False),
                ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'Data',            'form-control-label'), ('td-9', None),
                ('td-0', 'table-active', 2, None, 1, None, None), ('label-0', 'Linha',           'form-control-label'), ('td-9', None),
                ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'Veículo/Serviço', 'form-control-label'), ('td-9', None),
                ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'Tipo de dia',     'form-control-label'), ('td-9', None),
                ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'Motivo',          'form-control-label'), ('td-9', None),
                ('td-0', 'table-active', 1, None, 1, None, None), ('td-9', None),
            ('tr-9', None)
        ]
        loperesp = []
        for lauxi001 in lsqlre01:
            iidooesp = lauxi001[0]
            lsemanax = abnf_converte_data_semana(lauxi001[1])
            ddataope = abnf_converte_data(lauxi001[1]) + ' - ' + lsemanax[1]
            iidolinh = lauxi001[2]
            iveicser = lauxi001[3]
            stipodia = abnf_personal_retorna_string(13001, lauxi001[4])[:3]
            sdescmot = lauxi001[5]
            scodolin, sdesolin = drelolin.get(iidolinh, ('[ TODOS ]', '[ TODOS ]'))
            if iveicser == 0: iveicser = '[ TODOS ]'
            bvalidad = False
            if sfilprio == '': bvalidad = True
            else:
                if   sfilprio in str(ddataope): bvalidad = True
                elif sfilprio in scodolin:      bvalidad = True
                elif sfilprio in sdesolin:      bvalidad = True
                elif sfilprio in str(iveicser): bvalidad = True
                elif sfilprio in stipodia:      bvalidad = True
                elif sfilprio in sdescmot:      bvalidad = True
            if bvalidad:
                loperesp.append((ddataope, scodolin, sdesolin, iveicser, stipodia, sdescmot, iidooesp))
        loperesp.sort()
        for lauxi001 in loperesp:
            lnewpage = lnewpage + [
                ('tr-0', None, False),
                    ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '16px', 'brown', lauxi001[0]), ('td-9', None),
                    ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '16px', 'brown', lauxi001[1]), ('td-9', None),
                    ('td-0', None, 1, None, 0, None, None), ('font-0', 'Courier New;', '16px', 'brown', lauxi001[2]), ('td-9', None),
                    ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '16px', 'brown', lauxi001[3]), ('td-9', None),
                    ('td-0', None, 1, None, 0, None, None), ('font-0', 'Courier New;', '16px', None, lauxi001[4]), ('td-9', None),
                    ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '16px', '#B52480', lauxi001[5]), ('td-9', None),
                    ('td-0', None, 1, None, 1, None, None), ('radio-0', 'iidooesp', lauxi001[6], None, 'Courier New', '16px', 'b', 'P', None), ('td-9', None),
                ('tr-9', None)
            ]
        lnewpage = lnewpage + [
            ('table-9', None),
            ('div-9', None),    # <== Esse 'div-9' é uma necessidade pelo uso de 'table-2'.
        ]
        lnewpage = lnewpage + [
        ('table-0', 'table table-bordered table-sm table-responsive'),
            ('tr-0', None, False),
                ('td-0', None, 1, None, 1, 1, None),
                    ('button-0', 'btselreg', 'btn btn-primary mt-1', 'Abrir registro selecionado'),
                ('td-9', None),
                ('td-0', None, 1, None, 2, 1, None),
                    ('label-0',  'Filtro:', 'form-control-label'),
                ('td-9', None),
                ('td-0', None, 1, None, 1, 1, None),
                    ('alt255-0', 20),
                ('td-9', None),                
                ('td-0', None, 1, None, 1, 1, None),
                    ('input-0',  'sfilprio', 'form-control', 0, 20, '16px', None, 'btfilreg', True, 0),
                ('td-9', None),
                ('td-0', None, 1, None, 1, 1, None),
                    ('alt255-0', 1),
                ('td-9', None),
                ('td-0', None, 1, None, 1, 1, None),
                    ('button-0', 'btfilreg', 'btn btn-primary mt-1', 'Filtrar registros'),
                ('td-9', None),
                ('td-0', None, 1, None, 1, 1, None),
                    ('button-0', 'btrelcad', 'btn btn-primary mt-1', 'Relação de operações especiais cadastradas'),
                ('td-9', None),
            ('tr-9', None),
        ('table-9', None)]
        # //////////////
        # Atualiza a DIV
        # //////////////
        snewpage = abnf_create_page(lnewpage)
        abnf_socket_004([1, 'sdivprio', snewpage])

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00904_operacional_cadastro_operacoes_especiais ] //////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Operações Especiais.                                                                                                      // #
# // Relatórios.                                                                                                                                         // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00904_operacional_cadastro_operacoes_especiais(dabnfopg, sfilprio):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00904_operacional_cadastro_operacoes_especiais(...)')
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
        drelolin = abnf_database_menu(icodbase, iidfilia, 'D', '1303C', 0, 1, 1)
        # ///////////////////
        # Gerando o relatório
        # ///////////////////
        sarqurel = abnf_imprime_file(0, sabntoke)
        with open('abnftmp/' + sarqurel, 'w') as sarquwri:
            snomeemp, snomefil = abnf_database_retorna_empresa_filial(icodbase, iidfilia)
            abnf_imprime_doctype_head_fhead_body_form_table_thead(sarquwri, 3)
            abnf_imprime_thead_001_abeinfo_sistemas(sarquwri, icolspan)
            abnf_imprime_thead_002_titulo_relatorio(sarquwri, icolspan, 'RELAÇÃO DE OPERAÇÕES ESPECIAIS')
            abnf_imprime_thead_003_empresa_filial(sarquwri, icolspan, snomeemp, snomefil)
            # smensage = 'Per&iacute;odo: ' + abnf_converte_data(ddataini) + ' &agrave;s ' + abnf_converte_hora(thoraini) + ' at&eacute; ' + abnf_converte_data(ddatafim) + ' &agrave;s ' + abnf_converte_hora(thorafim)
            # abnf_imprime_thead_004_parametros(sarquwri, icolspan, smensage)
            abnf_imprime_thead_005_datetime(sarquwri, icolspan)
            abnf_imprime_fthead_tbody(sarquwri)
            # /////////////////////////////////////////
            # Mostra o filtro caso ele tenha sido usado
            # /////////////////////////////////////////
            if sfilprio != '':
                abnf_imprime_info_001(sarquwri, None, None, 1,
                    [
                        ('Filtro: [' + sfilprio + ']', icolspan, 0, None, 'center', 'black', 'Courier New', ifontlen + 1, True, False),
                    ]
                )
            abnf_imprime_line(sarquwri, icolspan, 'darkcyan')
            abnf_imprime_info_001(sarquwri, '#D1C5C5', None, 1,
                [
                    ('Data',             1, 0, None, 'center', 'black', 'Courier New', ifontlen + 1, True, False),
                    ('Linha',            2, 0, None, 'center', 'black', 'Courier New', ifontlen + 1, True, False),
                    ('Veículo/Serviço',  1, 0, None, 'center', 'black', 'Courier New', ifontlen + 1, True, False),
                    ('Motivo',           1, 0, None, 'center', 'black', 'Courier New', ifontlen + 1, True, False),
                    ('Tipo de dia',      1, 0, None, 'center', 'black', 'Courier New', ifontlen + 1, True, False),
                ]
            )
            # ///////////////////////////////////////////////
            # Busca todos os registros de operações especiais
            # ///////////////////////////////////////////////
            lcamposb = ('idooesp', 'dataope', 'idolinh', 'veicser', 'tipodia', 'descmot')
            lfilbusc = (('idfilia', '=', iidfilia), ('situreg', '!=', 'C'))
            lorderby = ('dataope', 'idolinh', 'veicser', 'idooesp')
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_operacoes_especiais', lcamposb, lfilbusc, lorderby)
            loperesp = []
            for lauxi001 in lsqlre01:
                iidooesp = lauxi001[0]
                lsemanax = abnf_converte_data_semana(lauxi001[1])
                ddataope = abnf_converte_data(lauxi001[1]) + ' - ' + lsemanax[1]
                iidolinh = lauxi001[2]
                iveicser = lauxi001[3]
                stipodia = abnf_personal_retorna_string(13001, lauxi001[4])[:3]
                sdescmot = lauxi001[5]
                scodolin, sdesolin = drelolin.get(iidolinh, ('[ TODOS ]', '[ TODOS ]'))
                if iveicser == 0: iveicser = '[ TODOS ]'
                bvalidad = False
                if sfilprio == '': bvalidad = True
                else:
                    if   sfilprio in str(ddataope): bvalidad = True
                    elif sfilprio in scodolin:      bvalidad = True
                    elif sfilprio in sdesolin:      bvalidad = True
                    elif sfilprio in str(iveicser): bvalidad = True
                    elif sfilprio in stipodia:      bvalidad = True
                    elif sfilprio in sdescmot:      bvalidad = True
                if bvalidad:
                    loperesp.append((ddataope, scodolin, sdesolin, iveicser, stipodia, sdescmot))
            loperesp.sort()
            for lauxi001 in loperesp:
                abnf_imprime_info_001(sarquwri, None, None, 1,
                    [
                        (lauxi001[0], 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                        (lauxi001[1], 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                        (lauxi001[2], 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                        (lauxi001[3], 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                        (lauxi001[4], 1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                        (lauxi001[5], 1, 0, None, 'center', 'black', 'Courier New', ifontlen, True, False),
                    ]
                )
                icontreg += 1
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