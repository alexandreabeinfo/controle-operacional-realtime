## =======================================
## [abnf000u01c00400.py] - Cadastro de CPF
## =======================================

from abnfsrc.abnf000u00s00003 import *              # Arquivo de funções comuns que serão utilizadas por todos os módulos do sistema
from abnfsrc.abnf000u00s00004 import *              # Arquivo de banco de dados

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u01c00400_cadastro_cpf ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de CPF.                                                                                                                                    // #
# // Form inicial.                                                                                                                                       // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u01c00400_cadastro_cpf(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u01c00400_cadastro_cpf(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        abnf_socket_004([1, 'abnfdv03', abnf_create_spinner(1, 100)])
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, '01C00401A'])
        icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
        lidcpfpj = abnf_database_menu(icodbase, None, 'L', '0104', 1, 1, 2)
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
            ('legend-0', 'Cadastro de CPF'),
            ('hr-0', None),
            ('label-0',  'CPF', 'form-control-label'),
            ('cpf-0',    'scodpfpj', 'form-control', 0, 14, '16px', None, 'btbusreg', True, 0),
            ('label-0',  'Lista de CPF', 'form-control-label'),
            ('select-0', 'iidcpfpj', 'form-control', '16px', 'btbusreg', lidcpfpj, 1, None, False),
            ('hr-0', None),
            ('button-0', 'btbusreg', 'btn btn-primary mt-2', 'Buscar'),
            ('alt255-0', 2),
            ('button-0', 'btnovreg', 'btn btn-primary mt-2', 'Novo registro'),
            ('alt255-0', 2),
            ('button-0', 'btrelcad', 'btn btn-primary mt-2', 'Relação de CPF cadastrados'),
            ('form-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
            ('div-9', None),
        ]
        snewpage = abnf_create_page(lnewpage)
        abnf_socket_004([1, 'abnfdv03', snewpage])
        
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u01c00401_cadastro_cpf ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de CPF.                                                                                                                                    // #
# // Form de cadastro/alteração do CPF.                                                                                                                  // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u01c00401_cadastro_cpf(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u01c00401_cadastro_cpf(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        if dabnfopg['abnfobj0'] == ['btbusreg', 'btbusreg']:        # Buscar registro existente
            lmfields = [
                ['scodpfpj', 'input',  'M', 'CPF',          ['CPF'],                             None],
                ['iidcpfpj', 'select', 'M', 'Lista de CPF', ['Empty_to_zero', 'Return_integer'], None],
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
                    # //////////////////////////////////////////////
                    # Buscando o CPF caso seja um registro existente
                    # //////////////////////////////////////////////
                    lcamposb = (
                        'idcpfpj', 'codpfpj', 'nomraso', 'idlogra', 'logrnum', 'logrcom', 'logrcep',
                        'sexoxxx', 'rgiexxx', 'cnhxxxx', 'titenum', 'titezon', 'titesec', 'certres',
                        'datanas', 'datacas', 'datafal', 'nomepai', 'nomemae', 'nomecon', 'telef01',
                        'telef02', 'telef03', 'telef04', 'telef05', 'email01', 'email02', 'email03',
                        'email04', 'email05', 'hpage01', 'hpage02', 'hpage03', 'hpage04', 'hpage05',
                        'situreg', 'observa', 'idfotof'
                    )
                    if   scodpfpj != '': lfilbusc = (('codpfpj', '=', scodpfpj), ('tippfpj', '=', 'F'), ('situreg', '!=', 'C'))
                    elif iidcpfpj > 0:   lfilbusc = (('idcpfpj', '=', iidcpfpj), ('situreg', '!=', 'C'))
                    lorderby = None
                    lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_cpfcnpj', lcamposb, lfilbusc, lorderby)
                    if lsqlre01 == [] or iqtdre01 == 0:
                        abnf_alert('O CPF não foi encontrado!', 4)
                    else:
                        # Debug: (inicio)
                        # abnf_show('10', lsqlre01, 1)
                        # Debug: (fim)
                        abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('iidcpfpj', lsqlre01[0][0]),)])    # ==> Guardando o ID do registro. Obs: tem que ter essa vírgula: "),)])"
                        abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '01C00402A'),)])       # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
                        # Define o local de documentos do projeto e busca o arquivo de foto do usuário (caso tenha)
                        simage01 = None
                        if lsqlre01[0][37] != None:
                            sldocpro = abnf_websocket_local_docs(sabnproj)
                            scamposb = 'nomearq'
                            sfilbusc = 'idarqui = ' + str(lsqlre01[0][37])
                            lsqlre02, iqtdre02 = abnf_database_busca_dados_v01(icodbase, 'abnf_sistema_arquivos', scamposb, sfilbusc, None)
                            if lsqlre02 != '[]' and iqtdre02 != 0:
                                sarqimag = sldocpro + lsqlre02[0][0]                    
                                simage01 = abnf_websocket_converte_arquivo_imagem_base64(sarqimag, 'rounded mx-auto d-block', '25%', '25%')
                                # Nota: 24/07/2024
                                # Não esta funcionando da forma abaixo.
                                # simage01 = abnf_websocket_arquivo_imagem(sarqimag, 'rounded mx-auto d-block', '25%', '25%') 
                                # Provavelmente vai ter que criar um link igual fez para a JSON do Elevar
                                # <img src="/static/abnfsrc/static/abnfarc/abnfuser000000008-9e8f26db-1864-4051-8487-0dfb24.jpg" width="25%" height="25%" class="rounded mx-auto d-block">
                                # Testar com a sugestão abaixo do Gemini:
                                # == Sugestão do Gemini ==> from flask import Flask, send_from_directory
                                # == Sugestão do Gemini ==> 
                                # == Sugestão do Gemini ==> app = Flask(__name__)
                                # == Sugestão do Gemini ==> 
                                # == Sugestão do Gemini ==> @app.route('/arquivos_imagens/<arquivo>')
                                # == Sugestão do Gemini ==> def arquivos_imagens(arquivo):
                                # == Sugestão do Gemini ==>    #return send_from_directory('/home/usuarios/imagens', arquivo)
                                # == Sugestão do Gemini ==> 
                                # == Sugestão do Gemini ==> if __name__ == '__main__':
                                # == Sugestão do Gemini ==>    #app.run(debug=True)
                        lidlogra = abnf_database_menu(icodbase, None, 'L', '0103', 1, 1, 2)
                        lnewpage = [
                            ('div-0', 'container', None, None),
                            ('hr-0', None),
                            ('div-0', 'row', None, None),
                            ('div-0', 'col d-flex justify-content-center', None, None),
                            ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                            ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                            ('legend-0', 'Cadastro de CPF - [ Registro existente ]'),
                            ('hr-0', None),
                        ]    
                        if simage01 != None: lnewpage = lnewpage + [
                            ('div-0', 'img-responsive mt-2 d-flex flex-row align-items-center w-100', None, simage01),
                            ('div-9', None),
                            ('hr-0', None),
                        ]
                        lnewpage = lnewpage + [
                            ('label-0',  'CPF', 'form-control-label'),
                            ('cpf-0',    'scodpfpj', 'form-control', 0, 14, '16px', lsqlre01[0][1], 'snomraso', True, 0),
                            ('label-0',  'Nome', 'form-control-label'),
                            ('input-0',  'snomraso', 'form-control', 0, 100, '16px', lsqlre01[0][2], 'iidlogra', True, 0),
                            ('label-0',  'Logradouro: Rua/Bairro/Cidade/Estado', 'form-control-label'),
                            ('select-0', 'iidlogra', 'form-control', '16px', 'slogrnum', lidlogra, 1, lsqlre01[0][3], False),
                            ('label-0',  'Logradouro: Número', 'form-control-label'),
                            ('input-0',  'slogrnum', 'form-control', 0, 20, '16px', lsqlre01[0][4], 'slogrcom', True, 0),
                            ('label-0',  'Logradouro: Complemento (Opcional)', 'form-control-label'),
                            ('input-0',  'slogrcom', 'form-control', 0, 100, '16px', lsqlre01[0][5], 'slogrcep', True, 0),
                            ('label-0',  'Logradouro: CEP (Opcional)', 'form-control-label'),
                            ('cep-0',    'slogrcep', 'form-control', 0, 9, '16px', lsqlre01[0][6], 'ssexoxxx', True, 0),
                            ('label-0',  'Sexo (Opcional)', 'form-control-label'),
                            ('select-0', 'ssexoxxx', 'form-control', '16px', 'srgiexxx', abnf_personal_retorna_lista(10002), 0, lsqlre01[0][7], False),
                            ('label-0',  'RG (Opcional)', 'form-control-label'),
                            ('input-0',  'srgiexxx', 'form-control', 0, 20, '16px', lsqlre01[0][8], 'scnhxxxx', True, 0),
                            ('label-0',  'CNH (Opcional)', 'form-control-label'),
                            ('input-0',  'scnhxxxx', 'form-control', 0, 20, '16px', lsqlre01[0][9], 'stitenum', True, 0),
                            ('label-0',  'Titulo de eleitor - Número (Opcional)', 'form-control-label'),
                            ('number-0', 'stitenum', 'form-control', 0, 20, '16px', lsqlre01[0][10], 'stitezon', True, None),
                            ('label-0',  'Titulo de eleitor - Zona (Opcional)'  , 'form-control-label'),
                            ('number-0', 'stitezon', 'form-control', 0, 10, '16px', lsqlre01[0][11], 'stitesec', True, None),
                            ('label-0',  'Titulo de eleitor - Seção (Opcional)'  , 'form-control-label'),
                            ('number-0', 'stitesec', 'form-control', 0, 10, '16px', lsqlre01[0][12], 'scertres', True, None),
                            ('label-0',  'Certificado de reservista (Opcional)'  , 'form-control-label'),
                            ('input-0',  'scertres', 'form-control', 0, 20, '16px', lsqlre01[0][13], 'ddatanas', True, 0),
                            ('label-0',  'Data de nascimento (Opcional)'                 , 'form-control-label'),
                            ('date-0',   'ddatanas', 'form-control', '16px', lsqlre01[0][14], 'ddatacas', True, 0, None),
                            ('label-0',  'Data de casamento (Opcional)'                  , 'form-control-label'),
                            ('date-0',   'ddatacas', 'form-control', '16px', lsqlre01[0][15], 'ddatafal', True, 0, None),
                            ('label-0',  'Data de falecimento (Opcional)'                , 'form-control-label'),
                            ('date-0',   'ddatafal', 'form-control', '16px', lsqlre01[0][16], 'snomepai', True, 0 , None),
                            ('label-0',  'Nome pai (Opcional)'                           , 'form-control-label'),
                            ('input-0',  'snomepai', 'form-control', 0, 100, '16px', lsqlre01[0][17], 'snomemae', True, 0),
                            ('label-0',  'Nome mãe (Opcional)'                           , 'form-control-label'),
                            ('input-0',  'snomemae', 'form-control', 0, 100, '16px', lsqlre01[0][18], 'snomecon', True, 0),
                            ('label-0',  'Nome conjuge (Opcional)'                       , 'form-control-label'),
                            ('input-0',  'snomecon', 'form-control', 0, 100, '16px', lsqlre01[0][19], 'stelef01', True, 0),
                            ('label-0',  'Telefone 01 (Opcional)'                       , 'form-control-label'),
                            ('phone-0',  'stelef01', 'form-control', 0, 15, '16px', lsqlre01[0][20], 'stelef02', True, 0),
                            ('label-0',  'Telefone 02 (Opcional)'                        , 'form-control-label'),
                            ('phone-0',  'stelef02', 'form-control', 0, 15, '16px', lsqlre01[0][21], 'stelef03', True, 0),
                            ('label-0',  'Telefone 03 (Opcional)'                        , 'form-control-label'),
                            ('phone-0',  'stelef03', 'form-control', 0, 15, '16px', lsqlre01[0][22], 'stelef04', True, 0),
                            ('label-0',  'Telefone 04 (Opcional)'                        , 'form-control-label'),
                            ('phone-0',  'stelef04', 'form-control', 0, 15, '16px', lsqlre01[0][23], 'stelef05', True, 0),
                            ('label-0',  'Telefone 05 (Opcional)'                        , 'form-control-label'),
                            ('phone-0',  'stelef05', 'form-control', 0, 15, '16px', lsqlre01[0][24], 'semail01', True, 0),
                            ('label-0',  'E-mail 01 (Opcional)'                          , 'form-control-label'),
                            ('input-0',  'semail01', 'form-control', 0, 100, '16px', lsqlre01[0][25], 'semail02', True, 0),
                            ('label-0',  'E-mail 02 (Opcional)'                          , 'form-control-label'),
                            ('input-0',  'semail02', 'form-control', 0, 100, '16px', lsqlre01[0][26], 'semail03', True, 0),
                            ('label-0',  'E-mail 03 (Opcional)'                          , 'form-control-label'),
                            ('input-0',  'semail03', 'form-control', 0, 100, '16px', lsqlre01[0][27], 'semail04', True, 0),
                            ('label-0',  'E-mail 04 (Opcional)'                          , 'form-control-label'),
                            ('input-0',  'semail04', 'form-control', 0, 100, '16px', lsqlre01[0][28], 'semail05', True, 0),
                            ('label-0',  'E-mail 05 (Opcional)'                          , 'form-control-label'),
                            ('input-0',  'semail05', 'form-control', 0, 100, '16px', lsqlre01[0][29], 'shpage01', True, 0),
                            ('label-0',  'Home page (ou página social) 01 (Opcional)'    , 'form-control-label'),
                            ('input-0',  'shpage01', 'form-control', 0, 100, '16px', lsqlre01[0][30], 'shpage02', True, 0),
                            ('label-0',  'Home page (ou página social) 02 (Opcional)'    , 'form-control-label'),
                            ('input-0',  'shpage02', 'form-control', 0, 100, '16px', lsqlre01[0][31], 'shpage03', True, 0),
                            ('label-0',  'Home page (ou página social) 03 (Opcional)'    , 'form-control-label'),
                            ('input-0',  'shpage03', 'form-control', 0, 100, '16px', lsqlre01[0][32], 'shpage04', True, 0),
                            ('label-0',  'Home page (ou página social) 04 (Opcional)'    , 'form-control-label'),
                            ('input-0',  'shpage04', 'form-control', 0, 100, '16px', lsqlre01[0][33], 'shpage05', True, 0),
                            ('label-0',  'Home page (ou página social) 05 (Opcional)'    , 'form-control-label'),
                            ('input-0',  'shpage05', 'form-control', 0, 100, '16px', lsqlre01[0][34], 'ssitureg', True, 0),
                            ('label-0',  'Situação do registro', 'form-control-label'),
                            ('select-0', 'ssitureg', 'form-control', '16px', 'sobserva', abnf_personal_retorna_lista(10001), 0, lsqlre01[0][35], False),                        
                            ('hr-0', None),
                            ('label-0',  'Observação (Opcional) (1000 caracteres)', 'form-control-label'),
                            ('textarea-0', 'sobserva', 'form-control', 2, 1000, '16px', lsqlre01[0][36], 'btmodsav'),
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
            abnf_websocket_control_globdws(sabnproj, sabntoke, [3, (('sabnfsys', '01C00402A'),)])   # ==> Próximo módulo que o sistema deverá buscar. Obs: tem que ter essa vírgula: "),)])"
            icodbase = int(dabnfopg['abnproje'][2][14:]) * 100      # Código do banco de dados a ser utilizado
            lidlogra = abnf_database_menu(icodbase, None, 'L', '0103', 1, 1, 2)
            lnewpage = [
                ('div-0', 'container', None, None),
                ('hr-0', None),
                ('div-0', 'row', None, None),
                ('div-0', 'col d-flex justify-content-center', None, None),
                ('div-0', 'w-100 p-3', 'background-color: #eee;', None),
                ('form-0', 'border p-4 mt-2 rounded border-secondary border-3'),
                ('legend-0', 'Cadastro de CPF - [ Novo registro ]'),
                ('hr-0', None),
                ('label-0',  'CPF', 'form-control-label'),
                ('cpf-0',    'scodpfpj', 'form-control', 0, 14, '16px', None, 'snomraso', True, 0),
                ('label-0',  'Nome', 'form-control-label'),
                ('input-0',  'snomraso', 'form-control', 0, 100, '16px', None, 'iidlogra', True, 0),
                ('label-0',  'Logradouro: Rua/Bairro/Cidade/Estado', 'form-control-label'),
                ('select-0', 'iidlogra', 'form-control', '16px', 'slogrnum', lidlogra, 1, None, False),
                ('label-0',  'Logradouro: Número', 'form-control-label'),
                ('input-0',  'slogrnum', 'form-control', 0, 20, '16px', None, 'slogrcom', True, 0),
                ('label-0',  'Logradouro: Complemento (Opcional)', 'form-control-label'),
                ('input-0',  'slogrcom', 'form-control', 0, 100, '16px', None, 'slogrcep', True, 0),
                ('label-0',  'Logradouro: CEP (Opcional)', 'form-control-label'),
                ('cep-0',    'slogrcep', 'form-control', 0, 9, '16px', None, 'ssexoxxx', True, 0),
                ('label-0',  'Sexo (Opcional)', 'form-control-label'),
                ('select-0', 'ssexoxxx', 'form-control', '16px', 'srgiexxx', abnf_personal_retorna_lista(10002), 0, None, False),
                ('label-0',  'RG (Opcional)', 'form-control-label'),
                ('input-0',  'srgiexxx', 'form-control', 0, 20, '16px', None, 'scnhxxxx', True, 0),
                ('label-0',  'CNH (Opcional)', 'form-control-label'),
                ('input-0',  'scnhxxxx', 'form-control', 0, 20, '16px', None, 'stitenum', True, 0),
                ('label-0',  'Titulo de eleitor - Número (Opcional)', 'form-control-label'),
                ('number-0', 'stitenum', 'form-control', 0, 20, '16px', None, 'stitezon', True, None),
                ('label-0',  'Titulo de eleitor - Zona (Opcional)'  , 'form-control-label'),
                ('number-0', 'stitezon', 'form-control', 0, 10, '16px', None, 'stitesec', True, None),
                ('label-0',  'Titulo de eleitor - Seção (Opcional)'  , 'form-control-label'),
                ('number-0', 'stitesec', 'form-control', 0, 10, '16px', None, 'scertres', True, None),
                ('label-0',  'Certificado de reservista (Opcional)'  , 'form-control-label'),
                ('input-0',  'scertres', 'form-control', 0, 20, '16px', None, 'ddatanas', True, 0),
                ('label-0',  'Data de nascimento (Opcional)'                 , 'form-control-label'),
                ('date-0',   'ddatanas', 'form-control', '16px', None, 'ddatacas', True, 0, None),
                ('label-0',  'Data de casamento (Opcional)'                  , 'form-control-label'),
                ('date-0',   'ddatacas', 'form-control', '16px', None, 'ddatafal', True, 0, None),
                ('label-0',  'Data de falecimento (Opcional)'                , 'form-control-label'),
                ('date-0',   'ddatafal', 'form-control', '16px', None, 'snomepai', True, 0, None),
                ('label-0',  'Nome pai (Opcional)'                           , 'form-control-label'),
                ('input-0',  'snomepai', 'form-control', 0, 100, '16px', None, 'snomemae', True, 0),
                ('label-0',  'Nome mãe (Opcional)'                           , 'form-control-label'),
                ('input-0',  'snomemae', 'form-control', 0, 100, '16px', None, 'snomecon', True, 0),
                ('label-0',  'Nome conjuge (Opcional)'                       , 'form-control-label'),
                ('input-0',  'snomecon', 'form-control', 0, 100, '16px', None, 'stelef01', True, 0),
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
            # abnf_socket_004([3, 'scodpfpj', '057.336.440-01'                                                                                        ])
            # abnf_socket_004([3, 'snomraso', 'ALEXANDRE AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA0'  ])
            # abnf_socket_004([3, 'iidlogra', '1'                                                                                                     ])
            # abnf_socket_004([3, 'slogrnum', '0BBBBBBBBBBBBBBBBBB0'                                                                                  ])
            # abnf_socket_004([3, 'slogrcom', '0CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC0'  ])
            # abnf_socket_004([3, 'slogrcep', '09999-990'                                                                                             ])
            # abnf_socket_004([3, 'ssexoxxx', 'M'                                                                                                     ])
            # abnf_socket_004([3, 'srgiexxx', '0DDDDDDDDDDDDDDDDDD0'                                                                                  ])
            # abnf_socket_004([3, 'scnhxxxx', '0EEEEEEEEEEEEEEEEEE0'                                                                                  ])
            # abnf_socket_004([3, 'stitenum', '91111111111111111119'                                                                                  ])
            # abnf_socket_004([3, 'stitezon', '9222222229'                                                                                            ])
            # abnf_socket_004([3, 'stitesec', '9333333339'                                                                                            ])
            # abnf_socket_004([3, 'scertres', '0FFFFFFFFFFFFFFFFFF0'                                                                                  ])
            # abnf_socket_004([3, 'ddatanas', '2024-02-01'                                                                                            ])
            # abnf_socket_004([3, 'ddatacas', '2024-04-03'                                                                                            ])
            # abnf_socket_004([3, 'ddatafal', '2024-06-05'                                                                                            ])
            # abnf_socket_004([3, 'snomepai', '0GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG0'  ])
            # abnf_socket_004([3, 'snomemae', '0HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH0'  ])
            # abnf_socket_004([3, 'snomecon', '0IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII0'  ])
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
        elif dabnfopg['abnfobj0'] == ['btrelcad', 'btrelcad']:      # Relação de CPF cadastrados
            abnf000u01c00403_cadastro_cpf(dabnfopg)
            
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u01c00402_cadastro_cpf ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de CPF.                                                                                                                                    // #
# // Gravação dos registros e geração de log.                                                                                                            // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #

def abnf000u01c00402_cadastro_cpf(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u01c00402_cadastro_cpf(dabnfopg)')
    print('----------------------------------------------------------------------------------------------------------------------------------')
    bvalidad, sabnproj, sabntoke = abnf_valida_projeto_token(dabnfopg)
    if bvalidad:
        # Busca registro em dglobdws:
        dglobaux = abnf_websocket_control_globdws(sabnproj, sabntoke, [2, None])
        if dabnfopg['abnfobj0'] == ['btcancel', 'btcancel']:        # Voltar para tela anterior
            abnf000u01c00400_cadastro_cpf(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btsalreg', 'btsalreg']:      # Salvar o registro
            iidcpfpj = dglobaux['iidcpfpj']
            lmfields = [
                ['scodpfpj', 'input',    'M', 'CPF',                                   ['Notnull', 'CPF', 'D'],                    None],
                ['snomraso', 'input',    'M', 'nome',                                  ['Notnull', 'D'],                           None],
                ['iidlogra', 'number',   'M', 'logradouro (rua/bairro/cidade/estado)', ['Notnull', 'D'],                           None],
                ['slogrnum', 'input',    'M', 'logradouro (número)',                   ['Notnull', 'D'],                           None],
                ['slogrcom', 'input',    'M', 'logradouro (complemento)',              [],                                         None],
                ['slogrcep', 'input',    'M', 'logradouro (CEP)',                      [],                                         None],
                ['ssexoxxx', 'select',   'M', 'sexo',                                  [],                                         None],
                ['srgiexxx', 'input',    'M', 'RG',                                    [],                                         None],
                ['scnhxxxx', 'input',    'M', 'CNH',                                   [],                                         None],
                ['stitenum', 'number',   'M', 'título de eleitor (número)',            ['Empty_to_string'],                        None],
                ['stitezon', 'number',   'M', 'título de eleitor (zona)',              ['Empty_to_string'],                        None],
                ['stitesec', 'number',   'M', 'título de eleitor (seção)',             ['Empty_to_string'],                        None],
                ['scertres', 'input',    'M', 'certificado de reservista',             [],                                         None],
                ['ddatanas', 'date',     'F', 'data de nascimento',                    ['Notnull', 'D', 'Return_date', '<=today'], None],
                ['ddatacas', 'date',     'F', 'data de casamento',                     ['Return_date', '<=today'],                 None],
                ['ddatafal', 'date',     'F', 'data de falecimento',                   ['Return_date', '<=today'],                 None],
                ['snomepai', 'input',    'M', 'nome do pai',                           [],                                         None],
                ['snomemae', 'input',    'M', 'nome da mãe',                           [],                                         None],
                ['snomecon', 'input',    'M', 'nome do conjuge',                       [],                                         None],
                ['stelef01', 'input',    'M', 'telefone 01',                           [],                                         None],
                ['stelef02', 'input',    'M', 'telefone 02',                           [],                                         None],
                ['stelef03', 'input',    'M', 'telefone 03',                           [],                                         None],
                ['stelef04', 'input',    'M', 'telefone 04',                           [],                                         None],
                ['stelef05', 'input',    'M', 'telefone 05',                           [],                                         None],
                ['semail01', 'input',    'M', 'e-mail 01',                             ['e-mail'],                                 None],
                ['semail02', 'input',    'M', 'e-mail 02',                             ['e-mail'],                                 None],
                ['semail03', 'input',    'M', 'e-mail 03',                             ['e-mail'],                                 None],
                ['semail04', 'input',    'M', 'e-mail 04',                             ['e-mail'],                                 None],
                ['semail05', 'input',    'M', 'e-mail 05',                             ['e-mail'],                                 None],
                ['shpage01', 'input',    'F', 'home page 01',                          [],                                         None],
                ['shpage02', 'input',    'F', 'home page 02',                          [],                                         None],
                ['shpage03', 'input',    'F', 'home page 03',                          [],                                         None],
                ['shpage04', 'input',    'F', 'home page 04',                          [],                                         None],
                ['shpage05', 'input',    'F', 'home page 05',                          [],                                         None],
                ['sobserva', 'textarea', 'F', 'observação',                            [],                                         None],
            ]
            if iidcpfpj > 0: lmfields = lmfields + [
                ['ssitureg', 'select',   'F', 'situação do registro',                  ['Notnull', 'D'],                None],
            ]
            bvalidad, lmfields = abnf_check_structure_fields(dabnfopg, lmfields, 'btsalreg')
            # Debug: (inicio)
            # abnf_show('10', lmfields, 1)
            # abnf_show('09', dabnfopg, 2)
            # abnf_show('10', dglobaux, 0)
            # Debug: (fim)
            if bvalidad:
                icodbase = int(dabnfopg['abnproje'][2][14:]) * 100          # Código do banco de dados a ser utilizado
                scodpfpj = lmfields[0][5] 
                snomraso = lmfields[1][5] 
                iidlogra = lmfields[2][5] 
                slogrnum = lmfields[3][5] 
                slogrcom = lmfields[4][5] 
                slogrcep = lmfields[5][5] 
                ssexoxxx = lmfields[6][5] 
                srgiexxx = lmfields[7][5] 
                scnhxxxx = lmfields[8][5] 
                stitenum = lmfields[9][5] 
                stitezon = lmfields[10][5]
                stitesec = lmfields[11][5]
                scertres = lmfields[12][5]
                ddatanas = lmfields[13][5]
                ddatacas = lmfields[14][5]
                ddatafal = lmfields[15][5]
                snomepai = lmfields[16][5]
                snomemae = lmfields[17][5]
                snomecon = lmfields[18][5]
                stelef01 = lmfields[19][5]
                stelef02 = lmfields[20][5]
                stelef03 = lmfields[21][5]
                stelef04 = lmfields[22][5]
                stelef05 = lmfields[23][5]
                semail01 = lmfields[24][5]
                semail02 = lmfields[25][5]
                semail03 = lmfields[26][5]
                semail04 = lmfields[27][5]
                semail05 = lmfields[28][5]
                shpage01 = lmfields[29][5]
                shpage02 = lmfields[30][5]
                shpage03 = lmfields[31][5]
                shpage04 = lmfields[32][5]
                shpage05 = lmfields[33][5]
                sobserva = lmfields[34][5]
                if iidcpfpj > 0:
                    ssitureg = lmfields[35][5]
                lmrulesx = [
                    ['e2>=e1', ddatanas, 'F', 'data de mascimento', ddatacas, 'F', 'data de casamento'],
                    ['e2>=e1', ddatanas, 'F', 'data de mascimento', ddatafal, 'F', 'data de falecimento'],
                    ['e2>=e1', ddatacas, 'F', 'data de casamento',  ddatafal, 'F', 'data de falecimento'],
                ]
                bvalidad =  abnf_check_rules_fields(lmrulesx, 'btsalreg')                
                if bvalidad: 
                    
                    if iidcpfpj == 0:   # Novo registro
                        lcamposb = ('codpfpj', 'idcpfpj')
                        lfilbusc = (('codpfpj', '=', lmfields[0][5]), ('situreg', '!=', 'C'))
                        lorderby = None
                        lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_cpfcnpj', lcamposb, lfilbusc, lorderby)
                        if lsqlre01 != [] or iqtdre01 != 0:
                            abnf_alert('Não foi possível salvar! O CPF ' + str(lmfields[0][5]) + ' já está sendo utilizado em outro registro!', 4)
                        else:
                            bvalidad, iproxiid = abnf_database_insere_dados_v02(icodbase, sabnproj, 'abnf_cadastro_cpfcnpj', dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                            [
                                ('codpfpj', scodpfpj),
                                ('nomraso', snomraso),
                                ('idlogra', iidlogra),
                                ('logrnum', slogrnum),
                                ('logrcom', slogrcom),
                                ('logrcep', slogrcep),
                                ('sexoxxx', ssexoxxx),
                                ('rgiexxx', srgiexxx),
                                ('cnhxxxx', scnhxxxx),
                                ('titenum', stitenum),
                                ('titezon', stitezon),
                                ('titesec', stitesec),
                                ('certres', scertres),
                                ('datanas', ddatanas),
                                ('datacas', ddatacas),
                                ('datafal', ddatafal),
                                ('nomepai', snomepai),
                                ('nomemae', snomemae),
                                ('nomecon', snomecon),
                                ('telef01', stelef01),
                                ('telef02', stelef02),
                                ('telef03', stelef03),
                                ('telef04', stelef04),
                                ('telef05', stelef05),
                                ('email01', semail01),
                                ('email02', semail02),
                                ('email03', semail03),
                                ('email04', semail04),
                                ('email05', semail05),
                                ('hpage01', shpage01),
                                ('hpage02', shpage02),
                                ('hpage03', shpage03),
                                ('hpage04', shpage04),
                                ('hpage05', shpage05),
                                ('observa', sobserva),
                                ('tippfpj', 'F'),
                                ('situreg', 'A'),
                            ])
                            if bvalidad:
                                abnf_alert('Novo CPF gravado com sucesso!', 3)
                                abnf000u01c00400_cadastro_cpf(dabnfopg)
                    elif iidcpfpj > 0:  # Registro existente
                        lcamposb = ('codpfpj', 'idcpfpj')
                        lfilbusc = (('codpfpj', '=', lmfields[0][5]), ('situreg', '!=', 'C'), ('idcpfpj', '!=', iidcpfpj))
                        lorderby = None
                        lsqlre01, iqtdre01 = abnf_database_busca_dados_v02(icodbase, 'abnf_cadastro_cpfcnpj', lcamposb, lfilbusc, lorderby)
                        if lsqlre01 != [] or iqtdre01 != 0:
                            abnf_alert('Não foi possível salvar! O CPF ' + str(lmfields[0][5]) + ' já está sendo utilizado em outro registro!', 4)
                        else:
                            # abnf_show('08', lmfields, 1)
                            bvalidad = abnf_database_altera_dados_v02(icodbase, sabnproj, 'abnf_cadastro_cpfcnpj', iidcpfpj, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'],
                            [
                                ('codpfpj', scodpfpj),
                                ('nomraso', snomraso),
                                ('idlogra', iidlogra),
                                ('logrnum', slogrnum),
                                ('logrcom', slogrcom),
                                ('logrcep', slogrcep),
                                ('sexoxxx', ssexoxxx),
                                ('rgiexxx', srgiexxx),
                                ('cnhxxxx', scnhxxxx),
                                ('titenum', stitenum),
                                ('titezon', stitezon),
                                ('titesec', stitesec),
                                ('certres', scertres),
                                ('datanas', ddatanas),
                                ('datacas', ddatacas),
                                ('datafal', ddatafal),
                                ('nomepai', snomepai),
                                ('nomemae', snomemae),
                                ('nomecon', snomecon),
                                ('telef01', stelef01),
                                ('telef02', stelef02),
                                ('telef03', stelef03),
                                ('telef04', stelef04),
                                ('telef05', stelef05),
                                ('email01', semail01),
                                ('email02', semail02),
                                ('email03', semail03),
                                ('email04', semail04),
                                ('email05', semail05),
                                ('hpage01', shpage01),
                                ('hpage02', shpage02),
                                ('hpage03', shpage03),
                                ('hpage04', shpage04),
                                ('hpage05', shpage05),
                                ('observa', sobserva),
                                ('situreg', ssitureg),
                            ])
                            if bvalidad:
                                abnf_alert('Registro alterado com sucesso!', 3)
                                abnf000u01c00400_cadastro_cpf(dabnfopg)
        elif dabnfopg['abnfobj0'] == ['btexcreg', 'btexcreg']:      # Excluir registro
            iidcpfpj = dglobaux['iidcpfpj']        
            icodbase = int(dabnfopg['abnproje'][2][14:]) * 100      # Código do banco de dados a ser utilizado
            bvalidad = abnf_database_exclui_registro(icodbase, sabnproj, 'abnf_cadastro_cpfcnpj', iidcpfpj, dglobaux['iidusuar'], dglobaux['slogiusu'], dglobaux['snomeusu'])
            if bvalidad:
                abnf_alert('Registro excluído com sucesso!', 3)
                abnf000u01c00400_cadastro_cpf(dabnfopg)
                
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // [ abnf000u01c00403_cadastro_cpf ] //////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
# // Cadastro de CPF.                                                                                                                                    // #
# // Relatório de CPF.                                                                                                                                   // #
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #
                
def abnf000u01c00403_cadastro_cpf(dabnfopg):
    print('■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□■□')
    print('==================================================================================================================================')
    print('abnf000u01c00403_cadastro_cpf(dabnfopg)')
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
            abnf_imprime_thead_002_titulo_relatorio(sarquwri, icolspan, 'RELAÇÃO DE CPF')
            abnf_imprime_thead_003_empresa_filial(sarquwri, icolspan, snomeemp, snomefil)
            # smensage = 'Per&iacute;odo: ' + abnf_converte_data(ddataini) + ' &agrave;s ' + abnf_converte_hora(thoraini) + ' at&eacute; ' + abnf_converte_data(ddatafim) + ' &agrave;s ' + abnf_converte_hora(thorafim)
            # abnf_imprime_thead_004_parametros(sarquwri, icolspan, smensage)
            abnf_imprime_thead_005_datetime(sarquwri, icolspan)
            abnf_imprime_line(sarquwri, icolspan, 'darkcyan')
            abnf_imprime_info_001(sarquwri, '#D1C5C5', 'center', 1,
                [
                    ('Nome',        1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('CPF',         1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                    ('Situação',    1, 0, None, None, 'black', 'Courier New', ifontlen, True, False),
                ]
            )
            abnf_imprime_fthead_tbody(sarquwri)
            lcamposb = ('nomraso', 'codpfpj', 'situreg')
            lfilbusc = (('situreg', '!=', 'C'), ('tippfpj', '=', 'F'))
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