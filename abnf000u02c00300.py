## ============================================
## [abnf000u02c00300.py] - Cadastro de Veículos
## ============================================

from abnfsrc.abnf000u00s00003 import *              # Arquivo de funções comuns que serão utilizadas por todos os módulos do sistema
from abnfsrc.abnf000u00s00004 import *              # Arquivo de banco de dados

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u02c00300_cadastro_veiculos ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de Veículos.                                                                                                                               // #
# // Form inicial.                                                                                                                                       // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u02c00300_cadastro_veiculos(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u02c00300_cadastro_veiculos(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, '02C00301A'])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        lidveicu = abnf_database_sqlx(icodbase, 'L', '02003A', 1, (0, iidfilia))
        lnewpage = [                                                                         
            ('div-0', 'container', None, None),
            ('hr-0', None),
            ('div-0', 'row', None, None),
            ('div-0', 'col d-flex justify-content-center', None, None),
            ('div-0', 'w-50 p-3', 'background-color: #eee;', None),
            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
            ('legend-0', 'Cadastro de Veículos'),
            ('hr-0', None),
            ('label-0',  'Veículo', 'form-control-label'),
            ('select-0', 'iidveicu', 'form-control', '16px', 'btbusreg', lidveicu, 1, None, False),
            ('hr-0', None),
            ('button-0', 'btbusreg', 'btn btn-primary mt-2', 'Buscar'),
            ('alt255-0', 2),
            ('button-0', 'btnovreg', 'btn btn-primary mt-2', 'Novo registro'),
            ('alt255-0', 2),
            ('button-0', 'btrelcad', 'btn btn-primary mt-2', 'Relação de veículos cadastrados'),
            ('form-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
        ]
        snewpage = abnf_create_page(lnewpage)
        abnf_socket_004([1, 'abnfdv03', snewpage])
        
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u02c00301_cadastro_veiculos ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de Veículos.                                                                                                                               // #
# // Form de cadastro/alteração do veículo.                                                                                                              // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u02c00301_cadastro_veiculos(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u02c00301_cadastro_veiculos(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        if dabnfopg['abnfobj0'] == ['btbusreg', 'btbusreg']:        # Buscar registro existente
            lmfields = [
                ['iidveicu', 'input', 'M', 'veículo', ['Notnull', 'D', 'Return_integer'], None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btbusreg')
            # Debug: (inicio)
            # abnf_show('08', lmfields, 1)
            # abnf_show('09', dabnfopg, 2)
            # abnf_show('10', dglobaux, 2)
            # Debug: (fim)
            if bvalidad:
                icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
                iidfilia = dglobaux['iidfilia']
                iidveicu = lmfields[0][5]
                # //////////////////////////////////////////////////
                # Buscando o veículo caso seja um registro existente
                # //////////////////////////////////////////////////
                lcamposb = ('prefvei', 'placave', 'idmodel', 'renavam', 'chassiv', 'corveic', 'anofabr', 'anomode', 'tipmoto', 'tipcomb', 'captanq',
                'lugsent', 'lugempe', 'lugroda', 'lugacom', 'numport', 'dataini', 'datafim', 'arcondi', 'veielev', 'observa', 'libpsod', 'libpsro', 'situreg')
                lfilbusc = (('idveicu', '=', iidveicu), ('idfilia', '=', iidfilia), ('situreg', '!=', 'C'))
                lorderby = None
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_veiculos', lcamposb, lfilbusc, lorderby)
                if lsqlre01 == [] or iqtdre01 == 0:
                    abnf_alert('O veículo não foi encontrado!', 4)
                else:
                    # Debug: (inicio)
                    # abnf_show('10', lsqlre01, 1)
                    # Debug: (fim)
                    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidveicu', iidveicu),)])      # ==> Guardando o ID do registro. Obs: tem que ter essa vírgula: "),)])"
                    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '02C00302A'),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
                    lidmodel = abnf_database_sqlx(icodbase, 'L', '02002A', 1, (0, None))
                    lnewpage = [
                        ('div-0', 'container', None, None),
                        ('hr-0', None),
                        ('div-0', 'row', None, None),
                        ('div-0', 'col d-flex justify-content-center', None, None),
                        ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                        ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                        ('legend-0', 'Cadastro de Veículos - [ Registro existente ]'),
                        ('hr-0', None),
                        ('label-0',  'Prefixo', 'form-control-label'),
                        ('input-0',  'sprefvei', 'form-control', 0, 20, '16px', lsqlre01[0][0], 'splacave', True, 0),
                        ('label-0',  'Placa', 'form-control-label'),
                        ('input-0',  'splacave', 'form-control', 0, 8, '16px', lsqlre01[0][1], 'iidmodel', True, 0),
                        ('label-0',  'Marca - Modelo', 'form-control-label'),
                        ('select-0', 'iidmodel', 'form-control', '16px', 'srenavam', lidmodel, 0, lsqlre01[0][2], False),
                        ('label-0',  'Renavam', 'form-control-label'),
                        ('input-0',  'srenavam', 'form-control', 0, 30, '16px', lsqlre01[0][3], 'schassiv', True, 0),
                        ('label-0',  'Chassi', 'form-control-label'),
                        ('input-0',  'schassiv', 'form-control', 0, 30, '16px', lsqlre01[0][4], 'scorveic', True, 0),
                        ('label-0',  'Cor', 'form-control-label'),
                        ('input-0',  'scorveic', 'form-control', 0, 30, '16px', lsqlre01[0][5], 'ianofabr', True, 0),
                        ('label-0',  'Ano de fabricação', 'form-control-label'),
                        ('number-0', 'ianofabr', 'form-control', 0, 4, '16px', lsqlre01[0][6], 'ianomode', True, None),
                        ('label-0',  'Ano do modelo', 'form-control-label'),
                        ('number-0', 'ianomode', 'form-control', 0, 4, '16px', lsqlre01[0][7], 'itipmoto', True, None),
                        ('label-0',  'Tipo de motor', 'form-control-label'),
                        ('select-0', 'itipmoto', 'form-control', '16px', 'itipcomb', abnf_personal_retorna_lista(10201), 0, lsqlre01[0][8], False),
                        ('label-0',  'Combustível', 'form-control-label'),
                        ('select-0', 'itipcomb', 'form-control', '16px', 'icaptanq', abnf_personal_retorna_lista(10202), 0, lsqlre01[0][9], False),
                        ('label-0',  'Capacidade do tanque (litros)', 'form-control-label'),
                        ('number-0', 'icaptanq', 'form-control', 0, 4, '16px', lsqlre01[0][10], 'ilugsent', True, None),
                        ('label-0',  'Número de lugares sentados', 'form-control-label'),
                        ('number-0', 'ilugsent', 'form-control', 0, 3, '16px', lsqlre01[0][11], 'ilugempe', True, None),
                        ('label-0',  'Número de lugares em pé', 'form-control-label'),
                        ('number-0', 'ilugempe', 'form-control', 0, 3, '16px', lsqlre01[0][12], 'ilugroda', True, None),
                        ('label-0',  'Número de lugares para cadeirantes', 'form-control-label'),
                        ('number-0', 'ilugroda', 'form-control', 0, 3, '16px', lsqlre01[0][13], 'ilugacom', True, None),
                        ('label-0',  'Número de lugares para acompanhantes', 'form-control-label'),
                        ('number-0', 'ilugacom', 'form-control', 0, 3, '16px', lsqlre01[0][14], 'inumport', True, None),
                        ('label-0',  'Número de portas', 'form-control-label'),
                        ('number-0', 'inumport', 'form-control', 0, 3, '16px', lsqlre01[0][15], 'ddataini', True, None),
                        ('label-0',  'Data de aquisição (ou início de atividade)', 'form-control-label'),
                        ('date-0',   'ddataini', 'form-control', '16px', lsqlre01[0][16], 'ddatafim', True, 0, None),
                        ('label-0',  'Data de venda (ou fim de atividade)', 'form-control-label'),
                        ('date-0',   'ddatafim', 'form-control', '16px', lsqlre01[0][17], 'sobserva', True, 0, None),
                        ('hr-0', None),
                        ('checkbox-0', 'barcondi', 1, (1 if lsqlre01[0][18] else 0), 'Courier New', '14px', 'b', 'P', 'Veículo com ar condicionado'),
                        ('checkbox-0', 'bveielev', 1, (1 if lsqlre01[0][19] else 0), 'Courier New', '14px', 'b', 'P', 'Veículo do Elevar'),
                        ('hr-0', None),
                        ('label-0',  'Observação (Opcional) (1000 caracteres)', 'form-control-label'),
                        ('textarea-0', 'sobserva', 'form-control', 2, 1000, '16px', lsqlre01[0][20], 'ssitureg'),
                        ('hr-0', None),
                        ('checkbox-0', 'blibpsod', 1, (1 if lsqlre01[0][21] else 0), 'Courier New', '14px', 'b', 'P', 'Libera o odômetro para ser lançado como novo'),
                        ('checkbox-0', 'blibpsro', 1, (1 if lsqlre01[0][22] else 0), 'Courier New', '14px', 'b', 'P', 'Libera a roleta para ser lançada como nova'),
                        ('hr-0', None),
                        ('label-0',  'Situação do registro', 'form-control-label'),
                        ('select-0', 'ssitureg', 'form-control', '16px', 'btmodsav', abnf_personal_retorna_lista(10001), 0, lsqlre01[0][23], False),
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
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidveicu', 0),)])             # ==> Indicativo para dizer que é novo registro. Obs: tem que ter essa vírgula: "),)])"
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '02C00302A'),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
            icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
            lidmodel = abnf_database_sqlx(icodbase, 'L', '02002A', 1, (0, None))
            lnewpage = [
                ('div-0', 'container', None, None),
                ('hr-0', None),
                ('div-0', 'row', None, None),
                ('div-0', 'col d-flex justify-content-center', None, None),
                ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                ('legend-0', 'Cadastro de Veículos - [ Novo registro ]'),
                ('hr-0', None),
                ('label-0',  'Prefixo', 'form-control-label'),
                ('input-0',  'sprefvei', 'form-control', 0, 20, '16px', None, 'splacave', True, 0),
                ('label-0',  'Placa', 'form-control-label'),
                ('input-0',  'splacave', 'form-control', 0, 8, '16px', None, 'iidmodel', True, 0),
                ('label-0',  'Marca - Modelo', 'form-control-label'),
                ('select-0', 'iidmodel', 'form-control', '16px', 'srenavam', lidmodel, 0, None, False),
                ('label-0',  'Renavam', 'form-control-label'),
                ('input-0',  'srenavam', 'form-control', 0, 30, '16px', None, 'schassiv', True, 0),
                ('label-0',  'Chassi', 'form-control-label'),
                ('input-0',  'schassiv', 'form-control', 0, 30, '16px', None, 'scorveic', True, 0),
                ('label-0',  'Cor', 'form-control-label'),
                ('input-0',  'scorveic', 'form-control', 0, 30, '16px', None, 'ianofabr', True, 0),
                ('label-0',  'Ano de fabricação', 'form-control-label'),
                ('number-0', 'ianofabr', 'form-control', 0, 4, '16px', None, 'ianomode', True, None),
                ('label-0',  'Ano do modelo', 'form-control-label'),
                ('number-0', 'ianomode', 'form-control', 0, 4, '16px', None, 'itipmoto', True, None),
                ('label-0',  'Tipo de motor', 'form-control-label'),
                ('select-0', 'itipmoto', 'form-control', '16px', 'itipcomb', abnf_personal_retorna_lista(10201), 0, None, False),
                ('label-0',  'Combustível', 'form-control-label'),
                ('select-0', 'itipcomb', 'form-control', '16px', 'icaptanq', abnf_personal_retorna_lista(10202), 0, None, False),
                ('label-0',  'Capacidade do tanque (litros)', 'form-control-label'),
                ('number-0', 'icaptanq', 'form-control', 0, 4, '16px', None, 'ilugsent', True, None),
                ('label-0',  'Número de lugares sentados', 'form-control-label'),
                ('number-0', 'ilugsent', 'form-control', 0, 3, '16px', None, 'ilugempe', True, None),
                ('label-0',  'Número de lugares em pé', 'form-control-label'),
                ('number-0', 'ilugempe', 'form-control', 0, 3, '16px', None, 'ilugroda', True, None),
                ('label-0',  'Número de lugares para cadeirantes', 'form-control-label'),
                ('number-0', 'ilugroda', 'form-control', 0, 3, '16px', None, 'ilugacom', True, None),
                ('label-0',  'Número de lugares para acompanhantes', 'form-control-label'),
                ('number-0', 'ilugacom', 'form-control', 0, 3, '16px', None, 'inumport', True, None),
                ('label-0',  'Número de portas', 'form-control-label'),
                ('number-0', 'inumport', 'form-control', 0, 3, '16px', None, 'ddataini', True, None),
                ('label-0',  'Data de aquisição (ou início de atividade)', 'form-control-label'),
                ('date-0',   'ddataini', 'form-control', '16px', None, 'ddatafim', True, 0, None),
                ('label-0',  'Data de venda (ou fim de atividade)', 'form-control-label'),
                ('date-0',   'ddatafim', 'form-control', '16px', None, 'sobserva', True, 0, None),
                ('hr-0', None),
                ('checkbox-0', 'barcondi', 1, 0, 'Courier New', '14px', 'b', 'P', 'Veículo com ar condicionado'),
                ('checkbox-0', 'bveielev', 1, 0, 'Courier New', '14px', 'b', 'P', 'Veículo do Elevar'),
                ('hr-0', None),
                ('label-0',  'Observação (Opcional) (1000 caracteres)', 'form-control-label'),
                ('textarea-0', 'sobserva', 'form-control', 2, 1000, '16px', None, 'btmodsav'),
                ('hr-0', None),
                ('checkbox-0', 'blibpsod', 1, 0, 'Courier New', '14px', 'b', 'P', 'Libera o odômetro para ser lançado como novo'),
                ('checkbox-0', 'blibpsro', 1, 0, 'Courier New', '14px', 'b', 'P', 'Libera a roleta para ser lançada como nova'),
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
        elif dabnfopg['abnfobj0'] == ['btrelcad', 'btrelcad']:      # Relação de veículos cadastrados
            abnf000u02c00303_cadastro_veiculos(dabnfopg)
            
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u02c00302_cadastro_veiculos ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de Veículos.                                                                                                                               // #
# // Gravação dos registros e geração de log.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u02c00302_cadastro_veiculos(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u02c00302_cadastro_veiculos(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        if dabnfopg['abnfobj0'] == ['btcancel', 'btcancel']:        # Voltar para tela anterior
            abnf000u02c00300_cadastro_veiculos(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btsalreg', 'btsalreg']:      # Salvar o registro
            iidveicu = dglobaux['iidveicu']
            lmfields = [
                ['sprefvei', 'input',    'M', 'prefixo do veículo',                         ['Notnull', 'D'],                    None],
                ['splacave', 'input',    'F', 'placa do veículo',                           ['Notnull', 'D'],                    None],
                ['iidmodel', 'select',   'F', 'marca/modelo do veículo',                    ['Notnull', 'D'],                    None],
                ['srenavam', 'input',    'M', 'renavam do veículo',                         ['Notnull', 'D'],                    None],
                ['schassiv', 'input',    'M', 'chassi do veículo',                          ['Notnull', 'D'],                    None],
                ['scorveic', 'input',    'F', 'cor do veículo',                             ['Notnull', 'D'],                    None],
                ['ianofabr', 'number',   'M', 'ano de fabricação',                          ['Notnull', 'D', 'Return_integer'],  None],
                ['ianomode', 'number',   'M', 'ano do modelo',                              ['Notnull', 'D', 'Return_integer'],  None],
                ['itipmoto', 'select',   'M', 'tipo de motor',                              ['Notnull', 'D', 'Return_integer'],  None],
                ['itipcomb', 'select',   'M', 'combustível do veículo',                     ['Notnull', 'D', 'Return_integer'],  None],
                ['icaptanq', 'number',   'F', 'capacidade do tanque',                       ['Notnull', 'D', 'Return_integer'],  None],
                ['ilugsent', 'number',   'M', 'número de lugares sentados',                 ['Notnull', 'D', 'Return_integer'],  None],
                ['ilugempe', 'number',   'M', 'número de lugares em pé',                    ['Return_integer', 'Empty_to_zero'], None],
                ['ilugroda', 'number',   'M', 'número de lugares para cadeirantes',         ['Return_integer', 'Empty_to_zero'], None],
                ['ilugacom', 'number',   'M', 'número de lugares para acompanhantes',       ['Return_integer', 'Empty_to_zero'], None],
                ['inumport', 'number',   'M', 'número de portas do veículo',                ['Notnull', 'D', 'Return_integer'],  None],
                ['ddataini', 'date',     'F', 'data de aquisição (ou início de atividade)', ['Notnull', 'D', 'Return_date'],     None],
                ['ddatafim', 'date',     'F', 'data de venda (ou fim de atividade)',        ['Return_date'],                     None],
                ['barcondi', 'checkbox', 'M', 'veículo com ar condicionado',                [],                                  None],
                ['bveielev', 'checkbox', 'M', 'veículo do Elevar',                          [],                                  None],
                ['sobserva', 'textarea', 'F', 'observação',                                 [],                                  None],
                ['blibpsod', 'checkbox', 'F', 'liberação o odômetro',                       [],                                  None],
                ['blibpsro', 'checkbox', 'F', 'liberação a roleta',                         [],                                  None],
            ]
            if iidveicu > 0: lmfields = lmfields + [
                ['ssitureg', 'select',   'F', 'situação do registro',                       ['Notnull', 'D'],                    None],
            ]            
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btsalreg')
            if bvalidad:
                sprefvei = lmfields[0][5]
                splacave = lmfields[1][5]
                iidmodel = lmfields[2][5]
                srenavam = lmfields[3][5]
                schassiv = lmfields[4][5]
                scorveic = lmfields[5][5]
                ianofabr = lmfields[6][5]
                ianomode = lmfields[7][5]
                itipmoto = lmfields[8][5]
                itipcomb = lmfields[9][5]
                icaptanq = lmfields[10][5]
                ilugsent = lmfields[11][5]
                ilugempe = lmfields[12][5]
                ilugroda = lmfields[13][5]
                ilugacom = lmfields[14][5]
                inumport = lmfields[15][5]
                ddataini = lmfields[16][5]
                ddatafim = lmfields[17][5]
                barcondi = lmfields[18][5]
                bveielev = lmfields[19][5]
                sobserva = lmfields[20][5]
                blibpsod = lmfields[21][5]
                blibpsro = lmfields[22][5]
                if iidveicu > 0:
                    ssitureg = lmfields[23][5]
                lmrulesx = [
                    ['e1>=limite', ianofabr, 'M', 'ano de fabricação', 2000],
                    ['e2>=e1', ianofabr, 'M', 'ano de fabricação', ianomode, 'M', 'ano do modelo'],
                    ['e1<=limite', icaptanq, 'F', 'capacidade do tanque', 2000],
                    ['e2>=e1', ddataini, 'F', 'data de aquisição (ou início de atividade)', ddatafim, 'F', 'data de venda (ou fim de atividade)'],
                ]
                bvalidad =  abnf_check_rules_fields(lmrulesx, 'btsalreg')
                if bvalidad:
                    icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
                    iidfilia = dglobaux['iidfilia']
                    if abnf_database_registro_nao_ativo(icodbase, 'abnf_cadastro_veiculos_modelos', iidmodel, 'M', 'modelo do veículo', ('desmode', 'codmode')):  pass
                    elif iidveicu == 0:   # Novo registro
                        lcamposb = ('prefvei', None)
                        lfilbusc = (('prefvei', '=', sprefvei), ('idfilia', '=', iidfilia), ('situreg', '!=', 'C'))
                        lorderby = None
                        lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_veiculos', lcamposb, lfilbusc, lorderby)
                        if lsqlre01 != [] or iqtdre01 != 0:
                            abnf_alert('Não foi possível salvar! O prefixo ' + sprefvei + ' já está sendo utilizado em outro registro!', 4)
                        else:
                            bvalidad, iproxiid = abnf_database_insere_dados_v02(icodbase, sabnproj, 'abnf_cadastro_veiculos', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                            [
                                ('prefvei', sprefvei),
                                ('placave', splacave),
                                ('idmodel', iidmodel),
                                ('renavam', srenavam),
                                ('chassiv', schassiv),
                                ('corveic', scorveic),
                                ('anofabr', ianofabr),
                                ('anomode', ianomode),
                                ('tipmoto', itipmoto),
                                ('tipcomb', itipcomb),
                                ('captanq', icaptanq),
                                ('lugsent', ilugsent),
                                ('lugempe', ilugempe),
                                ('lugroda', ilugroda),
                                ('lugacom', ilugacom),
                                ('numport', inumport),
                                ('dataini', ddataini),
                                ('datafim', ddatafim),
                                ('arcondi', barcondi),
                                ('veielev', bveielev),
                                ('observa', sobserva),
                                ('libpsod', blibpsod),
                                ('libpsro', blibpsro),
                                ('idfilia', iidfilia),
                                ('situreg', 'A'),
                            ])
                            if bvalidad:
                                abnf_alert('Novo veículo gravado com sucesso!', 3)
                                abnf000u02c00300_cadastro_veiculos(dabnfopg)
                    elif iidveicu > 0:  # Registro existente
                        lcamposb = ('prefvei', None)
                        lfilbusc = (('prefvei', '=', sprefvei), ('idfilia', '=', iidfilia), ('situreg', '!=', 'C'), ('idveicu', '!=', iidveicu))
                        lorderby = None
                        lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_veiculos', lcamposb, lfilbusc, lorderby)
                        if lsqlre01 != [] or iqtdre01 != 0:
                            abnf_alert('Não foi possível salvar! O prefixo ' + sprefvei + ' já está sendo utilizado em outro registro!', 4)
                        else:
                            bvalidad = abnf_database_altera_dados_v02(icodbase, sabnproj, 'abnf_cadastro_veiculos', iidveicu, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                            [
                                ('prefvei', sprefvei),
                                ('placave', splacave),
                                ('idmodel', iidmodel),
                                ('renavam', srenavam),
                                ('chassiv', schassiv),
                                ('corveic', scorveic),
                                ('anofabr', ianofabr),
                                ('anomode', ianomode),
                                ('tipmoto', itipmoto),
                                ('tipcomb', itipcomb),
                                ('captanq', icaptanq),
                                ('lugsent', ilugsent),
                                ('lugempe', ilugempe),
                                ('lugroda', ilugroda),
                                ('lugacom', ilugacom),
                                ('numport', inumport),
                                ('dataini', ddataini),
                                ('datafim', ddatafim),
                                ('arcondi', barcondi),
                                ('veielev', bveielev),
                                ('observa', sobserva),
                                ('libpsod', blibpsod),
                                ('libpsro', blibpsro),
                                ('idfilia', iidfilia),
                                ('situreg', ssitureg),
                            ])
                            if bvalidad:
                                abnf_alert('Registro alterado com sucesso!', 3)
                                abnf000u02c00300_cadastro_veiculos(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btexcreg', 'btexcreg']:      # Excluir registro
            iidveicu = dglobaux['iidveicu']        
            icodbase = int(dabnfopg['abnproje'][2][14:]) * 100      # Código do banco de dados a ser utilizado
            bvalidad = abnf_database_exclui_registro(icodbase, sabnproj, 'abnf_cadastro_veiculos', iidveicu, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'])
            if bvalidad:
                abnf_alert('Registro excluído com sucesso!', 3)
                abnf000u02c00300_cadastro_veiculos(dabnfopg)
                
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u02c00303_cadastro_veiculos ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de Veículos.                                                                                                                               // #
# // Relatório de veículos.                                                                                                                              // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
                
def abnf000u02c00303_cadastro_veiculos(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u02c00303_cadastro_veiculos(dabnfopg)')
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
        icolspan = 7
        ifontlen = 2
        icontreg = 0
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
            abnf_imprime_thead_005_datetime(sarquwri, icolspan)
            abnf_imprime_line(sarquwri, icolspan, 'darkcyan')
            abnf_imprime_info_001(sarquwri, '#D1C5C5', 'center', 1,
                [
                    ('Prefixo',  1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Placa',    1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Marca',    1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Modelo',   1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Início',   1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Término',  1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Situação', 1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                ]
            )
            abnf_imprime_fthead_tbody(sarquwri)
            lsqlre01 = abnf_database_sqlx(icodbase, 'X', '02003B', 1, (0, iidfilia))
            for lauxi001 in lsqlre01:
                sauxi001 = lauxi001[2] + ' (' + str(lauxi001[3]) + ')'
                sauxi002 = lauxi001[4] + ' (' + str(lauxi001[5]) + ')'
                sdataini = abnf_converte_data(lauxi001[6])
                sdatafim = abnf_converte_data(lauxi001[7])
                ssitureg = abnf_personal_retorna_string(10001, lauxi001[8])
                icontreg += 1
                abnf_imprime_info_001(sarquwri, None, None, 1,
                    [
                        (lauxi001[0], 1, 0, None, 'Left',   'black', 'Courier New', ifontlen, True, False),
                        (lauxi001[1], 1, 0, None, 'Left',   'black', 'Courier New', ifontlen, True, False),
                        (sauxi001,    1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                        (sauxi002,    1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                        (sdataini,    1, 0, None, 'Center', 'black', 'Courier New', ifontlen, True, False),
                        (sdatafim,    1, 0, None, 'Center', 'black', 'Courier New', ifontlen, True, False),
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