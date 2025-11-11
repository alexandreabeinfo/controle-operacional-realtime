## ================================================
## [abnf000u03c00200.py] - Cadastro de Funcionários
## ================================================

from abnfsrc.abnf000u00s00003 import *              # Arquivo de funções comuns que serão utilizadas por todos os módulos do sistema
from abnfsrc.abnf000u00s00004 import *              # Arquivo de banco de dados

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u03c00200_cadastro_funcionarios ] /////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de Funcionários.                                                                                                                           // #
# // Form inicial.                                                                                                                                       // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u03c00200_cadastro_funcionarios(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u03c00200_cadastro_funcionarios(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, '03C00201A'])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        iidfilia = dglobaux['iidfilia']
        lidfunci = abnf_database_sqlx(icodbase, 'L', '03002A', 1, (0, iidfilia))
        lnewpage = [                                                                         
            ('div-0', 'container', None, None),
            ('hr-0', None),
            ('div-0', 'row', None, None),
            ('div-0', 'col d-flex justify-content-center', None, None),
            ('div-0', 'w-50 p-3', 'background-color: #eee;', None),
            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
            ('legend-0', 'Cadastro de Funcionários'),
            ('hr-0', None),
            ('label-0',  'Funcionário', 'form-control-label'),
            ('select-0', 'iidfunci', 'form-control', '16px', 'btbusreg', lidfunci, 1, None, False),
            ('hr-0', None),
            ('button-0', 'btbusreg', 'btn btn-primary mt-2', 'Buscar'),
            ('alt255-0', 2),
            ('button-0', 'btnovreg', 'btn btn-primary mt-2', 'Novo registro'),
            ('alt255-0', 2),
            ('button-0', 'btrelcad', 'btn btn-primary mt-2', 'Relação de funcionários cadastrados'),
            ('form-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
        ]
        snewpage = abnf_create_page(lnewpage)
        abnf_socket_004([1, 'abnfdv03', snewpage])
        
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u03c00201_cadastro_funcionarios ] /////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de Funcionários.                                                                                                                           // #
# // Form de cadastro/alteração do funcionário.                                                                                                          // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u03c00201_cadastro_funcionarios(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u03c00201_cadastro_funcionarios(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        if dabnfopg['abnfobj0'] == ['btbusreg', 'btbusreg']:        # Buscar registro existente
            lmfields = [
                ['iidfunci', 'input', 'M', 'funcionário', ['Notnull', 'D', 'Return_integer'], None],
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
                iidfunci = lmfields[0][5]
                # //////////////////////////////////////////////////////
                # Buscando o funcionário caso seja um registro existente
                # //////////////////////////////////////////////////////
                lcamposb = ('codfunc', 'idcpfpj', 'idcargo', 'dataadm', 'dataafa', 'datades', 'dataitr', 'dataftr', 'motelev', 'observa', 'situreg')
                lfilbusc = (('idfunci', '=', iidfunci), ('idfilia', '=', iidfilia), ('situreg', '!=', 'C'))
                lorderby = None
                lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_funcionarios', lcamposb, lfilbusc, lorderby)
                if lsqlre01 == [] or iqtdre01 == 0:
                    abnf_alert('O funcionário não foi encontrado!', 4)
                else:
                    # Debug: (inicio)
                    # abnf_show('10', lsqlre01, 1)
                    # Debug: (fim)
                    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidfunci', iidfunci),)])      # ==> Guardando o ID do registro. Obs: tem que ter essa vírgula: "),)])"
                    abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '03C00202A'),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
                    lidcpfpj = abnf_database_menu(icodbase, None, 'L', '0104', 1, 1, 2)
                    lidcargo = abnf_database_sqlx(icodbase, 'L', '03001A', 1, (0, None))
                    lnewpage = [
                        ('div-0', 'container', None, None),
                        ('hr-0', None),
                        ('div-0', 'row', None, None),
                        ('div-0', 'col d-flex justify-content-center', None, None),
                        ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                        ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                        ('legend-0', 'Cadastro de Funcionários - [ Registro existente ]'),
                        ('hr-0', None),
                        ('label-0',  'Código do funcionário', 'form-control-label'),
                        ('number-0', 'icodfunc', 'form-control', 0, 10, '16px', lsqlre01[0][0], 'iidcpfpj', True, None),
                        ('label-0',  'CPF do funcionário', 'form-control-label'),
                        ('select-0', 'iidcpfpj', 'form-control', '16px', 'iidcargo', lidcpfpj, 1, lsqlre01[0][1], False),
                        ('label-0',  'Cargo de funcionário', 'form-control-label'),
                        ('select-0', 'iidcargo', 'form-control', '16px', 'ddataadm', lidcargo, 1, lsqlre01[0][2], False),
                        ('label-0',  'Data de admissão', 'form-control-label'),
                        ('date-0',   'ddataadm', 'form-control', '16px', lsqlre01[0][3], 'ddataafa', True, 0, None),
                        ('label-0',  'Data de afastamento', 'form-control-label'),
                        ('date-0',   'ddataafa', 'form-control', '16px', lsqlre01[0][4], 'ddatades', True, 0, None),
                        ('label-0',  'Data de desligamento', 'form-control-label'),
                        ('date-0',   'ddatades', 'form-control', '16px', lsqlre01[0][5], 'ddataitr', True, 0, None),
                        ('label-0',  'Data de início de treinamento', 'form-control-label'),
                        ('date-0',   'ddataitr', 'form-control', '16px', lsqlre01[0][6], 'ddataftr', True, 0, None),
                        ('label-0',  'Data de fim de treinamento', 'form-control-label'),
                        ('date-0',   'ddataftr', 'form-control', '16px', lsqlre01[0][7], 'sobserva', True, 0, None),
                        ('hr-0', None),
                        ('checkbox-0', 'bmotelev', 1, (1 if lsqlre01[0][8] else 0), 'Courier New', '14px', 'b', 'P', 'Motorista do Elevar'),
                        ('hr-0', None),
                        ('label-0',  'Observação (Opcional) (1000 caracteres)', 'form-control-label'),
                        ('textarea-0', 'sobserva', 'form-control', 2, 1000, '16px', lsqlre01[0][9], 'ssitureg'),
                        ('hr-0', None),
                        ('label-0',  'Situação do registro', 'form-control-label'),
                        ('select-0', 'ssitureg', 'form-control', '16px', 'btmodsav', abnf_personal_retorna_lista(10001), 0, lsqlre01[0][10], False),
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
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidfunci', 0),)])             # ==> Indicativo para dizer que é novo registro. Obs: tem que ter essa vírgula: "),)])"
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '03C00202A'),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
            icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
            lidcpfpj = abnf_database_menu(icodbase, None, 'L', '0104', 1, 1, 2)
            lidcargo = abnf_database_sqlx(icodbase, 'L', '03001A', 1, (0, None))
            lnewpage = [
                ('div-0', 'container', None, None),
                ('hr-0', None),
                ('div-0', 'row', None, None),
                ('div-0', 'col d-flex justify-content-center', None, None),
                ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                ('legend-0', 'Cadastro de Funcionários - [ Novo registro ]'),
                ('hr-0', None),
                ('label-0',  'Código do funcionário', 'form-control-label'),
                ('number-0', 'icodfunc', 'form-control', 0, 10, '16px', None, 'iidcpfpj', True, None),
                ('label-0',  'CPF do funcionário', 'form-control-label'),
                ('select-0', 'iidcpfpj', 'form-control', '16px', 'iidcargo', lidcpfpj, 1, None, False),
                ('label-0',  'Cargo de funcionário', 'form-control-label'),
                ('select-0', 'iidcargo', 'form-control', '16px', 'ddataadm', lidcargo, 1, None, False),
                ('label-0',  'Data de admissão', 'form-control-label'),
                ('date-0',   'ddataadm', 'form-control', '16px', None, 'ddataafa', True, 0, None),
                ('label-0',  'Data de afastamento', 'form-control-label'),
                ('date-0',   'ddataafa', 'form-control', '16px', None, 'ddatades', True, 0, None),
                ('label-0',  'Data de desligamento', 'form-control-label'),
                ('date-0',   'ddatades', 'form-control', '16px', None, 'ddataitr', True, 0, None),
                ('label-0',  'Data de início de treinamento', 'form-control-label'),
                ('date-0',   'ddataitr', 'form-control', '16px', None, 'ddataftr', True, 0, None),
                ('label-0',  'Data de fim de treinamento', 'form-control-label'),
                ('date-0',   'ddataftr', 'form-control', '16px', None, 'sobserva', True, 0, None),
                ('hr-0', None),
                ('checkbox-0', 'bmotelev', 1, 0, 'Courier New', '14px', 'b', 'P', 'Motorista do Elevar'),
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
        elif dabnfopg['abnfobj0'] == ['btrelcad', 'btrelcad']:      # Relação de funcionários cadastrados
            abnf000u03c00203_cadastro_funcionarios(dabnfopg)
            
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u03c00202_cadastro_funcionarios ] /////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de Funcionários.                                                                                                                           // #
# // Gravação dos registros e geração de log.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u03c00202_cadastro_funcionarios(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u03c00202_cadastro_funcionarios(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        if dabnfopg['abnfobj0'] == ['btcancel', 'btcancel']:        # Voltar para tela anterior
            abnf000u03c00200_cadastro_funcionarios(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btsalreg', 'btsalreg']:      # Salvar o registro
            iidfunci = dglobaux['iidfunci']
            lmfields = [
                ['icodfunc', 'number',   'M', 'código do funcionário',         ['Notnull', 'D', 'Return_integer'], None],
                ['iidcpfpj', 'select',   'M', 'CPF do funcionário',            ['Notnull', 'D', 'Return_integer'], None],
                ['iidcargo', 'select',   'M', 'cargo do funcionário',          ['Notnull', 'D', 'Return_integer'], None],
                ['ddataadm', 'date',     'F', 'data de admissão',              ['Notnull', 'D', 'Return_date'],    None],
                ['ddataafa', 'date',     'F', 'data de afastamento',           ['Return_date'],                    None],
                ['ddatades', 'date',     'F', 'data de desligamento',          ['Return_date'],                    None],
                ['ddataitr', 'date',     'F', 'data de início de treinamento', ['Return_date'],                    None],
                ['ddataftr', 'date',     'F', 'data de fim de treinamento',    ['Return_date'],                    None],
                ['bmotelev', 'checkbox', 'M', 'motorista do Elevar',           [],                                 None],
                ['sobserva', 'textarea', 'F', 'observação',                    [],                                 None],
            ]
            if iidfunci > 0: lmfields = lmfields + [
                ['ssitureg', 'select',   'F', 'situação do registro',          ['Notnull', 'D'],                   None],
            ]            
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btsalreg')
            if bvalidad:
                icodfunc = lmfields[0][5]
                iidcpfpj = lmfields[1][5]
                iidcargo = lmfields[2][5]
                ddataadm = lmfields[3][5]
                ddataafa = lmfields[4][5]
                ddatades = lmfields[5][5]
                ddataitr = lmfields[6][5]
                ddataftr = lmfields[7][5]
                bmotelev = lmfields[8][5]
                sobserva = lmfields[9][5]
                if iidfunci > 0:
                    ssitureg = lmfields[10][5]
                lmrulesx = [
                    ['e2>=e1', ddataadm, 'F', 'data de admissão', ddataafa, 'F', 'data de afastamento'],
                    ['e2>=e1', ddataadm, 'F', 'data de admissão', ddatades, 'F', 'data de desligamento'],
                    ['e2>=e1', ddataadm, 'F', 'data de admissão', ddataitr, 'F', 'data de início de treinamento'],
                    ['e2>=e1', ddataadm, 'F', 'data de admissão', ddataftr, 'F', 'data de fim de treinamento'],
                    ['e2>=e1', ddataitr, 'F', 'data de início de treinamento', ddataftr, 'F', 'data de fim de treinamento'],
                ]
                bvalidad =  abnf_check_rules_fields(lmrulesx, 'btsalreg')
                if bvalidad:
                    icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
                    iidfilia = dglobaux['iidfilia']
                    if   abnf_database_registro_nao_ativo(icodbase, 'abnf_cadastro_cpfcnpj',             iidcpfpj, 'M', 'CPF',                  ('nomraso', 'codpfpj')):  pass
                    elif abnf_database_registro_nao_ativo(icodbase, 'abnf_cadastro_funcionarios_cargos', iidcargo, 'M', 'cargo de funcionário', ('descarg', 'codcarg')):  pass                    
                    elif iidfunci == 0:   # Novo registro
                        lcamposb = ('codfunc', None)
                        lfilbusc = (('codfunc', '=', icodfunc), ('idfilia', '=', iidfilia), ('situreg', '!=', 'C'))
                        lorderby = None
                        lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_funcionarios', lcamposb, lfilbusc, lorderby)
                        if lsqlre01 != [] or iqtdre01 != 0:
                            abnf_alert('Não foi possível salvar! O código ' + str(icodfunc) + ' já está sendo utilizado em outro registro!', 4)
                        else:
                            bvalidad, iproxiid = abnf_database_insere_dados_v02(icodbase, sabnproj, 'abnf_cadastro_funcionarios', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                            [
                                ('codfunc', icodfunc),
                                ('idcpfpj', iidcpfpj),
                                ('idcargo', iidcargo),
                                ('dataadm', ddataadm),
                                ('dataafa', ddataafa),
                                ('datades', ddatades),
                                ('dataitr', ddataitr),
                                ('dataftr', ddataftr),
                                ('motelev', bmotelev),
                                ('observa', sobserva),
                                ('idfilia', iidfilia),
                                ('situreg', 'A'),
                            ])
                            if bvalidad:
                                abnf_alert('Novo funcionário gravado com sucesso!', 3)
                                abnf000u03c00200_cadastro_funcionarios(dabnfopg)
                    elif iidfunci > 0:  # Registro existente
                        lcamposb = ('codfunc', None)
                        lfilbusc = (('codfunc', '=', icodfunc), ('idfilia', '=', iidfilia), ('situreg', '!=', 'C'), ('idfunci', '!=', iidfunci))
                        lorderby = None
                        lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_funcionarios', lcamposb, lfilbusc, lorderby)
                        if lsqlre01 != [] or iqtdre01 != 0:
                            abnf_alert('Não foi possível salvar! O código ' + str(icodfunc) + ' já está sendo utilizado em outro registro!', 4)
                        else:
                            bvalidad = abnf_database_altera_dados_v02(icodbase, sabnproj, 'abnf_cadastro_funcionarios', iidfunci, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                            [
                                ('codfunc', icodfunc),
                                ('idcpfpj', iidcpfpj),
                                ('idcargo', iidcargo),
                                ('dataadm', ddataadm),
                                ('dataafa', ddataafa),
                                ('datades', ddatades),
                                ('dataitr', ddataitr),
                                ('dataftr', ddataftr),
                                ('motelev', bmotelev),
                                ('observa', sobserva),
                                ('idfilia', iidfilia),
                                ('situreg', ssitureg),
                            ])
                            if bvalidad:
                                abnf_alert('Registro alterado com sucesso!', 3)
                                abnf000u03c00200_cadastro_funcionarios(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btexcreg', 'btexcreg']:      # Excluir registro
            iidfunci = dglobaux['iidfunci']        
            icodbase = int(dabnfopg['abnproje'][2][14:]) * 100      # Código do banco de dados a ser utilizado
            bvalidad = abnf_database_exclui_registro(icodbase, sabnproj, 'abnf_cadastro_funcionarios', iidfunci, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'])
            if bvalidad:
                abnf_alert('Registro excluído com sucesso!', 3)
                abnf000u03c00200_cadastro_funcionarios(dabnfopg)
                
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u03c00203_cadastro_funcionarios ] /////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de Funcionários.                                                                                                                           // #
# // Relatório de funcionários.                                                                                                                          // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
                
def abnf000u03c00203_cadastro_funcionarios(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u03c00203_cadastro_funcionarios(dabnfopg)')
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
            abnf_imprime_thead_002_titulo_relatorio(sarquwri, icolspan, 'RELAÇÃO DE FUNCIONÁRIOS')
            abnf_imprime_thead_003_empresa_filial(sarquwri, icolspan, snomeemp, snomefil)
            abnf_imprime_thead_005_datetime(sarquwri, icolspan)
            abnf_imprime_line(sarquwri, icolspan, 'darkcyan')
            abnf_imprime_info_001(sarquwri, '#D1C5C5', 'center', 1,
                [
                    ('Funcionário',  1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Código',       1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('CPF',          1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Cargo',        1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Admissão',     1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Desligamento', 1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Situação',     1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                ]
            )
            abnf_imprime_fthead_tbody(sarquwri)
            lsqlre01 = abnf_database_sqlx(icodbase, 'X', '03002B', 1, (0, iidfilia))
            for lauxi001 in lsqlre01:
                sauxi001 = lauxi001[3] + ' (' + str(lauxi001[4]) + ')'
                sdataadm = abnf_converte_data(lauxi001[5])
                sdatades = abnf_converte_data(lauxi001[6])
                ssitureg = abnf_personal_retorna_string(10001, lauxi001[7])
                icontreg += 1
                abnf_imprime_info_001(sarquwri, None, None, 1,
                    [
                        (lauxi001[0], 1, 0, None, 'Left',   'black', 'Courier New', ifontlen, True, False),
                        (lauxi001[1], 1, 0, None, 'Center', 'black', 'Courier New', ifontlen, True, False),
                        (lauxi001[3], 1, 0, None, 'Center', 'black', 'Courier New', ifontlen, True, False),
                        (sauxi001,    1, 0, None, 'left',   'black', 'Courier New', ifontlen, True, False),
                        (sdataadm,    1, 0, None, 'Center', 'black', 'Courier New', ifontlen, True, False),
                        (sdatades,    1, 0, None, 'Center', 'black', 'Courier New', ifontlen, True, False),
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