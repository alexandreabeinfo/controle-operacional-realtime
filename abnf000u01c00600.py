## ===========================================================
## [abnf000u01c00600.py] - Cadastro de Clientes e Fornecedores
## ===========================================================

from abnfsrc.abnf000u00s00003 import *              # Arquivo de funções comuns que serão utilizadas por todos os módulos do sistema
from abnfsrc.abnf000u00s00004 import *              # Arquivo de banco de dados

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u01c00600_cadastro_clientes_fornecedores ] ////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de Clientes e Fornecedores.                                                                                                                // #
# // Form inicial.                                                                                                                                       // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u01c00600_cadastro_clientes_fornecedores(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u01c00600_cadastro_clientes_fornecedores(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        abnf_socket_004([1, 'abnfdv03', abnf_create_spinner(1, 100)])
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        if   dglobaux['sabnfsys'] in ['01C00600A','01C00602A']: sctrlmod = ['Clientes'    , 'cliente'   , 'clientes'    , '01C00601A', '010B']
        elif dglobaux['sabnfsys'] in ['01C00600B','01C00602B']: sctrlmod = ['Fornecedores', 'fornecedor', 'fornecedores', '01C00601B', '010C']
        abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', sctrlmod[3]),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        lidclfor = abnf_database_menu(icodbase, None, 'L', sctrlmod[4], 1, 1, 2)
        # Debug: (inicio)
        # abnf_show('08', iidclfor, 1)
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
            ('legend-0', 'Cadastro de ' + sctrlmod[0]),
            ('hr-0', None),
            ('label-0',  'Código do ' + sctrlmod[1], 'form-control-label'),
            ('number-0', 'icodclfo', 'form-control', 0, 6, '14px', None, 'btbusreg', True, '01C006A'),
            ('label-1', 'Courier New;', '20px', 'darkcyan', 'form-control-label', 'sdesclfo', None),
            ('br-0', None),
            ('label-0',  'Lista de ' + sctrlmod[2], 'form-control-label'),
            ('select-0', 'iidclfor', 'form-control', '16px', 'btbusreg', lidclfor, 1, None, False),
            ('hr-0', None),
            ('button-0', 'btbusreg', 'btn btn-primary mt-2', 'Buscar'),
            ('alt255-0', 2),
            ('button-0', 'btnovreg', 'btn btn-primary mt-2', 'Novo registro'),
            ('alt255-0', 2),
            ('button-0', 'btrelcad', 'btn btn-primary mt-2', 'Relação de ' + sctrlmod[2]),
            ('form-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
        ]
        snewpage = abnf_create_page(lnewpage)
        abnf_socket_004([1, 'abnfdv03', snewpage])
        
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u01c00601_cadastro_clientes_fornecedores ] ////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de Clientes e Fornecedores.                                                                                                                // #
# // Form de cadastro/alteração do cliente.                                                                                                              // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u01c00601_cadastro_clientes_fornecedores(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u01c00601_cadastro_clientes_fornecedores(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        if   dglobaux['sabnfsys'] == '01C00601A': sctrlmod = ['Clientes'    , 'cliente'   , 'clientes'    , 'C', '01C00602A']
        elif dglobaux['sabnfsys'] == '01C00601B': sctrlmod = ['Fornecedores', 'fornecedor', 'fornecedores', 'F', '01C00602B']
        # abnf_show('07', dabnfopg['icodclfo'][2], 0)
        # abnf_show('08', dabnfopg['sonblurx'], 0)
        # abnf_show('09', dglobaux, 2)
        # abnf_show('10', dabnfopg, 2)
        if dabnfopg['sonblurx'] == '01C006A':
            icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
            sretmess = abnf_database_find(icodbase, None, '010A', dabnfopg['icodclfo'][2], [sctrlmod[3]])
            abnf_socket_004([1, 'sdesclfo', sretmess])
        elif dabnfopg['abnfobj0'] == ['btbusreg', 'btbusreg']:        # Buscar registro existente
            lmfields = [
                ['icodclfo', 'number', 'M', 'código do ' + sctrlmod[1], ['Empty_to_zero']                  , None],
                ['iidclfor', 'input',  'M', 'Lista de '  + sctrlmod[2], ['Empty_to_zero', 'Return_integer'], None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btbusreg')
            # Debug: (inicio)
            # abnf_show('08', lmfields, 1)
            # abnf_show('09', dabnfopg, 2)
            # abnf_show('10', dglobaux, 2)
            # Debug: (fim)
            if bvalidad:
                icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
                icodclfo = lmfields[0][5]
                iidclfor = lmfields[1][5]
                if icodclfo == 0 and iidclfor == 0:
                    abnf_alert('Um dos campos de busca tem que ser preenchido!', 5)
                    abnf_socket_004([5, 'btbusreg'])
                elif icodclfo > 0 and iidclfor > 0:
                    abnf_alert('Utilize somente um dos campos de busca!', 5)
                    abnf_socket_004([5, 'btbusreg'])
                else:
                    # //////////////////////////////////////////////////
                    # Buscando o cliente caso seja um registro existente
                    # //////////////////////////////////////////////////
                    lcamposb = ('idclfor', 'codclfo', 'idcpfpj', 'ccontab', 'situreg', 'observa')
                    if   icodclfo > 0: lfilbusc = (('tipclfo', '=', sctrlmod[3]), ('codclfo', '=', icodclfo), ('situreg', '!=', 'C'))
                    elif iidclfor > 0: lfilbusc = (('idclfor', '=', iidclfor), ('situreg', '!=', 'C'))
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_clientes_fornecedores', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 == [] or iqtdre01 == 0:
                        abnf_alert('O ' + sctrlmod[1] + ' não foi encontrado!', 4)
                        abnf_socket_004([5, 'btbusreg'])
                    else:
                        # Debug: (inicio)
                        # abnf_show('10', lsqlre01, 1)
                        # Debug: (fim)
                        abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidclfor', lsqlre01[0][0]),)])    # ==> Guardando o ID do registro. Obs: tem que ter essa vírgula: "),)])"
                        abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', sctrlmod[4]),)])       # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
                        lidcpfpj = abnf_database_menu(icodbase, None, 'L', '010A', 1, 2, 2)
                        lnewpage = [
                            ('div-0', 'container', None, None),
                            ('hr-0', None),
                            ('div-0', 'row', None, None),
                            ('div-0', 'col d-flex justify-content-center', None, None),
                            ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                            ('legend-0', 'Cadastro de ' + sctrlmod[0] + ' - [ Registro existente ]'),
                            ('hr-0', None),
                            ('label-0',  'Código do ' + sctrlmod[1], 'form-control-label'),
                            ('number-0', 'icodclfo', 'form-control', 0, 6, '16px', lsqlre01[0][1], 'iidcpfpj', True, None),
                            ('label-0',  'CPF/CNPJ', 'form-control-label'),
                            ('select-0', 'iidcpfpj', 'form-control', '16px', 'iccontab', lidcpfpj, 1, lsqlre01[0][2], False),
                            ('label-0',  'Conta contábil', 'form-control-label'),
                            ('number-0', 'iccontab', 'form-control', 0, 10, '16px', lsqlre01[0][3], 'ssitureg', True, None),
                            ('label-0',  'Situação do registro', 'form-control-label'),
                            ('select-0', 'ssitureg', 'form-control', '16px', 'sobserva', abnf_personal_retorna_lista(10001), 0, lsqlre01[0][4], False),
                            ('hr-0', None),
                            ('label-0',  'Observação (Opcional) (1000 caracteres)', 'form-control-label'),
                            ('textarea-0', 'sobserva', 'form-control', 2, 1000, '16px', lsqlre01[0][5], 'btmodsav'),
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
                        # abnf_show('08', lsqlre01[0], 1)
                        # abnf_show('09', lnewpage, 1)
                        # abnf_socket_004([3, 'sobserva', 'TESTE DE DADOS NA OBSERVAÇÂO'])
                        # Debug: (fim)                    
        elif dabnfopg['abnfobj0'] == ['btnovreg', 'btnovreg']:      # Novo registro
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidclfor', 0),)])             # ==> Indicativo para dizer que é novo registro. Obs: tem que ter essa vírgula: "),)])"
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', sctrlmod[4]),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
            icodbase = int(dabnfopg['abnproje'][2][14:]) * 100      # Código do banco de dados a ser utilizado
            lidcpfpj = abnf_database_menu(icodbase, None, 'L', '010A', 1, 2, 2)
            lnewpage = [
                ('div-0', 'container', None, None),
                ('hr-0', None),
                ('div-0', 'row', None, None),
                ('div-0', 'col d-flex justify-content-center', None, None),
                ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                ('legend-0', 'Cadastro de ' + sctrlmod[0] + ' - [ Novo registro ]'),
                ('hr-0', None),
                ('label-0',  'Código do ' + sctrlmod[1], 'form-control-label'),
                ('number-0', 'icodclfo', 'form-control', 0, 6, '16px', None, 'iidcpfpj', True, None),
                ('label-0',  'CPF/CNPJ', 'form-control-label'),
                ('select-0', 'iidcpfpj', 'form-control', '16px', 'iccontab', lidcpfpj, 1, None, False),
                ('label-0',  'Conta contábil', 'form-control-label'),
                ('number-0', 'iccontab', 'form-control', 0, 10, '16px', None, 'sobserva', True, None),
                ('hr-0', None),
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
            # abnf_socket_004([3, 'icodclfo', '150'])
            # abnf_socket_004([3, 'iidcpfpj', '1'])
            # abnf_socket_004([3, 'sobserva', 'TESTE DE DADOS NA OBSERVAÇÃO'])
            # Debug: (fim)
        elif dabnfopg['abnfobj0'] == ['btrelcad', 'btrelcad']:      # Relação de clientes/fornecedores cadastrados
            abnf000u01c00603_cadastro_clientes_fornecedores(dabnfopg, sctrlmod[3], 'btrelcad')
            
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u01c00602_cadastro_clientes_fornecedores ] ////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de Clientes e Fornecedores.                                                                                                                // #
# // Gravação dos registros e geração de log.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u01c00602_cadastro_clientes_fornecedores(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u01c00602_cadastro_clientes_fornecedores(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        if   dglobaux['sabnfsys'] == '01C00602A': sctrlmod = ['cliente'   , 'C']
        elif dglobaux['sabnfsys'] == '01C00602B': sctrlmod = ['fornecedor', 'F']
        if dabnfopg['abnfobj0'] == ['btcancel', 'btcancel']:        # Voltar para tela anterior
            abnf000u01c00600_cadastro_clientes_fornecedores(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btsalreg', 'btsalreg']:      # Salvar o registro
            iidclfor = dglobaux['iidclfor']
            lmfields = [
                ['icodclfo', 'number',   'M', 'código do ' + sctrlmod[0], ['Notnull', 'D'],  None],
                ['iidcpfpj', 'select',   'M', 'CPF/CNPJ',                 ['Notnull', 'D'],  None],
                ['iccontab', 'number',   'F', 'conta contábil',           ['Empty_to_null'], None],
                ['sobserva', 'textarea', 'F', 'observação',               [],                None],
            ]
            if iidclfor > 0: lmfields = lmfields + [
                ['ssitureg', 'select',   'F', 'situação do registro',     ['Notnull', 'D'],  None],
            ]            
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btsalreg')
            # Debug: (inicio)
            # abnf_show('10', lmfields, 1)
            # abnf_show('09', dabnfopg, 2)
            # abnf_show('10', dglobaux, 0)
            # Debug: (fim)            
            if bvalidad:
                icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
                if iidclfor == 0:   # Novo registro
                    lcamposb = ('codclfo', 'idclfor')
                    lfilbusc = (('tipclfo', '=', sctrlmod[1]), ('codclfo', '=', lmfields[0][5]), ('situreg', '!=', 'C'))
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_clientes_fornecedores', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 != [] or iqtdre01 != 0:
                        abnf_alert('Não foi possível salvar! O código ' + str(lmfields[0][5]) + ' já está sendo utilizado em outro registro!', 4)
                    else:
                        bvalidad, iproxiid = abnf_database_insere_dados_v02(icodbase, sabnproj, 'abnf_cadastro_clientes_fornecedores', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                        [
                            ('tipclfo', sctrlmod[1]   ),
                            ('codclfo', lmfields[0][5]),
                            ('idcpfpj', lmfields[1][5]),
                            ('ccontab', lmfields[2][5]),
                            ('observa', lmfields[3][5]),
                            ('situreg', 'A'           ),
                        ])
                        if bvalidad:
                            abnf_alert('Novo ' + sctrlmod[0] + ' gravado com sucesso!', 3)
                            abnf000u01c00600_cadastro_clientes_fornecedores(dabnfopg)
                elif iidclfor > 0:  # Registro existente
                    lcamposb = ('codclfo', 'idclfor')
                    lfilbusc = (('tipclfo', '=', sctrlmod[1]), ('codclfo', '=', lmfields[0][5]), ('situreg', '!=', 'C'), ('idclfor', '!=', iidclfor))
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_clientes_fornecedores', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 != [] or iqtdre01 != 0:
                        abnf_alert('Não foi possível salvar! O código ' + str(lmfields[0][5]) + ' já está sendo utilizado em outro registro!', 4)
                    else:
                        bvalidad = abnf_database_altera_dados_v02(icodbase, sabnproj, 'abnf_cadastro_clientes_fornecedores', iidclfor, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                        [
                            ('codclfo', lmfields[0][5]),
                            ('idcpfpj', lmfields[1][5]),
                            ('ccontab', lmfields[2][5]),
                            ('observa', lmfields[3][5]),
                            ('situreg', lmfields[4][5]),
                        ])
                        if bvalidad:
                            abnf_alert('Registro alterado com sucesso!', 3)
                            abnf000u01c00600_cadastro_clientes_fornecedores(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btexcreg', 'btexcreg']:      # Excluir registro
            iidclfor = dglobaux['iidclfor']        
            icodbase = int(dabnfopg['abnproje'][2][14:]) * 100      # Código do banco de dados a ser utilizado
            bvalidad = abnf_database_exclui_registro(icodbase, sabnproj, 'abnf_cadastro_clientes_fornecedores', iidclfor, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'])
            if bvalidad:
                abnf_alert('Registro excluído com sucesso!', 3)
                abnf000u01c00600_cadastro_clientes_fornecedores(dabnfopg)
                
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u01c00603_cadastro_clientes_fornecedores ] ////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de Clientes e Fornecedores.                                                                                                                // #
# // Relatório de clientes.                                                                                                                              // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
                
def abnf000u01c00603_cadastro_clientes_fornecedores(dabnfopg, stipclfo, sbuttrel):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u01c00603_cadastro_clientes_fornecedores(dabnfopg, stipclfo, sbuttrel)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        abnf_alert('Aguarde! Gerando relatório...', 15)
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        if   stipclfo == 'C': sctrlmod = ['CLIENTES'    , 'C']
        elif stipclfo == 'F': sctrlmod = ['FORNECEDORES', 'F']
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        # /////////////////////
        # Variaveis de ambiente
        # /////////////////////
        icolspan = 5
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
            abnf_imprime_thead_002_titulo_relatorio(sarquwri, icolspan, 'RELAÇÃO DE ' + sctrlmod[0])
            abnf_imprime_thead_003_empresa_filial(sarquwri, icolspan, snomeemp, snomefil)
            # smensage = 'Per&iacute;odo: ' + abnf_converte_data(ddataini) + ' &agrave;s ' + abnf_converte_hora(thoraini) + ' at&eacute; ' + abnf_converte_data(ddatafim) + ' &agrave;s ' + abnf_converte_hora(thorafim)
            # abnf_imprime_thead_004_parametros(sarquwri, icolspan, smensage)
            abnf_imprime_thead_005_datetime(sarquwri, icolspan)
            abnf_imprime_line(sarquwri, icolspan, 'darkcyan')
            abnf_imprime_info_001(sarquwri, '#D1C5C5', 'center', 1,
                [
                    ('Nome/Razão Social', 1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Código',            1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('CPF/CNPJ',          1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Conta contábil',    1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Situação',          1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                ]
            )
            abnf_imprime_fthead_tbody(sarquwri)
            lcamposb = ('nomraso', 'codpfpj', 'idcpfpj')
            lfilbusc = (('situreg', '!=', 'C'), None )
            lorderby = ('nomraso', 'idcpfpj')
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_cpfcnpj', lcamposb, lfilbusc, lorderby)
            lcamposb = ('codclfo', 'situreg', 'idcpfpj', 'ccontab')
            lfilbusc = (('situreg', '!=', 'C'), ('tipclfo', '=', sctrlmod[1]))
            lorderby = ('tipclfo', 'codclfo', 'idclfor')
            lsqlre02, iqtdre02 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_clientes_fornecedores', lcamposb, lfilbusc, lorderby)
            for lauxi001 in lsqlre01:
                for lauxi002 in lsqlre02:
                    if lauxi001[2] == lauxi002[2]:
                        ssitureg = abnf_personal_retorna_string(10001, lauxi002[1])
                        iccontab = lauxi002[3] if lauxi002[3] != None else ''
                        icontreg += 1
                        abnf_imprime_info_001(sarquwri, None, None, 1,
                            [
                                (lauxi001[0], 1, 0, None, 'Left'    , 'black', 'Courier New', ifontlen, True, False),
                                (lauxi002[0], 1, 0, None, 'Center'  , 'black', 'Courier New', ifontlen, True, False),
                                (lauxi001[1], 1, 0, None, 'Center'  , 'black', 'Courier New', ifontlen, True, False),
                                (iccontab,    1, 0, None, 'Center'  , 'black', 'Courier New', ifontlen, True, False),
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
        abnf_socket_004([5, sbuttrel])
        abnf_alert('Relatório gerado com sucesso!', 3)
        time.sleep(5)
        abnf_alert('', 0)
                    
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #