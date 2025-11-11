## ====================================================================
## [abnf000u13c00700.py] - Operacional - Cadastro de Grupos de Veículos
## ====================================================================

from abnfsrc.abnf000u00s00003 import *              # Arquivo de funções comuns que serão utilizadas por todos os módulos do sistema
from abnfsrc.abnf000u00s00004 import *              # Arquivo de banco de dados

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00700_operacional_cadastro_grupos_veiculos ] //////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Grupos de Veículos.                                                                                                       // #
# // Form inicial.                                                                                                                                       // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00700_operacional_cadastro_grupos_veiculos(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00700_operacional_cadastro_grupos_veiculos(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, '13C00701A'])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        lidogrve = abnf_database_menu(icodbase, iidfilia, 'L', '1321A', 1, 1, 2)
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
            ('legend-0', 'Operacional - Cadastro de Grupos de Veículos'),
            ('hr-0', None),
            ('label-0',  'Grupo de veiculos', 'form-control-label'),
            ('select-0', 'iidogrve', 'form-control', '16px', 'ssentido', lidogrve, 1, None, False),
            ('hr-0', None),
            ('button-0', 'btbusreg', 'btn btn-primary mt-2', 'Buscar'),
            ('alt255-0', 2),
            ('button-0', 'btnovreg', 'btn btn-primary mt-2', 'Novo registro'),
            ('hr-0', None),
            ('button-0', 'btrelgrv', 'btn btn-primary mt-2', 'Relação de grupos com seus respetivos veículos'),
            ('alt255-0', 2),
            ('button-0', 'btrelveg', 'btn btn-primary mt-2', 'Relação de veículos com seus respetivos grupos'),
            ('form-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
        ]
        snewpage = abnf_create_page(lnewpage)
        abnf_socket_004([1, 'abnfdv03', snewpage])
        
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00701_operacional_cadastro_grupos_veiculos ] //////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Grupos de Veículos.                                                                                                       // #
# // Form de cadastro/alteração do grupo de veículos.                                                                                                    // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00701_operacional_cadastro_grupos_veiculos(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00701_operacional_cadastro_grupos_veiculos(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        if dabnfopg['abnfobj0'] in (['btbusreg', 'btbusreg'], ['btnovreg', 'btnovreg']):
            if dabnfopg['abnfobj0'] == ['btbusreg', 'btbusreg']:        # Buscar registro existente
                lmfields = [
                    ['iidogrve', 'input',  'M', 'grupo de veículo', ['Notnull', 'D', 'Return_integer'], None],
                ]
                bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btbusreg')
                # Debug: (inicio)
                # abnf_show('08', lmfields, 1)
                # abnf_show('09', dabnfopg, 2)
                # abnf_show('10', dglobaux, 2)
                # Debug: (fim)
                if bvalidad:
                    iidogrve = lmfields[0][5]
                    # ///////////////////////////
                    # Buscando o grupo de veículo
                    # ///////////////////////////
                    lcamposb = ('codogrf', 'descgrf', 'situreg')
                    lfilbusc = (('idogrve', '=', iidogrve), ('situreg', '!=', 'C'))
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_grupos_veiculos', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 == [] or iqtdre01 == 0:
                        abnf_alert('O grupo de veículo não foi encontrado!', 4)
                        abnf_socket_004([5, 'btbusreg'])
                        bvalidad = False
                    else:
                        lidveicu = abnf_database_menu(icodbase, iidfilia, 'L', '0203', 0, 1, None)
                        icodogrf = lsqlre01[0][0]
                        sdescgrf = lsqlre01[0][1]
                        ssitureg = lsqlre01[0][2]
                        lidveigr = []   # <= Veículos do grupo
                        lidveifo = []   # <= Veículos fora do grupo
                        # /////////////////////////////////////////////////
                        # Criando as listas de veículo do grupo e fora dele
                        # /////////////////////////////////////////////////
                        lcamposb = ('idveicu', None)
                        lfilbusc = (('idogrve', '=', iidogrve), ('situreg', '!=', 'C'))
                        lorderby = None
                        lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_grupos_veiculos_vinculos', lcamposb, lfilbusc, lorderby)
                        for lauxi001 in lidveicu:
                            iidveicu = lauxi001[0]
                            sprefvei = lauxi001[1][0]
                            splacave = lauxi001[1][1]
                            bidveigr = False
                            if lsqlre01 != [] or iqtdre01 != 0:
                                for lauxi002 in lsqlre01:
                                    if lauxi002[0] == iidveicu:
                                        lidveigr.append((sprefvei, splacave, iidveicu))
                                        bidveigr = True
                                        break
                            if not bidveigr:
                                lidveifo.append((sprefvei, splacave, iidveicu))
            elif dabnfopg['abnfobj0'] == ['btnovreg', 'btnovreg']:        # Novo registro
                lidveicu = abnf_database_menu(icodbase, iidfilia, 'L', '0203', 0, 1, None)
                iidogrve = 0
                icodogrf = abnf_database_valor_maximo_campo(icodbase, 'abnf_operacional_cadastro_grupos_veiculos', 'codogrf', None) + 1
                sdescgrf = ''
                lidveigr = []   # <= Veículos do grupo
                lidveifo = []   # <= Veículos fora do grupo
                # ///////////////////////////////////////////////////////////////
                # Criando as listas de veículo geral (para ser incluída no grupo)
                # ///////////////////////////////////////////////////////////////
                for lauxi001 in lidveicu:
                    iidveicu = lauxi001[0]
                    sprefvei = lauxi001[1][0]
                    splacave = lauxi001[1][1]
                    lidveifo.append((sprefvei, splacave, iidveicu))
            # //////////////////////////////////////////////
            # Busca de veículos sem grupo e montagem da tela
            # //////////////////////////////////////////////
            if bvalidad:
                abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '13C00702A'),)]) # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
                abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidogrve', iidogrve),)])    # ==> Guardado dados do grupo de veículo para a próxima função. Obs: tem que ter essa vírgula: "),)])"
                # ////////////////
                # Tela de cadastro
                # ////////////////
                if iidogrve > 0:
                    sauxi001 = '[ Registro existente ]'
                    sauxi002 = 'ssitureg'
                else:    
                    sauxi001 = '[ Novo registro ]'
                    sauxi002 = 'btinsvei'
                lsitureg = abnf_personal_retorna_lista(10001)
                lnewpage = [
                    ('div-0', 'container', None, None),
                    ('hr-0', None),
                    ('div-0', 'row', None, None),
                    ('div-0', 'col d-flex justify-content-center', None, None),
                    ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                    ('table-0', 'table table-bordered table-sm table-responsive'),
                        ('tr-0', 'text-white bg-secondary', False),
                            ('td-0', None, 2, None, 1, None, None),
                                ('legend-0', 'Cadastro de Grupos de Veículos - ' + sauxi001),
                            ('td-9', None),
                        ('tr-9', None),
                        ('tr-0', None, False),
                            ('td-0', None, None, None, None, None, None),
                                ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                                ('table-0', 'table table-bordered table-sm table-responsive'),
                                    ('tr-0', None, False),
                                        ('td-0', 'table-active', 1, None, 0, None, None), ('label-0', 'Código do grupo', 'form-control-label'),                                       ('td-9', None),
                                        ('td-0', None, 1, None, 0, None, None),           ('label-0', '&nbsp;', 'form-control-label'),                                                ('td-9', None),
                                        ('td-0', None, 1, None, 0, None, None),           ('number-0', 'icodogrf', 'form-control', 0, 4, '16px', icodogrf, 'sdescgrf', True, None),   ('td-9', None),
                                    ('tr-9', None),
                                    ('tr-0', None, False),
                                        ('td-0', 'table-active', 1, None, 0, None, None), ('label-0', 'Descrição do grupo', 'form-control-label'),                                    ('td-9', None),
                                        ('td-0', None, 1, None, 0, None, None),           ('label-0', '&nbsp;', 'form-control-label'),                                                ('td-9', None),
                                        ('td-0', None, 1, None, 0, None, None),           ('input-0', 'sdescgrf', 'form-control', 0, 100, '16px', sdescgrf, sauxi002, True, 0),       ('td-9', None),
                                    ('tr-9', None)
                ]
                if iidogrve > 0:
                    lsitureg = abnf_personal_retorna_lista(10001)
                    lnewpage = lnewpage + [
                                    ('tr-0', None, False),
                                        ('td-0', 'table-active', 1, None, 0, None, None), ('label-0', 'Situação do registro', 'form-control-label'),                                  ('td-9', None),
                                        ('td-0', None, 1, None, 0, None, None),           ('label-0', '&nbsp;', 'form-control-label'),                                                ('td-9', None),
                                        ('td-0', None, 1, None, 0, None, None),           ('select-0', 'ssitureg', 'form-control', '16px', 'btinsvei', lsitureg, 0, ssitureg, False), ('td-9', None),
                                    ('tr-9', None)
                    ]
                lnewpage = lnewpage + [    
                                ('table-9', None),
                                ('form-9', None),
                                ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                                ('table-0', None),
                                    ('tr-0', None, False),
                                        ('td-0', None, 5, None, 1, None, None), 
                                            ('font-0', 'Courier New', '20px', 'blue', 'Veículos fora deste grupo'),
                                        ('td-9', None),
                                        ('td-0', None, 1, None, 1, None, None), ('alt255-0', 5), ('td-9', None),
                                        ('td-0', None, 5, None, 1, None, None),
                                            ('font-0', 'Courier New', '20px', 'red', 'Veículos deste grupo'),
                                        ('td-9', None),
                                    ('tr-9', None),
                                    ('tr-0', None, False),
                                        ('td-0', 'table-active border p-4 mt-2 rounded border-secondary border-2', 5, None, 0, None, None),
                                            ('div-1', 'sdivvfor'), ('div-9', None),
                                        ('td-9', None),
                                        ('td-0', None, 1, None, 1, None, None), ('alt255-0', 5), ('td-9', None),
                                        ('td-0', 'table-active border p-4 mt-2 rounded border-secondary border-2', 5, None, 0, None, None),
                                            ('div-1', 'sdivvgru'), ('div-9', None),
                                        ('td-9', None),
                                    ('tr-9', None),
                                    ('tr-0', None, False),
                                    ('tr-9', None),
                                    ('tr-0', None, False),
                                        ('td-0', None, 1, None, 1, None, None),
                                            ('button-0', 'btinsvei', 'btn btn-primary mt-1', 'Inserir veículos selecionados', None),
                                        ('td-9', None),
                                        ('td-0', None, 1, None, 1, None, None), ('alt255-0', 3), ('td-9', None),
                                        ('td-0', None, 1, None, 1, 1, None),
                                            ('input-0',  'sfilvfor', 'form-control mt-1', 0, 20, '16px', None, 'btfilvfo', True, 0),
                                        ('td-9', None),
                                        ('td-0', None, 1, None, 1, None, None), ('alt255-0', 3), ('td-9', None),
                                        ('td-0', None, 1, None, 1, 1, None),
                                            ('button-0', 'btfilvfo', 'btn btn-primary mt-1', 'Filtrar'),
                                        ('td-9', None),
                                        ('td-0', None, 1, None, 1, None, None), ('alt255-0', 5), ('td-9', None),
                                        ('td-0', None, 1, None, 1, None, None),    
                                            ('button-0', 'btremvei', 'btn btn-danger mt-1', 'Remover veículos selecionados', None),
                                        ('td-9', None),
                                        ('td-0', None, 1, None, 1, None, None), ('alt255-0', 3), ('td-9', None),
                                        ('td-0', None, 1, None, 1, 1, None),
                                            ('input-0',  'sfilvgru', 'form-control mt-1', 0, 20, '16px', None, 'btfilvgr', True, 0),
                                        ('td-9', None),
                                        ('td-0', None, 1, None, 1, None, None), ('alt255-0', 3), ('td-9', None),
                                        ('td-0', None, 1, None, 1, 1, None),
                                            ('button-0', 'btfilvgr', 'btn btn-danger mt-1', 'Filtrar'),
                                        ('td-9', None),                                        
                                    ('tr-9', None), 
                                ('table-9', None),
                                ('form-9', None),
                                ('form-0', 'border p-2 mt-2 rounded border-secondary border-3'),
                                ('table-0', None),
                                    ('tr-0', None, False),
                                        ('td-0', None, 1, None, 1, None, None), ('alt255-0', 5), ('td-9', None),
                                        ('td-0', None, 1, None, 1, None, None),
                                            ('button-1', 'btmodsav', 'btn btn-primary mt-1', 'Salvar', 'Salvar Registro', 'btsalreg', 'btn btn-primary mt-2', 'Salvar', 'Confirma a gravação?'),
                                        ('td-9', None),
                                        ('td-0', None, 1, None, 1, None, None), ('alt255-0', 2), ('td-9', None),
                                        ('td-0', 'table-active', 1, None, 1, None, None), 
                                            ('button-0', 'btcancel', 'btn btn-primary mt-1', 'Cancelar'),
                                        ('td-9', None),
                ]
                if iidogrve > 0:
                    lnewpage = lnewpage + [
                                        ('td-0', None, 1, None, 1, None, None), ('alt255-0', 2), ('td-9', None),
                                        ('td-0', None, 1, None, 1, None, None),    
                                            ('button-1', 'btexclui', 'btn btn-primary mt-1', 'Excluir', 'Excluir Registro', 'btexcreg', 'btn btn-danger mt-2', 'Excluir', 'Confirma a exclusão deste registro?'),
                                        ('td-9', None),
                    ]
                lnewpage = lnewpage + [
                                        ('td-0', None, 1, None, 1, None, None), ('alt255-0', 30), ('td-9', None),
                                        ('td-0', None, 1, None, 1, None, None),
                                            ('table-0', 'table table-bordered table-sm table-responsive border-secondary mt-3'),
                                                ('tr-0', None, False),
                                                    ('td-0', None, 1, None, 1, None, None),
                                                        ('checkbox-0', 'lpermvog', 1, None, 'Courier New', '18px', 'b', 'P', 'Permite incluir veículos que já estejam em outros grupos'),
                                                    ('td-9', None),
                                                ('tr-9', None),
                                            ('table-9', None),
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
                if iidogrve == 0:
                    abnf_socket_004([10, 'btexclui'])               # Desabilita o botão de exclusão do registro
                abnf000u13c00703_operacional_cadastro_grupos_veiculos(sabnproj, sabntoke, lidveifo, lidveigr)
        elif dabnfopg['abnfobj0'] == ['btrelgrv', 'btrelgrv']:      # Relação de grupos com seus respetivos veículos
            abnf000u13c00705_operacional_cadastro_grupos_veiculos(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btrelveg', 'btrelveg']:      # Relação de veículos com seus respetivos grupos
            abnf000u13c00706_operacional_cadastro_grupos_veiculos(dabnfopg)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00702_operacional_cadastro_grupos_veiculos ] //////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Grupos de Veículos.                                                                                                       // #
# // Gravação/exclusão do grupo de veículo.                                                                                                              // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00702_operacional_cadastro_grupos_veiculos(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00702_operacional_cadastro_grupos_veiculos(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        iidogrve = dglobaux['iidogrve']
        if dabnfopg['abnfobj0'] == ['btcancel', 'btcancel']:        # Voltar para tela anterior
            abnf000u13c00700_operacional_cadastro_grupos_veiculos(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btinsvei', 'btinsvei']:      # Inserir veículos no grupo
            lmfields = [
                ['iidveisg', 'checkbox', 'Nenhum veículo foi marcado para ser inserido', ['Notnull', 'Return_integer'], []],
            ]
            bvalidad, lmfields = abnf_find_checkbox_radio(dabnfopg, lmfields, 'btinsvei')
            if bvalidad:
                lidvesel = lmfields[0][4]
                # //////////////////////////////////////
                # Busca na memória as listas de veículos
                # //////////////////////////////////////
                lidveifo = dglobaux['lidveifo']
                lidveigr = dglobaux['lidveigr']
                # //////////////////////////////////////////
                # Insere ítens na lista de veículos do grupo
                # //////////////////////////////////////////
                for lauxi001 in lidveifo:
                    sprefvei = lauxi001[0]
                    splacave = lauxi001[1]
                    iidveicu = lauxi001[2]
                    if iidveicu in lidvesel:
                        lidveigr.append((sprefvei, splacave, iidveicu))
                # //////////////////////////////////////////////////////////////
                # Recria a lista de veículos sem grupo sem os ítens selecionados
                # //////////////////////////////////////////////////////////////
                lidvenew = []
                for lauxi001 in lidveifo:
                    iidveicu = lauxi001[2]
                    if not iidveicu in lidvesel:
                        lidvenew.append(lauxi001)
                lidveifo = lidvenew
                # ///////////////////////////////////
                # Atualiza as listas e mostra em tela
                # ///////////////////////////////////
                abnf000u13c00703_operacional_cadastro_grupos_veiculos(sabnproj, sabntoke, lidveifo, lidveigr)
        elif dabnfopg['abnfobj0'] == ['btremvei', 'btremvei']:      # Remover veículos do grupo
            lmfields = [
                ['iidveigr', 'checkbox', 'Nenhum veículo foi marcado para ser removido', ['Notnull', 'Return_integer'], []],
            ]
            bvalidad, lmfields = abnf_find_checkbox_radio(dabnfopg, lmfields, 'btremvei')
            if bvalidad:
                lidvesel = lmfields[0][4]
                # //////////////////////////////////////
                # Busca na memória as listas de veículos
                # //////////////////////////////////////
                lidveifo = dglobaux['lidveifo']
                lidveigr = dglobaux['lidveigr']
                # ///////////////////////////////////////////
                # Insere ítens na lista de veículos sem grupo
                # ///////////////////////////////////////////
                for lauxi001 in lidveigr:
                    sprefvei = lauxi001[0]
                    splacave = lauxi001[1]
                    iidveicu = lauxi001[2]
                    if iidveicu in lidvesel:
                        lidveifo.append((sprefvei, splacave, iidveicu))
                # /////////////////////////////////////////////////////////////
                # Recria a lista de veículos do grupo sem os ítens selecionados
                # /////////////////////////////////////////////////////////////
                lidvenew = []
                for lauxi001 in lidveigr:
                    iidveicu = lauxi001[2]
                    if not iidveicu in lidvesel:
                        lidvenew.append(lauxi001)
                lidveigr = lidvenew
                # ///////////////////////////////////
                # Atualiza as listas e mostra em tela
                # ///////////////////////////////////
                abnf000u13c00703_operacional_cadastro_grupos_veiculos(sabnproj, sabntoke, lidveifo, lidveigr)
        elif dabnfopg['abnfobj0'] == ['btsalreg', 'btsalreg']:      # Salvar o registro
            lmfields = [
                ['icodogrf', 'number',   'M', 'código do grupo',      ['Notnull', 'D', 'Notzero'], None],
                ['sdescgrf', 'input',    'F', 'descrição do grupo',   ['Notnull', 'D'],            None],
            ]
            if iidogrve > 0: lmfields = lmfields + [
                ['ssitureg', 'select',   'F', 'situação do registro', ['Notnull', 'D'],            None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btsalreg')
            # Debug: (inicio)
            # abnf_show('10', lmfields, 1)
            # abnf_show('09', dabnfopg, 2)
            # abnf_show('10', dglobaux, 0)
            # Debug: (fim)
            if bvalidad:
                icodogrf = lmfields[0][5]
                sdescgrf = lmfields[1][5]
                if iidogrve > 0:
                    ssitureg = lmfields[2][5]
                lmfields = [
                    ['lpermvog', 'checkbox', '', ['Return_integer'], []],
                ]
                bvalidad, lmfields = abnf_find_checkbox_radio(dabnfopg, lmfields, 'btsalreg')
                if bvalidad:
                    lpermvog = lmfields[0][4]
                    lidveigr = dglobaux['lidveigr']
                    lgrupout = [] # Lista de veiculos vinculados a outros grupos
                    # //////////////////////////////////////////////////////////////////////////////////////////////////////////
                    # Da lista de veículos deste grupo, busca os veículos que estão em outros grupos e coloca na lista "lgrupout"
                    # //////////////////////////////////////////////////////////////////////////////////////////////////////////
                    if lpermvog != [1]:
                        for lauxi001 in lidveigr:
                            sprefvei = lauxi001[0]
                            iidveicu = lauxi001[2]
                            lcamposb = ('idogrve', None)
                            lfilbusc = (('idogrve', '!=', iidogrve), ('idveicu', '=', iidveicu), ('situreg', '!=', 'C'))
                            lorderby = None
                            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_grupos_veiculos_vinculos', lcamposb, lfilbusc, lorderby)
                            if lsqlre01 != [] or iqtdre01 != 0:
                                lgrupout.append((sprefvei, iidveicu))
                        # /////////////////////////////////////////////////////////////////////////////////////////////////////////
                        # Caso a lista lgrupout não esteja vazia então verifica se cada veículo dela também não esta no grupo atual
                        # Obs: isso para evitar do sistema ficar mandando mensagens de confirmação para todo caso que encontrar
                        # /////////////////////////////////////////////////////////////////////////////////////////////////////////
                        sauxi001 = ''
                        if lgrupout != []:
                            for lauxi001 in lgrupout:
                                sprefvei = lauxi001[0]
                                iidveicu = lauxi001[1]
                                lfilbusc = (('idogrve', '=', iidogrve), ('idveicu', '=', iidveicu), ('situreg', '!=', 'C'))
                                lorderby = None
                                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_grupos_veiculos_vinculos', lcamposb, lfilbusc, lorderby)
                                if lsqlre01 == [] or iqtdre01 == 0:
                                    if sauxi001 != '':
                                        sauxi001 = sauxi001 + ' - '
                                    sauxi001 = sauxi001 + sprefvei
                        if sauxi001 != '':
                            abnf_alert('Registro não salvo! Veículo(s) vinculado(s) a outros grupos: ' + sauxi001, 4)
                            bvalidad = False
                    # //////////////////////////
                    # Grava o registro principal
                    # //////////////////////////
                    if bvalidad:
                        if iidogrve == 0:   # Novo registro
                            bnovoreg = True
                            lcamposb = ('codogrf', 'idogrve')
                            lfilbusc = (('codogrf', '=', icodogrf), ('situreg', '!=', 'C'))
                            lorderby = None
                            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_grupos_veiculos', lcamposb, lfilbusc, lorderby)
                            if lsqlre01 != [] or iqtdre01 != 0:
                                abnf_alert('Não foi possível salvar! O código ' + str(icodogrf) + ' já está sendo utilizado em outro registro!', 4)
                            else:
                                bvalidad, iproxiid = abnf_database_insere_dados_v02(icodbase, sabnproj, 'abnf_operacional_cadastro_grupos_veiculos', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                                [
                                    ('codogrf', icodogrf),
                                    ('descgrf', sdescgrf),
                                    ('idfilia', iidfilia),
                                    ('situreg', 'A'),
                                ])
                                iidogrve = iproxiid
                        elif iidogrve > 0:  # Registro existente
                            bnovoreg = False
                            lcamposb = ('codogrf', 'idogrve')
                            lfilbusc = (('codogrf', '=', icodogrf), ('situreg', '!=', 'C'), ('idogrve', '!=', iidogrve))
                            lorderby = None
                            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_grupos_veiculos', lcamposb, lfilbusc, lorderby)
                            if lsqlre01 != [] or iqtdre01 != 0:
                                abnf_alert('Não foi possível salvar! O código ' + str(icodogrf) + ' já está sendo utilizado em outro registro!', 4)
                            else:
                                bvalidad = abnf_database_altera_dados_v02(icodbase, sabnproj, 'abnf_operacional_cadastro_grupos_veiculos', iidogrve, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                                [
                                    ('codogrf', icodogrf),
                                    ('descgrf', sdescgrf),
                                    ('situreg', ssitureg),
                                ], False)
                    # ////////////////////////////////////////////////////////////////////////
                    # Cancelando todos os registros atuais de vínculos de veículos com o grupo
                    # ////////////////////////////////////////////////////////////////////////
                    if bvalidad:
                        lcamposb = ('idogrvv', None)
                        lfilbusc = (('idogrve', '=', iidogrve), ('situreg', '!=', 'C'), None)
                        lorderby = ('idogrve', 'idveicu', 'idogrvv')
                        lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_grupos_veiculos_vinculos', lcamposb, lfilbusc, lorderby)
                        if lsqlre01 != [] or iqtdre01 != 0:
                            lidogrvv = []
                            for lauxi001 in lsqlre01:
                                lidogrvv.append(lauxi001[0])
                            for iidogrvv in lidogrvv:
                                bvalidad = abnf_database_exclui_registro(icodbase, sabnproj, 'abnf_operacional_cadastro_grupos_veiculos_vinculos', iidogrvv, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'])
                                if not bvalidad:
                                    abnf_alert('Erro ao excluir registros de vínculos de veículos! Entre em contato com o depto. de sistemas!', 4)
                                    break
                    # //////////////////////////////////////////////////////////////////////////////////
                    # Guardando os IDs de todos os registros que estão excluídos para serem reutilizados
                    # //////////////////////////////////////////////////////////////////////////////////
                    if bvalidad:
                        lidexclu = []
                        lcamposb = ('idogrvv', None)
                        lfilbusc = (('situreg', '=', 'C'), None)
                        lorderby = None
                        lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_grupos_veiculos_vinculos', lcamposb, lfilbusc, lorderby)
                        if lsqlre01 != [] or iqtdre01 != 0:
                            for lauxi001 in lsqlre01:
                                lidexclu.append(lauxi001[0])
                    # /////////////////////////////////////////////////////////////////////////////////////////////
                    # Inserindo veículos em registros excluídos ou criando novos registros para inserir os veículos
                    # /////////////////////////////////////////////////////////////////////////////////////////////
                    if bvalidad:
                        for lauxi001 in lidveigr:
                            iidveicu = lauxi001[2]
                            # //////////////////////////////////////////////////
                            # Insere os dados em um registro de vínculo excluído
                            # //////////////////////////////////////////////////
                            if lidexclu != []:
                                iidogrvv = lidexclu[0]
                                del lidexclu[0]
                                bvalidad = abnf_database_altera_dados_v02(icodbase, sabnproj, 'abnf_operacional_cadastro_grupos_veiculos_vinculos', iidogrvv, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                                [
                                    ('idogrve', iidogrve),
                                    ('idveicu', iidveicu),
                                    ('situreg', 'A'),
                                ])
                                if not bvalidad:
                                    break
                            # ///////////////////////////////
                            # Cria um registro novo de viagem
                            # ///////////////////////////////
                            else:
                                bvalidad, iproxiid = abnf_database_insere_dados_v02(icodbase, sabnproj, 'abnf_operacional_cadastro_grupos_veiculos_vinculos', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                                [
                                    ('idogrve', iidogrve),
                                    ('idveicu', iidveicu),
                                    ('situreg', 'A'),
                                ])
                                if not bvalidad:
                                    break
                        if not bvalidad:
                            abnf_alert('Erro ao criar novos registros de vínculos de veículos! Entre em contato com o depto. de sistemas!', 4)
                        else:
                            if bnovoreg: sauxi001 = 'Novo grupo gravado com sucesso!'
                            else:        sauxi001 = 'Registro alterado com sucesso!'
                            abnf_alert(sauxi001, 3)
                            abnf000u13c00700_operacional_cadastro_grupos_veiculos(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btexcreg', 'btexcreg']:      # Excluir registro
            iidogrve = dglobaux['iidogrve']        
            icodbase = int(dabnfopg['abnproje'][2][14:]) * 100      # Código do banco de dados a ser utilizado
            # /////////////////////////////////
            # Exclui os registros de vinculação
            # /////////////////////////////////
            lcamposb = ('idogrvv', None)
            lfilbusc = (('idogrve', '=', iidogrve), None)
            lorderby = None
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_grupos_veiculos_vinculos', lcamposb, lfilbusc, lorderby)
            for lauxi001 in lsqlre01:
                iidogrvv = lauxi001[0]
                bvalidad = abnf_database_exclui_registro(icodbase, sabnproj, 'abnf_operacional_cadastro_grupos_veiculos_vinculos', iidogrvv, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'])
                if not bvalidad:
                    abnf_alert('Erro ao excluir registros de vínculos de veículos! Entre em contato com o depto. de sistemas!', 4)
                    break
            # ///////////////////////////
            # Exclui o registro principal
            # ///////////////////////////
            if bvalidad:
                bvalidad = abnf_database_exclui_registro(icodbase, sabnproj, 'abnf_operacional_cadastro_grupos_veiculos', iidogrve, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'])
                if bvalidad:
                    abnf_alert('Registro excluído com sucesso!', 3)
                    abnf000u13c00700_operacional_cadastro_grupos_veiculos(dabnfopg)
        elif dabnfopg['abnfobj0'] in (['btfilvfo', 'btfilvfo'], ['btfilvgr', 'btfilvgr']):
            # //////////////////////////////////////
            # Busca na memória as listas de veículos
            # //////////////////////////////////////
            lidveifo = dglobaux['lidveifo']
            lidveigr = dglobaux['lidveigr']
            if   dabnfopg['abnfobj0'] == ['btfilvfo', 'btfilvfo']: lauxi001 = ('sfilvfor', 'filtro de veículos fora do grupo', 'btfilvfo', 'F')
            elif dabnfopg['abnfobj0'] == ['btfilvgr', 'btfilvgr']: lauxi001 = ('sfilvgru', 'filtro de veículos do grupo',      'btfilvgr', 'G')
            lmfields = [
                [lauxi001[0], 'input', 'M', lauxi001[1], [], None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, lauxi001[2])
            if bvalidad:
                sfilvxxx = lmfields[0][5]
                abnf000u13c00704_operacional_cadastro_grupos_veiculos(sfilvxxx, lauxi001[3], lidveifo, lidveigr)
                abnf_socket_004([5, lauxi001[2]])

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00703_operacional_cadastro_grupos_veiculos ] //////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Grupos de Veículos.                                                                                                       // #
# // Reorganiza a lista de veículos do grupo que esta em memória, atualiza e posta a DIV.                                                                // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00703_operacional_cadastro_grupos_veiculos(sabnproj, sabntoke, lidveifo, lidveigr):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00703_operacional_cadastro_grupos_veiculos(...)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    # ////////////////
    # Indexa as listas
    # ////////////////
    lidveifo.sort()
    lidveigr.sort()
    # ///////////////
    # Início das DIVs
    # ///////////////
    ldivvfor = [
        ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
        ('table-2', 'table table-bordered table-sm table-responsive border-secondary', 1, 530, 300, None, None),
    ]
    ldivvgru = [
        ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
        ('table-2', 'table table-bordered table-sm table-responsive border-secondary', 1, 530, 300, None, None),
    ]
    # ///////////////////////////////////
    # Inserindo os veículos fora do grupo
    # ///////////////////////////////////
    if lidveifo != []:
        for lauxi001 in lidveifo:
            sprefvei = lauxi001[0]
            splacave = lauxi001[1]
            iidveicu = lauxi001[2]
            lauxi002 = ('checkbox-0', 'iidveisg[' + str(iidveicu) + ']', iidveicu, None, 'Courier New', '12px', 'b', 'P', None)
            ldivvfor = ldivvfor + [
                ('tr-0', None, True),
                    ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '15px', None, sprefvei), ('td-9', None),
                    ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '15px', None, splacave), ('td-9', None),
                    ('td-0', None, 1, None, 1, None, None), lauxi002, ('td-9', None),
                ('tr-9', None)
            ]
    # //////////////////////////////
    # Inserindo os veículos do grupo
    # //////////////////////////////
    if lidveigr != []:
        for lauxi001 in lidveigr:
            sprefvei = lauxi001[0]
            splacave = lauxi001[1]
            iidveicu = lauxi001[2]
            lauxi002 = ('checkbox-0', 'iidveigr[' + str(iidveicu) + ']', iidveicu, None, 'Courier New', '12px', 'b', 'P', None)
            ldivvgru = ldivvgru + [
                ('tr-0', None, True),
                    ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '15px', None, sprefvei), ('td-9', None),
                    ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '15px', None, splacave), ('td-9', None),
                    ('td-0', None, 1, None, 1, None, None), lauxi002, ('td-9', None),
                ('tr-9', None)
            ]
    # ////////////
    # Fim das DIVs
    # ////////////
    ldivvfor = ldivvfor + [
        ('table-9', None),
        ('div-9', None),    # <== Esse 'div-9' é uma necessidade pelo uso de 'table-2'.
        ('form-9', None),
    ]
    ldivvgru = ldivvgru + [
        ('table-9', None),
        ('div-9', None),    # <== Esse 'div-9' é uma necessidade pelo uso de 'table-2'.
        ('form-9', None),
    ]
    # /////////////////////////////////////////
    # Armazena em memória as listas de veículos
    # /////////////////////////////////////////
    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('lidveifo', lidveifo),)]) # ==> Guardado lista de veículos fora do grupo. Obs: tem que ter essa vírgula: "),)])"
    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('lidveigr', lidveigr),)]) # ==> Guardado lista de veículos do grupo. Obs: tem que ter essa vírgula: "),)])"
    # //////////////
    # Atualiza a DIV
    # //////////////
    sdivvfor = abnf_create_page(ldivvfor)
    sdivvgru = abnf_create_page(ldivvgru)
    abnf_socket_004([1, 'sdivvfor', sdivvfor])
    abnf_socket_004([1, 'sdivvgru', sdivvgru])

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00704_operacional_cadastro_grupos_veiculos ] //////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Grupos de Veículos.                                                                                                       // #
# // Filtra as listas de veículos que estão em memória, atualiza suas respectivas DVIs e posta as DIVs.                                                  // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00704_operacional_cadastro_grupos_veiculos(sfilvxxx, stipogru, lidveifo, lidveigr):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00704_operacional_cadastro_grupos_veiculos(...)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    if   stipogru == 'F': lauxivei = (lidveifo, 'iidveisg', 'sdivvfor')
    elif stipogru == 'G': lauxivei = (lidveigr, 'iidveigr', 'sdivvgru')
    ldivvxxx = [
        ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
        ('table-2', 'table table-bordered table-sm table-responsive border-secondary', 1, 530, 300, None, None),
    ]
    if lauxivei[0] != []:
        for lauxi001 in lauxivei[0]:
            sprefvei = lauxi001[0]
            splacave = lauxi001[1]
            iidveicu = lauxi001[2]
            bvalidad = False
            if sfilvxxx == '': bvalidad = True
            else:
                if   sfilvxxx in sprefvei: bvalidad = True
                elif sfilvxxx in splacave: bvalidad = True
            if bvalidad:
                lauxi002 = ('checkbox-0', lauxivei[1] + '[' + str(iidveicu) + ']', iidveicu, None, 'Courier New', '12px', 'b', 'P', None)
                ldivvxxx = ldivvxxx + [
                    ('tr-0', None, True),
                        ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '15px', None, sprefvei), ('td-9', None),
                        ('td-0', None, 1, None, 1, None, None), ('font-0', 'Courier New;', '15px', None, splacave), ('td-9', None),
                        ('td-0', None, 1, None, 1, None, None), lauxi002, ('td-9', None),
                    ('tr-9', None)
                ]
    ldivvxxx = ldivvxxx + [
        ('table-9', None),
        ('div-9', None),    # <== Esse 'div-9' é uma necessidade pelo uso de 'table-2'.
        ('form-9', None),
    ]
    # //////////////
    # Atualiza a DIV
    # //////////////
    sdivvxxx = abnf_create_page(ldivvxxx)
    abnf_socket_004([1, lauxivei[2], sdivvxxx])

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00705_operacional_cadastro_grupos_veiculos ] //////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Grupos de Veículos.                                                                                                       // #
# // Relação de grupos com seus respetivos veículos.                                                                                                     // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00705_operacional_cadastro_grupos_veiculos(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00705_operacional_cadastro_grupos_veiculos(...)')
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
        lidveicu = abnf_database_menu(icodbase, iidfilia, 'L', '0203', 0, 1, None)
        # /////////////////////
        # Variaveis de ambiente
        # /////////////////////
        ifontlen = 2
        icolspan = 2
        icontreg = 0
        sarqurel = abnf_imprime_file(0, sabntoke)
        with open('abnftmp/' + sarqurel, 'w') as sarquwri:
            snomeemp, snomefil = abnf_database_retorna_empresa_filial(icodbase, iidfilia)
            abnf_imprime_doctype_head_fhead_body_form_table_thead(sarquwri, 3)
            abnf_imprime_thead_001_abeinfo_sistemas(sarquwri, icolspan)
            abnf_imprime_thead_002_titulo_relatorio(sarquwri, icolspan, 'GRUPOS COM SEUS RESPETIVOS VEÍCULOS')
            abnf_imprime_thead_003_empresa_filial(sarquwri, icolspan, snomeemp, snomefil)
            # smensage = 'Per&iacute;odo: ' + abnf_converte_data(ddataini) + ' &agrave;s ' + abnf_converte_hora(thoraini) + ' at&eacute; ' + abnf_converte_data(ddatafim) + ' &agrave;s ' + abnf_converte_hora(thorafim)
            # abnf_imprime_thead_004_parametros(sarquwri, icolspan, smensage)
            abnf_imprime_thead_005_datetime(sarquwri, icolspan)
            abnf_imprime_line(sarquwri, icolspan, 'darkcyan')
            # //////////////////////////////
            # Buscando os grupos de veículos
            # //////////////////////////////
            lcamposb = ('idogrve', 'codogrf', 'descgrf')
            lfilbusc = (('idfilia', '=', iidfilia), ('situreg', '!=', 'C'))
            lorderby = ('descgrf', 'codogrf', 'idogrve')
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_grupos_veiculos', lcamposb, lfilbusc, lorderby)
            for lauxi001 in lsqlre01:
                icontreg += 1
                iidogrve = lauxi001[0]
                sauxi001 = lauxi001[2] + ' (' + str(lauxi001[1]) + ')'
                abnf_imprime_info_001(sarquwri, None, None, 1,
                    [
                        ('Grupo:',            1, 0, '#CEF1F5', 'left', 'black', 'Courier New', ifontlen + 2, True, False),
                        (sauxi001, icolspan - 1, 0, None,      'left', 'blue',  'Courier New', ifontlen + 2, True, False),
                    ]
                )
                # ////////////////////////////////////////
                # Buscando os veiculos vinculados ao grupo
                # ////////////////////////////////////////
                sauxi001 = ''
                lcamposb = ('idveicu', None)
                lfilbusc = (('idogrve', '=', iidogrve), ('situreg', '!=', 'C'))
                lorderby = None
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_grupos_veiculos_vinculos', lcamposb, lfilbusc, lorderby)
                if lsqlre01 != [] or iqtdre01 != 0:
                    for lauxi001 in lidveicu:
                        iidveicu = lauxi001[0]
                        sprefvei = lauxi001[1][0]
                        for lauxi002 in lsqlre01:
                            if lauxi002[0] == iidveicu:
                                if sauxi001 != '': sauxi001 = sauxi001 + ' - '
                                sauxi001 = sauxi001 + sprefvei
                abnf_imprime_info_001(sarquwri, None, None, 1,
                    [
                        ('Veículos vinculados:', 1, 0, '#CEF1F5', 'left', 'black', 'Courier New', ifontlen, True, False),
                        (sauxi001,    icolspan - 1, 0, None,      'left', 'black', 'Courier New', ifontlen, True, False),
                    ]
                )
                abnf_imprime_line(sarquwri, icolspan, 'brown')
            abnf_imprime_info_001(sarquwri, None, None, 1,
                [
                    ('Quantidade de grupos de veículos:',         icolspan - 1, 0, None, 'left',  'black', 'Courier New', ifontlen, True, False),
                    (abnf_formata_numero_milhar_decimal(icontreg, True, 0),  1, 0, None, 'right', 'black', 'Courier New', ifontlen, True, False),
                ]
            )
            # ////////////////
            # Fim do relatório
            # ////////////////
            abnf_imprime_ftbody_ftable_fform_fbody(sarquwri)
        abnf_socket_004([7, sarqurel])
        abnf_socket_004([5, 'btrelgrv'])
        abnf_alert('Relatório gerado com sucesso!', 3)
        time.sleep(5)
        abnf_alert('', 0)
        
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u13c00706_operacional_cadastro_grupos_veiculos ] //////////////////////////////////////////////////////////////////////////////////////////// #
# // Operacional - Cadastro de Grupos de Veículos.                                                                                                       // #
# // Relação de veículos com seus respetivos grupos.                                                                                                     // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u13c00706_operacional_cadastro_grupos_veiculos(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u13c00706_operacional_cadastro_grupos_veiculos(...)')
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
        lidveicu = abnf_database_menu(icodbase, iidfilia, 'L', '0203', 0, 1, None)
        lidogrve = abnf_database_menu(icodbase, iidfilia, 'L', '1321A', 0, 1, 2)
        # ////////////////////////////////////////////////
        # Criando lista de vinculos de veículos com grupos
        # ////////////////////////////////////////////////
        lidogrvv = []
        lcamposb = ('idveicu', 'idogrve')
        lfilbusc = (('situreg', '!=', 'C'), None)
        lorderby = ('idogrve', 'idveicu', 'idogrvv')
        lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_operacional_cadastro_grupos_veiculos_vinculos', lcamposb, lfilbusc, lorderby)
        if lsqlre01 != [] or iqtdre01 != 0:
            for lauxi001 in lsqlre01:
                lidogrvv.append((lauxi001[0], lauxi001[1]))
        # Debug: (inicio)
        # abnf_show('08', lidveicu, 1)
        # abnf_show('09', lidogrve, 1)
        # abnf_show('10', lidogrvv, 1)
        # Debug: (fim)
        # /////////////////////
        # Variaveis de ambiente
        # /////////////////////
        ifontlen = 2
        icolspan = 2
        icontreg = 0
        sarqurel = abnf_imprime_file(0, sabntoke)
        with open('abnftmp/' + sarqurel, 'w') as sarquwri:
            snomeemp, snomefil = abnf_database_retorna_empresa_filial(icodbase, iidfilia)
            abnf_imprime_doctype_head_fhead_body_form_table_thead(sarquwri, 3)
            abnf_imprime_thead_001_abeinfo_sistemas(sarquwri, icolspan)
            abnf_imprime_thead_002_titulo_relatorio(sarquwri, icolspan, 'VEÍCULOS COM SEUS RESPETIVOS GRUPOS')
            abnf_imprime_thead_003_empresa_filial(sarquwri, icolspan, snomeemp, snomefil)
            # smensage = 'Per&iacute;odo: ' + abnf_converte_data(ddataini) + ' &agrave;s ' + abnf_converte_hora(thoraini) + ' at&eacute; ' + abnf_converte_data(ddatafim) + ' &agrave;s ' + abnf_converte_hora(thorafim)
            # abnf_imprime_thead_004_parametros(sarquwri, icolspan, smensage)
            abnf_imprime_thead_005_datetime(sarquwri, icolspan)
            abnf_imprime_line(sarquwri, icolspan, 'darkcyan')
            # ////////////////////
            # Listando os veículos
            # ////////////////////
            for lauxi001 in lidveicu:
                icontreg += 1
                abnf_imprime_info_001(sarquwri, None, None, 1,
                    [
                        ('Veículo:',                1, 0, '#CEF1F5', 'left', 'black', 'Courier New', ifontlen + 2, True, False),
                        (lauxi001[1][0], icolspan - 1, 0, None,      'left', 'blue',  'Courier New', ifontlen + 2, True, False),
                    ]
                )
                sauxi001 = ''
                for lauxi002 in lidogrve:
                    if (lauxi001[0], lauxi002[0]) in lidogrvv:
                        if sauxi001 != '':
                            sauxi001 = sauxi001 + '<br>'
                        sauxi001 = sauxi001 + lauxi002[1]
                abnf_imprime_info_001(sarquwri, None, None, 1,
                    [
                        ('Grupos vinculados:', 1, 0, '#CEF1F5', 'left', 'black', 'Courier New', ifontlen, True, False),
                        (sauxi001,  icolspan - 1, 0, None,      'left', 'black', 'Courier New', ifontlen, True, False),
                    ]
                )
                abnf_imprime_line(sarquwri, icolspan, 'brown')
            abnf_imprime_info_001(sarquwri, None, None, 1,
                [
                    ('Quantidade de veículos:',                   icolspan - 1, 0, None, 'left',  'black', 'Courier New', ifontlen, True, False),
                    (abnf_formata_numero_milhar_decimal(icontreg, True, 0),  1, 0, None, 'right', 'black', 'Courier New', ifontlen, True, False),
                ]
            )
            # ////////////////
            # Fim do relatório
            # ////////////////
            abnf_imprime_ftbody_ftable_fform_fbody(sarquwri)
        abnf_socket_004([7, sarqurel])
        abnf_socket_004([5, 'btrelveg'])
        abnf_alert('Relatório gerado com sucesso!', 3)
        time.sleep(5)
        abnf_alert('', 0)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #