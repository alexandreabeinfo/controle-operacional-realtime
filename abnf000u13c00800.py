## =======================================================================
## [abnf000u13c00800.py] - Operacional - Cadastro de Prioridades de Linhas
## =======================================================================

from abnfsrc.abnf000u00s00003 import *              # Arquivo de funções comuns que serão utilizadas por todos os módulos do sistema
from abnfsrc.abnf000u00s00004 import *              # Arquivo de banco de dados

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00800_operacional_cadastro_prioridades_linhas ] ///////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Prioridades de Linhas.                                                                                                    // #
# // Form inicial.                                                                                                                                       // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00800_operacional_cadastro_prioridades_linhas(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00800_operacional_cadastro_prioridades_linhas(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, '13C00801A'])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        lnewpage = [
            ('div-0', 'container', None, None),
            ('hr-0', None),
            ('div-0', 'row', None, None),
            ('div-0', 'col d-flex justify-content-center', None, None),
            ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
            ('legend-0', 'Operacional - Cadastro de Prioridades de Linhas'),
            ('hr-0', None),
            ('div-1', 'sdivprio'),
            ('div-9', None),
            ('hr-0', None),
            ('button-0', 'btnovpri', 'btn btn-primary mt-2', 'Nova prioridade de linha'),
            ('form-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
        ]
        snewpage = abnf_create_page(lnewpage)
        abnf_socket_004([1, 'abnfdv03', snewpage])
        abnf000u13c00803_operacional_cadastro_prioridades_linhas(icodbase, iidfilia, 1, '')
        
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00801_operacional_cadastro_prioridades_linhas ] ///////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Prioridades de Linhas.                                                                                                    // #
# // Form de inclusão/alteração/exclusão do registro principal de prioridade.                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00801_operacional_cadastro_prioridades_linhas(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00801_operacional_cadastro_prioridades_linhas(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        if dabnfopg['abnfobj0'] == ['btfilpri', 'btfilpri']:        # Filtrar prioridades
            lmfields = [
                ['sfilprio', 'input', 'M', 'filtro de prioridades', [], None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btfilpri')
            if bvalidad:
                sfilprio = lmfields[0][5]
                abnf000u13c00803_operacional_cadastro_prioridades_linhas(icodbase, iidfilia, 1, sfilprio)
            bvalidad = False    # => Para não entrar na parte que monta a tela principal
        elif dabnfopg['abnfobj0'] == ['btvingrf', 'btvingrf']:      # Vincular grupos de veículos
            # ///////////////////////////////////
            # Buscando uma prioridade selecionada
            # ///////////////////////////////////
            lmfields = [
                ['iidoplin', 'radio', 'Nenhum registro de prioridade foi selecionado', ['Notnull', 'Return_integer'], None],
            ]
            bvalidad, lmfields = abnf_find_checkbox_radio(dabnfopg, lmfields, 'btvingrf')
            if bvalidad:
                iidoplin = lmfields[0][4]
                abnf000u13c00804_operacional_cadastro_prioridades_linhas(dabnfopg, iidoplin)
            bvalidad = False    # => Para não entrar na parte que monta a tela principal
        elif dabnfopg['abnfobj0'] == ['btrelcad', 'btrelcad']:      # Relação de prioridades cadastradas
            lmfields = [
                ['sfilprio', 'input', 'M', 'filtro de prioridades', [], None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btfilpri')
            if bvalidad:
                sfilprio = lmfields[0][5]
                abnf000u13c00807_operacional_cadastro_prioridades_linhas(dabnfopg, sfilprio)
            bvalidad = False    # => Para não entrar na parte que monta a tela principal
        elif dabnfopg['abnfobj0'] == ['btnovpri', 'btnovpri']:        # Novo registro
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidoplin', 0),)]) # ==> Guardado dados da prioridade para a próxima função. Obs: tem que ter essa vírgula: "),)])"
            iidoplin = 0
            iordprio = None
            iidolinh = None
            iveicser = None
            iidveicu = None
            btpdiaut = False
            btpdiasa = False
            btpdiado = False
            btpdiafe = False
            btpdia2a = False
            btpdia3a = False
            btpdia4a = False
            btpdia5a = False
            btpdia6a = False
            ssitureg = None
            bvalidad = True
        elif dabnfopg['abnfobj0'] == ['btselreg', 'btselreg']:
            # ///////////////////////////////////
            # Buscando uma prioridade selecionada
            # ///////////////////////////////////
            lmfields = [
                ['iidoplin', 'radio', 'Nenhum registro de prioridade foi selecionado', ['Notnull', 'Return_integer'], None],
            ]
            bvalidad, lmfields = abnf_find_checkbox_radio(dabnfopg, lmfields, 'btselreg')
            if bvalidad:
                iidoplin = lmfields[0][4]
                # /////////////////////////////////
                # Buscando o registro de prioridade
                # /////////////////////////////////
                lcamposb = ('ordprio', 'idoplin', 'idolinh', 'veicser', 'idveicu', 'tpdiaut', 'tpdiasa', 'tpdiado', 'tpdiafe', 'tpdia2a', 'tpdia3a', 'tpdia4a', 'tpdia5a', 'tpdia6a', 'situreg')
                lfilbusc = (('idoplin', '=', iidoplin), ('situreg', '!=', 'C'))
                lorderby = None
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_prioridades_linhas', lcamposb, lfilbusc, lorderby)
                if lsqlre01 == [] or iqtdre01 == 0:
                    abnf_alert('Registro de prioridade não encontrado! Entre em contato com o depto. de sistemas!', 4)
                    abnf_socket_004([5, 'btselreg'])
                    bvalidad = False
                else:
                    iordprio = lsqlre01[0][0]
                    iidoplin = lsqlre01[0][1]
                    iidolinh = lsqlre01[0][2]
                    iveicser = lsqlre01[0][3]
                    iidveicu = lsqlre01[0][4]
                    btpdiaut = lsqlre01[0][5]
                    btpdiasa = lsqlre01[0][6]
                    btpdiado = lsqlre01[0][7]
                    btpdiafe = lsqlre01[0][8]
                    btpdia2a = lsqlre01[0][9]
                    btpdia3a = lsqlre01[0][10]
                    btpdia4a = lsqlre01[0][11]
                    btpdia5a = lsqlre01[0][12]
                    btpdia6a = lsqlre01[0][13]
                    ssitureg = lsqlre01[0][14]
                    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidoplin', iidoplin),)]) # ==> Guardado dados do registro de prioridade para a próxima função. Obs: tem que ter essa vírgula: "),)])"
                abnf_socket_004([5, 'btselreg'])
        if bvalidad:
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '13C00802A'),)]) # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
            # //////////////////////////
            # Buscas em tabelas externas
            # //////////////////////////
            lidolinh = abnf_database_menu(icodbase, iidfilia, 'L', '1303', 1, 2, 1)
            lidveicu = abnf_database_menu(icodbase, iidfilia, 'L', '0201', 1, 2, 0)
            # /// #
            if iidoplin > 0:
                sauxi001 = '[ Registro existente ]'
                sauxi002 = 'ssitureg'
            else:
                sauxi001 = '[ Novo registro ]'
                sauxi002 = 'btmodsav'
            lnewpage = [
                ('div-0', 'container', None, None),
                ('hr-0', None),
                ('div-0', 'row', None, None),
                ('div-0', 'col d-flex justify-content-center', None, None),
                ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                ('table-0', 'table table-bordered table-sm table-responsive'),
                    ('tr-0', 'text-white bg-secondary', False),
                        ('td-0', None, 2, None, 1, None, None),
                            ('legend-0', 'Cadastro de Prioridades de Linhas - ' + sauxi001),
                        ('td-9', None),
                    ('tr-9', None),
                    ('tr-0', None, False),
                        ('td-0', None, None, None, None, None, None),
                            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                            ('table-0', 'table table-bordered table-sm table-responsive'),
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None), ('label-0', 'Ordem de prioridade (vazio para por no final)', 'form-control-label'),         ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),           ('label-0', '&nbsp;', 'form-control-label'),                                                ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),           ('number-0', 'iordprio', 'form-control', 0, 6, '16px', iordprio, 'iidolinh', True, None),   ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None), ('label-0', 'Linha', 'form-control-label'),                                                 ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),           ('label-0', '&nbsp;', 'form-control-label'),                                                ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),           ('select-0', 'iidolinh', 'form-control', '16px', 'iveicser', lidolinh, 1, iidolinh, False), ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None), ('label-0', 'Veículo/serviço', 'form-control-label'),                                       ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),           ('label-0', '&nbsp;', 'form-control-label'),                                                ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),           ('number-0', 'iveicser', 'form-control', 0, 6, '16px', iveicser, 'iidveicu', True, None),   ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None), ('label-0', 'Veículo oficial (opcional)', 'form-control-label'),                            ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),           ('label-0', '&nbsp;', 'form-control-label'),                                                ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),           ('select-0', 'iidveicu', 'form-control', '16px', sauxi002, lidveicu, 1, iidveicu, False),   ('td-9', None),
                                ('tr-9', None),
            ]
            if iidoplin > 0:
                lauxi001 = ('select-0', 'ssitureg', 'form-control', '16px', 'btmodsav', abnf_personal_retorna_lista(10001), 0, ssitureg, False)
                lnewpage = lnewpage + [
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None),   ('label-0', 'Situação do registro', 'form-control-label'),                                ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),             ('label-0', '&nbsp;', 'form-control-label'),                                              ('td-9', None),
                                    ('td-0', None, 3, None, 0, None, None),             lauxi001,                                                                                 ('td-9', None),
                                ('tr-9', None),
                ]
            lnewpage = lnewpage + [
                                ('table-0', 'table table-bordered table-sm table-responsive border-secondary'),
                                    ('tr-0', None, False),
                                        ('td-0', 'table-active', 10, None, 1, None, None), ('label-0', 'Tipos de dia', 'form-control-label'), ('td-9', None),
                                    ('tr-9', None),
                                    ('tr-0', None, False),
                                        ('td-0', 'table-active',  1, None, 1, None, None), ('label-0', 'Dia útil', 'form-control-label'), ('td-9', None),
                                        ('td-0', 'table-active',  1, None, 1, None, None), ('label-0', 'Sábado',   'form-control-label'), ('td-9', None),
                                        ('td-0', 'table-active',  1, None, 1, None, None), ('label-0', 'Domingo',  'form-control-label'), ('td-9', None),
                                        ('td-0', 'table-active',  1, None, 1, None, None), ('label-0', 'Feriado',  'form-control-label'), ('td-9', None),
                                        ('td-0', 'table-active',  1, None, 1, None, None), ('label-0', 'Segunda',  'form-control-label'), ('td-9', None),
                                        ('td-0', 'table-active',  1, None, 1, None, None), ('label-0', 'Terça',    'form-control-label'), ('td-9', None),
                                        ('td-0', 'table-active',  1, None, 1, None, None), ('label-0', 'Quarta',   'form-control-label'), ('td-9', None),
                                        ('td-0', 'table-active',  1, None, 1, None, None), ('label-0', 'Quinta',   'form-control-label'), ('td-9', None),
                                        ('td-0', 'table-active',  1, None, 1, None, None), ('label-0', 'Sexta',    'form-control-label'), ('td-9', None),
                                    ('tr-9', None),
                                    ('tr-0', None, False),
                                        ('td-0', None, 1, None,  1, None, None), ('checkbox-0', 'btpdiaut', 1, (1 if btpdiaut else 0), 'Courier New', '16px', 'b', 'P', None), ('td-9', None),
                                        ('td-0', None, 1, None,  1, None, None), ('checkbox-0', 'btpdiasa', 1, (1 if btpdiasa else 0), 'Courier New', '16px', 'b', 'P', None), ('td-9', None),
                                        ('td-0', None, 1, None,  1, None, None), ('checkbox-0', 'btpdiado', 1, (1 if btpdiado else 0), 'Courier New', '16px', 'b', 'P', None), ('td-9', None),
                                        ('td-0', None, 1, None,  1, None, None), ('checkbox-0', 'btpdiafe', 1, (1 if btpdiafe else 0), 'Courier New', '16px', 'b', 'P', None), ('td-9', None),
                                        ('td-0', None, 1, None,  1, None, None), ('checkbox-0', 'btpdia2a', 1, (1 if btpdia2a else 0), 'Courier New', '16px', 'b', 'P', None), ('td-9', None),
                                        ('td-0', None, 1, None,  1, None, None), ('checkbox-0', 'btpdia3a', 1, (1 if btpdia3a else 0), 'Courier New', '16px', 'b', 'P', None), ('td-9', None),
                                        ('td-0', None, 1, None,  1, None, None), ('checkbox-0', 'btpdia4a', 1, (1 if btpdia4a else 0), 'Courier New', '16px', 'b', 'P', None), ('td-9', None),
                                        ('td-0', None, 1, None,  1, None, None), ('checkbox-0', 'btpdia5a', 1, (1 if btpdia5a else 0), 'Courier New', '16px', 'b', 'P', None), ('td-9', None),
                                        ('td-0', None, 1, None,  1, None, None), ('checkbox-0', 'btpdia6a', 1, (1 if btpdia6a else 0), 'Courier New', '16px', 'b', 'P', None), ('td-9', None),
                                    ('tr-9', None),
                                ('table-9', None),
                                # ==> ('form-9', None),
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
            if iidoplin > 0:
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
# // [ abnf000u13c00802_operacional_cadastro_prioridades_linhas ] ///////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Prioridades de Linhas.                                                                                                    // #
# // Somatória/gravação/exclusão do registro principal de prioridade.                                                                                    // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00802_operacional_cadastro_prioridades_linhas(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00802_operacional_cadastro_prioridades_linhas(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        iidoplin = dglobaux['iidoplin']
        # Debug: (inicio)
        # abnf_show('09', iidoplin, 0)
        # Debug: (fim)
        if dabnfopg['abnfobj0'] == ['btcancel', 'btcancel']:        # Voltar para tela anterior
            abnf000u13c00800_operacional_cadastro_prioridades_linhas(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btsalreg', 'btsalreg']:
            # ///////////////////////////
            # Gravar o registro principal
            # ///////////////////////////
            lmfields = []
            lmfields = lmfields + [
                ['iordprio', 'number',   'F', 'ordem de prioridade', ['Return_integer', 'Empty_to_zero'], None],
                ['iidolinh', 'select',   'F', 'linha',               ['Notnull', 'D', 'Return_integer'],  None],
                ['iveicser', 'number',   'M', 'veículo/serviço',     ['Notnull', 'D', 'Notzero'],         None],
                ['iidveicu', 'select',   'M', 'veículo oficial',     ['Return_integer', 'Empty_to_zero'], None],
                ['btpdiaut', 'checkbox', 'M', 'dia útil',            [],                                  None],
                ['btpdiasa', 'checkbox', 'M', 'sábado',              [],                                  None],
                ['btpdiado', 'checkbox', 'M', 'domingo',             [],                                  None],
                ['btpdiafe', 'checkbox', 'M', 'feriado',             [],                                  None],
                ['btpdia2a', 'checkbox', 'M', 'segunda',             [],                                  None],
                ['btpdia3a', 'checkbox', 'M', 'terça',               [],                                  None],
                ['btpdia4a', 'checkbox', 'M', 'quarta',              [],                                  None],
                ['btpdia5a', 'checkbox', 'M', 'quinta',              [],                                  None],
                ['btpdia6a', 'checkbox', 'M', 'sexta',               [],                                  None],
            ]
            if iidoplin > 0: lmfields = lmfields + [
                ['ssitureg', 'select',   'F', 'situação do registro', ['Notnull', 'D'],                    None],
            ]            
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btsalreg')
            if bvalidad:
                # Debug: (inicio)
                # abnf_show('10', lmfields, 1)
                # Debug: (fim)
                iordprio = lmfields[0][5]
                iidolinh = lmfields[1][5]
                iveicser = lmfields[2][5]
                iidveicu = lmfields[3][5]
                btpdiaut = lmfields[4][5]
                btpdiasa = lmfields[5][5]
                btpdiado = lmfields[6][5]
                btpdiafe = lmfields[7][5]
                btpdia2a = lmfields[8][5]
                btpdia3a = lmfields[9][5]
                btpdia4a = lmfields[10][5]
                btpdia5a = lmfields[11][5]
                btpdia6a = lmfields[12][5]
                if iidoplin > 0:
                    ssitureg = lmfields[13][5]
                if iordprio == 0:
                    iordprio = 999999
                # ////////////////////////////
                # Analisando os preenchimentos
                # ////////////////////////////
                if ((btpdiaut == False) and
                    (btpdiasa == False) and
                    (btpdiado == False) and
                    (btpdiafe == False) and
                    (btpdia2a == False) and
                    (btpdia3a == False) and
                    (btpdia4a == False) and
                    (btpdia5a == False) and
                    (btpdia6a == False)):
                    abnf_alert('Pelo menos um tipo de dia precisa ser definido!', 5)
                    abnf_socket_004([5, 'btsalreg'])
                elif ((btpdiaut == True) and (
                    (btpdia2a == True) or
                    (btpdia3a == True) or
                    (btpdia4a == True) or
                    (btpdia5a == True) or
                    (btpdia6a == True))):
                    abnf_alert('O dia útil não pode ser marcado junto com segunda, terça, quarta, quinta ou sexta!', 5)
                    abnf_socket_004([5, 'btsalreg'])
                else:
                    # ///////////////////////////////////////////////////
                    # Buscando incompatibilidade com registros existentes
                    # ///////////////////////////////////////////////////
                    lcamposb = ('idoplin', 'ordprio', 'idolinh', 'veicser', 'idveicu', 'tpdiaut', 'tpdiasa', 'tpdiado', 'tpdiafe', 'tpdia2a', 'tpdia3a', 'tpdia4a', 'tpdia5a', 'tpdia6a')
                    lfilbusc = (('idfilia', '=', iidfilia), ('situreg', '!=', 'C'), None)
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_prioridades_linhas', lcamposb, lfilbusc, lorderby)
                    for lauxi001 in lsqlre01:
                        idoplinx = lauxi001[0]
                        iordprix = lauxi001[1]
                        iidolinx = lauxi001[2]
                        iveicsex = lauxi001[3]
                        iidveicx = lauxi001[4]
                        btpdiaux = lauxi001[5]
                        btpdiasx = lauxi001[6]
                        btpdiadx = lauxi001[7]
                        btpdiafx = lauxi001[8]
                        btpdia2x = lauxi001[9]
                        btpdia3x = lauxi001[10]
                        btpdia4x = lauxi001[11]
                        btpdia5x = lauxi001[12]
                        btpdia6x = lauxi001[13]
                        # ////////////////////////////////////////////////////
                        # Comparação feita somente quando não tiver o mesmo ID
                        # ////////////////////////////////////////////////////
                        if iidoplin != idoplinx:
                            # ///////////////////////////////////////////////////////////////////////////////
                            # Comparação feita somente quando for o(s) mesmo(s) tipo(s) de dia selecionado(s)
                            # ///////////////////////////////////////////////////////////////////////////////
                            if ((btpdiaut == True and btpdiaut == btpdiaux) or
                                (btpdiasa == True and btpdiasa == btpdiasx) or
                                (btpdiado == True and btpdiado == btpdiadx) or
                                (btpdiafe == True and btpdiafe == btpdiafx) or
                                (btpdia2a == True and btpdia2a == btpdia2x) or
                                (btpdia3a == True and btpdia3a == btpdia3x) or
                                (btpdia4a == True and btpdia4a == btpdia4x) or
                                (btpdia5a == True and btpdia5a == btpdia5x) or
                                (btpdia6a == True and btpdia6a == btpdia6x)):
                                # //////////////////////////////////////////////
                                # Analisando mesma linha e mesmo veículo/serviço
                                # //////////////////////////////////////////////
                                if iidolinh == iidolinx:        # Mesma linha
                                    if iveicser == iveicsex:    # Mesmo serviço
                                        abnf_alert('Ja existe um registro destinado a esta linha-serviço para o(s) tipo(s) de dia selecionado(s)!', 5)
                                        abnf_socket_004([5, 'btsalreg'])
                                        bvalidad = False
                                        break
                                # ////////////////////////////////
                                # Analisando mesmo veículo oficial
                                # ////////////////////////////////
                                if iidveicu > 0:                # Veículo oficial definido
                                    if iidveicu == iidveicx:    # Mesmo veículo oficial
                                        abnf_alert('O veículo oficial selecionado ja esta sendo utilizado em outro registro com o(s) tipo(s) de dia selecionado(s)!', 5)
                                        abnf_socket_004([5, 'btsalreg'])
                                        bvalidad = False
                                        break
                    # /////////////////////////////////////////
                    # Grava a inclusão ou alteração do registro
                    # /////////////////////////////////////////
                    if bvalidad:
                        bvalidad = False
                        if iidoplin > 0:
                            # ///////////////////////////////////////////
                            # Buscando o registro principal de prioridade
                            # ///////////////////////////////////////////
                            lcamposb = ('idoplin', 'idfilia')
                            lfilbusc = (('idoplin', '=', iidoplin), ('situreg', '!=', 'C'), None)
                            lorderby = None
                            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_prioridades_linhas', lcamposb, lfilbusc, lorderby)
                            if lsqlre01 == [] or iqtdre01 == 0:
                                abnf_alert('Erro interno! Não foi encontrado o registro ID ' + str(iidoplin) + '! Entre em contato com o depto. de sistemas!', 4)
                                abnf_socket_004([5, 'btsalreg'])
                            else:
                                if lsqlre01[0][1] != iidfilia:
                                    abnf_alert('Alterações não permitidas devido a este registro de prioridade não pertencer a esta filial!', 5)
                                    abnf_socket_004([5, 'btsalreg'])
                                else:
                                    # ////////////////////////////////
                                    # Atualizando o registro principal
                                    # ////////////////////////////////
                                    bvalidad = abnf_database_altera_dados_v02(icodbase, sabnproj, 'abnf_operacional_cadastro_prioridades_linhas', iidoplin, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                                    [
                                        ('ordprio', iordprio),
                                        ('idolinh', iidolinh),
                                        ('veicser', iveicser),
                                        ('idveicu', iidveicu),
                                        ('tpdiaut', btpdiaut),
                                        ('tpdiasa', btpdiasa),
                                        ('tpdiado', btpdiado),
                                        ('tpdiafe', btpdiafe),
                                        ('tpdia2a', btpdia2a),
                                        ('tpdia3a', btpdia3a),
                                        ('tpdia4a', btpdia4a),
                                        ('tpdia5a', btpdia5a),
                                        ('tpdia6a', btpdia6a),
                                        ('situreg', ssitureg),
                                    ])
                                    if bvalidad:
                                        abnf_alert('Registro principal alterado com sucesso!', 3)
                        else:
                            # ////////////////////////////////
                            # Salvando novo registro principal
                            # ////////////////////////////////
                            bvalidad, iproxiid = abnf_database_insere_dados_v02(icodbase, sabnproj, 'abnf_operacional_cadastro_prioridades_linhas', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                            [
                                ('ordprio', iordprio),
                                ('idolinh', iidolinh),
                                ('veicser', iveicser),
                                ('idveicu', iidveicu),
                                ('tpdiaut', btpdiaut),
                                ('tpdiasa', btpdiasa),
                                ('tpdiado', btpdiado),
                                ('tpdiafe', btpdiafe),
                                ('tpdia2a', btpdia2a),
                                ('tpdia3a', btpdia3a),
                                ('tpdia4a', btpdia4a),
                                ('tpdia5a', btpdia5a),
                                ('tpdia6a', btpdia6a),
                                ('idfilia', iidfilia),
                                ('situreg', 'A'),
                            ])
                            if bvalidad:
                                abnf_alert('Registro principal de prioridade gravado com sucesso!', 3)
                        if bvalidad:
                            # ///////////////////////////////////////////////////////
                            # Reorganiza a prioridade de todos os registros da tabela
                            # ///////////////////////////////////////////////////////
                            lreorgan = []
                            icontord = 0
                            lcamposb = ('idoplin', 'ordprio')
                            lfilbusc = (('idfilia', '=', iidfilia), ('situreg', '!=', 'C'), None)
                            lorderby = ('ordprio', 'idoplin')
                            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_prioridades_linhas', lcamposb, lfilbusc, lorderby)
                            for laux001 in lsqlre01:
                                icontord += 1
                                lreorgan.append((laux001[0], laux001[1], icontord))
                            for laux001 in lreorgan:
                                if laux001[1] != laux001[2]:
                                    bvalidad = abnf_database_altera_dados_v02(icodbase, sabnproj, 'abnf_operacional_cadastro_prioridades_linhas', laux001[0], dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                                    [
                                        ('ordprio', laux001[2]),
                                    ], False)
                            abnf000u13c00800_operacional_cadastro_prioridades_linhas(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btexcreg', 'btexcreg']:
            # ////////////////////////////
            # Excluir o registro principal
            # ////////////////////////////
            lcamposb = ('idoplin', 'idfilia')
            lfilbusc = (('idoplin', '=', iidoplin), ('situreg', '!=', 'C'), None)
            lorderby = None
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_prioridades_linhas', lcamposb, lfilbusc, lorderby)
            if lsqlre01 == [] or iqtdre01 == 0:
                abnf_alert('Erro interno! Não foi encontrado o registro ID ' + str(iidoplin) + '! Entre em contato com o depto. de sistemas!', 4)
                abnf_socket_004([5, 'btexcreg'])
            elif lsqlre01[0][1] != iidfilia:
                abnf_alert('Alterações não permitidas devido a esta prioridade de linha não pertencer a esta filial!', 5)
                abnf_socket_004([5, 'btexcreg'])
            else:
                # /////////////////////////////////////////////////////////
                # Busca grupos de veículos vinculados ao registro principal
                # /////////////////////////////////////////////////////////
                lcamposb = ('idoplin', None)
                lfilbusc = (('idoplin', '=', iidoplin), ('situreg', '!=', 'C'), None)
                lorderby = None
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_prioridades_linhas_gv', lcamposb, lfilbusc, lorderby)
                if lsqlre01 != [] or iqtdre01 != 0:
                    abnf_alert('Este registro não pode ser excluído enquanto tiver registros de grupos de veículos vinculados a ele!', 5)
                    bvalidad = False
                else:
                    # ///////////////////////////
                    # Exclui o registro principal
                    # ///////////////////////////
                    bvalidad = abnf_database_exclui_registro(icodbase, sabnproj, 'abnf_operacional_cadastro_prioridades_linhas', iidoplin, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'])
                    if bvalidad:
                        abnf_alert('Prioridade de linha excluída com sucesso!', 3)
                        abnf000u13c00800_operacional_cadastro_prioridades_linhas(dabnfopg)
                abnf_socket_004([5, 'btexcreg'])

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00803_operacional_cadastro_prioridades_linhas ] ///////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Prioridades de Linhas.                                                                                                    // #
# // Cria a lista de prioridades de linha da tela inicial.                                                                                               // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00803_operacional_cadastro_prioridades_linhas(icodbase, iidfilia, iparfunc, sfilprio):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00803_operacional_cadastro_prioridades_linhas(...)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    # Prioridades
    lcamposb = ('idoplin', 'ordprio', 'idolinh', 'veicser', 'idveicu', 'tpdiaut', 'tpdiasa', 'tpdiado', 'tpdiafe', 'tpdia2a', 'tpdia3a', 'tpdia4a', 'tpdia5a', 'tpdia6a', 'situreg')
    lfilbusc = (('idfilia', '=', iidfilia), ('situreg', '!=', 'C'))
    lorderby = ('ordprio', 'idoplin')
    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_prioridades_linhas', lcamposb, lfilbusc, lorderby)
    # Relação de prioridades disponíveis
    if lsqlre01 != [] and iqtdre01 > 0:
        drelolin = abnf_database_menu(icodbase, iidfilia, 'D', '1303C', 0, 1, 1)
        drelveic = abnf_database_menu(icodbase, iidfilia, 'D', '0201', 0, 1, 2)
        lnewpage = [
        # ('table-1', 'table table-bordered table-sm table-responsive border-dark', 'abnftr01', 'lightgreen'),
        ('table-2', 'table table-bordered table-sm table-responsive border-secondary', 1, 1211, 300, 'abnftr01', 'lightgreen'),
            ('tr-0', 'text-white bg-secondary', False),
                ('td-0', None, 8, None, 1, None, None), ('label-0', 'Prioridades de linhas', 'form-control-label'), ('td-9', None),
            ('tr-9', None),
            ('tr-0', None, False),
                ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'Prioridade',      'form-control-label'), ('td-9', None),
                ('td-0', 'table-active', 2, None, 1, None, None), ('label-0', 'Linha',           'form-control-label'), ('td-9', None),
                ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'Tipos dia',       'form-control-label'), ('td-9', None),
                ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'Veículo/Serviço', 'form-control-label'), ('td-9', None),
                ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'Veículo oficial', 'form-control-label'), ('td-9', None),
                ('td-0', 'table-active', 1, None, 1, None, None), ('label-0', 'Situação',        'form-control-label'), ('td-9', None),
                ('td-0', 'table-active', 1, None, 1, None, None), ('td-9', None),
            ('tr-9', None)
        ]
        for lauxi001 in lsqlre01:
            iidoplin = lauxi001[0]
            iordprio = lauxi001[1]
            iidolinh = lauxi001[2]
            iveicser = lauxi001[3]
            iidveicu = lauxi001[4]
            stipodia = ''
            stipodia = stipodia + 'U' if lauxi001[5]  else stipodia + ''
            stipodia = stipodia + 'S' if lauxi001[6]  else stipodia + ''
            stipodia = stipodia + 'D' if lauxi001[7]  else stipodia + ''
            stipodia = stipodia + 'F' if lauxi001[8]  else stipodia + ''
            stipodia = stipodia + '2' if lauxi001[9]  else stipodia + ''
            stipodia = stipodia + '3' if lauxi001[10] else stipodia + ''
            stipodia = stipodia + '4' if lauxi001[11] else stipodia + ''
            stipodia = stipodia + '5' if lauxi001[12] else stipodia + ''
            stipodia = stipodia + '6' if lauxi001[13] else stipodia + ''
            scodolin, sdesolin = drelolin.get(iidolinh, ('', ''))
            sidveicu = drelveic.get(iidveicu, '') if iidveicu > 0 else ''
            ssitureg = abnf_personal_retorna_string(10001, lauxi001[14])
            bvalidad = False
            if sfilprio == '': bvalidad = True
            else:
                if   sfilprio in str(iordprio): bvalidad = True
                elif sfilprio in scodolin:      bvalidad = True
                elif sfilprio in sdesolin:      bvalidad = True
                elif sfilprio in stipodia:      bvalidad = True
                elif sfilprio in str(iveicser): bvalidad = True
                elif sfilprio in sidveicu:      bvalidad = True
                elif sfilprio in ssitureg:      bvalidad = True
            if bvalidad:
                lnewpage = lnewpage + [
                    ('tr-0', None, False),
                        ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '16px', 'brown', iordprio), ('td-9', None),
                        ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '16px', None, scodolin), ('td-9', None),
                        ('td-0', None, 1, None, 0, None, None), ('font-0', 'Courier New;', '16px', None, sdesolin), ('td-9', None),
                        ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '16px', '#B52480', stipodia), ('td-9', None),
                        ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '16px', None, iveicser), ('td-9', None),
                        ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '16px', None, sidveicu), ('td-9', None),
                        ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '16px', None, ssitureg), ('td-9', None),
                        ('td-0', None, 1, None, 1, None, None), ('radio-0', 'iidoplin', iidoplin, None, 'Courier New', '16px', 'b', 'P', None), ('td-9', None),
                    ('tr-9', None)
                ]
        lnewpage = lnewpage + [
            ('table-9', None),
            ('div-9', None),    # <== Esse 'div-9' é uma necessidade pelo uso de 'table-2'.
        ]
        if iparfunc == 1:
            lnewpage = lnewpage + [
            ('table-0', 'table table-bordered table-sm table-responsive'),
                ('tr-0', None, False),
                    ('td-0', None, 1, None, 1, 1, None),
                        ('button-0', 'btselreg', 'btn btn-primary mt-1', 'Abrir registro principal'),
                    ('td-9', None),
                    ('td-0', None, 1, None, 1, 1, None),
                        ('button-0', 'btvingrf', 'btn btn-primary mt-1', 'Vincular grupos de veículos'),
                    ('td-9', None),
                    ('td-0', None, 1, None, 2, 1, None),
                        ('label-0',  'Filtro:', 'form-control-label'),
                    ('td-9', None),
                    ('td-0', None, 1, None, 1, 1, None),
                        ('alt255-0', 2),
                    ('td-9', None),                
                    ('td-0', None, 1, None, 1, 1, None),
                        ('input-0',  'sfilprio', 'form-control', 0, 20, '16px', None, 'btfilpri', True, 0),
                    ('td-9', None),
                    ('td-0', None, 1, None, 1, 1, None),
                        ('alt255-0', 1),
                    ('td-9', None),
                    ('td-0', None, 1, None, 1, 1, None),
                        ('button-0', 'btfilpri', 'btn btn-primary mt-1', 'Filtrar prioridades'),
                    ('td-9', None),
                    ('td-0', None, 1, None, 1, 1, None),
                        ('button-0', 'btrelcad', 'btn btn-primary mt-1', 'Relação de prioridades cadastradas'),
                    ('td-9', None),
                ('tr-9', None),
            ('table-9', None)]
        elif iparfunc == 2:
            lnewpage = lnewpage + [
            ('table-0', 'table table-bordered table-sm table-responsive'),
                ('tr-0', None, False),
                    ('td-0', None, 1, None, 1, 1, None),
                        ('button-1', 'btimporx', 'btn btn-primary mt-2', 'Importar grupos de veículos da prioridade de linha selecionada', 'Importar grupos de veículos', 'btimport', 'btn btn-primary mt-2', 'Importar', 'Confirma a importação dos dados?'),
                    ('td-9', None),
                    ('td-0', None, 1, None, 1, 1, None),
                        ('alt255-0', 60),
                    ('td-9', None),
                    ('td-0', None, 1, None, 2, 1, None),
                        ('label-0',  'Filtro:', 'form-control-label'),
                    ('td-9', None),
                    ('td-0', None, 1, None, 1, 1, None),
                        ('alt255-0', 2),
                    ('td-9', None),                
                    ('td-0', None, 1, None, 1, 1, None),
                        ('input-0',  'sfilprio', 'form-control', 0, 20, '16px', None, 'btfilpri', True, 0),
                    ('td-9', None),
                    ('td-0', None, 1, None, 1, 1, None),
                        ('alt255-0', 1),
                    ('td-9', None),
                    ('td-0', None, 1, None, 1, 1, None),
                        ('button-0', 'btfilpri', 'btn btn-primary mt-1', 'Filtrar prioridades'),
                    ('td-9', None),
                ('tr-9', None),
            ('table-9', None)]
        # //////////////
        # Atualiza a DIV
        # //////////////
        snewpage = abnf_create_page(lnewpage)
        abnf_socket_004([1, 'sdivprio', snewpage])

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00804_operacional_cadastro_prioridades_linhas ] ///////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Prioridades de Linhas.                                                                                                    // #
# // Form de vinculação de grupos de veículos com o registro de prioridade de linha.                                                                     // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00804_operacional_cadastro_prioridades_linhas(dabnfopg, iidoplin):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00804_operacional_cadastro_prioridades_linhas(...)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        # /////////////////////////////
        # Etapa 01 - Buscando registros
        # /////////////////////////////
        # /////////////////////////////////
        # Buscando o registro de prioridade
        # /////////////////////////////////
        lcamposb = ('idoplin', 'idolinh', 'veicser', 'idveicu', 'ordprio', 'tpdiaut', 'tpdiasa', 'tpdiado', 'tpdiafe', 'tpdia2a', 'tpdia3a', 'tpdia4a', 'tpdia5a', 'tpdia6a', 'situreg')
        lfilbusc = (('idoplin', '=', iidoplin), ('situreg', '!=', 'C'))
        lorderby = None
        lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_prioridades_linhas', lcamposb, lfilbusc, lorderby)
        if lsqlre01 == [] or iqtdre01 == 0:
            abnf_alert('Registro de prioridade não encontrado! Entre em contato com o depto. de sistemas!', 4)
            abnf_socket_004([5, 'btvingrf'])
            bvalidad = False
        else:
            iidoplin = lsqlre01[0][0]
            iidolinh = lsqlre01[0][1]
            iveicser = lsqlre01[0][2]
            iidveicu = lsqlre01[0][3]
            iordprio = lsqlre01[0][4]
            btpdiaut = lsqlre01[0][5]
            btpdiasa = lsqlre01[0][6]
            btpdiado = lsqlre01[0][7]
            btpdiafe = lsqlre01[0][8]
            btpdia2a = lsqlre01[0][9]
            btpdia3a = lsqlre01[0][10]
            btpdia4a = lsqlre01[0][11]
            btpdia5a = lsqlre01[0][12]
            btpdia6a = lsqlre01[0][13]
            ssitureg = abnf_personal_retorna_string(10001, lsqlre01[0][14])
            stipodia = ''
            if btpdiaut: stipodia = stipodia + ' - DIA ÚTIL'
            if btpdiasa: stipodia = stipodia + ' - SÁBADO'
            if btpdiado: stipodia = stipodia + ' - DOMINGO'
            if btpdiafe: stipodia = stipodia + ' - FERIADO'
            if btpdia2a: stipodia = stipodia + ' - SEGUNDA-FEIRA'
            if btpdia3a: stipodia = stipodia + ' - TERÇA-FEIRA'
            if btpdia4a: stipodia = stipodia + ' - QUARTA-FEIRA'
            if btpdia5a: stipodia = stipodia + ' - QUINTA-FEIRA'
            if btpdia6a: stipodia = stipodia + ' - SEXTA-FEIRA'
            if stipodia != '': stipodia = stipodia[3:]
            # //////////////////////////////////////////////////////
            # Buscando a linha relacionada ao registro de prioridade
            # //////////////////////////////////////////////////////
            lcamposb = ('codolin', 'desolin')
            lfilbusc = (('idolinh', '=', iidolinh), ('situreg', '!=', 'C'))
            lorderby = None
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_linhas', lcamposb, lfilbusc, lorderby)
            if lsqlre01 == [] or iqtdre01 == 0:
                abnf_alert('Linha não encontrada! Entre em contato com o depto. de sistemas!', 4)
                abnf_socket_004([5, 'btvingrf'])
                bvalidad = False
            else:
                scodolin = lsqlre01[0][0]
                sdesolin = lsqlre01[0][1]
                # /////////////////////////////////////////////////////////////////////////////
                # Buscando o veículo oficial relacionado ao registro de prioridade (caso tenha)
                # /////////////////////////////////////////////////////////////////////////////
                if iidveicu > 0:
                    lcamposb = ('prefvei', 'placave')
                    lfilbusc = (('idveicu', '=', iidveicu), ('situreg', '!=', 'C'))
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_veiculos', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 == [] or iqtdre01 == 0:
                        abnf_alert('Veículo não encontrado! Entre em contato com o depto. de sistemas!', 4)
                        abnf_socket_004([5, 'btvingrf'])
                        bvalidad = False
                    else:
                        sprefvei = lsqlre01[0][0]
                        splacave = lsqlre01[0][1]
        # ///////////////////////////////////////////////////////
        # Etapa 02 - Criando a tela de inserir grupos de veículos
        # ///////////////////////////////////////////////////////
        if bvalidad:
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '13C00805A'),)]) # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidoplin', iidoplin),)])    # ==> Guardado dados do registro de prioridade de linha para a próxima função. Obs: tem que ter essa vírgula: "),)])"
            lidogrve = abnf_database_menu(icodbase, iidfilia, 'L', '1321A', 1, 1, 2)
            lnewpage = [
                ('div-0', 'container', None, None),
                ('hr-0', None),
                ('div-0', 'row', None, None),
                ('div-0', 'col d-flex justify-content-center', None, None),
                ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                ('table-0', 'table table-bordered table-sm table-responsive'),
                    ('tr-0', 'text-white bg-secondary', False),
                        ('td-0', None, 2, None, 1, None, None),
                            ('legend-0', 'Prioridades de Linhas - Vincular Grupos de Veículos'),
                        ('td-9', None),
                    ('tr-9', None),
                    ('tr-0', None, False),
                        ('td-0', None, None, None, None, None, None),
                            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                            ('table-0', 'table table-bordered table-sm table-responsive'),
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None),   ('label-0', 'Prioridade de linha', 'form-control-label'),                                   ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),             ('font-0', 'Courier New;', '20px', 'darkcyan', iordprio),                                   ('td-9', None),
                                    ('td-0', None, 1,    6, 1,    1, None),             ('button-0', 'btcancel', 'btn btn-primary mt-2', 'Cancelar'),                               ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None),   ('label-0', 'Linha', 'form-control-label'),                                                 ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),             ('font-0', 'Courier New;', '20px', 'darkcyan', scodolin + ' - ' + sdesolin),                ('td-9', None),
                                    
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None),   ('label-0', 'Tipos de dia', 'form-control-label'),                                          ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),             ('font-0', 'Courier New;', '20px', 'darkcyan', stipodia),                                   ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),                                                                                                         ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None),   ('label-0', 'Veículo/Serviço', 'form-control-label'),                                       ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),             ('font-0', 'Courier New;', '20px', 'darkcyan', iveicser),                                   ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),                                                                                                         ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None),   ('label-0', 'Veículo oficial', 'form-control-label'),                                       ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),             ('font-0', 'Courier New;', '20px', 'darkcyan', sprefvei + '(' + splacave + ')'),            ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),                                                                                                         ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None),   ('label-0', 'Situação', 'form-control-label'),                                              ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),             ('font-0', 'Courier New;', '20px', 'darkcyan', ssitureg),                                   ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),                                                                                                         ('td-9', None),
                                ('tr-9', None),
                            ('table-9', None),
                            ('form-9', None),
                            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                            ('table-0', None),
                                ('tr-0', None, False),
                                    ('div-1', 'sdivofic'),
                                    ('div-9', None),
                                    ('div-1', 'sdivgfvi'),
                                    ('div-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', None, 1, None, 1, None, None),
                                        ('button-1', 'btexcgfx', 'btn btn-danger mt-2', 'Remover grupos de veículos selecionados', 'Excluir Registro', 'btexcgfr', 'btn btn-danger mt-2', 'Excluir', 'Confirma a remoção do(s) grupo(s) de veículos selecionado(s)?'),
                                    ('td-9', None),
                                    ('td-0', None, 1, None, 1, None, None), ('alt255-0', 2), ('td-9', None),
                                    ('td-0', 'table-active', 1, None, 1, None, None),
                                        # ('button-0', 'btinvgrf', 'btn btn-success mt-2', 'Inverter ordem entre dois grupos', None),
                                        ('button-1', 'btinvgrx', 'btn btn-success mt-2', 'Inverter ordem entre dois grupos', 'Inveter Registros', 'btinvgrf', 'btn btn-success mt-2', 'Inverter', 'Confirma a inversão da ordem entre os registros selecionados?'),
                                    ('td-9', None),                                    
                                    ('td-0', None, 1, None, 1, None, None), ('alt255-0', 2), ('td-9', None),
                                    ('td-0', 'table-active', 1, None, 1, None, None), 
                                        ('button-1', 'btsalrax', 'btn btn-primary mt-2', 'Salvar rascunho', 'Salvar', 'btsalras', 'btn btn-primary mt-2', 'Salvar', 'Confirma a gravação desta(s) vinculação(ções)?'),
                                    ('td-9', None),
                                ('tr-9', None),
                            ('table-9', None),
                            ('form-9', None),
                            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                            ('table-0', 'table table-bordered table-sm table-responsive'),
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None), ('label-0', 'Ordem de prioridade (vazio para por no final)', 'form-control-label'),     ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),           ('label-0', '&nbsp;', 'form-control-label'),                                            ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),           ('number-0', 'iordprio', 'form-control', 0, 4, '16px', None, 'iidogrve', True, None),   ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 0, None, None), ('label-0', 'Grupo de veículos', 'form-control-label'),                                 ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),           ('label-0', '&nbsp;', 'form-control-label'),                                            ('td-9', None),
                                    ('td-0', None, 1, None, 0, None, None),           ('select-0', 'iidogrve', 'form-control', '16px', 'btinsgrf', lidogrve, 1, None, False), ('td-9', None),
                                ('tr-9', None),
                                ('tr-0', None, False),
                                    ('td-0', 'table-active', 1, None, 1, None, None), ('td-9', None),
                                    ('td-0', 'table-active', 2, None, 1, None, None), 
                                    ('button-0', 'btinsgrf', 'btn btn-primary mt-2', 'Inserir novo grupo de veículos', None),
                                    ('td-9', None),
                                ('tr-9', None),
                            ('table-9', None),
                            ('form-9', None),
                            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                            ('div-1', 'sdivprio'),
                            ('div-9', None),
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
            abnf000u13c00803_operacional_cadastro_prioridades_linhas(icodbase, iidfilia, 2, '')
            # /////////////////////////////////////////////////////
            # Buscando os grupos de veículos da prioridade de linha
            # /////////////////////////////////////////////////////
            lgrupvei = []
            lcamposb = ('ordprio', 'idogrve')
            lfilbusc = (('idoplin', '=', iidoplin), ('situreg', '!=', 'C'))
            lorderby = (('idoplin', 'ordprio', 'idoplgv'))
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_prioridades_linhas_gv', lcamposb, lfilbusc, lorderby)
            if lsqlre01 != [] and iqtdre01 > 0:
                for lauxi001 in lsqlre01:
                    lgrupvei.append([
                        lauxi001[0],
                        lauxi001[1],
                    ])
            abnf000u13c00806_operacional_cadastro_prioridades_linhas(sabnproj, sabntoke, icodbase, lgrupvei, True)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00805_operacional_cadastro_prioridades_linhas ] ///////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Prioridades de Linhas.                                                                                                    // #
# // Vinculação de grupos de veículos com o registro de prioridade de linha.                                                                             // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00805_operacional_cadastro_prioridades_linhas(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00805_operacional_cadastro_prioridades_linhas(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        if dabnfopg['abnfobj0'] == ['btcancel', 'btcancel']:        # Voltar para tela anterior
            abnf000u13c00800_operacional_cadastro_prioridades_linhas(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btfilpri', 'btfilpri']:        # Filtrar prioridades
            lmfields = [
                ['sfilprio', 'input', 'M', 'filtro de prioridades', [], None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btfilpri')
            if bvalidad:
                sfilprio = lmfields[0][5]
                abnf000u13c00803_operacional_cadastro_prioridades_linhas(icodbase, iidfilia, 2, sfilprio)
        elif dabnfopg['abnfobj0'] == ['btinsgrf', 'btinsgrf']:
            # ////////////////////////////////////////////////
            # Inserir grupo de veículos na prioridade de linha
            # ////////////////////////////////////////////////
            lmfields = [
                ['iordprio', 'number',   'F', 'ordem de prioridade do grupo de veículos', ['Empty_to_zero'],                  None],
                ['iidogrve', 'select',   'M', 'grupo de veículos',                        ['Notnull', 'D', 'Return_integer'], None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btinsgrf')
            if bvalidad:
                iordprio = lmfields[0][5]
                iidogrve = lmfields[1][5]
                if iordprio == 0: iordprio = 99999  # ==> Para ficar na ultima posição da lista
                # ////////////////////////////////////////
                # Buscando o registro do grupo de veículos
                # ////////////////////////////////////////
                lcamposb = ('idogrve', None)
                lfilbusc = (('idogrve', '=', iidogrve), ('situreg', '!=', 'C'), None)
                lorderby = None
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_grupos_veiculos', lcamposb, lfilbusc, lorderby)
                if lsqlre01 == [] or iqtdre01 == 0:
                    abnf_alert('Erro interno! Não foi encontrado o registro ID ' + str(iidogrve) + '! Entre em contato com o depto. de sistemas!', 4)
                    abnf_socket_004([5, 'btinsgrf'])
                else:
                    # //////////////////////////////
                    # Busca na memória a lista atual
                    # //////////////////////////////
                    lgrupvei = dglobaux['lgrupvei']
                    # /////////////////////////////////////////////////////////////////////////////////
                    # Acrescenta 1 na numeração de ordem igual ao acima da nova ordem que será incluída
                    # /////////////////////////////////////////////////////////////////////////////////
                    if lgrupvei != []:
                        for lauxi001 in lgrupvei:
                            if lauxi001[0] >= iordprio:
                               lauxi001[0] = lauxi001[0] + 1
                    # ///////////////////
                    # Inserer o novo ítem
                    # ///////////////////
                    lgrupvei.append([
                        iordprio,
                        iidogrve,
                    ])
                    # /////////////////////////
                    # Organiza a ordem da lista
                    # /////////////////////////
                    lgrupvei.sort()
                    # ///////////////////////////////////////////////////
                    # Atualiza toda a numeração da lista conforme a ordem
                    # ///////////////////////////////////////////////////
                    iauxi001 = 0
                    for lauxi001 in lgrupvei:
                        iauxi001 += 1
                        lauxi001[0] = iauxi001
                    # ///////////
                    # Finalização
                    # ///////////
                    abnf_alert('Grupo de veículos inserido com sucesso!', 3)
                    abnf000u13c00806_operacional_cadastro_prioridades_linhas(sabnproj, sabntoke, icodbase, lgrupvei, False)
                    abnf_socket_004([5, 'btinsgrf'])
                    abnf_socket_004([3, 'iordprio', ''])     # Limpa o campo
                    abnf_socket_004([3, 'iidogrve', ''])     # Limpa o campo
        elif dabnfopg['abnfobj0'] == ['btexcgfr', 'btexcgfr']:
            # /////////////////////////////////////////////////
            # Remover grupos de veículos na prioridade de linha
            # /////////////////////////////////////////////////
            lmfields = [
                ['iordprix', 'checkbox', 'Nenhum grupo de veículos foi marcado para ser removido', ['Notnull', 'Return_integer'], []],
            ]
            bvalidad, lmfields = abnf_find_checkbox_radio(dabnfopg, lmfields, 'btexcgfx')
            if bvalidad:
                lordprix = lmfields[0][4]
                # //////////////////////////////
                # Busca na memória a lista atual
                # //////////////////////////////
                lgrupvei = dglobaux['lgrupvei']
                # /////////////////////////////////////////////////////////
                # Refaz a lista somente com os ítens que não foram marcados
                # /////////////////////////////////////////////////////////
                lititemp = []
                for lauxi001 in lgrupvei:
                    if not lauxi001[0] in lordprix:
                        lititemp.append(lauxi001)
                lgrupvei = lititemp
                # /////////////////////////////////////////////////////////////////////////
                # Atualiza toda a numeração da lista conforme a ordem dos ítens que sobrarm
                # /////////////////////////////////////////////////////////////////////////
                if lgrupvei != []:
                    iauxi001 = 0
                    for lauxi001 in lgrupvei:
                        iauxi001 += 1
                        lauxi001[0] = iauxi001
                # ///////////
                # Finalização
                # ///////////
                iauxi001 = len(lordprix)
                if iauxi001 == 1: abnf_alert('1 grupo de veículos removido com sucesso!', 3)
                else:             abnf_alert(str(iauxi001) + ' grupos de veículos removidos com sucesso!', 3)
                abnf000u13c00806_operacional_cadastro_prioridades_linhas(sabnproj, sabntoke, icodbase, lgrupvei, False)
        elif dabnfopg['abnfobj0'] == ['btinvgrf', 'btinvgrf']:
            # ////////////////////////////////
            # Inverter ordem entre dois grupos
            # ////////////////////////////////
            lmfields = [
                ['iordprix', 'checkbox', 'Nenhum grupo de veículos foi marcado para inverter ordem', ['Notnull', 'Return_integer'], []],
            ]
            bvalidad, lmfields = abnf_find_checkbox_radio(dabnfopg, lmfields, 'btinvgrf')
            if bvalidad:
                lordprix = lmfields[0][4]
                iauxi001 = len(lordprix)
                if iauxi001 < 2:
                    abnf_alert('É necessário que dois registros sejam selecionados para poder trocar posição!', 5)
                    abnf_socket_004([5, 'btinvgrf'])
                elif iauxi001 > 2:
                    abnf_alert('Somente dois registros devem ser selecionados para trocarem posições!', 5)
                    abnf_socket_004([5, 'btinvgrf'])
                else:
                    # //////////////////////////////
                    # Busca na memória a lista atual
                    # //////////////////////////////
                    lgrupvei = dglobaux['lgrupvei']
                    # //////////////////////////////////////////////
                    # Troca as prioridades nos registros selecioados
                    # //////////////////////////////////////////////
                    for lauxi001 in lgrupvei:
                        if lauxi001[0] in lordprix:
                            if   lauxi001[0] == lordprix[0]: lauxi001[0] = lordprix[1]
                            elif lauxi001[0] == lordprix[1]: lauxi001[0] = lordprix[0]
                    lgrupvei.sort()
                    # ///////////
                    # Finalização
                    # ///////////
                    abnf_alert('Inversão de ordem realizada com sucesso!', 3)
                    abnf000u13c00806_operacional_cadastro_prioridades_linhas(sabnproj, sabntoke, icodbase, lgrupvei, False)
        elif dabnfopg['abnfobj0'] == ['btsalras', 'btsalras']:
            # ///////////////
            # Salvar rascunho
            # ///////////////
            iidoplin = dglobaux['iidoplin']
            lgrupvei = dglobaux['lgrupvei']
            # ///////////////////////////////////////////////////////////////
            # Verifica se não há registros de veículos duplicados em lgrupvei
            # ///////////////////////////////////////////////////////////////
            bvalidad = True
            lgrupfrx = []
            for lauxi001 in lgrupvei:
                iordprio = lauxi001[0]
                iidogrve = lauxi001[1]
                for lauxi002 in lgrupfrx:
                    if iidogrve == lauxi002[1]:
                        abnf_alert('As ordens ' + str(1000 + lauxi002[0])[1:] + ' e ' + str(1000 + iordprio)[1:] + ' estão com grupo de veículos repetido!', 5)
                        abnf_socket_004([5, 'btsalras'])
                        bvalidad = False
                        break
                if bvalidad:
                    lgrupfrx.append([iordprio, iidogrve])
                else:
                    break
            # /////////////
            # Próxima etapa
            # /////////////
            if bvalidad:
                # /////////////////////////////////
                # Buscando o registro de prioridade
                # /////////////////////////////////
                lcamposb = ('situreg', None)
                lfilbusc = (('idoplin', '=', iidoplin), ('situreg', '!=', 'C'))
                lorderby = None
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_prioridades_linhas', lcamposb, lfilbusc, lorderby)
                if lsqlre01 == [] or iqtdre01 == 0:
                    abnf_alert('Registro de prioridade de linha não encontrado! Entre em contato com o depto. de sistemas!', 4)
                    abnf_socket_004([5, 'btselreg'])
                    bvalidad = False
                elif lsqlre01[0][0] != 'A':
                    abnf_alert('O registro de prioridade de linha não está ativo!', 5)
                    abnf_socket_004([5, 'btsalras'])
                else:
                    abnf_alert('Aguarde! Gravando registros...', 15)
                    bvalidad = True
                    # /////////////////////////////////////////////////////////////////////////////
                    # Cancelando todos os registros atuais relacionados ao o registro de prioridade
                    # /////////////////////////////////////////////////////////////////////////////
                    if bvalidad:
                        lcamposb = ('idoplgv', None)
                        lfilbusc = (('idoplin', '=', iidoplin), ('situreg', '!=', 'C'), None)
                        lorderby = (('idoplin', 'ordprio', 'idoplgv'))
                        lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_prioridades_linhas_gv', lcamposb, lfilbusc, lorderby)
                        if lsqlre01 != [] or iqtdre01 != 0:
                            lidoplgv = []
                            for lauxi001 in lsqlre01:
                                lidoplgv.append(lauxi001[0])
                            for iidoplgv in lidoplgv:
                                bvalidad = abnf_database_exclui_registro(icodbase, sabnproj, 'abnf_operacional_cadastro_prioridades_linhas_gv', iidoplgv, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'])
                                if not bvalidad:
                                    abnf_alert('Erro ao excluir registros de grupos de veículos! Entre em contato com o depto. de sistemas!', 4)
                                    break
                    # //////////////////////////////////////////////////////////////////////////////////
                    # Guardando os IDs de todos os registros que estão excluídos para serem reutilizados
                    # //////////////////////////////////////////////////////////////////////////////////
                    if bvalidad:
                        lidexclu = []
                        lcamposb = ('idoplgv', None)
                        lfilbusc = (('situreg', '=', 'C'), None)
                        lorderby = None
                        lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_prioridades_linhas_gv', lcamposb, lfilbusc, lorderby)
                        if lsqlre01 != [] or iqtdre01 != 0:
                            for lauxi001 in lsqlre01:
                                lidexclu.append(lauxi001[0])
                        # Debug (início)
                        # abnf_show('09', lidexclu, 0)
                        # abnf_show('10', len(lidexclu), 0)
                        # Debug (fim)
                    # ///////////////////////////////////////////////////////////////////////////////////////////////////////
                    # Inserindo os grupos de veículos em registros excluídos ou criando novos registros de grupos de veículos
                    # ///////////////////////////////////////////////////////////////////////////////////////////////////////
                    if bvalidad:
                        for lauxi001 in lgrupvei:
                            iordprio = lauxi001[0]
                            iidogrve = lauxi001[1]
                            # /////////////////////////////////////////////////////////////
                            # Insere os dados em um registro de grupos de veículos excluído
                            # /////////////////////////////////////////////////////////////
                            if lidexclu != []:
                                iidoplgv = lidexclu[0]
                                del lidexclu[0]
                                bvalidad = abnf_database_altera_dados_v02(icodbase, sabnproj, 'abnf_operacional_cadastro_prioridades_linhas_gv', iidoplgv, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                                [
                                    ('idoplin', iidoplin),
                                    ('ordprio', iordprio),
                                    ('idogrve', iidogrve),
                                    ('situreg', 'A'),
                                ])
                                if not bvalidad:
                                    break
                            # ///////////////////////////////////////////
                            # Cria um registro novo de grupos de veículos
                            # ///////////////////////////////////////////
                            else:
                                bvalidad, iproxiid = abnf_database_insere_dados_v02(icodbase, sabnproj, 'abnf_operacional_cadastro_prioridades_linhas_gv', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                                [
                                    ('idoplin', iidoplin),
                                    ('ordprio', iordprio),
                                    ('idogrve', iidogrve),
                                    ('situreg', 'A'),
                                ])
                                if not bvalidad:
                                    break
                        if not bvalidad:
                            abnf_alert('Erro ao criar novos registros de grupos de veículos! Entre em contato com o depto. de sistemas!', 4)
                        else:
                            abnf_alert('Registros gravados com sucesso!', 3)
                            abnf000u13c00806_operacional_cadastro_prioridades_linhas(sabnproj, sabntoke, icodbase, lgrupvei, True)
                            abnf_socket_004([5, 'btsalras'])
        elif dabnfopg['abnfobj0'] == ['btimport', 'btimport']:
            # ////////////////////////////////
            # Importação de grupos de veículos
            # ////////////////////////////////
            lgrupvei = dglobaux['lgrupvei']
            # /////////////////////////////////
            # Buscando a prioridade selecionada
            # /////////////////////////////////
            lmfields = [
                ['iidoplin', 'radio', 'Nenhum registro de prioridade foi selecionado', ['Notnull', 'Return_integer'], None],
            ]
            bvalidad, lmfields = abnf_find_checkbox_radio(dabnfopg, lmfields, 'btimport')
            if bvalidad:
                iidoplin = lmfields[0][4]
                # /////////////////////////////////
                # Buscando o registro de prioridade
                # /////////////////////////////////
                lcamposb = ('situreg', None)
                lfilbusc = (('idoplin', '=', iidoplin), ('situreg', '!=', 'C'))
                lorderby = None
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_prioridades_linhas', lcamposb, lfilbusc, lorderby)
                if lsqlre01 == [] or iqtdre01 == 0:
                    abnf_alert('Registro de prioridade de linha não encontrado! Entre em contato com o depto. de sistemas!', 4)
                    abnf_socket_004([5, 'btimport'])
                    bvalidad = False
                elif lsqlre01[0][0] != 'A':
                    abnf_alert('O registro de prioridade de linha não está ativo!', 5)
                    abnf_socket_004([5, 'btimport'])
                else:
                    # /////////////////////////////////////////////////////
                    # Buscando os grupos de veículos da prioridade de linha
                    # /////////////////////////////////////////////////////
                    lcamposb = ('idogrve', None)
                    lfilbusc = (('idoplin', '=', iidoplin), ('situreg', '!=', 'C'))
                    lorderby = (('idoplin', 'ordprio', 'idoplgv'))
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_prioridades_linhas_gv', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 == [] or iqtdre01 == 0:
                        abnf_alert('Não havia registros para serem importados!', 5)
                        abnf_socket_004([5, 'btimport'])
                    else:
                        iauxi001 = len(lgrupvei)
                        for lauxi001 in lsqlre01:
                            iauxi001 += 1
                            lgrupvei.append([
                                iauxi001,
                                lauxi001[0],
                            ])
                        abnf_alert('Registros importados com sucesso!', 3)
                        abnf000u13c00806_operacional_cadastro_prioridades_linhas(sabnproj, sabntoke, icodbase, lgrupvei, False)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00806_operacional_cadastro_prioridades_linhas ] ///////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Prioridades de Linhas.                                                                                                    // #
# // Reorganiza a lista de grupos de veículos que está em memória, atualiza e posta a DIV.                                                               // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00806_operacional_cadastro_prioridades_linhas(sabnproj, sabntoke, icodbase, lgrupvei, boficial):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00806_operacional_cadastro_prioridades_linhas(...)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    # ********  lgrupvei  ********
    # iordprio  => [0]  - Ordem de prioridade
    # iidogrve  => [1]  - ID do grupo de veículos
    if boficial:
        lauxi001 = ('bg-success', 'white', 'Oficial')
        abnf_socket_004([10, 'btsalrax'])   # Desabilita o botão "Salvar rascunho"
    else:
        lauxi001 = ('bg-warning', None, 'Rascunho')
        abnf_socket_004([5, 'btsalrax'])    # Habilita o botão "Salvar rascunho"
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
                ('td-0', 'table-active', 1, None, 1, None, None), ('font-0', 'Courier New;', '12px', None, 'Ordem'            ), ('td-9', None),
                ('td-0', 'table-active', 1, None, 1, None, None), ('font-0', 'Courier New;', '12px', None, 'Grupo de veículos'), ('td-9', None),
                ('td-0', 'table-active', 1, None, 1, None, None), ('td-9', None),
            ('tr-9', None)
    ]
    if lgrupvei == []:
        abnf_socket_004([10, 'btexcgfx'])   # Desabilita o botão "Remover grupos de veículos selecionados"
        abnf_socket_004([10, 'btinvgrx'])   # Desabilita o botão "Inverter ordem entre dois grupos"
    else:
        # ///////////////
        # Habilita botões
        # ///////////////
        abnf_socket_004([5, 'btexcgfx'])    # Habilita o botão "Remover grupos de veículos selecionados"
        abnf_socket_004([5, 'btinvgrx'])    # Habilita o botão "Inverter ordem entre dois grupos"
        # ////////////////////
        # Monta os dicionários
        # ////////////////////
        didogrve = abnf_database_menu(icodbase, None, 'D', '1321A', 1, 1, 2)
        # //////////////////////////////////////
        # Monta a tela com os grupos de veículos
        # //////////////////////////////////////
        icontgrf = 0
        for lauxi001 in lgrupvei:
            icontgrf += 1
            iordprio = lauxi001[0]
            iidogrve = lauxi001[1]
            # /// #
            sordprio = str(1000 + iordprio)[1:]
            sidogrve = didogrve.get(iidogrve, '')
            lauxi002 = ('checkbox-0', 'iordprix[' + str(iordprio) + ']', iordprio, None, 'Courier New', '12px', 'b', 'P', None)
            # /// #
            lnewpage = lnewpage + [
                ('tr-0', None, True),
                    ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '15px', 'darkcyan', sordprio), ('td-9', None),
                    ('td-0', None, 1, None, 0, None, None), ('font-0', 'Courier New;', '15px', None, sidogrve),       ('td-9', None),
                    ('td-0', None, 1, None, 1, None, None), lauxi002, ('td-9', None),
                ('tr-9', None)
            ]
        lnewpage = lnewpage + [
                ('tr-0', None, False),
                    ('td-0', 'table-active', 2, None, 2, None, None), ('font-0', 'Courier New;', '12px', None, 'Quantidade de grupos de veículos:'), ('td-9', None),
                    ('td-0', 'table-active', 1, None, 1, None, None), ('font-0', 'Courier New;', '12px', None, abnf_formata_numero_milhar_decimal(icontgrf, True, 0)), ('td-9', None),
                ('tr-9', None),
        ]
    lnewpage = lnewpage + [
        ('table-9', None),
        ('div-9', None),    # <== Esse 'div-9' é uma necessidade pelo uso de 'table-2'.
        ('form-9', None),
    ]
    # //////////////////////////////
    # Armazena 'lgrupvei' em memória
    # //////////////////////////////
    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('lgrupvei', lgrupvei),)]) # ==> Guardado lista de grupo de veículos para a próxima função. Obs: tem que ter essa vírgula: "),)])"
    # //////////////
    # Atualiza a DIV
    # //////////////
    snewpage = abnf_create_page(lnewpage)
    abnf_socket_004([1, 'sdivgfvi', snewpage])
    # Debug (início)
    # abnf_show('10', lgrupvei, 0)
    # Debug (fim)            
    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00807_operacional_cadastro_prioridades_linhas ] ///////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Prioridades de Linhas.                                                                                                    // #
# // Relatórios.                                                                                                                                         // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00807_operacional_cadastro_prioridades_linhas(dabnfopg, sfilprio):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00807_operacional_cadastro_prioridades_linhas(...)')
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
        icolspan = 13
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
            abnf_imprime_thead_002_titulo_relatorio(sarquwri, icolspan, 'RELAÇÃO DE PRIORIDADES DE LINHAS')
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
            # ///////////////////////////////////////////////////////////
            # Busca todos os registros de prioridade de linha cadastrados
            # ///////////////////////////////////////////////////////////
            lcamposb = ('idoplin', 'ordprio', 'idolinh', 'veicser', 'idveicu', 'tpdiaut', 'tpdiasa', 'tpdiado', 'tpdiafe', 'tpdia2a', 'tpdia3a', 'tpdia4a', 'tpdia5a', 'tpdia6a', 'situreg')
            lfilbusc = (('idfilia', '=', iidfilia), ('situreg', '!=', 'C'))
            lorderby = ('ordprio', 'idoplin')
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_prioridades_linhas', lcamposb, lfilbusc, lorderby)
            # Relação de prioridades disponíveis
            if lsqlre01 != [] and iqtdre01 > 0:
                drelolin = abnf_database_menu(icodbase, iidfilia, 'D', '1303C', 0, 1, 1)
                drelveic = abnf_database_menu(icodbase, iidfilia, 'D', '0201', 0, 1, 2)
                didogrve = abnf_database_menu(icodbase, None,     'D', '1321A', 1, 1, 2)
                didveicu = abnf_database_menu(icodbase, iidfilia, 'D', '0203', 0, 1, None)
                for lauxi001 in lsqlre01:
                    iidoplin = lauxi001[0]
                    iordprio = lauxi001[1]
                    iidolinh = lauxi001[2]
                    iveicser = lauxi001[3]
                    iidveicu = lauxi001[4]
                    stipodia = ''
                    stipodia = stipodia + 'U' if lauxi001[5]  else stipodia + ''
                    stipodia = stipodia + 'S' if lauxi001[6]  else stipodia + ''
                    stipodia = stipodia + 'D' if lauxi001[7]  else stipodia + ''
                    stipodia = stipodia + 'F' if lauxi001[8]  else stipodia + ''
                    stipodia = stipodia + '2' if lauxi001[9]  else stipodia + ''
                    stipodia = stipodia + '3' if lauxi001[10] else stipodia + ''
                    stipodia = stipodia + '4' if lauxi001[11] else stipodia + ''
                    stipodia = stipodia + '5' if lauxi001[12] else stipodia + ''
                    stipodia = stipodia + '6' if lauxi001[13] else stipodia + ''
                    scodolin, sdesolin = drelolin.get(iidolinh, ('', ''))
                    sidveicu = drelveic.get(iidveicu, '') if iidveicu > 0 else ''
                    ssitureg = abnf_personal_retorna_string(10001, lauxi001[14])
                    bvalidad = False
                    if sfilprio == '': bvalidad = True
                    else:
                        if   sfilprio in str(iordprio): bvalidad = True
                        elif sfilprio in scodolin:      bvalidad = True
                        elif sfilprio in sdesolin:      bvalidad = True
                        elif sfilprio in stipodia:      bvalidad = True
                        elif sfilprio in str(iveicser): bvalidad = True
                        elif sfilprio in sidveicu:      bvalidad = True
                        elif sfilprio in ssitureg:      bvalidad = True
                    if bvalidad:
                        icontreg += 1
                        abnf_imprime_line(sarquwri, icolspan, 'brown')
                        abnf_imprime_info_001(sarquwri, '#D1C5C5', None, 1,
                            [
                                ('Prioridade:',      1, 0, None, None,     'black', 'Courier New', ifontlen + 1, True, False),
                                (iordprio,           1, 0, None, 'center', 'blue',  'Courier New', ifontlen + 1, True, False),
                                ('Linha:',           1, 0, None, None,     'black', 'Courier New', ifontlen + 1, True, False),
                                (scodolin,           1, 0, None, 'center', 'blue',  'Courier New', ifontlen + 1, True, False),
                                (sdesolin,           1, 0, None, None,     'blue',  'Courier New', ifontlen + 1, True, False),
                                ('Tipos dia:',       1, 0, None, None,     'black', 'Courier New', ifontlen + 1, True, False),
                                (stipodia,           1, 0, None, 'center', 'blue',  'Courier New', ifontlen + 1, True, False),                                  
                                ('Veículo/Serviço:', 1, 0, None, None,     'black', 'Courier New', ifontlen + 1, True, False),
                                (iveicser,           1, 0, None, 'center', 'blue',  'Courier New', ifontlen + 1, True, False),
                                ('Veículo oficial:', 1, 0, None, None,     'black', 'Courier New', ifontlen + 1, True, False),
                                (sidveicu,           1, 0, None, 'center', 'blue',  'Courier New', ifontlen + 1, True, False),
                                ('Situação:',        1, 0, None, None,     'black', 'Courier New', ifontlen + 1, True, False),
                                (ssitureg,           1, 0, None, 'center', 'blue',  'Courier New', ifontlen + 1, True, False),
                            ]
                        )
                        # /////////////////////////////////////////////////////////
                        # Busca grupos de veículos vinculados ao registro principal
                        # /////////////////////////////////////////////////////////
                        lcamposb = ('ordprio', 'idogrve')
                        lfilbusc = (('idoplin', '=', iidoplin), ('situreg', '!=', 'C'), None)
                        lorderby = (('idoplin', 'ordprio', 'idoplgv'))
                        lsqlre02, iqtdre02 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_prioridades_linhas_gv', lcamposb, lfilbusc, lorderby)
                        if lsqlre02 != [] and iqtdre02 > 0:
                            abnf_imprime_line(sarquwri, icolspan, 'darkcyan')
                            for lauxi002 in lsqlre02:
                                iordprio = lauxi002[0]
                                iidogrve = lauxi002[1]
                                sidogrve = didogrve.get(iidogrve, '')
                                sveiculo = ''
                                lcamposb = ('idveicu', None)
                                lfilbusc = (('idogrve', '=', iidogrve), ('situreg', '!=', 'C'), None)
                                lorderby = (('idogrve', 'idveicu', 'idogrvv'))
                                lsqlre03, iqtdre03 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_grupos_veiculos_vinculos', lcamposb, lfilbusc, lorderby)
                                if lsqlre03 != [] and iqtdre03 > 0:
                                    lveiculo = []
                                    for lauxi003 in lsqlre03:
                                        iidveicu = lauxi003[0]
                                        prefvei, placave = didveicu.get(iidveicu, ('', ''))
                                        if not prefvei in lveiculo:
                                            lveiculo.append(prefvei)
                                    if lveiculo != []:
                                        lveiculo.sort()
                                        for lauxi003 in lveiculo:
                                            if sveiculo != '':
                                                sveiculo = sveiculo + ' - '
                                            sveiculo = sveiculo + lauxi003
                                abnf_imprime_info_001(sarquwri, None, None, 1,
                                    [
                                        ('Ordem:',             1, 0, None, None,     'black', 'Courier New', ifontlen, True, False),
                                        (iordprio,             1, 0, None, 'center', 'brown', 'Courier New', ifontlen, True, False),
                                        ('Grupo de veículos:', 1, 0, None, None,     'black', 'Courier New', ifontlen, True, False),
                                        (sidogrve,             4, 0, None, None,     'brown', 'Courier New', ifontlen, True, False),
                                        ('Veículos:',          1, 0, None, None,     'black', 'Courier New', ifontlen, True, False),
                                        (sveiculo,             5, 0, None, None,     'brown', 'Courier New', ifontlen, True, False),
                                    ]
                                )
            abnf_imprime_line(sarquwri, icolspan, 'black')
            abnf_imprime_info_001(sarquwri, None, None, 1,
                [
                    ('Total de prioridades de linhas impressas:', icolspan - 1, 0, None, 'Left'  , 'black', 'Courier New', ifontlen, True, False),
                    (icontreg,                                               1, 0, None, 'Right' , 'black', 'Courier New', ifontlen, True, False),
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