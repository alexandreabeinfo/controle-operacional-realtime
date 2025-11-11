## ========================================
## [abnf000u01c00500.py] - Cadastro de CNPJ
## ========================================

from abnfsrc.abnf000u00s00003 import *              # Arquivo de funções comuns que serão utilizadas por todos os módulos do sistema
from abnfsrc.abnf000u00s00004 import *              # Arquivo de banco de dados

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u01c00500_cadastro_cnpj ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de CNPJ.                                                                                                                                   // #
# // Form inicial.                                                                                                                                       // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u01c00500_cadastro_cnpj(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u01c00500_cadastro_cnpj(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        abnf_socket_004([1, 'abnfdv03', abnf_create_spinner(1, 100)])
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, '01C00501A'])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        lidcpfpj = abnf_database_menu(icodbase, None, 'L', '0105', 1, 1, 2)
        # Debug: (inicio)
        # abnf_show('08', iidcpfpj, 1)
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
            ('legend-0', 'Cadastro de CNPJ'),
            ('hr-0', None),
            ('label-0',  'CNPJ', 'form-control-label'),
            ('cnpj-0',   'scodpfpj', 'form-control', 0, 18, '16px', None, 'btbusreg', True, 0),
            ('label-0',  'Lista de CNPJ', 'form-control-label'),
            ('select-0', 'iidcpfpj', 'form-control', '16px', 'btbusreg', lidcpfpj, 1, None, False),
            ('hr-0', None),
            ('button-0', 'btbusreg', 'btn btn-primary mt-2', 'Buscar'),
            ('alt255-0', 2),
            ('button-0', 'btnovreg', 'btn btn-primary mt-2', 'Novo registro'),
            ('alt255-0', 2),
            ('button-0', 'btrelcad', 'btn btn-primary mt-2', 'Relação de CNPJ cadastrados'),
            ('form-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
        ]
        snewpage = abnf_create_page(lnewpage)
        abnf_socket_004([1, 'abnfdv03', snewpage])
        
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u01c00501_cadastro_cnpj ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de CNPJ.                                                                                                                                   // #
# // Form de cadastro/alteração do CNPJ.                                                                                                                 // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u01c00501_cadastro_cnpj(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u01c00501_cadastro_cnpj(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        if dabnfopg['abnfobj0'] == ['btbusreg', 'btbusreg']:        # Buscar registro existente
            lmfields = [
                ['scodpfpj', 'input',  'M', 'CNPJ',          ['CNPJ'],                            None],
                ['iidcpfpj', 'select', 'M', 'Lista de CNPJ', ['Empty_to_zero', 'Return_integer'], None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btbusreg')
            # Debug: (inicio)
            # abnf_show('08', lmfields, 1)
            # abnf_show('09', dabnfopg, 2)
            # abnf_show('10', dglobaux, 2)
            # Debug: (fim)
            if bvalidad:
                icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
                scodpfpj = lmfields[0][5]
                iidcpfpj = lmfields[1][5]
                if scodpfpj == '' and iidcpfpj == 0:
                    abnf_alert('Um dos campos de busca tem que ser preenchido!', 5)
                    abnf_socket_004([5, 'btbusreg'])
                elif scodpfpj != '' and iidcpfpj > 0:
                    abnf_alert('Utilize somente um dos campos de busca!', 5)
                    abnf_socket_004([5, 'btbusreg'])
                else:
                    # ///////////////////////////////////////////////
                    # Buscando o CNPJ caso seja um registro existente
                    # ///////////////////////////////////////////////
                    lcamposb = (
                        'idcpfpj', 'codpfpj', 'nomraso', 'nomfant', 'idlogra', 'logrnum', 'logrcom',
                        'logrcep', 'rgiexxx', 'telef01', 'telef02', 'telef03', 'telef04', 'telef05',
                        'email01', 'email02', 'email03', 'email04', 'email05', 'hpage01', 'hpage02',
                        'hpage03', 'hpage04', 'hpage05', 'situreg', 'observa'
                    )
                    if   scodpfpj != '': lfilbusc = (('codpfpj', '=', scodpfpj), ('tippfpj', '=', 'J'), ('situreg', '!=', 'C'))
                    elif iidcpfpj > 0:   lfilbusc = (('idcpfpj', '=', iidcpfpj), ('situreg', '!=', 'C'))
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_cpfcnpj', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 == [] or iqtdre01 == 0:
                        abnf_alert('O CNPJ não foi encontrado!', 4)
                    else:
                        # Debug: (inicio)
                        # abnf_show('10', lsqlre01, 1)
                        # Debug: (fim)
                        abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidcpfpj', lsqlre01[0][0]),)])    # ==> Guardando o ID do registro. Obs: tem que ter essa vírgula: "),)])"
                        abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '01C00502A'),)])       # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
                        lidlogra = abnf_database_menu(icodbase, None, 'L', '0103', 1, 1, 2)
                        lnewpage = [
                            ('div-0', 'container', None, None),
                            ('hr-0', None),
                            ('div-0', 'row', None, None),
                            ('div-0', 'col d-flex justify-content-center', None, None),
                            ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                            ('legend-0', 'Cadastro de CNPJ - [ Registro existente ]'),
                            ('hr-0', None),
                            ('label-0',  'CNPJ', 'form-control-label'),
                            ('cnpj-0',   'scodpfpj', 'form-control', 0, 18, '16px', lsqlre01[0][1], 'snomraso', True, 0),
                            ('label-0',  'Razão social', 'form-control-label'),
                            ('input-0',  'snomraso', 'form-control', 0, 100, '16px', lsqlre01[0][2], 'snomfant', True, 0),
                            ('label-0',  'Nome fantasia', 'form-control-label'),
                            ('input-0',  'snomfant', 'form-control', 0, 100, '16px', lsqlre01[0][3], 'iidlogra', True, 0),
                            ('label-0',  'Logradouro: Rua/Bairro/Cidade/Estado', 'form-control-label'),
                            ('select-0', 'iidlogra', 'form-control', '16px', 'slogrnum', lidlogra, 1, lsqlre01[0][4], False),
                            ('label-0',  'Logradouro: Número', 'form-control-label'),
                            ('input-0',  'slogrnum', 'form-control', 0, 20, '16px', lsqlre01[0][5], 'slogrcom', True, 0),
                            ('label-0',  'Logradouro: Complemento (Opcional)', 'form-control-label'),
                            ('input-0',  'slogrcom', 'form-control', 0, 100, '16px', lsqlre01[0][6], 'slogrcep', True, 0),
                            ('label-0',  'Logradouro: CEP (Opcional)', 'form-control-label'),
                            ('cep-0',    'slogrcep', 'form-control', 0, 9, '16px', lsqlre01[0][7], 'srgiexxx', True, 0),
                            ('label-0',  'IE (Opcional)', 'form-control-label'),
                            ('input-0',  'srgiexxx', 'form-control', 0, 20, '16px', lsqlre01[0][8], 'stelef01', True, 0),
                            ('label-0',  'Telefone 01 (Opcional)'                        , 'form-control-label'),
                            ('phone-0',  'stelef01', 'form-control', 0, 15, '16px', lsqlre01[0][9], 'stelef02', True, 0),
                            ('label-0',  'Telefone 02 (Opcional)'                        , 'form-control-label'),
                            ('phone-0',  'stelef02', 'form-control', 0, 15, '16px', lsqlre01[0][10], 'stelef03', True, 0),
                            ('label-0',  'Telefone 03 (Opcional)'                        , 'form-control-label'),
                            ('phone-0',  'stelef03', 'form-control', 0, 15, '16px', lsqlre01[0][11], 'stelef04', True, 0),
                            ('label-0',  'Telefone 04 (Opcional)'                        , 'form-control-label'),
                            ('phone-0',  'stelef04', 'form-control', 0, 15, '16px', lsqlre01[0][12], 'stelef05', True, 0),
                            ('label-0',  'Telefone 05 (Opcional)'                        , 'form-control-label'),
                            ('phone-0',  'stelef05', 'form-control', 0, 15, '16px', lsqlre01[0][13], 'semail01', True, 0),
                            ('label-0',  'E-mail 01 (Opcional)'                          , 'form-control-label'),
                            ('input-0',  'semail01', 'form-control', 0, 100, '16px', lsqlre01[0][14], 'semail02', True, 0),
                            ('label-0',  'E-mail 02 (Opcional)'                          , 'form-control-label'),
                            ('input-0',  'semail02', 'form-control', 0, 100, '16px', lsqlre01[0][15], 'semail03', True, 0),
                            ('label-0',  'E-mail 03 (Opcional)'                          , 'form-control-label'),
                            ('input-0',  'semail03', 'form-control', 0, 100, '16px', lsqlre01[0][16], 'semail04', True, 0),
                            ('label-0',  'E-mail 04 (Opcional)'                          , 'form-control-label'),
                            ('input-0',  'semail04', 'form-control', 0, 100, '16px', lsqlre01[0][17], 'semail05', True, 0),
                            ('label-0',  'E-mail 05 (Opcional)'                          , 'form-control-label'),
                            ('input-0',  'semail05', 'form-control', 0, 100, '16px', lsqlre01[0][18], 'shpage01', True, 0),
                            ('label-0',  'Home page (ou página social) 01 (Opcional)'    , 'form-control-label'),
                            ('input-0',  'shpage01', 'form-control', 0, 100, '16px', lsqlre01[0][19], 'shpage02', True, 0),
                            ('label-0',  'Home page (ou página social) 02 (Opcional)'    , 'form-control-label'),
                            ('input-0',  'shpage02', 'form-control', 0, 100, '16px', lsqlre01[0][20], 'shpage03', True, 0),
                            ('label-0',  'Home page (ou página social) 03 (Opcional)'    , 'form-control-label'),
                            ('input-0',  'shpage03', 'form-control', 0, 100, '16px', lsqlre01[0][21], 'shpage04', True, 0),
                            ('label-0',  'Home page (ou página social) 04 (Opcional)'    , 'form-control-label'),
                            ('input-0',  'shpage04', 'form-control', 0, 100, '16px', lsqlre01[0][22], 'shpage05', True, 0),
                            ('label-0',  'Home page (ou página social) 05 (Opcional)'    , 'form-control-label'),
                            ('input-0',  'shpage05', 'form-control', 0, 100, '16px', lsqlre01[0][23], 'ssitureg', True, 0),
                            ('label-0',  'Situação do registro', 'form-control-label'),
                            ('select-0', 'ssitureg', 'form-control', '16px', 'sobserva', abnf_personal_retorna_lista(10001), 0, lsqlre01[0][24], False),                        
                            ('hr-0', None),
                            ('label-0',  'Observação (Opcional) (1000 caracteres)', 'form-control-label'),
                            ('textarea-0', 'sobserva', 'form-control', 2, 1000, '16px', lsqlre01[0][25], 'btmodsav'),
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
                        # Debug: (fim)                    
        elif dabnfopg['abnfobj0'] == ['btnovreg', 'btnovreg']:      # Novo registro
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidcpfpj', 0),)])             # ==> Indicativo para dizer que é novo registro. Obs: tem que ter essa vírgula: "),)])"
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '01C00502A'),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
            icodbase = int(dabnfopg['abnproje'][2][14:]) * 100      # Código do banco de dados a ser utilizado
            lidlogra = abnf_database_menu(icodbase, None, 'L', '0103', 1, 1, 2)
            lnewpage = [
                ('div-0', 'container', None, None),
                ('hr-0', None),
                ('div-0', 'row', None, None),
                ('div-0', 'col d-flex justify-content-center', None, None),
                ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                ('legend-0', 'Cadastro de CNPJ - [ Novo registro ]'),
                ('hr-0', None),
                ('label-0',  'CNPJ', 'form-control-label'),
                ('cnpj-0',   'scodpfpj', 'form-control', 0, 18, '16px', None, 'snomraso', True, 0),
                ('label-0',  'Razão social', 'form-control-label'),
                ('input-0',  'snomraso', 'form-control', 0, 100, '16px', None, 'snomfant', True, 0),
                ('label-0',  'Nome fantasia', 'form-control-label'),
                ('input-0',  'snomfant', 'form-control', 0, 100, '16px', None, 'iidlogra', True, 0),
                ('label-0',  'Logradouro: Rua/Bairro/Cidade/Estado', 'form-control-label'),
                ('select-0', 'iidlogra', 'form-control', '16px', 'slogrnum', lidlogra, 1, None, False),
                ('label-0',  'Logradouro: Número', 'form-control-label'),
                ('input-0',  'slogrnum', 'form-control', 0, 20, '16px', None, 'slogrcom', True, 0),
                ('label-0',  'Logradouro: Complemento (Opcional)', 'form-control-label'),
                ('input-0',  'slogrcom', 'form-control', 0, 100, '16px', None, 'slogrcep', True, 0),
                ('label-0',  'Logradouro: CEP (Opcional)', 'form-control-label'),
                ('cep-0',    'slogrcep', 'form-control', 0, 9, '16px', None, 'srgiexxx', True, 0),
                ('label-0',  'IE (Opcional)', 'form-control-label'),
                ('input-0',  'srgiexxx', 'form-control', 0, 20, '16px', None, 'stelef01', True, 0),
                ('label-0',  'Telefone 01 (Opcional)'                       , 'form-control-label'),
                ('phone-0',  'stelef01', 'form-control', 0, 15, '16px', None, 'stelef02', True, 0),
                ('label-0',  'Telefone 02 (Opcional)'                        , 'form-control-label'),
                ('phone-0',  'stelef02', 'form-control', 0, 15, '16px', None, 'stelef03', True, 0),
                ('label-0',  'Telefone 03 (Opcional)'                        , 'form-control-label'),
                ('phone-0',  'stelef03', 'form-control', 0, 15, '16px', None, 'stelef04', True, 0),
                ('label-0',  'Telefone 04 (Opcional)'                        , 'form-control-label'),
                ('phone-0',  'stelef04', 'form-control', 0, 15, '16px', None, 'stelef05', True, 0),
                ('label-0',  'Telefone 05 (Opcional)'                        , 'form-control-label'),
                ('phone-0',  'stelef05', 'form-control', 0, 15, '16px', None, 'semail01', True, 0),
                ('label-0',  'E-mail 01 (Opcional)'                          , 'form-control-label'),
                ('input-0',  'semail01', 'form-control', 0, 100, '16px', None, 'semail02', True, 0),
                ('label-0',  'E-mail 02 (Opcional)'                          , 'form-control-label'),
                ('input-0',  'semail02', 'form-control', 0, 100, '16px', None, 'semail03', True, 0),
                ('label-0',  'E-mail 03 (Opcional)'                          , 'form-control-label'),
                ('input-0',  'semail03', 'form-control', 0, 100, '16px', None, 'semail04', True, 0),
                ('label-0',  'E-mail 04 (Opcional)'                          , 'form-control-label'),
                ('input-0',  'semail04', 'form-control', 0, 100, '16px', None, 'semail05', True, 0),
                ('label-0',  'E-mail 05 (Opcional)'                          , 'form-control-label'),
                ('input-0',  'semail05', 'form-control', 0, 100, '16px', None, 'shpage01', True, 0),
                ('label-0',  'Home page (ou página social) 01 (Opcional)'    , 'form-control-label'),
                ('input-0',  'shpage01', 'form-control', 0, 100, '16px', None, 'shpage02', True, 0),
                ('label-0',  'Home page (ou página social) 02 (Opcional)'    , 'form-control-label'),
                ('input-0',  'shpage02', 'form-control', 0, 100, '16px', None, 'shpage03', True, 0),
                ('label-0',  'Home page (ou página social) 03 (Opcional)'    , 'form-control-label'),
                ('input-0',  'shpage03', 'form-control', 0, 100, '16px', None, 'shpage04', True, 0),
                ('label-0',  'Home page (ou página social) 04 (Opcional)'    , 'form-control-label'),
                ('input-0',  'shpage04', 'form-control', 0, 100, '16px', None, 'shpage05', True, 0),
                ('label-0',  'Home page (ou página social) 05 (Opcional)'    , 'form-control-label'),
                ('input-0',  'shpage05', 'form-control', 0, 100, '16px', None, 'sobserva', True, 0),
                ('label-0',  'Observação (Opcional) (1000 caracteres)'       , 'form-control-label'),
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
            # abnf_socket_004([3, 'scodpfpj', '16.643.656/0001-62'                                                                                    ])
            # abnf_socket_004([3, 'snomraso', 'ALEXANDRE HIKARI ABE'                                                                                  ])
            # abnf_socket_004([3, 'snomfant', 'ABEINFO SISTEMAS'                                                                                      ])
            # abnf_socket_004([3, 'iidlogra', '1'                                                                                                     ])
            # abnf_socket_004([3, 'slogrnum', '842'                                                                                                   ])
            # //////////////// #
            # abnf_socket_004([3, 'scodpfpj', '16.643.656/0001-62'                                                                                    ])
            # abnf_socket_004([3, 'snomraso', 'ALEXANDRE AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA0'  ])
            # abnf_socket_004([3, 'snomfant', '0BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB0'  ])
            # abnf_socket_004([3, 'iidlogra', '1'                                                                                                     ])
            # abnf_socket_004([3, 'slogrnum', '0CCCCCCCCCCCCCCCCCC0'                                                                                  ])
            # abnf_socket_004([3, 'slogrcom', '0DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD0'  ])
            # abnf_socket_004([3, 'slogrcep', '09999-990'                                                                                             ])
            # abnf_socket_004([3, 'srgiexxx', '0EEEEEEEEEEEEEEEEEE0'                                                                                  ])
            # abnf_socket_004([3, 'stelef01', '(01) 11111-1110'                                                                                       ])
            # abnf_socket_004([3, 'stelef02', '(02) 22222-2220'                                                                                       ])
            # abnf_socket_004([3, 'stelef03', '(03) 33333-3330'                                                                                       ])
            # abnf_socket_004([3, 'stelef04', '(04) 44444-4440'                                                                                       ])
            # abnf_socket_004([3, 'stelef05', '(05) 55555-5550'                                                                                       ])
            # abnf_socket_004([3, 'semail01', 'TESTE001@111111111111111111111111111111111111111111111111111111111111111111111111111111111111111.COM'  ])
            # abnf_socket_004([3, 'semail02', 'TESTE001@222222222222222222222222222222222222222222222222222222222222222222222222222222222222222.COM'  ])
            # abnf_socket_004([3, 'semail03', 'TESTE001@333333333333333333333333333333333333333333333333333333333333333333333333333333333333333.COM'  ])
            # abnf_socket_004([3, 'semail04', 'TESTE001@444444444444444444444444444444444444444444444444444444444444444444444444444444444444444.COM'  ])
            # abnf_socket_004([3, 'semail05', 'TESTE001@555555555555555555555555555555555555555555555555555555555555555555555555555555555555555.COM'  ])
            # abnf_socket_004([3, 'shpage01', '0VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV0'  ])
            # abnf_socket_004([3, 'shpage02', '0WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW0'  ])
            # abnf_socket_004([3, 'shpage03', '0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0'  ])
            # abnf_socket_004([3, 'shpage04', '0YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY0'  ])
            # abnf_socket_004([3, 'shpage05', '0ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ0'  ])
            # abnf_socket_004([3, 'sobserva', 'TESTANDO OBSERVACAO'                                                                                   ])
            # Debug: (fim)
        elif dabnfopg['abnfobj0'] == ['btrelcad', 'btrelcad']:      # Relação de CNPJ cadastrados
            abnf000u01c00503_cadastro_cnpj(dabnfopg)
            
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u01c00502_cadastro_cnpj ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de CNPJ.                                                                                                                                   // #
# // Gravação dos registros e geração de log.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u01c00502_cadastro_cnpj(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u01c00502_cadastro_cnpj(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        if dabnfopg['abnfobj0'] == ['btcancel', 'btcancel']:        # Voltar para tela anterior
            abnf000u01c00500_cadastro_cnpj(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btsalreg', 'btsalreg']:      # Salvar o registro
            iidcpfpj = dglobaux['iidcpfpj']
            lmfields = [
                ['scodpfpj', 'input',    'M', 'CNPJ',                                  ['Notnull', 'CNPJ', 'D'],  None],
                ['snomraso', 'input',    'F', 'razão social',                          ['Notnull', 'D'],          None],
                ['snomfant', 'input',    'F', 'nome fantasia',                         [],                        None],
                ['iidlogra', 'number',   'M', 'logradouro (rua/bairro/cidade/estado)', ['Notnull', 'D'],          None],
                ['slogrnum', 'input',    'M', 'logradouro (número)',                   ['Notnull', 'D'],          None],
                ['slogrcom', 'input',    'M', 'logradouro (complemento)',              [],                        None],
                ['slogrcep', 'input',    'M', 'logradouro (CEP)',                      [],                        None],
                ['srgiexxx', 'input',    'F', 'incrição estadual',                     [],                        None],
                ['stelef01', 'input',    'M', 'telefone 01',                           [],                        None],
                ['stelef02', 'input',    'M', 'telefone 02',                           [],                        None],
                ['stelef03', 'input',    'M', 'telefone 03',                           [],                        None],
                ['stelef04', 'input',    'M', 'telefone 04',                           [],                        None],
                ['stelef05', 'input',    'M', 'telefone 05',                           [],                        None],
                ['semail01', 'input',    'M', 'e-mail 01',                             ['e-mail'],                None],
                ['semail02', 'input',    'M', 'e-mail 02',                             ['e-mail'],                None],
                ['semail03', 'input',    'M', 'e-mail 03',                             ['e-mail'],                None],
                ['semail04', 'input',    'M', 'e-mail 04',                             ['e-mail'],                None],
                ['semail05', 'input',    'M', 'e-mail 05',                             ['e-mail'],                None],
                ['shpage01', 'input',    'F', 'home page 01',                          [],                        None],
                ['shpage02', 'input',    'F', 'home page 02',                          [],                        None],
                ['shpage03', 'input',    'F', 'home page 03',                          [],                        None],
                ['shpage04', 'input',    'F', 'home page 04',                          [],                        None],
                ['shpage05', 'input',    'F', 'home page 05',                          [],                        None],
                ['sobserva', 'textarea', 'F', 'observação',                            [],                        None],
            ]
            if iidcpfpj > 0: lmfields = lmfields + [
                ['ssitureg', 'select',   'F', 'situação do registro',                  ['Notnull', 'D'],          None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btsalreg')
            # Debug: (inicio)
            # abnf_show('10', lmfields, 1)
            # abnf_show('09', dabnfopg, 2)
            # abnf_show('10', dglobaux, 0)
            # Debug: (fim)
            if bvalidad:
                icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
                if iidcpfpj == 0:   # Novo registro
                    lcamposb = ('codpfpj', 'idcpfpj')
                    lfilbusc = (('codpfpj', '=', lmfields[0][5]), ('situreg', '!=', 'C'))
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_cpfcnpj', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 != [] or iqtdre01 != 0:
                        abnf_alert('Não foi possível salvar! O CNPJ ' + str(lmfields[0][5]) + ' já está sendo utilizado em outro registro!', 4)
                    else:
                        bvalidad, iproxiid = abnf_database_insere_dados_v02(icodbase, sabnproj, 'abnf_cadastro_cpfcnpj', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                        [
                            ('codpfpj', lmfields[0][5]),
                            ('nomraso', lmfields[1][5]),
                            ('nomfant', lmfields[2][5]),
                            ('idlogra', lmfields[3][5]),
                            ('logrnum', lmfields[4][5]),
                            ('logrcom', lmfields[5][5]),
                            ('logrcep', lmfields[6][5]),
                            ('rgiexxx', lmfields[7][5]),
                            ('telef01', lmfields[8][5]),
                            ('telef02', lmfields[9][5]),
                            ('telef03', lmfields[10][5]),
                            ('telef04', lmfields[11][5]),
                            ('telef05', lmfields[12][5]),
                            ('email01', lmfields[13][5]),
                            ('email02', lmfields[14][5]),
                            ('email03', lmfields[15][5]),
                            ('email04', lmfields[16][5]),
                            ('email05', lmfields[17][5]),
                            ('hpage01', lmfields[18][5]),
                            ('hpage02', lmfields[19][5]),
                            ('hpage03', lmfields[20][5]),
                            ('hpage04', lmfields[21][5]),
                            ('hpage05', lmfields[22][5]),
                            ('observa', lmfields[23][5]),
                            ('tippfpj', 'J'),
                            ('situreg', 'A'),
                        ])
                        if bvalidad:
                            abnf_alert('Novo CNPJ gravado com sucesso!', 3)
                            abnf000u01c00500_cadastro_cnpj(dabnfopg)
                elif iidcpfpj > 0:  # Registro existente
                    lcamposb = ('codpfpj', 'idcpfpj')
                    lfilbusc = (('codpfpj', '=', lmfields[0][5]), ('situreg', '!=', 'C'), ('idcpfpj', '!=', iidcpfpj))
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_cpfcnpj', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 != [] or iqtdre01 != 0:
                        abnf_alert('Não foi possível salvar! O CNPJ ' + str(lmfields[0][5]) + ' já está sendo utilizado em outro registro!', 4)
                    else:
                        # abnf_show('10', lmfields, 1)
                        bvalidad = abnf_database_altera_dados_v02(icodbase, sabnproj, 'abnf_cadastro_cpfcnpj', iidcpfpj, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                        [
                            ('codpfpj', lmfields[0][5]),
                            ('nomraso', lmfields[1][5]),
                            ('nomfant', lmfields[2][5]),
                            ('idlogra', lmfields[3][5]),
                            ('logrnum', lmfields[4][5]),
                            ('logrcom', lmfields[5][5]),
                            ('logrcep', lmfields[6][5]),
                            ('rgiexxx', lmfields[7][5]),
                            ('telef01', lmfields[8][5]),
                            ('telef02', lmfields[9][5]),
                            ('telef03', lmfields[10][5]),
                            ('telef04', lmfields[11][5]),
                            ('telef05', lmfields[12][5]),
                            ('email01', lmfields[13][5]),
                            ('email02', lmfields[14][5]),
                            ('email03', lmfields[15][5]),
                            ('email04', lmfields[16][5]),
                            ('email05', lmfields[17][5]),
                            ('hpage01', lmfields[18][5]),
                            ('hpage02', lmfields[19][5]),
                            ('hpage03', lmfields[20][5]),
                            ('hpage04', lmfields[21][5]),
                            ('hpage05', lmfields[22][5]),
                            ('observa', lmfields[23][5]),
                            ('situreg', lmfields[24][5]),
                        ])
                        if bvalidad:
                            abnf_alert('Registro alterado com sucesso!', 3)
                            abnf000u01c00500_cadastro_cnpj(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btexcreg', 'btexcreg']:      # Excluir registro
            iidcpfpj = dglobaux['iidcpfpj']        
            icodbase = int(dabnfopg['abnproje'][2][14:]) * 100      # Código do banco de dados a ser utilizado
            bvalidad = abnf_database_exclui_registro(icodbase, sabnproj, 'abnf_cadastro_cpfcnpj', iidcpfpj, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'])
            if bvalidad:
                abnf_alert('Registro excluído com sucesso!', 3)
                abnf000u01c00500_cadastro_cnpj(dabnfopg)
                
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u01c00503_cadastro_cnpj ] /////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de CNPJ.                                                                                                                                   // #
# // Relatório de CNPJ.                                                                                                                                  // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
                
def abnf000u01c00503_cadastro_cnpj(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u01c00503_cadastro_cnpj(dabnfopg)')
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
            abnf_imprime_thead_002_titulo_relatorio(sarquwri, icolspan, 'RELAÇÃO DE CNPJ')
            abnf_imprime_thead_003_empresa_filial(sarquwri, icolspan, snomeemp, snomefil)
            # smensage = 'Per&iacute;odo: ' + abnf_converte_data(ddataini) + ' &agrave;s ' + abnf_converte_hora(thoraini) + ' at&eacute; ' + abnf_converte_data(ddatafim) + ' &agrave;s ' + abnf_converte_hora(thorafim)
            # abnf_imprime_thead_004_parametros(sarquwri, icolspan, smensage)
            abnf_imprime_thead_005_datetime(sarquwri, icolspan)
            abnf_imprime_line(sarquwri, icolspan, 'darkcyan')
            abnf_imprime_info_001(sarquwri, '#D1C5C5', 'center', 1,
                [
                    ('Razão Social', 1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('CNPJ',         1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Situação',     1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                ]
            )
            abnf_imprime_fthead_tbody(sarquwri)
            lcamposb = ('nomraso', 'codpfpj', 'situreg')
            lfilbusc = (('situreg', '!=', 'C'), ('tippfpj', '=', 'J'))
            lorderby = ('nomraso', 'idcpfpj')
            lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_cpfcnpj', lcamposb, lfilbusc, lorderby)
            for lauxi001 in lsqlre01:
                ssitureg = abnf_personal_retorna_string(10001, lauxi001[2])
                icontreg += 1
                abnf_imprime_info_001(sarquwri, None, None, 1,
                    [
                        (lauxi001[0], 1, 0, None, 'Left'  , 'black', 'Courier New', ifontlen, True, False),
                        (lauxi001[1], 1, 0, None, 'Center', 'black', 'Courier New', ifontlen, True, False),
                        (ssitureg,    1, 0, None, 'Center', 'black', 'Courier New', ifontlen, True, False),
                    ]
                )
            abnf_imprime_line(sarquwri, icolspan, 'darkcyan')
            abnf_imprime_info_001(sarquwri, None, None, 1,
                [
                    ('Total de registros impressos:', icolspan - 1, 0, None, 'Left' , 'black', 'Courier New', ifontlen, True, False),
                    (icontreg,                                   1, 0, None, 'Right', 'black', 'Courier New', ifontlen, True, False),
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